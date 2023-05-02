import services.serviceDatabase as serviceDatabase
import settings.settingBot as settingBot

def databaseInit():
    if settingBot.databaseType == "MariaDB":
        tableName = "addon_reactionrole_reactions"
        columns = [
            ["serverID", "BIGINT NOT NULL"],
            ["channelID", "BIGINT NOT NULL"],
            ["messageID", "BIGINT NOT NULL"],
            ["roleID", "BIGINT NOT NULL"],
            ["emote", "VARCHAR(255) NOT NULL"],
            ["reactionType", "INT NOT NULL"]
        ]
        serviceDatabase.databaseCreation(tableName, columns)


    elif settingBot.databaseType == "SQLite":
        tableName = "addon_reactionrole_reactions"
        columns = [
            ["serverID", "integer NOT NULL"],
            ["channelID", "integer NOT NULL"],
            ["messageID", "integer NOT NULL"],
            ["roleID", "integer NOT NULL"],
            ["emote", "text NOT NULL"],
            ["reactionType", "integer NOT NULL"]
        ]
        serviceDatabase.databaseCreation(tableName, columns)