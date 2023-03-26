import addons.ReactionRole.handlers.handlerReactionRole as handlerReactionRole
import addons.ReactionRole.settings.settingColors as settingColors
import addons.ReactionRole.settings.settingThumbnail as settingThumbnail

import services.serviceBot as serviceBot
discord = serviceBot.classBot.getDiscord()

async def delete(ctx, ID):
    
    # PERMISSIONS CHECK
    import addons.ReactionRole.functions.services.servicePermission as servicePermission
    if await servicePermission.permissionCheck(ctx, "cmdReactionRoleDelete") == False:
        return
    

    # COMMAND  
    if handlerReactionRole.checkReactionRoleID(ctx.guild.id, ID) == False:
        embed = discord.Embed(title="Reaction Role", description="The reaction role ID does not exist.", color=settingColors.red)
        embed.set_thumbnail(url=settingThumbnail.doubleUpIcons)
        await ctx.respond(embed=embed)
        return
    
    handlerReactionRole.deleteReactionRole(ctx.guild.id, ID)

    
    #Message Commande
    embed = discord.Embed(title="Reaction Role", description="Reaction role deleted: " + str(ID), color=settingColors.green)
    embed.set_thumbnail(url=settingThumbnail.doubleUpIcons)
    await ctx.respond(embed=embed)