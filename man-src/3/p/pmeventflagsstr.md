---
title: "pmeventflagsstr(3)"
name: "pmeventflagsstr"
section: "3"
letter: "p"
url: "/docs/linux/man/3-pmeventflagsstr/"
description: "pmEventFlagsStr, pmEventFlagsStr_r – convert an event record flags value into a string"
---

<p><code>pmEventFlagsStr</code>, <code>pmEventFlagsStr_r</code> &#8211; convert an event record flags value into a string</p>
<h2>C Synopsis</h2>
<p><code> #include &lt;pcp/pmapi.h&gt; </p>
<p> const char *pmEventFlagsStr(int </code><i>flags</i>);<br />
 char *pmEventFlagsStr_r(int <i>flags</i>, char *<i>buf</i>, int <i>buflen</i>); </p>
<p> cc &#8230; -lpcp</p>
<h2>Description</h2>
<p>For use in error and diagnostic messages, <code>pmEventFlagsStr</code> returns a `human readable&#8217; version of the value <i>flags</i>, assuming this to be the <code>er_flags</code> field of a <code>pmEventRecord</code> or <code>pmEventHighResRecord</code>. The <code>pmEventFlagsStr_r</code> function does the same, but stores the result in a user-supplied buffer <i>buf</i> of length <i>buflen</i>, which should have room for at least 64 bytes. </p>
<p> The string value result from <code>pmEventFlagsStr</code> is held in a single static buffer, so the returned value is only valid until the next call to <code>pmEventFlagsStr</code>.</p>
<h2>Notes</h2>
<p><code>pmEventFlagsStr</code> returns a pointer to a static buffer and hence is not thread-safe. Multi-threaded applications should use <code>pmEventFlagsStr_r</code> instead.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-pmapi/">PMAPI</a></code>(3) and <code><a href="/docs/linux/man/3-pmdaeventaddrecord/">pmdaEventAddRecord</a></code>(3). </p>
