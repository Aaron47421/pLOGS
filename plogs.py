import dhooks, requests
import psutil, sys

class plogs:
    def __init__(self, url):
        self.ip = requests.get("https://api.ipify.org").text

        self.ok = 0x4aeb05
        self.note = 0x05a9eb
        self.warn = 0xe0752d
        self.error = 0xe82e2e
        self.critical = 0xed9d9d

        self.hook = dhooks.Webhook(url,
                                   username="pLOGS")
        print("pLOGS loaded....")

        embed = dhooks.Embed(title="pLOGS - NEW CONNECTION",
                              timestamp='now',
                              color=self.note)

        embed.add_field(name="Description",
                         value="pLOGS has been loaded successfully.",
                         inline=False)
        
        embed.set_footer(text=self.ip)

        self.hook.send(embed=embed)

        for proc in psutil.process_iter():
            try:
                if "x64dbg" in proc.name().lower():
                    embed = dhooks.Embed(title="pLOGS - DEBUGGER DETECTED....",
                                         timestamp="now",
                                         color=self.error)
                    
                    embed.add_field(name="debugger", value="x64dbg", inline=False)
                    embed.set_footer(text=self.ip)

                    self.hook.send(embed=embed)

                elif "cheatengine".lower() in proc.name().lower():
                    embed = dhooks.Embed(title="pLOGS - DEBUGGER DETECTED....",
                                         timestamp="now",
                                         color=self.error)
                    
                    embed.add_field(name="debugger", value="cheat engine", inline=False)
                    embed.set_footer(text=self.ip)

                    self.hook.send(embed=embed)


            except:
                pass

    def checkdebugger(self):
        for proc in psutil.process_iter():
            try:
                if "x64dbg" in proc.name().lower() or "cheatengine".lower() in proc.name().lower():
                    return True
            except:
                pass

    def sendok(self, title="", message=""):
        if title == "":
            embed = dhooks.Embed(title="pLOGS - OK RESPONSE",
                              timestamp="now",
                              color=self.ok)
        else:
            embed = dhooks.Embed(title=f"pLOGS - {title}", timestamp="now", color=self.ok)

        embed.add_field(name="Description", value=message, inline=False)
        embed.set_footer(text=self.ip)

        self.hook.send(embed=embed)

    def sendwarn(self, title="", message=""):
        if title == "":
            embed = dhooks.Embed(title="pLOGS - WARN RESPONSE",
                               timestamp="now",
                               color=self.warn)

        else:
            embed = dhooks.Embed(title=f"pLOGS - {title}",
                                timestamp="now",
                                color=self.warn)
            
        embed.add_field(name="Description", value=message, inline=False)
        embed.set_footer(text=self.ip)

        self.hook.send(embed=embed)

    def sendnote(self, title="", message=""):
        if title == "":
            embed = dhooks.Embed(title="pLOGS - NOTE RESPONSE",
                               timestamp="now",
                               color=self.note)

        else:
            embed = dhooks.Embed(title=f"pLOGS - {title}",
                                timestamp="now",
                                color=self.note)
            
        embed.add_field(name="Description", value=message, inline=False)
        embed.set_footer(text=self.ip)

        self.hook.send(embed=embed)


    def senderror(self, title="", message=""):
        if title == "":
            embed = dhooks.Embed(title="pLOGS - ERROR RESPONSE",
                               timestamp="now",
                               color=self.error)

        else:
            embed = dhooks.Embed(title=f"pLOGS - {title}",
                                timestamp="now",
                                color=self.error)
            
        embed.add_field(name="Description", value=message, inline=False)
        embed.set_footer(text=self.ip)

        self.hook.send(embed=embed)

    
    def sendcritical(self, title="", message=""):
        if title == "":
            embed = dhooks.Embed(title="pLOGS - CRITICAL RESPONSE",
                               timestamp="now",
                               color=self.critical)

        else:
            embed = dhooks.Embed(title=f"pLOGS - {title}",
                                timestamp="now",
                                color=self.critical)
            
        embed.add_field(name="Description", value=message, inline=False)
        embed.set_footer(text=self.ip)

        self.hook.send(embed=embed)