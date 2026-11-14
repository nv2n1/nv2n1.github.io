---
title: "stdfilesystemfile_type(3)"
name: "stdfilesystemfile_type"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdfilesystemfile_type/"
---

std::filesystem::file_type - std::filesystem::file_type

<h2>Synopsis</h2>

<pre><code>Defined in header &lt;filesystem&gt;

enum class file_type {

    none = /* unspecified */,

    not_found = /* unspecified */,

    regular = /* unspecified */,

    directory = /* unspecified */,

    symlink = /* unspecified */,

    block = /* unspecified */,      (since C++17)

    character = /* unspecified */,

    fifo = /* unspecified */,

    socket = /* unspecified */,

    unknown = /* unspecified */,

    /* implementation-defined */

};</code></pre> 
file_type defines constants that indicate a type of a file or directory a path refers to. The value of the enumerators are distinct. 
&nbsp;This section is incomplete 

<h2>Constants</h2>

Constant Meaning 
none indicates that the file status has not been evaluated yet, or an error occurred when evaluating it 
not_found indicates that the file was not found (this is not considered an error) 
regular a regular file 
directory a directory 
symlink a symbolic link 
block a block special file 
character a character special file 
fifo a FIFO (also known as pipe) file 
socket a socket file 
implementation-defined an additional implementation-defined constant for each additional file type supported by the implementation 
unknown the file exists but its type could not be determined

<h2>See also</h2>

&nbsp;This section is incomplete 
