---
title: "git-check-mailmap(1)"
name: "git-check-mailmap"
section: "1"
letter: "g"
url: "/docs/linux/man/1-git-check-mailmap/"
description: "git-check-mailmap – Show canonical names and email addresses of contacts"
---

<h2 class="name">NAME</h2>
<p> git-check-mailmap &#8211; Show canonical names and email addresses of contacts </p>
<h2>SYNOPSIS</h2>
<pre>
<i>git check-mailmap</i> [&lt;options&gt;] &lt;contact&gt;...
</pre>
<h2>DESCRIPTION</h2>
<p> For each &#8220;Name &lt;user [at] host&gt;&#8221; or &#8220;&lt;user [at] host&gt;&#8221; from the command-line or standard input (when using <code>&#8211;stdin</code>), look up the person&#8217;s canonical name and email address (see &quot;Mapping Authors&quot; below). If found, print them; otherwise print the input as-is.</p>
<h2>OPTIONS</h2>
<p> &#8211;stdin</p>
<dl>
<dt>
<dd> Read contacts, one per line, from the standard input after exhausting contacts provided on the command-line.</dl>
<h2>OUTPUT</h2>
<p> For each contact, a single line is output, terminated by a newline. If the name is provided or known to the <i>mailmap</i>, &#8220;Name &lt;user [at] host&gt;&#8221; is printed; otherwise only &#8220;&lt;user [at] host&gt;&#8221; is printed.</p>
<h2>CONFIGURATION</h2>
<p> See <code>mailmap.file</code> and <code>mailmap.blob</code> in <code><a href="/docs/linux/man/1-git-config/">git-config</a></code>(1) for how to specify a custom <code>.mailmap</code> target file or object.</p>
<h2>MAPPING AUTHORS</h2>
<p> See <code><a href="/docs/linux/man/5-gitmailmap/">gitmailmap</a></code>(5).</p>
<h2>GIT</h2>
<p> Part of the <code><a href="/docs/linux/man/1-git/">git</a></code>(1) suite </p>
<h2>Index</h2>
