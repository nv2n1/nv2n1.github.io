---
title: "mime-convs(5)"
name: "mime-convs"
section: "5"
letter: "m"
url: "/docs/linux/man/5-mime-convs/"
description: "mime.convs – mime type conversion file for cups (deprecated)"
---

<p>mime.convs &#8211; mime type conversion file for cups (deprecated)</p>
<h2>Description</h2>
<p>The <code>mime.convs</code> file defines the filters that are available for converting files from one format to another. The standard filters support text, PDF, PostScript, and many types of image files. </p>
<p> Additional filters are specified in files with the extension <i>.convs</i> in the CUPS configuration directory. </p>
<p> Each line in the <code>mime.convs</code> file is a comment, blank, or filter line. Comment lines start with the # character. Filter lines specify the source and destination MIME types along with a relative cost associated with the filter and the filter to run: </p>
<pre> source/type destination/type cost filter</pre>
<p>The <i>source/type</i> field specifies the source MIME media type that is consumed by the filter. </p>
<p> The <i>destination/type</i> field specifies the destination MIME media type that is produced by the filter. </p>
<p> The <i>cost</i> field specifies the relative cost for running the filter. A value of 100 means that the filter uses a large amount of resources while a value of 0 means that the filter uses very few resources. </p>
<p> The <i>filter</i> field specifies the filter program filename. Filenames are relative to the CUPS filter directory.</p>
<h2>Files</h2>
<p><i>/etc/cups</i> &#8211; Typical CUPS configuration directory.<br />
 <i>/usr/lib/cups/filter</i> &#8211; Typical CUPS filter directory.<br />
 <i>/usr/libexec/cups/filter</i> &#8211; CUPS filter directory on macOS.</p>
<h2>Examples</h2>
<p>Define a filter that converts PostScript documents to CUPS Raster format: </p>
<pre> application/vnd.cups-postscript application/vnd.cups-raster 50 pstoraster</pre>
<h2>Notes</h2>
<p>CUPS filters are deprecated and will no longer be supported in a future feature release of CUPS. Printers that do not support IPP can be supported using applications such as <code><a href="/docs/linux/man/1-ippeveprinter/">ippeveprinter</a></code>(1).</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/5-cups-files-conf/">cups-files.conf</a></code>(5), <code><a href="/docs/linux/man/5-cupsd-conf/">cupsd.conf</a></code>(5), <code><a href="/docs/linux/man/8-cupsd/">cupsd</a></code>(8), <code><a href="/docs/linux/man/8-cupsfilter/">cupsfilter</a></code>(8), <code><a href="/docs/linux/man/5-mime-types/">mime.types</a></code>(5), CUPS Online Help (<a rel="nofollow" href="http://localhost:631/help)">http://localhost:631/help)</a></p>
<h2>Copyright</h2>
<p>Copyright &#169; 2021-2022 by OpenPrinting.</p>
