# -*- coding: utf-8 -*-
"""
Created on Wed Apr  6 17:27:03 2022

@author: Cesar Skarbnik
"""
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
import random


class Dado(App):
        
    
      #Este es el constructor
    def init(self, **kwargs):
        #llamar al constructor de la clase base (App)
        super().__init__(**kwargs)
        #Defino un atributo
    
    def btnaccion_dado(self,obj):
        num = 0
        num = random.randint(1,6)
        self.lblnumdado.text = str(num)
    
    def build(self):
        #Vamos a defnir un layout
        gdl_principal = GridLayout(rows=3,cols=1)
        lbltitulo = Label(text='Aplicacion Dado')
        gdl_principal.add_widget(lbltitulo)
        #GridMedio
        gdl_medio = GridLayout(cols=2)
        lblresultado = Label(text='Resultado')
        gdl_medio.add_widget(lblresultado)
        lblnumdado = Label(text="6")
        gdl_medio.add_widget(lblnumdado)
        gdl_principal.add_widget(gdl_medio)
        #Boton
        btnaccion = Button(text="Presioname!!")
        #Enlaze
        gdl_principal.add_widget(btnaccion)
        btnaccion.bind(on_press = self.btnaccion_dado)
        #Atrivbuto
        self.gdl_principal = gdl_principal
        self.lblnumdado = lblnumdado
        return gdl_principal
    
if __name__ == '__main__':
    D = Dado()
    D.run()
    

