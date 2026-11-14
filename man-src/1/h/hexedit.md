---
title: "hexedit(1)"
name: "hexedit"
section: "1"
letter: "h"
url: "/docs/linux/man/1-hexedit/"
---

<h2>NAME</h2>

 hexedit - view and edit files in hexadecimal or in ASCII

<h2>SYNOPSIS</h2>

 <i>hexedit</i> [-s | --sector] [-m | --maximize] [-h | --help] [filename]

<h2>DESCRIPTION</h2>

 

 <i>hexedit</i> shows a file both in ASCII and in hexadecimal. The file can be a device as the file is read a piece at a time. You can modify the file and search through it.

<h2>OPTIONS</h2>

<dl>
<dt><i>-s, --sector</i>
<dd> Format the display to have entire sectors.
<dt><i>-m, --maximize</i>
<dd> Try to maximize the display.
<dt><i>--color</i>
<dd> Display colors. This feature is only available if your operating system supports it.
<dt><i>-h, --help</i>
<dd> Show the usage.</dl>

<h2>COMMANDS (quickly)</h2>

<h3>Moving</h3>

 <pre>
&lt;, &gt; :  go to start/end of the file
Right:  next character
Left:   previous character
Down:   next line
Up:     previous line
Home:   beginning of line
End:    end of line
PUp:    page forward
PDown:  page backward
</pre>

<h3>Miscellaneous</h3>

 <pre>
F2:     save
F3:     load file
F1:     help
Ctrl-L: redraw
Ctrl-Z: suspend
Ctrl-X: save and exit
Ctrl-C: exit without saving
Tab:    toggle hex/ascii
Return: go to
Backspace: undo previous character
Ctrl-U: undo all
Ctrl-S: search forward
Ctrl-R: search backward
</pre>

<h3>Cut&amp;Paste</h3>

 <pre>
Ctrl-Space: set mark
Esc-W:  copy
Ctrl-Y: paste
Esc-Y:  paste into a file
Esc-I:  fill
</pre>

<h2>COMMANDS (full and detailed)</h2>

 o <i>Right-Arrow</i>, <i>Left-Arrow</i>, <i>Down-Arrow</i>, <i>Up-Arrow</i> - move the cursor. 
 o <i>Ctrl+F</i>, <i>Ctrl+B</i>, <i>Ctrl+N</i>, <i>Ctrl+P</i> - move the cursor. 
 o <i>Ctrl+Right-Arrow</i>, <i>Ctrl+Left-Arrow</i>, <i>Ctrl+Down-Arrow</i>, <i>Ctrl+Up-Arrow</i> - move n times the cursor. 
 o <i>Esc+Right-Arrow</i>, <i>Esc+Left-Arrow</i>, <i>Esc+Down-Arrow</i>, <i>Esc+Up-Arrow</i> - move n times the cursor. 
 o <i>Esc+F</i>, <i>Esc+B</i>, <i>Esc+N</i>, <i>Esc+P</i> - move n times the cursor. 
 o <i>Home</i>, <i>Ctrl+A</i> - go the beginning of the line. 
 o <i>End</i>, <i>Ctrl+E</i> - go to the end of the line. 
 o <i>Page up</i>, <i>Esc+V</i>, <i>F5</i> - go up in the file by one page. 
 o <i>Page down</i>, <i>Ctrl+V</i>, <i>F6</i> - go down in the file by one page. 
 o <i>&lt;</i>, <i>Esc+&lt;</i>, <i>Esc+Home</i> - go to the beginning of the file. 
 o <i>&gt;</i>, <i>Esc+&gt;</i>, <i>Esc+End</i> - go to the end of the file (for regular files that have a size). 
 o <i>Ctrl+Z</i> - suspend hexedit. 
 o <i>Ctrl+U</i>, <i>Ctrl+_</i>, <i>Ctrl+/</i> - undo all (forget the modifications). 
 o <i>Ctrl+Q</i> - read next input character and insert it (this is useful for inserting control characters and bound keys). 
 o <i>Tab</i>, <i>Ctrl+T</i> - toggle between ASCII and hexadecimal. 
 o <i>/</i>, <i>Ctrl+S</i> - search forward (in ASCII or in hexadecimal, use <i>TAB</i> to change). 
 o <i>Ctrl+R</i> - search backward. 
 o <i>Ctrl+G</i>, <i>F4</i> - go to a position in the file. 
 o <i>Return</i> - go to a sector in the file if <i>--sector</i> is used, otherwise go to a position in the file. 
 o <i>Esc+L</i> - display the page starting at the current cursor position. 
 o <i>F2</i>, <i>Ctrl+W</i> - save the modifications. 
 o <i>F1</i>, <i>Esc+H</i> - help (show the man page). 
 o <i>Ctrl+O</i>, <i>F3</i> - open another file 
 o <i>Ctrl+L</i> - redisplay (refresh) the display (usefull when your terminal screws up). 
 o <i>Backspace</i>, <i>Ctrl+H</i> - undo the modifications made on the previous byte. 
 o <i>Esc+Ctrl+H</i> - undo the modifications made on the previous bytes. 
 o <i>Ctrl+Space</i>, <i>F9</i> - set mark where cursor is. 
 o <i>Esc+W</i>, <i>Delete</i>, <i>F7</i> - copy selected region. 
 o <i>Ctrl+Y</i>, <i>Insert</i>, <i>F8</i> - paste (yank) previously copied region. 
 o <i>Esc+Y</i>, <i>F11</i> - save previously copied region to a file. 
 o <i>Esc+I</i>, <i>F12</i> - fill the selection with a string 
 o <i>Esc+T</i> - truncate the file at the current location 
 o <i>Ctrl+C</i> - unconditional quit (without saving). 
 o <i>F10</i>, <i>Ctrl+X</i> - quit. 

 For the <i>Esc</i> commands, it sometimes works to use <i>Alt</i> instead of <i>Esc</i>. Funny things here (especially for froggies :) egrave = Alt+H , ccedilla = Alt+G, Alt+Y = ugrave. 

<h3>Modeline</h3>

 At the bottom of the display you have the modeline (copied from emacs). As in emacs, you have the indications --, ** and %% meaning unmodified, modified and read-only. Then you have the name of the file you're currently editing. Next to it is the current position of the cursor in the file followed by the total file size. The total file size isn't quite correct for devices. 
 While in --sector mode, it shows the sector the cursor is in.

<h3>Editing</h3>

 You can edit in ASCII or in hexadecimal. You can switch between the two with <i>Tab</i>. When the file is read-only, you can't edit it. When trying to edit a read-only file, a message (``File is read-only'') tells you it is non-writable. 
 The modifications are shown in bold until they are saved. The modeline indicates whether you have modified the file or not. 
 When editing in hexadecimal, only <i>0</i>,<i>1</i>,...,<i>9</i>, <i>a</i>,<i>b</i>,...,<i>f</i>, <i>A</i>,<i>B</i>,...<i>F</i> are legal. Other keys are unbound. The first time you hit an unbound key, the help pops up. It won't pop again unless you call the help directly (with <i>F1</i>). 
 When editing in ascii, you can find it difficult to enter characters like <i>/</i> which are bound to a function. The solution is to use the quoted insert function <i>Ctrl+Q</i>, the key after the quoted insert function is not processed by <i>hexedit</i> (like emacs' quoted-insert, or like the \ character in C).

<h3>Searching</h3>

 You can search for a string in ASCII or in hexadecimal. You can switch between the two with <i>Tab</i>. If the string is found, the cursor is moved to the beginning of the matching location. If the search failed, a message (``not found'') tells you so. You can cancel the search by pressing a key. 
 The search in hexadecimal is a bit confusing. You must give a hexadecimal string with an even number of characters. The search can then be done byte by byte. If you want to search a long number (eg: a 32 bit number), you must know the internal representation of that number (little/big endian problem) and give it the way it is in memory. For example, on an Intel processor (little endian), you must swap every bytes: 0x12345678 is written 0x78563412 in memory and that's the string you must give to the search engine. 
 Before searching you are asked if you want to save the changes, if the file is edited. 

 For more sophisticated search, see Volker Schatz's patch at &lt;<a rel="nofollow" HREF="http://www.volkerschatz.com/unix/homebrew.html#hexedit">http://www.volkerschatz.com/unix/homebrew.html#hexedit</a>&gt;.

<h3>Selecting, copying, pasting, filling</h3>

 First, select the part of the buffer you want to copy: start setting the mark where you want. Then go to the end of the area you want to copy (you can use the go to function and the search functions). Then copy it. You can then paste the copied area in the current file or in another file. 

 You can also fill the selected area with a string or a character: start choosing the block you want to fill in (set mark then move to the end of the block), and call the fill function (<i>F12</i>). <i>hexedit</i> ask you the string you want to fill the block with. 
 The code is not tuned for huge filling as it keeps the modifications in memory until you save them. That's why <i>hexedit</i> will warn you if you try to fill in a big block. 

 When the mark is set, the selection is shown in reverse mode. 
 Be aware that the copied area contains the modifications done at the time of the copy. But if you undo the modifications, it does not change the content of the copy buffer. It seems obvious but it's worth saying.

<h3>Scrolling</h3>

 The scrolling is different whether you are in <i>--sector</i> mode or not. In normal mode, the scrolling is line by line. In sector mode, the scrolling is sector by sector. In both modes, you can force the display to start at a given position using <i>Esc+L</i>.

<h2>SEE ALSO</h2>

 <a HREF="/docs/linux/man/1-od/">od</a>(1), <a HREF="/docs/linux/man/1-hdump/">hdump</a>(1), <a HREF="/docs/linux/man/1-hexdump/">hexdump</a>(1), <a HREF="/docs/linux/man/1-bpe/">bpe</a>(1), <a HREF="/docs/linux/man/1-hexed/">hexed</a>(1), <a HREF="/docs/linux/man/1-beav/">beav</a>(1).

<h2>AUTHOR</h2>

 Pixel (Pascal Rigaux) &lt;pixel [at] rigaux.org&gt;, 
 Home page is &lt;<a rel="nofollow" HREF="http://rigaux.org/">http://rigaux.org/</a>&gt;.

<h2>UNRESTRICTIONS</h2>

 <i>hexedit</i> is Open Source; anyone may redistribute copies of <i>hexedit</i> to anyone under the terms stated in the GNU General Public License. 

 You can find <i>hexedit</i> at 
 &lt;<a rel="nofollow" HREF="http://rigaux.org/hexedit-1.2.13.src.tgz">http://rigaux.org/hexedit-1.2.13.src.tgz</a>&gt; and 
 &lt;<a rel="nofollow" HREF="http://rigaux.org/hexedit-1.2.13.bin.i386.dynamic.tgz">http://rigaux.org/hexedit-1.2.13.bin.i386.dynamic.tgz</a>&gt;.

<h2>TODO</h2>

 Anything you think could be nice...

<h2>LIMITATIONS</h2>

 There are problems with the curses library given with Redhat 5.0 that make <i>hexedit</i> think the terminal is huge. The result is that hexedit is not usable. 

 The shortcuts work on some machines, and not on others. That's why there are many shortcuts for each function. The Ctrl+Arrows and the Alt+. do not work work as they should most of the time. On SUNs, you must do Ctrl+V-Ctrl+V instead of Ctrl+V (!); and the Alt key is the diamond one. 

 While searching, it could be interesting to know which position the search has reached. It's always nice to see something moving to help waiting. 

 The hexadecimal search could be able to search modulo 4 bits instead of 8 bits. Another feature could be to complete padd odd length hexadecimal searches with zeros.

<h2>BUGS</h2>

 I have an example where the display is completly screwed up. It seems to be a bug in ncurses (or maybe in xterm and rxvt)?? Don't know if it's me using ncurses badly or not... It seems to happen when <i>hexedit</i> leaves only one space at the end of the lines... If anyone has a (or the) solution, please tell me! 

 If you have any problem with the program (even a small one), please do report it to me. Remarks of any kind are also welcome. 

 

<h2>Index</h2>


