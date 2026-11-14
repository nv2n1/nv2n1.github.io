---
title: "stdfilesystemdirectory_options(3)"
name: "stdfilesystemdirectory_options"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdfilesystemdirectory_options/"
---

std::filesystem::directory_options - std::filesystem::directory_options

<h2>Synopsis</h2>

<pre><code>Defined in header &lt;filesystem&gt;

enum class directory_options {

    none = /* unspecified */,

    follow_directory_symlink = /* unspecified */,  (since C++17)

    skip_permission_denied = /* unspecified */

};</code></pre> 
This type represents available options that control the behavior of the directory_iterator and recursive_directory_iterator. 
directory_options satisfies the requirements of BitmaskType (which means the bitwise operators operator&amp;, operator|, operator^, operator~, operator&amp;=, operator|=, and operator^= are defined for this type). none represents the empty bitmask; every other enumerator represents a distinct bitmask element. 

<h2>Member constants</h2>

Member constant Meaning 
none (Default) Skip directory symlinks, permission denied is error. 
follow_directory_symlink Follow rather than skip directory symlinks. 
skip_permission_denied Skip directories that would otherwise result in permission denied errors.

<h2>See also</h2>

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;constructs a directory iterator 
constructor <i>(public member function of std::filesystem::directory_iterator)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;constructs a recursive directory iterator 
constructor <i>(public member function of std::filesystem::recursive_directory_iterator)</i> 
