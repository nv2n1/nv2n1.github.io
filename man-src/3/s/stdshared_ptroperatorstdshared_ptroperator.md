---
title: "stdshared_ptroperatorstdshared_ptroperator(3)"
name: "stdshared_ptroperatorstdshared_ptroperator"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdshared_ptroperatorstdshared_ptroperator/"
description: "std::shared_ptr<T>::operator*,std::shared_ptr<T>::operator-> – std::shared_ptr<T>::operator*,std::shared_ptr<T>::operator->"
---

<p>std::shared_ptr&lt;T&gt;::operator*,std::shared_ptr&lt;T&gt;::operator-&gt; &#8211; std::shared_ptr&lt;T&gt;::operator*,std::shared_ptr&lt;T&gt;::operator-&gt;</p>
<h2>Synopsis</h2>
<p>T&amp; operator*() const noexcept; <code>(1)</code> <i>(since C++11)</i><br />
T* operator-&gt;() const noexcept; <code>(2)</code> <i>(since C++11)</i><br />
Dereferences the stored pointer. The behavior is undefined if the stored pointer is null. </p>
<h2>Parameters</h2>
<p><i>(none)</i></p>
<h2>Return value</h2>
<p>1) The result of dereferencing the stored pointer, i.e., *get()<br />
2) The stored pointer, i.e., get()<br />
Remarks<br />
When T is a (possibly cv-qualified) void, it is unspecified whether function <code>(1)</code> is declared.<br />
When T is an array type, it is unspecified whether these member functions are declared, and if they are, what their return type is, except that the declaration (not necessarily the definition) of these functions is well-formed. <i>(since C++17)</i><br />
If either function is declared despite being unspecified, it is unspecified what its return type is, except that the declaration (although not necessarily the definition) of the function is guaranteed to be legal. This makes it possible to instantiate std::shared_ptr&lt;void&gt;. </p>
<h2>Example</h2>
<p>// Run this code </p>
<pre><code>#include &lt;iostream&gt;

#include &lt;memory&gt;
struct Foo

{
    Foo(int in)
        : a(in)
    {
    }
    void print() const
    {
        std::cout &lt;&lt; &quot;a = &quot; &lt;&lt; a &lt;&lt; '
';
    }
    int a;
};
int main()

{
    auto ptr = std::make_shared&lt;Foo&gt;(10);
    ptr-&gt;print();
    (*ptr).print();
}
</code></pre>
<h2>Output:</h2>
<p>&nbsp;<wbr>&nbsp;a = 10<br />
&nbsp;<wbr>&nbsp;a = 10</p>
<h2>See also</h2>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;returns the stored pointer<br />
get <i>(public member function)</i> </p>
