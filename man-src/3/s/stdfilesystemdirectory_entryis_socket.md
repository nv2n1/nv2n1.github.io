---
title: "stdfilesystemdirectory_entryis_socket(3)"
name: "stdfilesystemdirectory_entryis_socket"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdfilesystemdirectory_entryis_socket/"
---

std::filesystem::directory_entry::is_socket - std::filesystem::directory_entry::is_socket

<h2>Synopsis</h2>

<pre><code>bool is_socket() const;
(since C++ 17)

    bool is_socket(std::error_code &amp;ec) const noexcept;</code></pre> 
Checks whether the pointed-to object is a named socket. Effectively returns std::filesystem::is_socket(status()) or std::filesystem::is_socket(status(ec)), respectively 

<h2>Parameters</h2>

ec - out-parameter for error reporting in the non-throwing overload

<h2>Return value</h2>

true if the referred-to filesystem object is a named socket, false otherwise. 

<h2>Exceptions</h2>

The overload that does not take a std::error_code&amp; parameter throws filesystem_error on underlying OS API errors, constructed with p as the first path argument and the OS error code as the error code argument. The overload taking a std::error_code&amp; parameter sets it to the OS API error code if an OS API call fails, and executes ec.clear() if no errors occur. Any overload not marked noexcept may throw std::bad_alloc if memory allocation fails.

<h2>Example</h2>

&nbsp;This section is incomplete 
&nbsp;Reason: no example 

<h2>See also</h2>

is_socket checks whether the argument refers to a named IPC socket 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function)</i> 
<i>(C++17)</i> 
