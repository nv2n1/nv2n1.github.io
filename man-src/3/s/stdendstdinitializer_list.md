---
title: "stdendstdinitializer_list(3)"
name: "stdendstdinitializer_list"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdendstdinitializer_list/"
---

std::end(std::initializer_list) - std::end(std::initializer_list)

<h2>Synopsis</h2>

template&lt; class E &gt; <i>(since C++11)</i> 
const E* end( initializer_list&lt;E&gt; il ) noexcept; 
template&lt; class E &gt; <i>(since C++11)</i> 
constexpr const E* end( initializer_list&lt;E&gt; il ) noexcept; <i>(until C++14)</i> 
The overload of std::end for initializer_list returns a pointer to one past the last element of il. 

<h2>Parameters</h2>

il - an initializer_list

<h2>Return value</h2>

il.end() 

<h2>Example</h2>

// Run this code <pre><code>#include &lt;iostream&gt;
int main()

{
    // range-based for uses std::begin and std::end to iterate
    // over a given range; in this case, it's an initializer list
    for (int i : {3, 1, 4, 1}) {
        std::cout &lt;&lt; i &lt;&lt; '\n';
    }
}
</code></pre>

<h2>Output:</h2>

&nbsp;<wbr>&nbsp;3 
&nbsp;<wbr>&nbsp;1 
&nbsp;<wbr>&nbsp;4 
&nbsp;<wbr>&nbsp;1

<h2>See also</h2>

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;returns a pointer to one past the last element 
end <i>(public member function)</i> 
