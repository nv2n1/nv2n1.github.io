---
title: "clamd(8)"
name: "clamd"
section: "8"
letter: "c"
url: "/docs/linux/man/8-clamd/"
description: "clamd – an anti-virus daemon"
---

<p>clamd &#8211; an anti-virus daemon</p>
<h2>Synopsis</h2>
<p>clamd [options]</p>
<h2>Description</h2>
<p>The daemon listens for incoming connections on Unix and/or TCP socket and scans files or directories on demand. It reads the configuration from /etc/clamd.conf</p>
<h2>Commands</h2>
<p>It&#8217;s recommended to prefix clamd commands with the letter <code>z</code> (eg. zSCAN) to indicate that the command will be delimited by a NULL character and that clamd should continue reading command data until a NULL character is read. The null delimiter assures that the complete command and its entire argument will be processed as a single command. Alternatively commands may be prefixed with the letter <code>n</code> (e.g. nSCAN) to use a newline character as the delimiter. Clamd replies will honour the requested terminator in turn. If clamd doesn&#8217;t recognize the command, or the command doesn&#8217;t follow the requirements specified below, it will reply with an error message, and close the connection. </p>
<p> Clamd recognizes the following commands: </p>
<dl>
<dt><code>PING</code></p>
<dd>Check the server&#8217;s state. It should reply with &quot;PONG&quot;.</p>
<dt><code>VERSION</code></p>
<dd>Print program and database versions.</p>
<dt><code>RELOAD</code></p>
<dd>Reload the virus databases.</p>
<dt><code>SHUTDOWN</code></p>
<dd>Perform a clean exit.</p>
<dt><code>SCAN file/directory</code></p>
<dd>Scan a file or a directory (recursively) with archive support enabled (if not disabled in clamd.conf). A full path is required.</p>
<dt><code>CONTSCAN file/directory</code></p>
<dd>Scan file or directory (recursively) with archive support enabled and don&#8217;t stop the scanning when a virus is found.</p>
<dt><code>MULTISCAN file/directory</code></p>
<dd>Scan file in a standard way or scan directory (recursively) using multiple threads (to make the scanning faster on SMP machines).</p>
<dt><code>ALLMATCHSCAN file/directory</code></p>
<dd>ALLMATCHSCAN works just like SCAN except that it sets a mode where scanning continues after finding a match within a file.</p>
<dt><code>INSTREAM</code></p>
<dd>It is mandatory to prefix this command with <code>n</code> or <code>z</code>. </p>
<p> Scan a stream of data. The stream is sent to clamd in chunks, after INSTREAM, on the same socket on which the command was sent. This avoids the overhead of establishing new TCP connections and problems with NAT. The format of the chunk is: &#8216;&lt;length&gt;&lt;data&gt;&#8217; where &lt;length&gt; is the size of the following data in bytes expressed as a 4 byte unsigned integer in network byte order and &lt;data&gt; is the actual chunk. Streaming is terminated by sending a zero-length chunk. Note: do not exceed StreamMaxLength as defined in clamd.conf, otherwise clamd will reply with <code>INSTREAM size limit exceeded</code> and close the connection.</p>
<dt><code>FILDES</code></p>
<dd>It is mandatory to newline terminate this command, or prefix with <code>n</code> or <code>z</code>. </p>
<p> This command only works on UNIX domain sockets. Scan a file descriptor. After issuing a FILDES command a subsequent rfc2292/bsd4.4 style packet (with at least one dummy character) is sent to clamd carrying the file descriptor to be scanned inside the ancillary data. Alternatively the file descriptor may be sent in the same packet, including the extra character.</p>
<dt><code>STATS</code></p>
<dd>It is mandatory to newline terminate this command, or prefix with <code>n</code> or <code>z</code>, it is recommended to only use the <code>z</code> prefix. </p>
<p> Replies with statistics about the scan queue, contents of scan queue, and memory usage. The exact reply format is subject to change in future releases.</p>
<dt><code>IDSESSION, END</code></p>
<dd>It is mandatory to prefix this command with <code>n</code> or <code>z</code>, and all commands inside IDSESSION must be prefixed. </p>
<p> Start/end a clamd session. Within a session multiple SCAN, INSTREAM, FILDES, VERSION, STATS commands can be sent on the same socket without opening new connections. Replies from clamd will be in the form &#8216;&lt;id&gt;: &lt;response&gt;&#8217; where &lt;id&gt; is the request number (in ascii, starting from 1) and &lt;response&gt; is the usual clamd reply. The reply lines have same delimiter as the corresponding command had. Clamd will process the commands asynchronously, and reply as soon as it has finished processing. </p>
<p> Clamd requires clients to read all the replies it sent, before sending more commands to prevent send() deadlocks. The recommended way to implement a client that uses IDSESSION is with non-blocking sockets, and a select()/poll() loop: whenever send would block, sleep in select/poll until either you can write more data, or read more replies. <i>Note that using non-blocking sockets without the select/poll loop and alternating recv()/send() doesn&#8217;t comply with clamd&#8217;s requirements.</i> </p>
<p> If clamd detects that a client has deadlocked, it will close the connection. Note that clamd may close an IDSESSION connection too if you don&#8217;t follow the protocol&#8217;s requirements. The client can use the PING command to keep the connection alive.</p>
<dt><code>VERSIONCOMMANDS</code></p>
<dd>It is mandatory to prefix this command with either <code>n</code> or <code>z</code>. It is recommended to use <code>nVERSIONCOMMANDS</code>. </p>
<p> Print program and database versions, followed by &quot;| COMMANDS:&quot; and a space-delimited list of supported commands. Clamd &lt;0.95 will recognize this as the VERSION command, and reply only with their version, without the commands list. </p>
<p> This command can be used as an easy way to check for IDSESSION support for example.</dl>
<dl>
<dt><code>DEPRECATED COMMANDS</code></p>
<dd>
<dt><code>STREAM</code></p>
<dd>Scan stream &#8211; on this command clamd will return &quot;PORT number&quot; you should connect to and send data to scan. (<code>DEPRECATED</code>, use INSTREAM instead)</dl>
<dl>
<dt><code>NOT SUPPORTED COMMANDS</code></p>
<dd>
<dt><code>SESSION, END</code></p>
<dd>Start/end a clamd session which will allow you to run multiple commands per TCP session. (use IDSESSION instead)</dl>
<h2>Options</h2>
<dl>
<dt><code>-h, &#8211;help</code></p>
<dd>Output help information and exit.</p>
<dt><code>-V, &#8211;version</code></p>
<dd>Print the version number and exit.</p>
<dt><code>-c FILE, &#8211;config-file=FILE</code></p>
<dd>Read configuration from FILE.</dl>
<h2>Signals</h2>
<p>Clamd recognizes the following signals:</p>
<dl>
<dt><code>SIGHUP</code></p>
<dd>Reopen the logfile.</p>
<dt><code>SIGUSR2</code></p>
<dd>Reload the signature databases.</p>
<dt><code>SIGTERM</code></p>
<dd>Perform a clean exit.</dl>
<h2>Files</h2>
<p>/etc/clamd.conf</p>
<h2>Credits</h2>
<p>Please check the full documentation for credits.</p>
<h2>Author</h2>
<p>Tomasz Kojm &lt;tkojm [at] clamav.net&gt;</p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/5-clamd-conf/">clamd.conf</a>(5), <a href="/docs/linux/man/1-clamdscan/">clamdscan</a>(1), <a href="/docs/linux/man/1-freshclam/">freshclam</a>(1), <a href="/docs/linux/man/5-freshclam-conf/">freshclam.conf</a>(5), <a href="/docs/linux/man/8-clamav-milter/">clamav-milter</a>(8) </p>
