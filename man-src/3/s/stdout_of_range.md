---
title: "stdout_of_range(3)"
name: "stdout_of_range"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdout_of_range/"
description: "std::out_of_range – std::out_of_range"
---

<p>std::out_of_range &#8211; std::out_of_range</p>
<h2>Synopsis</h2>
<pre><code>Defined in header &lt;stdexcept&gt;

class out_of_range;</code></pre>
<p>Defines a type of object to be thrown as exception. It reports errors that are consequence of attempt to access elements out of defined range.<br />
It may be thrown by the member functions of std::bitset and std::basic_string, by std::stoi and std::stod families of functions, and by the bounds-checked member access functions (e.g. std::vector::at and std::map::at)<br />
&nbsp;std-out of range-inheritance.svg<br />
Inheritance diagram </p>
<h2>Member functions</h2>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;constructs the exception object<br />
constructor <i>(public member function)</i> </p>
<p>&nbsp;std::out_of_range::out_of_range </p>
<p>explicit out_of_range( const std::string&amp; what_arg ); <code>(1)</code><br />
explicit out_of_range( const char* what_arg ); <code>(2)</code> <i>(since C++11)</i> </p>
<p>Constructs the exception object with what_arg as explanatory string that can be accessed through what().<br />
Because copying std::out_of_range is not permitted to throw exceptions, this message is typically stored internally as a separately-allocated reference-counted string. This is also why there is no constructor taking std::string&amp;&amp;: it would have to copy the content anyway.</p>
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
<h2>Notes</h2>
<p>The standard error condition std::errc::result_out_of_range typically indicates the condition where the result, rather than the input, is out of range, and is more closely related to std::range_error and ERANGE. </p>
<h2>See also</h2>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;accesses the specified character with bounds checking<br />
at <i>(public member function of std::basic_string&lt;CharT,Traits,Allocator&gt;)</i> </p>
