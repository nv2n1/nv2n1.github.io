---
title: "pmatomstr(3)"
name: "pmatomstr"
section: "3"
letter: "p"
url: "/docs/linux/man/3-pmatomstr/"
description: "pmAtomStr, pmAtomStr_r – convert a performance metric value into a string"
---

<p><code>pmAtomStr</code>, <code>pmAtomStr_r</code> &#8211; convert a performance metric value into a string</p>
<h2>C Synopsis</h2>
<p><code> #include &lt;pcp/pmapi.h&gt; </p>
<p> const char *pmAtomStr(const pmAtomValue *</code><i>avp</i>, int <i>type</i>);<br />
 char *pmAtomStr_r(const pmAtomValue *<i>avp</i>, int <i>type</i>, char *<i>buf</i>, int <i>buflen</i>); </p>
<p> cc &#8230; -lpcp</p>
<h2>Description</h2>
<p>All performance metric values may be encoded in a <i>pmAtomValue</i> union, defined as follows; </p>
<pre>typedef union {
 __int32_t l; /* 32-bit signed */
 __uint32_t ul; /* 32-bit unsigned */
 __int64_t ll; /* 64-bit signed */
 __uint64_t ull; /* 64-bit unsigned */
 float f; /* 32-bit floating point */
 double d; /* 64-bit floating point */
 char *cp; /* char ptr */
 pmValueBlock *vbp; /* pmValueBlock ptr */
} pmAtomValue;</pre>
<p>Given the performance metric value pointed to by <i>avp</i>, and a performance metric type defined by <i>type</i>, <code>pmAtomStr</code> will generate the corresponding metric value as a string, suitable for diagnostic or report output. The <code>pmAtomStr_r</code> function does the same, but stores the result in a user-supplied buffer <i>buf</i> of length <i>buflen</i>, which should have room for at least 80 bytes. </p>
<p> The value for <i>type</i> is typically extracted from a <i>pmDesc</i> structure, following a call to <code><a href="/docs/linux/man/3-pmlookupdesc/">pmLookupDesc</a></code>(3) for a particular performance metric. </p>
<p> If the <i>type</i> is <code>PM_TYPE_STRING</code> values longer than 38 characters will be truncated after 34 characters, and truncation shown with ellipsis &#8220;&#8230;&#8221; at the end of the value. </p>
<p> If the <i>type</i> is <code>PM_TYPE_AGGREGATE</code> then up to the first three 32-bit words are displayed as hexadecimal values. </p>
<p> If the <i>type</i> is <code>PM_TYPE_EVENT</code> then a summary of the number of event records found in the value is generated. </p>
<p> The return value from <code>pmAtomStr</code> is held in a single static buffer, so the returned value is only valid until the next call to <code>pmAtomStr</code>.</p>
<h2>Notes</h2>
<p><code>pmAtomStr</code> returns a pointer to a static buffer and hence is not thread-safe. Multi-threaded applications should use <code>pmAtomStr_r</code> instead.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-pmapi/">PMAPI</a></code>(3), <code><a href="/docs/linux/man/3-pmconvscale/">pmConvScale</a></code>(3), <code><a href="/docs/linux/man/3-pmextractvalue/">pmExtractValue</a></code>(3), <code><a href="/docs/linux/man/3-pmlookupdesc/">pmLookupDesc</a></code>(3), <code><a href="/docs/linux/man/3-pmprintvalue/">pmPrintValue</a></code>(3), <code><a href="/docs/linux/man/3-pmtypestr/">pmTypeStr</a></code>(3) and <code><a href="/docs/linux/man/3-pmunitsstr/">pmUnitsStr</a></code>(3). </p>
