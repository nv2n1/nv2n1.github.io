---
title: "orca(1)"
name: "orca"
section: "1"
letter: "o"
url: "/docs/linux/man/1-orca/"
description: "orca – a scriptable screen reader"
---

<h2 class="name">NAME</h2>
<p> orca &#8211; a scriptable screen reader </p>
<h2>SYNOPSIS</h2>
<p> <code>orca</code> [<i>option&#8230;</i>]</p>
<h2>DESCRIPTION</h2>
<p> <code>orca</code> is a screen reader for people with visual impairments, it provides alternative access to the desktop by using speech synthesis and braille. </p>
<p> <code>orca</code> works with applications and toolkits that support the Assistive Technology Service Provider Interface (AT-SPI), which is the primary assistive technology infrastructure for Linux and Solaris. Applications and toolkits supporting the AT-SPI include the GNOME Gtk+ toolkit, the Java platform&#8217;s Swing toolkit, LibreOffice, Gecko, and WebKitGtk. AT-SPI support for the KDE Qt toolkit is being pursued.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-s, &#8211;setup</code></p>
<dd> When starting <code>orca</code>, initiate the GUI-based configuration.</p>
<dt><code>-u, &#8211;user-prefs-dir=</code><i>dirname</i></p>
<dd> When starting <code>orca</code>, use <i>dirname</i> as an alternate directory for the user preferences.</p>
<dt><code>-e, &#8211;enable=</code><i>speech|braille|braille-monitor</i></p>
<dd> When starting <code>orca</code>, force the enabling of the supplied options.</p>
<dt><code>-d, &#8211;disable=</code><i>speech|braille|braille-monitor</i></p>
<dd> When starting <code>orca</code>, force the disabling of the supplied options.</p>
<dt><code>-l, &#8211;list-apps</code></p>
<dd> Prints the names of all the currently running applications. This is used primarily for debugging purposes to see if <code>orca</code> can talk to the accessibility infrastructure. Note that if <code>orca</code> is already running, this will not kill the other <code>orca</code> process. It will just list the currently running applications, and you will see <code>orca</code> listed twice: once for the existing <code>orca</code> and once for this instance.</p>
<dt><code>&#8211;debug</code></p>
<dd> Enables debug output for <code>orca</code> and sends all debug output to a file with a name of the form &#8216;debug-YYYY-MM-DD-HH:MM:SS.out&#8217; in the current directory. The YYYY-MM-DD-HH:MM:SS portion will be replaced with the current date and time.</p>
<dt><code>&#8211;debug-file=</code><i>filename</i></p>
<dd> Enables debug output for <code>orca</code> and sends all debug output to the given filename.</p>
<dt><code>-v, &#8211;version</code></p>
<dd> outputs <code>orca</code> version number and exits.</p>
<dt><code>-h, &#8211;help</code></p>
<dd> displays <code>orca</code> help and exits.</p>
<dt><code>&#8211;replace</code></p>
<dd> Replace a currently running <code>orca</code> process. By default, if <code>orca</code> detects an existing <code>orca</code> process for the same session, it will not start a new <code>orca</code> process. This option will kill and cleanup after any existing <code>orca</code> process and then start a new <code>orca</code> in its place.</p>
<dt>
<dd></dl>
<h2>KEYBOARD SETTINGS</h2>
<p> Orca provides two keyboard modes, Desktop and Laptop keyboard layout. The <code>Orca_Modifier</code> key is <code>Insert</code> in desktop keyboard layout and <code>Caps_Lock</code> in laptop keyboard layout. </p>
<p> <code>Orca</code> uses default GNOME keyboard shortcuts to navigate the desktop and interact with various applications. The flat review commands provide an alternative method of interaction in certain inaccessible applications. It should not be confused with flat review functionality provided by other screen readers. </p>
<h2>Desktop Mode</h2>
<p> <code>Flat review commands</code> </p>
<p> <code>Numpad-7</code> move the flat review cursor to the previous line and read it. </p>
<p> <code>Numpad-8</code> read the current line. </p>
<p> <code>Numpad-9</code> move the flat review cursor to the next line and read it. </p>
<p> <code>Numpad-4</code> move the flat review cursor to the previous word and read it. </p>
<p> <code>Numpad-5</code> read the current word. </p>
<p> <code>Numpad-6</code> move the flat review cursor to the next word and read it. </p>
<p> <code>Numpad-1</code> move the flat review cursor to the previous character and read it. </p>
<p> <code>Numpad-2</code> read the current character. </p>
<p> <code>Numpad-3</code> move the flat review cursor to the next character and read it. </p>
<p> <code>Numpad-slash</code> perform a left mouse click at the location of the flat review cursor. </p>
<p> <code>Numpad-star</code> perform a right mouse click at the location of the flat review cursor. </p>
<p> <code>Bookmark commands</code> </p>
<p> <code>Alt+Insert+[1-6]</code> assign a bookmark to a numbered slot. If a bookmark already exists in the slot it will be replaced with the new one. </p>
<p> <code>Insert+[1-6]</code> go to the position pointed to by the bookmark bound to this numbered slot. </p>
<p> <code>Insert+B and Insert+Shift+B</code> move between the given bookmarks for the given application or page. </p>
<p> <code>Alt+Insert+B</code> save the defined bookmarks for the current application or page. </p>
<p> <code>Miscellaneous functions</code> </p>
<p> <code>Numpad+Plus</code><br />
&nbsp;&#8216;say all&#8217;&nbsp;command;&nbsp;reads from the current position of the caret to the end of the document. </p>
<p> <code>Numpad+Enter</code><br />
&nbsp;&#8216;Where am I&#8217;&nbsp;command;&nbsp;speaks information such as the title of the current application window, as well as the name of the control that currently has focus. </p>
<p> <code>Insert+H</code> enter into orca&#8217;s &#8216;learn mode&#8217;; press Escape to exit. </p>
<p> <code>Insert+Shift+Backslash</code> toggle live regions monitoring on and off. </p>
<p> <code>Insert+F</code> speak font and attribute information for the current character. </p>
<p> <code>Insert+Space</code> Launch the orca Configuration dialog. </p>
<p> <code>Insert+Ctrl+Space</code> reload user settings and reinitialize services as necessary. Also launches the orca Configuration dialog for the current application. </p>
<p> <code>Insert+S</code> toggle speech on and off. </p>
<p> <code>Insert+F11</code> toggle the reading of tables, either by single cell or whole row. </p>
<h2>Laptop Mode</h2>
<p> <code>Flat review commands</code> </p>
<p> <code>Caps_Lock+U</code> move the flat review cursor to the previous line and read it. Double-click to move flat review to the top of the current window. </p>
<p> <code>Caps_Lock+I</code> read the current line. Double-click to read the current line along with formatting and capitalization details. </p>
<p> <code>Caps_Lock+O</code> move the flat review cursor to the next line and read it. Double- click to move flat review to the bottom of the current window. </p>
<p> <code>Caps_Lock+J</code> move the flat review cursor to the previous word and read it. Double-click to move flat review to the word above the current word. </p>
<p> <code>Caps_Lock+K</code> read the current word. Double-click to spell the word. Triple-click to hear the word spelled phonetically. </p>
<p> <code>Caps_Lock+L</code> move the flat review cursor to the next word and read it. Double- click to move flat review to the word below the current word. </p>
<p> <code>Caps_Lock+M</code> move the flat review cursor to the previous character and read it. Double-click to move flat review to the end of the current line. </p>
<p> <code>Caps_Lock+Comma</code> read the current character. Double-click to pronounce the character phonetically if it is a letter. </p>
<p> <code>Caps_Lock+Period</code> move the flat review cursor to the next character and read it. </p>
<p> <code>Caps_Lock+7</code> perform a left mouse click at the location of the flat review cursor. </p>
<p> <code>Caps_Lock+8</code> perform a right mouse click at the location of the flat review cursor. </p>
<p> <code>Bookmark commands</code> </p>
<p> <code>Alt+Caps_Lock+[1-6]</code> </p>
<p> add a bookmark to the numbered slot. If a bookmark already exists for the slot it will be replaced with the new one. </p>
<p> <code>Caps_Lock+[1-6]</code> go to the position pointed to by the bookmark bound to this numbered slot. </p>
<p> <code>Caps_Lock+Band Caps_Lock+Shift+B</code> move between the given bookmarks for the given application or page. </p>
<p> <code>Alt+Caps_Lock+B</code> save the defined bookmarks for the current application or page. </p>
<p> <code>Miscellaneous functions</code> </p>
<p> <code>Caps_Lock+Semicolon</code><br />
&nbsp;&#8216;Say all&#8217;&nbsp;command;&nbsp;reads from the current position of the caret to the end of the document. <code>Caps_Lock+Enter</code><br />
&nbsp;&#8216;Where am I&#8217;&nbsp;command;&nbsp;speaks information such as the title of the current application window, as well as the name of the control that currently has focus. </p>
<p> <code>Caps_Lock+H</code> enter learn mode (press Escape to exit). </p>
<p> <code>Caps_Lock+Shift+Backslash</code> toggle live regions monitoring on and off. </p>
<p> <code>Caps_Lock+F</code> speak font and attribute information for the current character. </p>
<p> <code>Caps_Lock+Space</code> launch the orca Configuration dialog. </p>
<p> <code>Caps_Lock+Ctrl+Space</code> reload user settings and reinitialize services as necessary; also launches the orca Configuration dialog for the current application. </p>
<p> <code>Caps_Lock+S</code> toggle speech on and off. </p>
<p> <code>Caps_Lock+F11</code> toggle the reading of tables, either by single cell or whole row. </p>
<h2>FILES</h2>
<dl>
<dt><code>~/.local/share/orca</code></p>
<dd> <code>Orca</code> user preferences directory</p>
<dt><code>~/.local/share/orca/user-settings.conf</code></p>
<dd> <code>Orca</code> user preferences configuration file.</p>
<dt><code>~/.local/share/orca/orca-customizations.py</code></p>
<dd> <code>Orca</code> user customizations configuration file </p>
<dt><code>~/.local/share/orca/orca-scripts</code></p>
<dd> <code>Orca</code> user orca scripts directory</p>
<dt><code>~/.local/share/orca/bookmarks</code></p>
<dd> <code>Orca</code> user bookmarks directory</p>
<dt><code>~/.local/share/orca/app-settings</code></p>
<dd> <code>Orca</code> user application specific settings directory </p>
</dl>
<h2>AUTHOR</h2>
<p> <code>Orca</code> originated as a community effort led by the Sun Microsystems Inc. Accessibility Program Office and with contributions from many community members.</p>
<h2>SEE ALSO</h2>
<p> For more information please visit <code>orca</code> wiki at &lt;<a rel="nofollow" href="http://live.gnome.org/Orca">http://live.gnome.org/Orca</a>&gt; </p>
<p> The <code>orca</code> mailing list &lt;<a rel="nofollow" href="http://mail.gnome.org/mailman/listinfo/orca-list">http://mail.gnome.org/mailman/listinfo/orca-list</a>&gt; To post a message to all <code>orca</code> list, send a email to orca-list [at] gnome.org </p>
<h2>Index</h2>
