from flask import Flask, jsonify, render_template

app = Flask(__name__)

@app.route("/")
def  inicio():
  return render_template("index.html")

@app.route("/<conselho>")
def correspondencia(conselho):
  lista_conselhos = ["If you do something bad, make sure there’s someone else around to blame.", 
"Don’t follow what you think is the right way; make your way to what you think is happiness.", 
"Never break two laws at the same time because that’s how you get caught.", 
"If you can’t blind them with your brilliance, baffle them with your bullshit.", 
"If you sleep until lunchtime, you can save your breakfast money.", 
"Respect trans people and consume the rich. ", 
"Be happy.", 
"Be healthy.", 
"Sleep well.", 
"The definition of home is not where you are from, but where you are wanted.", 
"Just because you are trash doesn't mean you can't do great things. It's called garbage can, not garbage cannot", 
":)",
"Never be mean to doggys",
"Don't kill.",
"Never trust a man named Carlos who offers you marijuana at a convenience store's parking lot in the middle of the night while you are looking for your runaway dog, Spike."]

  lista_numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
  
  con = int(conselho)

  for i in lista_numeros:
    if i == con:
      cons = lista_conselhos[lista_numeros.index(i)]
      break
    else:
      cons = "keep an eye out for more news, possibly"
  
  return jsonify({conselho : cons})

app.run(host="0.0.0.0")
