# Mars Data Aggregator

This project is a webapp built in Django intended to be an aggregator for information about the current Mar's
rover mission Perseverance as well as other general information about
Mars.

This app is targeted to be educational for students at a 5th grade level.
The app draws on various API's provided by nasa as well as RSS feeds provided
by both NASA and ScienceDaily. We have the following pages in
the app:

| Image                                            | About                                                                                                      |
|--------------------------------------------------|------------------------------------------------------------------------------------------------------------|
| ![Newsfeed](./static/images/mars-calendar.png)   | An RSS newsfeed displaying the latest information about Mars.                                              |
| ![Weather](./static/images/mars-weather.png)     | Data from Perseverance MEDA sensor about weather on Mars.                                                  |
| ![Calculator](./static/images/my-weight.png)     | A calculator to show your weight earth weight on Mars.                                                     |
| ![Simulation](./static/images/photo-gallery.png) | Images from Perseverance camera's shown alongside an embed of Perseverance's location for cross reference. |
| ![Photos](./static/images/rover-cam.png)         | A simulation embedded from NASA showing the landing of the Perseverance rover.                             |

# Development Environment

This project was created using Django and Python.

To run this project will require using the following libraries:

*[Feedparser](https://pypi.org/project/feedparser/)

*[Django Rest Framework](https://www.django-rest-framework.org/)

# Collaborators

Daniel Hernandez

Kayleigh Hansen

Joshua Gubler

Aaron Whittier

# Useful Websites

* [Django Docs](https://docs.djangoproject.com/en/3.2/)
* [Nasa Open Apis](https://api.nasa.gov/)

# Future Work

* Added multiple rover cameras
* Select image date
* Add other mars missions
