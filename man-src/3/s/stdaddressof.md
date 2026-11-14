---
title: "stdaddressof(3)"
name: "stdaddressof"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdaddressof/"
description: "std::addressof – std::addressof"
---

<p>std::addressof &#8211; std::addressof</p>
<h2>Synopsis</h2>
<pre><code>Defined in header&lt;memory&gt;

    template &lt;class T&gt;
    (since C++ 11)

        T *addressof(T &amp;arg) noexcept;
(until C++ 17)

    template &lt;class T&gt;
    (1)(since C++ 17)

        constexpr T *addressof(T &amp;arg) noexcept;

template &lt;class T&gt;
(2)(since C++ 17)

    const T *addressof(const T &amp;&amp;) = delete;</code></pre>
<p>1) Obtains the actual address of the object or function arg, even in presence of overloaded operator&amp;<br />
2) Rvalue overload is deleted to prevent taking the address of const rvalues.<br />
The expression std::addressof(E) is a constant_subexpression, if E is an lvalue constant subexpression. <i>(since C++17)</i> </p>
<h2>Parameters</h2>
<p>arg &#8211; lvalue object or function</p>
<h2>Return value</h2>
<p>Pointer to arg. </p>
<h2>Possible implementation</h2>
<p>&nbsp;<wbr>&nbsp;template&lt; class T &gt;<br />
&nbsp;<wbr>&nbsp;T* addressof(T&amp; arg)<br />
&nbsp;<wbr>&nbsp;{<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;return reinterpret_cast&lt;T*&gt;(<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;&amp;const_cast&lt;char&amp;&gt;(<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;reinterpret_cast&lt;const volatile char&amp;&gt;(arg)));<br />
&nbsp;<wbr>&nbsp;} </p>
<p>Note: the above implementation is_oversimplified and is not constexpr (which requires compiler support).</p>
<h2>Example</h2>
<p>operator&amp; may be overloaded for a pointer wrapper class to obtain a pointer to pointer:<br />
 // Run this code </p>
<pre><code>#include &lt;iostream&gt;

#include &lt;memory&gt;
template &lt;class T&gt;

struct Ptr {
    T *pad; // add pad to show difference between 'this' and 'data'
    T *data;
    Ptr(T *arg)
        : pad(nullptr), data(arg)
    {
        std::cout &lt;&lt; &quot;Ctor this = &quot; &lt;&lt; this &lt;&lt; std::endl;
    }
    ~Ptr()
    {
        delete data;
    }
    T **operator&amp;()
    {
        return &amp;data;
    }
};
template &lt;class T&gt;

void f(Ptr&lt;T&gt; *p)

{
    std::cout &lt;&lt; &quot;Ptr   overload called with p = &quot; &lt;&lt; p &lt;&lt; '
';
}
void f(int **p)

{
    std::cout &lt;&lt; &quot;int** overload called with p = &quot; &lt;&lt; p &lt;&lt; '
';
}
int main()

{
    Ptr&lt;int&gt; p(new int(42));
    f(&amp;p);                // calls int** overload
    f(std::addressof(p)); // calls Ptr&lt;int&gt;* overload, (= this)
}
</code></pre>
<h2>Possible output:</h2>
<p>&nbsp;<wbr>&nbsp;Ctor this = 0x7fff59ae6e88<br />
&nbsp;<wbr>&nbsp;int** overload called with p = 0x7fff59ae6e90<br />
&nbsp;<wbr>&nbsp;Ptr overload called with p = 0x7fff59ae6e88</p>
<h2>See also</h2>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;the default allocator<br />
allocator <i>(class template)</i><br />
pointer_to obtains a dereferenceable pointer to its argument<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(public static member function of std::pointer_traits&lt;Ptr&gt;)</i><br />
<code>[static]</code> </p>
