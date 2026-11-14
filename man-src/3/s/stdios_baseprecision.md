---
title: "stdios_baseprecision(3)"
name: "stdios_baseprecision"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdios_baseprecision/"
description: "std::ios_base::precision – std::ios_base::precision"
---

<p>std::ios_base::precision &#8211; std::ios_base::precision</p>
<h2>Synopsis</h2>
<p>streamsize precision() const; <code>(1)</code><br />
streamsize precision( streamsize new_precision ); <code>(2)</code><br />
Manages the precision (i.e. how many digits are generated) of floating point output performed by std::num_put::do_put.<br />
1) Returns the current precision.<br />
2) Sets the precision to the given one. Returns the previous precision.<br />
The default precision, as established by std::basic_ios::init, is 6. </p>
<h2>Parameters</h2>
<p>new_precision &#8211; new precision setting</p>
<h2>Return value</h2>
<p>the precision before the call to the function </p>
<h2>Example</h2>
<p>// Run this code </p>
<pre><code>#include &lt;iostream&gt;

int main()

{
    const double d = 1.2345678901234;
    std::cout &lt;&lt; &quot;The  default precision is &quot; &lt;&lt; std::cout.precision() &lt;&lt; &quot;

&quot;;
    std::cout &lt;&lt; &quot;With default precision d is &quot; &lt;&lt; d &lt;&lt; '
';
    std::cout.precision(12);
    std::cout &lt;&lt; &quot;With high    precision d is &quot; &lt;&lt; d &lt;&lt; '
';
}
</code></pre>
<h2>Output:</h2>
<p>&nbsp;<wbr>&nbsp;The default precision is 6 </p>
<p>&nbsp;<wbr>&nbsp;With default precision d is 1.23457<br />
&nbsp;<wbr>&nbsp;With high precision d is 1.23456789012</p>
<h2>See also</h2>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;manages field width<br />
width <i>(public member function)</i><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;changes floating-point precision<br />
setprecision <i>(function)</i> </p>
