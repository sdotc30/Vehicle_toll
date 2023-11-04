import tkinter as tk
from tkinter import messagebox

MAX_QUEUE_SIZE = 10

class Vehicle:
    def __init__(self, vehicle_number):
        self.vehicleNumber = vehicle_number

class Queue:
    def __init__(self):
        self.data = [None] * MAX_QUEUE_SIZE
        self.front = -1
        self.rear = -1

def initialize_queue():
    toll_queue.front = -1
    toll_queue.rear = -1

def is_queue_empty():
    return toll_queue.front == -1

def is_queue_full():
    return (toll_queue.rear + 1) % MAX_QUEUE_SIZE == toll_queue.front

def enqueue(vehicle):
    global toll_queue
    if is_queue_full():
        messagebox.showinfo("Error", "Queue is full. Cannot enqueue.")
    else:
        if is_queue_empty():
            toll_queue.front = 0
        toll_queue.rear = (toll_queue.rear + 1) % MAX_QUEUE_SIZE
        toll_queue.data[toll_queue.rear] = vehicle
        messagebox.showinfo("Enqueue", "Vehicle {} enqueued.".format(vehicle.vehicleNumber))

def dequeue():
    global toll_queue
    if is_queue_empty():
        messagebox.showinfo("Error", "Queue is empty. Cannot dequeue.")
        removed_vehicle = Vehicle(-1)
    else:
        removed_vehicle = toll_queue.data[toll_queue.front]
        if toll_queue.front == toll_queue.rear:
            toll_queue.front = -1
            toll_queue.rear = -1
        else:
            toll_queue.front = (toll_queue.front + 1) % MAX_QUEUE_SIZE
        messagebox.showinfo("Dequeue", "Vehicle {} dequeued.".format(removed_vehicle.vehicleNumber))
    return removed_vehicle

def enqueue_callback(entry):
    new_vehicle = Vehicle(int(entry))
    enqueue(new_vehicle)

def dequeue_callback(data):
    dequeue()

def display_callback():
    global toll_queue
    if is_queue_empty():
        messagebox.showinfo("Queue Data", "Queue is empty.")
    else:
        queue_text = "Vehicles in the queue: "
        for i in range(toll_queue.front, (toll_queue.rear + 1) % MAX_QUEUE_SIZE):
            queue_text += "{} ".format(toll_queue.data[i].vehicleNumber)
        messagebox.showinfo("Queue Data", queue_text)

toll_queue = Queue()
initialize_queue()

# Create the GUI window
window = tk.Tk()
window.title("Toll Tax Bridge Queue")

# Create and configure widgets
entry_label = tk.Label(window, text="Enter Vehicle Number:")
entry_label.grid(row=0, column=0)

entry = tk.Entry(window)
entry.grid(row=0, column=1)

enqueue_button = tk.Button(window, text="Enqueue", command=lambda: enqueue_callback(entry.get()))
enqueue_button.grid(row=1, column=0)

dequeue_button = tk.Button(window, text="Dequeue", command=dequeue_callback)
dequeue_button.grid(row=1, column=1)

display_button = tk.Button(window, text="Display Queue", command=display_callback)
display_button.grid(row=2, column=0, columnspan=2)

# Run the GUI
window.mainloop()
