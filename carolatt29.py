from kivy.app import App
from kivy.uix.image import Image , AsyncImage

class MinhaApp(App):
    def build(self):

        return AsyncImage(source= 'https://img.freepik.com/fotos-premium/por-do-sol-bonito-da-praia-com-mar-azul-e-fundo-claro-dourado-da-nuvem-do-ceu_63726-347.jpg')
if __name__ == "__main__":
    MinhaApp().run()