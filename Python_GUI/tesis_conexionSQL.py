import mysql.connector
from PyQt5.QtWidgets import QMessageBox

class ConectaDB:
    def __init__(self):
        self._host = "127.0.0.1"
        self._puerto = 3306
        self._usuario = "root"
        self._contraseña = "2011"
        self._db = "recuperacion1"
        self.con = None
        self.cursor = None

    def conecta_base_datos(self):
        # Establece la conexión a la base de datos
        self.con = mysql.connector.connect(
            host=self._host,
            port=self._puerto,
            database=self._db,
            user=self._usuario,
            password=self._contraseña
        )

        # Crea un cursor para ejecuta consultas de SQL
        self.cursor = self.con.cursor(dictionary=True)

########## RECEPTOR  - Consultas en SQL para funciones básicas como agregar, buscar, eliminar y actualizar datos
    def agregar_datos_0(self, id_receptor, fecha_registro, nombre, edad, etnia, sexo,fecha_dg_erc,ter_sust_act,inst_provee_hd, vol_residual, tiempo_anuria, grupo_sanguineo,
                                        procedencia, residencia, ocupacion, etiologia_erc, tiempo_ini_st_renal, tiempo_dialisis, riesgo_cmv, yd, yi, fd, fi, est_acc_vasc, obs_acc_vasc):
        try:
            self.conecta_base_datos()  # Se asegura de que la conexión está abierta
            query = """INSERT INTO receptor (id_receptor, fecha_registro, nombre, edad, etnia, sexo,fecha_dg_erc,ter_sust_act,inst_provee_hd, vol_residual, tiempo_anuria, grupo_sanguineo,
                                        procedencia, residencia, ocupacion, etiologia_erc, tiempo_ini_st_renal, tiempo_dialisis, riesgo_cmv, yd, yi, fd, fi, est_acc_vasc, obs_acc_vasc)
                    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""
            
            # Si obs_acc_vasc está vacío, lo convertimos a None
            obs_acc_vasc = obs_acc_vasc if obs_acc_vasc else None
        
            self.cursor.execute(query, (id_receptor, fecha_registro, nombre, edad, etnia, sexo,fecha_dg_erc,ter_sust_act,inst_provee_hd, vol_residual, tiempo_anuria, grupo_sanguineo,
                                        procedencia, residencia, ocupacion, etiologia_erc, tiempo_ini_st_renal, tiempo_dialisis, riesgo_cmv, yd, yi, fd, fi, est_acc_vasc, obs_acc_vasc))
            self.con.commit()  # Confirma los cambios en la base de datos
            return True  # Indica que la inserción fue exitosa
        except Exception as e:
            QMessageBox.critical(None, "Error al Agregar Paciente", f"Error: {str(e)}")
            return False  # Indica que hubo un error
        finally:
            self.cursor.close()  # Cierra el cursor
            self.con.close()  # Cierra la conexión

    def buscar_datos_0(self):
        try:
            self.conecta_base_datos()
            query = "SELECT * FROM receptor"
            self.cursor.execute(query)
            results = self.cursor.fetchall()
            return results  # Retorna los resultados de la consulta
        except Exception as e:
            QMessageBox.critical(None, "Error al Buscar Pacientes", f"Error: {str(e)}")
            return []  # Retorna una lista vacía si hay un error
        finally:
            self.cursor.close()
            self.con.close()

    def buscar_datos_01(self, id_receptor):
        try:
            self.conecta_base_datos()
            query = "SELECT * FROM receptor WHERE id_receptor = %s"
            self.cursor.execute(query, (id_receptor,))
            result = self.cursor.fetchone()
            return result
        except Exception as e:
            QMessageBox.critical(None, "Error al Obtener Datos del Receptor", f"Error: {str(e)}")
            return None
        finally:
            self.cursor.close()
            self.con.close()

    def eliminar_datos_0(self, id_receptor):
        try:
            self.conecta_base_datos()
            query = "DELETE FROM receptor WHERE id_receptor = %s"
            self.cursor.execute(query, (id_receptor,))
            self.con.commit()
            return True
        except Exception as e:
            QMessageBox.critical(None, "Error al Eliminar Paciente", f"Error: {str(e)}")
            return False
        finally:
            self.cursor.close()
            self.con.close()

    def actualizar_datos_0(self, id_receptor, fecha_registro, nombre, edad, etnia, sexo,fecha_dg_erc,ter_sust_act,inst_provee_hd, vol_residual, tiempo_anuria, grupo_sanguineo,
                       procedencia, residencia, ocupacion, etiologia_erc, tiempo_ini_st_renal, tiempo_dialisis, riesgo_cmv, yd, yi, fd, fi, est_acc_vasc, obs_acc_vasc):
        try:
            self.conecta_base_datos()
            query = """UPDATE receptor SET fecha_registro = %s, nombre = %s, edad = %s, etnia = %s, sexo = %s, fecha_dg_erc = %s, ter_sust_act = %s, inst_provee_hd= %s, vol_residual= %s, tiempo_anuria= %s, grupo_sanguineo= %s,
                    procedencia= %s, residencia= %s, ocupacion= %s, etiologia_erc= %s, tiempo_ini_st_renal= %s, tiempo_dialisis= %s, riesgo_cmv= %s, yd= %s, yi= %s, fd= %s, fi= %s, est_acc_vasc= %s, obs_acc_vasc= %s

                    WHERE id_receptor = %s"""
            self.cursor.execute(query, (fecha_registro, nombre, edad, etnia, sexo, fecha_dg_erc, ter_sust_act,inst_provee_hd, vol_residual, tiempo_anuria, grupo_sanguineo,
                                        procedencia, residencia, ocupacion, etiologia_erc, tiempo_ini_st_renal, tiempo_dialisis, riesgo_cmv, yd, yi, fd, fi, est_acc_vasc, obs_acc_vasc,id_receptor))
            self.con.commit()  # Confirma los cambios
            return True  # Indica que la actualización fue exitosa
        except Exception as e:
            QMessageBox.critical(None, "Error al Actualizar Paciente", f"Error: {str(e)}")
            return False  # Indica que hubo un error
        finally:
            self.cursor.close()
            self.con.close()

################## DONANTES     - Consultas en SQL para funciones básicas como agregar, buscar, eliminar y actualizar datos

    def agregar_datos_1(self, id_donante, fecha_registro_1, nombre, sexo_2, edad_2, grupo_sanguineo_2):
        try:
            self.conecta_base_datos()  # Se asegura de que la conexión está abierta
            query = """INSERT INTO donante (id_donante, fecha_registro, nombre, sexo, edad, grupo_sanguineo)
                    VALUES (%s, %s, %s, %s, %s, %s)"""
        
            self.cursor.execute(query, (id_donante, fecha_registro_1, nombre, sexo_2, edad_2, grupo_sanguineo_2))
            self.con.commit()  # Confirma los cambios en la base de datos
            return True  # Indica que la inserción fue exitosa
        except Exception as e:
            QMessageBox.critical(None, "Error al Agregar Donante", f"Error: {str(e)}")
            return False  # Indica que hubo un error
        finally:
            self.cursor.close()  # Cierra el cursor
            self.con.close()  # Cierra la conexión

    def buscar_datos_1(self):
        try:
            self.conecta_base_datos()
            query = "SELECT * FROM donante"
            self.cursor.execute(query)
            results = self.cursor.fetchall()
            return results  # Retorna los resultados de la consulta
        except Exception as e:
            QMessageBox.critical(None, "Error al Buscar Donantes", f"Error: {str(e)}")
            return []  # Retorna una lista vacía si hay un error
        finally:
            self.cursor.close()
            self.con.close()

    def buscar_datos_1_2(self, id_donante):
        try:
            self.conecta_base_datos()
            query = "SELECT * FROM donante WHERE id_donante = %s"
            self.cursor.execute(query, (id_donante,))
            result = self.cursor.fetchone()
            return result
        except Exception as e:
            QMessageBox.critical(None, "Error al Obtener Datos del Donante", f"Error: {str(e)}")
            return None
        finally:
            self.cursor.close()
            self.con.close()

    def eliminar_datos_1(self, id_donante):
        try:
            self.conecta_base_datos()
            query = "DELETE FROM donante WHERE id_donante = %s"
            self.cursor.execute(query, (id_donante,))
            self.con.commit()
            return True
        except Exception as e:
            QMessageBox.critical(None, "Error al Eliminar Donante", f"Error: {str(e)}")
            return False
        finally:
            self.cursor.close()
            self.con.close()

    def actualizar_datos_1(self, id_donante, fecha_registro_1, nombre, sexo_2, edad_2, grupo_sanguineo_2):
        try:
            self.conecta_base_datos()
            query = """UPDATE donante SET fecha_registro = %s, nombre= %s, sexo= %s, edad= %s, grupo_sanguineo= %s WHERE id_donante= %s """
            self.cursor.execute(query, (fecha_registro_1, nombre, sexo_2, edad_2, grupo_sanguineo_2,id_donante))
            self.con.commit()  # Confirma los cambios
            return True  # Indica que la actualización fue exitosa
        except Exception as e:
            QMessageBox.critical(None, "Error al Actualizar Donante", f"Error: {str(e)}")
            return False  # Indica que hubo un error
        finally:
            self.cursor.close()
            self.con.close()

################## ANTECEDENTES  - Consultas en SQL para funciones básicas como agregar, buscar, eliminar y actualizar datos

    def agregar_datos_2(self, id_antecedente, id_paciente_2, fecha_registro_2, ant_medicos, ant_quirurgicos, ant_traumaticos, ant_alergicos, ant_transfusionales, ant_ginecoobstetricos):
        try:
            self.conecta_base_datos()  # Se asegura de que la conexión está abierta
            query = """INSERT INTO a_antecedentes (id_antecedente, id_paciente_2, fecha_registro_2, ant_medicos, ant_quirurgicos, ant_traumaticos, ant_alergicos, ant_transfusionales, ant_ginecoobstetricos)
                    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"""
            
            # Ejecuta la consulta con los valores proporcionados
            self.cursor.execute(query, (id_antecedente, id_paciente_2, fecha_registro_2, ant_medicos, ant_quirurgicos, ant_traumaticos, ant_alergicos, ant_transfusionales, ant_ginecoobstetricos))
            self.con.commit()  # Confirma los cambios en la base de datos
            return True  # Indica que la inserción fue exitosa
        except Exception as e:
            QMessageBox.critical(None, "Error al agregar antecedentes", f"Error: {str(e)}")
            return False  # Indica que hubo un error
        finally:
            self.cursor.close()  # Cierra el cursor
            self.con.close()  # Cierra la conexión

    def buscar_antecedentes_receptor(self):
        try:
            self.conecta_base_datos()  # Se asegura de que la conexión está abierta

            query = """
            SELECT * FROM a_antecedentes
            WHERE id_paciente_2 IN (SELECT id_receptor FROM receptor)
            """
            self.cursor.execute(query)
            results = self.cursor.fetchall()
            return results  # Retorna los resultados de la consulta

        except Exception as e:
            QMessageBox.critical(None, "Error al Buscar Antecedentes", f"Error: {str(e)}")
            return []  # Retorna una lista vacía si hay un error

        finally:
            self.cursor.close() 
            self.con.close()  

    def obtener_datos_antecedente(self, id_antecedente):
        try:
            self.conecta_base_datos()
            query = "SELECT * FROM a_antecedentes WHERE id_antecedente = %s"
            self.cursor.execute(query, (id_antecedente,))
            result = self.cursor.fetchone()
            return result
        except Exception as e:
            QMessageBox.critical(None, "Error al Obtener Datos del Antecedente", f"Error: {str(e)}")
            return None
        finally:
            self.cursor.close()
            self.con.close()

    def limpiar_datos_2(self):
        try:
            self.conecta_base_datos()  #Se asegura de que la conexión está abierta
            query = "DELETE FROM antecedentes"  # Eliminar todos los registros de antecedentes
            self.cursor.execute(query)
            self.con.commit()  # Confirma los cambios
            QMessageBox.information(None, "Éxito", "Todos los antecedentes han sido eliminados correctamente.")
        except Exception as e:
            QMessageBox.critical(None, "Error al Limpiar Antecedentes", f"Error: {str(e)}")
        finally:
            self.cursor.close()  # Cierra el cursor
            self.con.close()  # Cierra la conexión

    def eliminar_datos_2(self, id_antecedente):
        try:
            self.conecta_base_datos()  # Se asegura de que la conexión está abierta
            query = "DELETE FROM a_antecedentes WHERE id_antecedente = %s"
            self.cursor.execute(query, (id_antecedente,))
            self.con.commit()  # Confirma los cambios en la base de datos
            return True  # Indica que la eliminación fue exitosa
        except Exception as e:
            QMessageBox.critical(None, "Error al Eliminar Antecedente", f"Error: {str(e)}")
            return False  # Indica que hubo un error
        finally:
            self.cursor.close()  # Cierra el cursor
            self.con.close()  # Cierra la conexión

    def actualizar_datos_2(self, id_antecedente, id_paciente_2, fecha_registro_2, ant_medicos, ant_quirurgicos, ant_traumaticos, ant_alergicos, ant_transfusionales, ant_ginecoobstetricos):
        try:
            self.conecta_base_datos()  # Se asegura de que la conexión está abierta
            query = """UPDATE a_antecedentes SET 
                    id_paciente_2 = %s,
                    fecha_registro_2 = %s,
                    ant_medicos = %s,
                    ant_quirurgicos = %s,
                    ant_traumaticos = %s,
                    ant_alergicos = %s,
                    ant_transfusionales = %s,
                    ant_ginecoobstetricos = %s
                    WHERE id_antecedente = %s"""
            
            # Ejecuta la consulta con los valores proporcionados
            self.cursor.execute(query, (id_paciente_2, fecha_registro_2, ant_medicos, ant_quirurgicos, ant_traumaticos, ant_alergicos, ant_transfusionales, ant_ginecoobstetricos, id_antecedente))
            self.con.commit()  # Confirma los cambios en la base de datos
            return True  # Indica que la actualización fue exitosa
        except Exception as e:
            QMessageBox.critical(None, "Error al Actualizar Antecedentes", f"Error: {str(e)}")
            return False  # Indica que hubo un error
        finally:
            self.cursor.close()  # Cierra el cursor
            self.con.close()  # Cierra la conexión

################## FASE 1 - Consultas en SQL para funciones básicas como agregar, buscar, eliminar y actualizar datos
    def agregar_datos_3(self, id_fase1, id_paciente_3, fecha_registro_3, peso, talla, valor_imc, est_imc,
                        hema_wbc, hema_neutro, hema_hgb, hema_hct, hema_plt,
                        creatinina, tfg, bun, gli_pre, gli_post, hb_glicolisada,
                        rd_longitud, rd_anchura, rd_grosor,
                        ri_longitud, ri_anchura, ri_grosor,
                        usg_hep_bil, obs_usg_hep_bil, pra):
        try:
            self.conecta_base_datos()  # Se asegura de que la conexión está abierta
            query = """INSERT INTO fase_1 (id_fase1, id_paciente_3,fecha_registro_3, peso, talla, valor_imc, est_imc,
                                            hema_wbc, hema_neutro, hema_hgb, hema_hct, hema_plt,
                                            creatinina, tfg, bun, gli_pre, gli_post, hb_glicolisada,
                                            rd_longitud, rd_anchura, rd_grosor,
                                            ri_longitud, ri_anchura, ri_grosor,
                                            usg_hep_bil, obs_usg_hep_bil, pra)
                    VALUES (%s, %s, %s, %s, %s, %s, %s,
                            %s, %s, %s, %s, %s,
                            %s, %s, %s, %s, %s, %s,
                            %s,%s,%s,%s,%s,%s,
                            %s,%s,%s)"""
            
            # Si obs_usg_hep_bil está vacío o None lo convertimos a None para evitar errores
            obs_usg_hep_bil = obs_usg_hep_bil if obs_usg_hep_bil else None

            # Ejecuta la consulta con los valores proporcionados
            self.cursor.execute(query,
                                (id_fase1, id_paciente_3,fecha_registro_3, peso, talla, valor_imc, est_imc,
                                    hema_wbc, hema_neutro, hema_hgb, hema_hct, hema_plt,
                                    creatinina, tfg, bun, gli_pre, gli_post, hb_glicolisada,
                                    rd_longitud, rd_anchura, rd_grosor,
                                    ri_longitud, ri_anchura, ri_grosor,
                                    usg_hep_bil, obs_usg_hep_bil, pra))
            self.con.commit()  # Confirma los cambios en la base de datos
            return True  # Indica que la inserción fue exitosa
        except Exception as e:
            QMessageBox.critical(None,"Error al Agregar Fase 1",f"Error: {str(e)}")
            return False  # Indica que hubo un error
        finally:
            self.cursor.close()  # Cierra el cursor
            self.con.close()  # Cierra la conexión

    def buscar_f1_receptor(self):
        try:
            self.conecta_base_datos()  # Se asegura de que la conexión está abierta

            query = """
            SELECT * FROM fase_1
            WHERE id_paciente_3 IN (SELECT id_receptor FROM receptor)
            """
            self.cursor.execute(query)
            results = self.cursor.fetchall()
            return results  # Retorna los resultados de la consulta

        except Exception as e:
            QMessageBox.critical(None, "Error al Buscar Fase 1", f"Error: {str(e)}")
            return []  # Retorna una lista vacía si hay un error

        finally:
            self.cursor.close()  # Cierra el cursor
            self.con.close()  # Cierra la conexión

    def obtener_datos_fase1(self, id_fase1):
        try:
            self.conecta_base_datos()
            query = "SELECT * FROM fase_1 WHERE id_fase1 = %s"
            self.cursor.execute(query, (id_fase1,))
            result = self.cursor.fetchone()
            return result
        except Exception as e:
            QMessageBox.critical(None, "Error al Obtener Datos de Fase 1", f"Error: {str(e)}")
            return None
        finally:
            self.cursor.close()
            self.con.close()

    def limpiar_datos_3(self):
        try:
            self.conecta_base_datos()  # Se asegura de que la conexión está abierta
            query = "DELETE FROM fase_1"  # Eliminar todos los registros de la tabla fase1
            self.cursor.execute(query)
            self.con.commit()  # Confirma los cambios
            QMessageBox.information(None, "Éxito", "Todos los registros de Fase 1 han sido eliminados correctamente.")
        except Exception as e:
            QMessageBox.critical(None, "Error al Limpiar Datos de Fase 1", f"Error: {str(e)}")
        finally:
            self.cursor.close()  # Cierra el cursor
            self.con.close()  # Cierra la conexión

    def eliminar_datos_3(self, id_fase1):
        try:
            self.conecta_base_datos()  # Se asegura de que la conexión está abierta
            query = "DELETE FROM fase_1 WHERE id_fase1 = %s"
            self.cursor.execute(query, (id_fase1,))
            self.con.commit()  # Confirma los cambios en la base de datos
            return True  # Indica que la eliminación fue exitosa
        except Exception as e:
            QMessageBox.critical(None, "Error al Eliminar Datos de Fase 1", f"Error: {str(e)}")
            return False  # Indica que hubo un error
        finally:
            self.cursor.close()  # Cierra el cursor
            self.con.close()  # Cierra la conexión      

    def actualizar_datos_3(self, id_fase1, id_paciente_3,fecha_registro_3, peso, talla, valor_imc, est_imc,
                        hema_wbc, hema_neutro, hema_hgb, hema_hct, hema_plt,
                        creatinina, tfg, bun, gli_pre, gli_post, hb_glicolisada,
                        rd_longitud, rd_anchura, rd_grosor,
                        ri_longitud, ri_anchura, ri_grosor,
                        usg_hep_bil, obs_usg_hep_bil, pra):
        try:
            self.conecta_base_datos()  # Se asegura de que la conexión está abierta
            query = """UPDATE fase_1 SET 
                    id_paciente_3 = %s,
                    fecha_registro_3 = %s,
                    peso = %s,
                    talla = %s,
                    valor_imc = %s,
                    est_imc = %s,
                    hema_wbc = %s,
                    hema_neutro = %s,
                    hema_hgb = %s,
                    hema_hct = %s,
                    hema_plt = %s,
                    creatinina = %s,
                    tfg = %s,
                    bun = %s,
                    gli_pre = %s,
                    gli_post = %s,
                    hb_glicolisada = %s,
                    rd_longitud = %s,
                    rd_anchura = %s,
                    rd_grosor = %s,
                    ri_longitud = %s,
                    ri_anchura = %s,
                    ri_grosor = %s,
                    usg_hep_bil = %s,
                    obs_usg_hep_bil = %s,
                    pra = %s
                    WHERE id_fase1 = %s"""
            
            # Si obs_usg_hep_bil está vacío o None lo convertimos a None para evitar errores
            obs_usg_hep_bil = obs_usg_hep_bil if obs_usg_hep_bil else None

            # Ejecuta la consulta con los valores proporcionados
            self.cursor.execute(query, (id_paciente_3, fecha_registro_3, peso, talla, valor_imc, est_imc,
                                        hema_wbc, hema_neutro, hema_hgb, hema_hct, hema_plt,
                                        creatinina, tfg, bun, gli_pre, gli_post, hb_glicolisada,
                                        rd_longitud, rd_anchura, rd_grosor,
                                        ri_longitud, ri_anchura, ri_grosor,
                                        usg_hep_bil, obs_usg_hep_bil, pra,
                                        id_fase1))
            self.con.commit()  # Confirma los cambios en la base de datos
            return True  # Indica que la actualización fue exitosa
        except Exception as e:
            QMessageBox.critical(None, "Error al Actualizar Datos de Fase 1", f"Error: {str(e)}")
            return False  # Indica que hubo un error
        finally:
            self.cursor.close()  # Cierra el cursor
            self.con.close()  # Cierra la conexión

################## FASE 2A - Consultas en SQL para funciones básicas como agregar, buscar, eliminar y actualizar datos
    def agregar_datos_4(self, id_fase2a, id_paciente_4, fecha_registro_4, vac_cov19, dos1_cov19, tipo_dos1,
                        dos2_cov19, tipo_dos2, dos3_cov19, tipo_dos3, vac_influen, dos_influen,
                        vac_neum, dos_neum, cert_dental, obs_dental, eval_psico, obs_eval1,
                        eval_trab_social, obs_eval2, eval_legal, obs_eval3, eval_nutri,
                        obs_eval4, masa_muscular, grasa, agua):
        try:
            self.conecta_base_datos()  # Se asegura de que la conexión está abierta
            query = """INSERT INTO fase_2a (id_fase2a, id_paciente_4, fecha_registro_4,
                                            vac_cov19, dos1_cov19, tipo_dos1,
                                            dos2_cov19, tipo_dos2, dos3_cov19,
                                            tipo_dos3, vac_influen, dos_influen,
                                            vac_neum, dos_neum, cert_dental,
                                            obs_dental, eval_psico, obs_eval1,
                                            eval_trab_social, obs_eval2,
                                            eval_legal, obs_eval3,
                                            eval_nutri, obs_eval4,
                                            masa_muscular, grasa, agua)
                    VALUES (%s, %s, %s,
                            %s, %s, %s,
                            %s, %s, %s,
                            %s, %s, %s,
                            %s, %s, %s,
                            %s, %s, %s,
                            %s,%s,%s,
                            %s,%s,%s,%s,%s,%s)"""
            
            # Ejecuta la consulta con los valores proporcionados
            self.cursor.execute(query,
                                (id_fase2a,id_paciente_4 ,fecha_registro_4,
                                vac_cov19 ,dos1_cov19 ,tipo_dos1 ,
                                dos2_cov19 ,tipo_dos2 ,dos3_cov19 ,
                                tipo_dos3 ,vac_influen ,dos_influen ,
                                vac_neum ,dos_neum ,cert_dental ,
                                obs_dental ,eval_psico ,obs_eval1 ,
                                eval_trab_social ,obs_eval2 ,
                                eval_legal ,obs_eval3 ,
                                eval_nutri ,obs_eval4 ,
                                masa_muscular ,grasa ,agua))
            self.con.commit()  # Confirma los cambios en la base de datos
            return True  # Indica que la inserción fue exitosa
        except Exception as e:
            QMessageBox.critical(None,"Error al Agregar Fase 2a",f"Error: {str(e)}")
            return False  # Indica que hubo un error
        finally:
            self.cursor.close()  # Cierra el cursor
            self.con.close()  # Cierra la conexión


    def buscar_f2a_receptor(self):
        try:
            self.conecta_base_datos()  # Se asegura de que la conexión está abierta

            query = """
            SELECT * FROM fase_2a
            WHERE id_paciente_4 IN (SELECT id_receptor FROM receptor)
            """
            self.cursor.execute(query)
            results = self.cursor.fetchall()
            return results  # Retorna los resultados de la consulta

        except Exception as e:
            QMessageBox.critical(None, "Error al Buscar Fase 2a", f"Error: {str(e)}")
            return []  # Retorna una lista vacía si hay un error

        finally:
            self.cursor.close()  # Cierra el cursor
            self.con.close()  # Cierra la conexión

    def obtener_datos_fase2a(self, id_fase2a):
            try:
                self.conecta_base_datos()
                query = "SELECT * FROM fase_2a WHERE id_fase2a = %s"
                self.cursor.execute(query, (id_fase2a,))
                result = self.cursor.fetchone()
                return result
            except Exception as e:
                QMessageBox.critical(None, "Error al Obtener Datos de Fase 2a", f"Error: {str(e)}")
                return None
            finally:
                self.cursor.close()
                self.con.close()

    def limpiar_datos_4(self):
        try:
            self.conecta_base_datos()  # Se asegura de que la conexión está abierta
            query = "DELETE FROM fase_2a"  # Eliminar todos los registros de la tabla fase_2a
            self.cursor.execute(query)
            self.con.commit()  # Confirma los cambios
            QMessageBox.information(None, "Éxito", "Todos los registros de Fase 2a han sido eliminados correctamente.")
        except Exception as e:
            QMessageBox.critical(None, "Error al Limpiar Datos de Fase 2a", f"Error: {str(e)}")
        finally:
            self.cursor.close()  # Cierra el cursor
            self.con.close()  # Cierra la conexión

    def eliminar_datos_4(self, id_fase2a):
        try:
            self.conecta_base_datos()  # Se asegura de que la conexión está abierta
            query = "DELETE FROM fase_2a WHERE id_fase2a = %s"
            self.cursor.execute(query, (id_fase2a,))
            self.con.commit()  # Confirma los cambios en la base de datos
            return True  # Indica que la eliminación fue exitosa
        except Exception as e:
            QMessageBox.critical(None, "Error al Eliminar Datos de Fase 2a", f"Error: {str(e)}")
            return False  # Indica que hubo un error
        finally:
            self.cursor.close()  # Cierra el cursor
            self.con.close()  # Cierra la conexión

    def actualizar_datos_4(self, id_fase2a, id_paciente_4, fecha_registro_4, vac_cov19, dos1_cov19, tipo_dos1,
                        dos2_cov19, tipo_dos2, dos3_cov19, tipo_dos3, vac_influen, dos_influen,
                        vac_neum, dos_neum, cert_dental, obs_dental, eval_psico, obs_eval1,
                        eval_trab_social, obs_eval2, eval_legal, obs_eval3, eval_nutri,
                        obs_eval4, masa_muscular, grasa, agua):
        try:
            self.conecta_base_datos()  # Se asegura de que la conexión está abierta
            query = """UPDATE fase_2a SET 
                        id_paciente_4 = %s,
                        fecha_registro_4 = %s,
                        vac_cov19 = %s,
                        dos1_cov19 = %s,
                        tipo_dos1 = %s,
                        dos2_cov19 = %s,
                        tipo_dos2 = %s,
                        dos3_cov19 = %s,
                        tipo_dos3 = %s,
                        vac_influen = %s,
                        dos_influen = %s,
                        vac_neum = %s,
                        dos_neum = %s,
                        cert_dental = %s,
                        obs_dental = %s,
                        eval_psico = %s,
                        obs_eval1 = %s,
                        eval_trab_social = %s,
                        obs_eval2 = %s,
                        eval_legal = %s,
                        obs_eval3 = %s,
                        eval_nutri = %s,
                        obs_eval4 = %s,
                        masa_muscular = %s,
                        grasa = %s,
                        agua = %s
                    WHERE id_fase2a = %s"""
            
            # Ejecuta la consulta con los valores proporcionados
            self.cursor.execute(query, (id_paciente_4, fecha_registro_4, vac_cov19, dos1_cov19, tipo_dos1,
                                        dos2_cov19, tipo_dos2, dos3_cov19, tipo_dos3, vac_influen, dos_influen,
                                        vac_neum, dos_neum, cert_dental, obs_dental, eval_psico, obs_eval1,
                                        eval_trab_social, obs_eval2, eval_legal, obs_eval3, eval_nutri,
                                        obs_eval4, masa_muscular, grasa, agua, id_fase2a))
            self.con.commit()  # Confirma los cambios en la base de datos
            return True  # Indica que la actualización fue exitosa
        except Exception as e:
            QMessageBox.critical(None,"Error al Actualizar Datos de Fase 2a",f"Error: {str(e)}")
            return False  # Indica que hubo un error
        finally:
            self.cursor.close()  # Cierra el cursor
            self.con.close()  # Cierra la conexión   


################## FASE 2B- Consultas en SQL para funciones básicas como agregar, buscar, eliminar y actualizar datos
    def agregar_datos_5(self, id_fase2b, id_paciente_5, fecha_registro_5, vih, hepa_b, hepa_c, vdrl,
                            toxo_igg, toxo_igm, rubeo_igg, rubeo_igm, cmv_igg, cmv_igm, herpes_igg,
                            herpes_igm, veb_igg, veb_igm, cuantiferon, obs_cuantiferon,
                            tgo, tgp, bt, bd, bi, dhl, fa, albumina, acido_urico,
                            perfil_hdl, perfil_ldl, perfil_ct, perfil_tg, perfil_vldl,
                            sodio, potasio, fosforo, calcio, magnesio,
                            pth, tsh, t4_libre, c3, c4, bnp,
                            tp, tpt, inr,
                            nivel_ecg, obs_ecg,
                            anti_dna, ana,
                            b2_glicoprot, anticoag_lupico,
                            anticardio_igg_igm,
                            p_anca,c_anca,
                            urocultivo, obs_urocultivo,
                            orocultivo ,obs_orocultivo ,
                            ex_nasal ,obs_nasal):
        try:
            self.conecta_base_datos()  # Se asegura de que la conexión está abierta
            query = """INSERT INTO fase_2b (id_fase2b,id_paciente_5 ,fecha_registro_5 ,
                                            vih ,hepa_b ,hepa_c ,vdrl ,
                                            toxo_igg ,toxo_igm ,rubeo_igg ,rubeo_igm ,
                                            cmv_igg ,cmv_igm ,herpes_igg ,herpes_igm ,
                                            veb_igg ,veb_igm ,cuantiferon ,
                                            obs_cuantiferon ,
                                            tgo,tgp ,bt ,bd ,bi ,
                                            dhl ,fa ,albumina ,acido_urico ,
                                            perfil_hdl ,perfil_ldl ,perfil_ct ,
                                            perfil_tg ,perfil_vldl ,
                                            sodio,potasio,fosforo ,
                                            calcio ,magnesio ,
                                            pth,tsh,t4_libre ,
                                            c3,c4,bnp ,
                                            tp,tpt,inr ,
                                            nivel_ecg ,obs_ecg ,
                                            anti_dna ,ana ,
                                            b2_glicoprot ,anticoag_lupico ,
                                            anticardio_igg_igm ,
                                            p_anca,c_anca ,
                                            urocultivo ,obs_urocultivo ,
                                            orocultivo ,obs_orocultivo ,
                                            ex_nasal ,obs_nasal)
                    VALUES (%s,%s,%s,
                            %s,%s,%s,%s,
                            %s,%s,%s,%s,
                            %s,%s,%s,%s,
                            %s,%s,%s,
                            %s,%s,
                            %s,%s,%s,%s,
                            %s,%s,%s,%s,
                            %s,%s,%s,
                            %s,%s,
                            %s,%s,%s,
                            %s,%s,
                            %s,%s,%s,
                            %s,%s,%s,
                            %s,%s,
                            %s,%s,
                            %s,%s,
                            %s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"""
            
            # Ejecuta la consulta con los valores proporcionados
            self.cursor.execute(query,(id_fase2b,id_paciente_5 ,fecha_registro_5 ,
                                        vih ,hepa_b ,hepa_c ,vdrl ,
                                        toxo_igg,toxo_igm,rubeo_igg,rubeo_igm ,
                                        cmv_igg, cmv_igm, herpes_igg, herpes_igm, 
                                        veb_igg, veb_igm, cuantiferon, 
                                        obs_cuantiferon, 
                                        tgo, tgp, bt, bd, bi, 
                                        dhl, fa, albumina, acido_urico, 
                                        perfil_hdl, perfil_ldl, perfil_ct, 
                                        perfil_tg, perfil_vldl, 
                                        sodio, potasio, fosforo, 
                                        calcio, magnesio, 
                                        pth, tsh, t4_libre, 
                                        c3, c4, bnp, 
                                        tp, tpt, inr, 
                                        nivel_ecg, obs_ecg,
                                        anti_dna, ana, 
                                        b2_glicoprot, anticoag_lupico, 
                                        anticardio_igg_igm, 
                                        p_anca, c_anca,
                                        urocultivo, obs_urocultivo, 
                                        orocultivo, obs_orocultivo,
                                        ex_nasal, obs_nasal))
            self.con.commit()  # Confirma los cambios en la base de datos
            return True  # Indica que la inserción fue exitosa
        except Exception as e:
            QMessageBox.critical(None,"Error al Agregar Fase 2b",f"Error: {str(e)}")
            return False  # Indica que hubo un error
        finally:
            self.cursor.close()  # Cierra el cursor
            self.con.close()  # Cierra la conexión

    def buscar_f2b_receptor(self):
        try:
            self.conecta_base_datos()  # Se asegura de que la conexión está abierta

            query = """
            SELECT * FROM fase_2b
            WHERE id_paciente_5 IN (SELECT id_receptor FROM receptor)
            """
            self.cursor.execute(query)
            results = self.cursor.fetchall()
            return results  # Retorna los resultados de la consulta

        except Exception as e:
            QMessageBox.critical(None, "Error al Buscar Fase 2b", f"Error: {str(e)}")
            return []  # Retorna una lista vacía si hay un error

        finally:
            self.cursor.close()  # Cierra el cursor
            self.con.close()  # Cierra la conexión


    def obtener_datos_fase2b(self, id_fase2b):
                try:
                    self.conecta_base_datos()
                    query = "SELECT * FROM fase_2b WHERE id_fase2b = %s"
                    self.cursor.execute(query, (id_fase2b,))
                    result = self.cursor.fetchone()
                    return result
                except Exception as e:
                    QMessageBox.critical(None, "Error al Obtener Datos de Fase 2b", f"Error: {str(e)}")
                    return None
                finally:
                    self.cursor.close()
                    self.con.close()

    def limpiar_datos_5(self):
        try:
            self.conecta_base_datos()  # Se asegura de que la conexión está abierta
            query = "DELETE FROM fase_2b"  # Eliminar todos los registros de la tabla fase_2b
            self.cursor.execute(query)
            self.con.commit()  # Confirma los cambios
            QMessageBox.information(None, "Éxito", "Todos los registros de Fase 2b han sido eliminados correctamente.")
        except Exception as e:
            QMessageBox.critical(None, "Error al Limpiar Datos de Fase 2b", f"Error: {str(e)}")
        finally:
            self.cursor.close()  # Cierra el cursor
            self.con.close()  # Cierra la conexión

    def eliminar_datos_5(self, id_fase2b):
        try:
            self.conecta_base_datos()  # Se asegura de que la conexión está abierta
            query = "DELETE FROM fase_2b WHERE id_fase2b = %s"
            self.cursor.execute(query, (id_fase2b,))
            self.con.commit()  # Confirma los cambios en la base de datos
            return True  # Indica que la eliminación fue exitosa
        except Exception as e:
            QMessageBox.critical(None, "Error al Eliminar Datos de Fase 2a", f"Error: {str(e)}")
            return False  # Indica que hubo un error
        finally:
            self.cursor.close()  # Cierra el cursor
            self.con.close()  # Cierra la conexión
        
    def actualizar_datos_5(self, id_fase2b, id_paciente_5, fecha_registro_5, vih, hepa_b, hepa_c, vdrl,
                                toxo_igg, toxo_igm, rubeo_igg, rubeo_igm, cmv_igg, cmv_igm, herpes_igg,
                                herpes_igm, veb_igg, veb_igm, cuantiferon, obs_cuantiferon,
                                tgo, tgp, bt, bd, bi, dhl, fa, albumina, acido_urico,
                                perfil_hdl, perfil_ldl, perfil_ct, perfil_tg, perfil_vldl,
                                sodio, potasio, fosforo, calcio, magnesio,
                                pth, tsh, t4_libre, c3, c4, bnp,
                                tp, tpt, inr,
                                nivel_ecg, obs_ecg,
                                anti_dna, ana,
                                b2_glicoprot, anticoag_lupico,
                                anticardio_igg_igm,
                                p_anca,c_anca,
                                urocultivo, obs_urocultivo,
                                orocultivo ,obs_orocultivo ,
                                ex_nasal ,obs_nasal):
        try:
            self.conecta_base_datos()  # Se asegura de que la conexión está abierta
            query = """UPDATE fase_2b SET 
                        id_paciente_5 = %s,
                        fecha_registro_5 = %s,
                        vih = %s,
                        hepa_b = %s,
                        hepa_c = %s,
                        vdrl = %s,
                        toxo_igg = %s,
                        toxo_igm = %s,
                        rubeo_igg = %s,
                        rubeo_igm = %s,
                        cmv_igg = %s,
                        cmv_igm = %s,
                        herpes_igg = %s,
                        herpes_igm = %s,
                        veb_igg = %s,
                        veb_igm = %s,
                        cuantiferon = %s,
                        obs_cuantiferon = %s,
                        tgo = %s,
                        tgp = %s,
                        bt = %s,
                        bd = %s,
                        bi = %s,
                        dhl = %s,
                        fa = %s,
                        albumina = %s,
                        acido_urico = %s,
                        perfil_hdl= %s,
                        perfil_ldl= %s,
                        perfil_ct= %s,
                        perfil_tg= %s,
                        perfil_vldl= %s,
                        sodio= %s,
                        potasio= %s,
                        fosforo= %s,
                        calcio= %s,
                        magnesio= %s,
                        pth= %s,
                        tsh= %s,
                        t4_libre= %s,
                        c3= %s,
                        c4= %s,
                        bnp= %s,
                        tp= %s,
                        tpt= %s,inr= %s,nivel_ecg= %s ,obs_ecg= %s ,anti_dna= %s ,ana= %s ,
                        b2_glicoprot= %s ,anticoag_lupico= %s ,
                        anticardio_igg_igm= %s ,
                        p_anca=%s,c_anca=%s ,
                        urocultivo=%s ,obs_urocultivo=%s ,
                        orocultivo=%s ,obs_orocultivo=%s ,
                        ex_nasal=%s ,obs_nasal=%s 
                    WHERE id_fase2b =%s"""
            
            # Ejecuta la consulta con los valores proporcionados
            self.cursor.execute(query,(id_paciente_5 ,fecha_registro_5 ,
                                        vih ,hepa_b ,hepa_c ,vdrl ,
                                        toxo_igg,toxo_igm,rubeo_igg,rubeo_igm ,
                                        cmv_igg, cmv_igm, herpes_igg, herpes_igm, 
                                        veb_igg, veb_igm, cuantiferon, 
                                        obs_cuantiferon, 
                                        tgo, tgp, bt, bd, bi, 
                                        dhl, fa, albumina, acido_urico,
                                        perfil_hdl, perfil_ldl, perfil_ct, 
                                        perfil_tg, perfil_vldl, 
                                        sodio, potasio, fosforo, 
                                        calcio, magnesio, 
                                        pth, tsh, t4_libre, 
                                        c3, c4, bnp, 
                                        tp, tpt, inr, 
                                        nivel_ecg, obs_ecg, 
                                        anti_dna, ana, 
                                        b2_glicoprot, anticoag_lupico, 
                                        anticardio_igg_igm,
                                        p_anca, c_anca, 
                                        urocultivo, obs_urocultivo,
                                        orocultivo, obs_orocultivo, 
                                        ex_nasal ,obs_nasal,id_fase2b))
            self.con.commit()  # Confirma los cambios en la base de datos
            return True  # Indica que la actualización fue exitosa
        except Exception as e:
            QMessageBox.critical(None,"Error al Actualizar Datos de Fase 2b",f"Error: {str(e)}")
            return False  # Indica que hubo un error
        finally:
            self.cursor.close()  # Cierra el cursor
            self.con.close()  # Cierra la conexión 
    
################## FASE 3 - Consultas en SQL para funciones básicas como agregar, buscar, eliminar y actualizar datos
    def agregar_datos_6(self, id_fase3, id_paciente_6, fecha_registro_6,
                        est_antig_prost, obs_antig_prost,
                        est_hgc_sbeta, obs_hgc_sbeta,
                        est_pap, obs_pap,
                        est_mamo, obs_mamo,
                        est_guay_hec, obs_guay_hec,
                        est_endo_colon, obs_endo_colon,
                        est_rxt, obs_rxt,
                        est_rx_spn, obs_rx_spn,
                        est_cisto, obs_cisto,
                        est_usg_vesi, obs_usg_vesi,
                        est_eco_trans, obs_eco_trans,
                        est_eco_trans_dm, obs_eco_trans_dm,
                        est_dop_iliac, obs_dop_iliac,
                        est_dop_art, obs_dop_art,
                        est_2donantes, obs_2donantes,
                        est_pielograma, obs_pielograma):
        try:
            self.conecta_base_datos()  # Se asegura de que la conexión está abierta
            query = """INSERT INTO fase_3 (id_fase3, id_paciente_6, fecha_registro_6,
                                            est_antig_prost, obs_antig_prost,
                                            est_hgc_sbeta, obs_hgc_sbeta,
                                            est_pap, obs_pap,
                                            est_mamo, obs_mamo,
                                            est_guay_hec, obs_guay_hec,
                                            est_endo_colon, obs_endo_colon,
                                            est_rxt, obs_rxt,
                                            est_rx_spn, obs_rx_spn,
                                            est_cisto, obs_cisto,
                                            est_usg_vesi, obs_usg_vesi,
                                            est_eco_trans, obs_eco_trans,
                                            est_eco_trans_dm, obs_eco_trans_dm,
                                            est_dop_iliac, obs_dop_iliac,
                                            est_dop_art, obs_dop_art,
                                            est_2donantes, obs_2donantes,
                                            est_pielograma, obs_pielograma)
                    VALUES (%s,
                            %s, %s,
                            %s, %s,
                            %s, %s,
                            %s, %s,
                            %s, %s,
                            %s, %s,
                            %s, %s,
                            %s, %s,
                            %s, %s,
                            %s, %s,
                            %s, %s,
                            %s, %s,
                            %s, %s,
                            %s, %s,
                            %s, %s,
                            %s, %s,
                            %s, %s)"""
            
            # Ejecuta la consulta con los valores proporcionados
            self.cursor.execute(query, (id_fase3, id_paciente_6, fecha_registro_6,
                                        est_antig_prost, obs_antig_prost,
                                        est_hgc_sbeta, obs_hgc_sbeta,
                                        est_pap, obs_pap,
                                        est_mamo, obs_mamo,
                                        est_guay_hec, obs_guay_hec,
                                        est_endo_colon, obs_endo_colon,
                                        est_rxt, obs_rxt,
                                        est_rx_spn, obs_rx_spn,
                                        est_cisto, obs_cisto,
                                        est_usg_vesi, obs_usg_vesi,
                                        est_eco_trans, obs_eco_trans,
                                        est_eco_trans_dm, obs_eco_trans_dm,
                                        est_dop_iliac, obs_dop_iliac,
                                        est_dop_art, obs_dop_art,
                                        est_2donantes, obs_2donantes,
                                        est_pielograma, obs_pielograma))
            
            self.con.commit()  # Confirma los cambios en la base de datos
            return True  # Indica que la inserción fue exitosa
        except Exception as e:
            QMessageBox.critical(None,"Error al Agregar Fase 3",f"Error: {str(e)}")
            return False  # Indica que hubo un error
        finally:
            self.cursor.close()  # Cierra el cursor
            self.con.close()  # Cierra la conexión


    def buscar_f3_receptor(self):
        try:
            self.conecta_base_datos()  # Se asegura de que la conexión está abierta

            query = """
            SELECT * FROM fase_3
            WHERE id_paciente_6 IN (SELECT id_receptor FROM receptor)
            """
            self.cursor.execute(query)
            results = self.cursor.fetchall()
            return results  # Retorna los resultados de la consulta

        except Exception as e:
            QMessageBox.critical(None, "Error al Buscar Fase 3", f"Error: {str(e)}")
            return []  # Retorna una lista vacía si hay un error

        finally:
            self.cursor.close()  # Cierra el cursor
            self.con.close()  # Cierra la conexión

    def obtener_datos_fase3(self, id_fase3):
            try:
                self.conecta_base_datos()
                query = "SELECT * FROM fase_3 WHERE id_fase3 = %s"
                self.cursor.execute(query, (id_fase3,))
                result = self.cursor.fetchone()
                return result
            except Exception as e:
                QMessageBox.critical(None, "Error al Obtener Datos de Fase 3", f"Error: {str(e)}")
                return None
            finally:
                self.cursor.close()
                self.con.close()


    def limpiar_datos_6(self):
        try:
            self.conecta_base_datos()  
            query = "DELETE FROM fase_3"  # Elimina todos los datos del registro seleccionado
            self.cursor.execute(query)
            self.con.commit()  
            QMessageBox.information(None, "Éxito", "Todos los registros de Fase 3 han sido eliminados correctamente.")
        except Exception as e:
            QMessageBox.critical(None, "Error al Limpiar Datos de Fase 3", f"Error: {str(e)}")
        finally:
            self.cursor.close()  
            self.con.close()  

    def eliminar_datos_6(self, id_fase3):
        try:
            self.conecta_base_datos()  
            query = "DELETE FROM fase_3 WHERE id_fase3 = %s"
            self.cursor.execute(query, (id_fase3,))
            self.con.commit()  
            return True  
        except Exception as e:
            QMessageBox.critical(None, "Error al Eliminar Datos de Fase 3", f"Error: {str(e)}")
            return False  
        finally:
            self.cursor.close()  
            self.con.close()  

    def actualizar_datos_6(self, id_fase3, id_paciente_6, fecha_registro_6, est_antig_prost, obs_antig_prost,
                        est_hgc_sbeta, obs_hgc_sbeta, est_pap, obs_pap, est_mamo, obs_mamo,
                        est_guay_hec, obs_guay_hec, est_endo_colon, obs_endo_colon,
                        est_rxt, obs_rxt, est_rx_spn, obs_rx_spn,
                        est_cisto, obs_cisto, est_usg_vesi, obs_usg_vesi,
                        est_eco_trans, obs_eco_trans, est_eco_trans_dm, obs_eco_trans_dm,
                        est_dop_iliac, obs_dop_iliac, est_dop_art, obs_dop_art,
                        est_2donantes, obs_2donantes, est_pielograma, obs_pielograma):
        try:
            self.conecta_base_datos()  #Se conecta a la base de datos
            query = """UPDATE fase_3 SET 
                        id_paciente_6 = %s,
                        fecha_registro_6 = %s,
                        est_antig_prost = %s,
                        obs_antig_prost = %s,
                        est_hgc_sbeta = %s,
                        obs_hgc_sbeta = %s,
                        est_pap = %s,
                        obs_pap = %s,
                        est_mamo = %s,
                        obs_mamo = %s,
                        est_guay_hec = %s,
                        obs_guay_hec = %s,
                        est_endo_colon = %s,
                        obs_endo_colon = %s,
                        est_rxt = %s,
                        obs_rxt = %s,
                        est_rx_spn = %s,
                        obs_rx_spn = %s,
                        est_cisto = %s,
                        obs_cisto = %s,
                        est_usg_vesi = %s,
                        obs_usg_vesi = %s,
                        est_eco_trans = %s,
                        obs_eco_trans = %s,
                        est_eco_trans_dm = %s,
                        obs_eco_trans_dm = %s,
                        est_dop_iliac = %s,
                        obs_dop_iliac = %s,
                        est_dop_art = %s,
                        obs_dop_art = %s,
                        est_2donantes = %s,
                        obs_2donantes = %s,
                        est_pielograma = %s,
                        obs_pielograma = %s
                    WHERE id_fase3 =%s"""
            
            #Ejecuta la consulta con los valores correspondientes
            self.cursor.execute(query,(id_paciente_6 ,fecha_registro_6 ,
                                    est_antig_prost ,obs_antig_prost ,
                                    est_hgc_sbeta ,obs_hgc_sbeta ,
                                    est_pap ,obs_pap ,
                                    est_mamo ,obs_mamo ,
                                    est_guay_hec ,obs_guay_hec ,
                                    est_endo_colon ,obs_endo_colon ,
                                    est_rxt ,obs_rxt ,
                                    est_rx_spn ,obs_rx_spn ,
                                    est_cisto ,obs_cisto ,
                                    est_usg_vesi ,obs_usg_vesi ,
                                    est_eco_trans ,obs_eco_trans ,
                                    est_eco_trans_dm ,obs_eco_trans_dm ,
                                    est_dop_iliac ,obs_dop_iliac ,
                                    est_dop_art ,obs_dop_art ,
                                    est_2donantes ,obs_2donantes ,
                                    est_pielograma ,obs_pielograma,id_fase3))
            self.con.commit()  
            return True  # Indica que se actualizó correctamente
        except Exception as e:
            QMessageBox.critical(None,"Error al Actualizar Datos de Fase 3",f"Error: {str(e)}")
            return False  # Indica que un error ocurrió
        finally:
            self.cursor.close()
            self.con.close() 



################## FASE 4 - Consultas en SQL para funciones básicas como agregar, buscar, eliminar y actualizar datos

    def agregar_datos_7(self, id_fase4, id_paciente_7, fecha_registro_7, eval_urologia, eval_cardiologia,
                        angiotac_miem_inf, angiotac_ven_art, a1, a2, b1, b2, dr1, dr2, dq1, dq2,est_protocolo):
        try:
            self.conecta_base_datos()  # Se asegura de que la conexión está abierta

            query = """INSERT INTO fase_4 (id_fase4, id_paciente_7, fecha_registro_7,
                                        eval_urologia, eval_cardiologia,
                                        angiotac_miem_inf, angiotac_ven_art,
                                        a1, a2, b1, b2, dr1, dr2, dq1, dq2,est_protocolo)
                    VALUES (%s, %s, %s,
                            %s, %s,
                            %s, %s,
                            %s, %s, %s, %s,
                            %s, %s, %s, %s, %s)"""

            # Ejecuta la consulta con los valores proporcionados
            self.cursor.execute(query, (id_fase4, id_paciente_7, fecha_registro_7,
                                        eval_urologia, eval_cardiologia,
                                        angiotac_miem_inf, angiotac_ven_art,
                                        a1, a2, b1, b2,
                                        dr1, dr2, dq1, dq2,est_protocolo))

            self.con.commit()  # Confirma los cambios en la base de datos
            return True  # Indica que la inserción fue exitosa

        except Exception as e:
            QMessageBox.critical(None,"Error al Agregar Datos de Fase 4",f"Error: {str(e)}")
            return False  # Indica que hubo un error

        finally:
            self.cursor.close()  # Cierra el cursor
            self.con.close()  # Cierra la conexión

    def buscar_f4_receptor(self):
        try:
            self.conecta_base_datos()  # Se asegura de que la conexión está abierta

            query = """
            SELECT * FROM fase_4
            WHERE id_paciente_7 IN (SELECT id_receptor FROM receptor)
            """
            self.cursor.execute(query)
            results = self.cursor.fetchall()
            return results  # Retorna los resultados de la consulta

        except Exception as e:
            QMessageBox.critical(None, "Error al Buscar Fase 4", f"Error: {str(e)}")
            return []  # Retorna una lista vacía si hay un error

        finally:
            self.cursor.close()  # Cierra el cursor
            self.con.close()  # Cierra la conexión

    def obtener_datos_fase4(self, id_fase4):
                    try:
                        self.conecta_base_datos()
                        query = "SELECT * FROM fase_4 WHERE id_fase4 = %s"
                        self.cursor.execute(query, (id_fase4,))
                        result = self.cursor.fetchone()
                        return result
                    except Exception as e:
                        QMessageBox.critical(None, "Error al Obtener Datos de Fase 4", f"Error: {str(e)}")
                        return None
                    finally:
                        self.cursor.close()
                        self.con.close()
        
    def limpiar_datos_7(self):
        try:
            self.conecta_base_datos()  # Se asegura de que la conexión está abierta

            query = "DELETE FROM fase_4"  # Eliminar todos los registros de la tabla fase_4
            self.cursor.execute(query)

            self.con.commit()  # Confirma los cambios
            QMessageBox.information(None, "Éxito", "Todos los registros de Fase 4 han sido eliminados correctamente.")

        except Exception as e:
            QMessageBox.critical(None, "Error al Limpiar Datos de Fase 4", f"Error: {str(e)}")

        finally:
            self.cursor.close()  # Cierra el cursor
            self.con.close()  # Cierra la conexión

    def eliminar_datos_7(self, id_fase4):
        try:
            self.conecta_base_datos()  # Se asegura de que la conexión está abierta

            query = "DELETE FROM fase_4 WHERE id_fase4 = %s"  # Consulta para eliminar un registro específico
            self.cursor.execute(query, (id_fase4,))

            self.con.commit()  # Confirma los cambios en la base de datos
            return True  # Indica que la eliminación fue exitosa

        except Exception as e:
            QMessageBox.critical(None, "Error al Eliminar Datos de Fase 4", f"Error: {str(e)}")
            return False  # Indica que hubo un error

        finally:
            self.cursor.close()  # Cierra el cursor
            self.con.close()  # Cierra la conexión

    def actualizar_datos_7(self, id_fase4, id_paciente_7, fecha_registro_7, eval_urologia, eval_cardiologia,
                        angiotac_miem_inf, angiotac_ven_art, a1, a2, b1, b2, dr1, dr2, dq1, dq2,est_protocolo):
        try:
            self.conecta_base_datos()  # Se asegura de que la conexión está abierta

            query = """UPDATE fase_4 SET
                    id_paciente_7 = %s,
                    fecha_registro_7 = %s,
                    eval_urologia = %s,
                    eval_cardiologia = %s,
                    angiotac_miem_inf = %s,
                    angiotac_ven_art = %s,
                    a1 = %s,
                    a2 = %s,
                    b1 = %s,
                    b2 = %s,
                    dr1 = %s,
                    dr2 = %s,
                    dq1 = %s,
                    dq2 = %s,
                    est_protocolo = %s
                    WHERE id_fase4 = %s"""

            # Ejecuta la consulta con los valores proporcionados
            self.cursor.execute(query, (id_paciente_7, fecha_registro_7, eval_urologia, eval_cardiologia,
                                        angiotac_miem_inf, angiotac_ven_art, a1, a2, b1, b2, dr1, dr2, dq1, dq2, est_protocolo, id_fase4))

            self.con.commit()  # Confirma los cambios en la base de datos
            return True  # Indica que la actualización fue exitosa

        except Exception as e:
            QMessageBox.critical(None, "Error al Actualizar Datos de Fase 4", f"Error: {str(e)}")
            return False  # Indica que hubo un error

        finally:
            self.cursor.close()  # Cierra el cursor
            self.con.close()  # Cierra la conexión

    def agregar_datos_7(self, id_fase4, id_paciente_7, fecha_registro_7, eval_urologia, eval_cardiologia,
                            angiotac_miem_inf, angiotac_ven_art, a1, a2, b1, b2, dr1, dr2, dq1, dq2,est_protocolo):
            try:
                self.conecta_base_datos()  # Se asegura de que la conexión está abierta

                query = """INSERT INTO fase_4 (id_fase4, id_paciente_7, fecha_registro_7,
                                            eval_urologia, eval_cardiologia,
                                            angiotac_miem_inf, angiotac_ven_art,
                                            a1, a2, b1, b2, dr1, dr2, dq1, dq2,est_protocolo)
                        VALUES (%s, %s, %s,
                                %s, %s,
                                %s, %s,
                                %s, %s, %s, %s,
                                %s, %s, %s, %s,%s)"""

                # Ejecuta la consulta con los valores proporcionados
                self.cursor.execute(query, (id_fase4, id_paciente_7, fecha_registro_7,
                                            eval_urologia, eval_cardiologia,
                                            angiotac_miem_inf, angiotac_ven_art,
                                            a1, a2, b1, b2,
                                            dr1, dr2, dq1, dq2,est_protocolo))

                self.con.commit()  # Confirma los cambios en la base de datos
                return True  # Indica que la inserción fue exitosa

            except Exception as e:
                QMessageBox.critical(None,"Error al Agregar Datos de Fase 4",f"Error: {str(e)}")
                return False  # Indica que hubo un error

            finally:
                self.cursor.close()  # Cierra el cursor
                self.con.close()  # Cierra la conexión



#################################  Tabla de histocompatibilidad  - Consultas en SQL para funciones básicas como agregar, buscar, eliminar y actualizar datos
    def agregar_datos_9(self, id_fase_final, id_receptor_3, id_donante_2, fecha_registro_9, parentesco, tipo_donante, hla1, hla2, pra_hla1, prueba_cruzada):
        try:
            self.conecta_base_datos()  # Se asegura de que la conexión está abierta

            # Consulta SQL para insertar datos
            query = """
                INSERT INTO fase_final (
                    id_fase_final,
                    id_receptor,
                    id_donante,
                    fecha_registro,
                    parentesco,
                    tipo_donante,
                    hla_1,
                    hla_2,
                    pra_hla1_2,
                    prueba_cruzada
                ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
            """
            
            # Ejecuta la consulta con los valores proporcionados
            self.cursor.execute(query, (id_fase_final, id_receptor_3, id_donante_2, fecha_registro_9, parentesco, tipo_donante, hla1, hla2, pra_hla1, prueba_cruzada))
            
            # Ejecuta la consulta y Confirma los cambios
            self.con.commit()  # Confirma los cambios en la base de datos
            return True  # Indica que la inserción fue exitosa
        
        except Exception as e:
            QMessageBox.critical(None,"Error al Agregar Datos de Fase final",f"Error: {str(e)}")
            return False  # Indica que hubo un error

        finally:
            self.cursor.close()  # Cierra el cursor
            self.con.close()  # Cierra la conexión


    def buscar_datos_9(self):
            try:
                self.conecta_base_datos()  # Se asegura de que la conexión está abierta

                query = "SELECT * FROM fase_final"  # Consulta para obtener todos los registros de la tabla fase_4
                self.cursor.execute(query)

                results = self.cursor.fetchall()  # Obtener todos los resultados de la consulta
                return results  # Retorna los resultados de la consulta

            except Exception as e:
                QMessageBox.critical(None, "Error al Buscar Datos de Fase Final", f"Error: {str(e)}")
                return []  # Retorna una lista vacía si hay un error

            finally:
                self.cursor.close()  # Cierra el cursor

    def eliminar_datos_9(self, id_fase_final):
            try:
                self.conecta_base_datos()  # Se asegura de que la conexión está abierta

                query = "DELETE FROM fase_final WHERE id_fase_final = %s"  # Consulta para eliminar un registro específico
                self.cursor.execute(query, (id_fase_final,))

                self.con.commit()  # Confirma los cambios en la base de datos
                return True  # Indica que la eliminación fue exitosa

            except Exception as e:
                QMessageBox.critical(None, "Error al Eliminar Datos de Fase Final", f"Error: {str(e)}")
                return False  # Indica que hubo un error

            finally:
                self.cursor.close()  # Cierra el cursor
                self.con.close()  # Cierra la conexión


    def actualizar_datos_9(self, id_fase_final, fecha_registro_9, parentesco, tipo_donante, prueba_cruzada):
        try:
            self.conecta_base_datos()  # Se asegura de que la conexión está abierta

            query = """UPDATE fase_final SET
                    fecha_registro = %s,
                    parentesco = %s,
                    tipo_donante = %s,
                    prueba_cruzada = %s
                    WHERE id_fase_final = %s"""

            # Ejecuta la consulta con los valores proporcionados
            self.cursor.execute(query, (fecha_registro_9, parentesco, tipo_donante, prueba_cruzada, id_fase_final))

            self.con.commit()  # Confirma los cambios en la base de datos
            return True  # Indica que la actualización fue exitosa

        except Exception as e:
            QMessageBox.critical(None, "Error al Actualizar Datos", f"Error: {str(e)}")
            return False  # Indica que hubo un error

        finally:
            if self.cursor:
                self.cursor.close()  # Cierra el cursor
            if self.con:
                self.con.close()  # Cierra la conexión

###############3Función de exportar docx

    def obtener_datos_fase_final_por_receptor(self, id_receptor):
        try:
            self.conecta_base_datos()
            query = "SELECT * FROM fase_final WHERE id_receptor = %s"
            self.cursor.execute(query, (id_receptor,))
            result = self.cursor.fetchone()
            return result
        except Exception as e:
            print(f"Error al obtener datos de fase final: {str(e)}")
            return None
        finally:
            if self.cursor:
                self.cursor.close()
            if self.con:
                self.con.close()

    def obtener_datos_receptor_por_id(self, id_receptor):
        try:
            self.conecta_base_datos()
            query = "SELECT * FROM receptor WHERE id_receptor = %s"
            self.cursor.execute(query, (id_receptor,))
            result = self.cursor.fetchone()
            return result
        except Exception as e:
            print(f"Error al obtener datos del receptor: {str(e)}")
            return None
        finally:
            if self.cursor:
                self.cursor.close()
            if self.con:
                self.con.close()


    def existe_paciente_en_receptor_o_donante(self, id_paciente):   
        try:
            # Conecta a la base de datos
            print(f"Conectando a la base de datos para verificar el paciente con ID: {id_paciente}")
            self.conecta_base_datos()

            # Consultas para verifica si el paciente existe en receptor o donante
            query_receptor = "SELECT COUNT(*) FROM receptor WHERE id_receptor = %s"
            query_donante  = "SELECT COUNT(*) FROM donante WHERE id_donante = %s"

            # Verifica si existe en la tabla receptor
            print(f"Ejecutando consulta en la tabla receptor: {query_receptor}")
            self.cursor.execute(query_receptor, (id_paciente,))
            resultado_receptor = self.cursor.fetchone()

            # Muestra el resultado obtenido de la tabla receptor
            print(f"Resultado de la consulta en receptor: {resultado_receptor}")

            # Si no hay resultados o el conteo es 0, buscar en donante
            if resultado_receptor is None or resultado_receptor['COUNT(*)'] == 0:
                print(f"No se encontró al paciente en receptor, buscando en donante: {query_donante}")
                self.cursor.execute(query_donante, (id_paciente,))
                resultado_donante = self.cursor.fetchone()

                # Muestra el resultado obtenido de la tabla donante
                print(f"Resultado de la consulta en donante: {resultado_donante}")

                if resultado_donante is None or resultado_donante['COUNT(*)'] == 0:
                    print("El paciente no existe ni en receptor ni en donante.")
                    return False  # No existe ni en receptor ni en donante
                else:
                    print("El paciente existe en la tabla donante.")
                    return True  # Existe en donante
            else:
                print("El paciente existe en la tabla receptor.")
                return True  # Existe en receptor

        except mysql.connector.Error as e:
            print(f"Error al verificar la existencia del paciente: {str(e)}")
            return False

        finally:
            # Cierra el cursor y la conexión a la base de datos
            if self.cursor:
                self.cursor.close()
            if self.con:
                self.con.close()