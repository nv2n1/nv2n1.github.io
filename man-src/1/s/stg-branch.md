---
title: "stg-branch(1)"
name: "stg-branch"
section: "1"
letter: "s"
url: "/docs/linux/man/1-stg-branch/"
description: "stg-branch – Branch operations: switch, list, create, rename, delete, …"
---

<h2 class="name">NAME</h2>
<p> stg-branch &#8211; Branch operations: switch, list, create, rename, delete, &#8230; </p>
<h2>SYNOPSIS</h2>
<pre><code>
stg branch
    stg branch[--merge][--]&lt;branch&gt;
        stg branch-- list
            stg branch-- create[--]&lt;new - branch&gt;[&lt;committish&gt;] stg branch-- clone[--][&lt;new - branch&gt;] stg branch-- rename[--]&lt;old - name&gt;&lt;new - name&gt;
                stg branch-- protect[--][&lt;branch&gt;] stg branch-- unprotect[--][&lt;branch&gt;] stg branch-- delete[--force][--]&lt;branch&gt;
                    stg branch-- cleanup[--force][--][&lt;branch&gt;] stg branch-- description = &lt;description&gt;[--][&lt;branch&gt;]
</code></pre>
<h2>DESCRIPTION</h2>
<p> Create, clone, switch between, rename, or delete development branches within a git repository. </p>
<p> <i>stg branch</i></p>
<dl>
<dt>
<dd> Display the name of the current branch.</dl>
<p> <i>stg branch</i> &lt;branch&gt;</p>
<dl>
<dt>
<dd> Switch to the given branch.</dl>
<h2>OPTIONS</h2>
<p> -l, &#8211;list</p>
<dl>
<dt>
<dd> List each branch in the current repository, followed by its branch description (if any). The current branch is prefixed with <i>&gt;</i>. Branches that have been initialized for StGit (with <code><a href="/docs/linux/man/1-stg-init/">stg-init</a></code>(1)) are prefixed with <i>s</i>. Protected branches are prefixed with <i>p</i>.</dl>
<p> -c, &#8211;create</p>
<dl>
<dt>
<dd> Create (and switch to) a new branch. The new branch is already initialized as an StGit patch stack, so you do not have to run <code><a href="/docs/linux/man/1-stg-init/">stg-init</a></code>(1) manually. If you give a committish argument, the new branch is based there; otherwise, it is based at the current HEAD. </p>
<p> StGit will try to detect the branch off of which the new branch is forked, as well as the remote repository from which that parent branch is taken (if any), so that running <code><a href="/docs/linux/man/1-stg-pull/">stg-pull</a></code>(1) will automatically pull new commits from the correct branch. It will warn if it cannot guess the parent branch (e.g. if you do not specify a branch name as committish).</dl>
<p> &#8211;clone</p>
<dl>
<dt>
<dd> Clone the current branch, under the name &lt;new-branch&gt; if specified, or using the current branch&#8217;s name plus a timestamp. </p>
<p> The description of the new branch is set to tell it is a clone of the current branch. The parent information of the new branch is copied from the current branch.</dl>
<p> -r, &#8211;rename</p>
<dl>
<dt>
<dd> Rename an existing branch.</dl>
<p> -p, &#8211;protect</p>
<dl>
<dt>
<dd> Prevent StGit from modifying a branch &#8212; either the current one, or one named on the command line.</dl>
<p> -u, &#8211;unprotect</p>
<dl>
<dt>
<dd> Allow StGit to modify a branch &#8212; either the current one, or one named on the command line. This undoes the effect of an earlier <i>stg branch &#8211;protect</i> command.</dl>
<p> &#8211;delete</p>
<dl>
<dt>
<dd> Delete the named branch. If there are any patches left in the branch, StGit will refuse to delete it unless you give the <i>&#8211;force</i> flag. </p>
<p> A protected branch cannot be deleted; it must be unprotected first (see <i>&#8211;unprotect</i> above). </p>
<p> If you delete the current branch, you are switched to the &quot;master&quot; branch, if it exists.</dl>
<p> &#8211;cleanup</p>
<dl>
<dt>
<dd> Remove the StGit information for the current or given branch. If there are patches left in the branch, StGit refuses the operation unless <i>&#8211;force</i> is given. </p>
<p> A protected branch cannot be cleaned up; it must be unprotected first (see <i>&#8211;unprotect</i> above). </p>
<p> A cleaned up branch can be re-initialised using the <i>stg init</i> command.</dl>
<p> -d DESCRIPTION, &#8211;description DESCRIPTION</p>
<dl>
<dt>
<dd> Set the branch description.</dl>
<p> &#8211;merge</p>
<dl>
<dt>
<dd> Merge work tree changes into the other branch.</dl>
<p> &#8211;force</p>
<dl>
<dt>
<dd> Force a delete when the series is not empty.</dl>
<h2>STGIT</h2>
<p> Part of the StGit suite &#8211; see <code><a href="/docs/linux/man/1-stg/">stg</a></code>(1) </p>
<h2>Index</h2>
