---
title: "stddomain_error(3)"
name: "stddomain_error"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stddomain_error/"
description: "std::domain_error – std::domain_error"
---

<p>std::domain_error &#8211; std::domain_error</p>
<h2>Synopsis</h2>
<pre><code>Defined in header &lt;stdexcept&gt;

class domain_error;</code></pre>
<p>Defines a type of object to be thrown as exception. It may be used by the implementation to report domain errors, that is, situations where the inputs are outside of the domain on which an operation is defined.<br />
The standard library components do not throw this exception (mathematical functions report domain errors as specified in math_errhandling). Third-party libraries, however, use this. For example, boost.math throws std::domain_error if boost::math::policies::throw_on_error is enabled (the default setting).<br />
&nbsp;std-domain error-inheritance.svg<br />
Inheritance diagram </p>
<h2>Member functions</h2>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;constructs the exception object<br />
constructor <i>(public member function)</i> </p>
<p>&nbsp;std::domain_error::domain_error </p>
<p>explicit domain_error( const std::string&amp; what_arg ); <code>(1)</code><br />
explicit domain_error( const char* what_arg ); <code>(2)</code> <i>(since C++11)</i> </p>
<p>Constructs the exception object with what_arg as explanatory string that can be accessed through what().<br />
Because copying std::domain_error is not permitted to throw exceptions, this message is typically stored internally as a separately-allocated reference-counted string. This is also why there is no constructor taking std::string&amp;&amp;: it would have to copy the content anyway.</p>
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
