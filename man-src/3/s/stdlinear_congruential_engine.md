---
title: "stdlinear_congruential_engine(3)"
name: "stdlinear_congruential_engine"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdlinear_congruential_engine/"
---

std::linear_congruential_engine&lt;UIntType,a,c,m&gt;::seed - std::linear_congruential_engine&lt;UIntType,a,c,m&gt;::seed

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
