import os
import streamlit as st
from dotenv import load_dotenv
from ai_utils import extract_resume_text, analyze_resume

load_dotenv()

st.set_page_config(
	page_title="AI 简历与岗位匹配助手",
	page_icon="📄",
	layout="wide"
)

st.title("📄 AI 简历与岗位匹配助手")
st.caption("上传简历，粘贴招聘要求，AI 帮你分析岗位匹配度并提供优化建议。")

if "resume_text" not in st.session_state:
	st.session_state.resume_text = ""

if "resume_name" not in st.session_state:
	st.session_state.resume_name = ""

if "analysis" not in st.session_state:
	st.session_state.analysis = ""

with st.sidebar:
	st.header("📁 简历上传")

	uploaded_file = st.file_uploader(
		"上传 PDF 简历",
		type=["pdf"]
	)

	if st.button("提取简历内容", type="primary", use_container_width=True):
		if uploaded_file is None:
			st.warning("请先上传 PDF 简历。")
		else:
			try:
				with st.spinner("正在提取简历内容……"):
					resume_text = extract_resume_text(uploaded_file.getvalue())

				if resume_text:
					st.session_state.resume_text = resume_text
					st.session_state.resume_name = uploaded_file.name
					st.session_state.analysis = ""
					st.success("简历提取成功！")
				else:
					st.error("没有提取到文字，请检查 PDF 是否为扫描版。")

			except Exception as error:
				st.error(f"简历处理失败：{error}")

	if st.session_state.resume_name:
		st.success(f"当前简历：{st.session_state.resume_name}")
		st.caption(f"提取字符数：{len(st.session_state.resume_text)}")

	if st.button("清空简历和分析", use_container_width=True):
		st.session_state.resume_text = ""
		st.session_state.resume_name = ""
		st.session_state.analysis = ""
		st.rerun()

st.subheader("💼 目标岗位")

job_description = st.text_area(
	"粘贴招聘岗位 JD",
	height=260,
	placeholder="请粘贴招聘平台上的岗位职责、任职要求和技能要求……"
)

st.subheader("🤖 AI 简历分析")

if st.button("开始分析匹配度", type="primary", use_container_width=True):
	if not st.session_state.resume_text:
		st.warning("请先上传简历并提取内容。")
	elif not job_description.strip():
		st.warning("请先填写目标岗位描述。")
	else:
		try:
			with st.spinner("AI 正在分析简历与岗位要求，请稍候……"):
				result = analyze_resume(
					st.session_state.resume_text,
					job_description
				)

			st.session_state.analysis = result

		except Exception as error:
			st.error(f"分析失败：{error}")

if st.session_state.analysis:
	st.divider()
	st.subheader("📊 分析结果")
	st.markdown(st.session_state.analysis)

	st.download_button(
		"下载分析报告",
		data=st.session_state.analysis,
		file_name="resume_analysis.md",
		mime="text/markdown",
		use_container_width=True
	)

st.divider()

st.caption("AI 分析结果仅供求职参考，请结合实际经历核对并修改简历。")
