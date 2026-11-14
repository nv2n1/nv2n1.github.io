---
title: "kermit(1)"
name: "kermit"
section: "1"
letter: "k"
url: "/docs/linux/man/1-kermit/"
description: "kermit – C-Kermit 9.0: transport- and platform-independent interactive and scriptable communications software."
---

<h2 class="name">NAME</h2>
<p> kermit &#8211; <code>C-Kermit 9.0:</code> transport- and platform-independent interactive and scriptable communications software.</p>
<dl>
<dt>
<dd>
<p> This document is intended to give the beginner sufficient information to make basic (if not advanced) use of C-Kermit 9.0. Although it might be rather long for a Unix manual page, it&#8217;s still far shorter than the C-Kermit manual, which should be consulted for advanced topics such as customization, character-sets, scripting, etc. We also attempt to provide a clear structural overview of C-Kermit&#8217;s many capabilities, functional areas, states, and modes and their interrelation, that should be helpful to beginners and veterans alike, as well as to those upgrading to version 9.0 from earlier releases.</dl>
<p> This document is also available as a Web page at:</p>
<dl>
<dt>
<dd>
<p><a rel="nofollow" href="http://www.columbia.edu/kermit/ckututor.html">http://www.columbia.edu/kermit/ckututor.html</a></dl>
<h2>DESCRIPTION</h2>
<p> C-Kermit is an all-purpose communications software package from the Kermit Project at Columbia University that: </p>
<pre><code>
&amp;bull;
Is portable to many platforms, Unix and non - Unix alike.

                                                  &amp;bull;
Can make both serial and network connections.

    &amp;bull;
Can conduct interactive terminal sessions over its connection.

    &amp;bull;
Can transfer text or binary files over the same connection.

                         &amp;bull;
Can convert character sets in the terminal session.

    &amp;bull;
Can convert character sets during text - file file transfer.

                                             &amp;bull;
Is customizable in every aspect of its operation.
</code></pre>
<p> C-Kermit is a modem program, a Telnet client, an Rlogin client, an FTP client, an HTTP client, and on selected platforms, also an X.25 client. It can make its own secure Internet connections using IETF-approved security methods including Kerberos IV, Kerberos V, SSL/TLS, and SRP and it can also make SSH connections through your external SSH client application. It can be the far-end file-transfer or client/server partner of your desktop Kermit client. It can also accept incoming dialed and network connections. It can even be installed as an Internet service on its own standard TCP socket, 1649 [RFC2839, RFC2840]. </p>
<p> And perhaps most important, everything you can do &quot;by hand&quot; (interactively) with C-Kermit, can be &quot;scripted&quot; (automated) using its built-in cross-platform transport-independent script programming language, which happens to be identical to its interactive command language. </p>
<p> This manual page offers an overview of C-Kermit 9.0 for Unix (&quot;Unix&quot; is an operating system family that includes AIX, DG/UX, FreeBSD, HP-UX, IRIX, Linux, Mac OS X, NetBSD, OpenBSD, Open Server, Open Unix, QNX, Solaris, SunOS, System V R3, System V R4, Tru64 Unix, Unixware, Xenix, and many others). For thorough coverage, please consult the published C-Kermit manual and supplements (see DOCUMENTATION below). For further information about C-Kermit, Kermit software for other platforms, and Kermit manuals, visit the Kermit Project website: </p>
<p>&nbsp;<wbr>&nbsp;<wbr><a rel="nofollow" href="http://www.columbia.edu/kermit/">http://www.columbia.edu/kermit/</a> </p>
<p> This is a longer-than-average manual page, and yet it barely scratches the surface. Don&#8217;t be daunted. C-Kermit is a large and complex package, evolving over decades of practice and experience, but that doesn&#8217;t mean it&#8217;s hard to learn or use. Its most commonly used functions are explained here with pointers to additional information elsewhere.</p>
<h2>SYNOPSIS</h2>
<p> <code>kermit [</code> <i>filename</i> <code>] [</code> <i>options</i> <code>] [ {=,&#8211;,+}</code> <i>text</i> <code>] ]</code> </p>
<p> or: </p>
<p> <code>kermit </code> <i>URL</i> </p>
<p> If the first command-line argument is the name of a file, interactive-mode commands are executed from the file. The &#8216;=&#8217; (or &quot;&#8211;&quot;) argument tells Kermit not to parse the remainder of the command line, but to make the words following &#8216;=&#8217; available as \%1, \%2, &#8230; \%9. The &quot;+&quot; argument is like &quot;=&quot; but for use in &quot;kerbang scripts&quot; (explained below). A second command-line format allows the one and only argument to be a Telnet, FTP, HTTP, or IKSD URL. </p>
<p> Order of execution:</p>
<dl>
<dt>
&nbsp;<wbr>1.</p>
<dd> The command file (if any).</p>
<dt>
<pre>
<dd> 2.
The initialization file, if any, unless suppressed with -Y.
</pre>
<dt>
&nbsp;<wbr>3.</p>
<dd> The customization file (if it is executed by the initialization file).</p>
<dt>
&nbsp;<wbr>4.</p>
<dd> The command-line URL (if any, and if so, execution stops here).</p>
<dt>
&nbsp;<wbr>5.</p>
<dd> Command-line options (if any).</p>
<dt>
&nbsp;<wbr>6.</p>
<dd> Interactive commands.</dl>
<p> Some command-line options can cause actions (such as -s to send a file); others just set parameters. If any action options are included on the command line, Kermit exits when finished unless also given the -S (&quot;stay&quot;) option. If no action options are given, no initialization or command files contained an EXIT or QUIT command, and no fatal errors occurred, Kermit issues its prompt and waits for you to type commands.</p>
<dl>
<dt>
<dd> Bear in mind that C-Kermit can be built with selected features disabled, and also that certain features are not available on all platforms. For example, C-Kermit can&#8217;t be built with TCP/IP support on a platform that does not have TCP/IP header files and libraries (and even if Kermit does include TCP/IP support, it can&#8217;t be used to make TCP/IP connections on a computer that does not have a TCP/IP stack installed). If your version of C-Kermit lacks a feature mentioned here, use its SHOW FEATURES command to see what might have been excluded.</dl>
<p> C-Kermit has three kinds of commands: regular single-letter command-line options, extended-format command-line options, and interactive commands. </p>
<p> Like most Unix commands, C-Kermit can be be given options on the command line. But C-Kermit also can be used interactively by giving it commands composed of words, which are more intuitive than cryptic command-line options, and more flexible too. In other words, you don&#8217;t have to use C-Kermit&#8217;s command-line options, but they are available if you want to. (By the same token, you don&#8217;t have to use its interactive commands either &#8212; you can use either or both in any combination.) </p>
<p> C-Kermit is generally installed in the PATH as &quot;kermit&quot;, and therefore is invoked by typing the word &quot;kermit&quot; (lowercase) at the shell prompt, and then pressing the Return or Enter key. If you wish to include command-line options, put them after the word &quot;kermit&quot; but before pressing Return or Enter, separated by spaces, for example: </p>
<p>&nbsp;<wbr>&nbsp;<wbr>$&nbsp;<wbr>kermit -s ckermit.tar.gz </p>
<p> (&#8216;$&#8217; is the shell prompt; &quot;kermit -s ckermit.tar.gz&quot; is what you type, followed by Return or Enter.)</p>
<h2>OPTIONS</h2>
<p> Here is a list of C-Kermit&#8217;s single-letter command-line options, which start with a single dash (-), in ASCII (&quot;alphabetical&quot;) order. Alphabetic case is significant (-A is not the same as -a). Action options are tagged &quot;ACTION&quot;.</p>
<dl>
<dt>-0</p>
<dd> (digit zero) 100% transparent Connect state for &quot;in-the-middle&quot; operation: 8 bits, no parity, no escape character, everything passes through.</p>
<dt>-8</p>
<dd> (digit eight) Connection is 8-bit clean (this is the default in C-Kermit 8.0 and later). Equivalent to the EIGHTBIT command, which in turn is a shortcut for SET TERMINAL BYTESIZE 8, SET COMMAND BYTESIZE 8, SET PARITY NONE.</p>
<dt>-9 arg</p>
<dd> (digit nine) Make a connection to an FTP server. Equivalent to the FTP OPEN command. Argument: IP-address-or-hostname[:optional-TCP-port]. NOTE: C-Kermit also has a separate FTP command-line personality, with regular FTP-like command-line syntax. More about this below.</p>
<dt>-A</p>
<dd> Kermit is to be started as an Internet service (IKSD) (only from inetd.conf).</p>
<dt>-B</p>
<dd> Kermit is running in Batch or Background (no controlling terminal). To be used in case Kermit doesn&#8217;t automatically sense its background status. Equivalent to the SET BACKGROUND ON command.</p>
<dt>-C arg</p>
<dd> Interactive-mode Commands to be executed. Argument: Commands separated by commas, list in doublequotes.</p>
<dt>-D arg</p>
<dd> Delay before starting to send in Remote mode. Equivalent to the SET DELAY command. Argument: Number of seconds.</p>
<dt>-E</p>
<dd> Exit automatically when connection closes. Equivalent to SET EXIT ON-DISCONNECT ON.</p>
<dt>-F arg</p>
<dd> Use an open TCP connection. Argument: Numeric file descriptor of open TCP connection. Also see: -j, -J.</p>
<dt>-G arg</p>
<dd> (ACTION) Get file(s) from server, send contents to standard output, which normally would be piped to another process. Argument: Remote file specification, in quotes if it contains metacharacters. Also see: -g, -k.</p>
<dt>-H</p>
<dd> Suppress program startup Herald and greeting.</p>
<dt>-I</p>
<dd> Tell Kermit it has a reliable connection, to force streaming to be used where it normally would not be. Equivalent to the SET RELIABLE ON command.</p>
<dt>-J arg</p>
<dd> (ACTION) &quot;Be like Telnet.&quot; Like -j but implies -E. Argument: IP hostname/address optionally followed by service. NOTE: C-Kermit also has a separate Telnet command-line personality, with regular Telnet-like command-line syntax. More about this below.</p>
<dt>-L</p>
<dd> Recursive directory descent for files in -s option.</p>
<dt>-M arg</p>
<dd> My user name (for use with Telnet, Rlogin, FTP, etc). Equivalent to the SET LOGIN USER command. Argument: Username string.</p>
<dt>-O</p>
<dd> (ACTION) (Uppercase letter O) Be a server for One command only. Also see: -x.</p>
<dt>-P</p>
<dd> Don&#8217;t convert file (Path) names of transferred files. Equivalent to SET FILE NAMES LITERAL.</p>
<dt>-Q</p>
<dd> Quick Kermit protocol settings. Equivalent to the FAST command. This is the default in C-Kermit 7.0 and later.</p>
<dt>-R</p>
<dd> Remote-only (this just makes IF REMOTE true).</p>
<dt>-S</p>
<dd> Stay (enter command parser after action options).</p>
<dt>-T</p>
<dd> Force Text mode for file transfer; implies -V. Equivalent to SET TRANSFER MODE MANUAL, SET FILE TYPE TEXT.</p>
<dt>-V</p>
<dd> Disable automatic per-file text/binary switching. Equivalent to SET TRANSFER MODE MANUAL.</p>
<dt>-Y</p>
<dd> Skip (don&#8217;t execute) the initialization file.</p>
<dt>-a arg</p>
<dd> As-name for file(s) in -s, -r, or -g. Argument: As-name string (alternative filename). When receiving files, this can be a directory name.</p>
<dt>-b arg</p>
<dd> Speed for serial device. Equivalent to SET SPEED. Argument: Numeric Bits per second for serial connections.</p>
<dt>-c</p>
<dd> (ACTION) Enter Connect state before transferring files.</p>
<dt>-d</p>
<dd> Create a debug.log file with detailed debugging information (a second -d adds timestamps). Equivalent to LOG DEBUG but takes effect sooner.</p>
<dt>-e arg</p>
<dd> Maximum length for incoming Kermit file-transfer packets. Equivalent to SET RECEIVE PACKET-LENGTH. Argument: Length in bytes.</p>
<dt>-f</p>
<dd> (ACTION) Send a FINISH command to a Kermit server.</p>
<dt>-g arg</p>
<dd> Get file(s) from a Kermit server. Argument: File specification on other computer, in quotes if it contains metacharacters. Equivalent to GET. Also see: -a, -G, -r.</p>
<dt>-h</p>
<dd> (ACTION) Print Help text for single-letter command-line options (pipe thru &#8216;more&#8217; to prevent scrolling).</p>
<dt>-i</p>
<dd> Force binary (Image) mode for file transfer; implies -V. Equivalent to SET TRANSFER MODE MANUAL, SET FILE TYPE BINARY.</p>
<dt>-j arg</p>
<dd> Make a TCP/IP connection. Argument: IP host name/address and optional service name or number. Equivalent to the TELNET command. Also see: -J, -F.</p>
<dt>-k</p>
<dd> (ACTION) Receive file(s) to standard output, which normally would be piped to another process. Also see: -r, -G.</p>
<dt>-l arg</p>
<dd> (Lowercase letter L) Make a connection on the given serial communications device. Equivalent to the SET LINE (SET PORT) command. Argument: Serial device name, e.g. /dev/ttyS0.</p>
<dt>-m arg</p>
<dd> Modem type for use with the -l device. Equivalent to the SET MODEM TYPE command. Argument: Modem name as in SET MODEM TYPE command, e.g. &quot;usrobotics&quot;.</p>
<dt>-n</p>
<dd> (ACTION) Enter Connect state after transferring files (historical).</p>
<dt>-p arg</p>
<dd> Parity. Equivalent to the SET PARITY command. Argument: One of the following: e(ven), o(dd), m(ark), n(one), s(pace).</p>
<dt>-q</p>
<dd> Quiet (suppress most messages). Equivalent to SET QUIET ON.</p>
<dt>-r</p>
<dd> (ACTION) Receive file(s). Equivalent to the RECEIVE command. Argument: (none, but see -a)</p>
<dt>-s arg</p>
<dd> Send file(s). Argument: One or more local file specifications. Equivalent to the SEND command. Also see: -a.</p>
<dt>-t</p>
<dd> (Historical) Xon (Ctrl-Q) Turnaround character for half-duplex connections (used on serial linemode connections to old mainframes). Equivalent to SET DUPLEX HALF, SET HANDSHAKE XON.</p>
<dt>-v arg</p>
<dd> Window size for Kermit protocol (ignored when streaming). Equivalanet to SET WINDOW-SIZE. Argument: Number, 1 to 32.</p>
<dt>-w</p>
<dd> Incoming files Write over existing files. Equivalent to SET FILE COLLISION OVERWRITE.</p>
<dt>-x</p>
<dd> (ACTION) Enter server mode. Equivalent to the SERVER command. Also see: -O.</p>
<dt>-y arg</p>
<dd> Alternative initialization file. Argument: Filename.</p>
<dt>-z</p>
<dd> Force foreground behavior. To be used in case Kermit doesn&#8217;t automatically sense its foreground status. Equivalent to the SET BACKGROUND OFF command.</dl>
<p> Extended command-line options (necessary because single-letter ones are about used up) start with two dashes (&#8211;), with words rather than single letters as option names. If an extended option takes an argument, it is separated from the option word by a colon (:). Extended options include: </p>
<dl>
<dt>
&nbsp;<wbr>&#8211;bannerfile:filename</p>
<dd> File to display upon startup or IKSD login.</p>
<dt>
&nbsp;<wbr>&#8211;cdfile:filename</p>
<dd> File to be sent for display to the client when server changes directory (filename is relative to the changed-to directory).</p>
<dt>
&nbsp;<wbr>&#8211;cdmessage:{on,off}</p>
<dd> Enable/disable the server CD message feature.</p>
<dt>
&nbsp;<wbr>&#8211;help</p>
<dd> Prints usage message for extended options.</p>
<dt>
&nbsp;<wbr>&#8211;helpfile:filename</p>
<dd> Designates a file containing custom text to replace the top-level HELP command.</p>
<dt>
&nbsp;<wbr>&#8211;nointerrupts</p>
<dd> Disables keyboard interrupts.</p>
<dt>
&nbsp;<wbr>&#8211;noperms</p>
<dd> Disables the Kermit protocol file Permissions attribute, to prevent transmission of file permissions (protection) from sender to receiver.</p>
<dt>
&nbsp;<wbr>&#8211;version</p>
<dd> (ACTION) C-Kermit prints its version number.</dl>
<p> Plus several other IKSD-Only options described at: </p>
<p>&nbsp;<wbr>&nbsp;<wbr><a rel="nofollow" href="http://www.columbia.edu/kermit/iksd.html">http://www.columbia.edu/kermit/iksd.html</a> </p>
<p> See the file-transfer section for examples of command-line invocation.</p>
<h2>COMMAND LANGUAGE</h2>
<p> C-Kermit&#8217;s interactive command language is the subject of a 622-page book and another several hundred pages of updates, far too much for a manual page. But it&#8217;s not hard to get started. At the shell prompt, just type &quot;kermit&quot; to get C-Kermit&#8217;s interactive command prompt: </p>
<pre>
  $ kermit
  (/current/directory) C-Kermit&gt;
</pre>
<p> Begin by typing &quot;help&quot; (and then press the Return or Enter key) for a top-level overview, read it, and go from there. Your second command should probably be &quot;intro&quot; (introduction). Note the prompt shows your current directory (unless you tell Kermit to prompt you with something else). </p>
<p> Interactive commands are composed mainly of regular English words, usually in the form of imperative sentences, such as: </p>
<p>&nbsp;<wbr>&nbsp;<wbr>send oofa.txt </p>
<p> which tells Kermit to send (transfer) the file whose name is oofa.txt, or: </p>
<p>&nbsp;<wbr>&nbsp;<wbr>set transfer mode automatic </p>
<p> which sets Kermit&#8217;s &quot;transfer mode&quot; to &quot;automatic&quot; (whatever that means). </p>
<p> While typing commands, you can abbreviate, ask for help (by pressing the &quot;?&quot; key anywhere in a command), complete keywords or filenames (with the Tab or Esc key), and edit your typing with Backspace or Delete, Ctrl-W, Ctrl-U, etc. You can also recall previous commands, save your command history, and who knows what else. Give the INTRO command for details. </p>
<p> C-Kermit has hundreds of commands, and they can be issued in infinite variety and combinations, including commands for:<br />
&amp;bull;<br />
Making connections(SET LINE, DIAL, TELNET, SSH, FTP, &#8230;)</p>
<p>    &amp; bull;<br />
Breaking connections(HANGUP, CLOSE)</p>
<p>    &amp; bull;<br />
Transferring files(SEND, GET, RECEIVE, MOVE, RESEND, &#8230;)</p>
<p>    &amp; bull;<br />
Establishing preferences(SET)</p>
<p>    &amp; bull;<br />
Displaying preferences(SHOW)</p>
<p>    &amp; bull;<br />
Managing local files(CD, DELETE, MKDIR, DIR, RENAME, TYPE, &#8230;)</p>
<p>    &amp; bull;<br />
Managing remote files(RCD, RDEL, RMKDIR, RDIR, &#8230;)</p>
<p>    &amp; bull;<br />
Using local files(FOPEN, FCLOSE, FREAD, FWRITE)</p>
<p>    &amp; bull;<br />
Programming(TAKE, DEFINE, IF, FOR, WHILE, SWITCH, DECLARE, &#8230;)</p>
<p>    &amp; bull;<br />
Interacting with the user(ECHO, ASK, &#8230;)</p>
<p>    &amp; bull;<br />
Interacting with a remote computer(INPUT, OUTPUT, &#8230;)</p>
<p>    &amp; bull;<br />
Interacting with local programs(RUN, EXEC, PTY, &#8230;)</p>
<p>    &amp; bull;<br />
Logging things(LOG SESSION, LOG PACKETS, LOG DEBUG, &#8230;)<br />
 And of course QUIT or EXIT to get out and HELP to get help, and for programmers: loops, decision making, variables, arrays, associative arrays, integer and floating point arithmetic, macros, built-in and user-defined functions, string manipulation, pattern matching, block structure, scoping, recursion, and all the rest. To get a list of all C-Kermit&#8217;s commands, type a question mark (?) at the prompt. To get a description of any command, type HELP followed by the name of the command, for example: </p>
<p>&nbsp;<wbr>&nbsp;<wbr>help send </p>
<p> The command interruption character is Ctrl-C (hold down the Ctrl key and press the C key). </p>
<p> The command language &quot;escape character&quot;, used to introduce variable names, function invocations, and so on, is backslash (). If you need to include a literal backslash in a command, type two of them, e.g.: </p>
<p>&nbsp;<wbr>&nbsp;<wbr>get c:\k95\k95custom.ini</p>
<h3>Command Files, Macros, and Scripts</h3>
<p> A file containing Kermit commands is called a Kermit command file or Kermit script. It can be executed with Kermit&#8217;s TAKE command: </p>
<p>&nbsp;<wbr>&nbsp;<wbr>(/current/dir)&nbsp;<wbr>C-Kermit&gt;&nbsp;<wbr>take commandfile </p>
<p> (where &quot;commandfile&quot; is the name of the command file). Please don&#8217;t pipe a command file into Kermit&#8217;s standard input (which might or might not work); if you have Kermit commands in a file, tell Kermit to TAKE the file. </p>
<p> In Unix only, a Kermit command file can also be executed directly by including a &quot;kerbang&quot; line as the first line of the file: </p>
<p>&nbsp;<wbr>&nbsp;<wbr>#!/usr/local/bin/kermit&nbsp;<wbr>+ </p>
<p> That is, a top line that starts with &quot;#!&quot;, followed immediately by the full path of the Kermit executable, and then, if the Kermit script is to be given arguments on the command line, a space and a plus sign. The script file must also have execute permission: </p>
<p>&nbsp;<wbr>&nbsp;<wbr>chmod&nbsp;<wbr>+x commandfile </p>
<p> Except for the &quot; +&quot; part, this is exactly the same as you would do for a shell script, a Perl script, etc. Here&#8217;s a simple but useless example script that regurgitates its arguments (up to three of them): </p>
<p>&nbsp;<wbr>&nbsp;<wbr>#!/usr/local/bin/kermit&nbsp;<wbr>+<br />
&nbsp;<wbr>&nbsp;<wbr>if defined&nbsp;<wbr>\%1 echo&nbsp;<wbr>&quot;Argument 1:&nbsp;<wbr>\%1&quot;<br />
&nbsp;<wbr>&nbsp;<wbr>if defined&nbsp;<wbr>\%2 echo&nbsp;<wbr>&quot;Argument 2:&nbsp;<wbr>\%2&quot;<br />
&nbsp;<wbr>&nbsp;<wbr>if defined&nbsp;<wbr>\%3 echo&nbsp;<wbr>&quot;Argument 3:&nbsp;<wbr>\%3&quot;<br />
&nbsp;<wbr>&nbsp;<wbr>if defined&nbsp;<wbr>\%4 echo&nbsp;<wbr>&quot;etc&#8230;&quot;<br />
&nbsp;<wbr>&nbsp;<wbr>exit </p>
<p> If this file is stored in your current directory as &quot;commandfile&quot;, then: </p>
<p>&nbsp;<wbr>&nbsp;<wbr>./commandfile one two three four five </p>
<p> prints: </p>
<p>&nbsp;<wbr>&nbsp;<wbr>Argument 1: one<br />
&nbsp;<wbr>&nbsp;<wbr>Argument 2: two<br />
&nbsp;<wbr>&nbsp;<wbr>Argument 3: three<br />
&nbsp;<wbr>&nbsp;<wbr>etc&#8230; </p>
<p> This illustrates the basic structure of a standalone Kermit script: the &quot;kerbang line&quot;, then some commands. It should end with &quot;exit&quot; unless you want the Kermit prompt to appear when it is finished. \%1 is the first argument, \%2 the second, and so on. </p>
<p> You can also create your own commands by defining named macros composed of other Kermit commands (or macros). For example: </p>
<p>define mydelete<br />
{<br />
    local trash<br />
            assign trash (home) trashcan /<br />
        if not defined \% 1 end 1 &#8220;Delete what?&#8221; if wild \% 1<br />
    {<br />
        end 1 &#8220;Deleting multiple files is too scary&#8221;<br />
    }<br />
    if<br />
        not exist \% 1 end 1 &#8220;I can&#8217;t find \%1&#8221; if not directory \m(trash)<br />
        {<br />
            mkdir \m(trash) if fail end 1 &#8220;No trash can&#8221;<br />
        }<br />
    rename / list \% 1 \m(trash)<br />
}<br />
define myundelete<br />
{<br />
    local trash<br />
            assign trash (home) trashcan /<br />
        if not defined \% 1 end 1 &#8220;Undelete what?&#8221; if wild \% 1<br />
    {<br />
        end 1 &#8220;Undeleting multiple files is too hard&#8221;<br />
    }<br />
    if<br />
        not directory \m(trash) end 1 &#8220;No trash can&#8221; if not exist \m(trash)\% 1 {end 1 &#8220;I can&#8217;t find \%1 in trash can&#8221;} rename / list \m(trash)\% 1.<br />
}<br />
 These sample macros are not exactly production quality (they don&#8217;t handle filenames that include path segments, they don&#8217;t handle multiple files, etc), but you get the idea: you can pass arguments to macros, and they can check them and make other kinds of decisions. If you put the above lines into your initialization or customization file (explained below), you&#8217;ll have MYDELETE and MYUNDELETE commands available every time you start Kermit, at least as long as you don&#8217;t suppress execution of the initialization file. (Exercise for the reader: Make these macros generally useful: remove limitations, add trashcan display, browsing, emptying, etc.) </p>
<p> Kerbang scripts execute without the initialization file. This to keep them portable and also to make them start faster. If you want to write Kerbang scripts that depend on the initialization file, include the command </p>
<p>&nbsp;<wbr>&nbsp;<wbr>take&nbsp;<wbr>(home).kermrc </p>
<p> at the desired spot in the script. By the way, (xxx) is a built-in variable (xxx is the variable name, &quot;home&quot; in this case). To see what built-in variables are available, type &quot;show variables&quot; at the C-Kermit prompt. To see what else you can show, type &quot;show ?&quot;. \m(xxx) is a user defined variable (strictly speaking, it is a macro used as a variable).</p>
<h3>Command List</h3>
<p> C-Kermit has more than 200 top-level commands, and some of these, such as SET, branch off into hundreds of subcommands of their own, so it&#8217;s not practical to describe them all here. Instead, here&#8217;s a concise list of the most commonly used top-level commands, grouped by category. To learn about each command, type &quot;help&quot; followed by the command name, e.g. &quot;help set&quot;. Terms such as Command state and Connect state are explained in subsequent sections. </p>
<p> Optional fields are shown in [ brackets ]. &quot;filename&quot; means the name of a single file. filespec means a file specification that is allowed to contain wildcard characters like &#8216;*&#8217; to match groups of files. options are (optional) switches like /PAGE, /NOPAGE, /QUIET, etc, listed in the HELP text for each command. Example: </p>
<pre>
  send /recursive /larger:10000 /after:-1week /except:*.txt *
</pre>
<p> which can be read as &quot;send all the files in this directory and all the ones underneath it that are larger than 10000 bytes, no more than one week old, and whose names don&#8217;t end with &quot;.txt&quot;.</p>
<h3>Basic Commands</h3>
<dl>
<dt>
<dd>
<dl>
<dt>HELP</p>
<dd> Requests top-level help.</p>
<dt>HELP command</p>
<dd> Requests help about the given command.</p>
<dt>INTRODUCTION</p>
<dd> Requests a brief introduction to C-Kermit.</p>
<dt>LICENSE</p>
<dd> Displays the C-Kermit software copyright and license.</p>
<dt>VERSION</p>
<dd> Displays C-Kermit&#8217;s version number.</p>
<dt>EXIT [ number ]</p>
<dd> Exits from Kermit with the given status code. Synonyms: QUIT, E, Q.</p>
<dt>TAKE filename [ parameters&#8230; ]</p>
<dd> Executes commands from the given</p>
<dt>LOG item [ filename ]</p>
<dd> Keeps a log of the given item in the given file.</p>
<dt>[ DO ] macro [ parameters&#8230; ]</p>
<dd> Executes commands from the given macro.</p>
<dt>SET parameter value</p>
<dd> Sets the given parameter to the given value.</p>
<dt>SHOW category</p>
<dd> Shows settings in a given category.</p>
<dt>STATUS</p>
<dd> Tells whether previous command succeeded or failed.</p>
<dt>DATE [ date-and/or-time ]</p>
<dd> Shows current date-time or interprets given date-time.</p>
<dt>RUN [ extern-command [ parameters&#8230; ]</p>
<dd> Runs the given external command. Synonym: !.</p>
<dt>EXEC [ extern-command [ params&#8230; ]</p>
<dd> Kermit overlays itself with the given command.</p>
<dt>SUSPEND</p>
<dd> Stops Kermit and puts it in the background. Synonym: Z.</dl>
</dl>
<h3>Local File Management</h3>
<dl>
<dt>
<dd>
<dl>
<dt>TYPE [ options ] filename</p>
<dd> Displays the contents of the given file.</p>
<dt>MORE [ options ] filename</p>
<dd> Equivalent to TYPE /PAGE (pause after each screenful).</p>
<dt>CAT [ options ] filename</p>
<dd> Equivalent to TYPE /NOPAGE.</p>
<dt>HEAD [ options ] filename</p>
<dd> Displays the first few lines of a given file.</p>
<dt>TAIL [ options ] filename</p>
<dd> Displays the last few lines of a given file.</p>
<dt>GREP [ options ] pattern filespec</p>
<dd> Displays lines from files that match the pattern. Synonym: FIND.</p>
<dt>DIRECTORY [ options ] [filespec ]</p>
<dd> Lists files (built-in, many options).</p>
<dt>LS [ options ] [ filespec ]</p>
<dd> Lists files (runs external &quot;ls&quot; command).</p>
<dt>DELETE [ options ] [ filespec ]</p>
<dd> Deletes files. Synonym: RM.</p>
<dt>PURGE [ options ] [ filespec ]</p>
<dd> Removes backup (*.~n~) files.</p>
<dt>COPY [ options ] [ filespecs&#8230; ]</p>
<dd> Copies files. Synonym: CP.</p>
<dt>RENAME [ options ] [ filespecs&#8230; ]</p>
<dd> Renames files. Synonym: MV.</p>
<dt>CHMOD [ options ] [ filespecs&#8230; ]</p>
<dd> Changes permissions of files.</p>
<dt>TRANSLATE filename charsets [ filename ]</p>
<dd> Converts file&#8217;s character set. Synonym: XLATE.</p>
<dt>CD</p>
<dd> Changes your working directory to your home directory.</p>
<dt>CD directory</p>
<dd> Changes your working directory to the one given.</p>
<dt>CDUP</p>
<dd> Changes your working directory one level up.</p>
<dt>PWD</p>
<dd> Displays your working directory.</p>
<dt>BACK</p>
<dd> Returns to your previous working directory.</p>
<dt>MKDIR [ directory ]</p>
<dd> Creates a directory.</p>
<dt>RMDIR [ directory ]</p>
<dd> Removes a directory.</dl>
</dl>
<h3>Making Connections</h3>
<dl>
<dt>
<dd>
<dl>
<dt>SET LINE [ options ] devicename</p>
<dd> Opens the named serial port. Synonym: SET PORT.</p>
<dt>OPEN LINE [ options ] devicename</p>
<dd> Same as SET LINE. Synonym: OPEN PORT.</p>
<dt>SET MODEM TYPE [ name ]</p>
<dd> Tells Kermit what kind of modem is on the port.</p>
<dt>DIAL [ number ]</p>
<dd> Tells Kermit to dial the given phone number with the modem.</p>
<dt>REDIAL</p>
<dd> Redials the most recently dialed phone number.</p>
<dt>ANSWER</p>
<dd> Waits for and answers an incoming call on the modem.</p>
<dt>AUTHENTICATE [ parameters&#8230; ]</p>
<dd> Performs secure authentication on a TCP/IP connection.</p>
<dt>SET NETWORK TYPE { TCP/IP, X.25, &#8230; }</p>
<dd> Selects network type for subsequent SET HOST commands.</p>
<dt>SET HOST [ options ] host [ port ]</p>
<dd> Opens a network connection to the given host and port.</p>
<dt>SET HOST * port</p>
<dd> Waits for an incoming TCP/IP connection on the given port.</p>
<dt>TELNET [ options ] host</p>
<dd> Opens a Telnet connection to the host and enters Connect state.</p>
<dt>RLOGIN [ options ] host</p>
<dd> Opens an Rlogin connection to the host and enters Connect state.</p>
<dt>IKSD [ options ] host</p>
<dd> Opens a connection to an Internet Kermit Service.</p>
<dt>SSH [ options ] host</p>
<dd> Opens an SSH connection to the host and enters Connect state.</p>
<dt>FTP OPEN host [ options ]</p>
<dd> Opens an FTP connection to the host.</p>
<dt>HTTP [ options ] OPEN host</p>
<dd> Opens an HTTP connection to the host.</p>
<dt>PTY external-command</p>
<dd> Runs the command on a pseudoterminal as if it were a connection.</p>
<dt>PIPE external-command</p>
<dd> Runs the command through a pipe as if it were a connection.</dl>
</dl>
<h3>Using Connections</h3>
<dl>
<dt>
<dd>
<dl>
<dt>CONNECT [ options ]</p>
<dd> Enters Connect (terminal) state. Synonym: C.</p>
<dt>REDIRECT command</p>
<dd> Redirects the given external command over the connection.</p>
<dt>TELOPT command</p>
<dd> Sends a Telnet protocol command (Telnet connections only).</p>
<dt>Ctrl-\C</p>
<dd> &quot;Escapes back&quot; from Connect state to Command state.</p>
<dt>Ctrl-\B</p>
<dd> (In Connect state) Sends a BREAK signal (serial or Telnet).</p>
<dt>Ctrl-\!</p>
<dd> (In Connect state) Enters inferior shell; &quot;exit&quot; to return.</p>
<dt>Ctrl-\?</p>
<dd> (In Connect state) Shows a menu of other escape-level options.</p>
<dt>Ctrl-\Ctrl-\</p>
<dd> (In Connect state) Type two Ctrl-Backslashes to send one of them.</p>
<dt>SET ESCAPE [ character ]</p>
<dd> Changes Kermit&#8217;s Connect-state escape character.</dl>
</dl>
<h3>Closing Connections</h3>
<dl>
<dt>
<dd>
<dl>
<dt>HANGUP</p>
<dd> Hangs up the currently open serial-port or network connection.</p>
<dt>CLOSE</p>
<dd> Closes the currently open serial-port or network connection.</p>
<dt>SET LINE (with no devicename)</p>
<dd> Closes the currently open serial-port or network connection.</p>
<dt>SET HOST (with no hostname)</p>
<dd> Closes the currently open serial-port or network connection.</p>
<dt>FTP CLOSE</p>
<dd> Closes the currently open FTP connection.</p>
<dt>HTTP CLOSE</p>
<dd> Closes the currently open HTTP connection.</p>
<dt>EXIT</p>
<dd> Also closes all connections. Synonym: QUIT.</p>
<dt>SET EXIT WARNING OFF</p>
<dd> Suppresses warning about open connections on exit or close.</dl>
</dl>
<h3>File Transfer</h3>
<dl>
<dt>
<dd>
<dl>
<dt>SEND [ options ] filename [ as-name ]</p>
<dd> Sends the given file. Synonym: S.</p>
<dt>SEND [ options ] filespec</p>
<dd> Sends all files that match.</p>
<dt>RESEND [ options ] filespec</p>
<dd> Resumes an interrupted SEND from the point of failure.</p>
<dt>RECEIVE [ options ] [ as-name ]</p>
<dd> Waits passively for files to arrive. Synonym: R.</p>
<dt>LOG TRANSACTIONS [ filename ]</p>
<dd> Keeps a record of file transfers.</p>
<dt>FAST</p>
<dd> Use fast file-transfer settings (default).</p>
<dt>CAUTIOUS</p>
<dd> Use cautious and less fast file-transfer settings.</p>
<dt>ROBUST</p>
<dd> Use ultra-conservative and slow file-transfer settings.</p>
<dt>STATISTICS [ options ]</p>
<dd> Gives statistics about the most recent file transfer.</p>
<dt>WHERE</p>
<dd> After transfer: &quot;Where did my files go?&quot;.</p>
<dt>TRANSMIT [ options ] [ofilename ]</p>
<dd> Sends file without protocol. Synonym: XMIT.</p>
<dt>LOG SESSION [ filename ]</p>
<dd> Captures remote text or files without protocol.</p>
<dt>SET PROTOCOL [ name&#8230; ]</p>
<dd> Tells Kermit to use an external file-transfer protocol.</p>
<dt>FTP { PUT, MPUT, GET, MGET, &#8230; }</p>
<dd> FTP client commands.</p>
<dt>HTTP { PUT, GET, HEAD, POST, &#8230; }</p>
<dd> HTTP client commands.</dl>
</dl>
<h3>Kermit Server</h3>
<dl>
<dt>
<dd>
<dl>
<dt>ENABLE, DISABLE</p>
<dd> Controls which server features can be used by clients.</p>
<dt>SET SERVER</p>
<dd> Sets parameters prior to entering Server state.</p>
<dt>SERVER</p>
<dd> Enters Server state.</dl>
</dl>
<h3>Client of Kermit or FTP Server</h3>
<dl>
<dt>
<dd>
<dl>
<dt>[ REMOTE ] LOGIN [ user password ]</p>
<dd> Logs in to a Kermit server or IKSD that requires it.</p>
<dt>[ REMOTE ] LOGOUT</p>
<dd> Logs out from a Kermit server or IKSD.</p>
<dt>SEND [ options ] filename [ as-name ]</p>
<dd> Sends the given file to the server. Synonyms: S, PUT.</p>
<dt>SEND [ options ] filespec</p>
<dd> Sends all files that match.</p>
<dt>RESEND [ options ] filespec</p>
<dd> Resumes an interrupted SEND from the point of failure.</p>
<dt>GET [ options ] remote-filespec</p>
<dd> Asks the server to send the given files. Synonym: G.</p>
<dt>REGET [ options ] remote-filespec</p>
<dd> Resumes an interrupted GET from the point of failure.</p>
<dt>REMOTE CD [ directory ]</p>
<dd> Asks server to change its working directory. Synonym: RCD.</p>
<dt>REMOTE PWD [ directory ]</p>
<dd> Asks server to display its working directory. Synonym: RPWD.</p>
<dt>REMOTE DIRECTORY [ filespec&#8230; ]</p>
<dd> Asks server to send a directory listing. Synonym: RDIR.</p>
<dt>REMOTE DELETE [ filespec&#8230; ]</p>
<dd> Asks server to delete files. Synonym: RDEL.</p>
<dt>REMOTE [ command&#8230; ]</p>
<dd> (Many other commands: &quot;remote ?&quot; for a list).</p>
<dt>MAIL [ options ] filespec</p>
<dd> Sends file(s) to be delivered as e-mail (Kermit only).</p>
<dt>FINISH</p>
<dd> Asks the server to exit server state (Kermit only).</p>
<dt>BYE</p>
<dd> Asks the server to log out and close the connection.</dl>
</dl>
<h3>Script Programming</h3>
<dl>
<dt>
<dd> DEFINE, DECLARE, UNDEFINE, UNDECLARE, ASSIGN, EVALUATE, SEXPRESSION, ARRAY, SORT, INPUT, OUTPUT, IF, FOR, WHILE, SWITCH, GOTO, ECHO, ASK, GETC, GETOK, ASSERT, WAIT, SLEEP, FOPEN, FREAD, FWRITE, FCLOSE, STOP, END, RETURN, LEARN, SHIFT, TRACE, VOID, INCREMENT, DECREMENT, &#8230; For these and many more you&#8217;ll need to consult the manual and supplements, and/or visit the Kermit Script Library, which also includes a brief tutorial. Hint: HELP LEARN to find out how to get Kermit to write simple scripts for you.</dl>
<p> Many of Kermit&#8217;s commands have synonyms, variants, relatives, and so on. For example, MSEND is a version of SEND that accepts a list of file specifications to be sent, rather than just one file specification, and MPUT is a synonym of MSEND. MOVE means to SEND and then DELETE the source file if successful. MMOVE is like MOVE, but accepts a list of filespecs, and so on. These are described in the full documentation. </p>
<p> Use question mark to feel your way through an unfamiliar command, as in this example: </p>
<pre>
  C-Kermit&gt; remote ? One of the following:
   assign     directory  kermit     print      rmdir
   cd         exit       login      pwd        set
   copy       help       logout     query      space
   delete     host       mkdir      rename     type
  C-Kermit&gt; remote set ? One of the following:
   attributes   file         retry        transfer
   block-check  receive      server       window
  C-Kermit&gt; remote set file ? One of the following:
   character-set  incomplete     record-length
   collision      names          type
  C-Kermit&gt; remote set file names ? One of the following:
   converted  literal
  C-Kermit&gt; remote set file names literal
  C-Kermit&gt;
</pre>
<p> This is called menu on demand: you get a menu when you want one, but menus are not forced on you even when know what you&#8217;re doing. Note that you can also abbreviate most keywords, and you can complete them with the Tab or Esc key. Also note that ? works for filenames too, and that you can use it in the middle of a keyword or filename, not just at the beginning. For example, &quot;send x?&quot; lists all the files in the current directory whose names start with &#8216;x&#8217;.</p>
<h2>INITIALIZATION FILE</h2>
<p> In its default configuration, C-Kermit executes commands from a file called .kermrc in your home directory when it starts, unless it is given the -Y or -y command-line option. Custom configurations might substitute a shared system-wide initialization file. The SHOW FILE command tells what initialization file, if any, was used. The standard initialization file &quot;chains&quot; to an individual customization file, .mykermc, in the home directory, in which each user can establish her/his own preferences, define macros, and so on. </p>
<p> Since execution of the initialization file (at least the standard one) makes C-Kermit take longer to start, it might be better not to have an initialization file, especially now that Kermit&#8217;s default startup configuration is well attuned to modern computing and networking &#8212; in other words, you no longer have do anything special to make Kermit transfers go fast. So instead of having an initialization file that is executed every time Kermit starts, you might consider making one or more kerbang scripts (with names other that .kermrc) that do NOT include an &quot;exit&quot; command, and invoke those when you need the settings, macro definitions, and/or scripted actions they contain, and invoke C-Kermit directly when you don&#8217;t. </p>
<p> To put it another way&#8230; We still distribute the standard initialization file since it&#8217;s featured in the manual and backwards compatibility is important to us. But there&#8217;s no harm in not using it if you don&#8217;t need the stuff that&#8217;s in it (services directory, dialing directory, network directory, and associated macro definitions). On the other hand, if there are settings or macros you want in effect EVERY time you use Kermit, the initialization file (or the customization file it chains to) is the place to put them, because that&#8217;s the only place Kermit looks for them automatically each time you start it.</p>
<h2>MODES OF OPERATION</h2>
<p> Kermit is said to be in Local mode if it has made a connection to another computer, e.g. by dialing it or establishing a Telnet connection to it. The other computer is remote, so if you start another copy of Kermit on the remote computer, it is said to be in Remote mode (as long as it has not made any connections of its own). The local Kermit communicates over the communications device or network connection, acting as a conduit between the the remote computer and your keyboard and screen. The remote Kermit is the file-transfer partner to the local Kermit and communicates only through its standard input and output. </p>
<p> At any moment, a Kermit program can be in any of the following states. It&#8217;s important to know what they are and how to change from one to the other.</p>
<dl>
<dt>Command state</p>
<dd> In this state, Kermit reads commands from: </p>
<p> &bull;<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>Your keyboard; or:</p>
<p> &bull;<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>A file, or:</p>
<p> &bull;<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>A macro definition.</p>
<p> You can exit from Command state back to Unix with the EXIT or QUIT command (same thing). You can enter Connect state with any of various commands (CONNECT, DIAL, TELNET, etc). You can enter file transfer state with commands like SEND, RECEIVE, and GET. You can enter Server state with the SERVER command. The TAKE command tells Kermit to read and execute commands from a file. The (perhaps implied) DO command tells Kermit to read and execute commands from a macro definition. While in Command state, you can interrupt any command, macro, or command file by typing Ctrl-C (hold down the Ctrl key and press the C key); this normally brings you back to the prompt.</p>
<dt>Shell state</p>
<dd> You can invoke an inferior shell or external command from the Kermit command prompt by using the PUSH, RUN (!), EDIT, or BROWSE command. While the inferior shell or command is active, Kermit is suspended and does nothing. Return to Kermit Command state by exiting from the inferior shell or application.</p>
<dt>Connect state</p>
<dd> In this state, which can be entered only when in Local mode (i.e. when Kermit has made a connection to another computer), Kermit is acting as a terminal to the remote computer. Your keystrokes are sent to the remote computer and characters that arrive over the communication connection are displayed on your screen. This state is entered when you give a CONNECT, DIAL, TELNET, RLOGIN, or IKSD command. You can return to command state by logging out of the remote computer, or by typing: </p>
<p>&nbsp;<wbr>&nbsp;<wbr>Ctrl-
