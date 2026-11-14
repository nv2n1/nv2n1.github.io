---
title: "stdferaiseexcept(3)"
name: "stdferaiseexcept"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdferaiseexcept/"
---

std::feraiseexcept - std::feraiseexcept

<h2>Synopsis</h2>

Defined in header &lt;cfenv&gt; 
int feraiseexcept( int excepts ); <i>(since C++11)</i> 
Attempts to raise all floating point exceptions listed in excepts (a bitwise OR of the floating_point_exception_macros). If one of the exceptions is FE_OVERFLOW or FE_UNDERFLOW, this function may additionally raise FE_INEXACT. The order in which the exceptions are raised is unspecified, except that FE_OVERFLOW and FE_UNDERFLOW are always raised before FE_INEXACT. 

<h2>Parameters</h2>

excepts - bitmask listing the exception flags to raise

<h2>Return value</h2>

0 if all listed exceptions were raised, non-zero value otherwise. 

<h2>Example</h2>

// Run this code <pre><code>#include &lt;iostream&gt;

#include &lt;cfenv&gt;</code></pre> 
&nbsp;<wbr>&nbsp;#pragma STDC FENV_ACCESS ON <pre><code>int main()

{
    std::feclearexcept(FE_ALL_EXCEPT);
    int r = std::feraiseexcept(FE_UNDERFLOW | FE_DIVBYZERO);
    std::cout &lt;&lt; &quot;Raising divbyzero and underflow simultaneously &quot;
              &lt;&lt; (r ? &quot;fails&quot; : &quot;succeeds&quot;) &lt;&lt; &quot; and results in\n&quot;;
    int e = std::fetestexcept(FE_ALL_EXCEPT);
    if (e &amp; FE_DIVBYZERO) {
        std::cout &lt;&lt; &quot;division by zero\n&quot;;
    }
    if (e &amp; FE_INEXACT) {
        std::cout &lt;&lt; &quot;inexact\n&quot;;
    }
    if (e &amp; FE_INVALID) {
        std::cout &lt;&lt; &quot;invalid\n&quot;;
    }
    if (e &amp; FE_UNDERFLOW) {
        std::cout &lt;&lt; &quot;underflow\n&quot;;
    }
    if (e &amp; FE_OVERFLOW) {
        std::cout &lt;&lt; &quot;overflow\n&quot;;
    }
}
</code></pre>

<h2>Output:</h2>

&nbsp;<wbr>&nbsp;Raising divbyzero and underflow simultaneously succeeds and results in 
&nbsp;<wbr>&nbsp;division by zero 
&nbsp;<wbr>&nbsp;underflow

<h2>See also</h2>

feclearexcept clears the specified floating-point status flags 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function)</i> 
<i>(C++11)</i> 
fetestexcept determines which of the specified floating-point status flags are set 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function)</i> 
<i>(C++11)</i> 
