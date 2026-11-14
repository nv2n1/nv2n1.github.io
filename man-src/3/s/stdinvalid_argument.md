---
title: "stdinvalid_argument(3)"
name: "stdinvalid_argument"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdinvalid_argument/"
description: "std::invalid_argument – std::invalid_argument"
---

<p>std::invalid_argument &#8211; std::invalid_argument</p>
<h2>Synopsis</h2>
<pre><code>Defined in header &lt;stdexcept&gt;

class invalid_argument;</code></pre>
<p>Defines a type of object to be thrown as exception. It reports errors that arise because an argument value has not been accepted.<br />
This exception is thrown by std::bitset::bitset, and the std::stoi and std::stof families of functions.<br />
&nbsp;std-invalid argument-inheritance.svg<br />
Inheritance diagram </p>
<h2>Member functions</h2>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;constructs the exception object<br />
constructor <i>(public member function)</i> </p>
<p>&nbsp;std::invalid_argument::invalid_argument </p>
<p>explicit invalid_argument( const std::string&amp; what_arg ); <code>(1)</code><br />
explicit invalid_argument( const char* what_arg ); <code>(2)</code> <i>(since C++11)</i> </p>
<p>Constructs the exception object with what_arg as explanatory string that can be accessed through what().<br />
Because copying std::invalid_argument is not permitted to throw exceptions, this message is typically stored internally as a separately-allocated reference-counted string. This is also why there is no constructor taking std::string&amp;&amp;: it would have to copy the content anyway.</p>
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
<p>The purpose of this exception type is similar to the error condition std::errc::invalid_argument (thrown in std::system_error from member functions of std::thread) and the related errno constant EINVAL. </p>
