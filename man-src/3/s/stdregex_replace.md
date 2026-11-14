---
title: "stdregex_replace(3)"
name: "stdregex_replace"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdregex_replace/"
---

std::regex_replace - std::regex_replace

<h2>Synopsis</h2>

<pre><code>Defined in header&lt;regex&gt;

    template &lt;class OutputIt, class BidirIt,

              class Traits, class CharT,

              class STraits, class SAlloc&gt;

    OutputIt regex_replace(OutputIt out, BidirIt first, BidirIt last, (1)(since C++ 11)

                                                                          const std::basic_regex&lt;CharT, Traits&gt; &amp;re,

                           const std::basic_string&lt;CharT, STraits, SAlloc&gt; &amp;fmt,

                           std::regex_constants::match_flag_type flags =

                               std::regex_constants::match_default);

template &lt;class OutputIt, class BidirIt,

          class Traits, class CharT&gt;

OutputIt regex_replace(OutputIt out, BidirIt first, BidirIt last,

                       const std::basic_regex&lt;CharT, Traits&gt; &amp;re, (2)(since C++ 11)

                                                                      const CharT *fmt,

                       std::regex_constants::match_flag_type flags =

                           std::regex_constants::match_default);

template &lt;class Traits, class CharT,

          class STraits, class SAlloc,

          class FTraits, class FAlloc&gt;

std::basic_string&lt;CharT, STraits, SAlloc&gt;

regex_replace(const std::basic_string&lt;CharT, STraits, SAlloc&gt; &amp;s, (3)(since C++ 11)

                                                                      const std::basic_regex&lt;CharT, Traits&gt; &amp;re,

              const std::basic_string&lt;CharT, FTraits, FAlloc&gt; &amp;fmt,

              std::regex_constants::match_flag_type flags =

                  std::regex_constants::match_default);

template &lt;class Traits, class CharT,

          class STraits, class SAlloc&gt;

std::basic_string&lt;CharT, STraits, SAlloc&gt;

regex_replace(const std::basic_string&lt;CharT, STraits, SAlloc&gt; &amp;s, (4)(since C++ 11)

                                                                      const std::basic_regex&lt;CharT, Traits&gt; &amp;re,

              const CharT *fmt,

              std::regex_constants::match_flag_type flags =

                  std::regex_constants::match_default);

template &lt;class Traits, class CharT,

          class STraits, class SAlloc&gt;

std::basic_string&lt;CharT&gt;

regex_replace(const CharT *s, (5)(since C++ 11)

                                  const std::basic_regex&lt;CharT, Traits&gt; &amp;re,

              const std::basic_string&lt;CharT, STraits, SAlloc&gt; &amp;fmt,

              std::regex_constants::match_flag_type flags =

                  std::regex_constants::match_default);

template &lt;class Traits, class CharT&gt;

std::basic_string&lt;CharT&gt;

regex_replace(const CharT *s,

              const std::basic_regex&lt;CharT, Traits&gt; &amp;re, (6)(since C++ 11)

                                                             const CharT *fmt,

              std::regex_constants::match_flag_type flags =

                  std::regex_constants::match_default);</code></pre> 
regex_replace uses a regular expression to perform substitution on a sequence of characters: 
1) Copies characters in the range [first,last) to out, replacing any sequences that match re with characters formatted by fmt. In other words: 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;* Constructs a std::regex_iterator object i as if by std::regex_iterator&lt;BidirIt, CharT, traits&gt; i(first, last, re, flags), and uses it to step through every match of re within the sequence [first,last). 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;* For each such match m, copies the non-matched subsequence (m.prefix()) into out as if by out = std::copy(m.prefix().first, m.prefix().second, out) and then replaces the matched subsequence with the formatted replacement string as if by calling out_=_m.format(out,_fmt,_flags). 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;* When no more matches are found, copies the remaining non-matched characters to out as if by out = std::copy(last_m.suffix().first, last_m.suffix().second, out) where last_m is a copy of the last match found. 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;* If there are no matches, copies the entire sequence into out as-is, by out = std::copy(first, last, out) 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;* If flags contains std::regex_constants::format_no_copy, the non-matched subsequences are not copied into out. 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;* If flags contains std::regex_constants::format_first_only, only the first match is replaced. 2) same as 1), but the formatted replacement is performed as if by calling out_=_m.format(out,_fmt,_fmt_+_char_traits&lt;charT&gt;::length(fmt),_flags)

3-4) Constructs an empty string result of type std::basic_string&lt;CharT, ST, SA&gt; and calls std::regex_replace(std::back_inserter(result), s.begin(), s.end(), re, fmt, flags).

5-6) Constructs an empty string result of type std::basic_string&lt;CharT&gt; and calls std::regex_replace(std::back_inserter(result), s, s + std::char_traits&lt;CharT&gt;::length(s), re, fmt, flags).


<h2>Parameters</h2>

first, last - the input character sequence, represented as a pair of iterators 
s - the input character sequence, represented as std::basic_string or character array 
re - the std::basic_regex that will be matched against the input sequence 
flags - the match flags of type std::regex_constants::match_flag_type 
fmt - the regex replacement format string, exact syntax depends on the value of flags 
out - output iterator to store the result of the replacement

<h2>Type requirements</h2>

- 
OutputIt must meet the requirements of LegacyOutputIterator. 
- 
BidirIt must meet the requirements of LegacyBidirectionalIterator.

<h2>Return value</h2>

1-2) Returns a copy of the output iterator out after all the insertions. 
3-6) Returns the string result which contains the output. 

<h2>Exceptions</h2>

May throw std::regex_error to indicate an error_condition.

<h2>Example</h2>

// Run this code <pre><code>#include &lt;iostream&gt;

#include &lt;iterator&gt;

#include &lt;regex&gt;

#include &lt;string&gt;
int main()

{
    std::string text = &quot;Quick brown fox&quot;;
    std::regex vowel_re(&quot;a|e|i|o|u&quot;);
    // write the results to an output iterator
    std::regex_replace(std::ostreambuf_iterator&lt;char&gt;(std::cout),
                       text.begin(), text.end(), vowel_re, &quot;*&quot;);
    // construct a string holding the results
    std::cout &lt;&lt; '\n'
              &lt;&lt; std::regex_replace(text, vowel_re, &quot;[$&amp;]&quot;) &lt;&lt; '\n';
}
</code></pre>

<h2>Output:</h2>

&nbsp;<wbr>&nbsp;Q**ck br*wn f*x 
&nbsp;<wbr>&nbsp;Q[u][i]ck br[o]wn f[o]x

<h2>See also</h2>

regex_search attempts to match a regular expression to any part of a character sequence 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function template)</i> 
<i>(C++11)</i> 
match_flag_type options specific to matching 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(typedef)</i> 
<i>(C++11)</i> 
