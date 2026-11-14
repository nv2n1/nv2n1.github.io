---
title: "stdwcscpy(3)"
name: "stdwcscpy"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdwcscpy/"
---

std::wcscpy - std::wcscpy

<h2>Synopsis</h2>

<pre><code>Defined in header&lt;cwchar&gt;

    wchar_t *wcscpy(wchar_t *dest, const wchar_t *src);</code></pre> 
Copies the wide string pointed to by src (including the terminating null wide character) to wide character array pointed to by dest. 
If the strings overlap, the behavior is undefined. 

<h2>Parameters</h2>

dest - pointer to the wide character array to copy to 
src - pointer to the null-terminated wide string to copy from

<h2>Return value</h2>

dest 

<h2>Example</h2>

// Run this code <pre><code>#include &lt;iostream&gt;

#include &lt;cwchar&gt;

#include &lt;memory&gt;

#include &lt;clocale&gt;
int main()

{
    const wchar_t *src = L&quot;犬 means dog&quot;;

    //  src[0] = L'狗'; // can't modify string literal
    auto dst = std::make_unique&lt;wchar_t[]&gt;(std::wcslen(src) + 1); // +1 for the null
    std::wcscpy(dst.get(), src);
    dst[0] = L'狗';
    std::setlocale(LC_ALL, &quot;en_US.utf8&quot;);
    std::wcout.imbue(std::locale(&quot;&quot;));
    std::wcout &lt;&lt; src &lt;&lt; '\n'
               &lt;&lt; dst.get() &lt;&lt; '\n';
}
</code></pre>

<h2>Output:</h2>

&nbsp;<wbr>&nbsp;犬 means dog 
&nbsp;<wbr>&nbsp;狗 means dog

<h2>See also</h2>

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;copies a certain amount of wide characters from one string to another 
wcsncpy <i>(function)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;copies a certain amount of wide characters between two non-overlapping arrays 
wmemcpy <i>(function)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;copies one string to another 
strcpy <i>(function)</i> 
