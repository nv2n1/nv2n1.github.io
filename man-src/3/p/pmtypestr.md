---
title: "pmtypestr(3)"
name: "pmtypestr"
section: "3"
letter: "p"
url: "/docs/linux/man/3-pmtypestr/"
description: "pmTypeStr, pmTypeStr_r – convert a performance metric type into a string"
---

<p><code>pmTypeStr</code>, <code>pmTypeStr_r</code> &#8211; convert a performance metric type into a string</p>
<h2>C Synopsis</h2>
<p><code> #include &lt;pcp/pmapi.h&gt; </p>
<p> const char *pmTypeStr(int </code><i>type</i>);<br />
 char *pmTypeStr_r(int <i>type</i>, char *<i>buf</i>, int <i>buflen</i>); </p>
<p> cc &#8230; -lpcp</p>
<h2>Description</h2>
<p>Given a performance metric <i>type</i>, <code>pmTypeStr</code> produces a terse ASCII equivalent, appropriate for use in error and diagnostic messages. The <code>pmTypeStr_r</code> function does the same, but stores the result in a user-supplied buffer <i>buf</i> of length <i>buflen</i>, which should have room for at least 20 bytes. </p>
<p> The value for <i>type</i> is typically extracted from a <i>pmDesc</i> structure, following a call to <code><a href="/docs/linux/man/3-pmlookupdesc/">pmLookupDesc</a></code>(3) for a particular performance metric. </p>
<p> Examples are <code>32</code> (for <i>type</i> equals <code>PM_TYPE_32</code>), <code>U64</code> (for <i>type</i> equals <code>PM_TYPE_U64</code>), <code>AGGREGATE</code> (for <i>type</i> equals <code>PM_TYPE_AGGREGATE</code>), etc. </p>
<p> The string value result for <code>pmTypeStr</code> is held in a single static buffer, so the returned value is only valid until the next call to <code>pmTypeStr</code>.</p>
<h2>Notes</h2>
<p><code>pmTypeStr</code> returns a pointer to a static buffer and hence is not thread-safe. Multi-threaded applications should use <code>pmTypeStr_r</code> instead.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-pmapi/">PMAPI</a></code>(3), <code><a href="/docs/linux/man/3-pmatomstr/">pmAtomStr</a></code>(3), <code><a href="/docs/linux/man/3-pmconvscale/">pmConvScale</a></code>(3), <code><a href="/docs/linux/man/3-pmextractvalue/">pmExtractValue</a></code>(3), <code><a href="/docs/linux/man/3-pmlookupdesc/">pmLookupDesc</a></code>(3), <code><a href="/docs/linux/man/3-pmprintvalue/">pmPrintValue</a></code>(3) and <code><a href="/docs/linux/man/3-pmunitsstr/">pmUnitsStr</a></code>(3). </p>
