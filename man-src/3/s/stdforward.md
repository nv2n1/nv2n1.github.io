---
title: "stdforward(3)"
name: "stdforward"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdforward/"
description: "std::forward – std::forward"
---

<p>std::forward &#8211; std::forward</p>
<h2>Synopsis</h2>
<pre><code>Defined in header &lt;utility&gt;

template&lt; class T &gt;                                                            (1) (since C++11)

T&amp;&amp; forward( typename std::remove_reference&lt;T&gt;::type&amp; t ) noexcept;                (until C++14)

template&lt; class T &gt;                                                            (1) (since C++14)

constexpr T&amp;&amp; forward( typename std::remove_reference&lt;T&gt;::type&amp; t ) noexcept;

template&lt; class T &gt;                                                            (2) (since C++11)

T&amp;&amp; forward( typename std::remove_reference&lt;T&gt;::type&amp;&amp; t ) noexcept;               (until C++14)

template&lt; class T &gt;                                                            (2) (since C++14)

constexpr T&amp;&amp; forward( typename std::remove_reference&lt;T&gt;::type&amp;&amp; t ) noexcept;</code></pre>
<p>1) Forwards lvalues as either lvalues or as rvalues, depending on T<br />
When t is a forwarding_reference (a function argument that is declared as an rvalue reference to a cv-unqualified function template parameter), this overload forwards the argument to another function with the value_category it had when passed to the calling function.<br />
For example, if used in wrapper such as the following, the template behaves as described below: template &lt;class T&gt;</p>
<p>void wrapper(T &amp;&amp;arg)</p>
<p>{<br />
    // arg is always lvalue<br />
    foo(std::forward&lt;T&gt;(arg)); // Forward as lvalue or as rvalue, depending on T<br />
}</p>
<p>* If a call to wrapper() passes an rvalue std::string, then T is deduced to std::string (not std::string&amp;, const std::string&amp;, or std::string&amp;&amp;), and std::forward ensures that an rvalue reference is passed to foo.<br />
* If a call to wrapper() passes a const lvalue std::string, then T is deduced to const std::string&amp;, and std::forward ensures that a const lvalue reference is passed to foo.<br />
* If a call to wrapper() passes a non-const lvalue std::string, then T is deduced to std::string&amp;, and std::forward ensures that a non-const lvalue reference is passed to foo.<br />
2) Forwards rvalues as rvalues and prohibits forwarding of rvalues as lvalues<br />
This overload makes it possible to forward a result of an expression (such as function call), which may be rvalue or lvalue, as the original value category of a forwarding reference argument.<br />
For example, if a wrapper does not just forward its argument, but calls a member function on the argument, and forwards its result: // transforming wrapper</p>
<p>template &lt;class T&gt;</p>
<p>void wrapper(T &amp;&amp;arg)</p>
<p>{<br />
    foo(forward&lt;decltype(forward&lt;T&gt;(arg).get())&gt;(forward&lt;T&gt;(arg).get()));<br />
}<br />
where the type of arg may be struct Arg</p>
<p>{<br />
    int i = 1;<br />
    int get() &amp;&amp;<br />
    {<br />
        return i;<br />
    } // call to this overload is rvalue<br />
    int &amp;get() &amp;<br />
    {<br />
        return i;<br />
    } // call to this overload is lvalue<br />
};<br />
Attempting to forward an rvalue as an lvalue, such as by instantiating the form <code>(2)</code> with lvalue reference type T, is a compile-time error. </p>
<h2>Notes</h2>
<p>See template_argument_deduction for the special rules behind forwarding references (T&amp;&amp; used as a function parameter) and forwarding_references for other detail. </p>
<h2>Parameters</h2>
<p>t &#8211; the object to be forwarded</p>
<h2>Return value</h2>
<p>static_cast&lt;T&amp;&amp;&gt;(t) </p>
<h2>Example</h2>
<p>This example demonstrates perfect forwarding of the parameter(s) to the argument of the constructor of class T. Also, perfect forwarding of parameter packs is demonstrated.<br />
 // Run this code </p>
<pre><code>#include &lt;iostream&gt;

#include &lt;memory&gt;

#include &lt;utility&gt;
struct A {
    A(int &amp;&amp;n)
    {
        std::cout &lt;&lt; &quot;rvalue overload, n=&quot; &lt;&lt; n &lt;&lt; &quot;
&quot;;
    }
    A(int &amp;n)
    {
        std::cout &lt;&lt; &quot;lvalue overload, n=&quot; &lt;&lt; n &lt;&lt; &quot;
&quot;;
    }
};
class B
{

  public:
    template &lt;class T1, class T2, class T3&gt;
    B(T1 &amp;&amp;t1, T2 &amp;&amp;t2, T3 &amp;&amp;t3)
        : a1_{std::forward&lt;T1&gt;(t1)},
          a2_{std::forward&lt;T2&gt;(t2)},
          a3_{std::forward&lt;T3&gt;(t3)}
    {
    }

  private:
    A a1_, a2_, a3_;
};
template &lt;class T, class U&gt;

std::unique_ptr&lt;T&gt; make_unique1(U &amp;&amp;u)

{
    return std::unique_ptr&lt;T&gt;(new T(std::forward&lt;U&gt;(u)));
}
template &lt;class T, class... U&gt;

std::unique_ptr&lt;T&gt; make_unique2(U &amp;&amp;...u)

{
    return std::unique_ptr&lt;T&gt;(new T(std::forward&lt;U&gt;(u)...));
}
int main()

{
    auto p1 = make_unique1&lt;A&gt;(2); // rvalue
    int i = 1;
    auto p2 = make_unique1&lt;A&gt;(i); // lvalue
    std::cout &lt;&lt; &quot;B
&quot;;
    auto t = make_unique2&lt;B&gt;(2, i, 3);
}
</code></pre>
<h2>Output:</h2>
<p>&nbsp;<wbr>&nbsp;rvalue overload, n=2<br />
&nbsp;<wbr>&nbsp;lvalue overload, n=1<br />
&nbsp;<wbr>&nbsp;B<br />
&nbsp;<wbr>&nbsp;rvalue overload, n=2<br />
&nbsp;<wbr>&nbsp;lvalue overload, n=1<br />
&nbsp;<wbr>&nbsp;rvalue overload, n=3</p>
<h2>Complexity</h2>
<p>Constant</p>
<h2>See also</h2>
<p>move obtains an rvalue reference<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function template)</i><br />
<i>(C++11)</i><br />
move_if_noexcept obtains an rvalue reference if the move constructor does not throw<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function template)</i><br />
<i>(C++11)</i> </p>
