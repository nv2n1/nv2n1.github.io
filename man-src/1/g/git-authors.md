---
title: "git-authors(1)"
name: "git-authors"
section: "1"
letter: "g"
url: "/docs/linux/man/1-git-authors/"
description: "git-authors – Generate authors report"
---

<h2>NAME</h2>
<p> <code>git-authors</code> &#8211; Generate authors report</p>
<h2>SYNOPSIS</h2>
<p> <code>git-authors</code> [-l, &#8211;list]</p>
<h2>DESCRIPTION</h2>
<p> Populates the file matching <i>authors|contributors -i</i> with the authors of commits, according to the number of commits per author. Opens the file in <code>$EDITOR</code> when set. </p>
<p> See the &quot;MAPPING AUTHORS&quot; section of <code><a href="/docs/linux/man/1-git-shortlog/">git-shortlog</a></code>(1) to coalesce together commits by the same person.</p>
<h2>OPTIONS</h2>
<p> -l, &#8211;list </p>
<p> Show authors.</p>
<h2>EXAMPLES</h2>
<dl>
<dt>Updating AUTHORS file:</p>
<dd>
<dt>
<dd> $ git authors</p>
<dt>Listing authors:</p>
<dd>
<dt>
<dd> $ git authors &#8211;list</p>
<dt>
<dd>
<pre><code>
TJ Holowaychuk&lt;tj[at] vision - media.ca&gt;
        Tj Holowaychuk&lt;tj[at] vision - media.ca&gt;
            hemanth.hm&lt;hemanth.hm[at] gmail.com&gt;
                Jonhnny Weslley&lt;jw[at] jonhnnyweslley.net&gt;
                    nickl -
    &lt;github[at] jigsoft.co.za&gt;
        Leila Muhtasib&lt;muhtasib[at] gmail.com&gt;
</code></pre>
<dt>
<dd>
</dl>
<h2>AUTHOR</h2>
<p> Written by Titus Wormer &lt;<i>tituswormer [at] gmail.com</i>&gt;</p>
<h2>REPORTING BUGS</h2>
<p> &lt;<i><a rel="nofollow" href="https://github.com/tj/git-extras/issues">https://github.com/tj/git-extras/issues</a></i>&gt;</p>
<h2>SEE ALSO</h2>
<p> &lt;<i><a rel="nofollow" href="https://github.com/tj/git-extras">https://github.com/tj/git-extras</a></i>&gt; </p>
<h2>Index</h2>
