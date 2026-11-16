---
title: "arched(8)"
name: "arched"
section: "8"
letter: "a"
url: "/docs/linux/man/8-arched/"
description: "arched – ARC Hosting Environment Daemon"
---

<p>arched &#8211; ARC Hosting Environment Daemon</p>
<h2>Synopsis</h2>
<p><code>arched</code> [<i>OPTION</i>]&#8230;</p>
<h2>Description</h2>
<p>arched is the ARC Hosting Environment Daemon and is responsible for&#8230;</p>
<h2>Options</h2>
<dl>
<dt><code>-f</code>, <code>&#8211;foreground</code></dt>
<dd>run daemon in foreground</dd>
<dt><code>-w</code>, <code>&#8211;watchdog</code></dt>
<dd>enables watchdog which restarts stuck and failed arched (it works only in background mode)</dd>
<dt><code>-c</code>, <code>&#8211;xml-config</code></dt>
<dd>full path of XML config file</dd>
<dt><code>-i</code>, <code>&#8211;ini-config</code></dt>
<dd>full path of INI config file</dd>
<dt><code>-d</code>, <code>&#8211;config-dump</code></dt>
<dd>dump XML config generated from INI one</dd>
<dt><code>-p</code>, <code>&#8211;pid-file</code></dt>
<dd>full path of pid file</dd>
<dt><code>-u</code>, <code>&#8211;user</code></dt>
<dd>user name to switch after starting</dd>
<dt><code>-g</code>, <code>&#8211;group</code></dt>
<dd>group name to switch after starting</dd>
<dt><code>-s</code>, <code>&#8211;schema</code></dt>
<dd>full path of XML schema file to be used for validating configuration</dd>
<dt><code>-v</code>, <code>&#8211;version</code></dt>
<dd>output version information and exit</dd>
<dt><code>-a</code>, <code>&#8211;install</code></dt>
<dd>install windows service (only works on windows)</dd>
<dt><code>-r</code>, <code>&#8211;uninstall</code></dt>
<dd>uninstall windows service (only works on windows)</dd></dl>
<h2>Reporting Bugs</h2>
<p>Report bugs to <a rel="nofollow" href="http://bugzilla.nordugrid.org/">http://bugzilla.nordugrid.org/</a></p>
<h2>Copyright</h2>
<p>APACHE LICENSE Version 2.0</p>
<h2>Files</h2>
<p><code>/etc/arc.conf</code></p>
<h2>Author</h2>
<p>Aleksandr Konstantinov &lt;aleks [at] fys.uio.no&gt;</p>
