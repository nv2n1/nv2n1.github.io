---
title: "pmnewzone(3)"
name: "pmnewzone"
section: "3"
letter: "p"
url: "/docs/linux/man/3-pmnewzone/"
description: "pmNewZone – establish a reporting timezone"
---

<p><code>pmNewZone</code> &#8211; establish a reporting timezone</p>
<h2>C Synopsis</h2>
<p><code> #include &lt;pcp/pmapi.h&gt; </p>
<p> int pmNewZone(const char *</code><i>tz</i>); </p>
<p> cc &#8230; -lpcp</p>
<h2>Description</h2>
<p>The current reporting timezone affects the timezone used by <code><a href="/docs/linux/man/3-pmctime/">pmCtime</a></code>(3) and <code><a href="/docs/linux/man/3-pmlocaltime/">pmLocaltime</a></code>(3). </p>
<p> The argument <i>tz</i> defines a timezone string, in the format described for the <code>TZ</code> environment variable, see <code><a href="/docs/linux/man/7-environ/">environ</a></code>(7). </p>
<p> <code>pmNewZone</code> sets the current reporting timezone, and returns a value that may be used in a subsequent call to <code><a href="/docs/linux/man/3-pmusezone/">pmUseZone</a></code>(3) to restore this reporting timezone.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-pmapi/">PMAPI</a></code>(3), <code><a href="/docs/linux/man/3-pmctime/">pmCtime</a></code>(3), <code><a href="/docs/linux/man/3-pmgetconfig/">pmGetConfig</a></code>(3), <code><a href="/docs/linux/man/3-pmlocaltime/">pmLocaltime</a></code>(3), <code><a href="/docs/linux/man/3-pmnewcontextzone/">pmNewContextZone</a></code>(3), <code><a href="/docs/linux/man/3-pmusezone/">pmUseZone</a></code>(3), <code><a href="/docs/linux/man/3-pmwhichzone/">pmWhichZone</a></code>(3), <code><a href="/docs/linux/man/5-pcp-conf/">pcp.conf</a></code>(5), <code><a href="/docs/linux/man/5-pcp-env/">pcp.env</a></code>(5) and <code><a href="/docs/linux/man/7-environ/">environ</a></code>(7).</p>
<h2>Diagnostics</h2>
<p>A return value less than zero indicates a fatal error from a system call, most likely <code><a href="/docs/linux/man/3-malloc/">malloc</a></code>(3).</p>
