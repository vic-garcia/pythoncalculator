import  tkinter as tk

root = tk.Tk()
root.title("Calculator")

display= tk.Entry(root)
display.grid(row=1, columnspan=6, sticky="w,n")

#Numeric Buttons
tk.Button(root, text="1").grid(row=1,column=1, sticky="w,e,s")
tk.Button(root, text="2").grid(row=1,column=2, sticky="w,e,s")
tk.Button(root, text="3").grid(row=1,column=3, sticky="w,e,s")

tk.Button(root, text="4").grid(row=2,column=1, sticky="w,e,s")
tk.Button(root, text="5").grid(row=2,column=2, sticky="w,e,s")
tk.Button(root, text="6").grid(row=2,column=3, sticky="w,e,s")

tk.Button(root, text="7").grid(row=3,column=1, sticky="w,e,s")
tk.Button(root, text="8").grid(row=3,column=2, sticky="w,e,s")
tk.Button(root, text="9").grid(row=3,column=3, sticky="w,e,s")

tk.Button(root, text="#").grid(row=4,column=1, sticky="w,e,s")
tk.Button(root, text="0").grid(row=4,column=2, sticky="w,e,s")
tk.Button(root, text="*").grid(row=4,column=3, sticky="w,e,s")

#Opera
tk.Button(root, text="AC").grid(row=4,column=4, sticky="w,e,s")
tk.Button(root, text="=").grid(row=4,column=4, sticky="w,e,s")
tk.Button(root, text="/").grid(row=4,column=4, sticky="w,e,s")
tk.Button(root, text="×").grid(row=4,column=4, sticky="w,e,s")
tk.Button(root, text="√").grid(row=4,column=4, sticky="w,e,s")
tk.Button(root, text="0").grid(row=4,column=4, sticky="w,e,s")
tk.Button(root, text="0").grid(row=4,column=4, sticky="w,e,s")


root.columnconfigure(1, weight=1)
root.columnconfigure(2, weight=1)
root.columnconfigure(3, weight=1)
root.rowconfigure(1, weight=1)
root.rowconfigure(2, weight=1)
root.rowconfigure(3, weight=1)
root.displayconfigure(1,weight=1)
root.mainloop()

