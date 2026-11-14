---
title: "stdwmemchr(3)"
name: "stdwmemchr"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdwmemchr/"
---

std::wmemchr - std::wmemchr

<h2>Synopsis</h2>

<pre><code>Defined in header&lt;cwchar&gt;

    const wchar_t *wmemchr(const wchar_t *ptr, wchar_t ch, std::size_t count);

wchar_t *wmemchr(wchar_t *ptr, wchar_t ch, std::size_t count);</code></pre> 
Locates the first occurrence of wide character ch in the initial count wide characters of the wide character array pointed to by ptr. 
If count is zero, the function returns a null pointer. 

<h2>Parameters</h2>

ptr - pointer to the wide character array to be examined 
ch - wide character to search for 
count - number of wide characters to examine

<h2>Return value</h2>

Pointer to the location of the wide character, or a null pointer if no such character is found. 

<h2>Example</h2>

// Run this code <pre><code>#include &lt;iostream&gt;

#include &lt;cwchar&gt;

#include &lt;clocale&gt;

#include &lt;locale&gt;
int main()

{
    const wchar_t str[] = L&quot;诺不轻信，故人不负我\0诺不轻许，故我不负人。&quot;;
    wchar_t target = L'许';
    const std::size_t sz = sizeof str / sizeof *str;
    if (const wchar_t *result = std::wmemchr(str, target, sz)) {
        std::setlocale(LC_ALL, &quot;en_US.utf8&quot;);
        std::wcout.imbue(std::locale(&quot;en_US.utf8&quot;));
        std::wcout &lt;&lt; &quot;Found '&quot; &lt;&lt; target
                   &lt;&lt; &quot;' at position &quot; &lt;&lt; result - str &lt;&lt; &quot;\n&quot;;
    }
}
</code></pre>

<h2>Possible output:</h2>

&nbsp;<wbr>&nbsp;Found '许' at position 14

<h2>See also</h2>

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;searches an array for the first occurrence of a character 
memchr <i>(function)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;finds the first occurrence of a character 
strchr <i>(function)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;finds the first occurrence of a wide character in a wide string 
wcschr <i>(function)</i> 
find 
find_if 
find_if_not finds the first element satisfying specific criteria 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function template)</i> 
<i>(C++11)</i> 
