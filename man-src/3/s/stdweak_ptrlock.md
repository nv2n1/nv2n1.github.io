---
title: "stdweak_ptrlock(3)"
name: "stdweak_ptrlock"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdweak_ptrlock/"
---

std::weak_ptr&lt;T&gt;::lock - std::weak_ptr&lt;T&gt;::lock

<h2>Synopsis</h2>

std::shared_ptr&lt;T&gt; lock() const noexcept; <i>(since C++11)</i> 
Creates a new std::shared_ptr that shares ownership of the managed object. If there is no managed object, i.e. *this is empty, then the returned shared_ptr also is empty. 
Effectively returns expired() ? shared_ptr&lt;T&gt;() : shared_ptr&lt;T&gt;(*this), executed atomically. 

<h2>Parameters</h2>

<i>(none)</i>

<h2>Return value</h2>

A shared_ptr which shares ownership of the owned object if std::weak_ptr::expired returns false. Else returns default-constructed shared_ptr of type T. 

<h2>Notes</h2>

Both this function and the constructor of std::shared_ptr may be used to acquire temporary ownership of the managed object referred to by a std::weak_ptr. The difference is that the constructor of std::shared_ptr throws an exception when its std::weak_ptr argument is empty, while std::weak_ptr&lt;T&gt;::lock() constructs an empty std::shared_ptr&lt;T&gt;. 

<h2>Example</h2>

// Run this code <pre><code>#include &lt;iostream&gt;

#include &lt;memory&gt;
void observe(std::weak_ptr&lt;int&gt; weak)

{
    if (auto observe = weak.lock()) {
        std::cout &lt;&lt; &quot;\tobserve() able to lock weak_ptr&lt;&gt;, value=&quot; &lt;&lt; *observe &lt;&lt; &quot;\n&quot;;
    } else {
        std::cout &lt;&lt; &quot;\tobserve() unable to lock weak_ptr&lt;&gt;\n&quot;;
    }
}
int main()

{
    std::weak_ptr&lt;int&gt; weak;
    std::cout &lt;&lt; &quot;weak_ptr&lt;&gt; not yet initialized\n&quot;;
    observe(weak);
    {
        auto shared = std::make_shared&lt;int&gt;(42);
        weak = shared;
        std::cout &lt;&lt; &quot;weak_ptr&lt;&gt; initialized with shared_ptr.\n&quot;;
        observe(weak);
    }
    std::cout &lt;&lt; &quot;shared_ptr&lt;&gt; has been destructed due to scope exit.\n&quot;;
    observe(weak);
}
</code></pre>

<h2>Output:</h2>

&nbsp;<wbr>&nbsp;weak_ptr&lt;&gt; not yet initialized 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;observe() unable to lock weak_ptr&lt;&gt; 
&nbsp;<wbr>&nbsp;weak_ptr&lt;&gt; initialized with shared_ptr. 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;observe() able to lock weak_ptr&lt;&gt;, value=42 
&nbsp;<wbr>&nbsp;shared_ptr&lt;&gt; has been destructed due to scope exit. 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;observe() unable to lock weak_ptr&lt;&gt; 

 

 
Defect reports 

 
The following behavior-changing defect reports were applied retroactively to previously published C++ standards. 

 
DR Applied to Behavior as published Correct behavior 
LWG_2316 C++11 lock() was not required to be atomic, but required to be noexcept, which led to a contradiction specified to be atomic

<h2>See also</h2>

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;checks whether the referenced object was already deleted 
expired <i>(public member function)</i> 
