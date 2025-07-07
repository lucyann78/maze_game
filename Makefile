# Makefile para ConectaFlores Raycaster

.PHONY: run clean

# Regla para ejecutar el juego
run:
	python src/main.py

# Regla para limpiar archivos de caché de Python
clean:
	find . -name "__pycache__" -type d -exec rm -rf {} +
	find . -name "*.pyc" -delete
	echo "Archivos de caché de Python limpiados."
