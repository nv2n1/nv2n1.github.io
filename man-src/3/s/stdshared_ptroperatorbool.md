---
title: "stdshared_ptroperatorbool(3)"
name: "stdshared_ptroperatorbool"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdshared_ptroperatorbool/"
---

std::shared_ptr&lt;T&gt;::operatorbool - std::shared_ptr&lt;T&gt;::operatorbool

<h2>Synopsis</h2>

<pre><code>explicit operator bool() const noexcept;</code></pre> 
Checks if *this stores a non-null pointer, i.e. whether get() != nullptr. 

<h2>Parameters</h2>

<i>(none)</i>

<h2>Return value</h2>

true if *this stores a pointer, false otherwise. 

<h2>Notes</h2>

An empty shared_ptr (where use_count() == 0) may store a non-null pointer accessible by get(), e.g. if it were created using the aliasing constructor. 

<h2>Example</h2>

// Run this code <pre><code>#include &lt;iostream&gt;

#include &lt;memory&gt;
void report(std::shared_ptr&lt;int&gt; ptr)

{
    if (ptr) {
        std::cout &lt;&lt; &quot;*ptr=&quot; &lt;&lt; *ptr &lt;&lt; &quot;\n&quot;;
    } else {
        std::cout &lt;&lt; &quot;ptr is not a valid pointer.\n&quot;;
    }
}
int main()

{
    std::shared_ptr&lt;int&gt; ptr;
    report(ptr);
    ptr = std::make_shared&lt;int&gt;(7);
    report(ptr);
}
</code></pre>

<h2>Output:</h2>

&nbsp;<wbr>&nbsp;ptr is not a valid pointer. 
&nbsp;<wbr>&nbsp;*ptr=7

<h2>See also</h2>

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;returns the stored pointer 
get <i>(public member function)</i> 
