# # # import itertools

# # # a = [[10, 20], [30, 40], [50]]
# # # for j in (itertools.chain.from_iterable(a)):
# # #     print(j)
    
# # # print(list(itertools.chain.from_iterable(a)))
# # # import tkinter as tk
# # # # Create instance
# # # parent = tk.Tk()
# # # # Add a title
# # # parent.title("-Welcome to Python tkinter Basic exercises-")
# # # parent.geometry('600x300')
# # # #parent.resizable(0,0)
# # # #my_label = tk.Label(parent, text="Label widget")
# # # #my_label.grid(column=0, row=0)
# # # my_label = tk.Label(parent, text="Hello I am Amarendra", font=("Arial Bold", 70))
# # # my_label.grid(column=1, row=1)
# # # # Start GUI
# # # parent.mainloop()
# # # import tkinter as tk 
# # # parent = tk.Tk() 
# # # parent.title('Title - button') 
# # # my_button = tk.Button(parent, text='Quit', height=1, width=35, command=parent.destroy) 
# # # my_button.pack() 
# # # parent.mainloop()
# # # import tkinter as tk 
# # # parent = tk.Tk() 

# # # canvas_width = 100
# # # canvas_height = 80
# # # w = tk.Canvas(parent, 
# # #            width=canvas_width,
# # #            height=canvas_height)
# # # w.pack()

# # # y = int(canvas_height / 2)
# # # w.create_line(0, y, canvas_width, y, fill="#476042")
# # # parent.mainloop()
# # # import tkinter as tk   

# # # def write_text():
# # #     print("Tkinter is easy to create GUI!")

# # # parent = tk.Tk()
# # # frame = tk.Frame(parent)
# # # frame.pack()

# # # text_disp= tk.Button(frame, 
# # #                    text="Hello", 
# # #                    command=write_text
# # #                    )

# # # text_disp.pack(side=tk.LEFT)

# # # exit_button = tk.Button(frame,
# # #                    text="Exit",
# # #                    fg="green",
# # #                    command=quit)
# # # exit_button.pack(side=tk.RIGHT)

# # # parent.mainloop()
# # # import tkinter as tk
# # # from tkinter import ttk

# # # root = tk.Tk()
# # # my_str_var = tk.StringVar()

# # # my_combobox = ttk.Combobox(
# # #     root, textvariable = my_str_var,
# # #     values=["PHP", "Java", "Python","adarsh"])

# # # my_combobox.pack()
# # # root.mainloop()

# # import tkinter as tk
# # parent = tk.Tk()
# # parent.geometry("250x200")
# # label1 = tk.Label(parent,text = "A list of favourite languages...")
# # listbox = tk.Listbox(parent)
# # listbox.insert(1,"PHP")
# # listbox.insert(2, "Python")
# # listbox.insert(3, "Java")
# # listbox.insert(4, "C#")
# # label1.pack()
# # listbox.pack()
# # parent.mainloop()
# from bs4 import BeautifulSoup
# html_doc = """
# <html>
# <head>
# <meta http-equiv="Content-Type" content="text/html;
# charset=iso-8859-1">
# <title>An example of HTML page</title>
# </head>
# <body>
# <h2>This is an example HTML page</h2>
# <p>
# Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nunc at nisi velit,
# aliquet iaculis est. Curabitur porttitor nisi vel lacus euismod egestas. In hac
# habitasse platea dictumst. In sagittis magna eu odio interdum mollis. Phasellus
# sagittis pulvinar facilisis. Donec vel odio volutpat tortor volutpat commodo.
# Donec vehicula vulputate sem, vel iaculis urna molestie eget. Sed pellentesque
# adipiscing tortor, at condimentum elit elementum sed. Mauris dignissim
# elementum nunc, non elementum felis condimentum eu. In in turpis quis erat
# imperdiet vulputate. Pellentesque mauris turpis, dignissim sed iaculis eu,
# euismod eget ipsum. Vivamus mollis adipiscing viverra. Morbi at sem eget nisl
# euismod porta.</p>
# <p><a href="https://www.w3resource.com/html/HTML-tutorials.php">Learn HTML from
# w3resource.com</a></p>
# <p><a href="https://www.w3resource.com/css/CSS-tutorials.php">Learn CSS from 
# w3resource.com</a></p>
# </body>
# </html>
# """
# soup = BeautifulSoup(html_doc, 'html.parser')
# print("Title of the document:")
# print(soup.find("title"))


# import requests
# from bs4 import BeautifulSoup
# url = 'https://www.w3resource.com/'
# reqs = requests.get(url)
# soup = BeautifulSoup(reqs.text, 'lxml')
# print("\nFind and print all li tags:\n")
# for tag in soup.find_all("li"):
#     print("{0}: {1}".format(tag.name, tag.text))
a={"name":"anoop"}
print(type(a))    

