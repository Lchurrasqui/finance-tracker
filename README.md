Finance Tracker

1. Definición del Problema y Solución

Problema: Gestionar finanzas personales de forma manual es tedioso, propenso a errores y dificulta el análisis histórico de gastos para tomar decisiones de ahorro.

Solución: Una API Backend que permita centralizar el registro de ingresos y gastos, categorizarlos y consultar reportes de balance de forma programática.

2. Casos de Uso (¿Qué puede hacer el usuario?)

Registrar Usuario: El usuario crea una cuenta con email y contraseña.

Cargar Transacción: El usuario registra un monto, indica si es gasto/ingreso y le asigna una categoría.

Consultar Balance: El usuario pide ver cuánto dinero tiene disponible (Ingresos - Gastos).

Listar Movimientos: El usuario ve su historial filtrado por fecha o categoría.

3. User stories

    As a user, I want to create an account so that I can track my finances.

    As a user, I want to log in so that I can access my financial data.

    As a user, I want to add transactions manually so that I can record my expenses and income.

    As a user, I want to edit or delete transactions so that I can correct mistakes.

    As a user, I want to create categories so that I can organize my transactions.

    As a user, I want to see a graphical summary of my expenses so that I understand my spending habits.

    As a user, I want to import transactions from a CSV file so that I can upload data from my bank.

    As a user, I want to see my monthly balance so that I know if I am saving or spending more than I earn.

3. Requerimientos Funcionales (RF)

RF1: El sistema debe permitir el login seguro.

RF2: El sistema debe validar que no se ingresen montos negativos.

RF3: El sistema debe permitir crear categorías personalizadas (ej: "Suscripciones", "UTN").

5. Entidades (Modelo de Datos)

User
-----
id
email
password_hash
created_at
Account
-------
id
user_id
name
Category
--------
id
user_id
name
description
Transaction
-----------
id
account_id
category_id
amount
type
description
date

Relaciones:

User 1:N Account
User 1:N Category

Account 1:N Transaction
Category 1:N Transaction

## 2. Características actualizadas
- Registro de usuarios y autenticación básica.
- Gestión de gastos con descripción, monto y categorización.
- [En desarrollo] Integración con base de datos relacional.
- [Proyección] Interfaz de usuario (Web/Desktop) y visualización de reportes.

## 3. Arquitectura y Diseño de Datos
El sistema sigue un modelo relacional para garantizar la integridad de la información. A continuación se presenta el Diagrama Entidad-Relación (DER) que rige la base de datos:

![Diagrama Entidad Relación](./docs/der_finanzas.png)

### Entidades Principales:
* **Usuario:** Almacena la información de perfil y credenciales.
* **Gasto:** Registra cada transacción financiera vinculada a un usuario.
* **Categoría:** Clasificación para organizar los movimientos (Vivienda, Educación, Ocio, etc.).

## 4. Tecnologías Utilizadas
* **Lenguaje:** Python 3.x
* **Base de Datos:** SQLite (en implementación)
* **Gestión de Versiones:** Git & GitHub

## 5. Instalación y Ejecución
Para clonar y ejecutar este proyecto localmente:
