# Suerte Terminal

Este script en Python es un juego interactivo llamado "Suerte Terminal". En este juego, el jugador selecciona un número entre 1 y 10. Si el número elegido coincide con el número de la "muerte", el archivo o directorio seleccionado se elimina. El juego incluye un menú para iniciar el juego, continuar jugando o salir.

## Requisitos

- Python 3.x
- [colorama](https://pypi.org/project/colorama/) (para la coloración del texto en la consola)

## Instalación

1. **Clona o descarga el repositorio:**

    ```bash
    git clone https://github.com/CodingJAndres/suerte_terminal.git
    ```

2. **Navega al directorio del proyecto:**

    ```bash
    cd suerte_terminal 
    ```

3. **Instala la librería `colorama`:**

    ```bash
    pip install colorama
    ```

## Uso

1. **Ejecuta el script:**

    ```bash
    python ruleta.py
    ```

2. **Selecciona una opción del menú:**

    - **Introduce la ruta al archivo o directorio:** Se te pedirá que introduzcas la ruta del archivo o directorio que deseas poner en juego.
    - **Elige un número del 1 al 10:** Selecciona un número para intentar evitar el número de la "muerte".
    - **Continúa jugando o sal del juego:** Después de cada ronda, puedes elegir si quieres seguir jugando o salir del juego.

3. **Proporciona la información solicitada para cada opción:**

    - **Ruta del archivo/directorio:** La ruta completa al archivo o directorio que quieres que el juego maneje.
    - **Número entre 1 y 10:** El número que eliges en cada ronda.

## Descripción de Opciones

- **Ruta del archivo/directorio:** El archivo o directorio seleccionado será eliminado si el número elegido coincide con el número de la "muerte".
- **Número entre 1 y 10:** Si el número coincide con el número de la "muerte", el archivo/directorio se eliminará. Si no coincide, recibirás un mensaje y podrás seguir jugando.
- **Continuar jugando:** Después de cada ronda, puedes decidir si quieres seguir jugando o salir del juego.

## Manejo de Errores

- **Archivo/Directorio no existe:** Si la ruta proporcionada no existe, el script mostrará un mensaje de error.
- **Entrada inválida:** Si el número ingresado no es un número entero entre 1 y 10, el script pedirá una entrada válida.
- **Excepciones Generales:** Cualquier otro error durante la ejecución, como problemas al eliminar archivos/directorios, será mostrado en la consola.

## Licencia

Este proyecto está licenciado bajo la Licencia MIT - consulta el archivo [LICENSE](LICENSE) para obtener más detalles.

---

¡Disfruta de "Suerte Terminal" y buena suerte evitando la eliminación de tus archivos!
