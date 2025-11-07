from flask import Flask, render_template, request
from templates.app import app_bp, students, UPLOAD_FOLDER
import os 

app = Flask(__name__)

@app.route('/')
def main_page():
    return render_template('main.html')

app.register_blueprint(app_bp)

app.config['UPLOAD_FOLDER'] = 'UPLOAD_FOLDER'
app.config['MAX_CONTENT_LENGTH'] = 2 * 1024 * 1024

if __name__ == '__main__':

 os.makedirs(UPLOAD_FOLDER, exist_ok=True)
 students[1] = {
        'name': 'Ramos, Sean Axl G.',
        'course': 'BSIT',
        'hobbies': 'Gym, Basketball',
        'languages': 'HTML AND CSS',
        'motto': 'Its ok to cry, But you have to move on',
        'Career interests': 'Web Development',
        'reason': 'To bring bright to a website as a future Web-developer',
        'picture': 'Silver.png'
    }
 students[2] = {
        'name': 'Provido, Rasheed Rai',
        'course': 'BSIT',
        'hobbies': 'Basketball',
        'languages': 'JavaScript',
        'motto': 'Just Be Yourself.',
        'Career interests': 'Data analyst',
        'reason': 'Why I choose this Course: The scope of this course is broad and there are many opportunities that can be obtained'
        'once you apply for jobs.',
        'picture': 'provido.jpg'
    }
 students[3] = {
        'name': 'PELAEZ, SANDARAH N.',
        'course': 'BSIT',
        'hobbies': 'Reading and Cooking',
        'languages': 'C#',
        'motto': "Keep moving even if you feel like you're falling apart.",
        'Career interests': 'UI/UX Designer',
        'reason': 'Because I want to learn more about technologies and especially programming',
        'picture': 'PELAEZ.jpg'
    }
 students[4] = {
        'name': 'QUIRANTE, LANCE MICHAEL D.',
        'course': 'BSIT',
        'hobbies': 'SPORTS, MUSIC, INSTRUMENTS, CODING/PROGRAMMING',
        'languages': 'PHP',
        'motto': "If tomorrow isn't the due date, today isn't the do date.",
        'Career interests': 'IT Business Analyst',
        'reason': 'To sharpen my skills when it comes to coding and programming.',
        'picture': 'QUIRANTE.jpg'
    }
 students[5] = {
        'name': 'ZAMORA, KENNETH',
        'course': 'BSIT',
        'hobbies': 'BASKETBALL ',
        'languages': 'Ruby',
        'motto': "Pag kaya ng iba pagawa mo sa kanila..",
        'Career interests': 'Mobile App Developer',
        'reason': 'Dahil gusto ko maging programmer someday. ',
        'picture': 'ZAMORA.jpg'
    }
 students[6] = {
        'name': 'VILLAMER, JHAY-EHM C.',
        'course': 'BSIT',
        'hobbies': 'WATCHING MOVIES/ANIME, CRAFTING AND PLAYING GAMES. ',
        'languages': 'Python',
        'motto': 'LEARN HOW TO REST, NOT TO QUIT..',
        'Career interests': 'Mobile App Developer',
        'reason': 'I want to learn how to code and explore a new environment in the field of IT.',
        'picture': 'VILLAMER.jpg'
    }
 students[7] = {
        'name': 'LALIC, GILLIAN HILLARY T.',
        'course': 'BSIT',
        'hobbies': 'Watching kdrama, Listening to musics, Playing online games. ',
        'languages': 'JavaScript',
        'motto': 'Don’t wait for opportunity — create it.',
        'Career interests': 'Web Development',
        'reason': "I chose Computer Science instead of pursuing Law because even though I’m not "
        "naturally great at it, I see it as a challenge that will help me grow. I’ve always been curious "
        "about how technology works and how it shapes the world we live in. I believe that skills can be learned "
        "through effort and persistence, and Computer Science gives me the opportunity to keep improving myself. "
        "While Law is my dream course and focuses more on debate, analysis, and communication, Computer Science p"
        "ushes me to think logically, be creative, and solve problems — even when it’s difficult. I may not be the best at it yet, "
        "but I’m willing to learn, make mistakes, and get better along the way. For me, choosing Computer Science isn’t just about what "
        "I’m good at now, but about what I want to become good at in the future.'once you apply for jobs.",
        'picture': 'LALIC.jpg'
    }
 students[8] = {
        'name': 'Gubala, Jane Mariel',
        'course': 'BSIT',
        'hobbies': 'Dancing, Cooking, Playing badminton, Reading books, Watching Series',
        'languages': 'C#',
        'motto': "Keep moving even if you feel like you're falling apart.",
        'Career interests': 'UI/UX Designer',
        'reason': "My dream is to become a flight attendant, but I don’t want to focus only on that. That’s why I chose to take BSIT, since any course can qualify for a flight attendant career. I picked this course because it gives me more options and opportunities in the future. It’s also my backup plan—if I become a flight attendant and later retire, I can still go back to working in IT industry.",
        'picture': 'Gubala.jpg'
    }
 students[9] = {
        'name': 'Sison,John Alexis P.',
        'course': 'BSCS',
        'hobbies': ' Playing Mobile Games, Cooking, reading manwha,manhua,mangga',
        'languages': 'CSS And JavaScript',
        'motto': "follow the path that was meant to you not what others created",
        'Career interests': 'Web Development',
        'reason': 'I choose this course because i like creating personalize website and i just like coding ',
        'picture': 'SISON.jpg'
    }
 students[10] = {
        'name': 'Legarde, Xyrus James D.',
        'course': 'BSCS',
        'hobbies': 'Gym, Playing, Dancing, Singing',
        'languages': 'Ruby',
        'motto': "It is not death that a man should fear, but he should fear never beginning to live.",
        'Career interests': 'UI/UX Designer, DevOps Eng. ',
        'reason': 'di ko rin alam pano',
        'picture': 'Legarde.jpg'
    }
 students[11] = {
        'name': 'Romo, Zyron M.',
        'course': 'BSIT',
        'hobbies': 'Gym, Playing',
        'languages': 'Java',
        'motto': 'If i don’t have to do it, i won’t. but if i have to i will.',
        'Career interests': 'Web Development',
        'reason': 'To enhance my coding skills',
        'picture': 'Romo.jpg'
    }
 students[12] = {
        'name': 'VILLAPA, NICHOLE FAITH ',
        'course': 'BSIT',
        'hobbies': 'Watching Movies, Singing, Listening to Music',
        'languages': 'JavaScript',
        'motto': 'Dream big, work for it, and you’ll achieve it.',
        'Career interests': 'UI/UX DESIGNER',
        'reason': 'Because, Technology in the future will be more advanced, so I think taking this Course helps me in the future.',
        'picture': 'Villapa.jpg'
    }
 students[13] = {
        'name': ' Mallari, Florence Jamiel R.',
        'course': 'BSIT',
        'hobbies': 'Playing Video Games, Coding',
        'languages': 'Python',
        'motto': "God did🙏🏼.",
        'Career interests': 'DevOps',
        'reason': 'Nasanay kaka computer',
        'picture': 'Mallari.jpg'
    }
 students[14] = {
        'name': ' Ajeto, Charlemagne A. ',
        'course': 'BSIT',
        'hobbies': 'Drawing, Reading Comics, Watching YouTube Video',
        'languages': 'Python',
        'motto': "The best way to predict your future is to create it.– Abraham Lincoln.",
        'Career interests': 'UI/UX Designer',
        'reason': "Well, It's practical to choose this course. It has many advantages that could help me in future.",
        'picture': 'Ajeto.jpg'
    }
 students[15] = {
        'name': 'Abuan, Allen James G.',
        'course': 'BSIT',
        'hobbies': 'Drawing, playing',
        'languages': 'C++',
        'motto': "Trust the process",
        'Career interests': 'Data analyst',
        'reason': 'BSIT second choice ko sya tyaka suggested ng magulang ko',
        'picture': 'Abuan.jpg'
    }
 students[16] = {
        'name': 'ENDONA, AARON',
        'course': 'BSIT',
        'hobbies': 'ONLINE COURSES, MAKING OPERATING SYSTEM ',
        'languages': 'Python',
        'motto': 'FROM ZERO TO HERO',
        'Career interests': 'Mobile App Developer',
        'reason': 'I SEE MY FASHION ON THIS FIELD.',
        'picture': 'ENDONA.jpg'
    }
 students[17] = {
        'name': 'NUEVO, ROSALYN.',
        'course': 'BSIT',
        'hobbies': 'READING and WATCHING. ',
        'languages': 'C#',
        'motto': "IT ALWAYS SEEMS IMPOSSIBLE UNTIL IT'S DONE.",
        'Career interests': 'Software Developer',
        'reason': " I chose this course because, my heart flutters with excitement just thinking about writing a code or making my own program."
        " And I find it cool and thrilling.",
        'picture': 'NUEVO.jpg'
    }
 students[18] = {
        'name': 'Olveda, Angeline',
        'course': 'BSIT',
        'hobbies': 'Reading, learning new things',
        'languages': ' C++,Basic knowledge',
        'motto': "Keep learning, keep growing.",
        'Career interests': 'IT Specialist',
        'reason': "I chose this course because I want to learn different kinds of knowledge about technology.",
        'picture': 'Olveda.jpg'
    }
 students[19] = {
        'name': 'GALVEZ, JHEAN ROSE B.',
        'course': 'BSCS',
        'hobbies': 'Watching Animes & Kdrama, Singing, Dancing, DIY crafts, Crocheting, Painting, Drawing',
        'languages': 'CSS And JavaScript',
        'motto': "Positive energy over any negative energy.",
        'Career interests': 'UI/UX Designer',
        'reason': 'I chose BSIT because of high demand in technology and also to learn something new about technologies and softwares.  ',
        'picture': 'GALVEZ.jpg'
    }
 students[20] = {
        'name': 'FORMENTERA, FLORES S.',
        'course': 'BSIT',
        'hobbies': 'playing guitar, singing, watching vlog, ',
        'languages': 'minimal in python and java',
        'motto': "Matutong mag hintay, darating din ang panahon",
        'Career interests': 'Programmer',
        'reason': 'IT, Because In demand kasi siya ngayon, at sa susunod na henerasyone kaya ito ang pinasok ko.  ',
        'picture': 'FORMENTERA.jpg'
    }

app.run(debug=True)