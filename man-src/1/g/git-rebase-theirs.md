---
title: "git-rebase-theirs(1)"
name: "git-rebase-theirs"
section: "1"
letter: "g"
url: "/docs/linux/man/1-git-rebase-theirs/"
description: "git-rebase-theirs – Resolve rebase conflicts and failed cherry-picks by favoring ‘theirs’ version"
---

<h2 class="name">NAME</h2>
<p> git-rebase-theirs &#8211; Resolve rebase conflicts and failed cherry-picks by favoring &#8216;theirs&#8217; version </p>
<h2>SYNOPSIS</h2>
<p> <code>git-rebase-theirs</code> [<i>options</i>] [<i>&#8212;</i>] <i>FILE</i>&#8230;</p>
<h2>DESCRIPTION</h2>
<p> Resolve git rebase conflicts in FILE(s) by favoring &#8216;theirs&#8217; version. </p>
<p> When using git rebase, conflicts are usually wanted to be resolved by favoring the &lt;working branch&gt; version (the branch being rebased, &#8216;theirs&#8217; side in a rebase), instead of the &lt;upstream&gt; version (the base branch, &#8216;ours&#8217; side) </p>
<p> But git rebase &#8211;strategy -X theirs is only available from git 1.7.3 For older versions, git-rebase-theirs is the solution. And Despite the name, it&#8217;s also useful for fixing failed cherry-picks. </p>
<p> It works by discarding all lines between &#8216;&lt;&lt;&lt;&lt;&lt;&lt;&lt; &#8216; and &#8216;========&#8217; inclusive, and also the the &#8216;&gt;&gt;&gt;&gt;&gt;&gt; commit&#8217; marker. </p>
<p> By default it outputs to stdout, but files can be edited in-place using &#8211;in-place, which, unlike sed, creates a backup by default.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-h</code>,<code>&nbsp;<wbr>&#8211;help</code></p>
<dd> show usage information.</p>
<dt><code>-v</code>,<code>&nbsp;<wbr>&#8211;verbose</code></p>
<dd> print more details in stderr.</p>
<dt><code>&#8211;in-place</code><i>[=SUFFIX]</i></p>
<dd> edit files in place, creating a backup with <i>SUFFIX</i> extension. Default if blank is &quot;.bak&quot;</p>
<dt><code>&#8211;no-backup</code></p>
<dd> disables backup</dl>
<h2>SEE ALSO</h2>
<p> <code><a rel="nofollow" href="https://github.com/MestreLion/git-tools">https://github.com/MestreLion/git-tools</a></code></p>
<h2>AUTHOR</h2>
<p> Rodrigo Silva (MestreLion) linux [at] rodrigosilva.com </p>
<h2>Index</h2>
