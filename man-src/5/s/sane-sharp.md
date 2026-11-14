---
title: "sane-sharp(5)"
name: "sane-sharp"
section: "5"
letter: "s"
url: "/docs/linux/man/5-sane-sharp/"
description: "sane-sharp – SANE backend for SHARP scanners"
---

<p>sane-sharp &#8211; SANE backend for SHARP scanners</p>
<h2>Description</h2>
<p>The <code>sane-sharp</code> library implements a SANE (Scanner Access Now Easy) backend that provides access to Sharp SCSI scanners. This backend should be considered <code>beta-quality</code> software! In the current state it is known to work with JX-610 and JX-250 scanners. It is prepared for usage with the JX-330 series scanners, but we are not able to test it with these devices. </p>
<p> For other Sharp scanners, it may or may not work. </p>
<p> At present, the following scanners are known to work with this backend.</p>
<dl>
<dd>
<pre>Vendor Product id:
----- -----------
Sharp JX-610
Sharp JX-250
Sharp JX-320
Sharp JX-330
Sharp JX-350</pre>
</dl>
<p> The following scanners are detected by the backend, but not tested: </p>
<dl>
<dd>
<pre>Vendor Product id:
----- -----------
Sharp JX-325</pre>
</dl>
<h2>Device Names</h2>
<p>This backend expects device names of the form: </p>
<dl>
<dd><i>special</i></dl>
<p> where <i>special</i> is the path-name for the special device that corresponds to a SCSI scanner. The special device name must be a generic SCSI device or a symlink to such a device. Under Linux, such a device name could be <i>/dev/sga</i> or <i>/dev/sge</i>, for example. See <code><a href="/docs/linux/man/5-sane-scsi/">sane-scsi</a></code>(5) for details.</p>
<h2>Scan Options</h2>
<dl>
<dt><code>&#8211;mode</code></p>
<dd>Scan Mode. Possible settings are: <i>Lineart</i> (1 bit black &amp; white scans), <i>Gray</i> (8 bit gray scale scans), <i>Lineart Color</i> (bi-level color scans), and <i>Color</i> (8 bit RGB scans). The default value is <i>Color.</i> </p>
<dt><code>&#8211;halftone-pattern</code></p>
<dd>Halftone Pattern. Available only for the JX-330 series scanners. Possible settings: <i>none</i>, <i>Dither Bayer</i>, <i>Dither Spiral</i>, <i>Dither Dispersed</i> and <i>Error Diffusion</i>. The default value is <i>none</i>. </p>
<dt><code>&#8211;source</code></p>
<dd>Paper Source. This option is only available if an automatic document feeder or a transparency adapter is installed. Possible settings are: <i>Flatbed</i>, <i>Automatic Document Feeder</i>, and <i>Transparency Adapter</i>. If an ADF or a transparency adapter is installed, using it is the default selection. </p>
<dt><code>&#8211;custom-gamma</code></p>
<dd>Custom Gamma This option determines whether a builtin or a custom gamma table is used. Possible settings are: <i>yes</i> (enables custom gamma tables) or <i>no</i> (enables a built gamma table). </p>
<dt><code>&#8211;gamma</code></p>
<dd>Gamma. This option is only available if <code>Custom Gamma</code> is set to <i>no</i>. Possible values are: <i>1.0</i> or <i>2.2</i>. The default value is <i>2.2</i>. (The JX-250 and JX-350 have no built in gamma correction; for these scanners, a gamma table is downloaded to the scanner by the backend.) </p>
<dt><code>&#8211;gamma-table</code></p>
<dd>Gamma Table. Allowed values: 0..255; 256 numbers must be defined. The default values are 0, 1, 2, .. 255 (i.e., gamma == 1). This table is only used for gray scale scans. </p>
<dt><code>&#8211;red-gamma-table</code></p>
<dd>Red Gamma Table. Allowed values: 0..255; 256 numbers must be defined. The default values are 0, 1, 2, .. 255 (i.e., gamma == 1). </p>
<dt><code>&#8211;green-gamma-table</code></p>
<dd>Green Gamma Table. Allowed values: 0..255; 256 numbers must be defined. The default values are 0, 1, 2, .. 255 (i.e., gamma == 1). </p>
<dt><code>&#8211;blue-gamma-table</code></p>
<dd>Blue Gamma Table. Allowed values: 0..255; 256 numbers must be defined. The default values are 0, 1, 2, .. 255 (i.e., gamma == 1). </p>
<dt><code>&#8211;resolution</code></p>
<dd>Selects the resolution of the scanned image. Allowed values: <i>30..600</i> (JX-330, JX-350 and JX-610) and <i>30..400</i> (JX-250). The default value is 150. </p>
<dt><code>-l</code>, <code>-t</code>, <code>-x</code>, <code>-y</code></p>
<dd>Scan Window. Top-left x position of scan area (<code>-l</code>), top-left y position of scan area (<code>-t</code>), bottom right x position of scan area (<code>-x</code>) and bottom right y position of scan area (<code>-y</code>). The possible settings depend on the scanner model and, for the JX-250 and the JX-350, also on the usage of the automatic document feeder resp. the transparency adapter. Please refer to the values allowed by <code><a href="/docs/linux/man/1-xscanimage/">xscanimage</a></code>(1), or <code><a href="/docs/linux/man/1-xsane/">xsane</a></code>(1). With <code><a href="/docs/linux/man/1-scanimage/">scanimage</a></code>(1), enter one of the following commands in order to see the allowed parameter values for the scan window: </p>
<dl>
<dd>scanimage -d sharp &#8211;source &quot;Automatic Document Feeder&quot; &#8211;help </p>
<p> scanimage -d sharp &#8211;source Flatbed &#8211;help </p>
<p> scanimage -d sharp &#8211;source &quot;Transparency Adapter&quot; &#8211;help</dl>
<dt><code>&#8211;edge emphasis</code></p>
<dd>Edge emphasis. This option is not available for the JX-250 and the JX-350. Possible settings: <i>None</i>, <i>Middle</i>, <i>Strong</i>, and <i>Blur</i>. The default value is <i>None</i>. </p>
<dt><code>&#8211;threshold</code></p>
<dd>Sets the threshold for black and white pixels in lineart mode. Possible values are 1..255. The default value is 128. This option is only available in scan mode <i>lineart</i>. </p>
<dt><code>&#8211;threshold-red</code></p>
<dd>Sets the threshold for the red component of a pixel in in lineart color scan mode. Possible values are 1..255. The default value is 128. This option is only available in scan mode color <i>lineart</i>. </p>
<dt><code>&#8211;threshold-green</code></p>
<dd>Sets the threshold for the green component of a pixel in in lineart color scan mode. Possible values are 1..255. The default value is 128. This option is only available in scan mode color <i>lineart .</i> </p>
<dt><code>&#8211;threshold-blue</code></p>
<dd>Sets the threshold for the blue component of a pixel in in lineart color scan mode. Possible values are 1..255. The default value is 128. This option is only available in scan mode color <i>lineart</i>. </p>
<dt><code>&#8211;lightcolor</code></p>
<dd>Sets the color of the light source. Possible values are <i>white</i>, <i>red</i>, <i>green</i> and <i>blue</i>. The default value is <i>white</i>. This option is only available in scan modes <i>lineart color</i> and <i>color</i>. </p>
</dl>
<h2>Adf Usage</h2>
<p>If a paper jam occurrs, the maintenance cover <i>must</i> be opened and closed, even if the jammed paper can be removed without opening the maintenance cover. Otherwise, the error condition will not be cleared.</p>
<h2>Configuration</h2>
<p>The contents of the <i>sharp.conf</i> file is a list of options and device names that correspond to Sharp scanners. Empty lines and lines beginning with a hash mark (#) are ignored. See <code><a href="/docs/linux/man/5-sane-scsi/">sane-scsi</a></code>(5) for details about device names. </p>
<p> Lines setting an option start with the key word <code>option,</code> followed by the option&#8217;s name and the option&#8217;s value. At present, three options are defined: <code>buffers, buffersize,</code> and <code>readqueue.</code> </p>
<p> Options defined at the start of <i>sharp.conf</i> apply to all devices; options defined after a device name apply to this device. </p>
<p> The options <code>buffers</code> and <code>readqueue</code> are only significant if the backend has been compiled so that for each scan a second process is forked (switch <code>USE_FORK</code> in <i>sharp.c</i> ). This process reads the scan data from the scanner and writes this data into a block of shared memory. The parent process reads the data from this memory block and delivers it to the frontend. The options control the size and usage of this shared memory block. </p>
<p> <code>option buffers</code> defines the number of buffers used. The smallest number allowed is 2. </p>
<p> <code>option buffersize</code> defines the size of one buffer. Since each buffer is filled with a single read command sent to the scanner, its size is limited automatically to the size allowed by the operating system or by the Sane SCSI library for SCSI read commands. A buffer size of 128 kB or 256 kB is recommended for scan resolutions of 300 dpi and above. </p>
<p> <code>option readqueue</code> defines how many read commands to be sent to the scanner are queued. At present, the Sane SCSI library supports queued read commands only for for Linux. For other operating systems, <code>option readqueue</code> should be set to 0. For Linux, <code>option readqueue</code> should be set to 2. Larger values than 2 for <code>option readqueue</code> are not reasonable in most cases. <code>option buffers</code> should be greater than <code>option readqueue.</code></p>
<h2>Performance Considerations</h2>
<p>This section focuses on the problem of stops of the scanner&#8217;s carriage during a scan. Carriage stops happen mainly with the JX-250. This scanner has obviously only a small internal buffer compared to its speed. That means that the backend must read the data as fast as possible from the scanner in order to avoid carriage stops. </p>
<p> Even the JX-250 needs only less than 10 seconds for a 400 dpi A4 gray scale scan, which results in a data transfer rate of more than 1.6 MB per second. This means that the data produced by the scanner must be processed fairly fast. Due to the small internal buffer of the JX-250, the backend must issue a read request for the next data block as soon as possible after reading a block of data in order to avoid carriage stops. </p>
<p> Stops of the carriage can be caused by the following reasons: </p>
<dl>
<dd>&#8211; too much &quot;traffic&quot; on the SCSI bus<br />
 &#8211; slow responses by the backend to the scanner,<br />
 &#8211; a program which processes the data acquired by the backend too slow. </p>
</dl>
<p> Too much &quot;traffic&quot; on the SCSI bus: This happens for example, if hard disks are connected to the same SCSI bus as the scanner, and when data transfer from/to these hard disks requires a considerable part of the SCSI bandwidth during a scan. If this is the case, you should consider to connect the scanner to a separate SCSI adapter. </p>
<p> Slow responses by the backend to the scanner: Unfortunately, UNIX-like operating systems generally have no real time capabilities. Thus there is no guarantee that the backend is under any circumstances able to communicate with the scanner as fast as required. To minimize this problem, the backend should be compiled so that a separate reader process is forked: Make sure that <code>USE_FORK</code> is defined when you compile <i>sharp.c.</i> If slow responses of the backend remain to be problem, you could try to reduce the load of the system. Even while the backend and the reader process need only a minor amount of processor time, other running processes can cause an increase in the time delay between two time slices given to the reader process. On slower systems, such an increased delay can be enough to cause a carriage stop with the JX-250. For Linux, the usage of the SG driver version 2.1.36 or above is recommended, because it supports, in combination with the SCSI library of Sane version 1.0.2, command queueing within the kernel. This queueing implementation, combined with a buffer size of at least 128 kB, should avoid most carriage stops. </p>
<p> Slow processing of the scan data: An example for this situation is the access to the scanner via a 10 MBit Ethernet, which is definitely too slow to transfer the scan data as fast as they are produced by the scanner. If you have enough memory available, you can increase <code>option buffers,</code> so that an entire image can be stored in these buffers. </p>
<p> In order to see, if the backend is too slow or if the further processing of the data is too slow, set the environment variable <code>SANE_DEBUG_SHARP</code> to 1. When a scan is finished, the backend writes the line &quot;buffer full conditions: <i>nn</i>&quot; to stderr. If <i>nn</i> is zero, carriage stops are caused by too slow responses of the backend or too much &quot;traffic&quot; on the SCSI bus. If <i>nn</i> is greater than zero, the backend had to wait <i>nn</i> times until a buffer has been processed by the frontend. (Please note that <code>option buffers</code> must be greater than <code>option readqueue</code> in order to get useful output for &quot;buffer full conditions&quot;.)</p>
<h2>Files</h2>
<dl>
<dt><i>/etc/sane.d/sharp.conf</i></p>
<dd>The backend configuration file.</p>
<dt><i>/usr/lib/x86_64-linux-gnu/sane/libsane-sharp.a</i></p>
<dd>The static library implementing this backend.</p>
<dt><i>/usr/lib/x86_64-linux-gnu/sane/libsane-sharp.so</i></p>
<dd>The shared library implementing this backend (present on systems that support dynamic loading).</dl>
<h2>Environment</h2>
<dl>
<dt><code>SANE_DEBUG_SHARP</code></p>
<dd>If the library was compiled with debug support enabled, this environment variable controls the debug level for this backend. E.g., a value of 128 requests all debug output to be printed. Smaller levels reduce verbosity.</dl>
<h2>Known Problems</h2>
<p>1. ADF Mode</p>
<dl>
<dd>After several ADF scans, the scanner moves the carriage back to the idle position and back to ADF scan position, before a scan starts. We do not know, if this is a problem of the scanner, or if this is a bug of the backend. At present, the scanner must power off and on to stop this annoying behaviour.</dl>
<p> 2. Threshold level does not work (only JX-610) </p>
<p> 3. The maximum resolution is limited to 600 dpi(JX-610 supported to 1200 dpi) resp. 400 dpi (JX-250) </p>
<p> 4. If the JX250 is used with an ADF, the following situation can occur: After several scans, the scanner moves, after loading a new sheet of paper, the carriage to the idle position, and then back to the position used for ADF scans. This happens for <i>every</i> scan, in contrast to the calibration, which is done after 10 scans. (For the calibration, the carriage is also moved to the idle position.) We do not know if this behavior is caused by the backend, or if it is a bug in the firmware of the scanner. </p>
<p> 5. Usage of a transparency adapter (film scan unit) is supported, but not tested.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/7-sane/">sane</a></code>(7), <code><a href="/docs/linux/man/5-sane-scsi/">sane-scsi</a></code>(5) </p>
<h2>Authors</h2>
<p>Kazuya Fukuda, Abel Deuring</p>
<h2>Credits</h2>
<p>The Sharp backend is based on the Canon backend written by Helmut Koeberle </p>
<p> Parts of this man page are a plain copy of <code><a href="/docs/linux/man/5-sane-mustek/">sane-mustek</a></code>(5) by David Mosberger-Tang, Andreas Czechanowski and Andreas Bolsch</p>
