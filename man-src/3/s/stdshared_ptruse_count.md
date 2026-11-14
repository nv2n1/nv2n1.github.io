---
title: "stdshared_ptruse_count(3)"
name: "stdshared_ptruse_count"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdshared_ptruse_count/"
---

std::shared_ptr&lt;T&gt;::use_count - std::shared_ptr&lt;T&gt;::use_count

<h2>Synopsis</h2>

<pre><code>long use_count() const noexcept;</code></pre> 
Returns the number of different shared_ptr instances (this included) managing the current object. If there is no managed object, 0 is returned. 
In multithreaded environment, the value returned by use_count is approximate (typical implementations use a memory_order_relaxed load) 

<h2>Parameters</h2>

<i>(none)</i>

<h2>Return value</h2>

the number of shared_ptr instances managing the current object or 0 if there is no managed object. 

<h2>Notes</h2>

Common use cases include 
* comparison with 0. If use_count returns zero, the shared pointer is empty and manages no objects (whether or not its stored pointer is null). In multithreaded environment, this does not imply that the destructor of the managed object has completed. 
* comparison with 1. If use_count returns 1, there are no other owners. (The deprecated member function unique() is provided for this use case.) In multithreaded environment, this does not imply that the object is safe to modify because accesses to the managed object by former shared owners may not have completed, and because new shared owners may be introduced concurrently, such as by std::weak_ptr::lock. 

<h2>Example</h2>

// Run this code <pre><code>#include &lt;memory&gt;

#include &lt;iostream&gt;
void fun(std::shared_ptr&lt;int&gt; sp)

{
    std::cout &lt;&lt; &quot;fun: sp.use_count() == &quot; &lt;&lt; sp.use_count() &lt;&lt; '\n';
}
int main()

{
    auto sp1 = std::make_shared&lt;int&gt;(5);
    std::cout &lt;&lt; &quot;sp1.use_count() == &quot; &lt;&lt; sp1.use_count() &lt;&lt; '\n';
    fun(sp1);
}
</code></pre>

<h2>Output:</h2>

&nbsp;<wbr>&nbsp;sp1.use_count() == 1 
&nbsp;<wbr>&nbsp;fun: sp.use_count() == 2

<h2>See also</h2>

unique checks whether the managed object is managed only by the current shared_ptr instance 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(public member function)</i> 
<i>(until C++20)</i> 
