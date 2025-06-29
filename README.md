# Cold Email Generator Tool

An intelligent AI-powered tool that automatically generates personalized cold emails for job applications by analyzing job postings and matching them with relevant portfolio projects.

## 🚀 Features

- **Smart Job Analysis**: Automatically extracts job details (role, experience, skills, description) from career pages
- **Portfolio Matching**: Uses vector similarity search to find relevant portfolio projects based on required skills
- **AI-Powered Email Generation**: Creates personalized cold emails using Llama 3.3-70B model via Groq API
- **Web Interface**: User-friendly Streamlit web application
- **Text Cleaning**: Automatically cleans and processes scraped web content

## 🛠️ Technology Stack

- **Frontend**: Streamlit
- **AI/LLM**: Llama 3.3-70B (via Groq API)
- **Vector Database**: ChromaDB for portfolio similarity search
- **Web Scraping**: LangChain WebBaseLoader
- **Data Processing**: Pandas, Regular Expressions
- **Language**: Python

## 📋 Prerequisites

- Python 3.8+
- Groq API key
- Internet connection for web scraping

## 🚀 Installation

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd Cold_Email_Generator_Tool_GenAI_Llama3.1
   ```

2. **Install dependencies**
   ```bash
   pip install streamlit langchain-groq langchain-community chromadb pandas python-dotenv
   ```

3. **Set up environment variables**
   Create a `.env` file in the root directory:
   ```bash
   GROQ_API_KEY=your_groq_api_key_here
   ```

4. **Update portfolio data**
   - Edit `app/resources/my_portfolio.csv` with your actual portfolio projects
   - Format: `Techstack,Links` (comma-separated)

## 🎯 Usage

1. **Start the application**
   ```bash
   cd app
   streamlit run main.py
   ```

2. **Access the web interface**
   - Open your browser and go to `http://localhost:8501`
   - You'll see the "Cold Mail Generator" interface

3. **Generate a cold email**
   - Enter a job posting URL in the text field
   - Click "Submit"
   - The tool will:
     - Scrape and analyze the job posting
     - Extract job requirements and skills
     - Find relevant portfolio projects
     - Generate a personalized cold email

## 📁 Project Structure

```
Cold_Email_Generator_Tool_GenAI_Llama3.1/
├── app/
│   ├── main.py              # Streamlit application entry point
│   ├── chains.py            # LLM chains for job extraction and email generation
│   ├── portfolio.py         # Portfolio management and vector search
│   ├── utils.py             # Text cleaning utilities
│   └── resources/
│       └── my_portfolio.csv # Portfolio projects database
├── vectorstore/             # ChromaDB vector database files
├── my_portfolio.csv         # Root portfolio file
└── README.md               # This file
```

## 🔧 Configuration

### Portfolio Setup
The tool uses a CSV file to store your portfolio projects. Each row should contain:
- **Techstack**: Comma-separated list of technologies/skills
- **Links**: URL to the project or portfolio piece

Example:
```csv
Techstack,Links
"Python, Pandas, Machine Learning","https://github.com/username/ml-project"
"React, Node.js, MongoDB","https://github.com/username/web-app"
```

### API Configuration
- **Groq API**: Required for LLM functionality
- Get your API key from [Groq Console](https://console.groq.com/)
- Add it to your `.env` file

## 🎨 How It Works

1. **Job Analysis**: The tool scrapes the provided job URL and extracts key information using LLM
2. **Skill Matching**: Uses ChromaDB to find portfolio projects that match the job requirements
3. **Email Generation**: Creates a personalized cold email incorporating relevant portfolio links
4. **Output**: Displays the generated email in markdown format

## 📝 Example Output

The tool generates professional cold emails that include:
- Personalized introduction
- Relevant skills and experience
- Portfolio project links
- Professional closing

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🙏 Acknowledgments

- Built with [Streamlit](https://streamlit.io/)
- Powered by [Llama 3.3-70B](https://llama.meta.com/) via [Groq](https://groq.com/)
- Vector search powered by [ChromaDB](https://www.trychroma.com/)
- Web scraping with [LangChain](https://www.langchain.com/)

## 📞 Support

If you encounter any issues or have questions, please:
1. Check the existing issues
2. Create a new issue with detailed information
3. Include error messages and steps to reproduce

---

**Note**: This tool is designed for educational and professional use. Always review generated emails before sending them to ensure they accurately represent your skills and experience. 