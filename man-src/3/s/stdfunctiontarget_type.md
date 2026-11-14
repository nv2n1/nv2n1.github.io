---
title: "stdfunctiontarget_type(3)"
name: "stdfunctiontarget_type"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdfunctiontarget_type/"
---

std::function&lt;R(Args...)&gt;::target_type - std::function&lt;R(Args...)&gt;::target_type

<h2>Synopsis</h2>

<pre><code>const std::type_info &amp;target_type() const noexcept;
(since C++ 11)</code></pre> 
Returns the type of the stored function. 

<h2>Parameters</h2>

<i>(none)</i>

<h2>Return value</h2>

typeid(T) if the stored function has type T, otherwise typeid(void) 

<h2>Example</h2>

// Run this code <pre><code>#include &lt;functional&gt;

#include &lt;iostream&gt;
int f(int a)
{
    return -a;
}

int main()

{
    // fn1 and fn2 have the same type, but their targets do not
    std::function&lt;int(int)&gt; fn1(f),
        fn2([](int a) { return -a; });
    std::cout &lt;&lt; fn1.target_type().name() &lt;&lt; '\n'
              &lt;&lt; fn2.target_type().name() &lt;&lt; '\n';
}
</code></pre>

<h2>Possible output:</h2>

&nbsp;<wbr>&nbsp;int (*)(int) 
&nbsp;<wbr>&nbsp;main::$_0

<h2>See also</h2>

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;obtains a pointer to the stored target 
target <i>(public member function)</i> 
