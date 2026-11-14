---
title: "stdfunctiontarget(3)"
name: "stdfunctiontarget"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdfunctiontarget/"
---

std::function&lt;R(Args...)&gt;::target - std::function&lt;R(Args...)&gt;::target

<h2>Synopsis</h2>

<pre><code>template &lt;class T&gt;
(1)(since C++ 11)

    T *target() noexcept;

template &lt;class T&gt;
(2)(since C++ 11)

    const T *target() const noexcept;</code></pre> 
Returns a pointer to the stored callable function target. 

<h2>Parameters</h2>

<i>(none)</i>

<h2>Return value</h2>

A pointer to the stored function if target_type() == typeid(T), otherwise a null pointer. 

<h2>Example</h2>

// Run this code <pre><code>#include &lt;functional&gt;

#include &lt;iostream&gt;
int f(int, int)
{
    return 1;
}

int g(int, int)
{
    return 2;
}

void test(std::function&lt;int(int, int)&gt; const &amp;arg)

{
    std::cout &lt;&lt; &quot;test function: &quot;;
    if (arg.target&lt;std::plus&lt;int&gt;&gt;())
        std::cout &lt;&lt; &quot;it is plus\n&quot;;
    if (arg.target&lt;std::minus&lt;int&gt;&gt;())
        std::cout &lt;&lt; &quot;it is minus\n&quot;;
    int (*const *ptr)(int, int) = arg.target&lt;int (*)(int, int)&gt;();
    if (ptr &amp;&amp; *ptr == f)
        std::cout &lt;&lt; &quot;it is the function f\n&quot;;
    if (ptr &amp;&amp; *ptr == g)
        std::cout &lt;&lt; &quot;it is the function g\n&quot;;
}
int main()

{
    test(std::function&lt;int(int, int)&gt;(std::plus&lt;int&gt;()));
    test(std::function&lt;int(int, int)&gt;(std::minus&lt;int&gt;()));
    test(std::function&lt;int(int, int)&gt;(f));
    test(std::function&lt;int(int, int)&gt;(g));
}
</code></pre>

<h2>Output:</h2>

&nbsp;<wbr>&nbsp;test function: it is plus 
&nbsp;<wbr>&nbsp;test function: it is minus 
&nbsp;<wbr>&nbsp;test function: it is the function f 
&nbsp;<wbr>&nbsp;test function: it is the function g

<h2>See also</h2>

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;obtains the typeid of the stored target 
target_type <i>(public member function)</i> 
