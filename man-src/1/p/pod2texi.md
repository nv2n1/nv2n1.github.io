---
title: "pod2texi(1)"
name: "pod2texi"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pod2texi/"
description: "pod2texi – convert Pod to Texinfo"
---

<h2 class="name">NAME</h2>
<p> pod2texi &#8211; convert Pod to Texinfo </p>
<h2>SYNOPSIS</h2>
<pre>
  pod2texi [OPTION]... POD...
</pre>
<h2>DESCRIPTION</h2>
<p> Translate Pod file(s) to Texinfo. There are two basic modes of operation. First, by default, each pod is translated to a standalone Texinfo manual. </p>
<p> Second, if <tt>&quot;--base-level&quot;</tt> is set higher than 0, each pod is translated to a file suitable for <tt>@include</tt>, and one more file with all the <tt>@include</tt>s is generated, intended to be <tt>@include</tt>d in turn within a hand-written top-level file.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>&#8211;appendix-sections</code></p>
<dd> Use appendix sectioning commands (<tt>@appendix</tt>, &#8230;) instead of the default numbered sectioning Texinfo @-commands (<tt>@chapter</tt>, <tt>@section</tt>, &#8230;).</p>
<dt><code>&#8211;base-level</code>=<i>NUM|NAME</i></p>
<dd> Sets the level of the <tt>&quot;head1&quot;</tt> commands. It may be an integer or a Texinfo sectioning command (without the <tt>&quot;@&quot;</tt>): 1 corresponds to the <tt>@chapter</tt>/<tt>@unnumbered</tt> level, 2 to the <tt>@section</tt> level, and so on. The default is 0, meaning that <tt>&quot;head1&quot;</tt> commands are still output as chapters, but the output is arranged as a standalone manual. </p>
<p> If the level is not 0, the pod file is rendered as a fragment of a Texinfo manual suitable for <tt>@include</tt>. In this case, each pod file has an additional sectioning command covering the entire file, one level above the <tt>&quot;--base-level&quot;</tt> value. Therefore, to make each pod file a chapter in a large manual, you should use <tt>&quot;section&quot;</tt> as the base level. </p>
<p> For an example of making Texinfo out of the Perl documentation itself, see <tt>&quot;contrib/perldoc-all&quot;</tt> in the Texinfo source distribution, with output available at &lt;<a rel="nofollow" href="http://www.gnu.org/software/perl/manual">http://www.gnu.org/software/perl/manual</a>&gt;.</p>
<dt><code>&#8211;debug</code>=<i></i><font SIZE="-1"><i>NUM</i></font><i></i></p>
<dd> Set debugging level to <i></i><font SIZE="-1"><i>NUM</i></font><i></i>.</p>
<dt><code>&#8211;help</code></p>
<dd> Display help and exit.</p>
<dt><code>&#8211;output</code>=<i></i><font SIZE="-1"><i>NAME</i></font><i></i></p>
<dd> Name for the first manual, or the main manual if there is a main manual. Default is to write to standard output.</p>
<dt><code>&#8211;no-section-nodes</code></p>
<dd> Use anchors for sections instead of nodes.</p>
<dt><code>&#8211;no-fill-section-gaps</code></p>
<dd> Do not fill sectioning gaps with empty <tt>@unnumbered</tt> files. Ordinarily, it&#8217;s good to keep the sectioning hierarchy intact.</p>
<dt><code>&#8211;preamble</code>=<i></i><font SIZE="-1"><i>STR</i></font><i></i></p>
<dd> Insert <i></i><font SIZE="-1"><i>STR</i></font><i></i> as top boilerplate before includes. The default is a minimal beginning for a Texinfo document, and sets <tt>@documentencoding</tt> to <tt>&quot;utf-8&quot;</tt> (because the output is written that way).</p>
<dt><code>&#8211;subdir</code>=<i></i><font SIZE="-1"><i>NAME</i></font><i></i></p>
<dd> If there is a main manual with include files (each corresponding to an input pod file), then those include files are put in directory <i></i><font SIZE="-1"><i>NAME</i></font><i></i>.</p>
<dt><code>&#8211;unnumbered-sections</code></p>
<dd> Use unnumbered sectioning commands (<tt>@unnumbered</tt>, &#8230;) instead of the default numbered sectioning Texinfo @-commands (<tt>@chapter</tt>, <tt>@section</tt>, &#8230;).</p>
<dt><code>&#8211;top</code>=<i></i><font SIZE="-1"><i>TOP</i></font><i></i></p>
<dd> Name of the <tt>@top</tt> element for the main manual. May contain Texinfo code.</p>
<dt><code>&#8211;version</code></p>
<dd> Display version information and exit.</dl>
<h2>SEE ALSO</h2>
<p> Pod::Simple::Texinfo. perlpod. The Texinfo manual. Texinfo home page: &lt;<a rel="nofollow" href="http://www.gnu.org/software/texinfo/">http://www.gnu.org/software/texinfo/</a>&gt;</p>
<h2>COPYRIGHT</h2>
<p> Copyright 2021 Free Software Foundation, Inc. </p>
<p> This program is free software; you can redistribute it and/or modify it under the terms of the <font SIZE="-1">GNU</font> General Public License as published by the Free Software Foundation; either version 3 of the License, or (at your option) any later version. </p>
<p> There is <font SIZE="-1">NO WARRANTY,</font> to the extent permitted by law.</p>
<h2>AUTHOR</h2>
<p> Patrice Dumas &lt;bug-texinfo [at] gnu.org&gt;. </p>
<h2>Index</h2>
