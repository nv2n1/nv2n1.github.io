---
title: "stddefault_delete(3)"
name: "stddefault_delete"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stddefault_delete/"
description: "std::default_delete – std::default_delete"
---

<p>std::default_delete &#8211; std::default_delete</p>
<h2>Synopsis</h2>
<p>Defined in header &lt;memory&gt;<br />
template&lt; class T &gt; struct default_delete; <code>(1)</code> <i>(since C++11)</i><br />
template&lt; class T &gt; struct default_delete&lt;T[]&gt;; <code>(2)</code> <i>(since C++11)</i><br />
std::default_delete is the default destruction policy used by std::unique_ptr when no deleter is specified.<br />
1) The non-specialized default_delete uses delete to deallocate memory for a single object.<br />
2) A partial specialization for array types that uses delete[] is also provided. </p>
<h2>Member functions</h2>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;constructs a default_delete object<br />
constructor <i>(public member function)</i><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;deletes the object or array<br />
operator() <i>(public member function)</i> </p>
<p>&nbsp;std::default_delete::default_delete </p>
<p>constexpr default_delete() noexcept = default; <code>(1)</code><br />
template &lt;class U&gt; <code>(2)</code> (member only of primary default_delete template)<br />
default_delete( const default_delete&lt;U&gt;&amp; d ) noexcept;<br />
template&lt;class U&gt; <code>(3)</code> <i>(since C++17)</i><br />
default_delete( const default_delete&lt;U[]&gt;&amp; d) noexcept; (member only of the array default_delete specialization) </p>
<p>1) Constructs a std::default_delete object.<br />
2) Constructs a std::default_delete object from another std::default_delete object. This constructor will only participate in overload resolution if U* is implicitly convertible to T*.<br />
3) Constructs a std::default_delete&lt;U[]&gt; object from another std::default_delete&lt;U[]&gt; object. This constructor will only participate in overload resolution if U(*)[] is implicitly convertible to T(*)[].</p>
<h2>Parameters</h2>
<p>d &#8211; a deleter to copy from</p>
<h2>Notes</h2>
<p>The converting_constructor template of std::default_delete makes possible the implicit conversion from std::unique_ptr&lt;Derived&gt; to std::unique_ptr&lt;Base&gt;.<br />
&nbsp;std::default_delete::operator()<br />
1) Calls delete (primary template) or delete[] (array specialization) on ptr <i>(until C++17)</i><br />
2) Defined as deleted<br />
1) Calls delete on ptr <i>(since C++17)</i><br />
2) Calls delete[] on ptr. This function will only participate in overload resolution if U(*)[] is implicitly convertible to T(*)[].<br />
In any case, if U is an incomplete type, the program is ill-formed. </p>
<h2>Parameters</h2>
<p>ptr &#8211; an object or array to delete</p>
<h2>Exceptions</h2>
<p>No exception guarantees. </p>
<p>Invoking over Incomplete Types </p>
<p>At the point in the code the operator() is called, the type must be complete. In some implementations a static_assert is used to make sure this is the case. The reason for this requirement is that calling delete on an incomplete type is undefined behavior in C++ if the complete class type has a nontrivial destructor or a deallocation function, as the compiler has no way of knowing whether such functions exist and must be invoked.</p>
<h2>Example</h2>
<p>// Run this code </p>
<pre><code>#include &lt;memory&gt;

#include &lt;vector&gt;

#include &lt;algorithm&gt;
int main()

{

    //    {

    //        std::shared_ptr&lt;int&gt; shared_bad(new int[10]);

    //    } // the destructor calls delete, undefined behavior
    {
        std::shared_ptr&lt;int&gt; shared_good(new int[10], std::default_delete&lt;int[]&gt;

                                         ());
    } // the destructor calls delete[], ok
    {
        std::unique_ptr&lt;int&gt; ptr(new int(5));
    } // unique_ptr&lt;int&gt; uses default_delete&lt;int&gt;
    {
        std::unique_ptr&lt;int[]&gt; ptr(new int[10]);
    } // unique_ptr&lt;int[]&gt; uses default_delete&lt;int[]&gt;
      // default_delete can be used anywhere a delete functor is needed
    std::vector&lt;int *&gt; v;
    for (int n = 0; n &lt; 100; ++n)
        v.push_back(new int(n));
    std::for_each(v.begin(), v.end(), std::default_delete&lt;int&gt;());
}
</code></pre>
<h2>See also</h2>
<p>unique_ptr smart pointer with unique object ownership semantics<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(class template)</i><br />
<i>(C++11)</i> </p>
