---
title: "stdctypetolowerstdctypedo_tolower(3)"
name: "stdctypetolowerstdctypedo_tolower"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdctypetolowerstdctypedo_tolower/"
---

std::ctype&lt;CharT&gt;::tolower,std::ctype&lt;CharT&gt;::do_tolower - std::ctype&lt;CharT&gt;::tolower,std::ctype&lt;CharT&gt;::do_tolower

<h2>Synopsis</h2>

<pre><code>Defined in header&lt;locale&gt;

    public : (1)

                 CharT tolower(CharT c) const;

public:
(2)

    const CharT *tolower(CharT *beg, const CharT *end) const;

protected:
(3)

    virtual CharT do_tolower(CharT c) const;

protected:
(4)

    virtual const CharT *do_tolower(CharT *beg, const CharT *end) const;</code></pre> 
1,2) public member function, calls the protected virtual member function do_tolower of the most derived class. 
3) Converts the character c to lower case if a lower case form is defined by this locale. 
4) For every character in the character array [beg, end), for which a lower case form exists, replaces the character with that lower case form. 

<h2>Parameters</h2>

c - character to convert 
beg - pointer to the first character in an array of characters to convert 
end - one past the end pointer for the array of characters to convert

<h2>Return value</h2>

1,3) lower case character or c if no lower case form is listed by this locale. 
2,4) end. 

<h2>Notes</h2>

Only 1:1 character mapping can be performed by this function, e.g. the Greek uppercase letter 'Σ' has two lowercase forms, depending on the position in a word: 'σ' and 'ς'. A call to do_tolower cannot be used to obtain the correct lowercase form in this case. 

<h2>Example</h2>

// Run this code <pre><code>#include &lt;locale&gt;

#include &lt;iostream&gt;
void try_lower(const std::ctype&lt;wchar_t&gt; &amp;f, wchar_t c)

{
    wchar_t up = f.tolower(c);
    if (up != c) {
        std::wcout &lt;&lt; &quot;Lower case form of \'&quot; &lt;&lt; c &lt;&lt; &quot;' is &quot; &lt;&lt; up &lt;&lt; '\n';
    } else {
        std::wcout &lt;&lt; '\'' &lt;&lt; c &lt;&lt; &quot;' has no lower case form\n&quot;;
    }
}
int main()

{
    std::locale::global(std::locale(&quot;en_US.utf8&quot;));
    std::wcout.imbue(std::locale());
    std::wcout &lt;&lt; &quot;In US English UTF-8 locale:\n&quot;;
    auto &amp;f = std::use_facet&lt;std::ctype&lt;wchar_t&gt;&gt;(std::locale());
    try_lower(f, L'Σ');
    try_lower(f, L'Ɛ');
    try_lower(f, L'Ａ');
    std::wstring str = L&quot;HELLo, wORLD!&quot;;
    std::wcout &lt;&lt; &quot;Lowercase form of the string '&quot; &lt;&lt; str &lt;&lt; &quot;' is &quot;;
    f.tolower(&amp;str[0], &amp;str[0] + str.size());
    std::wcout &lt;&lt; &quot;'&quot; &lt;&lt; str &lt;&lt; &quot;'\n&quot;;
}
</code></pre>

<h2>Output:</h2>

&nbsp;<wbr>&nbsp;In US English UTF-8 locale: 
&nbsp;<wbr>&nbsp;Lower case form of 'Σ' is σ 
&nbsp;<wbr>&nbsp;Lower case form of 'Ɛ' is ɛ 
&nbsp;<wbr>&nbsp;Lower case form of 'Ａ' is ａ 
&nbsp;<wbr>&nbsp;Lowercase form of the string 'HELLo, wORLD!' is 'hello, world!'

<h2>See also</h2>

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;invokes do_toupper 
toupper <i>(public member function)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;converts a character to lowercase 
tolower <i>(function)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;converts a wide character to lowercase 
towlower <i>(function)</i> 
