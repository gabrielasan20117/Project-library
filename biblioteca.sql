CREATE TABLE Libros (
    id INT PRIMARY KEY,
    titulo VARCHAR(255) NOT NULL,
    autor_id INT NOT NULL,
    anio_publicacion DATE NOT NULL,
    genero_id INT NOT NULL,
    editorial_id INT NOT NULL,
    estante_id INT NOT NULL,
    categoria_id INT NOT NULL,
    FOREIGN KEY (autor_id) REFERENCES Autores(id),
    FOREIGN KEY (genero_id) REFERENCES Generos(id),
    FOREIGN KEY (editorial_id) REFERENCES Editoriales(id),
    FOREIGN KEY (estante_id) REFERENCES Estantes(id),
    FOREIGN KEY (categoria_id) REFERENCES Categorias(id)
);

CREATE TABLE Usuarios (
    id INT PRIMARY KEY,
    nombre VARCHAR(255) NOT NULL,
    direccion VARCHAR(255) NOT NULL,
    telefono INT NOT NULL
);

CREATE TABLE Prestamos (
    id INT PRIMARY KEY,
    libro_id INT NOT NULL,
    usuario_id INT NOT NULL,
    fecha_prestamo DATE NOT NULL,
    fecha_devolucion DATE NOT NULL,
    FOREIGN KEY (libro_id) REFERENCES Libros(id),
    FOREIGN KEY (usuario_id) REFERENCES Usuarios(id)
);

CREATE TABLE Autores (
    id INT PRIMARY KEY,
    nombre VARCHAR(255) NOT NULL,
    fecha_nacimiento DATE NOT NULL
);

CREATE TABLE Generos (
    id INT PRIMARY KEY,
    nombre VARCHAR(255) NOT NULL
);

CREATE TABLE Editoriales (
    id INT PRIMARY KEY,
    nombre VARCHAR(255) NOT NULL,
    direccion VARCHAR(255) NOT NULL
);

CREATE TABLE Estantes (
    id INT PRIMARY KEY,
    numero INT NOT NULL
);

CREATE TABLE Categorias (
    id INT PRIMARY KEY,
    nombre VARCHAR(255) NOT NULL
);
