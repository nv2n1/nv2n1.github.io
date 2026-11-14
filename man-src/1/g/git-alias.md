---
title: "git-alias(1)"
name: "git-alias"
section: "1"
letter: "g"
url: "/docs/linux/man/1-git-alias/"
description: "git-alias – Define, search and show aliases"
---

<h2>NAME</h2>
<p> <code>git-alias</code> &#8211; Define, search and show aliases</p>
<h2>SYNOPSIS</h2>
<p> <code>git-alias</code><br />
 <code>git-alias</code> &lt;search-pattern&gt;<br />
 <code>git-alias</code> &lt;alias-name&gt; &lt;command&gt;</p>
<h2>DESCRIPTION</h2>
<p> List all aliases, show one alias, or set one (global) alias.</p>
<h2>OPTIONS</h2>
<p> &lt;search-pattern&gt; </p>
<p> The pattern used to search aliases. </p>
<p> &lt;alias-name&gt; </p>
<p> The name of the alias to create. </p>
<p> &lt;command&gt; </p>
<p> The command for which you are creating an alias.</p>
<h2>EXAMPLES</h2>
<p> Defining a new alias:</p>
<dl>
<dt>
<dd>
<pre>
$ git alias last &quot;cat-file commit HEAD&quot;
</pre>
<dt>
<dd></dl>
<p> Providing only one argument, <code>git-alias</code> searchs for aliases matching the given value:</p>
<dl>
<dt>
<dd>
<pre>
$ git alias ^la
last = cat-file commit HEAD
</pre>
<dt>
<dd></dl>
<p> <code>git-alias</code> will show all aliases if no argument is given:</p>
<dl>
<dt>
<dd>
<pre><code>
$ git alias
    s = status
        amend = commit-- amend
            rank = shortlog - sn-- no - merges whatis = show - s-- pretty = 'tformat:%h (%s, %ad)' --date = short
                                                            whois = !sh - c 'git log -i -1 --pretty="format:%an &lt;%ae&gt;
</code></pre>
<dt>
<dd></dl>
<h2>AUTHOR</h2>
<p> Written by Jonhnny Weslley &lt;<i>jw [at] jonhnnyweslley.net</i>&gt;</p>
<h2>REPORTING BUGS</h2>
<p> &lt;<i><a rel="nofollow" href="https://github.com/tj/git-extras/issues">https://github.com/tj/git-extras/issues</a></i>&gt;</p>
<h2>SEE ALSO</h2>
<p> &lt;<i><a rel="nofollow" href="https://github.com/tj/git-extras">https://github.com/tj/git-extras</a></i>&gt; </p>
<h2>Index</h2>
