from flask import Flask, render_template

app = Flask(__name__)
app.config['FREEZER_RELATIVE_URLS'] = True

@app.route('/')
def home():
    skills = [
        {"name": "Flutter", "category": "Framework", "level": 95},
        {"name": "Dart", "category": "Language", "level": 90},
        {"name": "Python", "category": "Language", "level": 80},
        {"name": "Firebase", "category": "Backend", "level": 85},
        {"name": "REST APIs", "category": "Networking", "level": 90},
        {"name": "HTML & CSS", "category": "Frontend", "level": 85},
        {"name": "Git/GitHub", "category": "Version Control", "level": 85},
        {"name": "Android Studio", "category": "IDE", "level": 90},
        {"name": "VS Code", "category": "IDE", "level": 90}
    ]
    
    projects = [
        {
            "title": "Reachout",
            "description": "A smart, eco-friendly digital business card. ReachOut replaces physical clutter with dynamic, cloud-based profiles, seamless cross-device access, and real-time networking updates.",
            "type": "Mobile App",
            "tags": ["Flutter", "Dart", "API"],
            "links": [{"label": "Play Store", "url": "https://play.google.com/store/apps/details?id=in.reachout_mobile"}]
        },
        {
            "title": "Reachout Corporate (Ongoing)",
            "description": "A dynamic communication platform designed to enhance real-time collaboration, boost productivity, and foster transparent engagement across both remote and in-office teams.",
            "type": "App & Web",
            "tags": ["Flutter Web", "GetX", "REST"],
            "links": [
                {"label": "Play Store", "url": "https://play.google.com/store/apps/details?id=com.reachoutAlpha.corporatemobile"},
                {"label": "Website", "url": "https://corporate.reachout.ltd"}
            ]
        },
        {
            "title": "Buyit App",
            "description": "Provides users with a simple and efficient way to create and manage purchase lists.",
            "type": "Mobile App",
            "tags": ["Flutter", "BLoC", "UI/UX"],
            "links": [{"label": "Play Store", "url": "https://play.google.com/store/apps/details?id=com.buyitltd.buyit"}]
        }
    ]
    
    return render_template('index.html', skills=skills, projects=projects)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
