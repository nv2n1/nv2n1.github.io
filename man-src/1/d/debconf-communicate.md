---
title: "debconf-communicate(1)"
name: "debconf-communicate"
section: "1"
letter: "d"
url: "/docs/linux/man/1-debconf-communicate/"
description: "debconf-communicate – communicate with debconf"
---

<h2 class="name">NAME</h2>
<p> debconf-communicate &#8211; communicate with debconf </p>
<h2>SYNOPSIS</h2>
<pre><code>
echo commands | debconf - communicate[options][package]
</code></pre>
<h2>DESCRIPTION</h2>
<p> <code>debconf-communicate</code> allows you to communicate with debconf on the fly, from the command line. The package argument is the name of the package which you are pretending to be as you communicate with debconf, and it may be omitted if you are lazy. It reads commands in the form used by the debconf protocol from stdin. For documentation on the available commands and their usage, see the debconf specification. </p>
<p> The commands are executed in sequence. The textual return code of each is printed out to standard output. </p>
<p> The return value of this program is the numeric return code of the last executed command.</p>
<h2>EXAMPLE</h2>
<pre>
 echo get debconf/frontend | debconf-communicate
</pre>
<p> Print out the value of the debconf/frontend question.</p>
<h2>WARNING</h2>
<p> This program should never be used from a maintainer script of a package that uses debconf! It may however, be useful in debugging.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-debconf-loadtemplate/">debconf-loadtemplate</a></code>(1)</p>
<h2>AUTHOR</h2>
<p> Joey Hess &lt;joeyh [at] debian.org&gt; </p>
<h2>Index</h2>
