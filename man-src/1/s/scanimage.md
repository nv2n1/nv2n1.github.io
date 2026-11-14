---
title: "scanimage(1)"
name: "scanimage"
section: "1"
letter: "s"
url: "/docs/linux/man/1-scanimage/"
description: "scanimage – scan an image"
---

<h2 class="name">NAME</h2>
<p> scanimage &#8211; scan an image </p>
<h2>SYNOPSIS</h2>
<p> <code>scanimage</code> [<code>-d</code>|<code>&#8211;device-name</code> <i>dev</i>] [<code>&#8211;format</code> <i>format</i>] [<code>-i</code>|<code>&#8211;icc-profile</code> <i>profile</i>] [<code>-L</code>|<code>&#8211;list-devices</code>] [<code>-f</code>|<code>&#8211;formatted-device-list</code> <i>format</i>] [<code>-b</code>|<code>&#8211;batch</code> [<i>format</i>]] [<code>&#8211;batch-start</code> <i>start</i>] [<code>&#8211;batch-count</code> <i>count</i>] [<code>&#8211;batch-increment</code> <i>increment</i>] [<code>&#8211;batch-double</code>] [<code>&#8211;accept-md5-only</code>] [<code>-p</code>|<code>&#8211;progress</code>] [<code>-o</code>|<code>&#8211;output-file</code> <i>path</i>] [<code>-n</code>|<code>&#8211;dont-scan</code>] [<code>-T</code>|<code>&#8211;test</code>] [<code>-A</code>|<code>&#8211;all-options</code>] [<code>-h</code>|<code>&#8211;help</code>] [<code>-v</code>|<code>&#8211;verbose</code>] [<code>-B</code>|<code>&#8211;buffer-size</code> [=<i>size</i>]] [<code>-V</code>|<code>&#8211;version</code>] [<i>device-specific-options</i>]</p>
<h2>DESCRIPTION</h2>
<p> <code>scanimage</code> is a command-line interface to control image acquisition devices such as flatbed scanners or cameras. The device is controlled via command-line options. After command-line processing, <code>scanimage</code> normally proceeds to acquire an image. The image data is written to standard output in one of the PNM (portable aNyMaP) formats (PBM for black-and-white images, PGM for grayscale images, and PPM for color images), TIFF format (black-and-white, grayscale or color), PNG format, or JPEG format (compression level 75). <code>scanimage</code> accesses image acquisition devices through the <code>SANE</code> (Scanner Access Now Easy) interface and can thus support any device for which there exists a <code>SANE</code> backend (try <code>apropos</code> <i>sane-</i> to get a list of available backends). </p>
<h2>EXAMPLES</h2>
<p> To get a list of devices: </p>
<p>&nbsp;<wbr>&nbsp;scanimage -L </p>
<p> To scan with default settings to the file image.pnm: </p>
<p>&nbsp;<wbr>&nbsp;scanimage&nbsp;&gt;image.pnm </p>
<p> To scan 100&#215;100 mm to the file image.tiff (-x and -y may not be available with all devices): </p>
<p>&nbsp;<wbr>&nbsp;scanimage -x 100 -y 100 &#8211;format=tiff&nbsp;&gt;image.tiff </p>
<p> To print all available options: </p>
<p>&nbsp;<wbr>&nbsp;scanimage -h </p>
<h2>OPTIONS</h2>
<p> There are two sets of options available when running <code>scanimage</code>. </p>
<p> The options that are provided by <code>scanimage</code> itself are listed below. In addition, each backend offers its own set of options and these can also be specified. Note that the options available from the backend may vary depending on the scanning device that is selected. </p>
<p> Often options that are similar in function may be implemented differently across backends. An example of this difference is <i>&#8211;mode Gray</i> and <i>&#8211;mode Grayscale</i>. This may be due to differing backend author preferences. At other times, options are defined by the scanning device itself and therefore out of the control of the backend code. </p>
<p> Parameters are separated by a blank from single-character options (e.g. <code>-d </code><i>epson</i><code>)</code> and by a &quot;=&quot; from multi-character options (e.g. <code>&#8211;device-name</code>=<i>epsonFR</i><code>).</code> </p>
<dl>
<dt><code>-d</code><i> dev</i>, <code>&#8211;device-name</code>=<i>dev</i></p>
<dd> specifies the device to access and must be followed by a SANE device-name like `<i>epson:/dev/sg0</i>&#8216; or `<i>hp:/dev/usbscanner0</i>&#8216;. A (partial) list of available devices can be obtained with the <code>&#8211;list-devices</code> option (see below). If no device-name is specified explicitly, <code>scanimage</code> reads a device-name from the environment variable <code>SANE_DEFAULT_DEVICE</code>. If this variable is not set, <code>scanimage</code> will attempt to open the first available device. </p>
<dt><code>&#8211;format</code>=<i>format</i></p>
<dd> selects how image data is written to standard output or the file specified by the <code>&#8211;output-file</code> option. <i>format</i> can be <code>pnm</code>, <code>tiff</code>, <code>png</code>, or <code>jpeg</code>. If <code>&#8211;format</code> is not specified, PNM is written by default. </p>
<dt><code>-i</code><i> profile</i>, <code>&#8211;icc-profile</code>=<i>profile</i></p>
<dd> is used to include an ICC profile into a TIFF file. </p>
<dt><code>-L</code>, <code>&#8211;list-devices</code></p>
<dd> requests a (partial) list of devices that are available. The list may not be complete since some devices may be available, but are not listed in any of the configuration files (which are typically stored in directory <i>/etc/sane.d</i>). This is particularly the case when accessing scanners through the network. If a device is not listed in a configuration file, the only way to access it is by its full device name. You may need to consult your system administrator to find out the names of such devices. </p>
<dt><code>-f</code><i> format</i>, <code>&#8211;formatted-device-list</code>=<i>format</i></p>
<dd> works similar to <code>&#8211;list-devices</code>, but requires a format string. <code>scanimage</code> replaces the placeholders <code>%d %v %m %t %i %n</code> with the device name, vendor name, model name, scanner type, an index number and newline respectively. The command</dl>
<dl>
<dt>
<dd> <code>scanimage -f</code> <i>&#8220; scanner number %i device %d is a %t, model %m, produced by %v &#8221;</i> </p>
<p> will produce something like: </p>
<dl>
<dt>
<dd> scanner number 0 device sharp:/dev/sg1 is a flatbed scanner, model JX250 SCSI, produced by SHARP</dl>
</dl>
<p> The <code>&#8211;batch*</code> options provide features for scanning documents using document feeders. </p>
<dl>
<dt>
<dd>
<dl>
<dt><code>-b</code> [<i>format</i>], <code>&#8211;batch</code>=[<i>format</i>]</p>
<dd> is used to specify the format of the filename that each page will be written to. Each page is written out to a single file. If <i>format</i> is not specified, the default of <i>out%d.pnm</i> (or <i>out%d.tif</i> for <code>&#8211;format tiff</code>, <i>out%d.png</i> for <code>&#8211;format png</code> or <i>out%d.jpg</i> for <code>&#8211;format jpeg</code>) will be used. This option is incompatible with the <code>&#8211;output-path</code> option. <i>format</i> is given as a printf style string with one integer parameter. </p>
<dt><code>&#8211;batch-start</code>=<i>start</i></p>
<dd> selects the page number to start naming files with. If this option is not given, the counter will start at 1. </p>
<dt><code>&#8211;batch-count</code>=<i>count</i></p>
<dd> specifies the number of pages to attempt to scan. If not given, <code>scanimage</code> will continue scanning until the scanner returns a state other than OK. Not all scanners with document feeders signal when the ADF is empty. Use this option to work around them. </p>
<dt><code>&#8211;batch-increment</code>=<i>increment</i></p>
<dd> sets the amount that the number in the filename is incremented by. Generally this is used when you are scanning double-sided documents on a single-sided document feeder. <code>&#8211;batch-double</code> is a specific command provided to aid this. </p>
<dt><code>&#8211;batch-double</code></p>
<dd> will automatically set the increment to 2. Equivalent to <code>&#8211;batch-increment</code>=2 </p>
<dt><code>&#8211;batch-prompt</code></p>
<dd> will ask for pressing RETURN before scanning a page. This can be used for scanning multiple pages without an automatic document feeder.</dl>
</dl>
<dl>
<dt><code>&#8211;accept-md5-only</code></p>
<dd> only accepts user authorization requests that support MD5 security. The <code>SANE</code> network daemon <code><a href="/docs/linux/man/8-saned/">saned</a></code>(8) is capable of doing such requests. </p>
<dt><code>-p</code>, <code>&#8211;progress</code></p>
<dd> requests that <code>scanimage</code> prints a progress counter. It shows how much image data of the current image has already been received (in percent). </p>
<dt><code>-o</code><i> path</i>, <code>&#8211;output-file</code>=<i>path</i></p>
<dd> requests that <code>scanimage</code> saves the scanning output to the given <i>path</i>. This option is incompatible with the <code>&#8211;batch</code> option. The program will try to guess <code>&#8211;format</code> from the file name. If that is not possible, it will print an error message and exit. </p>
<dt><code>-n</code>, <code>&#8211;dont-scan</code></p>
<dd> requests that <code>scanimage</code> only sets the options provided by the user but doesn&#8217;t actually perform a scan. This option can be used to e.g. turn off the scanner&#8217;s lamp (if supported by the backend). </p>
<dt><code>-T</code>, <code>&#8211;test</code></p>
<dd> requests that <code>scanimage</code> performs a few simple sanity tests to make sure the backend works as defined by the <code>SANE</code> API. In particular the <code>sane_read</code>() function is exercised by this test. </p>
<dt><code>-A</code>, <code>&#8211;all-options</code></p>
<dd> requests that <code>scanimage</code> lists all available options exposed by the backend, including button options. The information is printed on standard output and no scan will be performed. </p>
<dt><code>-h</code>, <code>&#8211;help</code></p>
<dd> requests help information. The information is printed on standard output and no scan will be performed. </p>
<dt><code>-v</code>, <code>&#8211;verbose</code></p>
<dd> increases the verbosity of the output of <code>scanimage.</code> The option may be specified repeatedly, each time increasing the verbosity level. </p>
<dt><code>-B</code> [<i>size</i>], <code>&#8211;buffer-size</code>=[<i>size</i>]</p>
<dd> changes input buffer size from the default of 32KB to <i>size</i> KB. If <i>size</i> is not specified then the buffer is set to 1 MB. </p>
<dt><code>-V</code>, <code>&#8211;version</code></p>
<dd> requests that <code>scanimage</code> prints the program and package name, the version number of the <code>SANE</code> distribution that it came with and the version of the backend that it loads. If more information about the version numbers of the backends are necessary, the <code>DEBUG</code> variable for the dll layer can be used. Example: <i>SANE_DEBUG_DLL=3 scanimage -L .</i></dl>
<p> As you might imagine, much of the power of <code>scanimage</code> comes from the fact that it can control any <code>SANE</code> backend. Thus, the exact set of command-line options depends on the capabilities of the selected device. To see the options for a device named <i>dev</i>, invoke <code>scanimage</code> via a command-line of the form: </p>
<dl>
<dt>
<dd> scanimage &#8211;help &#8211;device-name <i>dev</i></dl>
<p> The documentation for the device-specific options printed by <code>&#8211;help</code> is best explained with a few examples: </p>
<p> <code>-l 0..218mm [0]</code></p>
<dl>
<dt>
<dd> Top-left x position of scan area. </p>
<p> The description above shows that option <code>-l</code> expects an option value in the range from 0 to 218 mm. The value in square brackets indicates that the current option value is 0 mm. Most backends provide similar geometry options for top-left y position (<code>-t</code>), width (<code>-x</code>) and height of scan-area (-y<code>).</code></dl>
<p> <code>&#8211;brightness -100..100% [0]</code></p>
<dl>
<dt>
<dd> Controls the brightness of the acquired image. </p>
<p> The description above shows that option <code>&#8211;brightness</code> expects an option value in the range from -100 to 100 percent. The value in square brackets indicates that the current option value is 0 percent.</dl>
<p> <code>&#8211;default-enhancements</code></p>
<dl>
<dt>
<dd> Set default values for enhancement controls. </p>
<p> The description above shows that option <code>&#8211;default-enhancements</code> has no option value. It should be thought of as having an immediate effect at the point of the command-line at which it appears. For example, since this option resets the <code>&#8211;brightness</code> option, the option-pair <code>&#8211;brightness 50 &#8211;default-enhancements</code> would effectively be a no-op.</dl>
<p> <code>&#8211;mode Lineart|Gray|Color [Gray]</code></p>
<dl>
<dt>
<dd> Selects the scan mode (e.g., lineart or color). </p>
<p> The description above shows that option <code>&#8211;mode</code> accepts an argument that must be one of the strings <code>Lineart</code>, <code>Gray</code>, or <code>Color</code>. The value in the square bracket indicates that the option is currently set to <code>Gray</code>. For convenience, it is legal to abbreviate the string values as long as they remain unique. Also, the case of the spelling doesn&#8217;t matter. For example, option setting <code>&#8211;mode col</code> is identical to <code>&#8211;mode Color</code>.</dl>
<p> <code>&#8211;custom-gamma[=(yes|no)] [inactive]</code></p>
<dl>
<dt>
<dd> Determines whether a builtin or a custom gamma-table should be used. </p>
<p> The description above shows that option <code>&#8211;custom-gamma</code> expects either no option value, a &quot;yes&quot; string, or a &quot;no&quot; string. Specifying the option with no value is equivalent to specifying &quot;yes&quot;. The value in square-brackets indicates that the option is not currently active. That is, attempting to set the option would result in an error message. The set of available options typically depends on the settings of other options. For example, the <code>&#8211;custom-gamma</code> table might be active only when a grayscale or color scan-mode has been requested. </p>
<p> Note that the <code>&#8211;help</code> option is processed only after all other options have been processed. This makes it possible to see the option settings for a particular mode by specifying the appropriate mode-options along with the <code>&#8211;help</code> option. For example, the command-line: </p>
<p> <code>scanimage &#8211;help &#8211;mode</code> <i>color</i> </p>
<p> would print the option settings that are in effect when the color-mode is selected.</dl>
<p> <code>&#8211;gamma-table 0..255,&#8230;</code></p>
<dl>
<dt>
<dd> Gamma-correction table. In color mode this option equally affects the red, green, and blue channels simultaneously (i.e., it is an intensity gamma table). </p>
<p> The description above shows that option <code>&#8211;gamma-table</code> expects zero or more values in the range 0 to 255. For example, a legal value for this option would be &quot;3,4,5,6,7,8,9,10,11,12&quot;. Since it&#8217;s cumbersome to specify long vectors in this form, the same can be expressed by the abbreviated form &quot;[0]3-[9]12&quot;. What this means is that the first vector element is set to 3, the 9-th element is set to 12 and the values in between are interpolated linearly. Of course, it is possible to specify multiple such linear segments. For example, &quot;[0]3-[2]3-[6]7,[7]10-[9]6&quot; is equivalent to &quot;3,3,3,4,5,6,7,10,8,6&quot;. The program <code>gamma4scanimage</code> can be used to generate such gamma tables (see <code><a href="/docs/linux/man/1-gamma4scanimage/">gamma4scanimage</a></code>(1) for details).</dl>
<p> <code>&#8211;filename &lt;string&gt; [/tmp/input.ppm]</code></p>
<dl>
<dt>
<dd> The filename of the image to be loaded. </p>
<p> The description above is an example of an option that takes an arbitrary string value (which happens to be a filename). Again, the value in brackets show that the option is current set to the filename <i>/tmp/input.ppm</i>.</dl>
<h2>ENVIRONMENT</h2>
<dl>
<dt><code>SANE_DEFAULT_DEVICE</code></p>
<dd> The default device-name.</dl>
<h2>FILES</h2>
<dl>
<dt><i>/etc/sane.d</i></p>
<dd> This directory holds various configuration files. For details, please refer to the manual pages listed below.</p>
<dt><i>~/.sane/pass</i></p>
<dd> This file contains lines of the form</dl>
<dl>
<dt>
<dd> user:password:resource </p>
<p> <code>scanimage</code> uses this information to answer user authorization requests automatically. The file must have 0600 permissions or stricter. You should use this file in conjunction with the <code>&#8211;accept-md5-only</code> option to avoid server-side attacks. The resource may contain any character but is limited to 127 characters. </p>
</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/7-sane/">sane</a></code>(7), <code><a href="/docs/linux/man/1-gamma4scanimage/">gamma4scanimage</a></code>(1), <code><a href="/docs/linux/man/1-xscanimage/">xscanimage</a></code>(1), <code><a href="/docs/linux/man/1-xcam/">xcam</a></code>(1)<code>,</code> <code><a href="/docs/linux/man/1-xsane/">xsane</a></code>(1)<code>,</code> <code><a href="/docs/linux/man/1-scanadf/">scanadf</a></code>(1), <code><a href="/docs/linux/man/5-sane-dll/">sane-dll</a></code>(5), <code><a href="/docs/linux/man/5-sane-net/">sane-net</a></code>(5), <code><a href="/docs/linux/man/5-sane-backendname/">sane-backendname</a></code>(5) </p>
<h2>AUTHOR</h2>
<p> David Mosberger, Andreas Beck, Gordon Matzigkeit, Caskey Dickson, and many others. For questions and comments contact the sane-devel mailinglist (see <i><a rel="nofollow" href="http://www.sane-project.org/mailing-lists.html">http://www.sane-project.org/mailing-lists.html</a></i>). </p>
<h2>BUGS</h2>
<p> For vector options, the help output currently has no indication as to how many elements a vector-value should have. </p>
<h2>Index</h2>
