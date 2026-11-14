---
title: "doveadm-exec(1)"
name: "doveadm-exec"
section: "1"
letter: "d"
url: "/docs/linux/man/1-doveadm-exec/"
description: "doveadm-exec – easily execute commands from Dovecot’s libexec_dir"
---

<h2>NAME</h2>
<p> doveadm-exec &#8211; easily execute commands from Dovecot&#8217;s libexec_dir</p>
<h2>SYNOPSIS</h2>
<p> <code>doveadm</code> [<code>-Dv</code>] <code>exec</code> <i>binary</i> [<i>binary arguments</i>]</p>
<h2>DESCRIPTION</h2>
<p> This command allows administrators and local users to simply execute commands from within <i>libexec_dir</i>. So for example a logged in system user could start a pre-authenticated imap session, using the command: <code>doveadm exec imap</code>. An administrator would use the command: <code>doveadm exec imap -u</code> <i>username</i>.</p>
<h2>OPTIONS</h2>
<p> Global <code><a href="/docs/linux/man/1-doveadm/">doveadm</a></code>(1) <i>options</i>:</p>
<dl>
<dt><code>-D</code></p>
<dd> Enables verbosity and debug messages.</p>
<dt><code>-v</code></p>
<dd> Enables verbosity, including progress counter.</dl>
<h2>ARGUMENTS</h2>
<dl>
<dt><i>binary</i></p>
<dd> the name of an executable located in <i>/usr/libexec/dovecot</i>.</p>
<dt><i>binary arguments</i></p>
<dd> options and arguments, wich will be passed through to the <i>binary</i>.</dl>
<h2>EXAMPLE</h2>
<p> This example demonstrates how to deliver a message from a file to a user&#8217;s mailbox. </p>
<pre><code>
doveadm exec dovecot - lda - d user[at] example.net - f admin[at] example.net &lt; ~ / stuff / welcome.msg
</code></pre>
<h2>REPORTING BUGS</h2>
<p> Report bugs, including <i>doveconf -n</i> output, to the Dovecot Mailing List &lt;dovecot [at] dovecot.org&gt;. Information about reporting bugs is available at: <a rel="nofollow" href="http://dovecot.org/bugreport.html">http://dovecot.org/bugreport.html</a></p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-doveadm/">doveadm</a></code>(1), <code><a href="/docs/linux/man/1-dovecot-lda/">dovecot-lda</a></code>(1) </p>
<h2>Index</h2>
