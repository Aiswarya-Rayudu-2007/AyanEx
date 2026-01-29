from flask import Flask, render_template, request, session
from flask import redirect, url_for, flash

app = Flask(__name__)
app.secret_key = "ayanex_secret_key"
# Temporary user store (for hackathon demo)
USERS = {}
# 2️⃣ AI MOCK INTERVIEW HELPER FUNCTION (STEP 1)
def generate_mock_interview_questions(role, level):
    return [
        {
            "id": 1,
            "question": f"What are the core skills required for a {role}?"
        },
        {
            "id": 2,
            "question": f"Explain one challenge you faced while learning {role} skills."
        },
        {
            "id": 3,
            "question": f"How do you keep yourself updated in the {role} field?"
        }
    ]


MARKET_SKILL_DEMAND = {
    "Python": "rising",
    "SQL": "rising",
    "Machine Learning": "rising",
    "AI tools":"rising",
    "React": "stable",
    "Java": "stable",
    "PHP": "declining",
    "Manual Testing": "declining"
}




# ------------------ SPLASH PAGE ------------------
@app.route('/')
def splash():
    return render_template('splash.html')


# ------------------ HOME PAGE ------------------
@app.route('/home')
def home():
    print("HOME SESSION:", session)  # DEBUG

    if 'user' not in session:
        return redirect(url_for('login'))

    return render_template('home.html', user=session['user'])




# ------------------ SKILL INPUT & RESULT ------------------
@app.route('/skill_input', methods=['GET', 'POST'])
def skill_input():
    if request.method == 'POST':
        role = request.form['role']
        experience = int(request.form['experience'])

        # ----------- Risk Logic -----------
        if role.lower() in ['data entry', 'data entry specialist']:
            risk = "High risk of AI disruption"
            risk_percentage = 85
            skills = ["Python", "AI Tools", "Data Analysis"]
            roadmap = [
                "Learn Python fundamentals (0–2 months)",
                "Understand AI tools & automation",
                "Start Data Analysis (Excel, Pandas, SQL)",
                "Build 2–3 mini projects",
                "Apply for AI-resilient roles"
            ]

        elif experience < 5:
            risk = "Moderate risk of AI disruption"
            risk_percentage = 55
            skills = ["Advanced Python", "One AI Tool", "System Design"]
            roadmap = [
                "Improve problem solving skills",
                "Learn one AI tool deeply",
                "Build one real-world project",
                "Prepare for mid-level roles"
            ]

        else:
            risk = "Low risk of AI disruption"
            risk_percentage = 25
            skills = ["AI-assisted development", "Leadership", "Architecture"]
            roadmap = [
                "Stay updated with AI trends",
                "Adopt AI-assisted coding",
                "Focus on leadership & mentoring",
                "Move towards architect roles"
            ]

        return render_template(
            'result.html',
            role=role,
            experience=experience,
            risk=risk,
            risk_percentage=risk_percentage,
            skills=skills,
            roadmap=roadmap
        )

    return render_template('skill_input.html')


# ------------------ DAILY TEST : PYTHON ------------------
@app.route('/daily_test/python', methods=['GET', 'POST'])
def daily_test_python():
  

    # 🔐 STEP 6 GOES HERE
    if 'user' not in session:
        return redirect(url_for('login'))

    

    init_progress() 
    questions = [
        {
            "id": 1,
            "question": "What is the output of print(type([]))?",
            "options": ["list", "tuple", "dict", "set"],
            "answer": "list",
            "explanation": "[] creates a list in Python."
        },
        {
            "id": 2,
            "question": "Which keyword defines a function in Python?",
            "options": ["func", "define", "def", "function"],
            "answer": "def",
            "explanation": "`def` is used to define functions."
        },
        {
            "id": 3,
            "question": "Which data type is immutable?",
            "options": ["list", "set", "dict", "tuple"],
            "answer": "tuple",
            "explanation": "Tuples cannot be changed after creation."
        },
        {
            "id": 4,
            "question": "What does len() do?",
            "options": ["Counts characters", "Returns length", "Adds values", "Deletes data"],
            "answer": "Returns length",
            "explanation": "len() returns number of items."
        },
        {
            "id": 5,
            "question": "Which symbol is used for comments?",
            "options": ["//", "/* */", "#", "<!-- -->"],
            "answer": "#",
            "explanation": "# is used for comments in Python."
        },
        {
            "id": 6,
            "question": "What is the output of 2**3?",
            "options": ["6", "8", "9", "5"],
            "answer": "8",
            "explanation": "** is exponent operator."
        },
        {
            "id": 7,
            "question": "Which keyword is used for loops?",
            "options": ["loop", "for", "iterate", "repeat"],
            "answer": "for",
            "explanation": "`for` is used for looping."
        }
    ]

    leetcode = [
        {"title": "Two Sum", "link": "https://leetcode.com/problems/two-sum/"},
        {"title": "Valid Parentheses", "link": "https://leetcode.com/problems/valid-parentheses/"},
        {"title": "Reverse Integer", "link": "https://leetcode.com/problems/reverse-integer/"}
    ]

    # -------- POST : calculate result --------
    if request.method == 'POST':
        score = 0
        wrong = []

        for q in questions:
            user_ans = request.form.get(f"q{q['id']}")
            if user_ans == q['answer']:
                score += 1
            else:
                wrong.append({
                    "question": q['question'],
                    "correct": q['answer'],
                    "explanation": q['explanation']
                })
        init_progress()

        session["progress"]["tests_taken"] += 1
        session["progress"]["questions_attempted"] += len(questions)
        session["progress"]["correct_answers"] += score

        session["progress"]["skills"]["Python"]["tests"] += 1
        session["progress"]["skills"]["Python"]["correct"] += score

        session.modified = True


        return render_template(
            'test_result.html',
            score=score,
            wrong=wrong,
            total=len(questions),
            skill="Python",
            progress=session["progress"]
        )

    # -------- GET : show questions --------
    return render_template(
        'daily_test.html',
        questions=questions,
        leetcode=leetcode,
        skill="Python",
        progress=session["progress"]
    )


# ------------------ DAILY TEST : AI ------------------
@app.route('/daily_test/ai', methods=['GET', 'POST'])
def daily_test_ai():
   

    # 🔐 STEP 6 GOES HERE
    if 'user' not in session:
        return redirect(url_for('login'))

    init_progress() 
    questions = [
        {
            "id": 1,
            "question": "What does AI primarily aim to do?",
            "options": [
                "Replace all humans",
                "Mimic human intelligence",
                "Only store data",
                "Control the internet"
            ],
            "answer": "Mimic human intelligence",
            "explanation": "AI systems are designed to simulate human intelligence like learning and decision-making."
        },
        {
            "id": 2,
            "question": "Which of the following is an AI application?",
            "options": [
                "Calculator",
                "Search engine ranking",
                "Text editor",
                "File explorer"
            ],
            "answer": "Search engine ranking",
            "explanation": "Search engines use AI algorithms to rank results."
        },
        {
            "id": 3,
            "question": "Which field is closely related to AI?",
            "options": [
                "Machine Learning",
                "Civil Engineering",
                "Mechanical Drawing",
                "Thermodynamics"
            ],
            "answer": "Machine Learning",
            "explanation": "Machine Learning is a core subfield of AI."
        },
        {
            "id": 4,
            "question": "What is Machine Learning?",
            "options": [
                "Hard-coded programming",
                "Learning from data automatically",
                "Manual testing process",
                "Database management"
            ],
            "answer": "Learning from data automatically",
            "explanation": "Machine Learning allows systems to learn patterns from data without explicit programming."
        },
        {
            "id": 5,
            "question": "Which of the following is an example of AI in daily life?",
            "options": [
                "Voice assistants",
                "Keyboard",
                "Mouse",
                "USB cable"
            ],
            "answer": "Voice assistants",
            "explanation": "Voice assistants like Alexa and Siri use AI."
        },
        {
            "id": 6,
            "question": "What does NLP stand for?",
            "options": [
                "Natural Learning Program",
                "Neural Language Process",
                "Natural Language Processing",
                "Network Logic Protocol"
            ],
            "answer": "Natural Language Processing",
            "explanation": "NLP helps machines understand human language."
        },
        {
            "id": 7,
            "question": "Which type of AI can perform a single task very well?",
            "options": [
                "General AI",
                "Super AI",
                "Narrow AI",
                "Strong AI"
            ],
            "answer": "Narrow AI",
            "explanation": "Narrow AI is designed for specific tasks like image recognition."
        },
        {
            "id": 8,
            "question": "Which algorithm is commonly used in Machine Learning?",
            "options": [
                "Linear Regression",
                "Bubble Sort",
                "Binary Search",
                "Stack"
            ],
            "answer": "Linear Regression",
            "explanation": "Linear Regression is a basic machine learning algorithm."
        },
        {
            "id": 9,
            "question": "What is the main requirement for training an AI model?",
            "options": [
                "High-speed internet",
                "Large amount of data",
                "Graphics card only",
                "Text editor"
            ],
            "answer": "Large amount of data",
            "explanation": "AI models learn patterns from large datasets."
        },
        {
            "id": 10,
            "question": "Which company is well-known for AI research?",
            "options": [
                "OpenAI",
                "Wikipedia",
                "Stack Overflow",
                "GitHub"
            ],
            "answer": "OpenAI",
            "explanation": "OpenAI is a leading organization in AI research."
        }
    ]


    # -------- POST : calculate result --------
    if request.method == 'POST':
        score = 0
        wrong = []

        for q in questions:
            user_ans = request.form.get(f"q{q['id']}")
            if user_ans == q['answer']:
                score += 1
            else:
                wrong.append({
                    "question": q['question'],
                    "correct": q['answer'],
                    "explanation": q['explanation']
                })
        init_progress()

        session["progress"]["tests_taken"] += 1
        session["progress"]["questions_attempted"] += len(questions)
        session["progress"]["correct_answers"] += score

        session["progress"]["skills"]["AI"]["tests"] += 1
        session["progress"]["skills"]["AI"]["correct"] += score

        session.modified = True


        return render_template(
            'test_result.html',
            score=score,
            wrong=wrong,
            total=len(questions),
            skill="AI",
            progress=session["progress"]
        )

    # -------- GET : show questions --------
    return render_template(
        'daily_test.html',
        questions=questions,
        skill="AI",
        progress=session["progress"]
    )
# ------------------ DAILY TEST : SQL ------------------
@app.route('/daily_test/sql', methods=['GET', 'POST'])
def daily_test_sql():
    if 'user' not in session:
        return redirect(url_for('login'))

    init_progress() 
    questions = [
        {
            "id": 1,
            "question": "What does SQL stand for?",
            "options": [
                "Structured Query Language",
                "Simple Query Language",
                "Sequential Query Language",
                "Standard Question Language"
            ],
            "answer": "Structured Query Language",
            "explanation": "SQL stands for Structured Query Language."
        },
        {
            "id": 2,
            "question": "Which SQL command is used to retrieve data?",
            "options": ["GET", "FETCH", "SELECT", "RETRIEVE"],
            "answer": "SELECT",
            "explanation": "SELECT is used to fetch data from a database."
        },
        {
            "id": 3,
            "question": "Which clause is used to filter records?",
            "options": ["ORDER BY", "GROUP BY", "WHERE", "HAVING"],
            "answer": "WHERE",
            "explanation": "WHERE filters rows based on a condition."
        },
        {
            "id": 4,
            "question": "Which SQL statement is used to insert data?",
            "options": ["ADD", "INSERT INTO", "UPDATE", "CREATE"],
            "answer": "INSERT INTO",
            "explanation": "INSERT INTO adds new records to a table."
        },
        {
            "id": 5,
            "question": "Which keyword is used to sort results?",
            "options": ["SORT", "ORDER BY", "GROUP BY", "ARRANGE"],
            "answer": "ORDER BY",
            "explanation": "ORDER BY sorts the result set."
        },
        {
            "id": 6,
            "question": "Which function returns the number of rows?",
            "options": ["SUM()", "COUNT()", "TOTAL()", "NUMBER()"],
            "answer": "COUNT()",
            "explanation": "COUNT() returns the number of rows."
        },
        {
            "id": 7,
            "question": "Which SQL statement updates existing data?",
            "options": ["UPDATE", "MODIFY", "CHANGE", "INSERT"],
            "answer": "UPDATE",
            "explanation": "UPDATE modifies existing records."
        },
        {
            "id": 8,
            "question": "Which keyword deletes data from a table?",
            "options": ["REMOVE", "DELETE", "DROP", "CLEAR"],
            "answer": "DELETE",
            "explanation": "DELETE removes records from a table."
        },
        {
            "id": 9,
            "question": "Which SQL constraint ensures unique values?",
            "options": ["PRIMARY KEY", "NOT NULL", "UNIQUE", "FOREIGN KEY"],
            "answer": "UNIQUE",
            "explanation": "UNIQUE ensures no duplicate values."
        },
        {
            "id": 10,
            "question": "Which statement removes a table completely?",
            "options": ["DELETE", "DROP", "TRUNCATE", "REMOVE"],
            "answer": "DROP",
            "explanation": "DROP deletes the table structure permanently."
        }
    ]

    # -------- POST : calculate result --------
    if request.method == 'POST':
        score = 0
        wrong = []

        for q in questions:
            user_ans = request.form.get(f"q{q['id']}")
            if user_ans == q['answer']:
                score += 1
            else:
                wrong.append({
                    "question": q['question'],
                    "correct": q['answer'],
                    "explanation": q['explanation']
                })
        init_progress()

        session["progress"]["tests_taken"] += 1
        session["progress"]["questions_attempted"] += len(questions)
        session["progress"]["correct_answers"] += score

        session["progress"]["skills"]["SQL"]["tests"] += 1
        session["progress"]["skills"]["SQL"]["correct"] += score

        session.modified = True

        return render_template(
            'test_result.html',
            score=score,
            wrong=wrong,
            total=len(questions),
            skill="SQL",
            progress=session["progress"]
        )

    # -------- GET : show questions --------
    return render_template(
        'daily_test.html',
        questions=questions,
        skill="SQL",
        progress=session["progress"]

    )
@app.route('/daily_test/robotics', methods=['GET', 'POST'])
def daily_test_robotics():
    if 'user' not in session:
        return redirect(url_for('login'))

    init_progress()
    questions = [
    {
        "id": 1,
        "question": "What is a robot?",
        "options": [
            "A human assistant",
            "A programmable machine",
            "A computer only",
            "An AI algorithm"
        ],
        "answer": "A programmable machine",
        "explanation": "A robot is a programmable machine capable of carrying out tasks automatically."
    },
    {
        "id": 2,
        "question": "Which component acts as the brain of a robot?",
        "options": ["Sensor", "Actuator", "Controller", "Motor"],
        "answer": "Controller",
        "explanation": "The controller processes inputs and controls robot actions."
    },
    {
        "id": 3,
        "question": "Which sensor helps a robot detect distance?",
        "options": ["Temperature sensor", "Ultrasonic sensor", "Light sensor", "Touch sensor"],
        "answer": "Ultrasonic sensor",
        "explanation": "Ultrasonic sensors measure distance using sound waves."
    },
    {
        "id": 4,
        "question": "What do actuators do in a robot?",
        "options": [
            "Sense environment",
            "Make decisions",
            "Perform movements",
            "Store data"
        ],
        "answer": "Perform movements",
        "explanation": "Actuators convert signals into physical movement."
    },
    {
        "id": 5,
        "question": "Which field combines AI with physical machines?",
        "options": ["Web development", "Robotics", "Networking", "Databases"],
        "answer": "Robotics",
        "explanation": "Robotics integrates AI with hardware to act in the real world."
    },{
    "id": 6,
    "question": "What is the main function of actuators in a robot?",
    "options": [
        "Sense the environment",
        "Process data",
        "Produce movement",
        "Store information"
    ],
    "answer": "Produce movement",
    "explanation": "Actuators convert electrical signals into physical motion."
},
{
    "id": 7,
    "question": "Which component acts as the brain of a robot?",
    "options": [
        "Motor",
        "Sensor",
        "Controller",
        "Battery"
    ],
    "answer": "Controller",
    "explanation": "The controller processes inputs and controls robot actions."
},
{
    "id": 8,
    "question": "Which sensor is commonly used to detect distance?",
    "options": [
        "Temperature sensor",
        "Ultrasonic sensor",
        "Light sensor",
        "Gas sensor"
    ],
    "answer": "Ultrasonic sensor",
    "explanation": "Ultrasonic sensors measure distance using sound waves."
},
{
    "id": 9,
    "question": "What does ROS stand for in robotics?",
    "options": [
        "Robot Operating System",
        "Real Object Simulation",
        "Remote Operating Software",
        "Robot Orientation System"
    ],
    "answer": "Robot Operating System",
    "explanation": "ROS is a flexible framework for writing robot software."
},
{
    "id": 10,
    "question": "Which type of robot is commonly used in manufacturing industries?",
    "options": [
        "Humanoid robot",
        "Medical robot",
        "Industrial robot",
        "Service robot"
    ],
    "answer": "Industrial robot",
    "explanation": "Industrial robots are widely used for automation in factories."
}
]


    if request.method == 'POST':
        score = 0
        wrong = []

        for q in questions:
            user_ans = request.form.get(f"q{q['id']}")
            if user_ans == q['answer']:
                score += 1
            else:
                wrong.append({
                    "question": q['question'],
                    "correct": q['answer'],
                    "explanation": q['explanation']
                })

        session["progress"]["tests_taken"] += 1
        session["progress"]["questions_attempted"] += len(questions)
        session["progress"]["correct_answers"] += score

        session["progress"]["skills"]["Robotics"]["tests"] += 1
        session["progress"]["skills"]["Robotics"]["correct"] += score

        session.modified = True

        return render_template(
            'test_result.html',
            score=score,
            wrong=wrong,
            total=len(questions),
            skill="Robotics",
            progress=session["progress"]
        )

    return render_template(
        'daily_test.html',
        questions=questions,
        skill="Robotics",
        progress=session["progress"]
    )

def init_progress():
    if "progress" not in session:
        session["progress"] = {
            "tests_taken": 0,
            "questions_attempted": 0,
            "correct_answers": 0,
            "skills": {
                "Python": {"tests": 0, "correct": 0},
                "AI": {"tests": 0, "correct": 0},
                "SQL": {"tests": 0, "correct": 0},
                "Robotics": {"tests": 0, "correct": 0}
            }
        }
@app.route('/skill-heatmap')
def skill_heatmap():
    heatmap_data = []

    for skill, trend in MARKET_SKILL_DEMAND.items():
        heatmap_data.append({
            "skill": skill,
            "trend": trend
        })

    return render_template("skill_heatmap.html", heatmap=heatmap_data)

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        if username in USERS:
            flash("User already exists")
            return redirect(url_for('register'))

        USERS[username] = password
        flash("Account created successfully. Please login.")
        return redirect(url_for('login'))

    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        print("LOGIN ATTEMPT:", username, password)  # DEBUG

        if username in USERS and USERS[username] == password:
            session.clear()                 # 🔥 IMPORTANT
            session['user'] = username
            session['is_premium'] = True
            print("LOGIN SUCCESS, SESSION:", session)
            return redirect(url_for('home'))
        else:
            flash("Invalid username or password")

    return render_template('login.html')

@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('login'))




@app.route('/mock_interview', methods=['GET', 'POST'])
def mock_interview():

    # 🔒 PREMIUM CHECK
    if not session.get('is_premium'):
        return render_template('premium_lock.html')

    questions = None

    if request.method == 'POST':
        role = request.form.get('role')
        level = request.form.get('level')

        questions = generate_mock_interview_questions(role, level)

    return render_template(
        'mock_interview.html',
        questions=questions
    )
@app.route('/mock_interview_result', methods=['POST'])
def mock_interview_result():
    answers = []
    
    for key in request.form:
        if key.startswith("answer_"):
            answers.append(request.form[key])

    total_questions = len(answers)

    # SAFETY CHECK (VERY IMPORTANT)
    if total_questions == 0:
        return "No answers submitted. Please try again."

    score = 0

    for ans in answers:
        if len(ans.strip()) > 30:
            score += 3
        elif len(ans.strip()) > 15:
            score += 2
        elif len(ans.strip()) > 5:
            score += 1

    final_score = round((score / (total_questions * 3)) * 10)

    confidence = int((score / (total_questions * 3)) * 100)
    feedback = []

    for i, ans in enumerate(answers, start=1):
        if len(ans.strip()) > 30:
            remark = "Good structured answer"
        elif len(ans.strip()) > 15:
            remark = "Answer needs more depth"
        else:
            remark = "Answer is too short"

        feedback.append({
            "question": f"Q{i}",
            "remark": remark
        })


    return render_template(
        'mock_result.html',
        final_score=final_score,
        confidence=confidence,
        feedback=feedback
    )


# ------------------ RUN APP ------------------
if __name__ == '__main__':
    app.run(debug=True)