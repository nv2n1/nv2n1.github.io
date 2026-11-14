---
title: "stdfilesystemfilesystem_errorfilesystem_error(3)"
name: "stdfilesystemfilesystem_errorfilesystem_error"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdfilesystemfilesystem_errorfilesystem_error/"
---

std::filesystem::filesystem_error::filesystem_error - std::filesystem::filesystem_error::filesystem_error

<h2>Synopsis</h2>

<pre><code>filesystem_error(const std::string &amp;what_arg, (1)(since C++ 17)

                                                  std::error_code ec);

filesystem_error(const std::string &amp;what_arg,

                 const std::filesystem::path &amp;p1, (2)(since C++ 17)

                                                      std::error_code ec);

filesystem_error(const std::string &amp;what_arg,

                 const std::filesystem::path &amp;p1, (3)(since C++ 17)

                                                      const std::filesystem::path &amp;p2,

                 std::error_code ec);</code></pre> 
Constructs a new filesystem error object. The error code is set to ec and optionally, the paths that were involved in the operation that resulted in the error, are set to p1 and p2. what() after construction returns a string that contains what_arg. 

<h2>Parameters</h2>

&nbsp;This section is incomplete

<h2>Example</h2>

&nbsp;This section is incomplete 
&nbsp;Reason: no example 
