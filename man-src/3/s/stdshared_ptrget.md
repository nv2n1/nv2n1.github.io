---
title: "stdshared_ptrget(3)"
name: "stdshared_ptrget"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdshared_ptrget/"
---

std::shared_ptr&lt;T&gt;::get - std::shared_ptr&lt;T&gt;::get

<h2>Synopsis</h2>

T* get() const noexcept; <i>(until C++17)</i> 
element_type* get() const noexcept; <i>(since C++17)</i> 
Returns the stored pointer. 

<h2>Parameters</h2>

<i>(none)</i>

<h2>Return value</h2>

The stored pointer. 

<h2>Notes</h2>

A shared_ptr may share ownership of an object while storing a pointer to another object. get() returns the stored pointer, not the managed pointer. 

<h2>Example</h2>

// Run this code <pre><code>#include &lt;iostream&gt;

#include &lt;memory&gt;

#include &lt;string_view&gt;
void output(std::string_view msg, int const *pInt)

{
    std::cout &lt;&lt; msg &lt;&lt; *pInt &lt;&lt; &quot;\n&quot;;
}
int main()

{
    int *pInt = new int(42);
    std::shared_ptr&lt;int&gt; pShared = std::make_shared&lt;int&gt;(42);
    output(&quot;Naked pointer &quot;, pInt);
    // output(&quot;Shared pointer &quot;, pShared); // compiler error
    output(&quot;Shared pointer with get() &quot;, pShared.get());
    delete pInt;
}
</code></pre>

<h2>Output:</h2>

&nbsp;<wbr>&nbsp;Naked pointer 42 
&nbsp;<wbr>&nbsp;Shared pointer with get() 42

<h2>See also</h2>

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;dereferences the stored pointer 
operator* <i>(public member function)</i> 
operator-&gt; 
