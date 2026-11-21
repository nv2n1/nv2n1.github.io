---
title: "needs-restarting(1)"
name: "needs-restarting"
section: "1"
letter: "n"
url: "/docs/linux/man/1-needs-restarting/"
description: "needs-restarting – report running processes that have been updated"
---

<h2>NAME</h2>
<p> needs-restarting &#8211; report running processes that have been updated</p>
<h2>SYNOPSIS</h2>
<p> <code>needs-restarting</code> [options]</p>
<h2>DESCRIPTION</h2>
<p> <code>needs-restarting</code> is a program that reports a list of process ids that started running before they or some component that they use were updated. </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-h, &#8211;help</code></dt>
<dd> Display a help message, and then quit.</dd>
<dt><code>-u, &#8211;useronly</code></dt>
<dd> Show processes for my userid only.</dd>
<dt><code>-r, &#8211;reboothint</code></dt>
<dd> Only report whether a full reboot is required (returns 1) or not (returns 0).</dd>
<dt><code>-s, &#8211;services</code></dt>
<dd> List the affected systemd services only. </dd>
</dl>
<h2>SEE ALSO</h2>
<pre>
<i>yum.conf (5)</i>
<a rel="nofollow" href="http://yum.baseurl.org/">http://yum.baseurl.org/</a>
</pre>
<h2>AUTHORS</h2>
<pre>
See the Authors file included with this program.
</pre>
