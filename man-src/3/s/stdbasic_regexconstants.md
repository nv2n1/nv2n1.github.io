---
title: "stdbasic_regexconstants(3)"
name: "stdbasic_regexconstants"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdbasic_regexconstants/"
---

std::basic_regexconstants - std::basic_regexconstants

<h2>Synopsis</h2>

<pre><code>Defined in header &lt;regex&gt;

static constexpr std::regex_constants::syntax_option_type icase =

std::regex_constants::icase;

static constexpr std::regex_constants::syntax_option_type nosubs =

std::regex_constants::nosubs;

static constexpr std::regex_constants::syntax_option_type optimize =

std::regex_constants::optimize;

static constexpr std::regex_constants::syntax_option_type collate =

std::regex_constants::collate;

static constexpr std::regex_constants::syntax_option_type ECMAScript =

std::regex_constants::ECMAScript;

static constexpr std::regex_constants::syntax_option_type basic =

std::regex_constants::basic;

static constexpr std::regex_constants::syntax_option_type extended =

std::regex_constants::extended;

static constexpr std::regex_constants::syntax_option_type awk =

std::regex_constants::awk;

static constexpr std::regex_constants::syntax_option_type grep =

std::regex_constants::grep;

static constexpr std::regex_constants::syntax_option_type egrep =

std::regex_constants::egrep;

static constexpr std::regex_constants::syntax_option_type multiline =   (since C++17)

std::regex_constants::multiline;</code></pre> 
std::basic_regex defines several constants that govern general regex matching syntax. 
These constants are duplicated from std::regex_constants: 
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

<h2>See also</h2>

syntax_option_type general options controlling regex behavior 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(typedef)</i> 
<i>(C++11)</i> 
