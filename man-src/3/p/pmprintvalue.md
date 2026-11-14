---
title: "pmprintvalue(3)"
name: "pmprintvalue"
section: "3"
letter: "p"
url: "/docs/linux/man/3-pmprintvalue/"
description: "pmPrintValue – print a performance metric value"
---

<p><code>pmPrintValue</code> &#8211; print a performance metric value</p>
<h2>C Synopsis</h2>
<p><code> #include &lt;stdio.h&gt;<br />
 #include &lt;pcp/pmapi.h&gt; </p>
<p> void pmPrintValue(FILE *</code><i>f</i>, int <i>valfmt</i>, int <i>type</i>, const pmValue&nbsp;<wbr>*<i>val</i>, int&nbsp;<wbr><i>minwidth</i>); </p>
<p> cc &#8230; -lpcp</p>
<h2>Description</h2>
<p>The value of a single performance metric (as identified by <i>val</i>) is printed on the standard I/O stream identified by <i>f</i>. </p>
<p> The value of the performance metric is interpreted according to the format of <i>val</i> as defined by <i>valfmt</i> (from a <i>pmValueSet</i> within a <i>pmResult</i> structure; see <code><a href="/docs/linux/man/3-pmfetch/">pmFetch</a></code>(3)) and the generic description of the metrics type passed in via <i>type</i>. </p>
<p> The value for <i>type</i> is typically extracted from a <i>pmDesc</i> structure, following a call to <code><a href="/docs/linux/man/3-pmlookupdesc/">pmLookupDesc</a></code>(3) for a particular performance metric. </p>
<p> The output will be optionally padded to be at least <i>minwidth</i> characters wide. </p>
<p> <code>pmPrintValue</code> is most useful for displaying values of performance metrics from <code><a href="/docs/linux/man/3-pmfetch/">pmFetch</a></code>(3) (which returns a set of <i>valfmt</i> and <i>val</i> pairs for each requested metric), based upon the metrics type as returned from <code><a href="/docs/linux/man/3-pmlookupdesc/">pmLookupDesc</a></code>(3).</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-pmapi/">PMAPI</a></code>(3), <code><a href="/docs/linux/man/3-pmatomstr/">pmAtomStr</a></code>(3), <code><a href="/docs/linux/man/3-pmconvscale/">pmConvScale</a></code>(3), <code><a href="/docs/linux/man/3-pmextractvalue/">pmExtractValue</a></code>(3), <code><a href="/docs/linux/man/3-pmfetch/">pmFetch</a></code>(3), <code><a href="/docs/linux/man/3-pmlookupdesc/">pmLookupDesc</a></code>(3), <code><a href="/docs/linux/man/3-pmtypestr/">pmTypeStr</a></code>(3) and <code><a href="/docs/linux/man/3-pmunitsstr/">pmUnitsStr</a></code>(3). </p>
