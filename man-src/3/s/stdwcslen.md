---
title: "stdwcslen(3)"
name: "stdwcslen"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdwcslen/"
---

std::wcslen - std::wcslen

<h2>Synopsis</h2>

<pre><code>Defined in header&lt;cwchar&gt;

    std::size_t wcslen(const wchar_t *str);</code></pre> 
Returns the length of a wide string, that is the number of non-null wide characters that precede the terminating null wide character. 
The behavior is undefined if there is no null character in the wide character array pointed to by str. 

<h2>Parameters</h2>

str - pointer to the null-terminated wide string to be examined

<h2>Return value</h2>

The length of the null-terminated wide string str. 

<h2>Example</h2>

// Run this code <pre><code>#include &lt;iostream&gt;

#include &lt;cwchar&gt;

#include &lt;clocale&gt;
int main()

{
    const wchar_t *str = L&quot;爆ぜろリアル！弾けろシナプス！パニッシュメントディス、ワールド！&quot;;
    std::setlocale(LC_ALL, &quot;en_US.utf8&quot;);
    std::wcout.imbue(std::locale(&quot;en_US.utf8&quot;));
    std::wcout &lt;&lt; &quot;The length of \&quot;&quot; &lt;&lt; str &lt;&lt; &quot;\&quot; is &quot; &lt;&lt; std::wcslen(str) &lt;&lt; '\n';
}
</code></pre>

<h2>Output:</h2>

&nbsp;<wbr>&nbsp;The length of &quot;爆ぜろリアル！弾けろシナプス！パニッシュメントディス、ワールド！&quot; is 32

<h2>See also</h2>

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;returns the length of a given string 
strlen <i>(function)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;returns the number of bytes in the next multibyte character 
mblen <i>(function)</i> 
