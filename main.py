from website import create_app 
## able to call function inside module bc in __init__.py file 

app=create_app()

if __name__=='__main__':
    app.run(debug=True)