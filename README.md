# Multilingual Poetry Viewer

An interactive web application for exploring Haizi's poetry collection in multiple languages with clickable vocabulary annotations.

## Features

- **Multilingual Support**: View poems in 13 different languages alongside the original Chinese
- **Interactive Vocabulary**: Click on Chinese characters to see pinyin, definitions, and usage descriptions
- **Poem Navigation**: Jump between different poem sections easily
- **Side-by-Side Display**: Compare original Chinese with any translation
- **Responsive Design**: Clean, modern interface optimized for reading

## Languages Supported

- Chinese (Original)
- English
- Spanish
- French
- German
- Arabic
- Greek
- Hindi
- Japanese
- Korean
- Portuguese
- Russian
- Thai
- Vietnamese

## Local Development

### Quick Start (Recommended)

**For macOS/Linux:**
```bash
./start.sh run
```

**For Windows:**
```cmd
start.bat run
```

This will automatically:
- Create a virtual environment
- Install all dependencies
- Start the application

### Manual Setup

1. **Create Virtual Environment**
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate.bat
   ```

2. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the Application**
   ```bash
   streamlit run app.py
   ```

4. **Open in Browser**
   The app will automatically open at `http://localhost:8501`

## Deployment on Streamlit Cloud

1. **Push to GitHub**
   - Upload your project to a GitHub repository
   - Ensure all files are included (app.py, requirements.txt, translations/, haizi_liming_zh.txt)

2. **Deploy on Streamlit Cloud**
   - Go to [share.streamlit.io](https://share.streamlit.io)
   - Connect your GitHub account
   - Select your repository
   - Set the main file path to `app.py`
   - Click "Deploy"

3. **Configuration**
   - The app will automatically detect the file structure
   - No additional configuration needed

## File Structure

```
kouyu_baogao_one/
├── app.py                    # Main Streamlit application
├── requirements.txt          # Python dependencies
├── README.md                # This file
├── haizi_liming_zh.txt      # Original Chinese poems
└── translations/            # Translation files
    ├── english/
    │   ├── en_poem.txt
    │   └── en_vocab.csv
    ├── spanish/
    │   ├── sp_poem.txt
    │   └── sp_vocab.csv
    └── ... (other languages)
```

## Usage

1. **Select Language**: Use the sidebar to choose your preferred translation language
2. **Navigate Poems**: Select different poem sections from the dropdown
3. **Interactive Vocabulary**: Click on highlighted Chinese characters to see detailed information
4. **Compare**: View original Chinese and translation side-by-side

## Technical Details

- Built with Streamlit for rapid web app development
- Uses pandas for CSV data processing
- Implements HTML/CSS for interactive vocabulary tooltips
- Caches data loading for optimal performance
- Responsive design with sidebar navigation

## About Haizi

Haizi (海子, 1964-1989) was a Chinese poet known for his lyrical and mystical poetry. This collection features his "Dawn" poems, exploring themes of hope, despair, and the human condition.

---

*Created for educational and literary appreciation purposes.*
