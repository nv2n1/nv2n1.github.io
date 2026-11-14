---
title: "stdgenerate_canonical(3)"
name: "stdgenerate_canonical"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdgenerate_canonical/"
---

std::generate_canonical - std::generate_canonical

<h2>Synopsis</h2>

<pre><code>Defined in header &lt;random&gt;

template&lt; class RealType, size_t bits, class Generator &gt;  (since C++11)

RealType generate_canonical( Generator&amp; g );
Generates a random floating point number in range [0, 1).

To generate enough entropy, generate_canonical() will call g() exactly k times, where \(k = max(1, \lceil \frac{b}{log_2 R} \rceil)\)k = max(1, ⌈ b / log

2 R ⌉) and
* b = std::min&lt;std::size_t&gt;(bits, std::numeric_limits&lt;RealType&gt;::digits)

* R = g.max() - g.min() + 1.

</code></pre>

<h2>Parameters</h2>

g - generator to use to acquire entropy

<h2>Return value</h2>

Floating point value in range [0, 1). 

<h2>Exceptions</h2>

None except from those thrown by g

<h2>Notes</h2>

Some existing implementations have a bug where they may occasionally return 1.0 if RealType is float GCC_#63176 LLVM_#18767. This is LWG_issue_2524 

<h2>Example</h2>

produce random numbers with 10 bits of randomness: this may produce only k*R distinct values 
 // Run this code <pre><code>#include &lt;random&gt;

#include &lt;iostream&gt;
int main()

{
    std::random_device rd;
    std::mt19937 gen(rd());
    for (int n = 0; n &lt; 10; ++n) {
        std::cout &lt;&lt; std::generate_canonical&lt;double, 10&gt;(gen) &lt;&lt; ' ';
    }
}
</code></pre>

<h2>Possible output:</h2>

&nbsp;<wbr>&nbsp;0.208143 0.824147 0.0278604 0.343183 0.0173263 0.864057 0.647037 0.539467 0.0583497 0.609219

<h2>See also</h2>

uniform_real_distribution produces real values evenly distributed across a range 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(class template)</i> 
<i>(C++11)</i> 
