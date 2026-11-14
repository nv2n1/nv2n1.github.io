---
title: "stdexperimentalfilesystemdirectory_options(3)"
name: "stdexperimentalfilesystemdirectory_options"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdexperimentalfilesystemdirectory_options/"
---

std::experimental::filesystem::directory_options - std::experimental::filesystem::directory_options

<h2>Synopsis</h2>

<pre><code>Defined in header &lt;experimental/filesystem&gt;

enum class directory_options {

    none,

    follow_directory_symlink,                    (filesystem TS)

    skip_permission_denied

};</code></pre> 
This type represents available options that control the behavior of the directory_iterator and recursive_directory_iterator. 
directory_options satisfies the requirements of BitmaskType (which means the bitwise operators operator&amp;, operator|, operator^, operator~, operator&amp;=, operator|=, and operator^= are defined for this type) 

<h2>Member constants</h2>

Member constant Value Meaning 
follow_directory_symlink 1 Follow rather than skip directory symlinks. 
skip_permission_denied 2 Skip directories that would otherwise result in permission denied errors.

<h2>See also</h2>

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;constructs a directory iterator 
constructor <i>(public member function of std::experimental::filesystem::directory_iterator)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;constructs a recursive directory iterator 
constructor <i>(public member function of std::experimental::filesystem::recursive_directory_iterator)</i> 
