---
title: "stdwmemcpy(3)"
name: "stdwmemcpy"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdwmemcpy/"
---

std::wmemcpy - std::wmemcpy

<h2>Synopsis</h2>

<pre><code>Defined in header&lt;cwchar&gt;

    wchar_t *wmemcpy(wchar_t *dest, const wchar_t *src, std::size_t count);</code></pre> 
Copies exactly count successive wide characters from the wide character array pointed to by src to the wide character array pointed to by dest. If the objects overlap, the behavior is undefined. If count is zero, the function does nothing. 

<h2>Parameters</h2>

dest - pointer to the wide character array to copy to 
src - pointer to the wide character array to copy from 
count - number of wide characters to copy

<h2>Return value</h2>

dest 

<h2>Notes</h2>

This function's analog for byte strings is std::strncpy, not std::strcpy. 
This function is not locale-sensitive and pays no attention to the values of the wchar_t objects it copies: nulls as well as invalid characters are copied too. 

<h2>Example</h2>

// Run this code <pre><code>#include &lt;iostream&gt;

#include &lt;cwchar&gt;

#include &lt;clocale&gt;

#include &lt;locale&gt;
int main(void)

{
    wchar_t from1[] = L&quot;नमस्ते&quot;;
    const size_t sz1 = sizeof from1 / sizeof *from1;
    wchar_t from2[] = L&quot;Բարև&quot;;
    const size_t sz2 = sizeof from2 / sizeof *from2;
    wchar_t to[sz1 + sz2];
    std::wmemcpy(to, from1, sz1);       // copy from1, along with its null terminator
    std::wmemcpy(to + sz1, from2, sz2); // append from2, along with its null terminator
    std::setlocale(LC_ALL, &quot;en_US.utf8&quot;);
    std::cout.imbue(std::locale(&quot;en_US.utf8&quot;));
    std::wcout &lt;&lt; &quot;Wide array contains: &quot;;
    for (size_t n = 0; n &lt; sizeof to / sizeof *to; ++n)
        if (to[n])
            std::wcout &lt;&lt; to[n];
        else
            std::wcout &lt;&lt; &quot;\\0&quot;;
    std::wcout &lt;&lt; '\n';
}
</code></pre>

<h2>Possible output:</h2>

&nbsp;<wbr>&nbsp;Wide array contains: नमस्ते\0Բարև\0

<h2>See also</h2>

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;copies a certain amount of characters from one string to another 
strncpy <i>(function)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;copies a certain amount of wide characters between two, possibly overlapping, arrays 
wmemmove <i>(function)</i> 
