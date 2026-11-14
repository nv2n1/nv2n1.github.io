---
title: "stdmake_any(3)"
name: "stdmake_any"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdmake_any/"
---

std::make_any - std::make_any

<h2>Synopsis</h2>

<pre><code>template &lt;class T, class... Args&gt;
(1)(since C++ 17)

    std::any make_any(Args &amp;&amp;...args);

template &lt;class T, class U, class... Args&gt;
(2)(since C++ 17)

    std::any make_any(std::initializer_list&lt;U&gt; il, Args &amp;&amp;...args);
Constructs an any object containing an object of type T, passing the provided arguments to T's constructor.

1) Equivalent to return std::any(std::in_place_type&lt;T&gt;, std::forward&lt;Args&gt;(args)...);

2) Equivalent to return std::any(std::in_place_type&lt;T&gt;, il, std::forward&lt;Args&gt;(args)...);
</code></pre>

<h2>See also</h2>

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;constructs an any object 
constructor <i>(public member function)</i> 
