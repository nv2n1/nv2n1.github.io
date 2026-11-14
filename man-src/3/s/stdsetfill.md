---
title: "stdsetfill(3)"
name: "stdsetfill"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdsetfill/"
---

std::setfill - std::setfill

<h2>Synopsis</h2>

<pre><code>Defined in header &lt;iomanip&gt;

template&lt; class CharT &gt;

/*unspecified*/ setfill( CharT c );</code></pre> 
When used in an expression out &lt;&lt; setfill(c) sets the fill character of the stream out to c. 

<h2>Parameters</h2>

c - new value for the fill character

<h2>Return value</h2>

Returns an object of unspecified type such that if out is the name of an output stream of type std::basic_ostream&lt;CharT, Traits&gt;, then the expression out &lt;&lt; setfill(n) behaves as if the following code was executed :

    out.fill(n);


<h2>Notes</h2>

The current fill character may be obtained with std::ostream::fill 

<h2>Example</h2>

// Run this code <pre><code>#include &lt;iostream&gt;

#include &lt;iomanip&gt;

int main()

{
    std::cout &lt;&lt; &quot;default fill: &quot; &lt;&lt; std::setw(10) &lt;&lt; 42 &lt;&lt; '\n'
              &lt;&lt; &quot;setfill('*'): &quot; &lt;&lt; std::setfill('*')
              &lt;&lt; std::setw(10) &lt;&lt; 42 &lt;&lt; '\n';
}
</code></pre>

<h2>Output:</h2>

&nbsp;<wbr>&nbsp;default fill: 42 
&nbsp;<wbr>&nbsp;setfill('*'): ********42

<h2>See also</h2>

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;manages the fill character 
fill <i>(public member function of std::basic_ios&lt;CharT,Traits&gt;)</i> 
internal sets the placement of fill characters 
left <i>(function)</i> 
right 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;changes the width of the next input/output field 
setw <i>(function)</i> 
