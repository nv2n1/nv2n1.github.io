---
title: "git-contrib(1)"
name: "git-contrib"
section: "1"
letter: "g"
url: "/docs/linux/man/1-git-contrib/"
description: "git-contrib – Show user’s contributions"
---

<h2>NAME</h2>
<p> <code>git-contrib</code> &#8211; Show user&#8217;s contributions</p>
<h2>SYNOPSIS</h2>
<p> <code>git-contrib</code> [&lt;username&gt;|&lt;email&gt;]</p>
<h2>DESCRIPTION</h2>
<p> Output a user&#8217;s contributions to a project, based on the author name or email. Returns multiple entries if there are more than one match.</p>
<h2>OPTIONS</h2>
<p> &lt;username&gt; </p>
<p> The name or email of the user who owns the contributions.</p>
<h2>EXAMPLES</h2>
<pre>
Searching with a username
$ git contrib visionmedia
visionmedia (18):
  Export STATUS_CODES
  Moved help msg to node-repl
  Added multiple arg support for sys.puts(), print(), etc.
  Fix stack output on socket error
  ...
Searching with a partial email
$ git contrib tj@
visionmedia (18):
  Export STATUS_CODES
  Moved help msg to node-repl
  Added multiple arg support for sys.puts(), print(), etc.
  Fix stack output on socket error
  ...
</pre>
<h2>AUTHOR</h2>
<p> Written by Tj Holowaychuk &lt;<i>tj [at] vision-media.ca</i>&gt;</p>
<h2>REPORTING BUGS</h2>
<p> &lt;<i><a rel="nofollow" href="https://github.com/tj/git-extras/issues">https://github.com/tj/git-extras/issues</a></i>&gt;</p>
<h2>SEE ALSO</h2>
<p> &lt;<i><a rel="nofollow" href="https://github.com/tj/git-extras">https://github.com/tj/git-extras</a></i>&gt; </p>
<h2>Index</h2>
