from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = 'chave_secreta_para_session'

@app.route('/')
def escolher_animal():
    session.clear()
    return render_template('index.html', animal=None, exame=None)

@app.route('/escolher-exame/<animal>')
def escolher_exame(animal):
    session['animal'] = animal
    return render_template('index.html', animal=animal, exame=None)

@app.route('/exame/<exame_tipo>', methods=['GET', 'POST'])
def exame(exame_tipo):
    animal = session.get('animal')
    mensagem = None
    refazer = False

    if not animal:
        return redirect(url_for('escolher_animal'))

    if request.method == 'POST':
        resultados = []

        try:
            if exame_tipo == 'eritrograma':
                eritr = float(request.form['eritr'])
                hgb = float(request.form['hgb'])
                hct = float(request.form['hct'])
                vcm = float(request.form['vcm'])
                chcm = float(request.form['chcm'])
                plaq = float(request.form['plaq'])

                if animal == 'gato':
                    
                    if eritr < 5:
                        resultados.append("Eritrócitos: Eita! Está Baixo – Sinal de anemia, seu pet pode ficar mais cansado, fraco ou apático.")
                    elif eritr <= 10:
                        resultados.append("Eritrócitos: Ufa! Seu pet está bem nesse parâmetro.")
                    else:
                        resultados.append("Eritrócitos: Eita! Está alto – Possível desidratação ou policitemia.")

                    if hgb < 8:
                        resultados.append("Hemoglobina: Eita! Está Baixa – Possível anemia.")
                    elif hgb <= 15:
                        resultados.append("Hemoglobina: Ufa! Seu pet está bem nesse parâmetro.")
                    else:
                        resultados.append("Hemoglobina: Eita! Está Alta – Investigar causas, sinal de condição subjacente")

                    # Hematócrito
                    if hct < 24:
                        resultados.append("Hematócrito: Eita! Está Baixo – possível anemia.")
                    elif hct <= 45:
                        resultados.append("Hematócrito: Ufa! Seu pet está bem nesse parâmetro.")
                    else:
                        resultados.append("Hematócrito: Eita! Está Alto – Possível desidratação.")

                    # VCM
                    if vcm < 39:
                        resultados.append("VCM: Eita! Está Baixo - Hemácias maiores que o normal, anemia macrocítica")
                    elif 39==vcm<=55:
                        resultados.append("VCM: Ufa! Seu pet está bem nesse parâmetro.")
                    else:
                        resultados.append("VCM: Eita! Está Alto - Hemácias menores que o normal, anemia microcítica, deficiência de ferro.")

                    # CHCM
                    if chcm < 31:
                        resultados.append("CHCM: Eita! Está Baixa – Possível hipocromia.")
                    elif chcm <= 35:
                        resultados.append("CHCM: Ufa! Seu pet está bem nesse parâmetro.")
                    else:
                        resultados.append("CHCM: Eita! Está Alta – Possível hipercromia.")

                    if plaq<300000:
                        resultados.append("Plaquetas: Eita! Está Baixa - Pode indicar dificuldade para estancar sangramentos e mais suscetíel a hematomas e doenças secundárias.")
                    elif plaq<=800000:
                        resultados.append("Plaquetas: Ufa! Seu pet está bem nesse parâmetro.")
                    else:
                        resultados.append("Plaquetas: Eita! Está Alta - O corpo está reagindo a algum processo inflamatório, infecciológico ou parasitário.")

                elif animal == 'cachorro':
                    if eritr < 5.5:
                        resultados.append("Eritrócitos: Eita! Está Baixo - Possível anemia.")
                    elif eritr <= 8.5:
                        resultados.append("Eritrócitos: Ufa! Seu pet está bem nesse parâmetro.")
                    else:
                        resultados.append("Eritrócitos: Eita! Está Alta - Possível policitemia ou desidratação.")

                    if hgb < 12:
                        resultados.append("Hemoglobina: Eita! Está Baixo - Possível anemia.")
                    elif hgb <= 18:
                        resultados.append("Hemoglobina: Ufa! Seu pet está bem nesse parâmetro.")
                    else:
                        resultados.append("Hemoglobina: Eita! Está Alta - Investigar causas, sinal de condição subjacente.")

                    if hct < 37:
                        resultados.append("Hematócrito: Eita! Está Baixo – Possível anemia.")
                    elif hct <= 55:
                        resultados.append("Hematócrito: Ufa! Seu pet está bem nesse parâmetro.")
                    else:
                        resultados.append("Hematócrito: Eita! Está Alto – Possível desidratação.")

                    if vcm < 60:
                        resultados.append("VCM: Eita! Está Baixo – Hemácias maiores que o normal, anemia macrocítica")
                    elif vcm <= 77:
                        resultados.append("VCM: Ufa! Seu pet está bem nesse parâmetro.")
                    else:
                        resultados.append("VCM: Eita! Está Alto – Hemácias menores que o normal, anemia microcítica, deficiência de ferro. ")

                    if chcm < 32:
                        resultados.append("CHCM: Eita! Está Baixa – Possível hipocromia.")
                    elif chcm <= 36:
                        resultados.append("CHCM: Ufa! Seu pet está bem nesse parâmetro.")
                    else:
                        resultados.append("CHCM: Eita! Está Alta – Possível hipercromia.")

                    if plaq<200000:
                        resultados.append("Plaquetas: Eita! Está Baixa - Pode indicar dificuldade para estancar sangramentos e mais suscetível a hematomas e doenças secundárias.")
                    elif plaq<=500000:
                        resultados.append("Plaquetas: Ufa! Seu pet está bem nesse parâmetro.")
                    else:
                        resultados.append("Plaquetas: Eita! Está Alta - O corpo está reagindo a algum processo inflamatório, infecciológico ou parasitário.")


            elif exame_tipo == 'leucograma':
                leuco = float(request.form['leucocitos'])
                seg = float(request.form['segmentados'])
                bast = float(request.form['bastonetes'])
                linf = float(request.form['linfocitos'])
                mono = float(request.form['monocitos'])
                eos = float(request.form['eosinofilos'])
                baso = float(request.form['basofilos'])

                if animal == 'gato':
                    if leuco < 5500:
                        resultados.append("Leucócitos totais: Eita! Está Baixo – Possível imunossupressão.")
                    elif leuco <= 19500:
                        resultados.append("Leucócitos totais: Ufa! Seu pet está bem nesse parâmetro.")
                    else:
                        resultados.append("Leucócitos totais: Eita! Está alto – Possível infecção ou inflamação.")

                    if seg < 2500:
                        resultados.append("Segmentados: Eita! Está Baixo – Poucas células de defesa no sangue.")
                    elif seg <= 12500:
                        resultados.append("Segmentados: Ufa! Seu pet está bem nesse parâmetro.")
                    else:
                        resultados.append("Segmentados: Eita! Está alto – Possível infecção bacteriana.")


                    if bast > 300:
                        resultados.append("Bastonetes: Eita! Esta alto – Possível infecção aguda (desvio à esquerda).")
                    elif bast<=300:
                        resultados.append("Bastonetes: Ufa! Seu pet está bem nesse parâmetro..")

                    if linf < 1500:
                        resultados.append("Linfócitos: Eita! Está Baixo – Possível estresse ou infecção viral.")
                    elif linf <= 7000:
                        resultados.append("Linfócitos: Ufa! Seu pet está bem nesse parâmetro.")
                    else:
                        resultados.append("Linfócitos: Eita! Está Alto – Possível infecção crônica ou linfocitose.")

                    if mono<=850:
                        resultados.append("Monócitos: Ufa! Seu pet está bem nesse parâmetro.")

                    elif mono>850:
                        resultados.append("Monócitos: Eita! Está Alto – Possível inflamação crônica ou infecção.")

                    if eos<=1500:
                        resultados.append("Eosinófilos: Ufa! Seu pet está bem nesse parâmetro.")

                    elif eos>1500:
                        resultados.append("Eosinófilos: Eita! Está Alto - Possível alergia ou parasitose.")

                    if baso<=170:
                        resultados.append("Basófilos: Ufa! Seu pet está bem nesse parâmetro.")
                    
                    if baso>170:
                        resultados.append("Basófilos: Eita! Está Alto - Possível reação alérgica ou parasitose.")

                elif animal == 'cachorro':
                    if leuco < 6.0:
                        resultados.append("Leucócitos totais: Eita! Está Baixo – Possível imunossupressão.")
                    elif leuco <= 17.0:
                        resultados.append("Leucócitos totais: Ufa! Seu pet está bem nesse parâmetro.")
                    else:
                        resultados.append("Leucócitos totais: Eita! Está Alto – Possível infecção ou inflamação.")

                    if seg < 3000:
                        resultados.append("Segmentados: Eita! Está baixo – Poucas células de defesa no sangue.")
                    elif seg <= 11500:
                        resultados.append("Segmentados: Ufa! Seu pet está bem nesse parâmetro.")
                    else:
                        resultados.append("Segmentados: Eita! Está Alto – Possível infecção bacteriana aguda.")

                    if bast > 300:
                        resultados.append("Bastonetes: Eita! Está Alto – Desvio à esquerda (infecção aguda).")
                    elif bast<=300:
                        resultados.append("Bastonetes: Ufa! Seu pet está bem nesse parâmetro.")

                    if linf < 1000:
                        resultados.append("Linfócitos: Eita! Está Baixo – Possível estresse.")
                    elif linf <= 4800:
                        resultados.append("Linfócitos: Ufa! Seu pet está bem nesse parâmetro.")
                    else:
                        resultados.append("Linfócitos: Eita! Está Alto – Possível infecção crônica.")

                    if mono<=1350:
                        resultados.append("Monócitos: Ufa! Seu pet está bem nesse parâmetro.")

                    elif mono > 1350:
                        resultados.append("Monócitos: Eita! Está Alto– Possível inflamação crônica ou infecção.")

                    if eos<100:
                        resultados.append("Eosinófilos: Eita! Está Baixo - Não é algo preocupante isoladamente.")

                    elif eos<=1250:
                        resultados.append("Eosinófilos: Ufa! Seu pet está bem nesse parâmetro.")

                    elif eos>1250:
                        resultados.append("Eosinófilos: Eita! Está Alto – Possível alergia ou parasitose.")

                    if baso > 1:
                        resultados.append("Basófilos:  Eita! Está Alto – Possível alergia ou distúrbio inflamatório.")
            
            elif exame_tipo == 'bioquimico':
                ureia = float(request.form['ureia'])
                creatinina = float(request.form['creatinina'])
                alt = float(request.form['alt'])
                albumina = float(request.form['albumina'])

                if animal == 'gato':
                    # Ureia
                    if ureia < 40:
                        resultados.append("Ureia: Eita! Está Baixa! – Possível disfunção hepática ou desnutrição.")
                    elif ureia <= 80:
                        resultados.append("Ureia: Ufa! Seu pet está bem nesse parâmetro.")
                    else:
                        resultados.append("Ureia: Eita! Está Alta – Possível insuficiência renal.")

                    # Creatinina
                    if creatinina < 0.8:
                        resultados.append("Creatinina: Eita! Está Baixa – Pouco comum, avaliar função hepática.")
                    elif creatinina <= 2.4:
                        resultados.append("Creatinina: Ufa! Seu pet está bem nesse parâmetro.")
                    else:
                        resultados.append("Creatinina: Eita! Está Alta – Possível doença renal.")

                    # ALT
                    if alt < 25:
                        resultados.append("ALT: Eita! Está Baixa – Normalmente sem relevância clínica.")
                    elif alt <= 97:
                        resultados.append("ALT: Ufa! Seu pet está bem nesse parâmetro.")
                    else:
                        resultados.append("ALT: Eita! Está Alta – Possível lesão hepática.")

                    # Albumina
                    if albumina < 2.2:
                        resultados.append("Albumina: Eita! Está Baixa – Possível insuficiência hepática ou perda proteica.")
                    elif albumina <= 3.9:
                        resultados.append("Albumina: Ufa! Seu pet está bem nesse parâmetro.")
                    else:
                        resultados.append("Albumina: Eita! Está alta - Possível desidratação.")

                elif animal == 'cachorro':
                    # Ureia
                    if ureia < 20:
                        resultados.append("Ureia: Eita! Está Baixa – Possível disfunção hepática.")
                    elif ureia <= 60:
                        resultados.append("Ureia: Ufa! Seu pet está bem nesse parâmetro.")
                    else:
                        resultados.append("Ureia: Eita! Está alta - Possível insuficiência renal.")

                    # Creatinina
                    if creatinina < 0.5:
                        resultados.append("Creatinina: Eita! Está Baixa – Avaliar contexto clínico.")
                    elif creatinina <= 1.8:
                        resultados.append("Creatinina: Ufa! Seu pet está bem nesse parâmetro.")
                    else:
                        resultados.append("Creatinina: Eita! Está alta - Possível doença renal.")

                    # ALT
                    if alt < 10:
                        resultados.append("ALT: Eita! Está Baixa – Geralmente sem importância clínica.")
                    elif alt <= 118:
                        resultados.append("ALT: Ufa! Seu pet está bem nesse parâmetro.")
                    else:
                        resultados.append("ALT: Eita! Está alta - Possível lesão hepática.")

                    # Albumina
                    if albumina < 2.6:
                        resultados.append("Albumina: Eita! Está Baixa – Possível hepatopatia ou enteropatia.")
                    elif albumina <= 4.0:
                        resultados.append("Albumina: Ufa! Seu pet está bem nesse parâmetro.")
                    else:
                        resultados.append("Albumina: Eita! Está alta - Possível desidratação.")

            mensagem = "<br><br>".join(resultados)
            refazer = True

        except ValueError:
            mensagem = "Por favor, insira apenas números válidos."

    return render_template('index.html', animal=animal, exame=exame_tipo, mensagem=mensagem, refazer=refazer)

if __name__ == '__main__':
    app.run(debug=True)