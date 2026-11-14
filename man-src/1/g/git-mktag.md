---
title: "git-mktag(1)"
name: "git-mktag"
section: "1"
letter: "g"
url: "/docs/linux/man/1-git-mktag/"
description: "git-mktag – Creates a tag object with extra validation"
---

<h2 class="name">NAME</h2>
<p> git-mktag &#8211; Creates a tag object with extra validation </p>
<h2>SYNOPSIS</h2>
<pre>
<i>git mktag</i>
</pre>
<h2>DESCRIPTION</h2>
<p> Reads a tag contents on standard input and creates a tag object. The output is the new tag&#8217;s &lt;object&gt; identifier. </p>
<p> This command is mostly equivalent to <code><a href="/docs/linux/man/1-git-hash-object/">git-hash-object</a></code>(1) invoked with <code>-t tag -w &#8211;stdin</code>. I.e. both of these will create and write a tag found in <code>my-tag</code>: </p>
<dl>
<dt>
<dd>
<pre>
git mktag &lt;my-tag
git hash-object -t tag -w --stdin &lt;my-tag
</pre>
</dl>
<p> The difference is that mktag will die before writing the tag if the tag doesn&#8217;t pass a <code><a href="/docs/linux/man/1-git-fsck/">git-fsck</a></code>(1) check. </p>
<p> The &quot;fsck&quot; check done mktag is stricter than what <code><a href="/docs/linux/man/1-git-fsck/">git-fsck</a></code>(1) would run by default in that all <code>fsck.&lt;msg-id&gt;</code> messages are promoted from warnings to errors (so e.g. a missing &quot;tagger&quot; line is an error). </p>
<p> Extra headers in the object are also an error under mktag, but ignored by <code><a href="/docs/linux/man/1-git-fsck/">git-fsck</a></code>(1). This extra check can be turned off by setting the appropriate <code>fsck.&lt;msg-id&gt;</code> varible: </p>
<dl>
<dt>
<dd>
<pre>
git -c fsck.extraHeaderEntry=ignore mktag &lt;my-tag-with-headers
</pre>
</dl>
<h2>OPTIONS</h2>
<p> &#8211;strict</p>
<dl>
<dt>
<dd> By default mktag turns on the equivalent of <code><a href="/docs/linux/man/1-git-fsck/">git-fsck</a></code>(1) <code>&#8211;strict</code> mode. Use <code>&#8211;no-strict</code> to disable it.</dl>
<h2>TAG FORMAT</h2>
<p> A tag signature file, to be fed to this command&#8217;s standard input, has a very simple fixed format: four lines of </p>
<dl>
<dt>
<dd>
<pre>
object &lt;hash&gt;
type &lt;typename&gt;
tag &lt;tagname&gt;
tagger &lt;tagger&gt;
</pre>
</dl>
<p> followed by some <i>optional</i> free-form message (some tags created by older Git may not have <code>tagger</code> line). The message, when it exists, is separated by a blank line from the header. The message part may contain a signature that Git itself doesn&#8217;t care about, but that can be verified with gpg.</p>
<h2>GIT</h2>
<p> Part of the <code><a href="/docs/linux/man/1-git/">git</a></code>(1) suite </p>
<h2>Index</h2>
