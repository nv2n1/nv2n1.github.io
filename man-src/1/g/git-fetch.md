---
title: "git-fetch(1)"
name: "git-fetch"
section: "1"
letter: "g"
url: "/docs/linux/man/1-git-fetch/"
description: "git-fetch – Download objects and refs from another repository"
---

<h2 class="name">NAME</h2>
<p> git-fetch &#8211; Download objects and refs from another repository </p>
<h2>SYNOPSIS</h2>
<pre><code>
git fetch[&lt;options&gt;][&lt;repository&gt;[&lt;refspec&gt;...]] git fetch[&lt;options&gt;]&lt;group&gt;
    git fetch-- multiple[&lt;options&gt;][(&lt;repository&gt; | &lt;group&gt;)...] git fetch-- all[&lt;options&gt;]
</code></pre>
<h2>DESCRIPTION</h2>
<p> Fetch branches and/or tags (collectively, &quot;refs&quot;) from one or more other repositories, along with the objects necessary to complete their histories. Remote-tracking branches are updated (see the description of &lt;refspec&gt; below for ways to control this behavior). </p>
<p> By default, any tag that points into the histories being fetched is also fetched; the effect is to fetch tags that point at branches that you are interested in. This default behavior can be changed by using the &#8211;tags or &#8211;no-tags options or by configuring remote.&lt;name&gt;.tagOpt. By using a refspec that fetches tags explicitly, you can fetch tags that do not point into branches you are interested in as well. </p>
<p> <i>git fetch</i> can fetch from either a single named repository or URL, or from several repositories at once if &lt;group&gt; is given and there is a remotes.&lt;group&gt; entry in the configuration file. (See <code><a href="/docs/linux/man/1-git-config/">git-config</a></code>(1)). </p>
<p> When no remote is specified, by default the <code>origin</code> remote will be used, unless there&#8217;s an upstream branch configured for the current branch. </p>
<p> The names of refs that are fetched, together with the object names they point at, are written to <code>.git/FETCH_HEAD</code>. This information may be used by scripts or other git commands, such as <code><a href="/docs/linux/man/1-git-pull/">git-pull</a></code>(1).</p>
<h2>OPTIONS</h2>
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
<p> &#8211;[no-]write-fetch-head</p>
<dl>
<dt>
<dd> Write the list of remote refs fetched in the <code>FETCH_HEAD</code> file directly under <code>$GIT_DIR</code>. This is the default. Passing <code>&#8211;no-write-fetch-head</code> from the command line tells Git not to write the file. Under <code>&#8211;dry-run</code> option, the file is never written.</dl>
<p> -f, &#8211;force</p>
<dl>
<dt>
<dd> When <i>git fetch</i> is used with <code>&lt;src&gt;:&lt;dst&gt;</code> refspec it may refuse to update the local branch as discussed in the <code>&lt;refspec&gt;</code> part below. This option overrides that check.</dl>
<p> -k, &#8211;keep</p>
<dl>
<dt>
<dd> Keep downloaded pack.</dl>
<p> &#8211;multiple</p>
<dl>
<dt>
<dd> Allow several &lt;repository&gt; and &lt;group&gt; arguments to be specified. No &lt;refspec&gt;s may be specified.</dl>
<p> &#8211;[no-]auto-maintenance, &#8211;[no-]auto-gc</p>
<dl>
<dt>
<dd> Run <code>git maintenance run &#8211;auto</code> at the end to perform automatic repository maintenance if needed. (<code>&#8211;[no-]auto-gc</code> is a synonym.) This is enabled by default.</dl>
<p> &#8211;[no-]write-commit-graph</p>
<dl>
<dt>
<dd> Write a commit-graph after fetching. This overrides the config setting <code>fetch.writeCommitGraph</code>.</dl>
<p> &#8211;prefetch</p>
<dl>
<dt>
<dd> Modify the configured refspec to place all refs into the <code>refs/prefetch/</code> namespace. See the <code>prefetch</code> task in <code><a href="/docs/linux/man/1-git-maintenance/">git-maintenance</a></code>(1).</dl>
<p> -p, &#8211;prune</p>
<dl>
<dt>
<dd> Before fetching, remove any remote-tracking references that no longer exist on the remote. Tags are not subject to pruning if they are fetched only because of the default tag auto-following or due to a &#8211;tags option. However, if tags are fetched due to an explicit refspec (either on the command line or in the remote configuration, for example if the remote was cloned with the &#8211;mirror option), then they are also subject to pruning. Supplying <code>&#8211;prune-tags</code> is a shorthand for providing the tag refspec. </p>
<p> See the PRUNING section below for more details.</dl>
<p> -P, &#8211;prune-tags</p>
<dl>
<dt>
<dd> Before fetching, remove any local tags that no longer exist on the remote if <code>&#8211;prune</code> is enabled. This option should be used more carefully, unlike <code>&#8211;prune</code> it will remove any local references (local tags) that have been created. This option is a shorthand for providing the explicit tag refspec along with <code>&#8211;prune</code>, see the discussion about that in its documentation. </p>
<p> See the PRUNING section below for more details.</dl>
<p> -n, &#8211;no-tags</p>
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
<p> &#8211;recurse-submodules[=yes|on-demand|no]</p>
<dl>
<dt>
<dd> This option controls if and under what conditions new commits of populated submodules should be fetched too. It can be used as a boolean option to completely disable recursion when set to <i>no</i> or to unconditionally recurse into all populated submodules when set to <i>yes</i>, which is the default when this option is used without any value. Use <i>on-demand</i> to only recurse into a populated submodule when the superproject retrieves a commit that updates the submodule&#8217;s reference to a commit that isn&#8217;t already in the local submodule clone. By default, <i>on-demand</i> is used, unless <code>fetch.recurseSubmodules</code> is set (see <code><a href="/docs/linux/man/1-git-config/">git-config</a></code>(1)).</dl>
<p> -j, &#8211;jobs=&lt;n&gt;</p>
<dl>
<dt>
<dd> Number of parallel children to be used for all forms of fetching. </p>
<p> If the <code>&#8211;multiple</code> option was specified, the different remotes will be fetched in parallel. If multiple submodules are fetched, they will be fetched in parallel. To control them independently, use the config settings <code>fetch.parallel</code> and <code>submodule.fetchJobs</code> (see <code><a href="/docs/linux/man/1-git-config/">git-config</a></code>(1)). </p>
<p> Typically, parallel recursive and multi-remote fetches will be faster. By default fetches are performed sequentially, not in parallel.</dl>
<p> &#8211;no-recurse-submodules</p>
<dl>
<dt>
<dd> Disable recursive fetching of submodules (this has the same effect as using the <code>&#8211;recurse-submodules=no</code> option).</dl>
<p> &#8211;set-upstream</p>
<dl>
<dt>
<dd> If the remote is fetched successfully, add upstream (tracking) reference, used by argument-less <code><a href="/docs/linux/man/1-git-pull/">git-pull</a></code>(1) and other commands. For more information, see <code>branch.&lt;name&gt;.merge</code> and <code>branch.&lt;name&gt;.remote</code> in <code><a href="/docs/linux/man/1-git-config/">git-config</a></code>(1).</dl>
<p> &#8211;submodule-prefix=&lt;path&gt;</p>
<dl>
<dt>
<dd> Prepend &lt;path&gt; to paths printed in informative messages such as &quot;Fetching submodule foo&quot;. This option is used internally when recursing over submodules.</dl>
<p> &#8211;recurse-submodules-default=[yes|on-demand]</p>
<dl>
<dt>
<dd> This option is used internally to temporarily provide a non-negative default value for the &#8211;recurse-submodules option. All other methods of configuring fetch&#8217;s submodule recursion (such as settings in <code><a href="/docs/linux/man/5-gitmodules/">gitmodules</a></code>(5) and <code><a href="/docs/linux/man/1-git-config/">git-config</a></code>(1)) override this option, as does specifying &#8211;[no-]recurse-submodules directly.</dl>
<p> -u, &#8211;update-head-ok</p>
<dl>
<dt>
<dd> By default <i>git fetch</i> refuses to update the head which corresponds to the current branch. This flag disables the check. This is purely for the internal use for <i>git pull</i> to communicate with <i>git fetch</i>, and unless you are implementing your own Porcelain you are not supposed to use it.</dl>
<p> &#8211;upload-pack &lt;upload-pack&gt;</p>
<dl>
<dt>
<dd> When given, and the repository to fetch from is handled by <i>git fetch-pack</i>, <code>&#8211;exec=&lt;upload-pack&gt;</code> is passed to the command to specify non-default path for the command run on the other end.</dl>
<p> -q, &#8211;quiet</p>
<dl>
<dt>
<dd> Pass &#8211;quiet to git-fetch-pack and silence any other internally used git commands. Progress is not reported to the standard error stream.</dl>
<p> -v, &#8211;verbose</p>
<dl>
<dt>
<dd> Be verbose.</dl>
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
<p> &lt;group&gt;</p>
<dl>
<dt>
<dd> A name referring to a list of repositories as the value of remotes.&lt;group&gt; in the configuration file. (See <code><a href="/docs/linux/man/1-git-config/">git-config</a></code>(1)).</dl>
<p> &lt;refspec&gt;</p>
<dl>
<dt>
<dd> Specifies which refs to fetch and which local refs to update. When no &lt;refspec&gt;s appear on the command line, the refs to fetch are read from <code>remote.&lt;repository&gt;.fetch</code> variables instead (see CONFIGURED REMOTE-TRACKING BRANCHES below). </p>
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
</dl>
<p> &#8211;stdin</p>
<dl>
<dt>
<dd> Read refspecs, one per line, from stdin in addition to those provided as arguments. The &quot;tag &lt;name&gt;&quot; format is not supported.</dl>
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
<h2>CONFIGURED REMOTE-TRACKING BRANCHES</h2>
<p> You often interact with the same remote repository by regularly and repeatedly fetching from it. In order to keep track of the progress of such a remote repository, <code>git fetch</code> allows you to configure <code>remote.&lt;repository&gt;.fetch</code> configuration variables. </p>
<p> Typically such a variable may look like this: </p>
<dl>
<dt>
<dd>
<pre>
[remote &quot;origin&quot;]
        fetch = +refs/heads/*:refs/remotes/origin/*
</pre>
</dl>
<p> This configuration is used in two ways: </p>
<dl>
<dt>
<dd> &bull; When <code>git fetch</code> is run without specifying what branches and/or tags to fetch on the command line, e.g. <code>git fetch origin</code> or <code>git fetch</code>, <code>remote.&lt;repository&gt;.fetch</code> values are used as the refspecs&#8212;they specify which refs to fetch and which local refs to update. The example above will fetch all branches that exist in the <code>origin</code> (i.e. any ref that matches the left-hand side of the value, <code>refs/heads/*</code>) and update the corresponding remote-tracking branches in the <code>refs/remotes/origin/*</code> hierarchy.</dl>
<dl>
<dt>
<dd> &bull; When <code>git fetch</code> is run with explicit branches and/or tags to fetch on the command line, e.g. <code>git fetch origin master</code>, the &lt;refspec&gt;s given on the command line determine what are to be fetched (e.g. <code>master</code> in the example, which is a short-hand for <code>master:</code>, which in turn means &quot;fetch the <i>master</i> branch but I do not explicitly say what remote-tracking branch to update with it from the command line&quot;), and the example command will fetch <i>only</i> the <i>master</i> branch. The <code>remote.&lt;repository&gt;.fetch</code> values determine which remote-tracking branch, if any, is updated. When used in this way, the <code>remote.&lt;repository&gt;.fetch</code> values do not have any effect in deciding <i>what</i> gets fetched (i.e. the values are not used as refspecs when the command-line lists refspecs); they are only used to decide <i>where</i> the refs that are fetched are stored by acting as a mapping.</dl>
<p> The latter use of the <code>remote.&lt;repository&gt;.fetch</code> values can be overridden by giving the <code>&#8211;refmap=&lt;refspec&gt;</code> parameter(s) on the command line.</p>
<h2>PRUNING</h2>
<p> Git has a default disposition of keeping data unless it&#8217;s explicitly thrown away; this extends to holding onto local references to branches on remotes that have themselves deleted those branches. </p>
<p> If left to accumulate, these stale references might make performance worse on big and busy repos that have a lot of branch churn, and e.g. make the output of commands like <code>git branch -a &#8211;contains &lt;commit&gt;</code> needlessly verbose, as well as impacting anything else that&#8217;ll work with the complete set of known references. </p>
<p> These remote-tracking references can be deleted as a one-off with either of: </p>
<dl>
<dt>
<dd>
<pre>
# While fetching
$ git fetch --prune &lt;name&gt;
# Only prune, don't fetch
$ git remote prune &lt;name&gt;
</pre>
</dl>
<p> To prune references as part of your normal workflow without needing to remember to run that, set <code>fetch.prune</code> globally, or <code>remote.&lt;name&gt;.prune</code> per-remote in the config. See <code><a href="/docs/linux/man/1-git-config/">git-config</a></code>(1). </p>
<p> Here&#8217;s where things get tricky and more specific. The pruning feature doesn&#8217;t actually care about branches, instead it&#8217;ll prune local &larr;&rarr; remote-references as a function of the refspec of the remote (see <code>&lt;refspec&gt;</code> and CONFIGURED REMOTE-TRACKING BRANCHES above). </p>
<p> Therefore if the refspec for the remote includes e.g. <code>refs/tags/*:refs/tags/*</code>, or you manually run e.g. <code>git fetch &#8211;prune &lt;name&gt; &quot;refs/tags/*:refs/tags/*&quot;</code> it won&#8217;t be stale remote tracking branches that are deleted, but any local tag that doesn&#8217;t exist on the remote. </p>
<p> This might not be what you expect, i.e. you want to prune remote <code>&lt;name&gt;</code>, but also explicitly fetch tags from it, so when you fetch from it you delete all your local tags, most of which may not have come from the <code>&lt;name&gt;</code> remote in the first place. </p>
<p> So be careful when using this with a refspec like <code>refs/tags/*:refs/tags/*</code>, or any other refspec which might map references from multiple remotes to the same local namespace. </p>
<p> Since keeping up-to-date with both branches and tags on the remote is a common use-case the <code>&#8211;prune-tags</code> option can be supplied along with <code>&#8211;prune</code> to prune local tags that don&#8217;t exist on the remote, and force-update those tags that differ. Tag pruning can also be enabled with <code>fetch.pruneTags</code> or <code>remote.&lt;name&gt;.pruneTags</code> in the config. See <code><a href="/docs/linux/man/1-git-config/">git-config</a></code>(1). </p>
<p> The <code>&#8211;prune-tags</code> option is equivalent to having <code>refs/tags/*:refs/tags/*</code> declared in the refspecs of the remote. This can lead to some seemingly strange interactions: </p>
<dl>
<dt>
<dd>
<pre>
# These both fetch tags
$ git fetch --no-tags origin 'refs/tags/*:refs/tags/*'
$ git fetch --no-tags --prune-tags origin
</pre>
</dl>
<p> The reason it doesn&#8217;t error out when provided without <code>&#8211;prune</code> or its config versions is for flexibility of the configured versions, and to maintain a 1=1 mapping between what the command line flags do, and what the configuration versions do. </p>
<p> It&#8217;s reasonable to e.g. configure <code>fetch.pruneTags=true</code> in <code>~/.gitconfig</code> to have tags pruned whenever <code>git fetch &#8211;prune</code> is run, without making every invocation of <code>git fetch</code> without <code>&#8211;prune</code> an error. </p>
<p> Pruning tags with <code>&#8211;prune-tags</code> also works when fetching a URL instead of a named remote. These will all prune tags not found on origin: </p>
<dl>
<dt>
<dd>
<pre><code>
$ git fetch origin-- prune-- prune - tags $ git fetch origin-- prune 'refs/tags/*:refs/tags/*' $ git fetch&lt;url of origin&gt; --prune-- prune - tags $ git fetch&lt;url of origin&gt; --prune 'refs/tags/*:refs/tags/*'
</code></pre>
</dl>
<h2>OUTPUT</h2>
<p> The output of &quot;git fetch&quot; depends on the transport method used; this section describes the output when fetching over the Git protocol (either locally or via ssh) and Smart HTTP protocol. </p>
<p> The status of the fetch is output in tabular form, with each line representing the status of a single ref. Each line is of the form: </p>
<dl>
<dt>
<dd>
<pre>
 &lt;flag&gt; &lt;summary&gt; &lt;from&gt; -&gt; &lt;to&gt; [&lt;reason&gt;]
</pre>
</dl>
<p> The status of up-to-date refs is shown only if the &#8211;verbose option is used. </p>
<p> In compact output mode, specified with configuration variable fetch.output, if either entire <code>&lt;from&gt;</code> or <code>&lt;to&gt;</code> is found in the other string, it will be substituted with <code>*</code> in the other string. For example, <code>master -&gt; origin/master</code> becomes <code>master -&gt; origin/*</code>. </p>
<p> flag</p>
<dl>
<dt>
<dd> A single character indicating the status of the ref: </p>
<p> (space)</p>
<dl>
<dt>
<dd> for a successfully fetched fast-forward;</dl>
<p> <code>+</code></p>
<dl>
<dt>
<dd> for a successful forced update;</dl>
<p> <code>&#8211;</code></p>
<dl>
<dt>
<dd> for a successfully pruned ref;</dl>
<p> <code>t</code></p>
<dl>
<dt>
<dd> for a successful tag update;</dl>
<p> <code>*</code></p>
<dl>
<dt>
<dd> for a successfully fetched new ref;</dl>
<p> <code>!</code></p>
<dl>
<dt>
<dd> for a ref that was rejected or failed to update; and</dl>
<p> <code>=</code></p>
<dl>
<dt>
<dd> for a ref that was up to date and did not need fetching.</dl>
</dl>
<p> summary</p>
<dl>
<dt>
<dd> For a successfully fetched ref, the summary shows the old and new values of the ref in a form suitable for using as an argument to <code>git log</code> (this is <code>&lt;old&gt;..&lt;new&gt;</code> in most cases, and <code>&lt;old&gt;&#8230;&lt;new&gt;</code> for forced non-fast-forward updates).</dl>
<p> from</p>
<dl>
<dt>
<dd> The name of the remote ref being fetched from, minus its <code>refs/&lt;type&gt;/</code> prefix. In the case of deletion, the name of the remote ref is &quot;(none)&quot;.</dl>
<p> to</p>
<dl>
<dt>
<dd> The name of the local ref being updated, minus its <code>refs/&lt;type&gt;/</code> prefix.</dl>
<p> reason</p>
<dl>
<dt>
<dd> A human-readable explanation. In the case of successfully fetched refs, no explanation is needed. For a failed ref, the reason for failure is described.</dl>
<h2>EXAMPLES</h2>
<dl>
<dt>
<dd> &bull; Update the remote-tracking branches: </p>
<dl>
<dt>
<dd>
<pre>
$ git fetch origin
</pre>
</dl>
<p> The above command copies all branches from the remote refs/heads/ namespace and stores them to the local refs/remotes/origin/ namespace, unless the branch.&lt;name&gt;.fetch option is used to specify a non-default refspec.</dl>
<dl>
<dt>
<dd> &bull; Using refspecs explicitly: </p>
<dl>
<dt>
<dd>
<pre>
$ git fetch origin +seen:seen maint:tmp
</pre>
</dl>
<p> This updates (or creates, as necessary) branches <code>seen</code> and <code>tmp</code> in the local repository by fetching from the branches (respectively) <code>seen</code> and <code>maint</code> from the remote repository. </p>
<p> The <code>seen</code> branch will be updated even if it does not fast-forward, because it is prefixed with a plus sign; <code>tmp</code> will not be.</dl>
<dl>
<dt>
<dd> &bull; Peek at a remote&#8217;s branch, without configuring the remote in your local repository: </p>
<dl>
<dt>
<dd>
<pre>
$ git fetch <a href="git://git.kernel.org/pub/scm/git/git.git">git://git.kernel.org/pub/scm/git/git.git</a> maint
$ git log FETCH_HEAD
</pre>
</dl>
<p> The first command fetches the <code>maint</code> branch from the repository at <code><a href="git://git.kernel.org/pub/scm/git/git.git">git://git.kernel.org/pub/scm/git/git.git</a></code> and the second command uses <code>FETCH_HEAD</code> to examine the branch with <code><a href="/docs/linux/man/1-git-log/">git-log</a></code>(1). The fetched objects will eventually be removed by git&#8217;s built-in housekeeping (see <code><a href="/docs/linux/man/1-git-gc/">git-gc</a></code>(1)).</dl>
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
<p> <code><a href="/docs/linux/man/1-git-pull/">git-pull</a></code>(1)</p>
<h2>GIT</h2>
<p> Part of the <code><a href="/docs/linux/man/1-git/">git</a></code>(1) suite </p>
<h2>Index</h2>
<dt><a href="#lbAK">CONFIGURED REMOTE-TRACKING BRANCHES</a></p>
<dd>
<dt><a href="#lbAL">PRUNING</a></p>
<dd>
<dt><a href="#lbAM">OUTPUT</a></p>
<dd>
<dt><a href="#lbAN">EXAMPLES</a></p>
<dd>
<dt><a href="#lbAO">SECURITY</a></p>
<dd>
<dt><a href="#lbAP">BUGS</a></p>
<dd>
<dt><a href="#lbAQ">SEE ALSO</a></p>
<dd>
<dt><a href="#lbAR">GIT</a></p>
<dd></dl>
