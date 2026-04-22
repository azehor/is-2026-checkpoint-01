-- Creacion de la tabla members
CREATE TABLE members (
    id SERIAL PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    apellido VARCHAR(100) NOT NULL,
    legajo VARCHAR(20) UNIQUE NOT NULL,
    feature VARCHAR(50) NOT NULL,
    servicio VARCHAR(100) NOT NULL,
    estado VARCHAR(20) NOT NULL,
);

-- Insercion de datos en la tabla members
INSERT INTO members (nombre, apellido, legajo, feature, servicio, estado) VALUES
('Juan Ignacio', 'Piazza', '31402', 'Feature 01', 'Infraestructura Base', 'Activo'),
('Ignacio', 'Williams', '33365', 'Feature 02', 'Backend', 'Activo'),
('Avril', 'Lugo Gonzalez', '33130', 'Feature 03', 'Frontend', 'Activo');
('Alfredo', 'Echeverría', '32850', 'Feature 04', 'Database', 'Activo');
('Nahuel Fabián', 'Fredes Coronilla', '32059', 'Feature 05', 'Portainer', 'Activo');