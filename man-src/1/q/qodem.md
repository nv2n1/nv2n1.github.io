---
title: "qodem(1)"
name: "qodem"
section: "1"
letter: "q"
url: "/docs/linux/man/1-qodem/"
description: "qodem – Qodem Terminal Emulator"
---

<h2 class="name">NAME</h2>
<p> qodem &#8211; Qodem Terminal Emulator</p>
<h2>SYNOPSIS</h2>
<p> <code>qodem</code> [ &#8211;enable-capture FILENAME ]<br />
 [ [ &#8211;connect HOST [ &#8211;connect-method method ]<br />
 [ &#8211;username name ] ] |<br />
 args&#8230; ] </p>
<dl>
<dt><code>qodem</code> [ &#8211;help | -h | -? ]</p>
<dd>
</dl>
<h2>DESCRIPTION</h2>
<p> <i>Qodem</i> is an open-source clone implementation of the popular DOS-based Qmodem serial communications program. Qodem incorporates many features that are useful on all kinds of text-based consoles such as scrollback buffer, session capture, screen dump, dialing directory, and also includes serial port handling and modem dialing. </p>
<p> The major features of Qodem are: </p>
<p>&nbsp;<wbr>&nbsp;<wbr>*&nbsp;<wbr>Unicode display: translation of CP437&nbsp;<wbr>(PC VGA), VT100 DEC Special<br />
&nbsp;<wbr>Graphics characters, VT220 National Replacement Character sets,<br />
&nbsp;<wbr>etc., to Unicode </p>
<p>&nbsp;<wbr>&nbsp;<wbr>*&nbsp;<wbr>Terminal interface conveniences: scrollback buffer, capture file,<br />
&nbsp;<wbr>screen dump, dialing directory, keyboard macros, script support </p>
<p>&nbsp;<wbr>&nbsp;<wbr>*&nbsp;<wbr>Connection methods: serial, local shell, command line, telnet,<br />
&nbsp;<wbr>ssh, rlogin, rsh </p>
<p>&nbsp;<wbr>&nbsp;<wbr>*&nbsp;<wbr>Emulations: ANSI, Avatar, VT52, VT100/102, VT220, Linux, and XTerm </p>
<p>&nbsp;<wbr>&nbsp;<wbr>*&nbsp;<wbr>Transfer protocols: Xmodem, Ymodem, Zmodem, and Kermit </p>
<h2>TERMINAL REQUIREMENTS</h2>
<p> Qodem requires the following characteristics of its shell/terminal: </p>
<p>&nbsp;<wbr>&nbsp;<wbr>*&nbsp;<wbr>Unicode capability.&nbsp;<wbr>&nbsp;<wbr>The raw Linux console, UXTerm, URxvt,<br />
&nbsp;<wbr>Konsole, and gnome-terminal all work well. </p>
<p>&nbsp;<wbr>&nbsp;<wbr>*&nbsp;<wbr>A Unicode font that includes the CP437&nbsp;<wbr>(PC VGA)&nbsp;<wbr>glyphs. </p>
<p>&nbsp;<wbr>&nbsp;<wbr>*&nbsp;<wbr>The meta key must use escape prefixing rather than setting the 8th<br />
&nbsp;<wbr>bit on the character.&nbsp;<wbr>&nbsp;<wbr>Many terminal emulators do this by<br />
&nbsp;<wbr>default.&nbsp;<wbr>&nbsp;<wbr>Qodem sends an xterm escape sequence to enable this<br />
&nbsp;<wbr>behavior.&nbsp;<wbr>&nbsp;<wbr>For XTerm, this can be enabled by clicking<br />
&nbsp;<wbr>CTRL-Mouse1&nbsp;<wbr>(left button)&nbsp;<wbr>and checking&nbsp;<wbr>&quot;Meta Sends Escape&quot;, or by<br />
&nbsp;<wbr>adding the following lines to&nbsp;<wbr>~/.Xresources:<br />
 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>XTerm*metaSendsEscape: true</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>UXTerm*metaSendsEscape: true</p>
<h2>EMULATIONS</h2>
<p> Emulations supported by Qodem and their status follows. Note that TTY, DEBUG, ANSI.SYS, AVATAR, LINUX, and XTERM emulations can use both CP437 (PC VGA) and ISO-8859-1 glyphs for 8-bit characters (see Alt-; Codepage below). If ISO-8859-1 is used, the C0 control characters (0x00 &#8211; 0x1F) are mapped to the equivalent CP437 glyphs since there are no glyphs defined in that range for ISO-8859-1.</p>
<dl>
<dt><code>ANSI</code></p>
<dd> This is the DOS-based &quot;ANSI.SYS&quot; emulation plus a few more codes than the original ANSI.SYS. It supports DSR 6 (Cursor Position) which many BBSes used to &quot;autodetect&quot; ANSI, and the following ANSI X3.64 functions: ICH, DCH, IL, DL, VPA, CHA, CHT, and REP. It also supports &quot;ANSI Music&quot; sequences that follow the &quot;PLAY&quot; command syntax; it plays these tones via SDL.</p>
<dt><code>AVATAR</code></p>
<dd> This is the BBS-era Avatar (&quot;Advanced Video Attribute Terminal Assembler and Recreator&quot;) emulation. It supports all of the &quot;Extended AVT/0&quot; commands as per George A. Stanislav&#8217;s 1 May 1989 document except for transmitting PC keyboard scan codes. It also includes ANSI fallback capability.</p>
<dt><code>VT52</code></p>
<dd> Fairly complete. Does not support HOLD SCREEN mode. Graphics mode glyphs that do not have direct Unicode equivalents render as a hatch.</p>
<dt><code>VT100</code></p>
<dd> Identical to VT102 except in how it responds to Device Attributes function.</p>
<dt><code>VT102</code></p>
<dd> Fairly complete. Double-width characters are not displayed with wide glyhps due to curses-based output. Does not support smooth scrolling, printing, keyboard locking, keyboard leds, and hardware tests. Many numeric keypad characters also do not work correctly due to console NUM LOCK handling. 132-column output is only supported if the host console / window is already 132 columns or wider; Qodem does <code>not</code> issue resize commands to the host console for 80/132 column switching codes.</p>
<dt><code>VT220</code></p>
<dd> Fairly complete. Converts National Replacement Character sets and DEC Supplemental Graphics characters to Unicode. In addition to limitations of VT102, also the following features are not supported: user-defined keys (DECUDK), downloadable fonts (DECDLD), VT100/ANSI compatibility mode (DECSCL).</p>
<dt><code>TTY</code></p>
<dd> This emulation supports bare control character handling (backspace, newline, etc.) and litte else. Characters that would be overwritten with underscores are instead made underlined as old teletypes would do.</p>
<dt><code>DEBUG</code></p>
<dd> This emulation displays all incoming characters in a format similar to a hex dump.</p>
<dt><code>LINUX</code></p>
<dd> This emulation has two modes: PC VGA (LINUX) and UTF-8 (L_UTF8). This emulation is similar to VT102 but also recognizes the Linux private mode sequences and ECMA-48 sequences VPA, CNL, CPL, ECH, CHA, VPA, VPR, and HPA. In addition to VT102 limitations, also the following features are not supported: selecting ISO 646/ISO 8859-1/UTF-8 character sets, X11 mouse reporting.</p>
<dt><code>XTERM</code></p>
<dd> This emulation has two modes: PC VGA (XTERM) and UTF-8 (X_UTF8). It is mostly identical to LINUX but also recognizes a few XTerm sequences and discards them to maintain a clean display. It does not support many of the features unique to XTerm such as Tektronix 4014 mode, mouse tracking, alternate screen buffer, and many more. </p>
</dl>
<h2>FILE TRANSFER PROTOCOLS</h2>
<p> Protocols supported by Qodem and their status follows:</p>
<dl>
<dt><code>XMODEM</code></p>
<dd> Supports original Xmodem, Xmodem-1k, Xmodem-CRC16, and Xmodem-G. Also supports &quot;Xmodem Relaxed&quot;, a variant of original Xmodem with longer timeouts.</p>
<dt><code>YMODEM</code></p>
<dd> Supports Ymodem and Ymodem-G. If a file exists, it will be appended to.</p>
<dt><code>ZMODEM</code></p>
<dd> Supports resume (crash recovery) and auto-start. Does not yet support changing block size on errors, so transfers over unreliable serial/modem connections might incur significant performance penalties.</p>
<dt><code>KERMIT</code></p>
<dd> Supports the original robust (slow) Kermit plus streaming and autostart. On reliable connections with streaming it should perform reasonably well. Does not yet support long or extra-long packets, RESEND/REGET, server mode, or sliding windows. </p>
</dl>
<h2>INTERFACE</h2>
<p> <code>Phonebook</code><br />
 When qodem first starts up, by default it will start in the phonebook. The menu on the bottom half of the screen lists the various actions available. When editing a phonebook entry, the status line will change to show options for each field. Connecting to a system or leaving the phonebook puts qodem in Terminal Mode. </p>
<p> <code>Terminal Mode</code><br />
 Terminal Mode is the main qodem terminal emulator interface. <code>Alt-Z</code> will bring up a help menu. While in Terminal Mode the following actions are supported:</p>
<dl>
<dt><code>Alt-D Phonebook</code></p>
<dd> This brings up the phonebook.</p>
<dt><code>Alt-G Term Emulation</code></p>
<dd> This brings up a menu to select the terminal emulation. Selecting the active terminal emulation will prompt to reset the emulation state; this may be useful to recover from corrupted escape sequences.</p>
<dt><code>Alt-C Clear Screen</code></p>
<dd> This clears the screen and homes the cursor.</p>
<dt><code>Alt-F Execute Script</code></p>
<dd> This prompts for a filename, and then executes that file as a script. Any program that reads from standard input and writes to standard output can be run as a script. See the section below on script support.</p>
<dt><code>Alt-K Send BREAK</code></p>
<dd> When connected via serial mode or modem, this calls tcsendbreak() to send a true &quot;Break Signal&quot; on the serial line.</p>
<dt><code>Alt-P Capture File</code></p>
<dd> Enable/disable capture to file. Three capture formats are supported: &quot;raw&quot;, &quot;text&quot;, and &quot;html&quot;. &quot;Raw&quot; format saves every byte as received from the other side before emulation processing; &quot;text&quot; saves UTF-8 characters after emulation processing; &quot;html&quot; saves in HTML format with Unicode entities and color attributes after emulation processing. ASCII file transfers will be included in the capture file; other file transfers (Xmodem, Ymodem, Zmodem, Kermit) are excluded from the capture file.</p>
<dt><code>Alt-S Split Screen</code></p>
<dd> This actives split screen mode, in which local characters are accumulated in a buffer before sending to the remote side. To send carriage return, enter &quot;^M&quot;.</p>
<dt><code>Alt-T Screen Dump</code></p>
<dd> This prompts for a filename, and then saves the current view to that file.</p>
<dt><code>Alt-Y COM Parameters</code></p>
<dd> This brings up a menu to alter the serial port settings.</p>
<dt><code>PgUp Upload Files</code></p>
<dd> This brings up the file upload menu. Note that CTRL-PgUp and ALT-PgUp may also work depending on the terminfo for the host terminal.</p>
<dt><code>PgDn Download Files</code></p>
<dd> This brings up the file download menu. Note that CTRL-PgDn and ALT-PgDn may also work depending on the terminfo for the host terminal.</p>
<dt><code>Alt-\ Compose Key</code></p>
<dd> This brings up a dialog to enter the 3-digit decimal value (0-255) for an 8-bit byte or a 4-digit hexadecimal value (0-ffff) for a 16-bit Unicode character (L_UTF8 and X_UTF8 only).</p>
<dt><code>Alt-; Codepage</code></p>
<dd> This brings up a dialog to change the current codepage. Codepages are limited by the current emulation. VT52, VT100, VT102, VT220, L_UTF8, and X_UTF8 can only be set to the DEC codepage; LINUX, XTERM, ANSI, AVATAR, TTY, and DEBUG emulations can be set to either CP437 (VGA) or ISO-8859-1.</p>
<dt><code>Alt-/ Scroll Back</code></p>
<dd> This selects the scrollback buffer. When viewing the buffer, &quot;S&quot; saves to file and &quot;C&quot; clears the scrollback buffer. By default qodem supports up to 20000 lines of scrollback; this can be changed by editing scrollback_max in scrollback.c.</p>
<dt><code>Alt-H Hangup/Close</code></p>
<dd> This hangs up the modem (drops DTR) or closes the remote connection (kills the child process).</p>
<dt><code>Alt-L Log View</code></p>
<dd> This brings the session log up in an editor. The session log stores information about connect, disconnect, and file upload/download events.</p>
<dt><code>Alt-M Mail Reader</code></p>
<dd> This spawns the mail reader, by default <code>mm</code>.</p>
<dt><code>Alt-X Exit Qodem</code></p>
<dd> This prompts to exit qodem. When not connected, Ctrl-C will also bring up the exit prompt.</p>
<dt><code>Alt-A Translate Table</code></p>
<dd> This brings up the translate table editor. Both incoming and outgoing bytes can be changed or stripped (set to ASCII NUL (0)). Note that translation occurs before both emulation processing and UTF-8 decoding.</p>
<dt><code>Alt-J Function Keys</code></p>
<dd> This brings up the keyboard macro editor. Keyboard macros support substitutions for carriage return (&quot;^M&quot;), the phonebook entry username (&quot;$USERNAME&quot;), and the phonebook entry password (&quot;$PASSWORD&quot;).</p>
<dt><code>Alt-N Configuration</code></p>
<dd> This brings the <code>qodemrc</code> options file up in an editor.</p>
<dt><code>Alt-O Modem Config</code></p>
<dd> This brings up the modem configuration dialog.</p>
<dt><code>Alt-R OS Shell</code></p>
<dd> This spawns a system shell.</p>
<dt><code>Alt-V View File</code></p>
<dd> This brings up a prompt to view a file in an editor.</p>
<dt><code>Alt-W List Directory</code></p>
<dd> This brings up a directory listing.</p>
<dt><code>Alt-0 Session Log</code></p>
<dd> This toggles the session log on or off.</p>
<dt><code>Alt-1 XON/XOFF Flow Ctrl</code></p>
<dd> When connected via modem or serial port, this toggles XON/XOFF on or off.</p>
<dt><code>Alt-2 Backspace/Del Mode</code></p>
<dd> This selects whether the backspace key on the keyboard sends an ASCII backspace (^H) or an ASCII DEL (127) character. Ctrl-H can always be used to send true backspace; Ctrl-? can be used to send true DEL. Note that VT220 emulation always sends DEL when the backspace key is pressed.</p>
<dt><code>Alt-3 Line Wrap</code></p>
<dd> This toggles line wrap mode on or off. When line wrap mode is enabled, if a character is received when the cursor is at the right margin it will wrap to the first column of the next line.</p>
<dt><code>Alt-4 Display NULL</code></p>
<dd> This selects whether ASCII NUL (0) will be displayed as a blank/space or stripped.</p>
<dt><code>Alt-6 Batch Entry Window</code></p>
<dd> This brings up the list of upload files used by Ymodem, Zmodem, and Kermit uploads.</p>
<dt><code>Alt-7 Status Line Info</code></p>
<dd> This selects between two formats for the status line.</p>
<dt><code>Alt-8 Hi-Bit Strip</code></p>
<dd> This selects whether or not to clear the 8th bit of all incoming bytes. Note that high-bit stripping occurs before both emulation processing and UTF-8 decoding.</p>
<dt><code>Alt-9 Serial Port</code></p>
<dd> This opens or closes the serial port. If already connected to a non-serial/modem remote host, this does nothing.</p>
<dt><code>Alt-B Beeps &amp; Bells</code></p>
<dd> This toggles beep support on or off. When beep support is on, beeps from the remote host will be played by qodem. In LINUX emulation, qodem supports setting the tone and duration of the beep as specified in <code><a href="/docs/linux/man/4-console-codes/">console-codes</a></code>(4).</p>
<dt><code>Alt-E Half/Full Duplex</code></p>
<dd> This toggles between half and full duplex.</p>
<dt><code>Alt-I Qodem Information</code></p>
<dd> This displays the qodem splash screen which includes the version and build date.</p>
<dt><code>Alt-U Scrollback Record</code></p>
<dd> This selects whether or not lines that scroll off the top of the screen will be saved to the scrollback buffer.</p>
<dt><code>Alt-= Doorway Mode</code></p>
<dd> This selects between three doorway modes: &quot;Doorway OFF&quot;, &quot;Doorway MIXED&quot; and &quot;Doorway FULL&quot;. When doorway mode is &quot;Doorway OFF&quot;, terminal mode responds to all of its command keys as described in this section. When doorway mode is &quot;Doorway FULL&quot;, all Alt- command keystrokes except <code>Alt-=</code> are passed to the remote side. When doorway mode is &quot;Doorway MIXED&quot;, terminal mode supports a few commands but passes the majority of Alt- command keystrokes to the remote side. The default commands supported in &quot;Doorway MIXED&quot; mode are:<br />
&nbsp;<wbr>&nbsp;<wbr>Alt-D Phonebook<br />
&nbsp;<wbr>&nbsp;<wbr>Alt-P Capture<br />
&nbsp;<wbr>&nbsp;<wbr>Alt-T Screen Dump<br />
&nbsp;<wbr>&nbsp;<wbr>Alt-Y COM Parameters<br />
&nbsp;<wbr>&nbsp;<wbr>Alt-Z Menu<br />
&nbsp;<wbr>&nbsp;<wbr>Alt-/&nbsp;<wbr>Scrollback<br />
&nbsp;<wbr>&nbsp;<wbr>Alt-PgUp or Ctrl-PgUp Upload Files<br />
&nbsp;<wbr>&nbsp;<wbr>Alt-PgDn or Ctrl-PgDn Download Files</p>
<dt><code>Alt&#8211; Status Lines</code></p>
<dd> This toggles the status line on or off.</p>
<dt><code>Alt-+ CR/CRLF Mode</code></p>
<dd> This toggles whether or not received carriage returns imply line feed or not.</p>
<dt><code>Alt-, ANSI Music</code></p>
<dd> This toggles ANSI music support on or off. </p>
</dl>
<h2>UNICODE SUPPORT</h2>
<p> Qodem supports Unicode (UTF-8 encoding only) in the following functions only: keyboard macros; phonebook entries (NAME, USERNAME, and PASSWORD); modem device name. </p>
<p> UTF-8 is NOT supported in filenames, modem strings, and remote addresses. </p>
<h2>SCRIPT SUPPORT</h2>
<p> Qodem does not have its own scripting language. Instead, any program that reads and writes to the standard input and output can be run as a Qodem script: </p>
<p>&nbsp;<wbr>*&nbsp;<wbr>Characters sent from the remote connection are visible to the<br />
script in its standard input. </p>
<p>&nbsp;<wbr>*&nbsp;<wbr>Characters the script emits to its standard output are passed on<br />
the remote connection. </p>
<p>&nbsp;<wbr>*&nbsp;<wbr>Messages to the standard error are reported to the user and also<br />
recorded in the session log. </p>
<p> Since scripts are communicating with the remote system and not Qodem itself, they are unable to script Qodem&#8217;s behavior, e.g. change the terminal emulation, hangup and dial another phonebook entry, download a file, etc. However, they can be written in any language, and they can be tested outside Qodem. </p>
<p> Scripts replace the user, and as such have similar constraints: </p>
<p>&nbsp;<wbr>&nbsp;<wbr>*&nbsp;<wbr>Script standard input, output, and error must all be in UTF-8 encoding. </p>
<p>&nbsp;<wbr>&nbsp;<wbr>*&nbsp;<wbr>Scripts should send carriage return&nbsp;<wbr>(0x0D, or&nbsp;<wbr>)&nbsp;<wbr>instead of new<br />
&nbsp;<wbr>line&nbsp;<wbr>(0x0A, or&nbsp;<wbr>
)&nbsp;<wbr>to the remote side &#8211; the same as if a user<br />
&nbsp;<wbr>pressed the Enter key.&nbsp;<wbr>&nbsp;<wbr>They should expect to see either bare<br />
&nbsp;<wbr>carriage return&nbsp;<wbr>(0x0D, or&nbsp;<wbr>)&nbsp;<wbr>or carriage return followed by<br />
&nbsp;<wbr>newline&nbsp;<wbr>(0x0D 0x0A, or&nbsp;<wbr>
)&nbsp;<wbr>from the remote side. </p>
<p>&nbsp;<wbr>&nbsp;<wbr>*&nbsp;<wbr>Input and output translate byte translation&nbsp;<wbr>(the Alt-A Translate Tables)&nbsp;<wbr>are honored for scripts. </p>
<p>&nbsp;<wbr>&nbsp;<wbr>*&nbsp;<wbr>While a script is running:<br />
&nbsp;<wbr>&nbsp;<wbr>&#8211; Zmodem and Kermit autostart are disabled.<br />
&nbsp;<wbr>&nbsp;<wbr>&#8211; Keyboard function key macros are disabled.<br />
&nbsp;<wbr>&nbsp;<wbr>&#8211; Qodem functions accessed through the Alt-character<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>combinations and PgUp/PgDn are unavailable.<br />
&nbsp;<wbr>&nbsp;<wbr>&#8211; Pressing Alt-P will pause the script. </p>
<p>&nbsp;<wbr>&nbsp;<wbr>*&nbsp;<wbr>While a script is paused:<br />
&nbsp;<wbr>&nbsp;<wbr>&#8211; The script will receive nothing on its standard input.<br />
&nbsp;<wbr>&nbsp;<wbr>&#8211; Anything in the script&#8217;s standard output will be held until<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>the script is resumed.<br />
&nbsp;<wbr>&nbsp;<wbr>&#8211; The script process will not be signaled;&nbsp;<wbr>it may continue<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>running in its own process.<br />
&nbsp;<wbr>&nbsp;<wbr>&#8211; The only Alt-character function recognized is AltP to<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>resume the script.&nbsp;<wbr>&nbsp;<wbr>All other Alt- keys will be ignored.<br />
&nbsp;<wbr>&nbsp;<wbr>&#8211; Keys pressed will be sent directly to the remote system.<br />
&nbsp;<wbr>&nbsp;<wbr>&#8211; Keyboard function key macros will work. </p>
<p> Scripts are launched in two ways: </p>
<p>&nbsp;<wbr>&nbsp;<wbr>*&nbsp;<wbr>In TERMINAL mode, press Alt-F and enter the script filename.&nbsp;<wbr>&nbsp;<wbr>The<br />
&nbsp;<wbr>script will start immediately. </p>
<p>&nbsp;<wbr>&nbsp;<wbr>*&nbsp;<wbr>In the phonebook, add a script filename to a phonebook entry.&nbsp;<wbr>&nbsp;<wbr>The<br />
&nbsp;<wbr>script will start once that entry is connected. </p>
<p> Script command-line arguments can be passed directly in both the Alt-F script dialog and the phonebook linked script field. For example, pressing Alt-F and entering &quot;my_script.pl arg1&quot; will launch my_script.pl and with its first command-line argument ($ARGV[0] in Perl) set to &quot;arg1&quot;. </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>&#8211;enable-capture FILENAME</code></p>
<dd> Capture the entire session and save to FILENAME.</p>
<dt><code>&#8211;connect HOST</code></p>
<dd> Immediately open a connection to HOST. The default connection method is &quot;ssh&quot; unless specified with the <code>&#8211;connect-method</code> option.</p>
<dt><code>&#8211;connect-method METHOD</code></p>
<dd> Use METHOD to connect for the <code>&#8211;connect</code> and <code>&#8211;dial</code> options. Valid values are &quot;ssh&quot;, &quot;rlogin&quot;, &quot;rsh&quot;, &quot;telnet&quot;, and &quot;shell&quot;.</p>
<dt><code>&#8211;username USERNAME</code></p>
<dd> Use USERNAME when connecting with the <code>&#8211;connect</code> option. This value is passed on the command line to <code>ssh</code>, <code>rsh</code>, and <code>rlogin</code>.</p>
<dt><code>args&#8230;</code></p>
<dd> Spawn a local shell and pass args to it.</p>
<dt><code>&#8211;help</code>, <code>-h</code>, <code>-?</code></p>
<dd> Display usage screen. </p>
</dl>
<h2>ENVIRONMENT VARIABLES</h2>
<dl>
<dt>Qodem makes use of the following variables:</p>
<dd>
<dt><code>HOME</code></p>
<dd> The user&#8217;s home directory. Qodem creates two directories: <code>$HOME/.qodem</code> for qodem&#8217;s internal files (phonebook, keyboard macro files, translate tables, etc.) and <code>$HOME/qodem</code> for uploaded and downloaded files, session log, capture, etc.</p>
<dt><code>EDITOR</code></p>
<dd> If present, this will be used when spawning external editors (log view, edit configuration, view file, edit phonebook note). If not present, by default (editable in the options file) use <code>vi</code>.</p>
<dt><code>ESCDELAY</code></p>
<dd> This is a timeout value in milliseconds used by the ncurses <code>get_wch()</code> and <code>wget_wch()</code> functions to determine if a user pressed bare ESCAPE. On some systems pressing ESCAPE may require up to a full second before qodem can process it. For qodem backtick (`) can be used instead of ESCAPE. </p>
</dl>
<h2>FILES</h2>
<dl>
<dt><code>$HOME/.qodem/qodemrc</code></p>
<dd> Qodem options/configuration file. Inline comments describe the options. </p>
</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-xqodem/">xqodem</a>(1),</code> <a href="/docs/linux/man/1-mm/">mm</a>(1),<code> <a href="/docs/linux/man/1-kermit/">kermit</a>(1),</code> <a href="/docs/linux/man/1-gkermit/">gkermit</a>(1),<code> <a href="/docs/linux/man/1-minicom/">minicom</a>(1),</code> <a href="/docs/linux/man/1-rlogin/">rlogin</a>(1),<code> <a href="/docs/linux/man/1-rsh/">rsh</a>(1),</code> <a href="/docs/linux/man/1-ssh/">ssh</a>(1),<code> <a href="/docs/linux/man/1-telnet/">telnet</a>(1),</code> <a href="/docs/linux/man/1-xterm/">xterm</a>(1),<code> <a href="/docs/linux/man/1-vttest/">vttest</a>(1),</code> <a href="/docs/linux/man/4-console-codes/">console-codes</a>(4) </p>
<h2>BUGS</h2>
<p> The screensaver might not load under all circumstances even after the timeout has passed. </p>
<h2>HOMEPAGE</h2>
<p> The qodem homepage is at &lt;<a rel="nofollow" href="http://qodem.sourceforge.net">http://qodem.sourceforge.net</a>&gt;. </p>
<h2>COPYRIGHT NOTICE</h2>
<p> Copyright &#169; 2010 Kevin Lamonte </p>
<p> This program is free software; you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation; either version 2 of the License, or (at your option) any later version. </p>
<h2>Index</h2>
