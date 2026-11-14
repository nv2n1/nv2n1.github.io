---
title: "stdsetiosflags(3)"
name: "stdsetiosflags"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdsetiosflags/"
---

std::setiosflags - std::setiosflags

<h2>Synopsis</h2>

<pre><code>Defined in header &lt;iomanip&gt;

/*unspecified*/ setiosflags( std::ios_base::fmtflags mask );</code></pre> 
When used in an expression out &lt;&lt; setiosflags(mask) or in &gt;&gt; setiosflags(mask), sets all format flags of the stream out or in as specified by the mask. 

<h2>Parameters</h2>

mask - bitmask of the flags to set

<h2>Return value</h2>

Returns an object of unspecified type such that if str is the name of a stream of type std::basic_ostream&lt;CharT, Traits&gt; or std::basic_istream&lt;CharT, Traits&gt;, then the expression str &lt;&lt; setiosflags(mask) or str &gt;&gt; setiosflags(mask) behaves as if the following code was executed :

    str.setf(mask);


<h2>Example</h2>

// Run this code <pre><code>#include &lt;iostream&gt;

#include &lt;iomanip&gt;
int main()

{
    std::cout &lt;&lt; std::resetiosflags(std::ios_base::dec)
              &lt;&lt; std::setiosflags(std::ios_base::hex | std::ios_base::uppercase | std::ios_base::showbase) &lt;&lt; 42 &lt;&lt; '\n';
}
</code></pre>

<h2>Output:</h2>

&nbsp;<wbr>&nbsp;0X2A

<h2>See also</h2>

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;sets specific format flag 
setf <i>(public member function of std::ios_base)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;clears the specified ios_base flags 
resetiosflags <i>(function)</i> 
