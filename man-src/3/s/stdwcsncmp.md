---
title: "stdwcsncmp(3)"
name: "stdwcsncmp"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdwcsncmp/"
---

std::wcsncmp - std::wcsncmp

<h2>Synopsis</h2>

<pre><code>Defined in header&lt;cwchar&gt;

    int wcsncmp(const wchar_t *lhs, const wchar_t *rhs, std::size_t count);</code></pre> 
Compares at most count wide characters of two null-terminated wide strings. The comparison is done lexicographically. 
The sign of the result is the sign of the difference between the values of the first pair of wide characters that differ in the strings being compared. 
The behavior is undefined if lhs or rhs are not pointers to null-terminated strings. 

<h2>Parameters</h2>

lhs, rhs - pointers to the null-terminated wide strings to compare 
count - maximum number of characters to compare

<h2>Return value</h2>

Negative value if lhs appears before rhs in lexicographical order. 
Zero if lhs and rhs compare equal. 
Positive value if lhs appears after rhs in lexicographical order. 

<h2>Example</h2>

// Run this code <pre><code>#include &lt;iostream&gt;

#include &lt;cwchar&gt;

#include &lt;clocale&gt;

#include &lt;locale&gt;
void demo(const wchar_t *lhs, const wchar_t *rhs, int sz)

{
    int rc = std::wcsncmp(lhs, rhs, sz);
    if (rc == 0)
        std::wcout &lt;&lt; &quot;First &quot; &lt;&lt; sz &lt;&lt; &quot; characters of [&quot;
                   &lt;&lt; lhs &lt;&lt; &quot;] equal [&quot; &lt;&lt; rhs &lt;&lt; &quot;]\n&quot;;
    else if (rc &lt; 0)
        std::wcout &lt;&lt; &quot;First &quot; &lt;&lt; sz &lt;&lt; &quot; characters of [&quot;
                   &lt;&lt; lhs &lt;&lt; &quot;] precede [&quot; &lt;&lt; rhs &lt;&lt; &quot;]\n&quot;;
    else if (rc &gt; 0)
        std::wcout &lt;&lt; &quot;First &quot; &lt;&lt; sz &lt;&lt; &quot; characters of [&quot;
                   &lt;&lt; lhs &lt;&lt; &quot;] follow [&quot; &lt;&lt; rhs &lt;&lt; &quot;]\n&quot;;
}
int main()

{
    const wchar_t str1[] = L&quot;안녕하세요&quot;;
    const wchar_t str2[] = L&quot;안녕히 가십시오&quot;;
    std::setlocale(LC_ALL, &quot;en_US.utf8&quot;);
    std::wcout.imbue(std::locale(&quot;en_US.utf8&quot;));
    demo(str1, str2, 5);
    demo(str2, str1, 8);
    demo(str1, str2, 2);
}
</code></pre>

<h2>Output:</h2>

&nbsp;<wbr>&nbsp;First 5 characters of [안녕하세요] precede [안녕히 가십시오] 
&nbsp;<wbr>&nbsp;First 8 characters of [안녕히 가십시오] follow [안녕하세요] 
&nbsp;<wbr>&nbsp;First 2 characters of [안녕하세요] equal [안녕히 가십시오]

<h2>See also</h2>

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;compares a certain number of characters from two strings 
strncmp <i>(function)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;compares two wide strings 
wcscmp <i>(function)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;compares a certain amount of wide characters from two arrays 
wmemcmp <i>(function)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;compares two wide strings in accordance to the current locale 
wcscoll <i>(function)</i> 
