---
title: "dosepsbin(1)"
name: "dosepsbin"
section: "1"
letter: "d"
url: "/docs/linux/man/1-dosepsbin/"
description: "dosepsbin — Extract PS/WMF/TIFF sections from DOS EPS binary files"
---

<h2 class="name">NAME</h2>
<p> dosepsbin &#8212; Extract PS/WMF/TIFF sections from DOS EPS binary files </p>
<h2>VERSION</h2>
<p> 2012-03-22 v1.2</p>
<h2>SYNOPSIS</h2>
<p> The progam <code>dosepsbin</code> analyses an <font SIZE="-1">EPS</font> file that is not a plain <font SIZE="-1">ASCII</font> PostScript file but given as <font SIZE="-1">DOS</font> <font SIZE="-1">EPS</font> binary file. </p>
<pre>
    dosepsbin [options] &lt;input file&gt;
</pre>
<p> First it analyzes the <i>input file</i>, validates its header and summarizes the available sections. Depending on the given options, the sections are then written to files. </p>
<p> Options: </p>
<pre><code>
--eps - file&lt;file&gt; Write PS section to&lt;file&gt;.--wmf - file&lt;file&gt; Write WMF section to&lt;file&gt;.--tiff - file&lt;file&gt; Write TIFF section to&lt;file&gt;.--inputfile&lt;file&gt; The name of the input file.--verbose Verbose output.--quiet Only errors and warnings are printed.--help Brief help message.--man Full documentation.--version Print version identification.
</code></pre>
<p> The files for output must be different from the input file.</p>
<h2>DESCRIPTION</h2>
<p> <code><font SIZE="-1">DOS</font> <font SIZE="-1">EPS</font> Binary File Format</code> </p>
<p> A Encapsulated PostScript (<font SIZE="-1">EPS</font>) file can also given in a special binary format to support the inclusion of a thumbnail. The file format starts with a binary header that contains the positions of the possible sections:</p>
<dl>
<dt>* Postscript (<font SIZE="-1">PS</font>)</p>
<dd>
<dt>* Windows Metafile Format (<font SIZE="-1">WMF</font>)</p>
<dd>
<dt>* Tag Image File Format (<font SIZE="-1">TIFF</font>)</p>
<dd></dl>
<p> The <font SIZE="-1">PS</font> section must be present and either the <font SIZE="-1">WMF</font> file or the <font SIZE="-1">TIFF</font> file should be given.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>&#8211;</code><code>-eps-file</code>=&lt;<i>file</i>&gt;</p>
<dd> The <font SIZE="-1">PS</font> section is written to &lt;<i>file</i>&gt;. The output file must be different from the input file.</p>
<dt><code>&#8211;</code><code>-wmf-file</code>=&lt;<i>file</i>&gt;</p>
<dd> The <font SIZE="-1">WMF</font> section is written to &lt;<i>file</i>&gt; if present. The output file must be different from the input file.</p>
<dt><code>&#8211;</code><code>-tiff-file</code>=&lt;<i>file</i>&gt;</p>
<dd> The <font SIZE="-1">TIFF</font> section is written to &lt;<i>file</i>&gt; if present. The output file must be different from the input file.</p>
<dt><code>&#8211;</code><code>-inputfile</code>=&lt;<i>file</i>&gt;</p>
<dd> The input file can also be given directly on the command line. If the file does not exist, then the file with extension `.eps&#8217; is tried.</p>
<dt><code>&#8211;</code><code>-verbose</code></p>
<dd> Verbose messages.</p>
<dt><code>&#8211;</code><code>-quiet</code></p>
<dd> No messages are printed except for errors and warnings.</p>
<dt><code>&#8211;</code><code>-help</code></p>
<dd> Display help screen.</p>
<dt><code>&#8211;</code><code>-man</code></p>
<dd> Prints manual page.</p>
<dt><code>&#8211;</code><code>-version</code></p>
<dd> Print version identification and exit.</dl>
<h2>EXAMPLES</h2>
<p> The following command extracts the <font SIZE="-1">PS</font> section from file <i>test.eps</i> and stores the result in file <i>test-ps.eps</i>: </p>
<pre>
    dosepsbin --eps-file test-ps.eps test.eps
</pre>
<h2>AUTHOR</h2>
<p> Heiko Oberdiek, email: heiko.oberdiek at googlemail.com</p>
<h2>COPYRIGHT AND LICENSE</h2>
<p> Copyright 2011-2012 by Heiko Oberdiek. </p>
<p> This library is free software; you may redistribute it and/or modify it under the same terms as Perl itself (Perl Artistic License/GNU General Public License, version 2).</p>
<h2>SEE ALSO</h2>
<p> The <font SIZE="-1">DOS</font> <font SIZE="-1">EPS</font> binary file format is described in section &#8220;5.2 Windows Metafile or <font SIZE="-1">TIFF</font>&#8221;: </p>
<pre>
    Adobe Developer Support,
    Encapsulated PostScript File Format Specification,
    Version 3.0,
    1992-05-01,
    <a rel="nofollow" href="http://partners.adobe.com/public/developer/en/ps/5002.EPSF_Spec.pdf">http://partners.adobe.com/public/developer/en/ps/5002.EPSF_Spec.pdf</a>
</pre>
<h2>HISTORY</h2>
<dl>
<dt><code>2011/11/10 v1.0</code></p>
<dd>
<dl>
<dt>
<dd>
<dl>
<dt>* First version.</p>
<dd></dl>
</dl>
<dl>
<dt>
<dd></dl>
<dt><code>2011/12/05 v1.1</code></p>
<dd>
<dl>
<dt>
<dd>
<dl>
<dt>* Typo fixed in help text (thanks Peter Breitenlohner).</p>
<dd></dl>
</dl>
<dl>
<dt>
<dd></dl>
<dt><code>2012/03/22 v1.2</code></p>
<dd>
<dl>
<dt>
<dd>
<dl>
<dt>* Fix in validation test for offset of <font SIZE="-1">PS</font> section.</p>
<dd></dl>
</dl>
<dl>
<dt>
<dd></dl>
</dl>
<h2>Index</h2>
