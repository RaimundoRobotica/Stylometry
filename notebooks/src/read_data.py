from .classes import Text

def read_text(address, title, author=None):
    f = open(address,'r', encoding="utf-8-sig")
    text = f.read()
    f.close()
    return Text(title, text, author=author)


def create_text_list():
    texts_list = []
    texts_list.append(read_text('data/raw/Galdos_Fortunata_y_Jacinta.txt', 'Fortunata y Jacinta', author='Benito Pérez Galdós'))
    texts_list.append(read_text('data/raw/Galdos_Gerona.txt', 'Gerona', author='Benito Pérez Galdós'))
    texts_list.append(read_text('data/raw/Galdos_La_corte_de_Carlos_IV.txt', 'La corte de Carlos IV', author='Benito Pérez Galdós'))
    texts_list.append(read_text('data/raw/Galdos_La_de_Bringas.txt', 'La de Bringas', author='Benito Pérez Galdós'))
    texts_list.append(read_text('data/raw/Galdos_Marianela.txt', 'Marianela', author='Benito Pérez Galdós'))
    texts_list.append(read_text('data/raw/Galdos_Misericordia.txt', 'Misericordia', author='Benito Pérez Galdós'))
    texts_list.append(read_text('data/raw/Galdos_Napoleon_en_Chamartin.txt', 'Napoleón en Chamartín', author='Benito Pérez Galdós'))
    texts_list.append(read_text('data/raw/Galdos_Trafalgar.txt', 'Trafalgar', author='Benito Pérez Galdós'))
    texts_list.append(read_text('data/raw/Pardo_Bazan_La_prueba.txt', 'La prueba', author='Emilia Pardo Bazán'))
    texts_list.append(read_text('data/raw/Pardo_Bazan_La_Tribuna.txt', 'La tribuna', author='Emilia Pardo Bazán'))
    texts_list.append(read_text('data/raw/Pardo_Bazan_Los_pazos_de_Ulloa.txt', 'Los pazos de Ulloa', author='Emilia Pardo Bazán'))
    texts_list.append(read_text('data/raw/Pardo_Bazan_Un_viaje_de_novios.txt', 'Un viaje de novios', author='Emilia Pardo Bazán'))
    texts_list.append(read_text('data/raw/Pardo_Bazan_Una_Cristiana.txt', 'Una cristiana', author='Emilia Pardo Bazán'))
    texts_list.append(read_text('data/raw/Valera_Algo_de_todo.txt', 'Algo de todo', author='Juan Valera'))
    texts_list.append(read_text('data/raw/Valera_De_varios_colores.txt', 'De varios colores', author='Juan Valera'))
    texts_list.append(read_text('data/raw/Valera_Doña_Luz.txt', 'Doña Luz', author='Juan Valera'))
    texts_list.append(read_text('data/raw/Valera_Genio_y_figura.txt', 'Genio y figura', author='Juan Valera'))
    texts_list.append(read_text('data/raw/Valera_Juanita_la_Larga.txt', 'Juanita la Larga', author='Juan Valera'))
    texts_list.append(read_text('data/raw/Valera_Morsamor.txt', 'Morsamor', author='Juan Valera'))
    texts_list.append(read_text('data/raw/Valera_Pasarse_de_listo.txt', 'Pasarse de listo', author='Juan Valera'))
    texts_list.append(read_text('data/raw/Valera_Pepita_Jimenez.txt', 'Pepita Jiménez', author='Juan Valera'))
    
    return texts_list
