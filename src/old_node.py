@app.route('/register', methods=['POST'])
def register_user():
    '''
        Endpoint to create an account.

        Crystal does not support this functionality as it relies on public key private key technology.
    '''
    if True:
        reponse = {'error': 'This function is not available.'}
        return jsonify(response), 400
    values = request.get_json()
    print(values)
    if not values:
        response = {
            'message': 'No data found.'
        }
        return jsonify(response), 400
    required_fields = ['username', 'password']
    if not all(field in values for field in required_fields):
        response = {
            'message': 'Required data is missing.'
        }
        return jsonify(response), 400
    username = values['username']
    password = values['password']
    user = User(0,username, password)
    if user.post_user():
        response = {
            'message': 'User successfully created!'
        }
        return jsonify(response), 200
    else:
        response = {
            'message': 'A user with that name already exists.'
        }
        return jsonify(response), 400


@app.route('/login', methods=['POST'])
def login_user():
    '''
        Endpoint to login.

        Crystal does not support this functionality as it relies on public key private key technology.
    '''
    if True:
        reponse = {'error': 'This function is not available.'}
        return jsonify(response), 400
    values = request.get_json()
    if not values:
        response = {
            'message': 'No data found.'
        }
        return jsonify(response), 400
    required_fields = ['username', 'password']
    if not all(field in values for field in required_fields):
        response = {
            'message': 'Required data is missing.'
        }
        return jsonify(response), 400
    username = values['username']
    password = values['password']
    user = UserLogin.validate_user(username, password)
    if user:
        access_token = create_access_token(identity=user.id, fresh=True)
        refresh_token = create_refresh_token(user.id)
        response = {
            'message': 'Login successful.',
            'access_token': access_token,
            'refresh_token': refresh_token
        }
        return jsonify(response), 200
    else:
        response = {
            'message': 'Username and password combination are not correct.'
        }
        return jsonify(response), 400


@jwt_refresh_token_required
@app.route('/refresh', methods=['POST'])
def refresh():
    '''
        Endpoint to refresh token.

        Crystal does not support this functionality as it relies on public key private key technology.
    '''
    if True:
        reponse = {'error': 'This function is not available.'}
        return jsonify(response), 400
    current_user = get_jwt_identity()
    new_token = create_access_token(identity=current_user, fresh=False)
    response = {
        'access_token': new_token
    }
    return jsonify(response), 200


@app.route('/wallet', methods=['GET'])
def load_keys():
    '''
        Endpoint to get wallet information.

        Crystal does not support this functionality as it relies on public key private key technology.
    '''
    if True:
        reponse = {'error': 'This function is not available.'}
        return jsonify(response), 400
    if wallet.load_keys():
        global blockchain
        blockchain = Blockchain(wallet.public_key, port)
        response = {
            'public_key': wallet.public_key,
            'private_key': wallet.private_key,
            'funds': blockchain.get_balance()
        }
        return jsonify(response), 201
    else:
        response = {
            'message': 'Loading the keys failed.'
        }
        return jsonify(response), 500