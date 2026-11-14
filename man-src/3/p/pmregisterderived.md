---
title: "pmregisterderived(3)"
name: "pmregisterderived"
section: "3"
letter: "p"
url: "/docs/linux/man/3-pmregisterderived/"
description: "pmRegisterDerived, pmRegisterDerivedMetric – register a derived metric name and definition"
---

<p><code>pmRegisterDerived</code>, <code>pmRegisterDerivedMetric</code> &#8211; register a derived metric name and definition</p>
<h2>C Synopsis</h2>
<p><code> #include &lt;pcp/pmapi.h&gt; </p>
<p> char *pmRegisterDerived(char *</code><i>name</i>, char *<i>expr</i>);<br />
 int pmRegisterDerivedMetric(char *<i>name</i>, char *<i>expr</i>, char **<i>errmsg</i>); </p>
<p> cc &#8230; -lpcp</p>
<h2>Description</h2>
<p>Derived metrics provide a way of extending the Performance Metrics Name Space (PMNS) with new metrics defined at the PCP client-side using arithmetic expressions over the existing performance metrics. </p>
<p> Typical uses would be to aggregate a number of similar metrics to provide a higher-level summary metric or to support the &#8220;delta V over delta V&#8221; class of metrics that are not possible in the base data semantics of PCP. An example of the latter class would be the average I/O size, defined as<br />
 <center><br />
 </center> delta(disk.dev.total_bytes) / delta(disk.dev.total) where both of the disk.dev metrics are counters, and what is required is to to sample both metrics, compute the difference between the current and previous values and then calculate the ratio of these differences. </p>
<p> The arguments to <code>pmRegisterDerived</code> are the <i>name</i> of the new derived metric and <i>expr</i> is an arithmetic expression defining how the values of <i>name</i> should be computed. </p>
<p> <code>pmRegisterDerivedMetric</code> is the exact functional equivalent to <code>pmRegisterDerived</code> except that it provides a simplified model of error handling, where a formatted message is returned via the <i>errmsg</i> parameter. </p>
<p> Syntactic checking is performed at the time <code>pmRegisterDerived</code> is called, but semantic checking is deferred until each new context is created with <code><a href="/docs/linux/man/3-pmnewcontext/">pmNewContext</a></code>(3) or re-established with <code><a href="/docs/linux/man/3-pmreconnectcontext/">pmReconnectContext</a></code>(3), at which time the PMNS and metadata is available to allow semantic checking and the metadata of the derived metrics to be established. This means <code>pmRegisterDerived</code> does not apply retrospectively to any open contexts, so the normal use would be to make all calls to <code>pmRegisterDerived</code> (possibly via <code><a href="/docs/linux/man/3-pmloadderivedconfig/">pmLoadDerivedConfig</a></code>(3)) or <code>pmRegisterDerivedMetric</code> and then call <code><a href="/docs/linux/man/3-pmnewcontext/">pmNewContext</a></code>(3). </p>
<p> <i>name</i> should follow the syntactic rules for the names of performance metrics, namely one or more components separated with a dot (&#8220;.&#8221;), and each component must begin with an alphabetic followed by zero or more characters drawn from the alphabetics, numerics and underscore (&#8220;_&#8221;). For more details, refer to <code><a href="/docs/linux/man/1-pcpintro/">PCPIntro</a></code>(1) and <code><a href="/docs/linux/man/5-pmns/">pmns</a></code>(5). </p>
<p> <i>name</i> must be unique across all derived metrics and should <code>not</code> match the name of any regular metric in the PMNS. It is acceptable for <i>name</i> to share some part of its prefix with an existing subtree of the PMNS, e.g. the average I/O size metric above could be named disk.dev.avgsz which would place it amongst the other disk.dev metrics in the PMNS. Alternatively, derived metrics could populate their own subtree of the PMNS, e.g. the average I/O size metric above could be named my.summary.disk.avgsz . </p>
<p> The expression <i>expr</i> follows these syntactic rules:</p>
<dl>
<dt>*</p>
<dd>Terminal elements are either names of existing metrics or integer constants. Recursive definitions are not allowed, so only the names of regular metrics (not other derived metrics) may be used. Integer constants are constrained to the precision of 32-bit unsigned integers.</p>
<dt>*</p>
<dd>The usual binary arithmetic operators are supported, namely &#8211; addition (&#8220;+&#8221;), subtraction (&#8220;-&#8221;), multiplication (&#8220;*&#8221;) and division (&#8220;/&#8221;) with the normal precedence rules where multiplication and division have higher precedence than addition and subtraction, so a+b*c is evaluated as a+(b*c)</p>
<dt>*</p>
<dd>Parenthesis may be used for grouping.</p>
<dt>*</p>
<dd>The following unary functions operate on a single performance metric and return one or more values. For all functions (except count() and instant() ), the type of the operand metric must be arithmetic (integer of various sizes and signedness, float or double). <center></p>
<table BORDER>
<tr>
<td>
<table>
<tr VALIGN=top>
<td ALIGN=center>Function</td>
<td ALIGN=center>Value
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>avg(x)</td>
<td> A singular instance being the average value across all instances for the metric x.
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>count(x)</td>
<td> A singular instance being the count of the number of instances for the metric x.
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>delta(x)</td>
<td> Returns the difference in values for the metric x between one call to <code><a href="/docs/linux/man/3-pmfetch/">pmFetch</a></code>(3) and the next. There is one value in the result for each instance that appears in both the current and the previous sample.
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>rate(x)</td>
<td> Returns the difference in values for the metric x between one call to <code><a href="/docs/linux/man/3-pmfetch/">pmFetch</a></code>(3) and the next divided by the elapsed time between the calls to <code><a href="/docs/linux/man/3-pmfetch/">pmFetch</a></code>(3). The semantics of the derived metric are based on the semantics of the operand (x) with the dimension in the <code>time</code> domain decreased by one and scaling if required in the time utilization case where the operand is in units of time, and the derived metric is unitless. This mimics the rate conversion applied to counter metrics by tools such as <code><a href="/docs/linux/man/1-pmval/">pmval</a></code>(1), <code><a href="/docs/linux/man/1-pmie/">pmie</a></code>(1) and <code><a href="/docs/linux/man/1-pmchart/">pmchart</a></code>(1). There is one value in the result for each instance that appears in both the current and the previous sample.
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>instant(x)</td>
<td> Returns the current value of the metric x, even it has the semantics of a counter, i.e. PM_SEM_COUNTER. The semantics of the derived metric are based on the semantics of the operand (x); if x has semantics PM_SEM_COUNTER, the semantics of instant(x) is PM_SEM_INSTANT, otherwise the semantics of the derived metric is the same as the semantics of the metric x.
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>max(x)</td>
<td> A singular instance being the maximum value across all instances for the metric x.
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>min(x)</td>
<td> A singular instance being the minimum value across all instances for the metric x.
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>sum(x)</td>
<td> A singular instance being the sum of the values across all instances for the metric x.
</td>
</tr>
</table>
</table>
<p></center></p>
<dt>*</p>
<dd>White space is ignored.</dl>
<h2>Semantic Checks And Rules</h2>
<p>There are a number of conversions required to determine the metadata for a derived metric and to ensure the semantics of the expressions are sound. </p>
<p> In a binary expression, if the semantics of both operands is not a counter (i.e. PM_SEM_INSTANT or PM_SEM_DISCRETE) then the result will have semantics PM_SEM_INSTANT unless both operands are PM_SEM_DISCRETE in which case the result is also PM_SEM_DISCRETE. </p>
<p> The mapping of the pmUnits of the metadata uses the following rules:</p>
<dl>
<dt>*</p>
<dd>If both operands have a dimension of COUNT and the scales are not the same, use the larger scale and convert the values of the operand with the smaller scale.</p>
<dt>*</p>
<dd>If both operands have a dimension of TIME and the scales are not the same, use the larger scale and convert the values of the operand with the smaller scale.</p>
<dt>*</p>
<dd>If both operands have a dimension of SPACE and the scales are not the same, use the larger scale and convert the values of the operand with the smaller scale.</p>
<dt>*</p>
<dd>For addition and subtraction all dimensions for each of the operands and result are identical.</p>
<dt>*</p>
<dd>For multiplication, the dimensions of the result are the sum of the dimensions of the operands.</p>
<dt>*</p>
<dd>For division, the dimensions of the result are the difference of the dimensions of the operands.</dl>
<p> Scale conversion involves division if the dimension is positive else multiplication if the dimension is negative. If scale conversion is applied to either of the operands, the result is promoted to type PM_TYPE_DOUBLE. </p>
<p> Putting all of this together in an example, consider the derived metric defined as follows:<br />
 x = network.interface.speed &#8211; delta(network.interface.in.bytes) / delta(sample.milliseconds)<br />
 The type, dimension and scale settings would propagate up the expression tree as follows. <center></p>
<table BORDER>
<tr>
<td>
<table>
<tr VALIGN=top>
<td ALIGN=center>Expression</td>
<td ALIGN=center>Type</td>
<td ALIGN=center> Dimension &amp; Scale </td>
<td ALIGN=center> Scale Factor(s)
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=4>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>sample.milliseconds</td>
<td>DOUBLE</td>
<td>millisec</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td>delta(&#8230;)</td>
<td>DOUBLE</td>
<td>millisec</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td>network&#8230;bytes</td>
<td>U64</td>
<td>byte</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td>delta(&#8230;)</td>
<td>U64</td>
<td>byte</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td>delta(&#8230;) / delta(&#8230;)</td>
<td>DOUBLE</td>
<td>byte/millisec</td>
<td> /1048576 and *1000
</td>
</tr>
<tr VALIGN=top>
<td>network&#8230;speed</td>
<td>FLOAT</td>
<td>Mbyte/sec</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td>x</td>
<td>DOUBLE</td>
<td>Mbyte/sec</td>
<td>
</td>
</tr>
</table>
</table>
<p></center> </p>
<p> Because semantic checking cannot be done at the time <code>pmRegisterDerived</code> is called, errors found during semantic checking are reported using <code><a href="/docs/linux/man/3-pmprintf/">pmprintf</a></code>(3). These include:</p>
<dl>
<dt>Error: derived metric &lt;name1&gt;: operand: &lt;name2&gt;: &lt;reason&gt;</p>
<dd>There was a problem calling <code><a href="/docs/linux/man/3-pmlookupname/">pmLookupName</a></code>(3) to identify the operand metric &lt;name2&gt; used in the definition of the derived metric &lt;name1&gt;.</p>
<dt>Error: derived metric &lt;name1&gt;: operand (&lt;name2&gt; [&lt;pmid2&gt;]): &lt;reason&gt;</p>
<dd>There was a problem calling <code><a href="/docs/linux/man/3-pmlookupdesc/">pmLookupDesc</a></code>(3) to identify the operand metric &lt;name2&gt; with PMID &lt;pmid2&gt; used in the definition of the derived metric &lt;name1&gt;.</p>
<dt>Semantic error: derived metric &lt;name&gt;: &lt;operand&gt; &lt;op&gt; &lt;operand&gt;: Illegal operator for counters</p>
<dd>If both operands have the semantics of counter, only addition or subtraction make sense, so multiplication and division are not allowed.</p>
<dt>Semantic error: derived metric &lt;name&gt;: &lt;operand&gt; &lt;op&gt; &lt;operand&gt;: Illegal operator for counter and non-counter</p>
<dd>Only multiplication or division are allowed if the left operand has the semantics of a counter and the right operand is <code>not</code> a counter.</p>
<dt>Semantic error: derived metric &lt;name&gt;: &lt;operand&gt; &lt;op&gt; &lt;operand&gt;: Illegal operator for non-counter and counter</p>
<dd>Only multiplication is allowed if the right operand has the semantics of a counter and the left operand is <code>not</code> a counter.</p>
<dt>Semantic error: derived metric &lt;name&gt;: &lt;operand&gt; &lt;op&gt; &lt;operand&gt;: Non-arithmetic type for &lt;left-or-right&gt; operand</p>
<dd>The binary arithmetic operators are only allowed with operands with an arithmetic type (integer of various sizes and signedness, float or double).</p>
<dt>Semantic error: derived metric &lt;name&gt;: &lt;function&gt;(&lt;operand&gt;): Non-arithmetic operand for function</p>
<dd>The unary functions are only defined if the operand has arithmetic type.</p>
<dt>Semantic error: derived metric &lt;name&gt;: Incorrect time dimension for operand</p>
<dd>Rate conversion using the <code>rate</code>() function is only possible for operand metrics with a Time dimension of 0 or 1 (see <code><a href="/docs/linux/man/3-pmlookupdesc/">pmLookupDesc</a></code>(3)). If the operand metric&#8217;s Time dimension is 0, then the derived metrics has a value &quot;per second&quot; (Time dimension of -1). If the operand metric&#8217;s Time dimension is 1, then the derived metrics has a value of time utilization (Time dimension of 0).</dl>
<h2>Expression Evaluation</h2>
<p>For the binary arithmetic operators, if either operand must be scaled (e.g. convert bytes to Kbytes) then the result is promoted to PM_TYPE_DOUBLE. Otherwise the type of the result is determined by the types of the operands, as per the following table which is evaluated from top to bottom until a match is found. <center></p>
<table BORDER>
<tr>
<td>
<table>
<tr VALIGN=top>
<td ALIGN=center>Operand Types</td>
<td ALIGN=center>Operator</td>
<td ALIGN=center>Result Type
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=3>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>either is PM_TYPE_DOUBLE</td>
<td>any</td>
<td>PM_TYPE_DOUBLE
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=3>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>any</td>
<td>division</td>
<td>PM_TYPE_DOUBLE
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=3>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>either is PM_TYPE_FLOAT</td>
<td>any</td>
<td>PM_TYPE_FLOAT
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=3>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>either is PM_TYPE_U64</td>
<td>any</td>
<td>PM_TYPE_U64
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=3>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>either is PM_TYPE_64</td>
<td>any</td>
<td>PM_TYPE_64
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=3>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>either is PM_TYPE_U32</td>
<td>any</td>
<td>PM_TYPE_U32
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=3>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> otherwise (both are PM_TYPE_32) </td>
<td>any</td>
<td>PM_TYPE_32
</td>
</tr>
</table>
</table>
<p></center></p>
<h2>Caveats</h2>
<p>Unary negation is not supported, so the following expressions would be syntactically incorrect, -3*abc and -this.number </p>
<p> Derived metrics are not available when using <code><a href="/docs/linux/man/3-pmfetcharchive/">pmFetchArchive</a></code>(3) as this routine does not use a target list of PMIDs that could be remapped (as is done for <code><a href="/docs/linux/man/3-pmfetch/">pmFetch</a></code>(3)). </p>
<p> There is no <code>pmUnregisterDerived</code> method, so once registered a derived metric persists for the life of the application.</p>
<h2>Diagnostics</h2>
<p>On success, <code>pmRegisterDerived</code> returns NULL. </p>
<p> If a syntactic error is found at the time of registration, the value returned by <code>pmRegisterDerived</code> is a pointer into <i>expr</i> indicating <code>where</code> the error was found. To identify <code>what</code> the error was, the application should call <code><a href="/docs/linux/man/3-pmderivederrstr/">pmDerivedErrStr</a></code>(3) to retrieve the corresponding parser error message. </p>
<p> <code>pmRegisterDerivedMetric</code> returns 0 and <i>errmsg</i> is undefined if the parsing is successful. </p>
<p> If the given <i>expr</i> does not conform to the required syntax <code>pmRegisterDerivedMetric</code> returns -1 and a dynamically allocated error message string in <i>errmsg</i>. The error message is terminated with a newline and includes both the input <i>name</i> and <i>expr</i>, along with an indicator of the position at which the error was detected. e.g.<br />
 Error: pmRegisterDerivedMetric(&quot;my.disk.rates&quot;, &#8230;) syntax error </p>
<p> The position indicator line may be followed by an additional diagnostic line describing the nature of the error, when available. </p>
<p> In the case of an error, the caller is responsible for calling <code><a href="/docs/linux/man/3-free/">free</a></code>(3) to release the space allocated for <i>errmsg</i>.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-pcpintro/">PCPIntro</a></code>(1), <code><a href="/docs/linux/man/3-free/">free</a></code>(3), <code><a href="/docs/linux/man/3-pmapi/">PMAPI</a></code>(3), <code><a href="/docs/linux/man/3-pmderivederrstr/">pmDerivedErrStr</a></code>(3), <code><a href="/docs/linux/man/3-pmfetch/">pmFetch</a></code>(3), <code><a href="/docs/linux/man/3-pmloadderivedconfig/">pmLoadDerivedConfig</a></code>(3), <code><a href="/docs/linux/man/3-pmnewcontext/">pmNewContext</a></code>(3) and <code><a href="/docs/linux/man/3-pmreconnectcontext/">pmReconnectContext</a></code>(3). </p>
