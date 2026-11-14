---
title: "gkermit(1)"
name: "gkermit"
section: "1"
letter: "g"
url: "/docs/linux/man/1-gkermit/"
---

<h2>NAME</h2>

 gkermit - G-Kermit (GNU Kermit) 1.00 file transfer software.

<h2>SYNOPSIS</h2>

 <pre><code>
gkermit[options] - s file(s)
Send files
        gkermit[options] -
    g file(s)
Get files
        gkermit[options] -
    r Receive files
</code></pre>

<h2>DESCRIPTION</h2>

 G-Kermit is a UNIX program for transferring files using the Kermit protocol. G-Kermit is a product of Kermit Project at Columbia University. It is free software under the GNU Public License. See the COPYING file for details. 

<h3>INVOKING G-KERMIT</h3>

 

 The G-Kermit binary is called &quot;gkermit&quot;. It should be stored someplace in your UNIX PATH; normally it is available as /usr/local/bin/gkermit. To run G-Kermit, just type &quot;gkermit&quot; followed by command-line options that tell it what to do. If no options are given, it prints a usage message listing the available options. 

 If an option takes an argument, the argument is required; if an option does not take an argument, no argument may be given (exception: -d). The action options are -r, -s, and -g. Only one action option may be given. If no action options are given, G-Kermit does nothing (except possibly to print its usage message or create a debug.log file). Here are some examples (&quot;$ &quot; is the shell prompt): 
$ gkermit - s hello.c &lt; --Send the hello.c file
                                $ gkermit -
                            s hello.*
    &lt; --Send all hello.*files
                            $ gkermit -
          r &lt;
    --Wait to receive files
            $ gkermit -
        g hello.c &lt;
    --Get hello.c file
            $ gkermit -
        g hello.\* &lt;
    --Get all hello.*files
 Options that do not take arguments can be &quot;bundled&quot; with other options. An option that takes an argument must always be followed by a space and then its argument(s). Examples: <pre>
  $ gkermit -is hello.o  &lt;-- Send hello.o in binary mode
  $ gkermit -dr          &lt;-- Receive with debugging
</pre>

<h3>COMMAND-LINE OPTIONS</h3>

 

 <pre><code>
  -r      RECEIVE.  Wait for incoming files.
  -s fn   SEND.  Send file(s)
  specified by fn.- g fn GET.Get specified file(s) from server.
  -a fn   AS-NAME.  Alternative name for file.
  -i      IMAGE.  Binary-mode transfer (default).
  -T      TEXT. Text-mode transfer.
  -P      PATH (filename)
  conversion disabled.- w WRITEOVER when filenames collide.- K KEEP incompletely received files.- p x PARITY.x = e, o, m, s, n;
  default = n(one).- e n PACKET LENGTH.n = 40 - 9000;
  default = 4000. - b n TIMEOUT.Per - packet timeout, seconds.- x XON / XOFF.Set Xon / Xoff in the tty driver.--x Unset Xon / Xoff in the tty driver.- S STREAMING disabled.- X EXTERNAL.G - Kermit is an external protocol.- q QUIET.Suppress messages.- d DEBUG.Write debugging info to./ debug.log.- d fn DEBUG.Write debugging info to given file.- h HELP.Display brief usage message.
</code></pre> 

 You may supply options to G-Kermit on the command line or through the GKERMIT environment variable, which can contain any valid gkermit command-line options. These are processed before the actual command-line options and so can be overridden by them. Example for bash or ksh, which you can put in your profile if you want to always keep incomplete files, suppress streaming, suppress messages, and use Space parity: <pre>
  export GKERMIT=&quot;-K -S -q -p s&quot;
</pre> 

<h3>MECHANICS OF FILE TRANSFER</h3>

 

 To transfer files with G-Kermit you must be connected through a terminal emulator to the UNIX system where G-Kermit is running, meaning you are online to UNIX and have access to the shell prompt (or to a menu that has an option to invoke G-Kermit). The connection can be serial (direct or dialed) or network (Telnet, Rlogin, X.25, etc). 

 When you tell G-Kermit to SEND a file (or files), e.g. with: <pre>
  $ gkermit -Ts oofa.txt
</pre> it pauses for a second and then sends its first packet. What happens next depends on the capabilities of your terminal emulator: 

 
 &bull;<tt>&nbsp;<wbr>&nbsp;<wbr></tt>If your emulator supports Kermit &quot;autodownloads&quot; then it receives the
 file automatically and puts you back in the terminal screen when done. 

 
 &bull;<tt>&nbsp;<wbr>&nbsp;<wbr></tt>Otherwise, you'll need to take whatever action is required by your
 emulator to get its attention: a mouse action, a keystroke like Alt-x, or a character sequence like Ctrl-\ or Ctrl-] followed by the letter &quot;c&quot; (this is called &quot;escaping back&quot;) and then tell it to receive the file. When the transfer is complete, you must instruct your emulator to go back to its terminal screen. 

 During file transfer, most terminal emulators put up some kind of running display of the file transfer progress. 

 When you tell G-Kermit to RECEIVE (with &quot;gkermit -r&quot;), this requires you to escape back to your terminal emulator and instruct it to send the desired file(s). 

 If your terminal emulator supports Kermit autodownloads AND Kermit server mode, then you can use GET (&quot;gkermit -g files...&quot;) rather than RECEIVE (&quot;gkermit -r&quot;), and the rest happens automatically, as when G-Kermit is sending.

<h3>INTERRUPTING FILE TRANSFER</h3>

 

 G-Kermit supports file and group interruption. The method for interrupting a transfer depends on your terminal emulator. For example, while the file-transfer display is active, you might type the letter 'x' to cancel the current file and go on to the next one (if any), and the letter 'z' to cancel the group. Or there might be buttons you can click with your mouse. 

 When G-Kermit is in packet mode and your terminal emulator is in its terminal screen, you can also type three (3) Ctrl-C characters in a row to make G-Kermit exit and restore the normal terminal modes. 

<h3>TEXT AND BINARY TRANSFER MODE</h3>

 

 When sending files in binary mode, G-Kermit sends every byte exactly as it is stored on the disk. This mode is appropriate for program binaries, graphics files, tar archives, compressed files, etc, and is G-Kermit's default file transfer mode when sending. When receiving files in binary mode, G-Kermit simply copies each byte to disk. (Obviously the bytes are encoded for transmission, but the encoding and decoding procedures give a replica of the original file after transfer.) 

 When sending files in text mode, G-Kermit converts the record format to the common one that is defined for the Kermit protocol, namely lines terminated by carriage return and linefeed (CRLF); the receiver converts the CRLFs to whatever line-end or record-format convention is used on its platform. When receiving files in text mode, G-Kermit simply strips carriage returns, leaving only a linefeed at the end of each line, which is the UNIX convention. 

 When receiving files, the sender's transfer mode (text or binary) predominates if the sender gives this information to G-Kermit in a Kermit File Attribute packet, which of course depends on whether your terminal emulator's Kermit protocol has this feature. Otherwise, if you gave a -i or -T option on the gkermit command line, the corresponding mode is used; otherwise the default mode (binary) is used. 

 Furthermore, when either sending or receiving, G-Kermit and your terminal emulator's Kermit can inform each other of their OS type (UNIX in G-Kermit's case). If your emulator supports this capability, which is called &quot;automatic peer recognition&quot;, and it tells G-Kermit that its platform is also UNIX, G-Kermit and the emulator's Kermit automatically switch into binary mode, since no record-format conversion is necessary in this case. Automatic peer recognition is disabled automatically if you include the -i (image) or -T (text) option. 

 When sending, G-Kermit sends all files in the same mode, text or binary. There is no automatic per-file mode switching. When receiving, however, per-file switching occurs automatically based on the incoming Attribute packets, if any (explained below), that accompany each file. 

<h3>PATHNAMES</h3>

 

 When SENDING a file, G-Kermit obtains the filenames from the command line. It depends on the shell to expand metacharacters (wildcards and tilde). 

 G-Kermit uses the full pathname given to find and open the file, but then strips the pathname before sending the name to the receiver. For example: <pre>
  $ gkermit -s /etc/hosts
</pre> results in the receiver getting a file called &quot;HOSTS&quot; or &quot;hosts&quot; (the directory part, &quot;/etc/&quot;, is stripped). 

 However, if a pathname is included in the -a option, the directory part is not stripped: <pre>
  $ gkermit -s /etc/hosts -a /tmp/hosts
</pre> This example sends the /etc/hosts file but tells the receiver that its name is &quot;/tmp/hosts&quot;. What the receiver does with the pathname is, of course, up to the receiver, which might have various options for dealing with incoming pathnames. 

 When RECEIVING a file, G-Kermit does NOT strip the pathname. If the incoming filename includes a path, G-Kermit tries to store the file in the specified place. If the path does not exist, the transfer fails. The incoming pathname can, of course, be overridden with the -a option. 

<h3>FILENAME CONVERSION</h3>

 

 When sending a file, G-Kermit normally converts outbound filenames to common form: uppercase, no more than one period, and no funny characters. So, for example, gkermit.tar.gz would be sent as GKERMIT_TAR.GZ. 

 When receiving a file, if the name is all uppercase, G-Kermit converts it to all lowercase. If the name contains any lowercase letters, G-Kermit leaves the name alone. 

 If the automatic peer recognition feature is available in the terminal emulator, and G-Kermit recognizes the emulator's platform as UNIX, G-Kermit automatically disables filename conversion and sends and accepts filenames literally. 

 You can force literal filenames by including the -P option on the command line. 

<h3>FILENAME COLLISIONS</h3>

 

 When G-Kermit receives a file whose name is the same as that of an existing file, G-Kermit &quot;backs up&quot; the existing file by adding a unique suffix to its name. The suffix is &quot;.~n~&quot;, where n is a number. This kind of backup suffix is compatible with GNU EMACS and various other popular applications. 

 To defeat the backup feature and have incoming files overwrite existing files of the same name, include the -w (writeover) option on the command line. 

<h2>RETURN VALUES</h2>

 G-Kermit resturns an exit status code of 0 if all actions succeeded and 1 if any actions failed. 

<h2>IMPLEMENTATION NOTES</h2>

 G-Kermit is designed to be small, portable, and stable, and is intended for use only on the &quot;far end&quot; of a connection; it does not make connections itself, although it can be used as an external protocol by other programs that do make connections. To keep it small and stable, it does not include sliding windows, a command or scripting language or character-set translation. To keep it portable and stable, it avoids use of system services that are not standardized across all UNIX varieties and therefore, in particular, does not support file timestamps, internal wildcard expansion, and other features that are not implemented consistently (or at all) across all UNIXes. 

<h2>ENVIRONMENT</h2>

 A GKERMIT environment variable may be defined (for example in your shell profile) to include G-Kermit command-line options; these are processed by G-Kermit before any options that are specified on the command line, and therefore are overriden by command-line options. 

<h2>DIAGNOSTICS</h2>

 If an error occurs during file transfer G-Kermit sends an error packet to your terminal emulator to cancel the transfer; an appropriate error message should be displayed on your screen. 

<h2>ERRORS</h2>

 File transfers can fail for a number of reasons: 

 
 &bull;<tt>&nbsp;<wbr>&nbsp;<wbr></tt>Lack of read access to a source file.
 
 &bull;<tt>&nbsp;<wbr>&nbsp;<wbr></tt>Lack of write access to a target directory.
 
 &bull;<tt>&nbsp;<wbr>&nbsp;<wbr></tt>Lack of adequate flow control.
 
 &bull;<tt>&nbsp;<wbr>&nbsp;<wbr></tt>Use of streaming on an unreliable connection.
 
 &bull;<tt>&nbsp;<wbr>&nbsp;<wbr></tt>Excessive unprefixing of control characters.
 
 &bull;<tt>&nbsp;<wbr>&nbsp;<wbr></tt>Sending bare 8-bit data on a 7-bit connection.
 
 &bull;<tt>&nbsp;<wbr>&nbsp;<wbr></tt>Packets too long for receiver's buffers.
 
 &bull;<tt>&nbsp;<wbr>&nbsp;<wbr></tt>Timeout interval too short for connection.
 
 

 and many others; these are covered in the references. 

<h2>REFERENCES</h2>

 

 The Kermit protocol is specified in &quot;Kermit, A File Transfer Protocol&quot; by Frank da Cruz, Digital Press (1987). A correctness proof of the Kermit protocol appears in &quot;Specification and Validation Methods&quot;, edited by Egon Boerger, Oxford University Press (1995). &quot;Using C-Kermit&quot; by Frank da Cruz and Christine M. Gianone, Digital Press (1997, or later edition) explains many of the terms and techniques referenced here in case you are not familiar with them, and also includes tutorials on data communications, extensive troubleshooting and performance tips, etc. Various other books on Kermit are available from Digital Press. Online resources include: <pre>
  Web:   <a rel="nofollow" HREF="http://www.columbia.edu/kermit/">http://www.columbia.edu/kermit/</a>
  FTP:   <a HREF="ftp://kermit.columbia.edu/kermit/g/">ftp://kermit.columbia.edu/kermit/g/</a>
  News:  comp.protocols.kermit.misc
  Email: kermit-support [at] columbia.edu
</pre> 

 Also see the README file distributed with G-Kermit for further detail. It can also be found at <a HREF="ftp://kermit.columbia.edu/kermit/g/README.">ftp://kermit.columbia.edu/kermit/g/README.</a> 

<h2>BUGS</h2>

 The speed of a file transfer depends not only on the speed of the two computers involved and the characteristics of the connection, but also on the capabilities and configuration of the two Kermit programs. Kermit is a fast and reliable protocol, but not all implementations of it are necessarily fast or reliable. 

 Nonstreaming transfers on a TCP/IP connection might be inordinately slow if one or both of the TCP/IP stacks uses the Nagle or Delayed ACK tricks. Streaming is used automatically if the other Kermit supports it. 

 When receiving files in text mode, G-Kermit strips all carriage returns, even if they aren't followed by linefeed. 

 A backups files are not guaranteed to have the highest number in their backup suffix. 

<h2>AUTHOR</h2>

 Frank da Cruz, the Kermit Project, Columbia University, New York City, December 1999. 
 

<h2>Index</h2>


