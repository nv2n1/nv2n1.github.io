---
title: "scanspool(8)"
name: "scanspool"
section: "8"
letter: "s"
url: "/docs/linux/man/8-scanspool/"
description: "scanspool – Perform a sanity scan over all articles in news spool"
---

<p>scanspool &#8211; Perform a sanity scan over all articles in news spool</p>
<h2>Synopsis</h2>
<p><code>scanspool</code> [<code>-cnv</code>] [<code>-a</code> <i>active-file</i>] [<code>-s</code> <i>spool-dir</i>]</p>
<h2>Description</h2>
<p><code>scanspool</code> is a Perl script for use with a <i>tradspool</i> article spool. It will scan the <i>active</i> file as well as all articles in the spool and report on the errors it encounters. As this may take a while, using the <code>-v</code> switch is recommended to see how far the program has progressed. </p>
<p> First, <code>scanspool</code> scans the <i>active</i> file, noting problems such as:</p>
<dl>
<dt>&bull;</p>
<dd>malformed lines;</p>
<dt>&bull;</p>
<dd>newsgroups aliased to a non-existent newsgroup;</p>
<dt>&bull;</p>
<dd>newsgroups aliased to a newsgroup that is also aliased.</dl>
<p> Then it will examine all articles under your news spool directory, complaining about articles that:</p>
<dl>
<dt>&bull;</p>
<dd>have a basename that starts with a leading 0;</p>
<dt>&bull;</p>
<dd>have a basename that is out of range according to the <i>active</i> file;</p>
<dt>&bull;</p>
<dd>do not contain a Newsgroups: header line;</p>
<dt>&bull;</p>
<dd>are all header and no text;</p>
<dt>&bull;</p>
<dd>are in a directory for which there is no newsgroup in the <i>active</i> file;</p>
<dt>&bull;</p>
<dd>are in a newsgroup to which they do not belong.</dl>
<p> <code>scanspool</code> understands aliased newsgroups. Thus, if an article is posted to foo.old.name that is aliased to foo.bar, it will be expected to be found under foo.bar and not foo.old.name. </p>
<p> Articles posted to a newsgroup of status <tt>&quot;j&quot;</tt> or <tt>&quot;x&quot;</tt> (the fourth field of the <i>active</i> file) will be expected to show up under the <i>junk</i> group. </p>
<p> <code>scanspool</code> assumes that the path of a valid newsgroup&#8217;s directory from the root of the spool tree will not contain any <tt>&quot;.&quot;</tt> character. Thus, directories such as <i>out.going</i>, <i>tmp.dir</i>, <i>in.coming</i> and <i>news.archive</i> will not be searched. This program also assumes that article basenames contain only decimal digits. Last, files under the top level directory <i>lost+found</i> are not scanned.</p>
<h2>Options</h2>
<dl>
<dt><code>-a</code> <i>active-file</i></p>
<dd>The <i>active</i> file to use; <i>pathdb</i>/active is the default.</p>
<dt><code>-c</code></p>
<dd>Only check article filenames. <code>scanspool</code> will therefore not actually scan the Newsgroups: header field of the articles.</p>
<dt><code>-n</code></p>
<dd>Don&#8217;t throttle <code>innd</code> while scanning.</p>
<dt><code>-s</code> <i>spool-dir</i></p>
<dd>The root of the spool tree; <i>patharticles</i> is the default.</p>
<dt><code>-v</code></p>
<dd>Setting this flag enables a verbose mode. <code>scanspool</code> will then print which newsgroup is currently worked upon. It will list all the articles found in non-<i>active</i> directories (that is to say articles sorted into groups no longer present in the <i>active</i> file), rather than just printing the group once.</dl>
<h2>Diagnostics</h2>
<p>The output of <code>scanspool</code> will start with one of the following forms:</p>
<dl>
<dt>&quot;FATAL:&quot; (to stderr)</p>
<dd>Fatal or internal error.</p>
<dt>&quot;WARN:&quot; (to stderr)</p>
<dd><i>active</i> or article format problem, newsgroup alias problem, <i><a href="/docs/linux/man/1-find/">find</a></i>(1) error, article open error.</p>
<dt>&quot;path/123:&quot; (to stdout)</p>
<dd>Issues such as:</p>
<dl>
<dd>
<dl>
<dt>&bull;</p>
<dd>basename starts with 0;</p>
<dt>&bull;</p>
<dd>article number out of range;</p>
<dt>&bull;</p>
<dd>article in the wrong directory;</p>
<dt>&bull;</p>
<dd>article in a directory not related to an <i>active</i> non-aliased newsgroup.</dl>
</dl>
<dl>
<dd></dl>
<dt>&quot;	 &#8230;&quot; (to stdout)</p>
<dd>Verbose messages start with a tab.</dl>
<h2>Bugs</h2>
<p><code>scanspool</code> is unable to detect and properly deal with spool formats other than tradspool. However, if the files that store your articles are named other than just all-digits, they will simply be skipped (and your <i>active</i> is still checked). </p>
<p> <code>scanspool</code> only considers the first line of the Newsgroups: header field. Continuation lines are not taken into account.</p>
<h2>History</h2>
<p><code>scanspool</code> was written by Landon Curt Noll (chongo was here /\../\). </p>
<p> This manual page was written by Florian Schlichting, largely based on comments in the script. </p>
<p> <tt>$Id:</tt> scanspool.pod 9302 2011-08-04 21:10:17Z iulius $</p>
<h2>See Also</h2>
<p><i><a href="/docs/linux/man/5-active/">active</a></i>(5). </p>
