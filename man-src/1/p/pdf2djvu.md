---
title: "pdf2djvu(1)"
name: "pdf2djvu"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pdf2djvu/"
description: "pdf2djvu – creates DjVu files from PDF files"
---

<h2 class="name">NAME</h2>
<p> pdf2djvu &#8211; creates DjVu files from PDF files </p>
<h2>SYNOPSIS</h2>
<dl>
<dt> <code>pdf2djvu</code> [{<code>-o</code>&nbsp;<wbr>|&nbsp;<wbr><code>&#8211;output</code>}&nbsp;<wbr><i>output-djvu-file</i>] [<i>option</i>&#8230;] <i>pdf-file</i>&#8230;</p>
<dt> <code>pdf2djvu</code> {<code>-i</code>&nbsp;<wbr>|&nbsp;<wbr><code>&#8211;indirect</code>}&nbsp;<wbr><i>index-djvu-file</i> [<i>option</i>&#8230;] <i>pdf-file</i>&#8230;</p>
<dt> <code>pdf2djvu</code> {<code>&#8211;version</code> | <code>&#8211;help</code> | <code>-h</code>}</dl>
<h2>DESCRIPTION</h2>
<dd>This program creates a DjVu file from one or more Portable Document Format files.</p>
<h2>OPTIONS</h2>
<p> <code>pdf2djvu</code> accepts the following options:</p>
<h3>Document type, file names</h3>
<p> <code>-o</code>, <code>&#8211;output=</code><i>output-djvu-file</i></p>
<dl>
<dt>
<dd> Generate a bundled multi-page document. Write the file into <i>output-djvu-file</i> instead of standard output.</dl>
<p> <code>-i</code>, <code>&#8211;indirect=</code><i>index-djvu-file</i></p>
<dl>
<dt>
<dd> Generate an indirect multi-page document. Use <i>index-djvu-file</i> as the index file name; put the component files into the same directory. The directory must exist and be writable.</dl>
<p> <code>&#8211;pageid-template=</code><i>template</i></p>
<dl>
<dt>
<dd> Specifies the naming scheme for page identifiers. Consult the &#8220;TEMPLATE LANGUAGE&#8221; section for the template language description. </p>
<p> The default template is &#8220;p{page:04*}.djvu&#8221;. </p>
<p> For portability reasons, page identifiers: </p>
<dl>
<dt>
<dd> &bull; must consist only of lowercase ASCII letters, digits, _, +, &#8211; and dot,</dl>
<dl>
<dt>
<dd> &bull; cannot start with a +, &#8211; or a dot,</dl>
<dl>
<dt>
<dd> &bull; cannot contain two consecutive dots,</dl>
<dl>
<dt>
<dd> &bull; must end with the .djvu or the .djv extension.</dl>
</dl>
<p> <code>&#8211;pageid-prefix=</code><i>prefix</i></p>
<dl>
<dt>
<dd> Equivalent to &#8220;&#8211;pageid-template=<i>prefix</i>{page:04*}.djvu&#8221;.</dl>
<p> <code>&#8211;page-title-template=</code><i>template</i></p>
<dl>
<dt>
<dd> Specifies the template for page titles. Consult the &#8220;TEMPLATE LANGUAGE&#8221; section for the template language description. </p>
<p> The default is to set no page titles.</dl>
<h3>Resolution, page size</h3>
<p> <code>-d</code>, <code>&#8211;dpi=</code><i>resolution</i></p>
<dl>
<dt>
<dd> Specifies the desired resolution to <i>resolution</i> dots per inch. The default is 300 dpi. The allowed range is: 72 &le; <i>resolution</i> &le; 6000.</dl>
<p> <code>&#8211;media-box</code></p>
<dl>
<dt>
<dd> Use MediaBox to determine page size. CropBox is used by default.</dl>
<p> <code>&#8211;page-size=</code><i>width</i><code>x</code><i>height</i></p>
<dl>
<dt>
<dd> Specifies the preferred page size to <i>width</i> pixels &#215; <i>height</i> pixels. The actual page size may be altered in order to respect aspect ratio and DjVu limitations on resolution. (This option takes precedence over <code>-d</code>/<code>&#8211;dpi</code>.)</dl>
<p> <code>&#8211;guess-dpi</code></p>
<dl>
<dt>
<dd> Try to guess native resolution by inspecting embedded images. Use with care.</dl>
<h3>Image quality</h3>
<p> <code>&#8211;bg-slices=</code><i>n</i><code>+</code><i>&#8230;</i><code>+</code><i>n</i>, <code>&#8211;bg-slices=</code><i>n</i><code>,</code><i>&#8230;</i><code>,</code><i>n</i></p>
<dl>
<dt>
<dd> Specifies the encoding quality of the IW44 background layer. This option is similar to the <code>-slice</code> option of <code>c44</code>. Consult the <code><a href="/docs/linux/man/1-c44/">c44</a></code>(1) manual page for details. The default is 72+11+10+10.</dl>
<p> <code>&#8211;bg-subsample=</code><i>n</i></p>
<dl>
<dt>
<dd> Specifies the background subsampling ratio. The default is 3. Valid values are integers between 1 and 12, inclusive.</dl>
<p> <code>&#8211;fg-colors=default</code></p>
<dl>
<dt>
<dd> Try to preserve all the foreground layer colors. This is the default.</dl>
<p> <code>&#8211;fg-colors=web</code></p>
<dl>
<dt>
<dd> Reduce foreground layer colors to the web palette (216 colors). This option is not recommended.</dl>
<p> <code>&#8211;fg-colors=</code><i>n</i></p>
<dl>
<dt>
<dd> Use GraphicsMagick to reduce number of distinct colors in the foreground layer to <i>n</i>. Valid values are integers between 1 and 4080. This option is not recommended.</dl>
<p> <code>&#8211;fg-colors=black</code></p>
<dl>
<dt>
<dd> Discard any color information from the foreground layer.</dl>
<p> <code>&#8211;monochrome</code></p>
<dl>
<dt>
<dd> Render pages as monochrome bitmaps. With this option, <code>&#8211;bg-</code><i>&#8230;</i> and <code>&#8211;fg-</code><i>&#8230;</i> options are not respected.</dl>
<p> <code>&#8211;loss-level=</code><i>n</i></p>
<dl>
<dt>
<dd> Specifies the aggressiveness of the lossy compression. The default is 0 (lossless). Valid values are integers between 0 and 200, inclusive. This option is similar to the <code>-losslevel</code> option of <code>cjb2</code>; consult the <code><a href="/docs/linux/man/1-cjb2/">cjb2</a></code>(1) manual page for details. This option is respected only along with the <code>&#8211;monochrome</code> option.</dl>
<p> <code>&#8211;lossy</code></p>
<dl>
<dt>
<dd> Synonym for <code>&#8211;loss-level=100</code>.</dl>
<p> <code>&#8211;anti-alias</code></p>
<dl>
<dt>
<dd> Enable font and vector anti-aliasing. This option is not recommended.</dl>
<h3>Extraction</h3>
<p> <code>&#8211;no-metadata</code></p>
<dl>
<dt>
<dd> Don&#8217;t extract the metadata. </p>
<p> By default: </p>
<dl>
<dt>
<dd> &bull; The following entries of the document information dictionary are extracted: Title, Author, Subject, Creator, Producer, CreationDate, ModDate. Timestamps are formatted according to m[blue]<code>RFC 3999</code>m[]<font SIZE="-2">[1]</font>, with date and time components separated by a single space.</dl>
<dl>
<dt>
<dd> &bull; The XMP metadata is extracted (or created) and updated accordingly.</dl>
<dl>
<dt>
<dd>
 <font SIZE="+1"> <code>Note</code> </font><br />
 If multiple input documents are specified, only metadata of the first one is taken into account. </p>
</dl>
</dl>
<p> <code>&#8211;verbatim-metadata</code></p>
<dl>
<dt>
<dd> Keep the original metadata intact.</dl>
<p> <code>&#8211;no-outline</code></p>
<dl>
<dt>
<dd> Don&#8217;t extract the document outline.</dl>
<p> <code>&#8211;hyperlinks=border-avis</code></p>
<dl>
<dt>
<dd> Make hyperlink borders always visible. </p>
<p> By default, a hyperlink border is visible only when the mouse is over the hyperlink.</dl>
<p> <code>&#8211;hyperlinks=#</code><i>RRGGBB</i></p>
<dl>
<dt>
<dd> Force the specified border color for hyperlinks.</dl>
<p> <code>&#8211;no-hyperlinks</code>, <code>&#8211;hyperlinks=none</code></p>
<dl>
<dt>
<dd> Don&#8217;t extract hyperlinks.</dl>
<p> <code>&#8211;no-text</code></p>
<dl>
<dt>
<dd> Don&#8217;t extract the text.</dl>
<p> <code>&#8211;words</code></p>
<dl>
<dt>
<dd> Extract the text. Record the location of every word. This is the default.</dl>
<p> <code>&#8211;lines</code></p>
<dl>
<dt>
<dd> Extract the text. Record the location of every line, rather that every word.</dl>
<p> <code>&#8211;crop-text</code></p>
<dl>
<dt>
<dd> Extract no text outside the page boundary.</dl>
<p> <code>&#8211;no-nfkc</code></p>
<dl>
<dt>
<dd> Don&#8217;t m[blue]<code>NFKC</code>m[]<font SIZE="-2">[2]</font>-normalize the text.</dl>
<p> <code>&#8211;filter-text=</code><i>command-line</i></p>
<dl>
<dt>
<dd> Filter the text through the <i>command-line</i>. The provided filter must preserve whitespace, control characters and decimal digits. </p>
<p> This option implies <code>&#8211;no-nfkc</code>.</dl>
<p> <code>-p</code>, <code>&#8211;pages=</code><i>page-range</i></p>
<dl>
<dt>
<dd> Specifies pages to convert. <i>page-range</i> is a comma-separated list of sub-ranges. Each sub-range is either a single page (e.g. 17) or a contiguous range of pages (e.g. 37-42). Pages are numbered from 1. </p>
<p> The default is to convert all pages.</dl>
<h3>Performance</h3>
<p> <code>-j</code>, <code>&#8211;jobs=</code><i>n</i></p>
<dl>
<dt>
<dd> Use <i>n</i> threads to perform conversion. The default is to use one thread.</dl>
<p> <code>-j0</code>, <code>&#8211;jobs=0</code></p>
<dl>
<dt>
<dd> Determine automatically how many threads to use to perform conversion.</dl>
<h3>Verbosity, help</h3>
<p> <code>-v</code>, <code>&#8211;verbose</code></p>
<dl>
<dt>
<dd> Display more informational messages while converting the file.</dl>
<p> <code>-q</code>, <code>&#8211;quiet</code></p>
<dl>
<dt>
<dd> Don&#8217;t display informational messages while converting the file.</dl>
<p> <code>&#8211;version</code></p>
<dl>
<dt>
<dd> Output version information and exit.</dl>
<p> <code>-h</code>, <code>&#8211;help</code></p>
<dl>
<dt>
<dd> Display help and exit.</dl>
<h2>ENVIRONMENT</h2>
<p> The following environment variables affects <code>pdf2djvu</code> on Unix systems: </p>
<p> <i>OMP_</i><i>*</i></p>
<dl>
<dt>
<dd> Details of runtime behaviour with respect to parallelism can be controlled by several environment variables. Please refer to the m[blue]<code>OpenMP API specification</code>m[]<font SIZE="-2">[3]</font> for details.</dl>
<p> <i>TMPDIR</i></p>
<dl>
<dt>
<dd> <code>pdf2djvu</code> makes heavy use of temporary files. It will store them in a directory specified by this variable. The default is /tmp.</dl>
<h2>TEMPLATE LANGUAGE</h2>
<h3>Template syntax</h3>
<p> The template language is roughly modelled on the m[blue]<code>Python string formatting syntax</code>m[]<font SIZE="-2">[4]</font>. </p>
<p> A template is a piece of text which contains fields, surrounded by curly braces {}. Fields are replaced with appropriately formatted values when the template is evaluated. Moreover, &#123;&#123; is replaced with a single { and }} is replaced with a single }.</p>
<h3>Field syntax</h3>
<p> Each field consists of a variable name, optionally followed by a shift, optionally followed by a format specification. </p>
<p> The shift is a signed (i.e. starting with a + or &#8211; character) integer. </p>
<p> The format specification consists of a colon, followed by a width specification. </p>
<p> The width specification is a decimal integer defining the minimum field width. If not specified, then the field width will be determined by the content. Preceding the width specification with a zero (0) character enables zero-padding. </p>
<p> The width specification is optionally followed by an asterisk (*) character, which increases the minimum field width to the width of the longest possible content of the variable.</p>
<h3>Available variables</h3>
<p> <i>page</i>, <i>spage</i></p>
<dl>
<dt>
<dd> Page number in the PDF document.</dl>
<p> <i>dpage</i></p>
<dl>
<dt>
<dd> Page number in the DjVu document.</dl>
<h2>IMPLEMENTATION DETAILS</h2>
<h3>Layer separation algorithm</h3>
<p> Unless the <code>&#8211;monochrome</code> option is on, pdf2djvu uses the following na&iuml;ve layer separation algorithm: </p>
<dl>
<dt>
<dd> 1. For each page, do the following: </p>
<dl>
<dt>
<dd> 1. Raster the page into a pixmap, in the usual manner.</dl>
<dl>
<dt>
<dd> 2. Raster the page into another pixmap, omitting the following page elements: </p>
<dl>
<dt>
<dd> &bull; text,</dl>
<dl>
<dt>
<dd> &bull; 1 bit-per-pixel raster images,</dl>
<dl>
<dt>
<dd> &bull; vector elements (except fills of large areas).</dl>
</dl>
<dl>
<dt>
<dd> 3. Compare both pixmaps, pixel by pixel: </p>
<dl>
<dt>
<dd> 1. If their colors match, classify the pixel as a part of the background layer.</dl>
<dl>
<dt>
<dd> 2. Otherwise, classify the pixel as a part of the foreground layer.</dl>
</dl>
</dl>
<h2>BUG REPORTS</h2>
<p> If you find a bug in pdf2djvu, please report it at m[blue]<code>the issue tracker</code>m[]<font SIZE="-2">[5]</font>.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-djvu/">djvu</a></code>(1), <code><a href="/docs/linux/man/1-djvudigital/">djvudigital</a></code>(1), <code><a href="/docs/linux/man/1-csepdjvu/">csepdjvu</a></code>(1)</p>
<h2>AUTHOR</h2>
<p> <code>Jakub Wilk</code> &lt;jwilk [at] jwilk.net&gt;</p>
<dl>
<dt>
<dd> Author.</dl>
<h2>NOTES</h2>
<dl>
<dt> 1.</p>
<dd> RFC 3999</p>
<dl>
<dt>
<dd> <a rel="nofollow" href="https://www.ietf.org/rfc/rfc3339">https://www.ietf.org/rfc/rfc3339</a></dl>
<dt> 2.</p>
<dd> NFKC</p>
<dl>
<dt>
<dd> <a rel="nofollow" href="http://unicode.org/reports/tr15/">http://unicode.org/reports/tr15/</a></dl>
<dt> 3.</p>
<dd> OpenMP API specification</p>
<dl>
<dt>
<dd> <a rel="nofollow" href="http://openmp.org/wp/openmp-specifications/">http://openmp.org/wp/openmp-specifications/</a></dl>
<dt> 4.</p>
<dd> Python string formatting syntax</p>
<dl>
<dt>
<dd> <a rel="nofollow" href="https://docs.python.org/library/string.html#format-string-syntax">https://docs.python.org/library/string.html#format-string-syntax</a></dl>
<dt> 5.</p>
<dd> the issue tracker</p>
<dl>
<dt>
<dd> <a rel="nofollow" href="https://bitbucket.org/jwilk/pdf2djvu/issues">https://bitbucket.org/jwilk/pdf2djvu/issues</a></dl>
</dl>
<h2>Index</h2>
