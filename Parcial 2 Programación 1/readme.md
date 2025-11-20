# 📚 Sistema de Gestión de Biblioteca (Library Management System)

Este proyecto es una aplicación de consola (CLI) desarrollada en **Python** para la gestión eficiente de un inventario de libros. Simula el funcionamiento de un sistema administrativo real, permitiendo el control de stock, préstamos y devoluciones mediante persistencia de datos.

## 📋 Descripción del Proyecto

El sistema permite a los bibliotecarios o administradores mantener un registro actualizado del catálogo de libros. A diferencia de programas que pierden los datos al cerrarse, este software implementa **persistencia de datos utilizando archivos CSV** (Comma Separated Values), lo que simula una base de datos ligera y portátil.

Este proyecto fue desarrollado como parte de la evaluación de **Programación I** en la **Tecnicatura Universitaria en Programación (UTN)**.

## 🚀 Funcionalidades Principales

El sistema cuenta con un menú interactivo que permite:

* **Persistencia de Datos:** Carga y guardado automático de información en `catalogo.csv`.
* **Gestión de Stock:**
    * Ingreso masivo o individual de nuevos títulos.
    * Actualización de ejemplares (sumar stock a libros existentes).
* **Movimientos (Lógica Transaccional):**
    * Registro de **Préstamos** (valida si hay stock disponible antes de restar).
    * Registro de **Devoluciones** (reingreso al stock).
* **Consultas y Reportes:**
    * Búsqueda inteligente de disponibilidad por título (normalización de texto).
    * Listado de libros agotados (stock cero).
    * Visualización del catálogo completo.

## 🛠️ Tecnologías y Conceptos Aplicados

Este proyecto demuestra el dominio de los siguientes conceptos técnicos:

* **Lenguaje:** Python 3.x
* **Manejo de Archivos:** Librería `csv` y `os` para lectura/escritura de bases de datos en texto plano.
* **Estructuras de Datos:** Uso avanzado de Listas de Diccionarios (`List[Dict]`) para manipular los registros en memoria.
* **Lógica de Programación:**
    * Validación de tipos de datos (control de errores de entrada de usuario).
    * Normalización de cadenas de texto (búsquedas *case-insensitive*).
    * Modularización mediante funciones para un código limpio y escalable.

## ⚙️ Cómo ejecutar el proyecto

1.  Asegúrate de tener Python instalado.
2.  Clona este repositorio o descarga los archivos.
3.  Ejecuta el script principal:
4.  El sistema creará automáticamente el archivo catalogo.csv si no existe.
```bash
python main.py

Autor: Neyen Maleh Estudiante de Tecnicatura Universitaria en Programación - UTN FRC
