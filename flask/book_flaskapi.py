from flask import*
from sqlalchemy import create_engine

app=Flask(__name__)
app.config['DEBUG']=True

def db_connection():
    
    db_string="postgresql://postgres:Balagowtham11@localhost:5432/bookdetail"
    return create_engine(db_string)

@app.route('/',methods=['GET'])
def get_book():
    
    book_details=db.execute("SELECT * from bookstore.book;")
    formatted_book_details=[dict(row) for row in book_details]
    return jsonify(formatted_book_details)

@app.route('/insert',methods=['GET','POST'])
def insert_book():
    
    if request.method=='POST':
        
        book_name=request.form['book_name']
        price=request.form['book_price']
        aut_name=request.form['author_name']
    
        db.execute("insert into bookstore.book(book_name,book_price,author_name) values('{}','{}','{}');".format(book_name,price,aut_name))
        return "successfully inserted"

db=db_connection()
app.run()
