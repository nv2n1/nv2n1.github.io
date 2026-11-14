---
title: "testscriptage(3)"
name: "testscriptage"
section: "3"
letter: "t"
url: "/docs/linux/man/3-testscriptage/"
description: "Test::ScriptAge — routines relating to the age of Perl scripts"
---

<p>Test::ScriptAge &#8212; routines relating to the age of Perl scripts </p>
<h2>Synopsis</h2>
<pre> my $executable_epoch = Test::ScriptAge::our_modification_epoch();
 print 'This script was last modified at ' . localtime($executable_epoch) . &quot;
&quot;;
 my $perl_epoch = Test::ScriptAge::perl_modification_epoch();
 print 'Perl was last modified at ' . localtime($perl_epoch) . &quot;
&quot;;</pre>
<h2>Description</h2>
<p>Routines to calculated modification times of Perl scripts.</p>
<h2>Functions</h2>
<dl COMPACT>
<dt>perl_modification_epoch</p>
<dd>Calculate the time our Perl was last modified.</p>
<dt>our_modification_epoch</p>
<dd>Calculate the time our scripts, including all libraries, was last modified.</dl>
<h2>Author</h2>
<p>Originally written by Felix Lechner &lt;felix.lechner [at] lease-up.com&gt; for Lintian.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-lintian/">lintian</a></code>(1)</p>
