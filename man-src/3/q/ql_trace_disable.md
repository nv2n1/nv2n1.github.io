---
title: "ql_trace_disable(3)"
name: "ql_trace_disable"
section: "3"
letter: "q"
url: "/docs/linux/man/3-ql_trace_disable/"
description: "Debugging macros –"
---

<p>Debugging macros &#8211; </p>
<h3>Defines</h3>
<p>#define <code>QL_TRACE_ENABLE</code><br />
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
<p>For debugging purposes, macros can be used to output information about the code being executed.</p>
<h2>Define Documentation</h2>
<h3>#define QL_TRACE_ENABLE</h3>
<p>enable tracing </p>
<p> The statement </p>
<pre> QL_TRACE_ENABLE;</pre>
<p>&nbsp;<wbr>can be used to enable tracing. Such statement might be ignored;&nbsp;<wbr>refer to QL_TRACE for details.&nbsp;<wbr> </p>
<p> <code>Examples: </code> <code>tracing_example.cpp</code>.</p>
<h3>#define QL_TRACE_DISABLE</h3>
<p>disable tracing </p>
<p> The statement </p>
<pre> QL_TRACE_DISABLE;</pre>
<p>&nbsp;<wbr>can be used to disable tracing. Such statement might be ignored;&nbsp;<wbr>refer to QL_TRACE for details.&nbsp;<wbr></p>
<h3>#define QL_TRACE_ON(out)</h3>
<p>set tracing stream </p>
<p> The statement </p>
<pre> QL_TRACE_ON(stream);</pre>
<p>&nbsp;<wbr>can be used to set the stream where tracing messages are output. Such statement might be ignored;&nbsp;<wbr>refer to QL_TRACE for details.&nbsp;<wbr></p>
<h3>#define QL_TRACE(message)</h3>
<p>output tracing information </p>
<p> The statement </p>
<pre> QL_TRACE(message);</pre>
<p>&nbsp;<wbr>can be used to output a trace of the code being executed. If tracing was disabled during configuration, such statements are removed by the preprocessor for maximum performance;&nbsp;<wbr>if it was enabled, whether and where the message is output depends on the current settings.&nbsp;<wbr> </p>
<p> <code>Examples: </code> <code>tracing_example.cpp</code>.</p>
<h3>#define QL_TRACE_ENTER_FUNCTION</h3>
<p>output tracing information </p>
<p> The statement </p>
<pre> QL_TRACE_ENTER_FUNCTION;</pre>
<p>&nbsp;<wbr>can be used at the beginning of a function to trace the fact that the program execution is entering such function. It should be paired with a corresponding QL_TRACE_EXIT_FUNCTION macro. Such statement might be ignored;&nbsp;<wbr>refer to QL_TRACE for details. Also, function information might not be available depending on the compiler.&nbsp;<wbr> </p>
<p> <code>Examples: </code> <code>tracing_example.cpp</code>.</p>
<h3>#define QL_TRACE_EXIT_FUNCTION</h3>
<p>output tracing information </p>
<p> The statement </p>
<pre> QL_TRACE_EXIT_FUNCTION;</pre>
<p>&nbsp;<wbr>can be used before returning from a function to trace the fact that the program execution is exiting such function. It should be paired with a corresponding QL_TRACE_ENTER_FUNCTION macro. Such statement might be ignored;&nbsp;<wbr>refer to QL_TRACE for details. Also, function information might not be available depending on the compiler.&nbsp;<wbr> </p>
<p> <code>Examples: </code> <code>tracing_example.cpp</code>.</p>
<h3>#define QL_TRACE_LOCATION</h3>
<p>output tracing information </p>
<p> The statement </p>
<pre> QL_TRACE_LOCATION;</pre>
<p>&nbsp;<wbr>can be used to trace the current file and line. Such statement might be ignored;&nbsp;<wbr>refer to QL_TRACE for details.&nbsp;<wbr> </p>
<p> <code>Examples: </code> <code>tracing_example.cpp</code>.</p>
<h3>#define QL_TRACE_VARIABLE(variable)</h3>
<p>output tracing information </p>
<p> The statement </p>
<pre> QL_TRACE_VARIABLE(variable);</pre>
<p>&nbsp;<wbr>can be used to trace the current value of a variable. Such statement might be ignored;&nbsp;<wbr>refer to QL_TRACE for details. Also, the variable type must allow sending it to an output stream.&nbsp;<wbr> </p>
<p> <code>Examples: </code> <code>tracing_example.cpp</code>.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
