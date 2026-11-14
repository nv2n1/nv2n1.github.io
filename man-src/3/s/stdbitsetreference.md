---
title: "stdbitsetreference(3)"
name: "stdbitsetreference"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdbitsetreference/"
description: "std::bitset<N>::reference – std::bitset<N>::reference"
---

<p>std::bitset&lt;N&gt;::reference &#8211; std::bitset&lt;N&gt;::reference</p>
<h2>Synopsis</h2>
<pre><code>class reference;</code></pre>
<p>The std::bitset class includes std::bitset::reference as a publicly-accessible nested class. This class is used as a proxy object to allow users to interact with individual bits of a bitset, since standard C++ types (like references and pointers) are not built with enough precision to specify individual bits.<br />
The primary use of std::bitset::reference is to provide an l-value that can be returned from operator[].<br />
Any reads or writes to a bitset that happen via a std::bitset::reference potentially read or write to the entire underlying bitset. </p>
<h2>Member functions</h2>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;constructs the reference. Accessible only to std::bitset itself<br />
constructor (private member function)<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;destroys the reference<br />
destructor <i>(public member function)</i><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;assigns a bool to the referenced bit<br />
operator= <i>(public member function)</i><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;returns the referenced bit<br />
operator bool <i>(public member function)</i><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;returns inverted referenced bit<br />
operator~ <i>(public member function)</i><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;flips the referenced bit<br />
flip <i>(public member function)</i> </p>
<p>&nbsp;std::bitset&lt;N&gt;::reference::~reference </p>
<p>~reference(); </p>
<p>Destroys the reference. </p>
<p>&nbsp;std::bitset&lt;N&gt;::reference::operator= </p>
<p>reference&amp; operator=( bool x ); <i>(until C++11)</i><br />
reference&amp; operator=( bool x ) noexcept; <code>(1)</code> <i>(since C++11)</i><br />
reference&amp; operator=( const reference&amp; x ); <code>(2)</code> <i>(until C++11)</i><br />
reference&amp; operator=( const reference&amp; x ) noexcept; <i>(since C++11)</i> </p>
<p>Assigns a value to the referenced bit.</p>
<h2>Parameters</h2>
<p>x &#8211; value to assign</p>
<h2>Return value</h2>
<p>*this<br />
&nbsp;std::bitset&lt;N&gt;::reference::operator bool<br />
operator bool() const; <i>(until C++11)</i><br />
operator bool() const noexcept; <i>(since C++11)</i><br />
Returns the value of the referenced bit. </p>
<h2>Parameters</h2>
<p><i>(none)</i></p>
<h2>Return value</h2>
<p>The referenced bit.<br />
&nbsp;std::bitset&lt;N&gt;::reference::operator~<br />
bool operator~() const; <i>(until C++11)</i><br />
bool operator~() const noexcept; <i>(since C++11)</i><br />
Returns the inverse of the referenced bit. </p>
<h2>Parameters</h2>
<p><i>(none)</i></p>
<h2>Return value</h2>
<p>The inverse of the referenced bit.<br />
&nbsp;std::bitset&lt;N&gt;::reference::flip<br />
reference&amp; flip(); <i>(until C++11)</i><br />
reference&amp; flip() noexcept; <i>(since C++11)</i><br />
Inverts the referenced bit. </p>
<h2>Parameters</h2>
<p><i>(none)</i></p>
<h2>Return value</h2>
<p>*this </p>
<h2>See also</h2>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;accesses specific bit<br />
operator[] <i>(public member function)</i> </p>
