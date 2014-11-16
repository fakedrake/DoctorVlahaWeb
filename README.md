# Developer Notes

[ ![Codeship Status for fakedrake/DoctorVlahaWeb](https://codeship.com/projects/cd152d70-4ffc-0132-86b2-263393a504fa/status)](https://codeship.com/projects/47949)

To have the site with a sample database run:

	$ virtualenv --no-site-packages py
	$ . ./py/bin/activate
	$ python manage.py syncdb --all
	<Fill in with your local instance details>
	$ python manage.py migrate --fake

And then to run a local server

	$ python manage.py runserver

And you can see it in [localhost:8000](http://localhohst:8000).
