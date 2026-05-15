from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <html>
    <head>
        <title>Flask AWS Deployment</title>
    </head>
    <body style="font-family:Arial; text-align:center; margin-top:50px;">
        <h1>🚀 Flask App Deployed on AWS ECS</h1>
        
        <div style="border:1px solid #ccc; padding:20px; width:60%; margin:auto;">
            <h2>Deployment Details</h2>
            <p><b>Status:</b> ✅ Running Successfully</p>
            <p><b>Container:</b> Docker</p>
            <p><b>Cloud:</b> AWS ECS Fargate</p>
            <p><b>Registry:</b> ECR</p>
            <p><b>Region:</b> ap-south-1 (Mumbai)</p>
        </div>

        <br>
        <h3>🎯 DevOps Pipeline Project Completed</h3>
    </body>
    </html>
    """
    
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)