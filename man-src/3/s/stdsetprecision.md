---
title: "stdsetprecision(3)"
name: "stdsetprecision"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdsetprecision/"
description: "std::setprecision – std::setprecision"
---

<p>std::setprecision &#8211; std::setprecision</p>
<h2>Synopsis</h2>
<pre><code>Defined in header&lt;iomanip&gt;

/*unspecified*/ setprecision(int n);</code></pre>
<p>When used in an expression out &lt;&lt; <a href="/docs/linux/man/n-setprecision/">setprecision</a>(n) or in &gt;&gt; <a href="/docs/linux/man/n-setprecision/">setprecision</a>(n), sets the precision parameter of the stream out or in to exactly n. </p>
<h2>Parameters</h2>
<p>n &#8211; new value for precision</p>
<h2>Return value</h2>
<p>Returns an object of unspecified type such that if str is the name of an output stream of type std::basic_ostream&lt;CharT, Traits&gt; or an input stream of type std::basic_istream&lt;CharT, Traits&gt;, then the expression str &lt;&lt; setprecision(n) or str &gt;&gt; setprecision(n) behaves as if the following code was executed :</p>
<p>    str.precision(n);</p>
<h2>Example</h2>
<p>// Run this code </p>
<pre><code>#include &lt;iostream&gt;

#include &lt;iomanip&gt;

#include &lt;cmath&gt;

#include &lt;limits&gt;

int main()

{
    const long double pi = std::acos(-1.L);
    std::cout &lt;&lt; &quot;default precision (6): &quot; &lt;&lt; pi &lt;&lt; '
'
              &lt;&lt; &quot;std::setprecision(10): &quot; &lt;&lt; std::setprecision(10) &lt;&lt; pi &lt;&lt; '
'
              &lt;&lt; &quot;max precision:         &quot;
              &lt;&lt; std::setprecision(std::numeric_limits&lt;long double&gt;::digits10 + 1)
              &lt;&lt; pi &lt;&lt; '
';
}
</code></pre>
<h2>Output:</h2>
<p>&nbsp;<wbr>&nbsp;default precision <code>(6)</code>: 3.14159<br />
&nbsp;<wbr>&nbsp;std::setprecision<code>(10)</code>: 3.141592654<br />
&nbsp;<wbr>&nbsp;max precision: 3.141592653589793239</p>
<h2>See also</h2>
<p>fixed<br />
scientific<br />
hexfloat<br />
defaultfloat changes formatting used for floating-point I/O<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function)</i><br />
<i>(C++11)</i><br />
<i>(C++11)</i><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;manages decimal precision of floating point operations<br />
precision <i>(public member function of std::ios_base)</i> </p>
