---
title: "stdskipwsstdnoskipws(3)"
name: "stdskipwsstdnoskipws"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdskipwsstdnoskipws/"
description: "std::skipws,std::noskipws – std::skipws,std::noskipws"
---

<p>std::skipws,std::noskipws &#8211; std::skipws,std::noskipws</p>
<h2>Synopsis</h2>
<p>Defined in header &lt;ios&gt;<br />
std::ios_base&amp; skipws( std::ios_base&amp; str ); <code>(1)</code><br />
std::ios_base&amp; noskipws( std::ios_base&amp; str ); <code>(2)</code><br />
Enables or disables skipping of leading whitespace by the formatted input functions (enabled by default). Has no effect on output.<br />
1) enables the skipws flag in the stream str as if by calling str.setf(std::ios_base::skipws)<br />
2) disables the skipws flag in the stream str as if by calling str.unsetf(std::ios_base::skipws)<br />
The whitespace skipping is performed by the constructor of std::basic_istream::sentry, which reads and discards the characters classified as whitespace by the std::ctype facet of the stream&#8217;s imbued locale.<br />
This is an I/O manipulator, it may be called with an expression such as out &lt;&lt; std::noskipws for any out of type std::basic_ostream or with an expression such as in &gt;&gt; std::noskipws for any in of type std::basic_istream. </p>
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
    char c1, c2, c3;
    std::istringstream(&quot;a b c&quot;) &gt;&gt; c1 &gt;&gt; c2 &gt;&gt; c3;
    std::cout &lt;&lt; &quot;Default  behavior: c1 = &quot; &lt;&lt; c1 &lt;&lt; &quot; c2 = &quot; &lt;&lt; c2 &lt;&lt; &quot; c3 = &quot; &lt;&lt; c3 &lt;&lt; '
';
    std::istringstream(&quot;a b c&quot;) &gt;&gt; std::noskipws &gt;&gt; c1 &gt;&gt; c2 &gt;&gt; c3;
    std::cout &lt;&lt; &quot;noskipws behavior: c1 = &quot; &lt;&lt; c1 &lt;&lt; &quot; c2 = &quot; &lt;&lt; c2 &lt;&lt; &quot; c3 = &quot; &lt;&lt; c3 &lt;&lt; '
';
}
</code></pre>
<h2>Output:</h2>
<p>&nbsp;<wbr>&nbsp;Default behavior: c1 = a c2 = b c3 = c<br />
&nbsp;<wbr>&nbsp;noskipws behavior: c1 = a c2 = c3 = b</p>
<h2>See also</h2>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;clears the specified ios_base flags<br />
resetiosflags <i>(function)</i><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;sets the specified ios_base flags<br />
setiosflags <i>(function)</i> </p>
