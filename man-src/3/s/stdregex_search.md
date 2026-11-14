---
title: "stdregex_search(3)"
name: "stdregex_search"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdregex_search/"
---

std::regex_search - std::regex_search

<h2>Synopsis</h2>

<pre><code>Defined in header&lt;regex&gt;

    template &lt;class BidirIt,

              class Alloc, class CharT, class Traits&gt;

    bool regex_search(BidirIt first, BidirIt last,

                      std::match_results&lt;BidirIt, Alloc&gt; &amp;m, (1)(since C++ 11)

                                                                 const std::basic_regex&lt;CharT, Traits&gt; &amp;e,

                      std::regex_constants::match_flag_type flags =

                          std::regex_constants::match_default);

template &lt;class CharT, class Alloc, class Traits&gt;

bool regex_search(const CharT *str,

                  std::match_results&lt;const CharT *, Alloc&gt; &amp;m, (2)(since C++ 11)

                                                                   const std::basic_regex&lt;CharT, Traits&gt; &amp;e,

                  std::regex_constants::match_flag_type flags =

                      std::regex_constants::match_default);

template &lt;class STraits, class SAlloc,

          class Alloc, class CharT, class Traits&gt;

bool regex_search(const std::basic_string&lt;CharT, STraits, SAlloc&gt; &amp;s,

                  std::match_results&lt;

                      typename std::basic_string&lt;CharT, STraits, SAlloc&gt;::const_iterator, (3)(since C++ 11)

                                                                                              Alloc

                      &gt; &amp;m,

                  const std::basic_regex&lt;CharT, Traits&gt; &amp;e,

                  std::regex_constants::match_flag_type flags =

                      std::regex_constants::match_default);

template &lt;class BidirIt,

          class CharT, class Traits&gt;

bool regex_search(BidirIt first, BidirIt last, (4)(since C++ 11)

                                                   const std::basic_regex&lt;CharT, Traits&gt; &amp;e,

                  std::regex_constants::match_flag_type flags =

                      std::regex_constants::match_default);

template &lt;class CharT, class Traits&gt;

bool regex_search(const CharT *str,

                  const std::basic_regex&lt;CharT, Traits&gt; &amp;e, (5)(since C++ 11)

                                                                std::regex_constants::match_flag_type flags =

                                                                    std::regex_constants::match_default);

template &lt;class STraits, class SAlloc,

          class CharT, class Traits&gt;

bool regex_search(const std::basic_string&lt;CharT, STraits, SAlloc&gt; &amp;s, (6)(since C++ 11)

                                                                          const std::basic_regex&lt;CharT, Traits&gt; &amp;e,

                  std::regex_constants::match_flag_type flags =

                      std::regex_constants::match_default);

template &lt;class STraits, class SAlloc,

          class Alloc, class CharT, class Traits&gt;

bool regex_search(const std::basic_string&lt;CharT, STraits, SAlloc&gt; &amp;&amp;,

                  std::match_results&lt;

                      typename std::basic_string&lt;CharT, STraits, SAlloc&gt;::const_iterator, (7)(since C++ 14)

                                                                                              Alloc

                      &gt; &amp;,

                  const std::basic_regex&lt;CharT, Traits&gt; &amp;,

                  std::regex_constants::match_flag_type flags =

                      std::regex_constants::match_default) = delete;</code></pre> 
Determines if there is a match between the regular expression e and some subsequence in the target character sequence. 
1) Analyzes generic range [first,last). Match results are returned in m. 
2) Analyzes a null-terminated string pointed to by str. Match results are returned in m. 
3) Analyzes a string s. Match results are returned in m. 
4-6) Equivalent to (1-3), just omits the match results. 
7) The overload 3 is prohibited from accepting temporary strings, otherwise this function populates match_results m with string iterators that become invalid immediately. 
regex_search will successfully match any subsequence of the given sequence, whereas std::regex_match will only return true if the regular expression matches the entire sequence. 

<h2>Parameters</h2>

first, last - a range identifying the target character sequence 
str - a pointer to a null-terminated target character sequence 
s - a string identifying target character sequence 
e - the std::regex that should be applied to the target character sequence 
m - the match results 
flags - std::regex_constants::match_flag_type governing search behavior

<h2>Type requirements</h2>

- 
BidirIt must meet the requirements of LegacyBidirectionalIterator. 
- 
Alloc must meet the requirements of Allocator.

<h2>Return value</h2>

Returns true if a match exists, false otherwise. In either case, the object m is updated, as follows: 
If the match does not exist: 
m.ready() == true 
m.empty() == true 
m.size() == 0 
If the match exists: 
m.ready() true 
m.empty() false 
m.size() number of marked_subexpressions plus 1, that is, 1+e.mark_count() 
m.prefix().first first 
m.prefix().second m[0].first 
m.prefix().matched m.prefix().first != m.prefix().second 
m.suffix().first m[0].second 
m.suffix().second last 
m.suffix().matched m.suffix().first != m.suffix().second 
m[0].first the start of the matching sequence 
m[0].second the end of the matching sequence 
m[0].matched true 
m[n].first the start of the sequence that matched marked_sub-expression n, or last if the subexpression did not participate in the match 
m[n].second the end of the sequence that matched marked_sub-expression n, or last if the subexpression did not participate in the match 
m[n].matched true if sub-expression n participated in the match, false otherwise 

<h2>Notes</h2>

In order to examine all matches within the target sequence, std::regex_search may be called in a loop, restarting each time from m[0].second of the previous call. std::regex_iterator offers an easy interface to this iteration. 

<h2>Example</h2>

// Run this code <pre><code>#include &lt;iostream&gt;

#include &lt;string&gt;

#include &lt;regex&gt;
int main()

{
    std::string lines[] = {&quot;Roses are #ff0000&quot;,
                           &quot;violets are #0000ff&quot;,
                           &quot;all of my base are belong to you&quot;};
    std::regex color_regex(&quot;#([a-f0-9]{2})&quot;
                           &quot;([a-f0-9]{2})&quot;
                           &quot;([a-f0-9]{2})&quot;);
    // simple match
    for (const auto &amp;line : lines) {
        std::cout &lt;&lt; line &lt;&lt; &quot;: &quot; &lt;&lt; std::boolalpha
                  &lt;&lt; std::regex_search(line, color_regex) &lt;&lt; '\n';
    }
    std::cout &lt;&lt; '\n';
    // show contents of marked subexpressions within each match
    std::smatch color_match;
    for (const auto &amp;line : lines) {
        if (std::regex_search(line, color_match, color_regex)) {
            std::cout &lt;&lt; &quot;matches for '&quot; &lt;&lt; line &lt;&lt; &quot;'\n&quot;;
            std::cout &lt;&lt; &quot;Prefix: '&quot; &lt;&lt; color_match.prefix() &lt;&lt; &quot;'\n&quot;;
            for (size_t i = 0; i &lt; color_match.size(); ++i)
                std::cout &lt;&lt; i &lt;&lt; &quot;: &quot; &lt;&lt; color_match[i] &lt;&lt; '\n';
            std::cout &lt;&lt; &quot;Suffix: '&quot; &lt;&lt; color_match.suffix() &lt;&lt; &quot;\'\n\n&quot;;
        }
    }
    // repeated search (see also std::regex_iterator)
    std::string log(R&quot;(
          Speed:      366
      Mass:       35
      Speed:      378
      Mass:       32
      Speed:      400

      Mass:   30)&quot;);
    std::regex r(R&quot;(Speed:\t\d*)&quot;);
    std::smatch sm;
    while (regex_search(log, sm, r)) {
        std::cout &lt;&lt; sm.str() &lt;&lt; '\n';
        log = sm.suffix();
    }
    // C-style string demo
    std::cmatch cm;
    if (std::regex_search(&quot;this is a test&quot;, cm, std::regex(&quot;test&quot;)))
        std::cout &lt;&lt; &quot;\nFound &quot; &lt;&lt; cm[0] &lt;&lt; &quot; at position &quot; &lt;&lt; cm.prefix().length();
}
</code></pre>

<h2>Output:</h2>

&nbsp;<wbr>&nbsp;Roses are #ff0000: true 
&nbsp;<wbr>&nbsp;violets are #0000ff: true 
&nbsp;<wbr>&nbsp;all of my base are belong to you: false 

 
&nbsp;<wbr>&nbsp;matches for 'Roses are #ff0000' 
&nbsp;<wbr>&nbsp;Prefix: 'Roses are ' 
&nbsp;<wbr>&nbsp;0: #ff0000 
&nbsp;<wbr>&nbsp;1: ff 
&nbsp;<wbr>&nbsp;2: 00 
&nbsp;<wbr>&nbsp;3: 00 
&nbsp;<wbr>&nbsp;Suffix: '' 

 
&nbsp;<wbr>&nbsp;matches for 'violets are #0000ff' 
&nbsp;<wbr>&nbsp;Prefix: 'violets are ' 
&nbsp;<wbr>&nbsp;0: #0000ff 
&nbsp;<wbr>&nbsp;1: 00 
&nbsp;<wbr>&nbsp;2: 00 
&nbsp;<wbr>&nbsp;3: ff 
&nbsp;<wbr>&nbsp;Suffix: '' 

 
&nbsp;<wbr>&nbsp;Speed:<tt> </tt>366
 
&nbsp;<wbr>&nbsp;Speed:<tt> </tt>378
 
&nbsp;<wbr>&nbsp;Speed:<tt> </tt>400
 

 
&nbsp;<wbr>&nbsp;Found test at position 10

<h2>See also</h2>

basic_regex regular expression object 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(class template)</i> 
<i>(C++11)</i> 
match_results identifies one regular expression match, including all sub-expression matches 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(class template)</i> 
<i>(C++11)</i> 
regex_match attempts to match a regular expression to an entire character sequence 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function template)</i> 
<i>(C++11)</i> 
