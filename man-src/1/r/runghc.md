---
title: "runghc(1)"
name: "runghc"
section: "1"
letter: "r"
url: "/docs/linux/man/1-runghc/"
description: "runghc – program to run Haskell programs without first having to compile them."
---

<h2 class="name">NAME</h2>
<p> runghc &#8211; program to run Haskell programs without first having to compile them. </p>
<h2>SYNOPSIS</h2>
<p> <code>runghc</code> [runghc|flags] [GHC|flags] module [program|flags]&#8230; </p>
<h2>DESCRIPTION</h2>
<p> <code>runghc </code> is considered a non-interactive interpreter and part of The Glasgow Haskell Compiler. <code>runghc</code> is a compiler that automatically runs its results at the end. </p>
<h2>OPTIONS</h2>
<dl>
<dt>the flags are:</p>
<dd>
<dt><code>-f</code></p>
<dd> it tells runghc which GHC to use to run the program. If it is not given then runghc will search for GHC in the directories in the system search path. runghc -f /path/to/ghc</p>
<dt><code>&#8212; </code></p>
<dd> runghc will try to work out where the boundaries between [runghc flags] and [GHC flags], and [GHC flags] and module are, but you can use a &#8212; flag if it doesn&#8217;t get it right. For example, runghc &#8212; -fglasgow-exts Foo means runghc won&#8217;t try to use glasgow-exts as the path to GHC, but instead will pass the flag to GHC. </p>
</dl>
<h2>EXAMPLES</h2>
<dl>
<dt><code>runghc foo</code></p>
<dd></dl>
<p> <code>runghc -f /path/to/ghc foo</code></p>
<dl>
<dt><code>runghc &#8212; -fglasgow-exts Foo</code></p>
<dd>
</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-ghc/">ghc</a></code>(1), <code><a href="/docs/linux/man/1-ghci/">ghci</a></code>(1). </p>
<h2>COPYRIGHT</h2>
<p> Copyright 2002, The University Court of the University of Glasgow. All rights reserved. </p>
<h2>AUTHOR</h2>
<p> This manual page was written by Efrain Valles Pulgar &lt;effie.jayx [at] gmail.com&gt;. This is free documentation; see the GNU General Public Licence version 2 or later for copying conditions. There is NO WARRANTY. </p>
<h2>Index</h2>
