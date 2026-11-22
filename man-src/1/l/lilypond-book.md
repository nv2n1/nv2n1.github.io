---

title: "lilypond-book(1)"
name: "lilypond-book"
section: "1"
letter: "l"
url: "/docs/linux/man/1-lilypond-book/"
description: "lilypond-book – manual page for lilypond-book 2.12.2"
---

<p> lilypond-book &#8211; manual page for lilypond-book 2.12.2</p>
<h2>SYNOPSIS</h2>
<p> <code>lilypond-book</code> [<i>OPTION</i>]&#8230; <i>FILE</i></p>
<h2>DESCRIPTION</h2>
<p> Process LilyPond snippets in hybrid HTML, LaTeX, texinfo or DocBook document.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-F</code>, <code>&#8211;filter</code>=<i>FILTER</i></dt>
<dd> pipe snippets through FILTER [default: `convert-ly <code>-n</code> -&#8216;]</dd>
<dt><code>-f</code>, <code>&#8211;format</code>=<i>FORMAT</i></dt>
<dd> use output format FORMAT (texi [default], texi-html, latex, html, docbook)</dd>
<dt><code>-h</code>, <code>&#8211;help</code></dt>
<dd> show this help and exit</dd>
<dt><code>-I</code>, <code>&#8211;include</code>=<i>DIR</i></dt>
<dd> add DIR to include path</dd>
<dt><code>&#8211;info-images-dir</code>=<i>DIR</i></dt>
<dd> format Texinfo output so that Info will look for images of music in DIR</dd>
<dt><code>&#8211;latex-program</code>=<i>PROG</i></dt>
<dd> run executable PROG instead of latex</dd>
<dt><code>&#8211;left-padding</code>=<i>PAD</i></dt>
<dd> pad left side of music to align music inspite of uneven bar numbers (in mm)</dd>
<dt><code>-o</code>, <code>&#8211;output</code>=<i>DIR</i></dt>
<dd> write output to DIR</dd>
<dt><code>&#8211;skip-lily-check</code></dt>
<dd> do not fail if no lilypond output is found</dd>
<dt><code>&#8211;skip-png-check</code></dt>
<dd> do not fail if no PNG images are found for EPS files</dd>
<dt><code>&#8211;lily-output-dir</code>=<i>DIR</i></dt>
<dd> write lily-XXX files to DIR, link into <code>&#8211;output</code> dir</dd>
<dt><code>-P</code>, <code>&#8211;process</code>=<i>COMMAND</i></dt>
<dd> process ly_files using COMMAND FILE&#8230;</dd>
<dt><code>&#8211;pdf</code></dt>
<dd> create PDF files for use with PDFTeX</dd>
<dt><code>-V</code>, <code>&#8211;verbose</code></dt>
<dd> be verbose</dd>
<dt><code>&#8211;version</code></dt>
<dd> show version number and exit</dd>
<dt><code>-w</code>, <code>&#8211;warranty</code></dt>
<dd> show warranty and copyright</dd></dl>
<h2>EXAMPLES</h2>
<dl>
<dt>
</dt><dd> <tt>$ lilypond-book --filter=&quot;tr '[a-z]' '[A-Z]'&quot; BOOK</tt><br/>
 <tt>$ lilypond-book -F &quot;convert-ly --no-version --from=2.0.0 -&quot; BOOK</tt><br/>
 <tt>$ lilypond-book --process='lilypond -I include' BOOK</tt></dd></dl>
<h2>REPORTING BUGS</h2>
<p> Report bugs via <a rel="nofollow" href="http://post.gmane.org/post.php?group=gmane.comp.gnu.lilypond.bugs">http://post.gmane.org/post.php?group=gmane.comp.gnu.lilypond.bugs</a></p>
<h2>SEE ALSO</h2>
<p> The full documentation for <code>lilypond-book</code> is maintained as a Texinfo manual. If the <code>info</code> and <code>lilypond-book</code> programs are properly installed at your site, the command</p>
<dl>
<dt>
</dt><dd> <code>info lilypond-book</code></dd></dl>
<p> should give you access to the complete manual. </p>
