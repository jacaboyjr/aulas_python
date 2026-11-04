"""
Se estiver chovendo, você leva o guarda-chuva. 
Se não estiver chovendo, você não leva. 
Mas se não estiver chovendo, porém estiver nublado, você leva o guarda-chuva mesmo assim!

"""
chovendo = True
nublado = True


if chovendo == True:
    print("Deve levar o guarda-chuva pois está chovendo")

if chovendo == False:
    if nublado == True: 
        print("Tempo Nublado levar o guarda-chuva")
    else:
        print("Não está chovendo e não está nublado, não precisa levar o guarda-chuva")
