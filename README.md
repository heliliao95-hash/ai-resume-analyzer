```markdown
# AI 简历智能分析助手

一个基于 Python、Streamlit 和通义千问 API 开发的 AI 简历分析工具。上传 PDF 简历并输入目标岗位要求，即可提取简历内容，生成岗位匹配度分析与优化建议。

## 项目功能

- **PDF 简历解析**：上传 PDF 文件并自动提取简历文本。
- **岗位要求输入**：填写目标岗位的技能要求和任职条件。
- **AI 简历分析**：调用通义千问 API 分析简历与岗位要求。
- **匹配度评估**：从技能、项目经验和岗位契合度等方面进行分析。
- **优化建议**：识别简历不足，并提供有针对性的修改方向。

## 技术栈

- Python
- Streamlit
- PyMuPDF
- OpenAI Python SDK
- 通义千问 API

## 项目结构

```text
ai-resume-matcher/
├── app.py
├── requirements.txt
├── README.md
├── .env.example
└── .gitignore
```

## 本地运行

### 1. 克隆项目

```bash
git clone https://github.com/你的GitHub用户名/ai-resume-matcher.git
cd ai-resume-matcher
```

### 2. 创建虚拟环境并安装依赖

建议使用 Python 3.10 或更高版本。

```powershell
python -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
```

### 3. 配置 API

在项目根目录创建 `.env` 文件并填写自己的 API 配置：

```env
DASHSCOPE_API_KEY=你的API_KEY
DASHSCOPE_BASE_URL=https://dashscope.aliyuncs.com/compatible-mode/v1
DASHSCOPE_MODEL=qwen-plus
```

请勿将真实 API Key 提交或上传到 GitHub。

### 4. 启动项目

```powershell
.\.venv\Scripts\python.exe -m streamlit run app.py
```

启动后，在浏览器打开 <http://localhost:8501>。

## 使用流程

1. 上传 PDF 格式的个人简历。
2. 等待系统提取简历内容。
3. 输入目标岗位的招聘要求。
4. 点击开始分析。
5. 查看 AI 分析结果和简历优化建议。

## 项目展示

可将项目运行截图放在 `screenshots/` 文件夹中，展示实际运行效果。

## 后续优化方向

- 支持更多简历文件格式。
- 增加不同岗位的简历匹配分析。
- 优化简历关键词提取。
- 增加简历修改前后的对比功能。
- 支持生成优化后的简历文件。

## License

MIT License
```
