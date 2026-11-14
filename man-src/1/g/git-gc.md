---
title: "git-gc(1)"
name: "git-gc"
section: "1"
letter: "g"
url: "/docs/linux/man/1-git-gc/"
description: "git-gc – Cleanup unnecessary files and optimize the local repository"
---

<h2 class="name">NAME</h2>
<p> git-gc &#8211; Cleanup unnecessary files and optimize the local repository </p>
<h2>SYNOPSIS</h2>
<pre><code>
git gc[--aggressive][--auto][--quiet][--prune = &lt;date&gt; | --no - prune][--force][--keep - largest - pack]
</code></pre>
<h2>DESCRIPTION</h2>
<p> Runs a number of housekeeping tasks within the current repository, such as compressing file revisions (to reduce disk space and increase performance), removing unreachable objects which may have been created from prior invocations of <i>git add</i>, packing refs, pruning reflog, rerere metadata or stale working trees. May also update ancillary indexes such as the commit-graph. </p>
<p> When common porcelain operations that create objects are run, they will check whether the repository has grown substantially since the last maintenance, and if so run <code>git gc</code> automatically. See <code>gc.auto</code> below for how to disable this behavior. </p>
<p> Running <code>git gc</code> manually should only be needed when adding objects to a repository without regularly running such porcelain commands, to do a one-off repository optimization, or e.g. to clean up a suboptimal mass-import. See the &quot;PACKFILE OPTIMIZATION&quot; section in <code><a href="/docs/linux/man/1-git-fast-import/">git-fast-import</a></code>(1) for more details on the import case.</p>
<h2>OPTIONS</h2>
<p> &#8211;aggressive</p>
<dl>
<dt>
<dd> Usually <i>git gc</i> runs very quickly while providing good disk space utilization and performance. This option will cause <i>git gc</i> to more aggressively optimize the repository at the expense of taking much more time. The effects of this optimization are mostly persistent. See the &quot;AGGRESSIVE&quot; section below for details.</dl>
<p> &#8211;auto</p>
<dl>
<dt>
<dd> With this option, <i>git gc</i> checks whether any housekeeping is required; if not, it exits without performing any work. </p>
<p> See the <code>gc.auto</code> option in the &quot;CONFIGURATION&quot; section below for how this heuristic works. </p>
<p> Once housekeeping is triggered by exceeding the limits of configuration options such as <code>gc.auto</code> and <code>gc.autoPackLimit</code>, all other housekeeping tasks (e.g. rerere, working trees, reflog&#8230;) will be performed as well.</dl>
<p> &#8211;prune=&lt;date&gt;</p>
<dl>
<dt>
<dd> Prune loose objects older than date (default is 2 weeks ago, overridable by the config variable <code>gc.pruneExpire</code>). &#8211;prune=now prunes loose objects regardless of their age and increases the risk of corruption if another process is writing to the repository concurrently; see &quot;NOTES&quot; below. &#8211;prune is on by default.</dl>
<p> &#8211;no-prune</p>
<dl>
<dt>
<dd> Do not prune any loose objects.</dl>
<p> &#8211;quiet</p>
<dl>
<dt>
<dd> Suppress all progress reports.</dl>
<p> &#8211;force</p>
<dl>
<dt>
<dd> Force <code>git gc</code> to run even if there may be another <code>git gc</code> instance running on this repository.</dl>
<p> &#8211;keep-largest-pack</p>
<dl>
<dt>
<dd> All packs except the largest pack and those marked with a <code>.keep</code> files are consolidated into a single pack. When this option is used, <code>gc.bigPackThreshold</code> is ignored.</dl>
<h2>AGGRESSIVE</h2>
<p> When the <code>&#8211;aggressive</code> option is supplied, <code><a href="/docs/linux/man/1-git-repack/">git-repack</a></code>(1) will be invoked with the <code>-f</code> flag, which in turn will pass <code>&#8211;no-reuse-delta</code> to <code><a href="/docs/linux/man/1-git-pack-objects/">git-pack-objects</a></code>(1). This will throw away any existing deltas and re-compute them, at the expense of spending much more time on the repacking. </p>
<p> The effects of this are mostly persistent, e.g. when packs and loose objects are coalesced into one another pack the existing deltas in that pack might get re-used, but there are also various cases where we might pick a sub-optimal delta from a newer pack instead. </p>
<p> Furthermore, supplying <code>&#8211;aggressive</code> will tweak the <code>&#8211;depth</code> and <code>&#8211;window</code> options passed to <code><a href="/docs/linux/man/1-git-repack/">git-repack</a></code>(1). See the <code>gc.aggressiveDepth</code> and <code>gc.aggressiveWindow</code> settings below. By using a larger window size we&#8217;re more likely to find more optimal deltas. </p>
<p> It&#8217;s probably not worth it to use this option on a given repository without running tailored performance benchmarks on it. It takes a lot more time, and the resulting space/delta optimization may or may not be worth it. Not using this at all is the right trade-off for most users and their repositories.</p>
<h2>CONFIGURATION</h2>
<p> The below documentation is the same as what&#8217;s found in <code><a href="/docs/linux/man/1-git-config/">git-config</a></code>(1): </p>
<p> gc.aggressiveDepth</p>
<dl>
<dt>
<dd> The depth parameter used in the delta compression algorithm used by <i>git gc &#8211;aggressive</i>. This defaults to 50, which is the default for the <code>&#8211;depth</code> option when <code>&#8211;aggressive</code> isn&#8217;t in use. </p>
<p> See the documentation for the <code>&#8211;depth</code> option in <code><a href="/docs/linux/man/1-git-repack/">git-repack</a></code>(1) for more details.</dl>
<p> gc.aggressiveWindow</p>
<dl>
<dt>
<dd> The window size parameter used in the delta compression algorithm used by <i>git gc &#8211;aggressive</i>. This defaults to 250, which is a much more aggressive window size than the default <code>&#8211;window</code> of 10. </p>
<p> See the documentation for the <code>&#8211;window</code> option in <code><a href="/docs/linux/man/1-git-repack/">git-repack</a></code>(1) for more details.</dl>
<p> gc.auto</p>
<dl>
<dt>
<dd> When there are approximately more than this many loose objects in the repository, <code>git gc &#8211;auto</code> will pack them. Some Porcelain commands use this command to perform a light-weight garbage collection from time to time. The default value is 6700. </p>
<p> Setting this to 0 disables not only automatic packing based on the number of loose objects, but any other heuristic <code>git gc &#8211;auto</code> will otherwise use to determine if there&#8217;s work to do, such as <code>gc.autoPackLimit</code>.</dl>
<p> gc.autoPackLimit</p>
<dl>
<dt>
<dd> When there are more than this many packs that are not marked with <code>*.keep</code> file in the repository, <code>git gc &#8211;auto</code> consolidates them into one larger pack. The default value is 50. Setting this to 0 disables it. Setting <code>gc.auto</code> to 0 will also disable this. </p>
<p> See the <code>gc.bigPackThreshold</code> configuration variable below. When in use, it&#8217;ll affect how the auto pack limit works.</dl>
<p> gc.autoDetach</p>
<dl>
<dt>
<dd> Make <code>git gc &#8211;auto</code> return immediately and run in background if the system supports it. Default is true.</dl>
<p> gc.bigPackThreshold</p>
<dl>
<dt>
<dd> If non-zero, all packs larger than this limit are kept when <code>git gc</code> is run. This is very similar to <code>&#8211;keep-largest-pack</code> except that all packs that meet the threshold are kept, not just the largest pack. Defaults to zero. Common unit suffixes of <i>k</i>, <i>m</i>, or <i>g</i> are supported. </p>
<p> Note that if the number of kept packs is more than gc.autoPackLimit, this configuration variable is ignored, all packs except the base pack will be repacked. After this the number of packs should go below gc.autoPackLimit and gc.bigPackThreshold should be respected again. </p>
<p> If the amount of memory estimated for <code>git repack</code> to run smoothly is not available and <code>gc.bigPackThreshold</code> is not set, the largest pack will also be excluded (this is the equivalent of running <code>git gc</code> with <code>&#8211;keep-largest-pack</code>).</dl>
<p> gc.writeCommitGraph</p>
<dl>
<dt>
<dd> If true, then gc will rewrite the commit-graph file when <code><a href="/docs/linux/man/1-git-gc/">git-gc</a></code>(1) is run. When using <code>git gc &#8211;auto</code> the commit-graph will be updated if housekeeping is required. Default is true. See <code><a href="/docs/linux/man/1-git-commit-graph/">git-commit-graph</a></code>(1) for details.</dl>
<p> gc.logExpiry</p>
<dl>
<dt>
<dd> If the file gc.log exists, then <code>git gc &#8211;auto</code> will print its content and exit with status zero instead of running unless that file is more than <i>gc.logExpiry</i> old. Default is &quot;1.day&quot;. See <code>gc.pruneExpire</code> for more ways to specify its value.</dl>
<p> gc.packRefs</p>
<dl>
<dt>
<dd> Running <code>git pack-refs</code> in a repository renders it unclonable by Git versions prior to 1.5.1.2 over dumb transports such as HTTP. This variable determines whether <i>git gc</i> runs <code>git pack-refs</code>. This can be set to <code>notbare</code> to enable it within all non-bare repos or it can be set to a boolean value. The default is <code>true</code>.</dl>
<p> gc.pruneExpire</p>
<dl>
<dt>
<dd> When <i>git gc</i> is run, it will call <i>prune &#8211;expire 2.weeks.ago</i>. Override the grace period with this config variable. The value &quot;now&quot; may be used to disable this grace period and always prune unreachable objects immediately, or &quot;never&quot; may be used to suppress pruning. This feature helps prevent corruption when <i>git gc</i> runs concurrently with another process writing to the repository; see the &quot;NOTES&quot; section of <code><a href="/docs/linux/man/1-git-gc/">git-gc</a></code>(1).</dl>
<p> gc.worktreePruneExpire</p>
<dl>
<dt>
<dd> When <i>git gc</i> is run, it calls <i>git worktree prune &#8211;expire 3.months.ago</i>. This config variable can be used to set a different grace period. The value &quot;now&quot; may be used to disable the grace period and prune <code>$GIT_DIR/worktrees</code> immediately, or &quot;never&quot; may be used to suppress pruning.</dl>
<p> gc.reflogExpire, gc.&lt;pattern&gt;.reflogExpire</p>
<dl>
<dt>
<dd> <i>git reflog expire</i> removes reflog entries older than this time; defaults to 90 days. The value &quot;now&quot; expires all entries immediately, and &quot;never&quot; suppresses expiration altogether. With &quot;&lt;pattern&gt;&quot; (e.g. &quot;refs/stash&quot;) in the middle the setting applies only to the refs that match the &lt;pattern&gt;.</dl>
<p> gc.reflogExpireUnreachable, gc.&lt;pattern&gt;.reflogExpireUnreachable</p>
<dl>
<dt>
<dd> <i>git reflog expire</i> removes reflog entries older than this time and are not reachable from the current tip; defaults to 30 days. The value &quot;now&quot; expires all entries immediately, and &quot;never&quot; suppresses expiration altogether. With &quot;&lt;pattern&gt;&quot; (e.g. &quot;refs/stash&quot;) in the middle, the setting applies only to the refs that match the &lt;pattern&gt;. </p>
<p> These types of entries are generally created as a result of using <code>git commit &#8211;amend</code> or <code>git rebase</code> and are the commits prior to the amend or rebase occurring. Since these changes are not part of the current project most users will want to expire them sooner, which is why the default is more aggressive than <code>gc.reflogExpire</code>.</dl>
<p> gc.rerereResolved</p>
<dl>
<dt>
<dd> Records of conflicted merge you resolved earlier are kept for this many days when <i>git rerere gc</i> is run. You can also use more human-readable &quot;1.month.ago&quot;, etc. The default is 60 days. See <code><a href="/docs/linux/man/1-git-rerere/">git-rerere</a></code>(1).</dl>
<p> gc.rerereUnresolved</p>
<dl>
<dt>
<dd> Records of conflicted merge you have not resolved are kept for this many days when <i>git rerere gc</i> is run. You can also use more human-readable &quot;1.month.ago&quot;, etc. The default is 15 days. See <code><a href="/docs/linux/man/1-git-rerere/">git-rerere</a></code>(1).</dl>
<h2>NOTES</h2>
<p> <i>git gc</i> tries very hard not to delete objects that are referenced anywhere in your repository. In particular, it will keep not only objects referenced by your current set of branches and tags, but also objects referenced by the index, remote-tracking branches, reflogs (which may reference commits in branches that were later amended or rewound), and anything else in the refs/* namespace. Note that a note (of the kind created by <i>git notes</i>) attached to an object does not contribute in keeping the object alive. If you are expecting some objects to be deleted and they aren&#8217;t, check all of those locations and decide whether it makes sense in your case to remove those references. </p>
<p> On the other hand, when <i>git gc</i> runs concurrently with another process, there is a risk of it deleting an object that the other process is using but hasn&#8217;t created a reference to. This may just cause the other process to fail or may corrupt the repository if the other process later adds a reference to the deleted object. Git has two features that significantly mitigate this problem: </p>
<dl>
<dt>
<dd> 1. Any object with modification time newer than the <code>&#8211;prune</code> date is kept, along with everything reachable from it.</dl>
<dl>
<dt>
<dd> 2. Most operations that add an object to the database update the modification time of the object if it is already present so that #1 applies.</dl>
<p> However, these features fall short of a complete solution, so users who run commands concurrently have to live with some risk of corruption (which seems to be low in practice).</p>
<h2>HOOKS</h2>
<p> The <i>git gc &#8211;auto</i> command will run the <i>pre-auto-gc</i> hook. See <code><a href="/docs/linux/man/5-githooks/">githooks</a></code>(5) for more information.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-git-prune/">git-prune</a></code>(1) <code><a href="/docs/linux/man/1-git-reflog/">git-reflog</a></code>(1) <code><a href="/docs/linux/man/1-git-repack/">git-repack</a></code>(1) <code><a href="/docs/linux/man/1-git-rerere/">git-rerere</a></code>(1)</p>
<h2>GIT</h2>
<p> Part of the <code><a href="/docs/linux/man/1-git/">git</a></code>(1) suite </p>
<h2>Index</h2>
