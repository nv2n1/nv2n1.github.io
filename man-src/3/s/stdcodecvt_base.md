---
title: "stdcodecvt_base(3)"
name: "stdcodecvt_base"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdcodecvt_base/"
---

std::codecvt_base - std::codecvt_base

<h2>Synopsis</h2>

<pre><code>Defined in header &lt;locale&gt;

class codecvt_base;</code></pre> 
The class std::codecvt_base provides the conversion status constants which are inherited and used by the std::codecvt facets. 

<h2>Member types</h2>

Member type Definition 
enum result { ok, partial, error, noconv }; Unscoped enumeration type 

 

 
Value Explanation 
ok conversion was completed with no error 
partial not all source characters were converted 
error encountered an invalid character 
noconv no conversion required, input and output types are the same

<h2>Notes</h2>

The value std::codecvt_base::partial is used to indicate that either the destination range is too short to receive the results of the conversion or the input is truncated in the middle of an otherwise valid multibyte character. 

<h2>See also</h2>

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;converts between character encodings, including UTF-8, UTF-16, UTF-32 
codecvt <i>(class template)</i> 
