---
title: "runlevel(8)"
name: "runlevel"
section: "8"
letter: "r"
url: "/docs/linux/man/8-runlevel/"
description: "runlevel – Print previous and current SysV runlevel"
---

<p>runlevel &#8211; Print previous and current SysV runlevel</p>
<h2>Synopsis</h2>
<dl>
<dt> <code>runlevel</code> [options&#8230;]</dl>
<h2>Overview</h2>
<p>&quot;Runlevels&quot; are an obsolete way to start and stop groups of services used in SysV init. systemd provides a compatibility layer that maps runlevels to targets, and associated binaries like <code>runlevel</code>. Nevertheless, only one runlevel can be &quot;active&quot; at a given time, while systemd can activate multiple targets concurrently, so the mapping to runlevels is confusing and only approximate. Runlevels should not be used in new code, and are mostly useful as a shorthand way to refer the matching systemd targets in kernel boot parameters. </p>
<dd><code>Table 1. Mapping between runlevels and systemd targets</code> </p>
<table BORDER>
<tr VALIGN=top>
<td><code></p>
<dd>Runlevel </code></td>
<td><code> Target </code>
</td>
</tr>
<tr VALIGN=top>
<td> 0 </td>
<td> poweroff.target
</td>
</tr>
<tr VALIGN=top>
<td> 1 </td>
<td> rescue.target
</td>
</tr>
<tr VALIGN=top>
<td> 2, 3, 4 </td>
<td> multi-user.target
</td>
</tr>
<tr VALIGN=top>
<td> 5 </td>
<td> graphical.target
</td>
</tr>
<tr VALIGN=top>
<td> 6 </td>
<td> reboot.target
</td>
</tr>
</table>
<h2>Description</h2>
<p><code>runlevel</code> prints the previous and current SysV runlevel if they are known. </p>
<p> The two runlevel characters are separated by a single space character. If a runlevel cannot be determined, N is printed instead. If neither can be determined, the word &quot;unknown&quot; is printed. </p>
<p> Unless overridden in the environment, this will check the utmp database for recent runlevel changes.</p>
<h2>Options</h2>
<p>The following option is understood: </p>
<p> <code>&#8211;help</code></p>
<dl>
<dd>Print a short help text and exit.</dl>
<h2>Exit Status</h2>
<p>If one or both runlevels could be determined, 0 is returned, a non-zero failure code otherwise.</p>
<h2>Environment</h2>
<p><i>$RUNLEVEL</i></p>
<dl>
<dd>If <i>$RUNLEVEL</i> is set, <code>runlevel</code> will print this value as current runlevel and ignore utmp.</dl>
<p> <i>$PREVLEVEL</i></p>
<dl>
<dd>If <i>$PREVLEVEL</i> is set, <code>runlevel</code> will print this value as previous runlevel and ignore utmp.</dl>
<h2>Files</h2>
<p>/run/utmp</p>
<dl>
<dd>The utmp database <code>runlevel</code> reads the previous and current runlevel from.</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-systemd/">systemd</a></code>(1), <code><a href="/docs/linux/man/5-systemd-target/">systemd.target</a></code>(5), <code><a href="/docs/linux/man/1-systemctl/">systemctl</a></code>(1) </p>
