Anleitung zur Ausführung und die Vorführung des Programms als Video :
**https://youtu.be/GVV6QkHvKZE** (Anleitung ist als Untertitel enthalten)
-  



Schritte zum Ausführen des Programms:
--
**1.Python installieren:**   
Da das Programm in Python geschrieben wurde, muss zuerst eine Pythonversion (am besten eine der neuesten) installiert werden.
Python kann entweder im Microsoft Store installiert https://apps.microsoft.com/detail/9pjpw5ldxlz5?hl=en-US&gl=US werden 
oder online über https://www.python.org/downloads/.  

**2. Anwendung  herunterladen:**  
Nachdem Python heruntergeladen und installiert wurde können die Dateien von Github heruntergeladen werden.
Dazu kann unter dem Button "Code" (oben rechts, siehe oberes Bild), die Option "download ZIP" gewählt werden (siehe unteres Bild).  
![grafik](https://github.com/Moppi1/3D_demo/assets/150188517/dbb51c8c-3c0c-44b5-ab87-4717f780275d)
![grafik](https://github.com/Moppi1/3D_demo/assets/150188517/e9dce9b8-7a07-4315-beb0-88caba47dade)  
Sobald die ZIP datei heruntergeladen wurde kann diese extrahiert werden.  

**3. Anwendung  Ausführen:**   
In dem Ordner, in dem die einzelnen Python-Skripte liegen, kann nun bei Windows in die Kopfzeile mit/anstatt
der Pfadangabe, `cmd` eingegeben werden (mit Enter bestätigen).
![grafik](https://github.com/Moppi1/3D_demo/assets/150188517/dc4073e6-fcc7-4af8-a361-460cc4716732)

Dadurch öffnet sich die Konsole direkt im richtigen Verzeichnis.
![grafik](https://github.com/Moppi1/3D_demo/assets/150188517/d346a169-f531-433c-b2dd-3a928667f265)

In dem neu geöffneten Konsolenfenster kann nun `python main.py` eingegeben, und bestätigt werden.
Dadurch sollte sich das Programm öffnen und ausgeführt werden können.

Mögliche Probleme:
------
Nach der Richtigen Ausführung der Schritte 1 bis 3 sollte das Programm eigentlich starten.
Sollte die Anwendung dennoch nicht startet kann das mehrere Gründe haben..  

**1. Falsches Verzeichnis**  
Der Befehl `python main.py` wurde nicht in dem richtigen Verzeichnis ausgeführt. Schließen sie dazu die Konsole,
gehen sie in den Projekt-Ordner, in dem sich die Datei `main.py` findet, und führen sie dort erneut Schritt 3 aus.  

**2. Fehlende Library**  
Eine der genutzten Library's ist nicht installiert.
Standardmäßig sollte bei einer Pythoninstallation sowohl Pygame als auch Numpy 
(eine Python Library für schnellere Listen(also Datenstrukturen)) installiert sein. Sollte dies aber nicht der Fall sein, kann in der 
Konsole der Befehl `pip install pygame` ausgeführt werden, um Pygame zu installieren, und der Befehl `pip install Numpy` ausgeführt werden,
um Numpy zu installieren. Sollten diese Library's bereits installiert sein, werden sie nur geupdatet wenn eine neue Version verfügbar ist,
oder nicht verändert. Es kann also, selbst wenn die Library's installiert sind nicht schaden beide Library's mit den Befehlen zu installieren/updaten.
