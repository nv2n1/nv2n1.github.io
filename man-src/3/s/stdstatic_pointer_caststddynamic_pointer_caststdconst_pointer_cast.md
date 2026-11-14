---
title: "stdstatic_pointer_caststddynamic_pointer_caststdconst_pointer_cast(3)"
name: "stdstatic_pointer_caststddynamic_pointer_caststdconst_pointer_cast"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdstatic_pointer_caststddynamic_pointer_caststdconst_pointer_cast/"
description: "std::static_pointer_cast,std::dynamic_pointer_cast,std::const_pointer_cast, – std::static_pointer_cast,std::dynamic_pointer_cast,std::const_pointer_cast,"
---

<p>std::static_pointer_cast,std::dynamic_pointer_cast,std::const_pointer_cast, &#8211; std::static_pointer_cast,std::dynamic_pointer_cast,std::const_pointer_cast,</p>
<h2>Synopsis</h2>
<pre><code>Defined in header&lt;memory&gt;

    template &lt;class T, class U&gt;

    std::shared_ptr&lt;T&gt; static_pointer_cast(const std::shared_ptr&lt;U&gt; &amp;(1)(since C++ 11)

                                               r) noexcept;

template &lt;class T, class U&gt;

std::shared_ptr&lt;T&gt; static_pointer_cast(std::shared_ptr&lt;U&gt; &amp;&amp;r)(2)(since C++ 20)

    noexcept;

template &lt;class T, class U&gt;

std::shared_ptr&lt;T&gt; dynamic_pointer_cast(const std::shared_ptr&lt;U&gt; &amp;(3)(since C++ 11)

                                            r) noexcept;

template &lt;class T, class U&gt;

std::shared_ptr&lt;T&gt; dynamic_pointer_cast(std::shared_ptr&lt;U&gt; &amp;&amp;r)(4)(since C++ 20)

    noexcept;

template &lt;class T, class U&gt;

std::shared_ptr&lt;T&gt; const_pointer_cast(const std::shared_ptr&lt;U&gt; &amp;r(5)(since C++ 11)

                                          ) noexcept;

template &lt;class T, class U&gt;

std::shared_ptr&lt;T&gt; const_pointer_cast(std::shared_ptr&lt;U&gt; &amp;&amp;r)(6)(since C++ 20)

    noexcept;

template &lt;class T, class U&gt;

std::shared_ptr&lt;T&gt; reinterpret_pointer_cast(const(7)(since C++ 17)

                                                std::shared_ptr&lt;U&gt; &amp;r) noexcept;

template &lt;class T, class U&gt;

std::shared_ptr&lt;T&gt; reinterpret_pointer_cast(std::shared_ptr&lt;U&gt; &amp;&amp; (8)(since C++ 20)

                                                                      r) noexcept;</code></pre>
<p>Creates a new instance of std::shared_ptr whose stored pointer is obtained from r&#8217;s<br />
stored pointer using a cast expression.<br />
If r is empty, so is the new shared_ptr&nbsp;<wbr>(but its stored pointer is not necessarily<br />
null). Otherwise, the new shared_ptr will share ownership with the initial value of<br />
r, except that it is empty if the dynamic_cast performed by dynamic_pointer_cast<br />
returns a null pointer.<br />
Let Y be typename std::shared_ptr&lt;T&gt;::element_type, then the resulting<br />
std::shared_ptr&#8217;s stored pointer will be obtained by evaluating, respectively:<br />
1-2)&nbsp;<wbr>static_cast&lt;Y*&gt;(r.get()).<br />
3-4)&nbsp;<wbr>dynamic_cast&lt;Y*&gt;(r.get())&nbsp;<wbr>(If the result of the dynamic_cast is a null pointer<br />
value, the returned shared_ptr will be empty.)<br />
5-6)&nbsp;<wbr>const_cast&lt;Y*&gt;(r.get()).<br />
7-8)&nbsp;<wbr>reinterpret_cast&lt;Y*&gt;(r.get())<br />
The behavior of these functions is undefined unless the corresponding cast from U*<br />
to T*&nbsp;<wbr>is well formed:<br />
1-2)&nbsp;<wbr>The behavior is undefined unless static_cast&lt;T*&gt;((U*)nullptr)&nbsp;<wbr>is well formed.<br />
3-4)&nbsp;<wbr>The behavior is undefined unless dynamic_cast&lt;T*&gt;((U*)nullptr)&nbsp;<wbr>is well formed.<br />
5-6)&nbsp;<wbr>The behavior is undefined unless const_cast&lt;T*&gt;((U*)nullptr)&nbsp;<wbr>is well formed.<br />
7-8)&nbsp;<wbr>The behavior is undefined unless reinterpret_cast&lt;T*&gt;((U*)nullptr)&nbsp;<wbr>is well<br />
formed.<br />
After calling the rvalue overloads&nbsp;<wbr>(2,4,6,8), r is empty and r.get()<br />
==&nbsp;<wbr>nullptr, except that r is not modified for dynamic_pointer_cast&nbsp;<wbr><code>(4)</code>&nbsp;<wbr><i>(since C++20)</i><br />
if the dynamic_cast fails. </p>
<h2>Parameters</h2>
<p>r &#8211; The pointer to convert</p>
<h2>Notes</h2>
<p>The expressions std::shared_ptr&lt;T&gt;(static_cast&lt;T*&gt;(r.get())),<br />
std::shared_ptr&lt;T&gt;(dynamic_cast&lt;T*&gt;(r.get()))&nbsp;<wbr>and<br />
std::shared_ptr&lt;T&gt;(const_cast&lt;T*&gt;(r.get()))&nbsp;<wbr>might seem to have the same effect, but<br />
they all will likely result in undefined behavior, attempting to delete the same<br />
object twice! </p>
<h2>Possible implementation</h2>
<h2>First version</h2>
<p>template&lt;&nbsp;<wbr>class T, class U&nbsp;<wbr>&gt;<br />
std::shared_ptr&lt;T&gt;&nbsp;<wbr>static_pointer_cast(&nbsp;<wbr>const std::shared_ptr&lt;U&gt;&amp;&nbsp;<wbr>r&nbsp;<wbr>)&nbsp;<wbr>noexcept<br />
{<br />
&nbsp;<wbr>auto p&nbsp;<wbr>=&nbsp;<wbr>static_cast&lt;typename std::shared_ptr&lt;T&gt;::element_type*&gt;(r.get());<br />
&nbsp;<wbr>return std::shared_ptr&lt;T&gt;(r, p);<br />
}</p>
<h2>Second version</h2>
<p>template&lt;&nbsp;<wbr>class T, class U&nbsp;<wbr>&gt;<br />
std::shared_ptr&lt;T&gt;&nbsp;<wbr>dynamic_pointer_cast(&nbsp;<wbr>const std::shared_ptr&lt;U&gt;&amp;&nbsp;<wbr>r&nbsp;<wbr>)&nbsp;<wbr>noexcept<br />
{<br />
&nbsp;<wbr>if&nbsp;<wbr>(auto p&nbsp;<wbr>=&nbsp;<wbr>dynamic_cast&lt;typename std::shared_ptr&lt;T&gt;::element_type*&gt;(r.get()))&nbsp;<wbr>{<br />
&nbsp;<wbr>&nbsp;<wbr>return std::shared_ptr&lt;T&gt;(r, p);<br />
&nbsp;<wbr>}&nbsp;<wbr>else&nbsp;<wbr>{<br />
&nbsp;<wbr>&nbsp;<wbr>return std::shared_ptr&lt;T&gt;();<br />
&nbsp;<wbr>}<br />
}<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Third version<br />
template&lt;&nbsp;<wbr>class T, class U&nbsp;<wbr>&gt;<br />
std::shared_ptr&lt;T&gt;&nbsp;<wbr>const_pointer_cast(&nbsp;<wbr>const std::shared_ptr&lt;U&gt;&amp;&nbsp;<wbr>r&nbsp;<wbr>)&nbsp;<wbr>noexcept<br />
{<br />
&nbsp;<wbr>auto p&nbsp;<wbr>=&nbsp;<wbr>const_cast&lt;typename std::shared_ptr&lt;T&gt;::element_type*&gt;(r.get());<br />
&nbsp;<wbr>return std::shared_ptr&lt;T&gt;(r, p);<br />
}<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Fourth version<br />
template&lt;&nbsp;<wbr>class T, class U&nbsp;<wbr>&gt;<br />
std::shared_ptr&lt;T&gt;&nbsp;<wbr>reinterpret_pointer_cast(&nbsp;<wbr>const std::shared_ptr&lt;U&gt;&amp;&nbsp;<wbr>r&nbsp;<wbr>)&nbsp;<wbr>noexcept<br />
{<br />
&nbsp;<wbr>auto p&nbsp;<wbr>=&nbsp;<wbr>reinterpret_cast&lt;typename std::shared_ptr&lt;T&gt;::element_type*&gt;(r.get());<br />
&nbsp;<wbr>return std::shared_ptr&lt;T&gt;(r, p);<br />
}</p>
<h2>Example</h2>
<p>// Run this code </p>
<pre><code>#include &lt;iostream&gt;

#include &lt;memory&gt;
struct Base

{
    int a;
    virtual void f() const
    {
        std::cout &lt;&lt; &quot;I am base!
&quot;;
    }
    virtual ~Base()
    {
    }
};
struct Derived : Base

{
    void f() const override
    {
        std::cout &lt;&lt; &quot;I am derived!
&quot;;
    }
    ~Derived()
    {
    }
};
int main()
{
    auto basePtr = std::make_shared&lt;Base&gt;();
    std::cout &lt;&lt; &quot;Base pointer says: &quot;;
    basePtr-&gt;f();
    auto derivedPtr = std::make_shared&lt;Derived&gt;();
    std::cout &lt;&lt; &quot;Derived pointer says: &quot;;
    derivedPtr-&gt;f();
    // static_pointer_cast to go up class hierarchy
    basePtr = std::static_pointer_cast&lt;Base&gt;(derivedPtr);
    std::cout &lt;&lt; &quot;Base pointer to derived says: &quot;;
    basePtr-&gt;f();
    // dynamic_pointer_cast to go down/across class hierarchy
    auto downcastedPtr = std::dynamic_pointer_cast&lt;Derived&gt;(basePtr);
    if (downcastedPtr) {

        std::cout &lt;&lt; &quot;Downcasted pointer says: &quot;;

        downcastedPtr-&gt;f();
    }
    // All pointers to derived share ownership
    std::cout &lt;&lt; &quot;Pointers to underlying derived: &quot;
              &lt;&lt; derivedPtr.use_count()
              &lt;&lt; &quot;
&quot;;
}
</code></pre>
<h2>Output:</h2>
<p>&nbsp;<wbr>Base pointer says: I am base!<br />
&nbsp;<wbr>Derived pointer says: I am derived!<br />
&nbsp;<wbr>Base pointer to derived says: I am derived!<br />
&nbsp;<wbr>Downcasted pointer says: I am derived!<br />
&nbsp;<wbr>Pointers to underlying derived: 3</p>
<h2>See also</h2>
<p>constructor&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>constructs new shared_ptr<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr><i>(public member function)</i> </p>
