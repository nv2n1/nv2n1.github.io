---

title: "podselect(1)"
name: "podselect"
section: "1"
letter: "p"
url: "/docs/linux/man/1-podselect/"
description: "podselect – print selected sections of pod documentation on standard output"
---

<p> podselect &#8211; print selected sections of pod documentation on standard output </p>
<h2>SYNOPSIS</h2>
<p> <code>podselect</code> [<code>-help</code>] [<code>-man</code>] [<code>-section</code> <i>section-spec</i>] [<i>file</i> &#8230;]</p>
<h2>OPTIONS AND ARGUMENTS</h2>
<dl>
<dt><code>-help</code></dt>
<dd> Print a brief help message and exit.</dd>
<dt><code>-man</code></dt>
<dd> Print the manual page and exit.</dd>
<dt><code>-section</code> <i>section-spec</i></dt>
<dd> Specify a section to include in the output. See &#8220;SECTION SPECIFICATIONS&#8221; in Pod::Parser for the format to use for <i>section-spec</i>. This option may be given multiple times on the command line.</dd>
<dt><i>file</i></dt>
<dd> The pathname of a file from which to select sections of pod documentation (defaults to standard input).</dd></dl>
<h2>DESCRIPTION</h2>
<p> <code>podselect</code> will read the given input files looking for pod documentation and will print out (in raw pod format) all sections that match one ore more of the given section specifications. If no section specifications are given than all pod sections encountered are output. </p>
<p> <code>podselect</code> invokes the <code>podselect()</code> function exported by <code>Pod::Select</code> Please see &#8220;<code>podselect()</code>&#8221; in Pod::Select for more details.</p>
<h2>SEE ALSO</h2>
<p> Pod::Parser and Pod::Select</p>
<h2>AUTHOR</h2>
<p> Please report bugs using &lt;<a rel="nofollow" href="http://rt.cpan.org">http://rt.cpan.org</a>&gt;. </p>
<p> Brad Appleton &lt;bradapp [at] enteract.com&gt; </p>
<p> Based on code for <code>Pod::Text::pod2text(1)</code> written by Tom Christiansen &lt;tchrist [at] mox.perl.com&gt; </p>
