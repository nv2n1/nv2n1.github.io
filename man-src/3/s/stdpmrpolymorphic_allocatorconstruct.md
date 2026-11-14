---
title: "stdpmrpolymorphic_allocatorconstruct(3)"
name: "stdpmrpolymorphic_allocatorconstruct"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdpmrpolymorphic_allocatorconstruct/"
description: "std::pmr::polymorphic_allocator<T>::construct – std::pmr::polymorphic_allocator<T>::construct"
---

<p>std::pmr::polymorphic_allocator&lt;T&gt;::construct &#8211; std::pmr::polymorphic_allocator&lt;T&gt;::construct</p>
<h2>Synopsis</h2>
<p>template &lt; class U, class&#8230; Args &gt; <code>(1)</code> <i>(since C++17)</i><br />
void construct( U* p, Args&amp;&amp;&#8230; args );<br />
template&lt; class T1, class T2, class&#8230; Args1, class&#8230; Args2 &gt;<br />
void construct( std::pair&lt;T1, T2&gt;* p, <i>(since C++17)</i><br />
std::piecewise_construct_t, <code>(2)</code> <i>(until C++20)</i><br />
std::tuple&lt;Args1&#8230;&gt; x,<br />
std::tuple&lt;Args2&#8230;&gt; y );<br />
template&lt; class T1, class T2 &gt; <code>(3)</code> <i>(since C++17)</i><br />
void construct( std::pair&lt;T1, T2&gt;* p ); <i>(until C++20)</i><br />
template&lt; class T1, class T2, class U, class V &gt; <code>(4)</code> <i>(since C++17)</i><br />
void construct( std::pair&lt;T1, T2&gt;* p, U&amp;&amp; x, V&amp;&amp; y ); <i>(until C++20)</i><br />
template&lt; class T1, class T2, class U, class V &gt; <code>(5)</code> <i>(since C++17)</i><br />
void construct( std::pair&lt;T1, T2&gt;* p, const std::pair&lt;U, V&gt;&amp; xy ); <i>(until C++20)</i><br />
template&lt; class T1, class T2, class U, class V &gt; <code>(6)</code> <i>(since C++17)</i><br />
void construct( std::pair&lt;T1, T2&gt;* p, std::pair&lt;U, V&gt;&amp;&amp; xy ); <i>(until C++20)</i><br />
Constructs an object in allocated, but not initialized storage pointed to by p the provided constructor arguments. If the object is of type that itself uses allocators, or if it is std::pair, passes this-&gt;resource() down to the constructed object.<br />
1) Creates an object of the given type U by means of uses-allocator_construction at the uninitialized memory location indicated by p, using *this as the allocator.<br />
This overload only participates in overload resolution if U is not a specialization of std::pair.<br />
<i>(until C++20)</i><br />
2) First, if either T1 or T2 is allocator-aware, modifies the tuples x and y to include this-&gt;resource(), resulting in the two new tuples xprime and yprime, according to the following three rules:<br />
2a) if T1 is not allocator-aware (std::uses_allocator&lt;T1, polymorphic_allocator&gt;::value==false) and std::is_constructible&lt;T1, Args1&#8230;&gt;::value==true, then xprime is x, unmodified.<br />
2b) if T1 is allocator-aware (std::uses_allocator&lt;T1, polymorphic_allocator&gt;::value==true), and its constructor takes an allocator tag (std::is_constructible&lt;T1, std::allocator_arg_t, polymorphic_allocator, Args1&#8230;&gt;::value==true, then xprime is std::tuple_cat(std::make_tuple(std::allocator_arg, *this), std::move(x))<br />
2c) if T1 is allocator-aware (std::uses_allocator&lt;T1, polymorphic_allocator&gt;::value==true), and its constructor takes the allocator as the last argument (std::is_constructible&lt;T1, Args1&#8230;, polymorphic_allocator&gt;::value==true), then xprime is std::tuple_cat(std::move(x), std::make_tuple(*this)).<br />
2d) Otherwise, the program is ill-formed.<br />
Same rules apply to T2 and the replacement of y with yprime.<br />
Once xprime and yprime are constructed, constructs the pair p in allocated storage as if by ::new((void *) p) pair&lt;T1, T2&gt;(std::piecewise_construct, std::move(xprime), std::move(yprime));<br />
3) Equivalent to construct(p, std::piecewise_construct, std::tuple&lt;&gt;(), std::tuple&lt;&gt;()), that is, passes the memory resource on to the pair&#8217;s member types if they accept them.<br />
4) Equivalent to<br />
&nbsp;<wbr>&nbsp;construct(p, std::piecewise_construct, std::forward_as_tuple(std::forward&lt;U&gt;(x)),<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;std::forward_as_tuple(std::forward&lt;V&gt;(y))) <i>(until C++20)</i><br />
5) Equivalent to<br />
&nbsp;<wbr>&nbsp;construct(p, std::piecewise_construct, std::forward_as_tuple(xy.first),<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;std::forward_as_tuple(xy.second))<br />
6) Equivalent to<br />
&nbsp;<wbr>&nbsp;construct(p, std::piecewise_construct, std::forward_as_tuple(std::forward&lt;U&gt;(xy.first)),<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;std::forward_as_tuple(std::forward&lt;V&gt;(xy.second))) </p>
<h2>Parameters</h2>
<p>p &#8211; pointer to allocated, but not initialized storage<br />
args&#8230; &#8211; the constructor arguments to pass to the constructor of T<br />
x &#8211; the constructor arguments to pass to the constructor of T1<br />
y &#8211; the constructor arguments to pass to the constructor of T2<br />
xy &#8211; the pair whose two members are the constructor arguments for T1 and T2</p>
<h2>Return value</h2>
<p><i>(none)</i> </p>
<h2>Notes</h2>
<p>This function is called (through std::allocator_traits) by any allocator-aware object, such as std::pmr::vector (or another std::vector that was given a std::std::polymorphic_allocator as the allocator to use).<br />
Defect reports<br />
The following behavior-changing defect reports were applied retroactively to previously published C++ standards.<br />
DR Applied to Behavior as published Correct behavior<br />
LWG_2969 C++17 uses-allocator construction passed resource() passes *this<br />
LWG_2975 C++17 first overload is mistakenly used for pair construction in some cases constrained to not accept pairs </p>
<h2>See also</h2>
<p>construct constructs an object in the allocated storage<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function template)</i><br />
<code>[static]</code><br />
construct constructs an object in allocated storage<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(public member function of std::allocator&lt;T&gt;)</i><br />
(deprecated in C++17)<br />
(removed in C++20) </p>
