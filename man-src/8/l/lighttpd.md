---
title: "lighttpd(8)"
name: "lighttpd"
section: "8"
letter: "l"
url: "/docs/linux/man/8-lighttpd/"
description: "lighttpd – a fast, secure and flexible web server"
---

<p>lighttpd &#8211; a fast, secure and flexible web server</p>
<h2>Synopsis</h2>
<p><code>lighttpd</code> [<code>-ptDvVh</code>] <code>-f</code> <i>configfile</i> [<code>-m</code> <i>moduledir</i>]</p>
<h2>Description</h2>
<p><code>lighttpd</code> (pronounced &#8216;lighty&#8217;) is an advanced HTTP daemon that aims to be secure, fast, compliant and very flexible. It has been optimized for high performance. Its feature set includes, but is not limited to, FastCGI, CGI, basic and digest HTTP authentication, output compression, URL rewriting. </p>
<p> This manual page only lists the command line arguments. For details on how to configure <code>lighttpd</code> and its modules see the files in the doc-directory.</p>
<h2>Options</h2>
<p>The following options are supported:</p>
<dl>
<dt><code>-f&nbsp;<wbr></code> <i>configfile</i></dt>
<dd>Load configuration file <i>configfile</i>.</dd>
<dt><code>-m&nbsp;<wbr></code> <i>moduledir</i></dt>
<dd>Use <i>moduledir</i> as the directory that contains modules, instead of the default.</dd>
<dt><code>-p</code></dt>
<dd>Print the parsed configuration file in its internal form and exit.</dd>
<dt><code>-t</code></dt>
<dd>Test the configuration file for syntax errors and exit.</dd>
<dt><code>-D</code></dt>
<dd>Do not daemonize (go into background). The default is to daemonize.</dd>
<dt><code>-v</code></dt>
<dd>Show version and exit.</dd>
<dt><code>-V</code></dt>
<dd>Show compile-time features and exit.</dd>
<dt><code>-h</code></dt>
<dd>Show a brief help message and exit.</dd></dl>
<h2>Files</h2>
<dl>
<dt>/etc/lighttpd/lighttpd.conf</dt>
<dd>The standard location for the configuration file.</dd>
<dt>/var/run/lighttpd.pid</dt>
<dd>The standard location for the PID of the running <code>lighttpd</code> process.</dd></dl>
<h2>See Also</h2>
<p>Online Documentation: <a rel="nofollow" href="http://wiki.lighttpd.net/">http://wiki.lighttpd.net/</a> </p>
<p> <a href="/docs/linux/man/1-spawn-fcgi/">spawn-fcgi</a>(1) </p>
<p> <i>Hypertext Transfer Protocol &#8212; HTTP/1.1</i>, RFC 2616. </p>
<p> <i>HTTP Authentication: Basic and Digest Access Authentication</i>, RFC 2617. </p>
<p> <i>The Common Gateway Interface Version 1.1</i>, RFC 3875. </p>
<p> <i>The FastCGI specification</i>.</p>
<h2>Author</h2>
<p>Jan Kneschke &lt;jan [at] kneschke.de&gt;</p>
