# Ficha de Propuesta - Proyecto Final Redes

**Universidad de Concepción**  
**Redes de Computadores (501403)**  

---

## 1. Identificación del grupo

| Nombre | GitHub | Matrícula | Correo UDEC |
|--------|--------|-----------|
| Ignacio Jesús Soto Miranda |  [@Liivne](http://github.com/Liivne)  | 2023447412 | ignsoto2023@udec.cl |
| Lucas Daniel Morales Oyanedel | [@Falling-Bridge](https://github.com/Falling-Bridge) | 2023441490 | lucmorales2023@udec.cl | 
| Valentina Alejandra Serón Canales | [@arenisca](https://github.com/arenisca) | | vseron2020@udec.cl |

---

## 2. Título tentativo del proyecto

**Sistema IoT de Monitoreo y Control de Estacionamiento con Arquitectura de Tres Capas y Comunicación Bidireccional**

---

## 3. Variante temática elegida

- [x] Monitoreo de acceso o presencia

**Variante específica:** Sistema de monitoreo de ocupación de estacionamiento con sensores simulados tipo sonar IoT.

---

## 4. Problema o necesidad a resolver

Los estacionamientos urbanos y empresariales carecen de sistemas de monitoreo en tiempo real que permitan conocer la disponibilidad de espacios, gestionar alertas ante condiciones anómalas y optimizar el uso de los recursos. Los sistemas actuales son costosos o no ofrecen capacidades de control remoto.

El proyecto propone un sistema simulado que demuestre los principios de un entorno ciberfísico aplicado a estacionamientos, permitiendo:

- Monitorear en tiempo real el estado (libre/ocupado) de cada espacio
- Detectar condiciones anómalas (objetos muy cerca, temperatura extrema, humedad)
- Enviar comandos de vuelta a los sensores para ajustar su comportamiento
- Validar toda la comunicación con herramientas de análisis de red

---

## 5. Objetivo general del proyecto

Diseñar, implementar y validar un sistema de monitoreo remoto seguro para un estacionamiento simulado, con arquitectura IoT de tres capas (sensor IoT, repeater, router central), comunicación bidireccional sobre TCP/IP y capacidades de control automático y manual.

---

## 6. Objetivos específicos

1. Simular sensores de distancia tipo sonar que detecten ocupación de espacios de estacionamiento, incluyendo variables ambientales (temperatura, humedad).
2. Implementar un repeater (gateway intermedio) que filtre, valide y reenvíe mensajes entre sensores y router central.
3. Desarrollar un router central que procese mediciones, genere alertas por condiciones anómalas y envíe comandos de vuelta a los sensores.
4. Incorporar autenticación multi-capa como medida de seguridad (claves distintas para sensor→repeater→router).
5. Validar el sistema capturando y analizando tráfico TCP/IP con Wireshark, documentando handshakes, estructura de mensajes y latencia.
6. Garantizar la reproducibilidad del proyecto mediante contenedores Docker y docker-compose.

---

## 7. Arquitectura preliminar del sistema

El sistema sigue una arquitectura IoT de tres capas con comunicación bidireccional:

[Sensor IoT] <----> [Repeater] <----> [Router Central]
   (Sonar)         (Gateway)          (Procesa)


**Componentes:**

- **Nodos IoT:** Programas Python que simulan mediciones de distancia (20-500cm), temperatura (15-35°C) y humedad (30-80%). Cada sensor tiene un puerto para recibir comandos.
- **Repeater:** Gateway intermedio que valida autenticación, agrega metadata (TTL, hop_count) y filtra mediciones inválidas.
- **Router Central:** Servidor que procesa mediciones, detecta alertas (distancia<30cm, temp>45°C), envía comandos y mantiene historial.
- **Comunicación:** TCP/IP sobre red interna de Docker (bidireccional).

---

## 8. Software y herramientas que usarán

| Categoría | Herramientas |
|-----------|--------------|
| **Lenguaje principal** | Python 3.11 |
| **Bibliotecas** | socket, threading, json, random, time |
| **Orquestación** | Docker, docker-compose |
| **Validación** | Wireshark, Nmap |

---

## 9. Comunicación prevista

- [x] TCP

**Protocolo elegido:** TCP/IP sobre red interna de Docker

**Puertos asignados:**

- Sensor → Repeater: Puerto 5002
- Repeater → Router: Puerto 8080
- Router → Sensor: Puertos 6001-600N (uno por sensor)

**Justificación:** TCP garantiza entrega confiable y ordenada de los mensajes, lo cual es crítico para los comandos de control enviados desde el router a los sensores. La pérdida de un comando podría afectar el comportamiento del sistema. Además, TCP permite identificar fácilmente las conexiones en Wireshark.

---

## 10. Seguridad o confiabilidad prevista

Medidas incorporadas:

- [x] Autenticación básica
- [x] Validación de mensajes
- [x] Detección de datos inválidos
- [x] Alertas por condición anómala

**Justificación:** Se implementará autenticación multi-capa con claves secretas diferentes para cada segmento de la comunicación (sensor→repeater, repeater→router, router→sensor). Adicionalmente, el router validará que las mediciones estén dentro de rangos físicamente posibles (distancia 0-1000cm, temperatura 0-50°C, humedad 0-100%) y generará alertas ante condiciones anómalas como distancia peligrosamente cercana (<30cm) o temperatura extrema (>45°C).

---

## 11. Validación prevista con herramientas del curso

**Uso previsto de Wireshark:**

- Captura de tráfico en interfaz loopback y/o interfaz de red de Docker
- Análisis del handshake TCP (SYN, SYN-ACK, ACK) entre cada par de componentes
- Inspección del payload JSON para verificar estructura y autenticación
- Medición de latencia entre medición y comando de respuesta
- Documentación de capturas en el informe final

**Uso previsto de Nmap (opcional):**

- Escaneo de puertos abiertos en el sistema (solo sobre entorno local autorizado)
- Verificación de que solo los puertos necesarios (5002, 8080, 6001-600N) están expuestos

---

## 12. Viabilidad del proyecto

**1. ¿El proyecto puede ejecutarse completamente con el PC del grupo?**

Sí. El proyecto es 100% software, utiliza la interfaz loopback y/o red interna de Docker, y no requiere hardware adicional. Cualquier computador con Docker instalado puede ejecutar el sistema con un solo comando: `docker-compose up`

**2. ¿Qué riesgo técnico principal anticipa el grupo?**

La coordinación de múltiples hilos y sockets bidireccionales (cada sensor debe enviar mediciones y recibir comandos simultáneamente).

**3. ¿Cómo planean reducir ese riesgo?**

Implementar primero la comunicación unidireccional (sensor→router) y, una vez validada, agregar la bidireccionalidad (router→sensor) con un hilo separado para escucha de comandos en cada sensor.

---

## 13. Roles preliminares del grupo

*Por asignar*

| Rol | Responsable |
|-----|-------------|
| Arquitectura y documentación |  |
| Cliente / Nodo IoT simulado |  |
| Repeater y Router central |  |
| Pruebas y análisis con Wireshark | |

---

## 14. Observaciones del docente o ayudante

(Espacio reservado para comentarios del equipo docente)

---

## 15. Criterios de revisión de esta propuesta

- [x] Coherencia con el marco del proyecto (monitoreo remoto seguro de entorno ciberfísico)
- [x] Viabilidad técnica (100% software, Docker, Python)
- [x] Realización completa en software (sin hardware)
- [x] Claridad del problema y de la arquitectura preliminar
- [x] Presencia de comunicación real sobre red (TCP/IP)
- [x] Presencia prevista de seguridad o confiabilidad básica

---

**Fecha de entrega:** 10/06/2026

**Firma del grupo (representante):** ___________________________
