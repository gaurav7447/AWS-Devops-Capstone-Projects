const express = require('express');

const app = express();

const PORT = 4000;

app.get('/', (req, res) => {

    res.send(`
    
    <!DOCTYPE html>
    <html>

    <head>
        <title>AWS ECS Node App</title>

        <style>

            body{
                margin:0;
                padding:0;
                font-family: Arial, sans-serif;
                background: linear-gradient(135deg, #141e30, #243b55);
                height:100vh;
                display:flex;
                justify-content:center;
                align-items:center;
                color:white;
            }

            .container{
                text-align:center;
                background: rgba(255,255,255,0.1);
                padding:40px;
                border-radius:20px;
                width:80%;
                max-width:700px;
                box-shadow:0 8px 32px rgba(0,0,0,0.3);
            }

            h1{
                font-size:50px;
                margin-bottom:20px;
            }

            p{
                font-size:22px;
                line-height:1.6;
            }

            .btn{
                margin-top:25px;
                display:inline-block;
                padding:12px 25px;
                background:#00ff99;
                color:black;
                border-radius:30px;
                text-decoration:none;
                font-weight:bold;
            }

            .cards{
                margin-top:30px;
                display:flex;
                justify-content:center;
                gap:15px;
                flex-wrap:wrap;
            }

            .card{
                background:white;
                color:black;
                padding:15px 20px;
                border-radius:10px;
                font-weight:bold;
            }

        </style>

    </head>

    <body>

        <div class="container">

            <h1>🚀 AWS ECS Project</h1>

            <p>
                Containerized Node.js Application Running Successfully on AWS ECS Fargate
            </p>

            <a class="btn">Deployment Successful ✅</a>

            <div class="cards">
                <div class="card">Node.js</div>
                <div class="card">Docker</div>
                <div class="card">AWS ECR</div>
                <div class="card">AWS ECS</div>
            </div>

        </div>

    </body>

    </html>

    `);

});

app.listen(PORT, () => {
    console.log(`Server running on port ${PORT}`);
});
