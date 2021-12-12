from MainApp.models import Topic, Entry
import django
import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "learning_log.settings")


django.setup()


topics = Topic.objects.all()

for topic in topics:
    print(topic.id)
    print(topic.text)
    print(topic.date_added)

t = Topic.objects.get(id=1)
print(t)

entries = t.entry_set.all()

for e in entries:
    print(e)
