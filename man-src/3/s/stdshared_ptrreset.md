---
title: "stdshared_ptrreset(3)"
name: "stdshared_ptrreset"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdshared_ptrreset/"
description: "std::shared_ptr<T>::reset – std::shared_ptr<T>::reset"
---

<p>std::shared_ptr&lt;T&gt;::reset &#8211; std::shared_ptr&lt;T&gt;::reset</p>
<h2>Synopsis</h2>
<pre><code>void reset() noexcept;
(1)(since C++ 11)

    template &lt;class Y&gt;
    (2)(since C++ 11)

        void reset(Y *ptr);

template &lt;class Y, class Deleter&gt;
(3)(since C++ 11)

    void reset(Y *ptr, Deleter d);

template &lt;class Y, class Deleter, class Alloc&gt;
(4)(since C++ 11)

    void reset(Y *ptr, Deleter d, Alloc alloc);</code></pre>
<p>Replaces the managed object with an object pointed to by ptr. Optional deleter d can be supplied, which is later used to destroy the new object when no shared_ptr objects own it. By default, delete expression is used as deleter. Proper delete expression corresponding to the supplied type is always selected, this is the reason why the function is implemented as template using a separate parameter Y.<br />
If *this already owns an object and it is the last shared_ptr owning it, the object is destroyed through the owned deleter.<br />
If the object pointed to by ptr is already owned, the function results in undefined behavior.<br />
1) Releases the ownership of the managed object, if any. After the call, *this manages no object. Equivalent to shared_ptr().swap(*this);<br />
2-4) Replaces the managed object with an object pointed to by ptr. Y must be a complete type and implicitly convertible to T. Additionally:<br />
2) Uses the delete expression as the deleter. A valid delete expression must be available, i.e. delete ptr must be well formed, have well-defined behavior and not throw any exceptions. Equivalent to shared_ptr&lt;T&gt;(ptr).swap(*this);.<br />
3) Uses the specified deleter d as the deleter. Deleter must be callable for the type T, i.e. d(ptr) must be well formed, have well-defined behavior and not throw any exceptions. Deleter must be CopyConstructible, and its copy constructor and destructor must not throw exceptions. Equivalent to shared_ptr&lt;T&gt;(ptr, d).swap(*this);.<br />
4) Same as <code>(3)</code>, but additionally uses a copy of alloc for allocation of data for internal use. Alloc must be a Allocator. The copy constructor and destructor must not throw exceptions. Equivalent to shared_ptr&lt;T&gt;(ptr, d, alloc).swap(*this);. </p>
<h2>Parameters</h2>
<p>ptr &#8211; pointer to an object to acquire ownership of<br />
d &#8211; deleter to store for deletion of the object<br />
alloc &#8211; allocator to use for internal allocations</p>
<h2>Return value</h2>
<p><i>(none)</i> </p>
<h2>Exceptions</h2>
<p>2) std::bad_alloc if required additional memory could not be obtained. May throw implementation-defined exception for other errors. delete ptr is called if an exception occurs.<br />
3-4) std::bad_alloc if required additional memory could not be obtained. May throw implementation-defined exception for other errors. d(ptr) is called if an exception occurs.</p>
<h2>Example</h2>
<p>// Run this code </p>
<pre><code>#include &lt;memory&gt;

#include &lt;iostream&gt;
struct Foo {
    Foo(int n = 0) noexcept
        : bar(n)
    {
        std::cout &lt;&lt; &quot;Foo: constructor, bar = &quot; &lt;&lt; bar &lt;&lt; '
';
    }
    ~Foo()
    {
        std::cout &lt;&lt; &quot;Foo: destructor, bar = &quot; &lt;&lt; bar &lt;&lt; '
';
    }
    int getBar() const noexcept
    {
        return bar;
    }

  private:
    int bar;
};
int main()

{
    std::shared_ptr&lt;Foo&gt; sptr = std::make_shared&lt;Foo&gt;(1);
    std::cout &lt;&lt; &quot;The first Foo's bar is &quot; &lt;&lt; sptr-&gt;getBar() &lt;&lt; &quot;
&quot;;
    // reset the shared_ptr, hand it a fresh instance of Foo
    // (the old instance will be destroyed after this call)
    sptr.reset(new Foo);
    std::cout &lt;&lt; &quot;The second Foo's bar is &quot; &lt;&lt; sptr-&gt;getBar() &lt;&lt; &quot;
&quot;;
}
</code></pre>
<h2>Output:</h2>
<p>&nbsp;<wbr>&nbsp;Foo: constructor, bar = 1<br />
&nbsp;<wbr>&nbsp;The first Foo&#8217;s bar is 1<br />
&nbsp;<wbr>&nbsp;Foo: constructor, bar = 0<br />
&nbsp;<wbr>&nbsp;Foo: destructor, bar = 1<br />
&nbsp;<wbr>&nbsp;The second Foo&#8217;s bar is 0<br />
&nbsp;<wbr>&nbsp;Foo: destructor, bar = 0</p>
<h2>See also</h2>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;constructs new shared_ptr<br />
constructor <i>(public member function)</i> </p>
