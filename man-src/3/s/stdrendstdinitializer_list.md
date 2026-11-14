---
title: "stdrendstdinitializer_list(3)"
name: "stdrendstdinitializer_list"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdrendstdinitializer_list/"
---

std::rend(std::initializer_list) - std::rend(std::initializer_list)

<h2>Synopsis</h2>

<pre><code>Defined in header&lt;iterator&gt;

    template &lt;class E&gt;
    (since C++ 14)

        std::reverse_iterator&lt;const E *&gt; rend(std::initializer_list&lt;E&gt; il);</code></pre> 
The overload of std::rend for initializer_list returns an std::reverse_iterator pointing at the first element of il. 

<h2>Parameters</h2>

il - an initializer_list

<h2>Return value</h2>

std::reverse_iterator&lt;const E*&gt;(il.begin()). 

<h2>Exceptions</h2>

<i>(none)</i>

<h2>Notes</h2>

This overload is necessary because std::initializer_list does not have a member function rend. No overload is needed for std::crend because it is implemented in terms of std::rend. 

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
