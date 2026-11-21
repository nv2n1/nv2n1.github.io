---

title: "kermit(1)"
name: "kermit"
section: "1"
letter: "k"
url: "/docs/linux/man/1-kermit/"
description: "kermit – C-Kermit 9.0: transport- and platform-independent interactive and scriptable communications software."
---

<p> kermit &#8211; <code>C-Kermit 9.0:</code> transport- and platform-independent interactive and scriptable communications software.</p>
<dl>
<dt>
</dt><dd>
<p> This document is intended to give the beginner sufficient information to make basic (if not advanced) use of C-Kermit 9.0. Although it might be rather long for a Unix manual page, it&#8217;s still far shorter than the C-Kermit manual, which should be consulted for advanced topics such as customization, character-sets, scripting, etc. We also attempt to provide a clear structural overview of C-Kermit&#8217;s many capabilities, functional areas, states, and modes and their interrelation, that should be helpful to beginners and veterans alike, as well as to those upgrading to version 9.0 from earlier releases.</dd></dl>
<p> This document is also available as a Web page at:</p>
<dl>
<dt>
</dt><dd>
<p><a rel="nofollow" href="http://www.columbia.edu/kermit/ckututor.html">http://www.columbia.edu/kermit/ckututor.html</a></dd></dl>
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
<p> <code>kermit [</code> <i>filename</i> <code>] [</code> <i>options</i> <code>] [ {=,&#8211;,+}</code> <i>text</i> <code>] ]</code> </p>
<p> or: </p>
<p> <code>kermit </code> <i>URL</i> </p>
<p> If the first command-line argument is the name of a file, interactive-mode commands are executed from the file. The &#8216;=&#8217; (or &quot;&#8211;&quot;) argument tells Kermit not to parse the remainder of the command line, but to make the words following &#8216;=&#8217; available as \%1, \%2, &#8230; \%9. The &quot;+&quot; argument is like &quot;=&quot; but for use in &quot;kerbang scripts&quot; (explained below). A second command-line format allows the one and only argument to be a Telnet, FTP, HTTP, or IKSD URL. </p>
<p> Order of execution:</p>
<dl>
<dt>
&nbsp;<wbr>1.</dt>
<dd> The command file (if any).</dd>
<dt>
<pre>
</dt><dd> 2.
The initialization file, if any, unless suppressed with -Y.
</pre>
</dd><dt>
&nbsp;<wbr>3.</dt>
<dd> The customization file (if it is executed by the initialization file).</dd>
<dt>
&nbsp;<wbr>4.</dt>
<dd> The command-line URL (if any, and if so, execution stops here).</dd>
<dt>
&nbsp;<wbr>5.</dt>
<dd> Command-line options (if any).</dd>
<dt>
&nbsp;<wbr>6.</dt>
<dd> Interactive commands.</dd></dl>
<p> Some command-line options can cause actions (such as -s to send a file); others just set parameters. If any action options are included on the command line, Kermit exits when finished unless also given the -S (&quot;stay&quot;) option. If no action options are given, no initialization or command files contained an EXIT or QUIT command, and no fatal errors occurred, Kermit issues its prompt and waits for you to type commands.</p>
<dl>
<dt>
</dt><dd> Bear in mind that C-Kermit can be built with selected features disabled, and also that certain features are not available on all platforms. For example, C-Kermit can&#8217;t be built with TCP/IP support on a platform that does not have TCP/IP header files and libraries (and even if Kermit does include TCP/IP support, it can&#8217;t be used to make TCP/IP connections on a computer that does not have a TCP/IP stack installed). If your version of C-Kermit lacks a feature mentioned here, use its SHOW FEATURES command to see what might have been excluded.</dd></dl>
<p> C-Kermit has three kinds of commands: regular single-letter command-line options, extended-format command-line options, and interactive commands. </p>
<p> Like most Unix commands, C-Kermit can be be given options on the command line. But C-Kermit also can be used interactively by giving it commands composed of words, which are more intuitive than cryptic command-line options, and more flexible too. In other words, you don&#8217;t have to use C-Kermit&#8217;s command-line options, but they are available if you want to. (By the same token, you don&#8217;t have to use its interactive commands either &#8212; you can use either or both in any combination.) </p>
<p> C-Kermit is generally installed in the PATH as &quot;kermit&quot;, and therefore is invoked by typing the word &quot;kermit&quot; (lowercase) at the shell prompt, and then pressing the Return or Enter key. If you wish to include command-line options, put them after the word &quot;kermit&quot; but before pressing Return or Enter, separated by spaces, for example: </p>
<p>&nbsp;<wbr>&nbsp;<wbr>$&nbsp;<wbr>kermit -s ckermit.tar.gz </p>
<p> (&#8216;$&#8217; is the shell prompt; &quot;kermit -s ckermit.tar.gz&quot; is what you type, followed by Return or Enter.)</p>
<h2>OPTIONS</h2>
<p> Here is a list of C-Kermit&#8217;s single-letter command-line options, which start with a single dash (-), in ASCII (&quot;alphabetical&quot;) order. Alphabetic case is significant (-A is not the same as -a). Action options are tagged &quot;ACTION&quot;.</p>
<dl>
<dt>-0</dt>
<dd> (digit zero) 100% transparent Connect state for &quot;in-the-middle&quot; operation: 8 bits, no parity, no escape character, everything passes through.</dd>
<dt>-8</dt>
<dd> (digit eight) Connection is 8-bit clean (this is the default in C-Kermit 8.0 and later). Equivalent to the EIGHTBIT command, which in turn is a shortcut for SET TERMINAL BYTESIZE 8, SET COMMAND BYTESIZE 8, SET PARITY NONE.</dd>
<dt>-9 arg</dt>
<dd> (digit nine) Make a connection to an FTP server. Equivalent to the FTP OPEN command. Argument: IP-address-or-hostname[:optional-TCP-port]. NOTE: C-Kermit also has a separate FTP command-line personality, with regular FTP-like command-line syntax. More about this below.</dd>
<dt>-A</dt>
<dd> Kermit is to be started as an Internet service (IKSD) (only from inetd.conf).</dd>
<dt>-B</dt>
<dd> Kermit is running in Batch or Background (no controlling terminal). To be used in case Kermit doesn&#8217;t automatically sense its background status. Equivalent to the SET BACKGROUND ON command.</dd>
<dt>-C arg</dt>
<dd> Interactive-mode Commands to be executed. Argument: Commands separated by commas, list in doublequotes.</dd>
<dt>-D arg</dt>
<dd> Delay before starting to send in Remote mode. Equivalent to the SET DELAY command. Argument: Number of seconds.</dd>
<dt>-E</dt>
<dd> Exit automatically when connection closes. Equivalent to SET EXIT ON-DISCONNECT ON.</dd>
<dt>-F arg</dt>
<dd> Use an open TCP connection. Argument: Numeric file descriptor of open TCP connection. Also see: -j, -J.</dd>
<dt>-G arg</dt>
<dd> (ACTION) Get file(s) from server, send contents to standard output, which normally would be piped to another process. Argument: Remote file specification, in quotes if it contains metacharacters. Also see: -g, -k.</dd>
<dt>-H</dt>
<dd> Suppress program startup Herald and greeting.</dd>
<dt>-I</dt>
<dd> Tell Kermit it has a reliable connection, to force streaming to be used where it normally would not be. Equivalent to the SET RELIABLE ON command.</dd>
<dt>-J arg</dt>
<dd> (ACTION) &quot;Be like Telnet.&quot; Like -j but implies -E. Argument: IP hostname/address optionally followed by service. NOTE: C-Kermit also has a separate Telnet command-line personality, with regular Telnet-like command-line syntax. More about this below.</dd>
<dt>-L</dt>
<dd> Recursive directory descent for files in -s option.</dd>
<dt>-M arg</dt>
<dd> My user name (for use with Telnet, Rlogin, FTP, etc). Equivalent to the SET LOGIN USER command. Argument: Username string.</dd>
<dt>-O</dt>
<dd> (ACTION) (Uppercase letter O) Be a server for One command only. Also see: -x.</dd>
<dt>-P</dt>
<dd> Don&#8217;t convert file (Path) names of transferred files. Equivalent to SET FILE NAMES LITERAL.</dd>
<dt>-Q</dt>
<dd> Quick Kermit protocol settings. Equivalent to the FAST command. This is the default in C-Kermit 7.0 and later.</dd>
<dt>-R</dt>
<dd> Remote-only (this just makes IF REMOTE true).</dd>
<dt>-S</dt>
<dd> Stay (enter command parser after action options).</dd>
<dt>-T</dt>
<dd> Force Text mode for file transfer; implies -V. Equivalent to SET TRANSFER MODE MANUAL, SET FILE TYPE TEXT.</dd>
<dt>-V</dt>
<dd> Disable automatic per-file text/binary switching. Equivalent to SET TRANSFER MODE MANUAL.</dd>
<dt>-Y</dt>
<dd> Skip (don&#8217;t execute) the initialization file.</dd>
<dt>-a arg</dt>
<dd> As-name for file(s) in -s, -r, or -g. Argument: As-name string (alternative filename). When receiving files, this can be a directory name.</dd>
<dt>-b arg</dt>
<dd> Speed for serial device. Equivalent to SET SPEED. Argument: Numeric Bits per second for serial connections.</dd>
<dt>-c</dt>
<dd> (ACTION) Enter Connect state before transferring files.</dd>
<dt>-d</dt>
<dd> Create a debug.log file with detailed debugging information (a second -d adds timestamps). Equivalent to LOG DEBUG but takes effect sooner.</dd>
<dt>-e arg</dt>
<dd> Maximum length for incoming Kermit file-transfer packets. Equivalent to SET RECEIVE PACKET-LENGTH. Argument: Length in bytes.</dd>
<dt>-f</dt>
<dd> (ACTION) Send a FINISH command to a Kermit server.</dd>
<dt>-g arg</dt>
<dd> Get file(s) from a Kermit server. Argument: File specification on other computer, in quotes if it contains metacharacters. Equivalent to GET. Also see: -a, -G, -r.</dd>
<dt>-h</dt>
<dd> (ACTION) Print Help text for single-letter command-line options (pipe thru &#8216;more&#8217; to prevent scrolling).</dd>
<dt>-i</dt>
<dd> Force binary (Image) mode for file transfer; implies -V. Equivalent to SET TRANSFER MODE MANUAL, SET FILE TYPE BINARY.</dd>
<dt>-j arg</dt>
<dd> Make a TCP/IP connection. Argument: IP host name/address and optional service name or number. Equivalent to the TELNET command. Also see: -J, -F.</dd>
<dt>-k</dt>
<dd> (ACTION) Receive file(s) to standard output, which normally would be piped to another process. Also see: -r, -G.</dd>
<dt>-l arg</dt>
<dd> (Lowercase letter L) Make a connection on the given serial communications device. Equivalent to the SET LINE (SET PORT) command. Argument: Serial device name, e.g. /dev/ttyS0.</dd>
<dt>-m arg</dt>
<dd> Modem type for use with the -l device. Equivalent to the SET MODEM TYPE command. Argument: Modem name as in SET MODEM TYPE command, e.g. &quot;usrobotics&quot;.</dd>
<dt>-n</dt>
<dd> (ACTION) Enter Connect state after transferring files (historical).</dd>
<dt>-p arg</dt>
<dd> Parity. Equivalent to the SET PARITY command. Argument: One of the following: e(ven), o(dd), m(ark), n(one), s(pace).</dd>
<dt>-q</dt>
<dd> Quiet (suppress most messages). Equivalent to SET QUIET ON.</dd>
<dt>-r</dt>
<dd> (ACTION) Receive file(s). Equivalent to the RECEIVE command. Argument: (none, but see -a)</dd>
<dt>-s arg</dt>
<dd> Send file(s). Argument: One or more local file specifications. Equivalent to the SEND command. Also see: -a.</dd>
<dt>-t</dt>
<dd> (Historical) Xon (Ctrl-Q) Turnaround character for half-duplex connections (used on serial linemode connections to old mainframes). Equivalent to SET DUPLEX HALF, SET HANDSHAKE XON.</dd>
<dt>-v arg</dt>
<dd> Window size for Kermit protocol (ignored when streaming). Equivalanet to SET WINDOW-SIZE. Argument: Number, 1 to 32.</dd>
<dt>-w</dt>
<dd> Incoming files Write over existing files. Equivalent to SET FILE COLLISION OVERWRITE.</dd>
<dt>-x</dt>
<dd> (ACTION) Enter server mode. Equivalent to the SERVER command. Also see: -O.</dd>
<dt>-y arg</dt>
<dd> Alternative initialization file. Argument: Filename.</dd>
<dt>-z</dt>
<dd> Force foreground behavior. To be used in case Kermit doesn&#8217;t automatically sense its foreground status. Equivalent to the SET BACKGROUND OFF command.</dd></dl>
<p> Extended command-line options (necessary because single-letter ones are about used up) start with two dashes (&#8211;), with words rather than single letters as option names. If an extended option takes an argument, it is separated from the option word by a colon (:). Extended options include: </p>
<dl>
<dt>
&nbsp;<wbr>&#8211;bannerfile:filename</dt>
<dd> File to display upon startup or IKSD login.</dd>
<dt>
&nbsp;<wbr>&#8211;cdfile:filename</dt>
<dd> File to be sent for display to the client when server changes directory (filename is relative to the changed-to directory).</dd>
<dt>
&nbsp;<wbr>&#8211;cdmessage:{on,off}</dt>
<dd> Enable/disable the server CD message feature.</dd>
<dt>
&nbsp;<wbr>&#8211;help</dt>
<dd> Prints usage message for extended options.</dd>
<dt>
&nbsp;<wbr>&#8211;helpfile:filename</dt>
<dd> Designates a file containing custom text to replace the top-level HELP command.</dd>
<dt>
&nbsp;<wbr>&#8211;nointerrupts</dt>
<dd> Disables keyboard interrupts.</dd>
<dt>
&nbsp;<wbr>&#8211;noperms</dt>
<dd> Disables the Kermit protocol file Permissions attribute, to prevent transmission of file permissions (protection) from sender to receiver.</dd>
<dt>
&nbsp;<wbr>&#8211;version</dt>
<dd> (ACTION) C-Kermit prints its version number.</dd></dl>
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
<dl>
<dt>HELP</dt>
<dd> Requests top-level help.</dd>
<dt>HELP command</dt>
<dd> Requests help about the given command.</dd>
<dt>INTRODUCTION</dt>
<dd> Requests a brief introduction to C-Kermit.</dd>
<dt>LICENSE</dt>
<dd> Displays the C-Kermit software copyright and license.</dd>
<dt>VERSION</dt>
<dd> Displays C-Kermit&#8217;s version number.</dd>
<dt>EXIT [ number ]</dt>
<dd> Exits from Kermit with the given status code. Synonyms: QUIT, E, Q.</dd>
<dt>TAKE filename [ parameters&#8230; ]</dt>
<dd> Executes commands from the given</dd>
<dt>LOG item [ filename ]</dt>
<dd> Keeps a log of the given item in the given file.</dd>
<dt>[ DO ] macro [ parameters&#8230; ]</dt>
<dd> Executes commands from the given macro.</dd>
<dt>SET parameter value</dt>
<dd> Sets the given parameter to the given value.</dd>
<dt>SHOW category</dt>
<dd> Shows settings in a given category.</dd>
<dt>STATUS</dt>
<dd> Tells whether previous command succeeded or failed.</dd>
<dt>DATE [ date-and/or-time ]</dt>
<dd> Shows current date-time or interprets given date-time.</dd>
<dt>RUN [ extern-command [ parameters&#8230; ]</dt>
<dd> Runs the given external command. Synonym: !.</dd>
<dt>EXEC [ extern-command [ params&#8230; ]</dt>
<dd> Kermit overlays itself with the given command.</dd>
<dt>SUSPEND</dt>
<dd> Stops Kermit and puts it in the background. Synonym: Z.</dd></dl>
</dl>
<h3>Local File Management</h3>
<dl>
<dl>
<dt>TYPE [ options ] filename</dt>
<dd> Displays the contents of the given file.</dd>
<dt>MORE [ options ] filename</dt>
<dd> Equivalent to TYPE /PAGE (pause after each screenful).</dd>
<dt>CAT [ options ] filename</dt>
<dd> Equivalent to TYPE /NOPAGE.</dd>
<dt>HEAD [ options ] filename</dt>
<dd> Displays the first few lines of a given file.</dd>
<dt>TAIL [ options ] filename</dt>
<dd> Displays the last few lines of a given file.</dd>
<dt>GREP [ options ] pattern filespec</dt>
<dd> Displays lines from files that match the pattern. Synonym: FIND.</dd>
<dt>DIRECTORY [ options ] [filespec ]</dt>
<dd> Lists files (built-in, many options).</dd>
<dt>LS [ options ] [ filespec ]</dt>
<dd> Lists files (runs external &quot;ls&quot; command).</dd>
<dt>DELETE [ options ] [ filespec ]</dt>
<dd> Deletes files. Synonym: RM.</dd>
<dt>PURGE [ options ] [ filespec ]</dt>
<dd> Removes backup (*.~n~) files.</dd>
<dt>COPY [ options ] [ filespecs&#8230; ]</dt>
<dd> Copies files. Synonym: CP.</dd>
<dt>RENAME [ options ] [ filespecs&#8230; ]</dt>
<dd> Renames files. Synonym: MV.</dd>
<dt>CHMOD [ options ] [ filespecs&#8230; ]</dt>
<dd> Changes permissions of files.</dd>
<dt>TRANSLATE filename charsets [ filename ]</dt>
<dd> Converts file&#8217;s character set. Synonym: XLATE.</dd>
<dt>CD</dt>
<dd> Changes your working directory to your home directory.</dd>
<dt>CD directory</dt>
<dd> Changes your working directory to the one given.</dd>
<dt>CDUP</dt>
<dd> Changes your working directory one level up.</dd>
<dt>PWD</dt>
<dd> Displays your working directory.</dd>
<dt>BACK</dt>
<dd> Returns to your previous working directory.</dd>
<dt>MKDIR [ directory ]</dt>
<dd> Creates a directory.</dd>
<dt>RMDIR [ directory ]</dt>
<dd> Removes a directory.</dd></dl>
</dl>
<h3>Making Connections</h3>
<dl>
<dl>
<dt>SET LINE [ options ] devicename</dt>
<dd> Opens the named serial port. Synonym: SET PORT.</dd>
<dt>OPEN LINE [ options ] devicename</dt>
<dd> Same as SET LINE. Synonym: OPEN PORT.</dd>
<dt>SET MODEM TYPE [ name ]</dt>
<dd> Tells Kermit what kind of modem is on the port.</dd>
<dt>DIAL [ number ]</dt>
<dd> Tells Kermit to dial the given phone number with the modem.</dd>
<dt>REDIAL</dt>
<dd> Redials the most recently dialed phone number.</dd>
<dt>ANSWER</dt>
<dd> Waits for and answers an incoming call on the modem.</dd>
<dt>AUTHENTICATE [ parameters&#8230; ]</dt>
<dd> Performs secure authentication on a TCP/IP connection.</dd>
<dt>SET NETWORK TYPE { TCP/IP, X.25, &#8230; }</dt>
<dd> Selects network type for subsequent SET HOST commands.</dd>
<dt>SET HOST [ options ] host [ port ]</dt>
<dd> Opens a network connection to the given host and port.</dd>
<dt>SET HOST * port</dt>
<dd> Waits for an incoming TCP/IP connection on the given port.</dd>
<dt>TELNET [ options ] host</dt>
<dd> Opens a Telnet connection to the host and enters Connect state.</dd>
<dt>RLOGIN [ options ] host</dt>
<dd> Opens an Rlogin connection to the host and enters Connect state.</dd>
<dt>IKSD [ options ] host</dt>
<dd> Opens a connection to an Internet Kermit Service.</dd>
<dt>SSH [ options ] host</dt>
<dd> Opens an SSH connection to the host and enters Connect state.</dd>
<dt>FTP OPEN host [ options ]</dt>
<dd> Opens an FTP connection to the host.</dd>
<dt>HTTP [ options ] OPEN host</dt>
<dd> Opens an HTTP connection to the host.</dd>
<dt>PTY external-command</dt>
<dd> Runs the command on a pseudoterminal as if it were a connection.</dd>
<dt>PIPE external-command</dt>
<dd> Runs the command through a pipe as if it were a connection.</dd></dl>
</dl>
<h3>Using Connections</h3>
<dl>
<dl>
<dt>CONNECT [ options ]</dt>
<dd> Enters Connect (terminal) state. Synonym: C.</dd>
<dt>REDIRECT command</dt>
<dd> Redirects the given external command over the connection.</dd>
<dt>TELOPT command</dt>
<dd> Sends a Telnet protocol command (Telnet connections only).</dd>
<dt>Ctrl-\C</dt>
<dd> &quot;Escapes back&quot; from Connect state to Command state.</dd>
<dt>Ctrl-\B</dt>
<dd> (In Connect state) Sends a BREAK signal (serial or Telnet).</dd>
<dt>Ctrl-\!</dt>
<dd> (In Connect state) Enters inferior shell; &quot;exit&quot; to return.</dd>
<dt>Ctrl-\?</dt>
<dd> (In Connect state) Shows a menu of other escape-level options.</dd>
<dt>Ctrl-\Ctrl-\</dt>
<dd> (In Connect state) Type two Ctrl-Backslashes to send one of them.</dd>
<dt>SET ESCAPE [ character ]</dt>
<dd> Changes Kermit&#8217;s Connect-state escape character.</dd></dl>
</dl>
<h3>Closing Connections</h3>
<dl>
<dl>
<dt>HANGUP</dt>
<dd> Hangs up the currently open serial-port or network connection.</dd>
<dt>CLOSE</dt>
<dd> Closes the currently open serial-port or network connection.</dd>
<dt>SET LINE (with no devicename)</dt>
<dd> Closes the currently open serial-port or network connection.</dd>
<dt>SET HOST (with no hostname)</dt>
<dd> Closes the currently open serial-port or network connection.</dd>
<dt>FTP CLOSE</dt>
<dd> Closes the currently open FTP connection.</dd>
<dt>HTTP CLOSE</dt>
<dd> Closes the currently open HTTP connection.</dd>
<dt>EXIT</dt>
<dd> Also closes all connections. Synonym: QUIT.</dd>
<dt>SET EXIT WARNING OFF</dt>
<dd> Suppresses warning about open connections on exit or close.</dd></dl>
</dl>
<h3>File Transfer</h3>
<dl>
<dl>
<dt>SEND [ options ] filename [ as-name ]</dt>
<dd> Sends the given file. Synonym: S.</dd>
<dt>SEND [ options ] filespec</dt>
<dd> Sends all files that match.</dd>
<dt>RESEND [ options ] filespec</dt>
<dd> Resumes an interrupted SEND from the point of failure.</dd>
<dt>RECEIVE [ options ] [ as-name ]</dt>
<dd> Waits passively for files to arrive. Synonym: R.</dd>
<dt>LOG TRANSACTIONS [ filename ]</dt>
<dd> Keeps a record of file transfers.</dd>
<dt>FAST</dt>
<dd> Use fast file-transfer settings (default).</dd>
<dt>CAUTIOUS</dt>
<dd> Use cautious and less fast file-transfer settings.</dd>
<dt>ROBUST</dt>
<dd> Use ultra-conservative and slow file-transfer settings.</dd>
<dt>STATISTICS [ options ]</dt>
<dd> Gives statistics about the most recent file transfer.</dd>
<dt>WHERE</dt>
<dd> After transfer: &quot;Where did my files go?&quot;.</dd>
<dt>TRANSMIT [ options ] [ofilename ]</dt>
<dd> Sends file without protocol. Synonym: XMIT.</dd>
<dt>LOG SESSION [ filename ]</dt>
<dd> Captures remote text or files without protocol.</dd>
<dt>SET PROTOCOL [ name&#8230; ]</dt>
<dd> Tells Kermit to use an external file-transfer protocol.</dd>
<dt>FTP { PUT, MPUT, GET, MGET, &#8230; }</dt>
<dd> FTP client commands.</dd>
<dt>HTTP { PUT, GET, HEAD, POST, &#8230; }</dt>
<dd> HTTP client commands.</dd></dl>
</dl>
<h3>Kermit Server</h3>
<dl>
<dl>
<dt>ENABLE, DISABLE</dt>
<dd> Controls which server features can be used by clients.</dd>
<dt>SET SERVER</dt>
<dd> Sets parameters prior to entering Server state.</dd>
<dt>SERVER</dt>
<dd> Enters Server state.</dd></dl>
</dl>
<h3>Client of Kermit or FTP Server</h3>
<dl>
<dl>
<dt>[ REMOTE ] LOGIN [ user password ]</dt>
<dd> Logs in to a Kermit server or IKSD that requires it.</dd>
<dt>[ REMOTE ] LOGOUT</dt>
<dd> Logs out from a Kermit server or IKSD.</dd>
<dt>SEND [ options ] filename [ as-name ]</dt>
<dd> Sends the given file to the server. Synonyms: S, PUT.</dd>
<dt>SEND [ options ] filespec</dt>
<dd> Sends all files that match.</dd>
<dt>RESEND [ options ] filespec</dt>
<dd> Resumes an interrupted SEND from the point of failure.</dd>
<dt>GET [ options ] remote-filespec</dt>
<dd> Asks the server to send the given files. Synonym: G.</dd>
<dt>REGET [ options ] remote-filespec</dt>
<dd> Resumes an interrupted GET from the point of failure.</dd>
<dt>REMOTE CD [ directory ]</dt>
<dd> Asks server to change its working directory. Synonym: RCD.</dd>
<dt>REMOTE PWD [ directory ]</dt>
<dd> Asks server to display its working directory. Synonym: RPWD.</dd>
<dt>REMOTE DIRECTORY [ filespec&#8230; ]</dt>
<dd> Asks server to send a directory listing. Synonym: RDIR.</dd>
<dt>REMOTE DELETE [ filespec&#8230; ]</dt>
<dd> Asks server to delete files. Synonym: RDEL.</dd>
<dt>REMOTE [ command&#8230; ]</dt>
<dd> (Many other commands: &quot;remote ?&quot; for a list).</dd>
<dt>MAIL [ options ] filespec</dt>
<dd> Sends file(s) to be delivered as e-mail (Kermit only).</dd>
<dt>FINISH</dt>
<dd> Asks the server to exit server state (Kermit only).</dd>
<dt>BYE</dt>
<dd> Asks the server to log out and close the connection.</dd></dl>
</dl>
<h3>Script Programming</h3>
<dl>
<dt>
</dt><dd> DEFINE, DECLARE, UNDEFINE, UNDECLARE, ASSIGN, EVALUATE, SEXPRESSION, ARRAY, SORT, INPUT, OUTPUT, IF, FOR, WHILE, SWITCH, GOTO, ECHO, ASK, GETC, GETOK, ASSERT, WAIT, SLEEP, FOPEN, FREAD, FWRITE, FCLOSE, STOP, END, RETURN, LEARN, SHIFT, TRACE, VOID, INCREMENT, DECREMENT, &#8230; For these and many more you&#8217;ll need to consult the manual and supplements, and/or visit the Kermit Script Library, which also includes a brief tutorial. Hint: HELP LEARN to find out how to get Kermit to write simple scripts for you.</dd></dl>
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
<dt>Command state</dt>
<dd> In this state, Kermit reads commands from: </dd>
<p> &bull;<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>Your keyboard; or:</p>
<p> &bull;<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>A file, or:</p>
<p> &bull;<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>A macro definition.</p>
<p> You can exit from Command state back to Unix with the EXIT or QUIT command (same thing). You can enter Connect state with any of various commands (CONNECT, DIAL, TELNET, etc). You can enter file transfer state with commands like SEND, RECEIVE, and GET. You can enter Server state with the SERVER command. The TAKE command tells Kermit to read and execute commands from a file. The (perhaps implied) DO command tells Kermit to read and execute commands from a macro definition. While in Command state, you can interrupt any command, macro, or command file by typing Ctrl-C (hold down the Ctrl key and press the C key); this normally brings you back to the prompt.</p>
<dt>Shell state</dt>
<dd> You can invoke an inferior shell or external command from the Kermit command prompt by using the PUSH, RUN (!), EDIT, or BROWSE command. While the inferior shell or command is active, Kermit is suspended and does nothing. Return to Kermit Command state by exiting from the inferior shell or application.</dd>
<dt>Connect state</dt>
<dd> In this state, which can be entered only when in Local mode (i.e. when Kermit has made a connection to another computer), Kermit is acting as a terminal to the remote computer. Your keystrokes are sent to the remote computer and characters that arrive over the communication connection are displayed on your screen. This state is entered when you give a CONNECT, DIAL, TELNET, RLOGIN, or IKSD command. You can return to command state by logging out of the remote computer, or by typing: </dd>
<p>&nbsp;<wbr>&nbsp;<wbr>Ctrl-\c </p>
<p> That is: Hold down the Ctrl key and press the backslash key, then let go of the Ctrl key and press the C key. This is called escaping back. Certain other escape-level commands are also provided; type Ctrl-\? for a list. For example, you can enter Shell state with: </p>
<p> <br />
&nbsp;<wbr>&nbsp;<wbr>Ctrl-\! </p>
<p> To send a Ctrl-\ to the host while in Connect state, type two of them in a row. See HELP CONNECT and HELP SET ESCAPE for more info. </p>
<dt>Local file-transfer state</dt>
<dd> <p> In this state, Kermit is sending packets back and forth with the other computer in order to transfer a file or accomplish some other file-related task. And at the same time, it is displaying its progress on your screen and watching your keyboard for interruptions. In this state, the following single-keystroke commands are accepted: </p>
 </dd>
<dl>
<dd>  </dd>
<dl>
<dt>X</dt>
<dd> <p> Interrupt the current file and go on to the next (if any). </p>
 </dd>
<dt>Z</dt>
<dd> <p> Interrupt the current file and skip all the rest. </p>
 </dd>
<dt>E</dt>
<dd> <p> Like Z but uses a &quot;stronger&quot; protocol (use if X or Z don&#8217;t work). </p>
 </dd>
<dt>Ctrl-C</dt>
<dd> <p> Interrupt file-transfer mode (use if Z or E don&#8217;t work). </p>
 </dd></dl>
</dl>
<p> Kermit returns to its previous state (Command or Connect) when the transfer is complete or when interrupted successfully by X, Z, E, or Ctrl-C (hold down the Ctrl key and press the C key). </p>
<dt>Remote file-transfer state</dt>
<dd> <p> In this state, Kermit is exchanging file-transfer packets with its local partner over its standard i/o. It leaves this state automatically when the transfer is complete. In case you find your local Kermit in Connect state and the remote one in File-transfer state (in which it seems to ignore your keystrokes), you can usually return it to command state by typing three Ctrl-C&#8217;s in a row. If that doesn&#8217;t work, return your local Kermit to Command state (Ctrl-\ C) and type &quot;e-packet&quot; and then press the Return or Enter key; this forces a fatal Kermit protocol error. </p>
 </dd>
<dt>Remote Server state</dt>
<dd> <p> This is like Remote File-transfer state, except it never returns automatically to Command state. Rather, it awaits further instructions from the client program; that is, from your Local Kermit program. You can return the Remote Server to its previous state by issuing a &quot;finish&quot; command to the client, or if you are in Connect state, by typing three Ctrl-C&#8217;s in a row. You can tell the server job to log out and break the connection by issuing a &quot;bye&quot; command to the client. </p>
 </dd>
<dt>Local Server state</dt>
<dd> <p> Like Remote-Server state, but in local mode, and therefore with its file-transfer display showing, and listening for single-key commands, as in Local File-transfer state. Usually this state is entered automatically when a remote Kermit program gives a GET command. </p>
<p> C-Kermit, Kermit 95, and MS-DOS Kermit all can switch automatically from Connect state to Local File-transfer state when you initiate a file transfer from the remote computer by starting Kermit and telling it to send or get a file, in which case, Connect state is automatically resumed after the file transfer is finished. </p>
<p> Note that C-Kermit is not a terminal emulator. It is a communications application that you run in a terminal window (e.g. console or Xterm). The specific emulation, such as VT100, VT220, Linux Console, or Xterm, is provided by the terminal window in which you are running C-Kermit. Kermit 95 and MS-DOS Kermit, on the other hand, are true terminal emulators. Why is C-Kermit not a terminal emulator? CLICK HERE to read about it. </p>
 </dd></dl>
<h2>MAKING CONNECTIONS</h2>
<p> Here is how to make different kinds of connections using interactive Kermit commands (as noted above, you can also make connections with command-line options). Note that you don&#8217;t have to make connections with Kermit. It can also be used on the far end of a connection as the remote file transfer and management partner of your local communications software. </p>
<dl>
<dt>Making a Telnet Connection</dt>
<dd> <p> At the C-Kermit command prompt, simply type: </p>
<pre><code>  telnet foo.bar.com
</code></pre>
<p> (substituting desired hostname or address). You can also include a port number: </p>
<pre><code>  telnet xyzcorp.com 3000 ;
</code></pre>
<p> If the connection is successful, Kermit automically enters Connect state. When you logout from the remote host, Kermit automatically returns to its prompt. More info: HELP TELNET, HELP SET TELNET, HELP SET TELOPT. Also see the IKSD section below. </p>
 </dd>
<dt>Making an Rlogin connection</dt>
<dd> <p> This is just like Telnet, except you have to be root to do it because Rlogin uses a privileged TCP port: </p>
<pre><code>  rlogin foo.bar.com
</code></pre>
<p> More info: HELP RLOGIN. </p>
 </dd>
<dt>Making an SSH Connection</dt>
<dd> <p> Unlike Telnet and Rlogin, SSH connections are not built-in, but handled by running your external SSH client through a pseudoterminal. Using C-Kermit to control the SSH client gives you all of Kermit&#8217;s features (file transfer, character-set conversion, scripting, etc) over SSH. </p>
<p> <br />
&nbsp;<wbr>&nbsp;<wbr>ssh foo.bar.com </p>
<p> More info: HELP SSH, HELP SET SSH. </p>
 </dd>
<dt>Dialing with a Modem</dt>
<dd> <p> If it&#8217;s an external modem, make sure it is connected to a usable serial port on your computer with a regular (straight-through) modem cable, and to the telephone jack with a telephone cable, and that it&#8217;s turned on. Then use these commands: </p>
<pre><code>  set modem type usrobotics ; Or other supported type
  set line /dev/ttyS0 ; Specify device name
  set speed 57600 ; Or other desired speed
  set flow rts/cts ; Most modern modems support this
  set dial method tone ; (or pulse)
  dial 7654321 ; Dial the desired number
</code></pre>
<p> Type &quot;set modem type ?&quot; for a list of supported modem types. If you omit the SET MODEM TYPE command, the default type is &quot;generic-high-speed&quot;, which should work for most modern AT-command-set modems. If the line is busy, Kermit redials automatically. If the call does not succeed, use &quot;set dial display on&quot; and try it again to watch what happens. If the call succeeds, Kermit enters Connect state automatically and returns to its prompt automatically when you log out from the remote computer or the connection is otherwise lost. </p>
<p> You can also dial from a modem that is accessible by Telnet, e.g. to a reverse terminal server. In this case the command sequence is: </p>
<pre><code>  set host ts.xxx.com 2000 ; Terminal-server and port
  set modem type usrobotics ; Or other supported type
  set dial method tone ; (or pulse)
  dial 7654321 ; Dial the desired number
</code></pre>
<p> If the terminal server supports the Telnet Com Port Option, RFC 2217, you can also give serial-port related commands such as SET SPEED, SET PARITY, and so on, and Kermit relays them to the terminal server using the protocol specified in the RFC. </p>
<p> More info: HELP SET MODEM, HELP SET LINE, HELP SET SPEED, HELP SET FLOW, HELP DIAL, HELP SET DIAL, HELP SET MODEM, HELP SET CARRIER-WATCH, SHOW COMMUNICATIONS, SHOW MODEM, SHOW DIAL. </p>
 </dd>
<dt>Direct Serial Port</dt>
<dd> <p> Connect the two computers, A and B, with a null modem cable (or two modem cables interconnected with a null-modem adapter or modem eliminator). From Computer A: </p>
<pre><code>  set modem type none ; There is no modem
  set line /dev/ttyS0 ; Specify device name
  set carrier-watch off ; If DTR CD are not cross-connected
  set speed 57600 ; Or other desired speed
  set flow rts/cts ; If RTS and CTS are cross-connected
  set parity even ; (or &quot;mark&quot; or &quot;space&quot;, if necessary)
  set stop-bits 2 ; (rarely necessary)
  set flow xon/xoff ; If you can't use RTS/CTS
  connect ; Enter Connect (terminal) state
</code></pre>
<p> This assumes Computer B is set up to let you log in. If it isn&#8217;t, you can run a copy of Kermit on Computer B and follow approximately the same directions. More info: As above plus HELP CONNECT. </p>
 </dd></dl>
<p> With modems or direct serial connections, you might also have to &quot;set parity even&quot; (or &quot;mark&quot; or &quot;space&quot;) if it&#8217;s a 7-bit connection. </p>
<p> Of the connection types listed above, only one can be open at a time. However, any one of these can be open concurrently with an FTP or HTTP session. Each connection type can be customized to any desired degree, scripted, logged, you name it. See the manual. </p>
<p> NOTE: On selected platforms, C-Kermit also can make X.25 connections. See the manual for details.  </p>
<h2>TRANSFERRING FILES WITH KERMIT</h2>
<p> There is a widespread and persistent belief that Kermit is a slow protocol. This is because, until recently, it used conservative tuning by default to make sure file transfers succeeded, rather than failing because they overloaded the connection. Some extra commands (or command-line options, like -Q) were needed to make it go fast, but nobody bothered to find out about them. Also, it takes two to tango: most non-Kermit-Project Kermit protocol implementations really ARE slow. The best file-transfer partners for C-Kermit are: another copy of C-Kermit (7.0 or later) and Kermit 95. These combinations work well and they work fast by default. MS-DOS Kermit is good too, but you have to tell it to go fast (by giving it the FAST command). </p>
<p> Furthermore, all three of these Kermit programs support &quot;autodownload&quot; and &quot;autoupload&quot;, meaning that when they are in Connect state and a Kermit packet comes in from the remote, they automatically switch into file transfer mode. </p>
<p> And plus, C-Kermit and K95 also switch automatically between text and binary mode for each file, so there is no need to &quot;set file type binary&quot; or &quot;set file type text&quot;, or to worry about files being corrupted because they were transferred in the wrong mode. </p>
<p> What all of these words add up to is that now, when you use up-to-date Kermit software from the Kermit Project, file transfer is not only fast, it&#8217;s ridiculously easy. You barely have to give any commands at all. </p>
<dl>
<dt>Downloading Files</dt>
<dd> <p> Let&#8217;s say you have Kermit 95, C-Kermit, or MS-DOS Kermit on your desktop computer, with a connection to a Unix computer that has C-Kermit installed as &quot;kermit&quot;. To download a file (send it from Unix to your desktop computer), just type the following command at your Unix shell prompt: </p>
<p> <br />
&nbsp;<wbr>&nbsp;<wbr>kermit -s oofa.txt </p>
<p> (where oofa.txt is the filename). If you want to send more than one file, you can put as many filenames as you want on the command line, and they can be any combination of text and binary: </p>
<p> <br />
&nbsp;<wbr>&nbsp;<wbr>kermit -s oofa.txt oofa.zip oofa.html oofa.tar.gz </p>
<p> and/or you can use wildcards to send groups of files: </p>
<p> <br />
&nbsp;<wbr>&nbsp;<wbr>kermit -s oofa.* </p>
<p> If you want to send a file under an assumed name, use: </p>
<p> <br />
&nbsp;<wbr>&nbsp;<wbr>kermit -s friday.txt -a today.txt </p>
<p> This sends the file friday.txt but tells the receiving Kermit that its name is today.txt. In all cases, as noted, when the file transfer is finished, your desktop Kermit returns automatically to Connect state. No worries about escaping back, re-connecting, text/binary mode switching. Almost too easy, right? </p>
 </dd>
<dt>Uploading Files</dt>
<dd> <p> To upload files (send them from your desktop computer to the remote Unix computer) do the same thing, but use the -g (GET) option instead of -s: </p>
<p> <br />
&nbsp;<wbr>&nbsp;<wbr>kermit -g oofa.txt </p>
<p> This causes your local Kermit to enter server mode; then the remote Kermit program requests the named file and the local Kermit sends it and returns automatically to Connect state when done. </p>
<p> If you want to upload multiple files, you have have use shell quoting rules, since these aren&#8217;t local files: </p>
<pre><code>  kermit -g &quot;oofa.txt oofa.zip oofa.html oofa.tar.gz&quot;
  kermit -g &quot;oofa.*&quot;
</code></pre>
<p> If you want to upload a file but store it under a different name, use: </p>
<p> <br />
&nbsp;<wbr>&nbsp;<wbr>kermit -g friday.txt -a today.txt </p>
 </dd>
<dt>Kermit Transfers the Old-Fashioned Way</dt>
<dd> <p> If your desktop communications software does not support autoupload or autodownload, or it does not include Kermit server mode, the procedure requires more steps. </p>
<p> To download a file, type: </p>
<p> <br />
&nbsp;<wbr>&nbsp;<wbr>kermit -s filename </p>
<p> on the host as before, but if nothing happens automatically in response to this command, you have to switch your desktop communications software into Kermit Receive state. This might be done by escaping back using keyboard characters or hot keys (Alt-x is typical) and/or with a command (like RECEIVE) or a menu. When the file transfer is complete, you have to go back to Connect state, Terminal emulation, or whatever terminology applies to your desktop communications software. </p>
<p> To upload a file, type: </p>
<p> <br />
&nbsp;<wbr>&nbsp;<wbr>kermit -r </p>
<p> on the host (rather than &quot;kermit -g&quot;). This tells C-Kermit to wait passively for a file to start arriving. Then regain the attention of your desktop software (Alt-x or whatever) and instruct it to send the desired file(s) with Kermit protocol. When the transfer is finished, return to the Connect or Terminal screen. </p>
 </dd>
<dt>If File Transfer Fails</dt>
<dd> <p> Although every aspect of Kermit&#8217;s operation can be finely tuned, there are also three short and simple &quot;omnibus tuning&quot; commands you can use for troubleshooting: </p>
 </dd>
<dl>
<dd>  </dd>
<dl>
<dt>FAST</dt>
<dd> <p> Use fast file-transfer settings. This has been the default since C-Kermit 7.0 now that most modern computers and connections support it. If transfers fail with fast settings, try . . . </p>
 </dd>
<dt>CAUTIOUS</dt>
<dd> <p> Use cautious but not paranoid settings. File transfers, if they work, will go at medium speed. If not, try . . . </p>
 </dd>
<dt>ROBUST</dt>
<dd> <p> Use the most robust, resilient, conservative, safe, and reliable settings. File transfers will almost certainly work, but they will be quite slow (of course this is a classic tradeoff; ROBUST was C-Kermit&#8217;s default tuning in versions 6.0 and earlier, which made everybody think Kermit protocol was slow). If ROBUST doesn&#8217;t do the trick, try again with SET PARITY SPACE first in case it&#8217;s not an 8-bit connection. </p>
 </dd></dl>
</dl>
<p> Obviously the success and performance of a file transfer also depends on C-Kermit&#8217;s file transfer partner. Up-to-date, real Kermit Project partners are recommended because they contain the best Kermit protocol implementations and because we can support them in case of trouble. </p>
<p> If you still have trouble, consult Chapter 10 of Using C-Kermit, or send email to kermit-support [at] columbia.edu. </p>
<dt>Advanced Kermit File-Transfer Features</dt>
<dd> <p> Obviously there is a lot more to Kermit file transfer, including all sorts of interactive commands, preferences, options, logging, debugging, troubleshooting, and anything else you can imagine but that&#8217;s what the manual and updates are for. Here are a few topics you can explore if you&#8217;re interested by Typing HELP for the listed commands: </p>
 </dd>
<dl>
<dd>  </dd>
<dl>
<dt>Logging transfers:</dt>
<dd> <p> LOG TRANSACTIONS (HELP LOG) </p>
 </dd>
<dt>Automatic per-file text/binary mode switching:</dt>
<dd> <p> SET TRANSFER MODE { AUTOMATIC, MANUAL } (HELP SET TRANSFER). </p>
 </dd>
<dt>Cross-platform recursive directory tree transfer:</dt>
<dd> <p> SEND /RECURSIVE, GET /RECURSIVE (HELP SEND, HELP GET). </p>
 </dd>
<dt>File collision options:</dt>
<dd> <p> SET FILE COLLISION { OVERWRITE, BACKUP, DISCARD, ... } (HELP SET FILE). </p>
 </dd>
<dt>Update: Transfer only files that changed since last time:</dt>
<dd> <p> SET FILE COLLISION UPDATE (HELP SET FILE). </p>
 </dd>
<dt>Filename selection patterns:</dt>
<dd> <p> (HELP WILDCARD). </p>
 </dd>
<dt>Flexible file selection:</dt>
<dd> <p> SEND (or GET) /BEFORE /AFTER /LARGER /SMALLER /TYPE /EXCEPT, ... </p>
 </dd>
<dt>Character-set conversion:</dt>
<dd> <p> SET { FILE, TRANSFER } CHARACTER-SET, ASSOCIATE, ... </p>
 </dd>
<dt>File/Pathname control:</dt>
<dd> <p> SET { SEND, RECEIVE } PATHNAMES, SET FILE NAMES. </p>
 </dd>
<dt>Atomic file movement:</dt>
<dd> <p> SEND (or GET) /DELETE /RENAME /MOVE-TO </p>
 </dd>
<dt>Transferring to/from standard i/o of other commands:</dt>
<dd> <p> SEND (or GET) /COMMAND </p>
 </dd>
<dt>Recovery of interrupted transfer from point of failure:</dt>
<dd> <p> RESEND, REGET (HELP RESEND, HELP REGET). </p>
 </dd></dl>
</dl>
<dt>Non-Kermit File Transfer</dt>
<dd> <p> You can also use C-Kermit to transfer files with FTP or HTTP Internet protocols; see below. </p>
<p> On a regular serial or Telnet connection where the other computer doesn&#8217;t support Kermit protocol at all, you have several options. For example, if your desktop communications software supports Zmodem, use &quot;rz&quot; and &quot;sz&quot; on the host rather than Kermit. But if Kermit is your desktop software, and you are using it to make calls or network connections to other computers that don&#8217;t support Kermit protocol (or that don&#8217;t have a good implementation of it), then if your computer also has external X, Y, or Zmodem programs that are redirectable, Kermit can use them as external protocols. HELP SET PROTOCOL for details. </p>
<p> You can also capture &quot;raw&quot; data streams from the other computer with LOG SESSION (HELP LOG and HELP SET SESSION-LOG for details), and you can upload files without any protocol at all with TRANSMIT (HELP TRANSMIT, HELP SET TRANSMIT). </p>
 </dd></dl>
<h2>KERMIT'S BUILT-IN FTP AND HTTP CLIENTS</h2>
<p> Kermit&#8217;s FTP client is like the regular Unix FTP client that you&#8217;re used to, but with some differences: </p>
<dl>
<dt>&bull;</dt>
<dd> <p> It has lots more commands and features. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Each FTP command must be prefixed with &quot;ftp&quot;, for example &quot;ftp open&quot;, &quot;ftp get&quot;, &quot;ftp bye&quot;, etc (this is not strictly true, but until you&#8217;re more familiar with it, it&#8217;s best to follow this rule). </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Commands like &quot;cd&quot;, &quot;directory&quot;, etc, execute locally, not on the server. Use &quot;ftp cd&quot;, &quot;ftp dir&quot;, etc, to have them act on the server. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> You can have an FTP session and a regular Kermit serial or Telnet session open at the same time. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> FTP sessions can be fully automated. </p>
 </dd></dl>
<p> Pending publication of the next edition of the manual, the Kermit FTP client is thoroughly documented at the Kermit Project website: </p>
<p> <br />
&nbsp;<wbr>&nbsp;<wbr><a rel="nofollow" href="http://www.columbia.edu/kermit/ftpclient.html">http://www.columbia.edu/kermit/ftpclient.html</a> </p>
<p> You also can use HELP FTP and HELP SET FTP to get descriptions of Kermit&#8217;s FTP-related commands. </p>
<p> The HTTP client is similar to the FTP one, except you prefix each command with HTTP instead of FTP: HTTP OPEN, HTTP GET, HTTP PUT, HTTP CLOSE, etc. Type HELP HTTP for details, or visit the to view the manual supplements. HTTP connections can be open at the same time as regular serial or Telnet connections and FTP connections. So Kermit can manage up to three types connections simultaneously.  </p>
<h2>INTERNET KERMIT SERVICE</h2>
<p> C-Kermit can be configured and run as an Internet service (called IKSD), similar to an FTP server (FTPD) except you can (but need not) interact with it directly, plus it does a lot more than an FTP server can do. The TCP port for IKSD is 1649. It uses Telnet protocol. C-Kermit can be an Internet Kermit Server, or it can be a client of an IKSD. You can make connections from C-Kermit to an IKSD with any of the following commands: </p>
<pre><code>  telnet foo.bar.edu 1649
  telnet foo.bar.edu kermit ; if &quot;kermit&quot; is listed in /etc/services
  iksd foo.bar.edu
</code></pre>
<p> The IKSD command is equivalent to a TELNET command specifying port 1649. For more information about making and using connections to an IKSD, see: </p>
<p> <br />
&nbsp;<wbr>&nbsp;<wbr><a rel="nofollow" href="http://www.columbia.edu/kermit/cuiksd.html">http://www.columbia.edu/kermit/cuiksd.html</a> </p>
<p> You can run an Internet Kermit Service on your own computer too (if you are the system administrator). For instructions, see: </p>
<p> <br />
&nbsp;<wbr>&nbsp;<wbr><a rel="nofollow" href="http://www.columbia.edu/kermit/iksd.html">http://www.columbia.edu/kermit/iksd.html</a>  </p>
<h2>SECURITY</h2>
<p> All of C-Kermit&#8217;s built-in TCP/IP networking methods (Telnet, Rlogin, IKSD, FTP, and HTTP) can be secured by one or more of the following IETF-approved methods: </p>
<p> &bull;<code>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></code>MIT Kerberos IV<br />
 <br />
 &bull;<code>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></code>MIT Kerberos V<br />
 <br />
 &bull;<code>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></code>SSL/TLS<br />
 <br />
 &bull;<code>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></code>Stanford SRP<br />
 </p>
<p> For complete instructions see: </p>
<p> <br />
&nbsp;<wbr>&nbsp;<wbr><a rel="nofollow" href="http://www.columbia.edu/kermit/security.html">http://www.columbia.edu/kermit/security.html</a> </p>
<p> And as noted previously, you can also make SSH connections with C-Kermit if you already have an SSH client installed.  </p>
<h2>ALTERNATIVE COMMAND-LINE PERSONALITIES</h2>
<p> When invoked as &quot;kermit&quot; or any other name besides &quot;ftp&quot; or &quot;telnet&quot;, C-Kermit has the command-line options described above in the OPTIONS section. However, if you invoke C-Kermit as &quot;telnet&quot; or &quot;ftp&quot;, it changes its command-line personality to match. This can be done (among other ways) with symbolic links (symlinks). For example, if you want C-Kermit to be your regular Telnet client, or the Telnet helper of your Web browser, you can create a link like the following in a directory that lies in your PATH ahead of the regular telnet program: </p>
<p> <br />
&nbsp;<wbr>&nbsp;<wbr>ln -s&nbsp;<wbr>/usr/local/bin/kermit telnet </p>
<p> Now when you give a &quot;telnet&quot; command, you are invoking Kermit instead, but with its Telnet command-line personality so, for example: </p>
<p> <br />
&nbsp;<wbr>&nbsp;<wbr>telnet xyzcorp.com </p>
<p> Makes a Telnet connection to xyzcorp.com, and Kermit exits automatically when the connection is closed (just like the regular Telnet client). Type &quot;telnet -h&quot; to get a list of Kermit&#8217;s Telnet-personality command-line options, which are intended to be as compatible as possible with the regular Telnet client. </p>
<p> Similarly for FTP: </p>
<p> <br />
&nbsp;<wbr>&nbsp;<wbr>ln -s&nbsp;<wbr>/usr/local/bin/kermit ftp </p>
<p> And now type &quot;ftp -h&quot; to see its command-line options, and command lines just like you would give your regular FTP client: </p>
<p> <br />
&nbsp;<wbr>&nbsp;<wbr>ftp xyzcorp.com </p>
<p> but with additional options allowing an entire session to be specified on the command line. Finally, if Kermit&#8217;s first command-line option is a Telnet, FTP, IKSD, or HTTP URL, Kermit automatically makes the appropriate kind of connection and, if indicated by the URL, takes the desired action: </p>
<dl>
<dt>kermit telnet:xyzcorp.com</dt>
<dd> <p> Opens a Telnet session </p>
 </dd>
<dt>kermit <a href="telnet://olga@xyzcorp.com">telnet://olga@xyzcorp.com</a></dt>
<dd> <p> Ditto for user olga </p>
 </dd>
<dt>kermit <a href="ftp://olga@xyzcorp.com/public/oofa.zip">ftp://olga@xyzcorp.com/public/oofa.zip</a></dt>
<dd> <p> Downloads a file </p>
 </dd>
<dt>kermit <a href="kermit://kermit.columbia.edu/kermit/f/READ.ME">kermit://kermit.columbia.edu/kermit/f/READ.ME</a></dt>
<dd> <p> Ditto for IKSD </p>
 </dd>
<dt>kermit <a href="iksd://kermit.columbia.edu/kermit/f/READ.ME">iksd://kermit.columbia.edu/kermit/f/READ.ME</a></dt>
<dd> <p> (This works too) </p>
 </dd>
<dt>kermit <a rel="nofollow" href="http://www.columbia.edu/kermit/index.html">http://www.columbia.edu/kermit/index.html</a></dt>
<dd> <p> Grabs a web page </p>
 </dd></dl>
<h2>LICENSE</h2>
<p> C-Kermit has an unusual license, but a fair and sensible one since the Kermit Project must support itself out of revenue: it&#8217;s not a BSD license, not GPL, not Artistic, not commercial, not shareware, not freeware. It can be summed up like this: if you want C-Kermit for your own use, you can download and use it without cost or license (but we&#8217;d appreciate it if you would purchase the manual). But if you want to sell C-Kermit or bundle it with a product or otherwise distribute it in a commercial setting EXCEPT WITH AN OPEN-SOURCE OPERATING SYSTEM DISTRIBUTION such as Linux, FreeBSD, NetBSD, or OpenBSD, you must license it. To see the complete license, give the LICENSE command at the prompt, or see the COPYING.TXT file distributed with C-Kermit 7.0 or later, or download it from </p>
<p> <br />
&nbsp;<wbr>&nbsp;<wbr><a href="ftp://kermit.columbia.edu/kermit/c-kermit/COPYING.TXT">ftp://kermit.columbia.edu/kermit/c-kermit/COPYING.TXT</a> </p>
<p> Send licensing inquiries to kermit [at] columbia.edu.  </p>
<h2>BUGS</h2>
<p> See the following files for listings of known bugs, limitations, workarounds, hints and tips: </p>
<dl>
<dt>ckcbwr.txt</dt>
<dd> <p> General C-Kermit bugs, hints, tips. </p>
 </dd>
<dt>ckubwr.txt</dt>
<dd> <p> Unix-specific C-Kermit bugs, hints, tips. </p>
 </dd></dl>
<p> Report bugs and problems by email to: </p>
<p> <br />
kermit-support [at] columbia.edu. </p>
<p> Before requesting technical support, please read the hints here: </p>
<p> <br />
&nbsp;<wbr>&nbsp;<wbr><a rel="nofollow" href="http://www.columbia.edu/kermit/support.html">http://www.columbia.edu/kermit/support.html</a> </p>
<p> and also read the C-Kermit Frequently Asked Questions: </p>
<p> <br />
&nbsp;<wbr>&nbsp;<wbr><a rel="nofollow" href="http://www.columbia.edu/kermit/ckfaq.html">http://www.columbia.edu/kermit/ckfaq.html</a>  </p>
<h2>OTHER TOPICS</h2>
<p> There&#8217;s way more to C-Kermit than we&#8217;ve touched on here -- troubleshooting, customization, character sets, dialing directories, sending pages, script writing, and on and on, all of which are covered in the manual and updates and supplements. For the most up-to-date information on documentation (or updated documentation itself) visit the Kermit Project website: </p>
<p> <br />
&nbsp;<wbr>&nbsp;<wbr><a rel="nofollow" href="http://www.columbia.edu/kermit/">http://www.columbia.edu/kermit/</a> </p>
<p> There you will also find Kermit software packages for other platforms: different Unix varieties, Windows, DOS, VMS, IBM mainframes, and many others: 20+ years&#8217; worth.  </p>
<h2>DOCUMENTATION AND UPDATES</h2>
<p> The manual for C-Kermit is: </p>
<dl>
<dt><i>Using C-Kermit</i></dt>
<dd> <p> Frank da Cruz and Christine M. Gianone, Second Edition, Digital Press / Butterworth-Heinemann, Woburn, MA, 1997, 622 pages, ISBN 1-55558-164-1. This is a printed book. It covers C-Kermit 6.0. </p>
 </dd>
<dt>The C-Kermit 7.0 Supplement</dt>
<dd> <p> <a rel="nofollow" href="http://www.columbia.edu/kermit/ckermit70.html">http://www.columbia.edu/kermit/ckermit70.html</a> </p>
 </dd>
<dt>The C-Kermit 8.0 Supplement</dt>
<dd> <p> <a rel="nofollow" href="http://www.columbia.edu/kermit/ckermit80.html">http://www.columbia.edu/kermit/ckermit80.html</a> </p>
 </dd>
<dt>The C-Kermit 9.0 Supplement</dt>
<dd> <p> <a rel="nofollow" href="http://www.columbia.edu/kermit/ckermit90.html">http://www.columbia.edu/kermit/ckermit90.html</a> </p>
 </dd></dl>
<p> Visit C-Kermit home page: </p>
<p> <br />
&nbsp;<wbr>&nbsp;<wbr><a rel="nofollow" href="http://www.columbia.edu/kermit/ckermit.html">http://www.columbia.edu/kermit/ckermit.html</a> </p>
<p> to learn about new versions, Beta tests, and other news; to read case studies and tutorials; to download source code, install packages, and prebuilt binaries for many platforms. Also visit: </p>
<dl>
<dt><a rel="nofollow" href="http://www.columbia.edu/kermit/scriptlib.html">http://www.columbia.edu/kermit/scriptlib.html</a></dt>
<dd> <p> The Kermit script library and tutorial </p>
 </dd>
<dt><a rel="nofollow" href="http://www.columbia.edu/kermit/newfaq.html">http://www.columbia.edu/kermit/newfaq.html</a></dt>
<dd> <p> The Kermit FAQ (Frequently Asked Questions about Kermit) </p>
 </dd>
<dt><a rel="nofollow" href="http://www.columbia.edu/kermit/ckfaq.html">http://www.columbia.edu/kermit/ckfaq.html</a></dt>
<dd> <p> The C-Kermit FAQ (Frequently Asked Questions about C-Kermit) </p>
 </dd>
<dt><a rel="nofollow" href="http://www.columbia.edu/kermit/telnet.html">http://www.columbia.edu/kermit/telnet.html</a></dt>
<dd> <p> C-Kermit Telnet client documentation </p>
 </dd>
<dt><a rel="nofollow" href="http://www.columbia.edu/kermit/security.html">http://www.columbia.edu/kermit/security.html</a></dt>
<dd> <p> C-Kermit security documentation (Kerberos, SSL/TLS, etc) </p>
 </dd>
<dt><a rel="nofollow" href="http://www.columbia.edu/kermit/cuiksd.html">http://www.columbia.edu/kermit/cuiksd.html</a></dt>
<dd> <p> Internet Kermit Service user documentation </p>
 </dd>
<dt><a rel="nofollow" href="http://www.columbia.edu/kermit/iksd.html">http://www.columbia.edu/kermit/iksd.html</a></dt>
<dd> <p> Internet Kermit Service administrator documentation </p>
 </dd>
<dt><a rel="nofollow" href="http://www.columbia.edu/kermit/studies.html">http://www.columbia.edu/kermit/studies.html</a></dt>
<dd> <p> Case studies. </p>
 </dd>
<dt><a rel="nofollow" href="http://www.columbia.edu/kermit/support.html">http://www.columbia.edu/kermit/support.html</a></dt>
<dd> <p> Technical support. </p>
 </dd>
<dt><a rel="nofollow" href="http://www.columbia.edu/kermit/k95tutorial.html">http://www.columbia.edu/kermit/k95tutorial.html</a></dt>
<dd> <p> Kermit 95 tutorial. </p>
 </dd>
<dt>comp.protocols.kermit.misc</dt>
<dd> <p> The Kermit newsgroup (unmoderated). </p>
 </dd></dl>
<h2>FILES</h2>
<dl>
<dt>COPYING.TXT</dt>
<dd> <p> C-Kermit license. </p>
 </dd>
<dt>~/.kermrc</dt>
<dd> <p> Initialization file. </p>
 </dd>
<dt>~/.mykermrc</dt>
<dd> <p> Customization file. </p>
 </dd>
<dt>~/.kdd</dt>
<dd> <p> Kermit dialing directory (see manual). </p>
 </dd>
<dt>~/.knd</dt>
<dd> <p> Kermit network directory (see manual). </p>
 </dd>
<dt>~/.ksd</dt>
<dd> <p> Kermit services directory (see manual). </p>
 </dd>
<dt>ca_certs.pem</dt>
<dd> <p> Certificate Authority certifcates used for SSL connections. </p>
 </dd>
<dt>ckuins.txt</dt>
<dd> <p> Installation instructions for Unix. Also at <a rel="nofollow" href="http://www.columbia.edu/kermit/ckuins.html.">http://www.columbia.edu/kermit/ckuins.html.</a> </p>
 </dd>
<dt>ckcbwr.txt</dt>
<dd> <p> General C-Kermit bugs, hints, tips. </p>
 </dd>
<dt>ckubwr.txt</dt>
<dd> <p> Unix-specific C-Kermit bugs, hints, tips. </p>
 </dd>
<dt>ckcplm.txt</dt>
<dd> <p> C-Kermit program logic manual. </p>
 </dd>
<dt>ckccfg.txt</dt>
<dd> <p> C-Kermit compile-time configuration options. </p>
 </dd>
<dt>ssh</dt>
<dd> <p> (in your PATH) SSH connection helper. </p>
 </dd>
<dt>rz, sz, etc.</dt>
<dd> <p> (in your PATH) external protocols for XYZmodem. </p>
 </dd>
<dt>/var/spool/locks (or whatever)</dt>
<dd> <p> UUCP lockfile for dialing out (see installation instructions). </p>
 </dd></dl>
<h2>AUTHORS</h2>
<dl>
<dt>Software</dt>
<dd> <p> Frank da Cruz and Jeffrey E Altman, <br />
 1985-present, with contributions from hundreds of others all over the world. </p>
 </dd>
<dt>Documentation</dt>
<dd> <p> Frank da Cruz </p>
 </dd>
<dt>Address</dt>
<dd> <pre><code>The Kermit Project - Columbia Univerity
612 West 115th Street
New York NY 10025-7799
USA
</code></pre>
 </dd>
<dt>E-Mail</dt>
<dd> <p> kermit [at] columbia.edu </p>
 </dd>
<dt>Web</dt>
<dd> <p> <a rel="nofollow" href="http://www.columbia.edu/kermit/">http://www.columbia.edu/kermit/</a> <br />
 </p>
 </dd></dl>
