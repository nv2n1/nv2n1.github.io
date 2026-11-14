---
title: "stdchronotzdb_listfront(3)"
name: "stdchronotzdb_listfront"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdchronotzdb_listfront/"
---

std::chrono::tzdb_list::front - std::chrono::tzdb_list::front

<h2>Synopsis</h2>

<pre><code>const std::chrono::tzdb &amp;front() const noexcept;
(since C++ 20)</code></pre> 
Obtains a reference to the first std::chrono::tzdb in the list. Simultaneous calls to this function and std::chrono::reload_tzdb() does not introduce a data race. 
