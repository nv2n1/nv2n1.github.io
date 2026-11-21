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
<dt><code>-4, -ipv4</code></dt>
<dd> Use IPv4 to connect to hosts.</dd>
<dt><code>-6, -ipv6</code></dt>
<dd> Use IPv6 to connect to hosts.</dd>
<dt><code>-S , -source </code><i>ip</i></dt>
<dd> Set source IP address.</dd>
<dt><code>-h , -host </code><i>host</i></dt>
<dd> Log to <i>host</i> instead of to the default /dev/log</dd>
<dt><code>-u , -unix </code><i>sock</i></dt>
<dd> Log to UNIX socket <i>sock</i> instead of /dev/log</dd>
<dt><code>-i , -id </code>[<i>pid</i> ]</dt>
<dd> Log the process id of the logger process with each line.</dd>
<dt><code>-s , -stderr</code></dt>
<dd> Log the message to standard error, as well as the system log.</dd>
<dt><code>-f , -file </code><i>file</i></dt>
<dd> Log the specified file.</dd>
<dt><code>-p , -priority </code><i>pri</i></dt>
<dd> Enter the message with the specified priority. The priority may be specified numerically or as a &quot;facility.level&quot; pair. For example, &quot;-p local3.info&quot; logs the message(s) as <i>info </i><code>rmational</code> level in the <i>local3</i> facility. The default is &quot;user.notice.&quot;</dd>
<dt><code>-t , -tag </code><i>tag</i></dt>
<dd> Mark every line in the log with the specified <i>tag </i></dd>
<dt><code>&#8211;usage</code></dt>
<dd> Display a short usage message.</dd>
<dt><code>-?, -help</code></dt>
<dd> Display a help list.</dd>
<dt><code>-V, -version</code></dt>
<dd> Display program version.</dd>
<dt><i>message</i></dt>
<dd> Write the message to log; if not specified, and the &#8211;<code>f</code> flag is not provided, standard input is logged.</dd></dl>
<p> The <code>logger</code> utility exits 0 on success, and &gt;0 if an error occurs.</p>
<h2>EXAMPLES</h2>
<blockquote>
<pre>
logger System rebooted
logger -p local0.notice -t HOSTIDM -f /dev/idmc
</pre>
</blockquote>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/3-syslog/">syslog</a>(3), syslogd(8).</p>
<h2>STANDARDS</h2>
<p> The <code>logger</code> command is expected to be St -p1003.2 compatible. </p>
