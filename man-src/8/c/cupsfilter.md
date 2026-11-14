---
title: "cupsfilter(8)"
name: "cupsfilter"
section: "8"
letter: "c"
url: "/docs/linux/man/8-cupsfilter/"
description: "cupsfilter – convert a file to another format using cups filters (deprecated)"
---

<p>cupsfilter &#8211; convert a file to another format using cups filters (deprecated)</p>
<h2>Synopsis</h2>
<p><code>cupsfilter</code> [ <code>&#8211;list-filters</code> ] [ <code>-D</code> ] [ <code>-U</code> <i>user</i> ] [ <code>-c</code> <i>config-file</i> ] [ <code>-d</code> <i>printer</i> ] [ <code>-e</code> ] [ <code>-i</code> <i>mime/type</i> ] [ <code>-j</code> <i>job-id[,N]</i> ] [ <code>-m</code> <i>mime/type</i> ] [ <code>-n</code> <i>copies</i> ] [ <code>-o</code> <i>name=value</i> ] [ <code>-p</code> <i>filename.ppd</i> ] [ <code>-t</code> <i>title</i> ] [ <code>-u</code> ] <i>filename</i></p>
<h2>Description</h2>
<p><code>cupsfilter</code> is a front-end to the CUPS filter subsystem which allows you to convert a file to a specific format, just as if you had printed the file through CUPS. By default, <code>cupsfilter</code> generates a PDF file. The converted file is sent to the standard output.</p>
<h2>Options</h2>
<dl>
<dt><code>&#8211;list-filters</code></p>
<dd>Do not actually run the filters, just print the filters used to stdout.</p>
<dt><code>-D</code></p>
<dd>Delete the input file after conversion.</p>
<dt><code>-U </code><i>user</i></p>
<dd>Specifies the username passed to the filters. The default is the name of the current user.</p>
<dt><code>-c </code><i>config-file</i></p>
<dd>Uses the named cups-files.conf configuration file.</p>
<dt><code>-d </code><i>printer</i></p>
<dd>Uses information from the named printer.</p>
<dt><code>-e</code></p>
<dd>Use every filter from the PPD file.</p>
<dt><code>-i </code><i>mime/type</i></p>
<dd>Specifies the source file type. The default file type is guessed using the filename and contents of the file.</p>
<dt><code>-j </code><i>job-id[,N]</i></p>
<dd>Converts document N from the specified job. If N is omitted, document 1 is converted.</p>
<dt><code>-m </code><i>mime/type</i></p>
<dd>Specifies the destination file type. The default file type is application/pdf. Use printer/foo to convert to the printer format defined by the filters in the PPD file.</p>
<dt><code>-n </code><i>copies</i></p>
<dd>Specifies the number of copies to generate.</p>
<dt><code>-o </code><i>name=value</i></p>
<dd>Specifies options to pass to the CUPS filters.</p>
<dt><code>-p </code><i>filename.ppd</i></p>
<dd>Specifies the PPD file to use.</p>
<dt><code>-t </code><i>title</i></p>
<dd>Specifies the document title.</p>
<dt><code>-u</code></p>
<dd>Delete the PPD file after conversion.</dl>
<h2>Exit Status</h2>
<p><code>cupsfilter</code> returns a non-zero exit status on any error.</p>
<h2>Environment</h2>
<p>All of the standard <code><a href="/docs/linux/man/1-cups/">cups</a></code>(1) environment variables affect the operation of <code>cupsfilter</code>.</p>
<h2>Files</h2>
<pre>/etc/cups/cups-files.conf
/etc/cups/*.convs
/etc/cups/*.types
/usr/share/cups/mime/*.convs
/usr/share/cups/mime/*.types</pre>
<h2>Notes</h2>
<p>CUPS printer drivers, filters, and backends are deprecated and will no longer be supported in a future feature release of CUPS. Printers that do not support IPP can be supported using applications such as <code><a href="/docs/linux/man/1-ippeveprinter/">ippeveprinter</a></code>(1). </p>
<p> Unlike when printing, filters run using the <code>cupsfilter</code> command use the current user and security session. This may result in different output or unexpected behavior.</p>
<h2>Example</h2>
<p>The following command will generate a PDF preview of job 42 for a printer named &quot;myprinter&quot; and save it to a file named &quot;preview.pdf&quot;: </p>
<pre> cupsfilter -m application/pdf -d myprinter -j 42 &gt;preview.pdf</pre>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-cups/">cups</a></code>(1), <code><a href="/docs/linux/man/5-cupsd-conf/">cupsd.conf</a></code>(5), <code><a href="/docs/linux/man/7-filter/">filter</a>(7),</code> <code><a href="/docs/linux/man/7-mime-convs/">mime.convs</a></code>(7), <code><a href="/docs/linux/man/7-mime-types/">mime.types</a></code>(7), CUPS Online Help (<a rel="nofollow" href="http://localhost:631/help)">http://localhost:631/help)</a></p>
<h2>Copyright</h2>
<p>Copyright &#169; 2021-2022 by OpenPrinting.</p>
