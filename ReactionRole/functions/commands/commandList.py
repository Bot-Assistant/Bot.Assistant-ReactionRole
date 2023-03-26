import os
from prettytable import PrettyTable

import addons.ReactionRole.handlers.handlerReactionRole as handlerReactionRole
import addons.ReactionRole.settings.settingColors as settingColors
import addons.ReactionRole.settings.settingThumbnail as settingThumbnail
import addons.ReactionRole.settings.settingReactionRole as settingReactionRole

import services.serviceBot as serviceBot
discord = serviceBot.classBot.getDiscord()


async def list(ctx):

    # PERMISSIONS CHECK
    import addons.ReactionRole.functions.services.servicePermission as servicePermission
    if await servicePermission.permissionCheck(ctx, "cmdReactionRoleList") == False:
        return
    

    # COMMAND
    # Get the reaction role from the database
    list = handlerReactionRole.getReactionRole(ctx.guild.id)

    # If the list is empty
    if list == []:
        embed = discord.Embed(title="Reaction Role", description="No reaction role defined", color=settingColors.red)
        embed.set_thumbnail(url=settingThumbnail.doubleUpIcons)
        await ctx.respond(embed=embed)
        return
    
    # If the list is not empty
    embed = discord.Embed(title="Reaction Role", description="The loading of the reaction role can take a few seconds.", color=settingColors.blue)
    embed.set_thumbnail(url=settingThumbnail.doubleUpIcons)
    await ctx.respond(embed=embed)

    # create a table with all the reaction role with pretty table
    myTable = PrettyTable(["ID", "Channel", "Message", "Role", "Emoji", "Type", "Active"])

    # Add rows to the table with some verifications
    # Verify if the channel, message, role and emoji exists
    for reactionRole in list:

        # Verify if the channel exists
        channel = discord.utils.get(ctx.guild.channels, id=reactionRole[1])
        if channel == None:
            channelResult = settingReactionRole.channelDeleted
        else:
            channelResult = channel.name

        # Verify if the message exists
        try:
            message = await channel.fetch_message(reactionRole[2])
            messageResult = message.id
        except:
            messageResult = settingReactionRole.messageDeleted

        # Verify if the role exists
        role = discord.utils.get(ctx.guild.roles, id=reactionRole[3])
        if role == None:
            roleResult = settingReactionRole.roleDeleted
        else:
            roleResult = role.name

        # Verify the type of reaction
        if reactionRole[5] == 0:
            typeResult = settingReactionRole.removeRole
        elif reactionRole[5] == 1:
            typeResult = settingReactionRole.addRole
        elif reactionRole[5] == 2:
            typeResult = settingReactionRole.addRemoveRole

        # Verify if the reaction role is active
        if channelResult == settingReactionRole.channelDeleted:
            active = "🔴"
        elif messageResult == settingReactionRole.messageDeleted:
            active = "🔴"
        elif roleResult == settingReactionRole.roleDeleted:
            active = "🔴"
        else:
            active = "🟢"


        # Add the row
        myTable.add_row([reactionRole[0], channelResult, messageResult, roleResult, reactionRole[4], typeResult, active])

    # If content has more than 1900 characters send it as a file with UTF-8 encoding
    if len(myTable.get_string()) > 1900:
        with open("ReactionsRoles.txt", "w", encoding="utf-8") as file:
            file.write(myTable.get_string())
        await ctx.send(file=discord.File("ReactionsRoles.txt"))
        os.remove("ReactionsRoles.txt")

    # If content has less than 1900 characters send it as a message
    else:
        await ctx.send(content="`" + myTable.get_string() + "`")