---
title: "lintiandeb822parser(3)"
name: "lintiandeb822parser"
section: "3"
letter: "l"
url: "/docs/linux/man/3-lintiandeb822parser/"
description: "Lintian::Deb822Parser – Lintian’s generic Deb822 parser functions"
---

<p>Lintian::Deb822Parser &#8211; Lintian&#8217;s generic Deb822 parser functions </p>
<h2>Synopsis</h2>
<pre> use Lintian::Deb822Parser qw(read_dpkg_control_utf8);
 
 my (@paragraphs);
 eval { @paragraphs = read_dpkg_control_utf8('some/debian/ctrl/file'); };
 if ($@) {
 # syntax error etc.
 die &quot;ctrl/file: $@&quot;;
 }
 
 foreach my $para (@paragraphs) {
 my $value = $para-&gt;{'some-field'};
 if (defined $value) {
 # ...
 }
 }</pre>
<h2>Description</h2>
<p>This module contains a number of utility subs that are nice to have, but on their own did not warrant their own module. </p>
<p> Most subs are imported only on request.</p>
<h3>Debian control parsers</h3>
<p>At first glance, this module appears to contain several debian control parsers. In practise, there is only one real parser (&#8220;visit_dpkg_paragraph&#8221;) &#8211; the rest are convenience functions around it. </p>
<p> If you have very large files (e.g. Packages_amd64), you almost certainly want &#8220;visit_dpkg_paragraph&#8221;. Otherwise, one of the convenience functions are probably what you are looking for.</p>
<dl COMPACT>
<dt>Use &quot;get_deb_info&quot; in Lintian::Util when</p>
<dd>You have a <i>.deb</i> (or <i>.udeb</i>) file and you want the control file from it.</p>
<dt>Use &quot;get_dsc_info&quot; in Lintian::Util when</p>
<dd>You have a <i>.dsc</i> (or <i>.changes</i>) file. Alternative, it is also useful if you have a control file and only care about the first paragraph.</p>
<dt>Use &quot;read_dpkg_control_utf8&quot; or &quot;read_dpkg_control&quot; when</p>
<dd>You have a debian control file (such <i>debian/control</i>) and you want a number of paragraphs from it.</p>
<dt>Use &quot;parse_dpkg_control&quot; when</p>
<dd>When you would have used &#8220;read_dpkg_control_utf8&#8221;, except you have an open filehandle rather than a file name.</dl>
<h2>Constants</h2>
<p>The following constants can be passed to the Debian control file parser functions to alter their parsing flag.</p>
<dl COMPACT>
<dt><font SIZE="-1">DCTRL_DEBCONF_TEMPLATE</font></p>
<dd>The file should be parsed as debconf template. These have slightly syntax rules for whitespace in some cases.</p>
<dt><font SIZE="-1">DCTRL_NO_COMMENTS</font></p>
<dd>The file do not allow comments. With this flag, any comment in the file is considered a syntax error.</dl>
<h2>Functions</h2>
<dl COMPACT>
<dt>parse_dpkg_control(HANDLE[, FLAGS[, <font SIZE="-1">LINES</font>]])</p>
<dd>Reads a debian control file from <font SIZE="-1">HANDLE</font> and returns a list of paragraphs in it. A paragraph is represented via a hashref, which maps (lower cased) field names to their values. </p>
<p> <font SIZE="-1">FLAGS</font> (if given) is a bitmask of the <i>DCTRL_*</i> constants. Please refer to &#8220;<font SIZE="-1">CONSTANTS&#8221;</font> for the list of constants and their meaning. The default value for <font SIZE="-1">FLAGS</font> is 0. </p>
<p> If <font SIZE="-1">LINES</font> is given, it should be a reference to an empty list. On return, <font SIZE="-1">LINES</font> will be populated with a hashref for each paragraph (in the same order as the returned list). Each hashref will also have a special key &quot;<i>START-OF-PARAGRAPH</i>&quot; that gives the line number of the first field in that paragraph. These hashrefs will map the field name of the given paragraph to the line number where the field name appeared. </p>
<p> This is a convenience sub around &#8220;visit_dpkg_paragraph&#8221; and can therefore produce the same errors as it. Please see &#8220;visit_dpkg_paragraph&#8221; for the finer semantics of how the control file is parsed. </p>
<p> <font SIZE="-1">NB:</font> parse_dpkg_control does <i>not</i> close the handle for the caller.</p>
<dt>visit_dpkg_paragraph (<font SIZE="-1">CODE,</font> HANDLE[, <font SIZE="-1">FLAGS</font>])</p>
<dd>Reads a debian control file from <font SIZE="-1">HANDLE</font> and passes each paragraph to <font SIZE="-1">CODE.</font> A paragraph is represented via a hashref, which maps (lower cased) field names to their values. </p>
<p> <font SIZE="-1">FLAGS</font> (if given) is a bitmask of the <i>DCTRL_*</i> constants. Please refer to &#8220;<font SIZE="-1">CONSTANTS&#8221;</font> for the list of constants and their meaning. The default value for <font SIZE="-1">FLAGS</font> is 0. </p>
<p> If the file is empty (i.e. it contains no paragraphs), the method will contain an <i>empty</i> list. The deb822 contents may be inside a <i>signed</i> <font SIZE="-1">PGP</font> message with a signature. </p>
<p> visit_dpkg_paragraph will require the <font SIZE="-1">PGP</font> headers to be correct (if present) and require that the entire file is covered by the signature. However, it will <i>not</i> validate the signature (in fact, the contents of the <font SIZE="-1">PGP SIGNATURE</font> part can be empty). The signature should be validated separately. </p>
<p> visit_dpkg_paragraph will pass paragraphs to <font SIZE="-1">CODE</font> as they are completed. If <font SIZE="-1">CODE</font> can process the paragraphs as they are seen, very large control files can be processed without keeping all the paragraphs in memory. </p>
<p> As a consequence of how the file is parsed, <font SIZE="-1">CODE</font> may be passed a number of (valid) paragraphs before parsing is stopped due to a syntax error. </p>
<p> <font SIZE="-1">NB:</font> visit_dpkg_paragraph does <i>not</i> close the handle for the caller. </p>
<p> <font SIZE="-1">CODE</font> is expected to be a callable reference (e.g. a sub) and will be invoked as the following:</p>
<dl COMPACT>
<dd>
<dl COMPACT>
<dt><font SIZE="-1">CODE-</font>&gt;(<font SIZE="-1">PARA, LINE_NUMBERS</font>)</p>
<dd>The first argument, <font SIZE="-1">PARA,</font> is a hashref to the most recent paragraph parsed. The second argument, <font SIZE="-1">LINE_NUMBERS,</font> is a hashref mapping each of the field names to the line number where the field name appeared. <font SIZE="-1">LINE_NUMBERS</font> will also have a special key &quot;<i>START-OF-PARAGRAPH</i>&quot; that gives the line number of the first field in that paragraph. </p>
<p> The return value of <font SIZE="-1">CODE</font> is ignored. </p>
<p> If the <font SIZE="-1">CODE</font> invokes die (or similar) the error is propagated to the caller.</dl>
</dl>
<dl COMPACT>
<dd><i>On syntax errors</i>, visit_dpkg_paragraph will call die with the following string: </p>
<pre> &quot;syntax error at line %d: %s
&quot;</pre>
<p>Where <tt>%d</tt> is the line number of the issue and <tt>%s</tt> is one of:</p>
<dl COMPACT>
<dt>Duplicate field %s</p>
<dd>The field appeared twice in the paragraph.</p>
<dt>Continuation line outside a paragraph (maybe line %d should be &quot; .&quot;)</p>
<dd>A continuation line appears outside a paragraph &#8211; usually caused by an unintended empty line before it.</p>
<dt>Whitespace line not allowed (possibly missing a &quot;.&quot;)</p>
<dd>An empty continuation line was found. This usually means that a period is missing to denote an &#8220;empty line&#8221; in (e.g.) the long description of a package.</p>
<dt>Cannot parse line &quot;%s&quot;</p>
<dd>Generic error containing the text of the line that confused the parser. Note that all non-printables in <tt>%s</tt> will be replaced by underscores.</p>
<dt>Comments are not allowed</p>
<dd>A comment line appeared and <font SIZE="-1">FLAGS</font> contained <font SIZE="-1">DCTRL_NO_COMMENTS.</font></p>
<dt><font SIZE="-1">PGP</font> signature seen before start of signed message</p>
<dd>A &#8220;<font SIZE="-1">BEGIN PGP SIGNATURE&#8221;</font> header is seen and a &#8220;<font SIZE="-1">BEGIN PGP MESSAGE&#8221;</font> has not been seen yet.</p>
<dt>Two <font SIZE="-1">PGP</font> signatures (first one at line %d)</p>
<dd>Two &#8220;<font SIZE="-1">BEGIN PGP SIGNATURE&#8221;</font> headers are seen in the same file.</p>
<dt>Unexpected %s header</p>
<dd>A valid <font SIZE="-1">PGP</font> header appears (e.g. &#8220;<font SIZE="-1">BEGIN PUBLIC KEY BLOCK&#8221;</font>).</p>
<dt>Malformed <font SIZE="-1">PGP</font> header</p>
<dd>An invalid or malformed <font SIZE="-1">PGP</font> header appears.</p>
<dt>Expected at most one signed message (previous at line %d)</p>
<dd>Two &#8220;<font SIZE="-1">BEGIN PGP MESSAGE&#8221;</font> headers appears in the same message.</p>
<dt>End of file but expected an &quot;<font SIZE="-1">END PGP SIGNATURE&quot;</font> header</p>
<dd>The file ended after a &#8220;<font SIZE="-1">BEGIN PGP SIGNATURE&#8221;</font> header without being followed by an &#8220;<font SIZE="-1">END PGP SIGNATURE&#8221;.</font></p>
<dt><font SIZE="-1">PGP MESSAGE</font> header must be first content if present</p>
<dd>The file had content before <font SIZE="-1">PGP MESSAGE.</font></p>
<dt>Data after the <font SIZE="-1">PGP SIGNATURE</font></p>
<dd>The file had data after the <font SIZE="-1">PGP SIGNATURE</font> block ended.</p>
<dt>End of file before &quot;<font SIZE="-1">BEGIN PGP SIGNATURE&quot;</font></p>
<dd>The file had a &#8220;<font SIZE="-1">BEGIN PGP MESSAGE&#8221;</font> header, but no signature was present.</dl>
</dl>
<dl COMPACT>
<dd></dl>
<dt>rstrip</p>
<dd>
<dt>read_dpkg_control_utf8(FILE[, FLAGS[, <font SIZE="-1">LINES</font>]])</p>
<dd>
<dt>read_dpkg_control(FILE[, FLAGS[, <font SIZE="-1">LINES</font>]])</p>
<dd>This is a convenience function to ease using &#8220;parse_dpkg_control&#8221; with paths to files (rather than open handles). The first argument must be the path to a <font SIZE="-1">FILE,</font> which should be read as a debian control file. If the file is empty, an empty list is returned. </p>
<p> Otherwise, this behaves like: </p>
<pre> use autodie;
 
 open(my $fd, '&lt;:encoding(UTF-8)', FILE); # or '&lt;'
 my @p = parse_dpkg_control($fd, FLAGS, LINES);
 close($fd);
 return @p;</pre>
<p>This goes without saying that may fail with any of the messages that &#8220;parse_dpkg_control(HANDLE[, FLAGS[, <font SIZE="-1">LINES</font>]])&#8221; do. It can also emit autodie exceptions if open or close fails.</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-lintian/">lintian</a></code>(1)</p>
