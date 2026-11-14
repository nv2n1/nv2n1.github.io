---
title: "stdleftstdrightstdinternal(3)"
name: "stdleftstdrightstdinternal"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdleftstdrightstdinternal/"
description: "std::left,std::right,std::internal – std::left,std::right,std::internal"
---

<p>std::left,std::right,std::internal &#8211; std::left,std::right,std::internal</p>
<h2>Synopsis</h2>
<p>Defined in header &lt;ios&gt;<br />
std::ios_base&amp; left( std::ios_base&amp; str ); <code>(1)</code><br />
std::ios_base&amp; right( std::ios_base&amp; str ); <code>(2)</code><br />
std::ios_base&amp; internal( std::ios_base&amp; str ); <code>(3)</code><br />
Modifies the default positioning of the fill characters. left and right apply to any output, internal applies to integer, floating-point, and monetary output. Has no effect on input.<br />
1) sets the adjustfield of the stream str to left as if by calling str.setf(std::ios_base::left, std::ios_base::adjustfield)<br />
2) sets the adjustfield of the stream str to right as if by calling str.setf(std::ios_base::right, std::ios_base::adjustfield)<br />
3) sets the adjustfield of the stream str to internal as if by calling str.setf(std::ios_base::internal, std::ios_base::adjustfield)<br />
This is an I/O manipulator. It may be called with an expression such as out &lt;&lt; std::left for any out of type std::basic_ostream or with an expression such as in &gt;&gt; std::left for any in of type std::basic_istream. </p>
<h2>Parameters</h2>
<p>str &#8211; reference to I/O stream</p>
<h2>Return value</h2>
<p>str (reference to the stream after manipulation) </p>
<h2>Example</h2>
<p>// Run this code </p>
<pre><code>#include &lt;iostream&gt;

#include &lt;iomanip&gt;

#include &lt;locale&gt;
int main()

{
    std::cout.imbue(std::locale(&quot;en_US.utf8&quot;));
    std::cout &lt;&lt; &quot;Left fill:
&quot;
              &lt;&lt; std::left &lt;&lt; std::setfill('*')
              &lt;&lt; std::setw(12) &lt;&lt; -1.23 &lt;&lt; '
'
              &lt;&lt; std::setw(12) &lt;&lt; std::hex &lt;&lt; std::showbase &lt;&lt; 42 &lt;&lt; '
'
              &lt;&lt; std::setw(12) &lt;&lt; std::put_money(123, true) &lt;&lt; &quot;

&quot;;
    std::cout &lt;&lt; &quot;Internal fill:
&quot;
              &lt;&lt; std::internal
              &lt;&lt; std::setw(12) &lt;&lt; -1.23 &lt;&lt; '
'
              &lt;&lt; std::setw(12) &lt;&lt; 42 &lt;&lt; '
'
              &lt;&lt; std::setw(12) &lt;&lt; std::put_money(123, true) &lt;&lt; &quot;

&quot;;
    std::cout &lt;&lt; &quot;Right fill:
&quot;
              &lt;&lt; std::right
              &lt;&lt; std::setw(12) &lt;&lt; -1.23 &lt;&lt; '
'
              &lt;&lt; std::setw(12) &lt;&lt; 42 &lt;&lt; '
'
              &lt;&lt; std::setw(12) &lt;&lt; std::put_money(123, true) &lt;&lt; '
';
}
</code></pre>
<h2>Output:</h2>
<p>&nbsp;<wbr>&nbsp;Left fill:<br />
&nbsp;<wbr>&nbsp;-1.23*******<br />
&nbsp;<wbr>&nbsp;0x2a********<br />
&nbsp;<wbr>&nbsp;USD *1.23*** </p>
<p>&nbsp;<wbr>&nbsp;Internal fill:<br />
&nbsp;<wbr>&nbsp;-*******1.23<br />
&nbsp;<wbr>&nbsp;0x********2a<br />
&nbsp;<wbr>&nbsp;USD ****1.23 </p>
<p>&nbsp;<wbr>&nbsp;Right fill:<br />
&nbsp;<wbr>&nbsp;*******-1.23<br />
&nbsp;<wbr>&nbsp;********0x2a<br />
&nbsp;<wbr>&nbsp;***USD *1.23</p>
<h2>See also</h2>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;changes the width of the next input/output field<br />
setw <i>(function)</i><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;changes the fill character<br />
setfill <i>(function template)</i> </p>
