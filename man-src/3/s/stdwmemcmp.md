---
title: "stdwmemcmp(3)"
name: "stdwmemcmp"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdwmemcmp/"
---

std::wmemcmp - std::wmemcmp

<h2>Synopsis</h2>

<pre><code>Defined in header&lt;cwchar&gt;

    int wmemcmp(const wchar_t *lhs, const wchar_t *rhs, std::size_t count);</code></pre> 
Compares the first count wide characters of the wide character arrays pointed to by lhs and rhs. The comparison is done lexicographically. 
The sign of the result is the sign of the difference between the values of the first pair of wide characters that differ in the arrays being compared. 
If count is zero, the function does nothing. 

<h2>Parameters</h2>

lhs, rhs - pointers to the wide character arrays to compare 
count - number of wide characters to examine

<h2>Return value</h2>

Negative value if the value of the first differing wide character in lhs is less than the value of the corresponding wide character in rhs: lhs precedes rhs in lexicographical order. 
0 if all count wide characters of lhs and rhs are equal. 
Positive value if the value of the first differing wide character in lhs is greater than the value of the corresponding wide character in rhs: rhs precedes lhs in lexicographical order. 

<h2>Notes</h2>

This function is not locale-sensitive and pays no attention to the values of the wchar_t objects it examines: nulls as well as invalid wide characters are compared too. 

<h2>Example</h2>

// Run this code <pre><code>#include &lt;iostream&gt;

#include &lt;string&gt;

#include &lt;cwchar&gt;

#include &lt;locale&gt;

#include &lt;clocale&gt;
void demo(const wchar_t *lhs, const wchar_t *rhs, std::size_t sz)

{
    std::wcout &lt;&lt; std::wstring(lhs, sz);
    int rc = std::wmemcmp(lhs, rhs, sz);
    if (rc == 0)
        std::wcout &lt;&lt; &quot; compares equal to &quot;;
    else if (rc &lt; 0)
        std::wcout &lt;&lt; &quot; precedes &quot;;
    else if (rc &gt; 0)
        std::wcout &lt;&lt; &quot; follows &quot;;
    std::wcout &lt;&lt; std::wstring(rhs, sz) &lt;&lt; &quot; in lexicographical order\n&quot;;
}
int main()

{
    std::setlocale(LC_ALL, &quot;en_US.utf8&quot;);
    std::wcout.imbue(std::locale(&quot;en_US.utf8&quot;));
    wchar_t a1[] = {L'α', L'β', L'γ'};
    constexpr std::size_t sz = sizeof a1 / sizeof *a1;
    wchar_t a2[sz] = {L'α', L'β', L'δ'};
    demo(a1, a2, sz);
    demo(a2, a1, sz);
    demo(a1, a1, sz);
}
</code></pre>

<h2>Possible output:</h2>

&nbsp;<wbr>&nbsp;αβγ precedes αβδ in lexicographical order 
&nbsp;<wbr>&nbsp;αβδ follows αβγ in lexicographical order 
&nbsp;<wbr>&nbsp;αβγ compares equal to αβγ in lexicographical order

<h2>See also</h2>

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;compares two wide strings 
wcscmp <i>(function)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;compares two buffers 
memcmp <i>(function)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;compares a certain amount of characters from two wide strings 
wcsncmp <i>(function)</i> 
