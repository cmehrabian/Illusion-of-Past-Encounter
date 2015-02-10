import os
import random
from time import time
import pygame
from Tkinter import *

class Experiment:

    def option(self):
        master = Tk()
        master.title("Introduction")
        master.geometry('450x300+100+100')

        labelText = StringVar()
        labelText.set("Enter your particpant number")
        label1 = Label(master, textvariable=labelText, height=4)
        label1.pack()

        e = Entry(master)
        e.pack()

        e.focus_set()

        def callback():
            global num
            num = e.get()
            fh = open("data_file"+num+".csv", "w")
            fh.write("Participant # " + str(num) +"\n")
            print num
            data = x.run("./novelSymbols")
        def quitback():
            master.destroy()


        b = Button(master, text="Click here to Begin", width=17, height = 2, command=callback)
        b.pack()

        q = Button(master, text="Quit", width=17, height = 2, command=quitback)
        q.pack()


        labelText = StringVar()
        labelText.set("Thank you for your participation!")
        label1 = Label(master, textvariable=labelText, height=20)
        label1.pack()

        mainloop()
        e = Entry(master, width=100)
        e.pack()

        text = e.get()
            
        def makeentry(parent, caption, width=None, **options):
            Label(parent, text=caption).pack(side=LEFT)
            entry = Entry(parent, **options)
            if width:
                entry.config(width=width)
            entry.pack(side=LEFT)
            return entry

        user = makeentry(parent, "User name:", 10)
        password = makeentry(parent, "Password:", 10, show="*")
        content = StringVar()
        entry = Entry(parent, text=caption, textvariable=content)

        text = content.get()
        content.set(text)

    
    
    def run(self, the_filepath):
        if not os.path.isdir(the_filepath):
            print "Error thats not a path"
            return None
        fh = open("data_file"+num+".csv", "w")
        fh.write("PictureID" + "," + "\n")

        dirlist = os.listdir(the_filepath)
        random.shuffle(dirlist)
   
        print dirlist

        for a in dirlist:
            print a
            if a == ".DS_Store":
                print "found that bitch"
                continue
            fh.write(str(a) + ",")
            pygame.init()
            surface_sz = 920
            main_surface = pygame.display.set_mode((surface_sz, surface_sz))
            
            img = pygame.image.load(a)
            my_font = pygame.font.SysFont("Times New Roman", 22)

            while True:
                ev = pygame.event.poll()
                if ev.type == pygame.QUIT:
                    break
                if ev.type == pygame.KEYDOWN:
                    ans = pygame.key.name(ev.key)
                    fh.write(str(ans) +",")
                    if ans == "y":
                        fh.write("1\n")
                    elif ans == "n":
                        fh.write("0\n")
                    else:
                        fh.write("N/A\n")
                    
                    break

                main_surface.fill((255, 255, 255)) #background
                main_surface.blit(img, (200,90))
                
                
                
                the_text = my_font.render("Have you ever encountered this symbol prior to the experiment? Yes or No.", True, (0,0,0))
                main_surface.blit(the_text, (160, 600))

                
               
                # Now the surface is ready, tell pygame to display it!
                pygame.display.flip()
        pygame.quit()

        

x = Experiment()
name = x.option()



        
