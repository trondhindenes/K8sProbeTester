from k8sprobetester import app

if __name__ == '__main__':
    app.run(threaded=True,
            host='0.0.0.0',
            debug=False,
            port=18000)