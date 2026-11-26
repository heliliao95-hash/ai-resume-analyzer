import os

import fitz
from openai import OpenAI


def extract_resume_text(pdf_bytes):
	pages = []

	with fitz.open(stream=pdf_bytes, filetype="pdf") as pdf:
		for page in pdf:
			text = page.get_text("text").strip()
			if text:
				pages.append(text)

	return "\n\n".join(pages)


def analyze_resume(resume_text, job_description):
	api_key = os.getenv("DASHSCOPE_API_KEY")
	base_url = os.getenv(
		"DASHSCOPE_BASE_URL",
		"https://dashscope.aliyuncs.com/compatible-mode/v1",
	)
	model = os.getenv("DASHSCOPE_MODEL", "qwen-plus")

	if not api_key:
		raise ValueError("未检测到 API Key，请检查 .env 文件。")

	if not resume_text.strip():
		raise ValueError("没有从 PDF 简历中提取到文字，请检查文件是否为扫描版 PDF。")

	if not job_description.strip():
		raise ValueError("请先填写招聘岗位描述。")

	client = OpenAI(
		api_key=api_key,
		base_url=base_url,
		timeout=60,
		max_retries=0,
	)

	response = client.chat.completions.create(
		model=model,
		messages=[
			{
				"role": "system",
				"content": (
					"你是一名专业的职业规划顾问和招聘专家。"
					"请根据用户提供的简历和岗位描述进行客观分析。"
					"不得编造简历中不存在的经历、技能或数据。"
					"请使用中文回答，并使用清晰的 Markdown 标题和列表。"
					"请包含岗位匹配度评分、匹配优势、技能差距、"
					"简历问题和具体优化建议。"
					"评分应基于简历与岗位要求的匹配情况，"
					"并说明评分依据。"
				),
			},
			{
				"role": "user",
				"content": (
					f"简历内容：\n{resume_text[:18000]}\n\n"
					f"招聘岗位描述：\n{job_description[:10000]}\n\n"
					"请分析这份简历与目标岗位的匹配情况。"
				),
			},
		],
		max_tokens=1800,
	)

	return response.choices[0].message.content or "暂时没有生成分析结果。"
