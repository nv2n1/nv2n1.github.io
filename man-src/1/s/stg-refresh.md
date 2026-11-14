---
title: "stg-refresh(1)"
name: "stg-refresh"
section: "1"
letter: "s"
url: "/docs/linux/man/1-stg-refresh/"
description: "stg-refresh – Generate a new commit for the current patch"
---

<h2 class="name">NAME</h2>
<p> stg-refresh &#8211; Generate a new commit for the current patch </p>
<h2>SYNOPSIS</h2>
<pre><code>
stg refresh[options][--][ &lt; files or dirs &gt; ]
</code></pre>
<h2>DESCRIPTION</h2>
<p> Include the latest work tree and index changes in the current patch. This command generates a new git commit object for the patch; the old commit is no longer visible. </p>
<p> Refresh will warn if the index is dirty, and require use of either the <i>&#8211;index</i> or <i>&#8211;force</i> options to override this check. This is to prevent accidental full refresh when only some changes were staged using git add interative mode. </p>
<p> You may optionally list one or more files or directories relative to the current working directory; if you do, only matching files will be updated. </p>
<p> Behind the scenes, stg refresh first creates a new temporary patch with your updates, and then merges that patch into the patch you asked to have refreshed. If you asked to refresh a patch other than the topmost patch, there can be conflicts; in that case, the temporary patch will be left for you to take care of, for example with stg squash. </p>
<p> The creation of the temporary patch is recorded in a separate entry in the patch stack log; this means that one undo step will undo the merge between the other patch and the temp patch, and two undo steps will additionally get rid of the temp patch.</p>
<h2>OPTIONS</h2>
<p> -u, &#8211;update</p>
<dl>
<dt>
<dd> Only update the current patch files.</dl>
<p> -i, &#8211;index</p>
<dl>
<dt>
<dd> Instead of setting the patch top to the current contents of the worktree, set it to the current contents of the index.</dl>
<p> -F, &#8211;force</p>
<dl>
<dt>
<dd> Instead of warning the user when some work has already been staged (such as with git add interactive mode) force a full refresh.</dl>
<p> -p PATCH, &#8211;patch PATCH</p>
<dl>
<dt>
<dd> Refresh (applied) PATCH instead of the top patch.</dl>
<p> -e, &#8211;edit</p>
<dl>
<dt>
<dd> Invoke an editor for the patch description.</dl>
<p> -a NOTE, &#8211;annotate NOTE</p>
<dl>
<dt>
<dd> Annotate the patch log entry.</dl>
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
<h2>STGIT</h2>
<p> Part of the StGit suite &#8211; see <code><a href="/docs/linux/man/1-stg/">stg</a></code>(1) </p>
<h2>Index</h2>
