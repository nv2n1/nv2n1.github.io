---
title: "git-reauthor(1)"
name: "git-reauthor"
section: "1"
letter: "g"
url: "/docs/linux/man/1-git-reauthor/"
description: "git-reauthor – Rewrite history to change author’s identity"
---

<h2>NAME</h2>
<p> <code>git-reauthor</code> &#8211; Rewrite history to change author&#8217;s identity</p>
<h2>SYNOPSIS</h2>
<p> <code>git reauthor [&lt;options&gt;]</code></p>
<h2>DESCRIPTION</h2>
<p> Lets you replace the author and/or committer identities in commits and tags. </p>
<p> The command goes through all existing commits and tags in all local branches to selectively modify the identities present in those objects. All the other informations such as dates, messages,.. are preserved. </p>
<p> You can rewrite all the identities in the commits and tags objects by using the &#8211;all flag, or only replace the identities whose email matches the value of the &#8211;old-email option. It is also possible to limit the rewrite to a certain type of identity: the author or the committer identity. By default, both of them are affected.<br />
 For each of those identities to update, the command will replace the name and/or email with the new correct values as defined via the options. If the new identity name to set is not defined, the current one will be kept (and vice-versa with the email). </p>
<p> <code>WARNING!</code> This command rewrites history and as a result you will not able to push your branch to the remote without using the &#8211;force option.<br />
 See more information with <code>git help filter-branch</code>.</p>
<h2>OPTIONS</h2>
<p> -a, &#8211;all</p>
<dl>
<dt>
<dd>
<pre>
Rewrite ALL identities in commits and tags.
</pre>
<dt>
<dd></dl>
<p> -c, &#8211;use-config</p>
<dl>
<dt>
<dd>
<pre>
Define correct values from user Git config
Values of --correct-email and --correct-name options take precedence over the ones from the config if specified as well
</pre>
<dt>
<dd></dl>
<p> -e, &#8211;correct-email &lt;<i>email</i>&gt;</p>
<dl>
<dt>
<dd>
<pre>
Define the correct email to set
Empty email '' is allowed
</pre>
<dt>
<dd></dl>
<p> -n, &#8211;correct-name &lt;<i>name</i>&gt;</p>
<dl>
<dt>
<dd>
<pre>
Define the correct name to set
Empty name '' is not allowed
</pre>
<dt>
<dd></dl>
<p> -o, &#8211;old-email &lt;<i>email</i>&gt;</p>
<dl>
<dt>
<dd>
<pre>
Rewrite identities matching old email in commits and tags
Empty email '' is allowed
</pre>
<dt>
<dd></dl>
<p> -t, &#8211;type &lt;<i>id</i>&gt;</p>
<dl>
<dt>
<dd>
<pre>
Define the type of identities affected by the rewrite
Possible type identifiers are: author, committer, both (default)
</pre>
<dt>
<dd></dl>
<h2>EXAMPLES</h2>
<p> Replace the personal email and name of Jack to his work ones</p>
<dl>
<dt>
<dd>
<pre><code>
$ git reauthor-- old - email jack[at] perso.me-- correct - email jack[at] work.com-- correct - name 'Jack Foobar'
</code></pre>
<dt>
<dd></dl>
<p> Replace the email and name of Jack to the ones defined in the Git config</p>
<dl>
<dt>
<dd>
$ git reauthor&#8211; old &#8211; email jack[at] perso.me&#8211; use &#8211; config</p>
<dt>
<dd></dl>
<p> Replace only the email of Jack (keep the name already used)</p>
<dl>
<dt>
<dd>
$ git reauthor&#8211; old &#8211; email jack[at] perso&#8211; correct &#8211; email jack[at] perso.me</p>
<dt>
<dd></dl>
<p> Change only the committer email of Jack (keep the author email already used)</p>
<dl>
<dt>
<dd>
$ git reauthor&#8211; old &#8211; email jack[at] perso.me&#8211; correct &#8211; email jack[at] work.com&#8211; type committer</p>
<dt>
<dd></dl>
<p> Set Jack&#8217;s identity as the only one of the whole repository</p>
<dl>
<dt>
<dd>
$ git reauthor&#8211; all&#8211; correct &#8211; email jack[at] perso.me&#8211; correct &#8211; name Jack</p>
<dt>
<dd></dl>
<p> Set Jack as the only committer of the whole repository (keeps authors)</p>
<dl>
<dt>
<dd>
<pre><code>
$ git reauthor-- all-- correct - email jack[at] perso.me-- correct - name Jack-- type committer
</code></pre>
<dt>
<dd></dl>
<h2>AUTHOR</h2>
<p> Written by Damien Tardy-Panis &lt;<i>damien [at] tardypad.me</i>&gt;</p>
<h2>REPORTING BUGS</h2>
<p> &lt;<i><a rel="nofollow" href="http://github.com/tj/git-extras/issues">http://github.com/tj/git-extras/issues</a></i>&gt;</p>
<h2>SEE ALSO</h2>
<p> &lt;<i><a rel="nofollow" href="https://github.com/tj/git-extras">https://github.com/tj/git-extras</a></i>&gt; </p>
<h2>Index</h2>
