from flask import Flask  

FAI=Flask(__name__)

@FAI.route('/wish')
def wish():
    return "Hello......."

@FAI.route('/radha')
def radha():
    return "Wellcome to Flask Page....."


if __name__=='__main__':
    FAI.run(debug=True)
