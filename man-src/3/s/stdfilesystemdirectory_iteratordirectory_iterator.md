---
title: "stdfilesystemdirectory_iteratordirectory_iterator(3)"
name: "stdfilesystemdirectory_iteratordirectory_iterator"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdfilesystemdirectory_iteratordirectory_iterator/"
description: "std::filesystem::directory_iterator::directory_iterator – std::filesystem::directory_iterator::directory_iterator"
---

<p>std::filesystem::directory_iterator::directory_iterator &#8211; std::filesystem::directory_iterator::directory_iterator</p>
<h2>Synopsis</h2>
<pre><code>directory_iterator() noexcept;
(1)(since C++ 17)

    explicit directory_iterator(const std::filesystem::path &amp;p);
(2)(since C++ 17)

    directory_iterator(const std::filesystem::path &amp;p, (3)(since C++ 17)

                                                           std::filesystem::directory_options options);

directory_iterator(const std::filesystem::path &amp;p, std::error_code &amp;ec);
(4)(since C++ 17)

    directory_iterator(const std::filesystem::path &amp;p,

                       std::filesystem::directory_options options, (5)(since C++ 17)

                                                                       std::error_code &amp;ec);

directory_iterator(const directory_iterator &amp;) = default;
(6)(since C++ 17)

    directory_iterator(directory_iterator &amp;&amp;) = default;
(7)(since C++ 17)</code></pre>
<p>Constructs a new directory iterator.<br />
1) Constructs the end iterator.<br />
2) Constructs a directory iterator that refers to the first directory entry of a directory identified by p. If p refers to an non-existing file or not a directory, throws std::filesystem::filesystem_error.<br />
3) Same as <code>(2)</code>, but if std::filesystem::directory_options::skip_permission_denied is set in options and construction encounters a permissions denied error, constructs the end iterator and does not report an error.<br />
4) Constructs a directory iterator that refers to the first directory entry of a directory identified by p. If p refers to an non-existing file or not a directory, returns the end iterator and sets ec.<br />
5) Same as <code>(4)</code>, but if std::filesystem::directory_options::skip_permission_denied is set in options and construction encounters a permissions denied error, constructs the end iterator and does not report an error. </p>
<h2>Parameters</h2>
<p>&nbsp;This section is incomplete</p>
<h2>Exceptions</h2>
<p>2-5) The overload that does not take a std::error_code&amp; parameter throws filesystem_error on underlying OS API errors, constructed with p as the first path argument and the OS error code as the error code argument. The overload taking a std::error_code&amp; parameter sets it to the OS API error code if an OS API call fails, and executes ec.clear() if no errors occur. Any overload not marked noexcept may throw std::bad_alloc if memory allocation fails.</p>
<h2>Notes</h2>
<p>To iterate over the current directory, construct the iterator as directory_iterator(&quot;.&quot;) instead of directory_iterator(&quot;&quot;).<br />
Defect reports<br />
The following behavior-changing defect reports were applied retroactively to previously published C++ standards.<br />
DR Applied to Behavior as published Correct behavior<br />
LWG_3013 C++17 error_code overload marked noexcept but can allocate memory noexcept removed </p>
