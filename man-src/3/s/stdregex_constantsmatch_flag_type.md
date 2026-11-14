---
title: "stdregex_constantsmatch_flag_type(3)"
name: "stdregex_constantsmatch_flag_type"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdregex_constantsmatch_flag_type/"
---

std::regex_constants::match_flag_type - std::regex_constants::match_flag_type

<h2>Synopsis</h2>

<pre><code>Defined in header &lt;regex&gt;

typedef /*unspecified*/ match_flag_type;                               (since C++11)

constexpr match_flag_type match_default = 0;

constexpr match_flag_type match_not_bol = /*unspecified*/;

constexpr match_flag_type match_not_eol = /*unspecified*/;

constexpr match_flag_type match_not_bow = /*unspecified*/;

constexpr match_flag_type match_not_eow = /*unspecified*/;

constexpr match_flag_type match_any = /*unspecified*/;                 (since C++11)

constexpr match_flag_type match_not_null = /*unspecified*/;            (until C++17)

constexpr match_flag_type match_continuous = /*unspecified*/;

constexpr match_flag_type match_prev_avail = /*unspecified*/;

constexpr match_flag_type format_default = 0;

constexpr match_flag_type format_sed = /*unspecified*/;

constexpr match_flag_type format_no_copy = /*unspecified*/;

constexpr match_flag_type format_first_only = /*unspecified*/;

inline constexpr match_flag_type match_default = 0;

inline constexpr match_flag_type match_not_bol = /*unspecified*/;

inline constexpr match_flag_type match_not_eol = /*unspecified*/;

inline constexpr match_flag_type match_not_bow = /*unspecified*/;

inline constexpr match_flag_type match_not_eow = /*unspecified*/;

inline constexpr match_flag_type match_any = /*unspecified*/;

inline constexpr match_flag_type match_not_null = /*unspecified*/;     (since C++17)

inline constexpr match_flag_type match_continuous = /*unspecified*/;

inline constexpr match_flag_type match_prev_avail = /*unspecified*/;

inline constexpr match_flag_type format_default = 0;

inline constexpr match_flag_type format_sed = /*unspecified*/;

inline constexpr match_flag_type format_no_copy = /*unspecified*/;

inline constexpr match_flag_type format_first_only = /*unspecified*/;</code></pre> 
match_flag_type is a BitmaskType that specifies additional regular expression matching options. 

<h2>Constants</h2>

Note: [first, last) refers to the character sequence being matched. 

 
Constant Explanation 
match_not_bol The first character in [first,last) will be treated as if it is not at the beginning of a line (i.e. ^ will not match [first,first) 
match_not_eol The last character in [first,last) will be treated as if it is not at the end of a line (i.e. $ will not match [last,last) 
match_not_bow &quot;\b&quot; will not match [first,first) 
match_not_eow &quot;\b&quot; will not match [last,last) 
match_any If more than one match is possible, then any match is an acceptable result 
match_not_null Do not match empty sequences 
match_continuous Only match a sub-sequence that begins at first 
match_prev_avail --first is a valid iterator position. When set, causes match_not_bol and match_not_bow to be ignored 
format_default Use ECMAScript rules to construct strings in std::regex_replace (syntax_documentation) 
format_sed Use POSIX sed utility rules in std::regex_replace. (syntax_documentation) 
format_no_copy Do not copy un-matched strings to the output in std::regex_replace 
format_first_only Only replace the first match in std::regex_replace 

 
All constants, except for match_default and format_default, are bitmask elements. The match_default and format_default constants are empty bitmasks

<h2>Notes</h2>

In C++11, these constants were specified with redundant keyword static, which was removed by C++14 via LWG_issue_2053 

<h2>See also</h2>

regex_match attempts to match a regular expression to an entire character sequence 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function template)</i> 
<i>(C++11)</i> 
syntax_option_type general options controlling regex behavior 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(typedef)</i> 
<i>(C++11)</i> 
error_type describes different types of matching errors 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(typedef)</i> 
<i>(C++11)</i> 
