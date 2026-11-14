---
title: "a2query(1)"
name: "a2query"
section: "1"
letter: "a"
url: "/docs/linux/man/1-a2query/"
description: "a2query – retrieve runtime configuration from a local Apache 2 HTTP server"
---

<h2 class="name">NAME</h2>
<p> a2query &#8211; retrieve runtime configuration from a local Apache 2 HTTP server </p>
<h2>SYNOPSIS</h2>
<p> <code>a2query</code> [-m [<i></i><font SIZE="-1"><i>MODULE</i></font><i></i>]] [-s [<i></i><font SIZE="-1"><i>SITE</i></font><i></i>]] [-c [<i></i><font SIZE="-1"><i>CONF</i></font><i></i>]] [-a] [-v] [-M] [-d] [-h]</p>
<h2>DESCRIPTION</h2>
<p> <code>a2query</code> is a program designed to retrieve configuration values from a locally available Apache 2 <font SIZE="-1">HTTP</font> web server. It was designed to be as robust as possible by returning feasible values even if the Apache 2 syntax validator fails. </p>
<p> This program is primarily meant to be used from maintainer scripts.</p>
<h2>OPTIONS</h2>
<dl>
<dt>-a</p>
<dd> Returns the Apache 2 &#8220;Module Magic Version&#8221; (<font SIZE="-1">API</font> version) number, the server was compiled with. The returned version does not contain any minor versions which are known to be compatible with the major version returned.</p>
<dt>-c [<i></i><font SIZE="-1"><i>CONF</i></font><i></i>]</p>
<dd> Checks whether the configuration <i></i><font SIZE="-1"><i>CONF</i></font><i></i> is enabled. If no argument was given, all enabled configuration files are being returned. <i></i><font SIZE="-1"><i>CONF</i></font><i></i> is compared by string comparison by ignoring a leading &#8220;mod_&#8221; prefix and possibly a &#8216;.conf&#8217; or &#8216;.load&#8217; suffix.</p>
<dt>-h</p>
<dd> Displays a brief summary how the program can be called and exits.</p>
<dt>-m [<i></i><font SIZE="-1"><i>MODULE</i></font><i></i>]</p>
<dd> Checks whether the module <i></i><font SIZE="-1"><i>MODULE</i></font><i></i> is enabled, The argument is interpreted in the same way, as for configuration files queried by the -c switch.</p>
<dt>-M</p>
<dd> Returns the currently enabled Apache 2 <font SIZE="-1">MPM</font> (Multi Processing Module).</p>
<dt>-s [<i></i><font SIZE="-1"><i>SITE</i></font><i></i>]</p>
<dd> Checks whether the module <i></i><font SIZE="-1"><i>SITE</i></font><i></i> is enabled, The argument is interpreted in the same way, as for configuration files queried by the -c switch.</p>
<dt>-v</p>
<dd> returns the currently installed Apache 2 <font SIZE="-1">HTTP</font> server version</p>
<dt>-q</p>
<dd> suppress any output. This is useful to invoke a2query from another script. This is useful if only the return code is of interest.</dl>
<h2>EXIT CODES</h2>
<p> <code>a2query</code> returns with a zero (0) exit status if the requested operation was effectuated successfully and with a non-zero status otherwise. In case of an error it leaves with error code 32 if a requested module, site or configuration was not found and 33 if a module, site or configuration was disabled by a maintainer script. However, exit status 1 is returned if the module was not found at all</p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/8-apache2ctl/">apache2ctl</a>(8), <a href="/docs/linux/man/8-apache2/">apache2</a>(8), <a href="/docs/linux/man/1-perl/">perl</a>(1)</p>
<h2>AUTHOR</h2>
<p> This manual and a2query was written by Arno Toell &lt;debian [at] toell.net&gt;. </p>
<h2>Index</h2>
