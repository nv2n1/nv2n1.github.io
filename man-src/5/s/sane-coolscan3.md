---
title: "sane-coolscan3(5)"
name: "sane-coolscan3"
section: "5"
letter: "s"
url: "/docs/linux/man/5-sane-coolscan3/"
description: "sane-coolscan3 – SANE backend for Nikon Coolscan film scanners"
---

<p>sane-coolscan3 &#8211; SANE backend for Nikon Coolscan film scanners</p>
<h2>Description</h2>
<p>The <code>sane-coolscan3</code> library implements a SANE (Scanner Access Now Easy) backend that provides access to Nikon Coolscan film scanners. Some functions of this backend should be considered <code>beta-quality</code> software. Most functions have been stable for a long time, but of course new development can not and will not function properly from the very first day. At present, the following scanners are known to work with this backend:</p>
<dl>
<dd>
<pre>Model: Connection Type
--------------------------- -------------------
LS-30 (Coolscan III) SCSI
LS-40 ED (Coolscan IV) USB
LS-50 ED (Coolscan V) USB
LS-2000 SCSI
LS-4000 ED IEEE 1394
LS-8000 ED IEEE 1394</pre>
</dl>
<p> Please send mail to <i>sane-devel [at] alioth-lists.debian.net</i> to report successes or failures. </p>
<h2>Options</h2>
<p>The options the backend supports can either be selected through command line options to programs like <code><a href="/docs/linux/man/1-scanimage/">scanimage</a></code>(1) or through GUI elements in <code><a href="/docs/linux/man/1-xscanimage/">xscanimage</a></code>(1) or <code><a href="/docs/linux/man/1-xsane/">xsane</a></code>(1). </p>
<p> Valid command line options and their syntax can be listed by using: </p>
<dl>
<dd>scanimage &#8211;help -d coolscan3:&lt;interface&gt;:&lt;device&gt;</dl>
<p> where &lt;interface&gt; and &lt;device&gt; specify the device in question, as in the configuration file (see next section). The <code>-d</code> parameter and its argument can be omitted to obtain information on the first scanner identified. Use the command: </p>
<dl>
<dd>scanimage -L</dl>
<p> to list all devices recognized by your SANE installation. </p>
<p> The options should be fully described by the description or tooltips given by frontend. Here is a description of some of the most important options, in the syntax with which they must be supplied to <code><a href="/docs/linux/man/1-scanimage/">scanimage</a></code>(1):</p>
<dl>
<dt><code>&#8211;frame &lt;n&gt;</code></p>
<dd>This option specifies which frame to operate on, if a motorized film strip feeder or APS adapter are used. The frame number <i>&lt;n&gt;</i> ranges from 1 to the number of frames available, which is sensed each time the backend is initialized (usually each time you start the frontend).</p>
<dt><code>&#8211;subframe &lt;x&gt;</code></p>
<dd>This option shifts the scan window by the specified amount (default unit is mm).</p>
<dt><code>&#8211;infrared=yes/no</code></p>
<dd>If set to &quot;yes&quot;, the scanner will read the infrared channel, thus allowing defect removal in software. The infrared image is read during a second scan, with no options altered. The backend must not be restarted between the scans. If you use scanimage, perform a batch scan with <code>&#8211;batch-count=2</code> to obtain the IR information.</p>
<dt><code>&#8211;depth &lt;n&gt;</code></p>
<dd>Here &lt;n&gt; can either be 8 or the maximum number of bits supported by the scanner (10, 12, or 14). It specifies whether or not the scanner reduces the scanned data to 8 bits before sending it to the backend. If 8 bits are used, some information and thus image quality is lost, but the amount of data is smaller compared to higher depths. Also, many imaging programs and image formats cannot handle depths greater than 8 bits.</p>
<dt><code>&#8211;autofocus</code></p>
<dd>Perform autofocus operation. Unless otherwise specified by the other options ( <code>&#8211;focus-on-centre</code> and friends), focusing is performed on the centre of the selected scan area.</p>
<dt><code>&#8211;ae-wb</code></p>
<dd>
<dt><code>&#8211;ae</code></p>
<dd>Perform a pre-scan to calculate exposure values automatically. <code>&#8211;ae-wb</code> will maintain the white balance, while <code>&#8211;ae</code> will adjust each channel separately.</p>
<dt><code>&#8211;exposure</code></p>
<dd>Multiply all exposure times with this value. This allows exposure correction without modifying white balance.</p>
<dt><code>&#8211;load</code></p>
<dd>Load the next slide when using the slide loader (SF-200 bulk loader only).</p>
<dt><code>&#8211;eject</code></p>
<dd>Eject the film strip or mounted slide when using the slide loader.</p>
<dt><code>&#8211;reset</code></p>
<dd>Reset scanner. The scanner will perform the same action as when power is turned on: it will eject the film strip (with the SF-200 bulk loader) and calibrate itself. Use this whenever the scanner refuses to load a film strip properly, as a result of which <code>&#8211;eject</code> does not work. </p>
</dl>
<h2>Configuration File</h2>
<p>The configuration file <i>/etc/sane.d/coolscan3.conf</i> specifies the device(s) that the backend will use. Owing to the nature of the supported connection types SCSI, USB, and IEEE 1394, the default configuration file supplied with the SANE distribution should work without being edited. </p>
<p> Each line in the configuration file is either of the following, where all entries are case-sensitive:</p>
<dl>
<dt><i>blank or starting with a &#8216;#&#8217; character</i></p>
<dd>These lines are ignored, thus &#8216;#&#8217; can be used to include comments.</p>
<dt><i>containing only the word auto</i></p>
<dd>This instructs the backend to probe for a scanner by scanning the buses for devices with known identifiers. This is the default action when no configuration file is present.</p>
<dt><i>a line of the form &lt;interface&gt;:&lt;device&gt;</i></p>
<dd>Here &lt;interface&gt; can be one of &quot;scsi&quot; or &quot;usb&quot;, and &lt;device&gt; is the device file of the scanner. Note that IEEE 1394 devices are handled by the SBP-2 module in the kernel and appear to SANE as SCSI devices. </p>
</dl>
<h2>Files</h2>
<dl>
<dt><i>/usr/lib/x86_64-linux-gnu/sane/libsane-coolscan3.a</i></p>
<dd>The static library implementing this backend.</p>
<dt><i>/usr/lib/x86_64-linux-gnu/sane/libsane-coolscan3.so</i></p>
<dd>The shared library implementing this backend (present on systems that support dynamic loading).</p>
<dt><i>/etc/sane.d/coolscan3.conf</i></p>
<dd>Configuration file for this backend, read each time the backend is initialized. </p>
</dl>
<h2>Environment</h2>
<dl>
<dt><code>SANE_DEBUG_COOLSCAN3</code></p>
<dd>If the library was compiled with debug support enabled, this environment variable controls the debug level for this backend. E.g., a value of 128 requests all debug output to be printed. Smaller levels reduce verbosity. </p>
</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/5-sane-scsi/">sane-scsi</a></code>(5), <code><a href="/docs/linux/man/5-sane-usb/">sane-usb</a></code>(5), <code><a href="/docs/linux/man/1-scanimage/">scanimage</a></code>(1), <code><a href="/docs/linux/man/1-xscanimage/">xscanimage</a></code>(1), <code><a href="/docs/linux/man/1-xsane/">xsane</a></code>(1) </p>
<h2>Bugs</h2>
<p>Currently, the SANE protocol does not allow automatically updating options whenever the hardware changes. Thus the number of choices for the <code>&#8211;frame</code> option will be fixed when the backend is initialized (usually when the user runs the frontend). In particular, if there is no film strip in the automatic film strip feeder when the backend is initialized, the <code>&#8211;frame</code> option will not appear at all. Also, restarting the frontend after swapping film adapters is strongly recommended. Linux kernels prior to 2.4.19 had a patch that truncated INQUIRY data from IEEE 1394 scanners to 36 bytes, discarding vital information about the scanner. The IEEE 1394 models therefore only work with 2.4.19 or later. No real bugs currently known, please report any to the SANE developers&#8217; list. </p>
<h2>Authors</h2>
<p>coolscan3 written by A. Zummo &lt;<i>a.zummo [at] towertech.it</i>&gt;, based heavily on coolscan2 written by Andr&aacute;s Major &lt;<i>andras [at] users.sourceforge.net</i>&gt;.</p>
