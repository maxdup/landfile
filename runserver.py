from landfile import create_app
landfile = create_app('config')
landfile.run(host='0.0.0.0')
