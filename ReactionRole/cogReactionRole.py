# ADDON IMPORTS
import addons.ReactionRole.init as init

import addons.ReactionRole.functions.commands.commandRequirements as commandRequirements
import addons.ReactionRole.functions.commands.commandCreate as commandCreate
import addons.ReactionRole.functions.commands.commandDelete as commandDelete
import addons.ReactionRole.functions.commands.commandList as commandList
import addons.ReactionRole.functions.events.eventOnRawReactionAdd as eventOnRawReactionAdd
import addons.ReactionRole.functions.events.eventOnRawReactionRemove as eventOnRawReactionRemove

import addons.ReactionRole.handlers.handlerDatabaseInit as handlerDatabaseInit

import addons.ReactionRole.settings.settingReactionRole as settingReactionRole

# BOTASSISTANT IMPORTS
from services.serviceLogger import Logger
from services.serviceDiscordLogger import discordLogger as DiscordLogger
from settings.settingBot import debug

# INIT BOT VARIABLES
import services.serviceBot as serviceBot
discord = serviceBot.classBot.getDiscord()
discordCommands = serviceBot.classBot.getDiscordCommands()
commands = serviceBot.classBot.getCommands()
bot = serviceBot.classBot.getBot()



class ReactionRole(commands.Cog):
    
    def __init__(self, bot):
        self.bot = bot
        
    
    # EVENTS LISTENERS
    @commands.Cog.listener()
    async def on_raw_reaction_add(self, payload):
        await eventOnRawReactionAdd.OnRawReactionAdd(payload)
        
    @commands.Cog.listener()
    async def on_raw_reaction_remove(self, payload):
        await eventOnRawReactionRemove.OnRawReactionRemove(payload)
    
    # INIT GROUP COMMAND
    groupReactionRole = discordCommands.SlashCommandGroup(init.cogName, "🔶 Group of commands to manage the ReactionRole addon.")
    
    # Verify if the bot has the prerequisites permissions
    @groupReactionRole.command(name="requirements", description="Check the prerequisites permissions of the addon.")
    async def cmdPermissions(self, ctx: commands.Context):
        await DiscordLogger.info(ctx, init.cogName, ctx.author.name + " has used the requirements command.", str(ctx.command))
        await commandRequirements.checkRequirements(ctx)

    #t CREATE
    @groupReactionRole.command(name="create", description="Command to create a reaction role.")
    async def cmdCreate(
        self,
        ctx,
        
        channel: discord.Option(discord.TextChannel, required=True),
        message_id: discord.Option(str, required=True),
        role: discord.Option(discord.Role, required=True),
        emote: discord.Option(str, required=True),
        reactiontype: discord.Option(str, choices=settingReactionRole.reactionsTypes, required=True)
    ):
        await DiscordLogger.info(ctx, init.cogName, ctx.author.name + " has used the create command.", str(ctx.command))
        await commandCreate.create(ctx, channel, message_id, role, emote, reactiontype)
        
        
    #t DELETE
    @groupReactionRole.command(name="delete", description="Command to delete a reaction role.")
    async def cmdDelete(
        self,
        ctx,
        id: discord.Option(int, required=True)
    ):
        await DiscordLogger.info(ctx, init.cogName, ctx.author.name + " has used the delete command.", str(ctx.command))
        await commandDelete.delete(ctx, id)
        
        
    #t LIST
    @groupReactionRole.command(name="list", description="Command to list the reaction roles.")
    async def cmdList(
        self,
        ctx
    ):
        await DiscordLogger.info(ctx, init.cogName, ctx.author.name + " has used the list command.", str(ctx.command))
        await commandList.list(ctx)
    


def setup(bot):
    Logger.debug("Loading cog: " + init.cogName)
    handlerDatabaseInit.databaseInit()
    bot.add_cog(ReactionRole(bot))