---
title: "git-sed(1)"
name: "git-sed"
section: "1"
letter: "g"
url: "/docs/linux/man/1-git-sed/"
description: "git-sed – replace patterns in git-controlled files"
---

<h2>NAME</h2>
<p> <code>git-sed</code> &#8211; replace patterns in git-controlled files</p>
<h2>SYNOPSIS</h2>
<p> <code>git-sed</code> [ -c ] [ -f <i>flags</i> ] <i>search</i> <i>replacement</i></p>
<h2>DESCRIPTION</h2>
<p> Run git grep and then send results to sed for replacement with the given flags, if -f is provided. </p>
<p> Also runs git commit if -c is provided.</p>
<h2>OPTIONS</h2>
<p> -c </p>
<p> commit the resulting changes with a standard commit message detailing the exact command ran. will fail if there are unstaged changes. </p>
<p> -f &lt;flags&gt; </p>
<p> will use the given regex flags in the sed command (for example &quot;g&quot; replaces multiple times on the same line). </p>
<p> &lt;search&gt; </p>
<p> the pattern passed to grep and to the first part of the sed expression. </p>
<p> &lt;replacement&gt; </p>
<p> the replacement passed to sed, the second part of the sed expression.</p>
<h2>EXAMPLES</h2>
<pre>
$ git sed 'my_function' 'do_stuff'
# ... only does the changes, without committing
$ git commit -m&quot;use proper function name&quot;
$ git sed -c 'do_stuff' 'stuff'
# .. does the changes and a commit
$ git sed -f g do_stuff stuff
# .. g is actually pretty important, otherwise you will miss some
# stuff!
</pre>
<h2>AUTHOR</h2>
<p> Written by Antoine Beaupré &lt;<i>anarcat [at] debian.org</i>&gt; from inspiration by <a rel="nofollow" href="https://github.com/da-x/git-search-replace">https://github.com/da-x/git-search-replace</a> and <a href="http://stackoverflow.com/questions/9651898/is-there-a-git-sed-or-equivalent">http://stackoverflow.com/questions/9651898/is-there-a-git-sed-or-equivalent</a></p>
<h2>REPORTING BUGS</h2>
<p> &lt;<i><a rel="nofollow" href="https://github.com/tj/git-extras/issues">https://github.com/tj/git-extras/issues</a></i>&gt;</p>
<h2>SEE ALSO</h2>
<p> &lt;<i><a rel="nofollow" href="https://github.com/tj/git-extras">https://github.com/tj/git-extras</a></i>&gt; </p>
<h2>Index</h2>
