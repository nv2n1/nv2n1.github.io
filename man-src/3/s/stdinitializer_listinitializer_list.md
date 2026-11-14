---
title: "stdinitializer_listinitializer_list(3)"
name: "stdinitializer_listinitializer_list"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdinitializer_listinitializer_list/"
---

std::initializer_list&lt;T&gt;::initializer_list - std::initializer_list&lt;T&gt;::initializer_list

<h2>Synopsis</h2>

initializer_list() noexcept; <i>(since C++11)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(until C++14)</i> 
constexpr initializer_list() noexcept; <i>(since C++14)</i> 
Constructs an empty initializer list. 

<h2>Parameters</h2>

<i>(none)</i>

<h2>Complexity</h2>

Constant

<h2>Example</h2>

// Run this code <pre><code>#include &lt;iostream&gt;

#include &lt;initializer_list&gt;
int main()

{
    std::initializer_list&lt;int&gt; empty_list;
    std::cout &lt;&lt; &quot;empty_list.size(): &quot; &lt;&lt; empty_list.size() &lt;&lt; '\n';
    // create initializer lists using list-initialization
    std::initializer_list&lt;int&gt; digits{1, 2, 3, 4, 5};
    std::cout &lt;&lt; &quot;digits.size(): &quot; &lt;&lt; digits.size() &lt;&lt; '\n';
    // special rule for auto means 'fractions' has the
    // type std::initializer_list&lt;double&gt;
    auto fractions = {3.14159, 2.71828};
    std::cout &lt;&lt; &quot;fractions.size(): &quot; &lt;&lt; fractions.size() &lt;&lt; '\n';
}
</code></pre>

<h2>Output:</h2>

&nbsp;<wbr>&nbsp;empty_list.size(): 0 
&nbsp;<wbr>&nbsp;digits.size(): 5 
&nbsp;<wbr>&nbsp;fractions.size(): 2

<h2>Notes</h2>

Despite a lack of constructors, it is possible to create non-empty initializer lists. Instances of std::initializer_list are implicitly constructed when: 
* a braced-init-list is used in list-initialization, including function-call list initialization and assignment expressions (not to be confused with constructor_initializer_lists) 
* a braced-init-list is bound to auto, including in a ranged_for_loop 
