---
title: "stdbitsetallstdbitsetanystdbitsetnone(3)"
name: "stdbitsetallstdbitsetanystdbitsetnone"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdbitsetallstdbitsetanystdbitsetnone/"
description: "std::bitset<N>::all,std::bitset<N>::any,std::bitset<N>::none – std::bitset<N>::all,std::bitset<N>::any,std::bitset<N>::none"
---

<p>std::bitset&lt;N&gt;::all,std::bitset&lt;N&gt;::any,std::bitset&lt;N&gt;::none &#8211; std::bitset&lt;N&gt;::all,std::bitset&lt;N&gt;::any,std::bitset&lt;N&gt;::none</p>
<h2>Synopsis</h2>
<p>bool all() const noexcept; <code>(1)</code> <i>(since C++11)</i><br />
bool any() const; <i>(until C++11)</i><br />
bool any() const noexcept; <code>(2)</code> <i>(since C++11)</i><br />
bool none() const; <code>(3)</code> <i>(until C++11)</i><br />
bool none() const noexcept; <i>(since C++11)</i><br />
Checks if all, any or none of the bits are set to true.<br />
1) Checks if all bits are set to true<br />
2) Checks if any bits are set to true<br />
3) Checks if none of the bits are set to true </p>
<h2>Parameters</h2>
<p><i>(none)</i></p>
<h2>Return value</h2>
<p>1) true if all bits are set to true, otherwise false<br />
2) true if any of the bits are set to true, otherwise false<br />
3) true if none of the bits are set to true, otherwise false </p>
<h2>Example</h2>
<p>// Run this code </p>
<pre><code>#include &lt;iostream&gt;

#include &lt;bitset&gt;
int main()

{
    std::bitset&lt;4&gt; b1(&quot;0000&quot;);
    std::bitset&lt;4&gt; b2(&quot;0101&quot;);
    std::bitset&lt;4&gt; b3(&quot;1111&quot;);
    std::cout &lt;&lt; &quot;bitset	&quot;
              &lt;&lt; &quot;all	&quot;
              &lt;&lt; &quot;any	&quot;
              &lt;&lt; &quot;none
&quot;;
    std::cout &lt;&lt; b1 &lt;&lt; '	' &lt;&lt; b1.all() &lt;&lt; '	' &lt;&lt; b1.any() &lt;&lt; '	' &lt;&lt; b1.none() &lt;&lt; '
';
    std::cout &lt;&lt; b2 &lt;&lt; '	' &lt;&lt; b2.all() &lt;&lt; '	' &lt;&lt; b2.any() &lt;&lt; '	' &lt;&lt; b2.none() &lt;&lt; '
';
    std::cout &lt;&lt; b3 &lt;&lt; '	' &lt;&lt; b3.all() &lt;&lt; '	' &lt;&lt; b3.any() &lt;&lt; '	' &lt;&lt; b3.none() &lt;&lt; '
';
}
</code></pre>
<h2>Output:</h2>
<p>&nbsp;<wbr>&nbsp;bitset all any none<br />
&nbsp;<wbr>&nbsp;0000 0 0 1<br />
&nbsp;<wbr>&nbsp;0101 0 1 0<br />
&nbsp;<wbr>&nbsp;1111 1 1 0</p>
