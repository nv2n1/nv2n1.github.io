---
title: "mc(1)"
name: "mc"
section: "1"
letter: "m"
url: "/docs/linux/man/1-mc/"
description: "mc – Visual shell for Unix-like systems."
---

<h2 class="name">NAME</h2>
<p> mc &#8211; Visual shell for Unix-like systems. </p>
<h2>USAGE</h2>
<p> <code>mc</code> [-abcCdfhPstuUVx] [-l log] [dir1 [dir2]] [-e [file] &#8230;] [-v file]</p>
<h2>DESCRIPTION</h2>
<p> GNU Midnight Commander is a directory browser/file manager for Unix-like operating systems.</p>
<h2>OPTIONS</h2>
<dl>
<dt><i>-a, &#8211;stickchars</i></p>
<dd> Disable usage of graphic characters for line drawing.</p>
<dt><i>-b, &#8211;nocolor</i></p>
<dd> Force black and white display.</p>
<dt><i>-c, &#8211;color</i></p>
<dd> Force color mode, please check the section Colors for more information.</p>
<dt><i>-C arg, &#8211;colors=arg</i></p>
<dd> Specify a different color set in the command line. The format of arg is documented in the Colors section.</p>
<dt><i>-S arg, &#8211;skin=arg</i></p>
<dd> Specify a name of skin in the command line. Technology of skins is documented in the Skins section.</p>
<dt><i>-d, &#8211;nomouse</i></p>
<dd> Disable mouse support.</p>
<dt><i>-e [file], &#8211;edit[=file]</i></p>
<dd> Start the internal editor. If the file is specified, open it on startup. See also <code>mcedit (1)</code>.</p>
<dt><i>-f, &#8211;datadir</i></p>
<dd> Display the compiled-in search paths for Midnight Commander files.</p>
<dt><i>-F, &#8211;datadir-info</i></p>
<dd> Display extended info about compiled-in paths for Midnight Commander.</p>
<dt><i>&#8211;configure-options</i></p>
<dd> Display configure options.</p>
<dt><i>-k, &#8211;resetsoft</i></p>
<dd> Reset softkeys to their default from the termcap/terminfo database. Only useful on HP terminals when the function keys don&#8217;t work.</p>
<dt><i>-K file, &#8211;keymap=file</i></p>
<dd> Specify a name of keymap file in the command line.</p>
<dt><i>&#8211;nokeymap</i></p>
<dd> Don&#8217;t load key bindings from any file, use default hardcoded keys.</p>
<dt><i>-l file, &#8211;ftplog=file</i></p>
<dd> Save the ftpfs dialog with the server in file.</p>
<dt><i>-D N, &#8211;debuglevel=N</i></p>
<dd> Save the debug level for SMB VFS. N is in 0-10 range.</p>
<dt><i>-P file, &#8211;printwd=file</i></p>
<dd> Print the last working directory to the specified file. This option is not meant to be used directly. Instead, it&#8217;s used from a special shell script that automatically changes the current directory of the shell to the last directory the Midnight Commander was in. Source the file <code>/usr/share/mc/bin/mc.sh</code> (bash and zsh users) or <code>/usr/share/mc/bin/mc.csh</code> (tcsh users) respectively to define <code>mc</code> as an alias to the appropriate shell script.</p>
<dt><i>-s, &#8211;slow</i></p>
<dd> Set alternative mode drawing of frameworks. If the section [Lines] is not filled, the symbol for the pseudographics frame is a space, otherwise the frame characters are taken from following parameters. </p>
<p> <code>You can redefine the following variables:</code></p>
<dt><code>lefttop</code></p>
<dd> left-top corner</p>
<dt><code>righttop</code></p>
<dd> right-top corner</p>
<dt><code>centertop</code></p>
<dd> center-top cross</p>
<dt><code>centerbottom</code></p>
<dd> center-bottom cross</p>
<dt><code>leftbottom</code></p>
<dd> left-bottom corner</p>
<dt><code>rightbottom</code></p>
<dd> right-bottom corner</p>
<dt><code>leftmiddle</code></p>
<dd> left-middle cross</p>
<dt><code>rightmiddle</code></p>
<dd> right-middle cross</p>
<dt><code>centermiddle</code></p>
<dd> center cross</p>
<dt><code>horiz</code></p>
<dd> default horizontal line</p>
<dt><code>vert</code></p>
<dd> default vertical line</p>
<dt><code>thinhoriz</code></p>
<dd> thin horizontal line</p>
<dt><code>thinvert</code></p>
<dd> thin vertical line</p>
<dt><i>-t, &#8211;termcap</i></p>
<dd> Used only if the code was compiled with Slang and terminfo: it makes the Midnight Commander use the value of the <code>TERMCAP</code> variable for the terminal information instead of the information on the system wide terminal database</p>
<dt><i>-u, &#8211;nosubshell</i></p>
<dd> Disable use of the concurrent shell (only makes sense if the Midnight Commander has been built with concurrent shell support).</p>
<dt><i>-U, &#8211;subshell</i></p>
<dd> Enable use of the concurrent shell support (only makes sense if the Midnight Commander was built with the subshell support set as an optional feature).</p>
<dt><i>-v file, &#8211;view=file</i></p>
<dd> Start the internal viewer to view the specified file. See also <code>mcview (1)</code>.</p>
<dt><i>-V, &#8211;version</i></p>
<dd> Display the version of the program.</p>
<dt><i>-x, &#8211;xterm</i></p>
<dd> Force xterm mode. Used when running on xterm-capable terminals (two screen modes, and able to send mouse escape sequences).</p>
<dt><i>-X, &#8211;no-x11</i></p>
<dd> Do not use X11 to get the state of modifiers Alt, Ctrl, Shift</p>
<dt><i>-g, &#8211;oldmouse</i></p>
<dd> Force a &quot;normal tracking&quot; mouse mode. Used when running on xterm-capable terminals (tmux/screen).</dl>
<p> If specified, the first path name is the directory to show in the selected panel; the second path name is the directory to be shown in the other panel.</p>
<h2>Overview</h2>
<p> The screen of the Midnight Commander is divided into four parts. Almost all of the screen space is taken up by two directory panels. By default, the second line from the bottom of the screen is the shell command line, and the bottom line shows the function key labels. The topmost line is the menu bar line. The menu bar line may not be visible, but appears if you click the topmost line with the mouse or press the F9 key. </p>
<p> The Midnight Commander provides a view of two directories at the same time. One of the panels is the current panel (a selection bar is in the current panel). Almost all operations take place on the current panel. Some file operations like Rename and Copy by default use the directory of the unselected panel as a destination (don&#8217;t worry, they always ask you for confirmation first). For more information, see the sections on the Directory Panels, the Left and Right Menus and the File Menu. </p>
<p> You can execute system commands from the Midnight Commander by simply typing them. Everything you type will appear on the shell command line, and when you press Enter the Midnight Commander will execute the command line you typed; read the Shell Command Line and Input Line Keys sections to learn more about the command line.</p>
<h2>Mouse Support</h2>
<p> The Midnight Commander comes with mouse support. It is activated whenever you are running on an <code><a href="/docs/linux/man/1-xterm/">xterm</a>(1)</code> terminal (it even works if you take a telnet, ssh or rlogin connection to another machine from the xterm) or if you are running on a Linux console and have the <code>gpm</code> mouse server running. </p>
<p> When you left click on a file in the directory panels, that file is selected; if you click with the right button, the file is marked (or unmarked, depending on the previous state). </p>
<p> Double-clicking on a file will try to execute the command if it is an executable program; and if the extension file has a program specified for the file&#8217;s extension, the specified program is executed. </p>
<p> Also, it is possible to execute the commands assigned to the function key labels by clicking on them. </p>
<p> The default auto repeat rate for the mouse buttons is 400 milliseconds. This may be changed to other values by editing the ~/.config/mc/ini file and changing the <i>mouse_repeat_rate</i> parameter. </p>
<p> If you are running the Midnight Commander with the mouse support, you can get the default mouse behavior (cutting and pasting text) by holding down the Shift key.</p>
<h2></h2>
<h2>Keys</h2>
<p> Some commands in the Midnight Commander involve the use of the <i>Control</i> (sometimes labeled CTRL or CTL) and the <i>Meta</i> (sometimes labeled ALT or even Compose) keys. In this manual we will use the following abbreviations:</p>
<dl>
<dt><code>C-&lt;chr&gt;</code></p>
<dd> means hold the Control key while typing the character &lt;chr&gt;. Thus C-f would be: hold the Control key and type f.</p>
<dt><code>Alt-&lt;chr&gt;</code></p>
<dd> means hold the Meta or Alt key down while typing &lt;chr&gt;. If there is no Meta or Alt key, type <i>ESC</i>, release it, then type the character &lt;chr&gt;.</p>
<dt><code>S-&lt;chr&gt;</code></p>
<dd> means hold the Shift key down while typing &lt;chr&gt;.</dl>
<p> All input lines in the Midnight Commander use an approximation to the GNU Emacs editor&#8217;s key bindings (default). </p>
<p> You may redefine key bindings. See <i>redefine hotkey bindings</i> </p>
<p> for more info. All other key bindings (described in this manual) relative to default behavior. </p>
<p> There are many sections which tell about the keys. The following are the most important. </p>
<p> The File Menu section documents the keyboard shortcuts for the commands appearing in the File menu. This section includes the function keys. Most of these commands perform some action, usually on the selected file or the tagged files. </p>
<p> The Directory Panels section documents the keys which select a file or tag files as a target for a later action (the action is usually one from the file menu). </p>
<p> The Shell Command Line section list the keys which are used for entering and editing command lines. Most of these copy file names and such from the directory panels to the command line (to avoid excessive typing) or access the command line history. </p>
<p> Input Line Keys are used for editing input lines. This means both the command line and the input lines in the query dialogs. </p>
<h2> Redefine hotkey bindings</h2>
<p> Hotkey bindings may be read from external file (keymap-file). Initially, Mignight Commander creates key bindings using keymap defined in the source code. Then, two files <code>/usr/share/mc/mc.keymap</code> and <code>/etc/mc/mc.keymap</code> are loaded always, sequentially reassigned key bindings defined earlier. User-defined keymap-file is searched on the following algorithm (to the first one found):</p>
<dl>
<dt>
<dd>
 1) command line option <code>-K &lt;keymap&gt;</code> or <code>&#8211;keymap=&lt;keymap&gt;</code><br />
 2) Environment variable <code>MC_KEYMAP</code><br />
 3) Parameter <code>keymap</code> in section <code>[Midnight-Commander]</code> of config file.<br />
 4) File <code>~/.config/mc/mc.keymap</code>
</dl>
<p> Command line option, environment variable and parameter in config file may contain the absolute path to the keymap-file (with the extension .keymap or without it). Search of keymap-file will occur in (to the first one found):</p>
<dl>
<dt>
<dd>
 1) <code>~/.config/mc</code><br />
 2) <code>/etc/mc/</code><br />
 3) <code>/usr/share/mc/</code> </p>
</dl>
<h2> Miscellaneous Keys</h2>
<p> Here are some keys which don&#8217;t fall into any of the other categories:</p>
<dl>
<dt><code>Enter</code></p>
<dd> if there is some text in the command line (the one at the bottom of the panels), then that command is executed. If there is no text in the command line then if the selection bar is over a directory the Midnight Commander does a <code><a href="/docs/linux/man/2-chdir/">chdir</a>(2)</code> to the selected directory and reloads the information on the panel; if the selection is an executable file then it is executed. Finally, if the extension of the selected file name matches one of the extensions in the extensions file then the corresponding command is executed.</p>
<dt><code>C-l</code></p>
<dd> repaint all the information in the Midnight Commander.</p>
<dt><code>C-x c</code></p>
<dd> run the Chmod command on a file or on the tagged files.</p>
<dt><code>C-x o</code></p>
<dd> run the Chown command on the current file or on the tagged files.</p>
<dt><code>C-x l</code></p>
<dd> run the hard link command.</p>
<dt><code>C-x s</code></p>
<dd> run the absolute symbolic link command.</p>
<dt><code>C-x v</code></p>
<dd> run the relative symbolic link command. See the File Menu section for more information about symbolic links.</p>
<dt><code>C-x i</code></p>
<dd> set the other panel display mode to information.</p>
<dt><code>C-x q</code></p>
<dd> set the other panel display mode to quick view.</p>
<dt><code>C-x !</code></p>
<dd> execute the External panelize command.</p>
<dt><code>C-x h</code></p>
<dd> run the add directory to hotlist command.</p>
<dt><code>Alt-!</code></p>
<dd> executes the Filtered view command, described in the view command.</p>
<dt><code>Alt-?</code></p>
<dd> executes the Find file command.</p>
<dt><code>Alt-c</code></p>
<dd> pops up the quick cd dialog.</p>
<dt><code>C-o</code></p>
<dd> when the program is being run in the Linux or FreeBSD console or under an xterm, it will show you the output of the previous command. When ran on the Linux console, the Midnight Commander uses an external program (cons.saver) to handle saving and restoring of information on the screen.</dl>
<p> When the subshell support is compiled in, you can type C-o at any time and you will be taken back to the Midnight Commander main screen, to return to your application just type C-o. If you have an application suspended by using this trick, you won&#8217;t be able to execute other programs from the Midnight Commander until you terminate the suspended application.</p>
<h2> Directory Panels</h2>
<p> This section lists the keys which operate on the directory panels. If you want to know how to change the appearance of the panels take a look at the section on Left and Right Menus.</p>
<dl>
<dt><code>Tab, C-i</code></p>
<dd> change the current panel. The old other panel becomes the new current panel and the old current panel becomes the new other panel. The selection bar moves from the old current panel to the new current panel.</p>
<dt><code>Insert, C-t</code></p>
<dd> to tag files you may use the Insert key (the kich1 terminfo sequence). To untag files, just retag a tagged file.</p>
<dt><code>M-e</code></p>
<dd> to change charset of panel you may use M-e (Alt-e). Recoding is made from selected codepage into system codepage. To cancel the recoding you may select &quot;directory up&quot; (..) in active panel. To cancel the charsets in all directories, select &quot;No translation &quot; in the dialog of encodings.</p>
<dt><code>Alt-g, Alt-r, Alt-j</code></p>
<dd> used to select the top file in a panel, the middle file and the bottom one, respectively.</p>
<dt><code>Alt-t</code></p>
<dd> toggle the current display listing to show the next display listing mode. With this it is possible to quickly switch to brief listing, long listing, user defined listing mode, and back to the default.</p>
<dt><code>C-\ (control-backslash)</code></p>
<dd> show the directory hotlist and change to the selected directory.</p>
<dt><code>+ &nbsp;<wbr>(plus)</code></p>
<dd> this is used to select (tag) a group of files. The Midnight Commander will prompt for a selection options. When <i>Files only</i> checkbox is on, only files will be selected. If <i>Files only</i> is off, as files as directories will be selected. When <i>Shell Patterns</i> checkbox is on, the regular expression is much like the filename globbing in the shell (* standing for zero or more characters and ? standing for one character). If <i>Shell Patterns</i> is off, then the tagging of files is done with normal regular expressions (see ed (1)). When <i>Case sensitive</i> checkbox is on, the selection will be case sensitive characters. If <i>Case sensitive</i> is off, the case will be ignored.</p>
<dt><code>\ (backslash)</code></p>
<dd> use the &quot;\&quot; key to unselect a group of files. This is the opposite of the Plus key.</p>
<dt><code>up-key, C-p</code></p>
<dd> move the selection bar to the previous entry in the panel.</p>
<dt><code>down-key, C-n</code></p>
<dd> move the selection bar to the next entry in the panel.</p>
<dt><code>home, a1, Alt-&lt;</code></p>
<dd> move the selection bar to the first entry in the panel.</p>
<dt><code>end, c1, Alt-&gt;</code></p>
<dd> move the selection bar to the last entry in the panel.</p>
<dt><code>next-page, C-v</code></p>
<dd> move the selection bar one page down.</p>
<dt><code>prev-page, Alt-v</code></p>
<dd> move the selection bar one page up.</p>
<dt><code>Alt-o</code></p>
<dd> If the currently selected file is a directory, load that directory on the other panel and moves the selection to the next file. If the currently selected file is not a directory, load the parent directory on the other panel and moves the selection to the next file.</p>
<dt><code>Alt-i</code></p>
<dd> make the current directory of the current panel also the current directory of the other panel. Put the other panel to the listing mode if needed. If the current panel is panelized, the other panel doesn&#8217;t become panelized.</p>
<dt><code>C-PageUp, C-PageDown</code></p>
<dd> only when supported by the terminal: change to &quot;..&quot; and to the currently selected directory respectively.</p>
<dt><code>Alt-y</code></p>
<dd> moves to the previous directory in the history, equivalent to clicking the <i>&lt;</i> with the mouse.</p>
<dt><code>Alt-u</code></p>
<dd> moves to the next directory in the history, equivalent to clicking the <i>&gt;</i> with the mouse.</p>
<dt><code>Alt-Shift-h, Alt-H</code></p>
<dd> displays the directory history, equivalent to depressing the &#8216;v&#8217; with the mouse.</dl>
<h2> Quick search</h2>
<p> The Quick search mode allows you to perform fast file search in file panel. Press <i>C-s</i> or <i>Alt-s</i> to start a filename search in the directory listing. </p>
<p> When the search is active, the user input will be added to the search string instead of the command line. If the <i>Show mini-status</i> option is enabled the search string is shown on the mini-status line. When typing, the selection bar will move to the next file starting with the typed letters. The <i>Backspace</i> or <i>DEL</i> keys can be used to correct typing mistakes. If C-s is pressed again, the next match is searched for. </p>
<p> If quick search is started with double pressing of C-s, the previous quick search pattern will be used for current search. </p>
<p> Besides the filename characters, you can also use wildcard characters &#8216;*&#8217; and &#8216;?&#8217;.</p>
<h2> Shell Command Line</h2>
<p> This section lists keys which are useful to avoid excessive typing when entering shell commands.</p>
<dl>
<dt><code>Alt-Enter</code></p>
<dd> copy the currently selected file name to the command line.</p>
<dt><code>C-Enter</code></p>
<dd> same a Alt-Enter. May not work on remote systems and some terminals.</p>
<dt><code>C-Shift-Enter</code></p>
<dd> copy the full path name of the currently selected file to the command line. May not work on remote systems and some terminals.</p>
<dt><code>Alt-Tab</code></p>
<dd> does the filename, command, variable, username and hostname completion for you.</p>
<dt><code>C-x t, C-x C-t</code></p>
<dd> copy the tagged files (or if there are no tagged files, the selected file) of the current panel (C-x t) or of the other panel (C-x C-t) to the command line.</p>
<dt><code>C-x p, C-x C-p</code></p>
<dd> the first key sequence copies the current path name to the command line, and the second one copies the unselected panel&#8217;s path name to the command line.</p>
<dt><code>C-q</code></p>
<dd> the quote command can be used to insert characters that are otherwise interpreted by the Midnight Commander (like the &#8216;+&#8217; symbol)</p>
<dt><code>Alt-p, Alt-n</code></p>
<dd> use these keys to browse through the command history. Alt-p takes you to the last entry, Alt-n takes you to the next one.</p>
<dt><code>Alt-h</code></p>
<dd> displays the history for the current input line.</dl>
<h2> General Movement Keys</h2>
<p> The help viewer, the file viewer and the directory tree use common code to handle moving. Therefore they accept exactly the same keys. Each of them also accepts some keys of its own. </p>
<p> Other parts of the Midnight Commander use some of the same movement keys, so this section may be of use for those parts too.</p>
<dl>
<dt><code>Up, C-p</code></p>
<dd> moves one line backward.</p>
<dt><code>Down, C-n</code></p>
<dd> moves one line forward.</p>
<dt><code>Prev Page, Page Up, Alt-v</code></p>
<dd> moves one page up.</p>
<dt><code>Next Page, Page Down, C-v</code></p>
<dd> moves one page down.</p>
<dt><code>Home, A1</code></p>
<dd> moves to the beginning.</p>
<dt><code>End, C1</code></p>
<dd> move to the end.</dl>
<p> The help viewer and the file viewer accept the following keys in addition the to ones mentioned above:</p>
<dl>
<dt><code>b, C-b, C-h, Backspace, Delete</code></p>
<dd> moves one page up.</p>
<dt><code>Space bar</code></p>
<dd> moves one page down.</p>
<dt><code>u, d</code></p>
<dd> moves one half of a page up or down.</p>
<dt><code>g, G</code></p>
<dd> moves to the beginning or to the end.</dl>
<h2> Input Line Keys</h2>
<p> The input lines (they are used for the command line and for the query dialogs in the program) accept these keys:</p>
<dl>
<dt><code>C-a</code></p>
<dd> puts the cursor at the beginning of line.</p>
<dt><code>C-e</code></p>
<dd> puts the cursor at the end of the line.</p>
<dt><code>C-b, move-left</code></p>
<dd> move the cursor one position left.</p>
<dt><code>C-f, move-right</code></p>
<dd> move the cursor one position right.</p>
<dt><code>Alt-f</code></p>
<dd> moves one word forward.</p>
<dt><code>Alt-b</code></p>
<dd> moves one word backward.</p>
<dt><code>C-h, Backspace</code></p>
<dd> delete the previous character.</p>
<dt><code>C-d, Delete</code></p>
<dd> delete the character in the point (over the cursor).</p>
<dt><code>C-@</code></p>
<dd> sets the mark for cutting.</p>
<dt><code>C-w</code></p>
<dd> copies the text between the cursor and the mark to a kill buffer and removes the text from the input line.</p>
<dt><code>Alt-w</code></p>
<dd> copies the text between the cursor and the mark to a kill buffer.</p>
<dt><code>C-y</code></p>
<dd> yanks back the contents of the kill buffer.</p>
<dt><code>C-k</code></p>
<dd> kills the text from the cursor to the end of the line.</p>
<dt><code>Alt-p, Alt-n</code></p>
<dd> Use these keys to browse through the command history. Alt-p takes you to the last entry, Alt-n takes you to the next one.</p>
<dt><code>Alt-C-h, Alt-Backspace</code></p>
<dd> delete one word backward.</p>
<dt><code>Alt-Tab</code></p>
<dd> does the filename, command, variable, username and hostname completion for you.</dl>
<h2></h2>
<h2>Menu Bar</h2>
<p> The menu bar pops up when you press F9 or click the mouse on the top row of the screen. The menu bar has five menus: &quot;Left&quot;, &quot;File&quot;, &quot;Command&quot;, &quot;Options&quot; and &quot;Right&quot;. </p>
<p> The Left and Right Menus allow you to modify the appearance of the left and right directory panels. </p>
<p> The File Menu lists the actions you can perform on the currently selected file or the tagged files. </p>
<p> The Command Menu lists the actions which are more general and bear no relation to the currently selected file or the tagged files. </p>
<p> The Options Menu lists the actions which allow you to customize the Midnight Commander.</p>
<h2> Left and Right (Above and Below) Menus</h2>
<p> The outlook of the directory panels can be changed from the <code>Left</code> and <code>Right</code> menus (they are named <code>Above</code> and <code>Below</code> when the horizontal panel split is chosen from the Layout options dialog).</p>
<h2> Listing Mode&#8230;</h2>
<p> The listing mode view is used to display a listing of files, there are four different listing modes available: <code>Full</code>, <code>Brief</code>, <code>Long</code> and <code>User</code>. The full directory view shows the file name, the size of the file and the modification time. </p>
<p> The brief view shows only the file name and it has two columns (therefore showing twice as many files as other views). The long view is similar to the output of <code>ls -l</code> command. The long view takes the whole screen width. </p>
<p> If you choose the &quot;User&quot; display format, then you have to specify the display format. </p>
<p> The user display format must start with a panel size specifier. This may be &quot;half&quot; or &quot;full&quot;, and they specify a half screen panel and a full screen panel respectively. </p>
<p> After the panel size, you may specify the two columns mode on the panel, this is done by adding the number &quot;2&quot; to the user format string. </p>
<p> After this you add the name of the fields with an optional size specifier. This are the available fields you may display:</p>
<dl>
<dt><code>name</code></p>
<dd> displays the file name.</p>
<dt><code>size</code></p>
<dd> displays the file size.</p>
<dt><code>bsize</code></p>
<dd> is an alternative form of the <code>size</code> format. It displays the size of the files and for directories it just shows SUB-DIR or UP&#8211;DIR.</p>
<dt><code>type</code></p>
<dd> displays a one character wide type field. This character is similar to what is displayed by ls with the -F flag &#8211; <code>*</code> for executable files, <code>/</code> for directories, <code>@</code> for links, <code>=</code> for sockets, <code>&#8211;</code> for character devices, <code>+</code> for block devices, <code>|</code> for pipes, <code>~</code> for symbolic links to directories and <code>!</code> for stale symlinks (links that point nowhere).</p>
<dt><code>mark</code></p>
<dd> an asterisk if the file is tagged, a space if it&#8217;s not.</p>
<dt><code>mtime</code></p>
<dd> file&#8217;s last modification time.</p>
<dt><code>atime</code></p>
<dd> file&#8217;s last access time.</p>
<dt><code>ctime</code></p>
<dd> file&#8217;s status change time.</p>
<dt><code>perm</code></p>
<dd> a string representing the current permission bits of the file.</p>
<dt><code>mode</code></p>
<dd> an octal value with the current permission bits of the file.</p>
<dt><code>nlink</code></p>
<dd> the number of links to the file.</p>
<dt><code>ngid</code></p>
<dd> the GID (numeric).</p>
<dt><code>nuid</code></p>
<dd> the UID (numeric).</p>
<dt><code>owner</code></p>
<dd> the owner of the file.</p>
<dt><code>group</code></p>
<dd> the group of the file.</p>
<dt><code>inode</code></p>
<dd> the inode of the file.</dl>
<p> Also you can use following keywords to define the panel layout:</p>
<dl>
<dt><code>space</code></p>
<dd> a space in the display format.</p>
<dt><code>|</code></p>
<dd> add a vertical line to the display format.</dl>
<p> To force one field to a fixed size (a size specifier), you just add <code>:</code> followed by the number of characters you want the field to have. If the number is followed by the symbol <code>+</code>, then the size specifies the minimal field size &#8211; if the program finds out that there is more space on the screen, it will then expand that field. </p>
<p> For example, the <code>Full</code> display corresponds to this format: </p>
<p> half type name | size | mtime </p>
<p> And the <code>Long</code> display corresponds to this format: </p>
<p> full perm space nlink space owner space group space size space mtime space name </p>
<p> This is a nice user display format: </p>
<p> half name | size:7 | type mode:3 </p>
<p> Panels may also be set to the following modes:</p>
<dl>
<dt><code>Info</code></p>
<dd> The info view display information related to the currently selected file and if possible information about the current file system.</p>
<dt><code>Tree</code></p>
<dd> The tree view is quite similar to the directory tree feature. See the section about it for more information.</p>
<dt><code>Quick View</code></p>
<dd> In this mode, the panel will switch to a reduced viewer that displays the contents of the currently selected file, if you select the panel (with the tab key or the mouse), you will have access to the usual viewer commands.</dl>
<h2> Sort Order&#8230;</h2>
<p> The eight sort orders are by name, by extension, by modification time, by access time, and by inode information modification time, by size, by inode and unsorted. In the Sort order dialog box you can choose the sort order and you may also specify if you want to sort in reverse order by checking the reverse box. </p>
<p> By default directories are sorted before files but this can be changed from the Panel options menu (option <code>Mix all files</code>).</p>
<h2> Filter&#8230;</h2>
<p> The filter command allows you to specify a shell pattern (for example <code>*.tar.gz</code>) which the files must match to be shown. Regardless of the filter pattern, the directories and the links to directories are always shown in the directory panel.</p>
<h2> Reread</h2>
<p> The reread command reload the list of files in the directory. It is useful if other processes have created or removed files.</p>
<h2> File Menu</h2>
<p> The Midnight Commander uses the F1 &#8211; F10 keys as keyboard shortcuts for commands appearing in the file menu. The escape sequences for the function keys are terminfo capabilities kf1 trough kf10. On terminals without function key support, you can achieve the same functionality by pressing the ESC key and then a number in the range 1 through 9 and 0 (corresponding to F1 to F9 and F10 respectively). </p>
<p> The File menu has the following commands (keyboard shortcuts in parentheses): </p>
<p> <code>Help (F1)</code> </p>
<p> Invokes the built-in hypertext help viewer. Inside the help viewer, you can use the Tab key to select the next link and the Enter key to follow that link. The keys Space and Backspace are used to move forward and backward in a help page. Press F1 again to get the full list of accepted keys. </p>
<p> <code>Menu (F2)</code> </p>
<p> Invoke the user menu. The user menu provides an easy way to provide users with a menu and add extra features to the Midnight Commander. </p>
<p> <code>View (F3, F13)</code> </p>
<p> View the currently selected file. By default this invokes the Internal File Viewer but if the option &quot;Use internal view&quot; is off, it invokes an external file viewer specified by the <code>VIEWER</code> environment variable. If <code>VIEWER</code> is undefined, the <code>PAGER</code> environment variable is tried. If <code>PAGER</code> is also undefined, the &quot;view&quot; command is invoked. If you use F13 instead, the viewer will be invoked without doing any formatting or preprocessing to the file. </p>
<p> <code>Filtered View (Alt-!)</code> </p>
<p> This command prompts for a command and its arguments (the argument defaults to the currently selected file name), the output from such command is shown in the internal file viewer. </p>
<p> <code>Edit (F4, F14)</code> </p>
<p> Press F4 to edit the highlighted file. Press F14 (usually F14) to start the editor with a new, empty file. Currently they invoke the <code>vi</code> editor, or the editor specified in the <code>EDITOR</code> environment variable, or the Internal File Editor if the use_internal_edit option is on. </p>
<p> <code>Copy (F5, F15)</code> </p>
<p> Press F5 to pop up an input dialog to copy the currently selected file (or the tagged files, if there is at least one file tagged) to the directory/filename you specify in the input dialog. The destination defaults to the directory in the non-selected panel. Space for destination file may be preallocated relative to preallocate_space configure option. During this process, you can press C-c or ESC to abort the operation. For details about source mask (which will be usually either * or ^\(.*\)$ depending on setting of Use shell patterns) and possible wildcards in the destination see Mask copy/rename. </p>
<p> F15 (usually F15) is similar, but defaults to the directory in the selected panel. It always operates on the selected file, regardless of any tagged files. </p>
<p> On some systems, it is possible to do the copy in the background by clicking on the background button (or pressing Alt-b in the dialog box). The Background Jobs is used to control the background process. </p>
<p> <code>Link (C-x l)</code> </p>
<p> Create a hard link to the current file. </p>
<p> <code>Absolute symlink (C-x s)</code> </p>
<p> Create a absolute symbolic link to the current file. </p>
<p> <code>Relative symLink (C-x v)</code> </p>
<p> Create a relative symbolic link to the current file. </p>
<p> To those of you who don&#8217;t know what links are: creating a link to a file is a bit like copying the file, but both the source filename and the destination filename represent the same file image. For example, if you edit one of these files, all changes you make will appear in both files. Some people call links aliases or shortcuts. </p>
<p> A hard link appears as a real file. After making it, there is no way of telling which one is the original and which is the link. If you delete either one of them the other one is still intact. It is very difficult to notice that the files represent the same image. Use hard links when you don&#8217;t even want to know. </p>
<p> A symbolic link is a reference to the name of the original file. If the original file is deleted the symbolic link is useless. It is quite easy to notice that the files represent the same image. The Midnight Commander shows an &quot;@&quot;-sign in front of the file name if it is a symbolic link to somewhere (except to directory, where it shows a tilde (~)). The original file which the link points to is shown on mini-status line if the <i>Show mini-status</i> option is enabled. Use symbolic links when you want to avoid the confusion that can be caused by hard links. </p>
<p> When you press &quot;C-x s&quot; Midnight Commander will automatically fill in the complete path+filename of the original file and suggest a name for the link. You can change either one. </p>
<p> Sometimes you may want to change the absolute path of the original into a relative path. An absolute path starts from the root directory: </p>
<p> <i>/home/frodo/mc/mc -&gt; /home/frodo/new/mc</i> </p>
<p> A relative link describes the original file&#8217;s location starting from the location of the link itself: </p>
<p> <i>/home/frodo/mc/mc -&gt; ../new/mc</i> </p>
<p> You can force Midnight Commander to suggest a relative path by pressing &quot;C-x v&quot; instead of &quot;C-x s&quot;. </p>
<p> <code>Rename/Move (F6, F16)</code> </p>
<p> Press F6 to pop up an input dialog to copy the currently selected file (or the tagged files, if there is at least one file tagged) to the directory/filename you specify in the input dialog. The destination defaults to the directory in the non-selected panel. For more details look at Copy (F5) operation above, most of the things are quite similar. </p>
<p> F16 (usually F16) is similar, but defaults to the directory in the selected panel. It always operates on the selected file, regardless of any tagged files. </p>
<p> On some systems, it is possible to do the copy in the background by clicking on the background button (or pressing Alt-b in the dialog box). The Background Jobs is used to control the background process. </p>
<p> <code>Mkdir (F7)</code> </p>
<p> Pop up an input dialog and creates the directory specified. </p>
<p> <code>Delete (F8)</code> </p>
<p> Delete the currently selected file or the tagged files in the currently selected panel. During the process, you can press C-c or ESC to abort the operation. </p>
<p> <code>Quick cd (Alt-c)</code> Use the quick cd command if you have full command line and want to cd somewhere. </p>
<p> <code>Select group (+)</code> </p>
<p> This is used to select (tag) a group of files. The Midnight Commander will prompt for a selection options. When <i>Files only</i> checkbox is on, only files will be selected. If <i>Files only</i> is off, as files as directories will be selected. When <i>Shell Patterns</i> checkbox is on, the regular expression is much like the filename globbing in the shell (* standing for zero or more characters and ? standing for one character). If <i>Shell Patterns</i> is off, then the tagging of files is done with normal regular expressions (see ed (1)). When <i>Case sensitive</i> checkbox is on, the selection will be case sensitive characters. If <i>Case sensitive</i> is off, the case will be ignored. </p>
<p> <code>Unselect group (\)</code> </p>
<p> Used to unselect a group of files. This is the opposite of the <i>Select group</i> command. </p>
<p> <code>Quit (F10, Shift-F10)</code> </p>
<p> Terminate the Midnight Commander. Shift-F10 is used when you want to quit and you are using the shell wrapper. Shift-F10 will not take you to the last directory you visited with the Midnight Commander, instead it will stay at the directory where you started the Midnight Commander.</p>
<h2> Quick cd</h2>
<p> This command is useful if you have a full command line and want to cd somewhere without having to yank and paste the command line. This command pops up a small dialog, where you enter everything you would enter after <code>cd</code> on the command line and then you press enter. This features all the things that are already in the internal cd command.</p>
<h2> Command Menu</h2>
<p> The Directory tree command shows a tree figure of the directories. </p>
<p> The &quot;Find file&quot; command allows you to search for a specific file. </p>
<p> The &quot;Swap panels&quot; command swaps the contents of the two directory panels. </p>
<p> The &quot;Switch panels on/off&quot; command shows the output of the last shell command. This works only on xterm and on Linux and FreeBSD console. </p>
<p> The &quot;Compare directories&quot; command compares the directory panels with each other. You can then use the Copy (F5) command to make the panels identical. There are three compare methods. The quick method compares only file size and file date. The thorough method makes a full byte-by-byte compare. The thorough method is not available if the machine does not support the <a href="/docs/linux/man/2-mmap/">mmap</a>(2) system call. The size-only compare method just compares the file sizes and does not check the contents or the date times, it just checks the file size. </p>
<p> The &quot;External panelize&quot; allows you to execute an external program, and make the output of that program the contents of the current panel. </p>
<p> The &quot;Command history&quot; command shows a list of typed commands. The selected command is copied to the command line. The command history can also be accessed by typing Alt-p or Alt-n. </p>
<p> The &quot;Directory hotlist&quot; command makes changing of the current directory to often used directories faster. </p>
<p> The &quot;Screen list&quot; command shows a dialog window with the list of currently running internal editors, viewers and other MC modules that support this mode. </p>
<p> The &quot;Edit extension file&quot; command allows you to specify programs to executed when you try to execute, view, edit and do a bunch of other thing on files with certain extensions (filename endings). </p>
<p> The &quot;Edit menu file&quot; command may be used for editing the user menu (which appears by pressing F2).</p>
<h2> Directory Tree</h2>
<p> The Directory Tree command shows a tree figure of the directories. You can select a directory from the figure and the Midnight Commander will change to that directory. </p>
<p> There are two ways to invoke the tree. The real directory tree command is available from Commands menu. The other way is to select tree view from the Left or Right menu. </p>
<p> To get rid of long delays the Midnight Commander creates the tree figure by scanning only a small subset of all the directories. If the directory which you want to see is missing, move to its parent directory and press C-r (or F2). </p>
<p> You can use the following keys: </p>
<p> General movement keys are accepted. </p>
<p> <code>Enter.</code> In the directory tree, exits the directory tree and changes to this directory in the current panel. In the tree view, changes to this directory in the other panel and stays in tree view mode in the current panel. </p>
<p> <code>C-r, F2 (Rescan).</code> Rescan this directory. Use this when the tree figure is out of date: it is missing subdirectories or shows some subdirectories which don&#8217;t exist any more. </p>
<p> <code>F3 (Forget).</code> Delete this directory from the tree figure. Use this to remove clutter from the figure. If you want the directory back to the tree figure press F2 in its parent directory. </p>
<p> <code>F4 (Static/Dynamic).</code> Toggle between the dynamic navigation mode (default) and the static navigation mode. </p>
<p> In the static navigation mode you can use the Up and Down keys to select a directory. All known directories are shown. </p>
<p> In the dynamic navigation mode you can use the Up and Down keys to select a sibling directory, the Left key to move to the parent directory, and the Right key to move to a child directory. Only the parent, sibling and children directories are shown, others are left out. The tree figure changes dynamically as you traverse. </p>
<p> <code>F5 (Copy).</code> Copy the directory. </p>
<p> <code>F6 (RenMov).</code> Move the directory. </p>
<p> <code>F7 (Mkdir).</code> Make a new directory below this directory. </p>
<p> <code>F8 (Delete).</code> Delete this directory from the file system. </p>
<p> <code>C-s, Alt-s.</code> Search the next directory matching the search string. If there is no such directory these keys will move one line down. </p>
<p> <code>C-h, Backspace.</code> Delete the last character of the search string. </p>
<p> <code>Any other character.</code> Add the character to the search string and move to the next directory which starts with these characters. In the tree view you must first activate the search mode by pressing C-s. The search string is shown in the mini status line. </p>
<p> The following actions are available only in the directory tree. They aren&#8217;t supported in the tree view. </p>
<p> <code>F1 (Help).</code> Invoke the help viewer and show this section. </p>
<p> <code>Esc, F10.</code> Exit the directory tree. Do not change the directory. </p>
<p> The mouse is supported. A double-click behaves like Enter. See also the section on mouse support.</p>
<h2> Find File</h2>
<p> The Find File feature first asks for the start directory for the search and the filename to be searched for. By pressing the Tree button you can select the start directory from the directory tree figure. </p>
<p> Option form whole words. Like grep -w. </p>
<p> You can start the search by pressing the OK button. During the search you can stop from the Stop button and continue from the Start button. </p>
<p> You can browse the filelist with the up and down arrow keys. The Chdir button will change to the directory of the currently selected file. The Again button will ask for the parameters for a new search. The Quit button quits the search operation. The Panelize button will place the found files to the current directory panel so that you can do additional operations on them (view, copy, move, delete and so on). After panelizing you can press C-r to return to the normal file listing. </p>
<p> The &#8216;Enable ignore directories&#8217; checkbox and input field below it allow to set up the list of directories that should be skip during the search files (for example, you may want to avoid searches on a CD-ROM or on a NFS directory that is mounted across a slow link). List components must be separated with a colon, here is an example: </p>
<pre>
/cdrom:/nfs/wuarchive:/afs
</pre>
<p> Relative paths are supported also. The following example shows how to skip special directories of version control systems: </p>
<pre>
/cdrom:/nfs/wuarchive:/afs:.svn:.git:CVS
</pre>
<p> Attention: input field can contain a dot (.), this means the current absolute path. </p>
<p> You may consider using the External panelize command for some operations. Find file command is for simple queries only, while using External panelize you can do as mysterious searches as you would like.</p>
<h2> External panelize</h2>
<p> The External panelize allows you to execute an external program, and make the output of that program the contents of the current panel. </p>
<p> For example, if you want to manipulate in one of the panels all the symbolic links in the current directory, you can use external panelization to run the following command: </p>
<pre>
find . -type l -print
</pre>
<p> Upon command completion, the directory contents of the panel will no longer be the directory listing of the current directory, but all the files that are symbolic links. </p>
<p> If you want to panelize all of the files that have been downloaded from your FTP server, you can use this awk command to extract the file name from the transfer log files: </p>
<pre>
awk '$9 ~! /incoming/ { print $9 }' &lt; /var/log/xferlog
</pre>
<p> You may want to save often used panelize commands under a descriptive name, so that you can recall them quickly. You do this by typing the command on the input line and pressing Add new button. Then you enter a name under which you want the command to be saved. Next time, you just choose that command from the list and do not have to type it again.</p>
<h2> Hotlist</h2>
<p> The Directory hotlist command shows the labels of the directories in the directory hotlist. The Midnight Commander will change to the directory corresponding to the selected label. From the hotlist dialog, you can remove already created label/directory pairs and add new ones. To add new directories quickly, you can use the Add to hotlist command (C-x h), which adds the current directory into the directory hotlist, asking just for the label for the directory. </p>
<p> This makes cd to often used directories faster. You may consider using the CDPATH variable as described in internal cd command description.</p>
<h2> Extension File Edit</h2>
<p> This will invoke your editor on the file <i>~/.config/mc/mc.ext</i>. The format of this file following: </p>
<p> All lines starting with # or empty lines are thrown away. </p>
<p> Lines starting in the first column should have following format: </p>
<p> <i>keyword/expr</i>, i.e. everything after the slash until new line is <i>expr</i>. </p>
<p> <i>keyword</i> can be:</p>
<dl>
<dt><i>shell</i></p>
<dd> &#8211; <i>expr</i> is an extension (no wildcards). File matches it its name ends with <i>expr</i>. Example: <i>shell/.tar</i> matches <i>*.tar</i>.</p>
<dt><i>regex</i></p>
<dd> &#8211; <i>expr</i> is a regular expression. File matches if its name matches the regular expression.</p>
<dt><i>directory</i></p>
<dd> &#8211; <i>expr</i> is a regular expression. File matches if it is a directory and its name matches the regular expression.</p>
<dt><i>type</i></p>
<dd> &#8211; <i>expr</i> is a regular expression. File matches if the output of <i>file %f</i> without the initial &quot;filename:&quot; part matches regular expression <i>expr</i>.</p>
<dt><i>default</i></p>
<dd> &#8211; matches any file. <i>expr</i> is ignored.</p>
<dt><i>include</i></p>
<dd> &#8211; denotes a common section. <i>expr</i> is the name of the section.</dl>
<p> Other lines should start with a space or tab and should be of the format: <i>keyword=command</i> (with no spaces around =), where <i>keyword</i> should be: <i>Open</i> (invoked on Enter or double click), <i>View</i> (F3), <i>Edit</i> (F4) or <i>Include</i> (to add rules from the common section). <i>command</i> is any one-line shell command, with the simple macro substitution. </p>
<p> Rules are matched from top to bottom, thus the order is important. If the appropriate action is missing, search continues as if this rule didn&#8217;t match (i.e. if a file matches the first and second entry and View action is missing in the first one, then on pressing F3 the View action from the second entry will be used). <i>default</i> should match all the actions.</p>
<h2> Background Jobs</h2>
<p> This lets you control the state of any background Midnight Commander process (only copy and move files operations can be done in the background). You can stop, restart and kill a background job from here.</p>
<h2> Menu File Edit</h2>
<p> The user menu is a menu of useful actions that can be customized by the user. When you access the user menu, the file .mc.menu from the current directory is used if it exists, but only if it is owned by user or root and is not world-writable. If no such file found, ~/.config/mc/menu is tried in the same way, and otherwise mc uses the default system-wide menu /usr/share/mc/mc.menu. </p>
<p> The format of the menu file is very simple. Lines that start with anything but space or tab are considered entries for the menu (in order to be able to use it like a hot key, the first character should be a letter). All the lines that start with a space or a tab are the commands that will be executed when the entry is selected. </p>
<p> When an option is selected all the command lines of the option are copied to a temporary file in the temporary directory (usually /usr/tmp) and then that file is executed. This allows the user to put normal shell constructs in the menus. Also simple macro substitution takes place before executing the menu code. For more information, see macro substitution. </p>
<p> Here is a sample mc.menu file: </p>
<pre><code>
A Dump the currently selected file
        od -
    c % f
            B Edit a bug report and send it to root
                I =`mktemp ${MC_TMPDIR : - / tmp} / mail.XXXXXX` || exit 1 vi $I
                                                                                    mail -
                                                                                s "Midnight Commander bug" root &lt;
                                                                            $I
                                                                                    rm -
                                                                                f $I
                                                                                    M Read mail
                                                                                        emacs -
                                                                                f rmail
                                                                                    N Read Usenet news
                                                                                        emacs -
                                                                                f gnus
                                                                                    H Call the info hypertext browser
                                                                                        info
                                                                                            J Copy current directory to other panel recursively
                                                                                                tar cf -
                                                                                                    .|
                                                                        (cd % D &amp;&amp; tar xvpf -)
                                                                                K Make a release of the current subdirectory
                                                                                    echo -
                                                                            n "Name of distribution file: " read tar
                                                                                ln -
                                                                            s % d `dirname % d`/ $tar cd..tar cvhf ${tar}.tar $tar = f *.tar.gz | f *.tgz &amp; t n
                                                                                                                                                                    X Extract the contents of a compressed tar file
                                                                                                                                                                        tar xzvf %
                                                                                                                                                                f
</code></pre>
<p> <code>Default Conditions</code> </p>
<p> Each menu entry may be preceded by a condition. The condition must start from the first column with a &#8216;=&#8217; character. If the condition is true, the menu entry will be the default entry. </p>
<pre>
Condition syntax:       = &lt;sub-cond&gt;
  or:                   = &lt;sub-cond&gt; | &lt;sub-cond&gt; ...
  or:                   = &lt;sub-cond&gt; &amp; &lt;sub-cond&gt; ...
Sub-condition is one of following:
  y &lt;pattern&gt;           syntax of current file matching pattern?
                        (for edit menu only)
  f &lt;pattern&gt;           current file matching pattern?
  F &lt;pattern&gt;           other file matching pattern?
  d &lt;pattern&gt;           current directory matching pattern?
  D &lt;pattern&gt;           other directory matching pattern?
  t &lt;type&gt;              current file of type?
  T &lt;type&gt;              other file of type?
  x &lt;filename&gt;          is it executable filename?
  ! &lt;sub-cond&gt;          negate the result of sub-condition
</pre>
<p> Pattern is a normal shell pattern or a regular expression, according to the shell patterns option. You can override the global value of the shell patterns option by writing &quot;shell_patterns=x&quot; on the first line of the menu file (where &quot;x&quot; is either 0 or 1). </p>
<p> Type is one or more of the following characters: </p>
<pre>
  n     not a directory
  r     regular file
  d     directory
  l     link
  c     character device
  b     block device
  f     FIFO (pipe)
  s     socket
  x     executable file
  t     tagged
</pre>
<p> For example &#8216;rlf&#8217; means either regular file, link or fifo. The &#8216;t&#8217; type is a little special because it acts on the panel instead of the file. The condition &#8216;=t t&#8217; is true if there are tagged files in the current panel and false if not. </p>
<p> If the condition starts with &#8216;=?&#8217; instead of &#8216;=&#8217; a debug trace will be shown whenever the value of the condition is calculated. </p>
<p> The conditions are calculated from left to right. This means </p>
<pre>
        = f *.tar.gz | f *.tgz &amp; t n
</pre>
<p> is calculated as </p>
<pre>
        ( (f *.tar.gz) | (f *.tgz) ) &amp; (t n)
</pre>
<p> Here is a sample of the use of conditions: </p>
<pre>
= f *.tar.gz | f *.tgz &amp; t n
L       List the contents of a compressed tar-archive
        gzip -cd %f | tar xvf -
</pre>
<p> <code>Addition Conditions</code> </p>
<p> If the condition begins with &#8216;+&#8217; (or &#8216;+?&#8217;) instead of &#8216;=&#8217; (or &#8216;=?&#8217;) it is an addition condition. If the condition is true the menu entry will be included in the menu. If the condition is false the menu entry will not be included in the menu. </p>
<p> You can combine default and addition conditions by starting condition with &#8216;+=&#8217; or &#8216;=+&#8217; (or &#8216;+=?&#8217; or &#8216;=+?&#8217; if you want debug trace). If you want to use two different conditions, one for adding and another for defaulting, you can precede a menu entry with two condition lines, one starting with &#8216;+&#8217; and another starting with &#8216;=&#8217;. </p>
<p> Comments are started with &#8216;#&#8217;. The additional comment lines must start with &#8216;#&#8217;, space or tab.</p>
<h2> Options Menu</h2>
<p> The Midnight Commander has some options that may be toggled on and off in several dialogs which are accessible from this menu. Options are enabled if they have an asterisk or &quot;x&quot; in front of them. </p>
<p> The Configuration command pops up a dialog from which you can change most of settings of the Midnight Commander. </p>
<p> The Layout command pops up a dialog from which you specify a bunch of options how mc looks like on the screen. </p>
<p> The Panel options command pops up a dialog from which you specify options of file manager panels. </p>
<p> The Confirmation command pops up a dialog from which you specify which actions you want to confirm. </p>
<p> The Display bits command pops up a dialog from which you may select which characters is your terminal able to display. </p>
<p> The Learn keys command pops up a dialog from which you test some keys which are not working on some terminals and you may fix them. </p>
<p> The Virtual FS command pops up a dialog from which you specify some VFS related options. </p>
<p> The Save setup command saves the current settings of the Left, Right and Options menus. A small number of other settings is saved, too.</p>
<h2> Configuration</h2>
<p> The options in this dialog are divided into several groups: &quot;File operation options&quot;, &quot;Esc key mode&quot;, &quot;Pause after run&quot; and &quot;Other options&quot;. </p>
<p> <code>File operation options</code> </p>
<p> <i>Verbose operation.</i> This toggles whether the file Copy, Rename and Delete operations are verbose (i.e., display a dialog box for each operation). If you have a slow terminal, you may wish to disable the verbose operation. It is automatically turned off if the speed of your terminal is less than 9600 bps. </p>
<p> <i>Compute totals.</i> If this option is enabled, the Midnight Commander computes total byte sizes and total number of files prior to any Copy, Rename and Delete operations. This will provide you with a more accurate progress bar at the expense of some speed. This option has no effect, if <i>Verbose operation</i> is disabled. </p>
<p> <i>Classic progressbar.</i> If this option is enabled, the progressbar of Copy/Move/Delete operations is always grown form left to right. If disabled, the growing direction of progressbar follows to direction of Copy/Move/Delete operation: from left panel to right one and vice versa. Enabled by default. </p>
<p> <i>Mkdir autoname</i> When you press F7 to create a new directory, the input line in popup dialog will be filled by name of current file or directory in active panel. Disabled by default. </p>
<p> <i>Preallocate space</i> Preallocate space for whole target file, if possible, before copy operation. Disabled by default. </p>
<p> <code>Esc key mode.</code> </p>
<p> By default the Midnight Commander treats the ESC key as a key prefix. Therefore, you should press Esc code twice to exit a dialog. But there is a possibility to use a single press of ESC key for that action. </p>
<p> <i>Single press.</i> By default this option is disabled. If you&#8217;ll enable it, the ESC key will act as a prefix key for set up time interval (see <i>Timeout</i> option below), and if no extra keys have arrived, then the ESC key is interpreted as a cancel key (ESC ESC). </p>
<p> <i>Timeout.</i> This options is used to setup the time interval (in microseconds) for single press of ESC key. By default, this inrerval is one second (1000000 microseconds). Also the timeout can be set via KEYBOARD_KEY_TIMEOUT_US environment variable (also in microseconds), which has higher priority than Timeout option value. </p>
<p> <code>Pause after run</code> </p>
<p> After executing your commands, the Midnight Commander can pause, so that you can examine the output of the command. There are three possible settings for this variable: </p>
<p> <i>Never</i>. Means that you do not want to see the output of your command. If you are using the Linux or FreeBSD console or an xterm, you will be able to see the output of the command by typing C-o. </p>
<p> <i>On</i>dumb<i>terminals</i>. You will get the pause message on terminals that are not capable of showing the output of the last command executed (any terminal that is not an xterm or the Linux console). </p>
<p> <i>Always</i>. The program will pause after executing all of your commands. </p>
<p> <code>Other options</code> </p>
<p> <i>Use internal editor.</i> If this option is enabled, the built-in file editor is used to edit files. If the option is disabled, the editor specified in the <code>EDITOR</code> environment variable is used. If no editor is specified, <code>vi</code> is used. See the section on the internal file editor. </p>
<p> <i>Use internal viewer.</i> If this option is enabled, the built-in file viewer is used to view files. If the option is disabled, the pager specified in the <code>PAGER</code> environment variable is used. If no pager is specified, the <code>view</code> command is used. See the section on the internal file viewer. </p>
<p> <i>Auto menus.</i> If this option is enabled, the user menu will be invoked at startup. Useful for building menus for non-unixers. </p>
<p> <i>Drop down menus.</i> When this option is enabled, the pull down menus will be activated as soon as you press the F9 key. Otherwise, you will only get the menu title, and you will have to activate the menu either with the arrow keys or with the hotkeys. It is recommended if you are using hotkeys. </p>
<p> <i>Shell Patterns.</i> By default the Select, Unselect and Filter commands will use shell-like regular expressions. The following conversions are performed to achieve this: the &#8216;*&#8217; is replaced by &#8216;.*&#8217; (zero or more characters); the &#8216;?&#8217; is replaced by &#8216;.&#8217; (exactly one character) and &#8216;.&#8217; by the literal dot. If the option is disabled, then the regular expressions are the ones described in <a href="/docs/linux/man/1-ed/">ed</a>(1). </p>
<p> <i>Complete: show all.</i> By default the Midnight Commander pops up all possible completions if the completion is ambiguous only when you press <code>Alt-Tab</code> for the second time. For the first time, it just completes as much as possible and beeps in the case of ambiguity. Enable this option if you want to see all possible completions even after pressing <code>Alt-Tab</code> the first time. </p>
<p> <i>Rotating dash.</i> If this option is enabled, the Midnight Commander shows a rotating dash in the upper right corner as a work in progress indicator. </p>
<p> <i>Cd follows links.</i> This option, if set, causes the Midnight Commander to follow the logical chain of directories when changing current directory either in the panels, or using the cd command. This is the default behavior of bash. When unset, the Midnight Commander follows the real directory structure, so cd .. if you&#8217;ve entered that directory through a link will move you to the current directory&#8217;s real parent and not to the directory where the link was present. </p>
<p> <i>Safe delete.</i> If this option is enabled, deleting files and directory hotlist entries unintentionally becomes more difficult. The default selection in the confirmation dialogs for deletion changes from &quot;Yes&quot; to &quot;No&quot;. This option is disabled by default. </p>
<p> <i>Auto save setup.</i> If this option is enabled, when you exit the Midnight Commander the configurable options of the Midnight Commander are saved in the ~/.config/mc/ini file.</p>
<h2> Layout</h2>
<p> The layout dialog gives you a possibility to change the general layout of screen. The options in this dialog are divided into several groups: &quot;Panel split&quot;, &quot;Console output&quot; and &quot;Other options&quot;. </p>
<p> <code>Panel split</code> </p>
<p> The rest of the screen area is used for the two directory panels. You can specify whether the area is split to the panels in <i>Vertical</i><br />
&nbsp;<wbr>or <i>Horizontal</i> direction. Panel layout can be changed using Alt-, (Alt-comma) shortcut. </p>
<p> <i>Equal split.</i> By default, panels have equal sizes. Using this option you can specify an unequal split. </p>
<p> <code>Console output</code> </p>
<p> On the Linux or FreeBSD console you can specify how many lines are shown in the output window. This option is available if Midnight Commander runs on native console only. </p>
<p> <code>Other options</code> </p>
<p> <i>Menu bar visible.</i> If enabled, main menu of Midnight Commander is always visible on the top row of screen above panels. Enabled by default. </p>
<p> <i>Command prompt.</i> If enabled, command line is avalable. Enabled by default. </p>
<p> <i>Keybar visible.</i> If enabled, 10 lables associated with F1-F10 keys are located at the bottom row of screen. Enabled by default. </p>
<p> <i>Hintbar visible.</i> If enabled, the one-line hints are visible below panels. Enabled by default. </p>
<p> <i>XTerm window title.</i> When run in a terminal emulator for X11, Midnight Commander sets the terminal window title to the current working directory and updates it when necessary. If your terminal emulator is broken and you see some incorrect output on startup and directory change, turn off this option. Enabled by default. </p>
<p> <i>Show free space.</i> If enabled, free space and total space of current file system is shown at the bottom frame of panel. Enabled by default.</p>
<h2> Panel options</h2>
<p> <code>Main panel options</code> </p>
<p> <i>Show mini-status.</i> If enabled, one line of status information about the currently selected item is shown at the bottom of the panels. Enabled by default. </p>
<p> <i>Use SI size units.</i> If this option is enabled, Midnight Commander will use SI units (powers of 1000) when displaying any byte sizes. The suffixes (k, m &#8230;) are shown in lowercase. If disabled (default), Midnight Commander will use binary units (powers of 1024) and the suffixes are shown in upper case (K, M &#8230;) </p>
<p> <i>Mix all files.</i> If this option is enabled, all files and directories are shown mixed together. If the option is desabled (default), directories (and links to directories) are shown at the beginning of the listing, and other files below. </p>
<p> <i>Show backup files.</i> If enabled, the Midnight Commander will show files ending with a tilde. Otherwise, they won&#8217;t be shown (like GNU&#8217;s ls option -B). Enabled by default. </p>
<p> <i>Show hidden files.</i> If enabled, the Midnight Commander will show all files that start with a dot (like ls -a). Disabled by default. </p>
<p> <i>Fast directory reload.</i> If this option is enabled, the Midnight Commander will use a trick to determine if the directory contents have changed. The trick is to reload the directory only if the i-node of the directory has changed; this means that reloads only happen when files are created or deleted. If what changes is the i-node for a file in the directory (file size changes, mode or owner changes, etc) the display is not updated. In these cases, if you have the option on, you have to rescan the directory manually (with C-r). Disabled by default. </p>
<p> <i>Mark moves down.</i> If enabled, the selection bar will move down when you mark a file (with Insert key). Enabled by default. </p>
<p> <i>Reverse files only.</i> Allow revert selection of files only. Enabled by default. If enabled, the reverse selection is applied to files only, not to directories. The selection of directories is untouched. If off, the reverse selection is applied to files as well to directories: all unselected items become selected, and vice versa. </p>
<p> <i>Simple swap.</i> If both panels contain file listing, simple swap means that panels exchange its screen positions: left panel become right one, and vice versa. If this option is unchecked, file listing panels exchange its content keeping listing format and sort options. Unchecked by default. </p>
<p> <i>Auto save panels setup.</i> If this option is enabled, when you exit the Midnight Commander the current settings of panels are saved in the ~/.config/mc/panels.ini file. Disabled by default. </p>
<p> <code>Navigation</code> </p>
<p> <i>Lynx-like motion.</i> If this option is enabled, you may use the arrows keys to automatically chdir if the current selection is a subdirectory and the shell command line is empty. By default, this setting is off. </p>
<p> <i>Page scrolling.</i> If set (the default), panel will scroll by half the display when the cursor reaches the end or the beginning of the panel, otherwise it will just scroll a file at a time. </p>
<p> <i>Mouse page scrolling.</i> Controls whenever scrolling with the mouse wheel is done by pages or line by line on the panels. </p>
<p> <code>File highlight</code> </p>
<p> You can specify whether <i>permissions</i> and <i>file types</i> should be highlighted with distinctive Colors. If the permission highlighting is enabled, the parts of the <i>perm</i> and <i>mode</i> display fields which apply to the user running Midnight Commander are highlighted with the color defined by the <i>selected</i> keyword. If the file type highlighting is enabled, file names are colored according to rules described in /etc/mc/filehighlight.ini file. See Filenames Highlight for more info. </p>
<p> <code>Quick search</code> </p>
<p> You can specify how the Quick search mode should work: case insensitively, case sensitively or be matched to the panel sort order: case sensitive or not.</p>
<h2> Confirmation</h2>
<p> In this dialog you configure the confirmation options for file deletion, overwriting files, execution by pressing enter, quitting the program, directory hotlist entries deletion and history cleanup.<br />
&nbsp;<wbr>and.</p>
<h2> Display bits</h2>
<p> This is used to configure the range of visible characters on the screen. This setting may be 7-bits if your terminal/curses supports only seven output bits, ISO-8859-1 displays all the characters in the ISO-8859-1 map and full 8 bits is for those terminals that can display full 8 bit characters.</p>
<h2> Learn keys</h2>
<p> This dialog allows you to test and redefine functional keys, cursor arrows and some other keys to make them work properly on your terminal. They often don&#8217;t, since many terminal databases are incomplete or broken. </p>
<p> You can move around with the Tab key and with the vi moving keys (&#8216;h&#8217; left, &#8216;j&#8217; down, &#8216;k&#8217; up and &#8216;l&#8217; right). Once you press any cursor movement key and it is recognized, you can use that key as well. </p>
<p> You can test keys just by pressing each of them. When you press a key and it is recognized properly, OK should appear next to the name of that key. Once a key is marked OK it starts working as usually, e.g. F1 pressed the first time will just check that the F1 key works, but after that it will show help. The same applies to the arrow keys. The Tab key should be working always. </p>
<p> If some keys do not work properly then you won&#8217;t see OK appear after pressing one of these. Then you may want to redefine it. Do it by pressing the button with the name of that key (either by the mouse or by Enter or Space after selecting the button with Tab or arrows). Then a message box will appear asking you to press that key. Do it and wait until the message box disappears. If you want to abort, just press Escape once and wait. </p>
<p> When you finish with all the keys, you can Save them. The definitions for the keys you have redefined will be written into the [terminal:TERM] section of your ~/.config/mc/ini file (where TERM is the name of your current terminal). The definitions of the keys that were already working properly are not saved.</p>
<h2> Virtual FS</h2>
<p> This option gives you control over the settings of the Virtual File System. </p>
<p> The Midnight Commander keeps in memory the information related to some of the virtual file systems to speed up the access to the files in the file system (for example, directory listings fetched from FTP servers). </p>
<p> Also, in order to access the contents of compressed files (for example, compressed tar files) the Midnight Commander needs to create temporary uncompressed files on your disk. </p>
<p> Since both the information in memory and the temporary files on disk take up resources, you may want to tune the parameters of the cached information to decrease your resource usage or to maximize the speed of access to frequently used file systems. </p>
<p> Because of the format of the tar archives, the <i>Tar filesystem</i> needs to read the whole file just to load the file entries. Since most tar files are usually kept compressed (plain tar files are species in extinction), the tar file system has to uncompress the file on the disk in a temporary location and then access the uncompressed file as a regular tar file. </p>
<p> Now, since we all love to browse files and tar files all over the disk, it&#8217;s common that you will leave a tar file and then re-enter it later. Since decompression is slow, the Midnight Commander will cache the information in memory for a limited time. When the timeout expires, all the resources associated with the file system are released. The default timeout is set to one minute. </p>
<p> The FTP File System (ftpfs) allows you to browse directories on remote FTP servers. It has several options. </p>
<p> <i>ftp anonymous password</i> is the password used when you login as &quot;anonymous&quot;. Some sites require a valid e-mail address. On the other hand, you probably don&#8217;t want to give your real e-mail address to untrusted sites, especially if you are not using spam filtering. </p>
<p> ftpfs keeps the directory listing it fetches from a FTP server in a cache. The cache expire time is configurable with the <i>ftpfs directory cache timeout</i> option. A low value for this option may slow down every operation on the ftpfs because every operation would require sending a request to the FTP server. </p>
<p> You can define an FTP proxy host for doing FTP. Note that most modern firewalls are fully transparent at least for passive FTP (see below), so FTP proxies are considered obsolete. </p>
<p> If <i>Always use ftp proxy</i> is not set, you can use the exclamation sign to enable proxy for certain hosts. See FTP File System for examples. </p>
<p> If this option is set, the program will do two things: consult the /usr/lib/mc/mc.no_proxy file for lines containing host names that are local (if the host name starts with a dot, it is assumed to be a domain) and to assume that any hostnames without dots in their names are directly accessible. All other hosts will be accessed through the specified FTP proxy. </p>
<p> You can enable using <i>~/.netrc</i> file, which keeps login names and passwords for ftp servers. See netrc (5) for the description of the .netrc format. </p>
<p> <i>Use passive mode</i> enables using FTP passive mode, when the connection for data transfer is initiated by the client, not by the server. This option is recommended and enabled by default. If this option is turned off, the data connection is initiated by the server. This may not work with some firewalls.</p>
<h2> Save Setup</h2>
<p> At startup the Midnight Commander will try to load initialization information from the ~/.config/mc/ini file. If this file doesn&#8217;t exist, it will load the information from the system-wide configuration file, located in /usr/share/mc/mc.ini. If the system-wide configuration file doesn&#8217;t exist, MC uses the default settings. </p>
<p> The <i>Save Setup</i> command creates the ~/.config/mc/ini file by saving the current settings of the Left, Right and Options menus. </p>
<p> If you activate the <i>auto save setup</i> option, MC will always save the current settings when exiting. </p>
<p> There also exist settings which can&#8217;t be changed from the menus. To change these settings you have to edit the setup file with your favorite editor. See the section on Special Settings for more information.</p>
<h2></h2>
<h2>Executing operating system commands</h2>
<p> You may execute commands by typing them directly in the Midnight Commander&#8217;s input line, or by selecting the program you want to execute with the selection bar in one of the panels and hitting Enter. </p>
<p> If you press Enter over a file that is not executable, the Midnight Commander checks the extension of the selected file against the extensions in the Extensions File. If a match is found then the code associated with that extension is executed. A very simple macro expansion takes place before executing the command.</p>
<h2> The cd internal command</h2>
<p> The <i>cd</i> command is interpreted by the Midnight Commander, it is not passed to the command shell for execution. Thus it may not handle all of the nice macro expansion and substitution that your shell does, although it does some of them: </p>
<p> <i>Tilde substitution.</i> The (~) will be substituted with your home directory, if you append a username after the tilde, then it will be substituted with the login directory of the specified user. </p>
<p> For example, ~guest is the home directory for the user guest, while ~/guest is the directory guest in your home directory. </p>
<p> <i>Previous directory.</i> You can jump to the directory you were previously by using the special directory name &#8216;-&#8216; like this: <code>cd &#8211;</code> </p>
<p> <i>CDPATH directories.</i> If the directory specified to the <code>cd</code> command is not in the current directory, then The Midnight Commander uses the value in the environment variable <code>CDPATH</code> to search for the directory in any of the named directories. </p>
<p> For example you could set your <code>CDPATH</code> variable to ~/src:/usr/src, allowing you to change your directory to any of the directories inside the ~/src and /usr/src directories, from any place in the file system by using its relative name (for example cd linux could take you to /usr/src/linux).</p>
<h2> Macro Substitution</h2>
<p> When accessing a user menu, or executing an extension dependent command, or running a command from the command line input, a simple macro substitution takes place. </p>
<p> The macros are:</p>
<dl>
<dt><i>%i</i></p>
<dd> The indent of blank space, equal the cursor column position. For edit menu only.</p>
<dt><i>%y</i></p>
<dd> The syntax type of current file. For edit menu only.</p>
<dt><i>%k</i></p>
<dd> The block file name.</p>
<dt><i>%e</i></p>
<dd> The error file name.</p>
<dt><i>%m</i></p>
<dd> The current menu name.</p>
<dt><i>%f</i> and <i>%p</i></p>
<dd> The current file name.</p>
<dt><i>%x</i></p>
<dd> The extension of current file name.</p>
<dt><i>%b</i></p>
<dd> The current file name without extension.</p>
<dt><i>%d</i></p>
<dd> The current directory name.</p>
<dt><i>%F</i></p>
<dd> The current file in the unselected panel.</p>
<dt><i>%D</i></p>
<dd> The directory name of the unselected panel.</p>
<dt><i>%t</i></p>
<dd> The currently tagged files.</p>
<dt><i>%T</i></p>
<dd> The tagged files in the unselected panel.</p>
<dt><i>%u</i> and <i>%U</i></p>
<dd> Similar to the %t and %T macros, but in addition the files are untagged. You can use this macro only once per menu file entry or extension file entry, because next time there will be no tagged files.</p>
<dt><i>%s</i> and <i>%S</i></p>
<dd> The selected files: The tagged files if there are any. Otherwise the current file.</p>
<dt><i>%cd</i></p>
<dd> This is a special macro that is used to change the current directory to the directory specified in front of it. This is used primarily as an interface to the Virtual File System.</p>
<dt><i>%view</i></p>
<dd> This macro is used to invoke the internal viewer. This macro can be used alone, or with arguments. If you pass any arguments to this macro, they should be enclosed in brackets.</p>
<dt>
<dd> The arguments are: <i>ascii</i> to force the viewer into ascii mode; <i>hex</i> to force the viewer into hex mode; <i>nroff</i> to tell the viewer that it should interpret the bold and underline sequences of nroff; <i>unformatted</i> to tell the viewer to not interpret nroff commands for making the text bold or underlined.</p>
<dt><i>%%</i></p>
<dd> The % character</p>
<dt><i>%{some text}</i></p>
<dd> Prompt for the substitution. An input box is shown and the text inside the braces is used as a prompt. The macro is substituted by the text typed by the user. The user can press ESC or F10 to cancel. This macro doesn&#8217;t work on the command line yet.</p>
<dt><i>%var{ENV:default}</i></p>
<dd> If environment variable <i>ENV</i> is unset, the <i>default</i> is substituted. Otherwise, the value of <i>ENV</i> is substituted.</dl>
<h2> The subshell support</h2>
<p> The subshell support is a compile time option, that works with the shells: bash, tcsh and zsh. </p>
<p> When the subshell code is activated the Midnight Commander will spawn a concurrent copy of your shell (the one defined in the <code>SHELL</code> variable and if it is not defined, then the one in the /etc/passwd file) and run it in a pseudo terminal, instead of invoking a new shell each time you execute a command, the command will be passed to the subshell as if you had typed it. This also allows you to change the environment variables, use shell functions and define aliases that are valid until you quit the Midnight Commander. </p>
<p> If you are using <code>bash</code> you can specify startup commands for the subshell in your ~/.local/share/mc/bashrc file and special keyboard maps in the ~/.local/share/mc/inputrc file. <code>tcsh</code> users may specify startup commands in the ~/.local/share/mc/tcshrc file. </p>
<p> When the subshell code is used, you can suspend applications at any time with the sequence C-o and jump back to the Midnight Commander, if you interrupt an application, you will not be able to run other external commands until you quit the application you interrupted. </p>
<p> An extra added feature of using the subshell is that the prompt displayed by the Midnight Commander is the same prompt that you are currently using in your shell. </p>
<p> The OPTIONS section has more information on how you can control the subshell code.</p>
<h2>Chmod</h2>
<p> The Chmod window is used to change the attribute bits in a group of files and directories. It can be invoked with the C-x c key combination. </p>
<p> The Chmod window has two parts &#8211; <i>Permissions</i> and <i>File</i>. </p>
<p> In the File section are displayed the name of the file or directory and its permissions in octal form, as well as its owner and group. </p>
<p> In the Permissions section there is a set of check buttons which correspond to the file attribute bits. As you change the attribute bits, you can see the octal value change in the File section. </p>
<p> To move between the widgets (buttons and check buttons) use the <i>arrow keys</i> or the <i>Tab</i> key. To change the state of the check buttons or to select a button use <i>Space.</i> You can also use the hotkeys on the buttons to quickly activate them. Hotkeys are shown as highlighted letters on the buttons. </p>
<p> To set the attribute bits, use the Enter key. </p>
<p> When working with a group of files or directories, you just click on the bits you want to set or clear. Once you have selected the bits you want to change, you select one of the action buttons (Set marked or Clear marked). </p>
<p> Finally, to set the attributes exactly to those specified, you can use the <code>[Set all]</code> button, which will act on all the tagged files. </p>
<p> <code>[Marked all]</code> set only marked attributes to all selected files </p>
<p> <code>[Set marked]</code> set marked bits in attributes of all selected files </p>
<p> <code>[Clean marked]</code> clear marked bits in attributes of all selected files </p>
<p> <code>[Set]</code> set the attributes of one file </p>
<p> <code>[Cancel]</code> cancel the Chmod command</p>
<h2>Chown</h2>
<p> The Chown command is used to change the owner/group of a file. The hot key for this command is C-x o.</p>
<h2>Advanced Chown</h2>
<p> The Advanced Chown command is the Chmod and Chown command combined into one window. You can change the permissions and owner/group of files at once.</p>
<h2>File Operations</h2>
<p> When you copy, move or delete files the Midnight Commander shows the file operations dialog. It shows the files currently being processed and uses up to three progress bars. The file bar indicates the percentage of the current file that has been processed so far. The count bar shows how many of the tagged files have been handled. The bytes bar indicates the percentage of the total size of the tagged files that has been handled. If the verbose option is off, the file and bytes bars are not shown. </p>
<p> There are two buttons at the bottom of the dialog. Pressing the Skip button will skip the rest of the current file. Pressing the Abort button will abort the whole operation, the rest of the files are skipped. </p>
<p> There are three other dialogs which you can run into during the file operations. </p>
<p> The error dialog informs about error conditions and has three choices. Normally you select either the Skip button to skip the file or the Abort button to abort the operation altogether. You can also select the Retry button if you fixed the problem from another terminal. </p>
<p> The replace dialog is shown when you attempt to copy or move a file on the top of an existing file. The dialog shows the dates and sizes of the both files. Press the Yes button to overwrite the file, the No button to skip the file, the All button to overwrite all the files, the None button to never overwrite and the Update button to overwrite if the source file is newer than the target file. You can abort the whole operation by pressing the Abort button. </p>
<p> The recursive delete dialog is shown when you try to delete a directory which is not empty. Press the Yes button to delete the directory recursively, the No button to skip the directory, the All button to delete all the directories and the None button to skip all the non-empty directories. You can abort the whole operation by pressing the Abort button. If you selected the Yes or All button you will be asked for a confirmation. Type &quot;yes&quot; only if you are really sure you want to do the recursive delete. </p>
<p> If you have tagged files and perform an operation on them only the files on which the operation succeeded are untagged. Failed and skipped files are left tagged.</p>
<h2>Mask Copy/Rename</h2>
<p> The copy/move operations let you translate the names of files in an easy way. To do it, you have to specify the correct source mask and usually in the trailing part of the destination specify some wildcards. All the files matching the source mask are copied/renamed according to the target mask. If there are tagged files, only the tagged files matching the source mask are renamed. </p>
<p> There are other options which you can set: </p>
<p> <code>Follow links</code> </p>
<p> determines whether make the symlinks and hardlinks in the source directory (recursively in subdirectories) new links in the target directory or whether would you like to copy their content. </p>
<p> <code>Dive into subdirs</code> </p>
<p> determines the behavior when the source directory is about to be copied, but the target directory already exists. The default action is to copy the contents of the source directory into the target directory. Enabling this option causes copying the source directory itself into the target directory. </p>
<p> For example, you want to copy directory <i>/foo</i> containing file <i>bar</i> to <i>/bla/foo</i>, which is an already existing directory. Normally (when <code>Dive into subdirs</code> is not set), mc would copy file <i>/foo/bar</i> into the file <i>/bla/foo/bar</i>. By enabling this option the <i>/bla/foo/foo</i> directory will be created, and <i>/foo/bar</i> will be copied into <i>/bla/foo/foo/bar</i>. </p>
<p> <code>Preserve attributes</code> </p>
<p> determines whether to preserve the permissions, timestamps and (if you are root) the ownership of the original files. If this option is not set, the current value of the umask will be respected. </p>
<p> <code>Use shell patterns</code> </p>
<p> When this option is on you can use the &#8216;*&#8217; and &#8216;?&#8217; wildcards in the source mask. They work like they do in the shell. In the target mask only the &#8216;*&#8217; and &#8216;\&lt;digit&gt;&#8217; wildcards are allowed. The first &#8216;*&#8217; wildcard in the target mask corresponds to the first wildcard group in the source mask, the second &#8216;*&#8217; corresponds to the second group and so on. The &#8216;\1&#8217; wildcard corresponds to the first wildcard group in the source mask, the &#8216;\2&#8217; wildcard corresponds to the second group and so on all the way up to &#8216;\9&#8217;. The &#8216;
