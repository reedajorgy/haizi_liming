# 海子的《黎明》- 多语言诗歌集

**语言 / Language**: [中文](README_zh.md) | [English](README.md)

一个用于阅读海子诗歌的网络应用程序，提供13种语言翻译。包含中文字符的交互式词汇注释。

## 功能特色

- 在原文中文旁边查看13种不同语言的诗歌
- 点击中文字符查看拼音和定义
- 在不同诗歌段落间跳转
- 将原文中文与翻译版本并排比较
- 响应式网页界面

## 支持的语言

- 中文（原文）
- 英语
- 西班牙语
- 法语
- 德语
- 阿拉伯语
- 希腊语
- 印地语
- 日语
- 韩语
- 葡萄牙语
- 俄语
- 泰语
- 越南语

## 本地开发

### 设置

1. **创建虚拟环境**
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # Windows: venv\Scripts\activate.bat
   ```

2. **安装依赖**
   ```bash
   pip install -r requirements.txt
   ```

3. **运行应用程序**
   ```bash
   streamlit run app.py
   ```

4. **在浏览器中打开**
   应用程序将自动在 `http://localhost:8501` 打开

## 在 Streamlit Cloud 上部署

1. **推送到 GitHub**
   - 将您的项目上传到 GitHub 仓库
   - 确保包含所有文件（app.py、requirements.txt、translations/、haizi_liming_zh.txt）

2. **在 Streamlit Cloud 上部署**
   - 访问 [share.streamlit.io](https://share.streamlit.io)
   - 连接您的 GitHub 账户
   - 选择您的仓库
   - 将主文件路径设置为 `app.py`
   - 点击"部署"

3. **配置**
   - 应用程序将自动检测文件结构
   - 无需额外配置

## 文件结构

```
haizi_liming/
├── app.py                    # 主 Streamlit 应用程序
├── requirements.txt          # Python 依赖
├── README.md                # 此文件
├── haizi_liming_zh.txt      # 海子原创中文诗歌
└── translations/            # 翻译文件
    ├── english/
    │   ├── en_poem.txt
    │   └── en_vocab.csv
    ├── spanish/
    │   ├── sp_poem.txt
    │   └── sp_vocab.csv
    └── ... (其他语言)
```

## 使用方法

1. 从侧边栏选择翻译语言
2. 从下拉菜单中选择诗歌段落
3. 点击中文字符查看词汇信息
4. 并排查看原文中文和翻译

## 技术细节

- 使用 Streamlit 构建
- 使用 pandas 进行数据处理
- HTML/CSS 词汇提示
- 数据缓存提高性能

## 关于海子（海子）

海子（1964-1989），原名查海生，是20世纪末最具影响力的中国诗人之一。以其深刻的精神性和经常忧郁的诗句而闻名，海子的诗歌探索自然、死亡、重生以及希望与绝望之间永恒斗争的主题。

黎明（黎明）是海子诗歌中的重要主题。在我拥有的书中，我发现了6首以"黎明"命名的诗歌。这些诗歌将水、秋天以及昼夜之间的临界空间的意象编织在一起，创造了对死亡和超越的令人难忘的冥想。海子在25岁时的悲剧性死亡只是增加了围绕他作品的神秘感，使他成为现代中国文学中的传奇人物。

这个合集以原文中文呈现海子的诗歌，配有13种语言翻译和词汇注释。

这是为孟老师的课，北京大学汉语学13班制作的。

---

*为教育和文学欣赏目的而创建。*
