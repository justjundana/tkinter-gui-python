import tkinter as tk

# Membuat objek Tkinter
app = tk.Tk()
app.title("CRUD App")
app.geometry("400x300")

# Membuat sebuah array
data = []

# Membuat sebuah fungsi untuk membuka pop-up form
def create_form():
    create_window = tk.Toplevel(app)
    create_window.title("Form Tambah Data")
    create_window.geometry("300x200")

    # Membuat sebuah label dan entry untuk memasukkan data
    tk.Label(create_window, text="Nama:").grid(row=0, column=0)
    nama_entry = tk.Entry(create_window)
    nama_entry.grid(row=0, column=1)

    tk.Label(create_window, text="Umur:").grid(row=1, column=0)
    umur_entry = tk.Entry(create_window)
    umur_entry.grid(row=1, column=1)

    # Membuat sebuah tombol untuk menyimpan data
    tk.Button(
        create_window,
        text="Simpan",
        command=lambda: save_data(create_window, nama_entry, umur_entry),
    ).grid(row=2, column=1)


# Membuat sebuah fungsi untuk menyimpan data ke array
def save_data(create_window, nama_entry, umur_entry):
    nama = nama_entry.get()
    umur = umur_entry.get()

    # Menambahkan data ke array
    data.append({"nama": nama, "umur": umur})

    # Menutup pop-up form setelah data disimpan
    create_window.destroy()
    update_list()


# Membuat sebuah fungsi untuk memperbarui list data
def update_list():
    listbox.delete(0, "end")
    for item in data:
        listbox.insert("end", f"{item['nama']} ({item['umur']})")


# Membuat sebuah fungsi untuk membuka pop-up window dengan detail data
def read():
    # Menentukan index data yang dipilih
    index = listbox.curselection()[0]

    # Membuka pop-up window dengan detail data
    read_window = tk.Toplevel(app)
    read_window.title("Detail Data")
    read_window.geometry("300x200")

    # Membuat sebuah label dan entry untuk menampilkan data
    tk.Label(read_window, text="Nama:").grid(row=0, column=0)
    nama_label = tk.Label(read_window, text=data[index]["nama"])
    nama_label.grid(row=0, column=1)

    tk.Label(read_window, text="Umur:").grid(row=1, column=0)
    umur_label = tk.Label(read_window, text=data[index]["umur"])
    umur_label.grid(row=1, column=1)

    # Membuat sebuah tombol untuk update data
    tk.Button(read_window, text="Update", command=lambda: update_form(index)).grid(
        row=2, column=1
    )


def update_form(index):
    update_window = tk.Toplevel(app)
    update_window.title("Form Update Data")
    update_window.geometry("300x200")

    # Membuat sebuah label dan entry untuk menampilkan data
    tk.Label(update_window, text="Nama:").grid(row=0, column=0)
    nama_entry = tk.Entry(update_window)
    nama_entry.insert(0, data[index]["nama"])
    nama_entry.grid(row=0, column=1)

    tk.Label(update_window, text="Umur:").grid(row=1, column=0)
    umur_entry = tk.Entry(update_window)
    umur_entry.insert(0, data[index]["umur"])
    umur_entry.grid(row=1, column=1)

    # Membuat sebuah tombol untuk update data
    tk.Button(
        update_window,
        text="Update",
        command=lambda: update_data(update_window, index, nama_entry, umur_entry),
    ).grid(row=2, column=1)


# Membuat sebuah fungsi untuk update data
def update_data(update_window, index, nama_entry, umur_entry):
    nama = nama_entry.get()
    umur = umur_entry.get()

    # Update data pada list
    data[index]["nama"] = nama
    data[index]["umur"] = umur

    # Menutup pop-up window setelah data diupdate
    update_window.destroy()
    update_list()


# Membuat sebuah fungsi untuk menghapus data
def delete():
    # Menentukan index data yang dipilih
    index = listbox.curselection()[0]

    # Menghapus data dari list
    data.pop(index)

    # Memperbarui list data
    update_list()


# Membuat sebuah tombol untuk membuka pop-up form
tk.Button(app, text="Tambah Data", command=create_form).pack()

# Membuat sebuah tombol untuk membuka pop-up window dengan detail data
tk.Button(app, text="Detail Data", command=read).pack()

# Membuat sebuah tombol untuk menghapus data
tk.Button(app, text="Hapus Data", command=delete).pack()

# Membuat sebuah tombol untuk keluar dari aplikasi
tk.Button(app, text="Keluar", command=app.destroy).pack()

# Membuat sebuah widget untuk menampilkan list data
listbox = tk.Listbox(app)
listbox.pack()
listbox.bind("<Double-1>", read)

# Menjalankan aplikasi
app.mainloop()
