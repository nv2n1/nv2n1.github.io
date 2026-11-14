---
title: "stdwcscat(3)"
name: "stdwcscat"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdwcscat/"
---

std::wcscat - std::wcscat

<h2>Synopsis</h2>

<pre><code>Defined in header&lt;cwchar&gt;

    wchar_t *wcscat(wchar_t *dest, const wchar_t *src);</code></pre> 
Appends a copy of the wide string pointed to by src to the end of the wide string pointed to by dest. The wide character src[0] replaces the null terminator at the end of dest. The resulting wide string is null-terminated. 
The behavior is undefined if the destination array is not large enough for the contents of both str and dest and the terminating null wide character. 
The behavior is undefined if the strings overlap. 

<h2>Parameters</h2>

dest - pointer to the null-terminated wide string to append to 
src - pointer to the null-terminated wide string to copy from

<h2>Return value</h2>

Returns a copy of dest 

<h2>Example</h2>

// Run this code <pre><code>#include &lt;iostream&gt;

#include &lt;cwchar&gt;

#include &lt;clocale&gt;
int main(void)

{
    wchar_t str[50] = L&quot;Земля, прощай.&quot;;
    std::wcscat(str, L&quot; &quot;);
    std::wcscat(str, L&quot;В добрый путь.&quot;);
    std::setlocale(LC_ALL, &quot;en_US.utf8&quot;);
    std::wcout.imbue(std::locale(&quot;en_US.utf8&quot;));
    std::wcout &lt;&lt; str &lt;&lt; '\n';
}
</code></pre>

<h2>Possible output:</h2>

&nbsp;<wbr>&nbsp;Земля, прощай. В добрый путь.

<h2>See also</h2>

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;appends a certain amount of wide characters from one wide string to another 
wcsncat <i>(function)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;concatenates two strings 
strcat <i>(function)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;copies one wide string to another 
wcscpy <i>(function)</i> 
