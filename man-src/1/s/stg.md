---
title: "stg(1)"
name: "stg"
section: "1"
letter: "s"
url: "/docs/linux/man/1-stg/"
description: "stg – Manage stacks of patches using the Git content tracker"
---

<h2 class="name">NAME</h2>
<p> stg &#8211; Manage stacks of patches using the Git content tracker </p>
<h2>SYNOPSIS</h2>
<pre><code>
stg[--version | --help] stg[--help&lt;command&gt; | &lt;command&gt; --help] stg&lt;command&gt;[COMMAND OPTIONS][ARGS]
</code></pre>
<h2>DESCRIPTION</h2>
<p> StGit (Stacked Git) is an application that provides a convenient way to maintain a <i>patch stack</i> on top of a Git branch: </p>
<dl>
<dt>
<dd> &bull; The topmost (most recent) commits of a branch are given names. Such a named commit is called a <i>patch</i>.</dl>
<dl>
<dt>
<dd> &bull; After making changes to the worktree, you can incorporate the changes into an existing patch; this is called <i>refreshing</i>. You may refresh any patch, not just the topmost one.</dl>
<dl>
<dt>
<dd> &bull; You can <i>pop</i> a patch: temporarily putting it aside, so that the patch below it becomes the topmost patch. Later you may <i>push</i> it onto the stack again. Pushing and popping can be used to reorder patches.</dl>
<dl>
<dt>
<dd> &bull; You can easily <i>rebase</i> your patch stack on top of any other Git commit. (The <i>base</i> of a patch stack is the most recent Git commit that is not an StGit patch.) For example, if you started making patches on top of someone else&#8217;s branch, and that person publishes an updated branch, you can take all your patches and apply them on top of the updated branch.</dl>
<dl>
<dt>
<dd> &bull; As you would expect, changing what is below a patch can cause that patch to no longer apply cleanly &#8212; this can occur when you reorder patches, rebase patches, or refresh a non-topmost patch. StGit uses Git&#8217;s rename-aware three-way merge capability to automatically fix up what it can; if it still fails, it lets you manually resolve the conflict just like you would resolve a merge conflict in Git.</dl>
<dl>
<dt>
<dd> &bull; The patch stack is just some extra metadata attached to regular Git commits, so you can continue to use most Git tools along with StGit.</dl>
<h3>Typical uses</h3>
<p> Tracking branch</p>
<dl>
<dt>
<dd> Tracking changes from a remote branch, while maintaining local modifications against that branch, possibly with the intent of sending some patches upstream. You can modify your patch stack as much as you want, and when your patches are finally accepted upstream, the permanent recorded Git history will contain just the final sequence of patches, and not the messy sequence of edits that produced them. </p>
<p> Commands of interest in this workflow are e.g. rebase and mail.</dl>
<p> Development branch</p>
<dl>
<dt>
<dd> Even if you have no &quot;upstream&quot; to send patches to, you can use StGit as a convenient way to modify the recent history of a Git branch. For example, instead of first committing change <i>A</i>, then change <i>B</i>, and then <i>A2</i> to fix <i>A</i> because it wasn&#8217;t quite right, you could incorporate the fix directly into <i>A</i>. This way of working results in a much more readable Git history than if you had immortalized every misstep you made on your way to the right solution. </p>
<p> Commands of interest in this workflow are e.g. uncommit, which can be used to move the patch stack base downwards &#8212; i.e., turn Git commits into StGit patches after the fact &#8212; and commit, its inverse.</dl>
<p> For more information, see m[blue]<code>the tutorial</code>m[]<font SIZE="-2">[1]</font>.</p>
<h3>Specifying patches</h3>
<p> Many StGit commands take references to StGit patches as arguments. Patches in the stack are identified with short names, each of which must be unique in the stack. </p>
<p> Patches in the current branch are simply referred to by their name. Some commands allow you to specify a patch in another branch of the repository; this is done by prefixing the patch name with the branch name and a colon (e.g. otherbranch:thatpatch).</p>
<h3>Specifying commits</h3>
<p> Some StGit commands take Git commits as arguments. StGit accepts all commit expressions that Git does; and in addition, a patch name (optionally prefixed by a branch name and a colon) is allowed in this context. The usual Git modifiers ^ and ~ are also allowed; e.g., abranch:apatch~2 is the grandparent of the commit that is the patch apatch on branch abranch. </p>
<p> Instead of a patch name, you can say {base} to refer to the stack base (the commit just below the bottommost patch); so, abranch:{base} is the base of the stack in branch abranch. </p>
<p> If you need to pass a given StGit reference to a Git command, <code><a href="/docs/linux/man/1-stg-id/">stg-id</a></code>(1) will convert it to a Git commit id for you.</p>
<h2>OPTIONS</h2>
<p> The following generic option flags are available. Additional options are available for (and documented with) the different subcommands. </p>
<p> &#8211;version</p>
<dl>
<dt>
<dd> Prints the StGit version, as well as version of other components used, such as Git and Python.</dl>
<p> &#8211;help</p>
<dl>
<dt>
<dd> Prints the synopsis and a list of all subcommands. If an StGit subcommand is given, prints the synposis for that subcommand.</dl>
<h2>STGIT COMMANDS</h2>
<p> We divide StGit commands in thematic groups, according to the primary type of object they create or change. </p>
<p> Here is a short description of each command. A more detailed description is available in individual command manpages. Those manpages are named <i>stg-&lt;command&gt;(1)</i>.</p>
<h3>Repository commands</h3>
<p> clone</p>
<dl>
<dt>
<dd> Make a local clone of a remote repository</dl>
<p> id</p>
<dl>
<dt>
<dd> Print the git hash value of a StGit reference</dl>
<h3>Stack (branch) commands</h3>
<p> branch</p>
<dl>
<dt>
<dd> Branch operations: switch, list, create, rename, delete, &#8230;</dl>
<p> clean</p>
<dl>
<dt>
<dd> Delete the empty patches in the series</dl>
<p> commit</p>
<dl>
<dt>
<dd> Permanently store the applied patches into the stack base</dl>
<p> float</p>
<dl>
<dt>
<dd> Push patches to the top, even if applied</dl>
<p> goto</p>
<dl>
<dt>
<dd> Push or pop patches to the given one</dl>
<p> hide</p>
<dl>
<dt>
<dd> Hide a patch in the series</dl>
<p> init</p>
<dl>
<dt>
<dd> Initialise the current branch for use with StGIT</dl>
<p> log</p>
<dl>
<dt>
<dd> Display the patch changelog</dl>
<p> next</p>
<dl>
<dt>
<dd> Print the name of the next patch</dl>
<p> patches</p>
<dl>
<dt>
<dd> Show the applied patches modifying a file</dl>
<p> pop</p>
<dl>
<dt>
<dd> Pop one or more patches from the stack</dl>
<p> prev</p>
<dl>
<dt>
<dd> Print the name of the previous patch</dl>
<p> publish</p>
<dl>
<dt>
<dd> Push the stack changes to a merge-friendly branch</dl>
<p> pull</p>
<dl>
<dt>
<dd> Pull changes from a remote repository</dl>
<p> push</p>
<dl>
<dt>
<dd> Push one or more patches onto the stack</dl>
<p> rebase</p>
<dl>
<dt>
<dd> Move the stack base to another point in history</dl>
<p> redo</p>
<dl>
<dt>
<dd> Undo the last undo operation</dl>
<p> repair</p>
<dl>
<dt>
<dd> Fix StGit metadata if branch was modified with git commands</dl>
<p> reset</p>
<dl>
<dt>
<dd> Reset the patch stack to an earlier state</dl>
<p> series</p>
<dl>
<dt>
<dd> Print the patch series</dl>
<p> sink</p>
<dl>
<dt>
<dd> Send patches deeper down the stack</dl>
<p> squash</p>
<dl>
<dt>
<dd> Squash two or more patches into one</dl>
<p> top</p>
<dl>
<dt>
<dd> Print the name of the top patch</dl>
<p> uncommit</p>
<dl>
<dt>
<dd> Turn regular git commits into StGit patches</dl>
<p> undo</p>
<dl>
<dt>
<dd> Undo the last operation</dl>
<p> unhide</p>
<dl>
<dt>
<dd> Unhide a hidden patch</dl>
<h3>Patch commands</h3>
<p> delete</p>
<dl>
<dt>
<dd> Delete patches</dl>
<p> edit</p>
<dl>
<dt>
<dd> Edit a patch description or diff</dl>
<p> export</p>
<dl>
<dt>
<dd> Export patches to a directory</dl>
<p> files</p>
<dl>
<dt>
<dd> Show the files modified by a patch (or the current patch)</dl>
<p> fold</p>
<dl>
<dt>
<dd> Integrate a GNU diff patch into the current patch</dl>
<p> import</p>
<dl>
<dt>
<dd> Import a GNU diff file as a new patch</dl>
<p> mail</p>
<dl>
<dt>
<dd> Send a patch or series of patches by e-mail</dl>
<p> new</p>
<dl>
<dt>
<dd> Create a new, empty patch</dl>
<p> pick</p>
<dl>
<dt>
<dd> Import a patch from a different branch or a commit object</dl>
<p> refresh</p>
<dl>
<dt>
<dd> Generate a new commit for the current patch</dl>
<p> rename</p>
<dl>
<dt>
<dd> Rename a patch</dl>
<p> show</p>
<dl>
<dt>
<dd> Show the commit corresponding to a patch</dl>
<p> sync</p>
<dl>
<dt>
<dd> Synchronise patches with a branch or a series</dl>
<h3>Index/worktree commands</h3>
<p> diff</p>
<dl>
<dt>
<dd> Show the tree diff</dl>
<h2>CONFIGURATION MECHANISM</h2>
<p> StGit uses the same configuration mechanism as Git. See <code><a href="/docs/linux/man/7-git/">git</a></code>(7) for more details.</p>
<h2>TEMPLATES</h2>
<p> A number of StGit commands make use of template files to provide useful default texts to be edited by the user. These &lt;name&gt;.tmpl template files are searched in the following directories: </p>
<dl>
<dt>
<dd> 1. $GITDIR/ (in practice, the .git/ directory in your repository)</dl>
<dl>
<dt>
<dd> 2. $HOME/.stgit/templates/</dl>
<dl>
<dt>
<dd> 3. /usr/share/stgit/templates/</dl>
<h2>NOTES</h2>
<dl>
<dt> 1.</p>
<dd> the tutorial</p>
<dl>
<dt>
<dd> [set $man.base.url.for.relative.links]/tutorial.html</dl>
</dl>
<h2>Index</h2>
