---
title: "dh_bash-completion(1)"
name: "dh_bash-completion"
section: "1"
letter: "d"
url: "/docs/linux/man/1-dh_bash-completion/"
description: "dh_bash-completion – install bash completions for package"
---

<h2 class="name">NAME</h2>
<p> dh_bash-completion &#8211; install bash completions for package </p>
<h2>SYNOPSIS</h2>
<p> <code>dh_bash-completion</code> [<i>debhelper options</i>]</p>
<h2>DESCRIPTION</h2>
<p> dh_bash-completion is a debhelper program that is responsible for installing completions for bash, usable installing the &#8220;bash-completion&#8221; package. </p>
<p> If a file named debian/package.bash-completion exists, then different actions are performed, depending on its format. </p>
<p> It can be a proper completion snippet, and in that case it would be installed in the completion directory, and no other actions would be performed. </p>
<p> It can also be a list of files, with an optionally specified name to call the completion snippet after. The file format is as follows: </p>
<pre>
  my/path/to/foo-completion       # this would be installed as &quot;foo-completion&quot;
  my/path/to/bar-completion  baz  # this would be installed as &quot;baz&quot;
</pre>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-debhelper/">debhelper</a></code>(1) </p>
<p> This program is a part of bash-completion. </p>
<p> <code><a href="/docs/linux/man/1-bash/">bash</a></code>(1)</p>
<h2>AUTHOR</h2>
<p> David Paleino &lt;d.paleino [at] gmail.com&gt; </p>
<h2>Index</h2>
