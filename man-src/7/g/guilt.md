---
title: "guilt(7)"
name: "guilt"
section: "7"
letter: "g"
url: "/docs/linux/man/7-guilt/"
description: "guilt – quilt on top of git"
---

<p>guilt &#8211; quilt on top of git</p>
<h2>Synopsis</h2>
<p><i>guilt</i> COMMAND [ARGS]</p>
<h2>Description</h2>
<p>Andrew Morton originally developed a set of scripts for maintaining kernel patches outside of any SCM tool. Others extended these into a suite called quilt. The basic idea behind quilt is to maintain patches instead of maintaining source files. Patches can be added, removed or reordered, and they can be refreshed as you fix bugs or update to a new base revision. quilt is very powerful, but it is not integrated with the underlying SCM tools. This makes it difficult to visualize your changes. </p>
<p> Guilt allows one to use quilt functionality on top of a Git repository. Changes are maintained as patches which are committed into Git. Commits can be removed or reordered, and the underlying patch can be refreshed based on changes made in the working directory. The patch directory can also be placed under revision control, so you can have a separate history of changes made to your patches.</p>
<h2>Patches Directory</h2>
<p>In Guilt, all the patches are stored in .git/patches/$branch/, where $branch is the name of the branch being worked on. This means that one can have a independent series of patches for each branch present in the repository. Each of these per-branch directories contains 3 special files: </p>
<p> guards: This file contains any guards that should be applied to the series when pushing. It is only present when guards are selected. </p>
<p> series: This file contains a list of all the patch filenames relative to the per-branch patch directory. Empty and commented out lines are ignored. </p>
<p> status: This file contains the state of the stack. What patches are applied.</p>
<h2>Hooks</h2>
<p>Any guilt operation may execute zero or more hook scripts which can be used to run any housekeeping commands or even abort the execution of the command.</p>
<h2>Hooks Directory</h2>
<p>Guilt follows the same basic design of hooks in Git itself. All Guilt hooks are executable files (generally shell scripts, but they can be anything the operating system can execute) in .git/hooks/guilt/. </p>
<p> The following hooks are supported: </p>
<p> delete &lt;patch name&gt;</p>
<dl>
<dd>Executed when a patch is deleted from the patch series via linkguilt:guilt-delete[1].</dl>
<h2>Guilt Commands</h2>
<p>All commands can be called with or without a dash. e.g. <i>guilt add</i> or <i>guilt-add</i> </p>
<p> linkguilt:guilt-add[1]</p>
<dl>
<dd>guilt-add &#8211; Add a file to git and guilt.</dl>
<p> linkguilt:guilt-applied[1]</p>
<dl>
<dd>guilt-applied &#8211; List applied patches.</dl>
<p> linkguilt:guilt-branch[1]</p>
<dl>
<dd>guilt-branch &#8211; Branch the entire patch series.</dl>
<p> linkguilt:guilt-commit[1]</p>
<dl>
<dd>guilt-commit &#8211; Commit specified number of patches.</dl>
<p> linkguilt:guilt-delete[1]</p>
<dl>
<dd>guilt-delete &#8211; Delete a patch.</dl>
<p> linkguilt:guilt-diff[1]</p>
<dl>
<dd>guilt-diff &#8211; Outputs various diffs.</dl>
<p> linkguilt:guilt-export[1]</p>
<dl>
<dd>guilt-export &#8211; Export a patch series (to be used by quilt).</dl>
<p> linkguilt:guilt-files[1]</p>
<dl>
<dd>guilt-files &#8211; Print the list of files that the topmost patch changes.</dl>
<p> linkguilt:guilt-fold[1]</p>
<dl>
<dd>guilt-fold &#8211; Fold a specified patch into the topmost applied patch.</dl>
<p> linkguilt:guilt-fork[1]</p>
<dl>
<dd>guilt-fork &#8211; Fork the topmost applied patch.</dl>
<p> linkguilt:guilt-graph[1]</p>
<dl>
<dd>guilt-graph &#8211; Create a patch dependency graph.</dl>
<p> linkguilt:guilt-guard[1]</p>
<dl>
<dd>guilt-guard &#8211; Assign guards to patches.</dl>
<p> linkguilt:guilt-header[1]</p>
<dl>
<dd>guilt-header &#8211; Print a patch header.</dl>
<p> linkguilt:guilt-help[1]</p>
<dl>
<dd>guilt-help &#8211; open man page of a guilt command.</dl>
<p> linkguilt:guilt-import-commit[1]</p>
<dl>
<dd>guilt-import-commit &#8211; Import one or more commits as patches.</dl>
<p> linkguilt:guilt-import[1]</p>
<dl>
<dd>guilt-import &#8211; Import specified patch file.</dl>
<p> linkguilt:guilt-init[1]</p>
<dl>
<dd>guilt-init &#8211; Initialize guilt for use in a git repository.</dl>
<p> linkguilt:guilt-new[1]</p>
<dl>
<dd>guilt-new &#8211; Create a new patch.</dl>
<p> linkguilt:guilt-next[1]</p>
<dl>
<dd>guilt-next &#8211; Output the name of next patch to be pushed.</dl>
<p> linkguilt:guilt-patchbomb[1]</p>
<dl>
<dd>guilt-patchbomb &#8211; Email a series of commits interactively.</dl>
<p> linkguilt:guilt-pop[1]</p>
<dl>
<dd>guilt-pop &#8211; Pop patches from the tree.</dl>
<p> linkguilt:guilt-prev[1]</p>
<dl>
<dd>guilt-prev &#8211; Output name of second topmost applied patch.</dl>
<p> linkguilt:guilt-push[1]</p>
<dl>
<dd>guilt-push &#8211; Push patches onto the tree.</dl>
<p> linkguilt:guilt-rebase[1]</p>
<dl>
<dd>guilt-rebase &#8211; Rebase pushed patches.</dl>
<p> linkguilt:guilt-refresh[1]</p>
<dl>
<dd>guilt-refresh &#8211; Refresh topmost applied patch.</dl>
<p> linkguilt:guilt-repair[1]</p>
<dl>
<dd>guilt-repair &#8211; Repair the repository state.</dl>
<p> linkguilt:guilt-rm[1]</p>
<dl>
<dd>guilt-rm &#8211; Remove a file from the git tree and guilt.</dl>
<p> linkguilt:guilt-select[1]</p>
<dl>
<dd>guilt-select &#8211; Select guards to apply when pushing patches.</dl>
<p> linkguilt:guilt-series[1]</p>
<dl>
<dd>guilt-series &#8211; Print the stack of patches.</dl>
<p> linkguilt:guilt-status[1]</p>
<dl>
<dd>guilt-status &#8211; Print the status of files since the last refresh.</dl>
<p> linkguilt:guilt-top[1]</p>
<dl>
<dd>guilt-top &#8211; Output name of topmost applied patch.</dl>
<p> linkguilt:guilt-unapplied[1]</p>
<dl>
<dd>guilt-unapplied &#8211; List all unapplied patches.</dl>
<h2>Author</h2>
<p>Written by Josef &quot;Jeff&quot; Sipek &lt;m[blue]<code>jeffpc [at] josefsipek.net</code>m[]<font SIZE="-2">[1]</font>&gt;</p>
<h2>Documentation</h2>
<p>Documentation by Brandon Philips &lt;m[blue]<code>brandon [at] ifup.org</code>m[]<font SIZE="-2">[2]</font>&gt; and Josef &quot;Jeff&quot; Sipek &lt;m[blue]<code>jeffpc [at] josefsipek.net</code>m[]<font SIZE="-2">[1]</font>&gt;</p>
<h2>Guilt</h2>
<p>Part of the linkguilt:guilt[7] suite (Generated for Guilt v0.33)</p>
<h2>Notes</h2>
<dl>
<dt> 1.</p>
<dd>jeffpc [at] josefsipek.net</p>
<dl>
<dd>mailto:jeffpc [at] josefsipek.net</dl>
<dt> 2.</p>
<dd>brandon [at] ifup.org</p>
<dl>
<dd>mailto:brandon [at] ifup.org</dl>
