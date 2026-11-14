---
title: "pmconvscale(3)"
name: "pmconvscale"
section: "3"
letter: "p"
url: "/docs/linux/man/3-pmconvscale/"
description: "pmConvScale – rescale a performance metric value"
---

<p><code>pmConvScale</code> &#8211; rescale a performance metric value</p>
<h2>C Synopsis</h2>
<p><code> #include &lt;pcp/pmapi.h&gt; </p>
<p> int pmConvScale(int </code><i>type</i>, const pmAtomValue *<i>ival</i>, const pmUnits&nbsp;<wbr>*<i>iunit</i>, pmAtomValue&nbsp;<wbr>*<i>oval</i>, const pmUnits&nbsp;<wbr>*<i>ounit</i>); </p>
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
<p>The encoding of a performance metric&#8217;s dimensionality and scale uses a <i>pmUnits</i> structure; see <code><a href="/docs/linux/man/3-pmlookupdesc/">pmLookupDesc</a></code>(3). </p>
<p> Given a performance metric value pointed to by <i>ival</i> multiply it by a scale factor and return the value in <i>oval</i>. The scaling takes place from the units defined by <i>iunit</i> into the units defined by <i>ounit</i>. Both input and output units must have the same dimensionality. </p>
<p> The performance metric type for both input and output values is determined by <i>type</i>, the value for which is typically extracted from a <i>pmDesc</i> structure, following a call to <code><a href="/docs/linux/man/3-pmlookupdesc/">pmLookupDesc</a></code>(3) for a particular performance metric. </p>
<p> <code>pmConvScale</code> is most useful when values returned via <code><a href="/docs/linux/man/3-pmfetch/">pmFetch</a></code>(3), (and possibly extracted using <code><a href="/docs/linux/man/3-pmextractvalue/">pmExtractValue</a></code>(3)) need to be normalized into some canonical scale and units for the purposes of computation. </p>
<p> As a special case, if all components of the dimension are zero, then this is treated as synonymous with a &#8220;count&#8221; dimension of one, and so the &#8220;count&#8221; scale components determine the relative scaling. This accommodates the case where performance metrics are dimensionless, without special case handling on the part of the caller.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-pmapi/">PMAPI</a></code>(3), <code><a href="/docs/linux/man/3-pmatomstr/">pmAtomStr</a></code>(3), <code><a href="/docs/linux/man/3-pmextractvalue/">pmExtractValue</a></code>(3), <code><a href="/docs/linux/man/3-pmfetch/">pmFetch</a></code>(3), <code><a href="/docs/linux/man/3-pmlookupdesc/">pmLookupDesc</a></code>(3), <code><a href="/docs/linux/man/3-pmprintvalue/">pmPrintValue</a></code>(3), <code><a href="/docs/linux/man/3-pmtypestr/">pmTypeStr</a></code>(3) and <code><a href="/docs/linux/man/3-pmunitsstr/">pmUnitsStr</a></code>(3).</p>
<h2>Diagnostics</h2>
<p><code>PM_ERR_CONV</code></p>
<dl>
<dd><i>iunit</i> and <i>ounit</i> have different dimensionality, or have inappropriate <i>type</i></dl>
<p> <code>PM_ERR_UNIT</code></p>
<dl>
<dd>Inappropriate <i>iunit</i> or <i>ounit</i> parameter </p>
</dl>
