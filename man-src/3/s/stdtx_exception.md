---
title: "stdtx_exception(3)"
name: "stdtx_exception"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdtx_exception/"
description: "std::tx_exception – std::tx_exception"
---

<p>std::tx_exception &#8211; std::tx_exception</p>
<h2>Synopsis</h2>
<pre><code>Defined in header &lt;stdexcept&gt;

template&lt; class T &gt;                              (TM TS)

class tx_exception : public std::runtime_error;</code></pre>
<p>Defines an exception type that can be used to cancel and roll back an atomic transaction initiated by the keyword atomic_cancel<br />
If T is not TriviallyCopyable, the program that specializes std::tx_exception&lt;T&gt; is ill-formed. </p>
<h2>Member functions</h2>
<p>&nbsp;std::tx_exception::tx_exception </p>
<p>explicit tx_exception( T value ) transaction_safe; <code>(1)</code><br />
tx_exception( T value, const std::string&amp; what_arg ) transaction_safe; <code>(2)</code><br />
tx_exception( T value, const char* what_arg ) transaction_safe; <code>(3)</code> </p>
<p>Constructs the exception object with what_arg as explanatory string that can be accessed through what() and value as the object that can be accessed through get().</p>
<h2>Parameters</h2>
<p>value &#8211; payload object<br />
what_arg &#8211; explanatory string</p>
<h2>Exceptions</h2>
<p><i>(none)</i> </p>
<p>&nbsp;std::tx_exception::get </p>
<p>T get() const transaction_safe; </p>
<p>Returns the payload object object held by the exception object.</p>
<h2>Exceptions</h2>
<p><i>(none)</i> </p>
<p>Inherited from std::runtime_error </p>
<p>Inherited from std::exception</p>
<h2>Member functions</h2>
<p>destructor destroys the exception object<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(virtual public member function of std::exception)</i><br />
<code>[virtual]</code> </p>
<p>what returns an explanatory string<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(virtual public member function of std::exception)</i><br />
<code>[virtual]</code></p>
