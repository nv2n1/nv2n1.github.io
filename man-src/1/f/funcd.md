---
title: "funcd(1)"
name: "funcd"
section: "1"
letter: "f"
url: "/docs/linux/man/1-funcd/"
description: "funcd – deaemon for the Fedora Universal Network Controller"
---

<h2>NAME</h2>
<p> <code>funcd</code> &#8211; deaemon for the Fedora Universal Network Controller</p>
<h2>SYNOPSIS</h2>
<dl>
<dt>funcd [&#8211;daemon]</p>
<dd>
<dt>funcd &#8211;list-modules</p>
<dd></dl>
<h2>DESCRIPTION</h2>
<p> funcd registers itself to a certificate server (certmaster) listed in /etc/certmaster/minion.conf and takes orders from the command line func when that program is run from that certificate server. </p>
<p> Modules and capabilities provided by funcd are specified at <a rel="nofollow" href="https://fedorahosted.org/func/">https://fedorahosted.org/func/</a></p>
<h2>OPTIONS</h2>
<dl>
<dt><code>&#8211;daemon</code><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>daemonize the server on startup</p>
<dd>
<dt><code>&#8211;list-modules</code><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>list modules that would be loaded and exit</p>
<dd></dl>
<h2>CONFIGURATION</h2>
<p> See /etc/certmaster/minion.conf for other configuration options.</p>
<h2>ACCESS CONTROLS</h2>
<p> By default the certmaster host will always have full access to run all modules on minions, currently this behavior can be disabled by tweaking commonconfig.py. </p>
<p> Additional ACLs can be used to let other (<font SIZE="-1">SSL</font> authenticated) hosts access to specific modules. Access control files take one acl per row with the format: </p>
<p> &lt;common_name&gt;-&lt;certificate_hash&gt; = method[, method]&#8230; </p>
<p> where common_name is the <font SIZE="-1">CN</font> from the host certificate and certificate_hash is its hash as obtained from </p>
<p> openssl x509 -noout -in &lt;certificate_file&gt; -hash </p>
<p> See <a rel="nofollow" href="https://fedorahosted.org/func/wiki/FuncSecurity">https://fedorahosted.org/func/wiki/FuncSecurity</a> for additional details.</p>
<h2>FILES</h2>
<dl>
<dt><code>/etc/certmaster/minion.conf</code><tt>&nbsp;<wbr>&nbsp;<wbr></tt>certmaster config for this minion</p>
<dd>
<dt><code>/etc/func/minion.conf</code><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>minion configuration</p>
<dd>
<dt><code>/etc/func/async_methods.conf</code><tt>&nbsp;<wbr></tt>configuration for async methods</p>
<dd>
<dt><code>/etc/func/minion-acl.d/</code><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>directory for <font SIZE="-1">ACL</font> files</p>
<dd></dl>
<h2>ADDITONAL RESOURCES</h2>
<p> See the project wiki at <a rel="nofollow" href="https://fedorahosted.org/func/">https://fedorahosted.org/func/</a></p>
<h2>SEE ALSO</h2>
<p> <tt><a href="/docs/linux/man/1-func/">func</a>(1)</tt>, <tt><a href="/docs/linux/man/1-certmaster/">certmaster</a>(1)</tt>, <tt>&quot;<a href="/docs/linux/man/1-certmaster-ca/">certmaster-ca</a>(1)&quot;</tt>, <tt>&quot;<a href="/docs/linux/man/1-func-transmit/">func-transmit</a>(1)&quot;</tt></p>
<h2>AUTHOR</h2>
<p> Various, see <a rel="nofollow" href="https://fedorahosted.org/func/">https://fedorahosted.org/func/</a> </p>
<h2>Index</h2>
