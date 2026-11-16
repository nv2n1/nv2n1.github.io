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
<dt><code>-h, &#8211;help</code></dt>
<dd> Show help options</dd>
<dt><code>-c, &#8211;config=FILE</code></dt>
<dd> Use configuration file</dd>
<dt><code>-d, &#8211;debug</code></dt>
<dd> Print debugging messages</dd>
<dt><code>&#8211;test-mode</code></dt>
<dd> Run as unprivileged user, skipping things that require root access</dd>
<dt><code>&#8211;pid-file=FILE</code></dt>
<dd> File to write PID into</dd>
<dt><code>&#8211;xsessions-dir=DIRECTORY</code></dt>
<dd> Directory to load X sessions from</dd>
<dt><code>&#8211;xgreeters-dir=DIRECTORY</code></dt>
<dd> Directory to load X greeters from</dd>
<dt><code>&#8211;log-dir=DIRECTORY</code></dt>
<dd> Directory to write logs to</dd>
<dt><code>&#8211;run-dir=DIRECTORY</code></dt>
<dd> Directory to store running state</dd>
<dt><code>&#8211;cache-dir=DIRECTORY</code></dt>
<dd> Directory to cached information</dd>
<dt><code>-v, &#8211;version</code></dt>
<dd> Show release version</dd></dl>
<h2>FILES</h2>
<dl>
<dt><code>/etc/lightdm/lightdm.conf</code></dt>
<dd> Configuration</dd>
<dt><code>/etc/lightdm/users.conf</code></dt>
<dd> User list configuration (if not using Accounts Service)</dd>
<dt><code>/etc/lightdm/keys.conf</code></dt>
<dd> XDMCP keys</dd></dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-dm-tool/">dm-tool</a></code>(1) </p>
<h2>Index</h2>
