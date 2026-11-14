---
title: "lightdm(1)"
name: "lightdm"
section: "1"
letter: "l"
url: "/docs/linux/man/1-lightdm/"
description: "lightdm – a display manager"
---

<h2>NAME</h2>
<p> lightdm &#8211; a display manager</p>
<h2>SYNOPSIS</h2>
<p> <code>lightdm</code> [ <i>OPTION</i> ]</p>
<h2>DESCRIPTION</h2>
<p> <code>lightdm</code> is a display manager.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-h, &#8211;help</code></p>
<dd> Show help options</p>
<dt><code>-c, &#8211;config=FILE</code></p>
<dd> Use configuration file</p>
<dt><code>-d, &#8211;debug</code></p>
<dd> Print debugging messages</p>
<dt><code>&#8211;test-mode</code></p>
<dd> Run as unprivileged user, skipping things that require root access</p>
<dt><code>&#8211;pid-file=FILE</code></p>
<dd> File to write PID into</p>
<dt><code>&#8211;xsessions-dir=DIRECTORY</code></p>
<dd> Directory to load X sessions from</p>
<dt><code>&#8211;xgreeters-dir=DIRECTORY</code></p>
<dd> Directory to load X greeters from</p>
<dt><code>&#8211;log-dir=DIRECTORY</code></p>
<dd> Directory to write logs to</p>
<dt><code>&#8211;run-dir=DIRECTORY</code></p>
<dd> Directory to store running state</p>
<dt><code>&#8211;cache-dir=DIRECTORY</code></p>
<dd> Directory to cached information</p>
<dt><code>-v, &#8211;version</code></p>
<dd> Show release version</dl>
<h2>FILES</h2>
<dl>
<dt><code>/etc/lightdm/lightdm.conf</code></p>
<dd> Configuration</p>
<dt><code>/etc/lightdm/users.conf</code></p>
<dd> User list configuration (if not using Accounts Service)</p>
<dt><code>/etc/lightdm/keys.conf</code></p>
<dd> XDMCP keys</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-dm-tool/">dm-tool</a></code>(1) </p>
<h2>Index</h2>
