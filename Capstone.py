DataPegawai = [
    {
        'ID' : 101,
        'Nama' : 'Budianto',
        'Umur' : 27,
        'Kelamin' : 'Pria',
        'Departemen' : 'Finance'
    },
    {
        'ID' : 102,
        'Nama' : 'Rizka Utami',
        'Umur' : 31,
        'Kelamin' : 'Wanita',
        'Departemen' : 'Sales'
    },
    {
        'ID' : 103,
        'Nama' : 'Putri Sarita',
        'Umur' : 25,
        'Kelamin' : 'Wanita',
        'Departemen' : 'H. Capital'
    },
    {
        'ID' : 104,
        'Nama' : 'Dito Ramanda',
        'Umur' : 39,
        'Kelamin' : 'Pria',
        'Departemen' : 'Marketing'
    }
]

def TampilData():
    while(True):
        try:
            print('\nDaftar Pegawai')
            print('Index\t| ID\t| Nama\t\t| Umur\t| Kelamin\t| Departemen\t\t|')
            for i in range(len(DataPegawai)):
                print('{}\t| {}\t| {}\t| {}\t| {}  \t| {} \t\t|'.format(i, DataPegawai[i]['ID'], DataPegawai[i]['Nama'], DataPegawai[i]['Umur'], DataPegawai[i]['Kelamin'], DataPegawai[i]['Departemen']))
            Id0 = int(input('\nMasukkan index yang ingin dicari: '))
            print('Index\t| ID\t| Nama\t\t| Umur\t| Kelamin\t| Departemen\t\t|')
            print('{}\t| {}\t| {}\t| {}\t| {}  \t| {} \t\t|'.format(Id0, DataPegawai[Id0]['ID'], DataPegawai[Id0]['Nama'], DataPegawai[Id0]['Umur'], DataPegawai[Id0]['Kelamin'], DataPegawai[Id0]['Departemen']))
            break
        except IndexError:
                print('Data tidak ditemukan')

def SajiData():
    print('\nDaftar Pegawai')
    print('Index\t| ID\t| Nama\t\t| Umur\t| Kelamin\t| Departemen\t\t|')
    for i in range(len(DataPegawai)):
        print('{}\t| {}\t| {}\t| {}\t| {}  \t| {} \t\t|'.format(i, DataPegawai[i]['ID'], DataPegawai[i]['Nama'], DataPegawai[i]['Umur'], DataPegawai[i]['Kelamin'], DataPegawai[i]['Departemen']))

def MasukData():
    SajiData()
    while(True):
        MasukkanId = int(input('\nMasukkan data ID: '))
        MasukkanNm = input('Masukkan data nama: ')
        MasukkanUmr = int(input('Masukkan data umur: '))
        MasukkanKlm = input('Masukkan data kelamin: ')
        MasukkanDpm = input('Masukkan data departemen: ')
        Tanya1 = input('Ingin menyimpan data (Ya/Tidak)): ')
        if(Tanya1 == 'Ya'):
            print('Data delah tersimpan.')
            break
        
    DataPegawai.append({
    'ID' : MasukkanId,
    'Nama' : MasukkanNm,
    'Umur' : MasukkanUmr,
    'Kelamin' : MasukkanKlm,
    'Departemen' : MasukkanDpm
    })
    SajiData()

def UbahData():
    SajiData()
    print('\nMenu sunting hanya bisa menyunting data Umur dan Departemen \nSunting Data Umur')
    while(True):
        while(True):
            Sunting = input('Ingin menyunting data umur (Ya/Tidak)? ')
            if (Sunting == 'Ya'):
                while(True):
                    try:
                        Id = int(input('\nMasukkan index yang ingin disunting: '))
                        print('Index\t| ID\t| Nama\t\t| Umur\t| Kelamin\t| Departemen\t\t|')
                        print('{}\t| {}\t| {}\t| {}\t| {}  \t| {} \t\t|'.format(Id, DataPegawai[Id]['ID'], DataPegawai[Id]['Nama'], DataPegawai[Id]['Umur'], DataPegawai[Id]['Kelamin'], DataPegawai[Id]['Departemen']))
                        break
                    except IndexError:
                        print('Data tidak ditemukan')
                InputUmr = int(input('\nMasukkan data umur yang baru: '))
                Tanya2 = input('Ingin menyimpan data (Ya/Tidak)): ')
                if(Tanya2 == 'Ya'):
                    print('Data telah tersimpan.')
                elif(Tanya2 == 'Tidak'):
                    continue
                DataPegawai[Id]['Umur'] = InputUmr
                print('Index\t| ID\t| Nama\t\t| Umur\t| Kelamin\t| Departemen\t\t|')
                print('{}\t| {}\t| {}\t| {}\t| {}  \t| {} \t\t|'.format(Id, DataPegawai[Id]['ID'], DataPegawai[Id]['Nama'], DataPegawai[Id]['Umur'], DataPegawai[Id]['Kelamin'], DataPegawai[Id]['Departemen']))
                SajiData()
                break
            elif(Sunting == 'Tidak'):
                break
        while(True):
            print('\nSunting Data Departemen')
            Sunting2 = input('Ingin menyunting data departemen (Ya/Tidak)? ')
            if (Sunting2 == 'Ya'):
                while(True):
                    try:
                        Id2 = int(input('\nMasukkan index yang ingin disunting: '))
                        print('Index\t| ID\t| Nama\t\t| Umur\t| Kelamin  \t| Departemen\t\t|')
                        print('{}\t| {}\t| {}\t| {}\t| {}  \t| {} \t\t|'.format(Id2, DataPegawai[Id2]['ID'], DataPegawai[Id2]['Nama'], DataPegawai[Id2]['Umur'], DataPegawai[Id2]['Kelamin'], DataPegawai[Id2]['Departemen']))
                        InputDpm = (input('\nMasukkan data departemen yang baru: '))
                        break
                    except IndexError:
                        print('Data tidak ditemukan')
                Tanya3 = input('Ingin menyimpan data (Ya/Tidak)): ')
                if(Tanya3 == 'Ya'):
                    print('Data delah tersimpan.')
                elif(Tanya3 == 'Tidak'):
                    continue
                DataPegawai[Id2]['Departemen'] = InputDpm
                print('Index\t| ID\t| Nama\t\t| Umur\t| Kelamin\t| Departemen\t\t|')
                print('{}\t| {}\t| {}\t| {}\t| {}  \t| {} \t\t|'.format(Id2, DataPegawai[Id2]['ID'], DataPegawai[Id2]['Nama'], DataPegawai[Id2]['Umur'], DataPegawai[Id2]['Kelamin'], DataPegawai[Id2]['Departemen']))
                SajiData()
                break
            elif(Sunting2 == 'Tidak'):
                break
        break

def HapusData():
    while(True):
        while(True):
            SajiData()
            try:
                Id3 = int(input('\nMasukkan index pegawai yang ingin dihapus: '))
                print('Index\t| ID\t| Nama\t\t| Umur\t| Kelamin  \t| Departemen\t\t|')
                print('{}\t| {}\t| {}\t| {}\t| {}  \t| {} \t\t|'.format(Id3, DataPegawai[Id3]['ID'], DataPegawai[Id3]['Nama'], DataPegawai[Id3]['Umur'], DataPegawai[Id3]['Kelamin'], DataPegawai[Id3]['Departemen']))
                break
            except IndexError:
                print('Data tidak ditemukan')
        Tanya4 = input('Ingin menghapus data (Ya/Tidak)): ')
        if(Tanya4 == 'Ya'):
            print('Data delah terhapus.')
        elif(Tanya4 == 'Tidak'):
            continue
        del DataPegawai[Id3]
        SajiData()
        break
    
while(True):
    MenuPilihan = int(input('''
    Data Pegawai PT. Abadi Sejahtera
    
    Daftar Menu:
    1. Menyajikan Data Pegawai
    2. Memasukkan Data Pegawai
    3. Menyunting Data Pegawai
    4. Menghapus Data Pegawai
    5. Keluar dari Menu

    Masukkan menu yang ingin dijalankan: '''
    ))
    
    if(MenuPilihan == 1):
        TampilData()

    elif(MenuPilihan == 2):
        MasukData()
    
    elif(MenuPilihan == 3):
        UbahData()

    elif(MenuPilihan == 4):
        HapusData()

    elif(MenuPilihan == 5):
        break
