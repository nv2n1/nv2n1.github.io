---
title: "sane-mustek(5)"
name: "sane-mustek"
section: "5"
letter: "s"
url: "/docs/linux/man/5-sane-mustek/"
description: "sane-mustek – SANE backend for Mustek SCSI flatbed scanners (and some other devices)"
---

<p>sane-mustek &#8211; SANE backend for Mustek SCSI flatbed scanners (and some other devices)</p>
<h2>Description</h2>
<p>The <code>sane-mustek</code> library implements a SANE (Scanner Access Now Easy) backend that provides access to Mustek (and some relabeled Trust and Primax) SCSI and parport flatbed scanners. At present, the following scanners are known to work more or less with this backend:</p>
<dl>
<dd>Paragon MFS-6000CX<br />
 Paragon MFS-12000CX<br />
 Paragon MFC-600S, 600 II CD, ScanMagic 600 II SP<br />
 Paragon MFC-800S, 800 II SP<br />
 Paragon MFS-6000SP<br />
 Paragon MFS-8000SP<br />
 Paragon MFS-1200SP, MFS-12000SP<br />
 ScanExpress 6000SP<br />
 ScanExpress 12000SP, 12000SP Plus, Paragon 1200 III SP, ScanMagic 9636S, 9636S Plus<br />
 Paragon 1200 LS<br />
 ScanExpress A3 SP<br />
 Paragon 1200 SP Pro<br />
 Paragon 1200 A3 Pro<br />
 Paragon 600 II EP<br />
 Paragon 600 II N<br />
 Trust Imagery 1200<br />
 Trust Imagery 1200 SP<br />
 Trust Imagery 4800 SP<br />
 Trust SCSI Connect 19200<br />
 Primax Compact 4800 SCSI
</dl>
<p> More details can be found on the Mustek SCSI backend homepage <i><a rel="nofollow" href="http://www.meier-geinitz.de/sane/mustek-backend/">http://www.meier-geinitz.de/sane/mustek-backend/</a></i>. Don&#8217;t mix up MFS (Paragon), Pro and ScanExpress models! They&#8217;re completely different. Check the exact model name! Note that most of the above scanners come with a SCSI interface. The only non-SCSI scanners that have some support at this point is the 600 II N and 600 II EP scanners. The former one comes with its own parallel port adapter (i.e., it does <i>not</i> attach to the printer port). Both scanners use the SCSI protocol internally, too. More info on how to use these parallel port scanners can be found below in section <code>PARALLEL PORT SCANNERS</code>. Other parallel port scanners are not supported by this backend but you may be successful using the Mustek parallel port backend mustek_pp, see <code><a href="/docs/linux/man/5-sane-mustek_pp/">sane-mustek_pp</a></code>(5). USB scanners are also not supported by this backend but the ma1509, mustek_usb, gt68xx, and plustek backends include support for some of them, see <code><a href="/docs/linux/man/5-sane-ma1509/">sane-ma1509</a></code>(5), <code><a href="/docs/linux/man/5-sane-mustek_usb/">sane-mustek_usb</a></code>(5), <code><a href="/docs/linux/man/5-sane-gt68xx/">sane-gt68xx</a></code>(5), and <code><a href="/docs/linux/man/5-sane-plustek/">sane-plustek</a></code>(5). Mustek scanners have no protection against exceeding the physical scan area height. That is, if a scan is attempted with a height that exceeds the height of the scan surface, the scanner begins making loud noises and the scan mechanism may be damaged. Thus, if you hear such a noise, IMMEDIATELY turn off the scanner. This shouldn&#8217;t happen if your scanner is in the list of known scanners. There is more information in the <i>/usr/share/doc/libsane/PROBLEMS</i> file. If you own a Mustek (or Trust) scanner other than the ones listed above that works with this backend, please let us know by sending the scanner&#8217;s exact model name (look at the front and back of the scanner) and a debug output to <i>sane-devel [at] alioth-lists.debian.net</i>. You can get the debug output by setting the environment variable <code>SANE_DEBUG_MUSTEK</code> to 5 and showing the list of available scanners with <i>scanimage -L</i>. Please send all of it to the mailing list. You must be subscribed to sane-devel before you can send mail to the list. See <i><a rel="nofollow" href="http://www.sane-project.org/mailing-lists.html">http://www.sane-project.org/mailing-lists.html</a></i> for details. </p>
<h2>Device Names</h2>
<p>This backend expects device names of the form: </p>
<dl>
<dd><i>special</i></dl>
<p> Where <i>special</i> is either the path-name for the special device that corresponds to a SCSI scanner or the port number at which the parallel port scanners can be found (see section <code>PARALLEL PORT SCANNERS</code> below). For SCSI scanners, the special device name must be a generic SCSI device or a symlink to such a device. The program <code><a href="/docs/linux/man/1-sane-find-scanner/">sane-find-scanner</a></code>(1) helps to find out the correct device. Under Linux, such a device name could be <i>/dev/sg0</i> or <i>/dev/sg3</i>, for example. See <code><a href="/docs/linux/man/5-sane-scsi/">sane-scsi</a></code>(5) for details.</p>
<h2>Configuration</h2>
<p>The contents of the <i>mustek.conf</i> file is a list of options and device names that correspond to Mustek scanners. Empty lines and lines starting with a hash mark (#) are ignored. See <code><a href="/docs/linux/man/5-sane-scsi/">sane-scsi</a></code>(5) on details of what constitutes a valid device name. </p>
<p> The supported options are <code>linedistance-fix</code>, <code>lineart-fix</code>, <code>legal-size</code>, <code>buffersize</code>, <code>blocksize</code>, <code>strip-height</code>, <code>disable-double-buffering</code>, <code>disable-backtracking</code>, and <code>force-wait</code>. </p>
<p> Options come in two flavors: global and positional ones. Global options apply to all devices managed by the backend whereas positional options apply just to the most recently mentioned device. Note that this means that the order in which the options appear matters! </p>
<p> Option <code>linedistance-fix</code> is positional and works around a problem that occurs with some SCSI controllers (notably the ncr810 controller under Linux). If color scans have horizontal stripes and/or the colors are off, then it&#8217;s likely that your controller suffers from this problem. Turning on this option usually fixes the problem. </p>
<p> Option <code>lineart-fix</code> is positional and works around a timing problem that seems to exist with certain MFS-12000SP scanners. The problem manifests itself in dropped lines when scanning in lineart mode. Turning on this option should fix the problem but may slow down scanning a bit. </p>
<p> Option <code>legal-size</code> is positional and sets the size of the scan area to Legal format. Set this option if you own a Paragon 12000 LS. It can&#8217;t be distinguished by software from a ScanExpress 12000 SP (ISO A4 format). </p>
<p> Option <code>buffersize</code> is a positional option that overrides the default value set for the size of the SCSI buffer. The buffer size is specified in kilobytes. The default value is 128. Because of double buffering the buffer actually sent to the scanner is half the size of this value. Try to increase this value to achieve higher scan speeds. Note that some ScanExpress scanners don&#8217;t like buffer sizes above 64 kb (buffersize = 128). If your sg driver can&#8217;t set SCSI buffer sizes at runtime you may have to change that value, too. See <a href="/docs/linux/man/5-sane-scsi/">sane-scsi</a>(5) for details. </p>
<p> Option <code>blocksize</code> is a positional option that overrides the default value set for the maximum amount of data scanned in one block. The buffer size is specified in kilobytes. Some scanners freeze if this value is bigger than 2048. The default value is 1 GB (so effectively no limit) for most scanners. Don&#8217;t change this value if you don&#8217;t know exactly what you do. </p>
<p> Option <code>strip-height</code> is a global option that limits the maximum height of the strip scanned with a single SCSI read command. The height is specified in inches and may contain a fractional part (e.g., 1.5). Setting the strip-height to a small value (one inch, for example) reduces the likelihood of encountering problems with SCSI driver timeouts and/or timeouts with other devices on the same SCSI bus. Unfortunately, it also increases scan times. With current SCSI adapters and drivers this option shouldn&#8217;t be needed any more. </p>
<p> Option <code>disable-double-buffering</code> is a global option. If set, the backend will only send one buffer at a time to the scanner. Try this option if you have trouble while scanning, e.g. SCSI errors, freezes, or the first few cm are repeated over and over again in your image. </p>
<p> Option <code>disable-backtracking</code> is a positional option. If set, the scanner will not move back its slider after each SCSI buffer is filled (`backtracking&#8217;). Setting this option will lead to faster scans but may also produce horizontal stripes. This option doesn&#8217;t work with every scanner (only some of the paragon models can modify backtracking). </p>
<p> Finally, <code>force-wait</code> is a global option. If set, the backend will wait until the device is ready before sending the inquiry command. Further more the backend will force the scan slider to return to its starting position (not implemented for all scanners). This option may be necessary with the 600 II N or when <code><a href="/docs/linux/man/1-scanimage/">scanimage</a></code>(1) is used multiple times (e.g. in scripts). The default is off (not set). </p>
<p> A sample configuration file is shown below: </p>
<dl>
<dd># limit strip height of all scanners to 1.5 inches:<br />
 option strip-height 1.5 </p>
<p> /dev/scanner # first Mustek scanner<br />
 # 1 MB buffer for /dev/scanner:<br />
 option buffersize 1024<br />
 /dev/sge # second Mustek scanner<br />
 # turn on fixes for /dev/sge:<br />
 option lineart-fix<br />
 option linedistance-fix</dl>
<h2>Scsi Adapter Tips</h2>
<p>You need a SCSI adapter for the SCSI scanners. Even if the connector is the same as that of parallel port scanners, connecting it to the computers parallel port will NOT work. </p>
<p> Mustek SCSI scanners are typically delivered with an ISA SCSI adapter. Unfortunately, that adapter is not worth much since it is not interrupt driven. It is (sometimes) possible to get the supplied card to work, but without interrupt line, scanning will be very slow and put so much load on the system, that it becomes almost unusable for other tasks. </p>
<p> If you already have a working SCSI controller in your system, you should consider that Mustek scanners do not support the SCSI-2 disconnect/reconnect protocol and hence tie up the SCSI bus while a scan is in progress. This means that no other SCSI device on the same bus can be accessed while a scan is in progress. </p>
<p> Because the Mustek-supplied adapter is not worth much and because Mustek scanners do not support the SCSI-2 disconnect/reconnect protocol, it is recommended to install a separate (cheap) SCSI controller for Mustek scanners. For example, ncr810 based cards are known to work fine and cost as little as fifty US dollars. </p>
<p> For Mustek scanners, it is typically necessary to configure the low-level SCSI driver to disable synchronous transfers (sync negotiation), tagged command queuing, and target disconnects. See <code><a href="/docs/linux/man/5-sane-scsi/">sane-scsi</a></code>(5) for driver- and platform-specific information. </p>
<p> The ScanExpress models have sometimes trouble with high resolution color mode. If you encounter sporadic corrupted images (parts duplicated or shifted horizontally) kill all other applications before scanning and (if sufficient memory is available) disable swapping. </p>
<p> Details on how to get the Mustek SCSI adapters and other cards running can be found at <i><a rel="nofollow" href="http://www.meier-geinitz.de/sane/mustek-backend/#SCSI">http://www.meier-geinitz.de/sane/mustek-backend/#SCSI</a></i>.</p>
<h2>Parallel Port Scanners</h2>
<p>This backend has support for the Paragon 600 II EP and Paragon 600 II N parallel port scanners. Note that the latter scanner comes with its own ISA card that implements a funky parallel port (in other words, the scanner does not connected to the printer parallel port). </p>
<p> These scanners can be configured by listing the port number of the adapter or the parallel port in the mustek.conf file. Valid port numbers for the 600 II N are <i>0x26b</i>, <i>0x2ab</i>, <i>0x2eb</i>, <i>0x22b</i>, <i>0x32b</i>, <i>0x36b</i>, <i>0x3ab</i>, <i>0x3eb</i>. For the 600 II EP use one of these: <i>parport0</i>, <i>parport1</i>, <i>parport2</i>, <i>0x378</i>, <i>0x278</i>, <i>0x3bc</i>. Pick one that doesn&#8217;t conflict with the other hardware in your computer. Put only one number on a single line. Example: </p>
<dl>
<dd><i>0x3eb</i></dl>
<p> Note that for these scanners usually root privileges are required to access the I/O ports. Thus, either make frontends such as <code><a href="/docs/linux/man/1-scanimage/">scanimage</a></code>(1) and <code><a href="/docs/linux/man/1-xscanimage/">xscanimage</a></code>(1) setuid root (generally not recommended for safety reasons) or, alternatively, access this backend through the network daemon <code><a href="/docs/linux/man/8-saned/">saned</a></code>(8). </p>
<p> If the Mustek backend blocks while sending the inquiry command to the scanner, add the option <code>force-wait</code> to <i>mustek.conf</i>. </p>
<p> Also note that after a while of no activity, some scanners themselves (not the SANE backend) turns off their CCFL lamps. This shutdown is not always perfect with the result that the lamp sometimes continues to glow dimly at one end. This doesn&#8217;t appear to be dangerous since as soon as you use the scanner again, the lamp turns back on to the normal high brightness. However, the first image scanned after such a shutdown may have stripes and appear to be over-exposed. When this happens, just take another scan, and the image will be fine.</p>
<h2>Files</h2>
<dl>
<dt><i>/etc/sane.d/mustek.conf</i></p>
<dd>The backend configuration file (see also description of <code>SANE_CONFIG_DIR</code> below).</p>
<dt><i>/usr/lib/x86_64-linux-gnu/sane/libsane-mustek.a</i></p>
<dd>The static library implementing this backend.</p>
<dt><i>/usr/lib/x86_64-linux-gnu/sane/libsane-mustek.so</i></p>
<dd>The shared library implementing this backend (present on systems that support dynamic loading). </p>
</dl>
<h2>Environment</h2>
<dl>
<dt><code>SANE_CONFIG_DIR</code></p>
<dd>This environment variable specifies the list of directories that may contain the configuration file. On *NIX systems, the directories are separated by a colon (`:&#8217;), under OS/2, they are separated by a semi-colon (`;&#8217;). If this variable is not set, the configuration file is searched in two default directories: first, the current working directory (&quot;.&quot;) and then in <i>/etc/sane.d</i>. If the value of the environment variable ends with the directory separator character, then the default directories are searched after the explicitly specified directories. For example, setting <code>SANE_CONFIG_DIR</code> to &quot;/tmp/config:&quot; would result in directories <i>tmp/config</i>, <i>.</i>, and <i>/etc/sane.d</i> being searched (in this order).</p>
<dt><code>SANE_DEBUG_MUSTEK</code></p>
<dd>If the library was compiled with debug support enabled, this environment variable controls the debug level for this backend. Higher debug levels increase the verbosity of the output. </p>
<pre>Value Description
0 no output
1 print fatal errors
2 print important messages
3 print non-fatal errors and less important messages
4 print all but debugging messages
5 print everything</pre>
<p>Example: export SANE_DEBUG_MUSTEK=4 </p>
</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/7-sane/">sane</a></code>(7), <code><a href="/docs/linux/man/1-sane-find-scanner/">sane-find-scanner</a></code>(1), <code><a href="/docs/linux/man/5-sane-scsi/">sane-scsi</a></code>(5), <code><a href="/docs/linux/man/5-sane-mustek_usb/">sane-mustek_usb</a></code>(5), <code><a href="/docs/linux/man/5-sane-gt68xx/">sane-gt68xx</a></code>(5), <code><a href="/docs/linux/man/5-sane-plustek/">sane-plustek</a></code>(5), <code><a href="/docs/linux/man/5-sane-mustek_pp/">sane-mustek_pp</a></code>(5), <code><a href="/docs/linux/man/5-sane-ma1509/">sane-ma1509</a></code>(5), <code><a href="/docs/linux/man/1-scanimage/">scanimage</a></code>(1), <code><a href="/docs/linux/man/1-xscanimage/">xscanimage</a></code>(1)<br />
 <i>/usr/share/doc/libsane/mustek/mustek.CHANGES</i><br />
 <i><a rel="nofollow" href="http://www.meier-geinitz.de/sane/mustek-backend/">http://www.meier-geinitz.de/sane/mustek-backend/</a></i> </p>
<h2>Author</h2>
<p>David Mosberger, Andreas Czechanowski, Andreas Bolsch (SE extensions), Henning Meier-Geinitz, James Perry (600 II EP).</p>
<h2>Bugs</h2>
<p>Scanning with the SCSI adapters supplied by Mustek is very slow at high resolutions and wide scan areas. Some scanners (e.g. Paragon 1200 A3 + Pro, SE A3) need more testing. The gamma table supports only 256 colors, even if some scanners can do more. More detailed bug information is available at the Mustek backend homepage: <i><a rel="nofollow" href="http://www.meier-geinitz.de/sane/mustek-backend/">http://www.meier-geinitz.de/sane/mustek-backend/</a></i>. </p>
