---
title: "stdmake_exception_ptr(3)"
name: "stdmake_exception_ptr"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdmake_exception_ptr/"
---

std::make_exception_ptr - std::make_exception_ptr

<h2>Synopsis</h2>

<pre><code>Defined in header &lt;exception&gt;

template&lt; class E &gt;                                     (since C++11)

std::exception_ptr make_exception_ptr( E e ) noexcept;</code></pre> 
Creates an std::exception_ptr that holds a reference to a copy of e. This is done as if executing the following code: <pre><code>try {
    throw e;

} catch (...) {
    return std::current_exception();
}
</code></pre>

<h2>Parameters</h2>

<i>(none)</i>

<h2>Return value</h2>

An instance of std::exception_ptr holding a reference to the copy of e, or to an instance of std::bad_alloc or to an instance of std::bad_exception (see std::current_exception). 

<h2>Notes</h2>

The parameter is passed by value and is subject to slicing. 

<h2>See also</h2>

current_exception captures the current exception in a std::exception_ptr 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function)</i> 
<i>(C++11)</i> 
