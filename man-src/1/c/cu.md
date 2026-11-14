---
title: "cu(1)"
name: "cu"
section: "1"
letter: "c"
url: "/docs/linux/man/1-cu/"
description: "cu – Call up another system"
---

<h2>NAME</h2>
<p> cu &#8211; Call up another system</p>
<h2>SYNOPSIS</h2>
<p> <code>cu</code> [ options ] [ system | phone | &quot;dir&quot; ]</p>
<h2>DESCRIPTION</h2>
<p> The <i>cu</i> command is used to call up another system and act as a dial in terminal. It can also do simple file transfers with no error checking. </p>
<p> <i>cu</i> takes a single argument, besides the options. If the argument is the string &quot;dir&quot; cu will make a direct connection to the port. This may only be used by users with write access to the port, as it permits reprogramming the modem. </p>
<p> Otherwise, if the argument begins with a digit, it is taken to be a phone number to call. Otherwise, it is taken to be the name of a system to call. The <code>-z</code> or <code>&#8211;system</code> option may be used to name a system beginning with a digit, and the <code>-c</code> or <code>&#8211;phone</code> option may be used to name a phone number that does not begin with a digit. </p>
<p> <i>cu</i> locates a port to use in the UUCP configuration files. If a simple system name is given, it will select a port appropriate for that system. The <code>-p, &#8211;port, -l, &#8211;line, -s</code> and <code>&#8211;speed</code> options may be used to control the port selection. </p>
<p> When a connection is made to the remote system, <i>cu</i> forks into two processes. One reads from the port and writes to the terminal, while the other reads from the terminal and writes to the port. </p>
<p> <i>cu</i> provides several commands that may be used during the conversation. The commands all begin with an escape character, initially <code>~</code> (tilde). The escape character is only recognized at the beginning of a line. To send an escape character to the remote system at the start of a line, it must be entered twice. All commands are either a single character or a word beginning with <code>%</code> (percent sign). </p>
<p> <i>cu</i> recognizes the following commands: </p>
<dl>
<dt><code>~.</code></p>
<dd> Terminate the conversation.</p>
<dt><code>~! command</code></p>
<dd> Run command in a shell. If command is empty, starts up a shell.</p>
<dt><code>~$ command</code></p>
<dd> Run command, sending the standard output to the remote system.</p>
<dt><code>~| command</code></p>
<dd> Run command, taking the standard input from the remote system.</p>
<dt><code>~+ command</code></p>
<dd> Run command, taking the standard input from the remote system and sending the standard output to the remote system.</p>
<dt><code>~#, ~%break</code></p>
<dd> Send a break signal, if possible.</p>
<dt><code>~c directory, ~%cd directory</code></p>
<dd> Change the local directory.</p>
<dt><code>~&gt; file</code></p>
<dd> Send a file to the remote system. This just dumps the file over the communication line. It is assumed that the remote system is expecting it.</p>
<dt><code>~&lt;</code></p>
<dd> Receive a file from the remote system. This prompts for the local file name and for the remote command to execute to begin the file transfer. It continues accepting data until the contents of the <code>eofread</code> variable are seen.</p>
<dt><code>~p from to, ~%put from to</code></p>
<dd> Send a file to a remote Unix system. This runs the appropriate commands on the remote system.</p>
<dt><code>~t from to, ~%take from to</code></p>
<dd> Retrieve a file from a remote Unix system. This runs the appropriate commands on the remote system.</p>
<dt><code>~s variable value</code></p>
<dd> Set a <i>cu</i> variable to the given value. If value is not given, the variable is set to <code>true.</code></p>
<dt><code>~! variable</code></p>
<dd> Set a <i>cu</i> variable to <code>false.</code></p>
<dt><code>~z</code></p>
<dd> Suspend the cu session. This is only supported on some systems. On systems for which ^Z may be used to suspend a job, <code>~^Z</code> will also suspend the session.</p>
<dt><code>~%nostop</code></p>
<dd> Turn off XON/XOFF handling.</p>
<dt><code>~%stop</code></p>
<dd> Turn on XON/XOFF handling.</p>
<dt><code>~v</code></p>
<dd> List all the variables and their values.</p>
<dt><code>~?</code></p>
<dd> List all commands. </p>
<p> <i>cu</i> also supports several variables. They may be listed with the <code>~v</code> command, and set with the <code>~s</code> or <code>~!</code> commands. </p>
<dt><code>escape</code></p>
<dd> The escape character. Initially <code>~</code> (tilde).</p>
<dt><code>delay</code></p>
<dd> If this variable is true, <i>cu</i> will delay for a second after recognizing the escape character before printing the name of the local system. The default is true.</p>
<dt><code>eol</code></p>
<dd> The list of characters which are considered to finish a line. The escape character is only recognized after one of these is seen. The default is carriage return, ^U, ^C, ^O, ^D, ^S, ^Q, ^R.</p>
<dt><code>binary</code></p>
<dd> Whether to transfer binary data when sending a file. If this is false, then newlines in the file being sent are converted to carriage returns. The default is false.</p>
<dt><code>binary-prefix</code></p>
<dd> A string used before sending a binary character in a file transfer, if the <code>binary</code> variable is true. The default is ^V.</p>
<dt><code>echo-check</code></p>
<dd> Whether to check file transfers by examining what the remote system echoes back. This probably doesn&#8217;t work very well. The default is false.</p>
<dt><code>echonl</code></p>
<dd> The character to look for after sending each line in a file. The default is carriage return.</p>
<dt><code>timeout</code></p>
<dd> The timeout to use, in seconds, when looking for a character, either when doing echo checking or when looking for the <code>echonl</code> character. The default is 30.</p>
<dt><code>kill</code></p>
<dd> The character to use delete a line if the echo check fails. The default is ^U.</p>
<dt><code>resend</code></p>
<dd> The number of times to resend a line if the echo check continues to fail. The default is 10.</p>
<dt><code>eofwrite</code></p>
<dd> The string to write after sending a file with the <code>~&gt;</code> command. The default is ^D.</p>
<dt><code>eofread</code></p>
<dd> The string to look for when receiving a file with the <code>~&lt;</code> command. The default is $, which is intended to be a typical shell prompt.</p>
<dt><code>verbose</code></p>
<dd> Whether to print accumulated information during a file transfer. The default is true.</dl>
<h2>OPTIONS</h2>
<p> The following options may be given to <i>cu.</i></p>
<dl>
<dt><code>-e, &#8211;parity=even</code></p>
<dd> Use even parity.</p>
<dt><code>-o, &#8211;parity=odd</code></p>
<dd> Use odd parity.</p>
<dt><code>&#8211;parity=none</code></p>
<dd> Use no parity. No parity is also used if both <code>-e</code> and <code>-o</code> are given.</p>
<dt><code>-h, &#8211;halfduplex</code></p>
<dd> Echo characters locally (half-duplex mode).</p>
<dt><code>&#8211;nostop</code></p>
<dd> Turn off XON/XOFF handling (it is on by default).</p>
<dt><code>-E char, &#8211;escape char</code></p>
<dd> Set the escape character. Initially <code>~</code> (tilde). To eliminate the escape character, use <code>-E &#8221;.</code></p>
<dt><code>-z system, &#8211;system system</code></p>
<dd> The system to call.</p>
<dt><code>-c phone-number, &#8211;phone phone-number</code></p>
<dd> The phone number to call.</p>
<dt><code>-p port, &#8211;port port</code></p>
<dd> Name the port to use.</p>
<dt><code>-a port</code></p>
<dd> Equivalent to <code>&#8211;port port.</code></p>
<dt><code>-l line, &#8211;line line</code></p>
<dd> Name the line to use by giving a device name. This may be used to dial out on ports that are not listed in the UUCP configuration files. Write access to the device is required.</p>
<dt><code>-s speed, &#8211;speed speed</code></p>
<dd> The speed (baud rate) to use.</p>
<dt><code>-#</code></p>
<dd> Where # is a number, equivalent to <code>&#8211;speed #.</code></p>
<dt><code>-n, &#8211;prompt</code></p>
<dd> Prompt for the phone number to use.</p>
<dt><code>-d</code></p>
<dd> Enter debugging mode. Equivalent to <code>&#8211;debug all.</code></p>
<dt><code>-x type, &#8211;debug type</code></p>
<dd> Turn on particular debugging types. The following types are recognized: abnormal, chat, handshake, uucp-proto, proto, port, config, spooldir, execute, incoming, outgoing. Only abnormal, chat, handshake, port, config, incoming and outgoing are meaningful for <i>cu.</i> </p>
<p> Multiple types may be given, separated by commas, and the <code>&#8211;debug</code> option may appear multiple times. A number may also be given, which will turn on that many types from the foregoing list; for example, <code>&#8211;debug 2</code> is equivalent to <code>&#8211;debug abnormal,chat.</code> <code>&#8211;debug all</code> may be used to turn on all debugging options.</p>
<dt><code>-I file, &#8211;config file</code></p>
<dd> Set configuration file to use. This option may not be available, depending upon how <i>cu</i> was compiled.</p>
<dt><code>-v, &#8211;version</code></p>
<dd> Report version information and exit.</p>
<dt><code>&#8211;help</code></p>
<dd> Print a help message and exit.</dl>
<h2>BUGS</h2>
<p> This program does not work very well.</p>
<h2>AUTHOR</h2>
<p> Ian Lance Taylor &lt;ian [at] airs.com&gt; </p>
<h2>Index</h2>
