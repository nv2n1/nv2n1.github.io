---
title: "anytermd(1)"
name: "anytermd"
section: "1"
letter: "a"
url: "/docs/linux/man/1-anytermd/"
description: "anytermd – A terminal-emulating HTTP daemon"
---

<h2>NAME</h2>
<p> anytermd &#8211; A terminal-emulating HTTP daemon</p>
<h2>SYNOPSIS</h2>
<p> anytermd [<code>&#8211;command</code> <i>arg</i>] [<code>&#8211;device</code> <i>arg</i>] [<code>&#8211;port</code> <i>arg</i>] [<code>&#8211;user</code> <i>arg</i>] [<code>&#8211;auth</code> <i>arg</i>] [<code>&#8211;charset</code> <i>arg</i>] [<code>&#8211;foreground</code>] [<code>&#8211;diff</code>] [<code>&#8211;nodiff</code>] [<code>&#8211;max-sessions</code> <i>arg</i>] [<code>&#8211;max-http-connections</code> <i>arg</i>] [<code>&#8211;local-only</code>] [<code>&#8211;name</code> <i>arg</i>] </p>
<p> anytermd &#8211;help</p>
<h2>DESCRIPTION</h2>
<p> Anyterm provides a terminal window on a web page, so you can run command-line programs on a machine even when the only access to it is over HTTP. </p>
<p> Anyterm consists of some Javascript on a web page, an XmlHttpRequest channel on standard ports back to the server, an HTTP proxy such as Apache&#8217;s mod_proxy and the Anyterm daemon. The daemon, anytermd, uses a pseudo-terminal to communicate with a shell or other application, and includes terminal emulation. Key presses are picked up by the Javscript which sends them to the daemon; changes to the emulated screen are sent from the daemon to the Javascript which updates its display. Performance is quite reasonable and SSL can be used to secure the connection. <i>For security reasons, it is highly recommended that anytermd NOT be exposed directly to the Internet!</i> See the section <code>SECURITY</code> below.</p>
<h2>OPTIONS</h2>
<p> Default values are indicated in parentheses ().</p>
<dl>
<dt><code>-c | &#8211;command</code> <i>arg</i> (=/bin/bash)</p>
<dd> Command to run in terminal</p>
<dt><code>-d | &#8211;device</code> <i>arg</i></p>
<dd> Device to connect to (e.g. serial port)</p>
<dt><code>-p | &#8211;port</code> <i>arg</i> (=8080)</p>
<dd> Port number to listen on</p>
<dt><code>-u | &#8211;user</code> <i>arg</i></p>
<dd> User to run as</p>
<dt><code>-a | &#8211;auth</code> <i>arg</i> (=none)</p>
<dd> Authorisation: none|null|trivial</p>
<dt><code>-s | &#8211;charset</code> <i>arg</i> (=ascii)</p>
<dd> Character set</p>
<dt><code>-f | &#8211;foreground</code></p>
<dd> run in foreground</p>
<dt><code>&#8211;diff</code></p>
<dd> Send only differences to browser</p>
<dt><code>-n | &#8211;nodiff</code></p>
<dd> Send whole screen to browser each time</p>
<dt><code>-m | &#8211;max-sessions</code> <i>arg</i> (=20)</p>
<dd> Maximum number of simultaneous sessions</p>
<dt><code>&#8211;max-http-connections</code> <i>arg</i> (=unlimited)</p>
<dd> Maximum number of simultaneous HTTP connections</p>
<dt><code>&#8211;local-only</code></p>
<dd> Accept connections only from localhost</p>
<dt><code>&#8211;name</code> <i>arg</i> (=anyterm)</p>
<dd> Name used for logging and pid file</p>
<dt><code>&#8211;help</code></p>
<dd> show help message</dl>
<h2>SECURITY</h2>
<p> <i>Do not run anytermd as root.</i> </p>
<p> Anyterm&#8217;s code has not been audited for security. It is almost certainly possible to cause it to crash by sending it invalid input, and experience suggests that this sort of weakness can also be exploited to allow arbitary code execution. </p>
<p> Note that all CGI applications and similar programs are subject to this sort of problem, though some are better written than others. The Anyterm code does not need run with a higher priviledge level than any other web application, so weaknesses in Anyterm do not put your system at any higher risk than weaknesses in any other web application would. </p>
<p> <i>Avoid exposing anytermd directly to the Internet.</i> </p>
<p> anytermd should be used only as a backend service, reachable only via a frontend HTTPS proxy, such as Apache, that requires authentication. <i><a rel="nofollow" href="http://anyterm.org/1.1/install.html">http://anyterm.org/1.1/install.html</a></i> gives examples of how to set this up. </p>
<p> A more complete and up-to-date discussion of security issues in anytermd can be found at <i><a rel="nofollow" href="http://anyterm.org/security.html">http://anyterm.org/security.html</a></i>.</p>
<h2>EXAMPLES</h2>
<p> If you just want to test Anyterm, you can do: </p>
<p> anytermd &#8211;local-only </p>
<p> and then connect to <a rel="nofollow" href="http://localhost:8080">http://localhost:8080</a> with your Javascript-enabled web browser. The brower should display a terminal window containing a bash command prompt owned by the user who started anytermd. </p>
<p> If you want to set up SSH-over-HTTP access on localhost:8022, you might run it as: </p>
<p> anytermd &#8211;command &quot;/usr/bin/ssh -o your-username [at] localhost&quot; &#8211;port 8022 &#8211;user nobody &#8211;charset utf-8 &#8211;local-only</p>
<h2>SEE ALSO</h2>
<p> Anyterm is more fully documented on its web site, <code><a rel="nofollow" href="http://anyterm.org/">http://anyterm.org/</a></code>. The web site may be more up-to-date than this man page.</p>
<h2>AUTHOR</h2>
<p> Anyterm is written by Phil Endecott. This man page was contributed by Eric Rossen. </p>
<h2>Index</h2>
