---
title: "stdconjstdcomplex(3)"
name: "stdconjstdcomplex"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdconjstdcomplex/"
---

std::conj(std::complex) - std::conj(std::complex)

<h2>Synopsis</h2>

<pre><code>Defined in header&lt;complex&gt;

    template &lt;class T&gt;
    (until C++ 20)

        std::complex&lt;T&gt; conj(const std::complex&lt;T&gt; &amp;z);

template &lt;class T&gt;
(since C++ 20)

    constexpr std::complex&lt;T&gt; conj(const std::complex&lt;T&gt; &amp;z);

std::complex&lt;float&gt; conj(float z);

template &lt;class DoubleOrInteger&gt;
(1)(since C++ 11)

    std::complex&lt;double&gt; conj(DoubleOrInteger z);
(until C++ 20)

    std::complex&lt;long double&gt; conj(long double z);
(2)

    constexpr std::complex&lt;float&gt; conj(float z);

template &lt;class DoubleOrInteger&gt;
(since C++ 20)

    constexpr std::complex&lt;double&gt; conj(DoubleOrInteger z);

constexpr std::complex&lt;long double&gt; conj(long double z);</code></pre> 
1) Computes the complex_conjugate of z by reversing the sign of the imaginary part. 
2) Additional overloads are provided for float, double, long double, and all integer types, which are treated as complex numbers with zero imaginary component. <i>(since C++11)</i> 

<h2>Parameters</h2>

z - complex value

<h2>Return value</h2>

The complex conjugate of z 

<h2>Example</h2>

// Run this code <pre><code>#include &lt;iostream&gt;

#include &lt;complex&gt;
int main()

{
    std::complex&lt;double&gt; z(1, 2);
    std::cout &lt;&lt; &quot;The conjugate of &quot; &lt;&lt; z &lt;&lt; &quot; is &quot; &lt;&lt; std::conj(z) &lt;&lt; '\n'
              &lt;&lt; &quot;Their product is &quot; &lt;&lt; z * std::conj(z) &lt;&lt; '\n';
}
</code></pre>

<h2>Output:</h2>

&nbsp;<wbr>&nbsp;The conjugate of (1,2) is (1,-2) 
&nbsp;<wbr>&nbsp;Their product is (5,0)

<h2>See also</h2>

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;returns the magnitude of a complex number 
abs(std::complex) <i>(function template)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;returns the squared magnitude 
norm <i>(function template)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;constructs a complex number from magnitude and phase angle 
polar <i>(function template)</i> 
