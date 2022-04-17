import os
html = []
for root, dirs, files in os.walk(r"E:\Tiwombat\Tiwombat\CPGE", topdown=False):
   for name in files:
      if os.path.join(root, name).endswith(".html"):
          html.append(os.path.join(root, name))
   for name in dirs:
      if os.path.join(root, name).endswith(".html"):
          html.append(os.path.join(root, name))
          

navbar = """<style>
.main {
  font-family: 'Brush Script MT', cursive;
  text-align: center;
}

.navbar ul,li { 
  list-style-type: none;
  list-style-position:inside;
  margin:0;
  padding:0;
}

.navbar{
  display: inline-block;
  list-style-type: none;
  overflow: hidden;
  background-color: gray;
  border-radius: 10px;
  list-style-position: inside;
  text-align: center;
}

.navbar li{
  float: left;
  display:inline;
}

.navbar li a {
  display:inline-block;
  color: white;
  margin-left: 8px;
  margin-right: 8px;
  text-decoration: none;
  
}

.navbar li a:hover {
  border-radius: 10px;
  background-color: #111;
}
</style>

<div class="main">
	<h1 class="main">Wombat Never Die</h1>
	
	<div class="navbar">
		<ul>
			<li><a href="Accueil.html">Accueil</a></li>

			<li><a href="Presentation.html">Presentation</a></li>

			<li><a href="Physique.html">Physique</a></li>

			<li><a href="Chimie.html">Chimie</a></li>

			<li><a href="TP.html">TP</a></li>

			<li><a href="IC.html">IC</a></li>

			<li><a href="Devoirs.html">Devoirs</a></li>

			<li><a href="Colles.html">Colles</a></li>

			<li><a href="TIPE.html">TIPE</a></li>
		</ul>
	</div>
	
</div>"""

after = """<body style="background: rgb(101, 101, 101); margin: 0pt; " onload="onPageLoad();" onunload="onPageUnload();">"""

for page in html:
    with open(page, "r", encoding="utf8") as f:
        content = f.read()
        content = content.replace(after, after+"\n"+navbar)
        f.close()
    with open(page, "w", encoding="utf8") as f:
        f.write(content)
        f.close()
