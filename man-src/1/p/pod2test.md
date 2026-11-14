---
title: "pod2test(1)"
name: "pod2test"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pod2test/"
description: "pod2test – Convert embedded tests and code examples to .t files"
---

<h2 class="name">NAME</h2>
<p> pod2test &#8211; Convert embedded tests and code examples to .t files </p>
<h2>SYNOPSIS</h2>
<pre><code>
pod2test[-Mmodule][input[output]]
</code></pre>
<h2>DESCRIPTION</h2>
<p> <code>pod2test</code> is a front-end for Pod::Tests (formerly Test::Inline 1). It generates TAP-compatible .t testing scripts from embedded tests and code examples. </p>
<p> If output is not specified, the resulting .t file will go to <font SIZE="-1">STDOUT.</font> Otherwise, it will go to the given output file. If input is not given, it will draw from <font SIZE="-1">STDIN.</font> </p>
<p> If the given file contains no tests or code examples, no output will be given, no output file will be created and pod2test will exit with 1. </p>
<p> The Test::More module is made available to the testing blocks using the &#8216;no_plan&#8217; feature. Any further modules which should be used are specified with -M. <font SIZE="-1"><code>UNIMPLEMENTED</code></font></p>
<h2>BUGS and CAVEATS</h2>
<p> This is a very simple rough cut. It only does very rudimentary tests on the examples.</p>
<h2>SUPPORT</h2>
<p> This script has been superceded by <tt>&quot;inline2test&quot;</tt> from the newer Test::Inline 2. Most testing code that currently works with <tt>&quot;pod2test&quot;</tt> should continue to work with the new version. </p>
<p> The most notable exceptions are <tt>&quot;=for begin&quot;</tt> and <tt>&quot;=for end&quot;</tt>, which are deprecated in the newer version. </p>
<p> After upgrading Test::Inline, Pod::Tests and <tt>&quot;pod2test&quot;</tt> were split out to provide a compatibility package for legacy code. </p>
<p> <tt>&quot;pod2test&quot;</tt> will stay in <font SIZE="-1">CPAN,</font> but should remain unchanged indefinately, with the exception of any minor bugs that will require squishing. </p>
<p> Bugs in this dist should be reported via the following <font SIZE="-1">URL.</font> Feature requests should not be submitted, as further development is now occuring in Test::Inline. </p>
<p> &lt;<a rel="nofollow" href="http://rt.cpan.org/NoAuth/ReportBug.html?Queue=Pod-Tests">http://rt.cpan.org/NoAuth/ReportBug.html?Queue=Pod-Tests</a>&gt;</p>
<h2>AUTHOR</h2>
<p> Michael G Schwern &lt;schwern [at] pobox.com&gt; </p>
<p> Adam Kennedy &lt;adamk [at] cpan.org&gt;</p>
<h2>SEE ALSO</h2>
<p> Pod::Tests, Test::Inline</p>
<h2>COPYRIGHT</h2>
<p> Copyright 2005 &#8211; 2008 Adam Kennedy. </p>
<p> Copyright 2001 &#8211; 2003 Michael G Schwern. </p>
<p> This program is free software; you can redistribute it and/or modify it under the same terms as Perl itself. </p>
<p> The full text of the license can be found in the <font SIZE="-1">LICENSE</font> file included with this module. </p>
<h2>Index</h2>
