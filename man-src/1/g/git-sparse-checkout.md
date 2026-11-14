---
title: "git-sparse-checkout(1)"
name: "git-sparse-checkout"
section: "1"
letter: "g"
url: "/docs/linux/man/1-git-sparse-checkout/"
description: "git-sparse-checkout – Initialize and modify the sparse-checkout configuration, which reduces the checkout to a set of paths given by a list of patterns."
---

<h2 class="name">NAME</h2>
<p> git-sparse-checkout &#8211; Initialize and modify the sparse-checkout configuration, which reduces the checkout to a set of paths given by a list of patterns. </p>
<h2>SYNOPSIS</h2>
<pre>
<i>git sparse-checkout &lt;subcommand&gt; [options]</i>
</pre>
<h2>DESCRIPTION</h2>
<p> Initialize and modify the sparse-checkout configuration, which reduces the checkout to a set of paths given by a list of patterns. </p>
<p> THIS COMMAND IS EXPERIMENTAL. ITS BEHAVIOR, AND THE BEHAVIOR OF OTHER COMMANDS IN THE PRESENCE OF SPARSE-CHECKOUTS, WILL LIKELY CHANGE IN THE FUTURE.</p>
<h2>COMMANDS</h2>
<p> <i>list</i></p>
<dl>
<dt>
<dd> Describe the patterns in the sparse-checkout file.</dl>
<p> <i>init</i></p>
<dl>
<dt>
<dd> Enable the <code>core.sparseCheckout</code> setting. If the sparse-checkout file does not exist, then populate it with patterns that match every file in the root directory and no other directories, then will remove all directories tracked by Git. Add patterns to the sparse-checkout file to repopulate the working directory. </p>
<p> To avoid interfering with other worktrees, it first enables the <code>extensions.worktreeConfig</code> setting and makes sure to set the <code>core.sparseCheckout</code> setting in the worktree-specific config file. </p>
<p> When <code>&#8211;cone</code> is provided, the <code>core.sparseCheckoutCone</code> setting is also set, allowing for better performance with a limited set of patterns (see <i>CONE PATTERN SET</i> below). </p>
<p> Use the <code>&#8211;[no-]sparse-index</code> option to toggle the use of the sparse index format. This reduces the size of the index to be more closely aligned with your sparse-checkout definition. This can have significant performance advantages for commands such as <code>git status</code> or <code>git add</code>. This feature is still experimental. Some commands might be slower with a sparse index until they are properly integrated with the feature. </p>
<p> <code>WARNING:</code> Using a sparse index requires modifying the index in a way that is not completely understood by external tools. If you have trouble with this compatibility, then run <code>git sparse-checkout init &#8211;no-sparse-index</code> to rewrite your index to not be sparse. Older versions of Git will not understand the sparse directory entries index extension and may fail to interact with your repository until it is disabled.</dl>
<p> <i>set</i></p>
<dl>
<dt>
<dd> Write a set of patterns to the sparse-checkout file, as given as a list of arguments following the <i>set</i> subcommand. Update the working directory to match the new patterns. Enable the core.sparseCheckout config setting if it is not already enabled. </p>
<p> When the <code>&#8211;stdin</code> option is provided, the patterns are read from standard in as a newline-delimited list instead of from the arguments. </p>
<p> When <code>core.sparseCheckoutCone</code> is enabled, the input list is considered a list of directories instead of sparse-checkout patterns. The command writes patterns to the sparse-checkout file to include all files contained in those directories (recursively) as well as files that are siblings of ancestor directories. The input format matches the output of <code>git ls-tree &#8211;name-only</code>. This includes interpreting pathnames that begin with a double quote (&quot;) as C-style quoted strings.</dl>
<p> <i>add</i></p>
<dl>
<dt>
<dd> Update the sparse-checkout file to include additional patterns. By default, these patterns are read from the command-line arguments, but they can be read from stdin using the <code>&#8211;stdin</code> option. When <code>core.sparseCheckoutCone</code> is enabled, the given patterns are interpreted as directory names as in the <i>set</i> subcommand.</dl>
<p> <i>reapply</i></p>
<dl>
<dt>
<dd> Reapply the sparsity pattern rules to paths in the working tree. Commands like merge or rebase can materialize paths to do their work (e.g. in order to show you a conflict), and other sparse-checkout commands might fail to sparsify an individual file (e.g. because it has unstaged changes or conflicts). In such cases, it can make sense to run <code>git sparse-checkout reapply</code> later after cleaning up affected paths (e.g. resolving conflicts, undoing or committing changes, etc.).</dl>
<p> <i>disable</i></p>
<dl>
<dt>
<dd> Disable the <code>core.sparseCheckout</code> config setting, and restore the working directory to include all files. Leaves the sparse-checkout file intact so a later <i>git sparse-checkout init</i> command may return the working directory to the same state.</dl>
<h2>SPARSE CHECKOUT</h2>
<p> &quot;Sparse checkout&quot; allows populating the working directory sparsely. It uses the skip-worktree bit (see <code><a href="/docs/linux/man/1-git-update-index/">git-update-index</a></code>(1)) to tell Git whether a file in the working directory is worth looking at. If the skip-worktree bit is set, then the file is ignored in the working directory. Git will not populate the contents of those files, which makes a sparse checkout helpful when working in a repository with many files, but only a few are important to the current user. </p>
<p> The <code>$GIT_DIR/info/sparse-checkout</code> file is used to define the skip-worktree reference bitmap. When Git updates the working directory, it updates the skip-worktree bits in the index based on this file. The files matching the patterns in the file will appear in the working directory, and the rest will not. </p>
<p> To enable the sparse-checkout feature, run <code>git sparse-checkout init</code> to initialize a simple sparse-checkout file and enable the <code>core.sparseCheckout</code> config setting. Then, run <code>git sparse-checkout set</code> to modify the patterns in the sparse-checkout file. </p>
<p> To repopulate the working directory with all files, use the <code>git sparse-checkout disable</code> command.</p>
<h2>FULL PATTERN SET</h2>
<p> By default, the sparse-checkout file uses the same syntax as <code>.gitignore</code> files. </p>
<p> While <code>$GIT_DIR/info/sparse-checkout</code> is usually used to specify what files are included, you can also specify what files are <i>not</i> included, using negative patterns. For example, to remove the file <code>unwanted</code>: </p>
<dl>
<dt>
<dd>
<pre>
/*
!unwanted
</pre>
</dl>
<h2>CONE PATTERN SET</h2>
<p> The full pattern set allows for arbitrary pattern matches and complicated inclusion/exclusion rules. These can result in O(N*M) pattern matches when updating the index, where N is the number of patterns and M is the number of paths in the index. To combat this performance issue, a more restricted pattern set is allowed when <code>core.sparseCheckoutCone</code> is enabled. </p>
<p> The accepted patterns in the cone pattern set are: </p>
<dl>
<dt>
<dd> 1. <code>Recursive:</code> All paths inside a directory are included.</dl>
<dl>
<dt>
<dd> 2. <code>Parent:</code> All files immediately inside a directory are included.</dl>
<p> In addition to the above two patterns, we also expect that all files in the root directory are included. If a recursive pattern is added, then all leading directories are added as parent patterns. </p>
<p> By default, when running <code>git sparse-checkout init</code>, the root directory is added as a parent pattern. At this point, the sparse-checkout file contains the following patterns: </p>
<dl>
<dt>
<dd>
<pre>
/*
!/*/
</pre>
</dl>
<p> This says &quot;include everything in root, but nothing two levels below root.&quot; </p>
<p> When in cone mode, the <code>git sparse-checkout set</code> subcommand takes a list of directories instead of a list of sparse-checkout patterns. In this mode, the command <code>git sparse-checkout set A/B/C</code> sets the directory <code>A/B/C</code> as a recursive pattern, the directories <code>A</code> and <code>A/B</code> are added as parent patterns. The resulting sparse-checkout file is now </p>
<dl>
<dt>
<dd>
<pre>
/*
!/*/
/A/
!/A/*/
/A/B/
!/A/B/*/
/A/B/C/
</pre>
</dl>
<p> Here, order matters, so the negative patterns are overridden by the positive patterns that appear lower in the file. </p>
<p> If <code>core.sparseCheckoutCone=true</code>, then Git will parse the sparse-checkout file expecting patterns of these types. Git will warn if the patterns do not match. If the patterns do match the expected format, then Git will use faster hash- based algorithms to compute inclusion in the sparse-checkout. </p>
<p> In the cone mode case, the <code>git sparse-checkout list</code> subcommand will list the directories that define the recursive patterns. For the example sparse-checkout file above, the output is as follows: </p>
<dl>
<dt>
<dd>
<pre>
$ git sparse-checkout list
A/B/C
</pre>
</dl>
<p> If <code>core.ignoreCase=true</code>, then the pattern-matching algorithm will use a case-insensitive check. This corrects for case mismatched filenames in the <i>git sparse-checkout set</i> command to reflect the expected cone in the working directory. </p>
<p> When changing the sparse-checkout patterns in cone mode, Git will inspect each tracked directory that is not within the sparse-checkout cone to see if it contains any untracked files. If all of those files are ignored due to the <code>.gitignore</code> patterns, then the directory will be deleted. If any of the untracked files within that directory is not ignored, then no deletions will occur within that directory and a warning message will appear. If these files are important, then reset your sparse-checkout definition so they are included, use <code>git add</code> and <code>git commit</code> to store them, then remove any remaining files manually to ensure Git can behave optimally.</p>
<h2>SUBMODULES</h2>
<p> If your repository contains one or more submodules, then submodules are populated based on interactions with the <code>git submodule</code> command. Specifically, <code>git submodule init &#8212; &lt;path&gt;</code> will ensure the submodule at <code>&lt;path&gt;</code> is present, while <code>git submodule deinit [-f] &#8212; &lt;path&gt;</code> will remove the files for the submodule at <code>&lt;path&gt;</code> (including any untracked files, uncommitted changes, and unpushed history). Similar to how sparse-checkout removes files from the working tree but still leaves entries in the index, deinitialized submodules are removed from the working directory but still have an entry in the index. </p>
<p> Since submodules may have unpushed changes or untracked files, removing them could result in data loss. Thus, changing sparse inclusion/exclusion rules will not cause an already checked out submodule to be removed from the working copy. Said another way, just as <code>checkout</code> will not cause submodules to be automatically removed or initialized even when switching between branches that remove or add submodules, using <code>sparse-checkout</code> to reduce or expand the scope of &quot;interesting&quot; files will not cause submodules to be automatically deinitialized or initialized either. </p>
<p> Further, the above facts mean that there are multiple reasons that &quot;tracked&quot; files might not be present in the working copy: sparsity pattern application from sparse-checkout, and submodule initialization state. Thus, commands like <code>git grep</code> that work on tracked files in the working copy may return results that are limited by either or both of these restrictions.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-git-read-tree/">git-read-tree</a></code>(1) <code><a href="/docs/linux/man/5-gitignore/">gitignore</a></code>(5)</p>
<h2>GIT</h2>
<p> Part of the <code><a href="/docs/linux/man/1-git/">git</a></code>(1) suite </p>
<h2>Index</h2>
