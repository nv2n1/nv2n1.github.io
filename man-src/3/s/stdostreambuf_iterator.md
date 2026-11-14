---
title: "stdostreambuf_iterator(3)"
name: "stdostreambuf_iterator"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdostreambuf_iterator/"
description: "std::ostreambuf_iterator<CharT,Traits>::ostreambuf_iterator – std::ostreambuf_iterator<CharT,Traits>::ostreambuf_iterator"
---

<p>std::ostreambuf_iterator&lt;CharT,Traits&gt;::ostreambuf_iterator &#8211; std::ostreambuf_iterator&lt;CharT,Traits&gt;::ostreambuf_iterator</p>
<h2>Synopsis</h2>
<p>ostreambuf_iterator( streambuf_type* buffer ) throw(); <i>(until C++11)</i><br />
ostreambuf_iterator( streambuf_type* buffer ) noexcept; <code>(1)</code> <i>(since C++11)</i><br />
ostreambuf_iterator( ostream_type&amp; stream ) throw(); <code>(2)</code> <i>(until C++11)</i><br />
ostreambuf_iterator( ostream_type&amp; stream ) noexcept; <i>(since C++11)</i><br />
1) Constructs the iterator with the private streambuf_type* member set to buffer and the failed() bit set to false. The behavior is undefined if buffer is a null pointer.<br />
2) Same as ostreambuf_iterator(stream.rdbuf()) </p>
<h2>Parameters</h2>
<p>stream &#8211; the output stream whose rdbuf() will be accessed by this iterator<br />
buffer &#8211; the output stream buffer to be accessed by this iterator</p>
<h2>Example</h2>
<p>// Run this code </p>
<pre><code>#include &lt;iostream&gt;

#include &lt;fstream&gt;

#include &lt;iterator&gt;

int main()

{
    std::basic_filebuf&lt;char&gt; f;
    f.open(&quot;test.txt&quot;, std::ios::out);
    std::ostreambuf_iterator&lt;char&gt; out1(&amp;f);
    std::ostreambuf_iterator&lt;wchar_t&gt; out2(std::wcout);
    *out1 = 'a';
    *out2 = L'a';
}
</code></pre>
