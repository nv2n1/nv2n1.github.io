---
title: "cgred-conf(5)"
name: "cgred-conf"
section: "5"
letter: "c"
url: "/docs/linux/man/5-cgred-conf/"
description: "cgred.conf – libcgroup configuration file"
---

<p>cgred.conf &#8211; libcgroup configuration file</p>
<h2>Description</h2>
<p><code>cgred.conf</code> is cgred service configuration file. In this file there could be defined several internal values. Defining anything else in this file will cause the CGroup Rules Daemon program to fail.</p>
<dl>
<dd><code>CONFIG_FILE</code> specifies the configuration file for cgred service</p>
<dt><code>LOG_FILE</code></p>
<dd>variable specifies the file to which logs will be written (by default they are not sent to a file but to syslog)</p>
<dt><code>NODAEMON</code></p>
<dd>if it is equal to &quot;&#8211;nodamon&quot; then run cgred in non-daemon mode</p>
<dt><code>LOG</code></p>
<dd>define the verbosity of logging. Accepted values are &#8216;-v&#8217;, &#8216;-vv&#8217;, &#8216;-q&#8217; and &#8216;&#8211;nolog&#8217;.</dl>
<h2>Files</h2>
<dl>
<dt><code>/etc/cgred.conf</code></p>
<dd>
<dt>default libcgroup configuration file</p>
<dd></dl>
<h2>See Also</h2>
<p>cgrules.conf (5), cgconfig.conf (5), cgrules.d (5) </p>
