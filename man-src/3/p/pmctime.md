---
title: "pmctime(3)"
name: "pmctime"
section: "3"
letter: "p"
url: "/docs/linux/man/3-pmctime/"
description: "pmCtime – format the date and time for a reporting timezone"
---

<p><code>pmCtime</code> &#8211; format the date and time for a reporting timezone</p>
<h2>C Synopsis</h2>
<p><code> #include &lt;time.h&gt;<br />
 #include &lt;pcp/pmapi.h&gt; </p>
<p> char *pmCtime(const time_t *</code><i>clock</i>, char *<i>buf</i>); </p>
<p> cc &#8230; -lpcp</p>
<h2>Description</h2>
<p><code>pmCtime</code> is very similar to <code><a href="/docs/linux/man/3-ctime/">ctime</a></code>(3), except the timezone used is the current &#8220;reporting timezone&#8221; (rather than the default <code>TZ</code> environment variable scheme), and the result is returned into a caller-declared buffer (rather than a private buffer). </p>
<p> Like <code><a href="/docs/linux/man/3-ctime/">ctime</a></code>(3) the time to be converted is passed via <i>clock</i>, and the result in <i>buf</i> is fixed width fields in the format: </p>
<p> Fri Sep 13 00:00:00 1986

