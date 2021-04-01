from event import Event
import mongoengine as db

print("connecting...")
def mongo_setup():
    CON_URI = "mongodb+srv://admin:databaseprojectadmin@databaseproject.xy2o1.mongodb.net/event_scheduler"
    db.connect(host=CON_URI)


def create_event(name, date, time, length, location, guests):

    event = Event()
    event.name = name
    event.event_date = date
    event.event_time = time
    event.length = int(length)
    event.location = location
    event.guests = guests.split(", ")
    event.save()


def get_events():
    for event in Event.objects:
        print(event.name, " / ", event.location, " / ", event.event_time)
        print


mongo_setup()
get_events()