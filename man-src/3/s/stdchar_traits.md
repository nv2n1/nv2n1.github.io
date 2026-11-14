---
title: "stdchar_traits(3)"
name: "stdchar_traits"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdchar_traits/"
description: "std::char_traits – std::char_traits"
---

<p>std::char_traits &#8211; std::char_traits</p>
<h2>Synopsis</h2>
<pre><code>Defined in header &lt;string&gt;

template&lt;

class CharT

&gt; class char_traits;</code></pre>
<p>The char_traits class is a traits class template that abstracts basic character and string operations for a given character type. The defined operation set is such that generic algorithms almost always can be implemented in terms of it. It is thus possible to use such algorithms with almost any possible character or string type, just by supplying a customized char_traits class.<br />
The char_traits class template serves as a basis for explicit instantiations. The user can provide_a_specialization for any custom character types. Several specializations are defined for the standard character types.<br />
If an operation on traits emits an exception, the behavior is undefined.<br />
The values of the member typedefs are as follows.<br />
Specialization char_type int_type off_type pos_type state_type<br />
char_traits&lt;char&gt; char int std::streamoff std::streampos std::mbstate_t<br />
char_traits&lt;wchar_t&gt; wchar_t std::wint_t std::streamoff std::wstreampos std::mbstate_t<br />
char_traits&lt;char16_t&gt; <i>(C++11)</i> char16_t std::uint_least16_t std::streamoff std::u16streampos std::mbstate_t<br />
char_traits&lt;char32_t&gt; <i>(C++11)</i> char32_t std::uint_least32_t std::streamoff std::u32streampos std::mbstate_t<br />
char_traits&lt;char8_t&gt; (C++20) char8_t unsigned int std::streamoff std::u8streampos std::mbstate_t<br />
The semantics of the member functions are defined are as follows. Specialization                assign eq                   lt                  eof</p>
<p>char_traits&lt;char&gt;             =      == for unsigned char &lt; for unsigned char EOF</p>
<p>char_traits&lt;wchar_t&gt;          =      ==                   &lt;                   WEOF</p>
<p>char_traits&lt;char16_t&gt; (C++11) =      ==                   &lt;                   invalid UTF-16 code unit</p>
<p>char_traits&lt;char32_t&gt; (C++11) =      ==                   &lt;                   invalid UTF-32 code unit</p>
<p>char_traits&lt;char8_t&gt; (C++20)  =      ==                   &lt;                   invalid UTF-8 code unit<br />
The char_traits class template satisfies the requirements of CharTraits. </p>
<h2>Member types</h2>
<p>Type Definition<br />
char_type CharT<br />
int_type an integer type that can hold all values of char_type plus EOF<br />
off_type implementation-defined<br />
pos_type implementation-defined<br />
state_type implementation-defined</p>
<h2>Member functions</h2>
<p>assign assigns a character<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(public static member function)</i><br />
<code>[static]</code> </p>
<p>eq compares two characters<br />
lt <i>(public static member function)</i> </p>
<p><code>[static]</code> </p>
<p>move moves one character sequence onto another<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(public static member function)</i><br />
<code>[static]</code> </p>
<p>copy copies a character sequence<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(public static member function)</i><br />
<code>[static]</code> </p>
<p>compare lexicographically compares two character sequences<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(public static member function)</i><br />
<code>[static]</code> </p>
<p>length returns the length of a character sequence<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(public static member function)</i><br />
<code>[static]</code> </p>
<p>find finds a character in a character sequence<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(public static member function)</i><br />
<code>[static]</code> </p>
<p>to_char_type converts int_type to equivalent char_type<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(public static member function)</i><br />
<code>[static]</code> </p>
<p>to_int_type converts char_type to equivalent int_type<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(public static member function)</i><br />
<code>[static]</code> </p>
<p>eq_int_type compares two int_type values<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(public static member function)</i><br />
<code>[static]</code> </p>
<p>eof returns an eof value<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(public static member function)</i><br />
<code>[static]</code> </p>
<p>not_eof checks whether a character is eof value<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(public static member function)</i><br />
<code>[static]</code></p>
<h2>Example</h2>
<p>User-defined character traits may be used to provide case-insensitive_comparison<br />
 // Run this code </p>
<pre><code>#include &lt;string&gt;

#include &lt;iostream&gt;

#include &lt;cctype&gt;
struct ci_char_traits : public std::char_traits&lt;char&gt; {
    static char to_upper(char ch)
    {
        return std::toupper((unsigned char)ch);
    }
    static bool eq(char c1, char c2)
    {
        return to_upper(c1) == to_upper(c2);
    }
    static bool lt(char c1, char c2)
    {
        return to_upper(c1) &lt; to_upper(c2);
    }
    static int compare(const char *s1, const char *s2, size_t n)
    {
        while (n-- != 0) {
            if (to_upper(*s1) &lt; to_upper(*s2))
                return -1;
            if (to_upper(*s1) &gt; to_upper(*s2))
                return 1;
            ++s1;
            ++s2;
        }
        return 0;
    }
    static const char *find(const char *s, int n, char a)
    {
        auto const ua(to_upper(a));
        while (n-- != 0) {
            if (to_upper(*s) == ua)
                return s;
            s++;
        }
        return nullptr;
    }
};
using ci_string = std::basic_string&lt;char, ci_char_traits&gt;;
std::ostream &amp;operator&lt;&lt;(std::ostream &amp;os, const ci_string &amp;str)
{
    return os.write(str.data(), str.size());
}
int main()

{
    ci_string s1 = &quot;Hello&quot;;
    ci_string s2 = &quot;heLLo&quot;;
    if (s1 == s2)
        std::cout &lt;&lt; s1 &lt;&lt; &quot; and &quot; &lt;&lt; s2 &lt;&lt; &quot; are equal
&quot;;
}
</code></pre>
<h2>Output:</h2>
<p>&nbsp;<wbr>&nbsp;Hello and heLLo are equal</p>
<h2>See also</h2>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;stores and manipulates sequences of characters<br />
basic_string <i>(class template)</i> </p>
