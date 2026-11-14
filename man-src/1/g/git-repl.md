---
title: "git-repl(1)"
name: "git-repl"
section: "1"
letter: "g"
url: "/docs/linux/man/1-git-repl/"
description: "git-repl – git read-eval-print-loop"
---

<h2>NAME</h2>
<p> <code>git-repl</code> &#8211; git read-eval-print-loop</p>
<h2>SYNOPSIS</h2>
<p> <code>git-repl</code></p>
<h2>DESCRIPTION</h2>
<p> Git read-eval-print-loop. Let&#8217;s you run <code>git</code> commands without typing &#8216;git&#8217;. </p>
<p> Commands can be prefixed with an exclamation mark (!) to be interpreted as a regular command. </p>
<p> Type <code>exit</code> or <code>quit</code> to end the repl session.</p>
<h2>COMMANDS</h2>
<p> &lt;command&gt; </p>
<p> Interpreted as <code>git &lt;command&gt;</code>. </p>
<p> !&lt;command&gt; </p>
<p> Interpreted as <code>&lt;command&gt;</code> (not through <code>git</code>). </p>
<p> ls </p>
<p> Equivalent of &#8216;git ls-files&#8217;. </p>
<p> exit|quit </p>
<p> Ends the repl session.</p>
<h2>EXAMPLES</h2>
<pre>
$ git repl
git version 2.9.2
git-extras version 3.0.0
type 'ls' to ls files below current directory,
'!command' to execute any command or just 'subcommand' to execute any git subcommand
git (master)&gt; ls-files
History.md
Makefile
Readme.md
bin/git-changelog
bin/git-count
bin/git-delete-branch
bin/git-delete-tag
bin/git-ignore
bin/git-release
git (master)&gt; !echo Straight from the shell!
Straight from the shell!
git (master)&gt; quit
</pre>
<h2>AUTHOR</h2>
<p> Written by Tj Holowaychuk &lt;<i>tj [at] vision-media.ca</i>&gt;</p>
<h2>REPORTING BUGS</h2>
<p> &lt;<i><a rel="nofollow" href="https://github.com/tj/git-extras/issues">https://github.com/tj/git-extras/issues</a></i>&gt;</p>
<h2>SEE ALSO</h2>
<p> &lt;<i><a rel="nofollow" href="https://github.com/tj/git-extras">https://github.com/tj/git-extras</a></i>&gt; </p>
<h2>Index</h2>
