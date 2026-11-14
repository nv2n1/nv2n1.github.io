---
title: "mimedefang-pl(8)"
name: "mimedefang-pl"
section: "8"
letter: "m"
url: "/docs/linux/man/8-mimedefang-pl/"
description: "mimedefang.pl – Perl script to scan MIME messages."
---

<p>mimedefang.pl &#8211; Perl script to scan MIME messages.</p>
<h2>Synopsis</h2>
<p><code>mimedefang.pl [-f </code><i>filter</i>] <i>dir</i> </p>
<h2>Description</h2>
<p><code>mimedefang.pl</code> is a Perl script designed to work with <code><a href="/docs/linux/man/8-mimedefang/">mimedefang</a></code>(8). It takes a single argument which is a directory which should contain files laid out as described in <code><a href="/docs/linux/man/8-mimedefang/">mimedefang</a></code>(8). </p>
<h2>Options</h2>
<dl>
<dt><code>-f </code><i>filter</i></p>
<dd>Specifies the name of the file containing the filter. If this option is omitted, the default filter <code>/etc/mail/mimedefang-filter</code> is used. </p>
</dl>
<h2>Operation</h2>
<p><code>mimedefang.pl</code> evaluates the file <code>/etc/mail/mimedefang-filter</code> as a Perl fragment. This file should define the <code>filter</code> procedure. For each part of a MIME message, <code>mimedefang.pl</code> calls <code>filter</code> and disposes of the part as instructed by the filter. The various modes of disposition are described in <code><a href="/docs/linux/man/5-mimedefang-filter/">mimedefang-filter</a></code>(5).</p>
<h2>Testing Filters</h2>
<p>You are <i>strongly</i> recommended to test your filter before installing it in <code>/etc/mail/mimedefang-filter</code>. To test the filter, save it in a file (e.g. <code>test-filter</code>) and run this command: </p>
<pre> mimedefang.pl -f test-filter -test</pre>
<p>This tests the filter for syntactic correctness. If it passes, you can install it as a production filter. (Note that the test tests only for correct Perl syntax; it doesn&#8217;t make sure your filter does something sensible.)</p>
<h2>Miscellaneous Options</h2>
<p>There are a few other ways to invoke mimedefang.pl: </p>
<pre> mimedefang.pl -features</pre>
<p>prints a list of detected optional Perl modules. The output looks something like this: </p>
<pre> SpamAssassin: yes</pre>
<pre> mimedefang.pl -validate</pre>
<p>calls the function filter_validate, if it is defined in your filter. filter_validate should return an integer; this becomes the exit code. If filter_validate does not exist, an error message is printed and <code>mimedefang.pl</code> exits with an exit code of 1.</p>
<h2>Author</h2>
<p><code>mimedefang.pl</code> was written by Dianne Skoll &lt;dfs [at] roaringpenguin.com&gt;. The <code>mimedefang</code> home page is <i><a rel="nofollow" href="http://www.mimedefang.org/">http://www.mimedefang.org/</a></i>.</p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/8-mimedefang/">mimedefang</a>(8), <a href="/docs/linux/man/5-mimedefang-filter/">mimedefang-filter</a>(5), <a href="/docs/linux/man/7-mimedefang-protocol/">mimedefang-protocol</a>(7) </p>
