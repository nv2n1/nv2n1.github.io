---
title: "stdregex_constantssyntax_option_type(3)"
name: "stdregex_constantssyntax_option_type"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdregex_constantssyntax_option_type/"
---

std::regex_constants::syntax_option_type - std::regex_constants::syntax_option_type

<h2>Synopsis</h2>

<pre><code>Defined in header &lt;regex&gt;

typedef /*unspecified*/ syntax_option_type;                        (since C++11)

constexpr syntax_option_type icase = /*unspecified*/;

constexpr syntax_option_type nosubs = /*unspecified*/;

constexpr syntax_option_type optimize = /*unspecified*/;

constexpr syntax_option_type collate = /*unspecified*/;

constexpr syntax_option_type ECMAScript = /*unspecified*/;         (since C++11)

constexpr syntax_option_type basic = /*unspecified*/;              (until C++17)

constexpr syntax_option_type extended = /*unspecified*/;

constexpr syntax_option_type awk = /*unspecified*/;

constexpr syntax_option_type grep = /*unspecified*/;

constexpr syntax_option_type egrep = /*unspecified*/;

inline constexpr syntax_option_type icase = /*unspecified*/;

inline constexpr syntax_option_type nosubs = /*unspecified*/;

inline constexpr syntax_option_type optimize = /*unspecified*/;

inline constexpr syntax_option_type collate = /*unspecified*/;

inline constexpr syntax_option_type ECMAScript = /*unspecified*/;

inline constexpr syntax_option_type basic = /*unspecified*/;       (since C++17)

inline constexpr syntax_option_type extended = /*unspecified*/;

inline constexpr syntax_option_type awk = /*unspecified*/;

inline constexpr syntax_option_type grep = /*unspecified*/;

inline constexpr syntax_option_type egrep = /*unspecified*/;
inline constexpr syntax_option_type multiline = /*unspecified*/;</code></pre> 
The syntax_option_type is a BitmaskType that contains options that govern how regular expressions behave. 
The possible values for this type (icase, optimize, etc.) are duplicated inside std::basic_regex. 

<h2>Constants</h2>

Value Effect(s) 
icase Character matching should be performed without regard to case. 
nosubs When performing matches, all marked sub-expressions (expr) are treated as non-marking sub-expressions (?:expr). No matches are stored in the supplied std::regex_match structure and mark_count() is zero 
optimize Instructs the regular expression engine to make matching faster, with the potential cost of making construction slower. For example, this might mean converting a non-deterministic FSA to a deterministic FSA. 
collate Character ranges of the form &quot;[a-b]&quot; will be locale sensitive. 
multiline <i>(C++17)</i> Specifies that ^ shall match the beginning of a line and $ shall match the end of a line, if the ECMAScript engine is selected. 
ECMAScript Use the Modified_ECMAScript_regular_expression_grammar 
basic Use the basic POSIX regular expression grammar (grammar_documentation). 
extended Use the extended POSIX regular expression grammar (grammar_documentation). 
awk Use the regular expression grammar used by the awk utility in POSIX (grammar_documentation) 
grep Use the regular expression grammar used by the grep utility in POSIX. This is effectively the same as the basic option with the addition of newline '\n' as an alternation separator. 
egrep Use the regular expression grammar used by the grep utility, with the -E option, in POSIX. This is effectively the same as the extended option with the addition of newline '\n' as an alternation separator in addtion to '|'. 

 
At most one grammar option must be chosen out of ECMAScript, basic, extended, awk, grep, egrep. If no grammar is chosen, ECMAScript is assumed to be selected. The other options serve as modifiers, such that std::regex(&quot;meow&quot;, std::regex::icase) is equivalent to std::regex(&quot;meow&quot;, std::regex::ECMAScript|std::regex::icase)

<h2>Notes</h2>

Because POSIX uses &quot;leftmost longest&quot; matching rule (the longest matching subsequence is matched, and if there are several such subsequences, the first one is matched), it is not suitable, for example, for parsing markup languages: a POSIX regex such as &quot;&lt;tag[^&gt;]*&gt;.*&lt;/tag&gt;&quot; would match everything from the first &quot;&lt;tag&quot; to the last &quot;&lt;/tag&gt;&quot;, including every &quot;&lt;/tag&gt;&quot; and &quot;&lt;tag&gt;&quot; inbetween. On the other hand, ECMAScript supports non-greedy matches, and the ECMAScript regex &quot;&lt;tag[^&gt;]*&gt;.*?&lt;/tag&gt;&quot; would match only until the first closing tag. 
In C++11, these constants were specified with redundant keyword static, which was removed by C++14 via LWG_issue_2053 

<h2>Example</h2>

Illustrates the difference in the matching algorithm between ECMAScript and POSIX regular expressions 
 // Run this code <pre><code>#include &lt;iostream&gt;

#include &lt;string&gt;

#include &lt;regex&gt;
int main()

{
    std::string str = &quot;zzxayyzz&quot;;
    std::regex re1(&quot;.*(a|xayy)&quot;);                       // ECMA
    std::regex re2(&quot;.*(a|xayy)&quot;, std::regex::extended); // POSIX
    std::cout &lt;&lt; &quot;Searching for .*(a|xayy) in zzxayyzz:\n&quot;;
    std::smatch m;
    std::regex_search(str, m, re1);
    std::cout &lt;&lt; &quot; ECMA (depth first search) match: &quot; &lt;&lt; m[0] &lt;&lt; '\n';
    std::regex_search(str, m, re2);
    std::cout &lt;&lt; &quot; POSIX (leftmost longest)  match: &quot; &lt;&lt; m[0] &lt;&lt; '\n';
}
</code></pre>

<h2>Output:</h2>

&nbsp;<wbr>&nbsp;Searching for .*(a|xayy) in zzxayyzz: 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;ECMA (depth first search) match: zzxa 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;POSIX (leftmost longest) match: zzxayy

<h2>See also</h2>

basic_regex regular expression object 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(class template)</i> 
<i>(C++11)</i> 
