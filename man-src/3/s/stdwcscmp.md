---
title: "stdwcscmp(3)"
name: "stdwcscmp"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdwcscmp/"
---

std::wcscmp - std::wcscmp

<h2>Synopsis</h2>

<pre><code>Defined in header&lt;cwchar&gt;

    int wcscmp(const wchar_t *lhs, const wchar_t *rhs);</code></pre> 
Compares two null-terminated wide strings lexicographically. 
The sign of the result is the sign of the difference between the values of the first pair of wide characters that differ in the strings being compared. 
The behavior is undefined if lhs or rhs are not pointers to null-terminated wide strings. 

<h2>Parameters</h2>

lhs, rhs - pointers to the null-terminated wide strings to compare

<h2>Return value</h2>

Negative value if lhs appears before rhs in lexicographical order. 
Zero if lhs and rhs compare equal. 
Positive value if lhs appears after rhs in lexicographical order. 

<h2>Notes</h2>

This function is not locale-sensitive, unlike std::wcscoll, and the order may not be meaningful when characters from different Unicode blocks are used together or when the order of code units does not match collation order. 

<h2>Example</h2>

// Run this code <pre><code>#include &lt;vector&gt;

#include &lt;cwchar&gt;

#include &lt;algorithm&gt;

#include &lt;iostream&gt;
int main()

{
    std::vector&lt;const wchar_t *&gt; leaders{L&quot;Ленин&quot;, L&quot;Сталин&quot;, L&quot;Маленков&quot;,
                                         L&quot;Хрущёв&quot;, L&quot;Брежнев&quot;, L&quot;Андропов&quot;, L&quot;Черненко&quot;, L&quot;Горбачёв&quot;};
    std::sort(leaders.begin(), leaders.end(), [](auto strA, auto strB) {
        return std::wcscmp(strA, strB) &lt; 0;
    });
    std::setlocale(LC_ALL, &quot;en_US.utf8&quot;);
    std::wcout.imbue(std::locale(&quot;en_US.utf8&quot;));
    for (auto leader : leaders)
        std::wcout &lt;&lt; leader &lt;&lt; '\n';
}
</code></pre>

<h2>Possible output:</h2>

&nbsp;<wbr>&nbsp;Андропов 
&nbsp;<wbr>&nbsp;Брежнев 
&nbsp;<wbr>&nbsp;Горбачёв 
&nbsp;<wbr>&nbsp;Ленин 
&nbsp;<wbr>&nbsp;Маленков 
&nbsp;<wbr>&nbsp;Сталин 
&nbsp;<wbr>&nbsp;Хрущёв 
&nbsp;<wbr>&nbsp;Черненко

<h2>See also</h2>

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;compares a certain amount of characters from two wide strings 
wcsncmp <i>(function)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;compares a certain amount of wide characters from two arrays 
wmemcmp <i>(function)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;compares two strings 
strcmp <i>(function)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;compares two wide strings in accordance to the current locale 
wcscoll <i>(function)</i> 
