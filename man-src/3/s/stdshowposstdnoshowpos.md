---
title: "stdshowposstdnoshowpos(3)"
name: "stdshowposstdnoshowpos"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdshowposstdnoshowpos/"
description: "std::showpos,std::noshowpos – std::showpos,std::noshowpos"
---

<p>std::showpos,std::noshowpos &#8211; std::showpos,std::noshowpos</p>
<h2>Synopsis</h2>
<p>Defined in header &lt;ios&gt;<br />
std::ios_base&amp; showpos( std::ios_base&amp; str ); <code>(1)</code><br />
std::ios_base&amp; noshowpos( std::ios_base&amp; str ); <code>(2)</code><br />
Enables or disables the display of the plus sign &#8216;+&#8217; in non-negative integer output. Has no effect on input.<br />
1) enables the showpos flag in the stream str as if by calling str.setf(std::ios_base::showpos)<br />
2) disables the showpos flag in the stream str as if by calling str.unsetf(std::ios_base::showpos)<br />
This is an I/O manipulator, it may be called with an expression such as out &lt;&lt; std::showpos for any out of type std::basic_ostream or with an expression such as in &gt;&gt; std::showpos for any in of type std::basic_istream. </p>
<h2>Parameters</h2>
<p>str &#8211; reference to I/O stream</p>
<h2>Return value</h2>
<p>str (reference to the stream after manipulation) </p>
<h2>Example</h2>
<p>// Run this code </p>
<pre><code>#include &lt;iostream&gt;

int main()

{
    std::cout &lt;&lt; &quot;showpos: &quot; &lt;&lt; std::showpos &lt;&lt; 42 &lt;&lt; ' ' &lt;&lt; 3.14 &lt;&lt; ' ' &lt;&lt; 0 &lt;&lt; '
'
              &lt;&lt; &quot;noshowpos: &quot; &lt;&lt; std::noshowpos &lt;&lt; 42 &lt;&lt; ' ' &lt;&lt; 3.14 &lt;&lt; ' ' &lt;&lt; 0 &lt;&lt; '
';
}
</code></pre>
<h2>Output:</h2>
<p>&nbsp;<wbr>&nbsp;showpos: +42 +3.14 +0<br />
&nbsp;<wbr>&nbsp;noshowpos: 42 3.14 0</p>
<h2>See also</h2>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;clears the specified ios_base flags<br />
resetiosflags <i>(function)</i><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;sets the specified ios_base flags<br />
setiosflags <i>(function)</i> </p>
