#hola mundo con flet
import flet as ft
from flet import Page, Text, Button, Column, Row
def main(page: Page):
   page.title = "Hola Mundo con Flet" 
   page.vertical_alignment= "center" 
   page.horizontal_alignment = "center"

   def on_click():
       text.value = "¡Hola, mundo!" 
       page.update()

   text = Text(value="")
   button = Button("Haz clic aqui", on_click= on_click)

   page.add (Column ([text, button], alignment="center"))
   
ft.run(main)
