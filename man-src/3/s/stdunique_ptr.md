---
title: "stdunique_ptr(3)"
name: "stdunique_ptr"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdunique_ptr/"
---

std::unique_ptr&lt;T,Deleter&gt;::~unique_ptr - std::unique_ptr&lt;T,Deleter&gt;::~unique_ptr

<h2>Synopsis</h2>

~unique_ptr(); <i>(since C++11)</i> 
If get() == nullptr there are no effects. Otherwise, the owned object is destroyed via get_deleter()(get()). 
Requires that get_deleter()(get()) does not throw exceptions. 

<h2>Notes</h2>

Although std::unique_ptr&lt;T&gt; with the default deleter may be constructed with incomplete_type T, the type T must be complete at the point of code where the destructor is called. 

<h2>Example</h2>

The following program demonstrates usage of a custom deleter. 
 // Run this code <pre><code>#include &lt;iostream&gt;

#include &lt;memory&gt;
int main()

{
    auto deleter = [](int *ptr) {
        std::cout &lt;&lt; &quot;[deleter called]\n&quot;;
        delete ptr;
    };
    std::unique_ptr&lt;int, decltype(deleter)&gt; uniq(new int, deleter);
    std::cout &lt;&lt; (uniq ? &quot;not empty\n&quot; : &quot;empty\n&quot;);
    uniq.reset();
    std::cout &lt;&lt; (uniq ? &quot;not empty\n&quot; : &quot;empty\n&quot;);
}
</code></pre>

<h2>Output:</h2>

&nbsp;<wbr>&nbsp;not empty 
&nbsp;<wbr>&nbsp;[deleter called] 
&nbsp;<wbr>&nbsp;empty
