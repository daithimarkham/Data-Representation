#!flask/bin/python
from flask import Flask, jsonify,  request, abort, make_response

app = Flask(__name__,
            static_url_path='', 
            static_folder='../')

# Save all cars. Make an ARRAY (list) for storing the cars.
cars = [
    {
        "reg":"181 G 1234",
        "make":"Ford",
        "model":"Modeo",
        "price":18000
    },
    {
        "reg":"11 MO 1234",
        "make":"Nissan",
        "model":"Almera",
        "price":8000
    },
    {
        "reg":"test",
        "make":"Nissan",
        "model":"Almera",
        "price":8000
    }
]

# Route for GET cars
@app.route('/cars', methods=['GET']) # gets requests
def get_cars(): # from cars array 
    return jsonify( {'cars':cars}) # puts doubles quotes around list, looks nice etc.

# curl -i http://localhost:5000/cars

# Route for GET Reg.
@app.route('/cars/<string:reg>', methods =['GET']) 
def get_car(reg):
    foundCars = list(filter(lambda t : t['reg'] == reg , cars)) # returns only cars where reg matches.
    if len(foundCars) == 0: # if nothing is returned
        return jsonify( { 'car' : '' }),204 # send back an empty car with status 204
    return jsonify( { 'car' : foundCars[0] }) # otherwise send back first of cars found.

#curl -i http://localhost:5000/cars/test

# CREATE route, method POST.
@app.route('/cars', methods=['POST'])
def create_car():
    if not request.json: # checks request has json data
        abort(400) # if not, return error.
    if not 'reg' in request.json:
        abort(400) # if not, return 400 abort error.
    car={  # read the request object and create new car.
        "reg":  request.json['reg'],
        "make": request.json['make'],
        "model":request.json['model'],
        "price":request.json['price']
    }
    cars.append(car) # append to list of cars. 
    return jsonify( {'car':car }),201 # returns what we just added.

# sample test
# curl -i -H "Content-Type:application/json" -X POST -d '{"reg":"12 D 1234","make":"Fiat","model":"Punto","price":3000}' http://localhost:5000/cars
# for windows use this one
# curl -i -H "Content-Type:application/json" -X POST -d "{\"reg\":\"12 D 1234\",\"make\":\"Fiat\",\"model\":\"Punto\",\"price\":3000}" http://localhost:5000/cars

# UPDATE route.
@app.route('/cars/<string:reg>', methods =['PUT']) # if method is put, we call this function
def update_car(reg): # reg is passed in, (string after cars)
    foundCars=list(filter(lambda t : t['reg'] ==reg, cars)) # make an array of found cars.
    if len(foundCars) == 0:
        abort(404)
    if not request.json:
        abort(400)
    if 'make' in request.json and type(request.json['make']) != str:
        abort(400)
    if 'model' in request.json and type(request.json['model']) is not str:
        abort(400)
    if 'price' in request.json and type(request.json['price']) is not int:
        abort(400)
    foundCars[0]['make']  = request.json.get('make', foundCars[0]['make'])
    foundCars[0]['model'] =request.json.get('model', foundCars[0]['model'])
    foundCars[0]['price'] =request.json.get('price', foundCars[0]['price'])
    return jsonify( {'car':foundCars[0]})

#curl -i -H "Content-Type:application/json" -X PUT -d '{"make":"Fiesta"}' http://localhost:5000/cars/181%20G%201234
# for windows use this one
#curl -i -H "Content-Type:application/json" -X PUT -d "{\"make\":\"Fiesta\"}" http://localhost:5000/cars/181%20G%201234

# DELETE route
@app.route('/cars/<string:reg>', methods =['DELETE'])
def delete_car(reg):
    foundCars = list(filter (lambda t : t['reg'] == reg, cars))
    if len(foundCars) == 0:
        abort(404)
    cars.remove(foundCars[0]) # remove car from list of cars
    return  jsonify( { 'result':True }) # return json if true

# Error handler routes, good for production, but for us could comments these out, when debugging code.
# Returns simple JSON
@app.errorhandler(404)
def not_found404(error):
    return make_response( jsonify( {'error':'Not found' }), 404)

@app.errorhandler(400)
def not_found400(error):
    return make_response( jsonify( {'error':'Bad Request' }), 400)


if __name__ == '__main__' :
    app.run(debug= True) 