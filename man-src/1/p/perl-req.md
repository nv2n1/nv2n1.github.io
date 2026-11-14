---
title: "perl-req(1)"
name: "perl-req"
section: "1"
letter: "p"
url: "/docs/linux/man/1-perl-req/"
description: "perl.req – list requirements for Perl scripts and libraries"
---

<p>perl.req &#8211; list requirements for Perl scripts and libraries </p>
<h2>Synopsis</h2>
<p><code>perl.req</code> [<code>-h</code>|<code>&#8211;help</code>] [<code>-v</code>|<code>&#8211;verbose</code>] [<code>-m</code>|<code>&#8211;method</code>=<i>strict</i>|<i>normal</i>|<i>relaxed</i>] [<i></i><font SIZE="-1"><i>FILE</i></font><i></i>&#8230;]</p>
<h2>Description</h2>
<p><code>perl.req</code> calculates prerequisites for each Perl source <i>file</i> specified on a command line; alternatively, a list of files is obtained from standard input, one file per line. <tt>&quot;use&quot;</tt>, <tt>&quot;require&quot;</tt> and <tt>&quot;do&quot;</tt> statements are processed. The output of perl.req is suitable for automatic dependency tracking (e.g. for <font SIZE="-1">RPM</font> packaging). </p>
<p> For example, <i>/usr/lib/perl5/File/Temp.pm</i> requires, in particular, <tt>&quot;perl(Fcntl.pm) &gt;= 1.030&quot;</tt> (as of perl-5.8.6). </p>
<p> <code>perl.req</code> is basically a wrapper for B::PerlReq Perl compiler backend.</p>
<h2>Options</h2>
<dl COMPACT>
<dt><code>-m</code>, <code>&#8211;method</code>=<i>method</i></p>
<dd>Use particular <i>method</i> for dependency tracking. Alternatively, <font SIZE="-1">RPM_PERL_REQ_METHOD</font> environement variable can be used to set the method. </p>
<p> The following methods are available:</p>
<dl COMPACT>
<dd>
<dl COMPACT>
<dt><code>strict</code></p>
<dd>Search thoroughly and list all requirements. In particular, list platform-specific (non-UNIX) requirements and requirements found inside <tt>&quot;eval&quot;</tt> blocks.</p>
<dt><code>normal</code> (default)</p>
<dd>Enable moderate search most acceptable for <font SIZE="-1">RPM</font> packaging. That is, skip files known to be platform-specific; skip platform-specific requirements and those found inside <tt>&quot;eval&quot;</tt> blocks; skip most common requirements (e.g. <tt>&quot;strict.pm&quot;</tt>).</p>
<dt><code>relaxed</code></p>
<dd>Enable relaxed mode. That is, tolerate B::PerlReq failures; in addition to normal method, skip conditional requirements (e.g. <tt>&quot;require&quot;</tt> statements inside subroutines); skip <tt>&quot;do FILE&quot;</tt> statements; list only essential dependencies.</dl>
</dl>
<dl COMPACT>
<dd></dl>
<dt><code>-v</code>, <code>&#8211;verbose</code></p>
<dd>Increase verbosity.</dl>
<h2>Author</h2>
<p>Written by Alexey Tourbin &lt;at [at] altlinux.org&gt;, based on an earlier version by Ken Estes &lt;kestes [at] staff.mail.com&gt;, with contributions from Mikhail Zabaluev &lt;mhz [at] altlinux.org&gt;.</p>
<h2>History</h2>
<p>Initial version of perl.req (part of <font SIZE="-1">RPM 3.0</font>) done by Ken Estes in 1999. Regular expressions were used to extract dependencies. (Later a part of <font SIZE="-1">ALT</font> Linux Master 2.0, with modifications from Mikhail Zabaluev.) </p>
<p> Reworked in November 2002: complicated regular expressions were added to enhance search; methods added. (Later a part of <font SIZE="-1">ALT</font> Linux Master 2.2.) </p>
<p> Reworked in September 2003: B::Deparse was utilized to re-format Perl code before dependency extraction; hence more simple and accurate. Decoupled from rpm-build package into rpm-build-perl. (Later a part of <font SIZE="-1">ALT</font> Linux Master 2.4.) </p>
<p> Reworked in December 2004: B::PerlReq was developed. Released on <font SIZE="-1">CPAN,</font> see &lt;<a rel="nofollow" href="http://search.cpan.org/dist/rpm-build-perl/">http://search.cpan.org/dist/rpm-build-perl/</a>&gt;.</p>
<h2>Copying</h2>
<p>Copyright (c) 2003, 2004 Alexey Tourbin, <font SIZE="-1">ALT</font> Linux Team. </p>
<p> This is free software; you can redistribute it and/or modify it under the terms of the <font SIZE="-1">GNU</font> Library General Public License as published by the Free Software Foundation; either version 2 of the License, or (at your option) any later version.</p>
<h2>See Also</h2>
<p>B::PerlReq, perl.prov</p>
