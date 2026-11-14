---
title: "stdexperimentalfilesystemabsolutestdexperimentalfilesystemsystem_complete(3)"
name: "stdexperimentalfilesystemabsolutestdexperimentalfilesystemsystem_complete"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdexperimentalfilesystemabsolutestdexperimentalfilesystemsystem_complete/"
description: "std::experimental::filesystem::absolute,std::experimental::filesystem::system_complete – std::experimental::filesystem::absolute,std::experimental::filesystem::system_complete"
---

<p>std::experimental::filesystem::absolute,std::experimental::filesystem::system_complete &#8211; std::experimental::filesystem::absolute,std::experimental::filesystem::system_complete</p>
<h2>Synopsis</h2>
<pre><code>Defined in header&lt;experimental / filesystem&gt;

    path absolute(const path &amp;p, const path &amp;base = current_path());
(1)(filesystem TS)

    path system_complete(const path &amp;p);
(2)(filesystem TS)

    path system_complete(const path &amp;p, error_code &amp;ec);</code></pre>
<p>1) Returns absolute path of p relative to base according to the following rules:<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;* If p has both root name and root directory (e.g. &quot;C:
