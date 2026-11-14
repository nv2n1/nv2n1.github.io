---
title: "pmlocaltime(3)"
name: "pmlocaltime"
section: "3"
letter: "p"
url: "/docs/linux/man/3-pmlocaltime/"
description: "pmLocaltime – convert the date and time for a reporting timezone"
---

<p><code>pmLocaltime</code> &#8211; convert the date and time for a reporting timezone</p>
<h2>C Synopsis</h2>
<p><code> #include &lt;time.h&gt;<br />
 #include &lt;pcp/pmapi.h&gt; </p>
<p> struct tm *pmLocaltime(const time_t *</code><i>clock</i>, struct tm *<i>result</i>); </p>
<p> cc &#8230; -lpcp</p>
<h2>Description</h2>
<p><code>pmLocaltime</code> is very similar to <code><a href="/docs/linux/man/3-localtime/">localtime</a></code>(3), except the timezone used is the current &#8220;reporting timezone&#8221; (rather than the default <code>TZ</code> environment variable scheme), and the result is returned into a caller-declared buffer (rather than a private buffer). </p>
<p> Like <code><a href="/docs/linux/man/3-localtime/">localtime</a></code>(3) the time to be converted is passed via <i>clock</i>, and the <i>result </i> contains the components broken out in the elements of the <i>tm</i> struct. </p>
<p> <code>pmLocaltime</code> returns <i>result</i> as the value of the function. </p>
<p> The default current reporting timezone is as defined by the <code>TZ</code> environment variable, so <code>pmLocaltime</code> and <code><a href="/docs/linux/man/3-localtime/">localtime</a></code>(3) will initially produce a similar encoding of the date and time. </p>
<p> Use <code><a href="/docs/linux/man/3-pmnewzone/">pmNewZone</a></code>(3), <code><a href="/docs/linux/man/3-pmnewcontextzone/">pmNewContextZone</a></code>(3) or <code><a href="/docs/linux/man/3-pmusezone/">pmUseZone</a></code>(3) to establish a new current reporting timezone that will affect <code>pmLocaltime</code> but not <code><a href="/docs/linux/man/3-localtime/">localtime</a></code>(3).</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-localtime/">localtime</a></code>(3), <code><a href="/docs/linux/man/3-pmapi/">PMAPI</a></code>(3), <code><a href="/docs/linux/man/3-pmctime/">pmCtime</a></code>(3), <code><a href="/docs/linux/man/3-pmgetconfig/">pmGetConfig</a></code>(3), <code><a href="/docs/linux/man/3-pmnewcontextzone/">pmNewContextZone</a></code>(3), <code><a href="/docs/linux/man/3-pmnewzone/">pmNewZone</a></code>(3), <code><a href="/docs/linux/man/3-pmusezone/">pmUseZone</a></code>(3), <code><a href="/docs/linux/man/5-pcp-conf/">pcp.conf</a></code>(5) and <code><a href="/docs/linux/man/5-pcp-env/">pcp.env</a></code>(5). </p>
