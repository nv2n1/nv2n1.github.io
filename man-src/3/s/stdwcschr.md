---
title: "stdwcschr(3)"
name: "stdwcschr"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdwcschr/"
---

std::wcschr - std::wcschr

<h2>Synopsis</h2>

<pre><code>Defined in header&lt;cwchar&gt;

    const wchar_t *wcschr(const wchar_t *str, wchar_t ch);

wchar_t *wcschr(wchar_t *str, wchar_t ch);</code></pre> 
Finds the first occurrence of the wide character ch in the wide string pointed to by str. 

<h2>Parameters</h2>

str - pointer to the null-terminated wide string to be analyzed 
ch - wide character to search for

<h2>Return value</h2>

Pointer to the found character in str, or NULL if no such character is found. 

<h2>Example</h2>

// Run this code <pre><code>#include &lt;iostream&gt;

#include &lt;cwchar&gt;

#include &lt;locale&gt;
int main()

{
    wchar_t arr[] = L&quot;招き猫 кошка&quot;;
    const wchar_t *cat = std::wcschr(arr, L'猫');
    const wchar_t *dog = std::wcschr(arr, L'犬');
    std::cout.imbue(std::locale(&quot;en_US.utf8&quot;));
    if (cat)
        std::cout &lt;&lt; &quot;The character 猫 found at position &quot; &lt;&lt; cat - arr &lt;&lt; '\n';
    else
        std::cout &lt;&lt; &quot;The character 猫 not found\n&quot;;
    if (dog)
        std::cout &lt;&lt; &quot;The character 犬 found at position &quot; &lt;&lt; dog - arr &lt;&lt; '\n';
    else
        std::cout &lt;&lt; &quot;The character 犬 not found\n&quot;;
}
</code></pre>

<h2>Output:</h2>

&nbsp;<wbr>&nbsp;The character 猫 found at position 2 
&nbsp;<wbr>&nbsp;The character 犬 not found

<h2>See also</h2>

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;find characters in the string 
find <i>(public member function of std::basic_string&lt;CharT,Traits,Allocator&gt;)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;finds the first occurrence of a character 
strchr <i>(function)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;finds the last occurrence of a wide character in a wide string 
wcsrchr <i>(function)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;finds the first location of any wide character in one wide string, in another wide string 
wcspbrk <i>(function)</i> 
