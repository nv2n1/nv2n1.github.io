---
title: "stdanyemplace(3)"
name: "stdanyemplace"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdanyemplace/"
---

std::any::emplace - std::any::emplace

<h2>Synopsis</h2>

<pre><code>template&lt; class ValueType, class... Args &gt;                                       (1) (since C++17)

std::decay_t&lt;ValueType&gt;&amp; emplace( Args&amp;&amp;... args );

template&lt; class ValueType, class U, class... Args &gt;                              (2) (since C++17)

std::decay_t&lt;ValueType&gt;&amp; emplace( std::initializer_list&lt;U&gt; il, Args&amp;&amp;... args );</code></pre> 
Changes the contained object to one of type std::decay_t&lt;ValueType&gt; constructed from the arguments. 
First destroys the current contained object (if any) by reset(), then: 
1) constructs an object of type std::decay_t&lt;ValueType&gt;, direct-non-list-initialized from std::forward&lt;Args&gt;(args)..., as the contained object. This overload only participates in overload resolution if std::is_constructible_v&lt;std::decay_t&lt;ValueType&gt;, Args...&gt; and std::is_copy_constructible_v&lt;std::decay_t&lt;ValueType&gt;&gt; are both true. 
2) constructs an object of type std::decay_t&lt;ValueType&gt;, direct-non-list-initialized from il, std::forward&lt;Args&gt;(args)..., as the contained object. This overload only participates in overload resolution if std::is_constructible_v&lt;std::decay_t&lt;ValueType&gt;, std::initializer_list&lt;U&gt;&amp;, Args...&gt; and std::is_copy_constructible_v&lt;std::decay_t&lt;ValueType&gt;&gt; are both true. 

<h2>Template parameters</h2>

ValueType - contained value type

<h2>Type requirements</h2>

- 
std::decay_t&lt;ValueType&gt; must meet the requirements of CopyConstructible.

<h2>Return value</h2>

A reference to the new contained object. 

<h2>Exceptions</h2>

Throws any exception thrown by T's constructor. If an exception is thrown, the previously contained object (if any) has been destroyed, and *this does not contain a value.

<h2>Example</h2>

&nbsp;This section is incomplete 
&nbsp;Reason: no example 

<h2>See also</h2>

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;constructs an any object 
constructor <i>(public member function)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;destroys contained object 
reset <i>(public member function)</i> 
