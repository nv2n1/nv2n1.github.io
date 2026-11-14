---
title: "stdregex_traitsvalue(3)"
name: "stdregex_traitsvalue"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdregex_traitsvalue/"
---

std::regex_traits&lt;CharT&gt;::value - std::regex_traits&lt;CharT&gt;::value

<h2>Synopsis</h2>

<pre><code>int value(CharT ch, int radix) const;
(since C++ 11)</code></pre> 
Determines the value represented by the digit ch in the numeric base radix, given the currently imbued locale. This function is called by std::regex when processing Quantifiers such as {1} or {2,5}, Backreferences such as \1, and hexadecimal and Unicode character escapes. 

<h2>Parameters</h2>

ch - the character that may represent a digit 
radix - either 8, 10, or 16

<h2>Return value</h2>

The numeric value if ch indeed represents a digit in the currently imbued locale that is valid for the numeric base radix, or -1 on error. 

<h2>Example</h2>

// Run this code <pre><code>#include &lt;iostream&gt;

#include &lt;locale&gt;

#include &lt;regex&gt;

#include &lt;map&gt;
// This custom regex traits allows japanese numerals

struct jnum_traits : std::regex_traits&lt;wchar_t&gt;

{
    static std::map&lt;wchar_t, int&gt; data;
    int value(wchar_t ch, int radix) const
    {
        wchar_t up = std::toupper(ch, getloc());
        return data.count(up) ? data[up] : regex_traits::value(ch, radix);
    }
};

std::map&lt;wchar_t, int&gt; jnum_traits::data = &#123;&#123;L'〇', 0}, {L'一', 1}, {L'二', 2}, {L'三', 3}, {L'四', 4}, {L'五', 5}, {L'六', 6}, {L'七', 7}, {L'八', 8}, {L'九', 9}, {L'Ａ', 10}, {L'Ｂ', 11}, {L'Ｃ', 12}, {L'Ｄ', 13}, {L'Ｅ', 14}, {L'Ｆ', 15}};

int main()

{
    std::locale::global(std::locale(&quot;ja_JP.utf8&quot;));
    std::wcout.sync_with_stdio(false);
    std::wcout.imbue(std::locale());
    std::wstring in = L&quot;風&quot;;
    if (std::regex_match(in, std::wregex(L&quot;\\u98a8&quot;)))
        std::wcout &lt;&lt; &quot;\\u98a8 matched &quot; &lt;&lt; in &lt;&lt; '\n';
    if (std::regex_match(in, std::basic_regex&lt;wchar_t, jnum_traits&gt;(L&quot;\\u九八ａ八&quot;)))
        std::wcout &lt;&lt; L&quot;\\u九八ａ八 with custom traits matched &quot; &lt;&lt; in &lt;&lt; '\n';
}
</code></pre>

<h2>Output:</h2>

&nbsp;<wbr>&nbsp;\u98a8 matched 風 
&nbsp;<wbr>&nbsp;\u九八ａ八 with custom traits matched 風
