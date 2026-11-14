---
title: "git-strip-merge(1)"
name: "git-strip-merge"
section: "1"
letter: "g"
url: "/docs/linux/man/1-git-strip-merge/"
description: "git-strip-merge – A git-merge wrapper that deletes files on a \"foreign\" branch before merging"
---

<h2 class="name">NAME</h2>
<p> git-strip-merge &#8211; A git-merge wrapper that deletes files on a &quot;foreign&quot; branch before merging </p>
<h2>SYNOPSIS</h2>
<p> <code>git-strip-merge</code> [<i>git-merge options</i>] [<code>-M</code> <i>&lt;commitmsg&gt;</i>] <i>&lt;branch&gt;</i> <i>FILE</i>&#8230;</p>
<h2>DESCRIPTION</h2>
<p> git-merge that deletes files on &quot;foreign&quot; &lt;branch&gt; before merging. </p>
<p> Useful for ignoring a folder in &lt;branch&gt; before merging it with current branch. Works by deleting FILE(S) in a detached commit based on &lt;branch&gt;, and then performing the merge of this new commit in the current branch. Note that &lt;branch&gt; is not changed by this procedure. Also note that &lt;branch&gt; may actually be any reference, like a tag, or a remote branch, or even a commit SHA. </p>
<p> For more information, see &lt;<a rel="nofollow" href="http://stackoverflow.com/questions/3111515">http://stackoverflow.com/questions/3111515</a>&gt;</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-h</code>,<code>&nbsp;<wbr>&#8211;help</code></p>
<dd> show help message and exit</p>
<dt><code>-v</code>,<code>&nbsp;<wbr>&#8211;verbose</code></p>
<dd> do not use -q to supress normal output of internal steps from git checkout, rm, commit. By default, only git merge output is shown. Errors, however, are never supressed.</p>
<dt><code>-M&nbsp;<wbr></code>&lt;message&gt;,<code>&nbsp;<wbr>&#8211;msgcommit</code>=&lt;message&gt;</p>
<dd> message for the removal commit in &lt;branch&gt;. Not to be confused with the message of the merge commit, which is set by -m. Default message is: &quot;remove files from &#8216;&lt;branch&gt;&#8217; before merge&quot;.</p>
<dt><code>-m&nbsp;<wbr></code>&lt;message&gt;,<code>&nbsp;<wbr>&#8211;message</code>=&lt;message&gt;</p>
<dd> message for the merge commit. Since we are not merging &lt;branch&gt; directly, but rather a detached commit based on it, we forge a message similar to git&#8217;s default for a branch merge. Otherwise git would use in message the full and ugly SHA1 of our commit. Default message is: &quot;Merge stripped branch &#8216;&lt;branch&gt;&#8217;&quot;.</dl>
<p> For both commit messages, the token &quot;&lt;branch&gt;&quot; is replaced for the actual &lt;branch&gt; name. </p>
<p> Additional options are passed unchecked to git merge. </p>
<p> All options must precede &lt;branch&gt; and FILE(s), except -h and &#8211;help that may appear anywhere on the command line.</p>
<h2>EXAMPLE</h2>
<pre>
git-strip-merge design &quot;photoshop/*&quot;
</pre>
<h2>SEE ALSO</h2>
<p> <code><a rel="nofollow" href="https://github.com/MestreLion/git-tools">https://github.com/MestreLion/git-tools</a></code></p>
<h2>AUTHOR</h2>
<p> Rodrigo Silva (MestreLion) linux [at] rodrigosilva.com </p>
<h2>Index</h2>
