---
title: "stdsetw(3)"
name: "stdsetw"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdsetw/"
description: "std::setw – std::setw"
---

<p>std::setw &#8211; std::setw</p>
<h2>Synopsis</h2>
<pre><code>Defined in header&lt;iomanip&gt;

/*unspecified*/ setw(int n);</code></pre>
<p>When used in an expression out &lt;&lt; <a href="/docs/linux/man/n-setw/">setw</a>(n) or in &gt;&gt; <a href="/docs/linux/man/n-setw/">setw</a>(n), sets the width parameter of the stream out or in to exactly n. </p>
<h2>Parameters</h2>
<p>n &#8211; new value for width</p>
<h2>Return value</h2>
<p>Returns an object of unspecified type such that if str is the name of an output stream of type std::basic_ostream&lt;CharT, Traits&gt; or std::basic_istream&lt;CharT, Traits&gt;, then the expression str &lt;&lt; setw(n) or str &gt;&gt; setw(n) behaves as if the following code was executed :</p>
<p>    str.width(n);</p>
<h2>Notes</h2>
<p>The width property of the stream will be reset to zero (meaning &quot;unspecified&quot;) if any of the following functions are called:<br />
* Input<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;* operator&gt;&gt;(basic_istream&amp;,_basic_string&amp;)<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;* operator&gt;&gt;(basic_istream&amp;,_char*)<br />
* Output<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;* Overloads 1-7 of basic_ostream::operator&lt;&lt;() (at Stage 3 of num_put::put())<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;* operator&lt;&lt;(basic_ostream&amp;,_char) and operator&lt;&lt;(basic_ostream&amp;,_char*)<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;* operator&lt;&lt;(basic_ostream&amp;,_basic_string&amp;)<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;* std::put_money (inside money_put::put())<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;* std::quoted (when used with an output stream)<br />
The exact effects this modifier has on the input and output vary between the individual I/O functions and are described at each operator&lt;&lt; and operator&gt;&gt; overload page individually. </p>
<h2>Example</h2>
<p>// Run this code </p>
<pre><code>#include &lt;sstream&gt;

#include &lt;iostream&gt;

#include &lt;iomanip&gt;
int main()

{
    std::cout &lt;&lt; &quot;no setw:&quot; &lt;&lt; 42 &lt;&lt; '
'
              &lt;&lt; &quot;setw(6):&quot; &lt;&lt; std::setw(6) &lt;&lt; 42 &lt;&lt; '
'
              &lt;&lt; &quot;setw(6), several elements: &quot; &lt;&lt; 89 &lt;&lt; std::setw(6) &lt;&lt; 12 &lt;&lt; 34 &lt;&lt; '
';
    std::istringstream is(&quot;hello, world&quot;);
    char arr[10];
    is &gt;&gt; std::setw(6) &gt;&gt; arr;
    std::cout &lt;&lt; &quot;Input from \&quot;&quot; &lt;&lt; is.str() &lt;&lt; &quot;\&quot; with setw(6) gave \&quot;&quot;
              &lt;&lt; arr &lt;&lt; &quot;\&quot;
&quot;;
}
</code></pre>
<h2>Output:</h2>
<p>&nbsp;<wbr>&nbsp;no setw:42<br />
&nbsp;<wbr>&nbsp;<a href="/docs/linux/man/6-setw/">setw</a><code>(6)</code>: 42<br />
&nbsp;<wbr>&nbsp;<a href="/docs/linux/man/6-setw/">setw</a><code>(6)</code>, several elements: 89 1234<br />
&nbsp;<wbr>&nbsp;Input from &quot;hello, world&quot; with <a href="/docs/linux/man/6-setw/">setw</a><code>(6)</code> gave &quot;hello&quot;</p>
<h2>See also</h2>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;manages field width<br />
width <i>(public member function of std::ios_base)</i><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;changes the fill character<br />
setfill <i>(function template)</i><br />
internal sets the placement of fill characters<br />
left <i>(function)</i><br />
right </p>
