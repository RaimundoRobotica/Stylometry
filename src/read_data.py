from classes import Text

def read_text(address, title, author=None):
    f = open(address,'r', encoding="utf-8-sig")
    text = f.read()
    f.close()
    return Text(title, text, author=author)


def create_text_list():
    texts_list = []
    texts_list.append(read_text('data/Galdos_Fortunata_y_Jacinta.txt', 'Fortunata y Jacinta', author='Benito Pérez Galdós'))
    texts_list.append(read_text('data/Galdos_Gerona.txt', 'Gerona', author='Benito Pérez Galdós'))
    texts_list.append(read_text('data/Galdos_La_corte_de_Carlos_IV.txt', 'La corte de Carlos IV', author='Benito Pérez Galdós'))
    texts_list.append(read_text('data/Galdos_La_de_Bringas.txt', 'La de Bringas', author='Benito Pérez Galdós'))
    texts_list.append(read_text('data/Galdos_Marianela.txt', 'Marianela'))
    texts_list.append(read_text('data/Galdos_Misericordia.txt', 'Misericordia', author='Benito Pérez Galdós'))
    texts_list.append(read_text('data/Galdos_Napoleon_en_Chamartin.txt', 'Napoleón en Chamartín', author='Benito Pérez Galdós'))
    texts_list.append(read_text('data/Galdos_Trafalgar.txt', 'Trafalgar', author='Benito Pérez Galdós'))
    texts_list.append(read_text('data/Pardo_Bazan_La_prueba.txt', 'La prueba', author='Emilia Pardo Bazán'))
    texts_list.append(read_text('data/Pardo_Bazan_La_Tribuna.txt', 'La tribuna', author='Emilia Pardo Bazán'))
    texts_list.append(read_text('data/Pardo_Bazan_Los_pazos_de_Ulloa.txt', 'Los pazos de Ulloa', author='Emilia Pardo Bazán'))
    texts_list.append(read_text('data/Pardo_Bazan_Un_viaje_de_novios.txt', 'Un viaje de novios', author='Emilia Pardo Bazán'))
    texts_list.append(read_text('data/Pardo_Bazan_Una_Cristiana.txt', 'Una cristiana', author='Emilia Pardo Bazán'))
    texts_list.append(read_text('data/Valera_Algo_de_todo.txt', 'Algo de todo', author='Juan Valera'))
    texts_list.append(read_text('data/Valera_De_varios_colores.txt', 'De varios colores', author='Juan Valera'))
    texts_list.append(read_text('data/Valera_Doña_Luz.txt', 'Doña_luz', author='Juan Valera'))
    texts_list.append(read_text('data/Valera_Genio_y_figura.txt', 'Genio y figura', author='Juan Valera'))
    texts_list.append(read_text('data/Valera_Juanita_la_Larga.txt', 'Juanita_la_Larga', author='Juan Valera'))
    texts_list.append(read_text('data/Valera_Morsamor.txt', 'Morsamor'))
    texts_list.append(read_text('data/Valera_Pasarse_de_listo.txt', 'Pasarse de listo', author='Juan Valera'))
    texts_list.append(read_text('data/Valera_Pepita_Jimenez.txt', 'Pepita Jiménez', author='Juan Valera'))
    
    return texts_list
