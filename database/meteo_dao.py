from database.DB_connect import DBConnect
from model.situazione import Situazione


class MeteoDao():

    @staticmethod
    def get_situations_month(month):
        cnx = DBConnect.get_connection()
        cursor = cnx.cursor(dictionary=True)
        query = f"""SELECT Localita, Data, Umidita
                    FROM situazione
                    WHERE MONTH(Data) = {month}
                    ORDER BY Data ASC"""
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(Situazione(row["Localita"],
                                     row["Data"],
                                     row["Umidita"]))
        cursor.close()
        cnx.close()
        return result


    @staticmethod
    def get_mean_humidity(month):
        conn = DBConnect.get_connection()
        cursor = conn.cursor(dictionary=True)

        query = f"""SELECT Localita, SUM(Umidita) / COUNT(*) as Mean_humidity FROM situazione WHERE MONTH(Data) = {month} GROUP BY Localita """
        cursor.execute(query)
        result = cursor.fetchall()
        cursor.close()
        conn.close()
        if not result:
            return None
        return result