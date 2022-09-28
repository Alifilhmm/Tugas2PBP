

## Apa kegunaan {% csrf_token %} pada elemen <form>? Apa yang terjadi apabila tidak ada potongan kode tersebut pada elemen <form>?

    {% csrf_token %} kita implementasikan dengan tujuan menghindari serangan-serangan terhadap aplikasi web kita. Serangan yang mencari dan menggunakan bug atau kelemahan di aplikasi web kita, biasanya mengeksploitasi task memanfaat autentikasi yang dimiliki user. Jika tidak ada potongan kode {% csrf_token %}, akan mengancam keamanan post request dari user ke server.

## Apakah kita dapat membuat elemen <form> secara manual (tanpa menggunakan generator seperti {{ form.as_table }})? Jelaskan secara gambaran besar bagaimana cara membuat <form> secara manual.

    Bisa, kita bisa membuat elemen form secara manual dan menyimpan data-data form dengan syntax/method save(). Tidak lupa mencantumkan {% csrf_token %}. Dalam membuat elemen form secara manual, pertama-tama kita akan membuat elemen <form> itu sendiri memasukkan url untuk fungsi yang ingin kita panggil nantinya menggunakan method POST, setelah itu masukkan ke table. Data yang nantinya dimasukkan ke form dapat kita anggil kembali menggunakan request.POST.get(namafielddata).

##  Jelaskan proses alur data dari submisi yang dilakukan oleh pengguna melalui HTML form, penyimpanan data pada database, hingga munculnya data yang telah disimpan pada template HTML.

    1. user submit new task dengan menekan button submit
    2. form mengakses data input dengan menggunakan method request.POST.get()
    3. membuat objek baru yang akan disimpan ke database dengan cara ToDoList.objects.create(title = title, description = description, date = datetime.datetime.now(), user = request.user)
    4. Simpan data kedalam context dan kita return render dengan target html, setelah itu di html kita langsung bisa mengiterasi data menggunakan loop seperti yang diajarkan di lab dan data akan ditampilkan pada html

## Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas.

    1. Menggunakan command python manage.py startapp todolist di terminal
    2. Menambahkan path('todolist/', include('todolist.urls')), ke urls.py yang ada di project django
    3. Membuat class di models.py(todolist) dan membuat field sesuai dengan yang diminta tugas
    4. Membuat fungsi login,logout,register yang dihubungkan ke login.html dan register.html. Melakukannya sama dengan tutorial 3
    5. Menampilan username pengguna dengan syntax :
    <h5>Logged in as: </h5>
    <p>{{ user.get_username }}</p>

    Menampilkan tombol tambah task baru (Add New Task) dengan syntax :
    <button><a href="{% url 'todolist:create-task' %}">Add New Task</a></button>

    Menampilkan tombol logout dengan syntax :
    <button><a href="{% url 'todolist:logout' %}">Logout</a></button>

    Menampilkan tabel task beserta komponennya menggunakan looping dengan syntax:
    {% for task in todolist %}
      <tr>
          <th>{{task.date}}</th>
          <th>{{task.title}}</th>
          <th>{{task.description}}</th>

          {% if task.is_finished %} 
            <th>Selesai</th>
          {% else %}
            <th>Belum Selesai</th>
          {% endif %}
    
    6. Menampilkan input yang dapat diisi user dan tombol submit dengan syntax :
    <form method="POST" >  
            {% csrf_token %}  
            <table>  
                {{ form.as_table }}  
                <tr>  
                    <td></td>
                    <td><input type="submit" name="submit" value="Tambah"/></td>  
                </tr>  
            </table>  
        </form>
    
    7. Menambahkan urlpattern di urls.py(todolist) 
    path('register/', register, name='register'), 
    path('login/', login_user, name='login'), 
    path('logout/', logout_user, name='logout'), 
    path('create-task/', addTask, name='create-task'),

## Akun Dummy

    
