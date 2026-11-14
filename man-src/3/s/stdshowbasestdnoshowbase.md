---
title: "stdshowbasestdnoshowbase(3)"
name: "stdshowbasestdnoshowbase"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdshowbasestdnoshowbase/"
description: "std::showbase,std::noshowbase – std::showbase,std::noshowbase"
---

<p>std::showbase,std::noshowbase &#8211; std::showbase,std::noshowbase</p>
<h2>Synopsis</h2>
<p>Defined in header &lt;ios&gt;<br />
std::ios_base&amp; showbase( std::ios_base&amp; str ); <code>(1)</code><br />
std::ios_base&amp; noshowbase( std::ios_base&amp; str ); <code>(2)</code><br />
1) enables the showbase flag in the stream str as if by calling str.setf(std::ios_base::showbase)<br />
2) disables the showbase flag in the stream str as if by calling str.unsetf(std::ios_base::showbase)<br />
This is an I/O manipulator, it may be called with an expression such as out &lt;&lt; std::showbase for any out of type std::basic_ostream or with an expression such as in &gt;&gt; std::showbase for any in of type std::basic_istream.<br />
The showbase flag affects the behavior of integer output (see std::num_put::put), monetary input (see std::money_get::get) and monetary output (see std::money_put::put). </p>
<h2>Parameters</h2>
<p>str &#8211; reference to I/O stream</p>
<h2>Return value</h2>
<p>str (reference to the stream after manipulation) </p>
<h2>Notes</h2>
<p>As specifed in std::num_put::put, the showbase flag in integer output acts like the # format specifier in std::printf, which means the numeric base prefix is not added when outputting the value zero. </p>
<h2>Example</h2>
<p>// Run this code </p>
<pre><code>#include &lt;sstream&gt;

#include &lt;locale&gt;

#include &lt;iostream&gt;

#include &lt;iomanip&gt;

int main()

{
    // showbase affects the output of octals and hexadecimals
    std::cout &lt;&lt; std::hex
              &lt;&lt; &quot;showbase: &quot; &lt;&lt; std::showbase &lt;&lt; 42 &lt;&lt; '
'
              &lt;&lt; &quot;noshowbase: &quot; &lt;&lt; std::noshowbase &lt;&lt; 42 &lt;&lt; '
';
    // and both input and output of monetary values
    std::locale::global(std::locale(&quot;en_US.utf8&quot;));
    long double val = 0;
    std::istringstream is(&quot;3.14&quot;);
    is &gt;&gt; std::showbase &gt;&gt; std::get_money(val);
    std::cout &lt;&lt; &quot;With showbase, parsing 3.14 as money gives &quot; &lt;&lt; val &lt;&lt; '
';
    is.seekg(0);
    is &gt;&gt; std::noshowbase &gt;&gt; std::get_money(val);
    std::cout &lt;&lt; &quot;Without showbase, parsing 3.14 as money gives &quot; &lt;&lt; val &lt;&lt; '
';
}
</code></pre>
<h2>Output:</h2>
<p>&nbsp;<wbr>&nbsp;showbase: 0x2a<br />
&nbsp;<wbr>&nbsp;noshowbase: 2a<br />
&nbsp;<wbr>&nbsp;With showbase, parsing 3.14 as money gives 0<br />
&nbsp;<wbr>&nbsp;Without showbase, parsing 3.14 as money gives 314</p>
<h2>See also</h2>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;clears the specified ios_base flags<br />
resetiosflags <i>(function)</i><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;sets the specified ios_base flags<br />
setiosflags <i>(function)</i> </p>
