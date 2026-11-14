---
title: "log4cppstringutil(3)"
name: "log4cppstringutil"
section: "3"
letter: "l"
url: "/docs/linux/man/3-log4cppstringutil/"
description: "log4cpp::StringUtil –"
---

<p>log4cpp::StringUtil &#8211; </p>
<h2>Synopsis</h2>
<p>#include &lt;StringUtil.hh&gt;</p>
<h3>Static Public Member Functions</h3>
<p>static std::string <code>vform</code> (const char *format, va_list args)<br />
 <i>Returns a string contructed from the a format specifier and a va_list of arguments, analogously to <a href="/docs/linux/man/3-vprintf/">vprintf</a>(3). </i><br />
 static std::string <code>trim</code> (const std::string &amp;s)<br />
 <i>Returns a string identical to the given string but without leading or trailing HTABs or spaces. </i><br />
 static unsigned int <code>split</code> (std::vector&lt; std::string &gt; &amp;v, const std::string &amp;s, char delimiter, unsigned int maxSegments=INT_MAX)<br />
 <i>splits a string into a vector of string segments based on the given delimiter. </i><br />
 template&lt;typename T &gt; static unsigned int <code>split</code> (T &amp;output, const std::string &amp;s, char delimiter, unsigned int maxSegments=INT_MAX)<br />
 <i>splits a string into string segments based on the given delimiter and assigns the segments through an output_iterator. </i></p>
<h2>Member Function Documentation</h2>
<h3>unsigned int log4cpp::StringUtil::split (std::vector&lt; std::string &gt; &amp;v, const std::string &amp;s, chardelimiter, unsigned intmaxSegments = INT_MAX) [static]</h3>
<p>splits a string into a vector of string segments based on the given delimiter. </p>
<pre>@param v The vector in which the segments will be stored. The vector
will be emptied before storing the segments
@param s The string to split into segments.
@param delimiter The delimiter character
@param maxSegments the maximum number of segments. Upon return
v.size() &lt;= maxSegments. The string is scanned from left to right
so v[maxSegments - 1] may contain a string containing the delimiter
character.</pre>
<p>&nbsp;<wbr> </p>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>The actual number of segments (limited by maxSegments).</dl>
<h3>template&lt;typename T &gt; static unsigned int log4cpp::StringUtil::split (T &amp;output, const std::string &amp;s, chardelimiter, unsigned intmaxSegments = INT_MAX) [inline], [static]</h3>
<p>splits a string into string segments based on the given delimiter and assigns the segments through an output_iterator. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>output</i> The output_iterator through which to assign the string segments. Typically this will be a back_insertion_iterator.<br />
 <i>s</i> The string to split into segments.<br />
 <i>delimiter</i> The delimiter character<br />
 <i>maxSegments</i> The maximum number of segments.</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>The actual number of segments (limited by maxSegments).</dl>
<h3>std::string log4cpp::StringUtil::trim (const std::string &amp;s) [static]</h3>
<p>Returns a string identical to the given string but without leading or trailing HTABs or spaces.</p>
<h3>std::string log4cpp::StringUtil::vform (const char *format, va_listargs) [static]</h3>
<p>Returns a string contructed from the a format specifier and a va_list of arguments, analogously to <a href="/docs/linux/man/3-vprintf/">vprintf</a>(3). </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>format</i> the format specifier.<br />
 <i>args</i> the va_list of arguments.</dl>
<h2>Author</h2>
<p>Generated automatically by Doxygen for log4cpp from the source code.</p>
