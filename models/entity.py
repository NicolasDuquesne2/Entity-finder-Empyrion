

class EntityModel():

    def __init__(self):
        self.db_query_tables = "SELECT name FROM sqlite_schema WHERE type ='table' AND name NOT LIKE 'sqlite_%' ORDER BY name"
        self.db_query_distinct_entity = "SELECT DISTINCT name from Entities ORDER BY name"
        self.entity_types = ["Structures terrestres", "Vaisseaux", "Stations spatiales", "Astéroids", "Gisements"]

    

    def get_one_db_entity_type_sql(self, criteria):
        return "SELECT DISTINCT name from Entities WHERE name like '" + criteria + '%'"' ORDER BY name"
    
    def get_list_db_entity_by_type(self, criteria):
        return "SELECT Entities.name, Playfields.name, SolarSystems.name FROM Entities  INNER JOIN Playfields ON Entities.pfid = Playfields.pfid INNER JOIN SolarSystems ON Playfields.ssid = SolarSystems.ssid WHERE Entities.name = '" + criteria + "'"