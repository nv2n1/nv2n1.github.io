---
title: "stdvectorreference(3)"
name: "stdvectorreference"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdvectorreference/"
description: "std::vector<bool>::reference – std::vector<bool>::reference"
---

<p>std::vector&lt;bool&gt;::reference &#8211; std::vector&lt;bool&gt;::reference</p>
<h2>Synopsis</h2>
<pre><code>class reference;</code></pre>
<p>The std::vector&lt;bool&gt; specialization defines std::vector&lt;bool&gt;::reference as a publicly-accessible nested class. std::vector&lt;bool&gt;::reference proxies the behavior of references to a single bit in std::vector&lt;bool&gt;.<br />
The primary use of std::vector&lt;bool&gt;::reference is to provide an l-value that can be returned from operator[].<br />
Any reads or writes to a vector that happen via a std::vector&lt;bool&gt;::reference potentially read or write to the entire underlying vector. </p>
<h2>Member functions</h2>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;constructs the reference. Accessible only to std::vector&lt;bool&gt; itself<br />
constructor <i>(public member function)</i><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;destroys the reference<br />
destructor <i>(public member function)</i><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;assigns a bool to the referenced bit<br />
operator= <i>(public member function)</i><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;returns the referenced bit<br />
operator bool <i>(public member function)</i><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;flips the referenced bit<br />
flip <i>(public member function)</i> </p>
<p>&nbsp;std::vector&lt;bool&gt;::reference::~reference </p>
<p>~reference() </p>
<p>Destroys the reference. </p>
<p>&nbsp;std::vector&lt;bool&gt;::reference::operator= </p>
<p>reference&amp; operator=( bool x ); <i>(until C++11)</i><br />
reference&amp; operator=( const reference&amp; x );<br />
reference&amp; operator=( bool x ) noexcept; <i>(since C++11)</i><br />
reference&amp; operator=( const reference&amp; x ) noexcept; </p>
<p>Assigns a value to the referenced bit.</p>
<h2>Parameters</h2>
<p>x &#8211; value to assign</p>
<h2>Return value</h2>
<p>*this<br />
&nbsp;std::vector&lt;bool&gt;::reference::operator bool<br />
operator bool() const; <i>(until C++11)</i><br />
operator bool() const noexcept; <i>(since C++11)</i><br />
Returns the value of the referenced bit. </p>
<h2>Parameters</h2>
<p><i>(none)</i></p>
<h2>Return value</h2>
<p>The referenced bit.<br />
&nbsp;std::vector&lt;bool&gt;::reference::flip </p>
<pre><code>void flip();
(until C++ 11)

    void flip() noexcept;
(since C++ 11)</code></pre>
<p>Inverts the referenced bit. </p>
<h2>Parameters</h2>
<p><i>(none)</i></p>
<h2>Return value</h2>
<p><i>(none)</i> </p>
<h2>See also</h2>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;access specified element<br />
operator[] <i>(public member function of std::vector&lt;T,Allocator&gt;)</i><br />
swap swaps two std::vector&lt;bool&gt;::references<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(public static member function)</i><br />
<code>[static]</code> </p>
