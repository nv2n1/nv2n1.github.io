---
title: "stdshared_futureget(3)"
name: "stdshared_futureget"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdshared_futureget/"
---

std::shared_future&lt;T&gt;::get - std::shared_future&lt;T&gt;::get

<h2>Synopsis</h2>

<pre><code>const T &amp;get() const;
(1)(member only of generic shared_future template)(since C++ 11)

    T &amp;get() const;
(2)(member only of shared_future&lt;T &amp;&gt; template specialization)(since C++ 11)

    void get() const;
(3)(member only of shared_future&lt;void&gt; template specialization)(since C++ 11)</code></pre> 
The get method waits until the shared_future has a valid result and (depending on which template is used) retrieves it. It effectively calls wait() in order to wait for the result. 
The generic template and two template specializations each contain a single version of get. The three versions of get differ only in the return type. 
The behavior is undefined if valid() is false before the call to this function. 

<h2>Parameters</h2>

<i>(none)</i>

<h2>Return value</h2>

1) Const reference to the value stored in the shared state. Accessing the value through this reference is undefined after the shared state has been destroyed. 
2) The reference stored as value in the shared state. 
3) Nothing. 

<h2>Exceptions</h2>

If an exception was stored in the shared state referenced by the future (e.g. via a call to std::promise::set_exception()) then that exception will be thrown.

<h2>Notes</h2>

The implementations are encouraged to detect the case when valid() is false before the call and throw a std::future_error with an error condition of std::future_errc::no_state. 

<h2>Example</h2>

&nbsp;This section is incomplete 
&nbsp;Reason: no example 

<h2>See also</h2>

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;checks if the future has a shared state 
valid <i>(public member function)</i> 
