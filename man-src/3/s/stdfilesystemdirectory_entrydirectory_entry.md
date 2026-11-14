---
title: "stdfilesystemdirectory_entrydirectory_entry(3)"
name: "stdfilesystemdirectory_entrydirectory_entry"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdfilesystemdirectory_entrydirectory_entry/"
---

std::filesystem::directory_entry::directory_entry - std::filesystem::directory_entry::directory_entry

<h2>Synopsis</h2>

<pre><code>directory_entry() noexcept = default;
(1)(since C++ 17)

    directory_entry(const directory_entry &amp;) = default;
(2)(since C++ 17)

    directory_entry(directory_entry &amp;&amp;) noexcept = default;
(3)(since C++ 17)

    explicit directory_entry(const std::filesystem::path &amp;p);
(4)(since C++ 17)

    directory_entry(const std::filesystem::path &amp;p, std::error_code &amp;ec);</code></pre> 
Constructs a new directory_entry object. 
1) Default constructor. 
2) Defaulted copy constructor. 
3) Defaulted move constructor. 
4) Initializes the directory entry with path p and calls refresh to update the cached attributes. If an error occurs, the non-throwing overload leaves the directory_entry holding a default-constructed path. 

<h2>Parameters</h2>

p - path to the filesystem object to which the directory entry will refer 
ec - out-parameter for error reporting in the non-throwing overload

<h2>Exceptions</h2>

The overload that does not take a std::error_code&amp; parameter throws filesystem_error on underlying OS API errors, constructed with p as the first path argument and the OS error code as the error code argument. The overload taking a std::error_code&amp; parameter sets it to the OS API error code if an OS API call fails, and executes ec.clear() if no errors occur. Any overload not marked noexcept may throw std::bad_alloc if memory allocation fails.

<h2>Example</h2>

&nbsp;This section is incomplete 
&nbsp;Reason: no example 
