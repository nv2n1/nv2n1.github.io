---
title: "git-ignore-io(1)"
name: "git-ignore-io"
section: "1"
letter: "g"
url: "/docs/linux/man/1-git-ignore-io/"
description: "git-ignore-io – Get sample gitignore file"
---

<h2>NAME</h2>
<p> <code>git-ignore-io</code> &#8211; Get sample gitignore file</p>
<h2>SYNOPSIS</h2>
<p> <code>git ignore-io</code> [&lt;OPTIONS&gt;]</p>
<h2>DESCRIPTION</h2>
<p> Get sample gitignore file from gitignore.io <i><a rel="nofollow" href="https://www.gitignore.io">https://www.gitignore.io</a></i></p>
<h2>OPTIONS</h2>
<p> &lt;OPTIONS&gt; </p>
<p> -a, &#8211;append &lt;types&gt;&#8230;<br />
 Append new .gitignore content to .gitignore under the current directory </p>
<p> -r, &#8211;replace &lt;types&gt;&#8230;<br />
 Export new .gitignore to the current directory (The old one will be replaced) </p>
<p> -l, &#8211;list-in-table<br />
 Print available types in table format </p>
<p> -L, &#8211;list-alphabetically<br />
 Print available types in alphabetical order </p>
<p> -s, &#8211;search &lt;word&gt;<br />
 Search word in available types </p>
<p> -t, &#8211;show-update-time<br />
 Show the last modified time of ~/.gi_list (where the list of available types is stored) </p>
<p> -u, &#8211;update-list<br />
 Update ~/.gi_list</p>
<h2>EXAMPLES</h2>
<p> Show sample gitignore file for vim</p>
<dl>
<dt>
<dd>
<pre><code>
$ git ignore - io vim
#Created by https: // www.gitignore.io/api/vim
                   ## #Vim## #
                       [._] *
                           .s[a - w][a - z]
                             [._] s[a - w][a - z] *
                           .un ~Session.vim
                           .netrwhist *
                   ~
</code></pre>
<dt>
<dd></dl>
<p> Append sample gitignore for vim and python to .gitignore in current directory.</p>
<dl>
<dt>
<dd>
<pre>
$ git ignore-io -a vim python
</pre>
<dt>
<dd></dl>
<p> Show all available types</p>
<dl>
<dt>
<dd>
<pre>
$ git ignore-io -l
    actionscript             ada                      agda                     android                  anjuta
    appceleratortitanium     appcode                  appengine                archives                 archlinuxpackages
    autotools                basercms                 bazel                    bluej                    bower
    bricxcc                  c                        c++                      cakephp                  carthage
    ......
</pre>
<dt>
<dd></dl>
<p> Search ja in all available types</p>
<dl>
<dt>
<dd>
<pre>
$ git ignore-io -s ja
    django
    jabref
    java
    ninja
</pre>
<dt>
<dd></dl>
<h2>AUTHOR</h2>
<p> Written by Lee-W <i>cl87654321 [at] gmail.com</i></p>
<h2>REPORTING BUGS</h2>
<p> &lt;<i><a rel="nofollow" href="https://github.com/tj/git-extras/issues">https://github.com/tj/git-extras/issues</a></i>&gt;</p>
<h2>SEE ALSO</h2>
<p> &lt;<i><a rel="nofollow" href="https://github.com/tj/git-extras">https://github.com/tj/git-extras</a></i>&gt; </p>
<h2>Index</h2>
