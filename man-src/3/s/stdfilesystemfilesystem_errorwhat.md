---
title: "stdfilesystemfilesystem_errorwhat(3)"
name: "stdfilesystemfilesystem_errorwhat"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdfilesystemfilesystem_errorwhat/"
---

std::filesystem::filesystem_error::what - std::filesystem::filesystem_error::what

<h2>Synopsis</h2>

<pre><code>const char *what() const noexcept override;
(since C++ 17)</code></pre> 
Returns an explanatory byte string. This explanatory string contains the explanatory string passed at the time of construction. Implementations are encouraged to include the pathnames of path1() and path2() in native format and the std::system_error::what() string inside the returned string as well. 

<h2>Parameters</h2>

<i>(none)</i>

<h2>Example</h2>

&nbsp;This section is incomplete 
&nbsp;Reason: no example 
