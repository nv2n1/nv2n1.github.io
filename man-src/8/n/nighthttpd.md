---
title: "nighthttpd(8)"
name: "nighthttpd"
section: "8"
letter: "n"
url: "/docs/linux/man/8-nighthttpd/"
description: "nighthttpd – a http server for nightviewd and telescoped"
---

<p>nighthttpd &#8211; a http server for nightviewd and telescoped</p>
<h2>Synopsis</h2>
<p>&nbsp;<wbr>nighthttpd&nbsp;<wbr>[options]</p>
<h2>Description</h2>
<p>The nighthttpd is a http server to provide internet access for nighthttpd and telescoped daemons of Nightview. It is designed as 1.0/http server with a few extensions to 1.1 (it is without keep-alieve support). This daemon is prepared for use in nightview including of a specific CGI support. It is not intended as a general http daemon. </p>
<p> The options are as follows:</p>
<dl>
<dt><code>-c</code></p>
<dd>A location of a configuration file. For example: /usr/local/etc/nightview.conf.</p>
<dt><code>-u</code></p>
<dd>User name to run under.</p>
<dt><code>-chroot</code></p>
<dd>Run in chroot environment.</p>
<dt><code>-h</code></p>
<dd>Host address.</p>
<dt><code>-p</code></p>
<dd>Listen port.</dl>
<h2>Security</h2>
<p>AuthKey in configuration file is used to control of access to the daemon. If the option is not present (eg. commented out), all clients are accepted. It the value is non-null, the clients are autenticated by Basic authentication scheme as is used by Internet&#8217;s browsers. It is highly reccomended to use any type of tunneling, when your are conecting via an unsecured network.</p>
<h2>Files</h2>
<dl>
<dt><code>/usr/local/etc/nightview.conf</code></p>
<dd>The configuration file.</dl>
<h2>See Also</h2>
<p><a href="/docs/linux/man/1-nightview/">nightview</a>(1). See the /usr/share/doc/nightview-doc directory for description. Homepage: <a rel="nofollow" href="http://www.physics.muni.cz/mb/nightview/,">http://www.physics.muni.cz/mb/nightview/,</a> <a href="http://www.sbig.com">http://www.sbig.com</a></p>
<h2>Author</h2>
<p>This manual page was written by F. Hroch &lt;hroch [at] physics.muni.cz&gt;, for the Debian GNU/Linux system (but may be used by others).</p>
