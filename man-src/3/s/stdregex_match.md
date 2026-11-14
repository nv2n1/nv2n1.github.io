---
title: "stdregex_match(3)"
name: "stdregex_match"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdregex_match/"
description: "std::regex_match – std::regex_match"
---

<p>std::regex_match &#8211; std::regex_match</p>
<h2>Synopsis</h2>
<pre><code>Defined in header&lt;regex&gt;

    template &lt;class BidirIt,

              class Alloc, class CharT, class Traits&gt;

    bool regex_match(BidirIt first, BidirIt last,

                     std::match_results&lt;BidirIt, Alloc&gt; &amp;m, (1)(since C++ 11)

                                                                const std::basic_regex&lt;CharT, Traits&gt; &amp;e,

                     std::regex_constants::match_flag_type flags =

                         std::regex_constants::match_default);

template &lt;class BidirIt,

          class CharT, class Traits&gt;

bool regex_match(BidirIt first, BidirIt last, (2)(since C++ 11)

                                                  const std::basic_regex&lt;CharT, Traits&gt; &amp;e,

                 std::regex_constants::match_flag_type flags =

                     std::regex_constants::match_default);

template &lt;class CharT, class Alloc, class Traits&gt;

bool regex_match(const CharT *str,

                 std::match_results&lt;const CharT *, Alloc&gt; &amp;m, (3)(since C++ 11)

                                                                  const std::basic_regex&lt;CharT, Traits&gt; &amp;e,

                 std::regex_constants::match_flag_type flags =

                     std::regex_constants::match_default);

template &lt;class STraits, class SAlloc,

          class Alloc, class CharT, class Traits&gt;

bool regex_match(const std::basic_string&lt;CharT, STraits, SAlloc&gt; &amp;s,

                 std::match_results&lt;

                     typename std::basic_string&lt;CharT, STraits, SAlloc&gt;::const_iterator, (4)(since C++ 11)

                                                                                             Alloc

                     &gt; &amp;m,

                 const std::basic_regex&lt;CharT, Traits&gt; &amp;e,

                 std::regex_constants::match_flag_type flags =

                     std::regex_constants::match_default);

template &lt;class CharT, class Traits&gt;

bool regex_match(const CharT *str,

                 const std::basic_regex&lt;CharT, Traits&gt; &amp;e, (5)(since C++ 11)

                                                               std::regex_constants::match_flag_type flags =

                                                                   std::regex_constants::match_default);

template &lt;class STraits, class SAlloc,

          class CharT, class Traits&gt;

bool regex_match(const std::basic_string&lt;CharT, STraits, SAlloc&gt; &amp;s, (6)(since C++ 11)

                                                                         const std::basic_regex&lt;CharT, Traits&gt; &amp;e,

                 std::regex_constants::match_flag_type flags =

                     std::regex_constants::match_default);

template &lt;class STraits, class SAlloc,

          class Alloc, class CharT, class Traits&gt;

bool regex_match(const std::basic_string&lt;CharT, STraits, SAlloc&gt; &amp;&amp;,

                 std::match_results&lt;

                     typename std::basic_string&lt;CharT, STraits, SAlloc&gt;::const_iterator, (7)(since C++ 14)

                                                                                             Alloc

                     &gt; &amp;,

                 const std::basic_regex&lt;CharT, Traits&gt; &amp;,

                 std::regex_constants::match_flag_type flags =

                     std::regex_constants::match_default) = delete;</code></pre>
<p>Determines if the regular expression e matches the entire target character sequence, which may be specified as std::string, a C-string, or an iterator pair.<br />
1) Determines if there is a match between the regular expression e and the entire target character sequence [first,last), taking into account the effect of flags. When determining if there is a match, only potential matches that match the entire character sequence are considered. Match results are returned in m.<br />
2) Behaves as <code>(1)</code> above, omitting the match results.<br />
3) Returns std::regex_match(str, str + std::char_traits&lt;charT&gt;::length(str), m, e, flags).<br />
4) Returns std::regex_match(s.begin(), s.end(), m, e, flags).<br />
5) Returns std::regex_match(str, str + std::char_traits&lt;charT&gt;::length(str), e, flags).<br />
6) Returns std::regex_match(s.begin(), s.end(), e, flags).<br />
7) The overload 4 is prohibited from accepting temporary strings, otherwise this function populates match_results m with string iterators that become invalid immediately.<br />
Note that regex_match will only successfully match a regular expression to an entire character sequence, whereas std::regex_search will successfully match subsequences. </p>
<h2>Parameters</h2>
<p>first, last &#8211; the target character range to apply the regex to, given as iterators<br />
m &#8211; the match results<br />
str &#8211; the target string, given as a null-terminated C-style string<br />
s &#8211; the target string, given as a std::basic_string<br />
e &#8211; the regular expression<br />
flags &#8211; flags used to determine how the match will be performed</p>
<h2>Type requirements</h2>
<p>&#8211;<br />
BidirIt must meet the requirements of LegacyBidirectionalIterator.</p>
<h2>Return value</h2>
<p>Returns true if a match exists, false otherwise. In either case, the object m is updated, as follows:<br />
If the match does not exist:<br />
m.ready() == true<br />
m.empty() == true<br />
m.size() == 0<br />
If the match exists:<br />
m.ready() true<br />
m.empty() false<br />
m.size() number_of_marked_subexpressions plus 1, that is, 1+e.mark_count()<br />
m.prefix().first first<br />
m.prefix().second first<br />
m.prefix().matched false (the match prefix is empty)<br />
m.suffix().first last<br />
m.suffix().second last<br />
m.suffix().matched false (the match suffix is empty)<br />
m[0].first first<br />
m[0].second last<br />
m[0].matched true (the entire sequence is matched)<br />
m[n].first the start of the sequence that matched marked_sub-expression n, or last if the subexpression did not participate in the match<br />
m[n].second the end of the sequence that matched marked_sub-expression n, or last if the subexpression did not participate in the match<br />
m[n].matched true if sub-expression n participated in the match, false otherwise </p>
<h2>Notes</h2>
<p>Because regex_match only considers full matches, the same regex may give different matches between regex_match and std::regex_search:<br />
&nbsp;<wbr>&nbsp;std::regex re(&quot;Get|GetValue&quot;);<br />
&nbsp;<wbr>&nbsp;std::cmatch m;<br />
&nbsp;<wbr>&nbsp;std::regex_search(&quot;GetValue&quot;, m, re); // returns true, and m[0] contains &quot;Get&quot;<br />
&nbsp;<wbr>&nbsp;std::regex_match (&quot;GetValue&quot;, m, re); // returns true, and m[0] contains &quot;GetValue&quot;<br />
&nbsp;<wbr>&nbsp;std::regex_search(&quot;GetValues&quot;, m, re); // returns true, and m[0] contains &quot;Get&quot;<br />
&nbsp;<wbr>&nbsp;std::regex_match (&quot;GetValues&quot;, m, re); // returns false </p>
<h2>Example</h2>
<p>// Run this code </p>
<pre><code>#include &lt;iostream&gt;

#include &lt;string&gt;

#include &lt;regex&gt;
int main()

{
    // Simple regular expression matching
    const std::string fnames[] = {&quot;foo.txt&quot;, &quot;bar.txt&quot;, &quot;baz.dat&quot;, &quot;zoidberg&quot;};
    const std::regex txt_regex(&quot;[a-z]+\.txt&quot;);
    for (const auto &amp;fname : fnames) {
        std::cout &lt;&lt; fname &lt;&lt; &quot;: &quot; &lt;&lt; std::regex_match(fname, txt_regex) &lt;&lt; '
';
    }
    // Extraction of a sub-match
    const std::regex base_regex(&quot;([a-z]+)\.txt&quot;);
    std::smatch base_match;
    for (const auto &amp;fname : fnames) {
        if (std::regex_match(fname, base_match, base_regex)) {
            // The first sub_match is the whole string; the next
            // sub_match is the first parenthesized expression.
            if (base_match.size() == 2) {
                std::ssub_match base_sub_match = base_match[1];
                std::string base = base_sub_match.str();
                std::cout &lt;&lt; fname &lt;&lt; &quot; has a base of &quot; &lt;&lt; base &lt;&lt; '
';
            }
        }
    }
    // Extraction of several sub-matches
    const std::regex pieces_regex(&quot;([a-z]+)\.([a-z]+)&quot;);
    std::smatch pieces_match;
    for (const auto &amp;fname : fnames) {
        if (std::regex_match(fname, pieces_match, pieces_regex)) {
            std::cout &lt;&lt; fname &lt;&lt; '
';
            for (size_t i = 0; i &lt; pieces_match.size(); ++i) {
                std::ssub_match sub_match = pieces_match[i];
                std::string piece = sub_match.str();
                std::cout &lt;&lt; &quot;  submatch &quot; &lt;&lt; i &lt;&lt; &quot;: &quot; &lt;&lt; piece &lt;&lt; '
';
            }
        }
    }
}
</code></pre>
<h2>Output:</h2>
<p>&nbsp;<wbr>&nbsp;foo.txt: 1<br />
&nbsp;<wbr>&nbsp;bar.txt: 1<br />
&nbsp;<wbr>&nbsp;baz.dat: 0<br />
&nbsp;<wbr>&nbsp;zoidberg: 0<br />
&nbsp;<wbr>&nbsp;foo.txt has a base of foo<br />
&nbsp;<wbr>&nbsp;bar.txt has a base of bar<br />
&nbsp;<wbr>&nbsp;foo.txt<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;submatch 0: foo.txt<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;submatch 1: foo<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;submatch 2: txt<br />
&nbsp;<wbr>&nbsp;bar.txt<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;submatch 0: bar.txt<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;submatch 1: bar<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;submatch 2: txt<br />
&nbsp;<wbr>&nbsp;baz.dat<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;submatch 0: baz.dat<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;submatch 1: baz<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;submatch 2: dat</p>
<h2>See also</h2>
<p>basic_regex regular expression object<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(class template)</i><br />
<i>(C++11)</i><br />
match_results identifies one regular expression match, including all sub-expression matches<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(class template)</i><br />
<i>(C++11)</i><br />
regex_search attempts to match a regular expression to any part of a character sequence<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function template)</i><br />
<i>(C++11)</i> </p>
