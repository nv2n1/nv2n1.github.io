---
title: "mupmate(1)"
name: "mupmate"
section: "1"
letter: "m"
url: "/docs/linux/man/1-mupmate/"
---

<h2>NAME</h2>

 

 mupmate - user interface for Mup music publisher

<h2>SYNOPSIS</h2>

 

 mupmate [<i>file</i>]

<h2>DESCRIPTION</h2>

 

 

 You can create a Mup file using any ordinary text editor. On Windows, Notepad is a typical choice; on Linux, editors like vim and emacs are commonly used. But if you prefer to be able to edit, display, and play from a single integrated and more graphical interface, a helper program called &quot;mupmate&quot; is provided. Mupmate is currently supported on Windows, Apple Mac OS-X, and Linux. However, since the source code is available, and it is based on the cross-platform FLTK toolkit, it can probably be made to run on any system supported by FLTK fairly easily. If you prefer to use the Mup program directly rather than via mupmate, you can. The Mupmate program just helps lead you through some of the steps. 

 Once you have installed Mup and Mupmate on Windows, double clicking a .mup file in Windows explorer will run Mupmate on that file. Or, you can run Mupmate by going to the Start menu, and choosing Programs, then Arkkra, and then Mupmate. If you would like an icon on the desktop, you can create one by right clicking the Mupmate choice in the Arkkra menu, choosing &quot;copy&quot;, right clicking somewhere on the desktop, and choosing &quot;paste.&quot; 

 On Linux, you can just type the mupmate command, optionally followed by the name of a Mup input file. Or you can add mupmate to your favorite window manager's menus. 

 On Mac OS-X, you can double-click on the MupMate.app in Finder. You should also be able to double-click any file with a .mup suffix, which should then run Mupmate on that file. For setting paths in the Preferences, several &quot;magic&quot; variables are set automatically, if you have not already set them to something else. $APPL is set to the top of the application directory hierarchy. $RSRC is effectively set to $APPL/MupMate.app/Contents/Resources. $HOME is set to your home directory. $SUPP is set to your applications support folder (which is typically $HOME/Library/Application Support). $DOCS is set to your document folder (which is typically $HOME/Documents). 

 Mupmate provides five top level menus: File, Edit, Run, Config, and Help. The File menu provides commands for opening new files and saving the file you are working on, as well as exit the program. The Edit menu provides the kinds of things you would expect in a editor: commands to find a pattern, or find and replace; to select text; to copy, cut, and paste; to go to a specific line; and to undo the previous operation, if you make a mistake or change you mind. The Run menu lets you set runtime options, and then run the Mup program on your input in various ways. You can either just generate a PostScript or MIDI file, or display the PostScript or play the MIDI. The Config menu lets you specify what application program you want to use to view PostScript files and which you want to use to play MIDI files, and well as specify locations for other Mup files. Mupmate will try to find reasonable default values, but you may want to check that they are what you want, and tweak them if they aren't. For paths, you can include environment variables to be expanded, by giving their name preceded by a dollar sign. A tilde by itself will be expanded to your home directory, whereas a tilde followed by the name of a user will be expanded to that user's home directory. The Help menu lets you browse the Mup User's Guide, view some startup hints, view the Mup license, or see the current version number of Mup and Mupmate.

<h2>SEE ALSO</h2>

 

 <a HREF="/docs/linux/man/1-gs/">gs</a>(1), <a HREF="/docs/linux/man/1-mup/">mup</a>(1). 
 Mup --- Music Publisher User's Guide

<h2>CAVEATS</h2>

 

 Mupmate is currently only supported on Microsoft Windows, Apple Mac OS-X, and Linux or similar. 

 Mupmate does not directly provide a print facility. Almost any PostScript viewer already provides this ability, so you can simply select &quot;Display&quot; from the Run menu and use the viewer's print capabilities. Alternately you can use the &quot;Write PostScript File&quot; from the Run menu and then print the resulting file. 

<h2>Index</h2>


