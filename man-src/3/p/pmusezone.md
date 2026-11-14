---
title: "pmusezone(3)"
name: "pmusezone"
section: "3"
letter: "p"
url: "/docs/linux/man/3-pmusezone/"
description: "pmUseZone – re-establish a reporting timezone"
---

<p><code>pmUseZone</code> &#8211; re-establish a reporting timezone</p>
<h2>C Synopsis</h2>
<p><code> #include &lt;pcp/pmapi.h&gt; </p>
<p> int pmUseZone(const int </code><i>tz_handle</i>); </p>
<p> cc &#8230; -lpcp</p>
<h2>Description</h2>
<p>The current reporting timezone effects the timezone used by <code><a href="/docs/linux/man/3-pmctime/">pmCtime</a></code>(3) and <code><a href="/docs/linux/man/3-pmlocaltime/">pmLocaltime</a></code>(3). </p>
<p> The argument <i>tz_handle</i> identifies a reporting timezone as previously established by a call to <code><a href="/docs/linux/man/3-pmnewzone/">pmNewZone</a></code>(3) or <code><a href="/docs/linux/man/3-pmnewcontextzone/">pmNewContextZone</a></code>(3), and this becomes the current reporting timezone.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-pmapi/">PMAPI</a></code>(3), <code><a href="/docs/linux/man/3-pmctime/">pmCtime</a></code>(3), <code><a href="/docs/linux/man/3-pmlocaltime/">pmLocaltime</a></code>(3), <code><a href="/docs/linux/man/3-pmnewcontextzone/">pmNewContextZone</a></code>(3), <code><a href="/docs/linux/man/3-pmnewzone/">pmNewZone</a></code>(3) and <code><a href="/docs/linux/man/3-pmwhichzone/">pmWhichZone</a></code>(3).</p>
<h2>Diagnostics</h2>
<p>A return value less than zero indicates the value of <i>tz_handle</i> is not legal.</p>
