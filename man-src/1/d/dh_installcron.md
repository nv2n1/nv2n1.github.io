---
title: "dh_installcron(1)"
name: "dh_installcron"
section: "1"
letter: "d"
url: "/docs/linux/man/1-dh_installcron/"
description: "dh_installcron – install cron scripts into etc/cron.*"
---

<h2 class="name">NAME</h2>
<p> dh_installcron &#8211; install cron scripts into etc/cron.* </p>
<h2>SYNOPSIS</h2>
<p> <code>dh_installcron</code> [<code>debhelper options</code>] [<code>&#8211;name=</code><i>name</i>]</p>
<h2>DESCRIPTION</h2>
<p> <code>dh_installcron</code> is a debhelper program that is responsible for installing cron scripts.</p>
<h2>FILES</h2>
<dl>
<dt>debian/<i>package</i>.cron.daily</p>
<dd>
<dt>debian/<i>package</i>.cron.weekly</p>
<dd>
<dt>debian/<i>package</i>.cron.monthly</p>
<dd>
<dt>debian/<i>package</i>.cron.hourly</p>
<dd>
<dt>debian/<i>package</i>.cron.d</p>
<dd> Installed into the appropriate <i>etc/cron.*/</i> directory in the package build directory.</dl>
<h2>OPTIONS</h2>
<dl>
<dt><code>&#8211;name=</code><i>name</i></p>
<dd> Look for files named <i>debian/package.name.cron.*</i> and install them as <i>etc/cron.*/name</i>, instead of using the usual files and installing them as the package name.</dl>
<h2>SEE ALSO</h2>
<p> <i><a href="/docs/linux/man/7-debhelper/">debhelper</a></i>(7) </p>
<p> This program is a part of debhelper.</p>
<h2>AUTHOR</h2>
<p> Joey Hess &lt;joeyh [at] debian.org&gt; </p>
<h2>Index</h2>
