---
title: "stdfilesystemdirectory_entryassign(3)"
name: "stdfilesystemdirectory_entryassign"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdfilesystemdirectory_entryassign/"
---

std::filesystem::directory_entry::assign - std::filesystem::directory_entry::assign

<h2>Synopsis</h2>

<pre><code>void assign(const std::filesystem::path &amp;p);
(since C++ 17)

    void assign(const std::filesystem::path &amp;p, std::error_code &amp;ec);</code></pre> 
Assigns new content to the directory entry object. Sets the path to p and calls refresh to update the cached attributes. If an error occurs, the values of the cached attributes are unspecified. 

<h2>Parameters</h2>

p - path to the filesystem object to which the directory entry will refer 
ec - out-parameter for error reporting in the non-throwing overload

<h2>Return value</h2>

<i>(none)</i> 

<h2>Exceptions</h2>

The overload that does not take a std::error_code&amp; parameter throws filesystem_error on underlying OS API errors, constructed with p as the first path argument and the OS error code as the error code argument. The overload taking a std::error_code&amp; parameter sets it to the OS API error code if an OS API call fails, and executes ec.clear() if no errors occur. Any overload not marked noexcept may throw std::bad_alloc if memory allocation fails.

<h2>Example</h2>

&nbsp;This section is incomplete 
&nbsp;Reason: no example 

<h2>See also</h2>

<pre><code>assigns contents

operator= (public member function)




</code></pre>
