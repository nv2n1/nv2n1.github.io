---
title: "stdenable_shared_from_thisshared_from_this(3)"
name: "stdenable_shared_from_thisshared_from_this"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdenable_shared_from_thisshared_from_this/"
description: "std::enable_shared_from_this<T>::shared_from_this – std::enable_shared_from_this<T>::shared_from_this"
---

<p>std::enable_shared_from_this&lt;T&gt;::shared_from_this &#8211; std::enable_shared_from_this&lt;T&gt;::shared_from_this</p>
<h2>Synopsis</h2>
<p>shared_ptr&lt;T&gt; shared_from_this(); <code>(1)</code><br />
shared_ptr&lt;T const&gt; shared_from_this() const; <code>(2)</code><br />
Returns a std::shared_ptr&lt;T&gt; that shares ownership of *this with all existing std::shared_ptr that refer to *this.<br />
Effectively executes std::shared_ptr&lt;T&gt;(weak_this), where weak_this is the private mutable std::weak_ptr&lt;T&gt; member of enable_shared_from_this. </p>
<h2>Notes</h2>
<p>It is permitted to call shared_from_this only on a previously shared object, i.e. on an object managed by std::shared_ptr (in particular, shared_from_this cannot be called during construction of *this).<br />
Otherwise<br />
the behavior is undefined<br />
<i>(until C++17)</i><br />
std::bad_weak_ptr is thrown (by the shared_ptr constructor from a default-constructed weak_this)<br />
<i>(since C++17)</i>. </p>
<h2>Return value</h2>
<p>std::shared_ptr&lt;T&gt; that shares ownership of *this with pre-existing std::shared_ptrs </p>
<h2>Example</h2>
<p>// Run this code </p>
<pre><code>#include &lt;iostream&gt;

#include &lt;memory&gt;
struct Foo : public std::enable_shared_from_this&lt;Foo&gt; {
    Foo()
    {
        std::cout &lt;&lt; &quot;Foo::Foo
&quot;;
    }
    ~Foo()
    {
        std::cout &lt;&lt; &quot;Foo::~Foo
&quot;;
    }
    std::shared_ptr&lt;Foo&gt; getFoo()
    {
        return shared_from_this();
    }
};
int main()
{
    Foo *f = new Foo;
    std::shared_ptr&lt;Foo&gt; pf1;
    {
        std::shared_ptr&lt;Foo&gt; pf2(f);
        pf1 = pf2-&gt;getFoo(); // shares ownership of object with pf2
    }
    std::cout &lt;&lt; &quot;pf2 is gone
&quot;;
}
</code></pre>
<h2>Output:</h2>
<p>&nbsp;<wbr>&nbsp;Foo::Foo<br />
&nbsp;<wbr>&nbsp;pf2 is gone<br />
&nbsp;<wbr>&nbsp;Foo::~Foo</p>
<h2>See also</h2>
<p>shared_ptr smart pointer with shared object ownership semantics<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(class template)</i><br />
<i>(C++11)</i> </p>
