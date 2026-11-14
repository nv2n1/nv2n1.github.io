---
title: "stdwmemset(3)"
name: "stdwmemset"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdwmemset/"
---

std::wmemset - std::wmemset

<h2>Synopsis</h2>

<pre><code>Defined in header &lt;cwchar&gt;

wchar_t* wmemset( wchar_t* dest, wchar_t ch, std::size_t count );</code></pre> 
Copies the wide character ch into each of the first count wide characters of the wide character array pointed to by dest. 
If overflow occurs, the behavior is undefined. 
If count is zero, the function does nothing. 

<h2>Parameters</h2>

dest - pointer to the wide character array to fill 
ch - fill wide character 
count - number of wide characters to fill

<h2>Return value</h2>

Returns a copy of dest 

<h2>Notes</h2>

This function is not locale-sensitive and pays no attention to the values of the wchar_t objects it writes: nulls as well as invalid wide characters are written too. 

<h2>Example</h2>

// Run this code <pre><code>#include &lt;iostream&gt;

#include &lt;cwchar&gt;

#include &lt;clocale&gt;

#include &lt;locale&gt;
int main()

{
    wchar_t ar[4] = {L'1', L'2', L'3', L'4'};
    std::wmemset(ar, L'\U0001f34c', 2); // replaces [12] with the &#x1f34c; bananas
    std::wmemset(ar + 2, L'蕉', 2);     // replaces [34] with the 蕉 bananas
    std::setlocale(LC_ALL, &quot;en_US.utf8&quot;);
    std::wcout.imbue(std::locale(&quot;en_US.utf8&quot;));
    std::wcout &lt;&lt; std::wstring(ar, 4) &lt;&lt; '\n';
}
</code></pre>

<h2>Possible output:</h2>

&nbsp;<wbr>&nbsp;蕉蕉

<h2>See also</h2>

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;fills a buffer with a character 
memset <i>(function)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;copies a certain amount of wide characters between two non-overlapping arrays 
wmemcpy <i>(function)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;copy-assigns the given value to N elements in a range 
fill_n <i>(function template)</i> 
