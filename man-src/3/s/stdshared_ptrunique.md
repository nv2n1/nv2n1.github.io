---
title: "stdshared_ptrunique(3)"
name: "stdshared_ptrunique"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdshared_ptrunique/"
---

std::shared_ptr&lt;T&gt;::unique - std::shared_ptr&lt;T&gt;::unique

<h2>Synopsis</h2>

bool unique() const noexcept; (deprecated in C++17) 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;(removed in C++20) 
Checks if *this is the only shared_ptr instance managing the current object, i.e. whether use_count() == 1. 

<h2>Parameters</h2>

<i>(none)</i>

<h2>Return value</h2>

true if *this is the only shared_ptr instance managing the current object, false otherwise. 

<h2>Notes</h2>

This function was deprecated in C++17 and removed in C++20 because use_count is only an approximation in multithreaded environment (see Notes in use_count) 

<h2>Example</h2>

// Run this code <pre><code>#include &lt;memory&gt;

#include &lt;iostream&gt;
int main()

{
    auto sp1 = std::make_shared&lt;int&gt;(5);
    std::cout &lt;&lt; std::boolalpha;
    std::cout &lt;&lt; &quot;sp1.unique() == &quot; &lt;&lt; sp1.unique() &lt;&lt; '\n';
    std::shared_ptr&lt;int&gt; sp2 = sp1;
    std::cout &lt;&lt; &quot;sp1.unique() == &quot; &lt;&lt; sp1.unique() &lt;&lt; '\n';
}
</code></pre>

<h2>Output:</h2>

&nbsp;<wbr>&nbsp;sp1.unique() == true 
&nbsp;<wbr>&nbsp;sp1.unique() == false

<h2>See also</h2>

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;returns the number of shared_ptr objects referring to the same managed object 
use_count <i>(public member function)</i> 
