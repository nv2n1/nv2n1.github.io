---
title: "scanadf(1)"
name: "scanadf"
section: "1"
letter: "s"
url: "/docs/linux/man/1-scanadf/"
description: "scanadf – acquire multiple images from a scanner equipped with an ADF"
---

<h2 class="name">NAME</h2>
<p> scanadf &#8211; acquire multiple images from a scanner equipped with an ADF </p>
<h2>SYNOPSIS</h2>
<p> <code>scanadf</code> [<code>-d</code>|<code>&#8211;device-name</code> <i>dev</i>] [<code>-h</code>|<code>&#8211;help</code>] [<code>-L</code>|<code>&#8211;list-devices</code>] [<code>-v</code>|<code>&#8211;verbose</code>] [<code>-V</code>|<code>&#8211;version</code>] [<code>-o</code>|<code>&#8211;output-file</code> <i>name</i>] [<code>-N</code>|<code>&#8211;no-overwrite</code>] [<code>-S</code>|<code>&#8211;scan-script</code> <i>name</i>] [<code>&#8211;script-wait</code>] [<code>-s</code>|<code>&#8211;start-count</code> <i>num</i>] [<code>-e</code>|<code>&#8211;end-count</code> <i>num</i>] [<code>-r</code>|<code>&#8211;raw</code>] [<i>device-specific-options</i>]</p>
<h2>DESCRIPTION</h2>
<p> <code>scanadf</code> is a command-line interface to control image acquisition devices which are capable of returning a series of images (e.g. a scanner with an automatic document feeder (ADF)). The device is controlled via command-line options. After command-line processing, <code>scanadf</code> normally proceeds to acquire a series of images until the device returns the <code>SANE_STATUS_NO_DOCS</code> status code. </p>
<p> The images are written to output files, specified by the <code>&#8211;output-file</code> option. These files are typically written in one of the PNM (portable aNyMaP) formats (PBM for black-and-white images, PGM for grayscale images, and PPM for color images). Several optional frame formats (SANE_FRAME_JPEG, SANE_FRAME_G31D, SANE_FRAME_G32D, SANE_FRAME_G42D, and SANE_FRAME_TEXT) are supported. In each case, the data is written out to the output file as-is without a header. Unrecognized frame formats are handled in the same way, although a warning message is printed in verbose mode. </p>
<p> Typically, the optional frame formats are used in conjunction with a scan script (specified by the <code>&#8211;scanscript</code> option) which is invoked for each acquired image. The script is provided with a series of environment variables which describe the parameters and format of the image file. </p>
<p> <code>scanadf</code> accesses image acquisition devices through the SANE (Scanner Access Now Easy) interface and can thus support any device for which there exists a SANE backend (try &quot;apropos sane-&quot; to get a list of available backends).</p>
<h2>OPTIONS</h2>
<p> The <code>-d</code> or <code>&#8211;device-name</code> options must be followed by a SANE device-name. A (partial) list of available devices can be obtained with the <code>&#8211;list-devices</code> option (see below). If no device-name is specified explicitly, <code>scanadf</code> will attempt to open the first available device. </p>
<p> The <code>-h</code> or <code>&#8211;help</code> options request help information. The information is printed on standard output and in this case, no attempt will be made to acquire an image. </p>
<p> The <code>-L</code> or <code>&#8211;list-devices</code> option requests a (partial) list of devices that are available. The list is not complete since some devices may be available, but are not listed in any of the configuration files (which are typically stored in directory /etc/sane.d). This is particularly the case when accessing scanners through the network. If a device is not listed in a configuration file, the only way to access it is by its full device name. You may need to consult your system administrator to find out the names of such devices. </p>
<p> The <code>-v</code> or <code>&#8211;verbose</code> options increase the verbosity of the operation of <code>scanadf.</code> The option may be specified repeatedly, each time increasing the verbosity level. </p>
<p> The <code>-V</code> or <code>&#8211;version</code> option requests that <code>scanadf</code> print the program and package name, as well as the version number of the SANE distribution that it came with. </p>
<p> The <code>-o</code> or <code>&#8211;output-file</code> option specifies a format string used to generate the name of file to write the image data to. You can use %d replacement in the output file name; this will be replaced with the current page number. The default format string is image-%04d. </p>
<p> The <code>-N</code> or <code>&#8211;no-overwrite</code> option prevents <code>scanadf </code> from overwriting existing image files. </p>
<p> The <code>-S</code> or <code>&#8211;scan-script</code> option specifies the name of script to run after each scanned image is acquired. The script receives the name of the image output file as its first and only command line argument. Additionally the scan script can reference the following environment variables to get information about the parameters of the image. </p>
<dl>
<dt>
<dd> <code>SCAN_RES</code> &#8211; the image resolution (in DPI)<br />
 <code>SCAN_WIDTH</code> &#8211; the image width (in pixels)<br />
 <code>SCAN_HEIGHT</code> &#8211; the image height (in pixels)<br />
 <code>SCAN_DEPTH</code> &#8211; the image bit-depth (in bits)<br />
 <code>SCAN_FORMAT</code> &#8211; a string representing the image format (e.g. gray, g42d, text, etc)<br />
 <code>SCAN_FORMAT_ID</code> &#8211; the numeric image format identifier
</dl>
<p> If the <code>&#8211;scipt-wait</code> option is given, scanadf will wait until all scan-scripts have been finished before exiting. That will be useful if scanadf is used in conjunction with tools to modify the scanned images. </p>
<p> The <code>-s</code> or <code>&#8211;start-count</code> option specifies the page number of first scanned image. </p>
<p> The <code>-e</code> or <code>&#8211;end-count</code> option specifies the last page number to scan. Using this option, you can request a specific number of pages to be scanned, rather than scanning until there are no more images available. </p>
<p> The <code>-r</code> or <code>&#8211;raw</code> option specifies that the raw image data be written to the output file as-is without interpretation. This disables the writing of the PNM header for basic frame types. This feature is usually used in conjunction with the <code>&#8211;scan-script</code> option where the scan script uses the environment variables to understand the format and parameters of the image and converts the file to a more useful format. NOTE: With support for the optional frame types and the default handling of unrecognized frametypes, this option becomes less and less useful. </p>
<p> As you might imagine, much of the power of <code>scanadf</code> comes from the fact that it can control any SANE backend. Thus, the exact set of command-line options depends on the capabilities of the selected device. To see the options for a device named <i>dev</i>, invoke <code>scanadf</code> via a command-line of the form: </p>
<dl>
<dt>
<dd> scanadf &#8211;help &#8211;device <i>dev</i></dl>
<p> The documentation for the device-specific options printed by <code>&#8211;help</code> is explained in the manual page for <code>scanimage.</code> </p>
<h2>FILES</h2>
<dl>
<dt><i>/etc/sane.d</i></p>
<dd> This directory holds various configuration files. For details, please refer to the manual pages listed below.</dl>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-scanimage/">scanimage</a>(1), <a href="/docs/linux/man/1-xscanimage/">xscanimage</a>(1), <a href="/docs/linux/man/7-sane/">sane</a>(7) </p>
<h2>AUTHOR</h2>
<p> scanadf is an adaptation by Tom Martone of scanimage by David Mosberger, Andreas Beck, and Gordon Matzigkeit following closely the features of bnhscan by Sean Reifschneider of tummy.com, ltd. </p>
<h2>BUGS</h2>
<p> Please send reports to <i>sane-devel [at] lists.alioth.debian.org</i>. </p>
<p> This program relies on the backend to return the <code>SANE_STATUS_NO_DOCS</code> status code when the automatic document feeder is out of paper. Use of this program with backends that do not support ADFs (e.g. flatbed scanners) will likely result in repeated scans of the same document. In this case, it is essential to use the start-count and end-count to control the number of images acquired. </p>
<p> Only a subset of the SANE backends support feeders and return SANE_STATUS_NO_DOCS appropriately. Backends which are known to work at this time are: </p>
<dl>
<dt>
<dd>
 <code>sane-bh</code> &#8211; Bell+Howell Copiscan II series scanners.<br />
 <code>sane-hp</code> &#8211; Hewlett Packard scanners. A patch to the sane-hp backend is necessary. The &#8211;scantype=ADF option must be specified (earlier versions of the backend used the &#8211;scan-from-adf option, instead).<br />
 <code>sane-umax</code> &#8211; UMAX scanners. Support exists in build 12 and later. The &#8211;source=&quot;Automatic Document Feeder&quot; option must be specified.
</dl>
<h2>Index</h2>
