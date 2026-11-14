---
title: "sane-plustek_pp(5)"
name: "sane-plustek_pp"
section: "5"
letter: "s"
url: "/docs/linux/man/5-sane-plustek_pp/"
description: "sane-plustek_pp – SANE backend for Plustek parallel port flatbed scanners"
---

<p>sane-plustek_pp &#8211; SANE backend for Plustek parallel port flatbed scanners</p>
<h2>Description</h2>
<p>The <code>sane-plustek_pp</code> library implements a SANE (Scanner Access Now Easy) backend that provides access to Plustek ASIC 9600[1/3] and P9800[1/3] based parallel port flatbed scanners. The access of the scanner is either done directly by the backend or via kernel module, called pt_drv which can be created out of the <code>sane-plustek_pp</code> backend code &#8211; see also section <code>BUILDING THE KERNEL MODULE</code> for further information. </p>
<h2>Supported Devices</h2>
<p>At present, the following scanners should work with this backend and/or the kernel module: </p>
<p> <code>PLUSTEK SCANNERS</code> </p>
<pre>Parallelport Model: ASIC: Properties:
---------------------- ----- ------------------------
OpticPro PT12 98003 600x1200 dpi 36bit 512Kb
OpticPro P12 98003 600x1200 dpi 36bit 512Kb
OpticPro 9636T/12000T 98001 600x1200 dpi 36bit 512Kb
OpticPro 12000P Turbo 98001 600x1200 dpi 36bit 512Kb
OpticPro 9636P+/Turbo 98001 600x1200 dpi 36bit 512Kb
OpticPro 9636P 96003 600x1200 dpi 36bit 128Kb
OpticPro 12000P/96000P 96003 600x1200 dpi 36bit 128Kb
OpticPro 1236P 96003 600x1200 dpi 30bit 128Kb
OpticPro 9600P 96003 600x1200 dpi 30bit 128Kb
OpticPro 9630P/FBIV 96003 600x1200 dpi 30bit 128Kb
OpticPro 9630PL (14&quot;) 96003 600x1200 dpi 30bit 128Kb
OpticPro A3I 96003 400x800 dpi 36bit 128Kb
OpticPro 600P/6000P 96003 300x600 dpi 30bit 32Kb
OpticPro 4831P 96003 300x600 dpi 30bit 32Kb
OpticPro 4830P/FBIII 96003 300x600 dpi 30bit 32Kb
OpticPro 4800P/FBII 96001 300x600 dpi 24bit 32Kb</pre>
<p><code>PRIMAX SCANNERS</code> </p>
<p> There are some scanners sold by Primax, but they are in fact Plustek devices. These scanners are also supported. The following table will show the relationship: </p>
<pre>Model: Plustek Model: Remarks:
--------------------------- -------------- ------------
Colorado 4800 OpticPro 4800 not tested
Compact 4800 Direct OpticPro 600 mov=2
Compact 4800 Direct 30bit OpticPro 4830 mov=7
Compact 9600 Direct 30bit OpticPro 9630 works</pre>
<p><code>GENIUS SCANNERS</code> </p>
<p> The following devices are sold as Genius Scanners, but are in fact Plustek devices. The table will show the relationship: </p>
<pre>Model: Remarks:
--------------------------- ----------------------------
Colorpage Vivid III V2 Like P12 but has two buttons
 and Wolfson DAC</pre>
<p><code>ARIES SCANNERS</code> </p>
<p> There&#8217;s one scanner sold as Aries Scanner, but is in fact a Plustek device. The following table will show the relationship: </p>
<pre>Model: Plustek Model: Remarks:
--------------------------- -------------- ------------
Scan-It 4800 OpticPro 600 mov=2</pre>
<p><code>BrightScan SCANNERS</code> </p>
<p> There&#8217;s one scanner sold as BrightScan OpticPro Scanner, this is also a rebadged Plustek device. The following table will show the relationship: </p>
<pre>Model: Remarks:
--------------------------- ----------------------------
BrightScan OpticPro OpticPro P12</pre>
<h2>Device Names</h2>
<p>This backend works in two modes, the so called &quot;direct-mode&quot; and the &quot;kernel-mode&quot;. In direct-mode, the user-space backend is used, in kernel-mode, you should have a kernel-module named pt_drv loaded. This backends default device is: </p>
<dl>
<dd><i>0x378</i></dl>
<p> This &quot;default device&quot; will be used, if no configuration file can be found. It is rather the base address of the parallel port on i386 machines. </p>
<p> As the backend supports up to four devices, it is possible to specify them in the configuration file </p>
<dl>
<dd><i>/etc/sane.d/plustek_pp.conf</i></dl>
<p> See this file for examples.</p>
<h2>Configuration</h2>
<p>This section describes the backend&#8217;s configuration file entries. The file is located at: <i>/etc/sane.d/plustek_pp.conf</i> </p>
<p> For a proper setup, you will need at least two entries:</p>
<dl>
<dd><i>[direct]</i><br />
 <i>device 0x378</i></dl>
<p> or</p>
<dl>
<dd><i>[kernel]</i><br />
 <i>device /dev/pt_drv</i></dl>
<p> <i>direct</i> tells the backend, that the following devicename (here <i>0x378</i>) has to be interpreted as parallel port scanner device. In fact it is the address to use, alternatively you can use <i>/dev/parport0</i> if the backend has been compiled with libieee1284 support. <i>kernel</i> should only be used, when a kernel-module has been built out of the backend sources. See below for more instructions about this. </p>
<p> Further options: </p>
<p> option warmup t</p>
<dl>
<dd><i>t</i> specifies the warmup period in seconds</dl>
<p> option lampOff t</p>
<dl>
<dd><i>t</i> is the time in seconds for switching off the lamps in standby mode</dl>
<p> option lOffonEnd b</p>
<dl>
<dd><i>b</i> specifies the behaviour when closing the backend, 1 &#8211;&gt; switch lamps off, 0 &#8211;&gt; do not change lamp status</dl>
<p> option mov m</p>
<dl>
<dd><i>m</i> is the model override switch, which only works in direct mode.</p>
<dl>
<dt><i>m</i> = 0</p>
<dd>default: no override</p>
<dt><i>m</i> = 1</p>
<dd>OpticPro 9630PL override (works if OP9630 has been detected) forces legal size (14&quot;)</p>
<dt><i>m</i> = 2</p>
<dd>Primax 4800Direct override (works if OP600 has been detected) swaps red/green color</p>
<dt><i>m</i> = 3</p>
<dd>OpticPro 9636 override (works if OP9636 has been detected) disables backends transparency/negative capabilities</p>
<dt><i>m</i> = 4</p>
<dd>OpticPro 9636P override (works if OP9636 has been detected) disables backends transparency/negative capabilities</p>
<dt><i>m</i> = 5</p>
<dd>OpticPro A3I override (works if OP12000 has been detected) enables A3 scanning</p>
<dt><i>m</i> = 6</p>
<dd>OpticPro 4800P override (works if OP600 has been detected) swaps red/green color</p>
<dt><i>m</i> = 7</p>
<dd>Primax 4800Direct 30bit override (works if OP4830 has been detected)</dl>
</dl>
<p> See the <i>plustek_pp.conf</i> file for examples.</p>
<h2>Building The Kernel Module</h2>
<p>As mentioned before, the <code>sane-plustek_pp</code> backend code can also be compiled and installed as linux kernel module. To do so, you will need the source-files of this sane-backend installation. Unpack this tar-ball and go to the directory: <i>sane-backends/doc/plustek</i>. Within this directory, you should find a script called: <i>MakeModule.sh</i>. Now if your Linux kernelsources are installed correctly, it should be possible to build, install and load the module <code>pt_drv</code>. <code>Please note,</code> that the kernelsources need to be configured correctly. Refer to your distributions manual on how this is done. As root user, try </p>
<p> <i>./MakeModule.sh</i> </p>
<p> the script will try and get all necessary information about your running kernel and will lead you through the whole installation process.<br />
 <code>Note: Installing and loading the can only be done as</code> superuser.</p>
<h2>Kernel Module Setup</h2>
<p>The configuration of the kernel module is done by providing some or more options found below to the kernel module at load time. This can be done by invoking <code><a href="/docs/linux/man/8-insmod/">insmod</a></code>(8) with the appropriate parameters or appending the options to the file <i>/etc/modules.conf (kernel &lt; 2.6.x)</i> or <i>/etc/modprobe.conf (kernel &gt;= 2.6.x)</i> </p>
<p> <code>The Options:</code><br />
 lampoff=lll</p>
<dl>
<dd>The value <i>lll</i> tells the driver, after how many seconds to switch-off the lamp(s). The default value is 180. 0 will disable this feature.<br />
 <code>HINT:</code> Do not use a value that is too small, because often switching on/off the lamps will reduce their lifetime.</dl>
<p> port=ppp</p>
<dl>
<dd><i>ppp</i> specifies the port base address, where the scanner is connected to. The default value is 0x378, which is normally a standard.</dl>
<p> warmup=www</p>
<dl>
<dd><i>www</i> specifies the time in seconds, how long a lamp has to be on, until the driver will start to scan. The default value is 30.</dl>
<p> lOffonEnd=e</p>
<dl>
<dd><i>e</i> specifies the behaviour when unloading the driver, 1 &#8211;&gt; switch lamps off, 0 &#8211;&gt; do not change lamp status</dl>
<p> slowIO=s</p>
<dl>
<dd><i>s</i> specifies which I/O functions the driver should use, 1 &#8211;&gt; use delayed functions, 0 &#8211;&gt; use the non-delayed ones</dl>
<p> forceMode=fm</p>
<dl>
<dd><i>fm</i> specifies port mode which should be used, 0 &#8211;&gt; autodetection, 1 &#8211;&gt; use SPP mode and 2 &#8211;&gt; use EPP mode</dl>
<p> mov=m</p>
<dl>
<dd>
<dl>
<dt><i>m</i> = 0</p>
<dd>default: no override</p>
<dt><i>m</i> = 1</p>
<dd>OpticPro 9630PL override (works if OP9630 has been detected) forces legal size (14&quot;)</p>
<dt><i>m</i> = 2</p>
<dd>Primax 4800Direct override (works if OP600 has been detected) swaps red/green color</p>
<dt><i>m</i> = 3</p>
<dd>OpticPro 9636 override (works if OP9636 has been detected) disables backends transparency/negative capabilities</p>
<dt><i>m</i> = 4</p>
<dd>OpticPro 9636P override (works if OP9636 has been detected) disables backends transparency/negative capabilities</p>
<dt><i>m</i> = 5</p>
<dd>OpticPro A3I override (works if OP12000 has been detected) enables A3 scanning</p>
<dt><i>m</i> = 6</p>
<dd>OpticPro 4800P override (works if OP600 has been detected) swaps red/green color</p>
<dt><i>m</i> = 7</p>
<dd>Primax 4800Direct 30bit override (works if OP4830 has been detected)</dl>
</dl>
<p> Sample entry for file <i>/etc/modules.conf</i>: </p>
<dl>
<dd>alias char-major-40 pt_drv<br />
 pre-install pt_drv modprobe -k parport<br />
 options pt_drv lampoff=180 warmup=15 port=0x378 lOffonEnd=0 mov=0 slowIO=0 forceMode=0</dl>
<p> For multidevice support, simply add values separated by commas to the different options </p>
<dl>
<dd>options pt_drv port=0x378,0x278 mov=0,4 slowIO=0,1 forceMode=0,1</dl>
<p> Remember to call <code><a href="/docs/linux/man/8-depmod/">depmod</a></code>(8) after changing <i>/etc/conf.modules</i>.</p>
<h2>Parallel Port Modes</h2>
<p>The current driver works best, when the parallel port has been set to EPP-mode. When detecting any other mode such as ECP or PS/2 the driver tries to set to a faster, supported mode. If this fails, it will use the SPP mode, as this mode should work with all Linux supported parallel ports. If in doubt, enter your BIOS and set it to any mode except ECP. </p>
<p> Former Plustek scanner models (4830, 9630) supplied a ISA parallel port adapter card. This card is <code>not</code> supported by the driver. </p>
<p> The ASIC 96001/3 based models have sometimes trouble with high resolution modes. If you encounter sporadic corrupted images (parts duplicated or shifted horizontally) kill all other applications before scanning and (if sufficient memory available) disable swapping. </p>
<p> See the <i>plustek_pp.conf</i> file for examples.</p>
<h2>Files</h2>
<dl>
<dt><i>/etc/sane.d/plustek_pp.conf</i></p>
<dd>The backend configuration file</p>
<dt><i>/usr/lib/x86_64-linux-gnu/sane/libsane-plustek_pp.a</i></p>
<dd>The static library implementing this backend.</p>
<dt><i>/usr/lib/x86_64-linux-gnu/sane/libsane-plustek_pp.so</i></p>
<dd>The shared library implementing this backend (present on systems that support dynamic loading).</p>
<dt><i>/lib/modules/&lt;Kernel-Version&gt;/kernel/drivers/parport/pt_drv.o</i></p>
<dd>The Linux kernelmodule for kernels &lt; 2.6.x.</p>
<dt><i>/lib/modules/&lt;Kernel-Version&gt;/kernel/drivers/parport/pt_drv.ko</i></p>
<dd>The Linux kernelmodule for kernels &gt;= 2.6.x.</dl>
<h2>Environment</h2>
<dl>
<dt><code>SANE_CONFIG_DIR</code></p>
<dd>This environment variable specifies the list of directories that may contain the configuration file. On *NIX systems, the directories are separated by a colon (`:&#8217;), under OS/2, they are separated by a semi-colon (`;&#8217;). If this variable is not set, the configuration file is searched in two default directories: first, the current working directory (&quot;.&quot;) and then in <i>/etc/sane.d</i>. If the value of the environment variable ends with the directory separator character, then the default directories are searched after the explicitly specified directories. For example, setting <code>SANE_CONFIG_DIR</code> to &quot;/tmp/config:&quot; would result in directories <i>tmp/config</i>, <i>.</i>, and <i>/etc/sane.d</i> being searched (in this order).</p>
<dt><code>SANE_DEBUG_PLUSTEK_PP</code></p>
<dd>If the library was compiled with debug support enabled, this environment variable controls the debug level for this backend. Higher debug levels increase the verbosity of the output. </p>
<p> Example: export SANE_DEBUG_PLUSTEK_PP=10 </p>
</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/7-sane/">sane</a></code>(7), <code><a href="/docs/linux/man/1-xscanimage/">xscanimage</a></code>(1),<br />
 <i>/usr/share/doc/libsane/plustek/Plustek-PARPORT.changes</i> </p>
<h2>Contact And Bug-Reports</h2>
<p>Please send any information and bug-reports to:<br />
 <code>SANE Mailing List</code> </p>
<p> Additional info and hints can be obtained from our<br />
 Mailing-List archive at:<br />
 <i><a rel="nofollow" href="http://www.sane-project.org/mailing-lists.html">http://www.sane-project.org/mailing-lists.html</a></i> </p>
<p> To obtain debug messages from the backend, please set the environment-variable <code>SANE_DEBUG_PLUSTEK_PP</code> before calling your favorite scan-frontend (i.e. <code><a href="/docs/linux/man/1-xscanimage/">xscanimage</a></code>(1)),<code>i.e.:</code><br />
 <i>export SANE_DEBUG_PLUSTEK_PP=20 ; xscanimage</i> </p>
<p> The value controls the verbosity of the backend.</p>
<h2>KNOWN BUGS &amp; RESTRICTIONS</h2>
<p>* The Halftoning works, but the quality is poor </p>
<p> * Printers (especially HP models) will start to print during scanning. This in fact is a problem to other printers too, using bidirectional protocol (see <a rel="nofollow" href="http://www.plustek.com">www.plustek.com</a> (TAIWAN) page for further details) </p>
<p> * The driver does not support these manic scalings up to 16 times the physical resolution. The only scaling is done on resolutions between the physical resolution of the CCD-sensor and the stepper motor i.e. you have a 600&#215;1200 dpi scanner and you are scanning using 800dpi, so scaling is necessary, because the sensor only delivers 600dpi but the motor is capable to perform 800dpi steps. </p>
<p> * On some devices, the pictures seems bluish </p>
<p> <i>ASIC 98001 based models:</i> </p>
<p> * The 300dpi transparency and negative mode does not work correctly. </p>
<p> * There is currently no way to distinguish a model with and without transparency unit. </p>
<p> * The scanned images seem to be too dark (P9636T) </p>
<p> <i>ASIC 96003/1 based models:</i> </p>
<p> * 30bit mode is currently not supported. </p>
<p> * On low end systems under heavy system load the driver may lose data, which can result in picture corruption or cause the sensor to hit the scan bed. </p>
<p> * The scanning speed on 600&#215;1200 dpi models is slow. </p>
<p> * The scanning quality of the A3I is poor.</p>
