---
title: "sane-mustek_pp(5)"
name: "sane-mustek_pp"
section: "5"
letter: "s"
url: "/docs/linux/man/5-sane-mustek_pp/"
description: "sane-mustek_pp – SANE backend for Mustek parallel port flatbed scanners"
---

<p>sane-mustek_pp &#8211; SANE backend for Mustek parallel port flatbed scanners</p>
<h2>Description</h2>
<p>The <code>sane-mustek_pp</code> library implements a SANE (Scanner Access Now Easy) backend that provides access to Mustek parallel port flatbed scanners and OEM versions. There are 2 classes of Mustek parallel port scanners: regular <code>CCD</code> (cold cathode device) scanners and <code>CIS</code> (contact image sensor) scanners. The current version of this backend supports both CCD type scanners and CIS type scanners. The following scanners might work with this backend:</p>
<h3>CCD scanners</h3>
<pre>Model: ASIC ID: CCD Type: works:
--------------------------------------------------------------
SE 6000 P 1013 00 yes
SM 4800 P 1013/1015 04/01 yes
SE 1200 ED Plus 1015 01 no
SM 1200 ED Plus 1015 01 no
SE 12000 P 1505 05 no
600 III EP Plus 1013/1015 00/01 yes
SE 600 SEP 1013 ?? yes
600 II EP ???? ?? no
MD9848 1015 00 yes
Gallery 4800 ???? ?? yes
Viviscan Compact II 1013 00 yes</pre>
<h3>CIS scanners</h3>
<pre>Model: ASIC ID: works:
-----------------------------------------------
Mustek 600 CP &amp; 96 CP 1015 yes (*)
Mustek 1200 CP 1015 yes
Mustek 1200 CP+ 1015 yes</pre>
<pre>OEM versions Original works
--------------------------------------------------
Medion/LifeTec/Tevion
 MD/LT 9350/9351 1200 CP yes
 MD/LT 9850/9851 1200 CP maybe (**)
 MD/LT 9858 1200 CP probably
 MD/LT 9890/9891 1200 CP yes
Targa
 Funline TS12EP 1200 CP yes
 Funline TS6EP 600 CP yes
Trust
 Easy Connect 9600+ 600 CP yes
Cybercom
 9352 1200 CP yes (***)</pre>
<dl>
<dt> (*) Calibration problems existed with earlier version of</p>
<dd>this driver. They seem to be solved now.</p>
<dt> (**) Problems have been reported in the past for the</p>
<dd>MD/LT9850 type (striped scans, head moving in wrong direction at some resolutions). It is not known whether the current version of the driver still has these problems.</dl>
<p> <code>IF YOU HEAR LOUD CLICKING NOISES, IMMEDIATELY UNPLUG THE SCANNER !</code> (This holds for any type of scanner).</p>
<dl>
<dt> (***) Possibly, the engine_delay parameter has to be set to 1 ms</p>
<dd>for accurate engine movements.</dl>
<p> Please note that this backend is still under construction. Certain models are currently not supported and some may never be because the communication protocol is still unknown (eg., SE 12000 P). Some scanners work faster when <code>EPP/ECP</code> is enabled in the BIOS. EPP mode however may lead to hard-locks on some Linux systems. If that is the case for you, you can either disable ECP/EPP in your BIOS or disable it in the backend itself (see GLOBAL OPTIONS). Note that the backend needs to run as root or has to have appropriate access rights to <i>/dev/parport*</i> if libieee1284 support is compiled in. To allow user access to the scanner run the backend through the network interface (See <code><a href="/docs/linux/man/8-saned/">saned</a></code>(8) and <code><a href="/docs/linux/man/5-sane-net/">sane-net</a></code>(5)). Note also that the backend <i>does not</i> support <i>parport sharing</i>, i.e. if you try printing while scanning, your computer may crash. To enable parport sharing, you have to enable libieee1284 at compile time. This backend also conflicts with the <code><a href="/docs/linux/man/5-sane-musteka4s2/">sane-musteka4s2</a></code>(5) backend. You can only enable one of them in your <i>dll.conf</i>. However, you have to enable the backend explicitly in your <i>dll.conf</i>, just remove the hash mark in the line &quot;mustek_pp&quot;. </p>
<h2>Device Definition</h2>
<p>This backend allows multiple devices being defined and configured via the <i>mustek_pp.conf</i> file (even simultaneously, provided that they are connected to different parallel ports). Please make sure to edit this file <code>before</code> you use the backend. </p>
<p> A device can be defined as follows: </p>
<dl>
<dd><i>scanner &lt;name&gt; &lt;port name&gt; &lt;driver&gt;</i></dl>
<p> where</p>
<dl>
<dt> <code>&lt;name&gt;</code></p>
<dd>is an arbitrary name for the device, optionally enclosed by double quotes, for instance &quot;LifeTec 9350&quot;.</p>
<dt> <code>&lt;port name&gt;</code></p>
<dd>is the name of the parallel port to which the device is connected. In case libieee1284 is used for communication with the port <i>(default</i> <i>setup)</i>, valid port names are <code>parport0</code>, <code>parport1</code>, and <code>parport2</code>.</dl>
<p> In case the backend is configured for raw IO <i>(old</i> <i>setup)</i>, port addresses have to be used instead of port names: <code>0x378</code>, <code>0x278</code>, or <code>0x3BC</code>. The mapping of parallel ports (lp0, lp1, and lp2) to these addresses can be different for different Linux kernel versions. For instance, if you are using a Kernel 2.2.x or better and you have only one parallel port, this port is named lp0 regardless of the base address. However, this backend requires the base address of your port. If you are not sure which port your scanner is connected to, have a look at your <i>/etc/conf.modules</i>, <i>/etc/modules.conf</i> and/or <i>/proc/ioports</i>. </p>
<p> If you are unsure which port to use, you can use the magic value <code>*</code> to probe for your scanner. </p>
<dl>
<dt> <code>&lt;driver&gt;</code></p>
<dd>is the driver to use for this device. Currently available drivers are:</p>
<dd><code>cis600</code> : for 600 CP, 96 CP &amp; OEM versions<br />
 <code>cis1200</code> : for 1200 CP &amp; OEM versions<br />
 <code>cis1200+</code> : for 1200 CP+ &amp; OEM versions<br />
 <code>ccd300</code> : for 600 IIIE P &amp; OEM version</p>
<dd><code>Choosing the wrong driver can damage your scanner!</code><br />
 Especially, using the 1200CP settings on a 600CP can be harmful. If the scanner starts making a loud noise, turn it off immediately !!!</dl>
<p> Using the cis600 driver on a 1200CP or a 1200CP+ is probably not dangerous. The cis1200+ driver also works for the 1200CP, and using the cis1200 driver on a 1200CP+ will typically result in scans that cover only half of the width of the scan area (also not dangerous). </p>
<p> If unsure about the exact model of your OEM version, check the optical resolution in the manual or on the box: the 600CP has a maximum optical resolution of 300&#215;600 DPI, whereas the 1200CP and 1200CP+ have a maximum optical resolution of 600&#215;1200 DPI. </p>
<p> Examples: </p>
<dl>
<dd>scanner &quot;LifeTec 9350&quot; 0x378 cis1200 </p>
<p> scanner Mustek_600CP 0x378 cis600 </p>
<p> scanner Mustek_600IIIEP * ccd300</dl>
<p> If in doubt which port you have to use, or whether your scanner is detected at all, you can use <i>sane-find-scanner -p</i> to probe all configured ports.</p>
<h2>Configuration</h2>
<p>The contents of the <i>mustek_pp.conf</i> file is a list of device definitions and device options that correspond to Mustek scanners. Empty lines and lines starting with a hash mark (#) are ignored. Options have the following format: </p>
<dl>
<dd><i>option &lt;name&gt; [&lt;value&gt;]</i></dl>
<p> Depending on the nature of the option, a value may or may not be present. Options always apply to the scanner definition that precedes them. There are no global options. Options are also driver-specific: not all drivers support all possible options.</p>
<h3>Common options</h3>
<dl>
<dt><code>bw &lt;value&gt;</code></p>
<dd>Black/white discrimination value to be used during lineart scanning. Pixel values below this value are assumed to be black, values above are assumed to be white.<br />
 Default value: 127<br />
 Minimum: 0<br />
 Maximum: 255 </p>
<p> Example: option bw 150 </p>
</dl>
<h3>CIS driver options</h3>
<dl>
<dt><code>top_adjust &lt;value&gt;</code></p>
<dd>Vertical adjustment of the origin, expressed in millimeter (floating point). This option can be used to calibrate the position of the origin, within certain limits. Note that CIS scanners are probably temperature sensitive, and that a certain inaccuracy may be hard to avoid. Differences in offset between runs in the order of 1 to 2 mm are not unusual.<br />
 Default value: 0.0<br />
 Minimum: -5.0<br />
 Maximum: 5.0 </p>
<p> Example: option top_adjust -2.5</p>
<dt><code>slow_skip</code></p>
<dd>Turns fast skipping to the start of the scan region off. When the region to scan does not start at the origin, the driver will try to move the scanhead to the start of the scan area at the fastest possible speed. On some models, this may not work, resulting in large inaccuracies (up to centimeters). By setting this option, the driver is forced to use normal speed during skipping, which can circumvent the accuracy problems. Currently, there are no models for which these inaccuracy problems are known to occur. </p>
<p> By default, fast skipping is used. </p>
<p> Example: option slow_skip</p>
<dt><code>engine_delay &lt;value&gt;</code></p>
<dd>Under normal circumstances, it is sufficient for the driver to wait for the scanner signaling that the engine is stable, before a new engine command can be transmitted. In rare cases, certain scanners and/or parallel port chipsets appear to prevent reliable detection of the engine state. As a result, engine commands are transmitted too soon and the movement of the scanner head becomes unreliable. Inaccuracies ranging up to 10 cm over the whole vertical scan range have been reported. To work around this problem, the engine_delay option can be set. If it is set, the driver waits an additional amount of time after every engine command, equal to the engine_delay parameter, expressed in milliseconds. It practice an engine_delay of 1 ms is usually sufficient. The maximum delay is 100 ms. </p>
<p> Note that every additional ms of delay can add up to 14 seconds to the total scanning time (highest resolution), so an as small as possible value is preferred. </p>
<p> Default value: 0<br />
 Minimum: 0<br />
 Maximum: 100 </p>
<p> Example: option engine_delay 1 </p>
</dl>
<h3>CCD driver options</h3>
<dl>
<dt><code>top &lt;value&gt;</code></p>
<dd>Number of scanlines to skip to the start of the scan area. The number can be any positive integer. Values known to me are 47 and 56. </p>
<p> Default value: 47<br />
 Minimum: 0<br />
 Maximum: none </p>
<p> Example: option top 56</p>
<dt><code>waitbank &lt;value&gt;</code></p>
<dd>The number of usecs to wait for a bank change. You should not touch this value actually. May be any positive integer </p>
<p> Default value: 700<br />
 Minimum: 0<br />
 Maximum: none </p>
<p> Example: option waitbank 700</dl>
<p> A sample configuration file is shown below: </p>
<pre>#
# LifeTec/Medion 9350 on port 0x378
#
scanner &quot;LifeTec 9350&quot; 0x378 cis1200
# Some calibration options (examples!).
option bw 127
option top_skip -0.8
#
# A Mustek 600CP on port 0x3BC
#
scanner &quot;Mustek 600CP&quot; 0x3BC cis600
# Some calibration options (examples!).
option bw 120
option top_skip 1.2
#
# A Mustek 1200CP+ on port 0x278
#
scanner &quot;Mustek 1200CP plus&quot; 0x278 cis1200+
# Some calibration options (examples!).
option bw 130
option top_skip 0.2
#
# A Mustek 600 III EPP on port parport0
#
scanner &quot;Mustek 600 III EPP&quot; parport0 ccd300
# Some calibration options (examples!).
option bw 130
option top 56</pre>
<h2>Global Options</h2>
<p>You can control the overall behaviour of the <code>sane-mustek_pp</code> backend by global options which precede any scanner definition in the <i>mustek_pp.conf</i> file. </p>
<p> Currently, there is only one global option:</p>
<h3>Global options</h3>
<dl>
<dt><code>no_epp</code></p>
<dd>Disable parallel port mode EPP: works around a known bug in the Linux parport code. Enable this option, if the backend hangs when trying to access the parallel port in EPP mode. </p>
<p> Default value: use EPP </p>
<p> Example: option no_epp </p>
</dl>
<h2>Files</h2>
<dl>
<dt><i>/etc/sane.d/mustek_pp.conf</i></p>
<dd>The backend configuration file (see also description of <code>SANE_CONFIG_DIR</code> below).</p>
<dt><i>/usr/lib/x86_64-linux-gnu/sane/libsane-mustek_pp.a</i></p>
<dd>The static library implementing this backend.</p>
<dt><i>/usr/lib/x86_64-linux-gnu/sane/libsane-mustek_pp.so</i></p>
<dd>The shared library implementing this backend (present on systems that support dynamic loading). </p>
</dl>
<h2>Environment</h2>
<dl>
<dt><code>SANE_CONFIG_DIR</code></p>
<dd>This environment variable specifies the list of directories that may contain the configuration file. On *NIX systems, the directories are separated by a colon (`:&#8217;), under OS/2, they are separated by a semi-colon (`;&#8217;). If this variable is not set, the configuration file is searched in two default directories: first, the current working directory (&quot;.&quot;) and then in <i>/etc/sane.d</i>. If the value of the environment variable ends with the directory separator character, then the default directories are searched after the explicitly specified directories. For example, setting <code>SANE_CONFIG_DIR</code> to &quot;/tmp/config:&quot; would result in directories <i>tmp/config</i>, <i>.</i>, and <i>/etc/sane.d</i> being searched (in this order).</p>
<dt><code>SANE_DEBUG_MUSTEK_PP</code></p>
<dd>If the library was compiled with debug support enabled, this environment variable controls the debug level for this backend. E.g., a value of 128 requests all debug output to be printed. Smaller levels reduce verbosity. </p>
<pre>level debug output
--------------------------------------
 0 nothing
 1 errors
 2 warnings &amp; minor errors
 3 additional information
 4 debug information
 5 code flow (not supported yet)
 6 special debug information</pre>
<dt><code>SANE_DEBUG_SANEI_PA4S2</code></p>
<dd>This variable sets the debug level for the SANE interface for the Mustek chipset A4S2. Note that enabling this will spam your terminal with some million lines of debug output. </p>
<pre>level debug output
----------------------------
 0 nothing
 1 errors
 2 warnings
 3 things nice to know
 4 code flow
 5 detailed code flow
 6 everything</pre>
</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/7-sane/">sane</a></code>(7), <code><a href="/docs/linux/man/5-sane-mustek/">sane-mustek</a></code>(5), <code><a href="/docs/linux/man/5-sane-net/">sane-net</a></code>(5), <code><a href="/docs/linux/man/8-saned/">saned</a></code>(8), <code><a href="/docs/linux/man/1-sane-find-scanner/">sane-find-scanner</a></code>(1), <code><a href="/docs/linux/man/1-scanimage/">scanimage</a></code>(1)</p>
<dl>
<dt>For latest bug fixes and information see</p>
<dd><i><a rel="nofollow" href="http://www.penguin-breeder.org/sane/mustek_pp/">http://www.penguin-breeder.org/sane/mustek_pp/</a></i></p>
<dt>For additional information on the CIS driver, see</p>
<dd><i><a rel="nofollow" href="http://home.scarlet.be/eddy_de_greef/">http://home.scarlet.be/eddy_de_greef/</a></i> </p>
<h2>Authors</h2>
<pre>Jochen Eisinger
&lt;<i>jochen at penguin-breeder dot org</i>&gt;
Eddy De Greef
&lt;<i>eddy_de_greef at scarlet dot be</i>&gt;</pre>
<h2>Bugs</h2>
<p>Too many&#8230; please send bug reports to <i>sane-devel [at] alioth-lists.debian.net</i> (note that you have to subscribe first to the list before you can send emails&#8230; see <i><a rel="nofollow" href="http://www.sane-project.org/mailing-lists.html">http://www.sane-project.org/mailing-lists.html</a></i>). </p>
<h2>Bug Reports</h2>
<p>If something doesn&#8217;t work, please contact us (Jochen for the CCD scanners, Eddy for the CIS scanners). But we need some information about your scanner to be able to help you&#8230; </p>
<dl>
<dt><i>SANE version</i></p>
<dd>Run <i>scanimage -V</i> to determine this.</p>
<dt><i>the backend version and your scanner hardware</i></p>
<dd>Run <i>SANE_DEBUG_MUSTEK_PP=128 scanimage -L</i> as root. If you don&#8217;t get any output from the <code>sane-mustek_pp</code> backend, make sure a line &quot;mustek_pp&quot; is included into your <i>/etc/sane.d/dll.conf</i>. If your scanner isn&#8217;t detected, make sure you&#8217;ve defined the right port address in your <i>mustek_pp.conf</i>.</p>
<dt><i>the name of your scanner/vendor also a worthy information. Please also include the</i></p>
<dd>optical resolution and lamp type of your scanner, both can be found in the manual of your scanner.</p>
<dt><i>any further comments</i></p>
<dd>if you have comments about the documentation (what could be done better), or you think I should know something, please include it. </p>
</dl>
