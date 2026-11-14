---
title: "sane-microtek2(5)"
name: "sane-microtek2"
section: "5"
letter: "s"
url: "/docs/linux/man/5-sane-microtek2/"
description: "sane-microtek2 – SANE backend for Microtek scanners with SCSI-2 command set"
---

<p>sane-microtek2 &#8211; SANE backend for Microtek scanners with SCSI-2 command set</p>
<h2>Description</h2>
<p>The <code>sane-microtek2</code> library implements a SANE (Scanner Access Now Easy) backend that provides access to Microtek scanners with a SCSI-2 command set. This backend can be considered alpha to beta. Some scanner models are reported to work well, others not. New development versions of this backend can be obtained from <i><a rel="nofollow" href="http://karstenfestag.gmxhome.de">http://karstenfestag.gmxhome.de</a></i>. There exists a different backend for Microtek scanners with SCSI-1 command set. Refer to <code><a href="/docs/linux/man/5-sane-microtek/">sane-microtek</a></code>(5) for details. And there is work in progress for the ScanMaker 3600. See <i><a rel="nofollow" href="http://sourceforge.net/projects/sm3600">http://sourceforge.net/projects/sm3600</a></i>. At present, the following scanners are known positively to work with this backend: </p>
<pre>Vendor Product id Remark
--------------------------------------------------------------------
Microtek E3+ Parport and SCSI
Microtek X6 SCSI
Microtek X6EL SCSI
Microtek X6USB USB
Microtek ScanMaker V300 Parport and SCSI
Microtek ScanMaker V310 Parport and SCSI
Microtek ScanMaker V600 Parport and SCSI
Microtek ScanMaker 330 SCSI
Microtek ScanMaker 630 SCSI
Microtek ScanMaker 636 SCSI
Microtek ScanMaker 9600XL SCSI; only flatbed mode?
Microtek Phantom 330CX Parport
Microtek SlimScan C3 Parport
Microtek SlimScan C6 USB
Microtek Phantom 636 SCSI
Microtek Phantom 636CX Parport
Microtek V6USL SCSI and USB
Microtek V6UPL USB; not stable
Microtek X12USL SCSI; only 8bit color, work in progress
Vobis HighScan SCSI (E3+ based models)
Scanport SQ300 Parport?
Scanport SQ4836 SCSI
Scanpaq SQ2030 Parport</pre>
<p>Additional information can be found at <i><a rel="nofollow" href="http://www.sane-project.org/">http://www.sane-project.org/</a></i>. If you own a Microtek scanner other than the ones listed above, it may or may not work with SANE! Because equal scanners are sold under different names in different countries your model may be equivalent to one of the above. The parport scanners work with the ppscsi + onscsi kernel modules. See <i><a rel="nofollow" href="http://cyberelk.net/tim/parport/ppscsi.html">http://cyberelk.net/tim/parport/ppscsi.html</a></i> and <i><a rel="nofollow" href="http://penguin-breeder.org/kernel/download/">http://penguin-breeder.org/kernel/download/</a></i>. The USB scanners work with the microtek kernel module. You may have to add the vendor and model codes to microtek.c if they aren&#8217;t yet listed there. Both parport and USB scanners need the generic SCSI support, so check if you have loaded the scsi_mod and sg modules! If you try your scanner for the first time keep an eye on it. If it gets commands that it doesn&#8217;t understand the scanhead may go beyond the scan area. The scanner then makes strange noises. In this case immediately switch off the scanner or disconnect its power cable to prevent damages! If your scanner is a different one than the models mentioned above and it is working please tell the author about it. It would be nice if you add a logfile to this information (creation of the logfile: see below). If your scanner is not working properly you also should create a logfile and send it to the author. He will use the information to improve the backend and possibly make your scanner work. </p>
<pre><code>How to create the logfile?

- put the line

&quot;option dump 2&quot; into your
microtek2.conf

file or change the existing &quot;option dump&quot; to &quot;2&quot;
- in a terminal (bash) type

&quot;export SANE_DEBUG_MICROTEK2=30&quot; and then

&quot;scanimage -l0 -t0 -x100 -y20 2&gt;scan.log &gt;sout.pnm&quot;

You get two files: scan.log contains the logfile and sout.pnm the scanned
image (if there was scanned something). Zip them before sending.
</code></pre>
<h2>Frontend Options</h2>
<p>This backend dynamically enables the options for the frontend, that are supported by the scanner in dependence of the scanning-mode and other options. Not supported options are disabled. </p>
<p> The following options are supported by the <code>sane-microtek2</code> driver: </p>
<p> Color, grayscale, halftone and lineart scans. </p>
<p> Highlight, midtone, shadow, contrast, brightness, exposure time control, gamma correction, threshold (dependent of the scan mode and the scanner capabilities) </p>
<p> Transparency media adapter, automatic document feeder </p>
<p> Additional options can be enabled or disabled in the <i>microtek2.conf</i> file. See the configuration section of this manpage.</p>
<h2>Device Names</h2>
<p>This backend expects device names of the form: </p>
<dl>
<dd><i>special</i></dl>
<p> Where <i>special</i> is the UNIX path-name for the special device that corresponds to the scanner. The special device name must be a generic SCSI device or a symlink to such a device. Under Linux, such a device name could be <i>/dev/sga</i> or <i>/dev/sge</i> for example.</p>
<h2>Configuration</h2>
<p>The configuration file for this backend resides in <i>/etc/sane.d/microtek2.conf</i>. </p>
<p> Its contents is a list of device names that correspond to Microtek scanners with SCSI-2 interface. Empty lines and lines starting with a hash mark (#) are ignored. </p>
<p> The configuration file may also contain options. Global options that are valid for all devices are placed above the device names. Device-specific options are placed under the device name. Note that, except for option dump &lt;n&gt; and option strip-height &lt;n&gt;, the entry in the microtek2.conf file only enables the corresponding option for being showed in the frontend. There, in the frontend, you can switch the options on and off. Currently the following options are supported: </p>
<dl>
<dd>option dump &lt;n&gt;<br />
 option strip-height &lt;n&gt;<br />
 option no-backtrack-option &lt;on/off&gt;<br />
 option lightlid-35 &lt;on/off&gt;<br />
 option toggle-lamp &lt;on/off&gt;<br />
 option lineart-autoadjust &lt;on/off&gt;<br />
 option backend-calibration &lt;on/off&gt;<br />
 option colorbalance-adjust &lt;on/off&gt;</dl>
<p> <i>option dump &lt;n&gt;</i> enables printing of additional information about the SCSI commands that are sent to the scanner to stderr. This option is primarily useful for debugging purpose. This option has to be a global option and is best placed at the top of the <i>microtek2.conf</i> file. </p>
<p> If n=1 the contents of the command blocks and the results for the INQUIRY and READ SCANNER ATTRIBUTES command are printed to stderr. </p>
<p> If n=2 the contents of the command blocks for all other SCSI commands are printed to stderr, too. If n=3 the contents of the gamma table is printed, too. If n=4 all scan data is additionally printed to stderr. </p>
<p> The default is n=1. </p>
<p> <i>option strip-height &lt;n&gt;</i> , where &lt;n&gt; is a floating point number, limits the amount of data that is read from the scanner with one read command. The unit is inch and &lt;n&gt; defaults to 1.0, if this option is not set in the configuration file. If less than &lt;n&gt; inch of data fit into the SCSI buffer, then the smaller value is used and this option has no effect. </p>
<p> If your system has a big SCSI buffer and you want to make use of the whole buffer, increase the value for &lt;n&gt;. For example, if &lt;n&gt; is set to 14.0, no restrictions apply for scanners with a letter, legal or A4 sized scan area. </p>
<p> The following options enable or disable additional frontend options. If an option is set to &lt;on&gt; an appropriate option will appear in the frontend. </p>
<p> <i>option no-backtrack-option &lt;on/off&gt;</i> prevents the scanner head from moving backwards between the read commands. This speeds up scanning. Try it. </p>
<p> <i>option lightlid-35 &lt;on/off&gt;</i> If you use the LightLid-35 transparency adapter you get an advanced option which switches off the flatbed lamp during the scan. </p>
<p> <i>option toggle-lamp &lt;on/off&gt;</i> You get a button in the frontend where you can switch on and off the flatbed lamp. </p>
<p> <i>option lineart-autoadjust &lt;on/off&gt;</i> You can tell the backend to try to determine a good value for the lineart threshold. </p>
<p> <i>option backend-calibration &lt;on/off&gt;</i> Some scanners (e.g. Phantom 330CX and 636CX) need to have calibrated the data by the backend. Try this option if you see vertical stripes in your pictures. </p>
<p> <i>option colorbalance-adjust &lt;on/off&gt;</i> Some scanners (e.g. Phantom 330CX and 636CX) need to have corrected the color balance. If this option is enabled you get advanced options where you can balance the colors. And you will have a button to use the values that the firmware of the scanner provides. </p>
<p> A sample configuration file is shown below: </p>
<dl>
<dd>option dump 1<br />
 option strip-height 1.0<br />
 /dev/scanner<br />
 option no-backtrack-option on<br />
 # this is a comment<br />
 /dev/sge<br />
 option lightlid-35 on</dl>
<p> This backend also supports the new configuration file format which makes it easier to detect scanners under Linux. If you have only one scanner it would be best to use the following configuration file for this backend: </p>
<dl>
<dd>option dump 1<br />
 option strip-height 14.0<br />
 option no-backtrack-option on<br />
 option backend-calibration on<br />
 option lightlid-35 on<br />
 option toggle-lamp on<br />
 option lineart-autoadjust on<br />
 option colorbalance-adjust off<br />
 scsi * * Scanner</dl>
<p> In this case all SCSI-Scanners should be detected automatically because of the </p>
<p> scsi * * Scanner </p>
<p> line.</p>
<h2>Files</h2>
<dl>
<dt><i>/etc/sane.d/microtek2.conf</i></p>
<dd>The backend configuration file.</p>
<dt><i>/usr/lib/x86_64-linux-gnu/sane/libsane-microtek2.a</i></p>
<dd>The static library implementing this backend.</p>
<dt><i>/usr/lib/x86_64-linux-gnu/sane/libsane-microtek2.so</i></p>
<dd>The shared library implementing this backend (present on systems that support dynamic loading).</dl>
<h2>Environment</h2>
<dl>
<dt><code>SANE_DEBUG_MICROTEK2</code></p>
<dd>If the library was compiled with debug support enabled, this environment variable controls the debug level for this backend. E.g., a value of 255 requests all debug output to be printed. Smaller levels reduce verbosity. To see error messages on stderr set <code>SANE_DEBUG_MICROTEK2</code> to 1 (Remark: The whole debugging levels should be better revised).<br />
 E.g. just say:<br />
 export SANE_DEBUG_MICROTEK2=128 </p>
</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/5-sane-scsi/">sane-scsi</a>(5)</code>, <code><a href="/docs/linux/man/7-sane/">sane</a></code>(7) </p>
<h2>Authors</h2>
<p>Bernd Schroeder (not active anymore)<br />
 Karsten Festag &lt;<i>karsten.festag [at] gmx.de</i>&gt;.</p>
