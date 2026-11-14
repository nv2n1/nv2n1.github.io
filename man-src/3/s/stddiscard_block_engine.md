---
title: "stddiscard_block_engine(3)"
name: "stddiscard_block_engine"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stddiscard_block_engine/"
---

std::discard_block_engine&lt;Engine,P,R&gt;::seed - std::discard_block_engine&lt;Engine,P,R&gt;::seed

<h2>Synopsis</h2>

<pre><code>void seed();
(1)(since C++ 11)

    void seed(result_type value);
(2)(since C++ 11)

    template &lt;class Sseq&gt;
    (3)(since C++ 11)

        void seed(Sseq &amp;seq);</code></pre> 
Reinitializes the internal state of the underlying engine using a new seed value. 
1) Seeds the underlying engine with the default seed value. Effectively calls e.seed(), where e is the underlying engine. 
2) Seeds the underlying engine with the seed value s. Effectively calls e.seed(value), where e is the underlying engine. 
3) Seeds the underlying engine with the seed sequence seq. Effectively calls e.seed(seq), where e is the underlying engine. This template only participate in overload resolution if Sseq qualifies as a SeedSequence. In particular, this template does not participate in overload resolution if Sseq is implicitly convertible to result_type. 

<h2>Parameters</h2>

value - seed value to use in the initialization of the internal state of the underlying engine 
seq - seed sequence to use in the initialization of the internal state of the underlying engine

<h2>Return value</h2>

<i>(none)</i> 

<h2>Exceptions</h2>

<i>(none)</i>
