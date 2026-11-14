---
title: "git-check-ignore(1)"
name: "git-check-ignore"
section: "1"
letter: "g"
url: "/docs/linux/man/1-git-check-ignore/"
description: "git-check-ignore – Debug gitignore / exclude files"
---

<h2 class="name">NAME</h2>
<p> git-check-ignore &#8211; Debug gitignore / exclude files </p>
<h2>SYNOPSIS</h2>
<pre><code>
git check - ignore[&lt;options&gt;]&lt;pathname&gt;... git check - ignore[&lt;options&gt;]-- stdin
</code></pre>
<h2>DESCRIPTION</h2>
<p> For each pathname given via the command-line or from a file via <code>&#8211;stdin</code>, check whether the file is excluded by .gitignore (or other input files to the exclude mechanism) and output the path if it is excluded. </p>
<p> By default, tracked files are not shown at all since they are not subject to exclude rules; but see &#8216;&#8211;no-index&#8217;.</p>
<h2>OPTIONS</h2>
<p> -q, &#8211;quiet</p>
<dl>
<dt>
<dd> Don&#8217;t output anything, just set exit status. This is only valid with a single pathname.</dl>
<p> -v, &#8211;verbose</p>
<dl>
<dt>
<dd> Instead of printing the paths that are excluded, for each path that matches an exclude pattern, print the exclude pattern together with the path. (Matching an exclude pattern usually means the path is excluded, but if the pattern begins with <i>!</i> then it is a negated pattern and matching it means the path is NOT excluded.) </p>
<p> For precedence rules within and between exclude sources, see <code><a href="/docs/linux/man/5-gitignore/">gitignore</a></code>(5).</dl>
<p> &#8211;stdin</p>
<dl>
<dt>
<dd> Read pathnames from the standard input, one per line, instead of from the command-line.</dl>
<p> -z</p>
<dl>
<dt>
<dd> The output format is modified to be machine-parsable (see below). If <code>&#8211;stdin</code> is also given, input paths are separated with a NUL character instead of a linefeed character.</dl>
<p> -n, &#8211;non-matching</p>
<dl>
<dt>
<dd> Show given paths which don&#8217;t match any pattern. This only makes sense when <code>&#8211;verbose</code> is enabled, otherwise it would not be possible to distinguish between paths which match a pattern and those which don&#8217;t.</dl>
<p> &#8211;no-index</p>
<dl>
<dt>
<dd> Don&#8217;t look in the index when undertaking the checks. This can be used to debug why a path became tracked by e.g. <code>git add .</code> and was not ignored by the rules as expected by the user or when developing patterns including negation to match a path previously added with <code>git add -f</code>.</dl>
<h2>OUTPUT</h2>
<p> By default, any of the given pathnames which match an ignore pattern will be output, one per line. If no pattern matches a given path, nothing will be output for that path; this means that path will not be ignored. </p>
<p> If <code>&#8211;verbose</code> is specified, the output is a series of lines of the form: </p>
<p> &lt;source&gt; &lt;COLON&gt; &lt;linenum&gt; &lt;COLON&gt; &lt;pattern&gt; &lt;HT&gt; &lt;pathname&gt; </p>
<p> &lt;pathname&gt; is the path of a file being queried, &lt;pattern&gt; is the matching pattern, &lt;source&gt; is the pattern&#8217;s source file, and &lt;linenum&gt; is the line number of the pattern within that source. If the pattern contained a <code>!</code> prefix or <code>/</code> suffix, it will be preserved in the output. &lt;source&gt; will be an absolute path when referring to the file configured by <code>core.excludesFile</code>, or relative to the repository root when referring to <code>.git/info/exclude</code> or a per-directory exclude file. </p>
<p> If <code>-z</code> is specified, the pathnames in the output are delimited by the null character; if <code>&#8211;verbose</code> is also specified then null characters are also used instead of colons and hard tabs: </p>
<p> &lt;source&gt; &lt;NULL&gt; &lt;linenum&gt; &lt;NULL&gt; &lt;pattern&gt; &lt;NULL&gt; &lt;pathname&gt; &lt;NULL&gt; </p>
<p> If <code>-n</code> or <code>&#8211;non-matching</code> are specified, non-matching pathnames will also be output, in which case all fields in each output record except for &lt;pathname&gt; will be empty. This can be useful when running non-interactively, so that files can be incrementally streamed to STDIN of a long-running check-ignore process, and for each of these files, STDOUT will indicate whether that file matched a pattern or not. (Without this option, it would be impossible to tell whether the absence of output for a given file meant that it didn&#8217;t match any pattern, or that the output hadn&#8217;t been generated yet.) </p>
<p> Buffering happens as documented under the <code>GIT_FLUSH</code> option in <code><a href="/docs/linux/man/1-git/">git</a></code>(1). The caller is responsible for avoiding deadlocks caused by overfilling an input buffer or reading from an empty output buffer.</p>
<h2>EXIT STATUS</h2>
<p> 0</p>
<dl>
<dt>
<dd> One or more of the provided paths is ignored.</dl>
<p> 1</p>
<dl>
<dt>
<dd> None of the provided paths are ignored.</dl>
<p> 128</p>
<dl>
<dt>
<dd> A fatal error was encountered.</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/5-gitignore/">gitignore</a></code>(5) <code><a href="/docs/linux/man/1-git-config/">git-config</a></code>(1) <code><a href="/docs/linux/man/1-git-ls-files/">git-ls-files</a></code>(1)</p>
<h2>GIT</h2>
<p> Part of the <code><a href="/docs/linux/man/1-git/">git</a></code>(1) suite </p>
<h2>Index</h2>
