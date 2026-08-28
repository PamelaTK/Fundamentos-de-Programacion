Algoritmo validar_descarga
	Definir empresa Como Caracter
	definir permiso Como Caracter
	definir tipo_permiso Como Caracter
	definir permiso_valido Como Logico
	definir volumen_agua Como Real
	definir contiene_quimicos como lógico
	definir cantidad_quimicos como entero
	definir sustancia Como Caracter
	definir concentracion como real
	definir limite como real
	definir acceso Como Logico
	definir contador Como Entero
	
	acceso <- Verdadero
	
	Escribir "Nombre de la empresa:"
	leer empresa
	
	Escribir "Número de permiso:"
	Leer permiso
	
	Escribir "Tipo de permiso:" 
	Leer tipo_permiso
	
	Si tipo_permiso <> "CONAGUA-01-001" y tipo_permiso <> "CONAGUA-01-011" entonces 
		escribir "ACCESO DENEGADO"
		acceso <- Falso
	FinSi
	
	si acceso = Verdadero Entonces
		escribir "¿El permiso está en regla? (Verdadero/Falso)"
		leer permiso_valido
		
		si permiso_valido = falso Entonces
			escribir "ACCESO DENEGADO"
			acceso <- falso
		FinSi
	FinSi
	
	si acceso = verdadero Entonces
		escribir"Cantidad de agua a descargar:"
		leer volumen_agua
		
		escribir"¿El agua contiene sustancias químicas? (Verdadero/Falso):"
		leer contiene_quimicos
		
		Si contiene_quimicos = verdadero Entonces
			escribir"¿Cuántas sustancias contiene?"
			leer cantidad_quimicos
			
			para contador <- 1 hasta cantidad_quimicos hacer
				Escribir "Nombre de la sustancia:"
				leer sustancia
				
				escribir "Concentración en ppm:"
				leer concentracion
				
				Escribir "Límite establecido en ppm:"
				leer limite
				
				si concentracion > limite entonces 
					escribir "ACCESO DENEGADO"
					acceso <- Falso
				FinSi
			FinPara
		FinSi
	FinSi
	
	Si acceso = Verdadero Entonces
		Escribir "Datos de la empresa"
		Escribir "Empresa:", empresa
		Escribir "Número de permiso:", permiso
		Escribir "Tipo de permiso:" , tipo_permiso
		Escribir "De acuerdo, tiene autorización para proseguir con su desecho."
	FinSi
	
FinAlgoritmo
