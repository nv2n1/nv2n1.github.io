---
title: "stdctypetoupperstdctypedo_toupper(3)"
name: "stdctypetoupperstdctypedo_toupper"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdctypetoupperstdctypedo_toupper/"
---

std::ctype&lt;CharT&gt;::toupper,std::ctype&lt;CharT&gt;::do_toupper - std::ctype&lt;CharT&gt;::toupper,std::ctype&lt;CharT&gt;::do_toupper

<h2>Synopsis</h2>

<pre><code>Defined in header&lt;locale&gt;

    public : (1)

                 CharT toupper(CharT c) const;

public:
(2)

    const CharT *toupper(CharT *beg, const CharT *end) const;

protected:
(3)

    virtual CharT do_toupper(CharT c) const;

protected:
(4)

    virtual const CharT *do_toupper(CharT *beg, const CharT *end) const;</code></pre> 
1,2) public member function, calls the protected virtual member function do_toupper of the most derived class. 
3) Converts the character c to upper case if an upper case form is defined by this locale. 
4) For every character in the character array [beg, end), for which an upper case form exists, replaces the character with that upper case form. 

<h2>Parameters</h2>

c - character to convert 
beg - pointer to the first character in an array of characters to convert 
end - one past the end pointer for the array of characters to convert

<h2>Return value</h2>

1,3) upper case character or c if no upper case form is listed by this locale. 
2,4) end. 

<h2>Notes</h2>

Only 1:1 character mapping can be performed by this function, e.g. the uppercase form of 'ß' is (with some exceptions) the two-character string &quot;SS&quot;, which cannot be obtained by do_toupper. 

<h2>Example</h2>

// Run this code <pre><code>#include &lt;locale&gt;

#include &lt;iostream&gt;
void try_upper(const std::ctype&lt;wchar_t&gt; &amp;f, wchar_t c)

{
    wchar_t up = f.toupper(c);
    if (up != c) {
        std::wcout &lt;&lt; &quot;Upper case form of \'&quot; &lt;&lt; c &lt;&lt; &quot;' is &quot; &lt;&lt; up &lt;&lt; '\n';
    } else {
        std::wcout &lt;&lt; '\'' &lt;&lt; c &lt;&lt; &quot;' has no upper case form\n&quot;;
    }
}
int main()

{
    std::locale::global(std::locale(&quot;en_US.utf8&quot;));
    std::wcout.imbue(std::locale());
    std::wcout &lt;&lt; &quot;In US English UTF-8 locale:\n&quot;;
    auto &amp;f = std::use_facet&lt;std::ctype&lt;wchar_t&gt;&gt;(std::locale());
    try_upper(f, L's');
    try_upper(f, L'ſ');
    try_upper(f, L'ß');
    std::wstring str = L&quot;Hello, World!&quot;;
    std::wcout &lt;&lt; &quot;Uppercase form of the string '&quot; &lt;&lt; str &lt;&lt; &quot;' is &quot;;
    f.toupper(&amp;str[0], &amp;str[0] + str.size());
    std::wcout &lt;&lt; &quot;'&quot; &lt;&lt; str &lt;&lt; &quot;'\n&quot;;
}
</code></pre>

<h2>Output:</h2>

&nbsp;<wbr>&nbsp;In US English UTF-8 locale: 
&nbsp;<wbr>&nbsp;Upper case form of 's' is S 
&nbsp;<wbr>&nbsp;Upper case form of 'ſ' is S 
&nbsp;<wbr>&nbsp;'ß' has no upper case form 
&nbsp;<wbr>&nbsp;Uppercase form of the string 'Hello, World!' is 'HELLO, WORLD!'

<h2>See also</h2>

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;invokes do_tolower 
tolower <i>(public member function)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;converts a character to uppercase 
toupper <i>(function)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;converts a wide character to uppercase 
towupper <i>(function)</i> 
