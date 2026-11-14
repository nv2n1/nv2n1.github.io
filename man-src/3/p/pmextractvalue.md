---
title: "pmextractvalue(3)"
name: "pmextractvalue"
section: "3"
letter: "p"
url: "/docs/linux/man/3-pmextractvalue/"
description: "pmExtractValue – extract a performance metric value from a pmResult structure"
---

<p><code>pmExtractValue</code> &#8211; extract a performance metric value from a pmResult structure</p>
<h2>C Synopsis</h2>
<p><code> #include &lt;pcp/pmapi.h&gt; </p>
<p> int pmExtractValue(int </code><i>valfmt</i>, const pmValue *<i>ival</i>, int&nbsp;<wbr><i>itype</i>, pmAtomValue&nbsp;<wbr>*<i>oval</i>, int&nbsp;<wbr><i>otype</i>); </p>
<p> cc &#8230; -lpcp</p>
<h2>Description</h2>
<p>The <i>pmValue</i> structure is embedded within the <i>pmResult</i> structure that is used to return one or more performance metrics; see <code><a href="/docs/linux/man/3-pmfetch/">pmFetch</a></code>(3). </p>
<p> All performance metric values may be encoded in a <i>pmAtomValue</i> union, defined as follows; </p>
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
<p>The routine <code>pmExtractValue</code> provides a convenient mechanism for extracting values from the <i>pmValue</i> part of a <i>pmResult</i> structure, optionally converting the data type, and making the result available to the application programmer. </p>
<p> <i>itype </i> defines the data type of the input value held in <i>ival</i> according to the storage format defined by <i>valfmt</i> (see <code><a href="/docs/linux/man/3-pmfetch/">pmFetch</a></code>(3)). <i>otype</i> defines the data type of the result to be placed in <i>oval</i>. </p>
<p> The value for <i>itype</i> is typically extracted from a <i>pmDesc</i> structure, following a call to <code><a href="/docs/linux/man/3-pmlookupdesc/">pmLookupDesc</a></code>(3) for a particular performance metric. </p>
<p> The <i>otype</i> value should be one of the defined <code>PM_TYPE_</code>&#8230; values, that have a 1:1 correspondence with the fields in the <i>pmAtomValue</i> union. </p>
<p> Normally the <i>valfmt</i> parameter would be plucked from the same <i>pmResult</i> structure that provides the <i>ival</i> parameter, and if <i>valfmt</i> specifies <code>PM_VAL_INSITU</code>, then the following types are not allowed, as these cannot be encoded in 32-bits; <code>__int64_t</code>, <code>__uint64_t</code>, <code>double</code>, <code>char *</code> and <code>void *</code> (the corresponding <i>itype</i> values are <code>PM_TYPE_64</code>, <code>PM_TYPE_U64</code>, <code>PM_TYPE_DOUBLE</code>, <code>PM_TYPE_STRING</code>, <code>PM_TYPE_AGGREGATE</code> and <code>PM_TYPE_EVENT</code> respectively). If <i>valfmt</i> specifies <code>PM_VAL_PTR</code>, then the value will be extracted from the associated <i>pmValueBlock</i> structure, and the <code>__int32_t</code>, <code>__uint32_t</code> and <code>float</code> options (<i>itype</i> being <code>PM_TYPE_32</code>, <code>PM_TYPE_U32</code> and <code>PM_TYPE_FLOAT</code> respectively) are not allowed, as <code>PM_VAL_INSITU</code> is the appropriate encoding for these. </p>
<p> The following table defines the various possibilities for the type conversion &#8212; the input type (<i>itype</i>) is shown vertically, and the output type (<i>otype</i>) is shown horizontally. Y means the conversion is always acceptable, N means the conversion can never be performed (the function returns <code>PM_ERR_CONV</code>), P means the conversion may lose accuracy (but no error status is returned), T means the result may be subject to high-order truncation (in which case the function returns <code>PM_ERR_TRUNC</code>) and S means the conversion may be impossible due to the sign of the input value (in which case the function returns <code>PM_ERR_SIGN</code>). If an error occurs, the value represented by <i>oval</i> will be zero (or <code>NULL</code>). </p>
<p> Note that although some of the conversions involving the types <code>PM_TYPE_STRING</code> and <code>PM_TYPE_AGGREGATE</code> are indeed possible, but are marked N &#8211; the rationale is that <code>pmExtractValue</code> should not be attempting to duplicate functionality already available in the C library via <code><a href="/docs/linux/man/3-sscanf/">sscanf</a></code>(3) and <code><a href="/docs/linux/man/3-sprintf/">sprintf</a></code>(3). </p>
<p> No conversion involving the type <code>PM_TYPE_EVENT</code> is supported. </p>
<pre> | 32 | U32 | 64 | U64 | FLOAT | DBLE | STRNG | AGGR | EVENT
======|=====|=======|=====|=======|=======|======|=======|======|=======
32 | Y | S | Y | S | P | P | N | N | N
U32 | T | Y | Y | Y | P | P | N | N | N
64 | T | T,S | Y | S | P | P | N | N | N
U64 | T | T | T | Y | P | P | N | N | N
FLOAT | P,T | P,T,S | P,T | P,T,S | Y | Y | N | N | N
DBLE | P,T | P,T,S | P,T | P,T,S | P | Y | N | N | N
STRNG | N | N | N | N | N | N | Y | N | N
AGGR | N | N | N | N | N | N | N | Y | N
EVENT | N | N | N | N | N | N | N | N | N</pre>
<p>In the cases where multiple conversion errors could occur, the first encountered error will be notified, and the order of checking is not defined. </p>
<p> If the output conversion is to one of the pointer types, i.e. <i>otype</i> is <code>PM_TYPE_STRING</code> or <code>PM_TYPE_AGGREGATE</code>, then the value buffer will have been allocated by <code><a href="/docs/linux/man/3-pmextractvalue/">pmExtractValue</a></code>(3) using <code><a href="/docs/linux/man/3-malloc/">malloc</a></code>(3), and it is the caller&#8217;s responsibility to free the space when it is no longer required. </p>
<p> Although this function appears rather complex, it has been constructed to assist the development of performance tools that wish to convert values, whose type is only known via the <i>type</i> field in a <i>pmDesc</i> structure, into a canonical type for local processing. See the <code>pmFetchGroup</code> functions for a simpler alternative.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-pmapi/">PMAPI</a></code>(3), <code><a href="/docs/linux/man/3-pmatomstr/">pmAtomStr</a></code>(3), <code><a href="/docs/linux/man/3-pmconvscale/">pmConvScale</a></code>(3), <code><a href="/docs/linux/man/3-pmfetch/">pmFetch</a></code>(3), <code><a href="/docs/linux/man/3-pmfetchgroup/">pmFetchGroup</a></code>(3), <code><a href="/docs/linux/man/3-pmlookupdesc/">pmLookupDesc</a></code>(3), <code><a href="/docs/linux/man/3-pmprintvalue/">pmPrintValue</a></code>(3), <code><a href="/docs/linux/man/3-pmtypestr/">pmTypeStr</a></code>(3), <code><a href="/docs/linux/man/3-pmunitsstr/">pmUnitsStr</a></code>(3) and <code><a href="/docs/linux/man/3-pmunpackeventrecords/">pmUnpackEventRecords</a></code>(3).</p>
<h2>Diagnostics</h2>
<p><code>PM_ERR_CONV</code></p>
<dl>
<dd>Impossible conversion, marked by N in above table</dl>
<p> <code>PM_ERR_TRUNC</code></p>
<dl>
<dd>High-order truncation occurred</dl>
<p> <code>PM_ERR_SIGN</code></p>
<dl>
<dd>Conversion of negative value to unsigned type attempted </p>
</dl>
