---
title: "zbarcam(1)"
name: "zbarcam"
section: "1"
letter: "z"
url: "/docs/linux/man/1-zbarcam/"
description: "zbarcam – scan and decode bar codes from a video device"
---

<h2 class="name">NAME</h2>
<p> zbarcam &#8211; scan and decode bar codes from a video device </p>
<h2>SYNOPSIS</h2>
<dl>
<dt> <code>zbarcam</code> [<code>-qv</code>] [<code>&#8211;quiet</code>] [<code>&#8211;nodisplay</code>] [<code>&#8211;xml</code>] [<code>&#8211;verbose</code><code>[=</code><i>n</i>]] [<code>&#8211;prescale=</code><i>W</i><code>x</code><i>H</i>] [<code>-S</code><code>[</code><i>symbology</i>.]<i>config</i><code>[=</code><i>value</i>]] [<code>&#8211;set&nbsp;<wbr></code><code>[</code><i>symbology</i>.]<i>config</i><code>[=</code><i>value</i>]] [<i>device</i>]</p>
<dt> <code>zbarcam</code> {<code>-h</code> | <code>&#8211;help</code> | <code>&#8211;version</code>}</dl>
<h2>DESCRIPTION</h2>
<p> <code>zbarcam</code></p>
<dd>scans a video4linux video source (eg, a webcam) for bar codes and prints any decoded data to the standard output. The video stream is also displayed to the screen. </p>
<p> <i>device</i> is the path to the video4linux (version 1 or 2) character device special file (major number 81 and minor number 0 thru 63). It defaults to /dev/video0 </p>
<p> The underlying library currently supports EAN-13 (including UPC and ISBN subsets), EAN-8, DataBar, DataBar Expanded, Code 128, Code 93, Code 39, Codabar, Interleaved 2 of 5 and QR Code symbologies. The specific type of each detected symbol is printed with the decoded data.</p>
<h2>OPTIONS</h2>
<p> This program follows the usual GNU command line syntax. Single letter options may be bundled, long options start with two dashes (`-&#8216;). </p>
<p> <code>-h</code>, <code>&#8211;help</code></p>
<dl>
<dt>
<dd> Print a short help message describing command line options to standard output and exit</dl>
<p> <code>&#8211;version</code></p>
<dl>
<dt>
<dd> Print program version information to standard output and exit</dl>
<p> <code>-v</code>, <code>&#8211;verbose</code><code>[=</code><i>n</i>]</p>
<dl>
<dt>
<dd> Increase debug output level. Multiple <code>-v</code> options create more spew. Alternatively specify <i>n</i> to set the debug level directly</dl>
<p> <code>-S</code><code>[</code><i>symbology</i>.]<i>config</i><code>[=</code><i>value</i>], <code>&#8211;set </code><code>[</code><i>symbology</i>.]<i>config</i><code>[=</code><i>value</i>]</p>
<dl>
<dt>
<dd> Set decoder configuration option <i>config</i> for <i>symbology</i> to <i>value</i>. <i>value</i> defaults to 1 if omitted. <i>symbology</i> is one of <code>ean13</code>, <code>ean8</code>, <code>upca</code>, <code>upce</code>, <code>isbn13</code>, <code>isbn10</code>, <code>i25</code>, <code>codabar</code>, <code>code39</code>, <code>code93</code>, <code>code128</code>, <code>qrcode</code> or the special value <code>*</code>. If <i>symbology</i> is omitted or <code>*</code>, the <i>config</i> will be set for all applicable symbologies. These are the currently recognized <i>config</i>s. Prefix a config with &quot;no-&quot; to negate it. Not all configs are appropriate for every symbology. </p>
<p> <code>enable</code></p>
<dl>
<dt>
<dd> Control decoding/reporting of a symbology. For symbologies which are just subsets of <code>ean13</code> (<code>upca</code>, <code>upce</code>, <code>isbn13</code>, <code>isbn10</code>), this config controls whether the subsets are detected and reported as such. These special cases are disabled by default, all other symbologies default to enabled</dl>
<p> <code>disable</code></p>
<dl>
<dt>
<dd> Antonym for <code>enable</code></dl>
<p> <code>emit-check</code></p>
<dl>
<dt>
<dd> Control whether check digits are included in the decoded output. Enabled by default. This config does not apply for <code>code128</code>, which never returns the check digit. It also not apply for cases where the check digit is disabled (see <code>add-check</code>). Check digits are currently not implemented for <code>i25</code> or <code>code39</code></dl>
<p> <code>add-check</code></p>
<dl>
<dt>
<dd> Enable decode and verification of a check digit for symbologies where it is optional: this will include <code>code39</code> and <code>i25</code>, neither of which implements the check digit yet</dl>
<p> <code>ascii</code></p>
<dl>
<dt>
<dd> Enable escape sequences that encode the full ASCII character set. This would apply to <code>code39</code>, except that it&#8217;s not implemented either&#8230;</dl>
<p> <code>position</code></p>
<dl>
<dt>
<dd> Enable collection of symbol position information. Enabled by default. Currently, the position information is unusable, so you can save a few cycles by disabling this.</dl>
<p> <code>min-length=</code><i>n</i>, <code>max-length=</code><i>n</i></p>
<dl>
<dt>
<dd> Bound the number of decoded characters in a valid symbol. If a decode result is outside the configured min/max range (inclusive), it will not be reported. Set to 0 to disable the corresponding check. This setting applies to variable-length symbologies: <code>i25</code>, <code>codabar</code>, <code>code39</code>, <code>code128</code> and <code>pdf417</code>. <code>min-length</code> defaults to 6 for <code>i25</code> and 1 for <code>code39</code> (per Code 39 autodiscrimination recommendation); all others default to 0</dl>
<p> <code>x-density=</code><i>n</i>, <code>y-density=</code><i>n</i></p>
<dl>
<dt>
<dd> Adjust the density of the scanner passes. Lower values scan more of the image at the cost of decreased performance. Setting to 0 disables scanning along that axis. Defaults are both 1.</dl>
</dl>
<p> <code>-q</code>, <code>&#8211;quiet</code></p>
<dl>
<dt>
<dd> Quiet operation; disable the audible beep otherwise emitted when a symbol is decoded</dl>
<p> <code>&#8211;nodisplay</code></p>
<dl>
<dt>
<dd> Disable output video window. Video input will be scanned until the program is interrupted or otherwise signaled</dl>
<p> <code>&#8211;xml</code></p>
<dl>
<dt>
<dd> Stream results using an XML output format. This format wraps the raw data from the symbol with information about the scan in an easy to parse format. The latest schema is available from m[blue]<code><a rel="nofollow" href="http://zbar.sourceforge.net/2008/barcode.xsd">http://zbar.sourceforge.net/2008/barcode.xsd</a></code>m[]</dl>
<p> <code>&#8211;raw</code></p>
<dl>
<dt>
<dd> Use raw symbol data output format. This format prints symbol data separated by newlines without the additional symbology type information that is printed by default</dl>
<p> <code>&#8211;prescale=</code><i>W</i><code>x</code><i>H</i></p>
<dl>
<dt>
<dd> Request video input scaling from the camera driver. Possibly useful for reducing huge frames to achieve a higher frame rate. Note that the driver may adjust or completely ignore the scaling request</dl>
<h2>EXAMPLES</h2>
<p> Scan for barcodes using the second video device and pipe the resulting data through a script that searches for each code in a database and does something useful with them: </p>
<dl>
<dt>
<dd>
<pre>
<code>zbarcam</code> /dev/video1 | <code>upcrpc.py</code>
</pre>
</dl>
<p> The <code>upcrpc.py</code> example script included in the examples/ subdirectory of the distribution will make an XMLRPC call to a popular internet UPC database and print the product description if found. </p>
<p> Scan for barcodes using the default video device and stream results to stdout in XML format, also disable recognition of Interleaved 2 of 5 codes to prevent confusion with other symbologies or background noise: </p>
<dl>
<dt>
<dd>
<pre>
<code>zbarcam</code> <code>--xml</code> <code>-Si25.disable</code>
</pre>
</dl>
<p> Scan only for Code 39, without using the preview window &#8211; maybe for a fixed installation. To enable only Code 39, first all symbologies are disabled, then Code 39 is re-enabled: </p>
<dl>
<dt>
<dd>
<pre>
<code>zbarcam</code> <code>--nodisplay</code> <code>-Sdisable</code> <code>-Scode39.enable</code>
</pre>
</dl>
<h2>EXIT STATUS</h2>
<p> <code>zbarcam</code> returns an exit code to indicate the status of the program execution. Current exit codes are: </p>
<p> 0</p>
<dl>
<dt>
<dd> Successful program completion.</dl>
<p> 1</p>
<dl>
<dt>
<dd> An error occurred. This includes bad arguments and I/O errors.</dl>
<p> 2</p>
<dl>
<dt>
<dd> A fatal error occurred.</dl>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-zbarimg/">zbarimg</a>(1) </p>
<p> m[blue]<code><a rel="nofollow" href="http://zbar.sf.net/">http://zbar.sf.net/</a></code>m[]</p>
<h2>BUGS</h2>
<p> See m[blue]<code><a rel="nofollow" href="http://sf.net/tracker/?group_id=189236">http://sf.net/tracker/?group_id=189236</a>&amp;atid=928515</code>m[]</p>
<h2>AUTHOR</h2>
<p> <code>Jeff Brown</code> &lt;spadix [at] users.sourceforge.net&gt;</p>
<dl>
<dt>
<dd> Lead developer</dl>
<h2>COPYRIGHT</h2>
<p> Copyright &#169; 2007-2010 Jeff Brown </p>
<p> All Rights Reserved </p>
<h2>Index</h2>
