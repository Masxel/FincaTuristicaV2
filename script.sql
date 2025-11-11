
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
    `id` INT NOT NULL,
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
    IN _id INT,
    IN _nombre VARCHAR(45),
    IN _apellido VARCHAR(45),
    IN _telefono VARCHAR(15),
    IN _email VARCHAR(45),
    INOUT _respuesta INT
)
BEGIN
   BEGIN
    INSERT INTO `db_fincaturistica`.`cliente` (`id`, `nombre`, `apellido`, `telefono`, `email`)
    VALUES (_id, _nombre, _apellido, _telefono, _email);
    
    IF ROW_COUNT() > 0 THEN
        SET _respuesta = _id; 
    ELSE
        SET _respuesta = 0; 
    END IF;
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

-- ==================== CONSULTAR CLIENTE POR ID ===================== --
DELIMITER $$

CREATE PROCEDURE `db_fincaturistica`.`proc_consultar_cliente_por_id` (
    IN _id INT
)
BEGIN
    SELECT `id`, `nombre`, `apellido`, `telefono`, `email`
    FROM `db_fincaturistica`.`cliente`
    WHERE `id` = _id;
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

-- ==================== INSERTAR EVENTO ===================== --
DELIMITER $$

CREATE PROCEDURE `db_fincaturistica`.`proc_insertar_evento` (
    IN p_descripcion VARCHAR(200)
)
BEGIN
    DECLARE EXIT HANDLER FOR SQLEXCEPTION
    BEGIN
        ROLLBACK;
        RESIGNAL;
    END;
    
    START TRANSACTION;
    
    INSERT INTO `db_fincaturistica`.`eventos` (`descripcion`)
    VALUES (p_descripcion);
    
    COMMIT;
END $$
-- ====================================================================================== --

-- ==================== CONSULTAR EVENTOS DISPONIBLES ===================== --
DELIMITER $$

CREATE PROCEDURE `db_fincaturistica`.`proc_consultar_eventos` ()
BEGIN
    SELECT `id`, `descripcion`
    FROM `db_fincaturistica`.`eventos`
    ORDER BY `id`;
END $$

-- ====================================================================================== --

-- ==================== CONSULTAR EVENTO POR ID ===================== --
DELIMITER $$

CREATE PROCEDURE `db_fincaturistica`.`proc_consultar_evento_por_id` (
    IN p_id INT
)
BEGIN
    SELECT `id`, `descripcion`
    FROM `db_fincaturistica`.`eventos`
    WHERE `id` = p_id;
END $$
-- ====================================================================================== --

-- ==================== ACTUALIZAR EVENTO ===================== --
DELIMITER $$

CREATE PROCEDURE `db_fincaturistica`.`proc_actualizar_evento` (
    IN p_id INT,
    IN p_descripcion VARCHAR(200)
)
BEGIN
    DECLARE EXIT HANDLER FOR SQLEXCEPTION
    BEGIN
        ROLLBACK;
        RESIGNAL;
    END;
    
    START TRANSACTION;
    
    UPDATE `db_fincaturistica`.`eventos`
    SET `descripcion` = p_descripcion
    WHERE `id` = p_id;
    
    COMMIT;
END $$
-- ====================================================================================== --

-- ==================== ELIMINAR EVENTO ===================== --
DELIMITER $$

CREATE PROCEDURE `db_fincaturistica`.`proc_eliminar_evento` (
    IN p_id INT
)
BEGIN
    DECLARE EXIT HANDLER FOR SQLEXCEPTION
    BEGIN
        ROLLBACK;
        RESIGNAL;
    END;
    
    START TRANSACTION;
    
    DELETE FROM `db_fincaturistica`.`eventos`
    WHERE `id` = p_id;
    
    COMMIT;
END $$

DELIMITER ;
-- ====================================================================================== --

-- ==================== PROCEDIMIENTOS ALMACENADOS PARA EMPLEADOS ===================== --

-- ==================== INSERTAR EMPLEADO ===================== --
DELIMITER $$

CREATE PROCEDURE `db_fincaturistica`.`proc_insertar_empleado` (
    IN p_id INT,
    IN p_nombre VARCHAR(45),
    IN p_apellido VARCHAR(45),
    IN p_telefono VARCHAR(15),
    IN p_email VARCHAR(45),
    IN p_cargo INT
)
BEGIN
    DECLARE EXIT HANDLER FOR SQLEXCEPTION
    BEGIN
        ROLLBACK;
        RESIGNAL;
    END;
    
    START TRANSACTION;

    INSERT INTO `db_fincaturistica`.`empleados` (`id`, `nombre`, `apellido`, `telefono`, `email`, `cargo`)
    VALUES (p_id, p_nombre, p_apellido, p_telefono, p_email, p_cargo);

    COMMIT;
END $$
-- ====================================================================================== --

-- ==================== CONSULTAR TODOS LOS EMPLEADOS ===================== --
DELIMITER $$

CREATE PROCEDURE `db_fincaturistica`.`proc_consultar_empleados` ()
BEGIN
    SELECT e.`id`, e.`nombre`, e.`apellido`, e.`telefono`, e.`email`, e.`cargo`, c.`descripcion` as `cargo_descripcion`
    FROM `db_fincaturistica`.`empleados` e
    LEFT JOIN `db_fincaturistica`.`cargo` c ON e.`cargo` = c.`id`
    ORDER BY e.`id`;
END $$

-- ====================================================================================== --

-- ==================== CONSULTAR EMPLEADO POR ID ===================== --
DELIMITER $$

CREATE PROCEDURE `db_fincaturistica`.`proc_consultar_empleado_por_id` (
    IN p_id INT
)
BEGIN
    SELECT e.`id`, e.`nombre`, e.`apellido`, e.`telefono`, e.`email`, e.`cargo`, c.`descripcion` as `cargo_descripcion`
    FROM `db_fincaturistica`.`empleados` e
    LEFT JOIN `db_fincaturistica`.`cargo` c ON e.`cargo` = c.`id`
    WHERE e.`id` = p_id;
END $$

-- ====================================================================================== --

-- ==================== ACTUALIZAR EMPLEADO ===================== --
DELIMITER $$

CREATE PROCEDURE `db_fincaturistica`.`proc_actualizar_empleado` (
    IN p_id INT,
    IN p_nombre VARCHAR(45),
    IN p_apellido VARCHAR(45),
    IN p_telefono VARCHAR(15),
    IN p_email VARCHAR(45),
    IN p_cargo INT
)
BEGIN
    DECLARE EXIT HANDLER FOR SQLEXCEPTION
    BEGIN
        ROLLBACK;
        RESIGNAL;
    END;
    
    START TRANSACTION;
    
    UPDATE `db_fincaturistica`.`empleados`
    SET `nombre` = p_nombre,
        `apellido` = p_apellido,
        `telefono` = p_telefono,
        `email` = p_email,
        `cargo` = p_cargo
    WHERE `id` = p_id;
    
    COMMIT;
END $$

-- ====================================================================================== --

-- ==================== ELIMINAR EMPLEADO ===================== --
DELIMITER $$

CREATE PROCEDURE `db_fincaturistica`.`proc_eliminar_empleado` (
    IN p_id INT
)
BEGIN
    DECLARE EXIT HANDLER FOR SQLEXCEPTION
    BEGIN
        ROLLBACK;
        RESIGNAL;
    END;
    
    START TRANSACTION;
    
    DELETE FROM `db_fincaturistica`.`empleados`
    WHERE `id` = p_id;
    
    COMMIT;
END $$

-- ====================================================================================== --

-- ==================== PROCEDIMIENTOS ALMACENADOS PARA CARGO ===================== --

-- ==================== INSERTAR CARGO ===================== --
DELIMITER $$

CREATE PROCEDURE `db_fincaturistica`.`proc_insertar_cargo` (
    IN p_descripcion VARCHAR(45)
)
BEGIN
    DECLARE EXIT HANDLER FOR SQLEXCEPTION
    BEGIN
        ROLLBACK;
        RESIGNAL;
    END;
    
    START TRANSACTION;
    
    INSERT INTO `db_fincaturistica`.`cargo` (`descripcion`)
    VALUES (p_descripcion);
    
    COMMIT;
END $$
-- ====================================================================================== --

-- ==================== CONSULTAR TODOS LOS CARGOS ===================== --
DELIMITER $$

CREATE PROCEDURE `db_fincaturistica`.`proc_consultar_cargos` ()
BEGIN
    SELECT `id`, `descripcion`
    FROM `db_fincaturistica`.`cargo`
    ORDER BY `id`;
END $$
-- ====================================================================================== --

-- ==================== ACTUALIZAR CARGO ===================== --
DELIMITER $$

CREATE PROCEDURE `db_fincaturistica`.`proc_actualizar_cargo` (
    IN p_id INT,
    IN p_descripcion VARCHAR(45)
)
BEGIN
    DECLARE EXIT HANDLER FOR SQLEXCEPTION
    BEGIN
        ROLLBACK;
        RESIGNAL;
    END;
    
    START TRANSACTION;
    
    UPDATE `db_fincaturistica`.`cargo`
    SET `descripcion` = p_descripcion
    WHERE `id` = p_id;
    
    COMMIT;
END $$
-- ====================================================================================== --

-- ==================== ELIMINAR CARGO ===================== --
DELIMITER $$

CREATE PROCEDURE `db_fincaturistica`.`proc_eliminar_cargo` (
    IN p_id INT
)
BEGIN
    DECLARE EXIT HANDLER FOR SQLEXCEPTION
    BEGIN
        ROLLBACK;
        RESIGNAL;
    END;
    
    START TRANSACTION;
    
    DELETE FROM `db_fincaturistica`.`metodo_pago`
    WHERE `id` = p_id;
    
    COMMIT;
END $$
-- ====================================================================================== --

-- ==================== PROCEDIMIENTOS ALMACENADOS PARA MENÚ ALIMENTACIÓN ===================== --

-- ==================== INSERTAR MENÚ ALIMENTACIÓN ===================== --
DELIMITER $$

CREATE PROCEDURE `db_fincaturistica`.`proc_insertar_menu_alimentacion` (
    IN p_dia VARCHAR(15),
    IN p_plato_principal VARCHAR(100),
    IN p_acompanamiento VARCHAR(100),
    IN p_postre VARCHAR(100)
)
BEGIN
    DECLARE EXIT HANDLER FOR SQLEXCEPTION
    BEGIN
        ROLLBACK;
        RESIGNAL;
    END;
    
    START TRANSACTION;
    
    INSERT INTO `db_fincaturistica`.`menualimentacion` (`dia`, `plato_principal`, `acompanamiento`, `postre`)
    VALUES (p_dia, p_plato_principal, p_acompanamiento, p_postre);
    
    COMMIT;
END $$
-- ====================================================================================== --

-- ==================== CONSULTAR MENÚS DE ALIMENTACIÓN ===================== --
DELIMITER $$

CREATE PROCEDURE `db_fincaturistica`.`proc_consultar_menus_alimentacion` ()
BEGIN
    SELECT `id`, `dia`, `plato_principal`, `acompanamiento`, `postre`
    FROM `db_fincaturistica`.`menualimentacion`
    ORDER BY `id`;
END $$
-- ====================================================================================== --

-- ==================== ACTUALIZAR MENÚ ALIMENTACIÓN ===================== --
DELIMITER $$

CREATE PROCEDURE `db_fincaturistica`.`proc_actualizar_menu_alimentacion` (
    IN p_id INT,
    IN p_dia VARCHAR(15),
    IN p_plato_principal VARCHAR(100),
    IN p_acompanamiento VARCHAR(100),
    IN p_postre VARCHAR(100)
)
BEGIN
    DECLARE EXIT HANDLER FOR SQLEXCEPTION
    BEGIN
        ROLLBACK;
        RESIGNAL;
    END;
    
    START TRANSACTION;
    
    UPDATE `db_fincaturistica`.`menualimentacion`
    SET `dia` = p_dia,
        `plato_principal` = p_plato_principal,
        `acompanamiento` = p_acompanamiento,
        `postre` = p_postre
    WHERE `id` = p_id;
    
    COMMIT;
END $$

-- ====================================================================================== --

-- ==================== ELIMINAR MENÚ ALIMENTACIÓN ===================== --
DELIMITER $$

CREATE PROCEDURE `db_fincaturistica`.`proc_eliminar_menu_alimentacion` (
    IN p_id INT
)
BEGIN
    DECLARE EXIT HANDLER FOR SQLEXCEPTION
    BEGIN
        ROLLBACK;
        RESIGNAL;
    END;
    
    START TRANSACTION;
    
    DELETE FROM `db_fincaturistica`.`menualimentacion`
    WHERE `id` = p_id;
    
    COMMIT;
END $$

DELIMITER ;
-- ====================================================================================== --

-- ==================== PROCEDIMIENTOS ALMACENADOS PARA ZONAS ENTRETENIMIENTO ===================== --

-- ==================== INSERTAR ZONA ENTRETENIMIENTO ===================== --
DELIMITER $$

CREATE PROCEDURE `db_fincaturistica`.`proc_insertar_zona_entretenimiento` (
    IN p_nombre VARCHAR(45),
    IN p_descripcion VARCHAR(200),
    IN p_estado INT
)
BEGIN
    DECLARE EXIT HANDLER FOR SQLEXCEPTION
    BEGIN
        ROLLBACK;
        RESIGNAL;
    END;
    
    START TRANSACTION;
    
    INSERT INTO `db_fincaturistica`.`zonas_entretenimiento` (`nombre`, `descripcion`, `estado`)
    VALUES (p_nombre, p_descripcion, p_estado);
    
    COMMIT;
END $$
-- ====================================================================================== --

-- ==================== CONSULTAR ZONAS DE ENTRETENIMIENTO ===================== --
DELIMITER $$

CREATE PROCEDURE `db_fincaturistica`.`proc_consultar_zonas_entretenimiento` ()
BEGIN
    SELECT `id`, `nombre`, `descripcion`, `estado`
    FROM `db_fincaturistica`.`zonas_entretenimiento`
    ORDER BY `id`;
END $$

-- ====================================================================================== --

-- ==================== ACTUALIZAR ZONA ENTRETENIMIENTO ===================== --
DELIMITER $$

CREATE PROCEDURE `db_fincaturistica`.`proc_actualizar_zona_entretenimiento` (
    IN p_id INT,
    IN p_nombre VARCHAR(45),
    IN p_descripcion VARCHAR(200),
    IN p_estado INT
)
BEGIN
    DECLARE EXIT HANDLER FOR SQLEXCEPTION
    BEGIN
        ROLLBACK;
        RESIGNAL;
    END;
    
    START TRANSACTION;
    
    UPDATE `db_fincaturistica`.`zonas_entretenimiento`
    SET `nombre` = p_nombre,
        `descripcion` = p_descripcion,
        `estado` = p_estado
    WHERE `id` = p_id;
    
    COMMIT;
END $$

-- ====================================================================================== --

-- ==================== ELIMINAR ZONA ENTRETENIMIENTO ===================== --
DELIMITER $$

CREATE PROCEDURE `db_fincaturistica`.`proc_eliminar_zona_entretenimiento` (
    IN p_id INT
)
BEGIN
    DECLARE EXIT HANDLER FOR SQLEXCEPTION
    BEGIN
        ROLLBACK;
        RESIGNAL;
    END;
    
    START TRANSACTION;
    
    DELETE FROM `db_fincaturistica`.`zonas_entretenimiento`
    WHERE `id` = p_id;
    
    COMMIT;
END $$

DELIMITER ;
-- ====================================================================================== --

-- ==================== PROCEDIMIENTOS ALMACENADOS PARA OPINIONES ===================== --

-- ==================== INSERTAR OPINIÓN ===================== --
DELIMITER $$

CREATE PROCEDURE `db_fincaturistica`.`proc_insertar_opinion` (
    IN p_idcliente INT,
    IN p_calificacion INT,
    IN p_comentario VARCHAR(500)
)
BEGIN
    DECLARE EXIT HANDLER FOR SQLEXCEPTION
    BEGIN
        ROLLBACK;
        RESIGNAL;
    END;
    
    START TRANSACTION;
    
    INSERT INTO `db_fincaturistica`.`opinion` (`idcliente`, `calificacion`, `comentario`)
    VALUES (p_idcliente, p_calificacion, p_comentario);
    
    COMMIT;
END $$
-- ====================================================================================== --

-- ==================== CONSULTAR OPINIONES CON INFORMACIÓN DE CLIENTE ===================== --
DELIMITER $$

CREATE PROCEDURE `db_fincaturistica`.`proc_consultar_opiniones` ()
BEGIN
    SELECT o.`id`, o.`idcliente`, c.`nombre`, c.`apellido`, o.`calificacion`, o.`comentario`
    FROM `db_fincaturistica`.`opinion` o
    LEFT JOIN `db_fincaturistica`.`cliente` c ON o.`idcliente` = c.`id`
    ORDER BY o.`id` DESC;
END $$
-- ====================================================================================== --

-- ==================== ACTUALIZAR OPINIÓN ===================== --
DELIMITER $$

CREATE PROCEDURE `db_fincaturistica`.`proc_actualizar_opinion` (
    IN p_id INT,
    IN p_idcliente INT,
    IN p_calificacion INT,
    IN p_comentario VARCHAR(500)
)
BEGIN
    DECLARE EXIT HANDLER FOR SQLEXCEPTION
    BEGIN
        ROLLBACK;
        RESIGNAL;
    END;
    
    START TRANSACTION;
    
    UPDATE `db_fincaturistica`.`opinion`
    SET `idcliente` = p_idcliente,
        `calificacion` = p_calificacion,
        `comentario` = p_comentario
    WHERE `id` = p_id;
    
    COMMIT;
END $$
-- ====================================================================================== --

-- ==================== ELIMINAR OPINIÓN ===================== --
DELIMITER $$

CREATE PROCEDURE `db_fincaturistica`.`proc_eliminar_opinion` (
    IN p_id INT
)
BEGIN
    DECLARE EXIT HANDLER FOR SQLEXCEPTION
    BEGIN
        ROLLBACK;
        RESIGNAL;
    END;
    
    START TRANSACTION;
    
    DELETE FROM `db_fincaturistica`.`opinion`
    WHERE `id` = p_id;
    
    COMMIT;
END $$
-- ====================================================================================== --

-- ====================================================================================== --

-- ==================== PROCEDIMIENTOS ALMACENADOS PARA MÉTODO DE PAGO ===================== --

-- ==================== INSERTAR MÉTODO DE PAGO ===================== --
DELIMITER $$

CREATE PROCEDURE `db_fincaturistica`.`proc_insertar_metodo_pago` (
    IN p_descripcion VARCHAR(45)
)
BEGIN
    DECLARE EXIT HANDLER FOR SQLEXCEPTION
    BEGIN
        ROLLBACK;
        RESIGNAL;
    END;
    
    START TRANSACTION;
    
    INSERT INTO `db_fincaturistica`.`metodo_pago` (`descripcion`)
    VALUES (p_descripcion);
    
    COMMIT;
END $$

-- ====================================================================================== --

-- ==================== CONSULTAR TODOS LOS MÉTODOS DE PAGO ===================== --
DELIMITER $$

CREATE PROCEDURE `db_fincaturistica`.`proc_consultar_metodos_pago` ()
BEGIN
    SELECT `id`, `descripcion`
    FROM `db_fincaturistica`.`metodo_pago`
    ORDER BY `id`;
END $$

-- ====================================================================================== --

-- ==================== ACTUALIZAR MÉTODO DE PAGO ===================== --
DELIMITER $$

CREATE PROCEDURE `db_fincaturistica`.`proc_actualizar_metodo_pago` (
    IN p_id INT,
    IN p_descripcion VARCHAR(45)
)
BEGIN
    DECLARE EXIT HANDLER FOR SQLEXCEPTION
    BEGIN
        ROLLBACK;
        RESIGNAL;
    END;
    
    START TRANSACTION;
    
    UPDATE `db_fincaturistica`.`metodo_pago`
    SET `descripcion` = p_descripcion
    WHERE `id` = p_id;
    
    COMMIT;
END $$
-- ====================================================================================== --

-- ==================== ELIMINAR MÉTODO DE PAGO ===================== --
DELIMITER $$

CREATE PROCEDURE `db_fincaturistica`.`proc_eliminar_metodo_pago` (
    IN p_id INT
)
BEGIN
    DECLARE EXIT HANDLER FOR SQLEXCEPTION
    BEGIN
        ROLLBACK;
        RESIGNAL;
    END;
    
    START TRANSACTION;
    
    DELETE FROM `db_fincaturistica`.`metodo_pago`
    WHERE `id` = p_id;
    
    COMMIT;
END $$
-- ====================================================================================== --

-- ====================================================================================== --

-- ==================== PROCEDIMIENTOS ALMACENADOS PARA MÉTODO DE ESTADO HABITACION ===================== --

-- ==================== INSERTAR ESTADO HABITACION ===================== --
DELIMITER $$
CREATE PROCEDURE `db_fincaturistica`.`proc_insertar_estado_habitacion` (
    IN p_descripcion VARCHAR(45)
)
BEGIN 
    INSERT INTO `db_fincaturistica`.`estadohabitacion` (`descripcion`)
    VALUES (p_descripcion);
END $$
-- ====================================================================================== --

-- ==================== CONSULTAR TODOS LOS ESTADOS DE HABITACION ===================== --
DELIMITER $$

CREATE PROCEDURE `db_fincaturistica`.`proc_consultar_estados_habitacion` ()
BEGIN
    SELECT `id`, `descripcion`
    FROM `db_fincaturistica`.`estadohabitacion`;
END $$
-- ====================================================================================== --

-- ==================== ACTUALIZAR ESTADO HABITACION ===================== --
DELIMITER $$
CREATE PROCEDURE `db_fincaturistica`.`proc_actualizar_estado_habitacion` (
    IN p_id INT,
    IN p_descripcion VARCHAR(45),
    INOUT _respuesta INT
)

BEGIN
    SET _respuesta = 0;
    UPDATE `db_fincaturistica`.`estadohabitacion`
    SET `descripcion` = p_descripcion
    WHERE `id` = p_id;
    SET _respuesta = ROW_COUNT();
END $$
-- ====================================================================================== --

-- ==================== ELIMINAR ESTADO HABITACION ===================== --
DELIMITER $$
CREATE PROCEDURE `db_fincaturistica`.`proc_eliminar_estado_habitacion` (
    IN p_id INT,
    OUT p_respuesta INT
)
BEGIN
    SET p_respuesta = 0;
    DELETE FROM `db_fincaturistica`.`estadohabitacion`
    WHERE `id` = p_id;
    SET p_respuesta = ROW_COUNT();
END $$
-- ====================================================================================== --

-- ==================== PROCEDIMIENTOS ALMACENADOS PARA ESTADO RESERVA ===================== --

-- ==================== INSERTAR ESTADO RESERVA ===================== --
DELIMITER $$

CREATE PROCEDURE `db_fincaturistica`.`proc_insertar_estadoreserva` (
    IN _descripcion VARCHAR(45),
    INOUT _respuesta INT
)
BEGIN
    SET _respuesta = 0;
    INSERT INTO `db_fincaturistica`.`estadoreserva` (`descripcion`)
    VALUES (_descripcion);
    SET _respuesta = LAST_INSERT_ID();
END $$
-- ====================================================================================== --

-- ==================== CONSULTAR TODOS LOS ESTADOS RESERVA ===================== --
DELIMITER $$

CREATE PROCEDURE `db_fincaturistica`.`proc_consultar_todos_estadosreserva` ()
BEGIN
    SELECT `id`, `descripcion`
    FROM `db_fincaturistica`.`estadoreserva`;
END $$
-- ====================================================================================== --

-- ==================== CONSULTAR ESTADO RESERVA POR ID ===================== --
DELIMITER $$

CREATE PROCEDURE `db_fincaturistica`.`proc_consultar_estadoreserva_por_id` (
    IN _id INT
)
BEGIN
    SELECT `id`, `descripcion`
    FROM `db_fincaturistica`.`estadoreserva`
    WHERE `id` = _id;
END $$
-- ====================================================================================== --

-- ==================== ACTUALIZAR ESTADO RESERVA ===================== --
DELIMITER $$

CREATE PROCEDURE `db_fincaturistica`.`proc_actualizar_estadoreserva` (
    IN _id INT,
    IN _descripcion VARCHAR(45),
    INOUT _respuesta INT
)
BEGIN
    SET _respuesta = 0;
    UPDATE `db_fincaturistica`.`estadoreserva`
    SET `descripcion` = _descripcion
    WHERE `id` = _id;
    SET _respuesta = ROW_COUNT();
END $$
-- ====================================================================================== --

-- ==================== ELIMINAR ESTADO RESERVA ===================== --
DELIMITER $$

CREATE PROCEDURE `db_fincaturistica`.`proc_eliminar_estadoreserva` (
    IN _id INT,
    INOUT _respuesta INT
)
BEGIN
    SET _respuesta = 0;
    DELETE FROM `db_fincaturistica`.`estadoreserva`
    WHERE `id` = _id;
    SET _respuesta = ROW_COUNT();
END $$
-- ====================================================================================== --

-- ==================== PROCEDIMIENTOS ALMACENADOS PARA EVENTOS ===================== --

-- ==================== INSERTAR EVENTO ===================== --
DELIMITER $$

CREATE PROCEDURE `db_fincaturistica`.`proc_insertar_eventos` (
    IN _descripcion VARCHAR(200),
    INOUT _respuesta INT
)
BEGIN
    SET _respuesta = 0;
    INSERT INTO `db_fincaturistica`.`eventos` (`descripcion`)
    VALUES (_descripcion);
    SET _respuesta = LAST_INSERT_ID();
END $$
-- ====================================================================================== --

-- ==================== CONSULTAR TODOS LOS EVENTOS ===================== --
DELIMITER $$

CREATE PROCEDURE `db_fincaturistica`.`proc_consultar_todos_eventos` ()
BEGIN
    SELECT `id`, `descripcion`
    FROM `db_fincaturistica`.`eventos`;
END $$
-- ====================================================================================== --

-- ==================== CONSULTAR EVENTO POR ID ===================== --
DELIMITER $$

CREATE PROCEDURE `db_fincaturistica`.`proc_consultar_eventos_por_id` (
    IN _id INT
)
BEGIN
    SELECT `id`, `descripcion`
    FROM `db_fincaturistica`.`eventos`
    WHERE `id` = _id;
END $$
-- ====================================================================================== --

-- ==================== ACTUALIZAR EVENTO ===================== --
DELIMITER $$

CREATE PROCEDURE `db_fincaturistica`.`proc_actualizar_eventos` (
    IN _id INT,
    IN _descripcion VARCHAR(200),
    INOUT _respuesta INT
)
BEGIN
    SET _respuesta = 0;
    UPDATE `db_fincaturistica`.`eventos`
    SET `descripcion` = _descripcion
    WHERE `id` = _id;
    SET _respuesta = ROW_COUNT();
END $$
-- ====================================================================================== --

-- ==================== ELIMINAR EVENTO ===================== --
DELIMITER $$

CREATE PROCEDURE `db_fincaturistica`.`proc_eliminar_eventos` (
    IN _id INT,
    INOUT _respuesta INT
)
BEGIN
    SET _respuesta = 0;
    DELETE FROM `db_fincaturistica`.`eventos`
    WHERE `id` = _id;
    SET _respuesta = ROW_COUNT();
END $$
-- ====================================================================================== --