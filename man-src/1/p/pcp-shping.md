---
title: "pcp-shping(1)"
name: "pcp-shping"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pcp-shping/"
description: "pcp-shping – report on shell service availability and response"
---

<h2>NAME</h2>
<p> <code>pcp-shping</code> &#8211; report on shell service availability and response</p>
<h2>SYNOPSIS</h2>
<p> <code>pcp shping</code> [<code>-cl</code>] <i>tag</i> &#8230;</p>
<h2>DESCRIPTION</h2>
<p> <code>pcp-shping</code> samples and reports on the shell-ping service metrics exported by the <code><a href="/docs/linux/man/1-pmdashping/">pmdashping</a></code>(1) agent. </p>
<p> The default report from <code>pcp-shping</code> shows two columns for each service <i>tag</i>, the first showing service status (zero indicating success) and the second service response time, for the last <code>pmdashping</code> command refresh cycle. </p>
<p> When invoked via the <code><a href="/docs/linux/man/1-pcp/">pcp</a></code>(1) command, the <code>-h</code>/<code>&#8211;host</code>, <code>-a</code>/<code>&#8211;archive</code>, <code>-O</code>/<code>&#8211;origin</code>, <code>-s</code>/<code>&#8211;samples</code>, <code>-t</code>/<code>&#8211;interval</code>, <code>-Z</code>/<code>&#8211;timezone</code> and several other options become indirectly available.</p>
<h3>Options</h3>
<p> The <code>-c</code>/<code>&#8211;status</code> switch displays a summary of the current shell-ping collector &#8211; information about service refresh interval, the current command timeout setting, count of refreshes, and the full command line associated with each <i>tag</i>. </p>
<p> The <code>-l</code>/<code>&#8211;tags</code> switch displays the valid <i>tag</i>s.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-pcp/">pcp</a></code>(1), <code><a href="/docs/linux/man/1-pmdashping/">pmdashping</a></code>(1) and <code><a href="/docs/linux/man/1-pcpintro/">PCPIntro</a></code>(1). </p>
<h2>Index</h2>
