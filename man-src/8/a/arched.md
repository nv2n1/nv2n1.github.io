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
<dt><code>-f</code>, <code>&#8211;foreground</code></p>
<dd>run daemon in foreground</p>
<dt><code>-w</code>, <code>&#8211;watchdog</code></p>
<dd>enables watchdog which restarts stuck and failed arched (it works only in background mode)</p>
<dt><code>-c</code>, <code>&#8211;xml-config</code></p>
<dd>full path of XML config file</p>
<dt><code>-i</code>, <code>&#8211;ini-config</code></p>
<dd>full path of INI config file</p>
<dt><code>-d</code>, <code>&#8211;config-dump</code></p>
<dd>dump XML config generated from INI one</p>
<dt><code>-p</code>, <code>&#8211;pid-file</code></p>
<dd>full path of pid file</p>
<dt><code>-u</code>, <code>&#8211;user</code></p>
<dd>user name to switch after starting</p>
<dt><code>-g</code>, <code>&#8211;group</code></p>
<dd>group name to switch after starting</p>
<dt><code>-s</code>, <code>&#8211;schema</code></p>
<dd>full path of XML schema file to be used for validating configuration</p>
<dt><code>-v</code>, <code>&#8211;version</code></p>
<dd>output version information and exit</p>
<dt><code>-a</code>, <code>&#8211;install</code></p>
<dd>install windows service (only works on windows)</p>
<dt><code>-r</code>, <code>&#8211;uninstall</code></p>
<dd>uninstall windows service (only works on windows)</dl>
<h2>Reporting Bugs</h2>
<p>Report bugs to <a rel="nofollow" href="http://bugzilla.nordugrid.org/">http://bugzilla.nordugrid.org/</a></p>
<h2>Copyright</h2>
<p>APACHE LICENSE Version 2.0</p>
<h2>Files</h2>
<p><code>/etc/arc.conf</code></p>
<h2>Author</h2>
<p>Aleksandr Konstantinov &lt;aleks [at] fys.uio.no&gt;</p>
