import web
import json
import csv
render=web.template.render('views/')
urls=(
    '/index','index',
    '/informacion(.*)','informacion',
    '/registros(.*)','registros'
    )

class index:
    def GET(self):
        return render.index()
class informacion:
    def GET(self,nombre):
        nombre='Francisco Javier Heredia Tellez'
        return render.informacion(nombre)
class registros:
    def GET(self,datos):
        data_list=[]
        with open('Datos.csv','r') as file_open:
            data=csv.reader(file_open, delimiter=',')
            for row in data:
                data_list.append(row)
        datos=data_list
        return render.registros(datos)
        
if __name__=='__main__':
    app=web.application(urls, globals())
    web.config.debug=True
    app.run()