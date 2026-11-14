---
title: "stdwregex(3)"
name: "stdwregex"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdwregex/"
---

std::basic_regex - std::basic_regex

<h2>Synopsis</h2>

<pre><code>Defined in header &lt;regex&gt;

template &lt;

class CharT,                             (since C++11)

class Traits = std::regex_traits&lt;CharT&gt;

&gt; class basic_regex;</code></pre> 
The class template basic_regex provides a general framework for holding regular expressions. 
Several specializations for common character types are provided: 
Defined in header &lt;regex&gt; 
Type Definition 
regex basic_regex&lt;char&gt; 
wregex basic_regex&lt;wchar_t&gt; 

<h2>Member types</h2>

Member type Definition 
value_type CharT 
traits_type Traits 
string_type Traits::string_type 
locale_type Traits::locale_type 
flag_type std::regex_constants::syntax_option_type

<h2>Member functions</h2>

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;constructs the regex object 
constructor <i>(public member function)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;destructs the regex object 
destructor <i>(public member function)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;assigns the contents 
operator= <i>(public member function)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;assigns the contents 
assign <i>(public member function)</i>

<h2>Observers</h2>

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;returns the number of marked sub-expressions within the regular expression 
mark_count <i>(public member function)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;returns the syntax flags 
flags <i>(public member function)</i>

<h2>Locale</h2>

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;get locale information 
getloc <i>(public member function)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;set locale information 
imbue <i>(public member function)</i>

<h2>Modifiers</h2>

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;swaps the contents 
swap <i>(public member function)</i>

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
The member constants in basic_regex are duplicates of the syntax_option_type constants defined in the namespace std::regex_constants.

<h2>Non-member functions</h2>

std::swap(std::basic_regex) specializes the std::swap algorithm 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function template)</i> 
<i>(C++11)</i> 

 

 
Deduction_guides<i>(since C++17)</i>
