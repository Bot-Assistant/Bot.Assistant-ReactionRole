import addons.ReactionRole.handlers.handlerReactionRole as handlerReactionRole
import addons.ReactionRole.settings.settingReactionRole as settingReactionRole
import addons.ReactionRole.settings.settingColors as settingColors
import addons.ReactionRole.settings.settingThumbnail as settingThumbnail

import services.serviceBot as serviceBot
discord = serviceBot.classBot.getDiscord()
bot = serviceBot.classBot.getBot()


async def create(ctx, channel, messageID, role, emote, reactionType):

    # PERMISSIONS CHECK
    import addons.ReactionRole.functions.services.servicePermission as servicePermission
    if await servicePermission.permissionCheck(ctx, "cmdReactionRoleCreate") == False:
        return
    

    # COMMAND        
    embed = discord.Embed(title="Reaction Role", description="New reaction role added \n This may take some time.", color=settingColors.green)
    embed.set_thumbnail(url=settingThumbnail.doubleUpIcons)
    embedSend = await ctx.respond(embed=embed)


    # Channel verification
    channel = bot.get_channel(int(channel.id))

    if channel == None:
        embed = discord.Embed(title="Reaction Role", description="Channel not found.", color=settingColors.red)
        embed.set_thumbnail(url=settingThumbnail.doubleUpIcons)
        await embedSend.edit_original_response(embed=embed)
        return


    # Message verification
    try:
        message = await channel.fetch_message(int(messageID))

    except Exception as error:

        embed = discord.Embed(title="Reaction Role", description="Message not found.", color=settingColors.red)
        embed.set_thumbnail(url=settingThumbnail.doubleUpIcons)
        await embedSend.edit_original_response(embed=embed)
        
        return
        

    #Message Commande
    embed = serviceBot.classBot.getDiscord().Embed(title="Reaction Role", description="New reaction role added ", color=settingColors.green)
    embed.set_thumbnail(url=settingThumbnail.doubleUpIcons)

    embed.add_field(name="Guild ID", value=str(ctx.guild.id) + " -> " + ctx.guild.name, inline=False)
    embed.add_field(name="Channel ID", value=str(channel.id) + " -> " + channel.name, inline=False)
    embed.add_field(name="Message ID", value=str(messageID), inline=False)
    embed.add_field(name="Role ID", value=str(role.id) + " -> " +  role.name, inline=False)
    embed.add_field(name="Emote", value=str(emote), inline=False)
    embed.add_field(name="Type of reaction", value=str(reactionType), inline=False)

    await embedSend.edit_original_response(embed=embed)

    match reactionType:
        case settingReactionRole.addRemoveRole:
            reactionType = 2
        case settingReactionRole.addRole:
            reactionType = 1
        case settingReactionRole.removeRole: 
            reactionType = 0
    
    # Add reaction
    try:
        await message.add_reaction(emote)
    except:
        
        #Message Commande
        embed = discord.Embed(title="Reaction Role", description="Emote not found on this server.", color=settingColors.red)
        embed.set_thumbnail(url=settingThumbnail.doubleUpIcons)
        await embedSend.edit_original_response(embed=embed)
        
        return
    
    #Ajout BDD
    handlerReactionRole.createReactionRole(ctx.guild.id, channel.id, messageID, role.id, emote, reactionType)