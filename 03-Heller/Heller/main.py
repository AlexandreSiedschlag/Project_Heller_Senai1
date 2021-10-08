from Website import create_app


app = create_app()

if __name__ == '__main__': #faz com que o programa seja executado somente se ele realmente for executado.
    app.run(debug=True)    #Se for importado nao será executado.








