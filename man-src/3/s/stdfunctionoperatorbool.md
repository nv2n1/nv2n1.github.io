---
title: "stdfunctionoperatorbool(3)"
name: "stdfunctionoperatorbool"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdfunctionoperatorbool/"
---

std::function&lt;R(Args...)&gt;::operatorbool - std::function&lt;R(Args...)&gt;::operatorbool

<h2>Synopsis</h2>

explicit operator bool() const noexcept; <i>(since C++11)</i> 
Checks whether *this stores a callable function target, i.e. is not empty. 

<h2>Parameters</h2>

<i>(none)</i>

<h2>Return value</h2>

true if *this stores a callable function target, false otherwise. 

<h2>Example</h2>

// Run this code <pre><code>#include &lt;functional&gt;

#include &lt;iostream&gt;
void sampleFunction()

{
    std::cout &lt;&lt; &quot;This is the sample function!\n&quot;;
}
void checkFunc(std::function&lt;void()&gt; &amp;func)

{
    // Use operator bool to determine if callable target is available.
    if (func) {
        std::cout &lt;&lt; &quot;Function is not empty! Calling function.\n&quot;;
        func();
    } else {
        std::cout &lt;&lt; &quot;Function is empty. Nothing to do.\n&quot;;
    }
}
int main()

{
    std::function&lt;void()&gt; f1;
    std::function&lt;void()&gt; f2(sampleFunction);
    std::cout &lt;&lt; &quot;f1: &quot;;
    checkFunc(f1);
    std::cout &lt;&lt; &quot;f2: &quot;;
    checkFunc(f2);
}
</code></pre>

<h2>Output:</h2>

&nbsp;<wbr>&nbsp;f1: Function is empty. Nothing to do. 
&nbsp;<wbr>&nbsp;f2: Function is not empty! Calling function. 
&nbsp;<wbr>&nbsp;This is the sample function!
