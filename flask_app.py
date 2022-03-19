from flask import Flask 
from flask import jsonify,request

app =  Flask(__name__)

contacts = [{
    'Id'  : 1,
    'Contact' : 9672043291,
    'Name' : 'Mohit',
    'Done' : False
} , {
    'Id'  : 2,
    'Contact' : 9672052433,
    'Name' : 'Rahul',
    'Done' : False
}]

@app.route('/add_data' , methods = ['Post'])

def add_task() :
    if not request.json : 

        return jsonify({
            'status' : 'error' , 
            'message' : 'Action Intruppted.., Please  provide the data'
        },400)

    temp_contacts =  {
        'Id' : contacts[-1]['id'] + 1,
        'Contact' : request.json.get['Contact'],
        'Name' : request.json['Name'],
        'done' :  False
    }
    
    contacts.append(temp_contacts)

    return jsonify({
        'status' : 'Success!!',
        'message' : 'The task has been done'
    })

@app.route('/get_contacts')
def display() :
    return jsonify({
        'data' : contacts
    })

if __name__ == '__main__' : 
    app.run(debug = True)
