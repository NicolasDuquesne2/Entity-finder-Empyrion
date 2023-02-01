from os.path import isfile, getsize
import re


class AppTests():
    def __init__(self):
        pass

    """ Sqlite db file header is 100 bytes and has its SQLite format 3 signature in its file header"""

    def is_SQLite3(self, file_name):
                
        if not isfile(file_name):
            return False
        if getsize(file_name) < 100:
            return False
        
        
        with open(file_name, 'rb') as fd:
            header = fd.read(100)
        

        return header[:16] == b'SQLite format 3\x00' or header[:16] == 'SQLite format 3\x00'


    """ Tests the db structure for empyrion game records """

    def is_empyrion_db_file(self, tables):
        expected_tables = ["Bookmarks",
                        "ChangedPlayfields",
                        "ChatMessages",
                        "DialogueVars",
                        "DialogueVisitedStates",
                        "DiscoveredFactions",
                        "DiscoveredPOIs",
                        "DiscoveredPlayfields",
                        "Entities",
                        "LoginLogoff",
                        "Marketplace",
                        "PerformanceDBResults",
                        "PerformanceData",
                        "PerformanceNWPackages",
                        "PlayerData",
                        "PlayerDeaths",
                        "PlayerInventory",
                        "PlayerInventoryItems",
                        "PlayerLevelUp",
                        "PlayerPosHistory",
                        "PlayerSkillValues",
                        "PlayerStatistics",
                        "PlayerStatisticsAIVessels",
                        "PlayerStatisticsCores",
                        "PlayerStatisticsOres",
                        "PlayerStatisticsPDAChapters",
                        "PlayfieldResources",
                        "Playfields",
                        "ServerStartStop",
                        "SolarSystems",
                        "StationServicesHistory",
                        "Structures",
                        "StructuresDeviceCount",
                        "StructuresHistory",
                        "TerrainPlaceables",
                        "TraderHistory",
                        "VisitedStructures"]

        for index, table in enumerate(expected_tables):
            if tables[index][0] != table:
                return False

        return True

    """ function witch add \ to special carcters in the text
        cheks if special caracters don't have alrady \ before them """
    def handle_quotes(self, text:str):
        reg = re.compile(r'[\']')
        match = re.search(reg, text)
        if match:
            text = text.replace('\'', '\'\'')
            
        return text

