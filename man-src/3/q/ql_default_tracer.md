---
title: "ql_default_tracer(3)"
name: "ql_default_tracer"
section: "3"
letter: "q"
url: "/docs/linux/man/3-ql_default_tracer/"
description: "ql/utilities/tracing.hpp – tracing facilities"
---

<p>ql/utilities/tracing.hpp &#8211; tracing facilities </p>
<h2>Synopsis</h2>
<p>#include &lt;ql/types.hpp&gt;<br />
 #include &lt;ql/errors.hpp&gt;<br />
 #include &lt;ql/patterns/singleton.hpp&gt;<br />
 #include &lt;boost/current_function.hpp&gt;<br />
 #include &lt;iosfwd&gt; </p>
<h3>Defines</h3>
<p>#define <code>QL_DEFAULT_TRACER</code> </p>
<p> #define <code>QL_TRACE_ENABLE</code><br />
 <i>enable tracing </i><br />
 #define <code>QL_TRACE_DISABLE</code><br />
 <i>disable tracing </i><br />
 #define <code>QL_TRACE_ON</code>(out)<br />
 <i>set tracing stream </i><br />
 #define <code>QL_TRACE</code>(message)<br />
 <i>output tracing information </i><br />
 #define <code>QL_TRACE_ENTER_FUNCTION</code><br />
 <i>output tracing information </i><br />
 #define <code>QL_TRACE_EXIT_FUNCTION</code><br />
 <i>output tracing information </i><br />
 #define <code>QL_TRACE_LOCATION</code><br />
 <i>output tracing information </i><br />
 #define <code>QL_TRACE_VARIABLE</code>(variable)<br />
 <i>output tracing information </i></p>
<h2>Detailed Description</h2>
<p>tracing facilities </p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
