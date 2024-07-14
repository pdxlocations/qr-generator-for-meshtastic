# meshtastic-qr-generator
 
Connect a Meshtastic device to your computer and this python script will generate a folder containing multinational QR codes of the board's current LoRa and channel settings.  This is a simple way to share your settings with people in different regions, without having to switch your device to that region (which may violate your local regulations).

Run the script `python3 qr_generator.py` with the board connected to generate a folder of png's.

Requirements pyping, pyqrcode, meshtastic