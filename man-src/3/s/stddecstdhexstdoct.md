---
title: "stddecstdhexstdoct(3)"
name: "stddecstdhexstdoct"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stddecstdhexstdoct/"
description: "std::dec,std::hex,std::oct – std::dec,std::hex,std::oct"
---

<p>std::dec,std::hex,std::oct &#8211; std::dec,std::hex,std::oct</p>
<h2>Synopsis</h2>
<p>Defined in header &lt;ios&gt;<br />
std::ios_base&amp; dec( std::ios_base&amp; str ); <code>(1)</code><br />
std::ios_base&amp; hex( std::ios_base&amp; str ); <code>(2)</code><br />
std::ios_base&amp; oct( std::ios_base&amp; str ); <code>(3)</code><br />
Modifies the default numeric base for integer I/O.<br />
1) sets the basefield of the stream str to dec as if by calling str.setf(std::ios_base::dec, std::ios_base::basefield)<br />
2) sets the basefield of the stream str to hex as if by calling str.setf(std::ios_base::hex, std::ios_base::basefield)<br />
3) sets the basefield of the stream str to oct as if by calling str.setf(std::ios_base::oct, std::ios_base::basefield)<br />
This is an I/O manipulator. It may be called with an expression such as out &lt;&lt; std::hex for any out of type std::basic_ostream or with an expression such as in &gt;&gt; std::hex for any in of type std::basic_istream. </p>
<h2>Parameters</h2>
<p>str &#8211; reference to I/O stream</p>
<h2>Return value</h2>
<p>str (reference to the stream after manipulation) </p>
<h2>Example</h2>
<p>// Run this code </p>
<pre><code>#include &lt;iostream&gt;

#include &lt;sstream&gt;

int main()

{
    std::cout &lt;&lt; &quot;The number 42 in octal:   &quot; &lt;&lt; std::oct &lt;&lt; 42 &lt;&lt; '
'
              &lt;&lt; &quot;The number 42 in decimal: &quot; &lt;&lt; std::dec &lt;&lt; 42 &lt;&lt; '
'
              &lt;&lt; &quot;The number 42 in hex:     &quot; &lt;&lt; std::hex &lt;&lt; 42 &lt;&lt; '
';
    int n;
    std::istringstream(&quot;2A&quot;) &gt;&gt; std::hex &gt;&gt; n;
    std::cout &lt;&lt; std::dec &lt;&lt; &quot;Parsing \&quot;2A\&quot; as hex gives &quot; &lt;&lt; n &lt;&lt; '
';
    // the output base is sticky until changed
    std::cout &lt;&lt; std::hex &lt;&lt; &quot;42 as hex gives &quot; &lt;&lt; 42
              &lt;&lt; &quot; and 21 as hex gives &quot; &lt;&lt; 21 &lt;&lt; '
';
}
</code></pre>
<h2>Output:</h2>
<p>&nbsp;<wbr>&nbsp;The number 42 in octal: 52<br />
&nbsp;<wbr>&nbsp;The number 42 in decimal: 42<br />
&nbsp;<wbr>&nbsp;The number 42 in hex: 2a<br />
&nbsp;<wbr>&nbsp;Parsing &quot;2A&quot; as hex gives 42<br />
&nbsp;<wbr>&nbsp;42 as hex gives 2a and 21 as hex gives 15</p>
<h2>See also</h2>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;changes the base used for integer I/O<br />
setbase <i>(function)</i><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;controls whether prefix is used to indicate numeric base<br />
showbase <i>(function)</i><br />
noshowbase </p>
