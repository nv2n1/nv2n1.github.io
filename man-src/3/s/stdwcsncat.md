---
title: "stdwcsncat(3)"
name: "stdwcsncat"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdwcsncat/"
---

std::wcsncat - std::wcsncat

<h2>Synopsis</h2>

<pre><code>Defined in header&lt;cwchar&gt;

    wchar_t *wcsncat(wchar_t *dest, const wchar_t *src, std::size_t count);</code></pre> 
Appends at most count wide characters from the wide string pointed to by src to the end of the character string pointed to by dest, stopping if the null terminator is copied. The wide character src[0] replaces the null terminator at the end of dest. The null terminator is always appended in the end (so the maximum number of wide characters the function may write is count+1). 
The behavior is undefined if the destination array is not large enough for the contents of both str and dest and the terminating null wide character. 
The behavior is undefined if the strings overlap. 

<h2>Parameters</h2>

dest - pointer to the null-terminated wide string to append to 
src - pointer to the null-terminated wide string to copy from 
count - maximum number of wide characters to copy

<h2>Return value</h2>

dest 

<h2>Example</h2>

// Run this code <pre><code>#include &lt;cwchar&gt;

#include &lt;iostream&gt;

#include &lt;clocale&gt;
int main(void)

{
    wchar_t str[50] = L&quot;Земля, прощай.&quot;;
    std::wcsncat(str, L&quot; &quot;, 1);
    std::wcsncat(str, L&quot;В добрый путь.&quot;, 8); // only append the first 8 wide chars
    std::setlocale(LC_ALL, &quot;en_US.utf8&quot;);
    std::wcout.imbue(std::locale(&quot;en_US.utf8&quot;));
    std::wcout &lt;&lt; str &lt;&lt; '\n';
}
</code></pre>

<h2>Possible output:</h2>

&nbsp;<wbr>&nbsp;Земля, прощай. В добрый

<h2>See also</h2>

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;appends a copy of one wide string to another 
wcscat <i>(function)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;concatenates a certain amount of characters of two strings 
strncat <i>(function)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;copies one wide string to another 
wcscpy <i>(function)</i> 
