---
title: "minicom(1)"
name: "minicom"
section: "1"
letter: "m"
url: "/docs/linux/man/1-minicom/"
description: "minicom – friendly serial communication program"
---

<h2>NAME</h2>
<p> minicom &#8211; friendly serial communication program</p>
<h2>SYNOPSIS</h2>
<p> <code>minicom</code> [options] [<i>configuration</i>]</p>
<h2>DESCRIPTION</h2>
<p> <code>minicom</code> is a communication program which somewhat resembles the shareware program TELIX but is free with source code and runs under most Unices. Features include dialing directory with auto-redial, support for UUCP-style lock files on serial devices, a separate script language interpreter, capture to file, multiple users with individual configurations, and more.</p>
<h2>COMMAND-LINE</h2>
<dl>
<dt><code>-s, &#8211;setup</code></p>
<dd> <code>S</code>etup. Root edits the system-wide defaults in /etc/minirc.dfl with this option. When it is used, minicom does <i>not </i> initialize, but puts you directly into the configuration menu. This is very handy if minicom refuses to start up because your system has changed, or for the first time you run minicom. For most systems, reasonable defaults are already compiled in.</p>
<dt><code>-o, &#8211;noinit</code></p>
<dd> Do not initialize. Minicom will skip the initialization code. This option is handy if you quit from minicom without resetting, and then want to restart a session. It is potentially dangerous though: no check for lock files etc. is made, so a normal user could interfere with things like UUCP&#8230; maybe this will be taken out later. For now it is assumed, that users who are given access to a modem are responsible enough for their actions.</p>
<dt><code>-m, &#8211;metakey</code></p>
<dd> Override command-key with the Meta or ALT key. This is the default in 1.80 and it can also be configured in one of minicom&#8217;s menus, but if you use different terminals all the time, of which some don&#8217;t have a Meta or ALT key, it&#8217;s handy to set the default command key to Ctrl-A and use this option when you have a keyboard supporting Meta or ALT keys. Minicom assumes that your Meta key sends the ESC prefix, not the other variant that sets the highest bit of the character.</p>
<dt><code>-M, &#8211;metakey8</code></p>
<dd> Same as -m, but assumes that your Meta key sets the 8th bit of the character high (sends 128 + character code).</p>
<dt><code>-z, &#8211;statline</code></p>
<dd> Use terminal status line. This only works on terminals that support it and that have the relevant information in their <i>termcap</i> or <i>terminfo</i> database entry.</p>
<dt><code>-l, &#8211;ansi</code></p>
<dd> <code>L</code>iteral translation of characters with the high bit set. With this flag on, minicom will try to translate the IBM line characters to ASCII. Many PC-unix clones will display character correctly without translation (Linux in a special mode, Coherent and SCO).</p>
<dt><code>-L, &#8211;iso</code></p>
<dd> Ditto but assume screen uses an ISO8859 character set.</p>
<dt><code>-w, &#8211;wrap</code></p>
<dd> Turns line-wrap on at startup by default.</p>
<dt><code>-H, &#8211;displayhex</code></p>
<dd> Turn on output in hex mode.</p>
<dt><code>-a, &#8211;attrib=on/off</code></p>
<dd> <code>A</code>ttribute usage. Some terminals, notably Televideo&#8217;s, have rotten attribute handling (serial instead of parallel). By default, minicom uses &#8216;-a on&#8217;, but if you are using such a terminal you can (must!) supply the option &#8216;-a off&#8217;. The trailing &#8216;on&#8217; or &#8216;off&#8217; is needed.</p>
<dt><code>-t, &#8211;term=TERM</code></p>
<dd> <code>T</code>erminal type. With this flag, you can override the environment TERM variable. This is handy for use in the MINICOM environment variable; one can create a special termcap entry for use with minicom on the console, that initializes the screen to raw mode so that in conjunction with the -l flag, the IBM line characters are displayed untranslated.</p>
<dt><code>-c, &#8211;color=on/off</code></p>
<dd> <code>C</code>olor usage. Some terminals (such as the Linux console) support color with the standard ANSI escape sequences. Because there is apparently no termcap support for color, these escape sequences are hard-coded into minicom. Therefore this option is off by default. You can turn it on with &#8216;-c on&#8217;. This, and the &#8216;-m&#8217; option, are good candidates to put into the MINICOM environment variable.</p>
<dt><code>-S, &#8211;script=SCRIPT</code></p>
<dd> <code>script</code>. Run the named script at startup. So far, passing username and password to a startup script is not supported. If you also use the -d option to start dialing at startup, the -S script will be run BEFORE dialing the entries specified with -d.</p>
<dt><code>-d, &#8211;dial=ENTRY</code></p>
<dd> <code>D</code>ial an entry from the dialing directory on startup. You can specify an index number, but also a substring of the name of the entry. If you specify a name that has multiple entries in the directory, they are all tagged for dialing. You can also specify multiple names or index numbers by separating them with commas. The dialing will start from the first entry specified after all other program initialization procedures are completed.</p>
<dt><code>-p, &#8211;ptty=TTYP</code></p>
<dd> <code>P</code>seudo terminal to use. This overrides the terminal port defined in the configuration files, but only if it is a pseudo TTY. The filename supplied must be of the form (/dev/)tty[p-z/][0-f], (/dev/)pts[p-z/][0-f] or (/dev/)pty[p-z/][0-f]. For example, /dev/ttyp1, pts/0 or /dev/ptyp2.</p>
<dt><code>-C, &#8211;capturefile=FILE</code></p>
<dd> <code>filename</code>. Open capture file at startup.</p>
<dt><code>-T, &#8211;disabletime</code></p>
<dd> Disable the display of the online time in the status bar.</p>
<dt><code>-b, &#8211;baudrate</code></p>
<dd> Specify the baud rate, overriding the value given in the configuration file.</p>
<dt><code>-D, &#8211;device</code></p>
<dd> Specify the device, overriding the value given in the configuration file.</p>
<dt><code>-R, &#8211;remotecharset</code></p>
<dd> Specify the character set of the remote system is using and convert it to the character set of the local side. Example might be &#8216;latin1&#8217;.</p>
<dt><code>-7, &#8211;7bit</code></p>
<dd> 7bit mode for terminals which aren&#8217;t 8bit capable. 8bit is default if the environment is configured for this via LANG or LC_ALL, 7bit otherwise.</p>
<dt><code>-8, &#8211;8bit</code></p>
<dd> 8bit characters pass through without any modification. &#8216;Continuous&#8217; means no locate/attribute control sequences are inserted without real change of locate/attribute. This mode is to display 8bit multi-byte characters such as Japanese. Not needed in every language with 8bit characters. (For example displaying Finnish text doesn&#8217;t need this.)</p>
<dt><code>-h, &#8211;help</code></p>
<dd> Display help and exit.</p>
<dt><code>-v, &#8211;version</code></p>
<dd> Print the minicom version.</dl>
<dl>
<dt>
<dd> When <code>minicom</code> starts, it first searches the MINICOM environment variable for command-line arguments, which can be over-ridden on the command line. Thus, if you have done </p>
<dl>
<dt>
<dd> MINICOM=&#8217;-m -c on&#8217; </p>
<p> export MINICOM </p>
</dl>
<p> or the equivalent, and start minicom, minicom will assume that your terminal <i>has </i> a Meta or &lt;ALT&gt; key and that color is supported. If you then log in from a terminal without color support, and you have set MINICOM in your startup (.profile or equivalent) file, and don&#8217;t want to re-set your environment variable, you can type &#8216;minicom -c off&#8217; and run without color support for that session.</dl>
<dl>
<dt><code>configuration</code></p>
<dd> The <i>configuration</i> argument is more interesting. Normally, minicom gets its defaults from a file called &quot;minirc.dfl&quot;. If you however give an argument to minicom, it will try to get its defaults from a file called &quot;minirc.<i>configuration</i>&quot;. So it is possible to create multiple configuration files, for different ports, different users etc. Most sensible is to use device names, such as tty1, tty64, sio2 etc. If a user creates his own configuration file, it will show up in his home directory as &quot;.minirc.dfl&quot; or &quot;.minirc.<i>configuration</i>&quot;.</dl>
<h2>USE</h2>
<p> Minicom is window based. To pop-up a window with the function you want, press Control-A (from now on, we will use C-A to mean Control-A), and then the function key (a-z or A-Z). By pressing C-A first and then &#8216;z&#8217;, a help screen comes up with a short summary of all commands. This escape key can be altered when minicom is configured (-s option or C-A O), but we&#8217;ll stick to Control-A for now. </p>
<p> For every menu the next keys can be used:</p>
<dl>
<dt><code>UP</code></p>
<dd> arrow-up or &#8216;k&#8217;</p>
<dt><code>DOWN</code></p>
<dd> arrow-down or &#8216;j&#8217;</p>
<dt><code>LEFT</code></p>
<dd> arrow-left or &#8216;h&#8217;</p>
<dt><code>RIGHT</code></p>
<dd> arrow-right or &#8216;l&#8217;</p>
<dt><code>CHOOSE</code></p>
<dd> Enter</p>
<dt><code>CANCEL</code></p>
<dd> ESCape.</dl>
<p> The screen is divided into two portions: the upper 24 lines are the terminal-emulator screen. In this window, ANSI or VT100 escape sequences are interpreted. If there is a line left at the bottom, a status line is placed there. If this is not possible the status line will be showed every time you press C-A. On terminals that have a special status line that will be used if the termcap information is complete <i>and</i> the <code>-k</code> flag has been given. </p>
<p> Possible commands are listed next, in alphabetical order.</p>
<dl>
<dt><code>C-A</code></p>
<dd> Pressing C-A a second time will just send a C-A to the remote system. If you have changed your &quot;escape character&quot; to something other than C-A, this works analogously for that character.</p>
<dt><code>A</code></p>
<dd> Toggle &#8216;Add Linefeed&#8217; on/off. If it is on, a linefeed is added before every carriage return displayed on the screen.</p>
<dt><code>B</code></p>
<dd> Gives you a scroll back buffer. You can scroll up with <code>u</code>, down with <code>d</code>, a page up with <code>b</code>, a page down with <code>f</code>, and if you have them the <code>arrow</code> and <code>page up/page down</code> keys can also be used. You can search for text in the buffer with <code>s</code> (case-sensitive) or <code>S</code> (case-insensitive). <code>N</code> will find the next occurrence of the string. <code>c</code> will enter citation mode. A text cursor appears and you specify the start line by hitting Enter key. Then scroll back mode will finish and the contents with prefix &#8216;&gt;&#8217; will be sent.</p>
<dt><code>C</code></p>
<dd> Clears the screen.</p>
<dt><code>D</code></p>
<dd> Dial a number, or go to the dialing directory.</p>
<dt><code>E</code></p>
<dd> Toggle local echo on and off (if your version of minicom supports it).</p>
<dt><code>F</code></p>
<dd> A break signal is sent to the modem.</p>
<dt><code>G</code></p>
<dd> Run script (Go). Runs a login script.</p>
<dt><code>H</code></p>
<dd> Hangup.</p>
<dt><code>I</code></p>
<dd> Toggle the type of escape sequence that the cursor keys send between normal and applications mode. (See also the comment about the status line below).</p>
<dt><code>J</code></p>
<dd> Jump to a shell. On return, the whole screen will be redrawn.</p>
<dt><code>K</code></p>
<dd> Clears the screen, runs kermit and redraws the screen upon return.</p>
<dt><code>L</code></p>
<dd> Turn Capture file on off. If turned on, all output sent to the screen will be captured in the file too.</p>
<dt><code>M</code></p>
<dd> Sends the modem initialization string. If you are online and the DCD line setting is on, you are asked for confirmation before the modem is initialized.</p>
<dt><code>N</code></p>
<dd> Toggle between three states, whether each line is prefixed with current date and time, a timestamp is added every second, or no timestamps.</p>
<dt><code>O</code></p>
<dd> Configure minicom. Puts you in the configuration menu.</p>
<dt><code>P</code></p>
<dd> Communication Parameters. Allows you to change the bps rate, parity and number of bits.</p>
<dt><code>Q</code></p>
<dd> Exit minicom without resetting the modem. If macros changed and were not saved, you will have a chance to do so.</p>
<dt><code>R</code></p>
<dd> Receive files. Choose from various protocols (external). If you have the filename selection window and the prompt for download directory enabled, you&#8217;ll get a selection window for choosing the directory for downloading. Otherwise the download directory defined in the Filenames and paths menu will be used.</p>
<dt><code>S</code></p>
<dd> Send files. Choose the protocol like you do with the receive command. If you don&#8217;t have the filename selection window enabled (in the File transfer protocols menu), you&#8217;ll just have to write the filename(s) in a dialog window. If you have the selection window enabled, a window will pop up showing the filenames in your upload directory. You can tag and untag filenames by pressing spacebar, and move the cursor up and down with the cursor keys or j/k. The selected filenames are shown highlighted. Directory names are shown [within brackets] and you can move up or down in the directory tree by pressing the spacebar twice. Finally, send the files by pressing ENTER or quit by pressing ESC.</p>
<dt><code>T</code></p>
<dd> Choose Terminal emulation: Ansi(color) or vt100. You can also change the backspace key here, turn the status line on or off, and define delay (in milliseconds) after each newline if you need that.</p>
<dt><code>W</code></p>
<dd> Toggle line-wrap on/off.</p>
<dt><code>X</code></p>
<dd> Exit minicom, reset modem. If macros changed and were not saved, you will have a chance to do so.</p>
<dt><code>Y</code></p>
<dd> Paste a file. Reads a file and sends its contests just as if it would be typed in.</p>
<dt><code>Z</code></p>
<dd> Pop up the help screen.</dl>
<h2>DIALING DIRECTORY</h2>
<p> By pressing C-A D the program puts you in the dialing directory. Select a command by pressing the capitalized letter or moving cursor right/left with the arrow keys or the h/l keys and pressing Enter. You can add, delete or edit entries and move them up and down in the directory list. By choosing &quot;dial&quot; the phone numbers of the tagged entries, or if nothing is tagged, the number of the highlighted entry will be dialed. While the modem is dialing, you can press escape to cancel dialing. Any other key will close the dial window, but won&#8217;t cancel the dialing itself. Your dialing directory will be saved into the file &quot;.dialdir&quot; in your home directory. You can scroll up and down with the arrow keys, but you can also scroll complete pages by pressing the PageUp or PageDown key. If you don&#8217;t have those, use Control-B (Backward) and Control-F (Forward). You can use the space bar to <code>tag</code> a number of entries and minicom will rotate trough this list if a connection can&#8217;t be made. A &#8216;&gt;&#8217; symbol is drawn in the directory before the names of the tagged entries. </p>
<p> The &quot;edit&quot; menu speaks for itself, but I will discuss it briefly here.</p>
<dl>
<dt><code>A &#8211; Name</code></p>
<dd> The name for this entry</p>
<dt><code>B &#8211; Number</code></p>
<dd> and its telephone number.</p>
<dt><code>C &#8211; Dial string #</code></p>
<dd> Which specific dial string you want to use to connect. There are three different dial strings (prefixes and suffixes) that can be configured in the <code>Modem and dialing</code> menu.</p>
<dt><code>D &#8211; Local echo</code></p>
<dd> can be on or off for this system (if your version of minicom supports it).</p>
<dt><code>E &#8211; Script </code></p>
<dd> The script that must be executed after a successful connection is made (see the manual for runscript)</p>
<dt><code>F &#8211; Username</code></p>
<dd> The username that is passed to the runscript program. It is passed in the environment string &quot;$LOGIN&quot;.</p>
<dt><code>G &#8211; Password</code></p>
<dd> The password is passed as &quot;$PASS&quot;.</p>
<dt><code>H &#8211; Terminal Emulation</code></p>
<dd> Use ANSI or VT100 emulation.</p>
<dt><code>I &#8211; Backspace key sends</code></p>
<dd> What code (Backspace or Delete) the backspace key sends.</p>
<dt><code>J &#8211; Linewrap</code></p>
<dd> Can be on or off.</p>
<dt><code>K &#8211; Line settings</code></p>
<dd> Bps rate, bits, parity and number of stop bits to use for this connection. You can choose <code>current</code> for the speed, so that it will use whatever speed is being used at that moment (useful if you have multiple modems).</p>
<dt><code>L &#8211; Conversion table</code></p>
<dd> You may specify a character conversion table to be loaded whenever this entry answers, before running the login script. If this field is blank, the conversion table stays unchanged.</dl>
<p> The edit menu also shows the latest date and time when you called this entry and the total number of calls there, but doesn&#8217;t let you change them. They are updated automatically when you connect. </p>
<p> The moVe command lets you move the highlighted entry up or down in the dialing directory with the up/down arrow keys or the k and j keys. Press Enter or ESC to end moving the entry. </p>
<h2>CONFIGURATION</h2>
<p> By pressing C-A O you will be thrown into the setup menu. </p>
<p> <code>Filenames and paths</code> </p>
<dl>
<dt>
<dd> This menu defines your default directories.</p>
<dl>
<dt><code>A &#8211; Download directory</code></p>
<dd> where the downloaded files go to.</p>
<dt><code>B &#8211; Upload directory</code></p>
<dd> where the uploaded files are read from.</p>
<dt><code>C &#8211; Script directory</code></p>
<dd> Where you keep your login scripts.</p>
<dt><code>D &#8211; Script program</code></p>
<dd> Which program to use as the script interpreter. Defaults to the program &quot;runscript&quot;, but if you want to use something else (eg, /bin/sh or &quot;expect&quot;) it is possible. Stdin and stdout are connected to the modem, stderr to the screen.</p>
<dl>
<dt>
<dd> If the path is relative (ie, does not start with a slash) then it&#8217;s relative to your home directory, except for the script interpreter.</dl>
<dt><code>E &#8211; Kermit program</code></p>
<dd> Where to find the executable for kermit, and it&#8217;s options. Some simple macro&#8217;s can be used on the command line: &#8216;%l&#8217; is expanded to the complete filename of the dial out-device, &#8216;%f&#8217; is expanded to the serial port file descriptor and &#8216;%b&#8217; is expanded to the current serial port speed.</p>
<dt><code>F &#8211; Logging options</code></p>
<dd> Options to configure the logfile writing.</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>A &#8211; File name</code></p>
<dd> Here you can enter the name of the logfile. The file will be written in your home directory, and the default value is &quot;minicom.log&quot;. If you blank the name, all logging is turned off.</p>
<dt><code>B &#8211; Log connects and hangups</code></p>
<dd> This option defines whether or not the logfile is written when the remote end answers the call or hangs up. Or when you give the hangup command yourself or leave minicom without hangup while online.</p>
<dt><code>C &#8211; Log file transfers</code></p>
<dd> Do you want log entries of receiving and sending files.</dl>
</dl>
<p> The &#8216;log&#8217; command in the scripts is not affected by logging options B and C. It is always executed, if you just have the name of the log file defined.</dl>
</dl>
<p> <code>File Transfer Protocols</code> </p>
<dl>
<dt>
<dd> Protocols defined here will show up when C-A s/r is pressed. &quot;Name&quot; in the beginning of the line is the name that will show up in the menu. &quot;Program&quot; is the path to the protocol. &quot;Name&quot; after that defines if the program needs an argument, e.g. a file to be transmitted. U/D defines if this entry should show up in the upload or the download menu. Fullscr defines if the program should run full screen, or that minicom will only show it&#8217;s stderr in a window. IO-Red defines if minicom should attach the program&#8217;s standard in and output to the modem port or not. &quot;Multi&quot; tells the filename selection window whether or not the protocol can send multiple files with one command. It has no effect on download protocols, and it is also ignored with upload protocols if you don&#8217;t use the filename selection window. The old sz and rz are not full screen, and have IO-Red set. However, there are curses based versions of at least rz that do not want their stdin and stdout redirected, and run full screen. All file transfer protocols are run with the UID of the user, and not with UID=root. &#8216;%l&#8217;, &#8216;%f&#8217; and &#8216;%b&#8217; can be used on the command line as with kermit. Within this menu you can also define if you want to use the filename selection window when prompted for files to upload, and if you like to be prompted for the download directory every time the automatic download is started. If you leave the download directory prompt disabled, the download directory defined in the file and directory menu is used.</dl>
<p> <code>Serial port setup</code></p>
<dl>
<dt>
<dd>
<dl>
<dt><code>A &#8211; Serial device</code></p>
<dd> /dev/tty1 or /dev/ttyS1 for most people. /dev/cua&lt;n&gt; is still possible under GNU/Linux, but no longer recommended as these devices are obsolete and many systems with kernel 2.2.x or newer don&#8217;t have them. Use /dev/ttyS&lt;n&gt; instead. You may also have /dev/modem as a symlink to the real device.<br />
 If you have modems connected to two or more serial ports, you may specify all of them here in a list separated by space, comma or semicolon. When Minicom starts, it checks the list until it finds an available modem and uses that one. (However, you can&#8217;t specify different init strings to them&#8230; at least not yet.)<br />
 To use a UNIX socket for communication the device name must be prefixed with &quot;unix#&quot; following by the full path and the filename of the socket. Minicom will then try to connect to this socket as a client. As long as it cannot connect to the socket it stays &#8216;offline&#8217;. As soon as the connection establishes, minicom goes &#8216;online&#8217;. If the server closes the socket, minicom switches to &#8216;offline&#8217; again.</p>
<dt><code>B &#8211; Lock file location</code></p>
<dd> On most systems This should be /usr/spool/uucp. GNU/Linux systems use /var/lock. If this directory does not exist, minicom will not attempt to use lockfiles.</p>
<dt><code>C &#8211; Callin program</code></p>
<dd> If you have a uugetty or something on your serial port, it could be that you want a program to be run to switch the modem cq. port into dialin/dialout mode. This is the program to get into dialin mode.</p>
<dt><code>D &#8211; Callout program</code></p>
<dd> And this to get into dialout mode.</p>
<dt><code>E &#8211; Bps/Par/Bits</code></p>
<dd> Default parameters at startup.</dl>
<p> If one of the entries is left blank, it will not be used. So if you don&#8217;t care about locking, and don&#8217;t have a getty running on your modemline, entries B &#8211; D should be left blank.</dl>
<p> <code>Modem and Dialing</code> </p>
<dl>
<dt>
<dd> Here, the parameters for your modem are defined. I will not explain this further because the defaults are for generic Hayes modems, and should work always. This file is not a Hayes tutorial :-) The only things worth noticing are that control characters can be sent by prefixing them with a &#8216;^&#8217;, in which &#8216;^^&#8217; means &#8216;^&#8217; itself, and the &#8216;\&#8217; character must also be doubled as &#8216;\&#8217;, because backslash is used specially in the macro definitions. Some options however, don&#8217;t have much to do with the modem but more with the behaviour of minicom itself: </p>
<dl>
<dt><code>M &#8211; Dial time</code></p>
<dd> The number of seconds before minicom times out if no connection is established.</p>
<dt><code>N &#8211; Delay before redial</code></p>
<dd> Minicom will redial if no connection was made, but it first waits some time.</p>
<dt><code>O &#8211; Number of tries</code></p>
<dd> Maximum number of times that minicom attempts to dial.</p>
<dt><code>P &#8211; Drop DTR time</code></p>
<dd> If you set this to 0, minicom hangs up by sending a Hayes-type hangup sequence. If you specify a non-zero value, the hangup will be done by dropping the DTR line. The value tells in seconds how long DTR will be kept down.</p>
<dt><code>Q &#8211; Auto bps detect</code></p>
<dd> If this is on, minicom tries to match the dialed party&#8217;s speed. With most modern modems this is NOT desirable, since the modem buffers the data and converts the speed.</p>
<dt><code>R &#8211; Modem has DCD line</code></p>
<dd> If your modem, and your O/S both support the DCD line (that goes &#8216;high&#8217; when a connection is made) minicom will use it. When you have this option on, minicom will also NOT start dialing while you are already online.</p>
<dt><code>S &#8211; Status line shows DTE speed / line speed</code></p>
<dd> You can toggle the status line to show either the DTE speed (the speed which minicom uses to communicate with your modem) or the line speed (the speed that your modem uses on the line to communicate with the other modem). Notice that the line speed may change during the connection, but you will still only see the initial speed that the modems started the connection with. This is because the modem doesn&#8217;t tell the program if the speed is changed. Also, to see the line speed, you need to have the modem set to show it in the connect string. Otherwise you will only see 0 as the line speed.</p>
<dt><code>T &#8211; Multi-line untag</code></p>
<dd> You can toggle the feature to untag entries from the dialing directory when a connection is established to a multi-line BBS. All the tagged entries that have the same name are untagged.</dl>
</dl>
<dl>
<dt>
<dd> <code>Note that a special exception is made for this menu: every user</code> <code>can change all parameters here, but some of them will not be saved.</code></dl>
<p> <code>Screen and keyboard</code></p>
<dl>
<dt>
<dd>
<dl>
<dt><code>A &#8211; Command key is</code></p>
<dd> the &#8216;Hot Key&#8217; that brings you into command mode. If this is set to &#8216;ALT&#8217; or &#8216;meta key&#8217;, you can directly call commands by alt-key instead of HotKey-key.</p>
<dt><code>B &#8211; Backspace key sends</code></p>
<dd> There still are some systems that want a VT100 to send DEL instead of BS. With this option you can enable that stupidity. (Eh, it&#8217;s even on by default&#8230;)</p>
<dt><code>C &#8211; Status line is</code></p>
<dd> Enabled or disabled. Some slow terminals (for example, X-terminals) cause the status line to jump &quot;up and down&quot; when scrolling, so you can turn it off if desired. It will still be shown in command-mode.</p>
<dt><code>D &#8211; Alarm sound</code></p>
<dd> If turned on, minicom will sound an alarm (on the console only) after a successful connection and when up/downloading is complete.</p>
<dt><code>E &#8211; Foreground Color (menu)</code></p>
<dd> indicates the foreground color to use for all the configuration windows in minicom.</p>
<dt><code>F &#8211; Background Color (menu)</code></p>
<dd> indicates the background color to use for all the configuration windows in minicom. Note that minicom will not allow you to set foreground and background colors to the same value.</p>
<dt><code>G &#8211; Foreground Color (term)</code></p>
<dd> indicates the foreground color to use in the terminal window.</p>
<dt><code>H &#8211; Background Color (term)</code></p>
<dd> indicates the background color to use in the terminal window. Note that minicom will not allow you to set foreground and background colors to the same value.</p>
<dt><code>I &#8211; Foreground Color (stat)</code></p>
<dd> indicates the foreground color to use in for the status bar.</p>
<dt><code>J &#8211; Background Color (stat)</code></p>
<dd> indicates the color to use in for the status bar. Note that minicom will allow you to set the status bar&#8217;s foreground and background colors to the same value. This will effectively make the status bar invisible but if these are your intentions, please see the option</p>
<dt><code>K &#8211; History buffer size</code></p>
<dd> The number of lines to keep in the history buffer (for backscrolling).</p>
<dt><code>L &#8211; Macros file</code></p>
<dd> is the full path to the file that holds macros. Macros allow you to define a string to be sent when you press a certain key. In minicom, you may define F1 through F10 to send up to 256 characters [this is set at compile time]. The filename you specify is verified as soon as you hit ENTER. If you do not have permissions to create the specified file, an error message will so indicate and you will be forced to re-edit the filename. If you are permitted to create the file, minicom checks to see if it already exists. If so, it assumes it&#8217;s a macro file and reads it in. If it isn&#8217;t, well, it&#8217;s your problem :-) If the file does not exist, the filename is accepted.</p>
<dt><code>M &#8211; Edit Macros</code></p>
<dd> opens up a new window which allows you to edit the F1 through F10 macros.</p>
<dt><code>N &#8211; Macros enabled</code></p>
<dd> &#8211; Yes or No. If macros are disabled, the F1-F10 keys will just send the VT100/VT220 function key escape sequences.</p>
<dt><code>O &#8211; Character conversion</code></p>
<dd> The active conversion table filename is shown here. If you can see no name, no conversion is active. Pressing O, you will see the conversion table edit menu.</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>Edit Macros</code></p>
<dd> Here, the macros for F1 through F10 are defined. The bottom of the window shows a legend of character combinations that have special meaning. They allow you to enter special control characters with plain text by prefixing them with a &#8216;^&#8217;, in which &#8216;^^&#8217; means &#8216;^&#8217; itself. You can send a 1 second delay with the &#8216;^~&#8217; code. This is useful when you are trying to login after ftp&#8217;ing or telnet&#8217;ing somewhere. You can also include your current username and password from the phone directory in the macros with &#8216;
