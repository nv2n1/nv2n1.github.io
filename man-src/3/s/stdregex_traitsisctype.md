---
title: "stdregex_traitsisctype(3)"
name: "stdregex_traitsisctype"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdregex_traitsisctype/"
description: "std::regex_traits<CharT>::isctype – std::regex_traits<CharT>::isctype"
---

<p>std::regex_traits&lt;CharT&gt;::isctype &#8211; std::regex_traits&lt;CharT&gt;::isctype</p>
<h2>Synopsis</h2>
<pre><code>bool isctype(CharT c, char_class_type f) const;</code></pre>
<p>Determines whether the character c belongs to the character class identified by f, which, in turn, is a value returned by lookup_classname() or a bitwise OR of several such values.<br />
The version of this function provided in the standard library specializations of std::regex_traits does the following:<br />
1) First converts f to some temporary value m of type std::ctype_base::mask in implementation-defined manner<br />
2) Then attempts to classify the character in the imbued locale by calling std::use_facet&lt;std::ctype&lt;CharT&gt;&gt;(getloc()).is(m, c). If that returned true, true is returned by isctype().<br />
3) Otherwise, checks whether c equals &#8216;_&#8217; and the bitmask f includes the result of calling lookup_classname() for the character class [:w:], in which case true is returned.<br />
4) Otherwise, false is returned. </p>
<h2>Parameters</h2>
<p>c &#8211; the character to classify<br />
f &#8211; the bitmask obtained from one or several calls to lookup_classname()</p>
<h2>Return value</h2>
<p>true if c is classified by f, false otherwise. </p>
<h2>Notes</h2>
<p>The description above summarizes C++14; the C++11 phrasing required this function to return true for &#8216;_&#8217; in all cases (LWG_issue_2018) </p>
<h2>Example</h2>
<p>// Run this code </p>
<pre><code>#include &lt;iostream&gt;

#include &lt;string&gt;

#include &lt;regex&gt;
int main()

{
    std::regex_traits&lt;char&gt; t;
    std::string str_alnum = &quot;alnum&quot;;
    auto a = t.lookup_classname(str_alnum.begin(), str_alnum.end());
    std::string str_w = &quot;w&quot;; // [:w:] is [:alnum:] plus '_'
    auto w = t.lookup_classname(str_w.begin(), str_w.end());
    std::cout &lt;&lt; std::boolalpha
              &lt;&lt; t.isctype('A', w) &lt;&lt; ' ' &lt;&lt; t.isctype('A', a) &lt;&lt; '
'
              &lt;&lt; t.isctype('_', w) &lt;&lt; ' ' &lt;&lt; t.isctype('_', a) &lt;&lt; '
'
              &lt;&lt; t.isctype(' ', w) &lt;&lt; ' ' &lt;&lt; t.isctype(' ', a) &lt;&lt; '
';
}
</code></pre>
<h2>Output:</h2>
<p>&nbsp;<wbr>&nbsp;true true<br />
&nbsp;<wbr>&nbsp;true false<br />
&nbsp;<wbr>&nbsp;false false </p>
<p>demonstraits a custom regex_traits implementation of lookup_classname/isctype<br />
 // Run this code </p>
<p>&nbsp;<wbr>&nbsp;#include &lt;iostream&gt;<br />
&nbsp;<wbr>&nbsp;#include &lt;locale&gt;<br />
&nbsp;<wbr>&nbsp;#include &lt;regex&gt;<br />
&nbsp;<wbr>&nbsp;#include &lt;cwctype&gt; </p>
<p>&nbsp;<wbr>&nbsp;// This custom regex traits uses wctype/iswctype to implement lookup_classname/isctype<br />
&nbsp;<wbr>&nbsp;struct wctype_traits : std::regex_traits&lt;wchar_t&gt;<br />
&nbsp;<wbr>&nbsp;{<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;using char_class_type = std::wctype_t;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;template&lt;class It&gt;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;char_class_type lookup_classname(It first, It last, bool=false) const {<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;return std::wctype(std::string(first, last).c_str());<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;}<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;bool isctype(wchar_t c, char_class_type f) const {<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;return std::iswctype(c, f);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;}<br />
&nbsp;<wbr>&nbsp;}; </p>
<p>&nbsp;<wbr>&nbsp;int main()<br />
&nbsp;<wbr>&nbsp;{<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;std::locale::global(std::locale(&quot;ja_JP.utf8&quot;));<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;std::wcout.sync_with_stdio(false);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;std::wcout.imbue(std::locale()); </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;std::wsmatch m;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;std::wstring in = L&quot;風の谷のナウシカ&quot;;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;// matches all characters (they are classified as alnum)<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;std::regex_search(in, m, std::wregex(L&quot;([[:alnum:]]+)&quot;));<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;std::wcout &lt;&lt; &quot;alnums: &quot; &lt;&lt; m[1] &lt;&lt; &#8216;
&#8217;; // prints &quot;風の谷のナウシカ&quot;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;// matches only the katakana<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;std::regex_search(in, m,<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;std::basic_regex&lt;wchar_t, wctype_traits&gt;(L&quot;([[:jkata:]]+)&quot;));<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;std::wcout &lt;&lt; &quot;katakana: &quot; &lt;&lt; m[1] &lt;&lt; &#8216;
&#8217;; // prints &quot;ナウシカ&quot;<br />
&nbsp;<wbr>&nbsp;}</p>
<h2>Output:</h2>
<p>&nbsp;<wbr>&nbsp;alnums: 風の谷のナウシカ<br />
&nbsp;<wbr>&nbsp;katakana: ナウシカ</p>
<h2>See also</h2>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;gets a character class by name<br />
lookup_classname <i>(public member function)</i><br />
do_is classifies a character or a character sequence<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(virtual protected member function of std::ctype&lt;CharT&gt;)</i><br />
<code>[virtual]</code><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;classifies a wide character according to the specified LC_CTYPE category<br />
iswctype <i>(function)</i> </p>
