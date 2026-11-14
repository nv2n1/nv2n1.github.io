---
title: "stdto_address(3)"
name: "stdto_address"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdto_address/"
description: "std::to_address – std::to_address"
---

<p>std::to_address &#8211; std::to_address</p>
<h2>Synopsis</h2>
<pre><code>Defined in header&lt;memory&gt;

    template &lt;class Ptr&gt;
    (1)(since C++ 20)

        auto to_address(const Ptr &amp;p) noexcept;

template &lt;class T&gt;
(2)(since C++ 20)

    constexpr T *to_address(T *p) noexcept;</code></pre>
<p>Obtain the address represented by p without forming a reference to the pointee.<br />
1) Fancy pointer overload: If the expression std::pointer_traits&lt;Ptr&gt;::to_address(p) is well-formed, returns the result of that expression. Otherwise, returns std::to_address(p.operator-&gt;()).<br />
2) Raw pointer overload: If T is a function type, the program is ill-formed. Otherwise, returns p unmodified. </p>
<h2>Parameters</h2>
<p>p &#8211; fancy or raw pointer</p>
<h2>Return value</h2>
<p>Raw pointer that represents the same address as p does. </p>
<h2>Possible implementation</h2>
<p>&nbsp;<wbr>&nbsp;template&lt;class&gt;<br />
&nbsp;<wbr>&nbsp;struct use_address : std::false_type { }; </p>
<p>&nbsp;<wbr>&nbsp;template&lt;class T&gt;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;requires requires(const T&amp; p) { std::pointer_traits&lt;T&gt;::to_address(p); }<br />
&nbsp;<wbr>&nbsp;struct use_address&lt;T&gt; : std::true_type { }; </p>
<p>&nbsp;<wbr>&nbsp;template&lt;class T&gt;<br />
&nbsp;<wbr>&nbsp;constexpr T* to_address(T* p) noexcept<br />
&nbsp;<wbr>&nbsp;{<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;static_assert(!std::is_function_v&lt;T&gt;);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;return p;<br />
&nbsp;<wbr>&nbsp;} </p>
<p>&nbsp;<wbr>&nbsp;template&lt;class T&gt;<br />
&nbsp;<wbr>&nbsp;auto to_address(const T&amp; p) noexcept<br />
&nbsp;<wbr>&nbsp;{<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;if constexpr (use_address&lt;T&gt;::value) {<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;return std::pointer_traits&lt;T&gt;::to_address(p);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;} else {<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;return std::to_address(p.operator-&gt;());<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;}<br />
&nbsp;<wbr>&nbsp;}</p>
<h2>Notes</h2>
<p>std::to_address can be used even when p does not reference storage that has an object constructed in it, in which case std::addressof(*p) cannot be used because there&#8217;s no valid object for the parameter of std::addressof to bind to. </p>
<h2>Example</h2>
<p>// Run this code </p>
<pre><code>#include &lt;memory&gt;
template &lt;class A&gt;

auto allocator_new(A &amp;a)

{
    auto p = a.allocate(1);
    try {
        std::allocator_traits&lt;A&gt;::construct(a, std::to_address(p));
    } catch (...) {
        a.deallocate(p, 1);
        throw;
    }
    return p;
}
template &lt;class A&gt;

void allocator_delete(A &amp;a, typename std::allocator_traits&lt;A&gt;::pointer p)

{
    std::allocator_traits&lt;A&gt;::destroy(a, std::to_address(p));
    a.deallocate(p, 1);
}
int main()

{
    std::allocator&lt;int&gt; a;
    auto p = allocator_new(a);
    allocator_delete(a, p);
}
</code></pre>
<h2>See also</h2>
<p>pointer_traits provides information about pointer-like types<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(class template)</i><br />
<i>(C++11)</i><br />
to_address obtains a raw pointer from a fancy pointer (inverse of pointer_to)<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(public static member function of std::pointer_traits&lt;Ptr&gt;)</i><br />
<code>[static]</code> (C++20) </p>
