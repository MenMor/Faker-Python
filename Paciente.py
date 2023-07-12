from faker import Faker
import mysql.connector
import random

fake = Faker()

conn  = mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database='clinicadental'
)
cursor = conn .cursor()

for _ in range(150):  
    tipo_identificacion = random.choice(["Cédula", "Pasaporte"])
    numero_identificacion = fake.unique.random_number(digits=10)
    nombre = fake.first_name()
    apellido = fake.last_name()
    telefono = fake.unique.random_number(digits=10)
    ciudad = fake.city()
    direccion = fake.address()
    correo = fake.email()
    fecha_nacimiento = fake.date_of_birth(minimum_age=18, maximum_age=90)
    alergia = fake.sentence()
    sexo = random.choice(["Masculino", "Femenino"])
    grupo_sanguineo = random.choice(["A+", "A-", "B+", "B-", "AB+", "AB-", "O+", "O-"])
    estado_civil = random.choice(["Soltero/a", "Casado/a", "Divorciado/a", "Viudo/a"])

    # Crear la consulta SQL para insertar los datos
    query = "INSERT INTO Paciente (tipoIdendificacion, numeroIdentificacion, nombre, apellido, telefono, ciudad, direccion, correo, fechaNacimiento, alergia, sexo, grupoSanguineo, estadoCivil) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
    values = (tipo_identificacion, numero_identificacion, nombre, apellido, telefono, ciudad, direccion, correo, fecha_nacimiento, alergia, sexo, grupo_sanguineo, estado_civil)
    cursor.execute(query, values)
    conn .commit()

for _ in range(150):
    id_paciente = random.randint(1, 150)
    nombre = fake.first_name()
    apellido = fake.last_name()
    telefono = fake.unique.random_number(digits=10)
    ciudad = fake.city()
    direccion = fake.address()
    correo = fake.email()
    parentesco = random.choice(["Padre", "Madre", "Hermano", "Hermana", "Esposo", "Esposa"])

    # Insertar registro en la tabla ContactoEmergencia
    cursor = conn.cursor()
    sql = "INSERT INTO ContactoEmergencia (idPaciente, nombre, apellido, telefono, ciudad, direccion, correo, parentesco) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
    values = (id_paciente, nombre, apellido, telefono, ciudad, direccion, correo, parentesco)
    cursor.execute(sql, values)
    conn.commit()

# Generar registros aleatorios para la tabla Recepcionista
for _ in range(2):
    cedula = fake.unique.random_number(digits=10)
    nombre = fake.first_name()
    apellido = fake.last_name()
    telefono = fake.unique.random_number(digits=10)
    direccion = fake.address()
    correo = fake.email()

    # Insertar registro en la tabla Recepcionista
    cursor = conn.cursor()
    sql = "INSERT INTO Recepcionista (cedula, nombre, apellido, telefono, direccion, correo) VALUES (%s, %s, %s, %s, %s, %s)"
    values = (cedula, nombre, apellido, telefono, direccion, correo)
    cursor.execute(sql, values)
    conn.commit()



# Generar registros aleatorios para la tabla Doctor
for _ in range(5):
    cedula = fake.unique.random_number(digits=10)
    nombre = fake.first_name()
    apellido = fake.last_name()
    telefono = fake.unique.random_number(digits=10)
    direccion = fake.address()
    correo = fake.email()

    # Insertar registro en la tabla Doctor
    cursor = conn.cursor()
    sql = "INSERT INTO Doctor (cedula, nombre, apellido, telefono, direccion, correo) VALUES (%s, %s, %s, %s, %s, %s)"
    values = (cedula, nombre, apellido, telefono, direccion, correo)
    cursor.execute(sql, values)
    conn.commit()

# Generar registros aleatorios para la tabla Especialidad
especialidades = ["Cardiología", "Dermatología", "Gastroenterología", "Neurología", "Pediatría", "Oftalmología", "Oncología"]
for especialidad in especialidades:
    # Insertar registro en la tabla Especialidad
    cursor = conn.cursor()
    sql = "INSERT INTO Especialidad (nombreEspecialidad) VALUES (%s)"
    values = (especialidad,)
    cursor.execute(sql, values)
    conn.commit()

# Generar registros aleatorios para la tabla Horario
dias_semana = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado"]
for _ in range(7):
    dia = random.choice(dias_semana)
    hora_inicio = fake.time(pattern="%H:%M:%S", end_datetime=None)
    hora_fin = fake.time(pattern="%H:%M:%S", end_datetime=None)

    # Insertar registro en la tabla Horario
    cursor = conn.cursor()
    sql = "INSERT INTO Horario (dia, horaInicio, horaFin) VALUES (%s, %s, %s)"
    values = (dia, hora_inicio, hora_fin)
    cursor.execute(sql, values)
    conn.commit()

# Generar registros aleatorios para la tabla EspecialidadDoctor
for _ in range(5):
    id_especialidad = random.randint(1, len(especialidades))
    id_doctor = random.randint(1, 5)
    id_horario = random.randint(1, 7)

    # Insertar registro en la tabla EspecialidadDoctor
    cursor = conn.cursor()
    sql = "INSERT INTO EspecialidadDoctor (idEspecialidad, idDoctor, idHorario) VALUES (%s, %s, %s)"
    values = (id_especialidad, id_doctor, id_horario)
    cursor.execute(sql, values)
    conn.commit()


# Generar registros aleatorios para la tabla NominaDoctor
for _ in range(5):
    id_especialidad = random.randint(1, len(especialidades))
    id_doctor = random.randint(1, 5)
    id_horario = random.randint(1, 7)
    monto = random.uniform(1000, 5000)
    fecha_inicio = fake.date_between(start_date='-1y', end_date='today')
    fecha_fin = fake.date_between(start_date=fecha_inicio, end_date='today')

    # Insertar registro en la tabla NominaDoctor
    cursor = conn.cursor()
    sql = "INSERT INTO NominaDoctor (idEspecialidad, idDoctor, idHorario, monto, fechaInicio, fechaFin) VALUES (%s, %s, %s, %s, %s, %s)"
    values = (id_especialidad, id_doctor, id_horario, monto, fecha_inicio, fecha_fin)
    cursor.execute(sql, values)
    conn.commit()


# Generar registros aleatorios para la tabla Cita
for _ in range(100):
    id_especialidad_doc = random.randint(1, 5)
    cursor.execute("SELECT idPaciente FROM Paciente")
    ids_pacientes = cursor.fetchall()
    id_paciente = random.choice(ids_pacientes)[0]
    id_recepcionista = random.randint(1, 2)
    fecha_dia_cita = fake.date_time_this_year(before_now=True, after_now=False)
    confirmacion = random.choice([0, 1])
    pendiente = random.choice([0, 1])

    # Insertar registro en la tabla Cita
    cursor = conn.cursor()
    sql = "INSERT INTO Cita (idEspecialidadDoc, idPaciente, idRecepcionista, fechaDiaCita, confirmacion, pendiente) VALUES (%s, %s, %s, %s, %s, %s)"
    values = (id_especialidad_doc, id_paciente, id_recepcionista, fecha_dia_cita, confirmacion, pendiente)
    cursor.execute(sql, values)
    conn.commit()

# Generar registros aleatorios para la tabla HistoriaClinicaGeneral
for _ in range(100):
    cursor.execute("SELECT idPaciente FROM Paciente")
    ids_pacientes = cursor.fetchall()
    id_paciente = random.choice(ids_pacientes)[0]
    fecha = fake.date_time_this_year(before_now=True, after_now=False)
    sector = fake.word()
    grupo_prioritario = fake.word()

    # Insertar registro en la tabla HistoriaClinicaGeneral
    cursor = conn.cursor()
    sql = "INSERT INTO HistoriaClinicaGeneral (idPaciente, fecha, sector, grupoPrioritario) VALUES (%s, %s, %s, %s)"
    values = (id_paciente, fecha, sector, grupo_prioritario)
    cursor.execute(sql, values)
    conn.commit()

# Generar registros aleatorios para la tabla HistoriaClinicaOdontologica
for _ in range(100):
    id_cita = random.randint(1, 100)
    id_historia_g = random.randint(1, 100)
    embarazo = random.choice([0, 1])
    presion_arterial = fake.random_int(min=80, max=140)
    temperatura = fake.random_int(min=36, max=38)
    frecuencia_respiratoria = fake.random_int(min=12, max=20)
    frecuencia_cardiaca = fake.random_int(min=60, max=100)
    motivo_atencion = fake.sentence()
    enfermedad_actual = fake.sentence()
    toma_medicamento = random.choice([0, 1])
    nombre_medicamento = fake.word() if toma_medicamento == 1 else None
    ihos = fake.sentence()
    gingivitis = random.choice([0, 1])
    oclusion = random.choice([0, 1])
    tipo_oculsion = random.choice(["Clase I", "Clase II", "Clase III"])
    enfermedad_periodontal = random.choice([0, 1])
    fluorosis = random.choice([0, 1])
    indice_cpo = random.randint(0, 6)

    # Insertar registro en la tabla HistoriaClinicaOdontologica
    cursor = conn.cursor()
    sql = "INSERT INTO HistoriaClinicaOdontologica (idCita, idHistoriaG, embarazo, presionArterial, temperatura, frecuenciaRespiratoria, frecuenciaCardiaca, motivoAtencion, enfermedadActual, tomaMedicamento, nombreMedicamento, ihos, gingivitis, oclusion, tipoOclusion, enfermedadPeriodontal, fluorosis, indiceCpo) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
    values = (id_cita, id_historia_g, embarazo, presion_arterial, temperatura, frecuencia_respiratoria, frecuencia_cardiaca, motivo_atencion, enfermedad_actual, toma_medicamento, nombre_medicamento, ihos, gingivitis, oclusion, tipo_oculsion, enfermedad_periodontal, fluorosis, indice_cpo)
    cursor.execute(sql, values)
    conn.commit()


# Generar registros aleatorios para la tabla Antecedente
for _ in range(100):
    id_historia_o = random.randint(1, 100)
    tipo = random.choice(["Personal", "Familiar"])
    grupo = fake.word()
    antecedente = fake.sentence()
    valor_descripcion = fake.sentence()
    observacion = fake.sentence() if random.choice([0, 1]) else None

    # Insertar registro en la tabla Antecedente
    cursor = conn.cursor()
    sql = "INSERT INTO Antecedente (idHistoriaO, tipo, grupo, antecedente, valorDescripcion, observacion) VALUES (%s, %s, %s, %s, %s, %s)"
    values = (id_historia_o, tipo, grupo, antecedente, valor_descripcion, observacion)
    cursor.execute(sql, values)
    conn.commit()

# Insertar registros en la tabla NomenclaturaProcedimiento
nomenclatura_procedimientos = [
    ('D0100-D0999', 'Exploración y Diagnóstico. Evaluaciones clínicas orales.'),
    ('D0120', 'Períodica evaluación oral - paciente subsecuente.'),
    ('D0140', 'Limitada evaluación oral - problema centrado.'),
    ('D0145', 'Evaluación oral a un paciente menor de tres años y asesoramiento, con primaria o cuidador.'),
    ('D0150', 'Completa evaluación oral - o establecimientos nuevo paciente.'),
    ('D0160', 'Extensa evaluación detallada y oral - problemas se centró en el informe.'),
    ('D0170', 'Re-evaluación – limitada, el problema se centró.'),
    ('D0180', 'Evaluación periodontal completa - o establecidos nuevo paciente.'),
    ('D1000 - D1999 II', 'Preventivo.'),
    ('D1110', 'Profilaxis adultos.'),
    ('D1120', 'Profilaxis infantil.'),
    ('D1203', 'La aplicación tópica de fluoruro- infantil.'),
    ('D1204', 'Aplicación tópica de fluoruro- adultos.'),
    ('D1206', 'Topicación de fluoruro barniz, la aplicación terapéutica de moderado a las caries pacientes de alto riesgo.'),
    ('D1310', 'Dietéticas específicas para el control de la enfermedad dental.'),
    ('D1330', 'Instrucciones de higiene oral.'),
    ('D1351', 'Sellador - por diente.'),
    ('D2330', 'A base de resina compuesta - una superficie, anterior.'),
    ('D2331', 'A base de resina compuestas - dos superficies, anterior.'),
    ('D2332', 'A base de resinas compuestas - tres superficies, anterior.'),
    ('D2335', 'A base de resinas compuestas - cuatro o más superficies o en relación con el ángulo incisal (anterior).'),
    ('D2390', 'Base compuesta corona con resina, anterior.'),
    ('D2391', 'A base de resina compuesta - una superficie, posterior.'),
    ('D2392', 'A base de resina compuesta - dos superficies, posterior.'),
    ('D2393', 'A base de resina compuesta - tres superficies, posterior.'),
    ('D2394', 'Compuesto base - cuatro o más superficies de resina, posterior.'),
    ('D3110', 'Recubrimiento pulpar - directa (excluyendo la reconstrucción final).'),
    ('D3120', 'Recubrimiento pulpar - indirectos (excluyendo la reconstrucción final).'),
    ('D3220', 'Pulpotomía terapéutica (excluyendo la reconstrucción final) - retirada de la pulpa coronal a la dentino cemental unión y la aplicación de la medicación.'),
    ('D3221', 'Pulpar, desbridamiento los dientes primarios y permanentes.'),
    ('D3222', 'Pulpotomía parcial para apexogénesis - diente permanente con el desarrollo radicular incompleto.'),
    ('D4320', 'Provisional ferulización - intracoronales.'),
    ('D4321', 'Férula provisional extracoronal.'),
    ('D7000 - D7999X', 'Extracciones (incluye anestesia local, sutura, si es necesario, y el cuidado posoperatorio de rutina).'),
    ('D7111', 'Extracciones remanentes coronal, dicente temporal.'),
    ('D7140', 'Extracción del diente o raíz expuesta.'),
    ('D7510', 'Incisión de drenaje de absceso - tejido blando intraoral.'),
    ('D7511', 'Incisión de drenaje de absceso - tejido blando intrabucal - complicado (incluye drenaje de múltiples espacios faciales).'),
    ('D7520', 'Incisión y drenaje de absceso tejidos blandos extraorales.'),
    ('D7521', 'Incisión o drenaje de absceso- tejidos blandos extraorales-complicado (incluyen drenaje de múltiples espacios faciales).'),
    ('D7530', 'Extracción de cuerpo extraño de la mucosa, la piel o tejido alveolar subcutáneo, la eliminación de la reacción D7540 producir cuerpos extraños, sistema músculo esquelético.'),
    ('D7820', 'Reducción cerrada de la luxación ATM.'),
    ('D7910', 'Sutura de heridas pequeñas recientes de hasta 5cm.'),
    ('D9215', 'Anestesia local.'),
    ('D9310', 'Consulta de servicio de diagnóstico proporcionado por el dentista u otro médico que solicita dentista o médico.'),
    ('D9910', 'Aplicación de medicamento de sensibilización.'),
    ('D9911', 'Aplicación de resina se sensibilización de la superficie del cuello/o de la raíz, por diente.'),
    ('D9930', 'Tratamiento de las complicaciones (pos-quirúrgico) -circunstancia excepcionales.'),
    ('D9940', 'Ajuste oclusal.')
]

cursor = conn.cursor()
sql = "INSERT INTO NomenclaturaProcedimiento (codigoProcs, descripcion) VALUES (%s, %s)"
cursor.executemany(sql, nomenclatura_procedimientos)
conn.commit()

# Insertar registros en la tabla catalogoPiezaDental
catalogo_piezas_dentales = [
    ('SD11', '11', 'Superior Derecho'),
    ('SD12', '12', 'Superior Derecho'),
    ('SD13', '13', 'Superior Derecho'),
    ('SD14', '14', 'Superior Derecho'),
    ('SD15', '15', 'Superior Derecho'),
    ('SD16', '16', 'Superior Derecho'),
    ('SD17', '17', 'Superior Derecho'),
    ('SD18', '18', 'Superior Derecho'),
    ('SI21', '21', 'Superior Izquierdo'),
    ('SI22', '22', 'Superior Izquierdo'),
    ('SI23', '23', 'Superior Izquierdo'),
    ('SI24', '24', 'Superior Izquierdo'),
    ('SI25', '25', 'Superior Izquierdo'),
    ('SI26', '26', 'Superior Izquierdo'),
    ('SI27', '27', 'Superior Izquierdo'),
    ('SI28', '28', 'Superior Izquierdo'),
    ('II31', '31', 'Inferior Izquierdo'),
    ('II32', '32', 'Inferior Izquierdo'),
    ('II33', '33', 'Inferior Izquierdo'),
    ('II34', '34', 'Inferior Izquierdo'),
    ('II35', '35', 'Inferior Izquierdo'),
    ('II36', '36', 'Inferior Izquierdo'),
    ('II37', '37', 'Inferior Izquierdo'),
    ('II38', '38', 'Inferior Izquierdo'),
    ('ID41', '41', 'Inferior Derecho'),
    ('ID42', '42', 'Inferior Derecho'),
    ('ID43', '43', 'Inferior Derecho'),
    ('ID44', '44', 'Inferior Derecho'),
    ('ID45', '45', 'Inferior Derecho'),
    ('ID46', '46', 'Inferior Derecho'),
    ('ID47', '47', 'Inferior Derecho'),
    ('ID48', '48', 'Inferior Derecho'),
    ('SD51', '51', 'Superior Derecho'),
    ('SD52', '52', 'Superior Derecho'),
    ('SD53', '53', 'Superior Derecho'),
    ('SD54', '54', 'Superior Derecho'),
    ('SD55', '55', 'Superior Derecho'),
    ('SI61', '61', 'Superior Izquierdo'),
    ('SI62', '62', 'Superior Izquierdo'),
    ('SI63', '63', 'Superior Izquierdo'),
    ('SI64', '64', 'Superior Izquierdo'),
    ('SI65', '65', 'Superior Izquierdo'),
    ('II71', '71', 'Inferior Izquierdo'),
    ('II72', '72', 'Inferior Izquierdo'),
    ('II73', '73', 'Inferior Izquierdo'),
    ('II74', '74', 'Inferior Izquierdo'),
    ('II75', '75', 'Inferior Izquierdo'),
    ('ID81', '81', 'Inferior Derecho'),
    ('ID82', '82', 'Inferior Derecho'),
    ('ID83', '83', 'Inferior Derecho'),
    ('ID84', '84', 'Inferior Derecho'),
    ('ID85', '85', 'Inferior Derecho')
]

cursor = conn.cursor()
sql = "INSERT INTO catalogoPiezaDental (codigoPieza, numeroDiente, cuadrante) VALUES (%s, %s, %s)"
cursor.executemany(sql, catalogo_piezas_dentales)
conn.commit()

# Insertar registros en la tabla codigoCIE10
codigos_cie10 = [
    ('A422', 'Actinomicosis cervicofacial.'),
    ('B002', 'Gingivoestomatitis Y Faringoamigdalitis Herpética.'),
    ('B009', 'Infección Debida A El Virus Del Herpes, No Especificada.'),
    ('B084', 'Estomatitis Vesicular Enteroviral Con Exantema.'),
    ('F808', 'Otros Trastornos Del Desarrollo Del Habla Y Del Lenguaje.'),
    ('F809', 'Trastorno Del Desarrollo Del Habla Y Del Lenguaje No Especificado.'),
    ('G500', 'Neuralgia Del Trigémino.'),
    ('G501', 'Dolor Facial Atípico.'),
    ('G508', 'Otros Trastornos Del Trigémino.'),
    ('G509', 'Trastornos Del Trigémino, No Especificado.'),
    ('K000', 'Anodoncia.'),
    ('K001', 'Dientes Supernumerarios.'),
    ('K002', 'Anomalías Del Tamaño Y De La Forma Del Diente.'),
    ('K003', 'Dientes Moteados.'),
    ('K004', 'Alteraciones En La Formación Dentaria.'),
    ('K005', 'Alteraciones Hereditarias De La Estructura Dentaria, No Clasificadas En Otra Parte.'),
    ('K006', 'Alteraciones En La Erupción Dentaria.'),
    ('K007', 'Síndrome De La Erupción Dentaria.'),
    ('K020', 'Caries Limitada Al Esmalte.'),
    ('K021', 'Caries De La Dentina.')
]

cursor = conn.cursor()
sql = "INSERT INTO codigoCIE10 (codigoCIE, descripcion) VALUES (%s, %s)"
cursor.executemany(sql, codigos_cie10)
conn.commit()


# Obtener todos los códigos de procedimiento, pieza dental y código CIE10
cursor = conn.cursor()
cursor.execute("SELECT codigoProcs FROM NomenclaturaProcedimiento")
codigos_procs = cursor.fetchall()

cursor.execute("SELECT codigoPieza FROM catalogoPiezaDental")
codigos_piezas = cursor.fetchall()

cursor.execute("SELECT codigoCIE FROM codigoCIE10")
codigos_cie10 = cursor.fetchall()

# Generar registros aleatorios para la tabla Diagnostico
for _ in range(100):
    id_historia_o = random.randint(1, 100)
    codigo_procs = random.choice(codigos_procs)[0]
    codigo_pieza = random.choice(codigos_piezas)[0]
    codigo_cie10 = random.choice(codigos_cie10)[0]
    observacion = fake.sentence() if random.choice([0, 1]) else None

    # Insertar registro en la tabla Diagnostico
    cursor = conn.cursor()
    sql = "INSERT INTO Diagnostico (idHistoriaO, codigoProcs, codigoPieza, codigoCIE, observacion) VALUES (%s, %s, %s, %s, %s)"
    values = (id_historia_o, codigo_procs, codigo_pieza, codigo_cie10, observacion)
    cursor.execute(sql, values)
    conn.commit()

# Cerrar la conexión a la base de datos
conn.close()


