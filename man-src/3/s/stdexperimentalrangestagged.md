---
title: "stdexperimentalrangestagged(3)"
name: "stdexperimentalrangestagged"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdexperimentalrangestagged/"
---

std::experimental::ranges::tagged&lt;Base,Tags...&gt;::tagged - std::experimental::ranges::tagged&lt;Base,Tags...&gt;::tagged

<h2>Synopsis</h2>

<pre><code>using Base::Base;
(1)

    tagged() = default;
(2)

    tagged(tagged &amp;&amp;that) = default;
(3)

    tagged(const tagged &amp;that) = default;
(4)

    tagged(Base &amp;&amp;that) noexcept(std::is_nothrow_move_constructible&lt;Base&gt;::value)(5)

        requires MoveConstructible&lt;Base&gt;;

tagged(const Base &amp;that) noexcept(std::is_nothrow_copy_constructible&lt;Base&gt;::value)(6)

    requires CopyConstructible&lt;Base&gt;;

template &lt;class Other&gt;

requires Constructible&lt;Base, Other&gt;(7)

constexpr tagged(ranges::tagged&lt;Other, Tags...&gt; &amp;&amp;that)

    noexcept(std::is_nothrow_constructible&lt;Base, Other&gt;::value);

template &lt;class Other&gt;

requires Constructible&lt;Base, const Other &amp;&gt;(8)

constexpr tagged(const ranges::tagged&lt;Other, Tags...&gt; &amp;that);</code></pre> 
Constructs a tagged object. 
1) tagged&lt;Base, Tags...&gt; inherits the constructors of Base. 
2-4) tagged has defaulted default, copy, and move constructors that invoke the corresponding constructor of Base. 
5) Converting move constructor from Base. Initializes the Base subobject with std::move(that). 
6) Converting copy constructor from Base. Initializes the Base subobject with that. 
7) Converting move constructor from a different tagged specialization with matching tags. Initializes the Base subobject with static_cast&lt;Other&amp;&amp;&gt;(that). 
8) Converting copy constructor from a different tagged specialization with matching tags. Initializes the Base subobject with static_cast&lt;const Other&amp;&gt;(that). 
