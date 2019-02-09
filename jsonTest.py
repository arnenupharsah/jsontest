import web
import json
import requests
### Url mappings

urls = (
    '/', 'Index',
    '/del/(\d+)', 'Delete'
)
### Templates
render = web.template.render('templates', base='base')


class Index:

    form = web.form.Form(
        web.form.Textbox('title', web.form.notnull, 
            description="I need to:"),
        web.form.Button('Add todo'),
    )


    def GET(self):
        with open('db.json') as json_file:  
            data = json.load(json_file)
        form = self.form()
        return render.index(data[u'todos'], form)
        

    def POST(self):
       
        form = self.form()
        with open('db.json') as json_file:  
            data = json.load(json_file)
        if not form.validates():
            return render.index(data, form)
        
        d2=data[u'todos']
        todos_len = len(d2)
        d1 = {'id':todos_len+1,'activity':form.d.title}
        d2.append(d1)
        d3={"todos":d2}
        with open('db.json', 'w') as outfile:
            json.dump(d3,outfile,indent=4)
        raise web.seeother('/')

class Delete:

    def byteify(self,input):
        if isinstance(input, dict):
            return dict([(self.byteify(key), self.byteify(value)) for key, value in input.iteritems()])
        elif isinstance(input, list):
            return [self.byteify(element) for element in input]
        elif isinstance(input, unicode):
            return input.encode('utf-8')
        else:
            return input
    
    def POST(self, id):
       
        id = int(id)
        with open('db.json') as json_file:  
            data = json.load(json_file)
        
        data=data[u'todos']
        for d in range(0,len(data)-1):
            if data[d][u'id']==id:
                del data[d]
                break

        d3={"todos":data}
        with open('db.json', 'w') as outfile:
            json.dump(d3,outfile,indent=4)
        raise web.seeother('/')

        


"""
 
                

    def POST(self):
        form = self.form()
        data = requests.get("https://my-json-server.typicode.com/arnenupharsah/jsondemo/todos")
        if not form.validates():
            return render.index(data, form)
        d1=data.json()
        todos_len = len(d1)
        d2 = {'id':todos_len +1,'activity':form.d.title}
        d1.append(d2)
        headers = {'Content-type':'application/json','Accept':'text/plain'}
        r=requests.post("https://my-json-server.typicode.com/arnenupharsah/jsondemo/todos",json = d1,headers=headers)
        return r

class Delete:
    
    def POST(self, id1):
       
        id1 = int(id1)
        payload = {'id':1}
        res = requests.delete("https://my-json-server.typicode.com/arnenupharsah/jsondemo/todos/1")
        return res
        


    def POST(self):
        form = self.form()
        data = requests.get("https://my-json-server.typicode.com/arnenupharsah/jsondemo/todos")
        if not form.validates():
            return render.index(data, form)
        todos_len = len(data)
        d1 = {"id":str(todos_len+1),"activity":form.d.title}
        response = requests.post('https://my-json-server.typicode.com/arnenupharsah/jsondemo/todos', data) 
        raise web.seeother('/')

    def GET(self):
    
        response = requests.get("https://my-json-server.typicode.com/arnenupharsah/jsondemo/todos")
        form = self.form()        
        return render.index(response, form)


    def POST(self):
       
        form = self.form()
        with open('db.json') as json_file:  
            data = json.load(json_file)
        if not form.validates():
            return render.index(data, form)
        
        d2=data[u'todos']
        todos_len = len(d2)
        d1 = {'id':str(todos_len+1),'activity':form.d.title}
        d2.append(d1)
        d3={"todos":d2}
        with open('db.json', 'w') as outfile:
            json.dump(d3,outfile,indent=4)
        raise web.seeother('/')
"""

app = web.application(urls, globals())

if __name__ == '__main__':
    app.run()
