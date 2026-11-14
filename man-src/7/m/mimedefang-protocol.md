---
title: "mimedefang-protocol(7)"
name: "mimedefang-protocol"
section: "7"
letter: "m"
url: "/docs/linux/man/7-mimedefang-protocol/"
description: "mimedefang-protocol – Conventions used by"
---

<p>mimedefang-protocol &#8211; Conventions used by <code></p>
<p><a href="/docs/linux/man/8-mimedefang/">mimedefang</a></code>(8) to communicate with filter programs. </p>
<h2>Description</h2>
<p><code><a href="/docs/linux/man/8-mimedefang/">mimedefang</a></code>(8) and <code><a href="/docs/linux/man/8-mimedefang-multiplexor/">mimedefang-multiplexor</a></code>(8) provide a simplified mechanism for hooking scripts and programs into Sendmail&#8217;s milter API. The milter API is multi-threaded and written in C; <code>mimedefang</code> lets you write single-threaded filters written in the language of your choice. Some of the flexibility and speed of milter is sacrificed, but the ease of writing filters more than compensates for this slight loss. This manual describes how <code>mimedefang</code> communicates with the filter program, and gives you enough information to write your own filter program as a replacement for <code>mimedefang.pl</code> if you wish. </p>
<h2>Protocol Overview</h2>
<p>The protocol is a simple file-based protocol. For each invocation of a filter, <code>mimedefang</code> creates a unique working directory and populates it with files. It calls the filter, which is expected to populate the working directory with more files, which communicate the scan results back to <code>mimedefang</code>. This simple mechanism allows you to easily write filters in scripting languages without worrying about C-level details.</p>
<h2>Filter Invocation</h2>
<p>The filter program may be invoked in one of five ways: </p>
<dl>
<dt><i>filter_prog</i> <i>directory</i></p>
<dd>If the program is invoked with a single argument which is an absolute path name (called the <code>working directory</code>, the program is expected to perform filtering in that directory and then exit. </p>
<dt><i>filter_prog</i> <code>-server</code></p>
<dd>If the program is invoked with the single argument <code>-server</code>, it is expected to run as a server. See SERVER MODE for details. </p>
<dt><i>filter_prog</i> <code>-serveru</code></p>
<dd>If the program is invoked with the single argument <code>-serveru</code>, it is expected to run as a server. In addition, anything it prints to file descriptor 3 is used to update the &quot;slave status&quot; field in the multiplexor. This lets the filter inform administrators exactly what it is doing. (See the <code>-Z</code> option to <code>mimedefang-multiplexor</code>.) </p>
<dt><i>filter_prog</i> <code>-embserver</code></p>
<dd>Similar to <code>-server</code>, but used by the embedded Perl code. The program should run any initialization routines and then exit. The multiplexor will subsequently call the Perl routine <code>do_main_loop</code> when it is time for the slave to begin running in server mode. </p>
<dt><i>filter_prog</i> <code>-embserveru</code></p>
<dd>Similar to <code>-embserver</code> with the additional magic of updating the slave status from data written to file descriptor 3. </p>
</dl>
<h2>Initial File Layout</h2>
<p>When the filter begins a scan, it should change directories to the working directory. In that directory, it will find the following files. </p>
<dl>
<dt><code>INPUTMSG</code></p>
<dd>A file containing the complete input e-mail message, including headers. </p>
<dt><code>HEADERS</code></p>
<dd>A file containing just the headers, one per line. Headers which are continued over several lines in the original message are collapsed into a single line in this file. </p>
<dt><code>COMMANDS</code></p>
<dd>A file containing a list of commands. Each command is a single letter and may be followed by arguments. Each command is on its own line. </p>
</dl>
<h2>The Commands File</h2>
<p>All commands have their arguments encoded as follows: All characters outside the range 33 to 126 ASCII, as well as the characters &quot;%&quot;, &quot;\&quot;, &quot;&#8217;&quot; and double-quote, are replaced by a percent sign followed by two hex digits specifying the character&#8217;s numerical value. The filter must un-escape the arguments when it reads the COMMANDS file. </p>
<p> The commands from the C to Perl filters are: </p>
<dl>
<dt><code>S</code><i>sender</i></p>
<dd>The sender of the message. </p>
<dt><code>s</code><i>esmtp_arg</i></p>
<dd>An ESMTP argument associated with the sender (such as SIZE=54432). There is one <code>s</code> line for each ESMTP argument. </p>
<dt><code>U</code><i>subject</i></p>
<dd>The message subject. </p>
<dt><code>X</code><i>message_id</i></p>
<dd>The Message-ID. </p>
<dt><code>R</code><i>recipient</i> <i>mailer</i> <i>host</i> <i>addr</i></p>
<dd>A recipient. There is one <code>R</code> line for each recipient. The <i>mailer</i>, <i>host</i> and <i>addr</i> parts of the line are the values of the Sendmail {rcpt_mailer}, {rcpt_host} and {rcpt_addr} macros if they are available, or &quot;?&quot; if not. </p>
<dt><code>r</code><i>esmtp_arg</i></p>
<dd>An ESMTP argument associated with the <i>most recent</i> recipient (such as NOTIFY=never). There is one <code>r</code> line for each SMTP argument. </p>
<dt><code>!</code></p>
<dd>If this command is present, there are suspicious characters in the message headers. </p>
<dt><code>?</code></p>
<dd>If this command is present, there are suspicious characters in the message body. </p>
<dt><code>I</code><i>host_addr</i></p>
<dd>The SMTP relay host&#8217;s IP address in dotted-quad notation. </p>
<dt><code>i</code><i>identifier</i></p>
<dd>An identifier generated by MIMEDefang. On a given host, this identifier is very likely to be unique over a timespan of about 24 years. </p>
<dt><code>J</code><i>host_addr</i></p>
<dd>The &quot;real&quot; SMTP relay host&#8217;s IP address in dotted-quad notation. Multi-stage MIMEDefang relays can use a special IP validation header so that even the innermost MIMEDefang relay can see the &quot;original&quot; relay&#8217;s IP address. </p>
<dt><code>H</code><i>host_name</i></p>
<dd>The SMTP relay host name. </p>
<dt><code>E</code><i>argument</i></p>
<dd>The argument to the SMTP &quot;EHLO&quot; or &quot;HELO&quot; command. </p>
<dt><code>Q</code><i>qid</i></p>
<dd>The message&#8217;s Sendmail queue-ID. </p>
<dt><code>=</code><i>macro</i> <i>val</i></p>
<dd>Set the value of the specified Sendmail macro to <i>val</i>. Both <i>macro</i> and <i>val</i> are percent-encoded, but the single space character between them is not. </p>
</dl>
<h2>Filter Operation</h2>
<p>When the filter performs a scan, it can make use of all the information in the files mentioned previously. If the filter needs temporary working files, it should create a subdirectory under the working directory for its own use. In this case, you do not have to clean up your working files, because <code>mimedefang</code> deletes the working directory when the filter returns.</p>
<h2>Final File Layout</h2>
<p>The filter communicates the results of the scan back to <code>mimedefang</code> by creating additional files in the working directory. The most important file is called RESULTS, and it contains a list of one-letter, one-line commands back to the filter. As usual, command arguments are percent-escaped. The commands from the filter back to <code>mimedefang</code> are: </p>
<dl>
<dt><code>B</code><i>code</i> <i>dsn</i> <i>reply_text</i></p>
<dd>Bounce (reject) the message with the specified SMTP reply code, DSN code and reply text. </p>
<dt><code>D</code></p>
<dd>Silently discard the message and pretend it was delivered. </p>
<dt><code>T</code><i>code</i> <i>dsn</i> <i>reply_text</i></p>
<dd>Return an SMTP temporary failure code with the specified SMTP code, DSN and reply text. </p>
<dt><code>C</code></p>
<dd>Replace the message body. If this command is present, the file NEWBODY must contain the new message body. </p>
<dt><code>M</code><i>header_val</i></p>
<dd>Replace the MIME Content-Type header with a new value. Used to change MIME boundaries or convert non-MIME to MIME messages. </p>
<dt><code>H</code><i>header</i> <i>val</i></p>
<dd>Add a new header <i>header</i> with value <i>val</i>. The <i>header</i> should not contain a colon. Each of <i>header</i> and <i>val</i> is percent-escaped, but the single space between them is not. </p>
<dt><code>N</code><i>header</i> <i>index</i> <i>val</i></p>
<dd>Adds a new header <i>header</i> with value <i>val</i> in position <i>index</i>. An index of zero specifies that the new header should be prepended before all existing headers. </p>
<dt><code>I</code><i>header</i> <i>index</i> <i>val</i></p>
<dd>Replace the <i>index&#8217;th</i> occurrence of <i>header</i> with value <i>val</i>. The <i>index</i> is 1-based. The <i>header</i> should not contain a colon. Each of <i>header</i>, <i>index</i> and <i>val</i> is percent-escaped, but the single space between them is not. </p>
<dt><code>J</code><i>header</i> <i>index</i></p>
<dd>Delete the <i>index</i>&#8216;th occurrence of <i>header</i>. </p>
<dt><code>R</code><i>recip</i></p>
<dd>Add a new recipient <i>recip</i> to the message. </p>
<dt><code>S</code><i>recip</i></p>
<dd>Delete <i>recip</i> from the list of message recipients. </p>
<dt><code>f</code><i>sender</i></p>
<dd>Change the envelope sender to <i>sender</i>. This is only supported by Sendmail 8.14.0 and higher. </p>
<dt><code>F</code></p>
<dd>Indicate that we have finished issuing commands. Anything after an F line is ignored. </p>
</dl>
<h2>Server Mode</h2>
<p>In server mode, <code>mimedefang-multiplexor</code> runs the filter program continuously in a server loop. The filter program reads commands from standard input, and writes results to standard output. The filter program <i>must</i> exit shortly after it sees EOF on its standard input. If it does not exit within 10 seconds, it will be terminated with SIGTERM. If that still does not work, then after a further 10 seconds, it is killed with SIGKILL. </p>
<dl>
<dt><code>SERVER COMMANDS</code></p>
<dd>All server commands are single line commands. Each command is followed by a space-separated list of arguments; each argument is percent-encoded. The commands defined are: </p>
<dt><code>ping</code></p>
<dd>Elicits a reply of &quot;PONG&quot; from the server. </p>
<dt><code>scan </code><i>queue_id</i> <i>dir</i></p>
<dd>Run a scan for the mail identiefied by the Sendmail queue-ID <i>queue_id</i> in the directory <i>dir</i>. The command is terminated with a newline. The server must write a newline-terminated &quot;ok&quot; if the scan completed successfully, or &quot;error: msg&quot; if something went wrong. </p>
<dt><code>relayok </code><i>ip_addr</i> <i>hostname</i> <i>client_port</i> <i>daemon_ip</i> <i>daemon_port</i></p>
<dd>Test whether or not to accept a connection from the specified host. The server must write &quot;ok 1&quot; if we will accept the connection, or &quot;ok 0 error_message code dsn&quot; if not. It can indicate a temporary failure by writing &quot;ok -1 error_message code dsn&quot;. Note that even if the connection is accepted, a later scan can still reject the message based on other criteria. &quot;ip_addr&quot; is the IP address of the relay and &quot;hostname&quot; is the hostname (if it could be determined; otherwise, the IP address in square brackets). </p>
<dt><code>helook </code><i>ip_addr</i> <i>hostname</i> <i>helo_string</i> <i>client_port</i> <i>daemon_ip</i> <i>daemon_port</i></p>
<dd>Test whether or not to accept the HELO/EHLO command. The server must write &quot;ok 1&quot; if we will accept the mail attempt, or &quot;ok 0 error_message code dsn&quot; if not. &quot;ok -1 error_message code dsn&quot; indicates a temporary failure. <i>helo_string</i> is the argument to the HELO/EHLO command. The remaining arguments have the same meaning as in <code>relayok</code>. </p>
<dt><code>senderok </code><i>sender_addr</i> <i>ip_addr</i> <i>hostname</i> <i>helo_string</i> <i>dir</i> <i>queue_id</i> [<i>esmtp_args</i>&#8230;]</p>
<dd>Test whether or not to accept mail from the specified sender. The server must write &quot;ok 1&quot; if we will accept the mail attempt, or &quot;ok 0 error_message code dsn&quot; if not. &quot;ok -1 error_message code dsn&quot; indicates a temporary failure. Note that even if the sender is accepted, a later scan can still reject the message based on other criteria. &quot;sender_addr&quot; is the sender&#8217;s e-mail address. The &quot;ip_addr&quot; and &quot;hostname&quot; arguments are as in <code>relayok</code>. &quot;helo_string&quot; is the argument to the SMTP HELO/EHLO command. &quot;dir&quot; is the MIMEDefang spool directory, and &quot;queue_id&quot; is the Sendmail queue identifier. </p>
<p> The optional &quot;esmtp_args&quot; are space-separated, percent-encoded ESMTP arguments supplied with the MAIL FROM: command. </p>
<dt><code>recipok </code><i>recip_addr</i> <i>sender_addr</i> <i>ip_addr</i> <i>hostname</i> <i>first_recip</i> <i>helo_string</i> <i>dir</i> <i>queue_id</i> [<i>esmtp_args</i>&#8230;]</p>
<dd>Test whether or not to accept mail for the specified recipient. The server must write &quot;ok 1&quot; if we will accept it, or &quot;ok 0 error_message code dsn&quot; if not. ok -1 error_message code dsn&quot; indicates a temporary-failure. </p>
<p> &quot;recip_addr&quot; is the argument to the RCPT TO: command, and &quot;first_recip&quot; is the argument to the first RCPT TO: command for this message. Other arguments are as in <code>senderok</code>. </p>
<dt><code>map </code><i>map_name</i> <i>key</i></p>
<dd>If you are using a map socket (the <code>-N</code> option to <code>mimedefang-multiplexor</code>), then the server should look up the key <i>key</i> in the map <i>map_name</i>. The server should print a single line to standard output. The first word on the line should be one of OK, NOTFOUND, TEMP, TIMEOUT or PERM, indicating a successful lookup, absence of the key, a temporary failure, a timeout or a permanent failure, respectively. This should be followed by a space and a percent-encoded string representing the value of the key (if it was found) or an optional error message (if something went wrong.) </p>
<dt><code>tick </code><i>band</i></p>
<dd>The filter should run <code>filter_tick</code> with the specified <i>band</i> argument. It should print a single line to standard output: </p>
<p> tock <i>band</i> </p>
<dt><code>Additional Commands</code></p>
<dd>The filter can define a function <code>filter_unknown_cmd</code> that can extend the list of server commands. If you do this, make sure all of your commands start with an upper-case letter to avoid conflicts if more built-in commands are defined in the future. </p>
<dt><code>SERVER REPLIES</code></p>
<dd>The reply codes are: </p>
<dt><code>ok [</code><i>return_code</i>] [<i>parameters</i>]</p>
<dd>The operation completed successfully. Some operations have an associated return code, and possibly other parameters as well. See the source code for the gory details. </p>
<dt><code>error: </code><i>Message</i></p>
<dd>The operation failed. <i>Message</i> may give additional details. </p>
</dl>
<p> In server mode, you should <i>not</i> write anything to standard output except reply codes, or the multiplexor will become confused. You should <i>not</i> terminate the program in server mode; simply echo an <code>error:</code> reply and return to the server loop. </p>
<p> When you send a reply code back to the multiplexor, be sure to terminate it with a newline, and to flush standard output. If your program uses the Standard I/O library, standard output may not be flushed immediately, and <code>mimedefang-multiplexor</code> will wait forever for the filter&#8217;s reply, and eventually kill the filter on the assumption it has hung up. </p>
<p> In server mode, if the filter program receives a SIGINT signal, it must terminate. This is used by <code>mimedefang-multiplexor</code> to terminate slaves after they have processed a given number of e-mail messages.</p>
<h2>Author</h2>
<p><code>mimedefang</code> was written by Dianne Skoll &lt;dfs [at] roaringpenguin.com&gt;. The <code>mimedefang</code> home page is <i><a rel="nofollow" href="http://www.mimedefang.org/">http://www.mimedefang.org/</a></i>.</p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/8-mimedefang-pl/">mimedefang.pl</a>(8), <a href="/docs/linux/man/8-mimedefang/">mimedefang</a>(8), <a href="/docs/linux/man/8-mimedefang-multiplexor/">mimedefang-multiplexor</a>(8), <a href="/docs/linux/man/5-mimedefang-filter/">mimedefang-filter</a>(5) </p>
