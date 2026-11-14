---
title: "git-effort(1)"
name: "git-effort"
section: "1"
letter: "g"
url: "/docs/linux/man/1-git-effort/"
description: "git-effort – Show effort statistics on file(s)"
---

<h2>NAME</h2>
<p> <code>git-effort</code> &#8211; Show effort statistics on file(s)</p>
<h2>SYNOPSIS</h2>
<p> <code>git-effort</code> [&#8211;above &lt;value&gt;] [&lt;path&gt;&#8230;] [&#8211; [&lt;log options&gt;&#8230;]]</p>
<h2>DESCRIPTION</h2>
<p> Shows effort statistics about files in the repository. </p>
<p> Display includes:<br />
 &#8211; Commits: number of commits per file &#8211; highlighting files with most activity.<br />
 &#8211; Active days: total number of days which contributed modifications to this file.</p>
<h2>OPTIONS</h2>
<p> &#8211;above &lt;value&gt; </p>
<p> Ignore files with commits &lt;= a value. </p>
<p> &lt;path&gt;&#8230; </p>
<p> Only count commits that touches the given paths. </p>
<p> Note: <code>git-effort</code> does not accept revision ranges, but the underlying <code>git log</code> does (See the examples). </p>
<p> &lt;log options&gt;&#8230; </p>
<p> Options for <code>git log</code>. Note that you must use <code>&#8212;</code> to separate options to <code>git log</code> from options to <code>git effort</code>. This makes it possible to only count commits you are interested in. Not all options are relevant in the context of <code>git-effort</code>, but those that are is listed under the &quot;Commit Limiting&quot; section on the <code>git-log</code> manpages.</p>
<h2>EXAMPLES</h2>
<p> Note: Output will first appear unsorted, then the screen is cleared and the sorted list is output. The initial unsorted list is not shown in the examples for brevity. </p>
<p> Displays &quot;effort&quot; statistics:</p>
<dl>
<dt>
<dd>
<pre><code>
$ git effort-- above 5 file commits active days
        git -
    extras 26 18 git - release 13 13 git - effort 13 2 git - ignore 11 7 git - changelog 11 8 git - graft 9 6 git - summary 8 6 git - delete - branch 8 6 git - repl 7 5 $ git effort-- above 5 bin/* -- --after="one year ago" --author="Leila Muhtasib"
  file                                          commits    active days
  git-extras                                    15         12
  git-release                                   6          4
  git-effort                                    6          2
  git-ignore                                    4          4
  git-changelog                                 3          2
  git-graft                                     2          2
</code></pre>
<dt>
<dd></dl>
<p> Showing statistics on directories is also possible:</p>
<dl>
<dt>
<dd>
<pre>
$ git effort bin man -- --after=&quot;one year ago&quot;
  file                                          commits    active days
  bin.......................................... 406        232
  man.......................................... 118        80
</pre>
<dt>
<dd></dl>
<p> Only count commits in the specified revision range: </p>
<p> $ git effort &#8212; master..feature</p>
<dl>
<dt>
<dd>
<pre>
  file                                          commits    active days
  bin/git-effort............................... 3          2
  man/git-effort.md............................ 1          1
</pre>
<dt>
<dd></dl>
<h2>AUTHOR</h2>
<p> Written by Leila Muhtasib &lt;<i>muhtasib [at] gmail.com</i>&gt;</p>
<h2>REPORTING BUGS</h2>
<p> &lt;<i><a rel="nofollow" href="https://github.com/tj/git-extras/issues">https://github.com/tj/git-extras/issues</a></i>&gt;</p>
<h2>SEE ALSO</h2>
<p> &lt;<i><a rel="nofollow" href="https://github.com/tj/git-extras">https://github.com/tj/git-extras</a></i>&gt; </p>
<h2>Index</h2>
