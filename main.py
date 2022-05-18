# Show time, weather and air quality app.
# Made with requests and tkinter.

from datetime import *
from tkinter import *
import threading, bs4, requests
import request_test

def showtime():
    # Create Label for clock.
    time_label = Label(root, bg='black', border=10, width=10, fg='white', text=datetime.now().strftime("%H:%M:%S"), font=('Arial', 50))

    # Display Label for clock.
    time_label.grid(row=0, column=0, columnspan=3, sticky='NSEW')
    # Refresh every 50 miliseconds.
    time_label.after(50,lambda : showtime())

def weather():
    global weat
    global atualizado

    try:
        weat = request_test.weat() # Save a tuple like (temperature, weather, quality_of_air, color_for_quality_of_air).
    except:
        print("Erro na conexão") # Connection error.
    else:
        atualizado = datetime.now().strftime("%H:%M:%S") # get Update time.

    # Create Label for weather.
    temper_label = Label(root, bg=weat[3], border=0, width=4, fg='black', text=weat[0], font=('Arial', 40))
    tempo_label = Label(root, bg=weat[3], border=8, width=0, fg='black', text=weat[1].replace('soalheiro','\n ensolarado'), font=('Arial', 20))
    titulo_label = Label(root, bg=weat[3], border=0, width=0, height=0, fg='black', text=f'Qualidade do ar:\n', font=('Arial', 13))
    quali_label = Label(root, bg=weat[3], border=0, width=0, height=0, fg='black', text=weat[2], font=('Arial', 18))
    atu_label = Label(root, bg=weat[3], border=0, width=0, height=0, fg='black', text=f'Atualizado em: {atualizado}', font=('Arial', 8))
    # Display Label for weather.
    temper_label.grid(row=1, column=0, rowspan=3, sticky='NSEW', ipadx=0)
    tempo_label.grid(row=1, column=1, rowspan=3, sticky='NSEW', ipadx=0)
    titulo_label.grid(row=1, column=2, sticky='NEW')
    quali_label.grid(row=2, column=2, sticky='NEW')
    atu_label.grid(row=3, column=2, sticky='NSEW')
    # Refresh every 15 seconds.
    quali_label.after(15000,lambda : weather())

# Set inicial values
weat = ('??°C', 'Indisponível', 'Desconhecido', 'white')
atualizado = 'Nunca'

# Create Object
root = Tk()
# Size
root.geometry("431x181")
# Title
root.title("Time and Weather")

# Create and start a new Thread to refresh time and weather independently
threadObj = threading.Thread(target=weather)
threadObj.start() # Start weather loop

showtime() # Start time loop

root.mainloop()




#
