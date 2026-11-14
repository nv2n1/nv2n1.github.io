---
title: "stdfilesystemdirectory_entryreplace_filename(3)"
name: "stdfilesystemdirectory_entryreplace_filename"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdfilesystemdirectory_entryreplace_filename/"
---

std::filesystem::directory_entry::replace_filename - std::filesystem::directory_entry::replace_filename

<h2>Synopsis</h2>

<pre><code>void replace_filename(const std::filesystem::path &amp;p);
(since C++ 17)

    void replace_filename(const std::filesystem::path &amp;p, std::error_code &amp;ec);</code></pre> 
Changes the filename of the directory entry. 
Effectively modifies the path member by path.replace_filename(p) and calls refresh to update the cached attributes. If an error occurs, the values of the cached attributes are unspecified. 
This function does not commit any changes to the filesystem. 

<h2>Parameters</h2>

p - the path to append to the parent path of the currently stored path 
ec - out-parameter for error reporting in the non-throwing overload

<h2>Return value</h2>

<i>(none)</i> 

<h2>Exceptions</h2>

The overload that does not take a std::error_code&amp; parameter throws filesystem_error on underlying OS API errors, constructed with p as the first path argument and the OS error code as the error code argument. The overload taking a std::error_code&amp; parameter sets it to the OS API error code if an OS API call fails, and executes ec.clear() if no errors occur. Any overload not marked noexcept may throw std::bad_alloc if memory allocation fails.

<h2>Example</h2>

&nbsp;This section is incomplete 
&nbsp;Reason: no example 

<h2>See also</h2>

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;assigns contents 
assign <i>(public member function)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;replaces the last path component with another path 
replace_filename <i>(public member function of std::filesystem::path)</i> 
