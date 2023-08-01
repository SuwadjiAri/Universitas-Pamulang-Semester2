from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button

class HomePage(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'vertical'

        # Tambahkan elemen-elemen UI
        label = Label(text="Selamat Datang di Aplikasi Sistem Informasi Manajemen")
        button1 = Button(text="Pengguna")
        button2 = Button(text="Perusahaan")
        button3 = Button(text="Produk")
        button4 = Button(text="Aplikasi")
        button5 = Button(text="Pelanggan")

        # Atur aksi untuk tombol-tombol
        button1.bind(on_release=self.goto_users)
        button2.bind(on_release=self.goto_companies)
        button3.bind(on_release=self.goto_products)
        button4.bind(on_release=self.goto_applications)
        button5.bind(on_release=self.goto_customers)

        # Tambahkan elemen-elemen ke dalam layout
        self.add_widget(label)
        self.add_widget(button1)
        self.add_widget(button2)
        self.add_widget(button3)
        self.add_widget(button4)
        self.add_widget(button5)

    def goto_users(self, instance):
        print("Pergi ke halaman Pengguna")

    def goto_companies(self, instance):
        print("Pergi ke halaman Perusahaan")

    def goto_products(self, instance):
        print("Pergi ke halaman Produk")

    def goto_applications(self, instance):
        print("Pergi ke halaman Aplikasi")

    def goto_customers(self, instance):
        print("Pergi ke halaman Pelanggan")

class MyApp(App):
    def build(self):
        return HomePage()

if __name__ == '__main__':
    MyApp().run()
