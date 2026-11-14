---
title: "git-pull(1)"
name: "git-pull"
section: "1"
letter: "g"
url: "/docs/linux/man/1-git-pull/"
description: "git-pull – Fetch from and integrate with another repository or a local branch"
---

<h2 class="name">NAME</h2>
<p> git-pull &#8211; Fetch from and integrate with another repository or a local branch </p>
<h2>SYNOPSIS</h2>
<pre><code>
git pull[&lt;options&gt;][&lt;repository&gt;[&lt;refspec&gt;...]]
</code></pre>
<h2>DESCRIPTION</h2>
<p> Incorporates changes from a remote repository into the current branch. If the current branch is behind the remote, then by default it will fast-forward the current branch to match the remote. If the current branch and the remote have diverged, the user needs to specify how to reconcile the divergent branches with <code>&#8211;rebase</code> or <code>&#8211;no-rebase</code> (or the corresponding configuration option in <code>pull.rebase</code>). </p>
<p> More precisely, <code>git pull</code> runs <code>git fetch</code> with the given parameters and then depending on configuration options or command line flags, will call either <code>git rebase</code> or <code>git merge</code> to reconcile diverging branches. </p>
<p> &lt;repository&gt; should be the name of a remote repository as passed to <code><a href="/docs/linux/man/1-git-fetch/">git-fetch</a></code>(1). &lt;refspec&gt; can name an arbitrary remote ref (for example, the name of a tag) or even a collection of refs with corresponding remote-tracking branches (e.g., refs/heads/*:refs/remotes/origin/*), but usually it is the name of a branch in the remote repository. </p>
<p> Default values for &lt;repository&gt; and &lt;branch&gt; are read from the &quot;remote&quot; and &quot;merge&quot; configuration for the current branch as set by <code><a href="/docs/linux/man/1-git-branch/">git-branch</a></code>(1) <code>&#8211;track</code>. </p>
<p> Assume the following history exists and the current branch is &quot;<code>master</code>&quot;: </p>
<dl>
<dt>
<dd>
A&#8211; &#8211; B&#8211; &#8211; C master on origin / D&#8211; &#8211; E&#8211; &#8211; F&#8211; &#8211; G master ^<br />
    origin / master in your repository
</dl>
<p> Then &quot;<code>git pull</code>&quot; will fetch and replay the changes from the remote <code>master</code> branch since it diverged from the local <code>master</code> (i.e., <code>E</code>) until its current commit (<code>C</code>) on top of <code>master</code> and record the result in a new commit along with the names of the two parent commits and a log message from the user describing the changes. </p>
<dl>
<dt>
<dd>
<pre><code>
A-- - B-- - C origin / master / D-- - E-- - F-- - G-- - H master
</code></pre>
</dl>
<p> See <code><a href="/docs/linux/man/1-git-merge/">git-merge</a></code>(1) for details, including how conflicts are presented and handled. </p>
<p> In Git 1.7.0 or later, to cancel a conflicting merge, use <code>git reset &#8211;merge</code>. <code>Warning</code>: In older versions of Git, running <i>git pull</i> with uncommitted changes is discouraged: while possible, it leaves you in a state that may be hard to back out of in the case of a conflict. </p>
<p> If any of the remote changes overlap with local uncommitted changes, the merge will be automatically canceled and the work tree untouched. It is generally best to get any local changes in working order before pulling or stash them away with <code><a href="/docs/linux/man/1-git-stash/">git-stash</a></code>(1).</p>
<h2>OPTIONS</h2>
<p> -q, &#8211;quiet</p>
<dl>
<dt>
<dd> This is passed to both underlying git-fetch to squelch reporting of during transfer, and underlying git-merge to squelch output during merging.</dl>
<p> -v, &#8211;verbose</p>
<dl>
<dt>
<dd> Pass &#8211;verbose to git-fetch and git-merge.</dl>
<p> &#8211;[no-]recurse-submodules[=yes|on-demand|no]</p>
<dl>
<dt>
<dd> This option controls if new commits of populated submodules should be fetched, and if the working trees of active submodules should be updated, too (see <code><a href="/docs/linux/man/1-git-fetch/">git-fetch</a></code>(1), <code><a href="/docs/linux/man/1-git-config/">git-config</a></code>(1) and <code><a href="/docs/linux/man/5-gitmodules/">gitmodules</a></code>(5)). </p>
<p> If the checkout is done via rebase, local submodule commits are rebased as well. </p>
<p> If the update is done via merge, the submodule conflicts are resolved and checked out.</dl>
<h3>Options related to merging</h3>
<p> &#8211;commit, &#8211;no-commit</p>
<dl>
<dt>
<dd> Perform the merge and commit the result. This option can be used to override &#8211;no-commit. Only useful when merging. </p>
<p> With &#8211;no-commit perform the merge and stop just before creating a merge commit, to give the user a chance to inspect and further tweak the merge result before committing. </p>
<p> Note that fast-forward updates do not create a merge commit and therefore there is no way to stop those merges with &#8211;no-commit. Thus, if you want to ensure your branch is not changed or updated by the merge command, use &#8211;no-ff with &#8211;no-commit.</dl>
<p> &#8211;edit, -e, &#8211;no-edit</p>
<dl>
<dt>
<dd> Invoke an editor before committing successful mechanical merge to further edit the auto-generated merge message, so that the user can explain and justify the merge. The <code>&#8211;no-edit</code> option can be used to accept the auto-generated message (this is generally discouraged). </p>
<p> Older scripts may depend on the historical behaviour of not allowing the user to edit the merge log message. They will see an editor opened when they run <code>git merge</code>. To make it easier to adjust such scripts to the updated behaviour, the environment variable <code>GIT_MERGE_AUTOEDIT</code> can be set to <code>no</code> at the beginning of them.</dl>
<p> &#8211;cleanup=&lt;mode&gt;</p>
<dl>
<dt>
<dd> This option determines how the merge message will be cleaned up before committing. See <code><a href="/docs/linux/man/1-git-commit/">git-commit</a></code>(1) for more details. In addition, if the <i>&lt;mode&gt;</i> is given a value of <code>scissors</code>, scissors will be appended to <code>MERGE_MSG</code> before being passed on to the commit machinery in the case of a merge conflict.</dl>
<p> &#8211;ff-only</p>
<dl>
<dt>
<dd> Only update to the new history if there is no divergent local history. This is the default when no method for reconciling divergent histories is provided (via the &#8211;rebase=* flags).</dl>
<p> &#8211;ff, &#8211;no-ff</p>
<dl>
<dt>
<dd> When merging rather than rebasing, specifies how a merge is handled when the merged-in history is already a descendant of the current history. If merging is requested, <code>&#8211;ff</code> is the default unless merging an annotated (and possibly signed) tag that is not stored in its natural place in the <code>refs/tags/</code> hierarchy, in which case <code>&#8211;no-ff</code> is assumed. </p>
<p> With <code>&#8211;ff</code>, when possible resolve the merge as a fast-forward (only update the branch pointer to match the merged branch; do not create a merge commit). When not possible (when the merged-in history is not a descendant of the current history), create a merge commit. </p>
<p> With <code>&#8211;no-ff</code>, create a merge commit in all cases, even when the merge could instead be resolved as a fast-forward.</dl>
<p> -S[&lt;keyid&gt;], &#8211;gpg-sign[=&lt;keyid&gt;], &#8211;no-gpg-sign</p>
<dl>
<dt>
<dd> GPG-sign the resulting merge commit. The <code>keyid</code> argument is optional and defaults to the committer identity; if specified, it must be stuck to the option without a space. <code>&#8211;no-gpg-sign</code> is useful to countermand both <code>commit.gpgSign</code> configuration variable, and earlier <code>&#8211;gpg-sign</code>.</dl>
<p> &#8211;log[=&lt;n&gt;], &#8211;no-log</p>
<dl>
<dt>
<dd> In addition to branch names, populate the log message with one-line descriptions from at most &lt;n&gt; actual commits that are being merged. See also <code><a href="/docs/linux/man/1-git-fmt-merge-msg/">git-fmt-merge-msg</a></code>(1). Only useful when merging. </p>
<p> With &#8211;no-log do not list one-line descriptions from the actual commits being merged.</dl>
<p> &#8211;signoff, &#8211;no-signoff</p>
<dl>
<dt>
<dd> Add a <code>Signed-off-by</code> trailer by the committer at the end of the commit log message. The meaning of a signoff depends on the project to which you&#8217;re committing. For example, it may certify that the committer has the rights to submit the work under the project&#8217;s license or agrees to some contributor representation, such as a Developer Certificate of Origin. (See m[blue]<code><a rel="nofollow" href="http://developercertificate.org">http://developercertificate.org</a></code>m[] for the one used by the Linux kernel and Git projects.) Consult the documentation or leadership of the project to which you&#8217;re contributing to understand how the signoffs are used in that project. </p>
<p> The &#8211;no-signoff option can be used to countermand an earlier &#8211;signoff option on the command line.</dl>
<p> &#8211;stat, -n, &#8211;no-stat</p>
<dl>
<dt>
<dd> Show a diffstat at the end of the merge. The diffstat is also controlled by the configuration option merge.stat. </p>
<p> With -n or &#8211;no-stat do not show a diffstat at the end of the merge.</dl>
<p> &#8211;squash, &#8211;no-squash</p>
<dl>
<dt>
<dd> Produce the working tree and index state as if a real merge happened (except for the merge information), but do not actually make a commit, move the <code>HEAD</code>, or record <code>$GIT_DIR/MERGE_HEAD</code> (to cause the next <code>git commit</code> command to create a merge commit). This allows you to create a single commit on top of the current branch whose effect is the same as merging another branch (or more in case of an octopus). </p>
<p> With &#8211;no-squash perform the merge and commit the result. This option can be used to override &#8211;squash. </p>
<p> With &#8211;squash, &#8211;commit is not allowed, and will fail. </p>
<p> Only useful when merging.</dl>
<p> &#8211;[no-]verify</p>
<dl>
<dt>
<dd> By default, the pre-merge and commit-msg hooks are run. When <code>&#8211;no-verify</code> is given, these are bypassed. See also <code><a href="/docs/linux/man/5-githooks/">githooks</a></code>(5). Only useful when merging.</dl>
<p> -s &lt;strategy&gt;, &#8211;strategy=&lt;strategy&gt;</p>
<dl>
<dt>
<dd> Use the given merge strategy; can be supplied more than once to specify them in the order they should be tried. If there is no <code>-s</code> option, a built-in list of strategies is used instead (<code>ort</code> when merging a single head, <code>octopus</code> otherwise).</dl>
<p> -X &lt;option&gt;, &#8211;strategy-option=&lt;option&gt;</p>
<dl>
<dt>
<dd> Pass merge strategy specific option through to the merge strategy.</dl>
<p> &#8211;verify-signatures, &#8211;no-verify-signatures</p>
<dl>
<dt>
<dd> Verify that the tip commit of the side branch being merged is signed with a valid key, i.e. a key that has a valid uid: in the default trust model, this means the signing key has been signed by a trusted key. If the tip commit of the side branch is not signed with a valid key, the merge is aborted. </p>
<p> Only useful when merging.</dl>
<p> &#8211;summary, &#8211;no-summary</p>
<dl>
<dt>
<dd> Synonyms to &#8211;stat and &#8211;no-stat; these are deprecated and will be removed in the future.</dl>
<p> &#8211;autostash, &#8211;no-autostash</p>
<dl>
<dt>
<dd> Automatically create a temporary stash entry before the operation begins, record it in the special ref <code>MERGE_AUTOSTASH</code> and apply it after the operation ends. This means that you can run the operation on a dirty worktree. However, use with care: the final stash application after a successful merge might result in non-trivial conflicts.</dl>
<p> &#8211;allow-unrelated-histories</p>
<dl>
<dt>
<dd> By default, <code>git merge</code> command refuses to merge histories that do not share a common ancestor. This option can be used to override this safety when merging histories of two projects that started their lives independently. As that is a very rare occasion, no configuration variable to enable this by default exists and will not be added. </p>
<p> Only useful when merging.</dl>
<p> -r, &#8211;rebase[=false|true|merges|interactive]</p>
<dl>
<dt>
<dd> When true, rebase the current branch on top of the upstream branch after fetching. If there is a remote-tracking branch corresponding to the upstream branch and the upstream branch was rebased since last fetched, the rebase uses that information to avoid rebasing non-local changes. </p>
<p> When set to <code>merges</code>, rebase using <code>git rebase &#8211;rebase-merges</code> so that the local merge commits are included in the rebase (see <code><a href="/docs/linux/man/1-git-rebase/">git-rebase</a></code>(1) for details). </p>
<p> When false, merge the upstream branch into the current branch. </p>
<p> When <code>interactive</code>, enable the interactive mode of rebase. </p>
<p> See <code>pull.rebase</code>, <code>branch.&lt;name&gt;.rebase</code> and <code>branch.autoSetupRebase</code> in <code><a href="/docs/linux/man/1-git-config/">git-config</a></code>(1) if you want to make <code>git pull</code> always use <code>&#8211;rebase</code> instead of merging. </p>
<dl>
<dt>
<dd>
 <font SIZE="+1"> <code>Note</code> </font><br />
 This is a potentially <i>dangerous</i> mode of operation. It rewrites history, which does not bode well when you published that history already. Do <code>not</code> use this option unless you have read <code><a href="/docs/linux/man/1-git-rebase/">git-rebase</a></code>(1) carefully. </p>
</dl>
</dl>
<p> &#8211;no-rebase</p>
<dl>
<dt>
<dd> This is shorthand for &#8211;rebase=false.</dl>
<h3>Options related to fetching</h3>
<p> &#8211;all</p>
<dl>
<dt>
<dd> Fetch all remotes.</dl>
<p> -a, &#8211;append</p>
<dl>
<dt>
<dd> Append ref names and object names of fetched refs to the existing contents of <code>.git/FETCH_HEAD</code>. Without this option old data in <code>.git/FETCH_HEAD</code> will be overwritten.</dl>
<p> &#8211;atomic</p>
<dl>
<dt>
<dd> Use an atomic transaction to update local refs. Either all refs are updated, or on error, no refs are updated.</dl>
<p> &#8211;depth=&lt;depth&gt;</p>
<dl>
<dt>
<dd> Limit fetching to the specified number of commits from the tip of each remote branch history. If fetching to a <i>shallow</i> repository created by <code>git clone</code> with <code>&#8211;depth=&lt;depth&gt;</code> option (see <code><a href="/docs/linux/man/1-git-clone/">git-clone</a></code>(1)), deepen or shorten the history to the specified number of commits. Tags for the deepened commits are not fetched.</dl>
<p> &#8211;deepen=&lt;depth&gt;</p>
<dl>
<dt>
<dd> Similar to &#8211;depth, except it specifies the number of commits from the current shallow boundary instead of from the tip of each remote branch history.</dl>
<p> &#8211;shallow-since=&lt;date&gt;</p>
<dl>
<dt>
<dd> Deepen or shorten the history of a shallow repository to include all reachable commits after &lt;date&gt;.</dl>
<p> &#8211;shallow-exclude=&lt;revision&gt;</p>
<dl>
<dt>
<dd> Deepen or shorten the history of a shallow repository to exclude commits reachable from a specified remote branch or tag. This option can be specified multiple times.</dl>
<p> &#8211;unshallow</p>
<dl>
<dt>
<dd> If the source repository is complete, convert a shallow repository to a complete one, removing all the limitations imposed by shallow repositories. </p>
<p> If the source repository is shallow, fetch as much as possible so that the current repository has the same history as the source repository.</dl>
<p> &#8211;update-shallow</p>
<dl>
<dt>
<dd> By default when fetching from a shallow repository, <code>git fetch</code> refuses refs that require updating .git/shallow. This option updates .git/shallow and accept such refs.</dl>
<p> &#8211;negotiation-tip=&lt;commit|glob&gt;</p>
<dl>
<dt>
<dd> By default, Git will report, to the server, commits reachable from all local refs to find common commits in an attempt to reduce the size of the to-be-received packfile. If specified, Git will only report commits reachable from the given tips. This is useful to speed up fetches when the user knows which local ref is likely to have commits in common with the upstream ref being fetched. </p>
<p> This option may be specified more than once; if so, Git will report commits reachable from any of the given commits. </p>
<p> The argument to this option may be a glob on ref names, a ref, or the (possibly abbreviated) SHA-1 of a commit. Specifying a glob is equivalent to specifying this option multiple times, one for each matching ref name. </p>
<p> See also the <code>fetch.negotiationAlgorithm</code> and <code>push.negotiate</code> configuration variables documented in <code><a href="/docs/linux/man/1-git-config/">git-config</a></code>(1), and the <code>&#8211;negotiate-only</code> option below.</dl>
<p> &#8211;negotiate-only</p>
<dl>
<dt>
<dd> Do not fetch anything from the server, and instead print the ancestors of the provided <code>&#8211;negotiation-tip=*</code> arguments, which we have in common with the server. </p>
<p> Internally this is used to implement the <code>push.negotiate</code> option, see <code><a href="/docs/linux/man/1-git-config/">git-config</a></code>(1).</dl>
<p> &#8211;dry-run</p>
<dl>
<dt>
<dd> Show what would be done, without making any changes.</dl>
<p> -f, &#8211;force</p>
<dl>
<dt>
<dd> When <i>git fetch</i> is used with <code>&lt;src&gt;:&lt;dst&gt;</code> refspec it may refuse to update the local branch as discussed in the <code>&lt;refspec&gt;</code> part of the <code><a href="/docs/linux/man/1-git-fetch/">git-fetch</a></code>(1) documentation. This option overrides that check.</dl>
<p> -k, &#8211;keep</p>
<dl>
<dt>
<dd> Keep downloaded pack.</dl>
<p> &#8211;prefetch</p>
<dl>
<dt>
<dd> Modify the configured refspec to place all refs into the <code>refs/prefetch/</code> namespace. See the <code>prefetch</code> task in <code><a href="/docs/linux/man/1-git-maintenance/">git-maintenance</a></code>(1).</dl>
<p> -p, &#8211;prune</p>
<dl>
<dt>
<dd> Before fetching, remove any remote-tracking references that no longer exist on the remote. Tags are not subject to pruning if they are fetched only because of the default tag auto-following or due to a &#8211;tags option. However, if tags are fetched due to an explicit refspec (either on the command line or in the remote configuration, for example if the remote was cloned with the &#8211;mirror option), then they are also subject to pruning. Supplying <code>&#8211;prune-tags</code> is a shorthand for providing the tag refspec.</dl>
<p> &#8211;no-tags</p>
<dl>
<dt>
<dd> By default, tags that point at objects that are downloaded from the remote repository are fetched and stored locally. This option disables this automatic tag following. The default behavior for a remote may be specified with the remote.&lt;name&gt;.tagOpt setting. See <code><a href="/docs/linux/man/1-git-config/">git-config</a></code>(1).</dl>
<p> &#8211;refmap=&lt;refspec&gt;</p>
<dl>
<dt>
<dd> When fetching refs listed on the command line, use the specified refspec (can be given more than once) to map the refs to remote-tracking branches, instead of the values of <code>remote.*.fetch</code> configuration variables for the remote repository. Providing an empty <code>&lt;refspec&gt;</code> to the <code>&#8211;refmap</code> option causes Git to ignore the configured refspecs and rely entirely on the refspecs supplied as command-line arguments. See section on &quot;Configured Remote-tracking Branches&quot; for details.</dl>
<p> -t, &#8211;tags</p>
<dl>
<dt>
<dd> Fetch all tags from the remote (i.e., fetch remote tags <code>refs/tags/*</code> into local tags with the same name), in addition to whatever else would otherwise be fetched. Using this option alone does not subject tags to pruning, even if &#8211;prune is used (though tags may be pruned anyway if they are also the destination of an explicit refspec; see <code>&#8211;prune</code>).</dl>
<p> -j, &#8211;jobs=&lt;n&gt;</p>
<dl>
<dt>
<dd> Number of parallel children to be used for all forms of fetching. </p>
<p> If the <code>&#8211;multiple</code> option was specified, the different remotes will be fetched in parallel. If multiple submodules are fetched, they will be fetched in parallel. To control them independently, use the config settings <code>fetch.parallel</code> and <code>submodule.fetchJobs</code> (see <code><a href="/docs/linux/man/1-git-config/">git-config</a></code>(1)). </p>
<p> Typically, parallel recursive and multi-remote fetches will be faster. By default fetches are performed sequentially, not in parallel.</dl>
<p> &#8211;set-upstream</p>
<dl>
<dt>
<dd> If the remote is fetched successfully, add upstream (tracking) reference, used by argument-less <code><a href="/docs/linux/man/1-git-pull/">git-pull</a></code>(1) and other commands. For more information, see <code>branch.&lt;name&gt;.merge</code> and <code>branch.&lt;name&gt;.remote</code> in <code><a href="/docs/linux/man/1-git-config/">git-config</a></code>(1).</dl>
<p> &#8211;upload-pack &lt;upload-pack&gt;</p>
<dl>
<dt>
<dd> When given, and the repository to fetch from is handled by <i>git fetch-pack</i>, <code>&#8211;exec=&lt;upload-pack&gt;</code> is passed to the command to specify non-default path for the command run on the other end.</dl>
<p> &#8211;progress</p>
<dl>
<dt>
<dd> Progress status is reported on the standard error stream by default when it is attached to a terminal, unless -q is specified. This flag forces progress status even if the standard error stream is not directed to a terminal.</dl>
<p> -o &lt;option&gt;, &#8211;server-option=&lt;option&gt;</p>
<dl>
<dt>
<dd> Transmit the given string to the server when communicating using protocol version 2. The given string must not contain a NUL or LF character. The server&#8217;s handling of server options, including unknown ones, is server-specific. When multiple <code>&#8211;server-option=&lt;option&gt;</code> are given, they are all sent to the other side in the order listed on the command line.</dl>
<p> &#8211;show-forced-updates</p>
<dl>
<dt>
<dd> By default, git checks if a branch is force-updated during fetch. This can be disabled through fetch.showForcedUpdates, but the &#8211;show-forced-updates option guarantees this check occurs. See <code><a href="/docs/linux/man/1-git-config/">git-config</a></code>(1).</dl>
<p> &#8211;no-show-forced-updates</p>
<dl>
<dt>
<dd> By default, git checks if a branch is force-updated during fetch. Pass &#8211;no-show-forced-updates or set fetch.showForcedUpdates to false to skip this check for performance reasons. If used during <i>git-pull</i> the &#8211;ff-only option will still check for forced updates before attempting a fast-forward update. See <code><a href="/docs/linux/man/1-git-config/">git-config</a></code>(1).</dl>
<p> -4, &#8211;ipv4</p>
<dl>
<dt>
<dd> Use IPv4 addresses only, ignoring IPv6 addresses.</dl>
<p> -6, &#8211;ipv6</p>
<dl>
<dt>
<dd> Use IPv6 addresses only, ignoring IPv4 addresses.</dl>
<p> &lt;repository&gt;</p>
<dl>
<dt>
<dd> The &quot;remote&quot; repository that is the source of a fetch or pull operation. This parameter can be either a URL (see the section GIT URLS below) or the name of a remote (see the section REMOTES below).</dl>
<p> &lt;refspec&gt;</p>
<dl>
<dt>
<dd> Specifies which refs to fetch and which local refs to update. When no &lt;refspec&gt;s appear on the command line, the refs to fetch are read from <code>remote.&lt;repository&gt;.fetch</code> variables instead (see the section &quot;CONFIGURED REMOTE-TRACKING BRANCHES&quot; in <code><a href="/docs/linux/man/1-git-fetch/">git-fetch</a></code>(1)). </p>
<p> The format of a &lt;refspec&gt; parameter is an optional plus <code>+</code>, followed by the source &lt;src&gt;, followed by a colon <code>:</code>, followed by the destination ref &lt;dst&gt;. The colon can be omitted when &lt;dst&gt; is empty. &lt;src&gt; is typically a ref, but it can also be a fully spelled hex object name. </p>
<p> A &lt;refspec&gt; may contain a <code>*</code> in its &lt;src&gt; to indicate a simple pattern match. Such a refspec functions like a glob that matches any ref with the same prefix. A pattern &lt;refspec&gt; must have a <code>*</code> in both the &lt;src&gt; and &lt;dst&gt;. It will map refs to the destination by replacing the <code>*</code> with the contents matched from the source. </p>
<p> If a refspec is prefixed by <code>^</code>, it will be interpreted as a negative refspec. Rather than specifying which refs to fetch or which local refs to update, such a refspec will instead specify refs to exclude. A ref will be considered to match if it matches at least one positive refspec, and does not match any negative refspec. Negative refspecs can be useful to restrict the scope of a pattern refspec so that it will not include specific refs. Negative refspecs can themselves be pattern refspecs. However, they may only contain a &lt;src&gt; and do not specify a &lt;dst&gt;. Fully spelled out hex object names are also not supported. </p>
<p> <code>tag &lt;tag&gt;</code> means the same as <code>refs/tags/&lt;tag&gt;:refs/tags/&lt;tag&gt;</code>; it requests fetching everything up to the given tag. </p>
<p> The remote ref that matches &lt;src&gt; is fetched, and if &lt;dst&gt; is not an empty string, an attempt is made to update the local ref that matches it. </p>
<p> Whether that update is allowed without <code>&#8211;force</code> depends on the ref namespace it&#8217;s being fetched to, the type of object being fetched, and whether the update is considered to be a fast-forward. Generally, the same rules apply for fetching as when pushing, see the <code>&lt;refspec&gt;&#8230;</code> section of <code><a href="/docs/linux/man/1-git-push/">git-push</a></code>(1) for what those are. Exceptions to those rules particular to <i>git fetch</i> are noted below. </p>
<p> Until Git version 2.20, and unlike when pushing with <code><a href="/docs/linux/man/1-git-push/">git-push</a></code>(1), any updates to <code>refs/tags/*</code> would be accepted without <code>+</code> in the refspec (or <code>&#8211;force</code>). When fetching, we promiscuously considered all tag updates from a remote to be forced fetches. Since Git version 2.20, fetching to update <code>refs/tags/*</code> works the same way as when pushing. I.e. any updates will be rejected without <code>+</code> in the refspec (or <code>&#8211;force</code>). </p>
<p> Unlike when pushing with <code><a href="/docs/linux/man/1-git-push/">git-push</a></code>(1), any updates outside of <code>refs/{tags,heads}/*</code> will be accepted without <code>+</code> in the refspec (or <code>&#8211;force</code>), whether that&#8217;s swapping e.g. a tree object for a blob, or a commit for another commit that&#8217;s doesn&#8217;t have the previous commit as an ancestor etc. </p>
<p> Unlike when pushing with <code><a href="/docs/linux/man/1-git-push/">git-push</a></code>(1), there is no configuration which&#8217;ll amend these rules, and nothing like a <code>pre-fetch</code> hook analogous to the <code>pre-receive</code> hook. </p>
<p> As with pushing with <code><a href="/docs/linux/man/1-git-push/">git-push</a></code>(1), all of the rules described above about what&#8217;s not allowed as an update can be overridden by adding an the optional leading <code>+</code> to a refspec (or using <code>&#8211;force</code> command line option). The only exception to this is that no amount of forcing will make the <code>refs/heads/*</code> namespace accept a non-commit object. </p>
<dl>
<dt>
<dd>
 <font SIZE="+1"> <code>Note</code> </font><br />
 When the remote branch you want to fetch is known to be rewound and rebased regularly, it is expected that its new tip will not be descendant of its previous tip (as stored in your remote-tracking branch the last time you fetched). You would want to use the <code>+</code> sign to indicate non-fast-forward updates will be needed for such branches. There is no way to determine or declare that a branch will be made available in a repository with this behavior; the pulling user simply must know this is the expected usage pattern for a branch. </p>
</dl>
<dl>
<dt>
<dd>
 <font SIZE="+1"> <code>Note</code> </font><br />
 There is a difference between listing multiple &lt;refspec&gt; directly on <i>git pull</i> command line and having multiple <code>remote.&lt;repository&gt;.fetch</code> entries in your configuration for a &lt;repository&gt; and running a <i>git pull</i> command without any explicit &lt;refspec&gt; parameters. &lt;refspec&gt;s listed explicitly on the command line are always merged into the current branch after fetching. In other words, if you list more than one remote ref, <i>git pull</i> will create an Octopus merge. On the other hand, if you do not list any explicit &lt;refspec&gt; parameter on the command line, <i>git pull</i> will fetch all the &lt;refspec&gt;s it finds in the <code>remote.&lt;repository&gt;.fetch</code> configuration and merge only the first &lt;refspec&gt; found into the current branch. This is because making an Octopus from remote refs is rarely done, while keeping track of multiple remote heads in one-go by fetching more than one is often useful. </p>
</dl>
</dl>
<h2>GIT URLS</h2>
<p> In general, URLs contain information about the transport protocol, the address of the remote server, and the path to the repository. Depending on the transport protocol, some of this information may be absent. </p>
<p> Git supports ssh, git, http, and https protocols (in addition, ftp, and ftps can be used for fetching, but this is inefficient and deprecated; do not use it). </p>
<p> The native transport (i.e. git:// URL) does no authentication and should be used with caution on unsecured networks. </p>
<p> The following syntaxes may be used with them: </p>
<dl>
<dt>
<dd> &bull; <a href="ssh://[user@]host.xz[:port]/path/to/repo.git/">ssh://[user@]host.xz[:port]/path/to/repo.git/</a></dl>
<dl>
<dt>
<dd> &bull; <a href="git://host.xz[:port]/path/to/repo.git/">git://host.xz[:port]/path/to/repo.git/</a></dl>
<dl>
<dt>
<dd> &bull; http[s]://host.xz[:port]/path/to/repo.git/</dl>
<dl>
<dt>
<dd> &bull; ftp[s]://host.xz[:port]/path/to/repo.git/</dl>
<p> An alternative scp-like syntax may also be used with the ssh protocol: </p>
<dl>
<dt>
<dd> &bull; [user@]host.xz:path/to/repo.git/</dl>
<p> This syntax is only recognized if there are no slashes before the first colon. This helps differentiate a local path that contains a colon. For example the local path <code>foo:bar</code> could be specified as an absolute path or <code>./foo:bar</code> to avoid being misinterpreted as an ssh url. </p>
<p> The ssh and git protocols additionally support ~username expansion: </p>
<dl>
<dt>
<dd> &bull; <a href="ssh://[user@]host.xz[:port]/~[user]/path/to/repo.git/">ssh://[user@]host.xz[:port]/~[user]/path/to/repo.git/</a></dl>
<dl>
<dt>
<dd> &bull; <a href="git://host.xz[:port]/~[user]/path/to/repo.git/">git://host.xz[:port]/~[user]/path/to/repo.git/</a></dl>
<dl>
<dt>
<dd> &bull; [user@]host.xz:/~[user]/path/to/repo.git/</dl>
<p> For local repositories, also supported by Git natively, the following syntaxes may be used: </p>
<dl>
<dt>
<dd> &bull; /path/to/repo.git/</dl>
<dl>
<dt>
<dd> &bull; file:///path/to/repo.git/</dl>
<p> These two syntaxes are mostly equivalent, except when cloning, when the former implies &#8211;local option. See <code><a href="/docs/linux/man/1-git-clone/">git-clone</a></code>(1) for details. </p>
<p> <i>git clone</i>, <i>git fetch</i> and <i>git pull</i>, but not <i>git push</i>, will also accept a suitable bundle file. See <code><a href="/docs/linux/man/1-git-bundle/">git-bundle</a></code>(1). </p>
<p> When Git doesn&#8217;t know how to handle a certain transport protocol, it attempts to use the <i>remote-&lt;transport&gt;</i> remote helper, if one exists. To explicitly request a remote helper, the following syntax may be used: </p>
<dl>
<dt>
<dd> &bull; &lt;transport&gt;::&lt;address&gt;</dl>
<p> where &lt;address&gt; may be a path, a server and path, or an arbitrary URL-like string recognized by the specific remote helper being invoked. See <code><a href="/docs/linux/man/7-gitremote-helpers/">gitremote-helpers</a></code>(7) for details. </p>
<p> If there are a large number of similarly-named remote repositories and you want to use a different format for them (such that the URLs you use will be rewritten into URLs that work), you can create a configuration section of the form: </p>
<dl>
<dt>
<dd>
<pre>
        [url &quot;&lt;actual url base&gt;&quot;]
                insteadOf = &lt;other url base&gt;
</pre>
</dl>
<p> For example, with this: </p>
<dl>
<dt>
<dd>
<pre>
        [url &quot;<a href="git://git.host.xz/">git://git.host.xz/</a>&quot;]
                insteadOf = host.xz:/path/to/
                insteadOf = work:
</pre>
</dl>
<p> a URL like &quot;work:repo.git&quot; or like &quot;host.xz:/path/to/repo.git&quot; will be rewritten in any context that takes a URL to be &quot;<a href="git://git.host.xz/repo.git">git://git.host.xz/repo.git</a>&quot;. </p>
<p> If you want to rewrite URLs for push only, you can create a configuration section of the form: </p>
<dl>
<dt>
<dd>
<pre>
        [url &quot;&lt;actual url base&gt;&quot;]
                pushInsteadOf = &lt;other url base&gt;
</pre>
</dl>
<p> For example, with this: </p>
<dl>
<dt>
<dd>
<pre>
        [url &quot;<a href="ssh://example.org/">ssh://example.org/</a>&quot;]
                pushInsteadOf = <a href="git://example.org/">git://example.org/</a>
</pre>
</dl>
<p> a URL like &quot;<a href="git://example.org/path/to/repo.git">git://example.org/path/to/repo.git</a>&quot; will be rewritten to &quot;<a href="ssh://example.org/path/to/repo.git">ssh://example.org/path/to/repo.git</a>&quot; for pushes, but pulls will still use the original URL.</p>
<h2>REMOTES</h2>
<p> The name of one of the following can be used instead of a URL as <code>&lt;repository&gt;</code> argument: </p>
<dl>
<dt>
<dd> &bull; a remote in the Git configuration file: <code>$GIT_DIR/config</code>,</dl>
<dl>
<dt>
<dd> &bull; a file in the <code>$GIT_DIR/remotes</code> directory, or</dl>
<dl>
<dt>
<dd> &bull; a file in the <code>$GIT_DIR/branches</code> directory.</dl>
<p> All of these also allow you to omit the refspec from the command line because they each contain a refspec which git will use by default.</p>
<h3>Named remote in configuration file</h3>
<p> You can choose to provide the name of a remote which you had previously configured using <code><a href="/docs/linux/man/1-git-remote/">git-remote</a></code>(1), <code><a href="/docs/linux/man/1-git-config/">git-config</a></code>(1) or even by a manual edit to the <code>$GIT_DIR/config</code> file. The URL of this remote will be used to access the repository. The refspec of this remote will be used by default when you do not provide a refspec on the command line. The entry in the config file would appear like this: </p>
<dl>
<dt>
<dd>
<pre>
        [remote &quot;&lt;name&gt;&quot;]
                url = &lt;url&gt;
                pushurl = &lt;pushurl&gt;
                push = &lt;refspec&gt;
                fetch = &lt;refspec&gt;
</pre>
</dl>
<p> The <code>&lt;pushurl&gt;</code> is used for pushes only. It is optional and defaults to <code>&lt;url&gt;</code>.</p>
<h3>Named file in <code>$GIT_DIR/remotes</code></h3>
<p> You can choose to provide the name of a file in <code>$GIT_DIR/remotes</code>. The URL in this file will be used to access the repository. The refspec in this file will be used as default when you do not provide a refspec on the command line. This file should have the following format: </p>
<dl>
<dt>
<dd>
<pre>
        URL: one of the above URL format
        Push: &lt;refspec&gt;
        Pull: &lt;refspec&gt;
</pre>
</dl>
<p> <code>Push:</code> lines are used by <i>git push</i> and <code>Pull:</code> lines are used by <i>git pull</i> and <i>git fetch</i>. Multiple <code>Push:</code> and <code>Pull:</code> lines may be specified for additional branch mappings.</p>
<h3>Named file in <code>$GIT_DIR/branches</code></h3>
<p> You can choose to provide the name of a file in <code>$GIT_DIR/branches</code>. The URL in this file will be used to access the repository. This file should have the following format: </p>
<dl>
<dt>
<dd>
<pre>
        &lt;url&gt;#&lt;head&gt;
</pre>
</dl>
<p> <code>&lt;url&gt;</code> is required; <code>#&lt;head&gt;</code> is optional. </p>
<p> Depending on the operation, git will use one of the following refspecs, if you don&#8217;t provide one on the command line. <code>&lt;branch&gt;</code> is the name of this file in <code>$GIT_DIR/branches</code> and <code>&lt;head&gt;</code> defaults to <code>master</code>. </p>
<p> git fetch uses: </p>
<dl>
<dt>
<dd>
<pre>
        refs/heads/&lt;head&gt;:refs/heads/&lt;branch&gt;
</pre>
</dl>
<p> git push uses: </p>
<dl>
<dt>
<dd>
<pre>
        HEAD:refs/heads/&lt;head&gt;
</pre>
</dl>
<h2>MERGE STRATEGIES</h2>
<p> The merge mechanism (<code>git merge</code> and <code>git pull</code> commands) allows the backend <i>merge strategies</i> to be chosen with <code>-s</code> option. Some strategies can also take their own options, which can be passed by giving <code>-X&lt;option&gt;</code> arguments to <code>git merge</code> and/or <code>git pull</code>. </p>
<p> ort</p>
<dl>
<dt>
<dd> This is the default merge strategy when pulling or merging one branch. This strategy can only resolve two heads using a 3-way merge algorithm. When there is more than one common ancestor that can be used for 3-way merge, it creates a merged tree of the common ancestors and uses that as the reference tree for the 3-way merge. This has been reported to result in fewer merge conflicts without causing mismerges by tests done on actual merge commits taken from Linux 2.6 kernel development history. Additionally this strategy can detect and handle merges involving renames. It does not make use of detected copies. The name for this algorithm is an acronym (&quot;Ostensibly Recursive&#8217;s Twin&quot;) and came from the fact that it was written as a replacement for the previous default algorithm, <code>recursive</code>. </p>
<p> The <i>ort</i> strategy can take the following options: </p>
<p> ours</p>
<dl>
<dt>
<dd> This option forces conflicting hunks to be auto-resolved cleanly by favoring <i>our</i> version. Changes from the other tree that do not conflict with our side are reflected in the merge result. For a binary file, the entire contents are taken from our side. </p>
<p> This should not be confused with the <i>ours</i> merge strategy, which does not even look at what the other tree contains at all. It discards everything the other tree did, declaring <i>our</i> history contains all that happened in it.</dl>
<p> theirs</p>
<dl>
<dt>
<dd> This is the opposite of <i>ours</i>; note that, unlike <i>ours</i>, there is no <i>theirs</i> merge strategy to confuse this merge option with.</dl>
<p> ignore-space-change, ignore-all-space, ignore-space-at-eol, ignore-cr-at-eol</p>
<dl>
<dt>
<dd> Treats lines with the indicated type of whitespace change as unchanged for the sake of a three-way merge. Whitespace changes mixed with other changes to a line are not ignored. See also <code><a href="/docs/linux/man/1-git-diff/">git-diff</a></code>(1) <code>-b</code>, <code>-w</code>, <code>&#8211;ignore-space-at-eol</code>, and <code>&#8211;ignore-cr-at-eol</code>. </p>
<dl>
<dt>
<dd> &bull; If <i>their</i> version only introduces whitespace changes to a line, <i>our</i> version is used;</dl>
<dl>
<dt>
<dd> &bull; If <i>our</i> version introduces whitespace changes but <i>their</i> version includes a substantial change, <i>their</i> version is used;</dl>
<dl>
<dt>
<dd> &bull; Otherwise, the merge proceeds in the usual way.</dl>
</dl>
<p> renormalize</p>
<dl>
<dt>
<dd> This runs a virtual check-out and check-in of all three stages of a file when resolving a three-way merge. This option is meant to be used when merging branches with different clean filters or end-of-line normalization rules. See &quot;Merging branches with differing checkin/checkout attributes&quot; in <code><a href="/docs/linux/man/5-gitattributes/">gitattributes</a></code>(5) for details.</dl>
<p> no-renormalize</p>
<dl>
<dt>
<dd> Disables the <code>renormalize</code> option. This overrides the <code>merge.renormalize</code> configuration variable.</dl>
<p> find-renames[=&lt;n&gt;]</p>
<dl>
<dt>
<dd> Turn on rename detection, optionally setting the similarity threshold. This is the default. This overrides the <i>merge.renames</i> configuration variable. See also <code><a href="/docs/linux/man/1-git-diff/">git-diff</a></code>(1) <code>&#8211;find-renames</code>.</dl>
<p> rename-threshold=&lt;n&gt;</p>
<dl>
<dt>
<dd> Deprecated synonym for <code>find-renames=&lt;n&gt;</code>.</dl>
<p> subtree[=&lt;path&gt;]</p>
<dl>
<dt>
<dd> This option is a more advanced form of <i>subtree</i> strategy, where the strategy makes a guess on how two trees must be shifted to match with each other when merging. Instead, the specified path is prefixed (or stripped from the beginning) to make the shape of two trees to match.</dl>
</dl>
<p> recursive</p>
<dl>
<dt>
<dd> This can only resolve two heads using a 3-way merge algorithm. When there is more than one common ancestor that can be used for 3-way merge, it creates a merged tree of the common ancestors and uses that as the reference tree for the 3-way merge. This has been reported to result in fewer merge conflicts without causing mismerges by tests done on actual merge commits taken from Linux 2.6 kernel development history. Additionally this can detect and handle merges involving renames. It does not make use of detected copies. This was the default strategy for resolving two heads from Git v0.99.9k until v2.33.0. </p>
<p> The <i>recursive</i> strategy takes the same options as <i>ort</i>. However, there are three additional options that <i>ort</i> ignores (not documented above) that are potentially useful with the <i>recursive</i> strategy: </p>
<p> patience</p>
<dl>
<dt>
<dd> Deprecated synonym for <code>diff-algorithm=patience</code>.</dl>
<p> diff-algorithm=[patience|minimal|histogram|myers]</p>
<dl>
<dt>
<dd> Use a different diff algorithm while merging, which can help avoid mismerges that occur due to unimportant matching lines (such as braces from distinct functions). See also <code><a href="/docs/linux/man/1-git-diff/">git-diff</a></code>(1) <code>&#8211;diff-algorithm</code>. Note that <code>ort</code> specifically uses <code>diff-algorithm=histogram</code>, while <code>recursive</code> defaults to the <code>diff.algorithm</code> config setting.</dl>
<p> no-renames</p>
<dl>
<dt>
<dd> Turn off rename detection. This overrides the <code>merge.renames</code> configuration variable. See also <code><a href="/docs/linux/man/1-git-diff/">git-diff</a></code>(1) <code>&#8211;no-renames</code>.</dl>
</dl>
<p> resolve</p>
<dl>
<dt>
<dd> This can only resolve two heads (i.e. the current branch and another branch you pulled from) using a 3-way merge algorithm. It tries to carefully detect criss-cross merge ambiguities. It does not handle renames.</dl>
<p> octopus</p>
<dl>
<dt>
<dd> This resolves cases with more than two heads, but refuses to do a complex merge that needs manual resolution. It is primarily meant to be used for bundling topic branch heads together. This is the default merge strategy when pulling or merging more than one branch.</dl>
<p> ours</p>
<dl>
<dt>
<dd> This resolves any number of heads, but the resulting tree of the merge is always that of the current branch head, effectively ignoring all changes from all other branches. It is meant to be used to supersede old development history of side branches. Note that this is different from the -Xours option to the <i>recursive</i> merge strategy.</dl>
<p> subtree</p>
<dl>
<dt>
<dd> This is a modified <code>ort</code> strategy. When merging trees A and B, if B corresponds to a subtree of A, B is first adjusted to match the tree structure of A, instead of reading the trees at the same level. This adjustment is also done to the common ancestor tree.</dl>
<p> With the strategies that use 3-way merge (including the default, <i>ort</i>), if a change is made on both branches, but later reverted on one of the branches, that change will be present in the merged result; some people find this behavior confusing. It occurs because only the heads and the merge base are considered when performing a merge, not the individual commits. The merge algorithm therefore considers the reverted change as no change at all, and substitutes the changed version instead.</p>
<h2>DEFAULT BEHAVIOUR</h2>
<p> Often people use <code>git pull</code> without giving any parameter. Traditionally, this has been equivalent to saying <code>git pull origin</code>. However, when configuration <code>branch.&lt;name&gt;.remote</code> is present while on branch <code>&lt;name&gt;</code>, that value is used instead of <code>origin</code>. </p>
<p> In order to determine what URL to use to fetch from, the value of the configuration <code>remote.&lt;origin&gt;.url</code> is consulted and if there is not any such variable, the value on the <code>URL:</code> line in <code>$GIT_DIR/remotes/&lt;origin&gt;</code> is used. </p>
<p> In order to determine what remote branches to fetch (and optionally store in the remote-tracking branches) when the command is run without any refspec parameters on the command line, values of the configuration variable <code>remote.&lt;origin&gt;.fetch</code> are consulted, and if there aren&#8217;t any, <code>$GIT_DIR/remotes/&lt;origin&gt;</code> is consulted and its <code>Pull:</code> lines are used. In addition to the refspec formats described in the OPTIONS section, you can have a globbing refspec that looks like this: </p>
<dl>
<dt>
<dd>
<pre>
refs/heads/*:refs/remotes/origin/*
</pre>
</dl>
<p> A globbing refspec must have a non-empty RHS (i.e. must store what were fetched in remote-tracking branches), and its LHS and RHS must end with <code>/*</code>. The above specifies that all remote branches are tracked using remote-tracking branches in <code>refs/remotes/origin/</code> hierarchy under the same name. </p>
<p> The rule to determine which remote branch to merge after fetching is a bit involved, in order not to break backward compatibility. </p>
<p> If explicit refspecs were given on the command line of <code>git pull</code>, they are all merged. </p>
<p> When no refspec was given on the command line, then <code>git pull</code> uses the refspec from the configuration or <code>$GIT_DIR/remotes/&lt;origin&gt;</code>. In such cases, the following rules apply: </p>
<dl>
<dt>
<dd> 1. If <code>branch.&lt;name&gt;.merge</code> configuration for the current branch <code>&lt;name&gt;</code> exists, that is the name of the branch at the remote site that is merged.</dl>
<dl>
<dt>
<dd> 2. If the refspec is a globbing one, nothing is merged.</dl>
<dl>
<dt>
<dd> 3. Otherwise the remote branch of the first refspec is merged.</dl>
<h2>EXAMPLES</h2>
<dl>
<dt>
<dd> &bull; Update the remote-tracking branches for the repository you cloned from, then merge one of them into your current branch: </p>
<dl>
<dt>
<dd>
<pre>
$ git pull
$ git pull origin
</pre>
</dl>
<p> Normally the branch merged in is the HEAD of the remote repository, but the choice is determined by the branch.&lt;name&gt;.remote and branch.&lt;name&gt;.merge options; see <code><a href="/docs/linux/man/1-git-config/">git-config</a></code>(1) for details.</dl>
<dl>
<dt>
<dd> &bull; Merge into the current branch the remote branch <code>next</code>: </p>
<dl>
<dt>
<dd>
<pre>
$ git pull origin next
</pre>
</dl>
<p> This leaves a copy of <code>next</code> temporarily in FETCH_HEAD, and updates the remote-tracking branch <code>origin/next</code>. The same can be done by invoking fetch and merge: </p>
<dl>
<dt>
<dd>
<pre>
$ git fetch origin
$ git merge origin/next
</pre>
</dl>
</dl>
<p> If you tried a pull which resulted in complex conflicts and would want to start over, you can recover with <i>git reset</i>.</p>
<h2>SECURITY</h2>
<p> The fetch and push protocols are not designed to prevent one side from stealing data from the other repository that was not intended to be shared. If you have private data that you need to protect from a malicious peer, your best option is to store it in another repository. This applies to both clients and servers. In particular, namespaces on a server are not effective for read access control; you should only grant read access to a namespace to clients that you would trust with read access to the entire repository. </p>
<p> The known attack vectors are as follows: </p>
<dl>
<dt>
<dd> 1. The victim sends &quot;have&quot; lines advertising the IDs of objects it has that are not explicitly intended to be shared but can be used to optimize the transfer if the peer also has them. The attacker chooses an object ID X to steal and sends a ref to X, but isn&#8217;t required to send the content of X because the victim already has it. Now the victim believes that the attacker has X, and it sends the content of X back to the attacker later. (This attack is most straightforward for a client to perform on a server, by creating a ref to X in the namespace the client has access to and then fetching it. The most likely way for a server to perform it on a client is to &quot;merge&quot; X into a public branch and hope that the user does additional work on this branch and pushes it back to the server without noticing the merge.)</dl>
<dl>
<dt>
<dd> 2. As in #1, the attacker chooses an object ID X to steal. The victim sends an object Y that the attacker already has, and the attacker falsely claims to have X and not Y, so the victim sends Y as a delta against X. The delta reveals regions of X that are similar to Y to the attacker.</dl>
<h2>BUGS</h2>
<p> Using &#8211;recurse-submodules can only fetch new commits in already checked out submodules right now. When e.g. upstream added a new submodule in the just fetched commits of the superproject the submodule itself cannot be fetched, making it impossible to check out that submodule later without having to do a fetch again. This is expected to be fixed in a future Git version.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-git-fetch/">git-fetch</a></code>(1), <code><a href="/docs/linux/man/1-git-merge/">git-merge</a></code>(1), <code><a href="/docs/linux/man/1-git-config/">git-config</a></code>(1)</p>
<h2>GIT</h2>
<p> Part of the <code><a href="/docs/linux/man/1-git/">git</a></code>(1) suite </p>
<h2>Index</h2>
<dt><a href="#lbAM">MERGE STRATEGIES</a></p>
<dd>
<dt><a href="#lbAN">DEFAULT BEHAVIOUR</a></p>
<dd>
<dt><a href="#lbAO">EXAMPLES</a></p>
<dd>
<dt><a href="#lbAP">SECURITY</a></p>
<dd>
<dt><a href="#lbAQ">BUGS</a></p>
<dd>
<dt><a href="#lbAR">SEE ALSO</a></p>
<dd>
<dt><a href="#lbAS">GIT</a></p>
<dd></dl>
