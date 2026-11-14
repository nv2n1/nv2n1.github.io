---
title: "pm-is-supported(1)"
name: "pm-is-supported"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pm-is-supported/"
description: "pm-is-supported – Test whether suspend or hibernate is supported."
---

<h2 class="name">NAME</h2>
<p> pm-is-supported &#8211; Test whether suspend or hibernate is supported. </p>
<h2>SYNOPSIS</h2>
<dl>
<dt> <code>pm-is-supported</code> [{<code>&#8211;suspend</code>&nbsp;<wbr>|&nbsp;<wbr><code>&#8211;hibernate</code>&nbsp;<wbr>|&nbsp;<wbr><code>&#8211;suspend-hybrid</code>}]</dl>
<h2>DESCRIPTION</h2>
<dd>This manual page documents briefly the <code>pm-is-supported</code> command. </p>
<p> The intended purpose of <code>pm-is-supported</code> is to find out which power management modes are supported by the system. <a href="/docs/linux/man/8-hald/">hald</a>(8) will call it to do just that. (Note that UPower does not use this.)</p>
<h2>OPTIONS</h2>
<p> <code>&#8211;suspend</code></p>
<dl>
<dt>
<dd> Test whether suspend is supported. Suspend is a state where most devices are shutdown, except for RAM. This state still draws power.</dl>
<p> <code>&#8211;hibernate</code></p>
<dl>
<dt>
<dd> Test whether hibernate is supported. During hibernate the state of the system is saved to disk, the system is fully powered off.</dl>
<p> <code>&#8211;suspend-hybrid</code></p>
<dl>
<dt>
<dd> Test whether hybrid-suspend is supported. Hybrid-suspend is the process where first the state of the system is saved to disk &#8212; just like with hibernate &#8212; but instead of poweroff, the system goes in suspend state, which means it can wakeup quicker than for normal hibernation. The advantage over suspend is that you can resume even if you run out of power. s2both is a hybrid-suspend implementation.</dl>
<h2>RETURN VALUE</h2>
<p> The result of the test for a certain powermanagement state is defined by the following exit codes. </p>
<table>
<tr VALIGN=top>
<td><i>Code</i></td>
<td><i>Diagnostic</i>
</td>
</tr>
<tr VALIGN=top>
<td> <code>0</code> </td>
<td> State available.
</td>
</tr>
<tr VALIGN=top>
<td> <code>1</code> </td>
<td> State NOT available.
</td>
</tr>
</table>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/8-hald/">hald</a></code>(8), <code><a href="/docs/linux/man/8-pm-suspend/">pm-suspend</a></code>(8), <code><a href="/docs/linux/man/8-s2both/">s2both</a></code>(8), <code><a href="/docs/linux/man/7-upower/">UPower</a></code>(7)</p>
<h2>AUTHOR</h2>
<p> <code>Tim Dijkstra</code> &lt;tim [at] famdijkstra.org&gt;</p>
<dl>
<dt>
<dd> Manpage author.</dl>
<h2>COPYRIGHT</h2>
<p> Copyright &#169; 2007 Tim Dijkstra </p>
<p> This manual page was originally written for the Debian(TM) system, and has been adopted by the pm-utils project. </p>
<p> Permission is granted to copy, distribute and/or modify this document under the terms of the GNU General Public License, Version 2 or (at your option) any later version published by the Free Software Foundation. </p>
<h2>Index</h2>
