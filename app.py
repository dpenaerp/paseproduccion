from flask import Flask, render_template, request, redirect, url_for
import sqlite3
from datetime import datetime

app = Flask(__name__)

# Configuración de base de datos
DATABASE = 'pases_produccion.db'

# Crear base de datos y tabla si no existe
def init_db():
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS pases_produccion (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            numero_pase TEXT,
            fecha_solicitud TEXT,
            solicitante TEXT,
            proveedor_responsable TEXT,
            area_departamento TEXT,
            nombre_sistema TEXT,
            version_actual TEXT,
            nueva_version TEXT,
            descripcion_actualizacion TEXT,
            tipo_cambio TEXT,
            impacto_infraestructura TEXT,
            fecha_hora_programada TEXT,
            pruebas_realizadas TEXT,
            resultados_pruebas TEXT,
            observaciones_qa TEXT,
            responsable_qa TEXT,
            fecha_aprobacion_qa TEXT,
            archivos_afectados TEXT,
            base_datos_afectados TEXT,
            requerimientos_previos TEXT,
            descripcion_cambios TEXT,
            plan_reversion TEXT,
            aprobacion_tecnologia TEXT,
            fecha_aprobacion_tecnologia TEXT,
            aprobacion_gerente TEXT,
            fecha_aprobacion_gerente TEXT,
            resultado_pase TEXT,
            observaciones TEXT,
            fecha_registro TEXT
        )
    ''')
    conn.commit()
    conn.close()

init_db()

# Ruta principal
@app.route('/')
def index():
    return render_template('index.html')

# Ruta para registrar un pase a producción
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        datos_pase = {
            "numero_pase": request.form['numero_pase'],
            "fecha_solicitud": request.form['fecha_solicitud'],
            "solicitante": request.form['solicitante'],
            "proveedor_responsable": request.form['proveedor_responsable'],
            "area_departamento": request.form['area_departamento'],
            "nombre_sistema": request.form['nombre_sistema'],
            "version_actual": request.form['version_actual'],
            "nueva_version": request.form['nueva_version'],
            "descripcion_actualizacion": request.form['descripcion_actualizacion'],
            "tipo_cambio": request.form['tipo_cambio'],
            "impacto_infraestructura": request.form['impacto_infraestructura'],
            "fecha_hora_programada": request.form['fecha_hora_programada'],
            "pruebas_realizadas": request.form['pruebas_realizadas'],
            "resultados_pruebas": request.form['resultados_pruebas'],
            "observaciones_qa": request.form['observaciones_qa'],
            "responsable_qa": request.form['responsable_qa'],
            "fecha_aprobacion_qa": request.form['fecha_aprobacion_qa'],
            "archivos_afectados": request.form['archivos_afectados'],
            "base_datos_afectados": request.form['base_datos_afectados'],
            "requerimientos_previos": request.form['requerimientos_previos'],
            "descripcion_cambios": request.form['descripcion_cambios'],
            "plan_reversion": request.form['plan_reversion'],
            "aprobacion_tecnologia": request.form['aprobacion_tecnologia'],
            "fecha_aprobacion_tecnologia": request.form['fecha_aprobacion_tecnologia'],
            "aprobacion_gerente": request.form['aprobacion_gerente'],
            "fecha_aprobacion_gerente": request.form['fecha_aprobacion_gerente'],
            "resultado_pase": request.form['resultado_pase'],
            "observaciones": request.form['observaciones'],
            "fecha_registro": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
        
        conn = sqlite3.connect(DATABASE)
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO pases_produccion (
                numero_pase, fecha_solicitud, solicitante, proveedor_responsable, area_departamento,
                nombre_sistema, version_actual, nueva_version, descripcion_actualizacion, tipo_cambio,
                impacto_infraestructura, fecha_hora_programada, pruebas_realizadas, resultados_pruebas,
                observaciones_qa, responsable_qa, fecha_aprobacion_qa, archivos_afectados, base_datos_afectados,
                requerimientos_previos, descripcion_cambios, plan_reversion, aprobacion_tecnologia,
                fecha_aprobacion_tecnologia, aprobacion_gerente, fecha_aprobacion_gerente, resultado_pase,
                observaciones, fecha_registro
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        ''', tuple(datos_pase.values()))
        conn.commit()
        conn.close()
        return redirect(url_for('index'))
    
    return render_template('register.html')

# Ruta para ver los pases registrados
@app.route('/records')
def view_records():
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM pases_produccion')
    registros = cursor.fetchall()
    conn.close()
    return render_template('view_records.html', registros=registros)

if __name__ == '__main__':
    app.run(debug=True)
