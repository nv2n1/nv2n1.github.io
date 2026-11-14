---
title: "stdmessages_base(3)"
name: "stdmessages_base"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdmessages_base/"
---

std::messages_base - std::messages_base

<h2>Synopsis</h2>

<pre><code>Defined in header &lt;locale&gt;

class messages_base;</code></pre> 
The class std::messages_base provides a type definition which is inherited and used by the std::messages facets. 

<h2>Member types</h2>

Member type Definition 
catalog /*unspecified signed integer type*/

<h2>Notes</h2>

catalog was erroneously specified as int in C++11, this was corrected in LWG_issue_#2028 and included in C++14 

<h2>See also</h2>

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;implements retrieval of strings from message catalogs 
messages <i>(class template)</i> 
