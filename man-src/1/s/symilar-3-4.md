---
title: "symilar-3-4(1)"
name: "symilar-3-4"
section: "1"
letter: "s"
url: "/docs/linux/man/1-symilar-3-4/"
description: "symilar – tool for checking similarities in different files"
---

<p><code>symilar</code> &#8211; tool for checking similarities in different files</p>
<h2>Synopsis</h2>
<p><code>symilar</code> [ <i>options</i> ] [ <i>&lt;files&gt;</i> ] </p>
<h2>Description</h2>
<p><code>symilar</code> is a tool for searching blocks of identical lines in different files. It can be used to find copy pasted blocks of code, or stuff that could be refactored. Differences concerning only stuff behind a &#8216;#&#8217; (Python comments) can be ignored. The size of identical blocks can be optionally modified. <code>symilar</code> &#8216;s functionality is integrated in <code>pylint</code> with the refactoring message &#8216;R0801&#8217;. </p>
<h2>Options</h2>
<dl COMPACT>
<dt>-h, &#8211;help</p>
<dd>show help message and exit</p>
<dt>-d &lt;min_duplicated_lines&gt;, &#8211;duplicates &lt;min_duplicated_lines&gt;</p>
<dd>minimum number of identical lines that should trigger a similarity message. Default is 4. So if it finds 3 identical lines, there will be no message, but 4 identical lines will be mentionned.</p>
<dt>-i, &#8211;ignore-comments</p>
<dd>ignore differences concerning only stuff behind a &#8216;#&#8217; (Python comments). This means that if just a comment was added, the message will still be triggered. </p>
</dl>
