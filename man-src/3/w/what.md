---
title: "what(3)"
name: "what"
section: "3"
letter: "w"
url: "/docs/linux/man/3-what/"
description: "QuantLib::Error – Base error class."
---

<p>QuantLib::Error &#8211; Base error class. </p>
<h2>Synopsis</h2>
<pre><code>
#include &lt;ql/errors.hpp&gt;</code></pre>
<p> Inherits std::exception.</p>
<h3>Public Member Functions</h3>
<p><code>Error</code> (const std::string &amp;file, long line, const std::string &amp;functionName, const std::string &amp;message=&#8221;) </p>
<p> <code>~Error</code> () throw () </p>
<p> const char * <code>what</code> () const throw ()<br />
 <i>returns the error message. </i></p>
<h2>Detailed Description</h2>
<p>Base error class.</p>
<h2>Constructor &amp; Destructor Documentation</h2>
<h3><code>Error</code> (const std::string &amp; file, long line, const std::string &amp; functionName, const std::string &amp; message = &#8221;)</h3>
<p>The explicit use of this constructor is not advised. Use the QL_FAIL macro instead.</p>
<h3>~<code>Error</code> () throw ()</h3>
<p>the automatically generated destructor would not have the throw specifier.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
