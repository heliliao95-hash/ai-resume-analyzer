# AI 简历智能分析助手

一个基于 Python、Streamlit 和大语言模型开发的 AI 简历分析工具。用户上传 PDF 简历并输入目标岗位要求，系统自动提取简历内容，分析候选人与岗位的匹配程度，并生成针对性的优化建议。

## 项目演示

用户上传 PDF 简历，填写目标岗位要求，点击「开始分析匹配度」，即可获得 AI 分析结果。

## 核心功能

- **PDF 简历上传**：支持上传 PDF 格式的个人简历。
- **简历内容提取**：自动读取并提取简历文本。
- **岗位要求输入**：支持自定义目标岗位及技能要求。
- **AI 智能分析**：从专业技能、项目经验、岗位匹配度等维度分析简历。
- **匹配度评估**：生成岗位匹配评分及分析结果。
- **简历优化建议**：指出简历存在的问题，并提供可执行的修改建议。
- **行动计划**：生成阶段性求职提升建议。

## 技术栈

| 技术 | 用途 |
|---|---|
| Python | 核心开发语言 |
| Streamlit | Web 应用界面 |
| PDF 文本提取工具 | 提取简历内容 |
| 大语言模型 API | AI 简历分析 |
| python-dotenv | 环境变量管理 |

## 项目结构

```text
ai-resume-analyzer/
├── app.py             # Streamlit 主程序
├── ai_utils.py        # AI 分析相关功能
├── requirements.txt   # 项目依赖
├── .env.example       # API 配置示例
├── .gitignore         # Git 忽略配置
└── README.md          # 项目说明
```

## 本地运行

### 1. 克隆项目

```bash
git clone https://github.com/heliliao95-hash/ai-resume-analyzer.git
cd ai-resume-analyzer
```

### 2. 创建虚拟环境

```bash
python -m venv .venv
```

Windows PowerShell：

```powershell
.\.venv\Scripts\Activate.ps1
```

### 3. 安装依赖

```bash
pip install -r requirements.txt
```

### 4. 配置 API Key

在项目根目录创建 `.env` 文件，参考 `.env.example` 填