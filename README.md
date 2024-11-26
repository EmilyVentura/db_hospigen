# Sistema de Gestión para Donación de Órganos

Este proyecto implementa un sistema integral diseñado para optimizar los procesos de gestión de datos relacionados con la donación de órganos en el **Hospital General San Juan de Dios**. El sistema permite registrar, analizar y gestionar la información de pacientes receptores y donantes, mejorando la toma de decisiones a través de herramientas visuales y filtros avanzados.

---

## Tabla de Contenidos
- [Características](#características)
- [Arquitectura del Proyecto](#arquitectura-del-proyecto)
- [Instalación](#instalación)
- [Uso](#uso)
- [Capturas de Pantalla](#capturas-de-pantalla)
- [Contribuciones](#contribuciones)
- [Licencia](#licencia)

---

## Características

### Funcionalidades Principales
1. **Registro de Pacientes:**
   - Gestión detallada de información de receptores y donantes.
   - Datos médicos clave, incluyendo antecedentes, evaluaciones, parámetros médicos y fases del proceso de donación.

2. **Sistema de Compatibilidad:**
   - Filtrado avanzado basado en criterios como:
     - Edad.
     - Grupo sanguíneo.
     - Estado de accesos vasculares.
     - Estado del protocolo de donación.
   - Emparejamiento automatizado de receptores y donantes.

3. **Evaluación Periódica:**
   - Comparación gráfica de indicadores médicos (por ejemplo, parámetros renales).
   - Visualización de datos a través de gráficos dinámicos para análisis longitudinal.

4. **Seguridad y Privacidad:**
   - Inicio de sesión con credenciales validadas.
   - Restricción de acceso a funciones críticas como agregar, actualizar y eliminar datos.
   - Contraseñas almacenadas utilizando hashing (bcrypt).

5. **Interfaz Gráfica Intuitiva:**
   - Navegación fácil para el personal médico.
   - Diseño modular y organizado con PyQt5.

---

## Arquitectura del Proyecto

### Estructura de Archivos

```
/nombre_del_proyecto
│
├── pacientesdb.sql          # Script para la base de datos MySQL.
├── tesis_principal.py       # Archivo principal de la aplicación.
├── tesis_conexionSQL.py     # Módulo de conexión a la base de datos.
├── tesis_login.py           # Módulo para autenticación de usuarios.
├── interfaz_ui.py           # Código generado para la interfaz gráfica.
├── README.md                # Este archivo.
└── requerimientos.txt         # Dependencias necesarias para el proyecto.
```

### Componentes Principales
- **Base de Datos MySQL:** Diseñada para almacenar la información de receptores, donantes y sus respectivas fases.
- **Backend en Python:** Manejo de la lógica de negocio y conexión con la base de datos.
- **Frontend con PyQt5:** Provee una interfaz gráfica que facilita la interacción del usuario con el sistema.

---

## Instalación

### Prerrequisitos
1. **Python 3.8+**: Asegúrate de tener Python instalado. [Descargar aquí](https://www.python.org/downloads/).
2. **MySQL Server**: Necesario para ejecutar la base de datos.
3. **Instalación de librerías**: Requiere las dependencias listadas en `requerimientos.txt`.

### Pasos de Instalación
1. **Clona el repositorio:**
   ```bash
   git clone https://github.com/EmilyVentura/db_hospigen.git
   cd db_hospigen
   ```

2. **Configura el entorno virtual (opcional pero recomendado):**
   ```bash
   python -m venv venv
   source venv/bin/activate   # En Linux/Mac
   venv\Scripts\activate      # En Windows
   ```

3. **Instala las dependencias:**
   ```bash
   pip install -r requerimientos.txt
   ```

4. **Configura la base de datos:**
   - Carga el archivo `pacientesdb.sql` en tu servidor MySQL:
     ```bash
     mysql -u root -p < pacientesdb.sql
     ```
   - Verifica que las credenciales en `tesis_conexionSQL.py` sean correctas:
     ```python
     self._host = "127.0.0.1"
     self._puerto = 3306
     self._usuario = "root"
     self._contraseña = "tu_contraseña"
     self._db = "nombre_base_datos"
     ```

5. **Ejecuta la aplicación:**
   ```bash
   python tesis_principal.py
   ```

---

## Uso

1. **Inicio de Sesión:**
   - Ingresa con un usuario y contraseña válidos.
   - El sistema validará las credenciales usando la base de datos.

2. **Navegación:**
   - Registra nuevos receptores y donantes.
   - Utiliza los filtros para encontrar coincidencias.
   - Visualiza gráficos y análisis médicos.

3. **Secciones del Sistema:**
   - **Registro de pacientes:** Ingreso de información inicial.
   - **Compatibilidad:** Emparejamiento automatizado.
   - **Evaluación periódica:** Seguimiento de indicadores médicos.
   - **Configuración:** Modifica ajustes del sistema.

---

## Contribuciones

Las contribuciones son bienvenidas. Por favor, sigue estos pasos:
1. Haz un fork del repositorio.
2. Crea una nueva rama con tu funcionalidad: `git checkout -b nueva_funcionalidad`.
3. Haz commit de tus cambios: `git commit -m "Descripción de los cambios"`.
4. Sube los cambios a tu fork: `git push origin nueva_funcionalidad`.
5. Abre un pull request en GitHub.

---

## Licencia

Este proyecto está licenciado bajo la [MIT License](LICENSE).

---

### Contacto

Proyecto desarrollado por [Emily Ventura](email:ven18391@uvg.edu.gt). Si tienes preguntas, no dudes en contactarme.

