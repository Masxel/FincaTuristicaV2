
CREATE DATABASE db_fincaturistica;
USE db_fincaturistica;

-- Tabla para registrar las reservas realizadas por los clientes.
CREATE TABLE `db_fincaturistica`.`reserva` (
	`id` INT AUTO_INCREMENT NOT NULL,
    `fechallegada` DATE NOT NULL,
    `fechasalida` DATE NOT NULL,
    `idcliente` int NOT NULL,
    `idhabitacion` int NOT NULL,
    `estadoreserva` int NOT NULL,
    `idevento` int NULL,
    PRIMARY KEY(`id`),
    CONSTRAINT `fk_reserva__cliente` FOREIGN KEY (`idcliente`) REFERENCES `cliente`(`id`),
    CONSTRAINT `fk_reserva__habitacion` FOREIGN KEY (`idhabitacion`) REFERENCES `habitacion`(`id`),
    CONSTRAINT `fk_reserva__estado` FOREIGN KEY (`estadoreserva`) REFERENCES `estadoreserva`(`id`),
    CONSTRAINT `fk_reserva__evento` FOREIGN KEY (`idevento`) REFERENCES `eventos`(`id`)
);


-- Tabla para registrar los estados de las reservas, como pendiente, confirmada, cancelada, etc.
CREATE TABLE `db_fincaturistica`.`estadoreserva` (
    `id` INT AUTO_INCREMENT NOT NULL,
    `descripcion` VARCHAR(45) NOT NULL,
    PRIMARY KEY(`id`)
);

-- Tabla para registrar los tipos de eventos disponibles como decoración aniversario, cumpleaños, amor, dia de sol, etc.
CREATE TABLE `db_fincaturistica`.`eventos` (
    `id` INT AUTO_INCREMENT NOT NULL,
    `descripcion` VARCHAR(200) NOT NULL,        
    PRIMARY KEY(`id`)
);

-- Tabla para registrar las habitaciones disponibles en la finca turistica.
CREATE TABLE `db_fincaturistica`.`habitacion` (
	`id` INT AUTO_INCREMENT NOT NULL,
    `tipohabitacion` VARCHAR(45) NOT NULL,
    `precio` int NOT NULL,
    `capacidad` int NOT NULL,
    `estado` int NOT NULL,
    `descripcion` VARCHAR(200) NOT NULL,
    PRIMARY KEY(`id`),
    CONSTRAINT `fk_habitacion__estado` FOREIGN KEY (`estado`) REFERENCES `estadohabitacion`(`id`)
);

-- Tabla para registrar los estados de las habitaciones, como disponible, ocupada, en mantenimiento, etc.
CREATE TABLE `db_fincaturistica`.`estadohabitacion` (
    `id` INT AUTO_INCREMENT NOT NULL,
    `descripcion` VARCHAR(45) NOT NULL,
    PRIMARY KEY(`id`)
);

-- Tabla para registrar los empleados de la finca turistica.
CREATE TABLE `db_fincaturistica`.`empleados` (
    `id` INT AUTO_INCREMENT NOT NULL,
    `nombre` VARCHAR(45) NOT NULL,
    `apellido` VARCHAR(45) NOT NULL,
    `telefono` VARCHAR(15) NOT NULL,
    `email` VARCHAR(45) NOT NULL,
    `cargo` int NOT NULL,
    PRIMARY KEY(`id`),
    CONSTRAINT `fk_empleados__cargo` FOREIGN KEY (`cargo`) REFERENCES `cargo`(`id`)
);

-- Tabla para registrar los cargos de los empleados, como administrador, recepcionista, personal de limpieza, etc.
CREATE TABLE `db_fincaturistica`.`cargo` (
    `id` INT AUTO_INCREMENT NOT NULL,
    `descripcion` VARCHAR(45) NOT NULL,
    PRIMARY KEY(`id`)
);

-- Tabla para registrar los insumos que se utilizan en la finca turistica, como productos de limpieza, almohadas, toallas, etc.
CREATE TABLE `db_fincaturistica`.`insumos` (
    `id` INT AUTO_INCREMENT NOT NULL,
    `nombre` VARCHAR(45) NOT NULL,
    `cantidad` int NOT NULL,
    `descripcion` VARCHAR(200) NOT NULL, 
    `precio` int NOT NULL,
    PRIMARY KEY(`id`)
);

-- Tabla para registrar los clientes que hacen reservas en la finca turistica.
CREATE TABLE `db_fincaturistica`.`cliente` (
    `id` INT AUTO_INCREMENT NOT NULL,
    `nombre` VARCHAR(45) NOT NULL,
    `apellido` VARCHAR(45) NOT NULL,
    `telefono` VARCHAR(15) NOT NULL,
    `email` VARCHAR(45) NOT NULL,
    PRIMARY KEY(`id`)
);

-- Tabla para registrar las facturas generadas por las reservas.
CREATE TABLE `db_fincaturistica`.`factura` (
    `id` INT AUTO_INCREMENT NOT NULL,
    `fecha` DATE NOT NULL,
    `total` int NOT NULL,
    `idreserva` int NOT NULL,
    `idmetodopago` int NOT NULL,
    PRIMARY KEY(`id`),
    CONSTRAINT `fk_factura__reserva` FOREIGN KEY (`idreserva`) REFERENCES `reserva`(`id`),
    CONSTRAINT `fk_factura__metodo_pago` FOREIGN KEY (`idmetodopago`) REFERENCES `metodo_pago`(`id`)
);

-- Metodos de pago como efectivo, tarjeta de credito, transferencia bancaria, etc.
CREATE TABLE `db_fincaturistica`.`metodo_pago` (
    `id` INT AUTO_INCREMENT NOT NULL,
    `descripcion` VARCHAR(45) NOT NULL,
    PRIMARY KEY(`id`)
);

--Son zonas como piscinas, jacuzzis, canchas deportivas, salones de eventos, cabalgatas, etc.
CREATE TABLE `db_fincaturistica`.`zonas_entretenimiento` (
    `id` INT AUTO_INCREMENT NOT NULL,
    `nombre` VARCHAR(45) NOT NULL,
    `descripcion` VARCHAR(200) NOT NULL,
    `estado` int NOT NULL,
    PRIMARY KEY(`id`)
);

-- Reseñas y calificaciones que los clientes dejan sobre su experiencia en la finca turistica.
CREATE TABLE `db_fincaturistica`.`opinion` (
    `id` INT AUTO_INCREMENT NOT NULL,
    `idcliente` int NOT NULL,
    `calificacion` int NOT NULL,
    `comentario` VARCHAR(500) NOT NULL,
    PRIMARY KEY(`id`),
    CONSTRAINT `fk_opinion__cliente` FOREIGN KEY (`idcliente`) REFERENCES `cliente`(`id`)
);

-- Menus de la semana para el restaurante de la finca turistica.
CREATE TABLE `db_fincaturistica`.`menualimentacion` (
    `id` INT AUTO_INCREMENT NOT NULL,
    `dia` VARCHAR(15) NOT NULL,
    `plato_principal` VARCHAR(100) NOT NULL,
    `acompanamiento` VARCHAR(100) NOT NULL,
    `postre` VARCHAR(100) NOT NULL,
    PRIMARY KEY(`id`)
);

-- Tienda donde los clientes pueden comprar recuerdos de su estadia en la finca turistica, cremas, bloqueadores, insecticidas, etc.
CREATE TABLE `db_fincaturistica`.`tienda_local` (
    `id` INT AUTO_INCREMENT NOT NULL,
    `nombre` VARCHAR(100) NOT NULL,
    `descripcion` VARCHAR(200) NOT NULL,
    `precio` int NOT NULL,
    `cantidaddisponible` int NOT NULL,
    PRIMARY KEY(`id`)
);


-- ==================== VALORES INICIALES PARA TRABAJAR CON LAS TABLAS CREADAS ===================== --
-- Los valores son basicos para el inicio de un producto, como llenar estados, cargos, metodos de pago, tienda local, etc.
-- Pero que no hacen parte del proyecto final, ya que estos valores pueden ser modificados por el administrador.

INSERT INTO `db_fincaturistica`.`estadoreserva` (`descripcion`) VALUES
('Pendiente'),
('Confirmada'),
('Cancelada');

INSERT INTO `db_fincaturistica`.`eventos` (`descripcion`) VALUES
('Decoracion aniversario'),
('Decoracion cumpleaños'),
('Decoracion amor y amistad'),
('Decoracion dia de sol');

INSERT INTO `db_fincaturistica`.`estadohabitacion` (`descripcion`) VALUES
('Disponible'),
('Ocupada'),
('En mantenimiento');

INSERT INTO `db_fincaturistica`.`cargo` (`descripcion`) VALUES
('Administrador'),
('Recepcionista'),
('Personal de limpieza');

INSERT INTO `db_fincaturistica`.`insumos` (`nombre`, `cantidad`, `descripcion`, `precio`) VALUES
('Jabón', 100, 'Jabón para limpieza', 500),
('Toalla', 50, 'Toalla de baño', 1500),
('Almohada', 30, 'Almohada de plumas', 2000),
('Cobija', 20, 'Cobija para cama doble', 3000);

INSERT INTO `db_fincaturistica`.`metodo_pago` (`descripcion`) VALUES
('Efectivo'),
('Tarjeta de credito'),
('Transferencia bancaria');

INSERT INTO `db_fincaturistica`.`zonas_entretenimiento` (`nombre`, `descripcion`, `estado`) VALUES
('Piscina', 'Zona de relajacion con piscina', 1),
('Jacuzzi', 'Zona de relajacion con jacuzzi', 1),
('Cancha de tenis', 'Zona deportiva', 1);

INSERT INTO `db_fincaturistica`.`menualimentacion` (`dia`, `plato_principal`, `acompanamiento`, `postre`) VALUES
('Lunes', 'Pollo asado', 'Ensalada', 'Yogurt con frutas'),
('Martes', 'Pastas', 'Pan de ajo', 'Pastel'),
('Miércoles', 'Salmón', 'Arroz', 'Helado');

INSERT INTO `db_fincaturistica`.`tienda_local` (`nombre`, `descripcion`, `precio`, `cantidaddisponible`) VALUES
('Crema solar', 'Proteccion solar', 20000, 100),
('Insecticida', 'Repelente contra insectos', 15000, 50),
('Recuerdo de la finca', 'Iman de nevera', 5000, 200);

-- ==================== PROCEDIMIENTOS ALMACENADOS PARA REGISTRAR NUEVOS INSUMOS ===================== --
DELIMITER $$

CREATE PROCEDURE `db_fincaturistica`.`proc_insertar_insumos` (
    IN _nombre VARCHAR(45),
    IN _cantidad INT,
    IN _descripcion VARCHAR(200),
    IN _precio INT,
    INOUT _respuesta INT
)
BEGIN
    SET _respuesta = 0;
    INSERT INTO `db_fincaturistica`.`insumos` (`nombre`, `cantidad`, `descripcion`, `precio`)
    VALUES (_nombre, _cantidad, _descripcion, _precio);
    SET _respuesta = LAST_INSERT_ID();
END $$
-- ====================================================================================== --

-- ==================== PROCEDIMIENTOS ALMACENADOS PARA CONSULTAR TODOS LOS INSUMOS ===================== --
DELIMITER $$

CREATE PROCEDURE `db_fincaturistica`.`proc_consultar_todos_insumos` ()
BEGIN
    SELECT `id`, `nombre`, `cantidad`, `descripcion`, `precio`
    FROM `db_fincaturistica`.`insumos`;
END $$

-- ====================================================================================== --

-- =================== PROCEDIMIENTOS ALMACENADOS PARA ELIMINAR INSUMO ===================== --

DELIMITER $$
CREATE PROCEDURE `db_fincaturistica`.`proc_eliminar_insumo` (
    IN _id INT,
    INOUT _respuesta INT
)
BEGIN
    SET _respuesta = 0;
    DELETE FROM `db_fincaturistica`.`insumos`
    WHERE `id` = _id;

    SET _respuesta = ROW_COUNT();
END $$
-- ====================================================================================== --

-- =================== PROCEDIMIENTOS ALMACENADOS PARA ACTUALIZAR INSUMO ===================== --
DELIMITER $$

CREATE PROCEDURE `db_fincaturistica`.`proc_actualizar_insumo` (
    IN _id INT,
    IN _nombre VARCHAR(45),
    IN _cantidad INT,
    IN _descripcion VARCHAR(200),
    IN _precio INT,
    INOUT _respuesta INT
)
BEGIN
    SET _respuesta = 0;
    UPDATE `db_fincaturistica`.`insumos`
    SET `nombre` = _nombre,
        `cantidad` = _cantidad,
        `descripcion` = _descripcion,
        `precio` = _precio
    WHERE `id` = _id;
    SET _respuesta = ROW_COUNT();
END $$
-- ====================================================================================== --

-- ==================== PROCEDIMIENTOS ALMACENADOS PARA TIENDA LOCAL ===================== --

-- ==================== INSERTAR PRODUCTO EN TIENDA LOCAL ===================== --
DELIMITER $$

CREATE PROCEDURE `db_fincaturistica`.`proc_insertar_tienda_local` (
    IN _nombre VARCHAR(100),
    IN _descripcion VARCHAR(200),
    IN _precio INT,
    IN _cantidaddisponible INT,
    INOUT _respuesta INT
)
BEGIN
    SET _respuesta = 0;
    INSERT INTO `db_fincaturistica`.`tienda_local` (`nombre`, `descripcion`, `precio`, `cantidaddisponible`)
    VALUES (_nombre, _descripcion, _precio, _cantidaddisponible);
    SET _respuesta = LAST_INSERT_ID();
END $$
-- ====================================================================================== --

-- ==================== CONSULTAR TODOS LOS PRODUCTOS DE TIENDA LOCAL ===================== --
DELIMITER $$

CREATE PROCEDURE `db_fincaturistica`.`proc_consultar_todos_tienda_local` ()
BEGIN
    SELECT `id`, `nombre`, `descripcion`, `precio`, `cantidaddisponible`
    FROM `db_fincaturistica`.`tienda_local`;
END $$
-- ====================================================================================== --

-- ==================== ACTUALIZAR PRODUCTO DE TIENDA LOCAL ===================== --
DELIMITER $$

CREATE PROCEDURE `db_fincaturistica`.`proc_actualizar_tienda_local` (
    IN _id INT,
    IN _nombre VARCHAR(100),
    IN _descripcion VARCHAR(200),
    IN _precio INT,
    IN _cantidaddisponible INT,
    INOUT _respuesta INT
)
BEGIN
    SET _respuesta = 0;
    UPDATE `db_fincaturistica`.`tienda_local`
    SET `nombre` = _nombre,
        `descripcion` = _descripcion,
        `precio` = _precio,
        `cantidaddisponible` = _cantidaddisponible
    WHERE `id` = _id;
    SET _respuesta = ROW_COUNT();
END $$
-- ====================================================================================== --

-- ==================== ELIMINAR PRODUCTO DE TIENDA LOCAL ===================== --
DELIMITER $$

CREATE PROCEDURE `db_fincaturistica`.`proc_eliminar_tienda_local` (
    IN _id INT,
    INOUT _respuesta INT
)
BEGIN
    SET _respuesta = 0;
    DELETE FROM `db_fincaturistica`.`tienda_local`
    WHERE `id` = _id;
    SET _respuesta = ROW_COUNT();
END $$
-- ====================================================================================== --

-- ==================== PROCEDIMIENTOS ALMACENADOS PARA CLIENTES ===================== --

-- ==================== INSERTAR CLIENTE ===================== --
DELIMITER $$

CREATE PROCEDURE `db_fincaturistica`.`proc_insertar_cliente` (
    IN _nombre VARCHAR(45),
    IN _apellido VARCHAR(45),
    IN _telefono VARCHAR(15),
    IN _email VARCHAR(45),
    INOUT _respuesta INT
)
BEGIN
    SET _respuesta = 0;
    INSERT INTO `db_fincaturistica`.`cliente` (`nombre`, `apellido`, `telefono`, `email`)
    VALUES (_nombre, _apellido, _telefono, _email);
    SET _respuesta = LAST_INSERT_ID();
END $$
-- ====================================================================================== --

-- ==================== CONSULTAR TODOS LOS CLIENTES ===================== --
DELIMITER $$

CREATE PROCEDURE `db_fincaturistica`.`proc_consultar_todos_clientes` ()
BEGIN
    SELECT `id`, `nombre`, `apellido`, `telefono`, `email`
    FROM `db_fincaturistica`.`cliente`;
END $$
-- ====================================================================================== --

-- ==================== ACTUALIZAR CLIENTE ===================== --
DELIMITER $$

CREATE PROCEDURE `db_fincaturistica`.`proc_actualizar_cliente` (
    IN _id INT,
    IN _nombre VARCHAR(45),
    IN _apellido VARCHAR(45),
    IN _telefono VARCHAR(15),
    IN _email VARCHAR(45),
    INOUT _respuesta INT
)
BEGIN
    SET _respuesta = 0;
    UPDATE `db_fincaturistica`.`cliente`
    SET `nombre` = _nombre,
        `apellido` = _apellido,
        `telefono` = _telefono,
        `email` = _email
    WHERE `id` = _id;
    SET _respuesta = ROW_COUNT();
END $$
-- ====================================================================================== --

-- ==================== ELIMINAR CLIENTE ===================== --
DELIMITER $$

CREATE PROCEDURE `db_fincaturistica`.`proc_eliminar_cliente` (
    IN _id INT,
    INOUT _respuesta INT
)
BEGIN
    SET _respuesta = 0;
    DELETE FROM `db_fincaturistica`.`cliente`
    WHERE `id` = _id;
    SET _respuesta = ROW_COUNT();
END $$
-- ====================================================================================== --

-- ==================== PROCEDIMIENTOS ALMACENADOS PARA HABITACIONES ===================== --

-- ==================== INSERTAR HABITACION ===================== --
DELIMITER $$

CREATE PROCEDURE `db_fincaturistica`.`proc_insertar_habitacion` (
    IN _tipohabitacion VARCHAR(45),
    IN _precio INT,
    IN _capacidad INT,
    IN _estado INT,
    IN _descripcion VARCHAR(200),
    INOUT _respuesta INT
)
BEGIN
    SET _respuesta = 0;
    INSERT INTO `db_fincaturistica`.`habitacion` (`tipohabitacion`, `precio`, `capacidad`, `estado`, `descripcion`)
    VALUES (_tipohabitacion, _precio, _capacidad, _estado, _descripcion);
    SET _respuesta = LAST_INSERT_ID();
END $$
-- ====================================================================================== --

-- ==================== CONSULTAR TODAS LAS HABITACIONES ===================== --
DELIMITER $$

CREATE PROCEDURE `db_fincaturistica`.`proc_consultar_todas_habitaciones` ()
BEGIN
    SELECT h.`id`, h.`tipohabitacion`, h.`precio`, h.`capacidad`, h.`estado`, h.`descripcion`, eh.`descripcion` as estado_descripcion
    FROM `db_fincaturistica`.`habitacion` h
    INNER JOIN `db_fincaturistica`.`estadohabitacion` eh ON h.`estado` = eh.`id`;
END $$
-- ====================================================================================== --

-- ==================== ACTUALIZAR HABITACION ===================== --
DELIMITER $$

CREATE PROCEDURE `db_fincaturistica`.`proc_actualizar_habitacion` (
    IN _id INT,
    IN _tipohabitacion VARCHAR(45),
    IN _precio INT,
    IN _capacidad INT,
    IN _estado INT,
    IN _descripcion VARCHAR(200),
    INOUT _respuesta INT
)
BEGIN
    SET _respuesta = 0;
    UPDATE `db_fincaturistica`.`habitacion`
    SET `tipohabitacion` = _tipohabitacion,
        `precio` = _precio,
        `capacidad` = _capacidad,
        `estado` = _estado,
        `descripcion` = _descripcion
    WHERE `id` = _id;
    SET _respuesta = ROW_COUNT();
END $$
-- ====================================================================================== --

-- ==================== ELIMINAR HABITACION ===================== --
DELIMITER $$

CREATE PROCEDURE `db_fincaturistica`.`proc_eliminar_habitacion` (
    IN _id INT,
    INOUT _respuesta INT
)
BEGIN
    SET _respuesta = 0;
    DELETE FROM `db_fincaturistica`.`habitacion`
    WHERE `id` = _id;
    SET _respuesta = ROW_COUNT();
END $$
-- ====================================================================================== --

-- ==================== PROCEDIMIENTOS ALMACENADOS PARA RESERVAS ===================== --

-- ==================== INSERTAR RESERVA ===================== --
DELIMITER $$

CREATE PROCEDURE `db_fincaturistica`.`proc_insertar_reserva` (
    IN _fechallegada DATE,
    IN _fechasalida DATE,
    IN _idcliente INT,
    IN _idhabitacion INT,
    IN _estadoreserva INT,
    IN _idevento INT,
    INOUT _respuesta INT
)
BEGIN
    SET _respuesta = 0;
    INSERT INTO `db_fincaturistica`.`reserva` (`fechallegada`, `fechasalida`, `idcliente`, `idhabitacion`, `estadoreserva`, `idevento`)
    VALUES (_fechallegada, _fechasalida, _idcliente, _idhabitacion, _estadoreserva, _idevento);
    SET _respuesta = LAST_INSERT_ID();
END $$
-- ====================================================================================== --

-- ==================== CONSULTAR TODAS LAS RESERVAS ===================== --
DELIMITER $$

CREATE PROCEDURE `db_fincaturistica`.`proc_consultar_todas_reservas` ()
BEGIN
    SELECT r.`id`, r.`fechallegada`, r.`fechasalida`, r.`idcliente`, r.`idhabitacion`, r.`estadoreserva`, r.`idevento`,
           CONCAT(c.`nombre`, ' ', c.`apellido`) as cliente_nombre,
           CONCAT(h.`tipohabitacion`, ' - ', h.`descripcion`) as habitacion_info,
           er.`descripcion` as estado_descripcion,
           e.`descripcion` as evento_descripcion
    FROM `db_fincaturistica`.`reserva` r
    INNER JOIN `db_fincaturistica`.`cliente` c ON r.`idcliente` = c.`id`
    INNER JOIN `db_fincaturistica`.`habitacion` h ON r.`idhabitacion` = h.`id`
    INNER JOIN `db_fincaturistica`.`estadoreserva` er ON r.`estadoreserva` = er.`id`
    LEFT JOIN `db_fincaturistica`.`eventos` e ON r.`idevento` = e.`id`;
END $$
-- ====================================================================================== --

-- ==================== ACTUALIZAR RESERVA ===================== --
DELIMITER $$

CREATE PROCEDURE `db_fincaturistica`.`proc_actualizar_reserva` (
    IN _id INT,
    IN _fechallegada DATE,
    IN _fechasalida DATE,
    IN _idcliente INT,
    IN _idhabitacion INT,
    IN _estadoreserva INT,
    IN _idevento INT,
    INOUT _respuesta INT
)
BEGIN
    SET _respuesta = 0;
    UPDATE `db_fincaturistica`.`reserva`
    SET `fechallegada` = _fechallegada,
        `fechasalida` = _fechasalida,
        `idcliente` = _idcliente,
        `idhabitacion` = _idhabitacion,
        `estadoreserva` = _estadoreserva,
        `idevento` = _idevento
    WHERE `id` = _id;
    SET _respuesta = ROW_COUNT();
END $$
-- ====================================================================================== --

-- ==================== ELIMINAR RESERVA ===================== --
DELIMITER $$

CREATE PROCEDURE `db_fincaturistica`.`proc_eliminar_reserva` (
    IN _id INT,
    INOUT _respuesta INT
)
BEGIN
    SET _respuesta = 0;
    DELETE FROM `db_fincaturistica`.`reserva`
    WHERE `id` = _id;
    SET _respuesta = ROW_COUNT();
END $$
-- ====================================================================================== --

-- ==================== PROCEDIMIENTOS ALMACENADOS PARA ESTADOS DE RESERVA ===================== --

-- ==================== CONSULTAR ESTADOS DE RESERVA ===================== --
DELIMITER $$

CREATE PROCEDURE `db_fincaturistica`.`proc_consultar_estados_reserva` ()
BEGIN
    SELECT `id`, `descripcion`
    FROM `db_fincaturistica`.`estadoreserva`
    ORDER BY `id`;
END $$
-- ====================================================================================== --

-- ==================== PROCEDIMIENTOS ALMACENADOS PARA EVENTOS ===================== --

-- ==================== CONSULTAR EVENTOS DISPONIBLES ===================== --
DELIMITER $$

CREATE PROCEDURE `db_fincaturistica`.`proc_consultar_eventos` ()
BEGIN
    SELECT `id`, `descripcion`
    FROM `db_fincaturistica`.`eventos`
    ORDER BY `id`;
END $$
-- ====================================================================================== --