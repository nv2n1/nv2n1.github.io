---
title: "stdexperimentalfilesystemdirectory_entrydirectory_entry(3)"
name: "stdexperimentalfilesystemdirectory_entrydirectory_entry"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdexperimentalfilesystemdirectory_entrydirectory_entry/"
---

std::experimental::filesystem::directory_entry::directory_entry - std::experimental::filesystem::directory_entry::directory_entry

<h2>Synopsis</h2>

<pre><code>directory_entry() = default;
(1)(filesystem TS)

    directory_entry(const directory_entry &amp;) = default;
(2)(filesystem TS)

    directory_entry(directory_entry &amp;&amp;) = default;
(3)(filesystem TS)

    explicit directory_entry(const path &amp;p);
(4)(filesystem TS)</code></pre> 
Constructs a new directory_entry object. 
1) Default constructor. 
2) Default copy constructor. 
3) Default move constructor. 
4) Initializes the directory entry with path p. 

<h2>Parameters</h2>

&nbsp;This section is incomplete

<h2>Exceptions</h2>

&nbsp;This section is incomplete
