### load/save files, file dialogs and all that
import pickle
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, GLib
import globals
import sprites

def add_filters(dialog):
    filter_wrld = Gtk.FileFilter()
    filter_wrld.set_name("CrazyHat world file .wrld")
    filter_wrld.add_pattern("*.wrld")
    dialog.add_filter(filter_wrld)
    ##
    filter_any = Gtk.FileFilter()
    filter_any.set_name("all files")
    filter_any.add_pattern("*")
    dialog.add_filter(filter_any)

def onTimeout():
    Gtk.main_quit()
    return False
    
def fileChooser(save):
    ## response variables here
    response = None
    fName = None
    ##
    if save:
        dialog = Gtk.FileChooserDialog("File to save the current world:", gtkRootWin,
                                       Gtk.FileChooserAction.SAVE,
                                       (Gtk.STOCK_CANCEL, Gtk.ResponseType.CANCEL,
                                        Gtk.STOCK_OPEN, Gtk.ResponseType.OK))
        dialog.set_do_overwrite_confirmation(True)
        dialog.set_current_name("crazy-world.wrld")
    else:
        dialog = Gtk.FileChooserDialog("World to load:", gtkRootWin,
                                       Gtk.FileChooserAction.OPEN,
            (Gtk.STOCK_CANCEL, Gtk.ResponseType.CANCEL,
            Gtk.STOCK_OPEN, Gtk.ResponseType.OK))
    add_filters(dialog)
    dialog.connect("destroy", Gtk.main_quit)
    ##
    response = dialog.run()
    fName = dialog.get_filename()
    dialog.destroy()
    ##
    GLib.timeout_add(100, onTimeout)
    Gtk.main()
    return response, fName

def loadWorld():
    response, fName = fileChooser(False)
    if response == Gtk.ResponseType.OK:
        file = open(fName, "rb")
        ##
        world = pickle.load(file)
        ##
        stateDict = pickle.load(file)
        gameState = globals.GameState()
        gameState.undictify(stateDict)
        ##
        crazyHat = sprites.CrazyHat(gameState.home)
        try:
            CHDict = pickle.load(file)
            crazyHat.undictify(CHDict)
        except:
            print("cannot read Crazy Hat data")
        ##
        file.close()
        return world, gameState, crazyHat
    else:
        # cancel pressed
        return None
        
def saveWorld(world, gameState, crazyHat):
    """
    worlds: should contain terrain and such
    gameState: points and such
    """
    response, fName = fileChooser(True)
    if response == Gtk.ResponseType.OK:
        file = open(fName, "wb")
        pickler = pickle.Pickler(file)
        pickler.dump(world)
        pickler.dump(gameState.dictify())
        # save as dict for compatibility
        pickler.dump(crazyHat.dictify())
        file.close()

## Global window
gtkRootWin = Gtk.Window(title="File chooser GTK parent")
gtkRootWin.connect("destroy", Gtk.main_quit)
gtkRootWin.hide()
