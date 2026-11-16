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
<dt><code>~.</code></dt>
<dd> Terminate the conversation.</dd>
<dt><code>~! command</code></dt>
<dd> Run command in a shell. If command is empty, starts up a shell.</dd>
<dt><code>~$ command</code></dt>
<dd> Run command, sending the standard output to the remote system.</dd>
<dt><code>~| command</code></dt>
<dd> Run command, taking the standard input from the remote system.</dd>
<dt><code>~+ command</code></dt>
<dd> Run command, taking the standard input from the remote system and sending the standard output to the remote system.</dd>
<dt><code>~#, ~%break</code></dt>
<dd> Send a break signal, if possible.</dd>
<dt><code>~c directory, ~%cd directory</code></dt>
<dd> Change the local directory.</dd>
<dt><code>~&gt; file</code></dt>
<dd> Send a file to the remote system. This just dumps the file over the communication line. It is assumed that the remote system is expecting it.</dd>
<dt><code>~&lt;</code></dt>
<dd> Receive a file from the remote system. This prompts for the local file name and for the remote command to execute to begin the file transfer. It continues accepting data until the contents of the <code>eofread</code> variable are seen.</dd>
<dt><code>~p from to, ~%put from to</code></dt>
<dd> Send a file to a remote Unix system. This runs the appropriate commands on the remote system.</dd>
<dt><code>~t from to, ~%take from to</code></dt>
<dd> Retrieve a file from a remote Unix system. This runs the appropriate commands on the remote system.</dd>
<dt><code>~s variable value</code></dt>
<dd> Set a <i>cu</i> variable to the given value. If value is not given, the variable is set to <code>true.</code></dd>
<dt><code>~! variable</code></dt>
<dd> Set a <i>cu</i> variable to <code>false.</code></dd>
<dt><code>~z</code></dt>
<dd> Suspend the cu session. This is only supported on some systems. On systems for which ^Z may be used to suspend a job, <code>~^Z</code> will also suspend the session.</dd>
<dt><code>~%nostop</code></dt>
<dd> Turn off XON/XOFF handling.</dd>
<dt><code>~%stop</code></dt>
<dd> Turn on XON/XOFF handling.</dd>
<dt><code>~v</code></dt>
<dd> List all the variables and their values.</dd>
<dt><code>~?</code></dt>
<dd> List all commands. </dd>
<p> <i>cu</i> also supports several variables. They may be listed with the <code>~v</code> command, and set with the <code>~s</code> or <code>~!</code> commands. </p>
<dt><code>escape</code></dt>
<dd> The escape character. Initially <code>~</code> (tilde).</dd>
<dt><code>delay</code></dt>
<dd> If this variable is true, <i>cu</i> will delay for a second after recognizing the escape character before printing the name of the local system. The default is true.</dd>
<dt><code>eol</code></dt>
<dd> The list of characters which are considered to finish a line. The escape character is only recognized after one of these is seen. The default is carriage return, ^U, ^C, ^O, ^D, ^S, ^Q, ^R.</dd>
<dt><code>binary</code></dt>
<dd> Whether to transfer binary data when sending a file. If this is false, then newlines in the file being sent are converted to carriage returns. The default is false.</dd>
<dt><code>binary-prefix</code></dt>
<dd> A string used before sending a binary character in a file transfer, if the <code>binary</code> variable is true. The default is ^V.</dd>
<dt><code>echo-check</code></dt>
<dd> Whether to check file transfers by examining what the remote system echoes back. This probably doesn&#8217;t work very well. The default is false.</dd>
<dt><code>echonl</code></dt>
<dd> The character to look for after sending each line in a file. The default is carriage return.</dd>
<dt><code>timeout</code></dt>
<dd> The timeout to use, in seconds, when looking for a character, either when doing echo checking or when looking for the <code>echonl</code> character. The default is 30.</dd>
<dt><code>kill</code></dt>
<dd> The character to use delete a line if the echo check fails. The default is ^U.</dd>
<dt><code>resend</code></dt>
<dd> The number of times to resend a line if the echo check continues to fail. The default is 10.</dd>
<dt><code>eofwrite</code></dt>
<dd> The string to write after sending a file with the <code>~&gt;</code> command. The default is ^D.</dd>
<dt><code>eofread</code></dt>
<dd> The string to look for when receiving a file with the <code>~&lt;</code> command. The default is $, which is intended to be a typical shell prompt.</dd>
<dt><code>verbose</code></dt>
<dd> Whether to print accumulated information during a file transfer. The default is true.</dd></dl>
<h2>OPTIONS</h2>
<p> The following options may be given to <i>cu.</i></p>
<dl>
<dt><code>-e, &#8211;parity=even</code></dt>
<dd> Use even parity.</dd>
<dt><code>-o, &#8211;parity=odd</code></dt>
<dd> Use odd parity.</dd>
<dt><code>&#8211;parity=none</code></dt>
<dd> Use no parity. No parity is also used if both <code>-e</code> and <code>-o</code> are given.</dd>
<dt><code>-h, &#8211;halfduplex</code></dt>
<dd> Echo characters locally (half-duplex mode).</dd>
<dt><code>&#8211;nostop</code></dt>
<dd> Turn off XON/XOFF handling (it is on by default).</dd>
<dt><code>-E char, &#8211;escape char</code></dt>
<dd> Set the escape character. Initially <code>~</code> (tilde). To eliminate the escape character, use <code>-E &#8221;.</code></dd>
<dt><code>-z system, &#8211;system system</code></dt>
<dd> The system to call.</dd>
<dt><code>-c phone-number, &#8211;phone phone-number</code></dt>
<dd> The phone number to call.</dd>
<dt><code>-p port, &#8211;port port</code></dt>
<dd> Name the port to use.</dd>
<dt><code>-a port</code></dt>
<dd> Equivalent to <code>&#8211;port port.</code></dd>
<dt><code>-l line, &#8211;line line</code></dt>
<dd> Name the line to use by giving a device name. This may be used to dial out on ports that are not listed in the UUCP configuration files. Write access to the device is required.</dd>
<dt><code>-s speed, &#8211;speed speed</code></dt>
<dd> The speed (baud rate) to use.</dd>
<dt><code>-#</code></dt>
<dd> Where # is a number, equivalent to <code>&#8211;speed #.</code></dd>
<dt><code>-n, &#8211;prompt</code></dt>
<dd> Prompt for the phone number to use.</dd>
<dt><code>-d</code></dt>
<dd> Enter debugging mode. Equivalent to <code>&#8211;debug all.</code></dd>
<dt><code>-x type, &#8211;debug type</code></dt>
<dd> Turn on particular debugging types. The following types are recognized: abnormal, chat, handshake, uucp-proto, proto, port, config, spooldir, execute, incoming, outgoing. Only abnormal, chat, handshake, port, config, incoming and outgoing are meaningful for <i>cu.</i> </dd>
<p> Multiple types may be given, separated by commas, and the <code>&#8211;debug</code> option may appear multiple times. A number may also be given, which will turn on that many types from the foregoing list; for example, <code>&#8211;debug 2</code> is equivalent to <code>&#8211;debug abnormal,chat.</code> <code>&#8211;debug all</code> may be used to turn on all debugging options.</p>
<dt><code>-I file, &#8211;config file</code></dt>
<dd> Set configuration file to use. This option may not be available, depending upon how <i>cu</i> was compiled.</dd>
<dt><code>-v, &#8211;version</code></dt>
<dd> Report version information and exit.</dd>
<dt><code>&#8211;help</code></dt>
<dd> Print a help message and exit.</dd></dl>
<h2>BUGS</h2>
<p> This program does not work very well.</p>
<h2>AUTHOR</h2>
<p> Ian Lance Taylor &lt;ian [at] airs.com&gt; </p>
<h2>Index</h2>
