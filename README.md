# pLOGS
python logs that get sent to your discord webhook.

contact me: Pyco#5460

## <u>FEATURES</u>
send ok, note, warn, error and critical responses.
check if a debugger is open by default and function to check

debuggers detected:
- cheat engine
- x64dbg

## <u>HOW TO USE</u>
```
from plogs import plogs
import sys

def main():
  pLOGS = plogs("WEBHOOK URL")
  pLOGS.sendok("title", "description")
  pLOGS.sendnote("title", "description")
  pLOGS.sendwarn("title", "description")
  pLOGS.senderror("title", "description")
  pLOGS.sendcritical("title", "description")
  
  if pLOGS.checkdebugger():
    print("sorry, but you cannot run this program with a debugger open!")
    sys.exit()
    
if __name__ == "__main__":
  main()  
```
<img src="https://cdn.discordapp.com/attachments/1111793042651873340/1112017229182152704/pLOGS.jpeg"></img>
