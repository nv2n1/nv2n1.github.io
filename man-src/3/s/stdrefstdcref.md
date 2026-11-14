---
title: "stdrefstdcref(3)"
name: "stdrefstdcref"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdrefstdcref/"
---

std::ref,std::cref - std::ref,std::cref

<h2>Synopsis</h2>

<pre><code>Defined in header&lt;functional&gt;

    template &lt;class T&gt;
    (1)(since C++ 11)

        std::reference_wrapper&lt;T&gt; ref(T &amp;t) noexcept;

template &lt;class T&gt;
(2)(since C++ 11)

    std::reference_wrapper&lt;T&gt; ref(std::reference_wrapper&lt;T&gt; t) noexcept;

template &lt;class T&gt;
(3)(since C++ 11)

    void ref(const T &amp;&amp;) = delete;

template &lt;class T&gt;
(4)(since C++ 11)

    std::reference_wrapper&lt;const T&gt; cref(const T &amp;t) noexcept;

template &lt;class T&gt;
(5)(since C++ 11)

    std::reference_wrapper&lt;const T&gt; cref(std::reference_wrapper&lt;T&gt; t) noexcept;

template &lt;class T&gt;
(6)(since C++ 11)

    void cref(const T &amp;&amp;) = delete;</code></pre> 
Function templates ref and cref are helper functions that generate an object of type std::reference_wrapper, using template_argument_deduction to determine the template argument of the result. 
T may be an incomplete type. <i>(since C++20)</i> 

<h2>Parameters</h2>

t - lvalue reference to object that needs to be wrapped or an instance of std::reference_wrapper

<h2>Return value</h2>

1) std::reference_wrapper&lt;T&gt;(t) 
2) ref(t.get()) 
4) std::reference_wrapper&lt;const T&gt;(t) 
5) cref(t.get()) 
3,6) rvalue reference wrapper is deleted. 

<h2>Example</h2>

// Run this code <pre><code>#include &lt;functional&gt;

#include &lt;iostream&gt;
void f(int &amp;n1, int &amp;n2, const int &amp;n3)

{
    std::cout &lt;&lt; &quot;In function: &quot; &lt;&lt; n1 &lt;&lt; ' ' &lt;&lt; n2 &lt;&lt; ' ' &lt;&lt; n3 &lt;&lt; '\n';
    ++n1; // increments the copy of n1 stored in the function object
    ++n2; // increments the main()'s n2
    // ++n3; // compile error
}
int main()

{
    int n1 = 1, n2 = 2, n3 = 3;
    std::function&lt;void()&gt; bound_f = std::bind(f, n1, std::ref(n2), std::cref(n3));
    n1 = 10;
    n2 = 11;
    n3 = 12;
    std::cout &lt;&lt; &quot;Before function: &quot; &lt;&lt; n1 &lt;&lt; ' ' &lt;&lt; n2 &lt;&lt; ' ' &lt;&lt; n3 &lt;&lt; '\n';
    bound_f();
    std::cout &lt;&lt; &quot;After function: &quot; &lt;&lt; n1 &lt;&lt; ' ' &lt;&lt; n2 &lt;&lt; ' ' &lt;&lt; n3 &lt;&lt; '\n';
}
</code></pre>

<h2>Output:</h2>

&nbsp;<wbr>&nbsp;Before function: 10 11 12 
&nbsp;<wbr>&nbsp;In function: 1 11 12 
&nbsp;<wbr>&nbsp;After function: 10 12 12

<h2>See also</h2>

reference_wrapper CopyConstructible and CopyAssignable reference wrapper 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(class template)</i> 
<i>(C++11)</i> 
