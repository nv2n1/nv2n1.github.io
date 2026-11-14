---
title: "stdmersenne_twister_engine(3)"
name: "stdmersenne_twister_engine"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdmersenne_twister_engine/"
---

std::mersenne_twister_engine&lt;UIntType,w,n,m,r,a,u,d,s,b,t,c,l,f&gt;::seed - std::mersenne_twister_engine&lt;UIntType,w,n,m,r,a,u,d,s,b,t,c,l,f&gt;::seed

<h2>Synopsis</h2>

<pre><code>void seed(result_type value = default_seed);
(1)(since C++ 11)

    template &lt;class Sseq&gt;
    (2)(since C++ 11)

        void seed(Sseq &amp;seq);</code></pre> 
Reinitializes the internal state of the random-number engine using new seed value. 
&nbsp;This section is incomplete 

<h2>Parameters</h2>

value - seed value to use in the initialization of the internal state 
seq - seed sequence to use in the initialization of the internal state

<h2>Exceptions</h2>

<i>(none)</i>

<h2>Complexity</h2>

&nbsp;This section is incomplete

<h2>Example</h2>

// Run this code <pre><code>#include &lt;iostream&gt;

#include &lt;random&gt;
int main()

{
    std::mt19937 gen;
    // Seed the engine with an unsigned int
    gen.seed(1);
    std::cout &lt;&lt; &quot;after seed by 1: &quot; &lt;&lt; gen() &lt;&lt; '\n';
    // Seed the engine with two unsigned ints
    std::seed_seq sseq{1, 2};
    gen.seed(sseq);
    std::cout &lt;&lt; &quot;after seed by {1,2}: &quot; &lt;&lt; gen() &lt;&lt; '\n';
}
</code></pre>

<h2>Possible output:</h2>

&nbsp;<wbr>&nbsp;after seed by 1: 1791095845 
&nbsp;<wbr>&nbsp;after seed by {1,2}: 3127717181
