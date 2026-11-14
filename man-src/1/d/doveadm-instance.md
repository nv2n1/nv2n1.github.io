---
title: "doveadm-instance(1)"
name: "doveadm-instance"
section: "1"
letter: "d"
url: "/docs/linux/man/1-doveadm-instance/"
description: "doveadm-instance – Manage the list of running Dovecot instances"
---

<h2>NAME</h2>
<p> doveadm-instance &#8211; Manage the list of running Dovecot instances</p>
<h2>SYNOPSIS</h2>
<p> <code>doveadm</code> [<code>-Dv</code>] [<code>-f</code> <i>formatter</i>] <code>instance list</code><br />
 <code>doveadm</code> [<code>-Dv</code>] <code>instance remove</code> <i>name</i> | <i>base_dir</i></p>
<h2>DESCRIPTION</h2>
<p> The <code>doveadm instance</code> commands are used to manage the list of Dovecot instances running on the server. In most installations there is only one Dovecot instance, but in some cases is may be useful to have more (e.g. running director proxy and backend in the same server). </p>
<p> Instances are added to the list automatically when Dovecot is started. Each instance is uniquely identified by its <i>base_dir</i> setting. Instances can be named by setting <i>instance_name</i> in each instance&#8217;s <i>dovecot.conf</i>. When an instance is named, it can be accessed easily by giving <code>-i&nbsp;<wbr></code><i>instance_name</i> command line parameter for Dovecot binaries (e.g. doveadm).</p>
<h2>OPTIONS</h2>
<p> Global <code><a href="/docs/linux/man/1-doveadm/">doveadm</a></code>(1) <i>options</i>:</p>
<dl>
<dt><code>-D</code></p>
<dd> Enables verbosity and debug messages.</p>
<dt><code>-f&nbsp;<wbr></code><i>formatter</i></p>
<dd> Specifies the <i>formatter</i> for formatting the output. Supported formatters are:</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>flow</code></p>
<dd> prints each line with <i>key</i><code>=</code><i>value</i> pairs.</p>
<dt><code>pager</code></p>
<dd> prints each <i>key</i>:&nbsp;<wbr><i>value</i> pair on its own line and separates records with form feed character (<code>^L</code>).</p>
<dt><code>tab</code></p>
<dd> prints a table header followed by tab separated value lines.</p>
<dt><code>table</code></p>
<dd> prints a table header followed by adjusted value lines.</dl>
</dl>
<dt><code>-v</code></p>
<dd> Enables verbosity, including progress counter.</dl>
<h2>ARGUMENTS</h2>
<dl>
<dt><i>name</i></p>
<dd> The value of an instance&#8217;s <i>instance_name</i> setting.</p>
<dt><i>base_dir</i></p>
<dd> The base directory of a Dovecot instance.</dl>
<h2>COMMANDS</h2>
<h3>instance list</h3>
<p> <code>doveadm instance list</code> </p>
<p> This command lists the seen Dovecot instances.</p>
<h3>instance remove</h3>
<p> <code>doveadm instance remove</code> <i>name</i> | <i>base_dir</i> </p>
<p> This command removes the specified instance.</p>
<h2>REPORTING BUGS</h2>
<p> Report bugs, including <i>doveconf -n</i> output, to the Dovecot Mailing List &lt;dovecot [at] dovecot.org&gt;. Information about reporting bugs is available at: <a rel="nofollow" href="http://dovecot.org/bugreport.html">http://dovecot.org/bugreport.html</a></p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-doveadm/">doveadm</a></code>(1) </p>
<h2>Index</h2>
