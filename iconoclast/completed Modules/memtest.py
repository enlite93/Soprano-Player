from gi.repository import Gtk, GdkPixbuf, GObject, AppIndicator3, Notify, Gst# about 8.5 Mb memory used here
import os
from settings import settings
from settings import sopranoGlobals

from music.mediakeys import mediakeys
from music.tagreading import TrackMetaData
from music.cdcover import getCover # 10.6 Mb of Memory
from music.gstreamerplayerGOBJECT import MusicPlayer
from music.mpris import SoundMenuControls

from gui.combobox import HeaderedComboBox
from gui.aboutbox import aboutBoxShow
from gui.propertreefilebrowser import IconoTreeFile # about 14.5mb of memory
from gui.AudioCD import IconoAudioCD # 14.3mb of Memory
from gui.NetRadio import IconoRadio
from gui.liststore import IconoListView # about 11.2mb of memory
from gui.prefs import SopranoPrefWin
from gui.trayicon import IconoTray

def main():
	win = Gtk.Window()
	win.connect('destroy', lambda x: Gtk.main_quit())
	win.set_default_size(550, 400)	
	win.show_all()

	if __name__ == '__main__':
		Gtk.main()

main()
