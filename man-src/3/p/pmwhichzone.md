---
title: "pmwhichzone(3)"
name: "pmwhichzone"
section: "3"
letter: "p"
url: "/docs/linux/man/3-pmwhichzone/"
description: "pmWhichZone – return current reporting timezone"
---

<p><code>pmWhichZone</code> &#8211; return current reporting timezone</p>
<h2>C Synopsis</h2>
<p><code> #include &lt;pcp/pmapi.h&gt; </p>
<p> int pmWhichZone(char **</code><i>tz</i>); </p>
<p> cc &#8230; -lpcp</p>
<h2>Description</h2>
<p>The current reporting timezone effects the timezone used by <code><a href="/docs/linux/man/3-pmctime/">pmCtime</a></code>(3) and <code><a href="/docs/linux/man/3-pmlocaltime/">pmLocaltime</a></code>(3). </p>
<p> <code>pmWhichZone</code> returns the handle of the current timezone, as previously established by a call to <code><a href="/docs/linux/man/3-pmnewzone/">pmNewZone</a></code>(3) or <code><a href="/docs/linux/man/3-pmnewcontextzone/">pmNewContextZone</a></code>(3). If the call is successful (i.e. there exists a current reporting timezone) then a non-negative integer is returned and <i>tz</i> is set to point to a static buffer containing the timezone string itself.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-pmapi/">PMAPI</a></code>(3), <code><a href="/docs/linux/man/3-pmctime/">pmCtime</a></code>(3), <code><a href="/docs/linux/man/3-pmlocaltime/">pmLocaltime</a></code>(3), <code><a href="/docs/linux/man/3-pmnewcontextzone/">pmNewContextZone</a></code>(3), <code><a href="/docs/linux/man/3-pmnewzone/">pmNewZone</a></code>(3) and <code><a href="/docs/linux/man/3-pmusezone/">pmUseZone</a></code>(3).</p>
<h2>Diagnostics</h2>
<p>A return value less than zero indicates there is no current reporting timezone.</p>
