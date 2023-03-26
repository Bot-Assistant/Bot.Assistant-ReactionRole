# Github informations
enableGithub = True
author = "Ted-18"
repository = "Bot.Assistant-ReactionRole"
version = "1.1.0"

# To activate this addon
cogEnabled = True

# Name of the addon
cogName = "reactionrole"

# Name of the file containing the cog
cogFile = "cogReactionRole"

# List of packages required by the addon
packageDependencies = [
    "py-cord",
    "mysql-connector-python"
]

# List of addons required by the addon
addonDependencies = [
    "Configuration"
]

# List of permissions required by the addon
addonPermissions = [
    "manage_roles",
    "send_messages",
    "add_reactions",
    "read_message_history"
]

commandPermissions = {
    # Permission to check the addon's permissions
    "cmdRequirements" : "discord.permission.manage_guild",

    # Permission to create a reaction role
    "cmdReactionRoleCreate" : "reactionrole.create",

    # Permission to delete a reaction role
    "cmdReactionRoleDelete" : "reactionrole.delete",

    # Permission to list the reaction roles
    "cmdReactionRoleList" : "reactionrole.list"
}