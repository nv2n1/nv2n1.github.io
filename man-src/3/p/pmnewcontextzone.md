---
title: "pmnewcontextzone(3)"
name: "pmnewcontextzone"
section: "3"
letter: "p"
url: "/docs/linux/man/3-pmnewcontextzone/"
description: "pmNewContextZone – establish a reporting timezone based on a PMAPI context"
---

<p><code>pmNewContextZone</code> &#8211; establish a reporting timezone based on a PMAPI context</p>
<h2>C Synopsis</h2>
<p><code> #include &lt;pcp/pmapi.h&gt; </p>
<p> int pmNewContextZone(void); </p>
<p> cc &#8230; -lpcp </code></p>
<h2>Description</h2>
<p>The current reporting timezone affects the timezone used by <code><a href="/docs/linux/man/3-pmctime/">pmCtime</a></code>(3) and <code><a href="/docs/linux/man/3-pmlocaltime/">pmLocaltime</a></code>(3). </p>
<p> If the current PMAPI context is an archive, <code>pmNewContextZone</code> uses the timezone from the archive label record to set the current reporting timezone. </p>
<p> If the current PMAPI context corresponds to a host source of metrics, <code>pmNewContextZone</code> executes a <code><a href="/docs/linux/man/3-pmfetch/">pmFetch</a></code>(3) to retrieve the value for the metric <i>pmcd.timezone</i> and uses that to set the current reporting timezone. </p>
<p> In both cases, <code>pmNewContextZone</code> returns a value to identify the current reporting timezone that may be used in a subsequent call to <code><a href="/docs/linux/man/3-pmusezone/">pmUseZone</a></code>(3) to restore this reporting timezone.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-pmapi/">PMAPI</a></code>(3), <code><a href="/docs/linux/man/3-pmctime/">pmCtime</a></code>(3), <code><a href="/docs/linux/man/3-pmfetch/">pmFetch</a></code>(3), <code><a href="/docs/linux/man/3-pmgetconfig/">pmGetConfig</a></code>(3), <code><a href="/docs/linux/man/3-pmlocaltime/">pmLocaltime</a></code>(3), <code><a href="/docs/linux/man/3-pmnewcontext/">pmNewContext</a></code>(3), <code><a href="/docs/linux/man/3-pmnewzone/">pmNewZone</a></code>(3), <code><a href="/docs/linux/man/3-pmusezone/">pmUseZone</a></code>(3), <code><a href="/docs/linux/man/3-pmwhichzone/">pmWhichZone</a></code>(3), <code><a href="/docs/linux/man/5-pcp-conf/">pcp.conf</a></code>(5), <code><a href="/docs/linux/man/5-pcp-env/">pcp.env</a></code>(5) and <code><a href="/docs/linux/man/7-environ/">environ</a></code>(7).</p>
<h2>Diagnostics</h2>
<dl>
<dt><code>PM_ERR_NOCONTEXT</code></p>
<dd>the current PMAPI context is not valid</p>
<dt>other</p>
<dd>a return value less than zero indicates a fatal error from a system call, most likely <code><a href="/docs/linux/man/3-malloc/">malloc</a></code>(3) </p>
</dl>
