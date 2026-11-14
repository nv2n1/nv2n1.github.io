---
title: "git(1)"
name: "git"
section: "1"
letter: "g"
url: "/docs/linux/man/1-git/"
description: "git – the stupid content tracker"
---

<h2 class="name">NAME</h2>
<p> git &#8211; the stupid content tracker </p>
<h2>SYNOPSIS</h2>
<pre><code>
git[--version][--help][-C&lt;path&gt;][-c &lt; name &gt;= &lt;value&gt;]
   [--exec - path[=&lt;path&gt;]][--html - path][--man - path][--info - path]
   [-p | --paginate | -P | --no - pager][--no - replace - objects][--bare]
   [--git - dir = &lt;path&gt;][--work - tree = &lt;path&gt;][--namespace = &lt;name&gt;]
   [--super - prefix = &lt;path&gt;][--config - env = &lt; name &gt;= &lt;envvar&gt;]&lt;command&gt;[&lt;args&gt;]
</code></pre>
<h2>DESCRIPTION</h2>
<p> Git is a fast, scalable, distributed revision control system with an unusually rich command set that provides both high-level operations and full access to internals. </p>
<p> See <code><a href="/docs/linux/man/7-gittutorial/">gittutorial</a></code>(7) to get started, then see <code><a href="/docs/linux/man/7-giteveryday/">giteveryday</a></code>(7) for a useful minimum set of commands. The m[blue]<code>Git User&#8217;s Manual</code>m[]<font SIZE="-2">[1]</font> has a more in-depth introduction. </p>
<p> After you mastered the basic concepts, you can come back to this page to learn what commands Git offers. You can learn more about individual Git commands with &quot;git help command&quot;. <code><a href="/docs/linux/man/7-gitcli/">gitcli</a></code>(7) manual page gives you an overview of the command-line command syntax. </p>
<p> A formatted and hyperlinked copy of the latest Git documentation can be viewed at m[blue]<code><a rel="nofollow" href="https://git.github.io/htmldocs/git.html">https://git.github.io/htmldocs/git.html</a></code>m[] or m[blue]<code><a rel="nofollow" href="https://git-scm.com/docs">https://git-scm.com/docs</a></code>m[].</p>
<h2>OPTIONS</h2>
<p> &#8211;version</p>
<dl>
<dt>
<dd> Prints the Git suite version that the <i>git</i> program came from. </p>
<p> This option is internally converted to <code>git version &#8230;</code> and accepts the same options as the <code><a href="/docs/linux/man/1-git-version/">git-version</a></code>(1) command. If <code>&#8211;help</code> is also given, it takes precedence over <code>&#8211;version</code>.</dl>
<p> &#8211;help</p>
<dl>
<dt>
<dd> Prints the synopsis and a list of the most commonly used commands. If the option <code>&#8211;all</code> or <code>-a</code> is given then all available commands are printed. If a Git command is named this option will bring up the manual page for that command. </p>
<p> Other options are available to control how the manual page is displayed. See <code><a href="/docs/linux/man/1-git-help/">git-help</a></code>(1) for more information, because <code>git &#8211;help &#8230;</code> is converted internally into <code>git help &#8230;</code>.</dl>
<p> -C &lt;path&gt;</p>
<dl>
<dt>
<dd> Run as if git was started in <i>&lt;path&gt;</i> instead of the current working directory. When multiple <code>-C</code> options are given, each subsequent non-absolute <code>-C &lt;path&gt;</code> is interpreted relative to the preceding <code>-C &lt;path&gt;</code>. If <i>&lt;path&gt;</i> is present but empty, e.g. <code>-C &quot;&quot;</code>, then the current working directory is left unchanged. </p>
<p> This option affects options that expect path name like <code>&#8211;git-dir</code> and <code>&#8211;work-tree</code> in that their interpretations of the path names would be made relative to the working directory caused by the <code>-C</code> option. For example the following invocations are equivalent: </p>
<dl>
<dt>
<dd>
git&#8211; git &#8211; dir = a.git&#8211; work &#8211; tree = b &#8211; C c status git&#8211; git &#8211; dir = c / a.git&#8211; work &#8211; tree = c / b status
</dl>
</dl>
<p> -c &lt;name&gt;=&lt;value&gt;</p>
<dl>
<dt>
<dd> Pass a configuration parameter to the command. The value given will override values from configuration files. The &lt;name&gt; is expected in the same format as listed by <i>git config</i> (subkeys separated by dots). </p>
<p> Note that omitting the <code>=</code> in <code>git -c foo.bar &#8230;</code> is allowed and sets <code>foo.bar</code> to the boolean true value (just like <code>[foo]bar</code> would in a config file). Including the equals but with an empty value (like <code>git -c foo.bar= &#8230;</code>) sets <code>foo.bar</code> to the empty string which <code>git config &#8211;type=bool</code> will convert to <code>false</code>.</dl>
<p> &#8211;config-env=&lt;name&gt;=&lt;envvar&gt;</p>
<dl>
<dt>
<dd> Like <code>-c &lt;name&gt;=&lt;value&gt;</code>, give configuration variable <i>&lt;name&gt;</i> a value, where &lt;envvar&gt; is the name of an environment variable from which to retrieve the value. Unlike <code>-c</code> there is no shortcut for directly setting the value to an empty string, instead the environment variable itself must be set to the empty string. It is an error if the <code>&lt;envvar&gt;</code> does not exist in the environment. <code>&lt;envvar&gt;</code> may not contain an equals sign to avoid ambiguity with <code>&lt;name&gt;</code> containing one. </p>
<p> This is useful for cases where you want to pass transitory configuration options to git, but are doing so on OS&#8217;s where other processes might be able to read your cmdline (e.g. <code>/proc/self/cmdline</code>), but not your environ (e.g. <code>/proc/self/environ</code>). That behavior is the default on Linux, but may not be on your system. </p>
<p> Note that this might add security for variables such as <code>http.extraHeader</code> where the sensitive information is part of the value, but not e.g. <code>url.&lt;base&gt;.insteadOf</code> where the sensitive information can be part of the key.</dl>
<p> &#8211;exec-path[=&lt;path&gt;]</p>
<dl>
<dt>
<dd> Path to wherever your core Git programs are installed. This can also be controlled by setting the GIT_EXEC_PATH environment variable. If no path is given, <i>git</i> will print the current setting and then exit.</dl>
<p> &#8211;html-path</p>
<dl>
<dt>
<dd> Print the path, without trailing slash, where Git&#8217;s HTML documentation is installed and exit.</dl>
<p> &#8211;man-path</p>
<dl>
<dt>
<dd> Print the manpath (see <code><a href="/docs/linux/man/1-man/">man</a>(1)</code>) for the man pages for this version of Git and exit.</dl>
<p> &#8211;info-path</p>
<dl>
<dt>
<dd> Print the path where the Info files documenting this version of Git are installed and exit.</dl>
<p> -p, &#8211;paginate</p>
<dl>
<dt>
<dd> Pipe all output into <i>less</i> (or if set, $PAGER) if standard output is a terminal. This overrides the <code>pager.&lt;cmd&gt;</code> configuration options (see the &quot;Configuration Mechanism&quot; section below).</dl>
<p> -P, &#8211;no-pager</p>
<dl>
<dt>
<dd> Do not pipe Git output into a pager.</dl>
<p> &#8211;git-dir=&lt;path&gt;</p>
<dl>
<dt>
<dd> Set the path to the repository (&quot;.git&quot; directory). This can also be controlled by setting the <code>GIT_DIR</code> environment variable. It can be an absolute path or relative path to current working directory. </p>
<p> Specifying the location of the &quot;.git&quot; directory using this option (or <code>GIT_DIR</code> environment variable) turns off the repository discovery that tries to find a directory with &quot;.git&quot; subdirectory (which is how the repository and the top-level of the working tree are discovered), and tells Git that you are at the top level of the working tree. If you are not at the top-level directory of the working tree, you should tell Git where the top-level of the working tree is, with the <code>&#8211;work-tree=&lt;path&gt;</code> option (or <code>GIT_WORK_TREE</code> environment variable) </p>
<p> If you just want to run git as if it was started in <code>&lt;path&gt;</code> then use <code>git -C &lt;path&gt;</code>.</dl>
<p> &#8211;work-tree=&lt;path&gt;</p>
<dl>
<dt>
<dd> Set the path to the working tree. It can be an absolute path or a path relative to the current working directory. This can also be controlled by setting the GIT_WORK_TREE environment variable and the core.worktree configuration variable (see core.worktree in <code><a href="/docs/linux/man/1-git-config/">git-config</a></code>(1) for a more detailed discussion).</dl>
<p> &#8211;namespace=&lt;path&gt;</p>
<dl>
<dt>
<dd> Set the Git namespace. See <code><a href="/docs/linux/man/7-gitnamespaces/">gitnamespaces</a></code>(7) for more details. Equivalent to setting the <code>GIT_NAMESPACE</code> environment variable.</dl>
<p> &#8211;super-prefix=&lt;path&gt;</p>
<dl>
<dt>
<dd> Currently for internal use only. Set a prefix which gives a path from above a repository down to its root. One use is to give submodules context about the superproject that invoked it.</dl>
<p> &#8211;bare</p>
<dl>
<dt>
<dd> Treat the repository as a bare repository. If GIT_DIR environment is not set, it is set to the current working directory.</dl>
<p> &#8211;no-replace-objects</p>
<dl>
<dt>
<dd> Do not use replacement refs to replace Git objects. See <code><a href="/docs/linux/man/1-git-replace/">git-replace</a></code>(1) for more information.</dl>
<p> &#8211;literal-pathspecs</p>
<dl>
<dt>
<dd> Treat pathspecs literally (i.e. no globbing, no pathspec magic). This is equivalent to setting the <code>GIT_LITERAL_PATHSPECS</code> environment variable to <code>1</code>.</dl>
<p> &#8211;glob-pathspecs</p>
<dl>
<dt>
<dd> Add &quot;glob&quot; magic to all pathspec. This is equivalent to setting the <code>GIT_GLOB_PATHSPECS</code> environment variable to <code>1</code>. Disabling globbing on individual pathspecs can be done using pathspec magic &quot;:(literal)&quot;</dl>
<p> &#8211;noglob-pathspecs</p>
<dl>
<dt>
<dd> Add &quot;literal&quot; magic to all pathspec. This is equivalent to setting the <code>GIT_NOGLOB_PATHSPECS</code> environment variable to <code>1</code>. Enabling globbing on individual pathspecs can be done using pathspec magic &quot;:(glob)&quot;</dl>
<p> &#8211;icase-pathspecs</p>
<dl>
<dt>
<dd> Add &quot;icase&quot; magic to all pathspec. This is equivalent to setting the <code>GIT_ICASE_PATHSPECS</code> environment variable to <code>1</code>.</dl>
<p> &#8211;no-optional-locks</p>
<dl>
<dt>
<dd> Do not perform optional operations that require locks. This is equivalent to setting the <code>GIT_OPTIONAL_LOCKS</code> to <code>0</code>.</dl>
<p> &#8211;list-cmds=group[,group&#8230;]</p>
<dl>
<dt>
<dd> List commands by group. This is an internal/experimental option and may change or be removed in the future. Supported groups are: builtins, parseopt (builtin commands that use parse-options), main (all commands in libexec directory), others (all other commands in <code>$PATH</code> that have git- prefix), list-&lt;category&gt; (see categories in command-list.txt), nohelpers (exclude helper commands), alias and config (retrieve command list from config variable completion.commands)</dl>
<h2>GIT COMMANDS</h2>
<p> We divide Git into high level (&quot;porcelain&quot;) commands and low level (&quot;plumbing&quot;) commands.</p>
<h2>HIGH-LEVEL COMMANDS (PORCELAIN)</h2>
<p> We separate the porcelain commands into the main commands and some ancillary user utilities.</p>
<h3>Main porcelain commands</h3>
<p> <code><a href="/docs/linux/man/1-git-add/">git-add</a></code>(1)</p>
<dl>
<dt>
<dd> Add file contents to the index.</dl>
<p> <code><a href="/docs/linux/man/1-git-am/">git-am</a></code>(1)</p>
<dl>
<dt>
<dd> Apply a series of patches from a mailbox.</dl>
<p> <code><a href="/docs/linux/man/1-git-archive/">git-archive</a></code>(1)</p>
<dl>
<dt>
<dd> Create an archive of files from a named tree.</dl>
<p> <code><a href="/docs/linux/man/1-git-bisect/">git-bisect</a></code>(1)</p>
<dl>
<dt>
<dd> Use binary search to find the commit that introduced a bug.</dl>
<p> <code><a href="/docs/linux/man/1-git-branch/">git-branch</a></code>(1)</p>
<dl>
<dt>
<dd> List, create, or delete branches.</dl>
<p> <code><a href="/docs/linux/man/1-git-bundle/">git-bundle</a></code>(1)</p>
<dl>
<dt>
<dd> Move objects and refs by archive.</dl>
<p> <code><a href="/docs/linux/man/1-git-checkout/">git-checkout</a></code>(1)</p>
<dl>
<dt>
<dd> Switch branches or restore working tree files.</dl>
<p> <code><a href="/docs/linux/man/1-git-cherry-pick/">git-cherry-pick</a></code>(1)</p>
<dl>
<dt>
<dd> Apply the changes introduced by some existing commits.</dl>
<p> <code><a href="/docs/linux/man/1-git-citool/">git-citool</a></code>(1)</p>
<dl>
<dt>
<dd> Graphical alternative to git-commit.</dl>
<p> <code><a href="/docs/linux/man/1-git-clean/">git-clean</a></code>(1)</p>
<dl>
<dt>
<dd> Remove untracked files from the working tree.</dl>
<p> <code><a href="/docs/linux/man/1-git-clone/">git-clone</a></code>(1)</p>
<dl>
<dt>
<dd> Clone a repository into a new directory.</dl>
<p> <code><a href="/docs/linux/man/1-git-commit/">git-commit</a></code>(1)</p>
<dl>
<dt>
<dd> Record changes to the repository.</dl>
<p> <code><a href="/docs/linux/man/1-git-describe/">git-describe</a></code>(1)</p>
<dl>
<dt>
<dd> Give an object a human readable name based on an available ref.</dl>
<p> <code><a href="/docs/linux/man/1-git-diff/">git-diff</a></code>(1)</p>
<dl>
<dt>
<dd> Show changes between commits, commit and working tree, etc.</dl>
<p> <code><a href="/docs/linux/man/1-git-fetch/">git-fetch</a></code>(1)</p>
<dl>
<dt>
<dd> Download objects and refs from another repository.</dl>
<p> <code><a href="/docs/linux/man/1-git-format-patch/">git-format-patch</a></code>(1)</p>
<dl>
<dt>
<dd> Prepare patches for e-mail submission.</dl>
<p> <code><a href="/docs/linux/man/1-git-gc/">git-gc</a></code>(1)</p>
<dl>
<dt>
<dd> Cleanup unnecessary files and optimize the local repository.</dl>
<p> <code><a href="/docs/linux/man/1-git-grep/">git-grep</a></code>(1)</p>
<dl>
<dt>
<dd> Print lines matching a pattern.</dl>
<p> <code><a href="/docs/linux/man/1-git-gui/">git-gui</a></code>(1)</p>
<dl>
<dt>
<dd> A portable graphical interface to Git.</dl>
<p> <code><a href="/docs/linux/man/1-git-init/">git-init</a></code>(1)</p>
<dl>
<dt>
<dd> Create an empty Git repository or reinitialize an existing one.</dl>
<p> <code><a href="/docs/linux/man/1-git-log/">git-log</a></code>(1)</p>
<dl>
<dt>
<dd> Show commit logs.</dl>
<p> <code><a href="/docs/linux/man/1-git-maintenance/">git-maintenance</a></code>(1)</p>
<dl>
<dt>
<dd> Run tasks to optimize Git repository data.</dl>
<p> <code><a href="/docs/linux/man/1-git-merge/">git-merge</a></code>(1)</p>
<dl>
<dt>
<dd> Join two or more development histories together.</dl>
<p> <code><a href="/docs/linux/man/1-git-mv/">git-mv</a></code>(1)</p>
<dl>
<dt>
<dd> Move or rename a file, a directory, or a symlink.</dl>
<p> <code><a href="/docs/linux/man/1-git-notes/">git-notes</a></code>(1)</p>
<dl>
<dt>
<dd> Add or inspect object notes.</dl>
<p> <code><a href="/docs/linux/man/1-git-pull/">git-pull</a></code>(1)</p>
<dl>
<dt>
<dd> Fetch from and integrate with another repository or a local branch.</dl>
<p> <code><a href="/docs/linux/man/1-git-push/">git-push</a></code>(1)</p>
<dl>
<dt>
<dd> Update remote refs along with associated objects.</dl>
<p> <code><a href="/docs/linux/man/1-git-range-diff/">git-range-diff</a></code>(1)</p>
<dl>
<dt>
<dd> Compare two commit ranges (e.g. two versions of a branch).</dl>
<p> <code><a href="/docs/linux/man/1-git-rebase/">git-rebase</a></code>(1)</p>
<dl>
<dt>
<dd> Reapply commits on top of another base tip.</dl>
<p> <code><a href="/docs/linux/man/1-git-reset/">git-reset</a></code>(1)</p>
<dl>
<dt>
<dd> Reset current HEAD to the specified state.</dl>
<p> <code><a href="/docs/linux/man/1-git-restore/">git-restore</a></code>(1)</p>
<dl>
<dt>
<dd> Restore working tree files.</dl>
<p> <code><a href="/docs/linux/man/1-git-revert/">git-revert</a></code>(1)</p>
<dl>
<dt>
<dd> Revert some existing commits.</dl>
<p> <code><a href="/docs/linux/man/1-git-rm/">git-rm</a></code>(1)</p>
<dl>
<dt>
<dd> Remove files from the working tree and from the index.</dl>
<p> <code><a href="/docs/linux/man/1-git-shortlog/">git-shortlog</a></code>(1)</p>
<dl>
<dt>
<dd> Summarize <i>git log</i> output.</dl>
<p> <code><a href="/docs/linux/man/1-git-show/">git-show</a></code>(1)</p>
<dl>
<dt>
<dd> Show various types of objects.</dl>
<p> <code><a href="/docs/linux/man/1-git-sparse-checkout/">git-sparse-checkout</a></code>(1)</p>
<dl>
<dt>
<dd> Initialize and modify the sparse-checkout.</dl>
<p> <code><a href="/docs/linux/man/1-git-stash/">git-stash</a></code>(1)</p>
<dl>
<dt>
<dd> Stash the changes in a dirty working directory away.</dl>
<p> <code><a href="/docs/linux/man/1-git-status/">git-status</a></code>(1)</p>
<dl>
<dt>
<dd> Show the working tree status.</dl>
<p> <code><a href="/docs/linux/man/1-git-submodule/">git-submodule</a></code>(1)</p>
<dl>
<dt>
<dd> Initialize, update or inspect submodules.</dl>
<p> <code><a href="/docs/linux/man/1-git-switch/">git-switch</a></code>(1)</p>
<dl>
<dt>
<dd> Switch branches.</dl>
<p> <code><a href="/docs/linux/man/1-git-tag/">git-tag</a></code>(1)</p>
<dl>
<dt>
<dd> Create, list, delete or verify a tag object signed with GPG.</dl>
<p> <code><a href="/docs/linux/man/1-git-worktree/">git-worktree</a></code>(1)</p>
<dl>
<dt>
<dd> Manage multiple working trees.</dl>
<p> <code><a href="/docs/linux/man/1-gitk/">gitk</a></code>(1)</p>
<dl>
<dt>
<dd> The Git repository browser.</dl>
<h3>Ancillary Commands</h3>
<p> Manipulators: </p>
<p> <code><a href="/docs/linux/man/1-git-config/">git-config</a></code>(1)</p>
<dl>
<dt>
<dd> Get and set repository or global options.</dl>
<p> <code><a href="/docs/linux/man/1-git-fast-export/">git-fast-export</a></code>(1)</p>
<dl>
<dt>
<dd> Git data exporter.</dl>
<p> <code><a href="/docs/linux/man/1-git-fast-import/">git-fast-import</a></code>(1)</p>
<dl>
<dt>
<dd> Backend for fast Git data importers.</dl>
<p> <code><a href="/docs/linux/man/1-git-filter-branch/">git-filter-branch</a></code>(1)</p>
<dl>
<dt>
<dd> Rewrite branches.</dl>
<p> <code><a href="/docs/linux/man/1-git-mergetool/">git-mergetool</a></code>(1)</p>
<dl>
<dt>
<dd> Run merge conflict resolution tools to resolve merge conflicts.</dl>
<p> <code><a href="/docs/linux/man/1-git-pack-refs/">git-pack-refs</a></code>(1)</p>
<dl>
<dt>
<dd> Pack heads and tags for efficient repository access.</dl>
<p> <code><a href="/docs/linux/man/1-git-prune/">git-prune</a></code>(1)</p>
<dl>
<dt>
<dd> Prune all unreachable objects from the object database.</dl>
<p> <code><a href="/docs/linux/man/1-git-reflog/">git-reflog</a></code>(1)</p>
<dl>
<dt>
<dd> Manage reflog information.</dl>
<p> <code><a href="/docs/linux/man/1-git-remote/">git-remote</a></code>(1)</p>
<dl>
<dt>
<dd> Manage set of tracked repositories.</dl>
<p> <code><a href="/docs/linux/man/1-git-repack/">git-repack</a></code>(1)</p>
<dl>
<dt>
<dd> Pack unpacked objects in a repository.</dl>
<p> <code><a href="/docs/linux/man/1-git-replace/">git-replace</a></code>(1)</p>
<dl>
<dt>
<dd> Create, list, delete refs to replace objects.</dl>
<p> Interrogators: </p>
<p> <code><a href="/docs/linux/man/1-git-annotate/">git-annotate</a></code>(1)</p>
<dl>
<dt>
<dd> Annotate file lines with commit information.</dl>
<p> <code><a href="/docs/linux/man/1-git-blame/">git-blame</a></code>(1)</p>
<dl>
<dt>
<dd> Show what revision and author last modified each line of a file.</dl>
<p> <code><a href="/docs/linux/man/1-git-bugreport/">git-bugreport</a></code>(1)</p>
<dl>
<dt>
<dd> Collect information for user to file a bug report.</dl>
<p> <code><a href="/docs/linux/man/1-git-count-objects/">git-count-objects</a></code>(1)</p>
<dl>
<dt>
<dd> Count unpacked number of objects and their disk consumption.</dl>
<p> <code><a href="/docs/linux/man/1-git-difftool/">git-difftool</a></code>(1)</p>
<dl>
<dt>
<dd> Show changes using common diff tools.</dl>
<p> <code><a href="/docs/linux/man/1-git-fsck/">git-fsck</a></code>(1)</p>
<dl>
<dt>
<dd> Verifies the connectivity and validity of the objects in the database.</dl>
<p> <code><a href="/docs/linux/man/1-git-help/">git-help</a></code>(1)</p>
<dl>
<dt>
<dd> Display help information about Git.</dl>
<p> <code><a href="/docs/linux/man/1-git-instaweb/">git-instaweb</a></code>(1)</p>
<dl>
<dt>
<dd> Instantly browse your working repository in gitweb.</dl>
<p> <code><a href="/docs/linux/man/1-git-merge-tree/">git-merge-tree</a></code>(1)</p>
<dl>
<dt>
<dd> Show three-way merge without touching index.</dl>
<p> <code><a href="/docs/linux/man/1-git-rerere/">git-rerere</a></code>(1)</p>
<dl>
<dt>
<dd> Reuse recorded resolution of conflicted merges.</dl>
<p> <code><a href="/docs/linux/man/1-git-show-branch/">git-show-branch</a></code>(1)</p>
<dl>
<dt>
<dd> Show branches and their commits.</dl>
<p> <code><a href="/docs/linux/man/1-git-verify-commit/">git-verify-commit</a></code>(1)</p>
<dl>
<dt>
<dd> Check the GPG signature of commits.</dl>
<p> <code><a href="/docs/linux/man/1-git-verify-tag/">git-verify-tag</a></code>(1)</p>
<dl>
<dt>
<dd> Check the GPG signature of tags.</dl>
<p> <code><a href="/docs/linux/man/1-git-whatchanged/">git-whatchanged</a></code>(1)</p>
<dl>
<dt>
<dd> Show logs with difference each commit introduces.</dl>
<p> <code><a href="/docs/linux/man/1-gitweb/">gitweb</a></code>(1)</p>
<dl>
<dt>
<dd> Git web interface (web frontend to Git repositories).</dl>
<h3>Interacting with Others</h3>
<p> These commands are to interact with foreign SCM and with other people via patch over e-mail. </p>
<p> <code><a href="/docs/linux/man/1-git-archimport/">git-archimport</a></code>(1)</p>
<dl>
<dt>
<dd> Import a GNU Arch repository into Git.</dl>
<p> <code><a href="/docs/linux/man/1-git-cvsexportcommit/">git-cvsexportcommit</a></code>(1)</p>
<dl>
<dt>
<dd> Export a single commit to a CVS checkout.</dl>
<p> <code><a href="/docs/linux/man/1-git-cvsimport/">git-cvsimport</a></code>(1)</p>
<dl>
<dt>
<dd> Salvage your data out of another SCM people love to hate.</dl>
<p> <code><a href="/docs/linux/man/1-git-cvsserver/">git-cvsserver</a></code>(1)</p>
<dl>
<dt>
<dd> A CVS server emulator for Git.</dl>
<p> <code><a href="/docs/linux/man/1-git-imap-send/">git-imap-send</a></code>(1)</p>
<dl>
<dt>
<dd> Send a collection of patches from stdin to an IMAP folder.</dl>
<p> <code><a href="/docs/linux/man/1-git-p4/">git-p4</a></code>(1)</p>
<dl>
<dt>
<dd> Import from and submit to Perforce repositories.</dl>
<p> <code><a href="/docs/linux/man/1-git-quiltimport/">git-quiltimport</a></code>(1)</p>
<dl>
<dt>
<dd> Applies a quilt patchset onto the current branch.</dl>
<p> <code><a href="/docs/linux/man/1-git-request-pull/">git-request-pull</a></code>(1)</p>
<dl>
<dt>
<dd> Generates a summary of pending changes.</dl>
<p> <code><a href="/docs/linux/man/1-git-send-email/">git-send-email</a></code>(1)</p>
<dl>
<dt>
<dd> Send a collection of patches as emails.</dl>
<p> <code><a href="/docs/linux/man/1-git-svn/">git-svn</a></code>(1)</p>
<dl>
<dt>
<dd> Bidirectional operation between a Subversion repository and Git.</dl>
<h3>Reset, restore and revert</h3>
<p> There are three commands with similar names: <code>git reset</code>, <code>git restore</code> and <code>git revert</code>. </p>
<dl>
<dt>
<dd> &bull; <code><a href="/docs/linux/man/1-git-revert/">git-revert</a></code>(1) is about making a new commit that reverts the changes made by other commits.</dl>
<dl>
<dt>
<dd> &bull; <code><a href="/docs/linux/man/1-git-restore/">git-restore</a></code>(1) is about restoring files in the working tree from either the index or another commit. This command does not update your branch. The command can also be used to restore files in the index from another commit.</dl>
<dl>
<dt>
<dd> &bull; <code><a href="/docs/linux/man/1-git-reset/">git-reset</a></code>(1) is about updating your branch, moving the tip in order to add or remove commits from the branch. This operation changes the commit history. </p>
<p> <code>git reset</code> can also be used to restore the index, overlapping with <code>git restore</code>.</dl>
<h2>LOW-LEVEL COMMANDS (PLUMBING)</h2>
<p> Although Git includes its own porcelain layer, its low-level commands are sufficient to support development of alternative porcelains. Developers of such porcelains might start by reading about <code><a href="/docs/linux/man/1-git-update-index/">git-update-index</a></code>(1) and <code><a href="/docs/linux/man/1-git-read-tree/">git-read-tree</a></code>(1). </p>
<p> The interface (input, output, set of options and the semantics) to these low-level commands are meant to be a lot more stable than Porcelain level commands, because these commands are primarily for scripted use. The interface to Porcelain commands on the other hand are subject to change in order to improve the end user experience. </p>
<p> The following description divides the low-level commands into commands that manipulate objects (in the repository, index, and working tree), commands that interrogate and compare objects, and commands that move objects and references between repositories.</p>
<h3>Manipulation commands</h3>
<p> <code><a href="/docs/linux/man/1-git-apply/">git-apply</a></code>(1)</p>
<dl>
<dt>
<dd> Apply a patch to files and/or to the index.</dl>
<p> <code><a href="/docs/linux/man/1-git-checkout-index/">git-checkout-index</a></code>(1)</p>
<dl>
<dt>
<dd> Copy files from the index to the working tree.</dl>
<p> <code><a href="/docs/linux/man/1-git-commit-graph/">git-commit-graph</a></code>(1)</p>
<dl>
<dt>
<dd> Write and verify Git commit-graph files.</dl>
<p> <code><a href="/docs/linux/man/1-git-commit-tree/">git-commit-tree</a></code>(1)</p>
<dl>
<dt>
<dd> Create a new commit object.</dl>
<p> <code><a href="/docs/linux/man/1-git-hash-object/">git-hash-object</a></code>(1)</p>
<dl>
<dt>
<dd> Compute object ID and optionally creates a blob from a file.</dl>
<p> <code><a href="/docs/linux/man/1-git-index-pack/">git-index-pack</a></code>(1)</p>
<dl>
<dt>
<dd> Build pack index file for an existing packed archive.</dl>
<p> <code><a href="/docs/linux/man/1-git-merge-file/">git-merge-file</a></code>(1)</p>
<dl>
<dt>
<dd> Run a three-way file merge.</dl>
<p> <code><a href="/docs/linux/man/1-git-merge-index/">git-merge-index</a></code>(1)</p>
<dl>
<dt>
<dd> Run a merge for files needing merging.</dl>
<p> <code><a href="/docs/linux/man/1-git-mktag/">git-mktag</a></code>(1)</p>
<dl>
<dt>
<dd> Creates a tag object with extra validation.</dl>
<p> <code><a href="/docs/linux/man/1-git-mktree/">git-mktree</a></code>(1)</p>
<dl>
<dt>
<dd> Build a tree-object from ls-tree formatted text.</dl>
<p> <code><a href="/docs/linux/man/1-git-multi-pack-index/">git-multi-pack-index</a></code>(1)</p>
<dl>
<dt>
<dd> Write and verify multi-pack-indexes.</dl>
<p> <code><a href="/docs/linux/man/1-git-pack-objects/">git-pack-objects</a></code>(1)</p>
<dl>
<dt>
<dd> Create a packed archive of objects.</dl>
<p> <code><a href="/docs/linux/man/1-git-prune-packed/">git-prune-packed</a></code>(1)</p>
<dl>
<dt>
<dd> Remove extra objects that are already in pack files.</dl>
<p> <code><a href="/docs/linux/man/1-git-read-tree/">git-read-tree</a></code>(1)</p>
<dl>
<dt>
<dd> Reads tree information into the index.</dl>
<p> <code><a href="/docs/linux/man/1-git-symbolic-ref/">git-symbolic-ref</a></code>(1)</p>
<dl>
<dt>
<dd> Read, modify and delete symbolic refs.</dl>
<p> <code><a href="/docs/linux/man/1-git-unpack-objects/">git-unpack-objects</a></code>(1)</p>
<dl>
<dt>
<dd> Unpack objects from a packed archive.</dl>
<p> <code><a href="/docs/linux/man/1-git-update-index/">git-update-index</a></code>(1)</p>
<dl>
<dt>
<dd> Register file contents in the working tree to the index.</dl>
<p> <code><a href="/docs/linux/man/1-git-update-ref/">git-update-ref</a></code>(1)</p>
<dl>
<dt>
<dd> Update the object name stored in a ref safely.</dl>
<p> <code><a href="/docs/linux/man/1-git-write-tree/">git-write-tree</a></code>(1)</p>
<dl>
<dt>
<dd> Create a tree object from the current index.</dl>
<h3>Interrogation commands</h3>
<p> <code><a href="/docs/linux/man/1-git-cat-file/">git-cat-file</a></code>(1)</p>
<dl>
<dt>
<dd> Provide content or type and size information for repository objects.</dl>
<p> <code><a href="/docs/linux/man/1-git-cherry/">git-cherry</a></code>(1)</p>
<dl>
<dt>
<dd> Find commits yet to be applied to upstream.</dl>
<p> <code><a href="/docs/linux/man/1-git-diff-files/">git-diff-files</a></code>(1)</p>
<dl>
<dt>
<dd> Compares files in the working tree and the index.</dl>
<p> <code><a href="/docs/linux/man/1-git-diff-index/">git-diff-index</a></code>(1)</p>
<dl>
<dt>
<dd> Compare a tree to the working tree or index.</dl>
<p> <code><a href="/docs/linux/man/1-git-diff-tree/">git-diff-tree</a></code>(1)</p>
<dl>
<dt>
<dd> Compares the content and mode of blobs found via two tree objects.</dl>
<p> <code><a href="/docs/linux/man/1-git-for-each-ref/">git-for-each-ref</a></code>(1)</p>
<dl>
<dt>
<dd> Output information on each ref.</dl>
<p> <code><a href="/docs/linux/man/1-git-for-each-repo/">git-for-each-repo</a></code>(1)</p>
<dl>
<dt>
<dd> Run a Git command on a list of repositories.</dl>
<p> <code><a href="/docs/linux/man/1-git-get-tar-commit-id/">git-get-tar-commit-id</a></code>(1)</p>
<dl>
<dt>
<dd> Extract commit ID from an archive created using git-archive.</dl>
<p> <code><a href="/docs/linux/man/1-git-ls-files/">git-ls-files</a></code>(1)</p>
<dl>
<dt>
<dd> Show information about files in the index and the working tree.</dl>
<p> <code><a href="/docs/linux/man/1-git-ls-remote/">git-ls-remote</a></code>(1)</p>
<dl>
<dt>
<dd> List references in a remote repository.</dl>
<p> <code><a href="/docs/linux/man/1-git-ls-tree/">git-ls-tree</a></code>(1)</p>
<dl>
<dt>
<dd> List the contents of a tree object.</dl>
<p> <code><a href="/docs/linux/man/1-git-merge-base/">git-merge-base</a></code>(1)</p>
<dl>
<dt>
<dd> Find as good common ancestors as possible for a merge.</dl>
<p> <code><a href="/docs/linux/man/1-git-name-rev/">git-name-rev</a></code>(1)</p>
<dl>
<dt>
<dd> Find symbolic names for given revs.</dl>
<p> <code><a href="/docs/linux/man/1-git-pack-redundant/">git-pack-redundant</a></code>(1)</p>
<dl>
<dt>
<dd> Find redundant pack files.</dl>
<p> <code><a href="/docs/linux/man/1-git-rev-list/">git-rev-list</a></code>(1)</p>
<dl>
<dt>
<dd> Lists commit objects in reverse chronological order.</dl>
<p> <code><a href="/docs/linux/man/1-git-rev-parse/">git-rev-parse</a></code>(1)</p>
<dl>
<dt>
<dd> Pick out and massage parameters.</dl>
<p> <code><a href="/docs/linux/man/1-git-show-index/">git-show-index</a></code>(1)</p>
<dl>
<dt>
<dd> Show packed archive index.</dl>
<p> <code><a href="/docs/linux/man/1-git-show-ref/">git-show-ref</a></code>(1)</p>
<dl>
<dt>
<dd> List references in a local repository.</dl>
<p> <code><a href="/docs/linux/man/1-git-unpack-file/">git-unpack-file</a></code>(1)</p>
<dl>
<dt>
<dd> Creates a temporary file with a blob&#8217;s contents.</dl>
<p> <code><a href="/docs/linux/man/1-git-var/">git-var</a></code>(1)</p>
<dl>
<dt>
<dd> Show a Git logical variable.</dl>
<p> <code><a href="/docs/linux/man/1-git-verify-pack/">git-verify-pack</a></code>(1)</p>
<dl>
<dt>
<dd> Validate packed Git archive files.</dl>
<p> In general, the interrogate commands do not touch the files in the working tree.</p>
<h3>Syncing repositories</h3>
<p> <code><a href="/docs/linux/man/1-git-daemon/">git-daemon</a></code>(1)</p>
<dl>
<dt>
<dd> A really simple server for Git repositories.</dl>
<p> <code><a href="/docs/linux/man/1-git-fetch-pack/">git-fetch-pack</a></code>(1)</p>
<dl>
<dt>
<dd> Receive missing objects from another repository.</dl>
<p> <code><a href="/docs/linux/man/1-git-http-backend/">git-http-backend</a></code>(1)</p>
<dl>
<dt>
<dd> Server side implementation of Git over HTTP.</dl>
<p> <code><a href="/docs/linux/man/1-git-send-pack/">git-send-pack</a></code>(1)</p>
<dl>
<dt>
<dd> Push objects over Git protocol to another repository.</dl>
<p> <code><a href="/docs/linux/man/1-git-update-server-info/">git-update-server-info</a></code>(1)</p>
<dl>
<dt>
<dd> Update auxiliary info file to help dumb servers.</dl>
<p> The following are helper commands used by the above; end users typically do not use them directly. </p>
<p> <code><a href="/docs/linux/man/1-git-http-fetch/">git-http-fetch</a></code>(1)</p>
<dl>
<dt>
<dd> Download from a remote Git repository via HTTP.</dl>
<p> <code><a href="/docs/linux/man/1-git-http-push/">git-http-push</a></code>(1)</p>
<dl>
<dt>
<dd> Push objects over HTTP/DAV to another repository.</dl>
<p> <code><a href="/docs/linux/man/1-git-receive-pack/">git-receive-pack</a></code>(1)</p>
<dl>
<dt>
<dd> Receive what is pushed into the repository.</dl>
<p> <code><a href="/docs/linux/man/1-git-shell/">git-shell</a></code>(1)</p>
<dl>
<dt>
<dd> Restricted login shell for Git-only SSH access.</dl>
<p> <code><a href="/docs/linux/man/1-git-upload-archive/">git-upload-archive</a></code>(1)</p>
<dl>
<dt>
<dd> Send archive back to git-archive.</dl>
<p> <code><a href="/docs/linux/man/1-git-upload-pack/">git-upload-pack</a></code>(1)</p>
<dl>
<dt>
<dd> Send objects packed back to git-fetch-pack.</dl>
<h3>Internal helper commands</h3>
<p> These are internal helper commands used by other commands; end users typically do not use them directly. </p>
<p> <code><a href="/docs/linux/man/1-git-check-attr/">git-check-attr</a></code>(1)</p>
<dl>
<dt>
<dd> Display gitattributes information.</dl>
<p> <code><a href="/docs/linux/man/1-git-check-ignore/">git-check-ignore</a></code>(1)</p>
<dl>
<dt>
<dd> Debug gitignore / exclude files.</dl>
<p> <code><a href="/docs/linux/man/1-git-check-mailmap/">git-check-mailmap</a></code>(1)</p>
<dl>
<dt>
<dd> Show canonical names and email addresses of contacts.</dl>
<p> <code><a href="/docs/linux/man/1-git-check-ref-format/">git-check-ref-format</a></code>(1)</p>
<dl>
<dt>
<dd> Ensures that a reference name is well formed.</dl>
<p> <code><a href="/docs/linux/man/1-git-column/">git-column</a></code>(1)</p>
<dl>
<dt>
<dd> Display data in columns.</dl>
<p> <code><a href="/docs/linux/man/1-git-credential/">git-credential</a></code>(1)</p>
<dl>
<dt>
<dd> Retrieve and store user credentials.</dl>
<p> <code><a href="/docs/linux/man/1-git-credential-cache/">git-credential-cache</a></code>(1)</p>
<dl>
<dt>
<dd> Helper to temporarily store passwords in memory.</dl>
<p> <code><a href="/docs/linux/man/1-git-credential-store/">git-credential-store</a></code>(1)</p>
<dl>
<dt>
<dd> Helper to store credentials on disk.</dl>
<p> <code><a href="/docs/linux/man/1-git-fmt-merge-msg/">git-fmt-merge-msg</a></code>(1)</p>
<dl>
<dt>
<dd> Produce a merge commit message.</dl>
<p> <code><a href="/docs/linux/man/1-git-interpret-trailers/">git-interpret-trailers</a></code>(1)</p>
<dl>
<dt>
<dd> Add or parse structured information in commit messages.</dl>
<p> <code><a href="/docs/linux/man/1-git-mailinfo/">git-mailinfo</a></code>(1)</p>
<dl>
<dt>
<dd> Extracts patch and authorship from a single e-mail message.</dl>
<p> <code><a href="/docs/linux/man/1-git-mailsplit/">git-mailsplit</a></code>(1)</p>
<dl>
<dt>
<dd> Simple UNIX mbox splitter program.</dl>
<p> <code><a href="/docs/linux/man/1-git-merge-one-file/">git-merge-one-file</a></code>(1)</p>
<dl>
<dt>
<dd> The standard helper program to use with git-merge-index.</dl>
<p> <code><a href="/docs/linux/man/1-git-patch-id/">git-patch-id</a></code>(1)</p>
<dl>
<dt>
<dd> Compute unique ID for a patch.</dl>
<p> <code><a href="/docs/linux/man/1-git-sh-i18n/">git-sh-i18n</a></code>(1)</p>
<dl>
<dt>
<dd> Git&#8217;s i18n setup code for shell scripts.</dl>
<p> <code><a href="/docs/linux/man/1-git-sh-setup/">git-sh-setup</a></code>(1)</p>
<dl>
<dt>
<dd> Common Git shell script setup code.</dl>
<p> <code><a href="/docs/linux/man/1-git-stripspace/">git-stripspace</a></code>(1)</p>
<dl>
<dt>
<dd> Remove unnecessary whitespace.</dl>
<h2>GUIDES</h2>
<p> The following documentation pages are guides about Git concepts. </p>
<p> <code><a href="/docs/linux/man/5-gitattributes/">gitattributes</a></code>(5)</p>
<dl>
<dt>
<dd> Defining attributes per path.</dl>
<p> <code><a href="/docs/linux/man/7-gitcli/">gitcli</a></code>(7)</p>
<dl>
<dt>
<dd> Git command-line interface and conventions.</dl>
<p> <code><a href="/docs/linux/man/7-gitcore-tutorial/">gitcore-tutorial</a></code>(7)</p>
<dl>
<dt>
<dd> A Git core tutorial for developers.</dl>
<p> <code><a href="/docs/linux/man/7-gitcredentials/">gitcredentials</a></code>(7)</p>
<dl>
<dt>
<dd> Providing usernames and passwords to Git.</dl>
<p> <code><a href="/docs/linux/man/7-gitcvs-migration/">gitcvs-migration</a></code>(7)</p>
<dl>
<dt>
<dd> Git for CVS users.</dl>
<p> <code><a href="/docs/linux/man/7-gitdiffcore/">gitdiffcore</a></code>(7)</p>
<dl>
<dt>
<dd> Tweaking diff output.</dl>
<p> <code><a href="/docs/linux/man/7-giteveryday/">giteveryday</a></code>(7)</p>
<dl>
<dt>
<dd> A useful minimum set of commands for Everyday Git.</dl>
<p> <code><a href="/docs/linux/man/7-gitfaq/">gitfaq</a></code>(7)</p>
<dl>
<dt>
<dd> Frequently asked questions about using Git.</dl>
<p> <code><a href="/docs/linux/man/7-gitglossary/">gitglossary</a></code>(7)</p>
<dl>
<dt>
<dd> A Git Glossary.</dl>
<p> <code><a href="/docs/linux/man/5-githooks/">githooks</a></code>(5)</p>
<dl>
<dt>
<dd> Hooks used by Git.</dl>
<p> <code><a href="/docs/linux/man/5-gitignore/">gitignore</a></code>(5)</p>
<dl>
<dt>
<dd> Specifies intentionally untracked files to ignore.</dl>
<p> <code><a href="/docs/linux/man/5-gitmailmap/">gitmailmap</a></code>(5)</p>
<dl>
<dt>
<dd> Map author/committer names and/or E-Mail addresses.</dl>
<p> <code><a href="/docs/linux/man/5-gitmodules/">gitmodules</a></code>(5)</p>
<dl>
<dt>
<dd> Defining submodule properties.</dl>
<p> <code><a href="/docs/linux/man/7-gitnamespaces/">gitnamespaces</a></code>(7)</p>
<dl>
<dt>
<dd> Git namespaces.</dl>
<p> <code><a href="/docs/linux/man/7-gitremote-helpers/">gitremote-helpers</a></code>(7)</p>
<dl>
<dt>
<dd> Helper programs to interact with remote repositories.</dl>
<p> <code><a href="/docs/linux/man/5-gitrepository-layout/">gitrepository-layout</a></code>(5)</p>
<dl>
<dt>
<dd> Git Repository Layout.</dl>
<p> <code><a href="/docs/linux/man/7-gitrevisions/">gitrevisions</a></code>(7)</p>
<dl>
<dt>
<dd> Specifying revisions and ranges for Git.</dl>
<p> <code><a href="/docs/linux/man/7-gitsubmodules/">gitsubmodules</a></code>(7)</p>
<dl>
<dt>
<dd> Mounting one repository inside another.</dl>
<p> <code><a href="/docs/linux/man/7-gittutorial/">gittutorial</a></code>(7)</p>
<dl>
<dt>
<dd> A tutorial introduction to Git.</dl>
<p> <code><a href="/docs/linux/man/7-gittutorial-2/">gittutorial-2</a></code>(7)</p>
<dl>
<dt>
<dd> A tutorial introduction to Git: part two.</dl>
<p> <code><a href="/docs/linux/man/7-gitworkflows/">gitworkflows</a></code>(7)</p>
<dl>
<dt>
<dd> An overview of recommended workflows with Git.</dl>
<h2>CONFIGURATION MECHANISM</h2>
<p> Git uses a simple text format to store customizations that are per repository and are per user. Such a configuration file may look like this: </p>
<dl>
<dt>
<dd>
<pre><code>
#
#A '#' or ';' character indicates a comment.
#
;
core variables
    [core];
Don't trust file modes filemode = false;
user identity
    [user] name = "Junio C Hamano" email = "gitster [at] pobox.com"
</code></pre>
</dl>
<p> Various commands read from the configuration file and adjust their operation accordingly. See <code><a href="/docs/linux/man/1-git-config/">git-config</a></code>(1) for a list and more details about the configuration mechanism.</p>
<h2>IDENTIFIER TERMINOLOGY</h2>
<p> &lt;object&gt;</p>
<dl>
<dt>
<dd> Indicates the object name for any type of object.</dl>
<p> &lt;blob&gt;</p>
<dl>
<dt>
<dd> Indicates a blob object name.</dl>
<p> &lt;tree&gt;</p>
<dl>
<dt>
<dd> Indicates a tree object name.</dl>
<p> &lt;commit&gt;</p>
<dl>
<dt>
<dd> Indicates a commit object name.</dl>
<p> &lt;tree-ish&gt;</p>
<dl>
<dt>
<dd> Indicates a tree, commit or tag object name. A command that takes a &lt;tree-ish&gt; argument ultimately wants to operate on a &lt;tree&gt; object but automatically dereferences &lt;commit&gt; and &lt;tag&gt; objects that point at a &lt;tree&gt;.</dl>
<p> &lt;commit-ish&gt;</p>
<dl>
<dt>
<dd> Indicates a commit or tag object name. A command that takes a &lt;commit-ish&gt; argument ultimately wants to operate on a &lt;commit&gt; object but automatically dereferences &lt;tag&gt; objects that point at a &lt;commit&gt;.</dl>
<p> &lt;type&gt;</p>
<dl>
<dt>
<dd> Indicates that an object type is required. Currently one of: <code>blob</code>, <code>tree</code>, <code>commit</code>, or <code>tag</code>.</dl>
<p> &lt;file&gt;</p>
<dl>
<dt>
<dd> Indicates a filename &#8211; almost always relative to the root of the tree structure <code>GIT_INDEX_FILE</code> describes.</dl>
<h2>SYMBOLIC IDENTIFIERS</h2>
<p> Any Git command accepting any &lt;object&gt; can also use the following symbolic notation: </p>
<p> HEAD</p>
<dl>
<dt>
<dd> indicates the head of the current branch.</dl>
<p> &lt;tag&gt;</p>
<dl>
<dt>
<dd> a valid tag <i>name</i> (i.e. a <code>refs/tags/&lt;tag&gt;</code> reference).</dl>
<p> &lt;head&gt;</p>
<dl>
<dt>
<dd> a valid head <i>name</i> (i.e. a <code>refs/heads/&lt;head&gt;</code> reference).</dl>
<p> For a more complete list of ways to spell object names, see &quot;SPECIFYING REVISIONS&quot; section in <code><a href="/docs/linux/man/7-gitrevisions/">gitrevisions</a></code>(7).</p>
<h2>FILE/DIRECTORY STRUCTURE</h2>
<p> Please see the <code><a href="/docs/linux/man/5-gitrepository-layout/">gitrepository-layout</a></code>(5) document. </p>
<p> Read <code><a href="/docs/linux/man/5-githooks/">githooks</a></code>(5) for more details about each hook. </p>
<p> Higher level SCMs may provide and manage additional information in the <code>$GIT_DIR</code>.</p>
<h2>TERMINOLOGY</h2>
<p> Please see <code><a href="/docs/linux/man/7-gitglossary/">gitglossary</a></code>(7).</p>
<h2>ENVIRONMENT VARIABLES</h2>
<p> Various Git commands use the following environment variables:</p>
<h3>The Git Repository</h3>
<p> These environment variables apply to <i>all</i> core Git commands. Nb: it is worth noting that they may be used/overridden by SCMS sitting above Git so take care if using a foreign front-end. </p>
<p> <code>GIT_INDEX_FILE</code></p>
<dl>
<dt>
<dd> This environment allows the specification of an alternate index file. If not specified, the default of <code>$GIT_DIR/index</code> is used.</dl>
<p> <code>GIT_INDEX_VERSION</code></p>
<dl>
<dt>
<dd> This environment variable allows the specification of an index version for new repositories. It won&#8217;t affect existing index files. By default index file version 2 or 3 is used. See <code><a href="/docs/linux/man/1-git-update-index/">git-update-index</a></code>(1) for more information.</dl>
<p> <code>GIT_OBJECT_DIRECTORY</code></p>
<dl>
<dt>
<dd> If the object storage directory is specified via this environment variable then the sha1 directories are created underneath &#8211; otherwise the default <code>$GIT_DIR/objects</code> directory is used.</dl>
<p> <code>GIT_ALTERNATE_OBJECT_DIRECTORIES</code></p>
<dl>
<dt>
<dd> Due to the immutable nature of Git objects, old objects can be archived into shared, read-only directories. This variable specifies a &quot;:&quot; separated (on Windows &quot;;&quot; separated) list of Git object directories which can be used to search for Git objects. New objects will not be written to these directories. </p>
<p> Entries that begin with <code>&quot;</code> (double-quote) will be interpreted as C-style quoted paths, removing leading and trailing double-quotes and respecting backslash escapes. E.g., the value <code>&quot;path-with-\&quot;-and-:-in-it&quot;:vanilla-path</code> has two paths: <code>path-with-&quot;-and-:-in-it</code> and <code>vanilla-path</code>.</dl>
<p> <code>GIT_DIR</code></p>
<dl>
<dt>
<dd> If the <code>GIT_DIR</code> environment variable is set then it specifies a path to use instead of the default <code>.git</code> for the base of the repository. The <code>&#8211;git-dir</code> command-line option also sets this value.</dl>
<p> <code>GIT_WORK_TREE</code></p>
<dl>
<dt>
<dd> Set the path to the root of the working tree. This can also be controlled by the <code>&#8211;work-tree</code> command-line option and the core.worktree configuration variable.</dl>
<p> <code>GIT_NAMESPACE</code></p>
<dl>
<dt>
<dd> Set the Git namespace; see <code><a href="/docs/linux/man/7-gitnamespaces/">gitnamespaces</a></code>(7) for details. The <code>&#8211;namespace</code> command-line option also sets this value.</dl>
<p> <code>GIT_CEILING_DIRECTORIES</code></p>
<dl>
<dt>
<dd> This should be a colon-separated list of absolute paths. If set, it is a list of directories that Git should not chdir up into while looking for a repository directory (useful for excluding slow-loading network directories). It will not exclude the current working directory or a GIT_DIR set on the command line or in the environment. Normally, Git has to read the entries in this list and resolve any symlink that might be present in order to compare them with the current directory. However, if even this access is slow, you can add an empty entry to the list to tell Git that the subsequent entries are not symlinks and needn&#8217;t be resolved; e.g., <code>GIT_CEILING_DIRECTORIES=/maybe/symlink::/very/slow/non/symlink</code>.</dl>
<p> <code>GIT_DISCOVERY_ACROSS_FILESYSTEM</code></p>
<dl>
<dt>
<dd> When run in a directory that does not have &quot;.git&quot; repository directory, Git tries to find such a directory in the parent directories to find the top of the working tree, but by default it does not cross filesystem boundaries. This environment variable can be set to true to tell Git not to stop at filesystem boundaries. Like <code>GIT_CEILING_DIRECTORIES</code>, this will not affect an explicit repository directory set via <code>GIT_DIR</code> or on the command line.</dl>
<p> <code>GIT_COMMON_DIR</code></p>
<dl>
<dt>
<dd> If this variable is set to a path, non-worktree files that are normally in $GIT_DIR will be taken from this path instead. Worktree-specific files such as HEAD or index are taken from $GIT_DIR. See <code><a href="/docs/linux/man/5-gitrepository-layout/">gitrepository-layout</a></code>(5) and <code><a href="/docs/linux/man/1-git-worktree/">git-worktree</a></code>(1) for details. This variable has lower precedence than other path variables such as GIT_INDEX_FILE, GIT_OBJECT_DIRECTORY&#8230;</dl>
<p> <code>GIT_DEFAULT_HASH</code></p>
<dl>
<dt>
<dd> If this variable is set, the default hash algorithm for new repositories will be set to this value. This value is currently ignored when cloning; the setting of the remote repository is used instead. The default is &quot;sha1&quot;. THIS VARIABLE IS EXPERIMENTAL! See <code>&#8211;object-format</code> in <code><a href="/docs/linux/man/1-git-init/">git-init</a></code>(1).</dl>
<h3>Git Commits</h3>
<p> <code>GIT_AUTHOR_NAME</code></p>
<dl>
<dt>
<dd> The human-readable name used in the author identity when creating commit or tag objects, or when writing reflogs. Overrides the <code>user.name</code> and <code>author.name</code> configuration settings.</dl>
<p> <code>GIT_AUTHOR_EMAIL</code></p>
<dl>
<dt>
<dd> The email address used in the author identity when creating commit or tag objects, or when writing reflogs. Overrides the <code>user.email</code> and <code>author.email</code> configuration settings.</dl>
<p> <code>GIT_AUTHOR_DATE</code></p>
<dl>
<dt>
<dd> The date used for the author identity when creating commit or tag objects, or when writing reflogs. See <code><a href="/docs/linux/man/1-git-commit/">git-commit</a></code>(1) for valid formats.</dl>
<p> <code>GIT_COMMITTER_NAME</code></p>
<dl>
<dt>
<dd> The human-readable name used in the committer identity when creating commit or tag objects, or when writing reflogs. Overrides the <code>user.name</code> and <code>committer.name</code> configuration settings.</dl>
<p> <code>GIT_COMMITTER_EMAIL</code></p>
<dl>
<dt>
<dd> The email address used in the author identity when creating commit or tag objects, or when writing reflogs. Overrides the <code>user.email</code> and <code>committer.email</code> configuration settings.</dl>
<p> <code>GIT_COMMITTER_DATE</code></p>
<dl>
<dt>
<dd> The date used for the committer identity when creating commit or tag objects, or when writing reflogs. See <code><a href="/docs/linux/man/1-git-commit/">git-commit</a></code>(1) for valid formats.</dl>
<p> <code>EMAIL</code></p>
<dl>
<dt>
<dd> The email address used in the author and committer identities if no other relevant environment variable or configuration setting has been set.</dl>
<h3>Git Diffs</h3>
<p> <code>GIT_DIFF_OPTS</code></p>
<dl>
<dt>
<dd> Only valid setting is &quot;&#8211;unified=??&quot; or &quot;-u??&quot; to set the number of context lines shown when a unified diff is created. This takes precedence over any &quot;-U&quot; or &quot;&#8211;unified&quot; option value passed on the Git diff command line.</dl>
<p> <code>GIT_EXTERNAL_DIFF</code></p>
<dl>
<dt>
<dd> When the environment variable <code>GIT_EXTERNAL_DIFF</code> is set, the program named by it is called to generate diffs, and Git does not use its builtin diff machinery. For a path that is added, removed, or modified, <code>GIT_EXTERNAL_DIFF</code> is called with 7 parameters: </p>
<dl>
<dt>
<dd>
<pre>
path old-file old-hex old-mode new-file new-hex new-mode
</pre>
</dl>
<p> where:</dl>
<p> &lt;old|new&gt;-file</p>
<dl>
<dt>
<dd> are files GIT_EXTERNAL_DIFF can use to read the contents of &lt;old|new&gt;,</dl>
<p> &lt;old|new&gt;-hex</p>
<dl>
<dt>
<dd> are the 40-hexdigit SHA-1 hashes,</dl>
<p> &lt;old|new&gt;-mode</p>
<dl>
<dt>
<dd> are the octal representation of the file modes. </p>
<p> The file parameters can point at the user&#8217;s working file (e.g. <code>new-file</code> in &quot;git-diff-files&quot;), <code>/dev/null</code> (e.g. <code>old-file</code> when a new file is added), or a temporary file (e.g. <code>old-file</code> in the index). <code>GIT_EXTERNAL_DIFF</code> should not worry about unlinking the temporary file &#8212; it is removed when <code>GIT_EXTERNAL_DIFF</code> exits. </p>
<p> For a path that is unmerged, <code>GIT_EXTERNAL_DIFF</code> is called with 1 parameter, &lt;path&gt;. </p>
<p> For each path <code>GIT_EXTERNAL_DIFF</code> is called, two environment variables, <code>GIT_DIFF_PATH_COUNTER</code> and <code>GIT_DIFF_PATH_TOTAL</code> are set.</dl>
<p> <code>GIT_DIFF_PATH_COUNTER</code></p>
<dl>
<dt>
<dd> A 1-based counter incremented by one for every path.</dl>
<p> <code>GIT_DIFF_PATH_TOTAL</code></p>
<dl>
<dt>
<dd> The total number of paths.</dl>
<h3>other</h3>
<p> <code>GIT_MERGE_VERBOSITY</code></p>
<dl>
<dt>
<dd> A number controlling the amount of output shown by the recursive merge strategy. Overrides merge.verbosity. See <code><a href="/docs/linux/man/1-git-merge/">git-merge</a></code>(1)</dl>
<p> <code>GIT_PAGER</code></p>
<dl>
<dt>
<dd> This environment variable overrides <code>$PAGER</code>. If it is set to an empty string or to the value &quot;cat&quot;, Git will not launch a pager. See also the <code>core.pager</code> option in <code><a href="/docs/linux/man/1-git-config/">git-config</a></code>(1).</dl>
<p> <code>GIT_PROGRESS_DELAY</code></p>
<dl>
<dt>
<dd> A number controlling how many seconds to delay before showing optional progress indicators. Defaults to 2.</dl>
<p> <code>GIT_EDITOR</code></p>
<dl>
<dt>
<dd> This environment variable overrides <code>$EDITOR</code> and <code>$VISUAL</code>. It is used by several Git commands when, on interactive mode, an editor is to be launched. See also <code><a href="/docs/linux/man/1-git-var/">git-var</a></code>(1) and the <code>core.editor</code> option in <code><a href="/docs/linux/man/1-git-config/">git-config</a></code>(1).</dl>
<p> <code>GIT_SEQUENCE_EDITOR</code></p>
<dl>
<dt>
<dd> This environment variable overrides the configured Git editor when editing the todo list of an interactive rebase. See also <code><a href="/docs/linux/man/1-git-rebase/">git-rebase</a></code>(1) and the <code>sequence.editor</code> option in <code><a href="/docs/linux/man/1-git-config/">git-config</a></code>(1).</dl>
<p> <code>GIT_SSH</code>, <code>GIT_SSH_COMMAND</code></p>
<dl>
<dt>
<dd> If either of these environment variables is set then <i>git fetch</i> and <i>git push</i> will use the specified command instead of <i>ssh</i> when they need to connect to a remote system. The command-line parameters passed to the configured command are determined by the ssh variant. See <code>ssh.variant</code> option in <code><a href="/docs/linux/man/1-git-config/">git-config</a></code>(1) for details. </p>
<p> <code>$GIT_SSH_COMMAND</code> takes precedence over <code>$GIT_SSH</code>, and is interpreted by the shell, which allows additional arguments to be included. <code>$GIT_SSH</code> on the other hand must be just the path to a program (which can be a wrapper shell script, if additional arguments are needed). </p>
<p> Usually it is easier to configure any desired options through your personal <code>.ssh/config</code> file. Please consult your ssh documentation for further details.</dl>
<p> <code>GIT_SSH_VARIANT</code></p>
<dl>
<dt>
<dd> If this environment variable is set, it overrides Git&#8217;s autodetection whether <code>GIT_SSH</code>/<code>GIT_SSH_COMMAND</code>/<code>core.sshCommand</code> refer to OpenSSH, plink or tortoiseplink. This variable overrides the config setting <code>ssh.variant</code> that serves the same purpose.</dl>
<p> <code>GIT_ASKPASS</code></p>
<dl>
<dt>
<dd> If this environment variable is set, then Git commands which need to acquire passwords or passphrases (e.g. for HTTP or IMAP authentication) will call this program with a suitable prompt as command-line argument and read the password from its STDOUT. See also the <code>core.askPass</code> option in <code><a href="/docs/linux/man/1-git-config/">git-config</a></code>(1).</dl>
<p> <code>GIT_TERMINAL_PROMPT</code></p>
<dl>
<dt>
<dd> If this environment variable is set to <code>0</code>, git will not prompt on the terminal (e.g., when asking for HTTP authentication).</dl>
<p> <code>GIT_CONFIG_GLOBAL</code>, <code>GIT_CONFIG_SYSTEM</code></p>
<dl>
<dt>
<dd> Take the configuration from the given files instead from global or system-level configuration files. If <code>GIT_CONFIG_SYSTEM</code> is set, the system config file defined at build time (usually <code>/etc/gitconfig</code>) will not be read. Likewise, if <code>GIT_CONFIG_GLOBAL</code> is set, neither <code>$HOME/.gitconfig</code> nor <code>$XDG_CONFIG_HOME/git/config</code> will be read. Can be set to <code>/dev/null</code> to skip reading configuration files of the respective level.</dl>
<p> <code>GIT_CONFIG_NOSYSTEM</code></p>
<dl>
<dt>
<dd> Whether to skip reading settings from the system-wide <code>$(prefix)/etc/gitconfig</code> file. This environment variable can be used along with <code>$HOME</code> and <code>$XDG_CONFIG_HOME</code> to create a predictable environment for a picky script, or you can set it temporarily to avoid using a buggy <code>/etc/gitconfig</code> file while waiting for someone with sufficient permissions to fix it.</dl>
<p> <code>GIT_FLUSH</code></p>
<dl>
<dt>
<dd> If this environment variable is set to &quot;1&quot;, then commands such as <i>git blame</i> (in incremental mode), <i>git rev-list</i>, <i>git log</i>, <i>git check-attr</i> and <i>git check-ignore</i> will force a flush of the output stream after each record have been flushed. If this variable is set to &quot;0&quot;, the output of these commands will be done using completely buffered I/O. If this environment variable is not set, Git will choose buffered or record-oriented flushing based on whether stdout appears to be redirected to a file or not.</dl>
<p> <code>GIT_TRACE</code></p>
<dl>
<dt>
<dd> Enables general trace messages, e.g. alias expansion, built-in command execution and external command execution. </p>
<p> If this variable is set to &quot;1&quot;, &quot;2&quot; or &quot;true&quot; (comparison is case insensitive), trace messages will be printed to stderr. </p>
<p> If the variable is set to an integer value greater than 2 and lower than 10 (strictly) then Git will interpret this value as an open file descriptor and will try to write the trace messages into this file descriptor. </p>
<p> Alternatively, if the variable is set to an absolute path (starting with a <i>/</i> character), Git will interpret this as a file path and will try to append the trace messages to it. </p>
<p> Unsetting the variable, or setting it to empty, &quot;0&quot; or &quot;false&quot; (case insensitive) disables trace messages.</dl>
<p> <code>GIT_TRACE_FSMONITOR</code></p>
<dl>
<dt>
<dd> Enables trace messages for the filesystem monitor extension. See <code>GIT_TRACE</code> for available trace output options.</dl>
<p> <code>GIT_TRACE_PACK_ACCESS</code></p>
<dl>
<dt>
<dd> Enables trace messages for all accesses to any packs. For each access, the pack file name and an offset in the pack is recorded. This may be helpful for troubleshooting some pack-related performance problems. See <code>GIT_TRACE</code> for available trace output options.</dl>
<p> <code>GIT_TRACE_PACKET</code></p>
<dl>
<dt>
<dd> Enables trace messages for all packets coming in or out of a given program. This can help with debugging object negotiation or other protocol issues. Tracing is turned off at a packet starting with &quot;PACK&quot; (but see <code>GIT_TRACE_PACKFILE</code> below). See <code>GIT_TRACE</code> for available trace output options.</dl>
<p> <code>GIT_TRACE_PACKFILE</code></p>
<dl>
<dt>
<dd> Enables tracing of packfiles sent or received by a given program. Unlike other trace output, this trace is verbatim: no headers, and no quoting of binary data. You almost certainly want to direct into a file (e.g., <code>GIT_TRACE_PACKFILE=/tmp/my.pack</code>) rather than displaying it on the terminal or mixing it with other trace output. </p>
<p> Note that this is currently only implemented for the client side of clones and fetches.</dl>
<p> <code>GIT_TRACE_PERFORMANCE</code></p>
<dl>
<dt>
<dd> Enables performance related trace messages, e.g. total execution time of each Git command. See <code>GIT_TRACE</code> for available trace output options.</dl>
<p> <code>GIT_TRACE_REFS</code></p>
<dl>
<dt>
<dd> Enables trace messages for operations on the ref database. See <code>GIT_TRACE</code> for available trace output options.</dl>
<p> <code>GIT_TRACE_SETUP</code></p>
<dl>
<dt>
<dd> Enables trace messages printing the .git, working tree and current working directory after Git has completed its setup phase. See <code>GIT_TRACE</code> for available trace output options.</dl>
<p> <code>GIT_TRACE_SHALLOW</code></p>
<dl>
<dt>
<dd> Enables trace messages that can help debugging fetching / cloning of shallow repositories. See <code>GIT_TRACE</code> for available trace output options.</dl>
<p> <code>GIT_TRACE_CURL</code></p>
<dl>
<dt>
<dd> Enables a curl full trace dump of all incoming and outgoing data, including descriptive information, of the git transport protocol. This is similar to doing curl <code>&#8211;trace-ascii</code> on the command line. See <code>GIT_TRACE</code> for available trace output options.</dl>
<p> <code>GIT_TRACE_CURL_NO_DATA</code></p>
<dl>
<dt>
<dd> When a curl trace is enabled (see <code>GIT_TRACE_CURL</code> above), do not dump data (that is, only dump info lines and headers).</dl>
<p> <code>GIT_TRACE2</code></p>
<dl>
<dt>
<dd> Enables more detailed trace messages from the &quot;trace2&quot; library. Output from <code>GIT_TRACE2</code> is a simple text-based format for human readability. </p>
<p> If this variable is set to &quot;1&quot;, &quot;2&quot; or &quot;true&quot; (comparison is case insensitive), trace messages will be printed to stderr. </p>
<p> If the variable is set to an integer value greater than 2 and lower than 10 (strictly) then Git will interpret this value as an open file descriptor and will try to write the trace messages into this file descriptor. </p>
<p> Alternatively, if the variable is set to an absolute path (starting with a <i>/</i> character), Git will interpret this as a file path and will try to append the trace messages to it. If the path already exists and is a directory, the trace messages will be written to files (one per process) in that directory, named according to the last component of the SID and an optional counter (to avoid filename collisions). </p>
<p> In addition, if the variable is set to <code>af_unix:[&lt;socket_type&gt;:]&lt;absolute-pathname&gt;</code>, Git will try to open the path as a Unix Domain Socket. The socket type can be either <code>stream</code> or <code>dgram</code>. </p>
<p> Unsetting the variable, or setting it to empty, &quot;0&quot; or &quot;false&quot; (case insensitive) disables trace messages. </p>
<p> See m[blue]<code>Trace2 documentation</code>m[]<font SIZE="-2">[2]</font> for full details.</dl>
<p> <code>GIT_TRACE2_EVENT</code></p>
<dl>
<dt>
<dd> This setting writes a JSON-based format that is suited for machine interpretation. See <code>GIT_TRACE2</code> for available trace output options and m[blue]<code>Trace2 documentation</code>m[]<font SIZE="-2">[2]</font> for full details.</dl>
<p> <code>GIT_TRACE2_PERF</code></p>
<dl>
<dt>
<dd> In addition to the text-based messages available in <code>GIT_TRACE2</code>, this setting writes a column-based format for understanding nesting regions. See <code>GIT_TRACE2</code> for available trace output options and m[blue]<code>Trace2 documentation</code>m[]<font SIZE="-2">[2]</font> for full details.</dl>
<p> <code>GIT_TRACE_REDACT</code></p>
<dl>
<dt>
<dd> By default, when tracing is activated, Git redacts the values of cookies, the &quot;Authorization:&quot; header, and the &quot;Proxy-Authorization:&quot; header. Set this variable to <code>0</code> to prevent this redaction.</dl>
<p> <code>GIT_LITERAL_PATHSPECS</code></p>
<dl>
<dt>
<dd> Setting this variable to <code>1</code> will cause Git to treat all pathspecs literally, rather than as glob patterns. For example, running <code>GIT_LITERAL_PATHSPECS=1 git log &#8212; &#8216;*.c&#8217;</code> will search for commits that touch the path <code>*.c</code>, not any paths that the glob <code>*.c</code> matches. You might want this if you are feeding literal paths to Git (e.g., paths previously given to you by <code>git ls-tree</code>, <code>&#8211;raw</code> diff output, etc).</dl>
<p> <code>GIT_GLOB_PATHSPECS</code></p>
<dl>
<dt>
<dd> Setting this variable to <code>1</code> will cause Git to treat all pathspecs as glob patterns (aka &quot;glob&quot; magic).</dl>
<p> <code>GIT_NOGLOB_PATHSPECS</code></p>
<dl>
<dt>
<dd> Setting this variable to <code>1</code> will cause Git to treat all pathspecs as literal (aka &quot;literal&quot; magic).</dl>
<p> <code>GIT_ICASE_PATHSPECS</code></p>
<dl>
<dt>
<dd> Setting this variable to <code>1</code> will cause Git to treat all pathspecs as case-insensitive.</dl>
<p> <code>GIT_REFLOG_ACTION</code></p>
<dl>
<dt>
<dd> When a ref is updated, reflog entries are created to keep track of the reason why the ref was updated (which is typically the name of the high-level command that updated the ref), in addition to the old and new values of the ref. A scripted Porcelain command can use set_reflog_action helper function in <code>git-sh-setup</code> to set its name to this variable when it is invoked as the top level command by the end user, to be recorded in the body of the reflog.</dl>
<p> <code>GIT_REF_PARANOIA</code></p>
<dl>
<dt>
<dd> If set to <code>0</code>, ignore broken or badly named refs when iterating over lists of refs. Normally Git will try to include any such refs, which may cause some operations to fail. This is usually preferable, as potentially destructive operations (e.g., <code><a href="/docs/linux/man/1-git-prune/">git-prune</a></code>(1)) are better off aborting rather than ignoring broken refs (and thus considering the history they point to as not worth saving). The default value is <code>1</code> (i.e., be paranoid about detecting and aborting all operations). You should not normally need to set this to <code>0</code>, but it may be useful when trying to salvage data from a corrupted repository.</dl>
<p> <code>GIT_ALLOW_PROTOCOL</code></p>
<dl>
<dt>
<dd> If set to a colon-separated list of protocols, behave as if <code>protocol.allow</code> is set to <code>never</code>, and each of the listed protocols has <code>protocol.&lt;name&gt;.allow</code> set to <code>always</code> (overriding any existing configuration). In other words, any protocol not mentioned will be disallowed (i.e., this is a whitelist, not a blacklist). See the description of <code>protocol.allow</code> in <code><a href="/docs/linux/man/1-git-config/">git-config</a></code>(1) for more details.</dl>
<p> <code>GIT_PROTOCOL_FROM_USER</code></p>
<dl>
<dt>
<dd> Set to 0 to prevent protocols used by fetch/push/clone which are configured to the <code>user</code> state. This is useful to restrict recursive submodule initialization from an untrusted repository or for programs which feed potentially-untrusted URLS to git commands. See <code><a href="/docs/linux/man/1-git-config/">git-config</a></code>(1) for more details.</dl>
<p> <code>GIT_PROTOCOL</code></p>
<dl>
<dt>
<dd> For internal use only. Used in handshaking the wire protocol. Contains a colon <i>:</i> separated list of keys with optional values <i>key[=value]</i>. Presence of unknown keys and values must be ignored. </p>
<p> Note that servers may need to be configured to allow this variable to pass over some transports. It will be propagated automatically when accessing local repositories (i.e., <code>file://</code> or a filesystem path), as well as over the <code>git://</code> protocol. For git-over-http, it should work automatically in most configurations, but see the discussion in <code><a href="/docs/linux/man/1-git-http-backend/">git-http-backend</a></code>(1). For git-over-ssh, the ssh server may need to be configured to allow clients to pass this variable (e.g., by using <code>AcceptEnv GIT_PROTOCOL</code> with OpenSSH). </p>
<p> This configuration is optional. If the variable is not propagated, then clients will fall back to the original &quot;v0&quot; protocol (but may miss out on some performance improvements or features). This variable currently only affects clones and fetches; it is not yet used for pushes (but may be in the future).</dl>
<p> <code>GIT_OPTIONAL_LOCKS</code></p>
<dl>
<dt>
<dd> If set to <code>0</code>, Git will complete any requested operation without performing any optional sub-operations that require taking a lock. For example, this will prevent <code>git status</code> from refreshing the index as a side effect. This is useful for processes running in the background which do not want to cause lock contention with other operations on the repository. Defaults to <code>1</code>.</dl>
<p> <code>GIT_REDIRECT_STDIN</code>, <code>GIT_REDIRECT_STDOUT</code>, <code>GIT_REDIRECT_STDERR</code></p>
<dl>
<dt>
<dd> Windows-only: allow redirecting the standard input/output/error handles to paths specified by the environment variables. This is particularly useful in multi-threaded applications where the canonical way to pass standard handles via <code>CreateProcess()</code> is not an option because it would require the handles to be marked inheritable (and consequently <code>every</code> spawned process would inherit them, possibly blocking regular Git operations). The primary intended use case is to use named pipes for communication (e.g. <code>\.\pipe\my-git-stdin-123</code>). </p>
<p> Two special values are supported: <code>off</code> will simply close the corresponding standard handle, and if <code>GIT_REDIRECT_STDERR</code> is <code>2&gt;&amp;1</code>, standard error will be redirected to the same handle as standard output.</dl>
<p> <code>GIT_PRINT_SHA1_ELLIPSIS</code> (deprecated)</p>
<dl>
<dt>
<dd> If set to <code>yes</code>, print an ellipsis following an (abbreviated) SHA-1 value. This affects indications of detached HEADs (<code><a href="/docs/linux/man/1-git-checkout/">git-checkout</a></code>(1)) and the raw diff output (<code><a href="/docs/linux/man/1-git-diff/">git-diff</a></code>(1)). Printing an ellipsis in the cases mentioned is no longer considered adequate and support for it is likely to be removed in the foreseeable future (along with the variable).</dl>
<h2>DISCUSSION</h2>
<p> More detail on the following is available from the m[blue]<code>Git concepts chapter of the user-manual</code>m[]<font SIZE="-2">[3]</font> and <code><a href="/docs/linux/man/7-gitcore-tutorial/">gitcore-tutorial</a></code>(7). </p>
<p> A Git project normally consists of a working directory with a &quot;.git&quot; subdirectory at the top level. The .git directory contains, among other things, a compressed object database representing the complete history of the project, an &quot;index&quot; file which links that history to the current contents of the working tree, and named pointers into that history such as tags and branch heads. </p>
<p> The object database contains objects of three main types: blobs, which hold file data; trees, which point to blobs and other trees to build up directory hierarchies; and commits, which each reference a single tree and some number of parent commits. </p>
<p> The commit, equivalent to what other systems call a &quot;changeset&quot; or &quot;version&quot;, represents a step in the project&#8217;s history, and each parent represents an immediately preceding step. Commits with more than one parent represent merges of independent lines of development. </p>
<p> All objects are named by the SHA-1 hash of their contents, normally written as a string of 40 hex digits. Such names are globally unique. The entire history leading up to a commit can be vouched for by signing just that commit. A fourth object type, the tag, is provided for this purpose. </p>
<p> When first created, objects are stored in individual files, but for efficiency may later be compressed together into &quot;pack files&quot;. </p>
<p> Named pointers called refs mark interesting points in history. A ref may contain the SHA-1 name of an object or the name of another ref. Refs with names beginning <code>ref/head/</code> contain the SHA-1 name of the most recent commit (or &quot;head&quot;) of a branch under development. SHA-1 names of tags of interest are stored under <code>ref/tags/</code>. A special ref named <code>HEAD</code> contains the name of the currently checked-out branch. </p>
<p> The index file is initialized with a list of all paths and, for each path, a blob object and a set of attributes. The blob object represents the contents of the file as of the head of the current branch. The attributes (last modified time, size, etc.) are taken from the corresponding file in the working tree. Subsequent changes to the working tree can be found by comparing these attributes. The index may be updated with new content, and new commits may be created from the content stored in the index. </p>
<p> The index is also capable of storing multiple entries (called &quot;stages&quot;) for a given pathname. These stages are used to hold the various unmerged version of a file when a merge is in progress.</p>
<h2>FURTHER DOCUMENTATION</h2>
<p> See the references in the &quot;description&quot; section to get started using Git. The following is probably more detail than necessary for a first-time user. </p>
<p> The m[blue]<code>Git concepts chapter of the user-manual</code>m[]<font SIZE="-2">[3]</font> and <code><a href="/docs/linux/man/7-gitcore-tutorial/">gitcore-tutorial</a></code>(7) both provide introductions to the underlying Git architecture. </p>
<p> See <code><a href="/docs/linux/man/7-gitworkflows/">gitworkflows</a></code>(7) for an overview of recommended workflows. </p>
<p> See also the m[blue]<code>howto</code>m[]<font SIZE="-2">[4]</font> documents for some useful examples. </p>
<p> The internals are documented in the m[blue]<code>Git API documentation</code>m[]<font SIZE="-2">[5]</font>. </p>
<p> Users migrating from CVS may also want to read <code><a href="/docs/linux/man/7-gitcvs-migration/">gitcvs-migration</a></code>(7).</p>
<h2>AUTHORS</h2>
<p> Git was started by Linus Torvalds, and is currently maintained by Junio C Hamano. Numerous contributions have come from the Git mailing list &lt;m[blue]<code>git [at] vger.kernel.org</code>m[]<font SIZE="-2">[6]</font>&gt;. m[blue]<code><a rel="nofollow" href="http://www.openhub.net/p/git/contributors/summary">http://www.openhub.net/p/git/contributors/summary</a></code>m[] gives you a more complete list of contributors. </p>
<p> If you have a clone of git.git itself, the output of <code><a href="/docs/linux/man/1-git-shortlog/">git-shortlog</a></code>(1) and <code><a href="/docs/linux/man/1-git-blame/">git-blame</a></code>(1) can show you the authors for specific parts of the project.</p>
<h2>REPORTING BUGS</h2>
<p> Report bugs to the Git mailing list &lt;m[blue]<code>git [at] vger.kernel.org</code>m[]<font SIZE="-2">[6]</font>&gt; where the development and maintenance is primarily done. You do not have to be subscribed to the list to send a message there. See the list archive at m[blue]<code><a rel="nofollow" href="https://lore.kernel.org/git">https://lore.kernel.org/git</a></code>m[] for previous bug reports and other discussions. </p>
<p> Issues which are security relevant should be disclosed privately to the Git Security mailing list &lt;m[blue]<code>git-security [at] googlegroups.com</code>m[]<font SIZE="-2">[7]</font>&gt;.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/7-gittutorial/">gittutorial</a></code>(7), <code><a href="/docs/linux/man/7-gittutorial-2/">gittutorial-2</a></code>(7), <code><a href="/docs/linux/man/7-giteveryday/">giteveryday</a></code>(7), <code><a href="/docs/linux/man/7-gitcvs-migration/">gitcvs-migration</a></code>(7), <code><a href="/docs/linux/man/7-gitglossary/">gitglossary</a></code>(7), <code><a href="/docs/linux/man/7-gitcore-tutorial/">gitcore-tutorial</a></code>(7), <code><a href="/docs/linux/man/7-gitcli/">gitcli</a></code>(7), m[blue]<code>The Git User&#8217;s Manual</code>m[]<font SIZE="-2">[1]</font>, <code><a href="/docs/linux/man/7-gitworkflows/">gitworkflows</a></code>(7)</p>
<h2>GIT</h2>
<p> Part of the <code><a href="/docs/linux/man/1-git/">git</a></code>(1) suite</p>
<h2>NOTES</h2>
<dl>
<dt> 1.</p>
<dd> Git User&#8217;s Manual</p>
<dl>
<dt>
<dd> file:///usr/share/doc/git/html/user-manual.html</dl>
<dt> 2.</p>
<dd> Trace2 documentation</p>
<dl>
<dt>
<dd> file:///usr/share/doc/git/html/technical/api-trace2.html</dl>
<dt> 3.</p>
<dd> Git concepts chapter of the user-manual</p>
<dl>
<dt>
<dd> file:///usr/share/doc/git/html/user-manual.html#git-concepts</dl>
<dt> 4.</p>
<dd> howto</p>
<dl>
<dt>
<dd> file:///usr/share/doc/git/html/howto-index.html</dl>
<dt> 5.</p>
<dd> Git API documentation</p>
<dl>
<dt>
<dd> file:///usr/share/doc/git/html/technical/api-index.html</dl>
<dt> 6.</p>
<dd> git [at] vger.kernel.org</p>
<dl>
<dt>
<dd> mailto:git [at] vger.kernel.org</dl>
<dt> 7.</p>
<dd> git-security [at] googlegroups.com</p>
<dl>
<dt>
<dd> mailto:git-security [at] googlegroups.com</dl>
</dl>
<h2>Index</h2>
