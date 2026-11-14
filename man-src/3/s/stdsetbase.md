---
title: "stdsetbase(3)"
name: "stdsetbase"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdsetbase/"
---

std::setbase - std::setbase

<h2>Synopsis</h2>

<pre><code>Defined in header&lt;iomanip&gt;

/*unspecified*/ setbase(int base);</code></pre> 
Sets the numeric base of the stream. When used in an expression out &lt;&lt; setbase(base) or in &gt;&gt; setbase(base), changes the basefield flag of the stream out or in, depending on the value of base: 
* the value 16 sets basefield to std::ios_base::hex 
* the value 8 sets std::ios_base::oct 
* the value 10 sets std::ios_base::dec. 
Values of base other than 8, 10, or 16 reset basefield to zero, which corresponds to decimal output and prefix-dependent input. 

<h2>Parameters</h2>

base - new value for basefield

<h2>Return value</h2>

Returns an object of unspecified type such that if str is the name of an output stream of type std::basic_ostream&lt;CharT, Traits&gt; or std::basic_istream&lt;CharT, Traits&gt;, then the expression str &lt;&lt; setbase(base) or str &gt;&gt; setbase(base) behaves as if the following code was executed: str.setf(base ==  8 ? std::ios_base::oct :
base == 10 ? std::ios_base::dec :
base == 16 ? std::ios_base::hex :
std::ios_base::fmtflags(0),
std::ios_base::basefield);



<h2>Example</h2>

// Run this code <pre><code>#include &lt;iostream&gt;

#include &lt;sstream&gt;

#include &lt;iomanip&gt;

int main()

{
    std::cout &lt;&lt; &quot;Parsing string \&quot;10 0x10 010\&quot;\n&quot;;
    int n1, n2, n3;
    std::istringstream s(&quot;10 0x10 010&quot;);
    s &gt;&gt; std::setbase(16) &gt;&gt; n1 &gt;&gt; n2 &gt;&gt; n3;
    std::cout &lt;&lt; &quot;hexadecimal parse: &quot; &lt;&lt; n1 &lt;&lt; ' ' &lt;&lt; n2 &lt;&lt; ' ' &lt;&lt; n3 &lt;&lt; '\n';
    s.clear();
    s.seekg(0);
    s &gt;&gt; std::setbase(0) &gt;&gt; n1 &gt;&gt; n2 &gt;&gt; n3;
    std::cout &lt;&lt; &quot;prefix-dependent parse: &quot; &lt;&lt; n1 &lt;&lt; ' ' &lt;&lt; n2 &lt;&lt; ' ' &lt;&lt; n3 &lt;&lt; '\n';
    std::cout &lt;&lt; &quot;hex output: &quot; &lt;&lt; std::setbase(16)
              &lt;&lt; std::showbase &lt;&lt; n1 &lt;&lt; ' ' &lt;&lt; n2 &lt;&lt; ' ' &lt;&lt; n3 &lt;&lt; '\n';
}
</code></pre>

<h2>Output:</h2>

&nbsp;<wbr>&nbsp;Parsing string &quot;10 0x10 010&quot; 
&nbsp;<wbr>&nbsp;hexadecimal parse: 16 16 16 
&nbsp;<wbr>&nbsp;prefix-dependent parse: 10 16 8 
&nbsp;<wbr>&nbsp;hex output: 0xa 0x10 0x8

<h2>See also</h2>

dec changes the base used for integer I/O 
hex <i>(function)</i> 
oct 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;controls whether prefix is used to indicate numeric base 
showbase <i>(function)</i> 
noshowbase 
