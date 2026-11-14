---
title: "stdboolalphastdnoboolalpha(3)"
name: "stdboolalphastdnoboolalpha"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdboolalphastdnoboolalpha/"
description: "std::boolalpha,std::noboolalpha – std::boolalpha,std::noboolalpha"
---

<p>std::boolalpha,std::noboolalpha &#8211; std::boolalpha,std::noboolalpha</p>
<h2>Synopsis</h2>
<p>Defined in header &lt;ios&gt;<br />
std::ios_base&amp; boolalpha( std::ios_base&amp; str ); <code>(1)</code><br />
std::ios_base&amp; noboolalpha( std::ios_base&amp; str ); <code>(2)</code><br />
1) Enables the boolalpha flag in the stream str as if by calling str.setf(std::ios_base::boolalpha)<br />
2) Disables the boolalpha flag in the stream str as if by calling str.unsetf(std::ios_base::boolalpha)<br />
std::boolalpha is an I/O manipulator, so it may be called with an expression such as out &lt;&lt; std::boolalpha for any out of type std::basic_ostream or with an expression such as in &gt;&gt; std::boolalpha for any in of type std::basic_istream. </p>
<h2>Parameters</h2>
<p>str &#8211; reference to I/O stream</p>
<h2>Return value</h2>
<p>str (reference to the stream after manipulation) </p>
<h2>Example</h2>
<p>// Run this code </p>
<pre><code>#include &lt;sstream&gt;

#include &lt;locale&gt;

#include &lt;iostream&gt;

int main()

{
    // boolalpha output
    std::cout &lt;&lt; std::boolalpha
              &lt;&lt; &quot;boolalpha true: &quot; &lt;&lt; true &lt;&lt; '
'
              &lt;&lt; &quot;boolalpha false: &quot; &lt;&lt; false &lt;&lt; '
';
    std::cout &lt;&lt; std::noboolalpha
              &lt;&lt; &quot;noboolalpha true: &quot; &lt;&lt; true &lt;&lt; '
'
              &lt;&lt; &quot;noboolalpha false: &quot; &lt;&lt; false &lt;&lt; '
';
    // boolalpha parse
    bool b1, b2;
    std::istringstream is(&quot;true false&quot;);
    is &gt;&gt; std::boolalpha &gt;&gt; b1 &gt;&gt; b2;
    std::cout &lt;&lt; '\&quot;' &lt;&lt; is.str() &lt;&lt; &quot;\&quot; parsed as &quot; &lt;&lt; b1 &lt;&lt; ' ' &lt;&lt; b2 &lt;&lt; '
';
}
</code></pre>
<h2>Output:</h2>
<p>&nbsp;<wbr>&nbsp;boolalpha true: true<br />
&nbsp;<wbr>&nbsp;boolalpha false: false<br />
&nbsp;<wbr>&nbsp;noboolalpha true: 1<br />
&nbsp;<wbr>&nbsp;noboolalpha false: 0<br />
&nbsp;<wbr>&nbsp;&quot;true false&quot; parsed as 1 0</p>
<h2>See also</h2>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;clears the specified ios_base flags<br />
resetiosflags <i>(function)</i><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;sets the specified ios_base flags<br />
setiosflags <i>(function)</i><br />
do_truename provides the string to use as the name of the boolean true and false<br />
do_falsename <i>(virtual protected member function of std::numpunct&lt;CharT&gt;)</i><br />
<code>[virtual]</code> </p>
