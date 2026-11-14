---
title: "qldefines(3)"
name: "qldefines"
section: "3"
letter: "q"
url: "/docs/linux/man/3-qldefines/"
---

ql/qldefines.hpp - Global definitions and compiler switches. 

<h2>Synopsis</h2>

<pre><code>#define BOOST_ENABLE_ASSERT_HANDLER



#define QL_INTEGER   int



#define QL_BIG_INTEGER   long



#define QL_REAL   double



#define QL_VERSION   '0.9.7'


version string


#define QL_HEX_VERSION   0x000907f0


version hexadecimal number


#define QL_LIB_VERSION   '0_9_7'


version string for output lib name


#define QL_MIN_INTEGER   ((std::numeric_limits&lt;QL_INTEGER&gt;::min)())



#define QL_MAX_INTEGER   ((std::numeric_limits&lt;QL_INTEGER&gt;::max)())



#define QL_MIN_REAL   -((std::numeric_limits&lt;QL_REAL&gt;::max)())



#define QL_MAX_REAL   ((std::numeric_limits&lt;QL_REAL&gt;::max)())



#define QL_MIN_POSITIVE_REAL   ((std::numeric_limits&lt;QL_REAL&gt;::min)())



#define QL_EPSILON   ((std::numeric_limits&lt;QL_REAL&gt;::epsilon)())



#define QL_NULL_INTEGER   ((std::numeric_limits&lt;int&gt;::max)())



#define QL_NULL_REAL   ((std::numeric_limits&lt;float&gt;::max)())</code></pre>

<h3>Defines</h3>

<pre><code>#define BOOST_ENABLE_ASSERT_HANDLER



#define QL_INTEGER   int



#define QL_BIG_INTEGER   long



#define QL_REAL   double



#define QL_VERSION   '0.9.7'


version string


#define QL_HEX_VERSION   0x000907f0


version hexadecimal number


#define QL_LIB_VERSION   '0_9_7'


version string for output lib name


#define QL_MIN_INTEGER   ((std::numeric_limits&lt;QL_INTEGER&gt;::min)())



#define QL_MAX_INTEGER   ((std::numeric_limits&lt;QL_INTEGER&gt;::max)())



#define QL_MIN_REAL   -((std::numeric_limits&lt;QL_REAL&gt;::max)())



#define QL_MAX_REAL   ((std::numeric_limits&lt;QL_REAL&gt;::max)())



#define QL_MIN_POSITIVE_REAL   ((std::numeric_limits&lt;QL_REAL&gt;::min)())



#define QL_EPSILON   ((std::numeric_limits&lt;QL_REAL&gt;::epsilon)())



#define QL_NULL_INTEGER   ((std::numeric_limits&lt;int&gt;::max)())



#define QL_NULL_REAL   ((std::numeric_limits&lt;float&gt;::max)())</code></pre>

<h2>Detailed Description</h2>

Global definitions and compiler switches.

<h2>Author</h2>

Generated automatically by Doxygen for QuantLib from the source code.
