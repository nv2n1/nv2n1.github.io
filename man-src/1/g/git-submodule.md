---
title: "git-submodule(1)"
name: "git-submodule"
section: "1"
letter: "g"
url: "/docs/linux/man/1-git-submodule/"
description: "git-submodule – Initialize, update or inspect submodules"
---

<h2 class="name">NAME</h2>
<p> git-submodule &#8211; Initialize, update or inspect submodules </p>
<h2>SYNOPSIS</h2>
<pre><code>
git submodule[--quiet][--cached] git submodule[--quiet] add[&lt;options&gt;][--]&lt;repository&gt;[&lt;path&gt;] git submodule[--quiet] status[--cached][--recursive][--][&lt;path&gt;...] git submodule[--quiet] init[--][&lt;path&gt;...] git submodule[--quiet] deinit[-f | --force](--all | [--]&lt;path&gt;...)
        git submodule[--quiet] update[&lt;options&gt;][--][&lt;path&gt;...] git submodule[--quiet] set
    - branch[&lt;options&gt;][--]&lt;path&gt; git submodule[--quiet] set - url[--]&lt;path&gt;&lt;newurl&gt; git submodule[--quiet] summary[&lt;options&gt;][--][&lt;path&gt;...] git submodule[--quiet] foreach[--recursive]&lt;command&gt; git submodule[--quiet] sync[--recursive][--][&lt;path&gt;...] git submodule[--quiet] absorbgitdirs[--][&lt;path&gt;...]
</code></pre>
<h2>DESCRIPTION</h2>
<p> Inspects, updates and manages submodules. </p>
<p> For more information about submodules, see <code><a href="/docs/linux/man/7-gitsubmodules/">gitsubmodules</a></code>(7).</p>
<h2>COMMANDS</h2>
<p> With no arguments, shows the status of existing submodules. Several subcommands are available to perform operations on the submodules. </p>
<p> add [-b &lt;branch&gt;] [-f|&#8211;force] [&#8211;name &lt;name&gt;] [&#8211;reference &lt;repository&gt;] [&#8211;depth &lt;depth&gt;] [&#8211;] &lt;repository&gt; [&lt;path&gt;]</p>
<dl>
<dt>
<dd> Add the given repository as a submodule at the given path to the changeset to be committed next to the current project: the current project is termed the &quot;superproject&quot;. </p>
<p> &lt;repository&gt; is the URL of the new submodule&#8217;s origin repository. This may be either an absolute URL, or (if it begins with ./ or ../), the location relative to the superproject&#8217;s default remote repository (Please note that to specify a repository <i>foo.git</i> which is located right next to a superproject <i>bar.git</i>, you&#8217;ll have to use <code>../foo.git</code> instead of <code>./foo.git</code> &#8211; as one might expect when following the rules for relative URLs &#8211; because the evaluation of relative URLs in Git is identical to that of relative directories). </p>
<p> The default remote is the remote of the remote-tracking branch of the current branch. If no such remote-tracking branch exists or the HEAD is detached, &quot;origin&quot; is assumed to be the default remote. If the superproject doesn&#8217;t have a default remote configured the superproject is its own authoritative upstream and the current working directory is used instead. </p>
<p> The optional argument &lt;path&gt; is the relative location for the cloned submodule to exist in the superproject. If &lt;path&gt; is not given, the canonical part of the source repository is used (&quot;repo&quot; for &quot;/path/to/repo.git&quot; and &quot;foo&quot; for &quot;host.xz:foo/.git&quot;). If &lt;path&gt; exists and is already a valid Git repository, then it is staged for commit without cloning. The &lt;path&gt; is also used as the submodule&#8217;s logical name in its configuration entries unless <code>&#8211;name</code> is used to specify a logical name. </p>
<p> The given URL is recorded into <code>.gitmodules</code> for use by subsequent users cloning the superproject. If the URL is given relative to the superproject&#8217;s repository, the presumption is the superproject and submodule repositories will be kept together in the same relative location, and only the superproject&#8217;s URL needs to be provided. git-submodule will correctly locate the submodule using the relative URL in <code>.gitmodules</code>.</dl>
<p> status [&#8211;cached] [&#8211;recursive] [&#8211;] [&lt;path&gt;&#8230;]</p>
<dl>
<dt>
<dd> Show the status of the submodules. This will print the SHA-1 of the currently checked out commit for each submodule, along with the submodule path and the output of <i>git describe</i> for the SHA-1. Each SHA-1 will possibly be prefixed with <code>&#8211;</code> if the submodule is not initialized, <code>+</code> if the currently checked out submodule commit does not match the SHA-1 found in the index of the containing repository and <code>U</code> if the submodule has merge conflicts. </p>
<p> If <code>&#8211;cached</code> is specified, this command will instead print the SHA-1 recorded in the superproject for each submodule. </p>
<p> If <code>&#8211;recursive</code> is specified, this command will recurse into nested submodules, and show their status as well. </p>
<p> If you are only interested in changes of the currently initialized submodules with respect to the commit recorded in the index or the HEAD, <code><a href="/docs/linux/man/1-git-status/">git-status</a></code>(1) and <code><a href="/docs/linux/man/1-git-diff/">git-diff</a></code>(1) will provide that information too (and can also report changes to a submodule&#8217;s work tree).</dl>
<p> init [&#8211;] [&lt;path&gt;&#8230;]</p>
<dl>
<dt>
<dd> Initialize the submodules recorded in the index (which were added and committed elsewhere) by setting <code>submodule.$name.url</code> in .git/config. It uses the same setting from <code>.gitmodules</code> as a template. If the URL is relative, it will be resolved using the default remote. If there is no default remote, the current repository will be assumed to be upstream. </p>
<p> Optional &lt;path&gt; arguments limit which submodules will be initialized. If no path is specified and submodule.active has been configured, submodules configured to be active will be initialized, otherwise all submodules are initialized. </p>
<p> When present, it will also copy the value of <code>submodule.$name.update</code>. This command does not alter existing information in .git/config. You can then customize the submodule clone URLs in .git/config for your local setup and proceed to <code>git submodule update</code>; you can also just use <code>git submodule update &#8211;init</code> without the explicit <i>init</i> step if you do not intend to customize any submodule locations. </p>
<p> See the add subcommand for the definition of default remote.</dl>
<p> deinit [-f|&#8211;force] (&#8211;all|[&#8211;] &lt;path&gt;&#8230;)</p>
<dl>
<dt>
<dd> Unregister the given submodules, i.e. remove the whole <code>submodule.$name</code> section from .git/config together with their work tree. Further calls to <code>git submodule update</code>, <code>git submodule foreach</code> and <code>git submodule sync</code> will skip any unregistered submodules until they are initialized again, so use this command if you don&#8217;t want to have a local checkout of the submodule in your working tree anymore. </p>
<p> When the command is run without pathspec, it errors out, instead of deinit-ing everything, to prevent mistakes. </p>
<p> If <code>&#8211;force</code> is specified, the submodule&#8217;s working tree will be removed even if it contains local modifications. </p>
<p> If you really want to remove a submodule from the repository and commit that use <code><a href="/docs/linux/man/1-git-rm/">git-rm</a></code>(1) instead. See <code><a href="/docs/linux/man/7-gitsubmodules/">gitsubmodules</a></code>(7) for removal options.</dl>
<p> update [&#8211;init] [&#8211;remote] [-N|&#8211;no-fetch] [&#8211;[no-]recommend-shallow] [-f|&#8211;force] [&#8211;checkout|&#8211;rebase|&#8211;merge] [&#8211;reference &lt;repository&gt;] [&#8211;depth &lt;depth&gt;] [&#8211;recursive] [&#8211;jobs &lt;n&gt;] [&#8211;[no-]single-branch] [&#8211;] [&lt;path&gt;&#8230;]</p>
<dl>
<dt>
<dd> Update the registered submodules to match what the superproject expects by cloning missing submodules, fetching missing commits in submodules and updating the working tree of the submodules. The &quot;updating&quot; can be done in several ways depending on command line options and the value of <code>submodule.&lt;name&gt;.update</code> configuration variable. The command line option takes precedence over the configuration variable. If neither is given, a <i>checkout</i> is performed. The <i>update</i> procedures supported both from the command line as well as through the <code>submodule.&lt;name&gt;.update</code> configuration are: </p>
<p> checkout</p>
<dl>
<dt>
<dd> the commit recorded in the superproject will be checked out in the submodule on a detached HEAD. </p>
<p> If <code>&#8211;force</code> is specified, the submodule will be checked out (using <code>git checkout &#8211;force</code>), even if the commit specified in the index of the containing repository already matches the commit checked out in the submodule.</dl>
<p> rebase</p>
<dl>
<dt>
<dd> the current branch of the submodule will be rebased onto the commit recorded in the superproject.</dl>
<p> merge</p>
<dl>
<dt>
<dd> the commit recorded in the superproject will be merged into the current branch in the submodule.</dl>
<p> The following <i>update</i> procedures are only available via the <code>submodule.&lt;name&gt;.update</code> configuration variable: </p>
<p> custom command</p>
<dl>
<dt>
<dd> arbitrary shell command that takes a single argument (the sha1 of the commit recorded in the superproject) is executed. When <code>submodule.&lt;name&gt;.update</code> is set to <i>!command</i>, the remainder after the exclamation mark is the custom command.</dl>
<p> none</p>
<dl>
<dt>
<dd> the submodule is not updated.</dl>
<p> If the submodule is not yet initialized, and you just want to use the setting as stored in <code>.gitmodules</code>, you can automatically initialize the submodule with the <code>&#8211;init</code> option. </p>
<p> If <code>&#8211;recursive</code> is specified, this command will recurse into the registered submodules, and update any nested submodules within.</dl>
<p> set-branch (-b|&#8211;branch) &lt;branch&gt; [&#8211;] &lt;path&gt;, set-branch (-d|&#8211;default) [&#8211;] &lt;path&gt;</p>
<dl>
<dt>
<dd> Sets the default remote tracking branch for the submodule. The <code>&#8211;branch</code> option allows the remote branch to be specified. The <code>&#8211;default</code> option removes the submodule.&lt;name&gt;.branch configuration key, which causes the tracking branch to default to the remote <i>HEAD</i>.</dl>
<p> set-url [&#8211;] &lt;path&gt; &lt;newurl&gt;</p>
<dl>
<dt>
<dd> Sets the URL of the specified submodule to &lt;newurl&gt;. Then, it will automatically synchronize the submodule&#8217;s new remote URL configuration.</dl>
<p> summary [&#8211;cached|&#8211;files] [(-n|&#8211;summary-limit) &lt;n&gt;] [commit] [&#8211;] [&lt;path&gt;&#8230;]</p>
<dl>
<dt>
<dd> Show commit summary between the given commit (defaults to HEAD) and working tree/index. For a submodule in question, a series of commits in the submodule between the given super project commit and the index or working tree (switched by <code>&#8211;cached</code>) are shown. If the option <code>&#8211;files</code> is given, show the series of commits in the submodule between the index of the super project and the working tree of the submodule (this option doesn&#8217;t allow to use the <code>&#8211;cached</code> option or to provide an explicit commit). </p>
<p> Using the <code>&#8211;submodule=log</code> option with <code><a href="/docs/linux/man/1-git-diff/">git-diff</a></code>(1) will provide that information too.</dl>
<p> foreach [&#8211;recursive] &lt;command&gt;</p>
<dl>
<dt>
<dd> Evaluates an arbitrary shell command in each checked out submodule. The command has access to the variables $name, $sm_path, $displaypath, $sha1 and $toplevel: $name is the name of the relevant submodule section in <code>.gitmodules</code>, $sm_path is the path of the submodule as recorded in the immediate superproject, $displaypath contains the relative path from the current working directory to the submodules root directory, $sha1 is the commit as recorded in the immediate superproject, and $toplevel is the absolute path to the top-level of the immediate superproject. Note that to avoid conflicts with <i>$PATH</i> on Windows, the <i>$path</i> variable is now a deprecated synonym of <i>$sm_path</i> variable. Any submodules defined in the superproject but not checked out are ignored by this command. Unless given <code>&#8211;quiet</code>, foreach prints the name of each submodule before evaluating the command. If <code>&#8211;recursive</code> is given, submodules are traversed recursively (i.e. the given shell command is evaluated in nested submodules as well). A non-zero return from the command in any submodule causes the processing to terminate. This can be overridden by adding <i>|| :</i> to the end of the command. </p>
<p> As an example, the command below will show the path and currently checked out commit for each submodule: </p>
<dl>
<dt>
<dd>
<pre>
git submodule foreach 'echo $sm_path `git rev-parse HEAD`'
</pre>
</dl>
</dl>
<p> sync [&#8211;recursive] [&#8211;] [&lt;path&gt;&#8230;]</p>
<dl>
<dt>
<dd> Synchronizes submodules&#8217; remote URL configuration setting to the value specified in <code>.gitmodules</code>. It will only affect those submodules which already have a URL entry in .git/config (that is the case when they are initialized or freshly added). This is useful when submodule URLs change upstream and you need to update your local repositories accordingly. </p>
<p> <code>git submodule sync</code> synchronizes all submodules while <code>git submodule sync &#8212; A</code> synchronizes submodule &quot;A&quot; only. </p>
<p> If <code>&#8211;recursive</code> is specified, this command will recurse into the registered submodules, and sync any nested submodules within.</dl>
<p> absorbgitdirs</p>
<dl>
<dt>
<dd> If a git directory of a submodule is inside the submodule, move the git directory of the submodule into its superproject&#8217;s <code>$GIT_DIR/modules</code> path and then connect the git directory and its working directory by setting the <code>core.worktree</code> and adding a .git file pointing to the git directory embedded in the superprojects git directory. </p>
<p> A repository that was cloned independently and later added as a submodule or old setups have the submodules git directory inside the submodule instead of embedded into the superprojects git directory. </p>
<p> This command is recursive by default.</dl>
<h2>OPTIONS</h2>
<p> -q, &#8211;quiet</p>
<dl>
<dt>
<dd> Only print error messages.</dl>
<p> &#8211;progress</p>
<dl>
<dt>
<dd> This option is only valid for add and update commands. Progress status is reported on the standard error stream by default when it is attached to a terminal, unless -q is specified. This flag forces progress status even if the standard error stream is not directed to a terminal.</dl>
<p> &#8211;all</p>
<dl>
<dt>
<dd> This option is only valid for the deinit command. Unregister all submodules in the working tree.</dl>
<p> -b &lt;branch&gt;, &#8211;branch &lt;branch&gt;</p>
<dl>
<dt>
<dd> Branch of repository to add as submodule. The name of the branch is recorded as <code>submodule.&lt;name&gt;.branch</code> in <code>.gitmodules</code> for <code>update &#8211;remote</code>. A special value of <code>.</code> is used to indicate that the name of the branch in the submodule should be the same name as the current branch in the current repository. If the option is not specified, it defaults to the remote <i>HEAD</i>.</dl>
<p> -f, &#8211;force</p>
<dl>
<dt>
<dd> This option is only valid for add, deinit and update commands. When running add, allow adding an otherwise ignored submodule path. When running deinit the submodule working trees will be removed even if they contain local changes. When running update (only effective with the checkout procedure), throw away local changes in submodules when switching to a different commit; and always run a checkout operation in the submodule, even if the commit listed in the index of the containing repository matches the commit checked out in the submodule.</dl>
<p> &#8211;cached</p>
<dl>
<dt>
<dd> This option is only valid for status and summary commands. These commands typically use the commit found in the submodule HEAD, but with this option, the commit stored in the index is used instead.</dl>
<p> &#8211;files</p>
<dl>
<dt>
<dd> This option is only valid for the summary command. This command compares the commit in the index with that in the submodule HEAD when this option is used.</dl>
<p> -n, &#8211;summary-limit</p>
<dl>
<dt>
<dd> This option is only valid for the summary command. Limit the summary size (number of commits shown in total). Giving 0 will disable the summary; a negative number means unlimited (the default). This limit only applies to modified submodules. The size is always limited to 1 for added/deleted/typechanged submodules.</dl>
<p> &#8211;remote</p>
<dl>
<dt>
<dd> This option is only valid for the update command. Instead of using the superproject&#8217;s recorded SHA-1 to update the submodule, use the status of the submodule&#8217;s remote-tracking branch. The remote used is branch&#8217;s remote (<code>branch.&lt;name&gt;.remote</code>), defaulting to <code>origin</code>. The remote branch used defaults to the remote <code>HEAD</code>, but the branch name may be overridden by setting the <code>submodule.&lt;name&gt;.branch</code> option in either <code>.gitmodules</code> or <code>.git/config</code> (with <code>.git/config</code> taking precedence). </p>
<p> This works for any of the supported update procedures (<code>&#8211;checkout</code>, <code>&#8211;rebase</code>, etc.). The only change is the source of the target SHA-1. For example, <code>submodule update &#8211;remote &#8211;merge</code> will merge upstream submodule changes into the submodules, while <code>submodule update &#8211;merge</code> will merge superproject gitlink changes into the submodules. </p>
<p> In order to ensure a current tracking branch state, <code>update &#8211;remote</code> fetches the submodule&#8217;s remote repository before calculating the SHA-1. If you don&#8217;t want to fetch, you should use <code>submodule update &#8211;remote &#8211;no-fetch</code>. </p>
<p> Use this option to integrate changes from the upstream subproject with your submodule&#8217;s current HEAD. Alternatively, you can run <code>git pull</code> from the submodule, which is equivalent except for the remote branch name: <code>update &#8211;remote</code> uses the default upstream repository and <code>submodule.&lt;name&gt;.branch</code>, while <code>git pull</code> uses the submodule&#8217;s <code>branch.&lt;name&gt;.merge</code>. Prefer <code>submodule.&lt;name&gt;.branch</code> if you want to distribute the default upstream branch with the superproject and <code>branch.&lt;name&gt;.merge</code> if you want a more native feel while working in the submodule itself.</dl>
<p> -N, &#8211;no-fetch</p>
<dl>
<dt>
<dd> This option is only valid for the update command. Don&#8217;t fetch new objects from the remote site.</dl>
<p> &#8211;checkout</p>
<dl>
<dt>
<dd> This option is only valid for the update command. Checkout the commit recorded in the superproject on a detached HEAD in the submodule. This is the default behavior, the main use of this option is to override <code>submodule.$name.update</code> when set to a value other than <code>checkout</code>. If the key <code>submodule.$name.update</code> is either not explicitly set or set to <code>checkout</code>, this option is implicit.</dl>
<p> &#8211;merge</p>
<dl>
<dt>
<dd> This option is only valid for the update command. Merge the commit recorded in the superproject into the current branch of the submodule. If this option is given, the submodule&#8217;s HEAD will not be detached. If a merge failure prevents this process, you will have to resolve the resulting conflicts within the submodule with the usual conflict resolution tools. If the key <code>submodule.$name.update</code> is set to <code>merge</code>, this option is implicit.</dl>
<p> &#8211;rebase</p>
<dl>
<dt>
<dd> This option is only valid for the update command. Rebase the current branch onto the commit recorded in the superproject. If this option is given, the submodule&#8217;s HEAD will not be detached. If a merge failure prevents this process, you will have to resolve these failures with <code><a href="/docs/linux/man/1-git-rebase/">git-rebase</a></code>(1). If the key <code>submodule.$name.update</code> is set to <code>rebase</code>, this option is implicit.</dl>
<p> &#8211;init</p>
<dl>
<dt>
<dd> This option is only valid for the update command. Initialize all submodules for which &quot;git submodule init&quot; has not been called so far before updating.</dl>
<p> &#8211;name</p>
<dl>
<dt>
<dd> This option is only valid for the add command. It sets the submodule&#8217;s name to the given string instead of defaulting to its path. The name must be valid as a directory name and may not end with a <i>/</i>.</dl>
<p> &#8211;reference &lt;repository&gt;</p>
<dl>
<dt>
<dd> This option is only valid for add and update commands. These commands sometimes need to clone a remote repository. In this case, this option will be passed to the <code><a href="/docs/linux/man/1-git-clone/">git-clone</a></code>(1) command. </p>
<p> <code>NOTE</code>: Do <code>not</code> use this option unless you have read the note for <code><a href="/docs/linux/man/1-git-clone/">git-clone</a></code>(1)&#8217;s <code>&#8211;reference</code>, <code>&#8211;shared</code>, and <code>&#8211;dissociate</code> options carefully.</dl>
<p> &#8211;dissociate</p>
<dl>
<dt>
<dd> This option is only valid for add and update commands. These commands sometimes need to clone a remote repository. In this case, this option will be passed to the <code><a href="/docs/linux/man/1-git-clone/">git-clone</a></code>(1) command. </p>
<p> <code>NOTE</code>: see the NOTE for the <code>&#8211;reference</code> option.</dl>
<p> &#8211;recursive</p>
<dl>
<dt>
<dd> This option is only valid for foreach, update, status and sync commands. Traverse submodules recursively. The operation is performed not only in the submodules of the current repo, but also in any nested submodules inside those submodules (and so on).</dl>
<p> &#8211;depth</p>
<dl>
<dt>
<dd> This option is valid for add and update commands. Create a <i>shallow</i> clone with a history truncated to the specified number of revisions. See <code><a href="/docs/linux/man/1-git-clone/">git-clone</a></code>(1)</dl>
<p> &#8211;[no-]recommend-shallow</p>
<dl>
<dt>
<dd> This option is only valid for the update command. The initial clone of a submodule will use the recommended <code>submodule.&lt;name&gt;.shallow</code> as provided by the <code>.gitmodules</code> file by default. To ignore the suggestions use <code>&#8211;no-recommend-shallow</code>.</dl>
<p> -j &lt;n&gt;, &#8211;jobs &lt;n&gt;</p>
<dl>
<dt>
<dd> This option is only valid for the update command. Clone new submodules in parallel with as many jobs. Defaults to the <code>submodule.fetchJobs</code> option.</dl>
<p> &#8211;[no-]single-branch</p>
<dl>
<dt>
<dd> This option is only valid for the update command. Clone only one branch during update: HEAD or one specified by &#8211;branch.</dl>
<p> &lt;path&gt;&#8230;</p>
<dl>
<dt>
<dd> Paths to submodule(s). When specified this will restrict the command to only operate on the submodules found at the specified paths. (This argument is required with add).</dl>
<h2>FILES</h2>
<p> When initializing submodules, a <code>.gitmodules</code> file in the top-level directory of the containing repository is used to find the url of each submodule. This file should be formatted in the same way as <code>$GIT_DIR/config</code>. The key to each submodule url is &quot;submodule.$name.url&quot;. See <code><a href="/docs/linux/man/5-gitmodules/">gitmodules</a></code>(5) for details.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/7-gitsubmodules/">gitsubmodules</a></code>(7), <code><a href="/docs/linux/man/5-gitmodules/">gitmodules</a></code>(5).</p>
<h2>GIT</h2>
<p> Part of the <code><a href="/docs/linux/man/1-git/">git</a></code>(1) suite </p>
<h2>Index</h2>
