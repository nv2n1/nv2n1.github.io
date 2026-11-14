---
title: "perl585delta(1)"
name: "perl585delta"
section: "1"
letter: "p"
url: "/docs/linux/man/1-perl585delta/"
description: "perl585delta – what is new for perl v5.8.5"
---

<h2 class="name">NAME</h2>
<p> perl585delta &#8211; what is new for perl v5.8.5 </p>
<h2>DESCRIPTION</h2>
<p> This document describes differences between the 5.8.4 release and the 5.8.5 release.</p>
<h2>Incompatible Changes</h2>
<p> There are no changes incompatible with 5.8.4.</p>
<h2>Core Enhancements</h2>
<p> Perl&#8217;s regular expression engine now contains support for matching on the intersection of two Unicode character classes. You can also now refer to user-defined character classes from within other user defined character classes.</p>
<h2>Modules and Pragmata</h2>
<dl>
<dt>&bull;</p>
<dd> Carp improved to work nicely with Safe. Carp&#8217;s message reporting should now be anomaly free &#8211; it will always print out line number information.</p>
<dt>&bull;</p>
<dd> <font SIZE="-1">CGI</font> upgraded to version 3.05</p>
<dt>&bull;</p>
<dd> charnames now avoids clobbering <tt>$_</tt></p>
<dt>&bull;</p>
<dd> Digest upgraded to version 1.08</p>
<dt>&bull;</p>
<dd> Encode upgraded to version 2.01</p>
<dt>&bull;</p>
<dd> FileCache upgraded to version 1.04</p>
<dt>&bull;</p>
<dd> libnet upgraded to version 1.19</p>
<dt>&bull;</p>
<dd> Pod::Parser upgraded to version 1.28</p>
<dt>&bull;</p>
<dd> Pod::Perldoc upgraded to version 3.13</p>
<dt>&bull;</p>
<dd> Pod::LaTeX upgraded to version 0.57</p>
<dt>&bull;</p>
<dd> Safe now works properly with Carp</p>
<dt>&bull;</p>
<dd> Scalar-List-Utils upgraded to version 1.14</p>
<dt>&bull;</p>
<dd> Shell&#8217;s documentation has been re-written, and its historical partial auto-quoting of command arguments can now be disabled.</p>
<dt>&bull;</p>
<dd> Test upgraded to version 1.25</p>
<dt>&bull;</p>
<dd> Test::Harness upgraded to version 2.42</p>
<dt>&bull;</p>
<dd> Time::Local upgraded to version 1.10</p>
<dt>&bull;</p>
<dd> Unicode::Collate upgraded to version 0.40</p>
<dt>&bull;</p>
<dd> Unicode::Normalize upgraded to version 0.30</dl>
<h2>Utility Changes</h2>
<h3>Perl&#8217;s debugger</h3>
<p> The debugger can now emulate stepping backwards, by restarting and rerunning all bar the last command from a saved command history.</p>
<h3>h2ph</h3>
<p> <i>h2ph</i> is now able to understand a very limited set of C inline functions &#8212; basically, the inline functions that look like <font SIZE="-1">CPP</font> macros. This has been introduced to deal with some of the headers of the newest versions of the glibc. The standard warning still applies; to quote <i>h2ph</i>&#8216;s documentation, <i>you may need to dicker with the files produced</i>.</p>
<h2>Installation and Configuration Improvements</h2>
<p> Perl 5.8.5 should build cleanly from source on LynxOS.</p>
<h2>Selected Bug Fixes</h2>
<dl>
<dt>&bull;</p>
<dd> The in-place sort optimisation introduced in 5.8.4 had a bug. For example, in code such as </p>
<pre>
    @a = sort ($b, @a)
</pre>
<p> the result would omit the value <tt>$b</tt>. This is now fixed.</p>
<dt>&bull;</p>
<dd> The optimisation for unnecessary assignments introduced in 5.8.4 could give spurious warnings. This has been fixed.</p>
<dt>&bull;</p>
<dd> Perl should now correctly detect and read BOM-marked and (BOMless) <font SIZE="-1">UTF-16</font> scripts of either endianness.</p>
<dt>&bull;</p>
<dd> Creating a new thread when weak references exist was buggy, and would often cause warnings at interpreter destruction time. The known bug is now fixed.</p>
<dt>&bull;</p>
<dd> Several obscure bugs involving manipulating Unicode strings with <tt>&quot;substr&quot;</tt> have been fixed.</p>
<dt>&bull;</p>
<dd> Previously if Perl&#8217;s file globbing function encountered a directory that it did not have permission to open it would return immediately, leading to unexpected truncation of the list of results. This has been fixed, to be consistent with Unix shells&#8217; globbing behaviour.</p>
<dt>&bull;</p>
<dd> Thread creation time could vary wildly between identical runs. This was caused by a poor hashing algorithm in the thread cloning routines, which has now been fixed.</p>
<dt>&bull;</p>
<dd> The internals of the ithreads implementation were not checking if OS-level thread creation had failed. threads-&gt;<code>create()</code> now returns <tt>&quot;undef&quot;</tt> in if thread creation fails instead of crashing perl.</dl>
<h2>New or Changed Diagnostics</h2>
<dl>
<dt>&bull;</p>
<dd> Perl -V has several improvements</p>
<dl>
<dt>
<dd>
<dl>
<dt>&bull;</p>
<dd> correctly outputs local patch names that contain embedded code snippets or other characters that used to confuse it.</p>
<dt>&bull;</p>
<dd> arguments to -V that look like regexps will give multiple lines of output.</p>
<dt>&bull;</p>
<dd> a trailing colon suppresses the linefeed and &#8216;;&#8217; terminator, allowing embedding of queries into shell commands.</p>
<dt>&bull;</p>
<dd> a leading colon removes the &#8216;name=&#8217; part of the response, allowing mapping to any name.</dl>
</dl>
<dl>
<dt>
<dd></dl>
<dt>&bull;</p>
<dd> When perl fails to find the specified script, it now outputs a second line suggesting that the user use the <tt>&quot;-S&quot;</tt> flag: </p>
<pre>
    $ perl5.8.5 missing.pl
    Can't open perl script &quot;missing.pl&quot;: No such file or directory.
    Use -S to search $PATH for it.
</pre>
</dl>
<h2>Changed Internals</h2>
<p> The Unicode character class files used by the regular expression engine are now built at build time from the supplied Unicode consortium data files, instead of being shipped prebuilt. This makes the compressed Perl source tarball about 200K smaller. A side effect is that the layout of files inside lib/unicore has changed.</p>
<h2>Known Problems</h2>
<p> The regression test <i>t/uni/class.t</i> is now performing considerably more tests, and can take several minutes to run even on a fast machine.</p>
<h2>Platform Specific Problems</h2>
<p> This release is known not to build on Windows 95.</p>
<h2>Reporting Bugs</h2>
<p> If you find what you think is a bug, you might check the articles recently posted to the comp.lang.perl.misc newsgroup and the perl bug database at <a rel="nofollow" href="http://bugs.perl.org.">http://bugs.perl.org.</a> There may also be information at <a rel="nofollow" href="http://www.perl.org,">http://www.perl.org,</a> the Perl Home Page. </p>
<p> If you believe you have an unreported bug, please run the <code>perlbug</code> program included with your release. Be sure to trim your bug down to a tiny but sufficient test case. Your bug report, along with the output of <tt>&quot;perl -V&quot;</tt>, will be sent off to perlbug [at] perl.org to be analysed by the Perl porting team. You can browse and search the Perl 5 bugs at <a rel="nofollow" href="http://bugs.perl.org/">http://bugs.perl.org/</a></p>
<h2>SEE ALSO</h2>
<p> The <i>Changes</i> file for exhaustive details on what changed. </p>
<p> The <i></i><font SIZE="-1"><i>INSTALL</i></font><i></i> file for how to build Perl. </p>
<p> The <i></i><font SIZE="-1"><i>README</i></font><i></i> file for general stuff. </p>
<p> The <i>Artistic</i> and <i>Copying</i> files for copyright information. </p>
<h2>Index</h2>
