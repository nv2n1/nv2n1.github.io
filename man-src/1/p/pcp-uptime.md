---
title: "pcp-uptime(1)"
name: "pcp-uptime"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pcp-uptime/"
description: "pcp-uptime – tell how long the system has been running"
---

<h2>NAME</h2>
<p> <code>pcp-uptime</code> &#8211; tell how long the system has been running</p>
<h2>SYNOPSIS</h2>
<p> <code>pcp</code> [<i>pcp options</i>] <code>uptime</code> [<code>-V</code>/[<code>&#8211;version</code>]</p>
<h2>DESCRIPTION</h2>
<p> <code>pcp-uptime</code> gives a one line display of the following information. The current time, how long the system has been running, how many users are currently logged on, and the system load averages for the past 1, 5, and 15 minutes. </p>
<p> When invoked via the <code><a href="/docs/linux/man/1-pcp/">pcp</a></code>(1) command, the <code>-h</code>/<code>&#8211;host</code>, <code>-a</code>/<code>&#8211;archive</code>, <code>-O</code>/<code>&#8211;origin</code>, <code>-Z</code>/<code>&#8211;timezone</code> and several other <i>pcp options</i> become indirectly available. </p>
<p> The current version of <code>pcp-uptime</code> can be queried using the <code>-V</code>/<code>&#8211;version</code> option.</p>
<h2>NOTES</h2>
<p> <code>pcp-uptime</code> is inspired by the <code><a href="/docs/linux/man/1-uptime/">uptime</a></code>(1) command and aims to be command line and output compatible with it.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-pcp/">pcp</a></code>(1), <code><a href="/docs/linux/man/1-uptime/">uptime</a></code>(1), <code><a href="/docs/linux/man/1-pcpintro/">PCPIntro</a></code>(1) and <code><a href="/docs/linux/man/7-environ/">environ</a></code>(7). </p>
<h2>Index</h2>
