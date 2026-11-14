---
title: "stdfilesystempathformat(3)"
name: "stdfilesystempathformat"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdfilesystempathformat/"
---

std::filesystem::path::format - std::filesystem::path::format

<h2>Synopsis</h2>

<pre><code>enum format {

    native_format,

    generic_format,  (since C++17)

    auto_format

};</code></pre> 
Determines how string representations of pathnames are interpreted by the constructors of std::filesystem::path that accept strings. 

<h2>Constants</h2>

Defined in header &lt;filesystem&gt; 
Value Explanation 
native_format Native pathname format 
generic_format Generic pathname format 
auto_format Implementation-defined pathname format, auto-detected where possible

<h2>Notes</h2>

On POSIX systems, there is no difference between native and generic format. 

<h2>See also</h2>

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;constructs a path 
constructor <i>(public member function)</i> 
