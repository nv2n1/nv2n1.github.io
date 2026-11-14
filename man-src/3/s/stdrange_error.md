---
title: "stdrange_error(3)"
name: "stdrange_error"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdrange_error/"
description: "std::range_error – std::range_error"
---

<p>std::range_error &#8211; std::range_error</p>
<h2>Synopsis</h2>
<pre><code>Defined in header &lt;stdexcept&gt;

class range_error;</code></pre>
<p>Defines a type of object to be thrown as exception. It can be used to report range errors (that is, situations where a result of a computation cannot be represented by the destination type)<br />
The only standard library components that throw this exception are std::wstring_convert::from_bytes and std::wstring_convert::to_bytes.<br />
The mathematical functions in the standard library components do not throw this exception (mathematical functions report range errors as specified in math_errhandling).<br />
&nbsp;std-range error-inheritance.svg<br />
Inheritance diagram </p>
<h2>Member functions</h2>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;constructs the exception object<br />
constructor <i>(public member function)</i> </p>
<p>&nbsp;std::range_error::range_error </p>
<p>explicit range_error( const std::string&amp; what_arg ); <code>(1)</code><br />
explicit range_error( const char* what_arg ); <code>(2)</code> <i>(since C++11)</i> </p>
<p>Constructs the exception object with what_arg as explanatory string that can be accessed through what().<br />
Because copying std::range_error is not permitted to throw exceptions, this message is typically stored internally as a separately-allocated reference-counted string. This is also why there is no constructor taking std::string&amp;&amp;: it would have to copy the content anyway.</p>
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
