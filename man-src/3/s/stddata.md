---
title: "stddata(3)"
name: "stddata"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stddata/"
---

std::data - std::data

<h2>Synopsis</h2>

<pre><code>Defined in header&lt;iterator&gt;

    template &lt;class C&gt;
    (1)(since C++ 17)

        constexpr auto data(C &amp;c) -&gt; decltype(c.data());

template &lt;class C&gt;
(2)(since C++ 17)

    constexpr auto data(const C &amp;c) -&gt; decltype(c.data());

template &lt;class T, std::size_t N&gt;
(3)(since C++ 17)

    constexpr T *data(T (&amp;array)[N]) noexcept;

template &lt;class E&gt;
(4)(since C++ 17)

    constexpr const E *data(std::initializer_list&lt;E&gt; il) noexcept;</code></pre> 
Returns a pointer to the block of memory containing the elements of the container. 
1,2) returns c.data() 
3) returns array 
4) returns il.begin() 

<h2>Parameters</h2>

c - a container with a data() method 
array - an array of arbitrary type 
il - an initializer list

<h2>Return value</h2>

A pointer to the block of memory containing the elements of the container. 

<h2>Notes</h2>

In addition to being included in &lt;iterator&gt;, std::data is guaranteed to become available if any of the following headers are included: &lt;array&gt;, &lt;deque&gt;, &lt;forward_list&gt;, &lt;list&gt;, &lt;map&gt;, &lt;regex&gt;, &lt;set&gt; 
, &lt;span&gt; 
<i>(since C++20)</i>, &lt;string&gt;, &lt;string_view&gt;, &lt;unordered_map&gt;, &lt;unordered_set&gt;, and &lt;vector&gt;. 

<h2>Possible implementation</h2>

<h2>First version</h2>

&nbsp;<wbr>&nbsp;template &lt;class C&gt; 
&nbsp;<wbr>&nbsp;constexpr auto data(C&amp; c) -&gt; decltype(c.data()) 
&nbsp;<wbr>&nbsp;{ 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;return c.data(); 
&nbsp;<wbr>&nbsp;}

<h2>Second version</h2>

&nbsp;<wbr>&nbsp;template &lt;class C&gt; 
&nbsp;<wbr>&nbsp;constexpr auto data(const C&amp; c) -&gt; decltype(c.data()) 
&nbsp;<wbr>&nbsp;{ 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;return c.data(); 
&nbsp;<wbr>&nbsp;} 

 
Third version 

 
&nbsp;<wbr>&nbsp;template &lt;class T, std::size_t N&gt; 
&nbsp;<wbr>&nbsp;constexpr T* data(T (&amp;array)[N]) noexcept 
&nbsp;<wbr>&nbsp;{ 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;return array; 
&nbsp;<wbr>&nbsp;} 

 
Fourth version 

 
&nbsp;<wbr>&nbsp;template &lt;class E&gt; 
&nbsp;<wbr>&nbsp;constexpr const E* data(std::initializer_list&lt;E&gt; il) noexcept 
&nbsp;<wbr>&nbsp;{ 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;return il.begin(); 
&nbsp;<wbr>&nbsp;}

<h2>Example</h2>

// Run this code <pre><code>#include &lt;string&gt; //std::data is guaranteed to be available after inclusion

#include &lt;cstring&gt;

#include &lt;iostream&gt;
int main()

{
    std::string s{&quot;Hello world!\n&quot;};
    char a[20]; // storage for a C-style string
    std::strcpy(a, std::data(s));
    //[s.data(), s.data() + s.size()] is guaranteed to be an NTBS since C++11
    std::cout &lt;&lt; a &lt;&lt; &quot;\n&quot;;
}
</code></pre>

<h2>Output:</h2>

&nbsp;<wbr>&nbsp;Hello world!
