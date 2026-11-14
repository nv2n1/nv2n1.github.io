---
title: "stdruntime_error(3)"
name: "stdruntime_error"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdruntime_error/"
description: "std::runtime_error – std::runtime_error"
---

<p>std::runtime_error &#8211; std::runtime_error</p>
<h2>Synopsis</h2>
<pre><code>Defined in header &lt;stdexcept&gt;

class runtime_error;</code></pre>
<p>Defines a type of object to be thrown as exception. It reports errors that are due to events beyond the scope of the program and can not be easily predicted.<br />
Exceptions of type std::runtime_error are thrown by the following standard library components: std::locale::locale and std::locale::combine.<br />
In addition, the standard exception types std::range_error, std::overflow_error, std::underflow_error, std::regex_error, and std::system_error are derived from std::runtime_error.<br />
&nbsp;std-runtime error-inheritance.svg<br />
Inheritance diagram </p>
<h2>Member functions</h2>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;constructs the exception object<br />
constructor <i>(public member function)</i> </p>
<p>&nbsp;std::runtime_error::runtime_error </p>
<p>explicit runtime_error( const std::string&amp; what_arg ); <code>(1)</code><br />
explicit runtime_error( const char* what_arg ); <code>(2)</code> <i>(since C++11)</i> </p>
<p>Constructs the exception object with what_arg as explanatory string that can be accessed through what().<br />
Because copying std::runtime_error is not permitted to throw exceptions, this message is typically stored internally as a separately-allocated reference-counted string. This is also why there is no constructor taking std::string&amp;&amp;: it would have to copy the content anyway.</p>
<h2>Parameters</h2>
<p>what_arg &#8211; explanatory string</p>
<h2>Exceptions</h2>
<p>May throw std::bad_alloc </p>
<p>Inherited from std::exception</p>
<h2>Member functions</h2>
<p>destructor destroys the exception object<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(virtual public member function of std::exception)</i><br />
<code>[virtual]</code> </p>
<p>what returns an explanatory string<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(virtual public member function of std::exception)</i><br />
<code>[virtual]</code></p>
