---
title: "npm-completion(1)"
name: "npm-completion"
section: "1"
letter: "n"
url: "/docs/linux/man/1-npm-completion/"
description: "npm-completion – Tab Completion for npm"
---

<h2 class="name">NAME</h2>
<p> <code>npm-completion</code> &#8211; Tab Completion for npm </p>
<h3>Synopsis</h3>
<dl>
<dt>
<dd>
<pre>
source &lt;(npm completion)
</pre>
</dl>
<h3>Description</h3>
<p> Enables tab-completion in all npm commands. </p>
<p> The synopsis above loads the completions into your current shell. Adding it to your ~/.bashrc or ~/.zshrc will make the completions available everywhere: </p>
<dl>
<dt>
<dd>
<pre>
npm completion &gt;&gt; ~/.bashrc
npm completion &gt;&gt; ~/.zshrc
</pre>
</dl>
<p> You may of course also pipe the output of <code>npm completion</code> to a file such as <code>/usr/local/etc/bash_completion.d/npm</code> or <code>/etc/bash_completion.d/npm</code> if you have a system that will read that file for you. </p>
<p> When <code>COMP_CWORD</code>, <code>COMP_LINE</code>, and <code>COMP_POINT</code> are defined in the environment, <code>npm completion</code> acts in &quot;plumbing mode&quot;, and outputs completions based on the arguments.</p>
<h3>See Also</h3>
<dl>
<dt>
<dd>
<dl>
<dt>&bull;</p>
<dd> npm help developers</p>
<dt>&bull;</p>
<dd> npm help npm </p>
</dl>
</dl>
<h2>Index</h2>
