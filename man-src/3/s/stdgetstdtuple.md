---
title: "stdgetstdtuple(3)"
name: "stdgetstdtuple"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdgetstdtuple/"
---

std::get(std::tuple) - std::get(std::tuple)

<h2>Synopsis</h2>

<pre><code>template &lt;std::size_t I, class... Types&gt;
(since C++ 11)

    typename std::tuple_element&lt;I, tuple&lt;Types...&gt;&gt;::type &amp;(1)(constexpr since C++ 14)

        get(tuple&lt;Types...&gt; &amp;t) noexcept;

template &lt;std::size_t I, class... Types&gt;
    (since C++ 11)

        typename std::tuple_element&lt;I, tuple&lt;Types...&gt;&gt;::type
    &amp;&amp; (2)(constexpr since C++ 14)

           get(tuple&lt;Types...&gt; &amp;&amp;t) noexcept;

template &lt;std::size_t I, class... Types&gt;
(since C++ 11)

    typename std::tuple_element&lt;I, tuple&lt;Types...&gt;&gt;::type const &amp;(3)(constexpr since C++ 14)

        get(const tuple&lt;Types...&gt; &amp;t) noexcept;

template &lt;std::size_t I, class... Types&gt;
    (since C++ 11)

        typename std::tuple_element&lt;I, tuple&lt;Types...&gt;&gt;::type const
    &amp;&amp; (4)(constexpr since C++ 14)

           get(const tuple&lt;Types...&gt; &amp;&amp;t) noexcept;

template &lt;class T, class... Types&gt;
(5)(since C++ 14)

    constexpr T &amp;get(tuple&lt;Types...&gt; &amp;t) noexcept;

template &lt;class T, class... Types&gt;
(6)(since C++ 14)

    constexpr T &amp;&amp;get(tuple&lt;Types...&gt; &amp;&amp;t) noexcept;

template &lt;class T, class... Types&gt;
(7)(since C++ 14)

    constexpr const T &amp;get(const tuple&lt;Types...&gt; &amp;t) noexcept;

template &lt;class T, class... Types&gt;
(8)(since C++ 14)

    constexpr const T &amp;&amp;get(const tuple&lt;Types...&gt; &amp;&amp;t) noexcept;</code></pre> 
1-4) Extracts the Ith element from the tuple. I must be an integer value in [0, sizeof...(Types)). 
5-8) Extracts the element of the tuple t whose type is T. Fails to compile unless the tuple has exactly one element of that type. 

<h2>Parameters</h2>

t - tuple whose contents to extract

<h2>Return value</h2>

A reference to the selected element of t. 
Defect reports 
The following behavior-changing defect reports were applied retroactively to previously published C++ standards. 
DR Applied to Behavior as published Correct behavior 
LWG_2485 C++11 there are no overloads for const tuple&amp;&amp; the overloads are added 

<h2>Example</h2>

// Run this code <pre><code>#include &lt;iostream&gt;

#include &lt;string&gt;

#include &lt;tuple&gt;
int main()

{
    auto t = std::make_tuple(1, &quot;Foo&quot;, 3.14);
    // index-based access
    std::cout &lt;&lt; &quot;(&quot; &lt;&lt; std::get&lt;0&gt;(t) &lt;&lt; &quot;, &quot; &lt;&lt; std::get&lt;1&gt;(t)
              &lt;&lt; &quot;, &quot; &lt;&lt; std::get&lt;2&gt;(t) &lt;&lt; &quot;)\n&quot;;
    // type-based access
    std::cout &lt;&lt; &quot;(&quot; &lt;&lt; std::get&lt;int&gt;(t) &lt;&lt; &quot;, &quot; &lt;&lt; std::get&lt;const char *&gt;(t)
              &lt;&lt; &quot;, &quot; &lt;&lt; std::get&lt;double&gt;(t) &lt;&lt; &quot;)\n&quot;;
    // Note: std::tie and structured binding may also be used to decompose a tuple
}
</code></pre>

<h2>Output:</h2>

&nbsp;<wbr>&nbsp;(1, Foo, 3.14) 
&nbsp;<wbr>&nbsp;(1, Foo, 3.14)

<h2>See also</h2>

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;accesses an element of an array 
std::get(std::array) <i>(function template)</i> 
std::get(std::pair) accesses an element of a pair 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function template)</i> 
<i>(C++11)</i> 
std::get(std::variant) reads the value of the variant given the index or the type (if the type is unique), throws on error 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function template)</i> 
<i>(C++17)</i> 
