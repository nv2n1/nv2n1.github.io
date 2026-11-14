---
title: "stdresetiosflags(3)"
name: "stdresetiosflags"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdresetiosflags/"
---

std::resetiosflags - std::resetiosflags

<h2>Synopsis</h2>

<pre><code>Defined in header &lt;iomanip&gt;

/*unspecified*/ resetiosflags( std::ios_base::fmtflags mask );</code></pre> 
When used in an expression out &lt;&lt; resetiosflags(mask) or in &gt;&gt; resetiosflags(mask), clears all format flags of the stream out or in as specified by the mask. 

<h2>Parameters</h2>

mask - bitmask of the flags to clear

<h2>Return value</h2>

Returns an object of unspecified type such that if str is the name of a stream of type std::basic_ostream&lt;CharT, Traits&gt; or std::basic_istream&lt;CharT, Traits&gt;, then the expression str &lt;&lt; resetiosflags(mask) or str &gt;&gt; resetiosflags(mask) behaves as if the following code was executed :

    str.setf(std::ios_base::fmtflags(0), mask);


<h2>Example</h2>

// Run this code <pre><code>#include &lt;sstream&gt;

#include &lt;iostream&gt;

#include &lt;iomanip&gt;

int main()

{
    std::istringstream in(&quot;10 010 10 010 10 010&quot;);
    int n1, n2;
    in &gt;&gt; std::oct &gt;&gt; n1 &gt;&gt; n2;
    std::cout &lt;&lt; &quot;Parsing \&quot;10 010\&quot; with std::oct gives:  &quot; &lt;&lt; n1 &lt;&lt; ' ' &lt;&lt; n2 &lt;&lt; '\n';
    in &gt;&gt; std::dec &gt;&gt; n1 &gt;&gt; n2;
    std::cout &lt;&lt; &quot;Parsing \&quot;10 010\&quot; with std::dec gives:  &quot; &lt;&lt; n1 &lt;&lt; ' ' &lt;&lt; n2 &lt;&lt; '\n';
    in &gt;&gt; std::resetiosflags(std::ios_base::basefield) &gt;&gt; n1 &gt;&gt; n2;
    std::cout &lt;&lt; &quot;Parsing \&quot;10 010\&quot; with autodetect gives: &quot; &lt;&lt; n1 &lt;&lt; ' ' &lt;&lt; n2 &lt;&lt; '\n';
}
</code></pre>

<h2>Output:</h2>

&nbsp;<wbr>&nbsp;Parsing &quot;10 010&quot; with std::oct gives: 8 8 
&nbsp;<wbr>&nbsp;Parsing &quot;10 010&quot; with std::dec gives: 10 10 
&nbsp;<wbr>&nbsp;Parsing &quot;10 010&quot; with autodetect gives: 10 8

<h2>See also</h2>

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;sets specific format flag 
setf <i>(public member function of std::ios_base)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;sets the specified ios_base flags 
setiosflags <i>(function)</i> 
