---
title: "stdweak_ptroperator(3)"
name: "stdweak_ptroperator"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdweak_ptroperator/"
---

std::weak_ptr&lt;T&gt;::operator= - std::weak_ptr&lt;T&gt;::operator=

<h2>Synopsis</h2>

<pre><code>weak_ptr &amp;operator=(const weak_ptr &amp;r) noexcept;
(1)(since C++ 11)

    template &lt;class Y&gt;
    (2)(since C++ 11)

        weak_ptr &amp;
        operator=(const weak_ptr&lt;Y&gt; &amp;r) noexcept;

template &lt;class Y&gt;
(3)(since C++ 11)

    weak_ptr &amp;
    operator=(const shared_ptr&lt;Y&gt; &amp;r) noexcept;

weak_ptr &amp;operator=(weak_ptr &amp;&amp;r) noexcept;
(4)(since C++ 14)

    template &lt;class Y&gt;
    (5)(since C++ 14)

        weak_ptr &amp;
        operator=(weak_ptr&lt;Y&gt; &amp;&amp;r) noexcept;</code></pre> 
Replaces the managed object with the one managed by r. The object is shared with r. If r manages no object, *this manages no object too. 
1-3) Equivalent to std::weak_ptr&lt;T&gt;(r).swap(*this). 
4,5) Equivalent to std::weak_ptr&lt;T&gt;(std::move(r)).swap(*this). 

<h2>Parameters</h2>

r - smart pointer to share an object with

<h2>Return value</h2>

*this 

<h2>Notes</h2>

The implementation may meet the requirements without creating a temporary weak_ptr object. 

<h2>See also</h2>

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;creates a new weak_ptr 
constructor <i>(public member function)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;swaps the managed objects 
swap <i>(public member function)</i> 
