---
title: "git-rename-tag(1)"
name: "git-rename-tag"
section: "1"
letter: "g"
url: "/docs/linux/man/1-git-rename-tag/"
description: "git-rename-tag – Rename a tag"
---

<h2>NAME</h2>
<p> <code>git-rename-tag</code> &#8211; Rename a tag</p>
<h2>SYNOPSIS</h2>
<p> <code>git-rename-tag</code> &lt;old-tag-name&gt; &lt;new-tag-name&gt;</p>
<h2>DESCRIPTION</h2>
<p> Rename a tag (locally and remotely)</p>
<h2>OPTIONS</h2>
<p> &lt;old-tag-name&gt; </p>
<p> The name of the tag you want to rename. </p>
<p> &lt;new-tag-name&gt; </p>
<p> The new name of the tag.</p>
<h2>EXAMPLES</h2>
<pre><code>
$ git tag test
    $ git push-- tags
        Total 0(delta 0),
    reused 0(delta 0)
            To git[at] myserver.com : myuser
        / myrepository.git
        * [new tag] test -&gt; test
                                $ git tag
                                test
                                $ git rename
                                - tag test test2
                                Deleted tag 'test'(was 1111111)
                                    Total 0(delta 0),
    reused 0(delta 0)
            To git[at] myserver.com : myuser
        / myrepository.git
        * [new tag] test2 -&gt; test2
                                 remote : warning : Deleting a non
                                                    -
                                                    existent ref.To git[at] myserver.com : myuser / myrepository.git
                                                    -
                                                    [deleted] refs / tag / test $ git tag test2
</code></pre>
<h2>AUTHOR</h2>
<p> Written by Jesús Espino &lt;<i>jespinog [at] gmail.com</i>&gt;</p>
<h2>REPORTING BUGS</h2>
<p> &lt;<i><a rel="nofollow" href="https://github.com/tj/git-extras/issues">https://github.com/tj/git-extras/issues</a></i>&gt;</p>
<h2>SEE ALSO</h2>
<p> &lt;<i><a rel="nofollow" href="https://github.com/tj/git-extras">https://github.com/tj/git-extras</a></i>&gt; </p>
<h2>Index</h2>
