---
title: "operatorstdnormal_distribution(3)"
name: "operatorstdnormal_distribution"
section: "3"
letter: "o"
url: "/docs/linux/man/3-operatorstdnormal_distribution/"
---

operator&lt;&lt;,&gt;&gt;(std::normal_distribution) - operator&lt;&lt;,&gt;&gt;(std::normal_distribution)

<h2>Synopsis</h2>

<pre><code>template &lt;class CharT, class Traits, class ResultType&gt;

std::basic_ostream&lt;CharT, Traits&gt; &amp;operator&lt;&lt;(std::basic_ostream&lt;CharT, Traits&gt; &amp;ost, (1)

                                                                                          const normal_distribution&lt;ResultType&gt; &amp;d);

template &lt;class CharT, class Traits, class ResultType&gt;

std::basic_istream&lt;CharT, Traits&gt; &amp;operator&gt;&gt;(std::basic_istream&lt;CharT, Traits&gt; &amp;ist, (2)

                                                                                          normal_distribution&lt;ResultType&gt; &amp;d);</code></pre> 
Performs stream input and output operations on pseudo-random number distribution d. 
1) Writes a textual representation of the distribution parameters and internal state to ost as textual representation. The formatting flags and fill character of ost are unchanged. 
2) Restores the distribution parameters and internal state with data read from ist. The formatting flags of ist are unchanged. The data must have been written using a stream with the same locale, CharT and Traits template parameters, otherwise the behavior is undefined. If bad input is encountered, ist.setstate(std::ios::failbit) is called, which may throw std::ios_base::failure. d is unchanged in that case. 

<h2>Parameters</h2>

ost - output stream to insert the data to 
ist - input stream to extract the data from 
d - pseudo-random number distribution

<h2>Return value</h2>

1) ost 
2) ist 

<h2>Exceptions</h2>

1) <i>(none)</i> 
2) may throw std::ios_base::failure on bad input.
