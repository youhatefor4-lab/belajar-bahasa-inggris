import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.radiobutton import RadioButton
from kivy.uix.gridlayout import GridLayout
from kivy.uix.popup import Popup
import random

# Bank soal bahasa Inggris
questions = [
    {
        "question": "_____ is your name?",
        "options": ["A. What", "B. Where", "C. Who", "D. When"],
        "correct": "A",
    },
    {
        "question": "She _____ to school every day.",
        "options": ["A. go", "B. goes", "C. going", "D. gone"],
        "correct": "B",
    },
    {
        "question": "Jam berapa sekarang dalam bahasa Inggris adalah?",
        "options": [
            "A. What color?",
            "B. What time is it?",
            "C. How old?",
            "D. Where are you?",
        ],
        "correct": "B",
    },
    {
        "question": "Kata 'Book' artinya?",
        "options": ["A. Pena", "B. Buku", "C. Meja", "D. Tas"],
        "correct": "B",
    },
    {
        "question": "They _____ playing football now.",
        "options": ["A. is", "B. are", "C. am", "D. be"],
        "correct": "B",
    },
]


class EnglishQuiz(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(orientation="vertical", padding=20, spacing=15, **kwargs)
        self.score = 0
        self.current_q = 0
        self.selected = None

        # Judul
        self.title_label = Label(
            text="KUIS BAHASA INGGRIS", font_size=24, bold=True, color=(0.2, 0.6, 1, 1)
        )
        self.add_widget(self.title_label)

        # Tampilan skor
        self.score_label = Label(text=f"Skor: {self.score}", font_size=18, bold=True)
        self.add_widget(self.score_label)

        # Tampilan soal
        self.question_label = Label(
            text="", font_size=16, halign="center", size_hint_y=0.4
        )
        self.add_widget(self.question_label)

        # Pilihan jawaban
        self.options_layout = GridLayout(cols=1, spacing=10)
        self.radio_buttons = []
        for opt in ["A", "B", "C", "D"]:
            btn = RadioButton(group="jawaban", font_size=16)
            btn.bind(on_release=lambda b, pilihan=opt: self.pilih_jawaban(pilihan))
            self.radio_buttons.append(btn)
            self.options_layout.add_widget(btn)
        self.add_widget(self.options_layout)

        # Tombol kirim
        self.submit_btn = Button(
            text="Kirim Jawaban",
            font_size=18,
            bold=True,
            background_color=(0.1, 0.7, 0.2, 1),
            size_hint_y=0.15,
        )
        self.submit_btn.bind(on_press=self.cek_jawaban)
        self.add_widget(self.submit_btn)

        # Tampilkan soal pertama
        self.tampilkan_soal()

    def tampilkan_soal(self):
        if self.current_q < len(questions):
            soal = questions[self.current_q]
            self.question_label.text = (
                f"Soal {self.current_q+1} dari {len(questions)}\n\n{soal['question']}"
            )
            for i, btn in enumerate(self.radio_buttons):
                btn.text = soal["options"][i]
                btn.active = False
            self.selected = None
        else:
            self.tampilkan_hasil()

    def pilih_jawaban(self, pilihan):
        self.selected = pilihan

    def cek_jawaban(self, instance):
        if not self.selected:
            Popup(
                title="Peringatan",
                content=Label(text="Silakan pilih jawaban dulu!"),
                size_hint=(0.8, 0.3),
            ).open()
            return

        benar = questions[self.current_q]["correct"]
        if self.selected == benar:
            self.score += 10
            Popup(
                title="Benar!",
                content=Label(text="Jawaban kamu tepat!"),
                size_hint=(0.7, 0.3),
            ).open()
        else:
            Popup(
                title="Salah",
                content=Label(text=f"Jawaban benar: {benar}"),
                size_hint=(0.7, 0.3),
            ).open()

        self.score_label.text = f"Skor: {self.score}"
        self.current_q += 1
        self.tampilkan_soal()

    def tampilkan_hasil(self):
        self.clear_widgets()
        hasil = f"SELESAI!\n\nSkor Akhir: {self.score}\nNilai: {(self.score / (len(questions)*10))*100:.0f}"
        hasil_label = Label(text=hasil, font_size=22, bold=True, halign="center")
        ulangi_btn = Button(
            text="Ulangi Kuis",
            font_size=18,
            background_color=(0.2, 0.5, 1, 1),
            size_hint_y=0.15,
        )
        ulangi_btn.bind(on_press=self.ulangi_kuis)
        self.add_widget(hasil_label)
        self.add_widget(ulangi_btn)

    def ulangi_kuis(self, instance):
        self.clear_widgets()
        self.__init__()


class QuizApp(App):
    def build(self):
        return EnglishQuiz()


if __name__ == "__main__":
    QuizApp().run()
