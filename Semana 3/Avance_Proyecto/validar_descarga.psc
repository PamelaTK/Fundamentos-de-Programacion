Algoritmo validar_descarga
	Definir empresa Como Cadena
	Definir permiso Como Cadena
	Definir tipo_permiso Como Cadena
	Definir permiso_valido Como Logico
	Definir volumen_agua Como Real
	Definir contiene_quimicos Como Logico
	Definir cantidad_quimicos Como Entero
	Definir sustancia Como Cadena
	Definir concentracion Como Real
	Definir limite Como Real
	Definir acceso Como Logico
	Definir contador Como Entero
	acceso <- Verdadero
	Escribir 'Nombre de la empresa:'
	Leer empresa
	Escribir 'Número de permiso:'
	Leer permiso
	Escribir 'Tipo de permiso:'
	Leer tipo_permiso
	Si tipo_permiso<>'CONAGUA-01-001' Y tipo_permiso<>'CONAGUA-01-011' Entonces
		Escribir 'ACCESO DENEGADO'
		acceso <- Falso
	FinSi
	Si acceso=Verdadero Entonces
		Escribir "¿El permiso está en regla? (Verdadero/Falso)'
		Leer permiso_valido
		Si permiso_valido=Falso Entonces
			Escribir 'ACCESO DENEGADO'
			acceso <- Falso
		FinSi
	FinSi
	Si acceso=Verdadero Entonces
		Escribir 'Cantidad de agua a descargar:'
		Leer volumen_agua
		Escribir '¿El agua contiene sustancias químicas? (Verdadero/Falso):'
		Leer contiene_quimicos
		Si contiene_quimicos=Verdadero Entonces
			Escribir '¿Cuántas sustancias contiene?'
			Leer cantidad_quimicos
			Para contador<-1 Hasta cantidad_quimicos Hacer
				Escribir 'Nombre de la sustancia:'
				Leer sustancia
				Escribir 'Concentración en ppm:'
				Leer concentracion
				Escribir 'Límite establecido en ppm:'
				Leer limite
				Si concentracion>limite Entonces
					Escribir 'ACCESO DENEGADO'
					acceso <- Falso
				FinSi
			FinPara
		FinSi
	FinSi
	Si acceso=Verdadero Entonces
		Escribir 'Datos de la empresa'
		Escribir 'Empresa:', empresa
		Escribir 'Número de permiso:', permiso
		Escribir 'Tipo de permiso:', tipo_permiso
		Escribir 'De acuerdo, tiene autorización para proseguir con su desecho.'
	FinSi
FinAlgoritmo
