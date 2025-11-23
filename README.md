# 🚀 AI-Powered Power Point Presentation Generator
*Built Using Streamlit • n8n Automation • Gemini LLM • python-pptx*

**📌 Project Overview**
This project is a fully automated AI-Powered PowerPoint Generator Web App that converts a simple text prompt into a complete, downloadable .pptx presentation.

**The system combines:**

- Streamlit for a clean, interactive frontend
- n8n for workflow orchestration
- Gemini AI for generating python-pptx code
- python-pptx for building the final PowerPoint file
- Users simply enter the topic, slide structure, and content idea, and the app instantly generates a formatted, ready-to-use presentation.

**✨ Key Features**

**🎨 1. User-Friendly Streamlit UI**
- Modern prompt-based interface
- Fields for topic, slide outline, and custom instructions
- Instant file download button

**🤖 2. AI-Powered Content & Code Generation**
- Gemini LLM acts as the AI engine
- Generates python-pptx code dynamically based on user input
- Supports multi-slide content with headings, bullet points, and structured formatting

**🔁 3. Automated Backend Workflow (n8n)**
- Webhook node collects user input from Streamlit
- AI Agent node generates code
- Custom execution node runs python-pptx code
- Output is returned as a .pptx file

**📥 4. One-Click PPT Download**
- File streamed back to Streamlit
- Clean, usable presentation with proper formatting

**🛠️ Tech Stack**
**Frontend**
- Streamlit
- Python (Requests / HTTPX)

 **Backend**
- n8n Workflow Automation
- Webhook + AI Agent + Code Execution Nodes

**AI & File Generation**
- Google Gemini API
- python-pptx library

**🚀 How It Works**
*User inputs:*

**Topic**
- Slide structure
- Any custom instructions
- Streamlit sends data → n8n Webhook
- Gemini generates python-pptx code
- n8n executes the generated code
- A.pptx file is created
- Streamlit displays a download button
  
**📸Screenshot**
<img width="1127" height="551" alt="Screenshot 2025-11-23 235823" src="https://github.com/user-attachments/assets/e60a69d2-6183-4f76-b283-bba4b79d76af" />


