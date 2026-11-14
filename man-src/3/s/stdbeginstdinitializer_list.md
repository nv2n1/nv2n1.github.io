---
title: "stdbeginstdinitializer_list(3)"
name: "stdbeginstdinitializer_list"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdbeginstdinitializer_list/"
---

std::begin(std::initializer_list) - std::begin(std::initializer_list)

<h2>Synopsis</h2>

<pre><code>template &lt;class E&gt;
(since C++ 11)

    const E *begin(initializer_list&lt;E&gt; il) noexcept;
(until C++ 14)

    template &lt;class E&gt;
    (since C++ 14)

        constexpr const E *begin(initializer_list&lt;E&gt; il) noexcept;</code></pre> 
The overload of std::begin for initializer_list returns a pointer to the first element of il. 

<h2>Parameters</h2>

il - an initializer_list

<h2>Return value</h2>

il.begin() 

<h2>Example</h2>

// Run this code <pre><code>#include &lt;iostream&gt;

#include &lt;initializer_list&gt;
int main()

{
    std::initializer_list&lt;int&gt; il = {3, 1, 4, 1};
    for (auto it = std::begin(il); it != std::end(il); ++it) {
        std::cout &lt;&lt; *it &lt;&lt; '\n';
    }
}
</code></pre>

<h2>Output:</h2>

&nbsp;<wbr>&nbsp;3 
&nbsp;<wbr>&nbsp;1 
&nbsp;<wbr>&nbsp;4 
&nbsp;<wbr>&nbsp;1

<h2>See also</h2>

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;returns a pointer to the first element 
begin <i>(public member function)</i> 
