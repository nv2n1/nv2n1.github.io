---
title: "inetutils-logger(1)"
name: "inetutils-logger"
section: "1"
letter: "i"
url: "/docs/linux/man/1-inetutils-logger/"
description: "logger – make entries in the system log"
---

<p>GNU Network Utilities</p>
<h2 class="name">NAME</h2>
<p> <code>logger</code> &#8211; make entries in the system log </p>
<h2>SYNOPSIS</h2>
<p> <code>logger</code> [<i>options &#8230;</i> ] [<i>message &#8230;</i> ]</p>
<h2>DESCRIPTION</h2>
<p> <code>logger</code> provides a shell command interface to the <a href="/docs/linux/man/3-syslog/">syslog</a>(3) system log module.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-4, -ipv4</code></p>
<dd> Use IPv4 to connect to hosts.</p>
<dt><code>-6, -ipv6</code></p>
<dd> Use IPv6 to connect to hosts.</p>
<dt><code>-S , -source </code><i>ip</i></p>
<dd> Set source IP address.</p>
<dt><code>-h , -host </code><i>host</i></p>
<dd> Log to <i>host</i> instead of to the default /dev/log</p>
<dt><code>-u , -unix </code><i>sock</i></p>
<dd> Log to UNIX socket <i>sock</i> instead of /dev/log</p>
<dt><code>-i , -id </code>[<i>pid</i> ]</p>
<dd> Log the process id of the logger process with each line.</p>
<dt><code>-s , -stderr</code></p>
<dd> Log the message to standard error, as well as the system log.</p>
<dt><code>-f , -file </code><i>file</i></p>
<dd> Log the specified file.</p>
<dt><code>-p , -priority </code><i>pri</i></p>
<dd> Enter the message with the specified priority. The priority may be specified numerically or as a &quot;facility.level&quot; pair. For example, &quot;-p local3.info&quot; logs the message(s) as <i>info </i><code>rmational</code> level in the <i>local3</i> facility. The default is &quot;user.notice.&quot;</p>
<dt><code>-t , -tag </code><i>tag</i></p>
<dd> Mark every line in the log with the specified <i>tag </i></p>
<dt><code>&#8211;usage</code></p>
<dd> Display a short usage message.</p>
<dt><code>-?, -help</code></p>
<dd> Display a help list.</p>
<dt><code>-V, -version</code></p>
<dd> Display program version.</p>
<dt><i>message</i></p>
<dd> Write the message to log; if not specified, and the &#8211;<code>f</code> flag is not provided, standard input is logged.</dl>
<p> The <code>logger</code> utility exits 0 on success, and &gt;0 if an error occurs.</p>
<h2>EXAMPLES</h2>
<blockquote>
<pre>
logger System rebooted
logger -p local0.notice -t HOSTIDM -f /dev/idmc
</pre>
</blockquote>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/3-syslog/">syslog</a>(3), <a href="/docs/linux/man/8-syslogd/">syslogd</a>(8).</p>
<h2>STANDARDS</h2>
<p> The <code>logger</code> command is expected to be St -p1003.2 compatible. </p>
<h2>Index</h2>
