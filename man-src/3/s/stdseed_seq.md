---
title: "stdseed_seq(3)"
name: "stdseed_seq"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdseed_seq/"
---

std::seed_seq - std::seed_seq

<h2>Synopsis</h2>

Defined in header &lt;random&gt; 
class seed_seq; <i>(since C++11)</i> 
std::seed_seq consumes a sequence of integer-valued data and produces a requested number of unsigned integer values i, 0 ≤ i &lt; 232 
, based on the consumed data. The produced values are distributed over the entire 32-bit range even if the consumed values are close. 
It provides a way to seed a large number of random number engines or to seed a generator that requires a lot of entropy, given a small seed or a poorly distributed initial seed sequence. 
std::seed_seq meets the requirements of SeedSequence. 

<h2>Member types</h2>

Member type Definition 
result_type std::uint_least32_t

<h2>Member functions</h2>

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;constructs and seeds the std::seed_seq object 
constructor <i>(public member function)</i> 

 
operator= not copy-assignable 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(public member function)</i> 
(deleted) 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;calculates the bias-eliminated, evenly distributed 32-bit values 
generate <i>(public member function)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;obtains the number of 32-bit values stored in std::seed_seq 
size <i>(public member function)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;obtains the 32-bit values stored in std::seed_seq 
param <i>(public member function)</i>

<h2>Example</h2>

// Run this code <pre><code>#include &lt;random&gt;

#include &lt;cstdint&gt;

#include &lt;iostream&gt;
int main()

{
    std::seed_seq seq{1, 2, 3, 4, 5};
    std::vector&lt;std::uint32_t&gt; seeds(10);
    seq.generate(seeds.begin(), seeds.end());
    for (std::uint32_t n : seeds) {
        std::cout &lt;&lt; n &lt;&lt; '\n';
    }
}
</code></pre>

<h2>Output:</h2>

&nbsp;<wbr>&nbsp;4204997637 
&nbsp;<wbr>&nbsp;4246533866 
&nbsp;<wbr>&nbsp;1856049002 
&nbsp;<wbr>&nbsp;1129615051 
&nbsp;<wbr>&nbsp;690460811 
&nbsp;<wbr>&nbsp;1075771511 
&nbsp;<wbr>&nbsp;46783058 
&nbsp;<wbr>&nbsp;3904109078 
&nbsp;<wbr>&nbsp;1534123438 
&nbsp;<wbr>&nbsp;1495905678
