# Simulador de Línea de Visión (FOV 2D) con Raycasting y Trigonometría

**Universidad Mariano Gálvez de Guatemala**  
**Facultad de Ingeniería en Sistemas de Información y Ciencias de la Computación**  
**Curso:** Precálculo  
**Catedrático:** M.A. Ing. Claudio Orazio López Calderón  
**Estudiantes:** Jose Carlos Alfaro García 0906-26-9140, Marvin Michael González de León 0906-26-4094.


---

## 📌 Descripción del Proyecto

Este proyecto es una aplicación web interactiva desarrollada en **HTML5 Canvas** y **JavaScript vanilla** que modela el comportamiento de la luz y el campo de visión de un observador en un plano bidimensional.

El sistema aplica conceptos de precálculo, tales como **trigonometría analítica, coordenadas polares, funciones inversas (`atan2`) y resolución de triángulos**, para calcular y renderizar en tiempo real el haz de visión proyectado sobre un mapa con obstáculos rígidos.

---

## 🚀 Características y Funcionalidades

- **Apuntado Dinámico:** Cálculo del ángulo de orientación en tiempo real mediante la posición del cursor (`mousemove`).
- **Control de Movimiento:** Movimiento fluido del jugador en 2D mediante teclas `W`, `A`, `S`, `D`.
- **Proyección Trigonométrica:** Generación de un abanico de 120 rayos parametrizados con funciones senoidales y cosenoidales.
- **Detección de Obstáculos:** Detención de rayos en tiempo real mediante comprobación de colisiones contra fronteras cuadrangulares.
- **Visualización Gráfica:** Renderizado de polígonos de luz y visualización de líneas de rayos individuales a 60 FPS.

---

## 🛠️ Tecnologías Utilizadas

- **HTML5:** Estructura del documento y elemento `<canvas>`.
- **CSS3:** Estilizado básico e interfaz oscura para simular entornos nocturnos/iluminados.
- **JavaScript (ES6+):** Lógica matemática, manejo de eventos de ratón/teclado y algoritmo de Raycasting.

---

## 📐 Fundamento Matemático Incorporado

1. **Cálculo de Ángulo de Mirada:**
   $$\theta = \text{atan2}(\Delta y, \Delta x)$$

2. **Conversión Angular:**
   $$\text{Radianes} = \text{Grados} \times \frac{\pi}{180}$$

3. **Proyección del Rayo (Avance Paramétrico):**
   $$x_{r} = x_{p} + d \cdot \cos(\theta)$$
   $$y_{r} = y_{p} + d \cdot \sin(\theta)$$

4. **Relación Pitagórica:**
   $$d = \sqrt{\Delta x^2 + \Delta y^2}$$

---

## 📋 Instrucciones de Ejecución

1. Descarga o clona este repositorio.
2. Abre el archivo `index.html` en cualquier navegador web moderno (Google Chrome, Mozilla Firefox, Microsoft Edge, Safari).
3. No se requiere instalación de dependencias ni servidores locales.

### Controles
- **Mover el cursor:** Orienta la dirección de la linterna / campo de visión.
- **Teclas W, A, S, D:** Mueven la posición del jugador por el escenario.

---

## 📁 Estructura del Repositorio

```text
├── index.html       # Código fuente completo (HTML, CSS y JavaScript)
├── DOCUMENTACION.pdf# Informe escrito según la guía de la Universidad
└── README.md        # Este archivo de instrucciones