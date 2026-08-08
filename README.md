# ✈️ Agentic AI Travel Planner

An AI-powered travel planning application that creates personalized,
budget-aware, and multilingual travel plans based on user requirements.

## 🚀 Features

- 📍 Starting location and destination planning
- 📅 Day-by-day travel itinerary
- 👥 Multiple traveler support
- 💰 Budget-aware trip planning
- 🚗 Transportation recommendations
- 🏨 Accommodation recommendations
- 🍴 Food recommendations
- 🎯 Personalized travel preferences
- 🌐 Multilingual travel plans
- 🇬🇧 English
- 🇮🇳 Telugu
- 🇮🇳 Hindi
- 🤖 AI-powered travel planning using Groq LLM
- ⚡ FastAPI backend
- 🎨 Streamlit frontend

## 🛠️ Technologies Used

- Python
- FastAPI
- Streamlit
- LangChain
- Groq
- Llama 3.1
- Requests
- python-dotenv

## 📁 Project Structure

```text
agentic-travel-planner/
│
├── be/
│   └── main.py
│
├── fe/
│   └── app.py
│
├── .gitignore
├── requirements.txt
└── README.md

## 🔄 How It Works

1. User enters the starting location.
2. User enters the destination.
3. User specifies the number of trip days.
4. User enters the number of travelers.
5. User provides the total budget.
6. User enters travel preferences.
7. User selects a preferred language.
8. Streamlit sends the trip details to FastAPI.
9. FastAPI creates the AI travel planning prompt.
10. Groq LLM generates the travel plan.
11. The generated plan is returned to Streamlit.
12. The travel plan is displayed to the user.

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/chinthalabhanup-arch/agentic-travel-planner.git

cd agentic-travel-planner

python -m venv venv

venv\Scripts\activate

pip install -r requirements.txt


### ⚠️ Important

In your `README.md`, make sure you have the closing three backticks after the clone command:

```text


Then start:

```markdown

### 2. Open the project folder

```bash
cd agentic-travel-planner
```

### 3. Create a virtual environment

```bash
python -m venv venv
```

### 4. Activate the virtual environment

For Windows:

```bash
venv\Scripts\activate
```

### 5. Install the required packages

```bash
pip install -r requirements.txt
```

## 🔐 Environment Variables

Create a `.env` file in the project root directory:

```text
GROQ_API_KEY=your_groq_api_key
```

Replace `your_groq_api_key` with your actual Groq API key.

**Important:** Never upload the `.env` file to GitHub.

## ▶️ Run the Backend

Open a terminal in the project root directory.

Make sure your virtual environment is activated.

Run:

```bash
uvicorn be.main:f_obj --reload
```

The FastAPI backend will run at:

```text
http://127.0.0.1:8000
```

## 🎨 Run the Frontend

Open another terminal in the project root directory.

Make sure your virtual environment is activated.

Run:

```bash
streamlit run fe/app.py
```

The Streamlit application will open in your browser.

## 🔄 How It Works

1. User enters the starting location.
2. User enters the destination.
3. User specifies the number of trip days.
4. User enters the number of travelers.
5. User provides the total budget.
6. User enters travel preferences.
7. User selects a preferred language.
8. Streamlit sends the trip details to FastAPI.
9. FastAPI creates the AI travel planning prompt.
10. The prompt is sent to the Groq LLM.
11. Groq generates the personalized travel plan.
12. FastAPI returns the generated plan to Streamlit.
13. Streamlit displays the travel plan to the user.

## 📋 User Inputs

The application accepts the following travel details:

- Starting location
- Destination location
- Number of trip days
- Number of people
- Total budget
- Travel specifications
- Preferred language

## 🌐 Supported Languages

The travel plan can be generated in:

- 🇬🇧 English
- 🇮🇳 Telugu
- 🇮🇳 Hindi

## ✨ Generated Travel Plan

The AI-generated travel plan includes:

- Trip overview
- Transportation plan
- Accommodation recommendations
- Day-by-day itinerary
- Food plan
- Budget breakdown
- Budget optimization
- Travel tips
- Final recommendation

## 💰 Budget Planning

The application considers the user's total budget and number of travelers.

The AI estimates costs for:

- Transportation
- Accommodation
- Food
- Local travel
- Activities
- Miscellaneous expenses

If the estimated cost exceeds the user's budget, the AI suggests cheaper alternatives and ways to reduce expenses.

## 🎯 Personalization

Users can provide specifications such as:

- Beaches
- Temples
- Party places
- Adventure
- Food
- Nature
- Shopping
- Family-friendly activities

The AI uses these preferences when creating the itinerary.

## 🛡️ Security

The Groq API key is stored in a local `.env` file.

The `.env` file is excluded from GitHub using `.gitignore`.

Never commit or share your API key publicly.



## 📸 Screenshots

### 🏠 Home Page

![AI Travel Planner Home Page](screenshots/home.png)

### ✈️ Generated Travel Plan

![Generated Travel Plan](screenshots/travel-plan.png)