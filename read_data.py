from classes import Text
def read_data():
    texts_list = []

    f = open('data/Galdos_Fortunata_y_Jacinta.txt','r', encoding="utf-8-sig")
    text = f.read()
    f.close()
    texts_list.append(Text('Fortunata y Jacinta', text, author='Benito Pérez Galdós'))

    f = open('data/Galdos_Gerona.txt','r', encoding="utf-8-sig")
    text = f.read()
    f.close()
    texts_list.append(Text('Gerona', text))

    f = open('data/Galdos_La_corte_de_Carlos_IV.txt','r', encoding="utf-8-sig")
    text = f.read()
    f.close()
    texts_list.append(Text('La corte de Carlos IV', text, author='Benito Pérez Galdós'))

    f = open('data/Galdos_La_de_Bringas.txt','r', encoding="utf-8-sig")
    text = f.read()
    f.close()
    texts_list.append(Text('La de Bringas', text, author='Benito Pérez Galdós'))

    f = open('data/Galdos_Marianela.txt','r', encoding="utf-8-sig")
    text = f.read()
    f.close()
    texts_list.append(Text('Marianela', text, author='Benito Pérez Galdós'))

    f = open('data/Galdos_Misericordia.txt','r', encoding="utf-8-sig")
    text = f.read()
    f.close()
    texts_list.append(Text('Misericordia', text, author='Benito Pérez Galdós'))

    f = open('data/Galdos_Napoleon_en_Chamartin.txt','r', encoding="utf-8-sig")
    text = f.read()
    f.close()
    texts_list.append(Text('Napoleón en Chamartín', text))

    f = open('data/Galdos_Trafalgar.txt','r', encoding="utf-8-sig")
    text = f.read()
    f.close()
    texts_list.append(Text('Trafalgar', text, author='Benito Pérez Galdós'))

    f = open('data/Pardo_Bazan_La_prueba.txt','r', encoding="utf-8-sig")
    text = f.read()
    f.close()
    texts_list.append(Text('La prueba', text, author='Emilia Pardo Bazán'))

    f = open('data/Pardo_Bazan_La_Tribuna.txt','r', encoding="utf-8-sig")
    text = f.read()
    f.close()
    texts_list.append(Text('La Tribuna', text, author='Emilia Pardo Bazán'))

    f = open('data/Pardo_Bazan_Los_pazos_de_Ulloa.txt','r', encoding="utf-8-sig")
    text = f.read()
    f.close()
    texts_list.append(Text('Los pazos de Ulloa', text))

    f = open('data/Pardo_Bazan_Un_viaje_de_novios.txt','r', encoding="utf-8-sig")
    text = f.read()
    f.close()
    texts_list.append(Text('Un viaje de novios', text, author='Emilia Pardo Bazán'))

    f = open('data/Pardo_Bazan_Una_Cristiana.txt','r', encoding="utf-8-sig")
    text = f.read()
    f.close()
    texts_list.append(Text('Una cristiana', text, author='Emilia Pardo Bazán'))

    f = open('data/Valera_Algo_de_todo.txt','r', encoding="utf-8-sig")
    text = f.read()
    f.close()
    texts_list.append(Text('Algo de todo', text, author='Juan Valera'))

    f = open('data/Valera_De_varios_colores.txt','r', encoding="utf-8-sig")
    text = f.read()
    f.close()
    texts_list.append(Text('De varios colores', text, author='Juan Valera'))

    f = open('data/Valera_Doña_Luz.txt','r', encoding="utf-8-sig")
    text = f.read()
    f.close()
    texts_list.append(Text('Doña_luz', text, author='Juan Valera'))

    f = open('data/Valera_Genio_y_figura.txt','r', encoding="utf-8-sig")
    text = f.read()
    f.close()
    texts_list.append(Text('Genio y figura', text, author='Juan Valera'))

    f = open('data/Valera_Juanita_la_Larga.txt','r', encoding="utf-8-sig")
    text = f.read()
    f.close()
    texts_list.append(Text('Juanita_la_Larga', text, author='Juan Valera'))

    f = open('data/Valera_Morsamor.txt','r', encoding="utf-8-sig")
    text = f.read()
    f.close()
    texts_list.append(Text('Morsamor', text, author='Juan Valera'))

    f = open('data/Valera_Pasarse_de_listo.txt','r', encoding="utf-8-sig")
    text = f.read()
    f.close()
    texts_list.append(Text('Pasarse_de_listo', text, author='Juan Valera'))

    f = open('data/Valera_Pepita_Jimenez.txt','r', encoding="utf-8-sig")
    text = f.read()
    f.close()
    texts_list.append(Text('Pepita Jiménez', text))

    return texts_list
