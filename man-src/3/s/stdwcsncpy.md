---
title: "stdwcsncpy(3)"
name: "stdwcsncpy"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdwcsncpy/"
---

std::wcsncpy - std::wcsncpy

<h2>Synopsis</h2>

<pre><code>Defined in header&lt;cwchar&gt;

    wchar_t *wcsncpy(wchar_t *dest, const wchar_t *src, std::size_t count);</code></pre> 
Copies at most count characters of the wide string pointed to by src (including the terminating null wide character) to wide character array pointed to by dest. 
If count is reached before the entire string src was copied, the resulting wide character array is not null-terminated. 
If, after copying the terminating null wide character from src, count is not reached, additional null wide characters are written to dest until the total of count characters have been written. 
If the strings overlap, the behavior is undefined. 

<h2>Parameters</h2>

dest - pointer to the wide character array to copy to 
src - pointer to the wide string to copy from 
count - maximum number of wide characters to copy

<h2>Return value</h2>

dest 

<h2>Notes</h2>

In typical usage, count is the size of the destination array. 

<h2>Example</h2>

// Run this code <pre><code>#include &lt;iostream&gt;

#include &lt;cwchar&gt;
int main()

{
    wchar_t src[] = L&quot;hi&quot;;
    wchar_t dest[6] = {L'a', L'b', L'c', L'd', L'e', L'f'};
    std::wcsncpy(dest, src, 5); // this will copy hi and repeat \0 three times
    std::wcout &lt;&lt; &quot;The contents of dest are: &quot;;
    for (wchar_t c : dest) {
        if (c)
            std::wcout &lt;&lt; c &lt;&lt; ' ';
        else
            std::wcout &lt;&lt; &quot;\\0&quot; &lt;&lt; ' ';
    }
    std::wcout &lt;&lt; '\n';
}
</code></pre>

<h2>Output:</h2>

&nbsp;<wbr>&nbsp;The contents of dest are: h i \0 \0 \0 f

<h2>See also</h2>

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;copies one wide string to another 
wcscpy <i>(function)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;copies a certain amount of wide characters between two non-overlapping arrays 
wmemcpy <i>(function)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;copies a certain amount of characters from one string to another 
strncpy <i>(function)</i> 
