from flask import Blueprint, render_template, request, redirect, url_for, send_from_directory
import os
from werkzeug.utils import secure_filename

app_bp = Blueprint("app_bp", __name__, template_folder='templates')

UPLOAD_FOLDER = os.path.join('static','uploads')
ALLOWED_EXT = {'png','jpg','jpeg','gif'}

app_bp.config = {}
app_bp.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

students, next_id = {}, 21

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXT



    
@app_bp.route('/home')
def home_page():
    students = {
        1: {
            'name': 'Ramos, Sean Axl G.',
            'course': 'BSIT',
            'hobbies': 'Gym, Basketball',
            'languages': 'HTML AND CSS',
            'motto': 'Its ok to cry, But you have to move on',
            'Career interests': 'Web Development',
            'reason': 'To bring bright to a website as a future Web-developer',
            'picture': 'Silver.png'
        },
        2: {
            'name': 'Provido, Rasheed Rai',
            'course': 'BSIT',
            'hobbies': 'Basketball',
            'languages': 'JavaScript',
            'motto': 'Just Be Yourself.',
            'Career interests': 'Data analyst',
            'reason': 'The scope of this course is broad and there are many opportunities that can be obtained'
            'once you apply for jobs.',
            'picture': 'provido.jpg'
        },
        3: {
            'name': 'PELAEZ, SANDARAH N.',
            'course': 'BSIT',
            'hobbies': 'Reading and Cooking',
            'languages': 'C#',
            'motto': "Keep moving even if you feel like you're falling apart.",
            'Career interests': 'UI/UX Designer',
            'reason': 'Because I want to learn more about technologies and especially programming',
            'picture': 'PELAEZ.jpg'
        },
        4: {
            'name': 'QUIRANTE, LANCE MICHAEL D.',
            'course': 'BSIT',
            'hobbies': 'SPORTS, MUSIC, INSTRUMENTS, CODING/PROGRAMMING',
            'languages': 'PHP',
            'motto': "If tomorrow isn't the due date, today isn't the do date.",
            'Career interests': 'IT Business Analyst',
            'reason': 'To sharpen my skills when it comes to coding and programming.',
            'picture': 'QUIRANTE.jpg'
        },
        5: {
            'name': 'ZAMORA, KENNETH',
            'course': 'BSIT',
            'hobbies': 'BASKETBALL ',
            'languages': 'Ruby',
            'motto': "Pag kaya ng iba pagawa mo sa kanila..",
            'Career interests': 'Mobile App Developer',
            'reason': 'Dahil gusto ko maging programmer someday. ',
            'picture': 'ZAMORA.jpg'
        },
        6: {
            'name': 'VILLAMER, JHAY-EHM C.',
            'course': 'BSIT',
            'hobbies': 'WATCHING MOVIES/ANIME, CRAFTING AND PLAYING GAMES. ',
            'languages': 'Python',
            'motto': 'LEARN HOW TO REST, NOT TO QUIT..',
            'Career interests': 'Mobile App Developer',
            'reason': 'I want to learn how to code and explore a new environment in the field of IT.',
            'picture': 'VILLAMER.jpg'
        },
        7: {
            'name': 'LALIC, GILLIAN HILLARY T.',
            'course': 'BSIT',
            'hobbies': 'Watching kdrama, Listening to musics, Playing online games. ',
            'languages': 'JavaScript',
            'motto': 'Don’t wait for opportunity — create it.',
            'Career interests': 'Web Development',
            'reason': "I chose Computer Science instead of pursuing Law because even though I’m not naturally great at it, I see it as a challenge that will help me grow. I’ve always been curious about how technology works and how it shapes the world we live in. I believe that skills can be learned through effort and persistence, and Computer Science gives me the opportunity to keep improving myself. While Law is my dream course and focuses more on debate, analysis, and communication, Computer Science pushes me to think logically, be creative, and solve problems — even when it’s difficult. I may not be the best at it yet, but I’m willing to learn, make mistakes, and get better along the way. For me, choosing Computer Science isn’t just about what I’m good at now, but about what I want to become good at in the future.'once you apply for jobs.",
            'picture': 'LALIC.jpg'
        },
        8: {
            'name': 'Gubala, Jane Mariel',
            'course': 'BSIT',
            'hobbies': 'Dancing, Cooking, Playing badminton, Reading books, Watching Series',
            'languages': 'C#',
            'motto': "Keep moving even if you feel like you're falling apart.",
            'Career interests': 'UI/UX Designer',
            'reason': "My dream is to become a flight attendant, but I don’t want to focus only on that. That’s why I chose to take BSIT, since any course can qualify for a flight attendant career. I picked this course because it gives me more options and opportunities in the future. It’s also my backup plan—if I become a flight attendant and later retire, I can still go back to working in IT industry.",
            'picture': 'Gubala.jpg'
        },
        9: {
            'name': 'Sison,John Alexis P.',
            'course': 'BSCS',
            'hobbies': ' Playing Mobile Games, Cooking, reading manwha,manhua,mangga',
            'languages': 'CSS And JavaScript',
            'motto': "follow the path that was meant to you not what others created",
            'Career interests': 'Web development',
            'reason': 'I choose this course because i like creating personalize website and i just like coding ',
            'picture': 'SISON.jpg'
            },
        10: {
            'name': 'Legarde, Xyrus James D.',
            'course': 'BSCS',
            'hobbies': 'Gym, Playing, Dancing, Singing',
            'languages': 'Ruby',
            'motto': "It is not death that a man should fear, but he should fear never beginning to live.",
            'Career interests': 'UI/UX Designer, DevOps Eng. ',
            'reason': 'di ko rin alam pano',
            'picture': 'Legarde.jpg'
        },
        11:{
            'name': 'Romo, Zyron M.',
            'course': 'BSIT',
            'hobbies': 'Gym, Playing',
            'languages': 'Java',
            'motto': 'If i don’t have to do it, i won’t. but if i have to i will.',
            'Career interests': 'Web Development',
            'reason': 'To enhance my coding skills',
            'picture': 'Romo.jpg'
        },
        12: {
            'name': 'VILLAPA, NICHOLE FAITH ',
            'course': 'BSIT',
            'hobbies': 'Watching Movies, Singing, Listening to Music',
            'languages': 'JavaScript',
            'motto': 'Dream big, work for it, and you’ll achieve it.',
            'Career interests': 'UI/UX DESIGNER',
            'reason': 'Because, Technology in the future will be more advanced, so I think taking this Course helps me in the future.',
            'picture': 'Villapa.jpg'
        },
        13: {
            'name': ' Mallari, Florence Jamiel R.',
            'course': 'BSIT',
            'hobbies': 'Playing Video Games, Coding',
            'languages': 'Python',
            'motto': "God did🙏🏼.",
            'Career interests': 'DevOps',
            'reason': 'Nasanay kaka computer',
            'picture': 'Mallari.jpg'
        },
        14: {
            'name': ' Ajeto, Charlemagne A. ',
            'course': 'BSIT',
            'hobbies': 'Drawing, Reading Comics, Watching YouTube Video',
            'languages': 'Python',
            'motto': "The best way to predict your future is to create it.– Abraham Lincoln.",
            'Career interests': 'UI/UX Designer',
            'reason': "Well, It's practical to choose this course. It has many advantages that could help me in future.",
            'picture': 'Ajeto.jpg'
        },
        15: {
            'name': 'Abuan, Allen James G.',
            'course': 'BSIT',
            'hobbies': 'Drawing, playing',
            'languages': 'C++',
            'motto': "Trust the process",
            'Career interests': 'Data analyst',
            'reason': 'BSIT second choice ko sya tyaka suggested ng magulang ko',
            'picture': 'Abuan.jpg'
        },
        16: {
            'name': 'ENDONA, AARON',
            'course': 'BSIT',
            'hobbies': 'ONLINE COURSES, MAKING OPERATING SYSTEM ',
            'languages': 'Python',
            'motto': 'FROM ZERO TO HERO',
            'Career interests': 'Mobile App Developer',
            'reason': 'I SEE MY FASHION ON THIS FIELD.',
            'picture': 'ENDONA.jpg'
        },
        17: {
            'name': 'NUEVO, ROSALYN.',
            'course': 'BSIT',
            'hobbies': 'READING and WATCHING. ',
            'languages': 'C#',
            'motto': "IT ALWAYS SEEMS IMPOSSIBLE UNTIL IT'S DONE.",
            'Career interests': 'Software Developer',
            'reason': " I chose this course because, my heart flutters with excitement just thinking about writing a code or making my own program."
            "And I find it cool and thrilling.",
            'picture': 'NUEVO.jpg'
        },
        18: {
            'name': 'Olveda, Angeline',
            'course': 'BSIT',
            'hobbies': 'Reading, learning new things',
            'languages': ' C++,Basic knowledge',
            'motto': "Keep learning, keep growing.",
            'Career interests': 'IT Specialist',
            'reason': "I chose this course because I want to learn different kinds of knowledge about technology.",
            'picture': 'Olveda.jpg'
        },
        19:{
            'name': 'GALVEZ, JHEAN ROSE B.',
            'course': 'BSCS',
            'hobbies': 'Watching Animes & Kdrama, Singing, Dancing, DIY crafts, Crocheting, Painting, Drawing',
            'languages': 'CSS And JavaScript',
            'motto': "Positive energy over any negative energy.",
            'Career interests': 'UI/UX Designer',
            'reason': 'I chose BSIT because of high demand in technology and also to learn something new about technologies and softwares.  ',
            'picture': 'GALVEZ.jpg'
        },
        20:{
            'name': 'FORMENTERA, FLORES S.',
            'course': 'BSIT',
            'hobbies': 'playing guitar, singing, watching vlog, ',
            'languages': 'minimal in python and java',
            'motto': "Matutong mag hintay, darating din ang panahon",
            'Career interests': 'Programmer ',
            'reason': 'IT, Because In demand kasi siya ngayon, at sa susunod na henerasyone kaya ito ang pinasok ko.  ',
            'picture': 'FORMENTERA.jpg'
        }
    }
    query = request.args.get('query', '').strip().lower()
    if query:
        students = {
            sid: student for sid, student in students.items()
            if query in student['name'].lower()
        }
    return render_template('home.html', students=students, query=query)

@app_bp.route('/about')
def about():
    return render_template('about.html')

@app_bp.route('/gallery')
def gallery():
    return render_template('gallery.html')


########### CAREER INTEREST ###########

@app_bp.route('/career')
def career_page():
     return render_template('career.html')

@app_bp.route('/software')
def software():
    student = [
        {'name': 'NUEVO, ROSALYN.', 'picture': 'uploads/NUEVO.jpg', 'course': 'BSIT'},
        {'name': 'Ramos, Sean Axl G.', 'picture': 'uploads/Silver.png', 'course': 'BSIT'},
        {'name': 'LALIC, GILLIAN HILLARY T.', 'picture': 'uploads/LALIC.jpg', 'course': 'BSIT'},
        {'name': 'Romo, Zyron M.', 'picture': 'uploads/Romo.jpg', 'course': 'BSIT'},
        {'name': 'Sison,John Alexis P.', 'picture': 'uploads/SISOn.jpg', 'course': 'BSCS'},
        {'name': 'FORMENTERA, FLORES S.', 'picture': 'uploads/FORMENTERA.jpg', 'course': 'BSIT'},
    ]
    return render_template('soft.html', student=student)

@app_bp.route('/cyber')
def cyber():
    student = [
        {'name': 'Provido, Rasheed Rai', 'picture': 'uploads/provido.jpg', 'course': 'BSIT'},
    ]
    return render_template('cyber.html' , student=student)

@app_bp.route('/database')
def data_base():
    student = [
        {'name': 'Olveda, Angeline', 'picture': 'uploads/Olveda.jpg', 'course': 'BSIT'},
    ]
    return render_template('database.html' , student=student)

@app_bp.route('/mobile')
def mobile():
    student = [
        {'name': 'ZAMORA, KENNETH', 'picture': 'uploads/ZAMORA.jpg', 'course': 'BSIT'},
        {'name': 'VILLAMER, JHAY-EHM C.', 'picture': 'uploads/VILLAMER.jpg', 'course': 'BSIT'},
        {'name': 'ENDONA, AARON', 'picture': 'uploads/ENDONA.jpg', 'course': 'BSIT'},
    ]
    return render_template('mobile.html' , student=student)

@app_bp.route('/support')
def support():
    student = [
    ]
    return render_template('support.html' , student=student)

@app_bp.route('/cloud')
def cloud():
    student = [
        
    ]
    return render_template('cloud.html' , student=student)

@app_bp.route('/business')
def business():
    student = [
         {'name': 'QUIRANTE, LANCE MICHAEL D.', 'picture': 'uploads/QUIRANTE.jpg', 'course': 'BSIT'},
    ]
    return render_template('business.html' , student=student)

@app_bp.route('/ai')
def ai():
    student = [
    ]
    return render_template('ai.html' , student=student)

@app_bp.route('/data_scientist')
def data_scientist():
    student = [
    ]
    return render_template('datascientist.html' , student=student)

@app_bp.route('/designer')
def designer():
    student = [
        {'name': 'PELAEZ, SANDARAH N.', 'picture': 'uploads/PELAEZ.jpg', 'course': 'BSIT'},
        {'name': 'Gubala, Jane Mariel', 'picture': 'uploads/Gubala.jpg', 'course': 'BSIT'},
        {'name': 'Legarde, Xyrus James D.', 'picture': 'uploads/Legarde.jpg', 'course': 'BSCS'},
        {'name': 'VILLAPA, NICHOLE FAITH ', 'picture': 'uploads/Villapa.jpg', 'course': 'BSIT'},
        {'name': 'Ajeto, Charlemagne A.', 'picture': 'uploads/Ajeto.jpg', 'course': 'BSIT'},
        {'name': 'GALVEZ, JHEAN ROSE B.', 'picture': 'uploads/GALVEZ.jpg', 'course': 'BSIT'},
    ]
    return render_template('designer.html' , student=student)

@app_bp.route('/tester')
def tester():
    student = [
    ]
    return render_template('tester.html' , student=student)

@app_bp.route('/consultant')
def consultant():
    student = [
    ]
    return render_template('consultant.html' , student=student)

@app_bp.route('/devOps')
def Devops():
    student = [
        {'name': 'Legarde, Xyrus James D.', 'picture': 'uploads/Legarde.jpg', 'course': 'BSCS'},
        {'name': 'Mallari, Florence Jamiel R.', 'picture': 'uploads/Mallari.jpg', 'course': 'BSIT'},
    ]
    return render_template('devOps.html' , student=student)

@app_bp.route('/analyst')
def analyst():
    student = [
        {'name': 'Abuan, Allen James G.', 'picture': 'uploads/Abuan.jpg', 'course': 'BSIT'},
    ]
    return render_template('data_analyst.html' , student=student)

@app_bp.route('/Administrator')
def Administrator():
    student = [
    ]
    return render_template('data_admin.html' , student=student)


########### END CAREER INTEREST ###########


@app_bp.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app_bp.config['UPLOAD_FOLDER'], filename)

@app_bp.route('/profile/<int:student_id>')
def profile(student_id):
    student = students.get(student_id)
    return render_template('profile.html', student=students.get(student_id), student_id=student_id)

@app_bp.route('/add', methods=['GET', 'POST'])
def add_student():
    global next_id
    if request.method == 'POST':
        data = {k: request.form.get(k, '').strip() for k in
                ['name','course','hobbies','languages','motto','reason']}
        file = request.files.get('picture')
        filename = 'default.png'
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(UPLOAD_FOLDER, filename))
        data['picture'] = filename
        students[next_id] = data
        next_id += 1
        return redirect(url_for('app_bp.home_page'))
    return render_template('add.html')

@app_bp.route('/edit/<int:student_id>', methods=['GET', 'POST'])
def edit(student_id):
    s = students.get(student_id)
    if not s: return "Student not found", 404
    if request.method == 'POST':
        for k in ['name','course','hobbies','languages','motto','reason']:
            s[k] = request.form.get(k, '').strip()
        file = request.files.get('picture')
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(UPLOAD_FOLDER, filename))
            s['picture'] = filename
        return redirect(url_for('app_bp.profile', student_id=student_id))
    return render_template('edit.html', student=s, student_id=student_id)

@app_bp.route('/delete/<int:student_id>', methods=['POST'])
def delete(student_id):
    global students           
    students.pop(student_id, None)
    return redirect(url_for('app_bp.home_page'))