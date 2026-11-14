---
title: "podselect(1)"
name: "podselect"
section: "1"
letter: "p"
url: "/docs/linux/man/1-podselect/"
description: "podselect – print selected sections of pod documentation on standard output"
---

<h2 class="name">NAME</h2>
<p> podselect &#8211; print selected sections of pod documentation on standard output </p>
<h2>SYNOPSIS</h2>
<p> <code>podselect</code> [<code>-help</code>] [<code>-man</code>] [<code>-section</code> <i>section-spec</i>] [<i>file</i> &#8230;]</p>
<h2>OPTIONS AND ARGUMENTS</h2>
<dl>
<dt><code>-help</code></p>
<dd> Print a brief help message and exit.</p>
<dt><code>-man</code></p>
<dd> Print the manual page and exit.</p>
<dt><code>-section</code> <i>section-spec</i></p>
<dd> Specify a section to include in the output. See &#8220;<font SIZE="-1">SECTION SPECIFICATIONS&#8221;</font> in Pod::Parser for the format to use for <i>section-spec</i>. This option may be given multiple times on the command line.</p>
<dt><i>file</i></p>
<dd> The pathname of a file from which to select sections of pod documentation (defaults to standard input).</dl>
<h2>DESCRIPTION</h2>
<p> <code>podselect</code> will read the given input files looking for pod documentation and will print out (in raw pod format) all sections that match one ore more of the given section specifications. If no section specifications are given than all pod sections encountered are output. </p>
<p> <code>podselect</code> invokes the <code>podselect()</code> function exported by <code>Pod::Select</code> Please see &#8220;<code>podselect()</code>&#8221; in Pod::Select for more details.</p>
<h2>SEE ALSO</h2>
<p> Pod::Parser and Pod::Select</p>
<h2>AUTHOR</h2>
<p> Please report bugs using &lt;<a rel="nofollow" href="http://rt.cpan.org">http://rt.cpan.org</a>&gt;. </p>
<p> Brad Appleton &lt;bradapp [at] enteract.com&gt; </p>
<p> Based on code for <code><a href="/docs/linux/man/1-pod--text--pod2text/">Pod::Text::pod2text</a>(1)</code> written by Tom Christiansen &lt;tchrist [at] mox.perl.com&gt; </p>
<h2>Index</h2>
