---
title: "stdweak_ptrexpired(3)"
name: "stdweak_ptrexpired"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdweak_ptrexpired/"
---

std::weak_ptr&lt;T&gt;::expired - std::weak_ptr&lt;T&gt;::expired

<h2>Synopsis</h2>

bool expired() const noexcept; <i>(since C++11)</i> 
Equivalent to use_count() == 0. The destructor for the managed object may not yet have been called, but this object's destruction is imminent (or may have already happened). 

<h2>Parameters</h2>

<i>(none)</i>

<h2>Return value</h2>

true if the managed object has already been deleted, false otherwise. 

<h2>Notes</h2>

This function is inherently racy if the managed object is shared among threads. In particular, a false result may become stale before it can be used. A true result is reliable. 

<h2>Example</h2>

Demonstrates how expired is used to check validity of the pointer. 
 // Run this code <pre><code>#include &lt;iostream&gt;

#include &lt;memory&gt;
std::weak_ptr&lt;int&gt; gw;
void f()

{
    if (!gw.expired()) {

        std::cout &lt;&lt; &quot;gw is valid\n&quot;;
    } else {
        std::cout &lt;&lt; &quot;gw is expired\n&quot;;
    }
}
int main()

{
    {
        auto sp = std::make_shared&lt;int&gt;(42);

        gw = sp;
        f();
    }
    f();
}
</code></pre>

<h2>Output:</h2>

&nbsp;<wbr>&nbsp;gw is valid 
&nbsp;<wbr>&nbsp;gw is expired

<h2>See also</h2>

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;creates a shared_ptr that manages the referenced object 
lock <i>(public member function)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;returns the number of shared_ptr objects that manage the object 
use_count <i>(public member function)</i> 
