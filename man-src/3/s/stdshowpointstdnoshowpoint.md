---
title: "stdshowpointstdnoshowpoint(3)"
name: "stdshowpointstdnoshowpoint"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdshowpointstdnoshowpoint/"
description: "std::showpoint,std::noshowpoint – std::showpoint,std::noshowpoint"
---

<p>std::showpoint,std::noshowpoint &#8211; std::showpoint,std::noshowpoint</p>
<h2>Synopsis</h2>
<p>Defined in header &lt;ios&gt;<br />
std::ios_base&amp; showpoint( std::ios_base&amp; str ); <code>(1)</code><br />
std::ios_base&amp; noshowpoint( std::ios_base&amp; str ); <code>(2)</code><br />
Enables or disables the unconditional inclusion of the decimal point character in floating-point output. Has no effect on input.<br />
1) enables the showpoint flag in the stream str as if by calling str.setf(std::ios_base::showpoint)<br />
2) disables the showpoint flag in the stream str as if by calling str.unsetf(std::ios_base::showpoint)<br />
This is an I/O manipulator, it may be called with an expression such as out &lt;&lt; std::showpoint for any out of type std::basic_ostream or with an expression such as in &gt;&gt; std::showpoint for any in of type std::basic_istream.<br />
The character to use as decimal point character is determined by the numpunct facet of the locale imbued in the stream at the time of output, as described in std::num_put::put </p>
<h2>Parameters</h2>
<p>str &#8211; reference to I/O stream</p>
<h2>Return value</h2>
<p>str (reference to the stream after manipulation) </p>
<h2>Example</h2>
<p>// Run this code </p>
<pre><code>#include &lt;iostream&gt;

int main()

{
    std::cout &lt;&lt; &quot;1.0 with showpoint: &quot; &lt;&lt; std::showpoint &lt;&lt; 1.0 &lt;&lt; '
'
              &lt;&lt; &quot;1.0 with noshowpoint: &quot; &lt;&lt; std::noshowpoint &lt;&lt; 1.0 &lt;&lt; '
';
}
</code></pre>
<h2>Output:</h2>
<p>&nbsp;<wbr>&nbsp;1.0 with showpoint: 1.00000<br />
&nbsp;<wbr>&nbsp;1.0 with noshowpoint: 1</p>
<h2>See also</h2>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;clears the specified ios_base flags<br />
resetiosflags <i>(function)</i><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;sets the specified ios_base flags<br />
setiosflags <i>(function)</i> </p>
