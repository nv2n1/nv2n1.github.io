---
title: "umax_pp(5)"
name: "umax_pp"
section: "5"
letter: "u"
url: "/docs/linux/man/5-umax_pp/"
description: "sane-umax_pp – SANE backend for Umax Astra parallel port flatbed scanners"
---

<p>sane-umax_pp &#8211; SANE backend for Umax Astra parallel port flatbed scanners</p>
<h2>Description</h2>
<p>The <code>sane-umax_pp</code> library implements a SANE (Scanner Access Now Easy) backend that provides access to Umax parallel port flatbed scanners. The following scanners work with this backend:</p>
<dl>
<dd>Model:<br />
 &#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8211;<br />
 Astra 610P<br />
 Astra 1220P<br />
 HP3200C<br />
 Astra 1600P<br />
 Astra 2000P<br />
 Genius ColorPage-Life Pro
</dl>
<p> This backend handles 75&#215;75, 150&#215;150, 300&#215;300, 600&#215;600 and 600&#215;1200 for 1220P/1600P/2000P dpi scan resolutions, and 75&#215;75, 150&#215;150, 300&#215;300 and 300&#215;600 for 610P. In color and gray levels, there is a software lineart mode. The new generation models share a newer version of the 610P ASIC embedded in an EPAT chip. Only parts such as CCD and ADC change from one to another. They even all reports being UMAX Astra 1220P via IEEE1284. There isn&#8217;t software way to recognize them properly. Under windows, model is set by the driver installed, regardless of the hardware.</p>
<dl>
<dt><code>EPP/ECP MODES ONLY</code></p>
<dd>The current version of the backend uses only EPP or ECP mode to communicate with the scanner. PS/2 mode isn&#8217;t implemented. The 610P only use SPP. It is recommended that you set your parallel port to EPP in BIOS with the current version of this backend. You can leave it to ECP or ECP+EPP, but in this case you may not use ppdev but only direct hardware access if you have to use ECP. ECPEPP will only work if you use a 2.4 or 2.6 kernel with ppdev character device support.</dl>
<p> This backend does support parport sharing only <i>if you have a kernel with ppdev support.</i> <i> </i> Note that if you don&#8217;t use the ppdev character device, the backend needs to run as root. To allow user access to the scanner run the backend through the network interface (See <a href="/docs/linux/man/8-saned/">saned</a>(8) and <a href="/docs/linux/man/5-sane-net/">sane-net</a>(5)). A more relaxed solution (security wise) is to add suid bit to the frontend (See <a href="/docs/linux/man/1-chmod/">chmod</a>(1)). The backend drop root privileges as soon as it can, right after gaining direct access to IO ports, which lessen risks when being root. </p>
<h2>Device Names</h2>
<p>This backend expects device names of the form: </p>
<dl>
<dd><i>port value</i></dl>
<p> Where <code>value</code> is : </p>
<dl>
<dd>
<dl>
<dt>auto</p>
<dd>autodetect all parallel ports and probe them for scanner</p>
<dt>safe-auto</p>
<dd>autodetect all parallel ports and probe them for scanner, but does not try direct hardware access</p>
<dt>/dev/ppi0</p>
<dd>uses *BSD ppi device, depending on the number of available parallel port, you have to use /dev/ppi1, /dev/ppi2, &#8230;</p>
<dt>/dev/parport0</p>
<dd>uses linux ppdev device, depending on the number of available parallel port, you have to use /dev/parport1, /dev/parport2, &#8230;</p>
<dt>0x378</p>
<dd>does direct hardware access on the given address. Usual values are 0x378, 0x278, 0x3BC In this case, you have to run the scanner as root (*BSD and linux), or with &#8216;IOPL=yes&#8217; on OS/2</dl>
</dl>
<p> <code>NOTE:</code> in all cases, you must have sufficient privileges to get access to the chosen device or address. Depending on the security settings, devices may not be available for all users. You have to change permissions on the dev/ppi* or /dev/parport* devices. </p>
<p> You can rename any device using the </p>
<dl>
<dd><i>name devname</i><br />
 <i>model model</i><br />
 <i>vendor vendor</i></dl>
<p> options. These options apply to the last port option.</p>
<h2>Configuration</h2>
<p>Please make sure to edit umax_pp.conf <code>before</code> you use the backend. </p>
<p> The contents of the <code>umax_pp.conf</code> file is a list of options and device names that correspond to Umax scanners. Empty lines and lines starting with a hash mark (#) are ignored. </p>
<p> The eight options supported are <code>red-gain</code>, <code>green-gain</code>, <code>blue-gain</code>, <code>red-offset</code>, <code>green-offset</code>, <code>blue-offset</code>, <code>astra</code>, and <code>buffer</code>. </p>
<p> Options <code>red-gain</code> , <code>green-gain</code> and <code>blue-gain</code> allow you to adjust the sensitivity of your scanner for the given color. Values range from 0 (lowest gain) to 15 (highest). If the advanced option &quot;Gain&quot; isn&#8217;t checked in the frontend, the backend does automatic gain calibration, and do not use user provided values. </p>
<p> Options <code>red-offset</code> , <code>green-offset</code> and <code>blue-offset</code> allow you to adjust the offset of your scanner for the given color. Values range from 0 (lowest offset) to 15 (highest). </p>
<p> Option <code>astra</code> allows you to change the model of your scanner. Current auto detection is based on side effects on scanning when using 1220P command set on other models, so it may fail on unknown hardware combination. Valid values are 610, 1220, 1600 and 2000. It is useful only when autodetection fails to detect properly your scanner model. If your scanner work properly but is reported wrongly, let it be that way. The only valid case to change the model is when your scanner produces &quot;black&quot; or &quot;inverted&quot; scans. In this case you can put the model. Be aware that it will prevent scanner model autodetection. </p>
<p> Option <code>buffer</code> allows you to change the size of the scan buffer. The size must be specified in bytes. The default value is 2 megabytes. Decreasing this value will improve the smoothness of progress bar in the frontend, but will stall the scan more often.</p>
<h2>Files</h2>
<dl>
<dt><i>@CONFIGDIR@/umax_pp.conf</i></p>
<dd>The backend configuration file (see also description of <code>SANE_CONFIG_DIR</code> below).</p>
<dt><i>@LIBDIR@/libsane-umax_pp.a</i></p>
<dd>The static library implementing this backend.</p>
<dt><i>@LIBDIR@/libsane-umax_pp.so</i></p>
<dd>The shared library implementing this backend (present on systems that support dynamic loading). </p>
</dl>
<h2>Environment</h2>
<dl>
<dt><code>SANE_CONFIG_DIR</code></p>
<dd>This environment variable specifies the list of directories that may contain the configuration file. Under UNIX, the directories are separated by a colon (`:&#8217;), under OS/2, they are separated by a semi-colon (`;&#8217;). If this variable is not set, the configuration file is searched in two default directories: first, the current working directory (&quot;.&quot;) and then in @CONFIGDIR@. If the value of the environment variable ends with the directory separator character, then the default directories are searched after the explicitly specified directories. For example, setting <code>SANE_CONFIG_DIR</code> to &quot;/tmp/config:&quot; would result in directories &quot;tmp/config&quot;, &quot;.&quot;, and &quot;@CONFIGDIR@&quot; being searched (in this order).</p>
<dt><code>SANE_DEBUG_UMAX_PP</code></p>
<dd>If the library was compiled with debug support enabled, this environment variable controls the debug level for this backend. E.g., a value of 128 requests all debug output to be printed. Smaller levels reduce verbosity. </p>
</dl>
<dl>
<dd>
<pre>level debug output
------- ------------------------------
 0 nothing
 1 errors
 2 warnings &amp; minor errors
 3 additional information
 4 debug information
 5 code flow (not supported yet)
 6 special debug information</pre>
</dl>
<dl>
<dt><code>SANE_DEBUG_UMAX_PP_LOW</code></p>
<dd>This variable sets the debug level for the SANE interface for the Umax ASIC. Note that enabling this will spam your terminal with some million lines of debug output. </p>
</dl>
<dl>
<dd>
<pre>level debug output
------- -------------------------------
 0 nothing
 1 errors
 8 command blocks
 16 detailed code flow
 32 dump datafiles
 255 everything</pre>
</dl>
<h2>See Also</h2>
<p><a href="/docs/linux/man/7-sane/">sane</a>(7), <a href="/docs/linux/man/5-sane-net/">sane-net</a>(5), <a href="/docs/linux/man/8-saned/">saned</a>(8)</p>
<dl>
<dt>For latest bug fixes and information see</p>
<dd><i><a rel="nofollow" href="http://umax1220p.sourceforge.net/">http://umax1220p.sourceforge.net/</a></i> </p>
<h2>Author</h2>
<p>St&eacute;phane Voltz &lt;stef.dev [at] free.fr&gt;</p>
<h2>Credits</h2>
<p>Support for the 610P has been made possible thank to an hardware donation by William Stuart.</p>
<h2>Bug Reports</h2>
<p>If something doesn&#8217;t work, please contact me. But I need some information about your scanner to be able to help you&#8230; </p>
<dl>
<dt><i>SANE version</i></p>
<dd>run &quot;scanimage -V&quot; to determine this</p>
<dt><i>the backend version and your scanner hardware</i></p>
<dd>run &quot;SANE_DEBUG_UMAX_PP=255 scanimage -L 2&gt;log&quot; as root. If you don&#8217;t get any output from the umax_pp backend, make sure a line &quot;umax_pp&quot; is included into your @CONFIGDIR@/dll.conf. If your scanner isn&#8217;t detected, make sure you&#8217;ve defined the right port address, or the correct device in your umax_pp.conf.</p>
<dt><i>the name of your scanner/vendor</i></p>
<dd>also a worthy information. Please also include the optical resolution and lamp type of your scanner, both can be found in the manual of your scanner.</p>
<dt><i>any further comments</i></p>
<dd>if you have comments about the documentation (what could be done better), or you think I should know something, please include it. </p>
</dl>
