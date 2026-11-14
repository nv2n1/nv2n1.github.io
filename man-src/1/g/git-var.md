---
title: "git-var(1)"
name: "git-var"
section: "1"
letter: "g"
url: "/docs/linux/man/1-git-var/"
description: "git-var – Show a Git logical variable"
---

<h2 class="name">NAME</h2>
<p> git-var &#8211; Show a Git logical variable </p>
<h2>SYNOPSIS</h2>
<pre>
<i>git var</i> ( -l | &lt;variable&gt; )
</pre>
<h2>DESCRIPTION</h2>
<p> Prints a Git logical variable.</p>
<h2>OPTIONS</h2>
<p> -l</p>
<dl>
<dt>
<dd> Cause the logical variables to be listed. In addition, all the variables of the Git configuration file .git/config are listed as well. (However, the configuration variables listing functionality is deprecated in favor of <code>git config -l</code>.)</dl>
<h2>EXAMPLES</h2>
<dl>
<dt>
<dd>
<pre>
$ git var GIT_AUTHOR_IDENT
Eric W. Biederman &lt;ebiederm [at] lnxi.com&gt; 1121223278 -0600
</pre>
</dl>
<h2>VARIABLES</h2>
<p> GIT_AUTHOR_IDENT</p>
<dl>
<dt>
<dd> The author of a piece of code.</dl>
<p> GIT_COMMITTER_IDENT</p>
<dl>
<dt>
<dd> The person who put a piece of code into Git.</dl>
<p> GIT_EDITOR</p>
<dl>
<dt>
<dd> Text editor for use by Git commands. The value is meant to be interpreted by the shell when it is used. Examples: <code>~/bin/vi</code>, <code>$SOME_ENVIRONMENT_VARIABLE</code>, <code>&quot;C:\Program Files\Vim\gvim.exe&quot; &#8211;nofork</code>. The order of preference is the <code>$GIT_EDITOR</code> environment variable, then <code>core.editor</code> configuration, then <code>$VISUAL</code>, then <code>$EDITOR</code>, and then the default chosen at compile time, which is usually <i>vi</i>. The build you are using chose <i>editor</i> as the default.</dl>
<p> GIT_PAGER</p>
<dl>
<dt>
<dd> Text viewer for use by Git commands (e.g., <i>less</i>). The value is meant to be interpreted by the shell. The order of preference is the <code>$GIT_PAGER</code> environment variable, then <code>core.pager</code> configuration, then <code>$PAGER</code>, and then the default chosen at compile time (usually <i>less</i>). The build you are using chose <i>pager</i> as the default.</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-git-commit-tree/">git-commit-tree</a></code>(1) <code><a href="/docs/linux/man/1-git-tag/">git-tag</a></code>(1) <code><a href="/docs/linux/man/1-git-config/">git-config</a></code>(1)</p>
<h2>GIT</h2>
<p> Part of the <code><a href="/docs/linux/man/1-git/">git</a></code>(1) suite </p>
<h2>Index</h2>
