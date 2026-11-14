---
title: "stdgetstdarray(3)"
name: "stdgetstdarray"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdgetstdarray/"
---

std::get(std::array) - std::get(std::array)

<h2>Synopsis</h2>

<pre><code>template &lt;size_t I, class T, size_t N&gt;
(1)(since C++ 11)

    constexpr T &amp;get(array&lt;T, N&gt; &amp;a) noexcept;

template &lt;size_t I, class T, size_t N&gt;
(2)(since C++ 11)

    constexpr T &amp;&amp;get(array&lt;T, N&gt; &amp;&amp;a) noexcept;

template &lt;size_t I, class T, size_t N&gt;
(3)(since C++ 11)

    constexpr const T &amp;get(const array&lt;T, N&gt; &amp;a) noexcept;

template &lt;size_t I, class T, size_t N&gt;
(4)(since C++ 17)

    constexpr const T &amp;&amp;get(const array&lt;T, N&gt; &amp;&amp;a) noexcept;</code></pre> 
Extracts the Ith element element from the array. 
I must be an integer value in range [0, N). This is enforced at compile time as opposed to at() or operator[]. 

<h2>Parameters</h2>

a - array whose contents to extract

<h2>Return value</h2>

A reference to the Ith element of a. 

<h2>Complexity</h2>

Constant.

<h2>Notes</h2>

The overloads are marked as constexpr since C++14. 

<h2>Example</h2>

// Run this code <pre><code>#include &lt;iostream&gt;

#include &lt;array&gt;
int main()

{
    std::array&lt;int, 3&gt; arr;
    // set values:
    std::get&lt;0&gt;(arr) = 1;
    std::get&lt;1&gt;(arr) = 2;
    std::get&lt;2&gt;(arr) = 3;
    // get values:
    std::cout &lt;&lt; &quot;(&quot; &lt;&lt; std::get&lt;0&gt;(arr) &lt;&lt; &quot;, &quot; &lt;&lt; std::get&lt;1&gt;(arr)
              &lt;&lt; &quot;, &quot; &lt;&lt; std::get&lt;2&gt;(arr) &lt;&lt; &quot;)\n&quot;;
}
</code></pre>

<h2>Output:</h2>

&nbsp;<wbr>&nbsp;(1, 2, 3)

<h2>See also</h2>

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;access specified element 
operator[] <i>(public member function)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;access specified element with bounds checking 
at <i>(public member function)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;tuple accesses specified element 
std::get(std::tuple) <i>(function template)</i> 
std::get(std::pair) accesses an element of a pair 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function template)</i> 
<i>(C++11)</i> 
std::get(std::variant) reads the value of the variant given the index or the type (if the type is unique), throws on error 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function template)</i> 
<i>(C++17)</i> 
