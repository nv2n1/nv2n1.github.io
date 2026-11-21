---
title: "minicom(1)"
name: "minicom"
section: "1"
letter: "m"
url: "/docs/linux/man/1-minicom/"
description: "minicom – friendly serial communication program"
---
<h2>NAME</h2>
<p> minicom - friendly serial communication program  </p>
<h2>SYNOPSIS</h2>
<p> <code>minicom</code> [options] [<i>configuration</i>]  </p>
<h2>DESCRIPTION</h2>
<p> <code>minicom</code> is a communication program which somewhat resembles the shareware program TELIX but is free with source code and runs under most Unices. Features include dialing directory with auto-redial, support for UUCP-style lock files on serial devices, a separate script language interpreter, capture to file, multiple users with individual configurations, and more.  </p>
<h2>COMMAND-LINE</h2>
<dl>
<dt><code>-s, --setup</code></dt>
<dd> <p> <code>S</code>etup. Root edits the system-wide defaults in /etc/minirc.dfl with this option. When it is used, minicom does <i>not </i> initialize, but puts you directly into the configuration menu. This is very handy if minicom refuses to start up because your system has changed, or for the first time you run minicom. For most systems, reasonable defaults are already compiled in. </p>
 </dd>
<dt><code>-o, --noinit</code></dt>
<dd> <p> Do not initialize. Minicom will skip the initialization code. This option is handy if you quit from minicom without resetting, and then want to restart a session. It is potentially dangerous though: no check for lock files etc. is made, so a normal user could interfere with things like UUCP... maybe this will be taken out later. For now it is assumed, that users who are given access to a modem are responsible enough for their actions. </p>
 </dd>
<dt><code>-m, --metakey</code></dt>
<dd> <p> Override command-key with the Meta or ALT key. This is the default in 1.80 and it can also be configured in one of minicom&#8217;s menus, but if you use different terminals all the time, of which some don&#8217;t have a Meta or ALT key, it&#8217;s handy to set the default command key to Ctrl-A and use this option when you have a keyboard supporting Meta or ALT keys. Minicom assumes that your Meta key sends the ESC prefix, not the other variant that sets the highest bit of the character. </p>
 </dd>
<dt><code>-M, --metakey8</code></dt>
<dd> <p> Same as -m, but assumes that your Meta key sets the 8th bit of the character high (sends 128 + character code). </p>
 </dd>
<dt><code>-z, --statline</code></dt>
<dd> <p> Use terminal status line. This only works on terminals that support it and that have the relevant information in their <i>termcap</i> or <i>terminfo</i> database entry. </p>
 </dd>
<dt><code>-l, --ansi</code></dt>
<dd> <p> <code>L</code>iteral translation of characters with the high bit set. With this flag on, minicom will try to translate the IBM line characters to ASCII. Many PC-unix clones will display character correctly without translation (Linux in a special mode, Coherent and SCO). </p>
 </dd>
<dt><code>-L, --iso</code></dt>
<dd> <p> Ditto but assume screen uses an ISO8859 character set. </p>
 </dd>
<dt><code>-w, --wrap</code></dt>
<dd> <p> Turns line-wrap on at startup by default. </p>
 </dd>
<dt><code>-H, --displayhex</code></dt>
<dd> <p> Turn on output in hex mode. </p>
 </dd>
<dt><code>-a, --attrib=on/off</code></dt>
<dd> <p> <code>A</code>ttribute usage. Some terminals, notably Televideo&#8217;s, have rotten attribute handling (serial instead of parallel). By default, minicom uses &#8216;-a on&#8217;, but if you are using such a terminal you can (must!) supply the option &#8216;-a off&#8217;. The trailing &#8216;on&#8217; or &#8216;off&#8217; is needed. </p>
 </dd>
<dt><code>-t, --term=TERM</code></dt>
<dd> <p> <code>T</code>erminal type. With this flag, you can override the environment TERM variable. This is handy for use in the MINICOM environment variable; one can create a special termcap entry for use with minicom on the console, that initializes the screen to raw mode so that in conjunction with the -l flag, the IBM line characters are displayed untranslated. </p>
 </dd>
<dt><code>-c, --color=on/off</code></dt>
<dd> <p> <code>C</code>olor usage. Some terminals (such as the Linux console) support color with the standard ANSI escape sequences. Because there is apparently no termcap support for color, these escape sequences are hard-coded into minicom. Therefore this option is off by default. You can turn it on with &#8216;-c on&#8217;. This, and the &#8216;-m&#8217; option, are good candidates to put into the MINICOM environment variable. </p>
 </dd>
<dt><code>-S, --script=SCRIPT</code></dt>
<dd> <p> <code>script</code>. Run the named script at startup. So far, passing username and password to a startup script is not supported. If you also use the -d option to start dialing at startup, the -S script will be run BEFORE dialing the entries specified with -d. </p>
 </dd>
<dt><code>-d, --dial=ENTRY</code></dt>
<dd> <p> <code>D</code>ial an entry from the dialing directory on startup. You can specify an index number, but also a substring of the name of the entry. If you specify a name that has multiple entries in the directory, they are all tagged for dialing. You can also specify multiple names or index numbers by separating them with commas. The dialing will start from the first entry specified after all other program initialization procedures are completed. </p>
 </dd>
<dt><code>-p, --ptty=TTYP</code></dt>
<dd> <p> <code>P</code>seudo terminal to use. This overrides the terminal port defined in the configuration files, but only if it is a pseudo TTY. The filename supplied must be of the form (/dev/)tty[p-z/][0-f], (/dev/)pts[p-z/][0-f] or (/dev/)pty[p-z/][0-f]. For example, /dev/ttyp1, pts/0 or /dev/ptyp2. </p>
 </dd>
<dt><code>-C, --capturefile=FILE</code></dt>
<dd> <p> <code>filename</code>. Open capture file at startup. </p>
 </dd>
<dt><code>-T, --disabletime</code></dt>
<dd> <p> Disable the display of the online time in the status bar. </p>
 </dd>
<dt><code>-b, --baudrate</code></dt>
<dd> <p> Specify the baud rate, overriding the value given in the configuration file. </p>
 </dd>
<dt><code>-D, --device</code></dt>
<dd> <p> Specify the device, overriding the value given in the configuration file. </p>
 </dd>
<dt><code>-R, --remotecharset</code></dt>
<dd> <p> Specify the character set of the remote system is using and convert it to the character set of the local side. Example might be &#8216;latin1&#8217;. </p>
 </dd>
<dt><code>-7, --7bit</code></dt>
<dd> <p> 7bit mode for terminals which aren&#8217;t 8bit capable. 8bit is default if the environment is configured for this via LANG or LC_ALL, 7bit otherwise. </p>
 </dd>
<dt><code>-8, --8bit</code></dt>
<dd> <p> 8bit characters pass through without any modification. &#8216;Continuous&#8217; means no locate/attribute control sequences are inserted without real change of locate/attribute. This mode is to display 8bit multi-byte characters such as Japanese. Not needed in every language with 8bit characters. (For example displaying Finnish text doesn&#8217;t need this.) </p>
 </dd>
<dt><code>-h, --help</code></dt>
<dd> <p> Display help and exit. </p>
 </dd>
<dt><code>-v, --version</code></dt>
<dd> <p> Print the minicom version. </p>
 </dd></dl>
<dl>
<dd> <p> When <code>minicom</code> starts, it first searches the MINICOM environment variable for command-line arguments, which can be over-ridden on the command line. Thus, if you have done </p>
 </dd>
<dl>
<dd> <p> MINICOM=&#8216;-m -c on&#8217; </p>
<p> export MINICOM </p>
 </dd></dl>
<p> or the equivalent, and start minicom, minicom will assume that your terminal <i>has </i> a Meta or &lt;ALT&gt; key and that color is supported. If you then log in from a terminal without color support, and you have set MINICOM in your startup (.profile or equivalent) file, and don&#8217;t want to re-set your environment variable, you can type &#8216;minicom -c off&#8217; and run without color support for that session. </dl>
 </p>
<dl>
<dt><code>configuration</code></dt>
<dd> <p> The <i>configuration</i> argument is more interesting. Normally, minicom gets its defaults from a file called &quot;minirc.dfl&quot;. If you however give an argument to minicom, it will try to get its defaults from a file called &quot;minirc.<i>configuration</i>&quot;. So it is possible to create multiple configuration files, for different ports, different users etc. Most sensible is to use device names, such as tty1, tty64, sio2 etc. If a user creates his own configuration file, it will show up in his home directory as &quot;.minirc.dfl&quot; or &quot;.minirc.<i>configuration</i>&quot;. </p>
 </dd></dl>
<h2>USE</h2>
<p> Minicom is window based. To pop-up a window with the function you want, press Control-A (from now on, we will use C-A to mean Control-A), and then the function key (a-z or A-Z). By pressing C-A first and then &#8216;z&#8217;, a help screen comes up with a short summary of all commands. This escape key can be altered when minicom is configured (-s option or C-A O), but we&#8217;ll stick to Control-A for now. </p>
<p> For every menu the next keys can be used: </p>
<dl>
<dt><code>UP</code></dt>
<dd> <p> arrow-up or &#8216;k&#8217; </p>
 </dd>
<dt><code>DOWN</code></dt>
<dd> <p> arrow-down or &#8216;j&#8217; </p>
 </dd>
<dt><code>LEFT</code></dt>
<dd> <p> arrow-left or &#8216;h&#8217; </p>
 </dd>
<dt><code>RIGHT</code></dt>
<dd> <p> arrow-right or &#8216;l&#8217; </p>
 </dd>
<dt><code>CHOOSE</code></dt>
<dd> <p> Enter </p>
 </dd>
<dt><code>CANCEL</code></dt>
<dd> <p> ESCape. </p>
 </dd></dl>
<p> The screen is divided into two portions: the upper 24 lines are the terminal-emulator screen. In this window, ANSI or VT100 escape sequences are interpreted. If there is a line left at the bottom, a status line is placed there. If this is not possible the status line will be showed every time you press C-A. On terminals that have a special status line that will be used if the termcap information is complete <i>and</i> the <code>-k</code> flag has been given. </p>
<p> Possible commands are listed next, in alphabetical order. </p>
<dl>
<dt><code>C-A</code></dt>
<dd> <p> Pressing C-A a second time will just send a C-A to the remote system. If you have changed your &quot;escape character&quot; to something other than C-A, this works analogously for that character. </p>
 </dd>
<dt><code>A</code></dt>
<dd> <p> Toggle &#8216;Add Linefeed&#8217; on/off. If it is on, a linefeed is added before every carriage return displayed on the screen. </p>
 </dd>
<dt><code>B</code></dt>
<dd> <p> Gives you a scroll back buffer. You can scroll up with <code>u</code>, down with <code>d</code>, a page up with <code>b</code>, a page down with <code>f</code>, and if you have them the <code>arrow</code> and <code>page up/page down</code> keys can also be used. You can search for text in the buffer with <code>s</code> (case-sensitive) or <code>S</code> (case-insensitive). <code>N</code> will find the next occurrence of the string. <code>c</code> will enter citation mode. A text cursor appears and you specify the start line by hitting Enter key. Then scroll back mode will finish and the contents with prefix &#8216;&gt;&#8216; will be sent. </p>
 </dd>
<dt><code>C</code></dt>
<dd> <p> Clears the screen. </p>
 </dd>
<dt><code>D</code></dt>
<dd> <p> Dial a number, or go to the dialing directory. </p>
 </dd>
<dt><code>E</code></dt>
<dd> <p> Toggle local echo on and off (if your version of minicom supports it). </p>
 </dd>
<dt><code>F</code></dt>
<dd> <p> A break signal is sent to the modem. </p>
 </dd>
<dt><code>G</code></dt>
<dd> <p> Run script (Go). Runs a login script. </p>
 </dd>
<dt><code>H</code></dt>
<dd> <p> Hangup. </p>
 </dd>
<dt><code>I</code></dt>
<dd> <p> Toggle the type of escape sequence that the cursor keys send between normal and applications mode. (See also the comment about the status line below). </p>
 </dd>
<dt><code>J</code></dt>
<dd> <p> Jump to a shell. On return, the whole screen will be redrawn. </p>
 </dd>
<dt><code>K</code></dt>
<dd> <p> Clears the screen, runs kermit and redraws the screen upon return. </p>
 </dd>
<dt><code>L</code></dt>
<dd> <p> Turn Capture file on off. If turned on, all output sent to the screen will be captured in the file too. </p>
 </dd>
<dt><code>M</code></dt>
<dd> <p> Sends the modem initialization string. If you are online and the DCD line setting is on, you are asked for confirmation before the modem is initialized. </p>
 </dd>
<dt><code>N</code></dt>
<dd> <p> Toggle between three states, whether each line is prefixed with current date and time, a timestamp is added every second, or no timestamps. </p>
 </dd>
<dt><code>O</code></dt>
<dd> <p> Configure minicom. Puts you in the configuration menu. </p>
 </dd>
<dt><code>P</code></dt>
<dd> <p> Communication Parameters. Allows you to change the bps rate, parity and number of bits. </p>
 </dd>
<dt><code>Q</code></dt>
<dd> <p> Exit minicom without resetting the modem. If macros changed and were not saved, you will have a chance to do so. </p>
 </dd>
<dt><code>R</code></dt>
<dd> <p> Receive files. Choose from various protocols (external). If you have the filename selection window and the prompt for download directory enabled, you&#8217;ll get a selection window for choosing the directory for downloading. Otherwise the download directory defined in the Filenames and paths menu will be used. </p>
 </dd>
<dt><code>S</code></dt>
<dd> <p> Send files. Choose the protocol like you do with the receive command. If you don&#8217;t have the filename selection window enabled (in the File transfer protocols menu), you&#8217;ll just have to write the filename(s) in a dialog window. If you have the selection window enabled, a window will pop up showing the filenames in your upload directory. You can tag and untag filenames by pressing spacebar, and move the cursor up and down with the cursor keys or j/k. The selected filenames are shown highlighted. Directory names are shown [within brackets] and you can move up or down in the directory tree by pressing the spacebar twice. Finally, send the files by pressing ENTER or quit by pressing ESC. </p>
 </dd>
<dt><code>T</code></dt>
<dd> <p> Choose Terminal emulation: Ansi(color) or vt100. You can also change the backspace key here, turn the status line on or off, and define delay (in milliseconds) after each newline if you need that. </p>
 </dd>
<dt><code>W</code></dt>
<dd> <p> Toggle line-wrap on/off. </p>
 </dd>
<dt><code>X</code></dt>
<dd> <p> Exit minicom, reset modem. If macros changed and were not saved, you will have a chance to do so. </p>
 </dd>
<dt><code>Y</code></dt>
<dd> <p> Paste a file. Reads a file and sends its contests just as if it would be typed in. </p>
 </dd>
<dt><code>Z</code></dt>
<dd> <p> Pop up the help screen. </p>
 </dd></dl>
<h2>DIALING DIRECTORY</h2>
<p> By pressing C-A D the program puts you in the dialing directory. Select a command by pressing the capitalized letter or moving cursor right/left with the arrow keys or the h/l keys and pressing Enter. You can add, delete or edit entries and move them up and down in the directory list. By choosing &quot;dial&quot; the phone numbers of the tagged entries, or if nothing is tagged, the number of the highlighted entry will be dialed. While the modem is dialing, you can press escape to cancel dialing. Any other key will close the dial window, but won&#8217;t cancel the dialing itself. Your dialing directory will be saved into the file &quot;.dialdir&quot; in your home directory. You can scroll up and down with the arrow keys, but you can also scroll complete pages by pressing the PageUp or PageDown key. If you don&#8217;t have those, use Control-B (Backward) and Control-F (Forward). You can use the space bar to <code>tag</code> a number of entries and minicom will rotate trough this list if a connection can&#8217;t be made. A &#8216;&gt;&#8216; symbol is drawn in the directory before the names of the tagged entries. </p>
<p> The &quot;edit&quot; menu speaks for itself, but I will discuss it briefly here. </p>
<dl>
<dt><code>A - Name</code></dt>
<dd> <p> The name for this entry </p>
 </dd>
<dt><code>B - Number</code></dt>
<dd> <p> and its telephone number. </p>
 </dd>
<dt><code>C - Dial string #</code></dt>
<dd> <p> Which specific dial string you want to use to connect. There are three different dial strings (prefixes and suffixes) that can be configured in the <code>Modem and dialing</code> menu. </p>
 </dd>
<dt><code>D - Local echo</code></dt>
<dd> <p> can be on or off for this system (if your version of minicom supports it). </p>
 </dd>
<dt><code>E - Script </code></dt>
<dd> <p> The script that must be executed after a successful connection is made (see the manual for runscript) </p>
 </dd>
<dt><code>F - Username</code></dt>
<dd> <p> The username that is passed to the runscript program. It is passed in the environment string &quot;$LOGIN&quot;. </p>
 </dd>
<dt><code>G - Password</code></dt>
<dd> <p> The password is passed as &quot;$PASS&quot;. </p>
 </dd>
<dt><code>H - Terminal Emulation</code></dt>
<dd> <p> Use ANSI or VT100 emulation. </p>
 </dd>
<dt><code>I - Backspace key sends</code></dt>
<dd> <p> What code (Backspace or Delete) the backspace key sends. </p>
 </dd>
<dt><code>J - Linewrap</code></dt>
<dd> <p> Can be on or off. </p>
 </dd>
<dt><code>K - Line settings</code></dt>
<dd> <p> Bps rate, bits, parity and number of stop bits to use for this connection. You can choose <code>current</code> for the speed, so that it will use whatever speed is being used at that moment (useful if you have multiple modems). </p>
 </dd>
<dt><code>L - Conversion table</code></dt>
<dd> <p> You may specify a character conversion table to be loaded whenever this entry answers, before running the login script. If this field is blank, the conversion table stays unchanged. </p>
 </dd></dl>
<p> The edit menu also shows the latest date and time when you called this entry and the total number of calls there, but doesn&#8217;t let you change them. They are updated automatically when you connect. </p>
<p> The moVe command lets you move the highlighted entry up or down in the dialing directory with the up/down arrow keys or the k and j keys. Press Enter or ESC to end moving the entry. </p>
<h2>CONFIGURATION</h2>
<p> By pressing C-A O you will be thrown into the setup menu. </p>
<p> <code>Filenames and paths</code> </p>
<dl>
<dd> <p> This menu defines your default directories. </p>
 </dd>
<dl>
<dt><code>A - Download directory</code></dt>
<dd> <p> where the downloaded files go to. </p>
 </dd>
<dt><code>B - Upload directory</code></dt>
<dd> <p> where the uploaded files are read from. </p>
 </dd>
<dt><code>C - Script directory</code></dt>
<dd> <p> Where you keep your login scripts. </p>
 </dd>
<dt><code>D - Script program</code></dt>
<dd> <p> Which program to use as the script interpreter. Defaults to the program &quot;runscript&quot;, but if you want to use something else (eg, /bin/sh or &quot;expect&quot;) it is possible. Stdin and stdout are connected to the modem, stderr to the screen. </p>
 </dd>
<dl>
<dd> <p> If the path is relative (ie, does not start with a slash) then it&#8217;s relative to your home directory, except for the script interpreter. </p>
 </dd></dl>
<dt><code>E - Kermit program</code></dt>
<dd> <p> Where to find the executable for kermit, and it&#8217;s options. Some simple macro&#8217;s can be used on the command line: &#8216;%l&#8217; is expanded to the complete filename of the dial out-device, &#8216;%f&#8217; is expanded to the serial port file descriptor and &#8216;%b&#8217; is expanded to the current serial port speed. </p>
 </dd>
<dt><code>F - Logging options</code></dt>
<dd> <p> Options to configure the logfile writing. </p>
 </dd>
<dl>
<dd>  </dd>
<dl>
<dt><code>A - File name</code></dt>
<dd> <p> Here you can enter the name of the logfile. The file will be written in your home directory, and the default value is &quot;minicom.log&quot;. If you blank the name, all logging is turned off. </p>
 </dd>
<dt><code>B - Log connects and hangups</code></dt>
<dd> <p> This option defines whether or not the logfile is written when the remote end answers the call or hangs up. Or when you give the hangup command yourself or leave minicom without hangup while online. </p>
 </dd>
<dt><code>C - Log file transfers</code></dt>
<dd> <p> Do you want log entries of receiving and sending files. </p>
 </dd></dl>
</dl>
<p> The &#8216;log&#8217; command in the scripts is not affected by logging options B and C. It is always executed, if you just have the name of the log file defined. </dl>
 </dl>
 </p>
<p> <code>File Transfer Protocols</code> </p>
<dl>
<dd> <p> Protocols defined here will show up when C-A s/r is pressed. &quot;Name&quot; in the beginning of the line is the name that will show up in the menu. &quot;Program&quot; is the path to the protocol. &quot;Name&quot; after that defines if the program needs an argument, e.g. a file to be transmitted. U/D defines if this entry should show up in the upload or the download menu. Fullscr defines if the program should run full screen, or that minicom will only show it&#8217;s stderr in a window. IO-Red defines if minicom should attach the program&#8217;s standard in and output to the modem port or not. &quot;Multi&quot; tells the filename selection window whether or not the protocol can send multiple files with one command. It has no effect on download protocols, and it is also ignored with upload protocols if you don&#8217;t use the filename selection window. The old sz and rz are not full screen, and have IO-Red set. However, there are curses based versions of at least rz that do not want their stdin and stdout redirected, and run full screen. All file transfer protocols are run with the UID of the user, and not with UID=root. &#8216;%l&#8217;, &#8216;%f&#8217; and &#8216;%b&#8217; can be used on the command line as with kermit. Within this menu you can also define if you want to use the filename selection window when prompted for files to upload, and if you like to be prompted for the download directory every time the automatic download is started. If you leave the download directory prompt disabled, the download directory defined in the file and directory menu is used. </p>
 </dd></dl>
<p> <code>Serial port setup</code> </p>
<dl>
<dd>  </dd>
<dl>
<dt><code>A - Serial device</code></dt>
<dd> <p> /dev/tty1 or /dev/ttyS1 for most people. /dev/cua&lt;n&gt; is still possible under GNU/Linux, but no longer recommended as these devices are obsolete and many systems with kernel 2.2.x or newer don&#8217;t have them. Use /dev/ttyS&lt;n&gt; instead. You may also have /dev/modem as a symlink to the real device. <br />
 If you have modems connected to two or more serial ports, you may specify all of them here in a list separated by space, comma or semicolon. When Minicom starts, it checks the list until it finds an available modem and uses that one. (However, you can&#8217;t specify different init strings to them... at least not yet.) <br />
 To use a UNIX socket for communication the device name must be prefixed with &quot;unix#&quot; following by the full path and the filename of the socket. Minicom will then try to connect to this socket as a client. As long as it cannot connect to the socket it stays &#8216;offline&#8217;. As soon as the connection establishes, minicom goes &#8216;online&#8217;. If the server closes the socket, minicom switches to &#8216;offline&#8217; again. </p>
 </dd>
<dt><code>B - Lock file location</code></dt>
<dd> <p> On most systems This should be /usr/spool/uucp. GNU/Linux systems use /var/lock. If this directory does not exist, minicom will not attempt to use lockfiles. </p>
 </dd>
<dt><code>C - Callin program</code></dt>
<dd> <p> If you have a uugetty or something on your serial port, it could be that you want a program to be run to switch the modem cq. port into dialin/dialout mode. This is the program to get into dialin mode. </p>
 </dd>
<dt><code>D - Callout program</code></dt>
<dd> <p> And this to get into dialout mode. </p>
 </dd>
<dt><code>E - Bps/Par/Bits</code></dt>
<dd> <p> Default parameters at startup. </p>
 </dd></dl>
<p> If one of the entries is left blank, it will not be used. So if you don&#8217;t care about locking, and don&#8217;t have a getty running on your modemline, entries B - D should be left blank. </dl>
 </p>
<p> <code>Modem and Dialing</code> </p>
<dl>
<dd> <p> Here, the parameters for your modem are defined. I will not explain this further because the defaults are for generic Hayes modems, and should work always. This file is not a Hayes tutorial :-) The only things worth noticing are that control characters can be sent by prefixing them with a &#8216;^&#8216;, in which &#8216;^^&#8216; means &#8216;^&#8216; itself, and the &#8216;\&#8216; character must also be doubled as &#8216;\\&#8216;, because backslash is used specially in the macro definitions. Some options however, don&#8217;t have much to do with the modem but more with the behaviour of minicom itself: </p>
 </dd>
<dl>
<dt><code>M - Dial time</code></dt>
<dd> <p> The number of seconds before minicom times out if no connection is established. </p>
 </dd>
<dt><code>N - Delay before redial</code></dt>
<dd> <p> Minicom will redial if no connection was made, but it first waits some time. </p>
 </dd>
<dt><code>O - Number of tries</code></dt>
<dd> <p> Maximum number of times that minicom attempts to dial. </p>
 </dd>
<dt><code>P - Drop DTR time</code></dt>
<dd> <p> If you set this to 0, minicom hangs up by sending a Hayes-type hangup sequence. If you specify a non-zero value, the hangup will be done by dropping the DTR line. The value tells in seconds how long DTR will be kept down. </p>
 </dd>
<dt><code>Q - Auto bps detect</code></dt>
<dd> <p> If this is on, minicom tries to match the dialed party&#8217;s speed. With most modern modems this is NOT desirable, since the modem buffers the data and converts the speed. </p>
 </dd>
<dt><code>R - Modem has DCD line</code></dt>
<dd> <p> If your modem, and your O/S both support the DCD line (that goes &#8216;high&#8217; when a connection is made) minicom will use it. When you have this option on, minicom will also NOT start dialing while you are already online. </p>
 </dd>
<dt><code>S - Status line shows DTE speed / line speed</code></dt>
<dd> <p> You can toggle the status line to show either the DTE speed (the speed which minicom uses to communicate with your modem) or the line speed (the speed that your modem uses on the line to communicate with the other modem). Notice that the line speed may change during the connection, but you will still only see the initial speed that the modems started the connection with. This is because the modem doesn&#8217;t tell the program if the speed is changed. Also, to see the line speed, you need to have the modem set to show it in the connect string. Otherwise you will only see 0 as the line speed. </p>
 </dd>
<dt><code>T - Multi-line untag</code></dt>
<dd> <p> You can toggle the feature to untag entries from the dialing directory when a connection is established to a multi-line BBS. All the tagged entries that have the same name are untagged. </p>
 </dd></dl>
<dl>
<dd> <p> <code>Note that a special exception is made for this menu: every user</code> <code>can change all parameters here, but some of them will not be saved.</code> </p>
 </dd></dl>
<p> <code>Screen and keyboard</code> </p>
<dl>
<dd>  </dd>
<dl>
<dt><code>A - Command key is</code></dt>
<dd> <p> the &#8216;Hot Key&#8217; that brings you into command mode. If this is set to &#8216;ALT&#8217; or &#8216;meta key&#8217;, you can directly call commands by alt-key instead of HotKey-key. </p>
 </dd>
<dt><code>B - Backspace key sends</code></dt>
<dd> <p> There still are some systems that want a VT100 to send DEL instead of BS. With this option you can enable that stupidity. (Eh, it&#8217;s even on by default...) </p>
 </dd>
<dt><code>C - Status line is</code></dt>
<dd> <p> Enabled or disabled. Some slow terminals (for example, X-terminals) cause the status line to jump &quot;up and down&quot; when scrolling, so you can turn it off if desired. It will still be shown in command-mode. </p>
 </dd>
<dt><code>D - Alarm sound</code></dt>
<dd> <p> If turned on, minicom will sound an alarm (on the console only) after a successful connection and when up/downloading is complete. </p>
 </dd>
<dt><code>E - Foreground Color (menu)</code></dt>
<dd> <p> indicates the foreground color to use for all the configuration windows in minicom. </p>
 </dd>
<dt><code>F - Background Color (menu)</code></dt>
<dd> <p> indicates the background color to use for all the configuration windows in minicom. Note that minicom will not allow you to set foreground and background colors to the same value. </p>
 </dd>
<dt><code>G - Foreground Color (term)</code></dt>
<dd> <p> indicates the foreground color to use in the terminal window. </p>
 </dd>
<dt><code>H - Background Color (term)</code></dt>
<dd> <p> indicates the background color to use in the terminal window. Note that minicom will not allow you to set foreground and background colors to the same value. </p>
 </dd>
<dt><code>I - Foreground Color (stat)</code></dt>
<dd> <p> indicates the foreground color to use in for the status bar. </p>
 </dd>
<dt><code>J - Background Color (stat)</code></dt>
<dd> <p> indicates the color to use in for the status bar. Note that minicom will allow you to set the status bar&#8217;s foreground and background colors to the same value. This will effectively make the status bar invisible but if these are your intentions, please see the option </p>
 </dd>
<dt><code>K - History buffer size</code></dt>
<dd> <p> The number of lines to keep in the history buffer (for backscrolling). </p>
 </dd>
<dt><code>L - Macros file</code></dt>
<dd> <p> is the full path to the file that holds macros. Macros allow you to define a string to be sent when you press a certain key. In minicom, you may define F1 through F10 to send up to 256 characters [this is set at compile time]. The filename you specify is verified as soon as you hit ENTER. If you do not have permissions to create the specified file, an error message will so indicate and you will be forced to re-edit the filename. If you are permitted to create the file, minicom checks to see if it already exists. If so, it assumes it&#8217;s a macro file and reads it in. If it isn&#8217;t, well, it&#8217;s your problem :-) If the file does not exist, the filename is accepted. </p>
 </dd>
<dt><code>M - Edit Macros</code></dt>
<dd> <p> opens up a new window which allows you to edit the F1 through F10 macros. </p>
 </dd>
<dt><code>N - Macros enabled</code></dt>
<dd> <p> - Yes or No. If macros are disabled, the F1-F10 keys will just send the VT100/VT220 function key escape sequences. </p>
 </dd>
<dt><code>O - Character conversion</code></dt>
<dd> <p> The active conversion table filename is shown here. If you can see no name, no conversion is active. Pressing O, you will see the conversion table edit menu. </p>
 </dd>
<dl>
<dd>  </dd>
<dl>
<dt><code>Edit Macros</code></dt>
<dd> <p> Here, the macros for F1 through F10 are defined. The bottom of the window shows a legend of character combinations that have special meaning. They allow you to enter special control characters with plain text by prefixing them with a &#8216;^&#8216;, in which &#8216;^^&#8216; means &#8216;^&#8216; itself. You can send a 1 second delay with the &#8216;^~&#8216; code. This is useful when you are trying to login after ftp&#8217;ing or telnet&#8217;ing somewhere. You can also include your current username and password from the phone directory in the macros with &#8216;\u&#8217; and &#8216;\p&#8217;, respectively. If you need the backslash character in the macro, write it doubled as &#8216;\\&#8216;. To edit a macro, press the number (or letter for F10) and you will be moved to the end of the macro. When editing the line, you may use the left &amp; right arrows, Home &amp; End keys, Delete &amp; BackSpace, and ESC and RETURN. ESC cancels any changes made while ENTER accepts the changes. </p>
 </dd>
<dt><code>Character conversion</code></dt>
<dd> <p> Here you can edit the character conversion table. If you are not an American, you know that in many languages there are characters that are not included in the ASCII character set, and in the old times they may have replaced some less important characters in ASCII and now they are often represented with character codes above 127. AND there are various different ways to represent them. This is where you may edit conversion tables for systems that use a character set different from the one on your computer. </p>
 </dd>
<dt><code>A - Load table</code></dt>
<dd> <p> You probably guessed it. This command loads a table from the disk. You are asked a file name for the table. Predefined tables .mciso, .mcpc8 and .mcsf7 should be included with the program. Table .mciso does no conversion, .mcpc8 is to be used for connections with systems that use the 8-bit pc character set, and .mcsf7 is for compatibility with the systems that uses the good old 7-bit coding to replace the characters {|}[]\ with the diacritical characters used in Finnish and Swedish. </p>
 </dd>
<dt><code>B - Save table</code></dt>
<dd> <p> This one saves the active table on the filename you specify. </p>
 </dd>
<dt><code>C - edit char</code></dt>
<dd> <p> This is where you can make your own modifications to the existing table. First you are asked the character value (in decimal) whose conversion you want to change. Next you&#8217;ll say which character you want to see on your screen when that character comes from the outside world. And then you&#8217;ll be asked what you want to be sent out when you enter that character from your keyboard. </p>
 </dd>
<dt><code>D - next screen</code></dt>
<dd>  </dd>
<dt><code>E - prev screen</code></dt>
<dd> <p> Yeah, you probably noticed that this screen shows you what kind of conversions are active. The screen just is (usually) too small to show the whole table at once in an easy-to-understand format. This is how you can scroll the table left and right. </p>
 </dd>
<dt><code>F - convert capture</code></dt>
<dd> <p> Toggles whether or not the character conversion table is used when writing the capture file. </p>
 </dd></dl>
</dl>
</dl>
</dl>
<dl>
<dt><code>Save setup as dfl</code></dt>
<dd> <p> Save the parameters as the default for the next time the program is started. Instead of dfl, any other parameter name may appear, depending on which one was used when the program was started. </p>
 </dd>
<dt><code>Save setup as..</code></dt>
<dd> <p> Save the parameters under a special name. Whenever Minicom is started with this name as an argument, it will use these parameters. This option is of course privileged to root. </p>
 </dd>
<dt><code>Exit</code></dt>
<dd> <p> Escape from this menu without saving. This can also be done with ESC. </p>
 </dd>
<dt><code>Exit from minicom</code></dt>
<dd> <p> Only root will see this menu entry, if he/she started minicom with the &#8216;-s&#8217; option. This way, it is possible to change the configuration without actually running minicom. </p>
 </dd></dl>
<h2>STATUS LINE</h2>
<p> The status line has several indicators, that speak for themselves. The mysterious APP or NOR indicator probably needs explanation. The VT100 cursor keys can be in two modes: applications mode and cursor mode. This is controlled by an escape sequence. If you find that the cursor keys do not work in, say, vi when you&#8217;re logged in using minicom then you can see with this indicator whether the cursor keys are in applications or cursor mode. You can toggle the two with the C-A I key. If the cursor keys then work, it&#8217;s probably an error in the remote system&#8217;s termcap initialization strings (is).  </p>
<h2>LOCALES</h2>
<p> Minicom has support for local languages. This means you can change most of the English messages and other strings to another language by setting the environment variable LANG.  </p>
<h2>MISC</h2>
<p> If minicom is hung, kill it with SIGTERM . (This means kill -15, or since sigterm is default, just plain &quot;kill &lt;minicompid&gt;&quot;. This will cause a graceful exit of minicom, doing resets and everything. You may kill minicom from a script with the command &quot;! killall -9 minicom&quot; without hanging up the line. Without the -9 parameter, minicom first hangs up before exiting. </p>
<p> Since a lot of escape sequences begin with ESC (Arrow up is ESC [ A), Minicom does not know if the escape character it gets is you pressing the escape key, or part of a sequence. </p>
<p> An old version of Minicom, V1.2, solved this in a rather crude way: to get the escape key, you had to press it <i>twice</i>. </p>
<p> As of release 1.3 this has bettered a little: now a 1-second timeout is builtin, like in vi. For systems that have the select() system call the timeout is 0.5 seconds. And... surprise: a special Linux-dependent <code>hack</code> :-) was added. Now, minicom can separate the escape key and escape-sequences. To see how dirty this was done, look into wkeys.c. But it works like a charm!  </p>
<h2>FILES</h2>
<p> Minicom keeps it&#8217;s configuration files in one directory, usually /var/lib/minicom, /usr/local/etc or /etc. To find out what default directory minicom has compiled in, issue the command <i>minicom -h</i>. You&#8217;ll probably also find the demo files for <code><a href="/docs/linux/man/1-runscript/">runscript</a></code>(1), and the examples of character conversion tables either there or in the subdirectories of /usr/doc/minicom*. The conversion tables are named something like mc.* in that directory, but you probably want to copy the ones you need in your home directory as something beginning with a dot. </p>
<pre><code>minirc.*
$HOME/.minirc.*
$HOME/.dialdir
$HOME/minicom.log
/usr/share/locale/*/LC_MESSAGES/minicom.mo
</code></pre>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-runscript/">runscript</a></code>(1)  </p>
<h2>BUGS</h2>
<p> Please report any bugs to <i>minicom-devel [at] lists.alioth.debian.org</i>. Thank you!  </p>
<h2>AUTHORS</h2>
<p> The original author of minicom is Miquel van Smoorenburg (miquels [at] cistron.nl). He wrote versions up to 1.75. <br />
 Jukka Lahtinen (walker [at] netsonic.fi, jukkal [at] despammed.com) has been responsible for new versions since 1.78, helped by some other people, including: <br />
 filipg [at] paranoia.com wrote the History buffer searching to 1.79. <br />
 Arnaldo Carvalho de Melo (acme [at] conectiva.com.br) did the internationalization and the Brazilian Portuguese translations. <br />
 Jim Seymour (jseymour [at] jimsun.LinxNet.com) wrote the multiple modem support and the filename selection window used since 1.80. <br />
 Tomohiro Kubota (kubota [at] debian.or.jp) wrote the Japanese translations and the citation facility, and did some fixes. <br />
 Gael Queri (gqueri [at] mail.dotcom.fr) wrote the French translations. <br />
 Arkadiusz Miskiewicz (misiek [at] pld.org.pl) wrote the Polish translations. <br />
 Kim Soyoung (nexti [at] chollian.net) wrote the Korean translations. <br />
 Jork Loeser (jork.loeser [at] inf.tu-dresden.de) provided the socket extension. </p>
<p> Most of this man page is copied, with corrections, from the original minicom README, but some pieces and the corrections are by Michael K. Johnson. </p>
<p> Jukka Lahtinen (walker [at] netsonic.fi) has added some information of the changes made after version 1.75. </p>
