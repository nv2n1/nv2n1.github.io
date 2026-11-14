---
title: "tsung(1)"
name: "tsung"
section: "1"
letter: "t"
url: "/docs/linux/man/1-tsung/"
description: "tsung – A distributed multi-protocol load testing tool."
---

<h2>NAME</h2>
<p> tsung &#8211; A distributed multi-protocol load testing tool.</p>
<h2>SYNOPSIS</h2>
<p> <code>tsung</code> [ <code>-f configuration file</code> ] [ <code>-l log dir</code> ] [ <code>-m filename</code> ] [ <code>-r command</code> ] [ <code>-X directory</code> ] [ <code>-w delay</code> ] [ <code>-L lifetime</code> ] [ <code>-s</code> ] [ <code>-n</code> ] [ <code>-k</code> ] [ <code>-v</code> ] [ <code>-6</code> ] [ <code>-h</code> ] [ <code>start|stop|debug|status</code> ]</p>
<h2>DESCRIPTION</h2>
<p> <code>tsung</code> is a distributed load testing tool. It is protocol-independent and can currently be used to stress and benchmark HTTP, WebDAV, LDAP, PostgreSQL, MySQL and Jabber/XMPP servers. </p>
<p> It simulates user behaviour using an XML description file, reports many measurements in real time (statistics can be customized with transactions, and graphics generated using gnuplot). </p>
<p> For HTTP, it supports 1.0 and 1.1, has a proxy mode to record sessions, supports GET and POST methods, Cookies, and Basic WWW-authentication. It also has support for SSL. </p>
<p> Several config examples can be found in <i>/usr/share/doc/tsung/examples/</i>.</p>
<dl>
<dt><code>start</code></p>
<dd> start tsung load testing</p>
<dt><code>debug</code></p>
<dd> start tsung with an interactive erlang shell</p>
<dt><code>stop</code></p>
<dd> stop tsung</p>
<dt><code>status</code></p>
<dd> print current status of a running instance of tsung (must be run on the controller host)</dl>
<h2>MANUAL</h2>
<p> A manual should be available at <i>/usr/share/doc/tsung/user_manual.html</i>. It is also available online at </p>
<dl>
<dt>
<dd>
<pre>
<a rel="nofollow" href="http://tsung.erlang-projects.org/user_manual.html">http://tsung.erlang-projects.org/user_manual.html</a>
</pre>
</dl>
<h2>OPTIONS</h2>
<dl>
<dt><code>-f filename</code></p>
<dd> specifies the configuration file to use. The default file name is <i>~/.tsung/tsung.xml</i>. Use &#8211; for standard input</p>
<dt><code>-l logdir</code></p>
<dd> Specifies the log directory to use. The default log dir name is <i>~/.tsung/log/YYYYMMDD-HHMM/</i></p>
<dt><code>-m monitoring_file</code></p>
<dd> Specifies the monitoring log file name to use. The default log file name is <i>tsung.log</i>. Use &#8211; for standard output</p>
<dt><code>-r command</code></p>
<dd> Specifies an alternative to ssh (rsh for ex.) for starting a slave node on a remote host</p>
<dt><code>-i id</code></p>
<dd> set controller id (default is empty). Needed to start several controllers on the same host.</p>
<dt><code>-F</code></p>
<dd> Use long names for erlang nodes (FQDN)</p>
<dt><code>-s</code></p>
<dd> Enable erlang smp on client nodes</p>
<dt><code>-p</code></p>
<dd> set maximum erlang processes per vm (default is 250000)</p>
<dt><code>-X directory</code></p>
<dd> add additional erlang load paths (multiple -X arguments allowed)</p>
<dt><code>-L lifetime</code></p>
<dd> SSL session lifetime in seconds (600 sec by default)</p>
<dt><code>-w delay</code></p>
<dd> warmup delay in seconds (1 sec by default)</p>
<dt><code>-v</code></p>
<dd> Show version</p>
<dt><code>-n</code></p>
<dd> disable web GUI</p>
<dt><code>-k</code></p>
<dd> keep web GUI (and controller) alive after the test has finished</p>
<dt><code>-6</code></p>
<dd> Use IPv6 for tsung internal communications</p>
<dt><code>-h</code></p>
<dd> Show usage</dl>
<h2>BUGS</h2>
<p> Please reports bugs to the mailing list &lt;tsung-users [at] process-one.net&gt;, see </p>
<dl>
<dt>
<dd>
<pre>
<a rel="nofollow" href="https://lists.process-one.net/mailman/listinfo/tsung-users">https://lists.process-one.net/mailman/listinfo/tsung-users</a>
</pre>
</dl>
<p> for archives. You can also use the issue tracker </p>
<dl>
<dt>
<dd>
<pre>
<a rel="nofollow" href="https://github.com/processone/tsung/issues">https://github.com/processone/tsung/issues</a>
</pre>
</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-erlang/">erlang</a></code>(3)</p>
<h2>AUTHORS</h2>
<p> <code>Tsung</code> is written by Nicolas Niclausse &lt;nicolas [at] niclux.org&gt;. Contributors list is available in <i>/usr/share/doc/tsung/CONTRIBUTORS</i> </p>
<h2>Index</h2>
