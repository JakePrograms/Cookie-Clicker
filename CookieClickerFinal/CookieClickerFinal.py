import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk
import time
from pygame import mixer

mixer.init()

starttime = time.time()

window = tk.Tk()
window.title("Cookie Clicker")
window.configure(background="white")
window.minsize(400,400)
window.geometry("1200x800")
window.iconbitmap('CookieIcon.ico')

cookie = Image.open('cookie.jpg')
cookie = cookie.resize((200,200), Image.ANTIALIAS)
cookie = ImageTk.PhotoImage(cookie)

shop = Image.open('shop.jpg')
shop = shop.resize((125,125), Image.ANTIALIAS)
shop = ImageTk.PhotoImage(shop)

Cursor = Image.open('Cursor.jpg')
Cursor = Cursor.resize((125,125), Image.ANTIALIAS)
Cursor = ImageTk.PhotoImage(Cursor)

Grandma = Image.open('Grandma.jpg')
Grandma = Grandma.resize((125,125), Image.ANTIALIAS)
Grandma = ImageTk.PhotoImage(Grandma)

Farm = Image.open('Farm.png')
Farm = Farm.resize((125,125), Image.ANTIALIAS)
Farm = ImageTk.PhotoImage(Farm)

Mine = Image.open('Mine.png')
Mine = Mine.resize((125,125), Image.ANTIALIAS)
Mine = ImageTk.PhotoImage(Mine)

Factory = Image.open('Factory.png')
Factory = Factory.resize((125,125), Image.ANTIALIAS)
Factory = ImageTk.PhotoImage(Factory)

C1 = Image.open('CursorUpgrade1.jpg')
C1 = C1.resize((125,125), Image.ANTIALIAS)
C1 = ImageTk.PhotoImage(C1)

C2 = Image.open('CursorUpgrade2.png')
C2 = C2.resize((125,125), Image.ANTIALIAS)
C2 = ImageTk.PhotoImage(C2)

S = Image.open('settings.jpg')
S = S.resize((400,400), Image.ANTIALIAS)
S = ImageTk.PhotoImage(S)

St = Image.open('stats.jpg')
St = St.resize((400,400), Image.ANTIALIAS)
St = ImageTk.PhotoImage(St)

mainFont = ('times', 20, 'bold italic')
creditFont = ('times', 20, 'bold')
NextPreviousFont = ('times', 13, 'bold')

TotalCookies = 0
Cookies = 0
cursorPrice = 20
cursorTotal = 0
cursorClicks = 1
grandmaPrice = 150
grandmaTotal = 0
grandmaClicks = 5
farmPrice = 2000
farmTotal = 0
farmClicks = 25
minePrice = 15000
mineTotal = 0
mineClicks = 200
factoryPrice = 200000
factoryTotal = 0
factoryClicks = 1000
UpgradePrice1 = 1000
UpgradePrice2 = 10000
CursorBonusTotal = 0
BoughtUpgrade1 = 0
BoughtUpgrade2 = 0
Music = 0
NameCheck = 0
def MainScreen():                                                                                                                                                               #Code where entire game starts
    global Music
    def MusicOnOff():
        if Music == 1:
            mixer.music.load("BGMusic.mp3")
            mixer.music.play(loops=10)
        elif Music == 0:
            mixer.music.stop()
    def press():                                                                                                                                                                #Counts an infinte amount of presses by user
        global CursorBonusTotal
        global Cookies
        global TotalCookies
        if CursorBonusTotal == 0:
            Cookies += 1
            CountDisplay.config(text=f" Cookies: \n"+str(Cookies))
            TotalCookies += 1
        elif CursorBonusTotal == 1:
            Cookies += 2
            CountDisplay.config(text=f" Cookies: \n"+str(Cookies))
            TotalCookies += 2
        elif CursorBonusTotal == 2:
            Cookies += 4
            CountDisplay.config(text=f" Cookies: \n"+str(Cookies))
            TotalCookies += 4
    def Settings():                                                                                                                                                             #Code for entire settings menu
        shopButton.destroy()
        MainCookie.destroy()
        settingsButton.destroy()
        infoButton.destroy()
        creditsButton.destroy()
        statsButton.destroy()
        CpsCounter.destroy()
        global Music
        global MusicButton
        def MainMusicOn():
            global Music
            global MusicButton1
            Music = 1
            MusicButton.config(text='Off', bg='red', fg='black', command =lambda:[MainMusicOff(), MusicOnOff()])
        def MainMusicOff():
            global Music
            global MusicButton1
            global MusicButton2
            Music = 0
            MusicButton.config(text='On', bg='green', fg='lime', command =lambda:[MainMusicOn(), MusicOnOff()])
        if Music == 1:
            MusicButton = Button(window, text='Off', bg='red', fg='black', highlightthickness=5, bd=10, relief=GROOVE, command =lambda:[MainMusicOff(), MusicOnOff()])
            MusicButton.place(x=350,y=200)
        elif Music == 0:
            MusicButton = Button(window, text='On', bg='green', fg='lime', highlightthickness=5, bd=10, relief=GROOVE, command =lambda:[MainMusicOn(), MusicOnOff()])
            MusicButton.place(x=350,y=200)
        MusicInfo = Label(window, text='Turn music on/off!', bg='white', font=mainFont)
        MusicInfo.place(x=100,y=205)
        SettingsImg = Label(window, image=S)
        SettingsImg.place(x=700,y=250)
        global BakeryName
        def BakeryNameChange():
            global UserBakeryName
            BakeryTitle = BakeryName.get()
            UserBakeryName = Label(window, text=str(BakeryTitle)+"'s Bakery", bg='white', width=25, font=('times', 20, 'bold'))
            UserBakeryName.place(x=400,y=50)
        BakeryName = Entry(window, width=20, bg='blue', font=mainFont, highlightthickness=5, bd=10, relief=RIDGE)
        BakeryName.place(x=100,y=400)
        BakeryInfo = Label(window, text='Enter Your Name!', bg='white', font=mainFont)
        BakeryInfo.place(x=125,y=350)
        BakeryButton = Button(window, text='Confirm Name', bg='purple', fg='pink', highlightthickness=5, bd=10, relief=GROOVE, command=BakeryNameChange)
        BakeryButton.place(x=200,y=475)
        def DestroyButton():
            returnButton.destroy()
            MusicButton.destroy()
            MusicInfo.destroy()
            BakeryName.destroy()
            BakeryInfo.destroy()
            BakeryButton.destroy()
            SettingsImg.destroy()
        returnButton = tk.Button(window, text="Return", command=lambda:[MainScreen(), DestroyButton()], highlightthickness = 5, bd = 10, font=mainFont, bg='black', fg='white', relief=GROOVE)
        returnButton.place(x=500,y=700)

    def Info():                                                                                                                                                                 #Code for entire info menu(DONE!)
        FMC = tk.Button(window, image=cookie, highlightthickness = 0, bd = 0)
        FMC.place(x=500,y=300)

        FSB = tk.Button(window, text="Settings", highlightthickness = 5, bd = 10, font=mainFont, bg='red', relief=GROOVE)
        FSB.place(x=100,y=700)

        FIB = tk.Button(window, text="Info", highlightthickness = 5, bd = 10, font=mainFont, bg='blue', relief=GROOVE)
        FIB.place(x=400,y=700)

        FCB = tk.Button(window, text="Credits", highlightthickness = 5, bd = 10, font=mainFont, bg='green', relief=GROOVE)
        FCB.place(x=700,y=700)

        FStB = tk.Button(window, text="Stats", highlightthickness = 5, bd = 10, font=mainFont, bg='yellow', relief=GROOVE)
        FStB.place(x=1000,y=700)

        FShB = tk.Button(window, image=shop, highlightthickness = 5, bd = 10, relief=GROOVE)
        FShB.place(x=50,y=50)
        cookieInfo = Label(window, text="Click here to gain cookies!", bg="white", font=mainFont, relief=RIDGE, bd=10)
        cookieInfo.place(x=700,y=300)
        def CounterInfo():
            cookieInfo.destroy()
            Next.destroy()
            counterInfo = Label(window, text="Counts your current coookies!", bg="white", font=mainFont, relief=RIDGE, bd=10)
            counterInfo.place(x=600,y=50)
            def ShopInfo():
                counterInfo.destroy()
                Next1.destroy()
                Previous1.destroy()
                shopInfo = Label(window, text="Spend your cookies for upgrades!", bg="white", font=mainFont, relief=RIDGE, bd=10)
                shopInfo.place(x=200, y=100)
                def FinishInfo():
                    shopInfo.destroy()
                    Next2.destroy()
                    Previous2.destroy()
                    MainCookie.destroy()
                    settingsButton.destroy()
                    infoButton.destroy()
                    creditsButton.destroy()
                    shopButton.destroy()
                    statsButton.destroy()
                    CpsCounter.destroy()
                    FMC.destroy()
                    FSB.destroy()
                    FIB.destroy()
                    FCB.destroy()
                    FShB.destroy()
                    FStB.destroy()
                Next2 = Button(window, text="Next", command=lambda:[FinishInfo(), MainScreen()], font=NextPreviousFont, relief=RIDGE, bd=5, height=1, width=4)
                Next2.place(x=550,y=150)
                def DestroyShopInfo():
                    Next2.destroy()
                    Previous2.destroy()
                    shopInfo.destroy()
                    FMC.destroy()
                    FSB.destroy()
                    FIB.destroy()
                    FCB.destroy()
                    FShB.destroy()
                    FStB.destroy()
                Previous2 = Button(window, text="Prev.", command=lambda:[CounterInfo(), DestroyShopInfo()], font=NextPreviousFont, relief=RIDGE, bd=5, height=1, width=4)
                Previous2.place(x=200,y=150)
            Next1 = Button(window, text="Next", command=ShopInfo, font=NextPreviousFont, relief=RIDGE, bd=5, height=1, width=4)
            Next1.place(x=912,y=100)
            def DestroyCounterInfo():
                Next1.destroy()
                Previous1.destroy()
                counterInfo.destroy()
                FMC.destroy()
                FSB.destroy()
                FIB.destroy()
                FCB.destroy()
                FShB.destroy()
                FStB.destroy()
            Previous1 = Button(window, text="Prev.", command=lambda:[Info(), DestroyCounterInfo()], font=NextPreviousFont, relief=RIDGE, bd=5, height=1, width=4)
            Previous1.place(x=600,y=100)
        Next = Button(window, text="Next", command=CounterInfo, font=NextPreviousFont, relief=RIDGE, bd=5, height=1, width=4)
        Next.place(x=972,y=350)

    def Credits():                                                                                                                                                              #Code for entire credits menu(DONE!)
        shopButton.destroy()
        MainCookie.destroy()
        settingsButton.destroy()
        infoButton.destroy()
        creditsButton.destroy()
        statsButton.destroy()
        CpsCounter.destroy()
        creditsTitle = Label(window, text="Credits", font=mainFont, bg="white")
        creditsTitle.place(x=500,y=100)
        programmer = Label(window, text="Programmer: \nJacob Matte-Kubecka", font=creditFont, bg="white")
        programmer.place(x=425,y=200)
        original = Label(window, text='Original Creator: \nJulien "Orteil" Thiennot', font=creditFont, bg="white")
        original.place(x=400,y=350)
        final = Label(window, text="This was a fan-made program!\nPlease support the official release.", font=creditFont, bg="white")
        final.place(x=375,y=500)
        def DestroyButton():
            returnButton.destroy()
            creditsTitle.destroy()
            programmer.destroy()
            original.destroy()
            final.destroy()
        returnButton = tk.Button(window, text="Return", command=lambda:[MainScreen(), DestroyButton()], highlightthickness = 5, bd = 10, font=mainFont, bg='black', fg='white', relief=GROOVE)
        returnButton.place(x=500,y=700)

    def Stats():                                                                                                                                                                #Code for entire stats menu
        global cursorTotal
        global grandmaTotal
        global farmTotal
        global mineTotal
        global factoryTotal
        shopButton.destroy()
        MainCookie.destroy()
        settingsButton.destroy()
        infoButton.destroy()
        creditsButton.destroy()
        statsButton.destroy()
        CpsCounter.destroy()
        endtime = time.time()
        totaltime = endtime - starttime
        totaltime = round(totaltime, 2)
        TotalTime = Label(window, text="Total Time Elapsed(seconds): "+str(totaltime), font=mainFont, bg="white")
        TotalTime.place(x=100,y=100)

        totalCookies = Label(window, text="Total Cookies earned(all-time): "+str(TotalCookies), font=mainFont, bg="white")
        totalCookies.place(x=100,y=150)

        CursorCPS = cursorClicks * cursorTotal
        totalCursors = Label(window, text="Total Cursors owned: "+str(cursorTotal)+" ("+str(CursorCPS)+" CpS)", font=mainFont, bg="white")
        totalCursors.place(x=100,y=200)

        GrandmaCPS = grandmaClicks * grandmaTotal
        totalGrandmas = Label(window, text="Total Grandmas owned: "+str(grandmaTotal)+" ("+str(GrandmaCPS)+" CpS)", font=mainFont, bg="white")
        totalGrandmas.place(x=100,y=250)

        FarmCPS = farmClicks * farmTotal
        totalFarms = Label(window, text="Total Farms owned: "+str(farmTotal)+" ("+str(FarmCPS)+" CpS)", font=mainFont, bg="white")
        totalFarms.place(x=100,y=300)

        MineCPS = mineClicks * mineTotal
        totalMines = Label(window, text="Total Mines owned: "+str(mineTotal)+" ("+str(MineCPS)+" CpS)", font=mainFont, bg="white")
        totalMines.place(x=100,y=350)

        FactoryCPS = factoryClicks * factoryTotal
        totalFactories = Label(window, text="Total Factories owned: "+str(factoryTotal)+" ("+str(FactoryCPS)+" CpS)", font=mainFont, bg="white")
        totalFactories.place(x=100,y=400)
        if BoughtUpgrade1 == 1 and BoughtUpgrade2 == 1:
            CM = Label(window, text="Total Click Multiplier: 4x", font=mainFont, bg="white")
            CM.place(x=100,y=450)
        elif BoughtUpgrade1 == 1:
            CM = Label(window, text="Total Click Multiplier: 2x", font=mainFont, bg="white")
            CM.place(x=100,y=450)
        elif BoughtUpgrade2 == 1:
            CM = Label(window, text="Total Click Multiplier: 2x", font=mainFont, bg="white")
            CM.place(x=100,y=450)
        else:
            CM = Label(window, text="Total Click Multiplier: 1x", font=mainFont, bg="white")
            CM.place(x=100,y=450)
        StatsImg = Label(window, image=St)
        StatsImg.place(x=700,y=300)
        def DestroyButton():
            returnButton.destroy()
            TotalTime.destroy()
            totalCookies.destroy()
            totalCursors.destroy()
            totalGrandmas.destroy()
            totalFarms.destroy()
            totalMines.destroy()
            totalFactories.destroy()
            CM.destroy()
            StatsImg.destroy()
        returnButton = tk.Button(window, text="Return", command=lambda:[MainScreen(), DestroyButton()], highlightthickness = 5, bd = 10, font=mainFont, bg='black', fg='white', relief=GROOVE)
        returnButton.place(x=500,y=700)

    def Shop():                                                                                                                                                                 #Code for enire shop menu
        global cursorInfo
        global grandmaInfo
        global farmInfo
        global mineInfo
        global factoryInfo
        global cursorButton
        global grandmaButton
        global farmButton
        global mineButton
        global factoryButton
        def cursorBuy():
            global Cookies
            global cursorTotal
            global cursorPrice
            if cursorPrice <= Cookies:
                Cookies = Cookies - cursorPrice
                cursorTotal += 1
                cursorPrice = cursorPrice * 1.15
                cursorPrice = round(cursorPrice, 0)
                cursorInfo.destroy()
                grandmaInfo.destroy()
                farmInfo.destroy()
                mineInfo.destroy()
                factoryInfo.destroy()
                cursorButton.destroy()
                grandmaButton.destroy()
                farmButton.destroy()
                mineButton.destroy()
                factoryButton.destroy()
                returnButton.destroy()
                CpsInfo.destroy()
                CursorUpgrade1.destroy()
                UpgradeInfo1.destroy()
                CursorUpgrade2.destroy()
                UpgradeInfo2.destroy()
            else:
                Cookies = Cookies - 0
                cursorInfo.destroy()
                grandmaInfo.destroy()
                farmInfo.destroy()
                mineInfo.destroy()
                factoryInfo.destroy()
                cursorButton.destroy()
                grandmaButton.destroy()
                farmButton.destroy()
                mineButton.destroy()
                factoryButton.destroy()
                returnButton.destroy()
                CpsInfo.destroy()
                CursorUpgrade1.destroy()
                UpgradeInfo1.destroy()
                CursorUpgrade2.destroy()
                UpgradeInfo2.destroy()
                NotEnough = tk.Label(window, text="Not Enough Cookies!", font=mainFont, fg='red', bg='white')
                NotEnough.place(x=100,y=600)
                def NotEnoughDestroy():
                    NotEnough.destroy()
                window.after(1000, NotEnoughDestroy)
        def grandmaBuy():
            global Cookies
            global grandmaTotal
            global grandmaPrice
            if grandmaPrice <= Cookies:
                Cookies = Cookies - grandmaPrice
                grandmaTotal += 1
                grandmaPrice = grandmaPrice * 1.15
                grandmaPrice = round(grandmaPrice, 0)
                cursorInfo.destroy()
                grandmaInfo.destroy()
                farmInfo.destroy()
                mineInfo.destroy()
                factoryInfo.destroy()
                cursorButton.destroy()
                grandmaButton.destroy()
                farmButton.destroy()
                mineButton.destroy()
                factoryButton.destroy()
                returnButton.destroy()
                CpsInfo.destroy()
                CursorUpgrade1.destroy()
                UpgradeInfo1.destroy()
                CursorUpgrade2.destroy()
                UpgradeInfo2.destroy()
            else:
                Cookies = Cookies - 0
                cursorInfo.destroy()
                grandmaInfo.destroy()
                farmInfo.destroy()
                mineInfo.destroy()
                factoryInfo.destroy()
                cursorButton.destroy()
                grandmaButton.destroy()
                farmButton.destroy()
                mineButton.destroy()
                factoryButton.destroy()
                returnButton.destroy()
                CpsInfo.destroy()
                CursorUpgrade1.destroy()
                UpgradeInfo1.destroy()
                CursorUpgrade2.destroy()
                UpgradeInfo2.destroy()
                NotEnough = tk.Label(window, text="Not Enough Cookies!", font=mainFont, fg='red', bg='white')
                NotEnough.place(x=100,y=600)
                def NotEnoughDestroy():
                    NotEnough.destroy()
                window.after(1000, NotEnoughDestroy)
        def farmBuy():
            global Cookies
            global farmTotal
            global farmPrice
            if farmPrice <= Cookies:
                Cookies = Cookies - farmPrice
                farmTotal += 1
                farmPrice = farmPrice * 1.15
                farmPrice = round(farmPrice, 0)
                cursorInfo.destroy()
                grandmaInfo.destroy()
                farmInfo.destroy()
                mineInfo.destroy()
                factoryInfo.destroy()
                cursorButton.destroy()
                grandmaButton.destroy()
                farmButton.destroy()
                mineButton.destroy()
                factoryButton.destroy()
                returnButton.destroy()
                CpsInfo.destroy()
                CursorUpgrade1.destroy()
                UpgradeInfo1.destroy()
                CursorUpgrade2.destroy()
                UpgradeInfo2.destroy()
            else:
                Cookies = Cookies - 0
                cursorInfo.destroy()
                grandmaInfo.destroy()
                farmInfo.destroy()
                mineInfo.destroy()
                factoryInfo.destroy()
                cursorButton.destroy()
                grandmaButton.destroy()
                farmButton.destroy()
                mineButton.destroy()
                factoryButton.destroy()
                returnButton.destroy()
                CpsInfo.destroy()
                CursorUpgrade1.destroy()
                UpgradeInfo1.destroy()
                CursorUpgrade2.destroy()
                UpgradeInfo2.destroy()
                NotEnough = tk.Label(window, text="Not Enough Cookies!", font=mainFont, fg='red', bg='white')
                NotEnough.place(x=100,y=600)
                def NotEnoughDestroy():
                    NotEnough.destroy()
                window.after(1000, NotEnoughDestroy)
        def mineBuy():
            global Cookies
            global mineTotal
            global minePrice
            if minePrice <= Cookies:
                Cookies = Cookies - minePrice
                mineTotal += 1
                minePrice = minePrice * 1.15
                minePrice = round(minePrice, 0)
                cursorInfo.destroy()
                grandmaInfo.destroy()
                farmInfo.destroy()
                mineInfo.destroy()
                factoryInfo.destroy()
                cursorButton.destroy()
                grandmaButton.destroy()
                farmButton.destroy()
                mineButton.destroy()
                factoryButton.destroy()
                returnButton.destroy()
                CpsInfo.destroy()
                CursorUpgrade1.destroy()
                UpgradeInfo1.destroy()
                CursorUpgrade2.destroy()
                UpgradeInfo2.destroy()
            else:
                Cookies = Cookies - 0
                cursorInfo.destroy()
                grandmaInfo.destroy()
                farmInfo.destroy()
                mineInfo.destroy()
                factoryInfo.destroy()
                cursorButton.destroy()
                grandmaButton.destroy()
                farmButton.destroy()
                mineButton.destroy()
                factoryButton.destroy()
                returnButton.destroy()
                CpsInfo.destroy()
                CursorUpgrade1.destroy()
                UpgradeInfo1.destroy()
                CursorUpgrade2.destroy()
                UpgradeInfo2.destroy()
                NotEnough = tk.Label(window, text="Not Enough Cookies!", font=mainFont, fg='red', bg='white')
                NotEnough.place(x=100,y=600)
                def NotEnoughDestroy():
                    NotEnough.destroy()
                window.after(1000, NotEnoughDestroy)
        def factoryBuy():
            global Cookies
            global factoryTotal
            global factoryPrice
            if factoryPrice <= Cookies:
                Cookies = Cookies - factoryPrice
                factoryTotal += 1
                factoryPrice = factoryPrice * 1.15
                factoryPrice = round(factoryPrice, 0)
                cursorInfo.destroy()
                grandmaInfo.destroy()
                farmInfo.destroy()
                mineInfo.destroy()
                factoryInfo.destroy()
                cursorButton.destroy()
                grandmaButton.destroy()
                farmButton.destroy()
                mineButton.destroy()
                factoryButton.destroy()
                returnButton.destroy()
                CpsInfo.destroy()
                CursorUpgrade1.destroy()
                UpgradeInfo1.destroy()
                CursorUpgrade2.destroy()
                UpgradeInfo2.destroy()
            else:
                Cookies = Cookies - 0
                cursorInfo.destroy()
                grandmaInfo.destroy()
                farmInfo.destroy()
                mineInfo.destroy()
                factoryInfo.destroy()
                cursorButton.destroy()
                grandmaButton.destroy()
                farmButton.destroy()
                mineButton.destroy()
                factoryButton.destroy()
                returnButton.destroy()
                CpsInfo.destroy()
                CursorUpgrade1.destroy()
                UpgradeInfo1.destroy()
                CursorUpgrade2.destroy()
                UpgradeInfo2.destroy()
                NotEnough = tk.Label(window, text="Not Enough Cookies!", font=mainFont, fg='red', bg='white')
                NotEnough.place(x=100,y=600)
                def NotEnoughDestroy():
                    NotEnough.destroy()
                window.after(1000, NotEnoughDestroy)
        def CU1():
            global CursorBonusTotal
            global Cookies
            global UpgradePrice1
            if UpgradePrice1 <= Cookies:
                Cookies = Cookies - UpgradePrice1
                CursorBonusTotal += 1
                cursorInfo.destroy()
                grandmaInfo.destroy()
                farmInfo.destroy()
                mineInfo.destroy()
                factoryInfo.destroy()
                cursorButton.destroy()
                grandmaButton.destroy()
                farmButton.destroy()
                mineButton.destroy()
                factoryButton.destroy()
                returnButton.destroy()
                CpsInfo.destroy()
                CursorUpgrade1.destroy()
                UpgradeInfo1.destroy()
                CursorUpgrade2.destroy()
                UpgradeInfo2.destroy()
                global BoughtUpgrade1
                BoughtUpgrade1 = 1
            else:
                Cookies = Cookies - 0
                cursorInfo.destroy()
                grandmaInfo.destroy()
                farmInfo.destroy()
                mineInfo.destroy()
                factoryInfo.destroy()
                cursorButton.destroy()
                grandmaButton.destroy()
                farmButton.destroy()
                mineButton.destroy()
                factoryButton.destroy()
                returnButton.destroy()
                CpsInfo.destroy()
                CursorUpgrade1.destroy()
                UpgradeInfo1.destroy()
                CursorUpgrade2.destroy()
                UpgradeInfo2.destroy()
                NotEnough = tk.Label(window, text="Not Enough Cookies!", font=mainFont, fg='red', bg='white')
                NotEnough.place(x=100,y=600)
                def NotEnoughDestroy():
                    NotEnough.destroy()
                window.after(1000, NotEnoughDestroy)
        def CU2():
            global CursorBonusTotal
            global Cookies
            global UpgradePrice2
            if UpgradePrice2 <= Cookies:
                Cookies = Cookies - UpgradePrice2
                CursorBonusTotal += 1
                cursorInfo.destroy()
                grandmaInfo.destroy()
                farmInfo.destroy()
                mineInfo.destroy()
                factoryInfo.destroy()
                cursorButton.destroy()
                grandmaButton.destroy()
                farmButton.destroy()
                mineButton.destroy()
                factoryButton.destroy()
                returnButton.destroy()
                CpsInfo.destroy()
                CursorUpgrade1.destroy()
                UpgradeInfo1.destroy()
                CursorUpgrade2.destroy()
                UpgradeInfo2.destroy()
                global BoughtUpgrade2
                BoughtUpgrade2 = 1
            else:
                Cookies = Cookies - 0
                cursorInfo.destroy()
                grandmaInfo.destroy()
                farmInfo.destroy()
                mineInfo.destroy()
                factoryInfo.destroy()
                cursorButton.destroy()
                grandmaButton.destroy()
                farmButton.destroy()
                mineButton.destroy()
                factoryButton.destroy()
                returnButton.destroy()
                CpsInfo.destroy()
                CursorUpgrade1.destroy()
                UpgradeInfo1.destroy()
                CursorUpgrade2.destroy()
                UpgradeInfo2.destroy()
                NotEnough = tk.Label(window, text="Not Enough Cookies!", font=mainFont, fg='red', bg='white')
                NotEnough.place(x=100,y=600)
                def NotEnoughDestroy():
                    NotEnough.destroy()
                window.after(1000, NotEnoughDestroy)
        cursorInfo = Label(window, text="Grants 1 CpS!\nPrice: "+str(cursorPrice)+"\nTotal owned: "+str(cursorTotal), font=('times', 10, 'bold italic'), bg='white')
        cursorInfo.place(x=125,y=300)
        cursorButton = tk.Button(window, image=Cursor, command=lambda:[cursorBuy(), Shop()], highlightthickness = 3, bd = 10, relief=GROOVE)
        cursorButton.place(x=100,y=150)

        grandmaInfo = Label(window, text="Grants 5 CpS!\nPrice: "+str(grandmaPrice)+"\nTotal owned: "+str(grandmaTotal), font=('times', 10, 'bold italic'), bg='white')
        grandmaInfo.place(x=325,y=300)
        grandmaButton = tk.Button(window, image=Grandma, command=lambda:[grandmaBuy(), Shop()], highlightthickness = 3, bd = 10, relief=GROOVE)
        grandmaButton.place(x=300,y=150)

        farmInfo = Label(window, text="Grants 25 CpS!\nPrice: "+str(farmPrice)+"\nTotal owned: "+str(farmTotal), font=('times', 10, 'bold italic'), bg='white')
        farmInfo.place(x=525,y=300)
        farmButton = tk.Button(window, image=Farm, command=lambda:[farmBuy(), Shop()], highlightthickness = 3, bd = 10, relief=GROOVE)
        farmButton.place(x=500,y=150)

        mineInfo = Label(window, text="Grants 200 CpS!\nPrice: "+str(minePrice)+"\nTotal owned: "+str(mineTotal), font=('times', 10, 'bold italic'), bg='white')
        mineInfo.place(x=725,y=300)
        mineButton = tk.Button(window, image=Mine, command=lambda:[mineBuy(), Shop()], highlightthickness = 3, bd = 10, relief=GROOVE)
        mineButton.place(x=700,y=150)

        factoryInfo = Label(window, text="Grants 1,000 CpS!\nPrice: "+str(factoryPrice)+"\nTotal owned: "+str(factoryTotal), font=('times', 10, 'bold italic'), bg='white')
        factoryInfo.place(x=925,y=300)
        factoryButton = tk.Button(window, image=Factory, command=lambda:[factoryBuy(), Shop()], highlightthickness = 3, bd = 10, relief=GROOVE)
        factoryButton.place(x=900,y=150)

        CpsInfo = Label(window, text="Cookies per Second = CpS\n Don't Forget it!", font=('times', 15, 'bold'), bg='white')
        CpsInfo.place(x=450,y=600)

        def Bought1():
            global BoughtLabel1
            BoughtLabel1 = tk.Label(window, text="Already Bought!", font=mainFont, fg='green', bg='white')
            BoughtLabel1.place(x=800,y=600)
            def BoughtDestroy1():
                BoughtLabel1.destroy()
            window.after(1000, BoughtDestroy1)
        def Bought2():
            global BoughtLabel2
            BoughtLabel2 = tk.Label(window, text="Already Bought!", font=mainFont, fg='green', bg='white')
            BoughtLabel2.place(x=800,y=600)
            def BoughtDestroy2():
                BoughtLabel2.destroy()
            window.after(1000, BoughtDestroy2)
        global BoughtUpgrade1
        if BoughtUpgrade1 == 1:
            CursorUpgrade1 = tk.Button(window, image=C1, command=Bought1, highlightthickness = 3, bd = 10, relief=GROOVE)
            CursorUpgrade1.place(x=400,y=400)
            UpgradeInfo1 = Label(window, text="Grants 2x Cookies/Click!\nPrice: 1,000", font=('times', 10, 'bold italic'), bg='white')
            UpgradeInfo1.place(x=400,y=550)
        else:
            CursorUpgrade1 = tk.Button(window, image=C1, command=lambda:[CU1(), Shop()], highlightthickness = 3, bd = 10, relief=GROOVE)
            CursorUpgrade1.place(x=400,y=400)
            UpgradeInfo1 = Label(window, text="Grants 2x Cookies/Click!\nPrice: 1,000", font=('times', 10, 'bold italic'), bg='white')
            UpgradeInfo1.place(x=400,y=550)

        global BoughtUpgrade2
        if BoughtUpgrade2 == 1:
            CursorUpgrade2 = tk.Button(window, image=C2, command=Bought2, highlightthickness = 3, bd = 10, relief=GROOVE)
            CursorUpgrade2.place(x=600,y=400)
            UpgradeInfo2 = Label(window, text="Grants 2x Cookies/Click!\nPrice: 10,000", font=('times', 10, 'bold italic'), bg='white')
            UpgradeInfo2.place(x=600,y=550)
        else:
            CursorUpgrade2 = tk.Button(window, image=C2, command=lambda:[CU2(), Shop()], highlightthickness = 3, bd = 10, relief=GROOVE)
            CursorUpgrade2.place(x=600,y=400)
            UpgradeInfo2 = Label(window, text="Grants 2x Cookies/Click!\nPrice: 10,000", font=('times', 10, 'bold italic'), bg='white')
            UpgradeInfo2.place(x=600,y=550)

        shopButton.destroy()
        MainCookie.destroy()
        settingsButton.destroy()
        infoButton.destroy()
        creditsButton.destroy()
        statsButton.destroy()
        CpsCounter.destroy()
        
        
        def DestroyButton():
            returnButton.destroy()
            cursorInfo.destroy()
            grandmaInfo.destroy()
            farmInfo.destroy()
            mineInfo.destroy()
            factoryInfo.destroy()
            cursorButton.destroy()
            grandmaButton.destroy()
            farmButton.destroy()
            mineButton.destroy()
            factoryButton.destroy()
            CpsInfo.destroy()
            CursorUpgrade1.destroy()
            UpgradeInfo1.destroy()
            CursorUpgrade2.destroy()
            UpgradeInfo2.destroy()
        returnButton = tk.Button(window, text="Return", command=lambda:[MainScreen(), DestroyButton()], highlightthickness = 5, bd = 10, font=mainFont, bg='black', fg='white', relief=GROOVE)
        returnButton.place(x=500,y=700)
    
    global Cookies
    global CpS
    global CpsCounter

    CpsCounter = tk.Label(window, text="Current CpS: \n"+str(CpS), font=mainFont, bg="white", highlightthickness = 0, bd = 0)
    CpsCounter.place(x=990,y=150)

    MainCookie = tk.Button(window, image=cookie, command=press, highlightthickness = 0, bd = 0)
    MainCookie.place(x=500,y=300)

    settingsButton = tk.Button(window, text="Settings", command=Settings, highlightthickness = 5, bd = 10, font=mainFont, bg='red', relief=GROOVE)
    settingsButton.place(x=100,y=700)

    infoButton = tk.Button(window, text="Info", command=Info, highlightthickness = 5, bd = 10, font=mainFont, bg='blue', relief=GROOVE)
    infoButton.place(x=400,y=700)

    creditsButton = tk.Button(window, text="Credits", command=Credits, highlightthickness = 5, bd = 10, font=mainFont, bg='green', relief=GROOVE)
    creditsButton.place(x=700,y=700)

    statsButton = tk.Button(window, text="Stats", command=Stats, highlightthickness = 5, bd = 10, font=mainFont, bg='yellow', relief=GROOVE)
    statsButton.place(x=1000,y=700)

    shopButton = tk.Button(window, image=shop, command=Shop, highlightthickness = 5, bd = 10, relief=GROOVE)
    shopButton.place(x=50,y=50)


global CountDisplay
CountDisplay = tk.Label(window, text=" Cookies: \n"+str(Cookies), font=mainFont, bg="orange", bd = 10, relief=RIDGE)
CountDisplay.place(x=1000,y=50)
def IdleCpS():
        global CpS
        global cursorTotal
        global cursorClicks
        global grandmaTotal
        global grandmaClicks
        global farmTotal
        global farmClicks
        global mineTotal
        global mineClicks
        global factoryTotal
        global factoryClicks
        global TotalCookies
        global Cookies
        CpS = (cursorClicks * cursorTotal)+(grandmaClicks * grandmaTotal)+(farmClicks * farmTotal)+(mineClicks * mineTotal)+(factoryClicks * factoryTotal)
        CpS = round(CpS, 0)
        Cookies += CpS
        TotalCookies += CpS
        CountDisplay.config(text=f" Cookies: \n"+str(Cookies))
        window.after(1000, IdleCpS)
IdleCpS()
MainScreen()
window.mainloop()
