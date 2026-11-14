---
title: "git-mailsplit(1)"
name: "git-mailsplit"
section: "1"
letter: "g"
url: "/docs/linux/man/1-git-mailsplit/"
description: "git-mailsplit – Simple UNIX mbox splitter program"
---

<h2 class="name">NAME</h2>
<p> git-mailsplit &#8211; Simple UNIX mbox splitter program </p>
<h2>SYNOPSIS</h2>
<pre><code>
git mailsplit[-b][-f&lt;nn&gt;][-d&lt;prec&gt;][--keep - cr][--mboxrd] - o&lt;directory&gt;[--][(&lt;mbox&gt; | &lt;Maildir&gt;)...]
</code></pre>
<h2>DESCRIPTION</h2>
<p> Splits a mbox file or a Maildir into a list of files: &quot;0001&quot; &quot;0002&quot; .. in the specified directory so you can process them further from there. </p>
<dl>
<dt>
<dd>
 <font SIZE="+1"> <code>Important</code> </font> </p>
<p> Maildir splitting relies upon filenames being sorted to output patches in the correct order. </p>
</dl>
<h2>OPTIONS</h2>
<p> &lt;mbox&gt;</p>
<dl>
<dt>
<dd> Mbox file to split. If not given, the mbox is read from the standard input.</dl>
<p> &lt;Maildir&gt;</p>
<dl>
<dt>
<dd> Root of the Maildir to split. This directory should contain the cur, tmp and new subdirectories.</dl>
<p> -o&lt;directory&gt;</p>
<dl>
<dt>
<dd> Directory in which to place the individual messages.</dl>
<p> -b</p>
<dl>
<dt>
<dd> If any file doesn&#8217;t begin with a From line, assume it is a single mail message instead of signaling error.</dl>
<p> -d&lt;prec&gt;</p>
<dl>
<dt>
<dd> Instead of the default 4 digits with leading zeros, different precision can be specified for the generated filenames.</dl>
<p> -f&lt;nn&gt;</p>
<dl>
<dt>
<dd> Skip the first &lt;nn&gt; numbers, for example if -f3 is specified, start the numbering with 0004.</dl>
<p> &#8211;keep-cr</p>
<dl>
<dt>
<dd> Do not remove <code></code> from lines ending with <code>
</code>.</dl>
<p> &#8211;mboxrd</p>
<dl>
<dt>
<dd> Input is of the &quot;mboxrd&quot; format and &quot;^&gt;+From &quot; line escaping is reversed.</dl>
<h2>GIT</h2>
<p> Part of the <code><a href="/docs/linux/man/1-git/">git</a></code>(1) suite </p>
<h2>Index</h2>
