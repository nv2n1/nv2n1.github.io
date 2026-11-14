---
title: "stdsub_matchoperatorstring_typestdsub_matchstr(3)"
name: "stdsub_matchoperatorstring_typestdsub_matchstr"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdsub_matchoperatorstring_typestdsub_matchstr/"
description: "std::sub_match<BidirIt>::operatorstring_type,std::sub_match<BidirIt>::str – std::sub_match<BidirIt>::operatorstring_type,std::sub_match<BidirIt>::str"
---

<p>std::sub_match&lt;BidirIt&gt;::operatorstring_type,std::sub_match&lt;BidirIt&gt;::str &#8211; std::sub_match&lt;BidirIt&gt;::operatorstring_type,std::sub_match&lt;BidirIt&gt;::str</p>
<h2>Synopsis</h2>
<p>operator string_type() const; <code>(1)</code><br />
string_type str() const; <code>(2)</code><br />
Converts to an object of the underlying std::basic_string type.<br />
The first version is an implicit conversion, the second one is explicit. </p>
<h2>Parameters</h2>
<p><i>(none)</i></p>
<h2>Return value</h2>
<p>Returns the matched character sequence as an object of the underlying std::basic_string type. If the matched member is false then the empty string is returned. </p>
<h2>Complexity</h2>
<p>Linear in the length of the underlying character sequence.</p>
<h2>Example</h2>
<p>// Run this code </p>
<pre><code>#include &lt;iostream&gt;

#include &lt;regex&gt;

#include &lt;string&gt;

int main()

{
    std::ssub_match sm;
    std::string s = sm; // implicit conversion
    std::cout &lt;&lt; s.length() &lt;&lt; '
';
}
</code></pre>
<h2>Output:</h2>
<p>&nbsp;<wbr>&nbsp;0</p>
