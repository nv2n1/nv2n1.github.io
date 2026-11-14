---
title: "bglprof(1)"
name: "bglprof"
section: "1"
letter: "b"
url: "/docs/linux/man/1-bglprof/"
description: "bglprof – display call graph profile data for Bigloo programs"
---

<h2 class="name">NAME</h2>
<p> bglprof &#8211; display call graph profile data for Bigloo programs</p>
<h2>SYNOPSIS</h2>
<p> <code>bglprof</code> [ options ] [ <i>objfile</i> [ <i>gmon.out</i> ] ] </p>
<h2>DESCRIPTION</h2>
<p> <code>bglprof</code> is a front-end to the <code>gprof</code> program. Any option that applied to <code>gprof</code> suits for <code>bglprof</code>. <code>bglprof</code> reads an extra monitoring file, the <i>bmon.out</i> file. This file is generated when executing a program that has been linked by <code>Bigloo</code> making use of the <i>-p</i> option. See the <code>glprof</code> manual for an detailed documentation. </p>
<h2>OPTIONS</h2>
<dl>
<dt>
<dt><code>-v </code></p>
<dd>
<dd> verbose mode. </p>
</dl>
<h2>EXAMPLE</h2>
<p> Here is the sequence of commands to get a Bigloo profile: </p>
<p> $ bigloo foo.scm -p -unsafe -O4 -c </p>
<p> $ bigloo foo.o -p -unsafe -O4 -c -o a.out </p>
<p> $ ./a.out </p>
<p> $ bglprof </p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-bigloo/">bigloo</a>(1), <a href="/docs/linux/man/1-prof/">prof</a>(1), <a href="/docs/linux/man/1-gprof/">gprof</a>(1) </p>
<h2>AUTHOR</h2>
<p> Manuel SERRANO, Manuel.Serrano [at] inria.fr </p>
<h2>Index</h2>
