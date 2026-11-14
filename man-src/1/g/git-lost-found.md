---
title: "git-lost-found(1)"
name: "git-lost-found"
section: "1"
letter: "g"
url: "/docs/linux/man/1-git-lost-found/"
description: "git-lost-found – Recover lost refs that luckily have not yet been pruned"
---

<h2 class="name">NAME</h2>
<p> git-lost-found &#8211; Recover lost refs that luckily have not yet been pruned </p>
<h2>SYNOPSIS</h2>
<pre>
<i>git lost-found</i>
</pre>
<h2>DESCRIPTION</h2>
<p> <code>NOTE</code>: this command is deprecated. Use <code><a href="/docs/linux/man/1-git-fsck/">git-fsck</a></code>(1) with the option <i>&#8211;lost-found</i> instead. </p>
<p> Finds dangling commits and tags from the object database, and creates refs to them in the .git/lost-found/ directory. Commits and tags that dereference to commits are stored in .git/lost-found/commit, and other objects are stored in .git/lost-found/other.</p>
<h2>OUTPUT</h2>
<p> Prints to standard output the object names and one-line descriptions of any commits or tags found.</p>
<h2>EXAMPLE</h2>
<p> Suppose you run <i>git tag -f</i> and mistype the tag to overwrite. The ref to your tag is overwritten, but until you run <i>git prune</i>, the tag itself is still there. </p>
<dl>
<dt>
<dd>
<pre>
$ git lost-found
[1ef2b196d909eed523d4f3c9bf54b78cdd6843c6] GIT 0.99.9c
...
</pre>
</dl>
<p> Also you can use gitk to browse how any tags found relate to each other. </p>
<dl>
<dt>
<dd>
<pre>
$ gitk $(cd .git/lost-found/commit &amp;&amp; echo ??*)
</pre>
</dl>
<p> After making sure you know which the object is the tag you are looking for, you can reconnect it to your regular refs hierarchy by using the update-ref command. </p>
<dl>
<dt>
<dd>
<pre>
$ git cat-file -t 1ef2b196
tag
$ git cat-file tag 1ef2b196
object fa41bbce8e38c67a218415de6cfa510c7e50032a
type commit
tag v0.99.9c
tagger Junio C Hamano &lt;junkio [at] cox.net&gt; 1131059594 -0800
GIT 0.99.9c
This contains the following changes from the &quot;master&quot; branch, since
...
$ git update-ref refs/tags/not-lost-anymore 1ef2b196
$ git rev-parse not-lost-anymore
1ef2b196d909eed523d4f3c9bf54b78cdd6843c6
</pre>
</dl>
<h2>GIT</h2>
<p> Part of the <code><a href="/docs/linux/man/1-git/">git</a></code>(1) suite </p>
<h2>Index</h2>
