---
title: "tla-gpg-check(1)"
name: "tla-gpg-check"
section: "1"
letter: "t"
url: "/docs/linux/man/1-tla-gpg-check/"
description: "tla-gpg-check – GNU Arch revision signature checker"
---

<h2 class="name">NAME</h2>
<p> tla-gpg-check &#8211; GNU Arch revision signature checker </p>
<h2>SYNOPSIS</h2>
<p> <code>tla-gpg-check</code> gpg_command=&quot;<i>gpg_command</i>&quot;</p>
<h2>DESCRIPTION</h2>
<p> Checks whether a revision is correctly signed. This is indended to be used in tla&#8217;s signing hooks. It calls <i>gpg_command</i> on the standard input and makes sure only one signed message is given. </p>
<p> Here is how to setup a simple automatic tla signature check: </p>
<pre><code>
mkdir - p - m 700 ~ /.arch - params / signing / echo 'tla-gpg-check gpg_command="gpg --verify-files -"' &gt; ~ /.arch - params / signing /= default.check
                                                                                                                                             echo 'gpg --clearsign --use-agent' &gt; ~ /.arch - params / signing /= default
</code></pre>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-tla/">tla</a></code>(1)<br />
 <a rel="nofollow" href="http://www.gnuarch.org/gnuarchwiki/ArchiveSigning">http://www.gnuarch.org/gnuarchwiki/ArchiveSigning</a></p>
<h2>AUTHOR</h2>
<p> tla-gpg-check was written by Tom Lord. </p>
<p> This manual page was written by Sylvain Beucler &lt;beuc [at] beuc.net&gt;, for the Debian project (but may be used by others). </p>
<h2>Index</h2>
