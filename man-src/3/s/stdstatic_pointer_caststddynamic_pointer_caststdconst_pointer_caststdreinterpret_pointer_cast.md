---
title: "stdstatic_pointer_caststddynamic_pointer_caststdconst_pointer_caststdreinterpret_pointer_cast(3)"
name: "stdstatic_pointer_caststddynamic_pointer_caststdconst_pointer_caststdreinterpret_pointer_cast"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdstatic_pointer_caststddynamic_pointer_caststdconst_pointer_caststdreinterpret_pointer_cast/"
description: "std::static_pointer_cast,std::dynamic_pointer_cast,std::const_pointer_cast,std::reinterpret_pointer_cast – std::static_pointer_cast,std::dynamic_pointer_cast,std::const_pointer_cast,std::reinterpre..."
---

<p>std::static_pointer_cast,std::dynamic_pointer_cast,std::const_pointer_cast,std::reinterpret_pointer_cast &#8211; std::static_pointer_cast,std::dynamic_pointer_cast,std::const_pointer_cast,std::reinterpret_pointer_cast</p>
<h2>Synopsis</h2>
<pre><code>Defined in header&lt;memory&gt;

    template &lt;class T, class U&gt;
    (1)(since C++ 11)

        std::shared_ptr&lt;T&gt; static_pointer_cast(const std::shared_ptr&lt;U&gt; &amp;r) noexcept;

template &lt;class T, class U&gt;
(2)(since C++ 20)

    std::shared_ptr&lt;T&gt; static_pointer_cast(std::shared_ptr&lt;U&gt; &amp;&amp;r) noexcept;

template &lt;class T, class U&gt;
(3)(since C++ 11)

    std::shared_ptr&lt;T&gt; dynamic_pointer_cast(const std::shared_ptr&lt;U&gt; &amp;r) noexcept;

template &lt;class T, class U&gt;
(4)(since C++ 20)

    std::shared_ptr&lt;T&gt; dynamic_pointer_cast(std::shared_ptr&lt;U&gt; &amp;&amp;r) noexcept;

template &lt;class T, class U&gt;
(5)(since C++ 11)

    std::shared_ptr&lt;T&gt; const_pointer_cast(const std::shared_ptr&lt;U&gt; &amp;r) noexcept;

template &lt;class T, class U&gt;
(6)(since C++ 20)

    std::shared_ptr&lt;T&gt; const_pointer_cast(std::shared_ptr&lt;U&gt; &amp;&amp;r) noexcept;

template &lt;class T, class U&gt;
(7)(since C++ 17)

    std::shared_ptr&lt;T&gt; reinterpret_pointer_cast(const std::shared_ptr&lt;U&gt; &amp;r) noexcept;

template &lt;class T, class U&gt;
(8)(since C++ 20)

    std::shared_ptr&lt;T&gt; reinterpret_pointer_cast(std::shared_ptr&lt;U&gt; &amp;&amp;r) noexcept;</code></pre>
<p>Creates a new instance of std::shared_ptr whose stored pointer is obtained from r&#8217;s stored pointer using a cast expression.<br />
If r is empty, so is the new shared_ptr (but its stored pointer is not necessarily null). Otherwise, the new shared_ptr will share ownership with the initial value of r, except that it is empty if the dynamic_cast performed by dynamic_pointer_cast returns a null pointer.<br />
Let Y be typename std::shared_ptr&lt;T&gt;::element_type, then the resulting std::shared_ptr&#8217;s stored pointer will be obtained by evaluating, respectively:<br />
1-2) static_cast&lt;Y*&gt;(r.get()).<br />
3-4) dynamic_cast&lt;Y*&gt;(r.get()) (If the result of the dynamic_cast is a null pointer value, the returned shared_ptr will be empty.)<br />
5-6) const_cast&lt;Y*&gt;(r.get()).<br />
7-8) reinterpret_cast&lt;Y*&gt;(r.get())<br />
The behavior of these functions is undefined unless the corresponding cast from U* to T* is well formed:<br />
1-2) The behavior is undefined unless static_cast&lt;T*&gt;((U*)nullptr) is well formed.<br />
3-4) The behavior is undefined unless dynamic_cast&lt;T*&gt;((U*)nullptr) is well formed.<br />
5-6) The behavior is undefined unless const_cast&lt;T*&gt;((U*)nullptr) is well formed.<br />
7-8) The behavior is undefined unless reinterpret_cast&lt;T*&gt;((U*)nullptr) is well formed.<br />
After calling the rvalue overloads (2,4,6,8), r is empty and r.get() == nullptr, except that r is not modified for dynamic_pointer_cast <code>(4)</code> if the dynamic_cast fails. <i>(since C++20)</i> </p>
<h2>Parameters</h2>
<p>r &#8211; The pointer to convert</p>
<h2>Notes</h2>
<p>The expressions std::shared_ptr&lt;T&gt;(static_cast&lt;T*&gt;(r.get())), std::shared_ptr&lt;T&gt;(dynamic_cast&lt;T*&gt;(r.get())) and std::shared_ptr&lt;T&gt;(const_cast&lt;T*&gt;(r.get())) might seem to have the same effect, but they all will likely result in undefined behavior, attempting to delete the same object twice! </p>
<h2>Possible implementation</h2>
<h2>First version</h2>
<p>&nbsp;<wbr>&nbsp;template&lt; class T, class U &gt;<br />
&nbsp;<wbr>&nbsp;std::shared_ptr&lt;T&gt; static_pointer_cast( const std::shared_ptr&lt;U&gt;&amp; r ) noexcept<br />
&nbsp;<wbr>&nbsp;{<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;auto p = static_cast&lt;typename std::shared_ptr&lt;T&gt;::element_type*&gt;(r.get());<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;return std::shared_ptr&lt;T&gt;(r, p);<br />
&nbsp;<wbr>&nbsp;}</p>
<h2>Second version</h2>
<p>&nbsp;<wbr>&nbsp;template&lt; class T, class U &gt;<br />
&nbsp;<wbr>&nbsp;std::shared_ptr&lt;T&gt; dynamic_pointer_cast( const std::shared_ptr&lt;U&gt;&amp; r ) noexcept<br />
&nbsp;<wbr>&nbsp;{<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;if (auto p = dynamic_cast&lt;typename std::shared_ptr&lt;T&gt;::element_type*&gt;(r.get())) {<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;return std::shared_ptr&lt;T&gt;(r, p);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;} else {<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;return std::shared_ptr&lt;T&gt;();<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;}<br />
&nbsp;<wbr>&nbsp;} </p>
<p>Third version </p>
<p>&nbsp;<wbr>&nbsp;template&lt; class T, class U &gt;<br />
&nbsp;<wbr>&nbsp;std::shared_ptr&lt;T&gt; const_pointer_cast( const std::shared_ptr&lt;U&gt;&amp; r ) noexcept<br />
&nbsp;<wbr>&nbsp;{<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;auto p = const_cast&lt;typename std::shared_ptr&lt;T&gt;::element_type*&gt;(r.get());<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;return std::shared_ptr&lt;T&gt;(r, p);<br />
&nbsp;<wbr>&nbsp;} </p>
<p>Fourth version </p>
<p>&nbsp;<wbr>&nbsp;template&lt; class T, class U &gt;<br />
&nbsp;<wbr>&nbsp;std::shared_ptr&lt;T&gt; reinterpret_pointer_cast( const std::shared_ptr&lt;U&gt;&amp; r ) noexcept<br />
&nbsp;<wbr>&nbsp;{<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;auto p = reinterpret_cast&lt;typename std::shared_ptr&lt;T&gt;::element_type*&gt;(r.get());<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;return std::shared_ptr&lt;T&gt;(r, p);<br />
&nbsp;<wbr>&nbsp;}</p>
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
<p>&nbsp;<wbr>&nbsp;Base pointer says: I am base!<br />
&nbsp;<wbr>&nbsp;Derived pointer says: I am derived!<br />
&nbsp;<wbr>&nbsp;Base pointer to derived says: I am derived!<br />
&nbsp;<wbr>&nbsp;Downcasted pointer says: I am derived!<br />
&nbsp;<wbr>&nbsp;Pointers to underlying derived: 3</p>
<h2>See also</h2>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;constructs new shared_ptr<br />
constructor <i>(public member function)</i> </p>
