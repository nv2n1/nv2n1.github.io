---
title: "stdchars_format(3)"
name: "stdchars_format"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdchars_format/"
---

std::chars_format - std::chars_format

<h2>Synopsis</h2>

<pre><code>Defined in header &lt;charconv&gt;

enum class chars_format {

    scientific = /*unspecified*/,

    fixed = /*unspecified*/,       (since C++17)

    hex = /*unspecified*/,

    general = fixed | scientific

};</code></pre> 
A BitmaskType used to specify floating-point formatting for std::to_chars and std::from_chars 

<h2>See also</h2>

to_chars converts an integer or floating-point value to a character sequence 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function)</i> 
<i>(C++17)</i> 
from_chars converts a character sequence to an integer or floating-point value 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function)</i> 
<i>(C++17)</i> 
