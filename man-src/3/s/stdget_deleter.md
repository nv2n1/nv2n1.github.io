---
title: "stdget_deleter(3)"
name: "stdget_deleter"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdget_deleter/"
---

std::get_deleter - std::get_deleter

<h2>Synopsis</h2>

<pre><code>template &lt;class Deleter, class T&gt;
(since C++ 11)

    Deleter *get_deleter(const std::shared_ptr&lt;T&gt; &amp;p) noexcept;</code></pre> 
Access to the p's deleter. If the shared pointer p owns a deleter of type cv-unqualified Deleter (e.g. if it was created with one of the constructors that take a deleter as a parameter), then returns a pointer to the deleter. Otherwise, returns a null pointer. 

<h2>Parameters</h2>

p - a shared pointer whose deleter needs to be accessed

<h2>Return value</h2>

A pointer to the owned deleter or nullptr. The returned pointer is valid at least as long as there remains at least one shared_ptr instance that owns it. 

<h2>Notes</h2>

The returned pointer may outlive the last shared_ptr if, for example, std::weak_ptrs remain and the implementation doesn't destroy the deleter until the entire control block is destroyed. 

<h2>Example</h2>

demonstrates that shared_ptr deleter is independent of the shared_ptr's type 
 // Run this code <pre><code>#include &lt;iostream&gt;

#include &lt;memory&gt;
struct Foo {
    int i;
};

void foo_deleter(Foo *p)

{
    std::cout &lt;&lt; &quot;foo_deleter called!\n&quot;;
    delete p;
}
int main()

{
    std::shared_ptr&lt;int&gt; aptr;
    {
        // create a shared_ptr that owns a Foo and a deleter
        auto foo_p = new Foo;
        std::shared_ptr&lt;Foo&gt; r(foo_p, foo_deleter);
        aptr = std::shared_ptr&lt;int&gt;(r, &amp;r-&gt;i); // aliasing ctor
        // aptr is now pointing to an int, but managing the whole Foo
    } // r gets destroyed (deleter not called)
      // obtain pointer to the deleter:
    if (auto del_p = std::get_deleter&lt;void (*)(Foo *)&gt;(aptr)) {
        std::cout &lt;&lt; &quot;shared_ptr&lt;int&gt; owns a deleter\n&quot;;
        if (*del_p == foo_deleter)
            std::cout &lt;&lt; &quot;...and it equals &amp;foo_deleter\n&quot;;
    } else
        std::cout &lt;&lt; &quot;The deleter of shared_ptr&lt;int&gt; is null!\n&quot;;

} // deleter called here
</code></pre>

<h2>Output:</h2>

&nbsp;<wbr>&nbsp;shared_ptr&lt;int&gt; owns a deleter 
&nbsp;<wbr>&nbsp;...and it equals &amp;foo_deleter 
&nbsp;<wbr>&nbsp;foo_deleter called!

<h2>See also</h2>

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;std::shared_ptr constructors 
constructor <i>(public member function)</i> 
