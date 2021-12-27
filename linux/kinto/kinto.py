# -*- coding: utf-8 -*-
# autostart = true

import re
from xkeysnail.transform import *

# Use the following for testing terminal keymaps
# terminals = [ "", ... ]
# xbindkeys -mk
terminals = [
    "alacritty",
    "deepin-terminal",
    "eterm",
    "gnome-terminal",
    "guake",
    "hyper",
    "io.elementary.terminal",
    "kinto-gui.py",
    "kitty",
    "konsole",
    "lxterminal",
    "mate-terminal",
    "qterminal",
    "st",
    "sakura",
    "station",
    "terminator",
    "termite",
    "tilda",
    "tilix",
    "urxvt",
    "xfce4-terminal",
    "xterm",
]
terminals = [term.casefold() for term in terminals]
termStr = "|".join(str('^'+x+'$') for x in terminals)

mscodes = ["code","vscodium"]
codeStr = "|".join(str('^'+x+'$') for x in mscodes)

# Add remote desktop clients & VM software here
# Ideally we'd only exclude the client window,
# but that may not be easily done.
remotes = [
    "Gnome-boxes",
    "org.remmina.Remmina",
    "remmina",
    "qemu-system-.*",
    "Virt-manager",
    "VirtualBox",
    "VirtualBox Machine",
    "xfreerdp",
]
remotes = [client.casefold() for client in remotes]

# Add remote desktop clients & VMs for no remapping
terminals.extend(remotes)
mscodes.extend(remotes)

# Use for browser specific hotkeys
browsers = [
    "Chromium",
    "Chromium-browser",
    "Discord",
    "Epiphany",
    "Firefox",
    "Firefox Developer Edition",
    "Waterfox",
    "Google-chrome",
    "microsoft-edge",
    "microsoft-edge-dev",
]
browsers = [browser.casefold() for browser in browsers]
browserStr = "|".join(str('^'+x+'$') for x in browsers)

chromes = [
    "Chromium",
    "Chromium-browser",
    "Google-chrome",
    "microsoft-edge",
    "microsoft-edge-dev",
]
chromes = [chrome.casefold() for chrome in chromes]
chromeStr = "|".join(str('^'+x+'$') for x in chromes)

def CK(exp):
    "Remaps to colemak"
    combo_key = K(exp)
    colemak_key_to_keyboard_key = {
        Key.MINUS       :Key.MINUS,
        Key.EQUAL       :Key.EQUAL,
        Key.Q           :Key.Q,
        Key.W           :Key.W,
        Key.F           :Key.E,
        Key.P           :Key.R,
        Key.G           :Key.T,
        Key.J           :Key.Y,
        Key.L           :Key.U,
        Key.U           :Key.I,
        Key.Y           :Key.O,
        Key.SEMICOLON   :Key.P,
        Key.LEFT_BRACE  :Key.LEFT_BRACE,
        Key.RIGHT_BRACE :Key.RIGHT_BRACE,
        Key.BACKSLASH   :Key.BACKSLASH,
        Key.A           :Key.A,
        Key.R           :Key.S,
        Key.S           :Key.D,
        Key.T           :Key.F,
        Key.D           :Key.G,
        Key.H           :Key.H,
        Key.N           :Key.J,
        Key.E           :Key.K,
        Key.I           :Key.L,
        Key.O           :Key.SEMICOLON,
        Key.APOSTROPHE  :Key.APOSTROPHE,
        Key.Z           :Key.Z,
        Key.X           :Key.X,
        Key.C           :Key.C,
        Key.V           :Key.V,
        Key.B           :Key.B,
        Key.K           :Key.N,
        Key.M           :Key.M,
        Key.COMMA       :Key.COMMA,
        Key.DOT         :Key.DOT,
        Key.SLASH       :Key.SLASH,
    }
    
    # qwerty_to_colemak_mapping = {v:k for k, v in colemak_to_qwerty_mapping.items()}

    if combo_key.key in colemak_key_to_keyboard_key:
        combo_key.key = colemak_key_to_keyboard_key[combo_key.key]
    return combo_key

# edges = ["microsoft-edge-dev","microsoft-edge"]
# edges = [edge.casefold() for edge in edges]
# edgeStr = "|".join(str('^'+x+'$') for x in edges)

define_multipurpose_modmap(
    # {Key.ENTER: [Key.ENTER, Key.RIGHT_CTRL]   # Enter2Cmd
    # {Key.CAPSLOCK: [Key.RIGHT_CTRL]}  # Caps2Esc
    # {Key.LEFT_META: [Key.ESC, Key.RIGHT_CTRL] # Caps2Esc - Chromebook
    {}
)

# Fix for avoiding modmapping when using Synergy keyboard/mouse sharing.
# Synergy doesn't set a wm_class, so this may cause issues with other
# applications that also don't set the wm_class.
# Enable only if you use Synergy.
# define_conditional_modmap(lambda wm_class: wm_class == '', {})

# [Global modemap] Change modifier keys as in xmodmap
define_conditional_modmap(lambda wm_class: wm_class.casefold() not in terminals,{

    Key.CAPSLOCK: Key.RIGHT_CTRL,   # Caps2Cmd
    # Key.LEFT_META: Key.RIGHT_CTRL,  # Caps2Cmd - Chromebook

    # - IBM
    # Key.LEFT_ALT: Key.RIGHT_CTRL,   # IBM
    # Key.LEFT_CTRL: Key.LEFT_ALT,    # IBM
    # Key.CAPSLOCK: Key.LEFT_META,    # IBM
    # Key.RIGHT_ALT: Key.RIGHT_CTRL,  # IBM - Multi-language (Remove)
    # Key.RIGHT_CTRL: Key.RIGHT_ALT,  # IBM - Multi-language (Remove)

    # - Chromebook
    # Key.LEFT_ALT: Key.RIGHT_CTRL,   # Chromebook
    # Key.LEFT_CTRL: Key.LEFT_ALT,    # Chromebook
    # Key.RIGHT_ALT: Key.RIGHT_CTRL,  # Chromebook - Multi-language (Remove)
    # Key.RIGHT_CTRL: Key.RIGHT_ALT,  # Chromebook - Multi-language (Remove)

    # - Default Mac/Win
    # - Default Win
    # Key.LEFT_ALT: Key.RIGHT_CTRL,   # WinMac
    # Key.LEFT_META: Key.LEFT_ALT,    # WinMac
    # Key.LEFT_CTRL: Key.LEFT_META,   # WinMac
    # Key.RIGHT_ALT: Key.RIGHT_CTRL,  # WinMac - Multi-language (Remove)
    # Key.RIGHT_META: Key.RIGHT_ALT,  # WinMac - Multi-language (Remove)
    # Key.RIGHT_CTRL: Key.RIGHT_META, # WinMac - Multi-language (Remove)

    # - Mac Only
    Key.LEFT_META: Key.RIGHT_CTRL,  # Mac
    Key.LEFT_CTRL: Key.LEFT_META,   # Mac
    Key.RIGHT_META: Key.RIGHT_CTRL, # Mac - Multi-language (Remove)
    Key.RIGHT_CTRL: Key.RIGHT_META, # Mac - Multi-language (Remove)
})

# [Conditional modmap] Change modifier keys in certain applications
define_conditional_modmap(re.compile(termStr, re.IGNORECASE), {
    # - IBM
    # Key.LEFT_ALT: Key.RIGHT_CTRL,     # IBM
    # # Left Ctrl Stays Left Ctrl
    # Key.CAPSLOCK: Key.LEFT_ALT,       # IBM
    # Key.RIGHT_ALT: Key.RIGHT_CTRL,    # IBM - Multi-language (Remove)
    # Key.RIGHT_CTRL: Key.RIGHT_ALT,    # IBM
    # # Right Meta does not exist on chromebooks

    # Key.RIGHT_ALT: Key.RIGHT_CTRL,  # IBM - Multi-language (Remove)
    # Key.RIGHT_CTRL: Key.RIGHT_ALT,  # IBM - Multi-language (Remove)

    # - Chromebook
    # Key.LEFT_ALT: Key.RIGHT_CTRL,     # Chromebook
    # # Left Ctrl Stays Left Ctrl
    # Key.LEFT_META: Key.LEFT_ALT,      # Chromebook
    # Key.RIGHT_ALT: Key.RIGHT_CTRL,    # Chromebook - Multi-language (Remove)
    # Key.RIGHT_CTRL: Key.RIGHT_ALT,    # Chromebook
    # # Right Meta does not exist on chromebooks

    # - Default Mac/Win
    # - Default Win
    # Key.LEFT_ALT: Key.RIGHT_CTRL,   # WinMac
    # Key.LEFT_META: Key.LEFT_ALT,    # WinMac
    # Key.LEFT_CTRL: Key.LEFT_CTRL,   # WinMac
    # Key.RIGHT_ALT: Key.RIGHT_CTRL,  # WinMac - Multi-language (Remove)
    # Key.RIGHT_META: Key.RIGHT_ALT,  # WinMac - Multi-language (Remove)
    # Key.RIGHT_CTRL: Key.LEFT_CTRL,  # WinMac - Multi-language (Remove)

    # - Mac Only
    Key.LEFT_META: Key.RIGHT_CTRL,  # Mac
    # # Left Ctrl Stays Left Ctrl
    Key.CAPSLOCK: Key.LEFT_CTRL,   # Caps2Cmd
    Key.RIGHT_META: Key.RIGHT_CTRL, # Mac - Multi-language (Remove)
    Key.RIGHT_CTRL: Key.LEFT_CTRL,  # Mac - Multi-language (Remove)
})

# Keybindings for IntelliJ
define_keymap(re.compile("^jetbrains-(?!.*toolbox).*$", re.IGNORECASE),{
    # General
    CK("C-Key_0"): CK("M-Key_0"),                 # Open corresponding tool window
    CK("C-Key_1"): CK("M-Key_1"),                 # Open corresponding tool window
    CK("C-Key_2"): CK("M-Key_2"),                 # Open corresponding tool window
    CK("C-Key_3"): CK("M-Key_3"),                 # Open corresponding tool window
    CK("C-Key_4"): CK("M-Key_4"),                 # Open corresponding tool window
    CK("C-Key_5"): CK("M-Key_5"),                 # Open corresponding tool window
    CK("C-Key_6"): CK("M-Key_6"),                 # Open corresponding tool window
    CK("C-Key_7"): CK("M-Key_7"),                 # Open corresponding tool window
    CK("C-Key_8"): CK("M-Key_8"),                 # Open corresponding tool window
    CK("C-Key_9"): CK("M-Key_9"),                 # Open corresponding tool window
    CK("Super-Grave"): CK("C-Grave"),             # Quick switch current scheme
    CK("C-Comma"): CK("C-M-s"),                   # Open Settings dialog
    CK("C-Semicolon"): CK("C-M-Shift-s"),         # Open Project Structure dialog
    # Debugging
    CK("C-M-r"): CK("F9"),                        # Resume program
    # Search/Replace
    CK("C-g"): CK("F3"),                          # Find next
    CK("C-Shift-F3"): CK("Shift-F3"),             # Find previous
    CK("Super-g"): CK("M-j"),                     # Select next occurrence
    CK("C-Super-g"): CK("C-M-Shift-j"),           # Select all occurrences
    CK("Super-Shift-g"): CK("M-Shift-j"),         # Unselect occurrence
    # Editing
    CK("Super-Space"): CK("LC-Space"),            # Basic code completion
    CK("Super-Shift-Space"): CK("LC-Shift-Space"),# Smart code completion
    CK("Super-j"): CK("C-q"),                     # Quick documentation lookup
    CK("C-n"): CK("M-Insert"),                    # Generate code...
    CK("Super-o"): CK("C-o"),                     # Override methods
    CK("Super-i"): CK("C-i"),                     # Implement methods
    CK("M-Up"): CK("C-w"),                        # Extend selection
    CK("M-Down"): CK("C-Shift-w"),                # Shrink selection
    CK("Super-Shift-q"): CK("M-q"),               # Context info
    CK("Super-M-o"): CK("C-M-o"),                 # Optimize imports
    CK("Super-M-i"): CK("C-M-i"),                 # Auto-indent line(s)
    CK("C-Backspace"): CK("C-y"),                 # Delete line at caret
    CK("Super-Shift-j"): CK("C-Shift-j"),         # Smart line join
    CK("M-Delete"): CK("C-Delete"),               # Delete to word end
    CK("M-Backspace"): CK("C-Backspace"),         # Delete to word start
    CK("C-Shift-Equal"): CK("C-KPPLUS"),          # Expand code block
    CK("C-Minus"): CK("C-KPMINUS"),               # Collapse code block
    CK("C-Shift-Equal"): CK("C-Shift-KPPLUS"),    # Expand all
    CK("C-Shift-Minus"): CK("C-Shift-KPMINUS"),   # Collapse all
    CK("C-w"): CK("C-F4"),                        # Close active editor tab
    # Refactoring
    CK("C-Delete"): CK("M-Delete"),               # Safe Delete
    CK("C-T"): CK("C-M-Shift-t"),                 # Refactor this
    # Navigation
    CK("C-o"): CK("C-n"),                         # Go to class
    CK("C-Shift-o"): CK("C-Shift-n"),             # Go to file
    CK("C-M-o"): CK("C-M-Shift-n"),               # Go to symbol
    CK("Super-Right"): CK("M-Right"),             # Go to next editor tab
    CK("Super-Left"): CK("M-Left"),               # Go to previous editor tab
    CK("C-l"): CK("C-g"),                         # Go to line
    CK("M-Space"): CK("C-Shift-i"),               # Open quick definition lookup
    CK("C-Y"): CK("C-Shift-i"),                   # Open quick definition lookup
    CK("Super-Shift-b"): CK("C-Shift-b"),         # Go to type declaration
    CK("Super-Up"): CK("M-Up"),                   # Go to previous
    CK("Super-Down"): CK("M-Down"),               # Go to next method
    CK("Super-h"): CK("C-h"),                     # Type hierarchy
    CK("Super-M-h"): CK("C-M-h"),                 # Call hierarchy
    CK("C-Down"): CK("C-Enter"),                  # Edit source/View source
    CK("M-Home"): CK("M-Home"),                   # Show navigation bar
    CK("F2"): CK("F11"),                          # Toggle bookmark
    CK("Super-F3"): CK("C-F11"),                  # Toggle bookmark with mnemonic
    CK("Super-Key_0"): CK("C-Key_0"),             # Go to numbered bookmark
    CK("Super-Key_1"): CK("C-Key_1"),             # Go to numbered bookmark
    CK("Super-Key_2"): CK("C-Key_2"),             # Go to numbered bookmark
    CK("Super-Key_3"): CK("C-Key_3"),             # Go to numbered bookmark
    CK("Super-Key_4"): CK("C-Key_4"),             # Go to numbered bookmark
    CK("Super-Key_5"): CK("C-Key_5"),             # Go to numbered bookmark
    CK("Super-Key_6"): CK("C-Key_6"),             # Go to numbered bookmark
    CK("Super-Key_7"): CK("C-Key_7"),             # Go to numbered bookmark
    CK("Super-Key_8"): CK("C-Key_8"),             # Go to numbered bookmark
    CK("Super-Key_9"): CK("C-Key_9"),             # Go to numbered bookmark
    CK("C-F3"): CK("Shift-F11"),                  # Show bookmarks
    # Compile and Run
    CK("Super-M-r"): CK("M-Shift-F10"),           # Select configuration and run
    CK("Super-M-d"): CK("M-Shift-F9"),            # Select configuration and debug
    CK("Super-r"): CK("Shift-F10"),               # Run
    CK("Super-d"): CK("Shift-F9"),                # Debug
    CK("Super-Shift-r"): CK("C-Shift-F10"),       # Run context configuration from editor
    CK("Super-Shift-d"): CK("C-Shift-F9"),        # Debug context configuration from editor
    # VCS/Local History
    CK("Super-v"): CK("M-Grave"),                 # VCS quick popup
    CK("Super-c"): CK("LC-c"),                    # Sigints - interrupt
},"Jetbrains")

##############################################
### START OF FILE MANAGER GROUP OF KEYMAPS ###
##############################################

# Keybindings overrides for Caja
# (overrides some bindings from general file manager code block below)
define_keymap(re.compile("caja", re.IGNORECASE),{
    # CK("RC-Super-o"): CK("RC-Shift-Enter"),       # Open in new tab
    CK("RC-Super-o"): CK("RC-Shift-W"),           # Open in new window
},"Overrides for Caja - Finder")

# Keybindings overrides for DDE (Deepin) File Manager
# (overrides some bindings from general file manager code block below)
define_keymap(re.compile("dde-file-manager", re.IGNORECASE),{
    CK("RC-i"): CK("RC-i"),                   # File properties dialog (Get Info)
    CK("RC-comma"): None,                    # Disable preferences shortcut (no shortcut available)
    CK("RC-Up"): CK("RC-Up"),                 # Go Up dir
},"Overrides for DDE File Manager - Finder")

# Keybindings overrides for Dolphin
# (overrides some bindings from general file manager code block below)
define_keymap(re.compile("dolphin", re.IGNORECASE),{
    ##########################################################################################
    ### "Open in new window" requires manually setting custom shortcut of Ctrl+Shift+o
    ### in Dolphin's keyboard shortcuts. There is no default shortcut set for this function.
    ##########################################################################################
    ### "Open in new tab" requires manually setting custom shortcut of Ctrl+Shift+o in
    ### Dolphin's keyboard shortcuts. There is no default shortcut set for this function.
    ##########################################################################################
    CK("RC-Super-o"): CK("RC-Shift-o"),           # Open in new window (or new tab, user's choice, see above)
    CK("RC-Shift-N"): CK("F10"),                  # Create new folder
    CK("RC-comma"): CK("RC-Shift-comma"),         # Open preferences dialog
},"Overrides for Dolphin - Finder")

# Keybindings overrides for elementary OS Files
# (overrides some bindings from general file manager code block below)
define_keymap(re.compile("io.elementary.files", re.IGNORECASE),{
    # CK("RC-Super-o"): CK("Shift-Enter"),          # Open folder in new tab
    CK("RC-Comma"): None,                        # Disable preferences shortcut since none available
},"Overrides for Pantheon - Finder")

# Keybindings overrides for Nautilus
# (overrides some bindings from general file manager code block below)
define_keymap(re.compile("org.gnome.nautilus|nautilus", re.IGNORECASE),{
    CK("RC-Super-o"): CK("Shift-Enter"),          # Open in new window
    # CK("RC-Super-o"): CK("RC-Enter"),             # Open in new tab
    CK("RC-comma"): CK("RC-comma"),               # Overrides "Open preferences dialog" shortcut below
},"Overrides for Nautilus - Finder")

# Keybindings overrides for PCManFM and PCManFM-Qt
# (overrides some bindings from general file manager code block below)
define_keymap(re.compile("pcmanfm|pcmanfm-qt", re.IGNORECASE),{
    CK("RC-Backspace"): [CK("Delete"),CK("Enter")],    # Move to Trash (delete, bypass dialog)
},"Overrides for PCManFM - Finder")

# Keybindings overrides for SpaceFM
# (overrides some bindings from general file manager code block below)
define_keymap(re.compile("spacefm", re.IGNORECASE),{
    CK("RC-Page_Up"): CK("C-Shift-Tab"),              # Go to prior tab
    CK("RC-Page_Down"): CK("C-Tab"),                  # Go to next tab
    CK("RC-Shift-Left_Brace"): CK("C-Shift-Tab"),     # Go to prior tab
    CK("RC-Shift-Right_Brace"): CK("C-Tab"),          # Go to next tab
    CK("RC-Shift-N"): [CK("RC-F")],	                # Create new folder is Ctrl+F by default
    CK("RC-Backspace"): [CK("Delete"),CK("Enter")],	# Move to Trash (delete, bypass dialog)
    CK("RC-comma"): [CK("M-V"),CK("p")],               # Overrides "Open preferences dialog" shortcut below
    # This shortcut ^^^^^^^^^^^^^^^ is not fully working in SpaceFM. Opens "View" menu but not Preferences.
    # SpaceFM seems to be doing some nasty binding that blocks things like Alt+Tab while the menu is open.
},"Overrides for SpaceFM - Finder")

# Keybindings overrides for Thunar
# (overrides some bindings from general file manager code block below)
define_keymap(re.compile("thunar", re.IGNORECASE),{
    CK("RC-Super-o"): CK("RC-Shift-P"),          # Open in new tab
    CK("RC-comma"): [CK("M-E"),CK("E")],          # Overrides "Open preferences dialog" shortcut below
},"Overrides for Thunar - Finder")

filemanagers = [
    "caja",
    "dde-file-manager",
    "dolphin",
    "io.elementary.files",
    "nautilus",
    "nemo",
    "org.gnome.nautilus",
    "pcmanfm",
    "pcmanfm-qt",
    "spacefm",
    "thunar",
]
filemanagers = [filemanager.casefold() for filemanager in filemanagers]
filemanagerStr = "|".join(str('^'+x+'$') for x in filemanagers)

# Currently supported Linux file managers (file browsers):
#
# Caja File Browser (MATE file manager, fork of Nautilus)
# DDE File Manager (Deepin Linux file manager)
# Dolphin (KDE file manager)
# Nautilus (GNOME file manager, may be named "Files")
# Nemo (Cinnamon file manager, fork of Nautilus, may be named "Files")
# Pantheon Files (elementary OS file manager, may be named "Files")
# PCManFM (LXDE file manager)
# PCManFM-Qt (LXQt file manager)
# SpaceFM (Fork of PCManFM file manager)
# Thunar File Manager (Xfce file manager)
#
# Keybindings for general Linux file managers group:
define_keymap(re.compile(filemanagerStr, re.IGNORECASE),{
    ###########################################################################################################
    ###  Show Properties (Get Info) | Open Settings/Preferences | Show/Hide hidden files                    ###
    ###########################################################################################################
    CK("RC-i"): CK("M-Enter"),                # File properties dialog (Get Info)
    CK("RC-comma"): [CK("M-E"),CK("N")],       # Open preferences dialog
    CK("RC-Shift-dot"): CK("RC-H"),           # Show/hide hidden files ("dot" files)
    ###########################################################################################################
    ###  Navigation                                                                                         ###
    ###########################################################################################################
    CK("RC-Left"): CK("M-Left"),              # Go Back
    CK("RC-Right"): CK("M-Right"),            # Go Forward
    CK("RC-Up"): CK("M-Up"),                  # Go Up dir
    # CK("RC-Down"): CK("M-Down"),              # Go Down dir (only works on folders) [not universal]
    # CK("RC-Down"): CK("RC-O"),                # Go Down dir (open folder/file) [not universal]
    CK("RC-Down"): CK("Enter"),               # Go Down dir (open folder/file) [universal]
    CK("RC-Shift-Left_Brace"): CK("C-Page_Up"),       # Go to prior tab
    CK("RC-Shift-Right_Brace"): CK("C-Page_Down"),    # Go to next tab
    ###########################################################################################################
    ###  Open in New Window | Move to Trash | Duplicate file/folder                                         ###
    ###########################################################################################################
    CK("RC-Super-o"): CK("RC-Shift-o"),       # Open in new window (or tab, depends on FM setup) [not universal]
    CK("RC-Backspace"): CK("Delete"),	        # Move to Trash (delete)
    CK("RC-D"): [CK("RC-C"),CK("RC-V")],       # Mimic Finder's Duplicate command (Copy, then Paste)
    ###########################################################################################################
    ###  To enable renaming files with the Enter key, uncomment the two keymapping lines just below this.   ###
    ###  Use Ctrl+Shift+Enter to escape or activate text fields such as "[F]ind" and "[L]ocation" fields.   ###
    ###########################################################################################################
    # CK("Enter"): CK("F2"),                    # Rename with Enter key
    # CK("RC-Shift-Enter"): CK("Enter"),        # Remap alternative "Enter" key to easily activate/exit text fields
},"File Managers - Finder")

############################################
### END OF FILE MANAGER GROUP OF KEYMAPS ###
############################################

# Keybindings for General Web Browsers
define_keymap(re.compile(browserStr, re.IGNORECASE),{
    CK("RC-Q"): CK("RC-Q"),           # Close all browsers Instances
    CK("M-RC-I"): CK("RC-Shift-I"),   # Dev tools
    CK("M-RC-J"): CK("RC-Shift-J"),   # Dev tools
    CK("RC-Key_1"): CK("M-Key_1"),    # Jump to Tab #1-#8
    CK("RC-Key_2"): CK("M-Key_2"),
    CK("RC-Key_3"): CK("M-Key_3"),
    CK("RC-Key_4"): CK("M-Key_4"),
    CK("RC-Key_5"): CK("M-Key_5"),
    CK("RC-Key_6"): CK("M-Key_6"),
    CK("RC-Key_7"): CK("M-Key_7"),
    CK("RC-Key_8"): CK("M-Key_8"),
    CK("RC-Key_9"): CK("M-Key_9"),    # Jump to last tab
    # Enable Cmd+Shift+Braces for tab navigation
    CK("RC-Shift-Left_Brace"):   CK("C-Page_Up"),     # Go to prior tab
    CK("RC-Shift-Right_Brace"):  CK("C-Page_Down"),   # Go to next tab
    # Enable Cmd+Option+Left/Right for tab navigation
    CK("RC-M-Left"):             CK("C-Page_Up"),     # Go to prior tab
    CK("RC-M-Right"):            CK("C-Page_Down"),   # Go to next tab
    # Enable Ctrl+PgUp/PgDn for tab navigation
    CK("Super-Page_Up"):         CK("C-Page_Up"),     # Go to prior tab
    CK("Super-Page_Down"):       CK("C-Page_Down"),   # Go to next tab
    # Use Cmd+Braces keys for tab navigation instead of page navigation 
    # CK("C-Left_Brace"): CK("C-Page_Up"),
    # CK("C-Right_Brace"): CK("C-Page_Down"),
}, "General Web Browsers")


# Open preferences in browsers
define_keymap(re.compile("Firefox", re.IGNORECASE),{
    CK("C-comma"): [
        CK("C-T"),CK("a"),CK("b"),CK("o"),CK("u"),CK("t"),
        CK("Shift-SEMICOLON"),CK("p"),CK("r"),CK("e"),CK("f"),
        CK("e"),CK("r"),CK("e"),CK("n"),CK("c"),CK("e"),CK("s"),CK("Enter")
    ],
    CK("RC-Shift-N"):    CK("RC-Shift-P"),        # Open private window with Ctrl+Shift+N like other browsers
})
define_keymap(re.compile(chromeStr, re.IGNORECASE),{
    CK("C-comma"): [CK("M-e"), CK("s"),CK("Enter")],
}, "Browsers")
# Opera C-F12

# Note: terminals extends to remotes as well
define_keymap(lambda wm_class: wm_class.casefold() not in terminals,{
    CK("RC-Dot"): CK("Esc"),                        # Mimic macOS Cmd+dot = Escape key (not in terminals)
})

# None referenced here originally
# - but remote clients and VM software ought to be set here
# These are the typical remaps for ALL GUI based apps
define_keymap(lambda wm_class: wm_class.casefold() not in remotes,{
    CK("RC-Space"): CK("Alt-F1"),                   # Default SL - Launch Application Menu (gnome/kde)
    CK("RC-F3"):CK("Super-d"),                      # Default SL - Show Desktop (gnome/kde,eos)
    CK("RC-Super-f"):CK("M-F10"),                   # Default SL - Maximize app (gnome/kde)
    # CK("RC-Super-f"): CK("Super-Page_Up"),          # SL - Toggle maximized window state (kde_neon)
    # CK("Super-Right"):CK("C-M-Right"),              # Default SL - Change workspace (budgie)
    # CK("Super-Left"):CK("C-M-Left"),                # Default SL - Change workspace (budgie)
    CK("RC-Q"): CK("M-F4"),                         # Default SL - not-popos
    CK("RC-H"):CK("Super-h"),                       # Default SL - Minimize app (gnome/budgie/popos/fedora)
    CK("M-Tab"): pass_through_key,                 # Default - Cmd Tab - App Switching Default
    CK("RC-Tab"): CK("M-Tab"),                      # Default - Cmd Tab - App Switching Default
    CK("RC-Shift-Tab"): CK("M-Shift-Tab"),          # Default - Cmd Tab - App Switching Default
    CK("RC-Grave"): CK("M-Grave"),                  # Default not-xfce4 - Cmd ` - Same App Switching
    CK("RC-Shift-Grave"): CK("M-Shift-Grave"),      # Default not-xfce4 - Cmd ` - Same App Switching
    # CK("RC-Grave"): CK("Super-Tab"),                # xfce4 Switch within app group
    # CK("RC-Shift-Grave"): CK("Super-Shift-Tab"),    # xfce4 Switch within app group
    # CK("Super-Right"):CK("Super-Page_Up"),          # SL - Change workspace (ubuntu/fedora)
    # CK("Super-Left"):CK("Super-Page_Down"),         # SL - Change workspace (ubuntu/fedora)
    # CK("Super-Right"):CK("Super-C-Up"),             # SL - Change workspace (popos)
    # CK("Super-Left"):CK("Super-C-Down"),            # SL - Change workspace (popos)
    # CK("RC-Q"):CK("Super-q"),                       # SL - Close Apps (popos)
    # CK("RC-Space"): CK("Super-Space"),              # SL - Launch Application Menu (eos)
    # CK("RC-H"): CK("Super-Page_Down"),              # SL - Minimize app (kde_neon)
                                                  # SL - Default SL - Change workspace (kde_neon)
    # CK("RC-Space"): CK("LC-Esc"),                   # SL- Launch Application Menu xfce4
    # CK("RC-F3"):CK("C-M-d"),                        # SL- Show Desktop xfce4
    # CK("RC-LC-f"):CK("Super-Up"),                   # SL- Maximize app eos
    # CK("RC-LC-f"):CK("Super-PAGE_UP"),              # SL- Maximize app manjaro
    # Basic App hotkey functions
    # CK("RC-H"):CK("M-F9"),                          # SL - Minimize app xfce4
    # CK("RC-LC-f"):CK("Super-PAGE_DOWN"),            # SL - Minimize app manjaro
    # In-App Tab switching
    # CK("M-Tab"): CK("C-Tab"),                       # Chromebook/IBM - In-App Tab switching
    # CK("M-Shift-Tab"): CK("C-Shift-Tab"),           # Chromebook/IBM - In-App Tab switching
    # CK("M-Grave") : CK("C-Shift-Tab"),              # Chromebook/IBM - In-App Tab switching
    CK("Super-Tab"): CK("LC-Tab"),                  # Default not-chromebook
    CK("Super-Shift-Tab"): CK("LC-Shift-Tab"),      # Default not-chromebook

    # Fn to Alt style remaps
    # CK("RM-Enter"): CK("insert"),                   # Insert

    # emacs style
    CK("Super-a"): CK("Home"),                      # Beginning of Line
    CK("Super-e"): CK("End"),                       # End of Line
    CK("Super-b"): CK("Left"),
    CK("Super-f"): CK("Right"),
    CK("Super-n"): CK("Down"),
    CK("Super-p"): CK("Up"),
    CK("Super-k"): [CK("Shift-End"), CK("Backspace")],
    CK("Super-d"): CK("Delete"),

    # CK("M-RC-Space"): CK(""),                       # Open Finder - Placeholder

    # Wordwise
    CK("RC-Left"): CK("Home"),                      # Beginning of Line
    CK("RC-Shift-Left"): CK("Shift-Home"),          # Select all to Beginning of Line
    CK("RC-Right"): CK("End"),                      # End of Line
    CK("RC-Shift-Right"): CK("Shift-End"),          # Select all to End of Line
    # CK("RC-Left"): CK("C-LEFT_BRACE"),              # Firefox-nw - Back
    # CK("RC-Right"): CK("C-RIGHT_BRACE"),            # Firefox-nw - Forward
    # CK("RC-Left"): CK("M-LEFT"),                    # Chrome-nw - Back
    # CK("RC-Right"): CK("M-RIGHT"),                  # Chrome-nw - Forward
    CK("RC-Up"): CK("C-Home"),                      # Beginning of File
    CK("RC-Shift-Up"): CK("C-Shift-Home"),          # Select all to Beginning of File
    CK("RC-Down"): CK("C-End"),                     # End of File
    CK("RC-Shift-Down"): CK("C-Shift-End"),         # Select all to End of File
    # CK("RM-Backspace"): CK("Delete"),               # Chromebook/IBM - Delete
    CK("Super-Backspace"): CK("C-Backspace"),       # Delete Left Word of Cursor
    CK("Super-Delete"): CK("C-Delete"),             # Delete Right Word of Cursor
    # CK("LM-Backspace"): CK("C-Backspace"),          # Chromebook/IBM - Delete Left Word of Cursor
    CK("M-Backspace"): CK("C-Backspace"),           # Default not-chromebook
    CK("RC-Backspace"): CK("C-Shift-Backspace"),    # Delete Entire Line Left of Cursor
    CK("Alt-Delete"): CK("C-Delete"),               # Delete Right Word of Cursor
    # CK(""): pass_through_key,                      # cancel
    # CK(""): CK(""),                                 #
}, "General GUI")

define_keymap(lambda wm_class: wm_class.casefold() not in mscodes,{
    # Wordwise remaining - for Everything but VS Code
    CK("M-Left"): CK("C-Left"),               # Left of Word
    CK("M-Shift-Left"): CK("C-Shift-Left"),   # Select Left of Word
    CK("M-Right"): CK("C-Right"),             # Right of Word
    CK("M-Shift-Right"): CK("C-Shift-Right"), # Select Right of Word
    CK("M-Shift-g"): CK("C-Shift-g"),         # View source control
    # ** VS Code fix **
    #   Electron issue precludes normal keybinding fix.
    #   Alt menu auto-focus/toggle gets in the way.
    #
    #   refer to ./xkeysnail-config/vscode_keybindings.json
    # **
    #
    # ** Firefox fix **
    #   User will need to set "ui.key.menuAccessKeyFocuses"
    #   under about:config to false.
    #
    #   https://superuser.com/questions/770301/pentadactyl-how-to-disable-menu-bar-toggle-by-alt
    # **
    #
}, "Wordwise - not vscode")

# Keybindings for VS Code
define_keymap(re.compile(codeStr, re.IGNORECASE),{
    CK("Super-Space"): CK("LC-Space"),                        # Basic code completion
    # Wordwise remaining - for VS Code
    # Alt-F19 hack fixes Alt menu activation
    CK("M-Left"): [CK("M-F19"),CK("C-Left")],                  # Left of Word
    CK("M-Right"): [CK("M-F19"),CK("C-Right")],                # Right of Word
    CK("M-Shift-Left"): [CK("M-F19"),CK("C-Shift-Left")],      # Select Left of Word
    CK("M-Shift-Right"): [CK("M-F19"),CK("C-Shift-Right")],    # Select Right of Word

    # CK("C-PAGE_DOWN"): pass_through_key,         # cancel next_view
    # CK("C-PAGE_UP"): pass_through_key,           # cancel prev_view
    CK("C-M-Left"): CK("C-PAGE_UP"),              # next_view
    CK("C-M-Right"): CK("C-PAGE_DOWN"),           # prev_view

    # VS Code Shortcuts
    CK("C-g"): pass_through_key,                 # cancel Go to Line...
    CK("Super-g"): CK("C-g"),                     # Go to Line...
    CK("F3"): pass_through_key,                  # cancel Find next
    CK("C-h"): pass_through_key,                 # cancel replace
    CK("C-M-f"): CK("C-h"),                       # replace
    CK("C-Shift-h"): pass_through_key,           # cancel replace_next
    CK("C-M-e"): CK("C-Shift-h"),                 # replace_next
    CK("f3"): pass_through_key,                  # cancel find_next
    CK("C-g"): CK("f3"),                          # find_next
    CK("Shift-f3"): pass_through_key,            # cancel find_prev
    CK("C-Shift-g"): CK("Shift-f3"),              # find_prev
    # CK("Super-c"): CK("LC-c"),                    # Default - Terminal - Sigint
    # CK("Super-x"): CK("LC-x"),                    # Default - Terminal - Exit nano
    # CK("M-c"): CK("LC-c"),                        #  Chromebook/IBM - Terminal - Sigint
    # CK("M-x"): CK("LC-x"),                        #  Chromebook/IBM - Terminal - Exit nano
    # CK("Super-C-g"): CK("C-f2"),                  # Default - Sublime - find_all_under
    # CK("C-M-g"): CK("C-f2"),                      # Chromebook/IBM - Sublime - find_all_under
    # CK("Super-Shift-up"): CK("M-Shift-up"),       # multi-cursor up - Sublime
    # CK("Super-Shift-down"): CK("M-Shift-down"),   # multi-cursor down - Sublime
    # CK(""): pass_through_key,                    # cancel
    # CK(""): CK(""),                               #
}, "Code")

# Keybindings for Sublime Text
define_keymap(re.compile("Sublime_text", re.IGNORECASE),{
    # CK("Super-c"): CK("LC-c"),                    # Default - Terminal - Sigint
    # CK("Super-x"): CK("LC-x"),                    # Default - Terminal - Exit nano
    # CK("M-c"): CK("LC-c"),                        #  Chromebook/IBM - Terminal - Sigint
    # CK("M-x"): CK("LC-x"),                        #  Chromebook/IBM - Terminal - Exit nano
    CK("Super-Space"): CK("C-Space"),             # Basic code completion
    CK("C-Super-up"): CK("M-o"),                  # Switch file
    CK("Super-RC-f"): CK("f11"),                  # toggle_full_screen
    CK("C-M-v"): [CK("C-k"), CK("C-v")],           # paste_from_history
    CK("C-up"): pass_through_key,                # cancel scroll_lines up
    CK("C-M-up"): CK("C-up"),                     # scroll_lines up
    CK("C-down"): pass_through_key,              # cancel scroll_lines down
    CK("C-M-down"): CK("C-down"),                 # scroll_lines down
    CK("Super-Shift-up"): CK("M-Shift-up"),       # multi-cursor up
    CK("Super-Shift-down"): CK("M-Shift-down"),   # multi-cursor down
    CK("C-PAGE_DOWN"): pass_through_key,         # cancel next_view
    CK("C-PAGE_UP"): pass_through_key,           # cancel prev_view
    CK("C-Shift-left_brace"): CK("C-PAGE_DOWN"),  # next_view
    CK("C-Shift-right_brace"): CK("C-PAGE_UP"),   # prev_view
    CK("C-M-right"): CK("C-PAGE_DOWN"),           # next_view
    CK("C-M-left"): CK("C-PAGE_UP"),              # prev_view
    CK("insert"): pass_through_key,              # cancel toggle_overwrite
    CK("C-M-o"): CK("insert"),                    # toggle_overwrite
    CK("M-c"): pass_through_key,                 # cancel toggle_case_sensitive
    CK("C-M-c"): CK("M-c"),                       # toggle_case_sensitive
    CK("C-h"): pass_through_key,                 # cancel replace
    CK("C-M-f"): CK("C-h"),                       # replace
    CK("C-Shift-h"): pass_through_key,           # cancel replace_next
    CK("C-M-e"): CK("C-Shift-h"),                 # replace_next
    CK("f3"): pass_through_key,                  # cancel find_next
    CK("C-g"): CK("f3"),                          # find_next
    CK("Shift-f3"): pass_through_key,            # cancel find_prev
    CK("C-Shift-g"): CK("Shift-f3"),              # find_prev
    CK("C-f3"): pass_through_key,                # cancel find_under
    CK("Super-M-g"): CK("C-f3"),                  # find_under
    CK("C-Shift-f3"): pass_through_key,          # cancel find_under_prev
    CK("Super-M-Shift-g"): CK("C-Shift-f3"),      # find_under_prev
    CK("M-f3"): pass_through_key,                # Default - cancel find_all_under
    # CK("M-Refresh"): pass_through_key,           # Chromebook/IBM - cancel find_all_under
    # CK("M-C-g"): CK("M-Refresh"),                 # Chromebook/IBM - find_all_under
    CK("Super-C-g"): CK("M-f3"),                  # Default - find_all_under
    CK("C-Shift-up"): pass_through_key,          # cancel swap_line_up
    CK("Super-M-up"): CK("C-Shift-up"),           # swap_line_up
    CK("C-Shift-down"): pass_through_key,        # cancel swap_line_down
    CK("Super-M-down"): CK("C-Shift-down"),       # swap_line_down
    CK("C-Pause"): pass_through_key,             # cancel cancel_build
    CK("Super-c"): CK("C-Pause"),                 # cancel_build
    CK("f9"): pass_through_key,                  # cancel sort_lines case_s false
    CK("f5"): CK("f9"),                           # sort_lines case_s false
    CK("Super-f9"): pass_through_key,            # cancel sort_lines case_s true
    CK("Super-f5"): CK("Super-f9"),               # sort_lines case_s true
    CK("M-Shift-Key_1"): pass_through_key,       # cancel set_layout
    CK("C-M-Key_1"): CK("M-Shift-Key_1"),         # set_layout
    CK("M-Shift-Key_2"): pass_through_key,       # cancel set_layout
    CK("C-M-Key_2"): CK("M-Shift-Key_2"),         # set_layout
    CK("M-Shift-Key_3"): pass_through_key,       # cancel set_layout
    CK("C-M-Key_3"): CK("M-Shift-Key_3"),         # set_layout
    CK("M-Shift-Key_4"): pass_through_key,       # cancel set_layout
    CK("C-M-Key_4"): CK("M-Shift-Key_4"),         # set_layout
    CK("M-Shift-Key_8"): pass_through_key,       # cancel set_layout
    CK("C-M-Shift-Key_2"): CK("M-Shift-Key_8"),   # set_layout
    CK("M-Shift-Key_9"): pass_through_key,       # cancel set_layout
    CK("C-M-Shift-Key_3"): CK("M-Shift-Key_9"),   # set_layout
    CK("M-Shift-Key_5"): pass_through_key,       # cancel set_layout
    CK("C-M-Shift-Key_5"): CK("M-Shift-Key_5"),   # set_layout
    # CK(""): pass_through_key,                    # cancel
    # CK(""): CK(""),                               #
}, "Sublime Text")

define_keymap(re.compile("konsole", re.IGNORECASE),{
    # Ctrl Tab - In App Tab Switching
    CK("LC-Tab") : CK("Shift-Right"),
    CK("LC-Shift-Tab") : CK("Shift-Left"),
    CK("LC-Grave") : CK("Shift-Left"),

}, "Konsole tab switching")

define_keymap(re.compile("Io.elementary.terminal|kitty", re.IGNORECASE),{
    # Ctrl Tab - In App Tab Switching
    CK("LC-Tab") : CK("LC-Shift-Right"),
    CK("LC-Shift-Tab") : CK("LC-Shift-Left"),
    CK("LC-Grave") : CK("LC-Shift-Left"),

}, "Elementary Terminal tab switching")

define_keymap(re.compile(termStr, re.IGNORECASE),{
    CK("LC-RC-f"): CK("M-F10"),                       # Toggle window maximized state
    # CK("RC-Grave"): CK("Super-Tab"),                # xfce4 Switch within app group
    # CK("RC-Shift-Grave"): CK("Super-Shift-Tab"),    # xfce4 Switch within app group
    # CK("LC-Right"):CK("C-M-Right"),                 # Default SL - Change workspace (budgie)
    # CK("LC-Left"):CK("C-M-Left"),                   # Default SL - Change workspace (budgie)
    # CK("LC-Left"):CK("C-M-End"),                    # SL - Change workspace xfce4
    # CK("LC-Left"):CK("Super-Left"),                 # SL - Change workspace eos
    # CK("LC-Right"):CK("C-M-Home"),                  # SL - Change workspace xfce4
    # CK("LC-Right"):CK("Super-Right"),               # SL - Change workspace eos
    # CK("LC-Right"):CK("Super-Page_Up"),             # SL - Change workspace (ubuntu/fedora)
    # CK("LC-Left"):CK("Super-Page_Down"),            # SL - Change workspace (ubuntu/fedora)
    # CK("LC-Right"):CK("Super-C-Up"),                # SL - Change workspace (popos)
    # CK("LC-Left"):CK("Super-C-Down"),               # SL - Change workspace (popos)
    # Ctrl Tab - In App Tab Switching
    CK("LC-Tab") : CK("LC-PAGE_DOWN"),
    CK("LC-Shift-Tab") : CK("LC-PAGE_UP"),
    CK("LC-Grave") : CK("LC-PAGE_UP"),
    # CK("M-Tab"): pass_through_key,                 # Default - Cmd Tab - App Switching Default
    # CK("RC-Tab"): CK("M-Tab"),                      # Default - Cmd Tab - App Switching Default
    # CK("RC-Shift-Tab"): CK("M-Shift-Tab"),          # Default - Cmd Tab - App Switching Default
    # Converts Cmd to use Ctrl-Shift
    CK("RC-MINUS"): CK("C-MINUS"),
    CK("RC-EQUAL"): CK("C-Shift-EQUAL"),
    CK("RC-BACKSPACE"): CK("C-Shift-BACKSPACE"),
    CK("RC-W"): CK("C-W"),
    CK("RC-E"): CK("C-Shift-E"),
    CK("RC-R"): CK("C-Shift-R"),
    CK("RC-T"): CK("C-T"),
    CK("RC-Y"): CK("C-Shift-Y"),
    CK("RC-U"): CK("C-Shift-U"),
    CK("RC-I"): CK("C-Shift-I"),
    CK("RC-O"): CK("C-Shift-O"),
    CK("RC-P"): CK("C-Shift-P"),
    CK("RC-LEFT_BRACE"): CK("C-Shift-LEFT_BRACE"),
    CK("RC-RIGHT_BRACE"): CK("C-Shift-RIGHT_BRACE"),
    CK("RC-A"): CK("C-Shift-A"),
    CK("RC-S"): CK("C-Shift-S"),
    CK("RC-D"): CK("C-D"),
    CK("RC-F"): CK("C-Shift-F"),
    CK("RC-G"): CK("C-Shift-G"),
    CK("RC-H"): CK("C-H"),
    CK("RC-J"): CK("C-J"),
    CK("RC-K"): CK("C-K"),
    CK("RC-L"): CK("C-L"),
    CK("RC-SEMICOLON"): CK("C-Shift-SEMICOLON"),
    CK("RC-APOSTROPHE"): CK("C-Shift-APOSTROPHE"),
    CK("RC-GRAVE"): CK("C-Shift-GRAVE"),
    CK("RC-Z"): CK("C-Shift-Z"),
    CK("RC-X"): CK("C-Shift-X"),
    CK("RC-C"): CK("C-Shift-C"),
    CK("RC-V"): CK("C-Shift-V"),
    CK("RC-B"): CK("C-Shift-B"),
    CK("RC-N"): CK("C-Shift-N"),
    CK("RC-M"): CK("C-Shift-M"),
    CK("RC-COMMA"): CK("C-Shift-COMMA"),
    CK("RC-Dot"): CK("LC-c"),
    CK("RC-SLASH"): CK("C-Shift-SLASH"),
    CK("RC-KPASTERISK"): CK("C-Shift-KPASTERISK"),
}, "terminals")




