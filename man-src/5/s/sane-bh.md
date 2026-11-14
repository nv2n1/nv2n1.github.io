---
title: "sane-bh(5)"
name: "sane-bh"
section: "5"
letter: "s"
url: "/docs/linux/man/5-sane-bh/"
description: "sane-bh – SANE backend for Bell+Howell Copiscan II series document scanners"
---

<p>sane-bh &#8211; SANE backend for Bell+Howell Copiscan II series document scanners</p>
<h2>Description</h2>
<p>The <code>sane-bh</code> library implements a SANE (Scanner Access Now Easy) backend that provides access to Bell+Howell Copiscan II series document scanners. The Copiscan II 6338 has been the primary scanner model used during development and testing, but since the programming interface for the entire series is consistent the backend should work for the following scanner models: </p>
<dl>
<dd>COPISCAN II 6338 Duplex Scanner with ACE<br />
 COPISCAN II 2135 Simplex Scanner<br />
 COPISCAN II 2137(A) Simplex Scanner (with ACE)<br />
 COPISCAN II 2138A Simplex Scanner with ACE<br />
 COPISCAN II 3238 Simplex Scanner<br />
 COPISCAN II 3338(A) Simplex Scanner (with ACE)
</dl>
<p> If you have a Bell+Howell scanner and are able to test it with this backend, please contact <i>sane-devel [at] alioth-lists.debian.net</i> with the model number and testing results. Have a look at <i><a rel="nofollow" href="http://www.sane-project.org/mailing-lists.html">http://www.sane-project.org/mailing-lists.html</a></i> concerning subscription to sane-devel. Additionally, the author is curious as to the likelihood of using this backend with the newer 4000 and 8000 series scanners. If you have such a beast, please let me know. </p>
<p> The Bell+Howell Copiscan II series document scanners are high volume, high throughput scanners designed for document scanning applications. As such, they are lineart/grayscale scanners supporting a fixed number of fairly low resolutions (e.g. 200/240/300dpi). However, they do have a number of interesting and useful features suited to needs of document imaging applications. This backend attempts to support as many of these features as possible. </p>
<p> The main technical reference used in writing this backend is the <code>Bell and Howell Copiscan II Remote SCSI Controller (RSC) OEM</code> <code>Technical Manual Version 1.5.</code> The Linux SCSI programming HOWTO, the SANE API documentation, and SANE source code were also extremely valuable resources. </p>
<p> The latest backend release, additional information and helpful hints are available from the backend homepage: </p>
<dl>
<dd><i><a rel="nofollow" href="http://www.martoneconsulting.com/sane-bh.html">http://www.martoneconsulting.com/sane-bh.html</a></i></dl>
<h2>Device Names</h2>
<p>This backend expects device names of the form: </p>
<dl>
<dd><i>special</i></dl>
<p> Where <i>special</i> is the path-name for the special device that corresponds to a SCSI scanner. For SCSI scanners, the special device name must be a generic SCSI device or a symlink to such a device. Under Linux, such a device name takes a format such as <i>/dev/sga</i> or <i>/dev/sg0</i>, for example. See <code><a href="/docs/linux/man/5-sane-scsi/">sane-scsi</a></code>(5) for details.</p>
<h2>Options</h2>
<dl>
<dt><code>Scan Mode Options:</code></p>
<dd>
<dt><code>&#8211;preview[=(yes|no)] [no]</code></p>
<dd>Request a preview-quality scan. When preview is set to yes image compression is disabled and the image is delivered in a <code>SANE_FRAME_GRAY</code> frame.</p>
<dt><code>&#8211;mode lineart|halftone [lineart]</code></p>
<dd>Selects the scan mode (e.g., lineart,monochrome, or color).</p>
<dt><code>&#8211;resolution 200|240|300dpi [200]</code></p>
<dd>Sets the resolution of the scanned image. Each scanner model supports a list of standard resolutions; only these resolutions can be used.</p>
<dt><code>&#8211;compression none|g31d|g32d|g42d [none]</code></p>
<dd>Sets the compression mode of the scanner. Determines the type of data returned from the scanner. Values are: </p>
<dl>
<dd><code>none</code> &#8211; uncompressed data &#8211; delivered in a SANE_FRAME_GRAY frame<br />
 <code>g31d</code> &#8211; CCITT G3 1 dimension (MH) &#8211; delivered in a SANE_FRAME_G31D frame<br />
 <code>g32d</code> &#8211; CCITT G3 2 dimensions (MR, K=4) &#8211; delivered in a SANE_FRAME_G32D frame<br />
 <code>g42d</code> &#8211; CCITT G4 (MMR) &#8211; delivered in a SANE_FRAME_G42D frame </p>
<p> <code>NOTE</code>: The use of g31d, g32d, and g42d compression values causes the backend to generate optional frame formats which may not be supported by all SANE frontends.</dl>
<dt><code>Geometry Options:</code></p>
<dd>
<dt><code>&#8211;autoborder[=(yes|no)] [yes]</code></p>
<dd>Enable/Disable automatic image border detection. When enabled, the RSC unit automatically detects the image area and sets the window geometry to match.</p>
<dt><code>&#8211;paper-size Custom|Letter|Legal|A3|A4|A5|A6|B4|B5 [Custom]</code></p>
<dd>Specify the scan window geometry by specifying the paper size of the documents to be scanned.</p>
<dt><code>&#8211;tl-x 0..297.18mm [0]</code></p>
<dd>Top-left x position of scan area.</p>
<dt><code>&#8211;tl-y 0..431.8mm [0]</code></p>
<dd>Top-left y position of scan area.</p>
<dt><code>&#8211;br-x 0..297.18mm [297.18]</code></p>
<dd>Bottom-right x position of scan area.</p>
<dt><code>&#8211;br-y 0..431.8mm [431.8]</code></p>
<dd>Bottom-right y position of scan area.</p>
<dt><code>Feeder Options:</code></p>
<dd>
<dt><code>&#8211;source Automatic Document Feeder|Manual Feed Tray [Automatic Document Feeder]</code></p>
<dd>Selects the scan source (such as a document feeder). This option is provided to allow multiple image scans with <code><a href="/docs/linux/man/1-xsane/">xsane</a></code>(1);<code>it</code>has<code>no</code>other<code>purpose.</code></p>
<dt><code>&#8211;batch[=(yes|no)] [no]</code></p>
<dd>Enable/disable batch mode scanning. Batch mode allows scanning at maximum throughput by buffering within the RSC unit. This option is recommended when performing multiple pages scans until the feeder is emptied.</p>
<dt><code>&#8211;duplex[=(yes|no)] [no]</code></p>
<dd>Enable duplex (dual-sided) scanning. The scanner takes an image of each side of the document during a single pass through the scanner. The front page is delivered followed by the back page. Most options, such as compression, affect both the front and back pages.</p>
<dt><code>&#8211;timeout-adf 0..255 [0]</code></p>
<dd>Sets the timeout in seconds for the automatic document feeder (ADF). The value 0 specifies the hardware default value which varies based on the scanner model.</p>
<dt><code>&#8211;timeout-manual 0..255 [0]</code></p>
<dd>Sets the timeout in seconds for semi-automatic feeder. The value 0 specifies the hardware default value which varies based on the scanner model.</p>
<dt><code>&#8211;check-adf[=(yes|no)] [no]</code></p>
<dd>Check ADF Status prior to starting scan using the OBJECT POSITION command. Note that this feature requires RSC firmware level 1.5 or higher and dip switch 4 must be in the on position. NOTE: This option has not been tested extensively and may produce undesirable results.</p>
<dt><code>Enhancement:</code></p>
<dd>
<dt><code>&#8211;control-panel[=(yes|no)] [yes]</code></p>
<dd>Enables the scanner&#8217;s control panel for selecting image enhancement parameters. When the option is set to no the following options are used to control image enhancement. See the Bell+Howell scanner users&#8217; guide for complete information on ACE functionality.</p>
<dt><code>&#8211;ace-function -4..4 [3]</code></p>
<dd>Specify the Automatic Contrast Enhancement (ACE) Function.</p>
<dt><code>&#8211;ace-sensitivity 0..9 [5]</code></p>
<dd>Specify the Automatic Contrast Enhancement (ACE) Sensitivity.</p>
<dt><code>&#8211;brightness 0..255 [0]</code></p>
<dd>Controls the brightness of the acquired image. Ignored for ACE capable scanners.</p>
<dt><code>&#8211;threshold 0..255 [0]</code></p>
<dd>Select minimum-brightness to get a white point. Ignored for ACE capable scanners.</p>
<dt><code>&#8211;contrast 0..255 [inactive]</code></p>
<dd>Controls the contrast of the acquired image. This option is not currently used by the scanner (and perhaps never will be).</p>
<dt><code>&#8211;negative[=(yes|no)] [no]</code></p>
<dd>Swap black and white, yielding a reverse-video image.</p>
<dt><code>Icon:</code></p>
<dd>
<dt><code>&#8211;icon-width 0..3600pel (in steps of 8) [0]</code></p>
<dd>Width of icon (thumbnail) image in pixels.</p>
<dt><code>&#8211;icon-length 0..3600pel (in steps of 8) [0]</code></p>
<dd>Length of icon (thumbnail) image in pixels.</p>
<dt><code>Barcode Options:</code></p>
<dd>
<dt><code>&#8211;barcode-search-bar &lt;see list&gt; [none]</code></p>
<dd>Specifies the barcode type to search for. If this option is not specified, or specified with a value of none, then the barcode decoding feature is completely disabled. The valid barcode type are: </p>
<dl>
<dd><code>none</code><br />
 <code>ean-8</code><br />
 <code>ean-13</code><br />
 <code>reserved-ean-add</code><br />
 <code>code39</code><br />
 <code>code2-5-interleaved</code><br />
 <code>code2-5-3lines-matrix</code><br />
 <code>code2-5-3lines-datalogic</code><br />
 <code>code2-5-5lines-industrial</code><br />
 <code>patchcode</code><br />
 <code>codabar</code><br />
 <code>codabar-with-start-stop</code><br />
 <code>code39ascii</code><br />
 <code>code128</code><br />
 <code>code2-5-5lines-iata</code>
</dl>
<dt><code>&#8211;barcode-search-count 1..7 [3]</code></p>
<dd>Number of times that the RSC performs the decoding algorithm. Specify the smallest number possible to increase performance. If you are having trouble recognizing barcodes, it is suggested that you increase this option to its maximum value (7).</p>
<dt><code>&#8211;barcode-search-mode &lt;see list&gt; [horiz-vert]</code></p>
<dd>Chooses the orientation of barcodes to be searched. The valid orientations are: </p>
<dl>
<dd><code>horiz-vert</code><br />
 <code>horizontal</code><br />
 <code>vertical</code><br />
 <code>vert-horiz</code></dl>
<dt><code>&#8211;barcode-hmin 0..1660mm [5]</code></p>
<dd>Sets the barcode minimum height in millimeters (larger values increase recognition speed). Of course the actual barcodes in the document must be of sufficient size.</p>
<dt><code>&#8211;barcode-search-timeout 20..65535us [10000]</code></p>
<dd>Sets the timeout for barcode searching in milliseconds. When the timeout expires, the decoder will stop trying to decode barcodes.</p>
<dt><code>&#8211;section &lt;string&gt; []</code></p>
<dd>Specifies a series of image sections. A section can be used to gather a subset image or to provide a small area for barcode decoding. Each section is specified in the following format (units are in millimeters):</dl>
<p> <code>&lt;width&gt;x&lt;height&gt;+&lt;top-left-x&gt;+&lt;top-left-y&gt;[:functioncode&#8230;]</code> </p>
<p> Multiple sections can be specified by separating them with commas. </p>
<p> For example <code>76.2&#215;25.4+50.8+0:frontbar</code> identifies an area 3 inches wide and 1 inch high with a top left corner at the top of the page two inches from the left hand edge of the page. This section will be used for barcode decoding on the front page only. </p>
<p> For example <code>50.8&#215;25.4+25.4+0:frontbar:front:g42d</code> identifies an area 2 inches wide and 1 inch high with a top left corner at the top of the page one inch from the left hand edge of the page. This section will be used for barcode decoding on the front page as well as generating an image compressed in g42d format. </p>
<p> Ordinarily barcodes are searched in the entire image. However, when you specify sections all barcode searching is done within the specific sections identified. This can significantly speed up the decoding process. </p>
<p> The following function codes are available: </p>
<dl>
<dd><code>front</code> &#8211; generate an image for the front page section<br />
 <code>back</code> &#8211; generate an image for the back page section<br />
 <code>frontbar</code> &#8211; perform barcode search in front page section<br />
 <code>backbar</code> &#8211; perform barcode search in back page section<br />
 <code>frontpatch</code> &#8211; perform patchcode search in front page section<br />
 <code>backpatch</code> &#8211; perform patchcode search in back page section<br />
 <code>none</code> &#8211; use no image compression<br />
 <code>g31d</code> &#8211; use Group 3 1 dimension image compression<br />
 <code>g32d</code> &#8211; use Group 3 2 dimensions image compression<br />
 <code>g42d</code> &#8211; use Group 4 2 dimensions image compression
</dl>
<p> If you omit a compression functioncode, the full page compression setting is used. If you specify multiple compression functioncodes, only the last one is used. </p>
<dl>
<dt><code>&#8211;barcode-relmax 0..255 [0]</code></p>
<dd>Specifies the maximum relation from the widest to the smallest bar.</p>
<dt><code>&#8211;barcode-barmin 0..255 [0]</code></p>
<dd>Specifies the minimum number of bars in Bar/Patch code.</p>
<dt><code>&#8211;barcode-barmax 0..255 [0]</code></p>
<dd>Specifies the maximum number of bars in a Bar/Patch code.</p>
<dt><code>&#8211;barcode-contrast 0..6 [3]</code></p>
<dd>Specifies the image contrast used in decoding. Use higher values when there are more white pixels in the code.</p>
<dt><code>&#8211;barcode-patchmode 0..1 [0]</code></p>
<dd>Controls Patch Code detection. </p>
</dl>
<h2>Configuration</h2>
<p>The contents of the <i>bh.conf</i> file is a list of device names that correspond to Bell+Howell scanners. See <code><a href="/docs/linux/man/5-sane-scsi/">sane-scsi</a></code>(5) on details of what constitutes a valid device name. Additionally, options can be specified; these lines begin with the word &quot;option&quot;. Each option is described in detail below. Empty lines and lines starting with a hash mark (#) are ignored.</p>
<h2>Options</h2>
<p>The following options can be specified in the <i>bh.conf</i> file.</p>
<dl>
<dt><code>disable-optional-frames</code></p>
<dd>This option prevents the backend from sending any optional frames. This option may be useful when dealing with frontends which do not support these optional frames. When this option is in effect, the data is sent in a <code>SANE_FRAME_GRAY</code> frame. The optional frames sent by this backend are: <code>SANE_FRAME_G31D</code>, <code>SANE_FRAME_G32D</code>, <code>SANE_FRAME_G42D</code> and <code>SANE_FRAME_TEXT</code>. These frames are generated based on the compression and barcode options. These frames are never sent in preview mode.</p>
<dt><code>fake-inquiry</code></p>
<dd>This option is used for debugging purposes and its use is not encouraged. Essentially, it allows the backend to initialize in the absence of a scanner. This is useful for development and not much else. This option must be specified earlier in the configuration file than the devices which are to be &quot;faked&quot;. </p>
</dl>
<h2>Files</h2>
<dl>
<dt><i>/etc/sane.d/bh.conf</i></p>
<dd>The backend configuration file (see also description of <code>SANE_CONFIG_DIR</code> below).</p>
<dt><i>/usr/lib/x86_64-linux-gnu/sane/libsane-bh.a</i></p>
<dd>The static library implementing this backend.</p>
<dt><i>/usr/lib/x86_64-linux-gnu/sane/libsane-bh.so</i></p>
<dd>The shared library implementing this backend (present on systems that support dynamic loading). </p>
</dl>
<h2>Environment</h2>
<dl>
<dt><code>SANE_CONFIG_DIR</code></p>
<dd>This environment variable specifies the list of directories that may contain the configuration file. On *NIX systems, the directories are separated by a colon (`:&#8217;), under OS/2, they are separated by a semi-colon (`;&#8217;). If this variable is not set, the configuration file is searched in two default directories: first, the current working directory (&quot;.&quot;) and then in <i>/etc/sane.d</i>. If the value of the environment variable ends with the directory separator character, then the default directories are searched after the explicitly specified directories. For example, setting <code>SANE_CONFIG_DIR</code> to &quot;/tmp/config:&quot; would result in directories <i>tmp/config</i>, <i>.</i>, and <i>/etc/sane.d</i> being searched (in this order).</p>
<dt><code>SANE_DEBUG_BH</code></p>
<dd>If the library was compiled with debug support enabled, this environment variable controls the debug level for this backend. E.g., a value of 255 requests all debug output to be printed. Smaller levels reduce verbosity. </p>
</dl>
<h2>Supported Features</h2>
<dl>
<dt><code>ADF support</code></p>
<dd>With document scanners, automatic document feeder (ADF) support is a key feature. The backend supports the ADF by default and returns <code>SANE_STATUS_NO_DOCS</code> when the out-of-paper condition is detected. The SANE frontend <code><a href="/docs/linux/man/1-scanadf/">scanadf</a></code>(1) is a command line frontend that supports multi-page scans. It has been used successfully with this backend. The SANE frontend <code><a href="/docs/linux/man/1-xsane/">xsane</a></code>(1) is an improved GUI frontend by Oliver Rauch. Support for multi-page scans is included in xsane version 0.35 and above. </p>
<dt><code>Duplex scanning</code></p>
<dd>Some models, such as the COPISCAN II 6338, support duplex scanning. That is, they scan both sides of the document during a single pass through the scanner (the scanner has two cameras). This backend supports duplex scanning (with the <code>&#8211;duplex</code> option). The front and back page images are delivered consecutively as if they were separately scanned pages. </p>
<dt><code>Hardware compression</code></p>
<dd>The scanner is capable of compressing the data into several industry standard formats (CCITT G3, CCITT G3-2D, CCITT G4). This results in increased performance as less data is passed from the scanner to the host over the SCSI bus. The backend supports these compression formats via the <code>&#8211;g31d, &#8211;g32d, &#8211;g42d</code> options, respectively. Many SANE frontends are not equipped to deal with these formats, however. The SANE frontend <code><a href="/docs/linux/man/1-scanadf/">scanadf</a></code>(1) supports these optional frame formats. The compressed image data is written directly to a file and can then be processed by a scan-script using the <code>&#8211;scan-script</code> option. Examples of this are given on the <code><a href="/docs/linux/man/1-scanadf/">scanadf</a></code>(1) homepage. </p>
<dt><code>Automatic Border Detection</code></p>
<dd>The scanner can automatically detect the paper size and adjust the scanning window geometry appropriately. The backend supports this useful feature with the <code>&#8211;autoborder</code> option. It is enabled by default. </p>
<dt><code>Batch Mode Scanning</code></p>
<dd>The batch scan mode allows for maximum throughput. The Set Window parameters must remain constant during the entire batch. </p>
<dt><code>Icon Generation</code></p>
<dd>The Icon function generates a thumbnail of the full page image, that can be transferred as if it were a separate page. This allows the host to quickly display a thumbnail representation during the scanning operation. Perhaps this would be a great way of implementing a preview scan, but since a normal scan is so quick, it might not be worth the trouble. </p>
<dt><code>Multiple Sections</code></p>
<dd>Multiple sections (scanning sub-windows) can be defined for the front and back pages. Each section can have different characteristics (e.g. geometry, compression). The sections are returned as if they were separately scanned images. Additionally sections can be used to greatly enhance the accuracy and efficiency of the barcode/patchcode decoding process by limiting the search area to a small subset of the page. Most Copiscan II series scanners support up to 8 user-defined sections. </p>
<dt><code>Support Barcode/Patchcode Decoding</code></p>
<dd>The RSC unit can recognize Bar and Patch Codes of various types embedded in the scanned image. The codes are decoded and the data is returned to the frontend as a text frame. The text is encoded in xml and contains a great deal of information about the decoded data such as the location where it was found, its orientation, and the time it took to find. Further information on the content of this text frame as well as some barcode decoding examples can be found on the backend homepage. </p>
</dl>
<h2>Limitations</h2>
<dl>
<dt><code>Decoding a single barcode type per scan</code></p>
<dd>The RSC unit can search for up to six different barcode types at a time. While the code generally supports this as well, the <code>&#8211;barcode-search-bar</code> option only allows the user to specify a single barcode type. Perhaps another option which allows a comma separated list of barcode type codes could be added to address this.</p>
<dt><code>Scanning a fixed number of pages in batch mode</code></p>
<dd>The separation of front and back end functionality in SANE presents a problem in supporting the &#8216;cancel batch&#8217; functionality in the scanner. In batch mode, the scanner is always a page ahead of the host. The host, knowing ahead of time which page will be the last, can cancel batch mode prior to initiating the last scan command. Currently, there is no mechanism available for the frontend to pass this knowledge to the backend. If batch mode is enabled and the <code>&#8211;end-count</code> terminates a scanadf session, an extra page will be pulled through the scanner, but is neither read nor delivered to the frontend. The issue can be avoided by specifying <code>&#8211;batch=no</code> when scanning a fixed number of pages.</p>
<dt><code>Revision 1.2 Patch detector</code></p>
<dd>There is an enhanced patchcode detection algorithm available in the RSC with revision 1.2 or higher that is faster and more reliable than the standard Bar/Patch code decoder. This is not currently supported. </p>
</dl>
<h2>Bugs</h2>
<p>This is a new backend; detailed bug reports are welcome &#8212; and expected ;) If you have found something that you think is a bug, please attempt to recreate it with the <code>SANE_DEBUG_BH</code> environment variable set to 255, and send a report detailing the conditions surrounding the bug to <i>sane-devel [at] alioth-lists.debian.net</i>. </p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/7-sane/">sane</a></code>(7), <code><a href="/docs/linux/man/5-sane-scsi/">sane-scsi</a></code>(5), <code><a href="/docs/linux/man/1-scanimage/">scanimage</a></code>(1), <code><a href="/docs/linux/man/1-scanadf/">scanadf</a></code>(1), <code><a href="/docs/linux/man/1-xsane/">xsane</a></code>(1) </p>
<h2>Author</h2>
<p>The <code>sane-bh backend</code> was written by Tom Martone, based on the <code><a href="/docs/linux/man/5-sane-ricoh/">sane-ricoh</a></code>(5) backend by Feico W. Dillema and the bnhscan program by Sean Reifschneider of tummy.com ltd. Some 8000 enhancements added by Mark Temple.</p>
