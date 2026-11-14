---
title: "stdexperimentalpmrpolymorphic_allocatorconstruct(3)"
name: "stdexperimentalpmrpolymorphic_allocatorconstruct"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdexperimentalpmrpolymorphic_allocatorconstruct/"
description: "std::experimental::pmr::polymorphic_allocator<T>::construct – std::experimental::pmr::polymorphic_allocator<T>::construct"
---

<p>std::experimental::pmr::polymorphic_allocator&lt;T&gt;::construct &#8211; std::experimental::pmr::polymorphic_allocator&lt;T&gt;::construct</p>
<h2>Synopsis</h2>
<pre><code>template &lt;class U, class... Args&gt;
(1)(library fundamentals TS)

    void construct(U *p, Args &amp;&amp;...args);

template &lt;class T1, class T2, class... Args1, class... Args2&gt;

void construct(std::pair&lt;T1, T2&gt; *p,

               std::piecewise_construct_t, (2)(library fundamentals TS)

                                               std::tuple&lt;Args1...&gt;
                                                   x,

               std::tuple&lt;Args2...&gt; y);

template &lt;class T1, class T2&gt;
(3)(library fundamentals TS)

    void construct(std::pair&lt;T1, T2&gt; *p);

template &lt;class T1, class T2, class U, class V&gt;
(4)(library fundamentals TS)

    void construct(std::pair&lt;T1, T2&gt; *p, U &amp;&amp;x, V &amp;&amp;y);

template &lt;class T1, class T2, class U, class V&gt;
(5)(library fundamentals TS)

    void construct(std::pair&lt;T1, T2&gt; *p, const std::pair&lt;U, V&gt; &amp;xy);

template &lt;class T1, class T2, class U, class V&gt;
(6)(library fundamentals TS)

    void construct(std::pair&lt;T1, T2&gt; *p, std::pair&lt;U, V&gt; &amp;&amp;xy);</code></pre>
<p>Constructs an object in allocated, but not initialized storage pointed to by p the provided constructor arguments. If the object is of type that itself uses allocators, or if it is std::pair, passes this-&gt;resource() down to the constructed object.<br />
1) If std::uses_allocator&lt;U, memory_resource*&gt;::value==false (the type U does not use allocators) and std::is_constructible&lt;U, Args&#8230;&gt;::value==true, then constructs the object as if by ::new((void *) p) U(std::forward&lt;Args&gt;(args)&#8230; );.<br />
Otherwise, if std::uses_allocator&lt;U, memory_resource*&gt;::value==true (the type U uses allocators, e.g. it is a container) and std::is_constructible&lt;U, std::allocator_arg_t, memory_resource*, Args&#8230;&gt;::value==true, then constructs the object as if by ::new((void *) p) U(std::allocator_arg, this-&gt;resource(), std::forward&lt;Args&gt;(args)&#8230; );.<br />
Otherwise, if std::uses_allocator&lt;U, memory_resource*&gt;::value==true (the type U uses allocators, e.g. it is a container) and std::is_constructible&lt;U, Args&#8230;, memory_resource*&gt;::value==true, then constructs the object as if by ::new((void *) p) U(std::forward&lt;Args&gt;(args)&#8230;, this-&gt;resource());.<br />
Otherwise, the program is ill-formed.<br />
2) First, if either T1 or T2 is allocator-aware, modifies the tuples x and y to include this-&gt;resource(), resulting in the two new tuples xprime and yprime, according to the following three rules:<br />
2a) if T1 is not allocator-aware (std::uses_allocator&lt;T1, memory_resource*&gt;::value==false) and std::is_constructible&lt;T1, Args1&#8230;&gt;::value==true, then xprime is x, unmodified.<br />
2b) if T1 is allocator-aware (std::uses_allocator&lt;T1, memory_resource*&gt;::value==true), and its constructor takes an allocator tag (std::is_constructible&lt;T1, std::allocator_arg_t, memory_resource*, Args1&#8230;&gt;::value==true, then xprime is std::tuple_cat(std::make_tuple(std::allocator_arg, this-&gt;resource()), std::move(x))<br />
2c) if T1 is allocator-aware (std::uses_allocator&lt;T1, memory_resource*&gt;::value==true), and its constructor takes the allocator as the last argument (std::is_constructible&lt;T1, Args1&#8230;, memory_resource*&gt;::value==true), then xprime is std::tuple_cat(std::move(x), std::make_tuple(this-&gt;resource())).<br />
2d) Otherwise, the program is ill-formed.<br />
Same rules apply to T2 and the replacement of y with yprime.<br />
Once xprime and yprime are constructed, constructs the pair p in allocated storage as if by ::new((void *) p) pair&lt;T1, T2&gt;(std::piecewise_construct, std::move(xprime), std::move(yprime));<br />
3) Equivalent to construct(p, std::piecewise_construct, std::tuple&lt;&gt;(), std::tuple&lt;&gt;()), that is, passes the memory resource on to the pair&#8217;s member types if they accept them.<br />
4) Equivalent to<br />
construct(p, std::piecewise_construct, std::forward_as_tuple(std::forward&lt;U&gt;(x)),<br />
std::forward_as_tuple(std::forward&lt;V&gt;(y)))<br />
5) Equivalent to<br />
construct(p, std::piecewise_construct, std::forward_as_tuple(xy.first),<br />
std::forward_as_tuple(xy.second))<br />
6) Equivalent to<br />
construct(p, std::piecewise_construct, std::forward_as_tuple(std::forward&lt;U&gt;(xy.first)),<br />
std::forward_as_tuple(std::forward&lt;V&gt;(xy.second))) </p>
<h2>Parameters</h2>
<p>p &#8211; pointer to allocated, but not initialized storage<br />
args&#8230; &#8211; the constructor arguments to pass to the constructor of T<br />
x &#8211; the constructor arguments to pass to the constructor of T1<br />
y &#8211; the constructor arguments to pass to the constructor of T2<br />
xy &#8211; the pair whose two members are the constructor arguments for T1 and T2</p>
<h2>Return value</h2>
<p><i>(none)</i> </p>
<h2>Notes</h2>
<p>This function is called (through std::allocator_traits) by any allocator-aware object, such as std::vector, that was given a std::polymorphic_allocator as the allocator to use. Since memory_resource* implicitly converts to polymorphic_allocator, the memory resource pointer will propagate to any allocator-aware subobjects using polymorphic allocators. </p>
<h2>See also</h2>
<p>construct constructs an object in the allocated storage<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function template)</i><br />
<code>[static]</code><br />
construct constructs an object in allocated storage<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(public member function of std::allocator&lt;T&gt;)</i><br />
(deprecated in C++17)<br />
(removed in C++20) </p>
