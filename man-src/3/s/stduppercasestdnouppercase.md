---
title: "stduppercasestdnouppercase(3)"
name: "stduppercasestdnouppercase"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stduppercasestdnouppercase/"
description: "std::uppercase,std::nouppercase – std::uppercase,std::nouppercase"
---

<p>std::uppercase,std::nouppercase &#8211; std::uppercase,std::nouppercase</p>
<h2>Synopsis</h2>
<p>Defined in header &lt;ios&gt;<br />
std::ios_base&amp; uppercase( std::ios_base&amp; str ); <code>(1)</code><br />
std::ios_base&amp; nouppercase( std::ios_base&amp; str ); <code>(2)</code><br />
Enables the use of uppercase characters in floating-point and hexadecimal integer output. Has no effect on input.<br />
1) enables the uppercase flag in the stream str as if by calling str.setf(std::ios_base::uppercase)<br />
2) disables the uppercase flag in the stream str as if by calling str.unsetf(std::ios_base::uppercase)<br />
This is an I/O manipulator, it may be called with an expression such as out &lt;&lt; std::uppercase for any out of type std::basic_ostream or with an expression such as in &gt;&gt; std::uppercase for any in of type std::basic_istream. </p>
<h2>Parameters</h2>
<p>str &#8211; reference to I/O stream</p>
<h2>Return value</h2>
<p>str (reference to the stream after manipulation) </p>
<h2>Example</h2>
<p>// Run this code </p>
<pre><code>#include &lt;iostream&gt;

int main()

{
    std::cout &lt;&lt; std::hex &lt;&lt; std::showbase
              &lt;&lt; &quot;0x2a with uppercase: &quot; &lt;&lt; std::uppercase &lt;&lt; 0x2a &lt;&lt; '
'
              &lt;&lt; &quot;0x2a with nouppercase: &quot; &lt;&lt; std::nouppercase &lt;&lt; 0x2a &lt;&lt; '
'
              &lt;&lt; &quot;1e-10 with uppercase: &quot; &lt;&lt; std::uppercase &lt;&lt; 1e-10 &lt;&lt; '
'
              &lt;&lt; &quot;1e-10 with nouppercase: &quot; &lt;&lt; std::nouppercase &lt;&lt; 1e-10 &lt;&lt; '
';
}
</code></pre>
<h2>Output:</h2>
<p>&nbsp;<wbr>&nbsp;0x2a with uppercase: 0X2A<br />
&nbsp;<wbr>&nbsp;0x2a with nouppercase: 0x2a<br />
&nbsp;<wbr>&nbsp;1e-10 with uppercase: 1E-10<br />
&nbsp;<wbr>&nbsp;1e-10 with nouppercase: 1e-10</p>
<h2>See also</h2>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;clears the specified ios_base flags<br />
resetiosflags <i>(function)</i><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;sets the specified ios_base flags<br />
setiosflags <i>(function)</i> </p>
