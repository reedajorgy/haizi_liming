import streamlit as st
import pandas as pd
import os
from pathlib import Path
import re

# Configure page
st.set_page_config(
    page_title="海子的黎明",
    page_icon="🌙",
    layout="wide"
)

@st.cache_data
def load_poetry_data():
    """Load all poem texts and vocabulary data from language directories."""
    base_path = Path(__file__).parent / "translations"
    
    # Language mapping with local names and country flags
    language_names = {
        'english': 'English',
        'spanish': 'Español', 
        'french': 'Français',
        'german': 'Deutsch',
        'arabic': 'العربية',
        'greek': 'Ελληνικά',
        'hindi': 'हिन्दी',
        'japanese': '日本語',
        'korean': '한국어',
        'portuguese': 'Português',
        'russian': 'Русский',
        'thai': 'ไทย',
        'vietnamese': 'Tiếng Việt'
    }
    
    # File prefix mapping for languages with non-standard prefixes
    file_prefixes = {
        'english': 'en',
        'spanish': 'sp', 
        'french': 'fr',
        'german': 'de',
        'arabic': 'ar',
        'greek': 'gr',
        'hindi': 'hi',
        'japanese': 'ja',
        'korean': 'ko',
        'portuguese': 'pt',
        'russian': 'ru',
        'thai': 'th',
        'vietnamese': 'vi'
    }
    
    data = {}
    
    # Load Chinese original
    chinese_path = Path(__file__).parent / "haizi_liming_zh.txt"
    with open(chinese_path, 'r', encoding='utf-8') as f:
        chinese_text = f.read()
    
    # Split Chinese text into individual poems
    chinese_poems = split_into_poems(chinese_text)
    
    data['chinese'] = {
        'name': '中文',
        'poems': chinese_poems,
        'vocab_by_poem': []
    }
    
    # Load each language
    for lang_code, lang_name in language_names.items():
        lang_path = base_path / lang_code
        
        if lang_path.exists():
            # Load poem text using correct file prefix
            prefix = file_prefixes.get(lang_code, lang_code[:2])
            poem_file = lang_path / f"{prefix}_poem.txt"
            vocab_file = lang_path / f"{prefix}_vocab.csv"
            
            if poem_file.exists():
                with open(poem_file, 'r', encoding='utf-8') as f:
                    poem_text = f.read()
                
                # Split into individual poems
                poems = split_into_poems(poem_text)
                
                # Load vocabulary organized by poem
                vocab_by_poem = []
                if vocab_file.exists():
                    try:
                        vocab_df = pd.read_csv(vocab_file)
                        current_poem_vocab = []
                        
                        for _, row in vocab_df.iterrows():
                            # Check if this is a separator line
                            if pd.notna(row['hanzi']) and row['hanzi'].strip() == '***':
                                # Save current poem's vocabulary and start new poem
                                if current_poem_vocab:
                                    vocab_by_poem.append(current_poem_vocab)
                                current_poem_vocab = []
                            elif pd.notna(row['hanzi']) and pd.notna(row['definition']):
                                # Add vocabulary word to current poem
                                current_poem_vocab.append({
                                    'hanzi': row['hanzi'],
                                    'pinyin': row.get('pinyin', ''),
                                    'definition': row['definition'],
                                    'description': row.get('short description of its use in the poem', '')
                                })
                        
                        # Add the last poem's vocabulary
                        if current_poem_vocab:
                            vocab_by_poem.append(current_poem_vocab)
                            
                    except Exception as e:
                        st.error(f"Error loading vocabulary for {lang_name}: {e}")
                        vocab_by_poem = []
                
                data[lang_code] = {
                    'name': lang_name,
                    'poems': poems,
                    'vocab_by_poem': vocab_by_poem
                }
    
    return data

def split_into_poems(text):
    """Split poem text into individual poems."""
    poems = []
    
    # Split by *** separators (works for both Chinese and translations)
    sections = text.split('***')
    
    for section in sections:
        section = section.strip()
        if not section:
            continue
            
        lines = section.split('\n')
        if not lines:
            continue
            
        # Extract title from first line (should be //title// format)
        title_line = lines[0].strip()
        title = title_line
        
        # Clean up title if it has // markers
        if title.startswith('///') and title.endswith('///'):
            title = title[3:-3].strip()
        elif title.startswith('//') and title.endswith('//'):
            title = title[2:-2].strip()
        
        # Get the rest of the content (skip the title line)
        content_lines = lines[1:] if len(lines) > 1 else []
        
        # Join content while preserving original line breaks and spacing
        content = '\n'.join(content_lines)
        
        poems.append({
            'title': title,
            'content': content
        })
    
    return poems

def make_vocab_clickable(text, vocab_dict):
    """Convert vocabulary words in text to clickable elements."""
    if not vocab_dict:
        return text
    
    # Create clickable spans for each vocabulary word
    for hanzi, info in vocab_dict.items():
        if hanzi in text:
            # Escape HTML characters in tooltip content
            escaped_pinyin = info['pinyin'].replace('"', '&quot;').replace("'", '&#39;')
            escaped_def = info['definition'].replace('"', '&quot;').replace("'", '&#39;')
            escaped_desc = info['description'].replace('"', '&quot;').replace("'", '&#39;')
            
            # Create tooltip content
            tooltip_content = f"{hanzi}<br/><em>{escaped_pinyin}</em><br/>{escaped_def}<br/><small>{escaped_desc}</small>"
            
            # Replace hanzi with clickable span
            clickable_span = f"""
            <span style="color: #1f77b4; cursor: pointer; border-bottom: 1px dotted #1f77b4; background-color: rgba(31, 119, 180, 0.1); padding: 1px 2px; border-radius: 2px;" 
                  title="{tooltip_content}">
                {hanzi}
            </span>
            """
            text = text.replace(hanzi, clickable_span)
    
    return text

def main():
    st.title("🌙 海子的黎明")
    st.markdown("*黎明 (Dawn) - A Multilingual Journey*")
    
    # Load data
    data = load_poetry_data()
    
    if not data:
        st.error("No poetry data found. Please check the file structure.")
        return
    
    # Create sidebar controls
    st.sidebar.header("Navigation")
    
    # Language selection
    available_langs = list(data.keys())
    lang_options = [data[lang]['name'] for lang in available_langs]
    
    # Default to English if available, otherwise first language
    default_idx = 0
    if 'english' in available_langs:
        default_idx = available_langs.index('english')
    
    selected_lang_idx = st.sidebar.selectbox(
        "Select Translation Language",
        range(len(lang_options)),
        index=default_idx,
        format_func=lambda x: lang_options[x]
    )
    selected_lang = available_langs[selected_lang_idx]
    
    # Poem selection - each poem is its own page
    chinese_poems = data['chinese']['poems']
    poem_titles = [poem['title'] for poem in chinese_poems]
    
    selected_poem_idx = st.sidebar.selectbox(
        "Select Poem",
        range(len(chinese_poems)),
        format_func=lambda x: poem_titles[x]
    )
    
    # Display poems side by side
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("中文")
        chinese_poem = chinese_poems[selected_poem_idx]
        
        # Make vocabulary clickable (for now, skip since Chinese doesn't have vocab)
        clickable_text = chinese_poem['content']
        
        # Display with preserved formatting
        st.markdown(f"**{chinese_poem['title']}**")
        # Format content to preserve line breaks and spacing with custom styling
        formatted_content = f'<div style="white-space: pre-line; line-height: 1.8; font-size: 16px;">{chinese_poem["content"]}</div>'
        st.markdown(formatted_content, unsafe_allow_html=True)
    
    with col2:
        st.subheader(f"{data[selected_lang]['name']}")
        if selected_lang in data and len(data[selected_lang]['poems']) > selected_poem_idx:
            translation_poem = data[selected_lang]['poems'][selected_poem_idx]
            st.markdown(f"**{translation_poem['title']}**")
            # Format content to preserve line breaks and spacing with custom styling
            formatted_content = f'<div style="white-space: pre-line; line-height: 1.8; font-size: 16px;">{translation_poem["content"]}</div>'
            st.markdown(formatted_content, unsafe_allow_html=True)
        else:
            st.warning("Translation not available for this poem.")
    
    # Add vocabulary section
    if selected_lang in data and data[selected_lang]['vocab_by_poem']:
        if selected_poem_idx < len(data[selected_lang]['vocab_by_poem']):
            current_poem_vocab = data[selected_lang]['vocab_by_poem'][selected_poem_idx]
            if current_poem_vocab:
                with st.expander("📚 View Vocabulary List", expanded=False):
                    st.markdown("### Vocabulary for this poem")
                    
                    # Create vocabulary cards
                    for vocab_item in current_poem_vocab:
                        with st.container():
                            st.markdown(f"""
                            <div style="
                                border: 1px solid #e0e0e0; 
                                border-radius: 8px; 
                                padding: 15px; 
                                margin: 10px 0; 
                                background-color: #fafafa;
                                box-shadow: 0 2px 4px rgba(0,0,0,0.1);
                            ">
                                <div style="display: flex; align-items: center; margin-bottom: 8px;">
                                    <h4 style="margin: 0; color: #1f77b4; font-size: 24px;">{vocab_item['hanzi']}</h4>
                                    <span style="margin-left: 10px; font-style: italic; color: #666; font-size: 16px;">{vocab_item['pinyin']}</span>
                                </div>
                                <div style="margin-bottom: 5px;">
                                    <strong style="color: #333; font-size: 16px;">{vocab_item['definition']}</strong>
                                </div>
                                <div style="color: #666; font-size: 14px; line-height: 1.4;">
                                    {vocab_item['description']}
                                </div>
                            </div>
                            """, unsafe_allow_html=True)
    
    
    # Footer
    st.markdown("---")
    st.markdown("""
    <div style="text-align: center; color: #666; font-size: 12px;">
        Haizi (海子) - Dawn Poems Collection<br/>
        Interactive multilingual poetry viewer
    </div>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()