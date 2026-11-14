---
title: "stdoverflow_error(3)"
name: "stdoverflow_error"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdoverflow_error/"
description: "std::overflow_error – std::overflow_error"
---

<p>std::overflow_error &#8211; std::overflow_error</p>
<h2>Synopsis</h2>
<pre><code>Defined in header &lt;stdexcept&gt;

class overflow_error;</code></pre>
<p>Defines a type of object to be thrown as exception. It can be used to report arithmetic overflow errors (that is, situations where a result of a computation is too large for the destination type)<br />
The only standard library components that throw this exception are std::bitset::to_ulong and std::bitset::to_ullong.<br />
The mathematical functions of the standard library components do not throw this exception (mathematical functions report overflow errors as specified in math_errhandling). Third-party libraries, however, use this. For example, boost.math throws std::overflow_error if boost::math::policies::throw_on_error is enabled (the default setting).<br />
&nbsp;std-overflow error-inheritance.svg<br />
Inheritance diagram </p>
<h2>Member functions</h2>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;constructs the exception object<br />
constructor <i>(public member function)</i> </p>
<p>&nbsp;std::overflow_error::overflow_error </p>
<p>explicit overflow_error( const std::string&amp; what_arg ); <code>(1)</code><br />
explicit overflow_error( const char* what_arg ); <code>(2)</code> <i>(since C++11)</i> </p>
<p>Constructs the exception object with what_arg as explanatory string that can be accessed through what().<br />
Because copying std::overflow_error is not permitted to throw exceptions, this message is typically stored internally as a separately-allocated reference-counted string. This is also why there is no constructor taking std::string&amp;&amp;: it would have to copy the content anyway.</p>
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
