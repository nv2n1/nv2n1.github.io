---
title: "stdabsstdlabsstdllabsstdimaxabs(3)"
name: "stdabsstdlabsstdllabsstdimaxabs"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdabsstdlabsstdllabsstdimaxabs/"
---

std::abs,std::labs,std::llabs,std::imaxabs - std::abs,std::labs,std::llabs,std::imaxabs

<h2>Synopsis</h2>

Defined in header &lt;cstdlib&gt; 
Defined in header &lt;cmath&gt; <i>(since C++17)</i> 
int abs( int n ); 
long abs( long n ); 
long long abs( long long n ); <i>(since C++11)</i> 
Defined in header &lt;cstdlib&gt; 
long labs( long n ); 
long long llabs( long long n ); <i>(since C++11)</i> 
Defined in header &lt;cinttypes&gt; 
std::intmax_t abs( std::intmax_t n ); <i>(since C++11)</i> 
std::intmax_t imaxabs( std::intmax_t n ); <i>(since C++11)</i> 
Computes the absolute value of an integer number. The behavior is undefined if the result cannot be represented by the return type. 
If std::abs is called with an argument of type X such that std::is_unsigned&lt;X&gt;::value is true and X cannot be converted to int by integral_promotion, the program is ill-formed. <i>(since C++17)</i> 

<h2>Parameters</h2>

n - integer value

<h2>Return value</h2>

The absolute value of n (i.e. |n|), if it is representable. 

<h2>Notes</h2>

In 2's complement systems, the absolute value of the most-negative value is out of range, e.g. for 32-bit 2's complement type int, INT_MIN is -2147483648, but the would-be result 2147483648 is greater than INT_MAX, which is 2147483647. 

<h2>Example</h2>

// Run this code <pre><code>#include &lt;iostream&gt;

#include &lt;cstdlib&gt;

#include &lt;climits&gt;
int main()

{
    std::cout &lt;&lt; &quot;abs(+3) = &quot; &lt;&lt; std::abs(3) &lt;&lt; '\n'
              &lt;&lt; &quot;abs(-3) = &quot; &lt;&lt; std::abs(-3) &lt;&lt; '\n';
    //  std::cout &lt;&lt; std::abs(INT_MIN); // undefined behavior on 2's complement systems
}
</code></pre>

<h2>Output:</h2>

&nbsp;<wbr>&nbsp;abs(+3) = 3 
&nbsp;<wbr>&nbsp;abs(-3) = 3

<h2>See also</h2>

abs(float) 
fabs 
fabsf 
fabsl absolute value of a floating point value (|x|) 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function)</i> 
<i>(C++11)</i> 
<i>(C++11)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;returns the magnitude of a complex number 
abs(std::complex) <i>(function template)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;applies the function std::abs to each element of valarray 
abs(std::valarray) <i>(function template)</i> 
