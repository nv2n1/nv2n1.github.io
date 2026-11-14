---
title: "sysctl-conf(5)"
name: "sysctl-conf"
section: "5"
letter: "s"
url: "/docs/linux/man/5-sysctl-conf/"
description: "sysctl.conf – sysctl preload/configuration file"
---

<p>sysctl.conf &#8211; sysctl preload/configuration file</p>
<h2>Description</h2>
<p><code>sysctl.conf</code> is a simple file containing sysctl values to be read in and set by <code>sysctl</code>. The syntax is simply as follows:</p>
<dl>
<dd>
<pre># comment
; comment
token = value</pre>
</dl>
<p> Note that blank lines are ignored, and whitespace before and after a token or value is ignored, although a value can contain whitespace within. Lines which begin with a <i>#</i> or <i>;</i> are considered comments and ignored. If a line begins with a single -, any attempts to set the value that fail will be ignored. </p>
<h2>Notes</h2>
<p>As the <code>/etc/sysctl.conf</code> file is used to override default kernel parameter values, only a small number of parameters is predefined in the file. Use <i>/sbin/sysctl -a</i> or follow <code><a href="/docs/linux/man/8-sysctl/">sysctl</a></code>(8) to list all possible parameters. The description of individual parameters can be found in the kernel documentation.</p>
<h2>Example</h2>
<pre># sysctl.conf sample
#
 kernel.domainname = example.com
; this one has a space which will be written to the sysctl!
 kernel.modprobe = /sbin/mod probe</pre>
</dl>
<h2>Files</h2>
<p><i>/etc/sysctl.d/*.conf</i><br />
 <i>/run/sysctl.d/*.conf</i><br />
 <i>/usr/local/lib/sysctl.d/*.conf</i><br />
 <i>/usr/lib/sysctl.d/*.conf</i><br />
 <i>/lib/sysctl.d/*.conf</i><br />
 <i>/etc/sysctl.conf</i> </p>
<p> The paths where <code>sysctl</code> preload files usually exist. See also <code>sysctl</code> option <i>&#8211;system</i>.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-sysctl/">sysctl</a></code>(8)</p>
<h2>Author</h2>
<p>George Staikos</p>
<h2>Reporting Bugs</h2>
<p>Please send bug reports to</p>
