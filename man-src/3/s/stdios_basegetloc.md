---
title: "stdios_basegetloc(3)"
name: "stdios_basegetloc"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdios_basegetloc/"
---

std::ios_base::getloc - std::ios_base::getloc

<h2>Synopsis</h2>

<pre><code>std::locale getloc() const;</code></pre> 
Returns the current locale associated with the stream. 

<h2>Parameters</h2>

<i>(none)</i>

<h2>Return value</h2>

the locale object associated with the stream. 

<h2>Example</h2>

// Run this code <pre><code>#include &lt;iostream&gt;

#include &lt;ctime&gt;

#include &lt;iomanip&gt;

#include &lt;codecvt&gt;
int main()

{
    std::wbuffer_convert&lt;std::codecvt_utf8&lt;wchar_t&gt;&gt; conv(std::cout.rdbuf());
    std::wostream out(&amp;conv);
    out.imbue(std::locale(out.getloc(),
                          new std::time_put_byname&lt;wchar_t&gt;(&quot;ja_JP&quot;)));
    std::time_t t = std::time(NULL);
    out &lt;&lt; std::put_time(std::localtime(&amp;t), L&quot;%A %c&quot;) &lt;&lt; '\n';
}
</code></pre>

<h2>Output:</h2>

&nbsp;<wbr>&nbsp;土曜日 2013年09月14日 11時31分15秒

<h2>See also</h2>

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;sets locale 
imbue <i>(public member function)</i> 
