---
title: "git-reflog(1)"
name: "git-reflog"
section: "1"
letter: "g"
url: "/docs/linux/man/1-git-reflog/"
description: "git-reflog – Manage reflog information"
---

<h2 class="name">NAME</h2>
<p> git-reflog &#8211; Manage reflog information </p>
<h2>SYNOPSIS</h2>
<pre>
<i>git reflog</i> &lt;subcommand&gt; &lt;options&gt;
</pre>
<h2>DESCRIPTION</h2>
<p> The command takes various subcommands, and different options depending on the subcommand: </p>
<dl>
<dt>
<dd>
<pre><code>
git reflog[show][log - options][&lt;ref&gt;] git reflog expire[--expire = &lt;time&gt;][--expire - unreachable = &lt;time&gt;]
                                                        [--rewrite][--updateref][--stale - fix]
                                                        [--dry - run | -n][--verbose][--all[--single - worktree] | &lt;refs&gt;...] git reflog delete[--rewrite][--updateref]
                                                                                                                                               [--dry - run | -n][--verbose] ref @{specifier}... git reflog exists&lt;ref&gt;
</code></pre>
</dl>
<p> Reference logs, or &quot;reflogs&quot;, record when the tips of branches and other references were updated in the local repository. Reflogs are useful in various Git commands, to specify the old value of a reference. For example, <code>HEAD@{2}</code> means &quot;where HEAD used to be two moves ago&quot;, <code>master@{one.week.ago}</code> means &quot;where master used to point to one week ago in this local repository&quot;, and so on. See <code><a href="/docs/linux/man/7-gitrevisions/">gitrevisions</a></code>(7) for more details. </p>
<p> This command manages the information recorded in the reflogs. </p>
<p> The &quot;show&quot; subcommand (which is also the default, in the absence of any subcommands) shows the log of the reference provided in the command-line (or <code>HEAD</code>, by default). The reflog covers all recent actions, and in addition the <code>HEAD</code> reflog records branch switching. <code>git reflog show</code> is an alias for <code>git log -g &#8211;abbrev-commit &#8211;pretty=oneline</code>; see <code><a href="/docs/linux/man/1-git-log/">git-log</a></code>(1) for more information. </p>
<p> The &quot;expire&quot; subcommand prunes older reflog entries. Entries older than <code>expire</code> time, or entries older than <code>expire-unreachable</code> time and not reachable from the current tip, are removed from the reflog. This is typically not used directly by end users &#8212; instead, see <code><a href="/docs/linux/man/1-git-gc/">git-gc</a></code>(1). </p>
<p> The &quot;delete&quot; subcommand deletes single entries from the reflog. Its argument must be an <i>exact</i> entry (e.g. &quot;<code>git reflog delete master@{2}</code>&quot;). This subcommand is also typically not used directly by end users. </p>
<p> The &quot;exists&quot; subcommand checks whether a ref has a reflog. It exits with zero status if the reflog exists, and non-zero status if it does not.</p>
<h2>OPTIONS</h2>
<h3>Options for <code>show</code></h3>
<p> <code>git reflog show</code> accepts any of the options accepted by <code>git log</code>.</p>
<h3>Options for <code>expire</code></h3>
<p> &#8211;all</p>
<dl>
<dt>
<dd> Process the reflogs of all references.</dl>
<p> &#8211;single-worktree</p>
<dl>
<dt>
<dd> By default when <code>&#8211;all</code> is specified, reflogs from all working trees are processed. This option limits the processing to reflogs from the current working tree only.</dl>
<p> &#8211;expire=&lt;time&gt;</p>
<dl>
<dt>
<dd> Prune entries older than the specified time. If this option is not specified, the expiration time is taken from the configuration setting <code>gc.reflogExpire</code>, which in turn defaults to 90 days. <code>&#8211;expire=all</code> prunes entries regardless of their age; <code>&#8211;expire=never</code> turns off pruning of reachable entries (but see <code>&#8211;expire-unreachable</code>).</dl>
<p> &#8211;expire-unreachable=&lt;time&gt;</p>
<dl>
<dt>
<dd> Prune entries older than <code>&lt;time&gt;</code> that are not reachable from the current tip of the branch. If this option is not specified, the expiration time is taken from the configuration setting <code>gc.reflogExpireUnreachable</code>, which in turn defaults to 30 days. <code>&#8211;expire-unreachable=all</code> prunes unreachable entries regardless of their age; <code>&#8211;expire-unreachable=never</code> turns off early pruning of unreachable entries (but see <code>&#8211;expire</code>).</dl>
<p> &#8211;updateref</p>
<dl>
<dt>
<dd> Update the reference to the value of the top reflog entry (i.e. &lt;ref&gt;@{0}) if the previous top entry was pruned. (This option is ignored for symbolic references.)</dl>
<p> &#8211;rewrite</p>
<dl>
<dt>
<dd> If a reflog entry&#8217;s predecessor is pruned, adjust its &quot;old&quot; SHA-1 to be equal to the &quot;new&quot; SHA-1 field of the entry that now precedes it.</dl>
<p> &#8211;stale-fix</p>
<dl>
<dt>
<dd> Prune any reflog entries that point to &quot;broken commits&quot;. A broken commit is a commit that is not reachable from any of the reference tips and that refers, directly or indirectly, to a missing commit, tree, or blob object. </p>
<p> This computation involves traversing all the reachable objects, i.e. it has the same cost as <i>git prune</i>. It is primarily intended to fix corruption caused by garbage collecting using older versions of Git, which didn&#8217;t protect objects referred to by reflogs.</dl>
<p> -n, &#8211;dry-run</p>
<dl>
<dt>
<dd> Do not actually prune any entries; just show what would have been pruned.</dl>
<p> &#8211;verbose</p>
<dl>
<dt>
<dd> Print extra information on screen.</dl>
<h3>Options for <code>delete</code></h3>
<p> <code>git reflog delete</code> accepts options <code>&#8211;updateref</code>, <code>&#8211;rewrite</code>, <code>-n</code>, <code>&#8211;dry-run</code>, and <code>&#8211;verbose</code>, with the same meanings as when they are used with <code>expire</code>.</p>
<h2>GIT</h2>
<p> Part of the <code><a href="/docs/linux/man/1-git/">git</a></code>(1) suite </p>
<h2>Index</h2>
<dt><a href="#lbAI">GIT</a></p>
<dd></dl>
