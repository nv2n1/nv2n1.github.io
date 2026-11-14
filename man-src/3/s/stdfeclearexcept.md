---
title: "stdfeclearexcept(3)"
name: "stdfeclearexcept"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdfeclearexcept/"
---

std::feclearexcept - std::feclearexcept

<h2>Synopsis</h2>

Defined in header &lt;cfenv&gt; 
int feclearexcept( int excepts ); <i>(since C++11)</i> 
Attempts to clear the floating-point exceptions that are listed in the bitmask argument excepts, which is a bitwise OR of the floating_point_exception_macros. 

<h2>Parameters</h2>

excepts - bitmask listing the exception flags to clear

<h2>Return value</h2>

0 if all indicated exceptions were successfully cleared or if excepts is zero. Returns a non-zero value on error. 

<h2>Example</h2>

// Run this code <pre><code>#include &lt;iostream&gt;

#include &lt;cfenv&gt;

#include &lt;cmath&gt;</code></pre> 
&nbsp;<wbr>&nbsp;#pragma STDC FENV_ACCESS ON <pre><code>volatile double zero = 0.0; // volatile not needed where FENV_ACCESS is supported

volatile double one = 1.0; // volatile not needed where FENV_ACCESS is supported
int main()

{
    std::feclearexcept(FE_ALL_EXCEPT);
    std::cout &lt;&lt; &quot;1.0/0.0 = &quot; &lt;&lt; 1.0 / zero &lt;&lt; '\n';
    if (std::fetestexcept(FE_DIVBYZERO)) {
        std::cout &lt;&lt; &quot;division by zero reported\n&quot;;
    } else {
        std::cout &lt;&lt; &quot;divsion by zero not reported\n&quot;;
    }
    std::feclearexcept(FE_ALL_EXCEPT);
    std::cout &lt;&lt; &quot;1.0/10 = &quot; &lt;&lt; one / 10 &lt;&lt; '\n';
    if (std::fetestexcept(FE_INEXACT)) {
        std::cout &lt;&lt; &quot;inexact result reported\n&quot;;
    } else {
        std::cout &lt;&lt; &quot;inexact result not reported\n&quot;;
    }
    std::feclearexcept(FE_ALL_EXCEPT);
    std::cout &lt;&lt; &quot;sqrt(-1) = &quot; &lt;&lt; std::sqrt(-1) &lt;&lt; '\n';
    if (std::fetestexcept(FE_INVALID)) {
        std::cout &lt;&lt; &quot;invalid result reported\n&quot;;
    } else {
        std::cout &lt;&lt; &quot;invalid result not reported\n&quot;;
    }
}
</code></pre>

<h2>Output:</h2>

&nbsp;<wbr>&nbsp;1.0/0.0 = inf 
&nbsp;<wbr>&nbsp;division by zero reported 
&nbsp;<wbr>&nbsp;1.0/10 = 0.1 
&nbsp;<wbr>&nbsp;inexact result reported 
&nbsp;<wbr>&nbsp;sqrt(-1) = -nan 
&nbsp;<wbr>&nbsp;invalid result reported

<h2>See also</h2>

fetestexcept determines which of the specified floating-point status flags are set 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function)</i> 
<i>(C++11)</i> 
