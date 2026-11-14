---
title: "stdbitsetto_ulong(3)"
name: "stdbitsetto_ulong"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdbitsetto_ulong/"
---

std::bitset&lt;N&gt;::to_ulong - std::bitset&lt;N&gt;::to_ulong

<h2>Synopsis</h2>

<pre><code>unsigned long to_ulong() const</code></pre> 
Converts the contents of the bitset to an unsigned long integer. 
The first bit of the bitset corresponds to the least significant digit of the number and the last bit corresponds to the most significant digit. 

<h2>Parameters</h2>

<i>(none)</i>

<h2>Return value</h2>

the converted integer 

<h2>Exceptions</h2>

throws std::overflow_error if the value can not be represented in unsigned long.

<h2>Example</h2>

// Run this code <pre><code>#include &lt;iostream&gt;

#include &lt;bitset&gt;
int main()

{
    for (unsigned long i = 0; i &lt; 10; ++i) {
        std::bitset&lt;5&gt; b(i);
        std::bitset&lt;5&gt; b_inverted = ~b;
        std::cout &lt;&lt; i &lt;&lt; '\t';
        std::cout &lt;&lt; b &lt;&lt; '\t';
        std::cout &lt;&lt; b_inverted &lt;&lt; '\t';
        std::cout &lt;&lt; b_inverted.to_ulong() &lt;&lt; '\n';
    }
}
</code></pre>

<h2>Output:</h2>

&nbsp;<wbr>&nbsp;0<tt> </tt>00000<tt> </tt>11111<tt> </tt>31
 
&nbsp;<wbr>&nbsp;1<tt> </tt>00001<tt> </tt>11110<tt> </tt>30
 
&nbsp;<wbr>&nbsp;2<tt> </tt>00010<tt> </tt>11101<tt> </tt>29
 
&nbsp;<wbr>&nbsp;3<tt> </tt>00011<tt> </tt>11100<tt> </tt>28
 
&nbsp;<wbr>&nbsp;4<tt> </tt>00100<tt> </tt>11011<tt> </tt>27
 
&nbsp;<wbr>&nbsp;5<tt> </tt>00101<tt> </tt>11010<tt> </tt>26
 
&nbsp;<wbr>&nbsp;6<tt> </tt>00110<tt> </tt>11001<tt> </tt>25
 
&nbsp;<wbr>&nbsp;7<tt> </tt>00111<tt> </tt>11000<tt> </tt>24
 
&nbsp;<wbr>&nbsp;8<tt> </tt>01000<tt> </tt>10111<tt> </tt>23
 
&nbsp;<wbr>&nbsp;9<tt> </tt>01001<tt> </tt>10110<tt> </tt>22

<h2>See also</h2>

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;returns a string representation of the data 
to_string <i>(public member function)</i> 
to_ullong returns an unsigned long long integer representation of the data 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(public member function)</i> 
<i>(C++11)</i> 
