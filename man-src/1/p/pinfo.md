---
title: "pinfo(1)"
name: "pinfo"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pinfo/"
description: "pinfo – curses based lynx-style info browser"
---

<h2>NAME</h2>
<p> <code>pinfo</code> &#8211; curses based lynx-style info browser</p>
<h2>SYNTAX</h2>
<p> <code>pinfo </code> [<i>options</i>] [<code>infopage</code>]</p>
<h2>DESCRIPTION</h2>
<p> This is a program for viewing info files. You specify which page you want to read by passing it an <i>infopage</i> argument. This argument contains the name of an info page (i.e. &#8216;bash&#8217;). The program will then (by default) search for it in the current directory, <i>/usr/share/info,</i> <i>/usr/info,</i> <i>/usr/local/share/info,</i> <i>/usr/local/info.</i> and <i>/opt/info.</i> The search path can be adjusted by INFOPATH environment variable or in the configuration file. Pinfo will also automatically add the suffix &#8216;-info&#8217;, &#8216;-info.Z&#8217;, &#8216;-info.gz&#8217;, or &#8216;-info.bz2&#8217;. At present other suffixes are not recognized, but you can easily add them to the function <i>openinfo() </i> in <i>filehandling_functions.c.</i> </p>
<p> When the search for info pages fails, man is called with the infopage argument, and it&#8217;s output is parsed by pinfo. This means that when you don&#8217;t have the appropriate info page, but have a man page instead; the man page will be viewed. </p>
<p> When no <i>infopage</i> is specified, the default `dir&#8217; page is shown. </p>
<p> Supported options are </p>
<p> <code>-h,</code> <code>&#8211;help</code> &#8211; print help information and exit. </p>
<p> <code>-v,</code> <code>&#8211;version</code> &#8211; print version information and exit. </p>
<p> <code>-m,</code> <code>&#8211;manual</code> &#8211; uses manual page instead of info by default. (pinfo -m could be used as a manual pager). <code>Warning</code>: Everything what follows this option is passed to the `<i>man</i>&#8216; program. Don&#8217;t be confused if pinfo options, which followed `<code>-m</code>&#8216; don&#8217;t work. When using this option, pinfo does not parse the info options as usual! It invokes the man part of program. </p>
<p> You can also call the man function of pinfo in another way. When pinfo is called with an argv[0] (the program file name), which contains the word &#8216;man&#8217; in it&#8217;s name, the man functions are enabled automatically. </p>
<p> Previously there was a symlink to pinfo, called pman, but I had to remove it from the distribution, since it&#8217;s name was in conflict with some other utility. Anyway, you can feel free to create such a link if you wish. </p>
<p> <code>-r,</code> <code>&#8211;raw-filename</code> &#8211; uses a raw filename first (i.e. the name which you specified as <i>infopage</i> is considered to be a real file in the specified location). </p>
<p> <code>-f,</code> <code>&#8211;file</code> synonym for -r. </p>
<p> <code>-a,</code> <code>&#8211;apropos</code> &#8211; if this is set, apropos is called when no man or info page could be found. </p>
<p> <code>-p,</code> <code>&#8211;plain-apropos</code> &#8211; if this is set, call only apropos. </p>
<p> <code>-c,</code> <code>&#8211;cut-man-headers</code> &#8211; if this is set, man parsing code will try to cut out the repeated man headers. Use with care. ;) </p>
<p> <code>-s,</code> <code>&#8211;squeeze-lines</code>&#8211; cut empty lines from manual pages. This option enables auto cutting of every repeated newline in a manual page. </p>
<p> <code>-d,</code> <code>&#8211;dont-handle-without-tag-table</code> &#8211; don&#8217;t display texinfo pages without tag table. </p>
<p> <code>-t,</code> <code>&#8211;force-manual-tag-table</code>&#8211; forces manual detection of tag table. This allows you to view info pages, which may be corrupted. (as i.e. version of jed&#8217;s pages, shipped with RH5.0). The tag table corruption usually appears in that the info links, which you follow, move you to quite unexpected nodes. </p>
<p> <code>&#8211;node=</code><i>nodename</i><code>,</code> <code>&#8211;node </code><i>nodename</i>&#8211; Go to the node `<i>nodename</i>&#8216; of info file. Since 0.6.7 it is also possible to specify nodes as in standalone info via file names, like `(gcc)Introduction&#8217;. </p>
<p> <code>&#8211;rcfile=</code><i>filename</i><code>,</code> <code>&#8211;rcfile </code><i>filename</i>&#8211; Use alternate configuration file. </p>
<p> <code>&#8211;long-manual-links,</code> <code>-l</code>&#8211; Use long link names in manuals. On some systems the manual hierarchy is divided into subsections like `3ncurses&#8217;, etc, while on other systems all belongs to section `3&#8242;. If this option is what your system is like, feel free to use it. </p>
<p> <code>&#8211;clear-at-exit,</code> <code>-x</code>&#8211; Clear screen at exit. </p>
<p> The options are handled by GNU getopt, so you can here (as in other programs) abbreviate the option names to the minimal number of characters by which the options differ. </p>
<p> Warning! If you do not have getopt, these options will not work! </p>
<h2>DEFAULT KEYS WHEN BROWSING INFO FILE</h2>
<p> Just take a look at the example configuration file (below), and at the key descriptions. Keys available in manual viewer differ a bit from the keys available in info viewer. </p>
<h2>ENVIRONMENT</h2>
<p> There is a variable $INFOPATH, which can specify the paths to be searched for info files. It&#8217;s format is similar to that of the $PATH variable. An example setting could look like: </p>
<p> <code>/usr/info:/usr/somewhere/info:/not/even/in/usr/info</code> </p>
<p> etc. Directories are separated by colons. </p>
<h2>COLOR AND KEY DEFINITIONS</h2>
<p> There are configuration files called ~/.pinforc and [prefix]/etc/pinforc, for local and global configuration (where prefix is the prefix of the directory, where pinfo is installed, i.e. /usr/local, or /). Here&#8217;s an example of such a file; we&#8217;ll discuss the contents below: </p>
<pre>
# Here are some color setting.
# Whitespace between the entries is optional.
COL_NORMAL = COLOR_WHITE, COLOR_BLACK, NO_BOLD, NO_BLINK
COL_MENUSELECTED = COLOR_RED, COLOR_BLACK, BOLD, NO_BLINK
COL_MENU=COLOR_BLUE,COLOR_BLACK,BOLD, NO_BLINK
COL_NOTESELECTED=COLOR_RED,COLOR_BLACK,BOLD, NO_BLINK
COL_NOTE=COLOR_GREEN,COLOR_BLACK,BOLD, NO_BLINK
COL_TOPLINE=COLOR_YELLOW,COLOR_BLUE,BOLD, NO_BLINK
COL_BOTTOMLINE=COLOR_YELLOW,COLOR_BLUE,BOLD, NO_BLINK
COL_MANUALBOLD=COLOR_WHITE,COLOR_BLACK,BOLD, NO_BLINK
COL_MANUALITALIC=COLOR_WHITE,COLOR_BLACK,BOLD, NO_BLINK
COL_URL=COLOR_MAGENTA,COLOR_BLACK,BOLD, NO_BLINK
COL_URLSELECTED=COLOR_RED,COLOR_BLACK,NO_BOLD, NO_BLINK
COL_INFOHIGHLIGHT=COLOR_WHITE,COLOR_BLACK,BOLD, NO_BLINK
#
# Here are some keybindings as well...
#
KEY_TOTALSEARCH_1 = 's'
KEY_TOTALSEARCH_2 = 'S'
KEY_SEARCH_1 = '/'
KEY_SEARCH_2 = '.'
KEY_GOTO_1='g'
KEY_GOTO_2='m'
KEY_HOME_1='h'
KEY_HOME_2='H'
KEY_PREVNODE_1='p'
KEY_PREVNODE_2='P'
KEY_NEXTNODE_1='n'
KEY_NEXTNODE_2='N'
KEY_UP_1=KEY_UP
KEY_UP_2='u'
KEY_END_1=
KEY_END_2='e'
KEY_PGDN_1=KEY_NPAGE
KEY_PGDN_2=' '
KEY_PGDN_AUTO_1=0
KEY_PGDN_AUTO_2=' '
KEY_PGUP_1=KEY_PPAGE
KEY_PGUP_2='b'
KEY_PGUP_AUTO_1=0
KEY_PGUP_AUTO_2='b'
KEY_DOWN_1=KEY_DOWN
KEY_DOWN_2='d'
KEY_TOP_1=KEY_HOME
KEY_TOP_2='t'
KEY_BACK_1=KEY_LEFT
KEY_BACK_2='l'
KEY_FOLLOWLINK_1=KEY_RIGHT
KEY_FOLLOWLINK_2='
# 12 is a code for ctrl+l
KEY_REFRESH_1=12
KEY_REFRESH_2='~'
KEY_SHELLFEED_1='!'
KEY_SHELLFEED_2='1'
KEY_QUIT_1='q'
KEY_QUIT_2='Q'
KEY_DIRPAGE_1='d'
KEY_DIRPAGE_2='D'
KEY_GOLINE_1='l'
KEY_GOLINE_2=0
KEY_PRINT_1=']'
KEY_PRINT_2=0
#
# Some options, explained in the man page
#
MANUAL=false
CUT-MAN-HEADERS=true
CUT-EMPTY-MAN-LINES=true
RAW-FILENAME=false
APROPOS=false
DONT-HANDLE-WITHOUT-TAG-TABLE=false
LONG-MANUAL-LINKS=false
FILTER-0xB7=true
QUIT-CONFIRMATION=false
QUIT-CONFIRM-DEFAULT=no
CLEAR-SCREEN-AT-EXIT=true
STDERR-REDIRECTION=&quot;2&gt; /dev/null&quot;
HTTPVIEWER=lynx
FTPVIEWER=lynx
MAILEDITOR=pine
MANLINKS=1:8:2:3:4:5:6:7:9:n:p:o:3X11:3Xt
INFOPATH=/usr/info:/usr/share/info:/usr/local/info
HIGHLIGHTREGEXP=Bash.*has
SAFE-USER=nobody
SAFE-GROUP=nobody
</pre>
<p> As you can see, the format is simple. First I&#8217;ll explain the color definitions. First you must enter a color name (all available color names are present in the example, and they&#8217;re self explanatory, I think. There is also a special color COLOR_DEFAULT, which stands for transparency). Then you enter the foreground color, and the background color. The BOLD attribute means that we want the foreground color to be highlighted. (i.e. light blue, light green). BLINK attribute is the blinking attribute, or highlighted background in some other configurations. </p>
<p> Now let&#8217;s move to the key definitions. Here we first put a key name (again all keys are present in the example); then we enter it&#8217;s value &#8212; either surrounded by apostrophes, or a keycode number (like in KEY_REFRESH_1), or its mnemonic code name if it&#8217;s a special key (like i.e. in KEY_FOLLOWLINK_1). </p>
<p> If you wish to specify key by code value, use the supplied program &#8216;testkey&#8217; to obtain the needed value. It mainly is a feature, when you want to add some CTRL+letter keybindings, and similar. </p>
<p> For each function you can bind two keys, i.e. you could bind both Enter and Cursor Right to the FollowLink-function. As you can see in the example above, the two key names are KEY_FOLLOWLINK_1 and KEY_FOLLOWLINK_2. </p>
<p> Here&#8217;s an explanation of the key names:</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>KEY_TOTALSEARCH_1</code></p>
<dd> Key for searching through all nodes of info file.</p>
<dt><code>KEY_TOTALSEARCH_2</code></p>
<dd> Alternate key for searching through all nodes of info file.</p>
<dt><code>KEY_SEARCH_1</code></p>
<dd> Key for searching through current node (or manual).</p>
<dt><code>KEY_SEARCH_2</code></p>
<dd> Alternate key for searching through current node (or manual).</p>
<dt><code>KEY_SEARCH_AGAIN_1</code></p>
<dd> Key for repeating the last search.</p>
<dt><code>KEY_SEARCH_AGAIN_2</code></p>
<dd> Alternate key for repeating the last search.</p>
<dt><code>KEY_GOTO_1</code></p>
<dd> Key for explicitly going to a node (by specifying it&#8217;s name).</p>
<dt><code>KEY_GOTO_2</code></p>
<dd> Alternate key for explicitly going to a node (by specifying it&#8217;s name).</p>
<dt><code>KEY_PREVNODE_1</code></p>
<dd> Key for going to a node marked as &#8216;Prev&#8217; in the header. In man page viewer this goes to the previous man section.</p>
<dt><code>KEY_PREVNODE_2</code></p>
<dd> Alternate key for going to a node marked as &#8216;Prev&#8217; in the header. In man page viewer this goes to the previous man section.</p>
<dt><code>KEY_NEXTNODE_1</code></p>
<dd> Key for going to a node marked as &#8216;Next&#8217; in the header. In man page viewer this goes to the next man section.</p>
<dt><code>KEY_NEXTNODE_2</code></p>
<dd> Alternate key for going to a node marked as &#8216;Next&#8217; in the header. In man page viewer this goes to the next man section.</p>
<dt><code>KEY_UP_1</code></p>
<dd> Key for scrolling text one line up.</p>
<dt><code>KEY_UP_2</code></p>
<dd> Alternate key for scrolling text one line up.</p>
<dt><code>KEY_END_1</code></p>
<dd> Key for going to the end of the node.</p>
<dt><code>KEY_END_2</code></p>
<dd> Alternate key for going to the end of the node.</p>
<dt><code>KEY_PGDN_1</code></p>
<dd> Key for going one page down in the viewed node.</p>
<dt><code>KEY_PGDN_2</code></p>
<dd> Alternate key for going one page down in the viewed node.</p>
<dt><code>KEY_PGDN_AUTO_1</code></p>
<dd> Key for going to the next node when you&#8217;re at the end of node (default is zero &#8212; turned off).</p>
<dt><code>KEY_PGDN_AUTO_2</code></p>
<dd> Alternate key for going to the next node when you&#8217;re at the end of node (default is space, as for pgdn_2).</p>
<dt><code>KEY_HOME_1</code></p>
<dd> Key for going to the beginning of the node.</p>
<dt><code>KEY_HOME_2</code></p>
<dd> Alternate key for going to the beginning of the node.</p>
<dt><code>KEY_PGUP_1</code></p>
<dd> Key for going one page up in the viewed node.</p>
<dt><code>KEY_PGUP_2</code></p>
<dd> Alternate key for going one page up in the viewed node.</p>
<dt><code>KEY_PGUP_AUTO_1</code></p>
<dd> Key for going to the `up&#8217; node, when being at the top of node. (Default value is zero &#8212; turned off).</p>
<dt><code>KEY_PGUP_AUTO_2</code></p>
<dd> Alternate key for going to the `up&#8217; node, when being at the top of node. (Default value is `-&#8216;, as for pgup_2).</p>
<dt><code>KEY_DOWN_1</code></p>
<dd> Key for scrolling the text down one line.</p>
<dt><code>KEY_DOWN_2</code></p>
<dd> Alternate key for scrolling the text down one line.</p>
<dt><code>KEY_TOP_1</code></p>
<dd> Key for going to the top (first) node.</p>
<dt><code>KEY_TOP_2</code></p>
<dd> Alternate key for going to the top (first) node.</p>
<dt><code>KEY_BACK_1</code></p>
<dd> Key for going back (in the history of viewed nodes).</p>
<dt><code>KEY_BACK_2</code></p>
<dd> Alternate key for going back (in the history of viewed nodes).</p>
<dt><code>KEY_FOLLOWLINK_1</code></p>
<dd> Key for following a hypertext link.</p>
<dt><code>KEY_FOLLOWLINK_2</code></p>
<dd> Alternate key for following a hypertext link.</p>
<dt><code>KEY_REFRESH_1</code></p>
<dd> Key for refreshing the screen (hard coded is the ^L value).</p>
<dt><code>KEY_REFRESH_2</code></p>
<dd> Alternate key for refreshing the screen.</p>
<dt><code>KEY_SHELLFEED_1</code></p>
<dd> Key for calling a shell command, and passing the viewed node to the stdin of that command.</p>
<dt><code>KEY_SHELLFEED_2</code></p>
<dd> Alternate key for calling a shell command, and passing the viewed node to the stdin of that command.</p>
<dt><code>KEY_QUIT_1</code></p>
<dd> Key for exiting the program.</p>
<dt><code>KEY_QUIT_2</code></p>
<dd> Alternate key for exiting the program.</p>
<dt><code>KEY_GOLINE_1</code></p>
<dd> Key for going to a specified line in file.</p>
<dt><code>KEY_GOLINE_2</code></p>
<dd> Alternate key for going to a specified line in file.</p>
<dt><code>KEY_PRINT_1</code></p>
<dd> Key for printing viewed node or man page.</p>
<dt><code>KEY_PRINT_2</code></p>
<dd> Alternate key for printing viewed node or man page. </p>
</dl>
</dl>
<p> The special mnemonics for keys (which are defined at present) are:</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>KEY_BREAK</code></p>
<dd>
<dt><code>KEY_DOWN</code></p>
<dd>
<dt><code>KEY_UP</code></p>
<dd>
<dt><code>KEY_LEFT</code></p>
<dd>
<dt><code>KEY_RIGHT</code></p>
<dd>
<dt><code>KEY_DOWN</code></p>
<dd>
<dt><code>KEY_HOME</code></p>
<dd>
<dt><code>KEY_BACKSPACE</code></p>
<dd>
<dt><code>KEY_NPAGE</code></p>
<dd>
<dt><code>KEY_PPAGE</code></p>
<dd>
<dt><code>KEY_END</code> [Note: this works probably <code>ONLY</code> with Linux ncurses]</p>
<dd>
<dt><code>KEY_F(x)</code></p>
<dd>
<dt><code>KEY_CTRL(&#8216;c&#8217;)</code></p>
<dd> &#8211; this assigns the key value to a <i>ctrl+c</i> combination. <i>c</i> may be any letter you wish.</p>
<dt><code>KEY_ALT(&#8216;c&#8217;)</code></p>
<dd> &#8211; this assigns the key value to a <i>alt+c</i> combination. <i>c</i> may be any letter you wish. If <i>alt</i> key won&#8217;t work, you may use <i>ESC+key</i> combination.</p>
<dt><code>&#8216;c&#8217;</code></p>
<dd> &#8211; this means a printable character <i>c</i>. The syntax is just like in C/C++ ;).</p>
<dt><code>[number]</code></p>
<dd> &#8211; you can also specify key as it&#8217;s code number. It is useful e.g. when specifying control keys, and some nonstandard keys. A numerical value of zero turns given key binding off. </p>
</dl>
</dl>
<p> See manual page for curs_getch (3x) for description of their meaning. </p>
<p> Warning! Try not to create some serious key binding conflicts! </p>
<p> The options in the last part of the example configuration file should be fairly self-explanatory. The variables that can be set to true or false do the same things as the command line arguments with the same names.</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>MANUAL </code></p>
<dd> If this is set to <code>true</code> the default is to first check for a man page, instead of a texinfo file.</p>
<dt><code>CUT-MAN-HEADERS </code></p>
<dd> If set to true, then pinfo tries to cut off the repeated headers throughout man pages.</p>
<dt><code>CUT-EMPTY-MAN-LINES</code></p>
<dd> If set to true, then pinfo tries to cut off the repeated newlines (i.e. it will shorten each set of consecutive newlines to one newline).</p>
<dt><code>RAW-FILENAME</code></p>
<dd> If set to true, the file argument is taken to be the name of a file in the current working directory, i.e. the directories in <code>INFOPATH</code> will only be searched if a file with this name is not in the working directory.</p>
<dt><code>APROPOS</code></p>
<dd> If set to true, <code>apropos</code> is called if no info or man page is found.</p>
<dt><code>DONT-HANDLE-WITHOUT-TAG-TABLE</code></p>
<dd> If set to <code>true</code> , pinfo will not attempt to display texinfo pages without tag tables.</p>
<dt><code>HTTPVIEWER</code></p>
<dd> Set this to the program you want to use to follow http links in documents.</p>
<dt><code>FTPVIEWER</code></p>
<dd> Set this to the program you want to use to follow ftp links in documents.</p>
<dt><code>MAILEDITOR</code></p>
<dd> Set this to your favorite email program, and it will be started if you follow an email link in a document.</p>
<dt><code>PRINTUTILITY</code></p>
<dd> Utility, which you use for printing. I.e. `lpr&#8217;. If you don&#8217;t use any, you may also try something like `cat &gt;/dev/lp1&#8242;, or sth. ;)</p>
<dt><code>MANLINKS</code></p>
<dd> This specifies the section names, which may be referenced in your man pages (i.e. Xtoolkit man pages match the section 3Xt (see for example XtVaCreateWidget) manpage), Xlib function pages match section 3X11, etc. Such extensions may not be recognized by default, so it is a good idea to add them).</p>
<dt><code>INFOPATH</code></p>
<dd> This allows you to override the default search path for info pages. The paths should be separated by colons.</p>
<dt><code>MAN-OPTIONS</code></p>
<dd> This specifies the options, which should be passed to the `man&#8217; program. (see <a href="/docs/linux/man/1-man/">man</a>(1) for description of what they&#8217;re like).</p>
<dt><code>STDERR-REDIRECTION</code></p>
<dd> Pinfo allows you to redirect the stderr output of called programs. For example if you don&#8217;t want to see man&#8217;s error messages about manual page formatting, you can use <i>STDER-REDIRECTION=&quot;2&gt; /dev/null&quot;. This is the default.</p>
<dt></i><code>LONG-MANUAL-LINKS</code></p>
<dd> This is another true/false option, which decides whether your system supports long manual section names, or not. (i.e. &quot;3ncurses&quot; instead of &quot;3&quot;).</p>
<dt><code>FILTER-0xB7</code></p>
<dd> This decides, whether you want to convert 0xb7 chars to `o&#8217;, or not. For example for iso-8859-2 fonts this makes man&#8217;s list marks a bit nicer ;) (look for example at perl&#8217;s man page, to see how those marks look like).</p>
<dt><code>QUIT-CONFIRMATION</code></p>
<dd> This decides whether you want to use quit confirmation on exit, or not.</p>
<dt><code>QUIT-CONFIRM-DEFAULT</code></p>
<dd> This yes/no option determines the default answer to the QUIT-CONFIRMATION dialog. (default answer is when you press a key, that does not match the asked question).</p>
<dt><code>CLEAR-SCREEN-AT-EXIT</code></p>
<dd> This true/false option determines if you want to have your screen cleared at exit, or no.</p>
<dt><code>CALL-READLINE-HISTORY</code></p>
<dd> This true/false option determines if you want to have a prompt of last history entry whenever calling readline wrapper, eg. in subsequent searches.</p>
<dt><code>HIGHLIGHTREGEXP</code></p>
<dd> This is an option, through which you may pass to pinfo regexps, which should be highlighted when working with document. Warning! This may turn very slow if you use it without care!</p>
<dt><code>SAFE-USER</code></p>
<dd> This option is used to pass the name of user, to which suid when pinfo is run with root privileges.</p>
<dt><code>SAFE-GROUP</code></p>
<dd> This option is used to pass the name of group, to which suid when pinfo is run with root privileges. </p>
</dl>
</dl>
<h2>INTERNATIONALIZATION SUPPORT</h2>
<p> Pinfo implements general features of gnu gettext library (the thing, which you need to see national messages ;). But it is not the end. Pinfo allows you to use national info pages! You only need to put them to your info directory, into a subdirectory, which is called `$LANG&#8217;. </p>
<h2>LICENSE</h2>
<p> This program is distributed under the terms of GPL. </p>
<h2>BUGS</h2>
<p> Please send bug reports to the author. </p>
<h2>AUTHOR</h2>
<p> Przemek Borys &lt;<code>pborys [at] dione.ids.pl</code>&gt; </p>
<p> If that E-mail address wont work (since the machine where it is being handled is a bit damaged lately), you can try <code>pborys [at] zeus.polsl.gliwice.pl</code>, or <code>pborys [at] p-soft.silesia.linux.org.pl</code>. </p>
<p> There was also a lot of other people, who contributed to this code. See the AUTHORS file. </p>
<h2>COMMENTS</h2>
<p> The author would like to read some comments and suggestions from you, if any. </p>
<h2>Index</h2>
