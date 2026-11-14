---
title: "stdbasic_stringstream(3)"
name: "stdbasic_stringstream"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdbasic_stringstream/"
description: "std::basic_stringstream<CharT,Traits,Allocator>::str – std::basic_stringstream<CharT,Traits,Allocator>::str"
---

<p>std::basic_stringstream&lt;CharT,Traits,Allocator&gt;::str &#8211; std::basic_stringstream&lt;CharT,Traits,Allocator&gt;::str</p>
<h2>Synopsis</h2>
<p>std::basic_string&lt;CharT,Traits,Allocator&gt; str() const; <code>(1)</code><br />
void str(const std::basic_string&lt;CharT,Traits,Allocator&gt;&amp; new_str); <code>(2)</code><br />
Manages the contents of the underlying string object.<br />
1) Returns a copy of the underlying string as if by calling rdbuf()-&gt;str().<br />
2) Replaces the contents of the underlying string as if by calling rdbuf()-&gt;str(new_str). </p>
<h2>Parameters</h2>
<p>new_str &#8211; new contents of the underlying string</p>
<h2>Return value</h2>
<p>1) a copy of the underlying string object.<br />
2) <i>(none)</i> </p>
<h2>Notes</h2>
<p>The copy of the underlying string returned by str is a temporary object that will be destructed at the end of the expression, so directly calling c_str() on the result of str() (for example in auto *ptr = out.str().c_str();) results in a dangling pointer. </p>
<h2>Example</h2>
<p>// Run this code </p>
<pre><code>#include &lt;sstream&gt;

#include &lt;iostream&gt;

int main()

{
    int n;
    std::istringstream in; // could also use in(&quot;1 2&quot;)
    in.str(&quot;1 2&quot;);
    in &gt;&gt; n;
    std::cout &lt;&lt; &quot;after reading the first int from \&quot;1 2\&quot;, the int is &quot;
              &lt;&lt; n &lt;&lt; &quot;, str() = \&quot;&quot; &lt;&lt; in.str() &lt;&lt; &quot;\&quot;
&quot;;
    std::ostringstream out(&quot;1 2&quot;);
    out &lt;&lt; 3;
    std::cout &lt;&lt; &quot;after writing the int '3' to output stream \&quot;1 2\&quot;&quot;
              &lt;&lt; &quot;, str() = \&quot;&quot; &lt;&lt; out.str() &lt;&lt; &quot;\&quot;
&quot;;
    std::ostringstream ate(&quot;1 2&quot;, std::ios_base::ate);
    ate &lt;&lt; 3;
    std::cout &lt;&lt; &quot;after writing the int '3' to append stream \&quot;1 2\&quot;&quot;
              &lt;&lt; &quot;, str() = \&quot;&quot; &lt;&lt; ate.str() &lt;&lt; &quot;\&quot;
&quot;;
}
</code></pre>
<h2>Output:</h2>
<p>&nbsp;<wbr>&nbsp;after reading the first int from &quot;1 2&quot;, the int is 1, str() = &quot;1 2&quot;<br />
&nbsp;<wbr>&nbsp;after writing the int &#8216;3&#8217; to output stream &quot;1 2&quot;, str() = &quot;3 2&quot;<br />
&nbsp;<wbr>&nbsp;after writing the int &#8216;3&#8217; to append stream &quot;1 2&quot;, str() = &quot;1 23&quot;</p>
<h2>See also</h2>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;replaces or obtains a copy of the associated character string<br />
str <i>(public member function of std::basic_stringbuf&lt;CharT,Traits,Allocator&gt;)</i> </p>
