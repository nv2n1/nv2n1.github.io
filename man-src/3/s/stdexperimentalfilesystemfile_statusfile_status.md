---
title: "stdexperimentalfilesystemfile_statusfile_status(3)"
name: "stdexperimentalfilesystemfile_statusfile_status"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdexperimentalfilesystemfile_statusfile_status/"
---

std::experimental::filesystem::file_status::file_status - std::experimental::filesystem::file_status::file_status

<h2>Synopsis</h2>

<pre><code>file_status(const file_status &amp;) = default;
(1)(filesystem TS)

    file_status(file_status &amp;&amp;) = default;
(2)(filesystem TS)

    explicit file_status(file_type type = file_type::none, (3)(filesystem TS)

                                                               perms permissions = perms::unknown);</code></pre> 
Constructs a new file_status object. 
1) Default copy constructor. 
2) Default move constructor. 
3) Initializes the file status object with type as type and permissions as permissions. 

<h2>Parameters</h2>

&nbsp;This section is incomplete

<h2>Exceptions</h2>

noexcept specification: 
noexcept
