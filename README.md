# PostalCodeSearch

---

##  Overview
Postal Code Search is a simple Flask web application connected to MariaDB that allows you to search and autocomplete addresses from the official SEPOMEX postal code database.
Type part of a colony, municipality, or postal code and the app suggests the full details: settlement, type, municipality, state, city, and postal code.

---

## Author

This project was created by Araceli Romero, a student of Information technologies in science(TICs) at [UNAM](https://www.unam.mx/), Mexico.

Movie Explorer was developed as part of the Distributed Database course (Class of 2025).

Feel free to reach out with questions, feedback, or collaboration ideas to araceliromerozerpa@gmail.com

---

## License

This projects is under [MIT License](https://choosealicense.com/licenses/mit/).

---

##  Introduction  

The Mexican Postal Code Searcher is a lightweight web application built with Flask and MariaDB that lets you quickly search and autocomplete addresses from the official SEPOMEX (Servicio Postal Mexicano) dataset.

With few keystrokes, you can look up a colony, municipality, or postal code and instantly see the complete information, such as: settlement type, municipality, state, city, and postal code.

---

## Aim

This project is designed for:

- Students and developers who want a simple practice with Flask + SQL integration.

- Analysts needing quick access to the SEPOMEX database.

- Anyone who wants a clean, fast postal code lookup tool for Mexico.

The app is simple, responsive, and easy to set up locally — making it a great starting point for learning database-driven web apps.

---

## Setup Instructions  
1. Clone the repository 
   ```bash
   git clone https://github.com/Marzerp/PostalCodeSearch.git
   cd PostalCodeSearch
   ```
2. Create and activate a virtual environment
  ``` bash
  python3 -m venv venv
  source venv/bin/activate   # Linux / Mac
  venv\Scripts\activate      # Windows
  ```

3. Install dependencies
   ```bash
   pip install -r requirements.txt
   ```
4. Prepare database
   - Follow "Script_mariadb.txt" for setup instructions
   - Make your .env file using env_example as reference in the app/ directory
   
5. Run the app
   ```bash
   python app.py
   ```
6. Open your browser at [http://127.0.0.1:5000](http://127.0.0.1:5000)

---

## Quick look at how Postal Code Search works

- Example search by city (Morelia, Michoacán, MX)
<p align="center"> <img src="docs/morelia.png" alt="Morelia" width="600"/> </p>

- Example search by postal code (58350 postal code of a colony in Morelia)
<p align="center"> <img src="docs/pc.png" alt="pc" width="600"/> </p>

---
## Example Queries 

- How many cities are in Mexico?

``` bash
SELECT COUNT(DISTINCT d_ciudad) FROM cp;
```

- Colonies containing "María":

```bash
SELECT * FROM cp WHERE d_asenta LIKE '%María%';
```
- How many rural and urban settlements are 

```bash 
SELECT d_zona, COUNT(*) FROM cp GROUP BY d_zona;
```
---

## Technologies

- Python3
- Flask
- MariaDB
- mysql-connector-python
