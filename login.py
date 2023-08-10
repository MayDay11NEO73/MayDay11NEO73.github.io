from flask import Flask, request, redirect
app = Flask(__name__)
@app.route('/', methods=['POST'])
def submit_form():
    password = request.form.get('password')
    user = request.form.get('user')
    if password == '89766817' and user == 'md11neo':
        return redirect('account-error.html')
    else:
        return redirect('manager.html')
    if __name__ == '__main__':
        app.run()
    
    
