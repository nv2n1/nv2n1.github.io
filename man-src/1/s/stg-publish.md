---
title: "stg-publish(1)"
name: "stg-publish"
section: "1"
letter: "s"
url: "/docs/linux/man/1-stg-publish/"
description: "stg-publish – Push the stack changes to a merge-friendly branch"
---

<h2 class="name">NAME</h2>
<p> stg-publish &#8211; Push the stack changes to a merge-friendly branch </p>
<h2>SYNOPSIS</h2>
<pre><code>
stg publish[options][--][branch]
</code></pre>
<h2>DESCRIPTION</h2>
<p> This command commits a set of changes on a separate (called public) branch based on the modifications of the given or current stack. The history of the public branch is not re-written, making it merge-friendly and feasible for publishing. The heads of the stack and public branch may be different but the corresponding tree objects are always the same. </p>
<p> If the trees of the stack and public branch are different (otherwise the command has no effect), StGit first checks for a rebase of the stack since the last publishing. If a rebase is detected, StGit creates a commit on the public branch corresponding to a merge between the new stack base and the latest public head. </p>
<p> If no rebasing was detected, StGit checks for new patches that may have been created on top of the stack since the last publishing. If new patches are found and are not empty, they are checked into the public branch keeping the same commit information (e.g. log message, author, committer, date). </p>
<p> If the above tests fail (e.g. patches modified or removed), StGit creates a new commit on the public branch having the same tree as the stack but the public head as its parent. The editor will be invoked if no &quot;&#8211;message&quot; option is given. </p>
<p> It is recommended that stack modifications falling in different categories as described above are separated by a publish command in order to keep the public branch history cleaner (otherwise StGit would generate a big commit including several stack modifications). </p>
<p> The <i>&#8211;unpublished</i> option can be used to check if there are applied patches that have not been published to the public branch. This is done by trying to revert the patches in the public tree (similar to the <i>push &#8211;merged</i> detection). The <i>&#8211;last</i> option tries to find the last published patch by checking the SHA1 of the patch tree agains the public tree. This may fail if the stack was rebased since the last publish command. </p>
<p> The public branch name can be set via the branch.&lt;branch&gt;.public configuration variable (defaulting to &quot;&lt;branch&gt;.public&quot;).</p>
<h2>OPTIONS</h2>
<p> -b BRANCH, &#8211;branch BRANCH</p>
<dl>
<dt>
<dd> Use BRANCH instead of the default branch.</dl>
<p> -l, &#8211;last</p>
<dl>
<dt>
<dd> Show the last published patch.</dl>
<p> -u, &#8211;unpublished</p>
<dl>
<dt>
<dd> Show applied patches that have not been published.</dl>
<p> &#8211;author &quot;NAME &lt;EMAIL&gt;&quot;</p>
<dl>
<dt>
<dd> Set the author details.</dl>
<p> &#8211;authname NAME</p>
<dl>
<dt>
<dd> Set the author name.</dl>
<p> &#8211;authemail EMAIL</p>
<dl>
<dt>
<dd> Set the author email.</dl>
<p> &#8211;authdate DATE</p>
<dl>
<dt>
<dd> Set the author date.</dl>
<p> -m MESSAGE, &#8211;message MESSAGE</p>
<dl>
<dt>
<dd> Use MESSAGE instead of invoking the editor.</dl>
<p> -f FILE, &#8211;file FILE</p>
<dl>
<dt>
<dd> Use the contents of FILE instead of invoking the editor. (If FILE is &quot;-&quot;, write to stdout.)</dl>
<p> &#8211;sign</p>
<dl>
<dt>
<dd> Add a &quot;Signed-off-by:&quot; to the end of the patch.</dl>
<p> &#8211;ack</p>
<dl>
<dt>
<dd> Add an &quot;Acked-by:&quot; line to the end of the patch.</dl>
<h2>STGIT</h2>
<p> Part of the StGit suite &#8211; see <code><a href="/docs/linux/man/1-stg/">stg</a></code>(1) </p>
<h2>Index</h2>
