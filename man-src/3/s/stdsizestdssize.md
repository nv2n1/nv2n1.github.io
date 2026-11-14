---
title: "stdsizestdssize(3)"
name: "stdsizestdssize"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdsizestdssize/"
---

std::size,std::ssize - std::size,std::ssize

<h2>Synopsis</h2>

<pre><code>Defined in header&lt;iterator&gt;

    template &lt;class C&gt;
    (1)(since C++ 17)

        constexpr auto size(const C &amp;c) -&gt; decltype(c.size());

template &lt;class C&gt;

constexpr auto ssize(const C &amp;c)(2)(since C++ 20)

    -&gt; std::common_type_t&lt;std::ptrdiff_t,

                          std::make_signed_t&lt;decltype(c.size())&gt;&gt;;

template &lt;class T, std::size_t N&gt;
(3)(since C++ 17)

    constexpr std::size_t size(const T (&amp;array)[N]) noexcept;

template &lt;class T, std::ptrdiff_t N&gt;
(4)(since C++ 20)

    constexpr std::ptrdiff_t ssize(const T (&amp;array)[N]) noexcept;
Returns the size of the given container c or array array.

1-2) Returns c.size(), converted to the return type if necessary.

3-4) Returns N.
</code></pre>

<h2>Parameters</h2>

c - a container with a size method 
array - an array of arbitrary type

<h2>Return value</h2>

The size of c or array 

<h2>Notes</h2>

In addition to being included in &lt;iterator&gt;, std::size and std::ssize are guaranteed to become available if any of the following headers are included: &lt;array&gt;, &lt;deque&gt;, &lt;forward_list&gt;, &lt;list&gt;, &lt;map&gt;, &lt;regex&gt;, &lt;set&gt; 
, &lt;span&gt; 
<i>(since C++20)</i>, &lt;string&gt;, &lt;string_view&gt;, &lt;unordered_map&gt;, &lt;unordered_set&gt;, and &lt;vector&gt;. 

<h2>Possible implementation</h2>

<h2>First version</h2>

&nbsp;<wbr>&nbsp;template &lt;class C&gt; 
&nbsp;<wbr>&nbsp;constexpr auto size(const C&amp; c) -&gt; decltype(c.size()) 
&nbsp;<wbr>&nbsp;{ 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;return c.size(); 
&nbsp;<wbr>&nbsp;}

<h2>Second version</h2>

&nbsp;<wbr>&nbsp;template &lt;class C&gt; 
&nbsp;<wbr>&nbsp;constexpr auto ssize(const C&amp; c) 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;-&gt; std::common_type_t&lt;std::ptrdiff_t, 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;std::make_signed_t&lt;decltype(c.size())&gt;&gt; { 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;using R = std::common_type_t&lt;std::ptrdiff_t, 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;std::make_signed_t&lt;decltype(c.size())&gt;&gt;; 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;return static_cast&lt;R&gt;(c.size()); 
&nbsp;<wbr>&nbsp;} 

 
Third version 

 
&nbsp;<wbr>&nbsp;template &lt;class T, std::size_t N&gt; 
&nbsp;<wbr>&nbsp;constexpr std::size_t size(const T (&amp;array)[N]) noexcept 
&nbsp;<wbr>&nbsp;{ 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;return N; 
&nbsp;<wbr>&nbsp;} 

 
Fourth version 

 
&nbsp;<wbr>&nbsp;template &lt;class T, std::ptrdiff_t N&gt; 
&nbsp;<wbr>&nbsp;constexpr std::ptrdiff_t ssize(const T (&amp;array)[N]) noexcept 
&nbsp;<wbr>&nbsp;{ 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;return N; 
&nbsp;<wbr>&nbsp;}

<h2>Example</h2>

// Run this code <pre><code>#include &lt;iostream&gt;

#include &lt;vector&gt;

#include &lt;iterator&gt;
int main()

{
    std::vector&lt;int&gt; v = {3, 1, 4};
    std::cout &lt;&lt; std::size(v) &lt;&lt; '\n';
    int a[] = {-5, 10, 15};
    std::cout &lt;&lt; std::size(a) &lt;&lt; '\n';
}
</code></pre>

<h2>Output:</h2>

&nbsp;<wbr>&nbsp;3 
&nbsp;<wbr>&nbsp;3
