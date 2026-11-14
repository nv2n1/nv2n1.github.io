---
title: "pmunitsstr(3)"
name: "pmunitsstr"
section: "3"
letter: "p"
url: "/docs/linux/man/3-pmunitsstr/"
description: "pmUnitsStr, pmUnitsStr_r – convert a performance metric’s units into a string"
---

<p><code>pmUnitsStr</code>, <code>pmUnitsStr_r &#8211; convert a performance metric&#8217;s units into a string </code></p>
<h2>C Synopsis</h2>
<p><code> #include &lt;pcp/pmapi.h&gt; </p>
<p> const char *pmUnitsStr(const pmUnits *</code><i>pu</i>);<br />
 char *pmUnitsStr_r(const pmUnits *<i>pu</i>, char *<i>buf</i>, int <i>buflen</i>); </p>
<p> cc &#8230; -lpcp</p>
<h2>Description</h2>
<p>The encoding of a performance metric&#8217;s dimensionality and scale uses a <i>pmUnits</i> structure; see <code><a href="/docs/linux/man/3-pmlookupdesc/">pmLookupDesc</a></code>(3). </p>
<p> As an aid to labeling graphs and tables, or for error messages, <code>pmUnitsStr</code> will take a dimension and scale specification as per <i>pu</i>, and return the corresponding text string. The <code>pmUnitsStr_r</code> function does the same, but stores the result in a user-supplied buffer <i>buf</i> of length <i>buflen</i>, which should have room for at least 60 bytes. If <i>buflen</i> is less than 60 then <code>pmUnitsStr_r</code> returns <code>NULL</code> and <i>buf</i> is not changed. </p>
<p> For example <i>{1, -2, 0, PM_SPACE_MBYTE, PM_TIME_SEC, 0}</i>, as the value of <i>*pu</i> gives the result string <i>Mbyte / sec^2</i>. </p>
<p> The string value result from <code>pmUnitsStr</code> is held in a single static buffer, so the returned value is only valid until the next call to <code>pmUnitsStr</code>. </p>
<p> If the &#8220;count&#8221; dimension is non-zero, and the &#8220;count&#8221; scale is not zero, then the text string will include a decimal scaling factor, eg. <i>count x 10^6</i>. </p>
<p> As a special case, if all components of the dimension are zero, then the &#8220;count&#8221; scale is used to produce the text. If this scale is zero the result is an empty string, otherwise the result is of the form <i>x1 0^2</i>.</p>
<h2>Notes</h2>
<p><code>pmUnitsStr</code> returns a pointer to a static buffer and hence is not thread-safe. Multi-threaded applications should use <code>pmUnitsStr_r</code> instead.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-pmapi/">PMAPI</a></code>(3), <code><a href="/docs/linux/man/3-pmatomstr/">pmAtomStr</a></code>(3), <code><a href="/docs/linux/man/3-pmconvscale/">pmConvScale</a></code>(3), <code><a href="/docs/linux/man/3-pmextractvalue/">pmExtractValue</a></code>(3), <code><a href="/docs/linux/man/3-pmlookupdesc/">pmLookupDesc</a></code>(3), <code><a href="/docs/linux/man/3-pmprintvalue/">pmPrintValue</a></code>(3) and <code><a href="/docs/linux/man/3-pmtypestr/">pmTypeStr</a></code>(3). </p>
