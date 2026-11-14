---
title: "stdios_baseseekdir(3)"
name: "stdios_baseseekdir"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdios_baseseekdir/"
---

std::ios_base::seekdir - std::ios_base::seekdir

<h2>Synopsis</h2>

<pre><code>typedef /*implementation defined*/ seekdir;

static constexpr seekdir beg = /*implementation defined*/

static constexpr seekdir end = /*implementation defined*/

static constexpr seekdir cur = /*implementation defined*/</code></pre> 
Specifies file seeking direction type. The following constants are defined: 
Constant Explanation 
beg the beginning of a stream 
end the ending of a stream 
cur the current position of stream position indicator 

<h2>Example</h2>

&nbsp;This section is incomplete 
&nbsp;Reason: no example 

<h2>See also</h2>

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;sets the input position indicator 
seekg <i>(public member function of std::basic_istream&lt;CharT,Traits&gt;)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;sets the output position indicator 
seekp <i>(public member function of std::basic_ostream&lt;CharT,Traits&gt;)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;invokes seekoff() 
pubseekoff <i>(public member function of std::basic_streambuf&lt;CharT,Traits&gt;)</i> 
