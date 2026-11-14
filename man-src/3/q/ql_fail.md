---
title: "ql_fail(3)"
name: "ql_fail"
section: "3"
letter: "q"
url: "/docs/linux/man/3-ql_fail/"
description: "ql/errors.hpp – Classes and functions for error handling."
---

<p>ql/errors.hpp &#8211; Classes and functions for error handling. </p>
<h2>Synopsis</h2>
<p>#include &lt;ql/qldefines.hpp&gt;<br />
 #include &lt;boost/assert.hpp&gt;<br />
 #include &lt;boost/current_function.hpp&gt;<br />
 #include &lt;boost/shared_ptr.hpp&gt;<br />
 #include &lt;exception&gt;<br />
 #include &lt;sstream&gt; </p>
<h3>Classes</h3>
<p>class <code>Error</code><br />
 <i>Base error class. </i></p>
<h3>Defines</h3>
<p>#define <code>QL_FAIL</code>(message)<br />
 <i>throw an error (possibly with file and line information) </i><br />
 #define <code>QL_ASSERT</code>(condition, message)<br />
 <i>throw an error if the given condition is not verified </i><br />
 #define <code>QL_REQUIRE</code>(condition, message)<br />
 <i>throw an error if the given pre-condition is not verified </i><br />
 #define <code>QL_ENSURE</code>(condition, message)<br />
 <i>throw an error if the given post-condition is not verified </i></p>
<h2>Detailed Description</h2>
<p>Classes and functions for error handling. </p>
<h2>Define Documentation</h2>
<h3>#define QL_FAIL(message)</h3>
<p><code>Value:</code> </p>
<pre>do { std::ostringstream _ql_msg_stream; _ql_msg_stream &lt;&lt; message; throw QuantLib::Error(__FILE__,__LINE__, BOOST_CURRENT_FUNCTION,_ql_msg_stream.str()); } while (false)</pre>
<p>throw an error (possibly with file and line information) </p>
<h3>#define QL_ASSERT(condition, message)</h3>
<p><code>Value:</code> </p>
<pre>if (!(condition)) { std::ostringstream _ql_msg_stream; _ql_msg_stream &lt;&lt; message; throw QuantLib::Error(__FILE__,__LINE__, BOOST_CURRENT_FUNCTION,_ql_msg_stream.str()); } else</pre>
<p>throw an error if the given condition is not verified </p>
<h3>#define QL_REQUIRE(condition, message)</h3>
<p><code>Value:</code> </p>
<pre>if (!(condition)) { std::ostringstream _ql_msg_stream; _ql_msg_stream &lt;&lt; message; throw QuantLib::Error(__FILE__,__LINE__, BOOST_CURRENT_FUNCTION,_ql_msg_stream.str()); } else</pre>
<p>throw an error if the given pre-condition is not verified </p>
<p> <code>Examples: </code> <code>DiscreteHedging.cpp</code>, and <code>swapvaluation.cpp</code>.</p>
<h3>#define QL_ENSURE(condition, message)</h3>
<p><code>Value:</code> </p>
<pre>if (!(condition)) { std::ostringstream _ql_msg_stream; _ql_msg_stream &lt;&lt; message; throw QuantLib::Error(__FILE__,__LINE__, BOOST_CURRENT_FUNCTION,_ql_msg_stream.str()); } else</pre>
<p>throw an error if the given post-condition is not verified </p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
