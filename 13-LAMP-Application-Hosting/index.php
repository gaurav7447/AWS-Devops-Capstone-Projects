<?php
echo "<!DOCTYPE html>
<html>
<head>
<title>LAMP Project</title>

<style>

body{
    margin:0;
    padding:0;
    font-family:Arial;
    background:linear-gradient(135deg,#141e30,#243b55);
    color:white;
    height:100vh;
    display:flex;
    justify-content:center;
    align-items:center;
}

.container{
    text-align:center;
    background:rgba(255,255,255,0.1);
    padding:50px;
    border-radius:20px;
    width:80%;
    max-width:700px;
}

h1{
    font-size:50px;
}

p{
    font-size:22px;
    line-height:1.6;
}

.badge{
    margin-top:20px;
    display:inline-block;
    background:#00ff99;
    color:black;
    padding:12px 25px;
    border-radius:30px;
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

<div class='container'>

<h1>🚀 LAMP Stack Project</h1>

<p>
Linux + Apache + MySQL + PHP successfully running on AWS EC2
</p>

<div class='badge'>
Deployment Successful ✅
</div>

<div class='cards'>
<div class='card'>Linux</div>
<div class='card'>Apache</div>
<div class='card'>MySQL</div>
<div class='card'>PHP</div>
<div class='card'>AWS EC2</div>
</div>

</div>

</body>
</html>";
?>