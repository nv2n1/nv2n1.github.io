---
title: "yum-updatesd-conf(5)"
name: "yum-updatesd-conf"
section: "5"
letter: "y"
url: "/docs/linux/man/5-yum-updatesd-conf/"
description: "yum-updatesd.conf – Configuration file for yum-updatesd(8)."
---

<p><code>yum-updatesd.conf</code> &#8211; Configuration file for <code><a href="/docs/linux/man/8-yum-updatesd/">yum-updatesd</a>(8)</code>.</p>
<h2>Description</h2>
<p>yum-updatesd uses a configuration file at <code>/etc/yum/yum-updatesd.conf</code>. Additional configuration information is read from the main <code>yum.conf (5)</code> configuration file. </p>
<h2>Parameters</h2>
<p>There is one section in the yum-updatesd configuration file, main, which defines all of the global configuration options.</p>
<h2>[main] OPTIONS</h2>
<p>The [main] section must exist for yum-updatesd to do anything. It consists of the following options: </p>
<dl>
<dt><code>run_interval</code></p>
<dd>Number of seconds to wait between checks for available updates. </p>
<dt><code>updaterefresh</code></p>
<dd>Minimum number of seconds between update information refreshes to avoid hitting the server too often. </p>
<dt><code>emit_via</code></p>
<dd>List of ways to emit update notification. Valid values are `email&#8217;, `dbus&#8217; and `syslog&#8217;. </p>
<dt><code>do_update</code></p>
<dd>Boolean option to decide whether or not updates should be automatically applied. Defaults to False. </p>
<dt><code>do_download</code></p>
<dd>Boolean option to decide whether or not updates should be automatically downloaded. Defaults to False. </p>
<dt><code>do_download_deps</code></p>
<dd>Boolean option to automatically download dependencies of packages which need updating as well. Defaults to False. </p>
</dl>
<h2>Mail Options</h2>
<dl>
<dt><code>email_to</code></p>
<dd>List of email addresses to send update notification to. Defaults to `root [at] localhost&#8217;. </p>
<dt><code>email_from</code></p>
<dd>Email address for update notifications to be from. Defaults to `yum-updatesd [at] localhost&#8217;. </p>
<dt><code>smtp_server</code></p>
<dd>SMTP server to use when sending mail, host or a host:port string. Defaults to `localhost:25&#8242;. </p>
</dl>
<h2>Syslog Options</h2>
<dl>
<dt><code>syslog_facility</code></p>
<dd>What syslog facility should be used. Defaults to `DAEMON&#8217;. </p>
<dt><code>syslog_level</code></p>
<dd>Level of syslog messages. Defaults to `WARN&#8217;. </p>
</dl>
<h2>Files</h2>
<pre>/etc/yum/yum-updatesd.conf</pre>
<h2>See Also</h2>
<p><a href="/docs/linux/man/8-yum-updatesd/">yum-updatesd</a>(8) <a href="/docs/linux/man/5-yum-conf/">yum.conf</a>(5) </p>
