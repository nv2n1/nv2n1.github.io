---
title: "stdrbeginstdinitializer_list(3)"
name: "stdrbeginstdinitializer_list"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdrbeginstdinitializer_list/"
---

std::rbegin(std::initializer_list) - std::rbegin(std::initializer_list)

<h2>Synopsis</h2>

<pre><code>Defined in header&lt;iterator&gt;

    template &lt;class E&gt;
    (since C++ 14)

        std::reverse_iterator&lt;const E *&gt; rbegin(std::initializer_list&lt;E&gt; il);</code></pre> 
The overload of std::rbegin for initializer_list returns an std::reverse_iterator pointing at the last element of il. 

<h2>Parameters</h2>

il - an initializer_list

<h2>Return value</h2>

std::reverse_iterator&lt;const E*&gt;(il.end()). 

<h2>Exceptions</h2>

<i>(none)</i>

<h2>Notes</h2>

This overload is necessary because std::initializer_list does not have a member function rbegin. No overload is needed for std::crbegin because it is implemented in terms of std::rbegin. 

<h2>Example</h2>

// Run this code <pre><code>#include &lt;iostream&gt;

#include &lt;iterator&gt;
int main()

{
    auto il = {3, 1, 4};
    for (auto it = std::rbegin(il); it != std::rend(il); ++it)
        std::cout &lt;&lt; *it &lt;&lt; '\n';
}
</code></pre>

<h2>Output:</h2>

&nbsp;<wbr>&nbsp;4 
&nbsp;<wbr>&nbsp;1 
&nbsp;<wbr>&nbsp;3

<h2>See also</h2>

rbegin returns a reverse iterator to a container or array 
crbegin <i>(function template)</i> 
<i>(C++14)</i> 
rend returns a reverse end iterator for a container or array 
crend <i>(function template)</i> 
<i>(C++14)</i> 
