---
title: "doveadm-mount(1)"
name: "doveadm-mount"
section: "1"
letter: "d"
url: "/docs/linux/man/1-doveadm-mount/"
description: "doveadm-mount – Manage the list of mountpoints where mails are stored"
---

<h2>NAME</h2>
<p> doveadm-mount &#8211; Manage the list of mountpoints where mails are stored</p>
<h2>SYNOPSIS</h2>
<p> <code>doveadm</code> [<code>-Dv</code>] [<code>-f</code> <i>formatter</i>] <code>mount</code> <i>command</i> [<i>arguments</i>]</p>
<h2>DESCRIPTION</h2>
<p> The doveadm <code>mount</code> <i>command</i>s can be used to manage the list of mountpoints where mails are stored. This is used mainly for better error handling when a mountpoint isn&#8217;t mounted for some reason:</p>
<dl>
<dt>*</dt>
<dd> If a mail directory doesn&#8217;t exist, it&#8217;s autocreated. If the user&#8217;s mails aren&#8217;t mounted and filesystem permissions still allow the autocreation, the user will see an empty mailbox and later will have to redownload all mails. If the mountpoint is known to be unmounted, Dovecot will simply fail opening any mailboxes.</dd>
<dt>*</dt>
<dd> If dbox alternate storage isn&#8217;t mounted and a mail in it is attempted to be accessed, Dovecot normally rebuilds the indexes and notices that all the mails in alt storage are expunged. When the alt storage is mounted back and even if index is again rebuilt, the mails won&#8217;t necessarily become visible anymore for IMAP clients. If the mountpoint is known to be unmounted, Dovecot won&#8217;t rebuild indexes and lose the mails.</dd></dl>
<p> Dovecot automatically adds mountpoints to this list at startup. If you don&#8217;t want some of the mountpoints added, you can add a wildcard ignore for it.</p>
<h2>OPTIONS</h2>
<p> Global <code><a href="/docs/linux/man/1-doveadm/">doveadm</a></code>(1) <i>options</i>:</p>
<dl>
<dt><code>-D</code></dt>
<dd> Enables verbosity and debug messages.</dd>
<dt><code>-f&nbsp;<wbr></code><i>formatter</i></dt>
<dd> Specifies the <i>formatter</i> for formatting the output. Supported formatters are:</dd>
<dl>
<dl>
<dt><code>flow</code></dt>
<dd> prints each line with <i>key</i><code>=</code><i>value</i> pairs.</dd>
<dt><code>pager</code></dt>
<dd> prints each <i>key</i>:&nbsp;<wbr><i>value</i> pair on its own line and separates records with form feed character (<code>^L</code>).</dd>
<dt><code>tab</code></dt>
<dd> prints a table header followed by tab separated value lines.</dd>
<dt><code>table</code></dt>
<dd> prints a table header followed by adjusted value lines.</dd></dl>
</dl>
<dt><code>-v</code></dt>
<dd> Enables verbosity, including progress counter.</dd></dl>
<h2>ARGUMENTS</h2>
<dl>
<dt><i>path</i></dt>
<dd> The directory name of a mountpoint</dd>
<dt><i>state</i></dt>
<dd> The <i>state</i> of a mountpoint. Either <code>online</code> or <code>ignore</code>.</dd></dl>
<h2>COMMANDS</h2>
<h3>mount add</h3>
<p> <code>doveadm mount add</code> [<i>path</i> [<i>state</i>]] </p>
<p> If this command is run without any parameters, doveadm detects all missing mountpoints and adds them (the same way as when Dovecot does at startup). </p>
<p> When a mountpoint <i>path</i> is given, it&#8217;s added as a mountpoint. The <i>state</i> can currently be either &quot;<code>online</code>&quot; (default) or &quot;<code>ignore</code>&quot;. The ignore state is mainly useful with path wildcards to add mountpoints that you never want Dovecot to automatically add, such as: <code>doveadm mount add &#8216;/mnt/*&#8217; ignore</code></p>
<h3>mount list</h3>
<p> <code>doveadm</code> [<code>-Dv</code> ] [<code>-f</code> <i>formatter</i>] <code>mount list</code> </p>
<p> This command lists the mountpoints known to Dovecot and their state.</p>
<h3>mount remove</h3>
<p> <code>doveadm mount remove </code><i>path</i> </p>
<p> This command removes the specified <i>path</i> from the mountpoint list.</p>
<h2>REPORTING BUGS</h2>
<p> Report bugs, including <i>doveconf -n</i> output, to the Dovecot Mailing List &lt;dovecot [at] dovecot.org&gt;. Information about reporting bugs is available at: <a rel="nofollow" href="http://dovecot.org/bugreport.html">http://dovecot.org/bugreport.html</a></p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-doveadm/">doveadm</a></code>(1) </p>
