---
title: "stdfilesystemdirectory_entryhard_link_count(3)"
name: "stdfilesystemdirectory_entryhard_link_count"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdfilesystemdirectory_entryhard_link_count/"
---

std::filesystem::directory_entry::hard_link_count - std::filesystem::directory_entry::hard_link_count

<h2>Synopsis</h2>

<pre><code>std::uintmax_t hard_link_count() const;
(since C++ 17)

    std::uintmax_t hard_link_count(std::error_code &amp;ec) const noexcept;</code></pre> 
If the number of hard links is cached in this directory_entry, returns the cached value. Otherwise, returns std::filesystem::hard_link_count(path()) or std::filesystem::hard_link_count(path(), ec), respectively 

<h2>Parameters</h2>

ec - out-parameter for error reporting in the non-throwing overload

<h2>Return value</h2>

The number of hard links for the referred-to filesystem object 

<h2>Exceptions</h2>

The overload that does not take a std::error_code&amp; parameter throws filesystem_error on underlying OS API errors, constructed with p as the first path argument and the OS error code as the error code argument. The overload taking a std::error_code&amp; parameter sets it to the OS API error code if an OS API call fails, and executes ec.clear() if no errors occur. Any overload not marked noexcept may throw std::bad_alloc if memory allocation fails.

<h2>Example</h2>

&nbsp;This section is incomplete 
&nbsp;Reason: no example 

<h2>See also</h2>

hard_link_count returns the number of hard links referring to the specific file 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function)</i> 
<i>(C++17)</i> 
