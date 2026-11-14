---
title: "git-summary(1)"
name: "git-summary"
section: "1"
letter: "g"
url: "/docs/linux/man/1-git-summary/"
description: "git-summary – Show repository summary"
---

<h2>NAME</h2>
<p> <code>git-summary</code> &#8211; Show repository summary</p>
<h2>SYNOPSIS</h2>
<p> <code>git-summary</code> [&#8211;line] [&lt;commitish&gt;]</p>
<h2>DESCRIPTION</h2>
<p> Shows a summary of the repository.</p>
<h2>OPTIONS</h2>
<p> &lt;commitish&gt; </p>
<p> Summarize only the range of commits included in the &lt;commitish&gt;. </p>
<p> &#8211;line </p>
<p> Summarize with lines other than commits. This actually just results in a call to <code><a href="/docs/linux/man/1-git-line-summary/">git-line-summary</a></code>(1). Any &lt;commitish&gt; is ignored when &#8211;line is specified. See <code><a href="/docs/linux/man/1-git-line-summary/">git-line-summary</a></code>(1) for more info.</p>
<h2>EXAMPLES</h2>
<p> Outputs a repo summary:</p>
<dl>
<dt>
<dd>
<pre>
$ git summary
project  : express
repo age : 10 months ago
commits  : 1893
active   : 93 days
files    : 111
authors  :
 1285 visionmedia
  478 Tj Holowaychuk
   48 Aaron Heckmann
   34 csausdev
   26 ciaranj
    6 Guillermo Rauch
    3 Nick Poulden
    2 Brian McKinney
    2 Benny Wong
    1 Justin Lilly
    1 James Herdman
    1 Adam Sanderson
    1 Viktor Kelemen
    1 Gregory Ritter
    1 Greg Ritter
    1 ewoudj
    1 isaacs
    1 Matt Colyer
</pre>
<dt>
<dd></dl>
<p> This command can also take a commitish, and will print a summary for the range of commits included in the commitish:</p>
<dl>
<dt>
<dd>
<pre>
$ git summary v42..
</pre>
<dt>
<dd></dl>
<h2>AUTHOR</h2>
<p> Written by Tj Holowaychuk &lt;<i>tj [at] vision-media.ca</i>&gt;</p>
<h2>REPORTING BUGS</h2>
<p> &lt;<i><a rel="nofollow" href="https://github.com/tj/git-extras/issues">https://github.com/tj/git-extras/issues</a></i>&gt;</p>
<h2>SEE ALSO</h2>
<p> &lt;<i><a rel="nofollow" href="https://github.com/tj/git-extras">https://github.com/tj/git-extras</a></i>&gt; </p>
<h2>Index</h2>
