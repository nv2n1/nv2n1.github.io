---
title: "git-push(1)"
name: "git-push"
section: "1"
letter: "g"
url: "/docs/linux/man/1-git-push/"
description: "git-push – Update remote refs along with associated objects"
---

<h2 class="name">NAME</h2>
<p> git-push &#8211; Update remote refs along with associated objects </p>
<h2>SYNOPSIS</h2>
<pre><code>
git push[--all | --mirror | --tags][--follow - tags][--atomic][-n | --dry - run][--receive - pack = &lt;git - receive - pack&gt;]
        [--repo = &lt;repository&gt;][-f | --force][-d | --delete][--prune][-v | --verbose]
        [-u | --set - upstream][-o&lt;string&gt; | --push - option = &lt;string&gt;]
        [--[no - ] signed | --signed = (true | false | if - asked)]
        [--force - with - lease[=&lt;refname&gt;[:&lt;expect&gt;]][--force - if - includes]]
        [--no - verify][&lt;repository&gt;[&lt;refspec&gt;...]]
</code></pre>
<h2>DESCRIPTION</h2>
<p> Updates remote refs using local refs, while sending objects necessary to complete the given refs. </p>
<p> You can make interesting things happen to a repository every time you push into it, by setting up <i>hooks</i> there. See documentation for <code><a href="/docs/linux/man/1-git-receive-pack/">git-receive-pack</a></code>(1). </p>
<p> When the command line does not specify where to push with the <code>&lt;repository&gt;</code> argument, <code>branch.*.remote</code> configuration for the current branch is consulted to determine where to push. If the configuration is missing, it defaults to <i>origin</i>. </p>
<p> When the command line does not specify what to push with <code>&lt;refspec&gt;&#8230;</code> arguments or <code>&#8211;all</code>, <code>&#8211;mirror</code>, <code>&#8211;tags</code> options, the command finds the default <code>&lt;refspec&gt;</code> by consulting <code>remote.*.push</code> configuration, and if it is not found, honors <code>push.default</code> configuration to decide what to push (See <code><a href="/docs/linux/man/1-git-config/">git-config</a></code>(1) for the meaning of <code>push.default</code>). </p>
<p> When neither the command-line nor the configuration specify what to push, the default behavior is used, which corresponds to the <code>simple</code> value for <code>push.default</code>: the current branch is pushed to the corresponding upstream branch, but as a safety measure, the push is aborted if the upstream branch does not have the same name as the local one.</p>
<h2>OPTIONS</h2>
<p> &lt;repository&gt;</p>
<dl>
<dt>
<dd> The &quot;remote&quot; repository that is destination of a push operation. This parameter can be either a URL (see the section GIT URLS below) or the name of a remote (see the section REMOTES below).</dl>
<p> &lt;refspec&gt;&#8230;</p>
<dl>
<dt>
<dd> Specify what destination ref to update with what source object. The format of a &lt;refspec&gt; parameter is an optional plus <code>+</code>, followed by the source object &lt;src&gt;, followed by a colon <code>:</code>, followed by the destination ref &lt;dst&gt;. </p>
<p> The &lt;src&gt; is often the name of the branch you would want to push, but it can be any arbitrary &quot;SHA-1 expression&quot;, such as <code>master~4</code> or <code>HEAD</code> (see <code><a href="/docs/linux/man/7-gitrevisions/">gitrevisions</a></code>(7)). </p>
<p> The &lt;dst&gt; tells which ref on the remote side is updated with this push. Arbitrary expressions cannot be used here, an actual ref must be named. If <code>git push [&lt;repository&gt;]</code> without any <code>&lt;refspec&gt;</code> argument is set to update some ref at the destination with <code>&lt;src&gt;</code> with <code>remote.&lt;repository&gt;.push</code> configuration variable, <code>:&lt;dst&gt;</code> part can be omitted&#8212;such a push will update a ref that <code>&lt;src&gt;</code> normally updates without any <code>&lt;refspec&gt;</code> on the command line. Otherwise, missing <code>:&lt;dst&gt;</code> means to update the same ref as the <code>&lt;src&gt;</code>. </p>
<p> If &lt;dst&gt; doesn&#8217;t start with <code>refs/</code> (e.g. <code>refs/heads/master</code>) we will try to infer where in <code>refs/*</code> on the destination &lt;repository&gt; it belongs based on the type of &lt;src&gt; being pushed and whether &lt;dst&gt; is ambiguous. </p>
<dl>
<dt>
<dd> &bull; If &lt;dst&gt; unambiguously refers to a ref on the &lt;repository&gt; remote, then push to that ref.</dl>
<dl>
<dt>
<dd> &bull; If &lt;src&gt; resolves to a ref starting with refs/heads/ or refs/tags/, then prepend that to &lt;dst&gt;.</dl>
<dl>
<dt>
<dd> &bull; Other ambiguity resolutions might be added in the future, but for now any other cases will error out with an error indicating what we tried, and depending on the <code>advice.pushUnqualifiedRefname</code> configuration (see <code><a href="/docs/linux/man/1-git-config/">git-config</a></code>(1)) suggest what refs/ namespace you may have wanted to push to.</dl>
<p> The object referenced by &lt;src&gt; is used to update the &lt;dst&gt; reference on the remote side. Whether this is allowed depends on where in <code>refs/*</code> the &lt;dst&gt; reference lives as described in detail below, in those sections &quot;update&quot; means any modifications except deletes, which as noted after the next few sections are treated differently. </p>
<p> The <code>refs/heads/*</code> namespace will only accept commit objects, and updates only if they can be fast-forwarded. </p>
<p> The <code>refs/tags/*</code> namespace will accept any kind of object (as commits, trees and blobs can be tagged), and any updates to them will be rejected. </p>
<p> It&#8217;s possible to push any type of object to any namespace outside of <code>refs/{tags,heads}/*</code>. In the case of tags and commits, these will be treated as if they were the commits inside <code>refs/heads/*</code> for the purposes of whether the update is allowed. </p>
<p> I.e. a fast-forward of commits and tags outside <code>refs/{tags,heads}/*</code> is allowed, even in cases where what&#8217;s being fast-forwarded is not a commit, but a tag object which happens to point to a new commit which is a fast-forward of the commit the last tag (or commit) it&#8217;s replacing. Replacing a tag with an entirely different tag is also allowed, if it points to the same commit, as well as pushing a peeled tag, i.e. pushing the commit that existing tag object points to, or a new tag object which an existing commit points to. </p>
<p> Tree and blob objects outside of <code>refs/{tags,heads}/*</code> will be treated the same way as if they were inside <code>refs/tags/*</code>, any update of them will be rejected. </p>
<p> All of the rules described above about what&#8217;s not allowed as an update can be overridden by adding an the optional leading <code>+</code> to a refspec (or using <code>&#8211;force</code> command line option). The only exception to this is that no amount of forcing will make the <code>refs/heads/*</code> namespace accept a non-commit object. Hooks and configuration can also override or amend these rules, see e.g. <code>receive.denyNonFastForwards</code> in <code><a href="/docs/linux/man/1-git-config/">git-config</a></code>(1) and <code>pre-receive</code> and <code>update</code> in <code><a href="/docs/linux/man/5-githooks/">githooks</a></code>(5). </p>
<p> Pushing an empty &lt;src&gt; allows you to delete the &lt;dst&gt; ref from the remote repository. Deletions are always accepted without a leading <code>+</code> in the refspec (or <code>&#8211;force</code>), except when forbidden by configuration or hooks. See <code>receive.denyDeletes</code> in <code><a href="/docs/linux/man/1-git-config/">git-config</a></code>(1) and <code>pre-receive</code> and <code>update</code> in <code><a href="/docs/linux/man/5-githooks/">githooks</a></code>(5). </p>
<p> The special refspec <code>:</code> (or <code>+:</code> to allow non-fast-forward updates) directs Git to push &quot;matching&quot; branches: for every branch that exists on the local side, the remote side is updated if a branch of the same name already exists on the remote side. </p>
<p> <code>tag &lt;tag&gt;</code> means the same as <code>refs/tags/&lt;tag&gt;:refs/tags/&lt;tag&gt;</code>.</dl>
<p> &#8211;all</p>
<dl>
<dt>
<dd> Push all branches (i.e. refs under <code>refs/heads/</code>); cannot be used with other &lt;refspec&gt;.</dl>
<p> &#8211;prune</p>
<dl>
<dt>
<dd> Remove remote branches that don&#8217;t have a local counterpart. For example a remote branch <code>tmp</code> will be removed if a local branch with the same name doesn&#8217;t exist any more. This also respects refspecs, e.g. <code>git push &#8211;prune remote refs/heads/*:refs/tmp/*</code> would make sure that remote <code>refs/tmp/foo</code> will be removed if <code>refs/heads/foo</code> doesn&#8217;t exist.</dl>
<p> &#8211;mirror</p>
<dl>
<dt>
<dd> Instead of naming each ref to push, specifies that all refs under <code>refs/</code> (which includes but is not limited to <code>refs/heads/</code>, <code>refs/remotes/</code>, and <code>refs/tags/</code>) be mirrored to the remote repository. Newly created local refs will be pushed to the remote end, locally updated refs will be force updated on the remote end, and deleted refs will be removed from the remote end. This is the default if the configuration option <code>remote.&lt;remote&gt;.mirror</code> is set.</dl>
<p> -n, &#8211;dry-run</p>
<dl>
<dt>
<dd> Do everything except actually send the updates.</dl>
<p> &#8211;porcelain</p>
<dl>
<dt>
<dd> Produce machine-readable output. The output status line for each ref will be tab-separated and sent to stdout instead of stderr. The full symbolic names of the refs will be given.</dl>
<p> -d, &#8211;delete</p>
<dl>
<dt>
<dd> All listed refs are deleted from the remote repository. This is the same as prefixing all refs with a colon.</dl>
<p> &#8211;tags</p>
<dl>
<dt>
<dd> All refs under <code>refs/tags</code> are pushed, in addition to refspecs explicitly listed on the command line.</dl>
<p> &#8211;follow-tags</p>
<dl>
<dt>
<dd> Push all the refs that would be pushed without this option, and also push annotated tags in <code>refs/tags</code> that are missing from the remote but are pointing at commit-ish that are reachable from the refs being pushed. This can also be specified with configuration variable <code>push.followTags</code>. For more information, see <code>push.followTags</code> in <code><a href="/docs/linux/man/1-git-config/">git-config</a></code>(1).</dl>
<p> &#8211;[no-]signed, &#8211;signed=(true|false|if-asked)</p>
<dl>
<dt>
<dd> GPG-sign the push request to update refs on the receiving side, to allow it to be checked by the hooks and/or be logged. If <code>false</code> or <code>&#8211;no-signed</code>, no signing will be attempted. If <code>true</code> or <code>&#8211;signed</code>, the push will fail if the server does not support signed pushes. If set to <code>if-asked</code>, sign if and only if the server supports signed pushes. The push will also fail if the actual call to <code>gpg &#8211;sign</code> fails. See <code><a href="/docs/linux/man/1-git-receive-pack/">git-receive-pack</a></code>(1) for the details on the receiving end.</dl>
<p> &#8211;[no-]atomic</p>
<dl>
<dt>
<dd> Use an atomic transaction on the remote side if available. Either all refs are updated, or on error, no refs are updated. If the server does not support atomic pushes the push will fail.</dl>
<p> -o &lt;option&gt;, &#8211;push-option=&lt;option&gt;</p>
<dl>
<dt>
<dd> Transmit the given string to the server, which passes them to the pre-receive as well as the post-receive hook. The given string must not contain a NUL or LF character. When multiple <code>&#8211;push-option=&lt;option&gt;</code> are given, they are all sent to the other side in the order listed on the command line. When no <code>&#8211;push-option=&lt;option&gt;</code> is given from the command line, the values of configuration variable <code>push.pushOption</code> are used instead.</dl>
<p> &#8211;receive-pack=&lt;git-receive-pack&gt;, &#8211;exec=&lt;git-receive-pack&gt;</p>
<dl>
<dt>
<dd> Path to the <i>git-receive-pack</i> program on the remote end. Sometimes useful when pushing to a remote repository over ssh, and you do not have the program in a directory on the default $PATH.</dl>
<p> &#8211;[no-]force-with-lease, &#8211;force-with-lease=&lt;refname&gt;, &#8211;force-with-lease=&lt;refname&gt;:&lt;expect&gt;</p>
<dl>
<dt>
<dd> Usually, &quot;git push&quot; refuses to update a remote ref that is not an ancestor of the local ref used to overwrite it. </p>
<p> This option overrides this restriction if the current value of the remote ref is the expected value. &quot;git push&quot; fails otherwise. </p>
<p> Imagine that you have to rebase what you have already published. You will have to bypass the &quot;must fast-forward&quot; rule in order to replace the history you originally published with the rebased history. If somebody else built on top of your original history while you are rebasing, the tip of the branch at the remote may advance with their commit, and blindly pushing with <code>&#8211;force</code> will lose their work. </p>
<p> This option allows you to say that you expect the history you are updating is what you rebased and want to replace. If the remote ref still points at the commit you specified, you can be sure that no other people did anything to the ref. It is like taking a &quot;lease&quot; on the ref without explicitly locking it, and the remote ref is updated only if the &quot;lease&quot; is still valid. </p>
<p> <code>&#8211;force-with-lease</code> alone, without specifying the details, will protect all remote refs that are going to be updated by requiring their current value to be the same as the remote-tracking branch we have for them. </p>
<p> <code>&#8211;force-with-lease=&lt;refname&gt;</code>, without specifying the expected value, will protect the named ref (alone), if it is going to be updated, by requiring its current value to be the same as the remote-tracking branch we have for it. </p>
<p> <code>&#8211;force-with-lease=&lt;refname&gt;:&lt;expect&gt;</code> will protect the named ref (alone), if it is going to be updated, by requiring its current value to be the same as the specified value <code>&lt;expect&gt;</code> (which is allowed to be different from the remote-tracking branch we have for the refname, or we do not even have to have such a remote-tracking branch when this form is used). If <code>&lt;expect&gt;</code> is the empty string, then the named ref must not already exist. </p>
<p> Note that all forms other than <code>&#8211;force-with-lease=&lt;refname&gt;:&lt;expect&gt;</code> that specifies the expected current value of the ref explicitly are still experimental and their semantics may change as we gain experience with this feature. </p>
<p> &quot;&#8211;no-force-with-lease&quot; will cancel all the previous &#8211;force-with-lease on the command line. </p>
<p> A general note on safety: supplying this option without an expected value, i.e. as <code>&#8211;force-with-lease</code> or <code>&#8211;force-with-lease=&lt;refname&gt;</code> interacts very badly with anything that implicitly runs <code>git fetch</code> on the remote to be pushed to in the background, e.g. <code>git fetch origin</code> on your repository in a cronjob. </p>
<p> The protection it offers over <code>&#8211;force</code> is ensuring that subsequent changes your work wasn&#8217;t based on aren&#8217;t clobbered, but this is trivially defeated if some background process is updating refs in the background. We don&#8217;t have anything except the remote tracking info to go by as a heuristic for refs you&#8217;re expected to have seen &amp; are willing to clobber. </p>
<p> If your editor or some other system is running <code>git fetch</code> in the background for you a way to mitigate this is to simply set up another remote: </p>
<dl>
<dt>
<dd>
<pre>
git remote add origin-push $(git config remote.origin.url)
git fetch origin-push
</pre>
</dl>
<p> Now when the background process runs <code>git fetch origin</code> the references on <code>origin-push</code> won&#8217;t be updated, and thus commands like: </p>
<dl>
<dt>
<dd>
<pre>
git push --force-with-lease origin-push
</pre>
</dl>
<p> Will fail unless you manually run <code>git fetch origin-push</code>. This method is of course entirely defeated by something that runs <code>git fetch &#8211;all</code>, in that case you&#8217;d need to either disable it or do something more tedious like: </p>
<dl>
<dt>
<dd>
<pre>
git fetch              # update 'master' from remote
git tag base master    # mark our base point
git rebase -i master   # rewrite some commits
git push --force-with-lease=master:base master:master
</pre>
</dl>
<p> I.e. create a <code>base</code> tag for versions of the upstream code that you&#8217;ve seen and are willing to overwrite, then rewrite history, and finally force push changes to <code>master</code> if the remote version is still at <code>base</code>, regardless of what your local <code>remotes/origin/master</code> has been updated to in the background. </p>
<p> Alternatively, specifying <code>&#8211;force-if-includes</code> as an ancillary option along with <code>&#8211;force-with-lease[=&lt;refname&gt;]</code> (i.e., without saying what exact commit the ref on the remote side must be pointing at, or which refs on the remote side are being protected) at the time of &quot;push&quot; will verify if updates from the remote-tracking refs that may have been implicitly updated in the background are integrated locally before allowing a forced update.</dl>
<p> -f, &#8211;force</p>
<dl>
<dt>
<dd> Usually, the command refuses to update a remote ref that is not an ancestor of the local ref used to overwrite it. Also, when <code>&#8211;force-with-lease</code> option is used, the command refuses to update a remote ref whose current value does not match what is expected. </p>
<p> This flag disables these checks, and can cause the remote repository to lose commits; use it with care. </p>
<p> Note that <code>&#8211;force</code> applies to all the refs that are pushed, hence using it with <code>push.default</code> set to <code>matching</code> or with multiple push destinations configured with <code>remote.*.push</code> may overwrite refs other than the current branch (including local refs that are strictly behind their remote counterpart). To force a push to only one branch, use a <code>+</code> in front of the refspec to push (e.g <code>git push origin +master</code> to force a push to the <code>master</code> branch). See the <code>&lt;refspec&gt;&#8230;</code> section above for details.</dl>
<p> &#8211;[no-]force-if-includes</p>
<dl>
<dt>
<dd> Force an update only if the tip of the remote-tracking ref has been integrated locally. </p>
<p> This option enables a check that verifies if the tip of the remote-tracking ref is reachable from one of the &quot;reflog&quot; entries of the local branch based in it for a rewrite. The check ensures that any updates from the remote have been incorporated locally by rejecting the forced update if that is not the case. </p>
<p> If the option is passed without specifying <code>&#8211;force-with-lease</code>, or specified along with <code>&#8211;force-with-lease=&lt;refname&gt;:&lt;expect&gt;</code>, it is a &quot;no-op&quot;. </p>
<p> Specifying <code>&#8211;no-force-if-includes</code> disables this behavior.</dl>
<p> &#8211;repo=&lt;repository&gt;</p>
<dl>
<dt>
<dd> This option is equivalent to the &lt;repository&gt; argument. If both are specified, the command-line argument takes precedence.</dl>
<p> -u, &#8211;set-upstream</p>
<dl>
<dt>
<dd> For every branch that is up to date or successfully pushed, add upstream (tracking) reference, used by argument-less <code><a href="/docs/linux/man/1-git-pull/">git-pull</a></code>(1) and other commands. For more information, see <code>branch.&lt;name&gt;.merge</code> in <code><a href="/docs/linux/man/1-git-config/">git-config</a></code>(1).</dl>
<p> &#8211;[no-]thin</p>
<dl>
<dt>
<dd> These options are passed to <code><a href="/docs/linux/man/1-git-send-pack/">git-send-pack</a></code>(1). A thin transfer significantly reduces the amount of sent data when the sender and receiver share many of the same objects in common. The default is <code>&#8211;thin</code>.</dl>
<p> -q, &#8211;quiet</p>
<dl>
<dt>
<dd> Suppress all output, including the listing of updated refs, unless an error occurs. Progress is not reported to the standard error stream.</dl>
<p> -v, &#8211;verbose</p>
<dl>
<dt>
<dd> Run verbosely.</dl>
<p> &#8211;progress</p>
<dl>
<dt>
<dd> Progress status is reported on the standard error stream by default when it is attached to a terminal, unless -q is specified. This flag forces progress status even if the standard error stream is not directed to a terminal.</dl>
<p> &#8211;no-recurse-submodules, &#8211;recurse-submodules=check|on-demand|only|no</p>
<dl>
<dt>
<dd> May be used to make sure all submodule commits used by the revisions to be pushed are available on a remote-tracking branch. If <i>check</i> is used Git will verify that all submodule commits that changed in the revisions to be pushed are available on at least one remote of the submodule. If any commits are missing the push will be aborted and exit with non-zero status. If <i>on-demand</i> is used all submodules that changed in the revisions to be pushed will be pushed. If on-demand was not able to push all necessary revisions it will also be aborted and exit with non-zero status. If <i>only</i> is used all submodules will be recursively pushed while the superproject is left unpushed. A value of <i>no</i> or using <code>&#8211;no-recurse-submodules</code> can be used to override the push.recurseSubmodules configuration variable when no submodule recursion is required.</dl>
<p> &#8211;[no-]verify</p>
<dl>
<dt>
<dd> Toggle the pre-push hook (see <code><a href="/docs/linux/man/5-githooks/">githooks</a></code>(5)). The default is &#8211;verify, giving the hook a chance to prevent the push. With &#8211;no-verify, the hook is bypassed completely.</dl>
<p> -4, &#8211;ipv4</p>
<dl>
<dt>
<dd> Use IPv4 addresses only, ignoring IPv6 addresses.</dl>
<p> -6, &#8211;ipv6</p>
<dl>
<dt>
<dd> Use IPv6 addresses only, ignoring IPv4 addresses.</dl>
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
<h2>OUTPUT</h2>
<p> The output of &quot;git push&quot; depends on the transport method used; this section describes the output when pushing over the Git protocol (either locally or via ssh). </p>
<p> The status of the push is output in tabular form, with each line representing the status of a single ref. Each line is of the form: </p>
<dl>
<dt>
<dd>
<pre>
 &lt;flag&gt; &lt;summary&gt; &lt;from&gt; -&gt; &lt;to&gt; (&lt;reason&gt;)
</pre>
</dl>
<p> If &#8211;porcelain is used, then each line of the output is of the form: </p>
<dl>
<dt>
<dd>
<pre>
 &lt;flag&gt; 	 &lt;from&gt;:&lt;to&gt; 	 &lt;summary&gt; (&lt;reason&gt;)
</pre>
</dl>
<p> The status of up-to-date refs is shown only if &#8211;porcelain or &#8211;verbose option is used. </p>
<p> flag</p>
<dl>
<dt>
<dd> A single character indicating the status of the ref: </p>
<p> (space)</p>
<dl>
<dt>
<dd> for a successfully pushed fast-forward;</dl>
<p> <code>+</code></p>
<dl>
<dt>
<dd> for a successful forced update;</dl>
<p> <code>&#8211;</code></p>
<dl>
<dt>
<dd> for a successfully deleted ref;</dl>
<p> <code>*</code></p>
<dl>
<dt>
<dd> for a successfully pushed new ref;</dl>
<p> <code>!</code></p>
<dl>
<dt>
<dd> for a ref that was rejected or failed to push; and</dl>
<p> <code>=</code></p>
<dl>
<dt>
<dd> for a ref that was up to date and did not need pushing.</dl>
</dl>
<p> summary</p>
<dl>
<dt>
<dd> For a successfully pushed ref, the summary shows the old and new values of the ref in a form suitable for using as an argument to <code>git log</code> (this is <code>&lt;old&gt;..&lt;new&gt;</code> in most cases, and <code>&lt;old&gt;&#8230;&lt;new&gt;</code> for forced non-fast-forward updates). </p>
<p> For a failed update, more details are given: </p>
<p> rejected</p>
<dl>
<dt>
<dd> Git did not try to send the ref at all, typically because it is not a fast-forward and you did not force the update.</dl>
<p> remote rejected</p>
<dl>
<dt>
<dd> The remote end refused the update. Usually caused by a hook on the remote side, or because the remote repository has one of the following safety options in effect: <code>receive.denyCurrentBranch</code> (for pushes to the checked out branch), <code>receive.denyNonFastForwards</code> (for forced non-fast-forward updates), <code>receive.denyDeletes</code> or <code>receive.denyDeleteCurrent</code>. See <code><a href="/docs/linux/man/1-git-config/">git-config</a></code>(1).</dl>
<p> remote failure</p>
<dl>
<dt>
<dd> The remote end did not report the successful update of the ref, perhaps because of a temporary error on the remote side, a break in the network connection, or other transient error.</dl>
</dl>
<p> from</p>
<dl>
<dt>
<dd> The name of the local ref being pushed, minus its <code>refs/&lt;type&gt;/</code> prefix. In the case of deletion, the name of the local ref is omitted.</dl>
<p> to</p>
<dl>
<dt>
<dd> The name of the remote ref being updated, minus its <code>refs/&lt;type&gt;/</code> prefix.</dl>
<p> reason</p>
<dl>
<dt>
<dd> A human-readable explanation. In the case of successfully pushed refs, no explanation is needed. For a failed ref, the reason for failure is described.</dl>
<h2>NOTE ABOUT FAST-FORWARDS</h2>
<p> When an update changes a branch (or more in general, a ref) that used to point at commit A to point at another commit B, it is called a fast-forward update if and only if B is a descendant of A. </p>
<p> In a fast-forward update from A to B, the set of commits that the original commit A built on top of is a subset of the commits the new commit B builds on top of. Hence, it does not lose any history. </p>
<p> In contrast, a non-fast-forward update will lose history. For example, suppose you and somebody else started at the same commit X, and you built a history leading to commit B while the other person built a history leading to commit A. The history looks like this: </p>
<dl>
<dt>
<dd>
<pre>
      B
     /
 ---X---A
</pre>
</dl>
<p> Further suppose that the other person already pushed changes leading to A back to the original repository from which you two obtained the original commit X. </p>
<p> The push done by the other person updated the branch that used to point at commit X to point at commit A. It is a fast-forward. </p>
<p> But if you try to push, you will attempt to update the branch (that now points at A) with commit B. This does <i>not</i> fast-forward. If you did so, the changes introduced by commit A will be lost, because everybody will now start building on top of B. </p>
<p> The command by default does not allow an update that is not a fast-forward to prevent such loss of history. </p>
<p> If you do not want to lose your work (history from X to B) or the work by the other person (history from X to A), you would need to first fetch the history from the repository, create a history that contains changes done by both parties, and push the result back. </p>
<p> You can perform &quot;git pull&quot;, resolve potential conflicts, and &quot;git push&quot; the result. A &quot;git pull&quot; will create a merge commit C between commits A and B. </p>
<dl>
<dt>
<dd>
<pre>
      B---C
     /   /
 ---X---A
</pre>
</dl>
<p> Updating A with the resulting merge commit will fast-forward and your push will be accepted. </p>
<p> Alternatively, you can rebase your change between X and B on top of A, with &quot;git pull &#8211;rebase&quot;, and push the result back. The rebase will create a new commit D that builds the change between X and B on top of A. </p>
<dl>
<dt>
<dd>
<pre>
      B   D
     /   /
 ---X---A
</pre>
</dl>
<p> Again, updating A with this commit will fast-forward and your push will be accepted. </p>
<p> There is another common situation where you may encounter non-fast-forward rejection when you try to push, and it is possible even when you are pushing into a repository nobody else pushes into. After you push commit A yourself (in the first picture in this section), replace it with &quot;git commit &#8211;amend&quot; to produce commit B, and you try to push it out, because forgot that you have pushed A out already. In such a case, and only if you are certain that nobody in the meantime fetched your earlier commit A (and started building on top of it), you can run &quot;git push &#8211;force&quot; to overwrite it. In other words, &quot;git push &#8211;force&quot; is a method reserved for a case where you do mean to lose history.</p>
<h2>EXAMPLES</h2>
<p> <code>git push</code></p>
<dl>
<dt>
<dd> Works like <code>git push &lt;remote&gt;</code>, where &lt;remote&gt; is the current branch&#8217;s remote (or <code>origin</code>, if no remote is configured for the current branch).</dl>
<p> <code>git push origin</code></p>
<dl>
<dt>
<dd> Without additional configuration, pushes the current branch to the configured upstream (<code>branch.&lt;name&gt;.merge</code> configuration variable) if it has the same name as the current branch, and errors out without pushing otherwise. </p>
<p> The default behavior of this command when no &lt;refspec&gt; is given can be configured by setting the <code>push</code> option of the remote, or the <code>push.default</code> configuration variable. </p>
<p> For example, to default to pushing only the current branch to <code>origin</code> use <code>git config remote.origin.push HEAD</code>. Any valid &lt;refspec&gt; (like the ones in the examples below) can be configured as the default for <code>git push origin</code>.</dl>
<p> <code>git push origin :</code></p>
<dl>
<dt>
<dd> Push &quot;matching&quot; branches to <code>origin</code>. See &lt;refspec&gt; in the OPTIONS section above for a description of &quot;matching&quot; branches.</dl>
<p> <code>git push origin master</code></p>
<dl>
<dt>
<dd> Find a ref that matches <code>master</code> in the source repository (most likely, it would find <code>refs/heads/master</code>), and update the same ref (e.g. <code>refs/heads/master</code>) in <code>origin</code> repository with it. If <code>master</code> did not exist remotely, it would be created.</dl>
<p> <code>git push origin HEAD</code></p>
<dl>
<dt>
<dd> A handy way to push the current branch to the same name on the remote.</dl>
<p> <code>git push mothership master:satellite/master dev:satellite/dev</code></p>
<dl>
<dt>
<dd> Use the source ref that matches <code>master</code> (e.g. <code>refs/heads/master</code>) to update the ref that matches <code>satellite/master</code> (most probably <code>refs/remotes/satellite/master</code>) in the <code>mothership</code> repository; do the same for <code>dev</code> and <code>satellite/dev</code>. </p>
<p> See the section describing <code>&lt;refspec&gt;&#8230;</code> above for a discussion of the matching semantics. </p>
<p> This is to emulate <code>git fetch</code> run on the <code>mothership</code> using <code>git push</code> that is run in the opposite direction in order to integrate the work done on <code>satellite</code>, and is often necessary when you can only make connection in one way (i.e. satellite can ssh into mothership but mothership cannot initiate connection to satellite because the latter is behind a firewall or does not run sshd). </p>
<p> After running this <code>git push</code> on the <code>satellite</code> machine, you would ssh into the <code>mothership</code> and run <code>git merge</code> there to complete the emulation of <code>git pull</code> that were run on <code>mothership</code> to pull changes made on <code>satellite</code>.</dl>
<p> <code>git push origin HEAD:master</code></p>
<dl>
<dt>
<dd> Push the current branch to the remote ref matching <code>master</code> in the <code>origin</code> repository. This form is convenient to push the current branch without thinking about its local name.</dl>
<p> <code>git push origin master:refs/heads/experimental</code></p>
<dl>
<dt>
<dd> Create the branch <code>experimental</code> in the <code>origin</code> repository by copying the current <code>master</code> branch. This form is only needed to create a new branch or tag in the remote repository when the local name and the remote name are different; otherwise, the ref name on its own will work.</dl>
<p> <code>git push origin :experimental</code></p>
<dl>
<dt>
<dd> Find a ref that matches <code>experimental</code> in the <code>origin</code> repository (e.g. <code>refs/heads/experimental</code>), and delete it.</dl>
<p> <code>git push origin +dev:master</code></p>
<dl>
<dt>
<dd> Update the origin repository&#8217;s master branch with the dev branch, allowing non-fast-forward updates. <code>This can leave unreferenced commits dangling in the origin repository.</code> Consider the following situation, where a fast-forward is not possible: </p>
<dl>
<dt>
<dd>
o&#8211; &#8211; o&#8211; &#8211; o&#8211; &#8211; A&#8211; &#8211; B origin / master</p>
<p>                                       X&#8211; &#8211;<br />
    Y&#8211; &#8211; Z dev
</dl>
<p> The above command would change the origin repository to </p>
<dl>
<dt>
<dd>
<pre><code>
A-- - B(unnamed branch) / o-- - o-- - o-- - X-- - Y-- - Z master
</code></pre>
</dl>
<p> Commits A and B would no longer belong to a branch with a symbolic name, and so would be unreachable. As such, these commits would be removed by a <code>git gc</code> command on the origin repository.</dl>
<h2>SECURITY</h2>
<p> The fetch and push protocols are not designed to prevent one side from stealing data from the other repository that was not intended to be shared. If you have private data that you need to protect from a malicious peer, your best option is to store it in another repository. This applies to both clients and servers. In particular, namespaces on a server are not effective for read access control; you should only grant read access to a namespace to clients that you would trust with read access to the entire repository. </p>
<p> The known attack vectors are as follows: </p>
<dl>
<dt>
<dd> 1. The victim sends &quot;have&quot; lines advertising the IDs of objects it has that are not explicitly intended to be shared but can be used to optimize the transfer if the peer also has them. The attacker chooses an object ID X to steal and sends a ref to X, but isn&#8217;t required to send the content of X because the victim already has it. Now the victim believes that the attacker has X, and it sends the content of X back to the attacker later. (This attack is most straightforward for a client to perform on a server, by creating a ref to X in the namespace the client has access to and then fetching it. The most likely way for a server to perform it on a client is to &quot;merge&quot; X into a public branch and hope that the user does additional work on this branch and pushes it back to the server without noticing the merge.)</dl>
<dl>
<dt>
<dd> 2. As in #1, the attacker chooses an object ID X to steal. The victim sends an object Y that the attacker already has, and the attacker falsely claims to have X and not Y, so the victim sends Y as a delta against X. The delta reveals regions of X that are similar to Y to the attacker.</dl>
<h2>GIT</h2>
<p> Part of the <code><a href="/docs/linux/man/1-git/">git</a></code>(1) suite </p>
<h2>Index</h2>
<dt><a href="#lbAK">OUTPUT</a></p>
<dd>
<dt><a href="#lbAL">NOTE ABOUT FAST-FORWARDS</a></p>
<dd>
<dt><a href="#lbAM">EXAMPLES</a></p>
<dd>
<dt><a href="#lbAN">SECURITY</a></p>
<dd>
<dt><a href="#lbAO">GIT</a></p>
<dd></dl>
