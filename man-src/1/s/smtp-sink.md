---
title: "smtp-sink(1)"
name: "smtp-sink"
section: "1"
letter: "s"
url: "/docs/linux/man/1-smtp-sink/"
description: "smtp-sink – parallelized SMTP/LMTP test server"
---

<h2 class="name">NAME</h2>
<p> smtp-sink &#8211; parallelized SMTP/LMTP test server </p>
<h2>SYNOPSIS</h2>
<p> <code>smtp-sink</code> [<i>options</i>] [<code>inet:</code>][<i>host</i>]:<i>port</i> <i>backlog</i> </p>
<p> <code>smtp-sink</code> [<i>options</i>] <code>unix:</code><i>pathname</i> <i>backlog</i></p>
<h2>DESCRIPTION</h2>
<p> <code>smtp-sink</code> listens on the named host (or address) and port. It takes SMTP messages from the network and throws them away. The purpose is to measure client performance, not protocol compliance. </p>
<p> <code>smtp-sink</code> may also be configured to capture each mail delivery transaction to file. Since disk latencies are large compared to network delays, this mode of operation can reduce the maximal performance by several orders of magnitude. </p>
<p> Connections can be accepted on IPv4 or IPv6 endpoints, or on UNIX-domain sockets. IPv4 and IPv6 are the default. This program is the complement of the <code><a href="/docs/linux/man/1-smtp-source/">smtp-source</a></code>(1) program. </p>
<p> Note: this is an unsupported test program. No attempt is made to maintain compatibility between successive versions. </p>
<p> Arguments:</p>
<dl>
<dt><code>-4</code></p>
<dd> Support IPv4 only. This option has no effect when Postfix is built without IPv6 support.</p>
<dt><code>-6</code></p>
<dd> Support IPv6 only. This option is not available when Postfix is built without IPv6 support.</p>
<dt><code>-8</code></p>
<dd> Do not announce 8BITMIME support.</p>
<dt><code>-a</code></p>
<dd> Do not announce SASL authentication support.</p>
<dt><code>-A </code><i>delay</i></p>
<dd> Wait <i>delay</i> seconds after responding to DATA, then abort prematurely with a 550 reply status. Do not read further input from the client; this is an attempt to block the client before it sends &quot;.&quot;. Specify a zero delay value to abort immediately.</p>
<dt><code>-b </code><i>soft-bounce-reply</i></p>
<dd> Use <i>soft-bounce-reply</i> for soft reject responses. The default reply is &quot;450 4.3.0 Error: command failed&quot;.</p>
<dt><code>-B </code><i>hard-bounce-reply</i></p>
<dd> Use <i>hard-bounce-reply</i> for hard reject responses. The default reply is &quot;500 5.3.0 Error: command failed&quot;.</p>
<dt><code>-c</code></p>
<dd> Display running counters that are updated whenever an SMTP session ends, a QUIT command is executed, or when &quot;.&quot; is received.</p>
<dt><code>-C</code></p>
<dd> Disable XCLIENT support.</p>
<dt><code>-d </code><i>dump-template</i></p>
<dd> Dump each mail transaction to a single-message file whose name is created by expanding the <i>dump-template</i> via <a href="/docs/linux/man/3-strftime/">strftime</a>(3) and appending a pseudo-random hexadecimal number (example: &quot;%Y%m%d%H/%M.&quot; expands into &quot;2006081203/05.809a62e3&quot;). If the template contains &quot;/&quot; characters, missing directories are created automatically. The message dump format is described below. </p>
<p> Note: this option keeps one capture file open for every mail transaction in progress.</p>
<dt><code>-D </code><i>dump-template</i></p>
<dd> Append mail transactions to a multi-message dump file whose name is created by expanding the <i>dump-template</i> via <a href="/docs/linux/man/3-strftime/">strftime</a>(3). If the template contains &quot;/&quot; characters, missing directories are created automatically. The message dump format is described below. </p>
<p> Note: this option keeps one capture file open for every mail transaction in progress.</p>
<dt><code>-e</code></p>
<dd> Do not announce ESMTP support.</p>
<dt><code>-E</code></p>
<dd> Do not announce ENHANCEDSTATUSCODES support.</p>
<dt><code>-f </code><i>command,command,&#8230;</i></p>
<dd> Reject the specified commands with a hard (5xx) error code. This option implies <code>-p</code>. </p>
<p> Examples of commands are CONNECT, HELO, EHLO, LHLO, MAIL, RCPT, VRFY, DATA, ., RSET, NOOP, and QUIT. Separate command names by white space or commas, and use quotes to protect white space from the shell. Command names are case-insensitive.</p>
<dt><code>-F</code></p>
<dd> Disable XFORWARD support.</p>
<dt><code>-h</code><i> hostname</i></p>
<dd> Use <i>hostname</i> in the SMTP greeting, in the HELO response, and in the EHLO response. The default hostname is &quot;smtp-sink&quot;.</p>
<dt><code>-H</code><i> delay</i></p>
<dd> Delay the first read operation after receiving DATA (time in seconds). Combine with a large test message and a small TCP window size (see the <code>-T</code> option) to test the Postfix client write_wait() implementation.</p>
<dt><code>-L</code></p>
<dd> Enable LMTP instead of SMTP.</p>
<dt><code>-m </code><i>count</i> (default: 256)</p>
<dd> An upper bound on the maximal number of simultaneous connections that <code>smtp-sink</code> will handle. This prevents the process from running out of file descriptors. Excess connections will stay queued in the TCP/IP stack.</p>
<dt><code>-M </code><i>count</i></p>
<dd> Terminate after receiving <i>count</i> messages.</p>
<dt><code>-n </code><i>count</i></p>
<dd> Terminate after <i>count</i> sessions.</p>
<dt><code>-N</code></p>
<dd> Do not announce support for DSN.</p>
<dt><code>-p</code></p>
<dd> Do not announce support for ESMTP command pipelining.</p>
<dt><code>-P</code></p>
<dd> Change the server greeting so that it appears to come through a CISCO PIX system. Implies <code>-e</code>.</p>
<dt><code>-q </code><i>command,command,&#8230;</i></p>
<dd> Disconnect (without replying) after receiving one of the specified commands. </p>
<p> Examples of commands are CONNECT, HELO, EHLO, LHLO, MAIL, RCPT, VRFY, DATA, ., RSET, NOOP, and QUIT. Separate command names by white space or commas, and use quotes to protect white space from the shell. Command names are case-insensitive.</p>
<dt><code>-Q </code><i>command,command,&#8230;</i></p>
<dd> Send a 421 reply and disconnect after receiving one of the specified commands. </p>
<p> Examples of commands are CONNECT, HELO, EHLO, LHLO, MAIL, RCPT, VRFY, DATA, ., RSET, NOOP, and QUIT. Separate command names by white space or commas, and use quotes to protect white space from the shell. Command names are case-insensitive.</p>
<dt><code>-r </code><i>command,command,&#8230;</i></p>
<dd> Reject the specified commands with a soft (4xx) error code. This option implies <code>-p</code>. </p>
<p> Examples of commands are CONNECT, HELO, EHLO, LHLO, MAIL, RCPT, VRFY, DATA, ., RSET, NOOP, and QUIT. Separate command names by white space or commas, and use quotes to protect white space from the shell. Command names are case-insensitive.</p>
<dt><code>-R </code><i>root-directory</i></p>
<dd> Change the process root directory to the specified location. This option requires super-user privileges. See also the <code>-u</code> option.</p>
<dt><code>-s </code><i>command,command,&#8230;</i></p>
<dd> Log the named commands to syslogd. </p>
<p> Examples of commands are CONNECT, HELO, EHLO, LHLO, MAIL, RCPT, VRFY, DATA, ., RSET, NOOP, and QUIT. Separate command names by white space or commas, and use quotes to protect white space from the shell. Command names are case-insensitive.</p>
<dt><code>-S start-string</code></p>
<dd> An optional string that is prepended to each message that is written to a dump file (see the dump file format description below). The following C escape sequences are supported:  (bell),  (backspace),  (formfeed), 
 (newline),  (carriage return), 	 (horizontal tab),  (vertical tab), \<i>ddd</i> (up to three octal digits) and \ (the backslash character).</p>
<dt><code>-t </code><i>timeout</i> (default: 100)</p>
<dd> Limit the time for receiving a command or sending a response. The time limit is specified in seconds.</p>
<dt><code>-T </code><i>windowsize</i></p>
<dd> Override the default TCP window size. To work around broken TCP window scaling implementations, specify a value &gt; 0 and &lt; 65536.</p>
<dt><code>-u </code><i>username</i></p>
<dd> Switch to the specified user privileges after opening the network socket and optionally changing the process root directory. This option is required when the process runs with super-user privileges. See also the <code>-R</code> option.</p>
<dt><code>-v</code></p>
<dd> Show the SMTP conversations.</p>
<dt><code>-w </code><i>delay</i></p>
<dd> Wait <i>delay</i> seconds before responding to a DATA command.</p>
<dt><code>-W </code><i>command:delay[:odds]</i></p>
<dd> Wait <i>delay</i> seconds before responding to <i>command</i>. If <i>odds</i> is also specified (a number between 1-99 inclusive), wait for a random multiple of <i>delay</i>. The random multiplier is equal to the number of times the program needs to roll a dice with a range of 0..99 inclusive, before the dice produces a result greater than or equal to <i>odds</i>.</p>
<dt>[<code>inet:</code>][<i>host</i>]:<i>port</i></p>
<dd> Listen on network interface <i>host</i> (default: any interface) TCP port <i>port</i>. Both <i>host</i> and <i>port</i> may be specified in numeric or symbolic form.</p>
<dt><code>unix:</code><i>pathname</i></p>
<dd> Listen on the UNIX-domain socket at <i>pathname</i>.</p>
<dt><i>backlog</i></p>
<dd> The maximum length the queue of pending connections, as defined by the <code><a href="/docs/linux/man/2-listen/">listen</a></code>(2) system call.</dl>
<h2>DUMP FILE FORMAT</h2>
<p> Each dumped message contains a sequence of text lines, terminated with the newline character. The sequence of information is as follows:</p>
<dl>
<dt>&bull;</p>
<dd> The optional string specified with the <code>-S</code> option.</p>
<dt>&bull;</p>
<dd> The <code>smtp-sink</code> generated headers as documented below.</p>
<dt>&bull;</p>
<dd> The message header and body as received from the SMTP client.</p>
<dt>&bull;</p>
<dd> An empty line.</dl>
<p> The format of the <code>smtp-sink</code> generated headers is as follows:</p>
<dl>
<dt><code>X-Client-Addr: </code><i>text</i></p>
<dd> The client IP address without enclosing []. An IPv6 address is prefixed with &quot;ipv6:&quot;. This record is always present.</p>
<dt><code>X-Client-Proto: </code><i>text</i></p>
<dd> The client protocol: SMTP, ESMTP or LMTP. This record is always present.</p>
<dt><code>X-Helo-Args: </code><i>text</i></p>
<dd> The arguments of the last HELO or EHLO command before this mail delivery transaction. This record is present only if the client sent a recognizable HELO or EHLO command before the DATA command.</p>
<dt><code>X-Mail-Args: </code><i>text</i></p>
<dd> The arguments of the MAIL command that started this mail delivery transaction. This record is present exactly once.</p>
<dt><code>X-Rcpt-Args: </code><i>text</i></p>
<dd> The arguments of an RCPT command within this mail delivery transaction. There is one record for each RCPT command, and they are in the order as sent by the client.</p>
<dt><code>Received: </code><i>text</i></p>
<dd> A message header for compatibility with mail processing software. This three-line header marks the end of the headers provided by <code>smtp-sink</code>, and is formatted as follows:</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>from </code><i>helo</i> ([<i>addr</i>])</p>
<dd> The HELO or EHLO command argument and client IP address. If the client did not send HELO or EHLO, the client IP address is used instead.</p>
<dt><code>by </code><i>host</i><code> (smtp-sink) with </code><i>proto</i><code> id </code><i>random</i><code>;</code></p>
<dd> The hostname specified with the <code>-h</code> option, the client protocol (see <code>X-Client-Proto</code> above), and the pseudo-random portion of the per-message capture file name.</p>
<dt><i>time-stamp</i></p>
<dd> A time stamp as defined in RFC 2822.</dl>
</dl>
</dl>
<h2>SEE ALSO</h2>
<pre>
<a href="//www.systutorials.com/docs/linux/man/1-smtp-source/">smtp-source</a>(1), SMTP/LMTP message generator
</pre>
<h2>LICENSE</h2>
<p> The Secure Mailer license must be distributed with this software.</p>
<h2>AUTHOR(S)</h2>
<pre>
Wietse Venema
IBM T.J. Watson Research
P.O. Box 704
Yorktown Heights, NY 10598, USA
Wietse Venema
Google, Inc.
111 8th Avenue
New York, NY 10011, USA
</pre>
<h2>Index</h2>
