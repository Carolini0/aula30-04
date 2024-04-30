from kivy.app import App
from kivy.uix.video import Video

class MinhaApp (App):
    def build(self):
        return Video(source= "C:/Users/aluno.sesipaulista/Downloads/4019911-sd_540_960_24fps.mp4")

if __name__ == "__main__":
    MinhaApp().run()
