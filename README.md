# Developer Notes

To have the site with a sample database run:

	$ virtualenv --no-site-packages py
	$ . ./py/bin/activate
	$ python manage.py syncdb --all
	<Fill in with your local instance details>
	$ python manage.py migrate --fake

And then to run a local server

	$ python manage.py runserver

And you can see it in [localhost:8000](http://localhohst:8000).
