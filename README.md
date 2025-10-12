# HaiZi's "Dawn" - Multilingual Poetry Collection

**Language / 语言**: [English](README.md) | [中文](README_zh.md)

A web application for reading HaiZi's (海子) poetry with translations in 13 languages. Includes interactive vocabulary annotations for Chinese characters.

## Features

- View poems in 13 languages alongside the original Chinese
- Click on Chinese characters to see pinyin and definitions
- Navigate between different poem sections
- Compare original Chinese with translations
- Responsive web interface

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

### Setup

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
haizi_liming/
├── app.py                    # Main Streamlit application
├── requirements.txt          # Python dependencies
├── README.md                # This file
├── haizi_liming_zh.txt      # Original Chinese poems by HaiZi
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

1. Select a translation language from the sidebar
2. Choose a poem section from the dropdown
3. Click on Chinese characters to see vocabulary information
4. View original Chinese and translation side-by-side

## Technical Details

- Built with Streamlit
- Uses pandas for data processing
- HTML/CSS for vocabulary tooltips
- Data caching for performance

## About HaiZi (海子)

HaiZi (1964-1989), born Zha Haisheng, was one of the most influential Chinese poets of the late 20th century. Known for his deeply spiritual and often melancholic verse, HaiZi's poetry explores themes of nature, death, rebirth, and the eternal struggle between hope and despair.

His themes of Dawn (黎明) is an important theme across his poems. In the book that I have, I found 6 poems that were named with the word 黎明. These poems weave together imagery of water, autumn, and the liminal space between night and day to create a haunting meditation on mortality and transcendence. HaiZi's tragic death at the age of 25 only added to the mystique surrounding his work, making him a legendary figure in modern Chinese literature.

This collection presents HaiZi's poems in their original Chinese with translations in 13 languages and vocabulary annotations.

This was made for 孟老师的 class, 北京大学汉语学13班. 

---

*Created for educational and literary appreciation purposes.*
