---
title: "log4cppcategorystream(3)"
name: "log4cppcategorystream"
section: "3"
letter: "l"
url: "/docs/linux/man/3-log4cppcategorystream/"
description: "log4cpp::CategoryStream –"
---

<p>log4cpp::CategoryStream &#8211; </p>
<p> This class enables streaming simple types and objects to a category.</p>
<h2>Synopsis</h2>
<p>#include &lt;CategoryStream.hh&gt;</p>
<h3>Public Types</h3>
<p>typedef <code>CategoryStream</code> &amp;(* <code>cspf</code> )(<code>CategoryStream</code> &amp;) </p>
<h3>Public Member Functions</h3>
<p><code>CategoryStream</code> (<code>Category</code> &amp;category, <code>Priority::Value</code> priority)<br />
 <i>Construct a </i><code>CategoryStream</code> for given <code>Category</code> with given priority.<br />
 <code>~CategoryStream</code> ()<br />
 <i>Destructor for </i><code>CategoryStream</code>.<br />
 <code>Category</code> &amp; <code>getCategory</code> () const<br />
 <i>Returns the destination </i><code>Category</code> for this stream.<br />
 <code>Priority::Value</code> <code>getPriority</code> () const throw ()<br />
 <i>Returns the priority for this stream. </i><br />
 void <code>flush</code> ()<br />
 <i>Flush the contents of the stream buffer to the </i><code>Category</code> and empties the buffer.<br />
 template&lt;typename T &gt; <code>CategoryStream</code> &amp; <code>operator&lt;&lt;</code> (const T &amp;t)<br />
 <i>Stream in arbitrary types and objects. </i><br />
 <code>CategoryStream</code> &amp; <code>operator&lt;&lt;</code> (const char *t) </p>
<p> template&lt;typename T &gt; <code>CategoryStream</code> &amp; <code>operator&lt;&lt;</code> (const std::string &amp;t) </p>
<p> std::streamsize <code>width</code> (std::streamsize wide)<br />
 <i>Set the width output on </i><code>CategoryStream</code>.<br />
 <code>CategoryStream</code> &amp; <code>operator&lt;&lt;</code> (<code>cspf</code>) </p>
<h3>Friends</h3>
<p><code>LOG4CPP_EXPORT</code> friend<br />
 <code>CategoryStream</code> &amp; <code>eol</code> (<code>CategoryStream</code> &amp;os)&quot;<br />
 <i>eol manipulator </i><br />
 <code>LOG4CPP_EXPORT</code> friend<br />
 <code>CategoryStream</code> &amp; <code>left</code> (<code>CategoryStream</code> &amp;os)&quot;<br />
 <i>left manipulator </i></p>
<h2>Detailed Description</h2>
<p>This class enables streaming simple types and objects to a category. </p>
<p> Use category.errorStream(), etc. to obtain a <code>CategoryStream</code> class.</p>
<h2>Member Typedef Documentation</h2>
<h3>typedef <code>CategoryStream</code>&amp;(* log4cpp::CategoryStream::cspf)(<code>CategoryStream</code> &amp;)</h3>
<h2>Constructor &amp; Destructor Documentation</h2>
<h3>log4cpp::CategoryStream::CategoryStream (<code>Category</code> &amp;category, <code>Priority::Value</code>priority)</h3>
<p>Construct a <code>CategoryStream</code> for given <code>Category</code> with given priority. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>category</i> The category this stream will send log messages to.<br />
 <i>priority</i> The priority the log messages will get or <code>Priority::NOTSET</code> to silently discard any streamed in messages.</dl>
<h3>log4cpp::CategoryStream::~CategoryStream ()</h3>
<p>Destructor for <code>CategoryStream</code>.</p>
<h2>Member Function Documentation</h2>
<h3>void log4cpp::CategoryStream::flush ()</h3>
<p>Flush the contents of the stream buffer to the <code>Category</code> and empties the buffer.</p>
<h3><code>Category</code>&amp; log4cpp::CategoryStream::getCategory () const [inline]</h3>
<p>Returns the destination <code>Category</code> for this stream. </p>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>The <code>Category</code>.</dl>
<h3><code>Priority::Value</code> log4cpp::CategoryStream::getPriority () const [inline]</h3>
<p>Returns the priority for this stream. </p>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>The priority.</dl>
<h3>template&lt;typename T &gt; <code>CategoryStream</code>&amp; log4cpp::CategoryStream::operator&lt;&lt; (const T &amp;t) [inline]</h3>
<p>Stream in arbitrary types and objects. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>t</i> The value or object to stream in.</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>A reference to itself.</dl>
<h3><code>CategoryStream</code> &amp; log4cpp::CategoryStream::operator&lt;&lt; (const char *t)</h3>
<h3>template&lt;typename T &gt; <code>CategoryStream</code>&amp; log4cpp::CategoryStream::operator&lt;&lt; (const std::string &amp;t) [inline]</h3>
<h3><code>CategoryStream</code> &amp; log4cpp::CategoryStream::operator&lt;&lt; (<code>cspf</code>pf)</h3>
<h3>std::streamsize log4cpp::CategoryStream::width (std::streamsizewide)</h3>
<p>Set the width output on <code>CategoryStream</code>.</p>
<h2>Friends And Related Function Documentation</h2>
<h3><code>LOG4CPP_EXPORT</code> friend <code>CategoryStream</code>&amp; eol (<code>CategoryStream</code> &amp;os) [friend]</h3>
<p>eol manipulator</p>
<h3><code>LOG4CPP_EXPORT</code> friend <code>CategoryStream</code>&amp; left (<code>CategoryStream</code> &amp;os) [friend]</h3>
<p>left manipulator</p>
<h2>Member Data Documentation</h2>
<h3><code>std::ostringstream</code>* log4cpp::CategoryStream::_buffer</h3>
<h2>Author</h2>
<p>Generated automatically by Doxygen for log4cpp from the source code.</p>
