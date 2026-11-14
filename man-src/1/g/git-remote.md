---
title: "git-remote(1)"
name: "git-remote"
section: "1"
letter: "g"
url: "/docs/linux/man/1-git-remote/"
description: "git-remote – Manage set of tracked repositories"
---

<h2 class="name">NAME</h2>
<p> git-remote &#8211; Manage set of tracked repositories </p>
<h2>SYNOPSIS</h2>
<pre><code>
git remote[-v | --verbose] git remote add[-t&lt;branch&gt;][-m&lt;master&gt;][-f][--[no - ] tags][--mirror = (fetch | push)]&lt;name&gt;&lt;url&gt;
        git remote rename&lt;old&gt;&lt;new&gt;
            git remote remove&lt;name&gt;
                git remote set - head&lt;name&gt;(-a | --auto | -d | --delete | &lt;branch&gt;) git remote set - branches[--add]&lt;name&gt;&lt;branch&gt;... git remote get - url[--push][--all]&lt;name&gt; git remote set - url[--push]&lt;name&gt;&lt;newurl&gt;[&lt;oldurl&gt;] git remote set - url-- add[--push]&lt;name&gt;&lt;newurl&gt; git remote set - url-- delete[--push]&lt;name&gt;&lt;url&gt; git remote[-v | --verbose] show[-n]&lt;name&gt;... git remote prune[-n | --dry - run]&lt;name&gt;... git remote[-v | --verbose] update[-p | --prune][(&lt;group&gt; | &lt;remote&gt;)...]
</code></pre>
<h2>DESCRIPTION</h2>
<p> Manage the set of repositories (&quot;remotes&quot;) whose branches you track.</p>
<h2>OPTIONS</h2>
<p> -v, &#8211;verbose</p>
<dl>
<dt>
<dd> Be a little more verbose and show remote url after name. NOTE: This must be placed between <code>remote</code> and subcommand.</dl>
<h2>COMMANDS</h2>
<p> With no arguments, shows a list of existing remotes. Several subcommands are available to perform operations on the remotes. </p>
<p> <i>add</i></p>
<dl>
<dt>
<dd> Add a remote named &lt;name&gt; for the repository at &lt;url&gt;. The command <code>git fetch &lt;name&gt;</code> can then be used to create and update remote-tracking branches &lt;name&gt;/&lt;branch&gt;. </p>
<p> With <code>-f</code> option, <code>git fetch &lt;name&gt;</code> is run immediately after the remote information is set up. </p>
<p> With <code>&#8211;tags</code> option, <code>git fetch &lt;name&gt;</code> imports every tag from the remote repository. </p>
<p> With <code>&#8211;no-tags</code> option, <code>git fetch &lt;name&gt;</code> does not import tags from the remote repository. </p>
<p> By default, only tags on fetched branches are imported (see <code><a href="/docs/linux/man/1-git-fetch/">git-fetch</a></code>(1)). </p>
<p> With <code>-t &lt;branch&gt;</code> option, instead of the default glob refspec for the remote to track all branches under the <code>refs/remotes/&lt;name&gt;/</code> namespace, a refspec to track only <code>&lt;branch&gt;</code> is created. You can give more than one <code>-t &lt;branch&gt;</code> to track multiple branches without grabbing all branches. </p>
<p> With <code>-m &lt;master&gt;</code> option, a symbolic-ref <code>refs/remotes/&lt;name&gt;/HEAD</code> is set up to point at remote&#8217;s <code>&lt;master&gt;</code> branch. See also the set-head command. </p>
<p> When a fetch mirror is created with <code>&#8211;mirror=fetch</code>, the refs will not be stored in the <i>refs/remotes/</i> namespace, but rather everything in <i>refs/</i> on the remote will be directly mirrored into <i>refs/</i> in the local repository. This option only makes sense in bare repositories, because a fetch would overwrite any local commits. </p>
<p> When a push mirror is created with <code>&#8211;mirror=push</code>, then <code>git push</code> will always behave as if <code>&#8211;mirror</code> was passed.</dl>
<p> <i>rename</i></p>
<dl>
<dt>
<dd> Rename the remote named &lt;old&gt; to &lt;new&gt;. All remote-tracking branches and configuration settings for the remote are updated. </p>
<p> In case &lt;old&gt; and &lt;new&gt; are the same, and &lt;old&gt; is a file under <code>$GIT_DIR/remotes</code> or <code>$GIT_DIR/branches</code>, the remote is converted to the configuration file format.</dl>
<p> <i>remove</i>, <i>rm</i></p>
<dl>
<dt>
<dd> Remove the remote named &lt;name&gt;. All remote-tracking branches and configuration settings for the remote are removed.</dl>
<p> <i>set-head</i></p>
<dl>
<dt>
<dd> Sets or deletes the default branch (i.e. the target of the symbolic-ref <code>refs/remotes/&lt;name&gt;/HEAD</code>) for the named remote. Having a default branch for a remote is not required, but allows the name of the remote to be specified in lieu of a specific branch. For example, if the default branch for <code>origin</code> is set to <code>master</code>, then <code>origin</code> may be specified wherever you would normally specify <code>origin/master</code>. </p>
<p> With <code>-d</code> or <code>&#8211;delete</code>, the symbolic ref <code>refs/remotes/&lt;name&gt;/HEAD</code> is deleted. </p>
<p> With <code>-a</code> or <code>&#8211;auto</code>, the remote is queried to determine its <code>HEAD</code>, then the symbolic-ref <code>refs/remotes/&lt;name&gt;/HEAD</code> is set to the same branch. e.g., if the remote <code>HEAD</code> is pointed at <code>next</code>, <code>git remote set-head origin -a</code> will set the symbolic-ref <code>refs/remotes/origin/HEAD</code> to <code>refs/remotes/origin/next</code>. This will only work if <code>refs/remotes/origin/next</code> already exists; if not it must be fetched first. </p>
<p> Use <code>&lt;branch&gt;</code> to set the symbolic-ref <code>refs/remotes/&lt;name&gt;/HEAD</code> explicitly. e.g., <code>git remote set-head origin master</code> will set the symbolic-ref <code>refs/remotes/origin/HEAD</code> to <code>refs/remotes/origin/master</code>. This will only work if <code>refs/remotes/origin/master</code> already exists; if not it must be fetched first.</dl>
<p> <i>set-branches</i></p>
<dl>
<dt>
<dd> Changes the list of branches tracked by the named remote. This can be used to track a subset of the available remote branches after the initial setup for a remote. </p>
<p> The named branches will be interpreted as if specified with the <code>-t</code> option on the <code>git remote add</code> command line. </p>
<p> With <code>&#8211;add</code>, instead of replacing the list of currently tracked branches, adds to that list.</dl>
<p> <i>get-url</i></p>
<dl>
<dt>
<dd> Retrieves the URLs for a remote. Configurations for <code>insteadOf</code> and <code>pushInsteadOf</code> are expanded here. By default, only the first URL is listed. </p>
<p> With <code>&#8211;push</code>, push URLs are queried rather than fetch URLs. </p>
<p> With <code>&#8211;all</code>, all URLs for the remote will be listed.</dl>
<p> <i>set-url</i></p>
<dl>
<dt>
<dd> Changes URLs for the remote. Sets first URL for remote &lt;name&gt; that matches regex &lt;oldurl&gt; (first URL if no &lt;oldurl&gt; is given) to &lt;newurl&gt;. If &lt;oldurl&gt; doesn&#8217;t match any URL, an error occurs and nothing is changed. </p>
<p> With <code>&#8211;push</code>, push URLs are manipulated instead of fetch URLs. </p>
<p> With <code>&#8211;add</code>, instead of changing existing URLs, new URL is added. </p>
<p> With <code>&#8211;delete</code>, instead of changing existing URLs, all URLs matching regex &lt;url&gt; are deleted for remote &lt;name&gt;. Trying to delete all non-push URLs is an error. </p>
<p> Note that the push URL and the fetch URL, even though they can be set differently, must still refer to the same place. What you pushed to the push URL should be what you would see if you immediately fetched from the fetch URL. If you are trying to fetch from one place (e.g. your upstream) and push to another (e.g. your publishing repository), use two separate remotes.</dl>
<p> <i>show</i></p>
<dl>
<dt>
<dd> Gives some information about the remote &lt;name&gt;. </p>
<p> With <code>-n</code> option, the remote heads are not queried first with <code>git ls-remote &lt;name&gt;</code>; cached information is used instead.</dl>
<p> <i>prune</i></p>
<dl>
<dt>
<dd> Deletes stale references associated with &lt;name&gt;. By default, stale remote-tracking branches under &lt;name&gt; are deleted, but depending on global configuration and the configuration of the remote we might even prune local tags that haven&#8217;t been pushed there. Equivalent to <code>git fetch &#8211;prune &lt;name&gt;</code>, except that no new references will be fetched. </p>
<p> See the PRUNING section of <code><a href="/docs/linux/man/1-git-fetch/">git-fetch</a></code>(1) for what it&#8217;ll prune depending on various configuration. </p>
<p> With <code>&#8211;dry-run</code> option, report what branches would be pruned, but do not actually prune them.</dl>
<p> <i>update</i></p>
<dl>
<dt>
<dd> Fetch updates for remotes or remote groups in the repository as defined by <code>remotes.&lt;group&gt;</code>. If neither group nor remote is specified on the command line, the configuration parameter remotes.default will be used; if remotes.default is not defined, all remotes which do not have the configuration parameter <code>remote.&lt;name&gt;.skipDefaultUpdate</code> set to true will be updated. (See <code><a href="/docs/linux/man/1-git-config/">git-config</a></code>(1)). </p>
<p> With <code>&#8211;prune</code> option, run pruning against all the remotes that are updated.</dl>
<h2>DISCUSSION</h2>
<p> The remote configuration is achieved using the <code>remote.origin.url</code> and <code>remote.origin.fetch</code> configuration variables. (See <code><a href="/docs/linux/man/1-git-config/">git-config</a></code>(1)).</p>
<h2>EXIT STATUS</h2>
<p> On success, the exit status is <code>0</code>. </p>
<p> When subcommands such as <i>add</i>, <i>rename</i>, and <i>remove</i> can&#8217;t find the remote in question, the exit status is <code>2</code>. When the remote already exists, the exit status is <code>3</code>. </p>
<p> On any other error, the exit status may be any other non-zero value.</p>
<h2>EXAMPLES</h2>
<dl>
<dt>
<dd> &bull; Add a new remote, fetch, and check out a branch from it </p>
<dl>
<dt>
<dd>
<pre><code>
$ git remote
        origin
            $ git branch -
    r
            origin /
        HEAD-&gt;origin / master origin / master $ git remote add staging git :                                                               // git.kernel.org/.../gregkh/staging.git
                                                                             $ git remote origin staging $ git fetch staging... From git : // git.kernel.org/pub/scm/linux/kernel/git/gregkh/staging
                                                                                                                                           *[new branch] master -&gt; staging / master * [new branch] staging - linus -&gt; staging / staging - linus * [new branch] staging - next -&gt; staging / staging - next $ git branch - r origin / HEAD -&gt; origin / master origin / master staging / master staging / staging - linus staging / staging - next $ git switch - c staging staging / master...
</code></pre>
</dl>
</dl>
<dl>
<dt>
<dd> &bull; Imitate <i>git clone</i> but track only selected branches </p>
<dl>
<dt>
<dd>
<pre>
$ mkdir project.git
$ cd project.git
$ git init
$ git remote add -f -t master -m master origin <a href="git://example.com/git.git/">git://example.com/git.git/</a>
$ git merge origin
</pre>
</dl>
</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-git-fetch/">git-fetch</a></code>(1) <code><a href="/docs/linux/man/1-git-branch/">git-branch</a></code>(1) <code><a href="/docs/linux/man/1-git-config/">git-config</a></code>(1)</p>
<h2>GIT</h2>
<p> Part of the <code><a href="/docs/linux/man/1-git/">git</a></code>(1) suite </p>
<h2>Index</h2>
