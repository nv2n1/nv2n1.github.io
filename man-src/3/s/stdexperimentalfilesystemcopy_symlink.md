---
title: "stdexperimentalfilesystemcopy_symlink(3)"
name: "stdexperimentalfilesystemcopy_symlink"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdexperimentalfilesystemcopy_symlink/"
---

std::experimental::filesystem::copy_symlink - std::experimental::filesystem::copy_symlink

<h2>Synopsis</h2>

<pre><code>Defined in header&lt;experimental / filesystem&gt;

    void copy_symlink(const path &amp;from, const path &amp;to);
(1)(filesystem TS)

    void copy_symlink(const path &amp;from, const path &amp;to, (2)(filesystem TS)

                                                            error_code &amp;ec);</code></pre> 
Copies a symlink to another location. 
1) Effectively calls f(read_symlink(from), to) where f is create_symlink() or create_directory_symlink depending on whether from resolves to a file or directory. 
2) Effectively calls f(read_symlink(from, ec), to, ec) where f is create_symlink() or create_directory_symlink depending on whether from resolves to a file or directory. 

<h2>Parameters</h2>

from - path to a symbolic link to copy 
to - destination path of the new symlink 
ec - out-parameter for error reporting in the non-throwing overload

<h2>Return value</h2>

<i>(none)</i> 

<h2>Exceptions</h2>

The overload that does not take a error_code&amp; parameter throws filesystem_error on underlying OS API errors, constructed with from as the first argument, to as the second argument, and the OS error code as the error code argument. std::bad_alloc may be thrown if memory allocation fails. The overload taking a error_code&amp; parameter sets it to the OS API error code if an OS API call fails, and executes ec.clear() if no errors occur. This overload has 
noexcept specification: 
noexcept

<h2>See also</h2>

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;copies files or directories 
copy <i>(function)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;copies file contents 
copy_file <i>(function)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;creates a symbolic link 
create_symlink <i>(function)</i> 
create_directory_symlink 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;obtains the target of a symbolic link 
read_symlink <i>(function)</i> 
