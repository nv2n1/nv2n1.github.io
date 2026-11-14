---
title: "gitglossary(7)"
name: "gitglossary"
section: "7"
letter: "g"
url: "/docs/linux/man/7-gitglossary/"
description: "gitglossary – A Git Glossary"
---

<p>gitglossary &#8211; A Git Glossary</p>
<h2>Synopsis</h2>
<p>*</p>
<h2>Description</h2>
<p>alternate object database</p>
<dl>
<dd>Via the alternates mechanism, a repository can inherit part of its object database from another object database, which is called an &quot;alternate&quot;.</dl>
<p> bare repository</p>
<dl>
<dd>A bare repository is normally an appropriately named directory with a <code>.git</code> suffix that does not have a locally checked-out copy of any of the files under revision control. That is, all of the Git administrative and control files that would normally be present in the hidden <code>.git</code> sub-directory are directly present in the <code>repository.git</code> directory instead, and no other files are present and checked out. Usually publishers of public repositories make bare repositories available.</dl>
<p> blob object</p>
<dl>
<dd>Untyped object, e.g. the contents of a file.</dl>
<p> branch</p>
<dl>
<dd>A &quot;branch&quot; is a line of development. The most recent commit on a branch is referred to as the tip of that branch. The tip of the branch is referenced by a branch head, which moves forward as additional development is done on the branch. A single Git repository can track an arbitrary number of branches, but your working tree is associated with just one of them (the &quot;current&quot; or &quot;checked out&quot; branch), and HEAD points to that branch.</dl>
<p> cache</p>
<dl>
<dd>Obsolete for: index.</dl>
<p> chain</p>
<dl>
<dd>A list of objects, where each object in the list contains a reference to its successor (for example, the successor of a commit could be one of its parents).</dl>
<p> changeset</p>
<dl>
<dd>BitKeeper/cvsps speak for &quot;commit&quot;. Since Git does not store changes, but states, it really does not make sense to use the term &quot;changesets&quot; with Git.</dl>
<p> checkout</p>
<dl>
<dd>The action of updating all or part of the working tree with a tree object or blob from the object database, and updating the index and HEAD if the whole working tree has been pointed at a new branch.</dl>
<p> cherry-picking</p>
<dl>
<dd>In SCM jargon, &quot;cherry pick&quot; means to choose a subset of changes out of a series of changes (typically commits) and record them as a new series of changes on top of a different codebase. In Git, this is performed by the &quot;git cherry-pick&quot; command to extract the change introduced by an existing commit and to record it based on the tip of the current branch as a new commit.</dl>
<p> clean</p>
<dl>
<dd>A working tree is clean, if it corresponds to the revision referenced by the current head. Also see &quot;dirty&quot;.</dl>
<p> commit</p>
<dl>
<dd>As a noun: A single point in the Git history; the entire history of a project is represented as a set of interrelated commits. The word &quot;commit&quot; is often used by Git in the same places other revision control systems use the words &quot;revision&quot; or &quot;version&quot;. Also used as a short hand for commit object. </p>
<p> As a verb: The action of storing a new snapshot of the project&#8217;s state in the Git history, by creating a new commit representing the current state of the index and advancing HEAD to point at the new commit.</dl>
<p> commit object</p>
<dl>
<dd>An object which contains the information about a particular revision, such as parents, committer, author, date and the tree object which corresponds to the top directory of the stored revision.</dl>
<p> commit-ish (also committish)</p>
<dl>
<dd>A commit object or an object that can be recursively dereferenced to a commit object. The following are all commit-ishes: a commit object, a tag object that points to a commit object, a tag object that points to a tag object that points to a commit object, etc.</dl>
<p> core Git</p>
<dl>
<dd>Fundamental data structures and utilities of Git. Exposes only limited source code management tools.</dl>
<p> DAG</p>
<dl>
<dd>Directed acyclic graph. The commit objects form a directed acyclic graph, because they have parents (directed), and the graph of commit objects is acyclic (there is no chain which begins and ends with the same object).</dl>
<p> dangling object</p>
<dl>
<dd>An unreachable object which is not reachable even from other unreachable objects; a dangling object has no references to it from any reference or object in the repository.</dl>
<p> detached HEAD</p>
<dl>
<dd>Normally the HEAD stores the name of a branch, and commands that operate on the history HEAD represents operate on the history leading to the tip of the branch the HEAD points at. However, Git also allows you to check out an arbitrary commit that isn&#8217;t necessarily the tip of any particular branch. The HEAD in such a state is called &quot;detached&quot;. </p>
<p> Note that commands that operate on the history of the current branch (e.g. <code>git commit</code> to build a new history on top of it) still work while the HEAD is detached. They update the HEAD to point at the tip of the updated history without affecting any branch. Commands that update or inquire information <i>about</i> the current branch (e.g. <code>git branch &#8211;set-upstream-to</code> that sets what remote-tracking branch the current branch integrates with) obviously do not work, as there is no (real) current branch to ask about in this state.</dl>
<p> directory</p>
<dl>
<dd>The list you get with &quot;ls&quot; :-)</dl>
<p> dirty</p>
<dl>
<dd>A working tree is said to be &quot;dirty&quot; if it contains modifications which have not been committed to the current branch.</dl>
<p> evil merge</p>
<dl>
<dd>An evil merge is a merge that introduces changes that do not appear in any parent.</dl>
<p> fast-forward</p>
<dl>
<dd>A fast-forward is a special type of merge where you have a revision and you are &quot;merging&quot; another branch&#8217;s changes that happen to be a descendant of what you have. In such a case, you do not make a new merge commit but instead just update your branch to point at the same revision as the branch you are merging. This will happen frequently on a remote-tracking branch of a remote repository.</dl>
<p> fetch</p>
<dl>
<dd>Fetching a branch means to get the branch&#8217;s head ref from a remote repository, to find out which objects are missing from the local object database, and to get them, too. See also <code><a href="/docs/linux/man/1-git-fetch/">git-fetch</a></code>(1).</dl>
<p> file system</p>
<dl>
<dd>Linus Torvalds originally designed Git to be a user space file system, i.e. the infrastructure to hold files and directories. That ensured the efficiency and speed of Git.</dl>
<p> Git archive</p>
<dl>
<dd>Synonym for repository (for arch people).</dl>
<p> gitfile</p>
<dl>
<dd>A plain file <code>.git</code> at the root of a working tree that points at the directory that is the real repository.</dl>
<p> grafts</p>
<dl>
<dd>Grafts enables two otherwise different lines of development to be joined together by recording fake ancestry information for commits. This way you can make Git pretend the set of parents a commit has is different from what was recorded when the commit was created. Configured via the <code>.git/info/grafts</code> file. </p>
<p> Note that the grafts mechanism is outdated and can lead to problems transferring objects between repositories; see <code><a href="/docs/linux/man/1-git-replace/">git-replace</a></code>(1) for a more flexible and robust system to do the same thing.</dl>
<p> hash</p>
<dl>
<dd>In Git&#8217;s context, synonym for object name.</dl>
<p> head</p>
<dl>
<dd>A named reference to the commit at the tip of a branch. Heads are stored in a file in <code>$GIT_DIR/refs/heads/</code> directory, except when using packed refs. (See <code><a href="/docs/linux/man/1-git-pack-refs/">git-pack-refs</a></code>(1).)</dl>
<p> HEAD</p>
<dl>
<dd>The current branch. In more detail: Your working tree is normally derived from the state of the tree referred to by HEAD. HEAD is a reference to one of the heads in your repository, except when using a detached HEAD, in which case it directly references an arbitrary commit.</dl>
<p> head ref</p>
<dl>
<dd>A synonym for head.</dl>
<p> hook</p>
<dl>
<dd>During the normal execution of several Git commands, call-outs are made to optional scripts that allow a developer to add functionality or checking. Typically, the hooks allow for a command to be pre-verified and potentially aborted, and allow for a post-notification after the operation is done. The hook scripts are found in the <code>$GIT_DIR/hooks/</code> directory, and are enabled by simply removing the <code>.sample</code> suffix from the filename. In earlier versions of Git you had to make them executable.</dl>
<p> index</p>
<dl>
<dd>A collection of files with stat information, whose contents are stored as objects. The index is a stored version of your working tree. Truth be told, it can also contain a second, and even a third version of a working tree, which are used when merging.</dl>
<p> index entry</p>
<dl>
<dd>The information regarding a particular file, stored in the index. An index entry can be unmerged, if a merge was started, but not yet finished (i.e. if the index contains multiple versions of that file).</dl>
<p> master</p>
<dl>
<dd>The default development branch. Whenever you create a Git repository, a branch named &quot;master&quot; is created, and becomes the active branch. In most cases, this contains the local development, though that is purely by convention and is not required.</dl>
<p> merge</p>
<dl>
<dd>As a verb: To bring the contents of another branch (possibly from an external repository) into the current branch. In the case where the merged-in branch is from a different repository, this is done by first fetching the remote branch and then merging the result into the current branch. This combination of fetch and merge operations is called a pull. Merging is performed by an automatic process that identifies changes made since the branches diverged, and then applies all those changes together. In cases where changes conflict, manual intervention may be required to complete the merge. </p>
<p> As a noun: unless it is a fast-forward, a successful merge results in the creation of a new commit representing the result of the merge, and having as parents the tips of the merged branches. This commit is referred to as a &quot;merge commit&quot;, or sometimes just a &quot;merge&quot;.</dl>
<p> object</p>
<dl>
<dd>The unit of storage in Git. It is uniquely identified by the SHA-1 of its contents. Consequently, an object cannot be changed.</dl>
<p> object database</p>
<dl>
<dd>Stores a set of &quot;objects&quot;, and an individual object is identified by its object name. The objects usually live in <code>$GIT_DIR/objects/</code>.</dl>
<p> object identifier</p>
<dl>
<dd>Synonym for object name.</dl>
<p> object name</p>
<dl>
<dd>The unique identifier of an object. The object name is usually represented by a 40 character hexadecimal string. Also colloquially called SHA-1.</dl>
<p> object type</p>
<dl>
<dd>One of the identifiers &quot;commit&quot;, &quot;tree&quot;, &quot;tag&quot; or &quot;blob&quot; describing the type of an object.</dl>
<p> octopus</p>
<dl>
<dd>To merge more than two branches.</dl>
<p> origin</p>
<dl>
<dd>The default upstream repository. Most projects have at least one upstream project which they track. By default <i>origin</i> is used for that purpose. New upstream updates will be fetched into remote-tracking branches named origin/name-of-upstream-branch, which you can see using <code>git branch -r</code>.</dl>
<p> overlay</p>
<dl>
<dd>Only update and add files to the working directory, but don&#8217;t delete them, similar to how <i>cp -R</i> would update the contents in the destination directory. This is the default mode in a checkout when checking out files from the index or a tree-ish. In contrast, no-overlay mode also deletes tracked files not present in the source, similar to <i>rsync &#8211;delete</i>.</dl>
<p> pack</p>
<dl>
<dd>A set of objects which have been compressed into one file (to save space or to transmit them efficiently).</dl>
<p> pack index</p>
<dl>
<dd>The list of identifiers, and other information, of the objects in a pack, to assist in efficiently accessing the contents of a pack.</dl>
<p> pathspec</p>
<dl>
<dd>Pattern used to limit paths in Git commands. </p>
<p> Pathspecs are used on the command line of &quot;git ls-files&quot;, &quot;git ls-tree&quot;, &quot;git add&quot;, &quot;git grep&quot;, &quot;git diff&quot;, &quot;git checkout&quot;, and many other commands to limit the scope of operations to some subset of the tree or worktree. See the documentation of each command for whether paths are relative to the current directory or toplevel. The pathspec syntax is as follows: </p>
<dl>
<dd>&bull; any path matches itself</dl>
<dl>
<dd>&bull; the pathspec up to the last slash represents a directory prefix. The scope of that pathspec is limited to that subtree.</dl>
<dl>
<dd>&bull; the rest of the pathspec is a pattern for the remainder of the pathname. Paths relative to the directory prefix will be matched against that pattern using <a href="/docs/linux/man/3-fnmatch/">fnmatch</a>(3); in particular, <i>*</i> and <i>?</i> <i>can</i> match directory separators.</dl>
<p> For example, Documentation/*.jpg will match all .jpg files in the Documentation subtree, including Documentation/chapter_1/figure_1.jpg. </p>
<p> A pathspec that begins with a colon <code>:</code> has special meaning. In the short form, the leading colon <code>:</code> is followed by zero or more &quot;magic signature&quot; letters (which optionally is terminated by another colon <code>:</code>), and the remainder is the pattern to match against the path. The &quot;magic signature&quot; consists of ASCII symbols that are neither alphanumeric, glob, regex special characters nor colon. The optional colon that terminates the &quot;magic signature&quot; can be omitted if the pattern begins with a character that does not belong to &quot;magic signature&quot; symbol set and is not a colon. </p>
<p> In the long form, the leading colon <code>:</code> is followed by an open parenthesis <code>(</code>, a comma-separated list of zero or more &quot;magic words&quot;, and a close parentheses <code>)</code>, and the remainder is the pattern to match against the path. </p>
<p> A pathspec with only a colon means &quot;there is no pathspec&quot;. This form should not be combined with other pathspec. </p>
<p> top</p>
<dl>
<dd>The magic word <code>top</code> (magic signature: <code>/</code>) makes the pattern match from the root of the working tree, even when you are running the command from inside a subdirectory.</dl>
<p> literal</p>
<dl>
<dd>Wildcards in the pattern such as <code>*</code> or <code>?</code> are treated as literal characters.</dl>
<p> icase</p>
<dl>
<dd>Case insensitive match.</dl>
<p> glob</p>
<dl>
<dd>Git treats the pattern as a shell glob suitable for consumption by <a href="/docs/linux/man/3-fnmatch/">fnmatch</a>(3) with the FNM_PATHNAME flag: wildcards in the pattern will not match a / in the pathname. For example, &quot;Documentation/*.html&quot; matches &quot;Documentation/git.html&quot; but not &quot;Documentation/ppc/ppc.html&quot; or &quot;tools/perf/Documentation/perf.html&quot;. </p>
<p> Two consecutive asterisks (&quot;<code>**</code>&quot;) in patterns matched against full pathname may have special meaning: </p>
<dl>
<dd>&bull; A leading &quot;<code>**</code>&quot; followed by a slash means match in all directories. For example, &quot;<code>**/foo</code>&quot; matches file or directory &quot;<code>foo</code>&quot; anywhere, the same as pattern &quot;<code>foo</code>&quot;. &quot;<code>**/foo/bar</code>&quot; matches file or directory &quot;<code>bar</code>&quot; anywhere that is directly under directory &quot;<code>foo</code>&quot;.</dl>
<dl>
<dd>&bull; A trailing &quot;<code>/**</code>&quot; matches everything inside. For example, &quot;<code>abc/**</code>&quot; matches all files inside directory &quot;abc&quot;, relative to the location of the <code>.gitignore</code> file, with infinite depth.</dl>
<dl>
<dd>&bull; A slash followed by two consecutive asterisks then a slash matches zero or more directories. For example, &quot;<code>a/**/b</code>&quot; matches &quot;<code>a/b</code>&quot;, &quot;<code>a/x/b</code>&quot;, &quot;<code>a/x/y/b</code>&quot; and so on.</dl>
<dl>
<dd>&bull; Other consecutive asterisks are considered invalid. </p>
<p> Glob magic is incompatible with literal magic.</dl>
</dl>
<p> attr</p>
<dl>
<dd>After <code>attr:</code> comes a space separated list of &quot;attribute requirements&quot;, all of which must be met in order for the path to be considered a match; this is in addition to the usual non-magic pathspec pattern matching. See <code><a href="/docs/linux/man/5-gitattributes/">gitattributes</a></code>(5). </p>
<p> Each of the attribute requirements for the path takes one of these forms: </p>
<dl>
<dd>&bull; &quot;<code>ATTR</code>&quot; requires that the attribute <code>ATTR</code> be set.</dl>
<dl>
<dd>&bull; &quot;<code>-ATTR</code>&quot; requires that the attribute <code>ATTR</code> be unset.</dl>
<dl>
<dd>&bull; &quot;<code>ATTR=VALUE</code>&quot; requires that the attribute <code>ATTR</code> be set to the string <code>VALUE</code>.</dl>
<dl>
<dd>&bull; &quot;<code>!ATTR</code>&quot; requires that the attribute <code>ATTR</code> be unspecified. </p>
<p> Note that when matching against a tree object, attributes are still obtained from working tree, not from the given tree object.</dl>
</dl>
<p> exclude</p>
<dl>
<dd>After a path matches any non-exclude pathspec, it will be run through all exclude pathspecs (magic signature: <code>!</code> or its synonym <code>^</code>). If it matches, the path is ignored. When there is no non-exclude pathspec, the exclusion is applied to the result set as if invoked without any pathspec.</dl>
</dl>
<p> parent</p>
<dl>
<dd>A commit object contains a (possibly empty) list of the logical predecessor(s) in the line of development, i.e. its parents.</dl>
<p> pickaxe</p>
<dl>
<dd>The term pickaxe refers to an option to the diffcore routines that help select changes that add or delete a given text string. With the <code>&#8211;pickaxe-all</code> option, it can be used to view the full changeset that introduced or removed, say, a particular line of text. See <code><a href="/docs/linux/man/1-git-diff/">git-diff</a></code>(1).</dl>
<p> plumbing</p>
<dl>
<dd>Cute name for core Git.</dl>
<p> porcelain</p>
<dl>
<dd>Cute name for programs and program suites depending on core Git, presenting a high level access to core Git. Porcelains expose more of a SCM interface than the plumbing.</dl>
<p> per-worktree ref</p>
<dl>
<dd>Refs that are per-worktree, rather than global. This is presently only HEAD and any refs that start with <code>refs/bisect/</code>, but might later include other unusual refs.</dl>
<p> pseudoref</p>
<dl>
<dd>Pseudorefs are a class of files under <code>$GIT_DIR</code> which behave like refs for the purposes of rev-parse, but which are treated specially by git. Pseudorefs both have names that are all-caps, and always start with a line consisting of a SHA-1 followed by whitespace. So, HEAD is not a pseudoref, because it is sometimes a symbolic ref. They might optionally contain some additional data. <code>MERGE_HEAD</code> and <code>CHERRY_PICK_HEAD</code> are examples. Unlike per-worktree refs, these files cannot be symbolic refs, and never have reflogs. They also cannot be updated through the normal ref update machinery. Instead, they are updated by directly writing to the files. However, they can be read as if they were refs, so <code>git rev-parse MERGE_HEAD</code> will work.</dl>
<p> pull</p>
<dl>
<dd>Pulling a branch means to fetch it and merge it. See also <code><a href="/docs/linux/man/1-git-pull/">git-pull</a></code>(1).</dl>
<p> push</p>
<dl>
<dd>Pushing a branch means to get the branch&#8217;s head ref from a remote repository, find out if it is an ancestor to the branch&#8217;s local head ref, and in that case, putting all objects, which are reachable from the local head ref, and which are missing from the remote repository, into the remote object database, and updating the remote head ref. If the remote head is not an ancestor to the local head, the push fails.</dl>
<p> reachable</p>
<dl>
<dd>All of the ancestors of a given commit are said to be &quot;reachable&quot; from that commit. More generally, one object is reachable from another if we can reach the one from the other by a chain that follows tags to whatever they tag, commits to their parents or trees, and trees to the trees or blobs that they contain.</dl>
<p> rebase</p>
<dl>
<dd>To reapply a series of changes from a branch to a different base, and reset the head of that branch to the result.</dl>
<p> ref</p>
<dl>
<dd>A name that begins with <code>refs/</code> (e.g. <code>refs/heads/master</code>) that points to an object name or another ref (the latter is called a symbolic ref). For convenience, a ref can sometimes be abbreviated when used as an argument to a Git command; see <code><a href="/docs/linux/man/7-gitrevisions/">gitrevisions</a></code>(7) for details. Refs are stored in the repository. </p>
<p> The ref namespace is hierarchical. Different subhierarchies are used for different purposes (e.g. the <code>refs/heads/</code> hierarchy is used to represent local branches). </p>
<p> There are a few special-purpose refs that do not begin with <code>refs/</code>. The most notable example is <code>HEAD</code>.</dl>
<p> reflog</p>
<dl>
<dd>A reflog shows the local &quot;history&quot; of a ref. In other words, it can tell you what the 3rd last revision in <i>this</i> repository was, and what was the current state in <i>this</i> repository, yesterday 9:14pm. See <code><a href="/docs/linux/man/1-git-reflog/">git-reflog</a></code>(1) for details.</dl>
<p> refspec</p>
<dl>
<dd>A &quot;refspec&quot; is used by fetch and push to describe the mapping between remote ref and local ref.</dl>
<p> remote repository</p>
<dl>
<dd>A repository which is used to track the same project but resides somewhere else. To communicate with remotes, see fetch or push.</dl>
<p> remote-tracking branch</p>
<dl>
<dd>A ref that is used to follow changes from another repository. It typically looks like <i>refs/remotes/foo/bar</i> (indicating that it tracks a branch named <i>bar</i> in a remote named <i>foo</i>), and matches the right-hand-side of a configured fetch refspec. A remote-tracking branch should not contain direct modifications or have local commits made to it.</dl>
<p> repository</p>
<dl>
<dd>A collection of refs together with an object database containing all objects which are reachable from the refs, possibly accompanied by meta data from one or more porcelains. A repository can share an object database with other repositories via alternates mechanism.</dl>
<p> resolve</p>
<dl>
<dd>The action of fixing up manually what a failed automatic merge left behind.</dl>
<p> revision</p>
<dl>
<dd>Synonym for commit (the noun).</dl>
<p> rewind</p>
<dl>
<dd>To throw away part of the development, i.e. to assign the head to an earlier revision.</dl>
<p> SCM</p>
<dl>
<dd>Source code management (tool).</dl>
<p> SHA-1</p>
<dl>
<dd>&quot;Secure Hash Algorithm 1&quot;; a cryptographic hash function. In the context of Git used as a synonym for object name.</dl>
<p> shallow clone</p>
<dl>
<dd>Mostly a synonym to shallow repository but the phrase makes it more explicit that it was created by running <code>git clone &#8211;depth=&#8230;</code> command.</dl>
<p> shallow repository</p>
<dl>
<dd>A shallow repository has an incomplete history some of whose commits have parents cauterized away (in other words, Git is told to pretend that these commits do not have the parents, even though they are recorded in the commit object). This is sometimes useful when you are interested only in the recent history of a project even though the real history recorded in the upstream is much larger. A shallow repository is created by giving the <code>&#8211;depth</code> option to <code><a href="/docs/linux/man/1-git-clone/">git-clone</a></code>(1), and its history can be later deepened with <code><a href="/docs/linux/man/1-git-fetch/">git-fetch</a></code>(1).</dl>
<p> stash entry</p>
<dl>
<dd>An object used to temporarily store the contents of a dirty working directory and the index for future reuse.</dl>
<p> submodule</p>
<dl>
<dd>A repository that holds the history of a separate project inside another repository (the latter of which is called superproject).</dl>
<p> superproject</p>
<dl>
<dd>A repository that references repositories of other projects in its working tree as submodules. The superproject knows about the names of (but does not hold copies of) commit objects of the contained submodules.</dl>
<p> symref</p>
<dl>
<dd>Symbolic reference: instead of containing the SHA-1 id itself, it is of the format <i>ref: refs/some/thing</i> and when referenced, it recursively dereferences to this reference. <i>HEAD</i> is a prime example of a symref. Symbolic references are manipulated with the <code><a href="/docs/linux/man/1-git-symbolic-ref/">git-symbolic-ref</a></code>(1) command.</dl>
<p> tag</p>
<dl>
<dd>A ref under <code>refs/tags/</code> namespace that points to an object of an arbitrary type (typically a tag points to either a tag or a commit object). In contrast to a head, a tag is not updated by the <code>commit</code> command. A Git tag has nothing to do with a Lisp tag (which would be called an object type in Git&#8217;s context). A tag is most typically used to mark a particular point in the commit ancestry chain.</dl>
<p> tag object</p>
<dl>
<dd>An object containing a ref pointing to another object, which can contain a message just like a commit object. It can also contain a (PGP) signature, in which case it is called a &quot;signed tag object&quot;.</dl>
<p> topic branch</p>
<dl>
<dd>A regular Git branch that is used by a developer to identify a conceptual line of development. Since branches are very easy and inexpensive, it is often desirable to have several small branches that each contain very well defined concepts or small incremental yet related changes.</dl>
<p> tree</p>
<dl>
<dd>Either a working tree, or a tree object together with the dependent blob and tree objects (i.e. a stored representation of a working tree).</dl>
<p> tree object</p>
<dl>
<dd>An object containing a list of file names and modes along with refs to the associated blob and/or tree objects. A tree is equivalent to a directory.</dl>
<p> tree-ish (also treeish)</p>
<dl>
<dd>A tree object or an object that can be recursively dereferenced to a tree object. Dereferencing a commit object yields the tree object corresponding to the revision&#8217;s top directory. The following are all tree-ishes: a commit-ish, a tree object, a tag object that points to a tree object, a tag object that points to a tag object that points to a tree object, etc.</dl>
<p> unmerged index</p>
<dl>
<dd>An index which contains unmerged index entries.</dl>
<p> unreachable object</p>
<dl>
<dd>An object which is not reachable from a branch, tag, or any other reference.</dl>
<p> upstream branch</p>
<dl>
<dd>The default branch that is merged into the branch in question (or the branch in question is rebased onto). It is configured via branch.&lt;name&gt;.remote and branch.&lt;name&gt;.merge. If the upstream branch of <i>A</i> is <i>origin/B</i> sometimes we say &quot;<i>A</i> is tracking <i>origin/B</i>&quot;.</dl>
<p> working tree</p>
<dl>
<dd>The tree of actual checked out files. The working tree normally contains the contents of the HEAD commit&#8217;s tree, plus any local changes that you have made but not yet committed.</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/7-gittutorial/">gittutorial</a></code>(7), <code><a href="/docs/linux/man/7-gittutorial-2/">gittutorial-2</a></code>(7), <code><a href="/docs/linux/man/7-gitcvs-migration/">gitcvs-migration</a></code>(7), <code><a href="/docs/linux/man/7-giteveryday/">giteveryday</a></code>(7), m[blue]<code>The Git User&#8217;s Manual</code>m[]<font SIZE="-2">[1]</font></p>
<h2>Git</h2>
<p>Part of the <code><a href="/docs/linux/man/1-git/">git</a></code>(1) suite</p>
<h2>Notes</h2>
<dl>
<dt> 1.</p>
<dd>The Git User&#8217;s Manual</p>
<dl>
<dd>file:///usr/share/doc/git/html/user-manual.html</dl>
