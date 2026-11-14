---
title: "tsung-recorder(1)"
name: "tsung-recorder"
section: "1"
letter: "t"
url: "/docs/linux/man/1-tsung-recorder/"
description: "tsung-recorder – Proxy recorder for the tsung load testing tool."
---

<h2>NAME</h2>
<p> tsung-recorder &#8211; Proxy recorder for the tsung load testing tool.</p>
<h2>SYNOPSIS</h2>
<p> <code>tsung-recorder</code> [ <code>-l log file</code> ] [ <code>-r command</code> ] [ <code>-p plugin</code> ] [ <code>-L listen port</code> ] [ <code>-I IP</code> ] [ <code>-P port</code> ] [ <code>-u </code> ] [ <code>start|stop|restart|record_tag</code> ]</p>
<h2>DESCRIPTION</h2>
<p> <code>tsung</code> is a distributed load testing tool. It is protocol-independent and can currently be used to stress and benchmark HTTP, WebDAV, LDAP, PostgreSQL, MySQL and Jabber/XMPP servers. <code>tsung-recorder</code> can be used to record sessions (only for HTTP, WebDAV and Postgresql) that can be edited and replayed later by tsung </p>
<p> tsung-recorder is a proxy that records a session in the tsung native XML format; it can be used by your favorite client (browser in the case of the http plugin).</p>
<dl>
<dt><code>start</code></p>
<dd> start the proxy recorder (listening port is 8090). By default the HTTP recorder is started. With the <code>-p</code> option, you can select another plugin. The resulting files will be created as <i>~/.tsung/tsung_recorderYYYMMDD-HH:MM.xml</i>; if it doesn&#8217;t work, take a look at <i>~/.tsung/log/tsung.log-tsunami_recorder [at] hostname</i></p>
<dt><code>stop</code></p>
<dd> stop the proxy recorder</p>
<dt><code>record_tag value</code></p>
<dd> add a string (comment or tag) while recording a session. This is useful for example to add transaction tag while recording a session.</dl>
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
<dt><code>-l logfile</code></p>
<dd> Specifies the log file to use. The default log file name is <i>~/tsung/log/tsung.log</i></p>
<dt><code>-p plugin</code></p>
<dd> Specifies the plugin used for the recorder. Default is http, available: http, pgsql, webdav</p>
<dt><code>-L port</code></p>
<dd> Listening port for the recorder. Default is 8090</p>
<dt><code>-I IP</code></p>
<dd> For the pgsql recorder (or parent proxy): server IP. default is 127.0.0.1</p>
<dt><code>-P port</code></p>
<dd> For the pgsql recorder (or parent proxy): server port. Default is 5432</p>
<dt><code>-u</code></p>
<dd> For the http recorder: use a parent proxy</dl>
<h2>BUGS</h2>
<p> Please reports bugs to the mailing list &lt;tsung-users [at] process-one.net&gt;, see </p>
<dl>
<dt>
<dd>
<pre>
<a rel="nofollow" href="https://lists.process-one.net/mailman/listinfo/tsung-users">https://lists.process-one.net/mailman/listinfo/tsung-users</a>
</pre>
</dl>
<p> for archives.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-erlang/">erlang</a></code>(3) and <code><a href="/docs/linux/man/1-tsung/">tsung</a></code>(1)</p>
<h2>AUTHORS</h2>
<p> <code>Tsung</code> is written by Nicolas Niclausse &lt;nicolas [at] niclux.org&gt;. Contributors list is available in <i>/usr/share/doc/tsung/CONTRIBUTORS</i> </p>
<h2>Index</h2>
