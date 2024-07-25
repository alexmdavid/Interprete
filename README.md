# Proyecto de Compilador Web con Django y PLY

![image](https://github.com/user-attachments/assets/801295b1-b9c2-4cbc-98ab-c558d8cd19b6)


Este proyecto es un compilador web desarrollado en Python utilizando Django y la biblioteca PLY (Python Lex-Yacc). El compilador se puede personalizar para crear tu propio lenguaje de programación modificando las variables y reglas gramaticales. La interfaz web permite a los usuarios ingresar código fuente y ver los resultados del análisis directamente en su navegador.

## Descripción del Proyecto

El objetivo de este proyecto es proporcionar una base para un compilador web que pueda ser de ayuda para crear un lenguaje de programacion con tus especificaciones. Utiliza PLY para realizar el análisis léxico y sintáctico del código fuente, mientras que Django proporciona una interfaz web para interactuar con el compilador.

### Características

- **Análisis Léxico**: Identificación y clasificación de los tokens del lenguaje de entrada.
- **Análisis Sintáctico**: Construcción de un árbol de análisis a partir de la secuencia de tokens.
- **Semántica y Validación**: Verificación de la corrección del código en términos de tipos de datos, declaraciones y expresiones.
- **Generación de Código**: Traducción del código fuente a un formato intermedio o ejecutable.
- **Interfaz Web**: Permite a los usuarios ingresar el código fuente y visualizar los resultados del análisis directamente en el navegador.

## Instalación y Configuración

Para ejecutar este proyecto, sigue estos pasos:

### 1. Crear un Entorno Virtual

Puedes crearlo con el siguiente comando:

```bash
python -m venv nombre_del_entorno
```

sino funciona intenta con este otro:

```bash
python3 -m venv nombre_del_entorno
```

por ultimo identificar si el entorno esta activo, para averiguarlo simplemente miras la terminal y si al comienzo empieza con (nombre_del_entorno) esta activo,
sino aparece significa que esta desactivado para activarlo lo puedes hacer con el siguiente comando:

```bash
source nombre_del_entorno/bin/activate
```


### 2. Instalar Dependecias en el Entorno Virtual

Puedes instalar las dependecias con el siguiente comando:

```bash
pip install -r requirements.txt</code>
```


### 3. Ejecutar Servidor de Desarrollo de Django
Para ejecuctarlo debes encontrarte en la raiz del proyecto y en la terminal ejecutar el siguiente codigo:

```bash
python manage.py runserver</code>
```

Por defecto, el servidor se ejecutará en http://127.0.0.1:8000/
igualmente el link se mostrara en la terminal siempre y cuando se ejecute correctamente.
