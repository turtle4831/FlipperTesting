from discord_webhook import DiscordWebhook

message = "Hello"

webhook = DiscordWebhook(url="https://discord.com/api/webhooks/1191069822658818141/n0wWuyRcUfFvNmUijktEJ_z6N6W6bJKkk4iIoNcVChN7-E-cQfmtNLM3xYbUveC987iD", content=message)
response = webhook.execute()
