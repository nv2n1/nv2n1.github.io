---
title: "stdfilesystemfile_statusfile_status(3)"
name: "stdfilesystemfile_statusfile_status"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdfilesystemfile_statusfile_status/"
description: "std::filesystem::file_status::file_status – std::filesystem::file_status::file_status"
---

<p>std::filesystem::file_status::file_status &#8211; std::filesystem::file_status::file_status</p>
<h2>Synopsis</h2>
<pre><code>file_status() noexcept
    : file_status(std::filesystem::file_type::none){}(1)(since C++ 17)

          file_status(const file_status &amp;) noexcept = default;
(2)(since C++ 17)

    file_status(file_status &amp;&amp;) noexcept = default;
(3)(since C++ 17)

    explicit file_status(

        std::filesystem::file_type type, (4)(since C++ 17)

                                             std::filesystem::perms permissions = std::filesystem::perms::unknown) noexcept;</code></pre>
<p>Constructs a new file_status object.<br />
1) Default constructor that calls <code>(4)</code> with std::filesystem::file_type::none.<br />
2-3) Copy and move constructors are defaulted.<br />
4) Initializes the file status object with type as type and permissions as permissions. </p>
<h2>Parameters</h2>
<p>type &#8211; type of the file status<br />
permissions &#8211; permissions of the file status</p>
<h2>Example</h2>
<p>&nbsp;This section is incomplete<br />
&nbsp;Reason: no example </p>
