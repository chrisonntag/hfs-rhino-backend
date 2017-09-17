# rhino-backend

API for the 'Rhino Insurcance' app built with Flask.

## Routes

```
/               GET     information about Rhino API
/rhino/update   POST    requires latitude and longitude as form data fields
```
## Install
Just rename ```my.cnf.sample``` to ```my.cnf``` and insert your API credentials. Then run

```bash
python main.py 
```

to start the flask development server.
