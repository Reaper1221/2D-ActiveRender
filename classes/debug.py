import numpy as np
import pygame as pg
import tkinter as Tk
from math import *

class Debug:

    window = Tk.Tk()

    def __init__(self, debug: bool) -> None:
        self.debug = debug
        self.windowWithd = 600
        self.windowheight = 450
        self.windowGeometry = f"300x100"

        self.window.title("Debug Widnow ActiveRender")
        self.window.geometry(self.windowGeometry) 

        self.selected = Tk.IntVar()  
        self.rad1 = Tk.Radiobutton(self.window,text='with stopmode', value=1, variable=self.selected)  
        self.rad2 = Tk.Radiobutton(self.window,text='with not stopmode', value=2, variable=self.selected)
        self.rad2.select()
        self.rad1.grid(column=0, row=0) 
        self.rad2.grid(column=2, row=0) 

        self.cadrs_entry = Tk.Entry(self.window,width=10)  
        self.cadrs_entry.grid(column=0, row=1) 
        self.start_btn = Tk.Button(self.window, text="START", command=self._start_click_)  
        self.start_btn.grid(column=1, row=1) 
        self.stop_btn = Tk.Button(self.window, text="STOP", command=self._stop_click_)  
        self.stop_btn.grid(column=2, row=1) 

        self.cadrs_entry.insert(0, "0")

        pg.font.init()
        pg.font.get_init()

        pg.display.set_caption('Debug')

        self.display_surface = pg.display.set_mode((self.windowWithd, self.windowheight))
        self.font = pg.font.SysFont('chalkduster.ttf', 24)

        self.textRect1 = (50, 30)
        self.textRect2 = (50, 60)
        self.textRect3 = (50, 90)
        self.textRect4 = (50, 120)
        self.textRect5 = (50, 150)
        self.textRect6 = (50, 180)
        self.textRect7 = (50, 210)
        self.textRect8 = (50, 240)
        self.textRect9 = (50, 270)
        self.textRect10 = (50, 300)
        self.textRect11 = (50, 330)

        self.text_color = (255,255,255)
        self.bg_color = (0,0,0)

    def debug_window_part(self, info:list, cost:list) -> None :
        if self.debug: 

            self.display_surface.fill(self.bg_color)

            logs = []

            for x in range(len(info)): 
                logs.append(f"{info[x]} =: {cost[x]}")

            for event in pg.event.get():
                if event.type == pg.QUIT: 
                    pg.quit()
                    quit()
            
            text1 = self.font.render(logs[0], True, self.text_color)
            text2 = self.font.render(logs[1], True, self.text_color)
            text3 = self.font.render(logs[2], True, self.text_color)
            text4 = self.font.render(logs[3], True, self.text_color)
            text5 = self.font.render(logs[4], True, self.text_color)
            text6 = self.font.render(logs[5], True, self.text_color)
            text7 = self.font.render(logs[6], True, self.text_color)
            text8 = self.font.render(logs[7], True, self.text_color)
            text9 = self.font.render(logs[8], True, self.text_color)

            self.display_surface.blit(text1, self.textRect1)
            self.display_surface.blit(text2, self.textRect2)
            self.display_surface.blit(text3, self.textRect3)
            self.display_surface.blit(text4, self.textRect4)
            self.display_surface.blit(text5, self.textRect5)
            self.display_surface.blit(text6, self.textRect6)
            self.display_surface.blit(text7, self.textRect7)
            self.display_surface.blit(text8, self.textRect8)
            self.display_surface.blit(text9, self.textRect9)

            if len(logs) == 11: 
                text10 = self.font.render(logs[9], True, self.text_color)
                text11 = self.font.render(logs[10], True, self.text_color)

                self.display_surface.blit(text10, self.textRect10)
                self.display_surface.blit(text11, self.textRect11)

            pg.display.update()
        
        if not self.debug: pg.quit() 

    def _init_start_method_(self, method) -> None : self.__start_method = method

    def _start_click_(self) -> None : 
        self.cadrs = self.cadrs_entry.get()
        self.stopmode = 1 if self.selected.get() == 1 else 0
        self.window.destroy()
        self.window.quit()

        self.__start_method(self.cadrs, self.stopmode)

    def _stop_click_(self) -> None: 0/0
 
