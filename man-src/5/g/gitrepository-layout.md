---
title: "gitrepository-layout(5)"
name: "gitrepository-layout"
section: "5"
letter: "g"
url: "/docs/linux/man/5-gitrepository-layout/"
description: "gitrepository-layout – Git Repository Layout"
---

<p>gitrepository-layout &#8211; Git Repository Layout</p>
<h2>Synopsis</h2>
<p>$GIT_DIR/*</p>
<h2>Description</h2>
<p>A Git repository comes in two different flavours: </p>
<dl>
<dd>&bull; a <code>.git</code> directory at the root of the working tree;</dl>
<dl>
<dd>&bull; a <code>&lt;project&gt;.git</code> directory that is a <i>bare</i> repository (i.e. without its own working tree), that is typically used for exchanging histories with others by pushing into it and fetching from it.</dl>
<p> <code>Note</code>: Also you can have a plain text file <code>.git</code> at the root of your working tree, containing <code>gitdir: &lt;path&gt;</code> to point at the real directory that has the repository. This mechanism is often used for a working tree of a submodule checkout, to allow you in the containing superproject to <code>git checkout</code> a branch that does not have the submodule. The <code>checkout</code> has to remove the entire submodule working tree, without losing the submodule repository. </p>
<p> These things may exist in a Git repository. </p>
<p> objects</p>
<dl>
<dd>Object store associated with this repository. Usually an object store is self sufficient (i.e. all the objects that are referred to by an object found in it are also found in it), but there are a few ways to violate it. </p>
<dl>
<dd>1. You could have an incomplete but locally usable repository by creating a shallow clone. See <code><a href="/docs/linux/man/1-git-clone/">git-clone</a></code>(1).</dl>
<dl>
<dd>2. You could be using the <code>objects/info/alternates</code> or <code>$GIT_ALTERNATE_OBJECT_DIRECTORIES</code> mechanisms to <i>borrow</i> objects from other object stores. A repository with this kind of incomplete object store is not suitable to be published for use with dumb transports but otherwise is OK as long as <code>objects/info/alternates</code> points at the object stores it borrows from. </p>
<p> This directory is ignored if $GIT_COMMON_DIR is set and &quot;$GIT_COMMON_DIR/objects&quot; will be used instead.</dl>
</dl>
<p> objects/[0-9a-f][0-9a-f]</p>
<dl>
<dd>A newly created object is stored in its own file. The objects are splayed over 256 subdirectories using the first two characters of the sha1 object name to keep the number of directory entries in <code>objects</code> itself to a manageable number. Objects found here are often called <i>unpacked</i> (or <i>loose</i>) objects.</dl>
<p> objects/pack</p>
<dl>
<dd>Packs (files that store many objects in compressed form, along with index files to allow them to be randomly accessed) are found in this directory.</dl>
<p> objects/info</p>
<dl>
<dd>Additional information about the object store is recorded in this directory.</dl>
<p> objects/info/packs</p>
<dl>
<dd>This file is to help dumb transports discover what packs are available in this object store. Whenever a pack is added or removed, <code>git update-server-info</code> should be run to keep this file up to date if the repository is published for dumb transports. <i>git repack</i> does this by default.</dl>
<p> objects/info/alternates</p>
<dl>
<dd>This file records paths to alternate object stores that this object store borrows objects from, one pathname per line. Note that not only native Git tools use it locally, but the HTTP fetcher also tries to use it remotely; this will usually work if you have relative paths (relative to the object database, not to the repository!) in your alternates file, but it will not work if you use absolute paths unless the absolute path in filesystem and web URL is the same. See also <code>objects/info/http-alternates</code>.</dl>
<p> objects/info/http-alternates</p>
<dl>
<dd>This file records URLs to alternate object stores that this object store borrows objects from, to be used when the repository is fetched over HTTP.</dl>
<p> refs</p>
<dl>
<dd>References are stored in subdirectories of this directory. The <i>git prune</i> command knows to preserve objects reachable from refs found in this directory and its subdirectories. This directory is ignored (except refs/bisect, refs/rewritten and refs/worktree) if $GIT_COMMON_DIR is set and &quot;$GIT_COMMON_DIR/refs&quot; will be used instead.</dl>
<p> refs/heads/<code>name</code></p>
<dl>
<dd>records tip-of-the-tree commit objects of branch <code>name</code></dl>
<p> refs/tags/<code>name</code></p>
<dl>
<dd>records any object name (not necessarily a commit object, or a tag object that points at a commit object).</dl>
<p> refs/remotes/<code>name</code></p>
<dl>
<dd>records tip-of-the-tree commit objects of branches copied from a remote repository.</dl>
<p> refs/replace/<code>&lt;obj-sha1&gt;</code></p>
<dl>
<dd>records the SHA-1 of the object that replaces <code>&lt;obj-sha1&gt;</code>. This is similar to info/grafts and is internally used and maintained by <code><a href="/docs/linux/man/1-git-replace/">git-replace</a></code>(1). Such refs can be exchanged between repositories while grafts are not.</dl>
<p> packed-refs</p>
<dl>
<dd>records the same information as refs/heads/, refs/tags/, and friends record in a more efficient way. See <code><a href="/docs/linux/man/1-git-pack-refs/">git-pack-refs</a></code>(1). This file is ignored if $GIT_COMMON_DIR is set and &quot;$GIT_COMMON_DIR/packed-refs&quot; will be used instead.</dl>
<p> HEAD</p>
<dl>
<dd>A symref (see glossary) to the <code>refs/heads/</code> namespace describing the currently active branch. It does not mean much if the repository is not associated with any working tree (i.e. a <i>bare</i> repository), but a valid Git repository <code>must</code> have the HEAD file; some porcelains may use it to guess the designated &quot;default&quot; branch of the repository (usually <i>master</i>). It is legal if the named branch <i>name</i> does not (yet) exist. In some legacy setups, it is a symbolic link instead of a symref that points at the current branch. </p>
<p> HEAD can also record a specific commit directly, instead of being a symref to point at the current branch. Such a state is often called <i>detached HEAD.</i> See <code><a href="/docs/linux/man/1-git-checkout/">git-checkout</a></code>(1) for details.</dl>
<p> config</p>
<dl>
<dd>Repository specific configuration file. This file is ignored if $GIT_COMMON_DIR is set and &quot;$GIT_COMMON_DIR/config&quot; will be used instead.</dl>
<p> config.worktree</p>
<dl>
<dd>Working directory specific configuration file for the main working directory in multiple working directory setup (see <code><a href="/docs/linux/man/1-git-worktree/">git-worktree</a></code>(1)).</dl>
<p> branches</p>
<dl>
<dd>A slightly deprecated way to store shorthands to be used to specify a URL to <i>git fetch</i>, <i>git pull</i> and <i>git push</i>. A file can be stored as <code>branches/&lt;name&gt;</code> and then <i>name</i> can be given to these commands in place of <i>repository</i> argument. See the REMOTES section in <code><a href="/docs/linux/man/1-git-fetch/">git-fetch</a></code>(1) for details. This mechanism is legacy and not likely to be found in modern repositories. This directory is ignored if $GIT_COMMON_DIR is set and &quot;$GIT_COMMON_DIR/branches&quot; will be used instead.</dl>
<p> hooks</p>
<dl>
<dd>Hooks are customization scripts used by various Git commands. A handful of sample hooks are installed when <i>git init</i> is run, but all of them are disabled by default. To enable, the <code>.sample</code> suffix has to be removed from the filename by renaming. Read <code><a href="/docs/linux/man/5-githooks/">githooks</a></code>(5) for more details about each hook. This directory is ignored if $GIT_COMMON_DIR is set and &quot;$GIT_COMMON_DIR/hooks&quot; will be used instead.</dl>
<p> common</p>
<dl>
<dd>When multiple working trees are used, most of files in $GIT_DIR are per-worktree with a few known exceptions. All files under <i>common</i> however will be shared between all working trees.</dl>
<p> index</p>
<dl>
<dd>The current index file for the repository. It is usually not found in a bare repository.</dl>
<p> sharedindex.&lt;SHA-1&gt;</p>
<dl>
<dd>The shared index part, to be referenced by $GIT_DIR/index and other temporary index files. Only valid in split index mode.</dl>
<p> info</p>
<dl>
<dd>Additional information about the repository is recorded in this directory. This directory is ignored if $GIT_COMMON_DIR is set and &quot;$GIT_COMMON_DIR/info&quot; will be used instead.</dl>
<p> info/refs</p>
<dl>
<dd>This file helps dumb transports discover what refs are available in this repository. If the repository is published for dumb transports, this file should be regenerated by <i>git update-server-info</i> every time a tag or branch is created or modified. This is normally done from the <code>hooks/update</code> hook, which is run by the <i>git-receive-pack</i> command when you <i>git push</i> into the repository.</dl>
<p> info/grafts</p>
<dl>
<dd>This file records fake commit ancestry information, to pretend the set of parents a commit has is different from how the commit was actually created. One record per line describes a commit and its fake parents by listing their 40-byte hexadecimal object names separated by a space and terminated by a newline. </p>
<p> Note that the grafts mechanism is outdated and can lead to problems transferring objects between repositories; see <code><a href="/docs/linux/man/1-git-replace/">git-replace</a></code>(1) for a more flexible and robust system to do the same thing.</dl>
<p> info/exclude</p>
<dl>
<dd>This file, by convention among Porcelains, stores the exclude pattern list. <code>.gitignore</code> is the per-directory ignore file. <i>git status</i>, <i>git add</i>, <i>git rm</i> and <i>git clean</i> look at it but the core Git commands do not look at it. See also: <code><a href="/docs/linux/man/5-gitignore/">gitignore</a></code>(5).</dl>
<p> info/attributes</p>
<dl>
<dd>Defines which attributes to assign to a path, similar to per-directory <code>.gitattributes</code> files. See also: <code><a href="/docs/linux/man/5-gitattributes/">gitattributes</a></code>(5).</dl>
<p> info/sparse-checkout</p>
<dl>
<dd>This file stores sparse checkout patterns. See also: <code><a href="/docs/linux/man/1-git-read-tree/">git-read-tree</a></code>(1).</dl>
<p> remotes</p>
<dl>
<dd>Stores shorthands for URL and default refnames for use when interacting with remote repositories via <i>git fetch</i>, <i>git pull</i> and <i>git push</i> commands. See the REMOTES section in <code><a href="/docs/linux/man/1-git-fetch/">git-fetch</a></code>(1) for details. This mechanism is legacy and not likely to be found in modern repositories. This directory is ignored if $GIT_COMMON_DIR is set and &quot;$GIT_COMMON_DIR/remotes&quot; will be used instead.</dl>
<p> logs</p>
<dl>
<dd>Records of changes made to refs are stored in this directory. See <code><a href="/docs/linux/man/1-git-update-ref/">git-update-ref</a></code>(1) for more information. This directory is ignored (except logs/HEAD) if $GIT_COMMON_DIR is set and &quot;$GIT_COMMON_DIR/logs&quot; will be used instead.</dl>
<p> logs/refs/heads/<code>name</code></p>
<dl>
<dd>Records all changes made to the branch tip named <code>name</code>.</dl>
<p> logs/refs/tags/<code>name</code></p>
<dl>
<dd>Records all changes made to the tag named <code>name</code>.</dl>
<p> shallow</p>
<dl>
<dd>This is similar to <code>info/grafts</code> but is internally used and maintained by shallow clone mechanism. See <code>&#8211;depth</code> option to <code><a href="/docs/linux/man/1-git-clone/">git-clone</a></code>(1) and <code><a href="/docs/linux/man/1-git-fetch/">git-fetch</a></code>(1). This file is ignored if $GIT_COMMON_DIR is set and &quot;$GIT_COMMON_DIR/shallow&quot; will be used instead.</dl>
<p> commondir</p>
<dl>
<dd>If this file exists, $GIT_COMMON_DIR (see <code><a href="/docs/linux/man/1-git/">git</a></code>(1)) will be set to the path specified in this file if it is not explicitly set. If the specified path is relative, it is relative to $GIT_DIR. The repository with commondir is incomplete without the repository pointed by &quot;commondir&quot;.</dl>
<p> modules</p>
<dl>
<dd>Contains the git-repositories of the submodules.</dl>
<p> worktrees</p>
<dl>
<dd>Contains administrative data for linked working trees. Each subdirectory contains the working tree-related part of a linked working tree. This directory is ignored if $GIT_COMMON_DIR is set, in which case &quot;$GIT_COMMON_DIR/worktrees&quot; will be used instead.</dl>
<p> worktrees/&lt;id&gt;/gitdir</p>
<dl>
<dd>A text file containing the absolute path back to the .git file that points to here. This is used to check if the linked repository has been manually removed and there is no need to keep this directory any more. The mtime of this file should be updated every time the linked repository is accessed.</dl>
<p> worktrees/&lt;id&gt;/locked</p>
<dl>
<dd>If this file exists, the linked working tree may be on a portable device and not available. The presence of this file prevents <code>worktrees/&lt;id&gt;</code> from being pruned either automatically or manually by <code>git worktree prune</code>. The file may contain a string explaining why the repository is locked.</dl>
<p> worktrees/&lt;id&gt;/config.worktree</p>
<dl>
<dd>Working directory specific configuration file.</dl>
<h2>Git Repository Format Versions</h2>
<p>Every git repository is marked with a numeric version in the <code>core.repositoryformatversion</code> key of its <code>config</code> file. This version specifies the rules for operating on the on-disk repository data. An implementation of git which does not understand a particular version advertised by an on-disk repository MUST NOT operate on that repository; doing so risks not only producing wrong results, but actually losing data. </p>
<p> Because of this rule, version bumps should be kept to an absolute minimum. Instead, we generally prefer these strategies: </p>
<dl>
<dd>&bull; bumping format version numbers of individual data files (e.g., index, packfiles, etc). This restricts the incompatibilities only to those files.</dl>
<dl>
<dd>&bull; introducing new data that gracefully degrades when used by older clients (e.g., pack bitmap files are ignored by older clients, which simply do not take advantage of the optimization they provide).</dl>
<p> A whole-repository format version bump should only be part of a change that cannot be independently versioned. For instance, if one were to change the reachability rules for objects, or the rules for locking refs, that would require a bump of the repository format version. </p>
<p> Note that this applies only to accessing the repository&#8217;s disk contents directly. An older client which understands only format <code>0</code> may still connect via <code>git://</code> to a repository using format <code>1</code>, as long as the server process understands format <code>1</code>. </p>
<p> The preferred strategy for rolling out a version bump (whether whole repository or for a single file) is to teach git to read the new format, and allow writing the new format with a config switch or command line option (for experimentation or for those who do not care about backwards compatibility with older gits). Then after a long period to allow the reading capability to become common, we may switch to writing the new format by default. </p>
<p> The currently defined format versions are:</p>
<h3>Version <code>0</code></h3>
<p>This is the format defined by the initial version of git, including but not limited to the format of the repository directory, the repository configuration file, and the object and ref storage. Specifying the complete behavior of git is beyond the scope of this document.</p>
<h3>Version <code>1</code></h3>
<p>This format is identical to version <code>0</code>, with the following exceptions: </p>
<dl>
<dd>1. When reading the <code>core.repositoryformatversion</code> variable, a git implementation which supports version 1 MUST also read any configuration keys found in the <code>extensions</code> section of the configuration file.</dl>
<dl>
<dd>2. If a version-1 repository specifies any <code>extensions.*</code> keys that the running git has not implemented, the operation MUST NOT proceed. Similarly, if the value of any known key is not understood by the implementation, the operation MUST NOT proceed.</dl>
<p> Note that if no extensions are specified in the config file, then <code>core.repositoryformatversion</code> SHOULD be set to <code>0</code> (setting it to <code>1</code> provides no benefit, and makes the repository incompatible with older implementations of git). </p>
<p> This document will serve as the master list for extensions. Any implementation wishing to define a new extension should make a note of it here, in order to claim the name. </p>
<p> The defined extensions are: </p>
<p> <font SIZE="+1"> <code>noop</code></p>
<dl>
<dd>This extension does not change git&#8217;s behavior at all. It is useful only for testing format-1 compatibility.</dl>
<p> </font><font SIZE="+2"> <code>preciousObjects</code></p>
<dl>
<dd>When the config key <code>extensions.preciousObjects</code> is set to <code>true</code>, objects in the repository MUST NOT be deleted (e.g., by <code>git-prune</code> or <code>git repack -d</code>).</dl>
<p> </font><font SIZE="+3"> <code>partialclone</code></p>
<dl>
<dd>When the config key <code>extensions.partialclone</code> is set, it indicates that the repo was created with a partial clone (or later performed a partial fetch) and that the remote may have omitted sending certain unwanted objects. Such a remote is called a &quot;promisor remote&quot; and it promises that all such omitted objects can be fetched from it in the future. </p>
<p> The value of this key is the name of the promisor remote.</dl>
<p> </font><font SIZE="+4"> <code>worktreeConfig</code></p>
<dl>
<dd>If set, by default &quot;git config&quot; reads from both &quot;config&quot; and &quot;config.worktree&quot; file from GIT_DIR in that order. In multiple working directory mode, &quot;config&quot; file is shared while &quot;config.worktree&quot; is per-working directory (i.e., it&#8217;s in GIT_COMMON_DIR/worktrees/&lt;id&gt;/config.worktree)</dl>
<p> </font></p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-git-init/">git-init</a></code>(1), <code><a href="/docs/linux/man/1-git-clone/">git-clone</a></code>(1), <code><a href="/docs/linux/man/1-git-fetch/">git-fetch</a></code>(1), <code><a href="/docs/linux/man/1-git-pack-refs/">git-pack-refs</a></code>(1), <code><a href="/docs/linux/man/1-git-gc/">git-gc</a></code>(1), <code><a href="/docs/linux/man/1-git-checkout/">git-checkout</a></code>(1), <code><a href="/docs/linux/man/7-gitglossary/">gitglossary</a></code>(7), m[blue]<code>The Git User&#8217;s Manual</code>m[]<font SIZE="-2">[1]</font></p>
<h2>Git</h2>
<p>Part of the <code><a href="/docs/linux/man/1-git/">git</a></code>(1) suite</p>
<h2>Notes</h2>
<dl>
<dt> 1.</p>
<dd>The Git User&#8217;s Manual</p>
<dl>
<dd>file:///usr/share/doc/git/html/user-manual.html</dl>
