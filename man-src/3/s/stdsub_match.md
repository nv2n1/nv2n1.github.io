---
title: "stdsub_match(3)"
name: "stdsub_match"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdsub_match/"
---

std::sub_match - std::sub_match

<h2>Synopsis</h2>

<pre><code>Defined in header &lt;regex&gt;

template&lt;

class BidirIt              (since C++11)

&gt; class sub_match;</code></pre> 
The class template sub_match is used by the regular expression engine to denote sequences of characters matched by marked sub-expressions. A match is a [begin, end) pair within the target range matched by the regular expression, but with additional observer functions to enhance code clarity. 
Only the default constructor is publicly accessible. Instances of sub_match are normally constructed and populated as a part of a std::match_results container during the processing of one of the regex algorithms. 
The member functions return defined default values unless the matched member is true. 
sub_match inherits from std::pair&lt;BidirIt, BidirIt&gt;, although it cannot be treated as a std::pair object because member functions such as swap and assignment will not work as expected. 

<h2>Type requirements</h2>

- 
BidirIt must meet the requirements of LegacyBidirectionalIterator.

<h2>Specializations</h2>

Several specializations for common character sequence types are provided: 

 
Defined in header &lt;regex&gt; 
Type Definition 
csub_match sub_match&lt;const char*&gt; 
wcsub_match sub_match&lt;const wchar_t*&gt; 
ssub_match sub_match&lt;std::string::const_iterator&gt; 
wssub_match sub_match&lt;std::wstring::const_iterator&gt;

<h2>Member types</h2>

Member type Definition 
iterator BidirIt 
value_type std::iterator_traits&lt;BidirIt&gt;::value_type 
difference_type std::iterator_traits&lt;BidirIt&gt;::difference_type 
string_type std::basic_string&lt;value_type&gt;

<h2>Member objects</h2>

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Indicates if this match was successful 
bool matched <i>(public member object)</i> 

 

 
Inherited from std::pair 

 

 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Start of the match sequence. 
BidirIt first <i>(public member object)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;One-past-the-end of the match sequence. 
BidirIt second <i>(public member object)</i>

<h2>Member functions</h2>

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;constructs the match object 
constructor <i>(public member function)</i>

<h2>Observers</h2>

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;returns the length of the match (if any) 
length <i>(public member function)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;converts to the underlying string type 
str <i>(public member function)</i> 
operator_string_type 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;compares matched subsequence (if any) 
compare <i>(public member function)</i>

<h2>Non-member functions</h2>

operator== 
operator!= compares two sub_match objects 
operator&lt; <i>(function template)</i> 
operator&lt;= 
operator&gt; 
operator&gt;= 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;outputs the matched character subsequence 
operator&lt;&lt; <i>(function template)</i>

<h2>See also</h2>

regex_token_iterator iterates through regex submatches 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(class template)</i> 
<i>(C++11)</i> 
