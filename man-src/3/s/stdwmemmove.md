---
title: "stdwmemmove(3)"
name: "stdwmemmove"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdwmemmove/"
---

std::wmemmove - std::wmemmove

<h2>Synopsis</h2>

<pre><code>Defined in header&lt;cwchar&gt;

    wchar_t *wmemmove(wchar_t *dest, const wchar_t *src, std::size_t count);</code></pre> 
Copies exactly count successive wide characters from the wide character array pointed to by src to the wide character array pointed to by dest. 
If count is zero, the function does nothing. 
The arrays may overlap: copying takes place as if the wide characters were copied to a temporary wide character array and then copied from the temporary array to dest. 

<h2>Parameters</h2>

dest - pointer to the wide character array to copy to 
src - pointer to the wide character array to copy from 
count - number of wide characters to copy

<h2>Return value</h2>

Returns a copy of dest 

<h2>Notes</h2>

This function is not locale-sensitive and pays no attention to the values of the wchar_t objects it copies: nulls as well as invalid characters are copied too. 

<h2>Example</h2>

// Run this code <pre><code>#include &lt;iostream&gt;

#include &lt;cwchar&gt;

#include &lt;locale&gt;

#include &lt;clocale&gt;
int main()

{
    std::setlocale(LC_ALL, &quot;en_US.utf8&quot;);
    std::wcout.imbue(std::locale(&quot;en_US.utf8&quot;));
    wchar_t str[] = L&quot;αβγδεζηθικλμνξοπρστυφχψω&quot;;
    std::wcout &lt;&lt; str &lt;&lt; '\n';
    std::wmemmove(str + 4, str + 3, 3); // copy from [δεζ] to [εζη]
    std::wcout &lt;&lt; str &lt;&lt; '\n';
}
</code></pre>

<h2>Possible output:</h2>

&nbsp;<wbr>&nbsp;αβγδεζηθικλμνξοπρστυφχψω 
&nbsp;<wbr>&nbsp;αβγδδεζθικλμνξοπρστυφχψω

<h2>See also</h2>

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;copies a certain amount of wide characters between two non-overlapping arrays 
wmemcpy <i>(function)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;moves one buffer to another 
memmove <i>(function)</i> 
copy 
copy_if copies a range of elements to a new location 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function template)</i> 
<i>(C++11)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;copies a range of elements in backwards order 
copy_backward <i>(function template)</i> 
