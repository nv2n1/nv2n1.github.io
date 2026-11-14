---
title: "scan_mojibake(1)"
name: "scan_mojibake"
section: "1"
letter: "s"
url: "/docs/linux/man/1-scan_mojibake/"
---

<h2 class="name">NAME</h2>
 

 scan_mojibake - scan Perl source and report bad character encoding 

<h2>VERSION</h2>

 version 0.9

<h2>SYNOPSIS</h2>

 <pre>
 scan_mojibake [FILES|DIRS]
</pre>

<h2>DESCRIPTION</h2>

 Standalone <font SIZE="-1">CLI</font> wrapper for the Test::Mojibake module. 

 Does exactly the same as: 

 <pre>
 perl -MTest::Mojibake -e 'all_files_encoding_ok(@ARGV)' bin/ lib/ t/*.t
</pre>

<h2>EXAMPLE</h2>

 <pre><code>
$ scan_mojibake bin / lib / t/*.t
 1..14
 ok 1 - Mojibake test for bin/scan_mojibake
 ok 2 - Mojibake test for lib/Test/Mojibake.pm
 ok 3 - Mojibake test for t/00-load.t
 ok 4 - Mojibake test for t/01-bad-check.t
 ok 5 - Mojibake test for t/01-self-check.t
 ok 6 - Mojibake test for t/01-test-check.t
 ok 7 - Mojibake test for t/02-bad-source.t
 ok 8 - Mojibake test for t/02-good-source.t
 ok 9 - Mojibake test for t/03-bad-pod.t
 ok 10 - Mojibake test for t/03-good-pod.t
 ok 11 - Mojibake test for t/04-bom.t
 ok 12 - Mojibake test for t/05-encode.t
 ok 13 - Mojibake test for t/06-pp-vs-xs.t
 ok 14 - Mojibake test for t/07-broken-utf8.t
</code></pre>

<h2>SEE ALSO</h2>

<dl>
<dt>&bull;
<dd> Test::Mojibake</dl>

<h2>AUTHOR</h2>

 Stanislaw Pusep &lt;stas [at] sysd.org&gt;

<h2>COPYRIGHT AND LICENSE</h2>

 This software is copyright (c) 2014 by Stanislaw Pusep. 

 This is free software; you can redistribute it and/or modify it under the same terms as the Perl 5 programming language system itself. 

<h2>Index</h2>


