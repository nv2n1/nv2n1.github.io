---
title: "splitword(1)"
name: "splitword"
section: "1"
letter: "s"
url: "/docs/linux/man/1-splitword/"
description: "splitwd – Collect several text-form dictionary files into a single file to make a <1 line / 1 word type / 1 candidate> format."
---

<h2>NAME</h2>
<p> splitwd &#8211; Collect several text-form dictionary files into a single file to make a &lt;1 line / 1 word type / 1 candidate&gt; format.</p>
<h2>SYNOPSISS</h2>
<p> <code>splitwd </code><i>textjisho</i> &#8230;</p>
<h2>DESCRIPTION</h2>
<p> If the file in which you registered words consists of several subfiles, it must be converted into a proper format before the word dictionary is created. splitword converts such text-form dictionaries <i>textjisho</i> to make a &lt;1 line / 1 word type / 1 candidate&gt; format. The result is output to the standard output.</p>
<h2>EXAMPLE</h2>
<pre>
% splitwd user1.t user2.t | ctow
</pre>
<p> Reads text-form dictionaries user1.t and user2.t, then modifies them into the &lt;1 word type, 1 candidate on 1 line&gt; format. The contents are converted into the Wnn textform dictionary, then output to the standard output.</p>
<h2>SEE ALSO</h2>
<dl>
<dt><a href="/docs/linux/man/1-ctow/">ctow</a>(1)</p>
<dd>
</dl>
<h2>Index</h2>
