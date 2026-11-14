---
title: "sz(1)"
name: "sz"
section: "1"
letter: "s"
url: "/docs/linux/man/1-sz/"
description: "sx, sb, sz – XMODEM, YMODEM, ZMODEM file send"
---

<h2>NAME</h2>
<p> sx, sb, sz &#8211; XMODEM, YMODEM, ZMODEM file send</p>
<h2>SYNOPSIS</h2>
<p> sz [-<code>+8abdefkLlNnopqTtuvyY</code>] <i>file &#8230;</i><br />
 sb [-<code>adfkqtuv</code>] <i>file &#8230;</i><br />
 sx [-<code>akqtuv</code>] <i>file</i><br />
 sz [-<code>oqtv</code>] <code>-c COMMAND</code><br />
 sz [-<code>oqtv</code>] <code>-i COMMAND</code><br />
 sz -TT</p>
<h2>DESCRIPTION</h2>
<p> <code>Sz</code> uses the ZMODEM, YMODEM or XMODEM error correcting protocol to send one or more files over a dial-in serial port to a variety of programs running under PC-DOS, CP/M, Unix, VMS, and other operating systems. </p>
<p> While <i>rz</i> is smart enough to be called from <i><a href="/docs/linux/man/1-cu/">cu</a>(1),</i> very few versions of <i><a href="/docs/linux/man/1-cu/">cu</a>(1)</i> are smart enough to allow <i>sz</i> to work properly. Unix flavors of Professional-YAM are available for such dial-out application. </p>
<p> <code>Sz</code> sends one or more files with ZMODEM protocol. </p>
<p> ZMODEM greatly simplifies file transfers compared to XMODEM. In addition to a friendly user interface, ZMODEM provides Personal Computer and other users an efficient, accurate, and robust file transfer method. </p>
<p> ZMODEM provides complete <code>END-TO-END</code> data integrity between application programs. ZMODEM&#8217;s 32 bit CRC catches errors that sneak into even the most advanced networks. </p>
<p> Advanced file management features include AutoDownload (Automatic file Download initiated without user intervention), Display of individual and total file lengths and transmission time estimates, Crash Recovery, selective file transfers, and preservation of exact file date and length. </p>
<p> Output from another program may be piped to <code>sz</code> for transmission by denoting standard input with &quot;-&quot;: <center> ls -l | sz &#8211;<br />
 </center> The program output is transmitted with the filename sPID.sz where PID is the process ID of the <code>sz</code> program. If the environment variable <code>ONAME</code> is set, that is used instead. In this case, the Unix command: <center> ls -l | ONAME=con sz -ay &#8211;<br />
 </center> will send a &quot;file&quot; to the PC-DOS console display. The <code>-y</code> option instructs the receiver to open the file for writing unconditionally. The <code>-a</code> option causes the receiver to convert Unix newlines to PC-DOS carriage returns and linefeeds. </p>
<p> <code>Sb</code> batch sends one or more files with YMODEM or ZMODEM protocol. The initial ZMODEM initialization is not sent. When requested by the receiver, <code>sb</code> supports <code>YMODEM-g</code> with &quot;cbreak&quot; tty mode, XON/XOFF flow control, and interrupt character set to CAN (^X). <code>YMODEM-g</code> (Professional-YAM <code>g</code> option) increases throughput over error free channels (direct connection, X.PC, etc.) by not acknowledging each transmitted sector. </p>
<p> On <font SIZE="-1">Unix</font> systems, additional information about the file is transmitted. If the receiving program uses this information, the transmitted file length controls the exact number of bytes written to the output dataset, and the modify time and file mode are set accordingly. </p>
<p> <code>Sx</code> sends a single <i>file</i> with <code>XMODEM</code> or <code>XMODEM-1k</code> protocol (sometimes incorrectly called &quot;ymodem&quot;). The user must supply the file name to both sending and receiving programs. </p>
<p> If <code>sz</code> is invoked with $SHELL set and if that variable contains the string <i>rsh</i> , <i>rbash</i> or <i>rksh</i> (restricted shell), <code>sz</code> operates in restricted mode. Restricted mode restricts pathnames to the current directory and PUBDIR (usually /usr/spool/uucppublic) and/or subdirectories thereof. </p>
<p> The fourth form sends a single COMMAND to a ZMODEM receiver for execution. <code>Sz</code> exits with the COMMAND return value. If COMMAND includes spaces or characters special to the shell, it must be quoted. </p>
<p> The fifth form sends a single COMMAND to a ZMODEM receiver for execution. <code>Sz</code> exits as soon as the receiver has correctly received the command, before it is executed. </p>
<p> The sixth form (sz -TT) attempts to output all 256 code combinations to the terminal. In you are having difficulty sending files, this command lets you see which character codes are being eaten by the operating system. </p>
<p> If <code>sz</code> is invoked with stdout and stderr to different datasets, Verbose is set to 2, causing frame by frame progress reports to stderr. This may be disabled with the <code>q</code> option. </p>
<p> The meanings of the available options are: </p>
<dl>
<dt><code>-+, &#8211;append</code></p>
<dd> Instruct the receiver to append transmitted data to an existing file (ZMODEM only).</p>
<dt><code>-2, &#8211;twostop</code></p>
<dd> use two stop bits (if possible). Do not use this unless you know what you are doing.</p>
<dt><code>-8, &#8211;try-8k</code></p>
<dd> Try to go up to 8KB blocksize. This is incompatible with standard zmodem, but a common extension in the bbs world. (ZMODEM only).</p>
<dt><code>&#8211;start-8k</code></p>
<dd> Start with 8KB blocksize. Like &#8211;try-8k.</p>
<dt><code>-a, &#8211;ascii</code></p>
<dd> Convert NL characters in the transmitted file to CR/LF. This is done by the sender for XMODEM and YMODEM, by the receiver for ZMODEM.</p>
<dt><code>-b, &#8211;binary</code></p>
<dd> (ZMODEM) Binary override: transfer file without any translation.</p>
<dt><code>-B NUMBER, &#8211;bufsize NUMBER</code></p>
<dd> Use a readbuffer of <code>NUMBER</code> bytes. Default is 16384, which should be enough for most situations. If you have a slow machine or a bad disk interface or suffer from other hardware problems you might want to increase the buffersize. <code>-1</code> or <code>auto</code> use a buffer large enough to buffer the whole file. Be careful with this option &#8211; things normally get worse, not better, if the machine starts to swap. </p>
<p> Using this option turns of memory mapping of the input file. This increases memory and CPU usage.</p>
<dt><code>-c COMMAND, &#8211;command COMMAND</code></p>
<dd> Send COMMAND to the receiver for execution, return with COMMAND&#8217;s exit status.</p>
<dt><code>-C N, &#8211;command-tries N</code></p>
<dd> Retry to send command N times (default: 11).</p>
<dt><code>-d, &#8211;dot-to-slash</code></p>
<dd> Change all instances of &quot;.&quot; to &quot;/&quot; in the transmitted pathname. Thus, C.omenB0000 (which is unacceptable to MSDOS or CP/M) is transmitted as C/omenB0000. If the resultant filename has more than 8 characters in the stem, a &quot;.&quot; is inserted to allow a total of eleven. </p>
<p> This option enables the <code>&#8211;full-path</code> option.</p>
<dt><code>&#8211;delay-startup N</code></p>
<dd> Wait <code>N</code> seconds before doing anything.</p>
<dt><code>-e, &#8211;escape</code></p>
<dd> Escape all control characters; normally XON, XOFF, DLE, CR-@-CR, and Ctrl-X are escaped.</p>
<dt>
<dd> Force the sender to rename the new file if a file with the same name already exists.</p>
<dt><code>-f, &#8211;full-path</code></p>
<dd> Send Full pathname. Normally directory prefixes are stripped from the transmitted filename. </p>
<p> This is also turned on with to <code>&#8211;dot-to-slash</code> option.</p>
<dt><code>-h, &#8211;help</code></p>
<dd> give help.</p>
<dt><code>-i COMMAND, &#8211;immediate-command COMMAND</code></p>
<dd> Send COMMAND to the receiver for execution, return immediately upon the receiving program&#8217;s successful reception of the command.</p>
<dt><code>-k, &#8211;1k</code></p>
<dd> (XMODEM/YMODEM) Send files using 1024 byte blocks rather than the default 128 byte blocks. 1024 byte packets speed file transfers at high bit rates. (ZMODEM streams the data for the best possible throughput.)</p>
<dt><code>-L N, &#8211;packetlen N</code></p>
<dd> Use ZMODEM sub-packets of length N. A larger N (32 &lt;= N &lt;= 1024) gives slightly higher throughput, a smaller N speeds error recovery. The default is 128 below 300 baud, 256 above 300 baud, or 1024 above 2400 baud.</p>
<dt><code>-m N, &#8211;min-bps N</code></p>
<dd> Stop transmission if BPS-Rate (Bytes Per Second) falls below N for a certain time (see &#8211;min-bps-time option).</p>
<dt><code>-M N, &#8211;min-bps-time</code></p>
<dd> Used together with &#8211;min-bps. Default is 120 (seconds).</p>
<dt><code>-l N, &#8211;framelen N</code></p>
<dd> Wait for the receiver to acknowledge correct data every <code>N</code> (32 &lt;= N &lt;= 1024) characters. This may be used to avoid network overrun when XOFF flow control is lacking.</p>
<dt><code>-n, &#8211;newer</code></p>
<dd> (ZMODEM) Send each file if destination file does not exist. Overwrite destination file if source file is newer than the destination file.</p>
<dt><code>-N, &#8211;newer-or-longer</code></p>
<dd> (ZMODEM) Send each file if destination file does not exist. Overwrite destination file if source file is newer or longer than the destination file.</p>
<dt><code>-o, &#8211;16-bit-crc</code></p>
<dd> (ZMODEM) Disable automatic selection of 32 bit CRC.</p>
<dt><code>-O, &#8211;disable-timeouts</code></p>
<dd> Disable read timeout handling. This makes lsz hang if the other side doesn&#8217;t send anything, but increases performance (not much) and decreases system load (reduces number of system calls by about 50 percent). </p>
<p> Use this option with care.</p>
<dt><code>-p, &#8211;protect</code></p>
<dd> (ZMODEM) Protect existing destination files by skipping transfer if the destination file exists.</p>
<dt><code>-q, &#8211;quiet</code></p>
<dd> Quiet suppresses verbosity.</p>
<dt><code>-R, &#8211;restricted</code></p>
<dd> Restricted mode: restricts pathnames to the current directory and PUBDIR (usually /usr/spool/uucppublic) and/or subdirectories thereof.</p>
<dt><code>-r, &#8211;resume</code></p>
<dd> (ZMODEM) Resume interrupted file transfer. If the source file is longer than the destination file, the transfer commences at the offset in the source file that equals the length of the destination file.</p>
<dt><code>-s HH:MM, &#8211;stop-at HH:MM</code></p>
<dd> Stop transmission at <code>HH </code> hours, <code>MM</code> minutes. Another variant, using <code>+N </code> instead of <code>HH:MM,</code> stops transmission in <code>N</code> seconds.</p>
<dt><code>-S, &#8211;timesync</code></p>
<dd> enable timesync protocol support. See timesync.doc for further information. </p>
<p> This option is incompatible with standard zmodem. Use it with care.</p>
<dt><code>&#8211;syslog[=off]</code></p>
<dd> turn syslogging on or off. the default is set at configure time. This option is ignored if no syslog support is compiled in.</p>
<dt><code>-t TIM, &#8211;timeout TIM</code></p>
<dd> Change timeout to <i>TIM</i> tenths of seconds.</p>
<dt><code>-T, &#8211;turbo</code></p>
<dd> Do not escape certain characters (^P, ^P|0x80, telenet escape sequence [CR + @]). This improves performance by about 1 percent and shouldn&#8217;t hurt in the normal case (but be careful &#8211; ^P might be useful if connected through a terminal server).</p>
<dt><code>&#8211;tcp</code></p>
<dd> Try to initiate a TCP/IP connection. lsz will ask the receiving zmodem to open a TCP/IP connection. All handshaking (which address / port to use) will be done by the zmodem programs. </p>
<p> You will normally not want to use this option as lrzsz is the only zmodem which understands what to do (private extension). You might want to use this option if the two programs are connected (stdin/out) over a slow or bad (not 8bit clean) network connection. </p>
<p> Use of this option imposes a security risk, somebody else could connect to the port in between. See <code>SECURITY</code> for details.</p>
<dt><code>&#8211;tcp-client ADDRESS:PORT</code></p>
<dd> Act as a tcp/ip client: Connect to the given port. </p>
<p> See <code>&#8211;tcp-server</code> for more information. </p>
<dt><code>&#8211;tcp-server</code></p>
<dd> Act as a server: Open a socket, print out what to do, wait for connection. </p>
<p> You will normally not want to use this option as lrzsz is the only zmodem which understands what to do (private extension). You might want to use this if you have to use zmodem (for which reason whatever), and cannot use the <code>&#8211;tcp</code> option of <i>lsz</i> (perhaps because your telnet doesn&#8217;t allow to spawn a local program with stdin/stdout connected to the remote side). </p>
<p> If you use this option you have to start <i>lsz</i> with the <code>&#8211;tcp-client ADDRESS:PORT</code> option. <i>lrz will print the address and port on startup.</i> </p>
<p> Use of this option imposes a security risk, somebody else could connect to the port in between. See <code>SECURITY</code> for details. </p>
<dt><code>-u</code></p>
<dd> Unlink the file after successful transmission.</p>
<dt><code>-U, &#8211;unrestrict</code></p>
<dd> Turn off restricted mode (this is not possible if running under a restricted shell).</p>
<dt><code>-w N, &#8211;windowsize N</code></p>
<dd> Limit the transmit window size to N bytes (ZMODEM).</p>
<dt><code>-v, &#8211;verbose</code></p>
<dd> Verbose output to stderr. More v&#8217;s generate more output.</p>
<dt><code>-X, &#8211;xmodem</code></p>
<dd> use XMODEM protocol.</p>
<dt><code>-y, &#8211;overwrite</code></p>
<dd> Instruct a ZMODEM receiving program to overwrite any existing file with the same name.</p>
<dt><code>-Y, &#8211;overwrite-or-skip</code></p>
<dd> Instruct a ZMODEM receiving program to overwrite any existing file with the same name, and to skip any source files that do have a file with the same pathname on the destination system.</p>
<dt><code>&#8211;ymodem</code></p>
<dd> use ZMODEM protocol.</p>
<dt><code>-Z, &#8211;zmodem</code></p>
<dd> use ZMODEM protocol.</dl>
<h2>SECURITY</h2>
<p> Restricted mode restricts pathnames to the current directory and PUBDIR (usually /var/spool/uucppublic) and/or subdirectories thereof, and disables remote command execution. </p>
<p> Restricted mode is entered if the <code>R</code> option is given or if lsz detects that it runs under a restricted shell or if the environment variable ZMODEM_RESTRICTED is found. </p>
<p> Restricted mode can be turned of with the <code>U</code> option if not running under a restricted shell. </p>
<dl>
<dt>Use of the</p>
<dd> <code>&#8211;tcp-client</code> or <code>&#8211;tcp-server</code> options imposes a security risk, as somebody else could connect to the port before you do it, and grab your data. If there&#8217;s strong demand for a more secure mode i might introduce some sort of password challenge. </p>
</dl>
<h2>ENVIRONMENT</h2>
<dl>
<dt><code>ZNULLS</code></p>
<dd> may be used to specify the number of nulls to send before a ZDATA frame.</p>
<dt><code>SHELL</code></p>
<dd> lsz recognizes a restricted shell if this variable includes <i>rsh</i> or <i>rksh</i></p>
<dt><code>ZMODEM_RESTRICTED</code></p>
<dd> lrz enters restricted mode if the variable is set.</p>
<dt><code>TMPDIR</code></p>
<dd> If this environment variable is set its content is used as the directory to place in the answer file to a <code>timesync </code> request. <code>TMP</code> Used instead of TMPDIR if TMPDIR is not set. If neither TMPDIR nor TMP is set /tmp will be used.</dl>
<h2>EXAMPLES</h2>
<p> <code>ZMODEM File Transfer</code> (Unix to DSZ/ZCOMM/Professional-YAM)<br />
 <code>% sz -a *.c</code><br />
 This single command transfers all .c files in the current Unix directory with conversion (<code>-a</code>) to end of line conventions appropriate to the receiving environment. With ZMODEM AutoDownload enabled, Professional-YAM and ZCOMM will automatically receive the files after performing a security check. </p>
<p> <code>% sz -Yan *.c *.h</code><br />
 Send only the .c and .h files that exist on both systems, and are newer on the sending system than the corresponding version on the receiving system, converting Unix to DOS text format.<br />
 <code>$ sz -\Yan file1.c file2.c file3.c foo.h baz.h</code> (for VMS) </p>
<p> <code>ZMODEM Command Download</code> (Unix to Professional-YAM) </p>
<p>&nbsp;<wbr>cpszall:all<br />
&nbsp;<wbr>sz -c&nbsp;<wbr>&quot;c:;cd&nbsp;<wbr>/yam/dist&quot;<br />
&nbsp;<wbr>sz -ya&nbsp;<wbr>$(YD)/*.me<br />
&nbsp;<wbr>sz -yqb y*.exe<br />
&nbsp;<wbr>sz -c&nbsp;<wbr>&quot;cd&nbsp;<wbr>/yam&quot;<br />
&nbsp;<wbr>sz -i&nbsp;<wbr>&quot;!insms&quot;<br />
 This Makefile fragment uses <code>sz</code> to issue commands to Professional-YAM to change current disk and directory. Next, <code>sz</code> transfers the <i>.me</i> files from the $YD directory, commanding the receiver to overwrite the old files and to convert from Unix end of line conventions to PC-DOS conventions. The third line transfers some <i>.exe</i> files. The fourth and fifth lines command Pro-YAM to change directory and execute a PC-DOS batch file <i>insms .</i> Since the batch file takes considerable time, the <code>-i</code> form is used to allow <code>sz</code> to exit immediately. </p>
<p> <code>XMODEM File Transfer</code> (Unix to Crosstalk)<br />
 % <code>sx -a foo.c</code><br />
 <code>ESC</code><br />
 <code>rx foo.c</code><br />
 The above three commands transfer a single file from Unix to a PC and Crosstalk with <i>sz</i> translating Unix newlines to DOS CR/LF. This combination is much slower and far less reliable than ZMODEM.</p>
<h2>ERROR MESSAGES</h2>
<p> &quot;Caught signal 99&quot; indicates the program was not properly compiled, refer to &quot;bibi(99)&quot; in rbsb.c for details.</p>
<h2>SEE ALSO</h2>
<p> rz(omen), ZMODEM.DOC, YMODEM.DOC, Professional-YAM, crc(omen), sq(omen), todos(omen), tocpm(omen), tomac(omen), yam(omen) </p>
<p> Compile time options required for various operating systems are described in the source file.</p>
<h2>VMS VERSION</h2>
<p> The VMS version does not support wild cards. Because of VMS DCL, upper case option letters muse be represented by \ proceeding the letter. </p>
<p> The current VMS version does not support XMODEM, XMODEM-1k, or YMODEM. </p>
<p> VMS C Standard I/O and RMS may interact to modify the file contents.</p>
<h2>FILES</h2>
<p> 32 bit CRC code courtesy Gary S. Brown. </p>
<p> sz.c, crctab.c, rbsb.c, zm.c, zmodem.h Unix source files </p>
<p> sz.c, crctab.c, vrzsz.c, zm.c, zmodem.h, vmodem.h, vvmodem.c, VMS source files. </p>
<p> /tmp/szlog stores debugging output (sz -vv) (szlog on VMS).</p>
<h2>TESTING FEATURE</h2>
<p> The command &quot;sz -T file&quot; exercises the <code>Attn</code> sequence error recovery by commanding errors with unterminated packets. The receiving program should complain five times about binary data packets being too long. Each time <code>sz</code> is interrupted, it should send a ZDATA header followed by another defective packet. If the receiver does not detect five long data packets, the <code>Attn</code> sequence is not interrupting the sender, and the <code>Myattn</code> string in <code>sz.c</code> must be modified. </p>
<p> After 5 packets, <code>sz</code> stops the &quot;transfer&quot; and prints the total number of characters &quot;sent&quot; (Tcount). The difference between Tcount and 5120 represents the number of characters stored in various buffers when the Attn sequence is generated.</p>
<h2>BUGS</h2>
<p> Calling <i>sz</i> from most versions of <a href="/docs/linux/man/1-cu/">cu</a>(1) doesn&#8217;t work because cu&#8217;s receive process fights <i>sz</i> for characters from the modem. </p>
<p> On at least one BSD system, sz would hang or exit when it got within a few kilobytes of the end of file. Using the &quot;-w 8192&quot; flag fixed the problem. The real cause is unknown, perhaps a bug in the kernel TTY output routines. </p>
<p> Programs that do not properly implement the specified file transfer protocol may cause <i>sz</i> to &quot;hang&quot; the port for a minute or two. This problem is corrected by using ZCOMM, Pro-YAM, or other program with a correct implementation of the specified protocol. </p>
<p> Many programs claiming to support YMODEM only support XMODEM with 1k blocks, and they often don&#8217;t get that quite right. </p>
<p> XMODEM transfers add up to 127 garbage bytes per file. XMODEM-1k and YMODEM-1k transfers use 128 byte blocks to avoid extra padding. </p>
<p> YMODEM programs use the file length transmitted at the beginning of the transfer to prune the file to the correct length; this may cause problems with source files that grow during the course of the transfer. This problem does not pertain to ZMODEM transfers, which preserve the exact file length unconditionally. </p>
<p> Most ZMODEM options are merely passed to the receiving program; some do not implement all these options. </p>
<p> Circular buffering and a ZMODEM sliding window should be used when input is from pipes instead of acknowledging frames each 1024 bytes. If no files can be opened, <code>sz</code> sends a ZMODEM command to echo a suitable complaint; perhaps it should check for the presence of at least one accessible file before getting hot and bothered. The test mode leaves a zero length file on the receiving system. </p>
<p> A few high speed modems have a firmware bug that drops characters when the direction of high speed transmission is reversed. The environment variable ZNULLS may be used to specify the number of nulls to send before a ZDATA frame. Values of 101 for a 4.77 MHz PC and 124 for an AT are typical. </p>
<h2>Index</h2>
