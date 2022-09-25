
# Пример использования Event - 2

from threading import Event, Thread
from time import sleep


def task(event, timeout):
    print("Started thread but waiting for event...")
    # make the thread wait for event with timeout set
    event_set = event.wait(timeout)
    if event_set:
        print("Event received, releasing thread...")
    else:
        print("Time out, moving ahead without event...")


def reminder_function(event):
    print("reminder_function is started...")
    while True:
        event.wait()
        print("Running reminder_function thread...")
        sleep(1)


if __name__ == '__main__':
    # Initializing <event> object
    event_obj = Event()

    # Starting the thread
    Thread(target=reminder_function, args=(event_obj, 2,), name='Event-Blocking-Thread', daemon=True).start()

    # Sleeping <main> thread for 3 seconds
    print('Waiting for Main Thread 3 seconds...')
    sleep(3)

    # Generating the event
    print("Event is set.")
    event_obj.set()
    sleep(3)
    event_obj.clear()
    print("Event is clear")
    sleep(3)
    print("End of main")
