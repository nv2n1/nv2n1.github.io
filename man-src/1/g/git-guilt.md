---
title: "git-guilt(1)"
name: "git-guilt"
section: "1"
letter: "g"
url: "/docs/linux/man/1-git-guilt/"
description: "git-guilt – calculate change between two revisions"
---

<h2>NAME</h2>
<p> <code>git-guilt</code> &#8211; calculate change between two revisions</p>
<h2>SYNOPSIS</h2>
<p> <code>git guilt</code> [&lt;option&gt;]<br />
 <code>git guilt</code> [&lt;option&gt;] &lt;since&gt; [&lt;until&gt;]</p>
<h2>DESCRIPTION</h2>
<p> In the first form, shows total blame count for files with unstaged changes. </p>
<p> In the second form, calculates the change in blame between two revisions. If not specified, &lt;until&gt; will default to HEAD.</p>
<h2>OPTIONS</h2>
<p> -h </p>
<p> Output usage information </p>
<p> -e, &#8211;email </p>
<p> Display author emails instead of names </p>
<p> -w, &#8211;ignore-whitespace </p>
<p> Ignore whitespace only changes when attributing blame </p>
<p> -d, &#8211;debug </p>
<p> Output debug information</p>
<h2>Examples</h2>
<p> Find blame on unstaged modified files:</p>
<dl>
<dt>
<dd>
<pre>
$ git guilt      (1)
spacewander                   ++++
(1) There is only one modified file and it is not staged. The four
plusses means that the file has four lines, all contributed by spacewander.
</pre>
<dt>
<dd></dl>
<p> Find blame delta between two commits:</p>
<dl>
<dt>
<dd>
<pre><code>
$ git guilt HEAD ~3 HEAD ^
    spacewander++ ++ ++ ++ ++ ++ ++ ++ ++ ++ ++ ++ ++ ++ ++ ++ ++ ++ ++ ++ ++ ++ +(115)
            Jesse Sipprell
        -
</code></pre>
<dt>
<dd></dl>
<p> Find blame delta over the last three weeks:</p>
<dl>
<dt>
<dd>
$ git guilt `git log&#8211; until = &#8220;3 weeks ago&#8221; &#8211;format = &#8220;%H&#8221; &#8211; n 1` Paul Schreiber++ ++ ++ ++ ++ ++ ++ ++ ++ ++ ++ ++ ++ ++ ++ ++ ++ ++ ++ ++ ++ ++ +(349)spacewander++ ++ ++ ++ ++ ++ ++ ++ ++ ++ ++ ++ ++ ++ ++ ++ ++ ++ ++ ++ ++ ++ +(113)Mark Eissler++ ++ ++ ++ ++ ++ ++ ++ ++ ++ ++ ++ ++CJ++ ++ +nickl &#8211; -Jesse Sipprell &#8211;<br />
                                                        Evan Grim &#8211;<br />
                                                        Ben Parnell &#8211;<br />
                                                        hemanth.hm&#8211;</p>
<dt>
<dd></dl>
<p> Since git 1.8.5, the above can also be written as: </p>
<p> $ git guilt @{3.weeks.ago} </p>
<p> Find blame delta for a topic branch:</p>
<dl>
<dt>
<dd>
<pre><code>
$ git guilt `git merge - base master git - guilt` git - guilt spacewander++ ++ ++ ++ ++ ++ ++ ++ ++ ++ ++ ++ ++ ++ ++ ++ ++ ++ ++ ++ ++ ++ +(112)
</code></pre>
<dt>
<dd></dl>
<h2>AUTHOR</h2>
<p> Written by spacewander &lt;<i>spacewanderlzx [at] gmail.com</i>&gt;</p>
<h2>REPORTING BUGS</h2>
<p> &lt;<i><a rel="nofollow" href="https://github.com/tj/git-extras/issues">https://github.com/tj/git-extras/issues</a></i>&gt;</p>
<h2>SEE ALSO</h2>
<p> &lt;<i><a rel="nofollow" href="https://github.com/tj/git-extras">https://github.com/tj/git-extras</a></i>&gt; </p>
<h2>Index</h2>
