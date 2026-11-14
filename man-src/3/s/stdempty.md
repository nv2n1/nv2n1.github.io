---
title: "stdempty(3)"
name: "stdempty"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdempty/"
---

std::empty - std::empty

<h2>Synopsis</h2>

<pre><code>Defined in header&lt;iterator&gt;

    template &lt;class C&gt;
    (since C++ 17)

        constexpr auto empty(const C &amp;c) -&gt; decltype(c.empty());
(until C++ 20)

    template &lt;class C&gt;
    (since C++ 20)

        [[nodiscard]] constexpr auto empty(const C &amp;c) -&gt; decltype(c.empty());

template &lt;class T, std::size_t N&gt;
(since C++ 17)

    constexpr bool empty(const T (&amp;array)[N]) noexcept;
(1)(until C++ 20)

    template &lt;class T, std::size_t N&gt;
    (since C++ 20)

        [[nodiscard]] constexpr bool empty(const T (&amp;array)[N]) noexcept;
(2)

    template &lt;class E&gt;
    (since C++ 17)

        constexpr bool empty(std::initializer_list&lt;E&gt; il) noexcept;
(3)(until C++ 20)

    template &lt;class E&gt;
    (since C++ 20)

        [[nodiscard]] constexpr bool empty(std::initializer_list&lt;E&gt; il) noexcept;</code></pre> 
Returns whether the given container is empty. 
1) returns c.empty() 
2) returns false 
3) returns il.size() == 0 

<h2>Parameters</h2>

c - a container with an empty method 
array - an array of arbitrary type 
il - an initializer list

<h2>Return value</h2>

true if the container doesn't have any element. 

<h2>Notes</h2>

In addition to being included in &lt;iterator&gt;, std::empty is guaranteed to become available if any of the following headers are included: &lt;array&gt;, &lt;deque&gt;, &lt;forward_list&gt;, &lt;list&gt;, &lt;map&gt;, &lt;regex&gt;, &lt;set&gt; 
, &lt;span&gt; 
<i>(since C++20)</i>, &lt;string&gt;, &lt;string_view&gt;, &lt;unordered_map&gt;, &lt;unordered_set&gt;, and &lt;vector&gt;. 

<h2>Possible implementation</h2>

<h2>First version</h2>

&nbsp;<wbr>&nbsp;template &lt;class C&gt; 
&nbsp;<wbr>&nbsp;constexpr auto empty(const C&amp; c) -&gt; decltype(c.empty()) 
&nbsp;<wbr>&nbsp;{ 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;return c.empty(); 
&nbsp;<wbr>&nbsp;}

<h2>Second version</h2>

&nbsp;<wbr>&nbsp;template &lt;class T, std::size_t N&gt; 
&nbsp;<wbr>&nbsp;constexpr bool empty(const T (&amp;array)[N]) noexcept 
&nbsp;<wbr>&nbsp;{ 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;return false; 
&nbsp;<wbr>&nbsp;} 

 
Third version 

 
&nbsp;<wbr>&nbsp;template &lt;class E&gt; 
&nbsp;<wbr>&nbsp;constexpr bool empty(std::initializer_list&lt;E&gt; il) noexcept 
&nbsp;<wbr>&nbsp;{ 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;return il.size() == 0; 
&nbsp;<wbr>&nbsp;}

<h2>Example</h2>

// Run this code <pre><code>#include &lt;iostream&gt;

#include &lt;vector&gt;
template &lt;class T&gt;

void print(const T &amp;container)

{
    if (!std::empty(container)) {
        std::cout &lt;&lt; &quot;Elements:\n&quot;;
        for (const auto &amp;element : container)
            std::cout &lt;&lt; element &lt;&lt; '\n';
    } else {
        std::cout &lt;&lt; &quot;Empty\n&quot;;
    }
}
int main()

{
    std::vector&lt;int&gt; c = {1, 2, 3};
    print(c);
    c.clear();
    print(c);
    int array[] = {4, 5, 6};
    print(array);
    auto il = {7, 8, 9};
    print(il);
}
</code></pre>

<h2>Output:</h2>

&nbsp;<wbr>&nbsp;Elements: 
&nbsp;<wbr>&nbsp;1 
&nbsp;<wbr>&nbsp;2 
&nbsp;<wbr>&nbsp;3 
&nbsp;<wbr>&nbsp;Empty 
&nbsp;<wbr>&nbsp;Elements: 
&nbsp;<wbr>&nbsp;4 
&nbsp;<wbr>&nbsp;5 
&nbsp;<wbr>&nbsp;6 
&nbsp;<wbr>&nbsp;Elements: 
&nbsp;<wbr>&nbsp;7 
&nbsp;<wbr>&nbsp;8 
&nbsp;<wbr>&nbsp;9
