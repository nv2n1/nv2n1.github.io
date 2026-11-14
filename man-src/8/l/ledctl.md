---
title: "ledctl(8)"
name: "ledctl"
section: "8"
letter: "l"
url: "/docs/linux/man/8-ledctl/"
description: "ledctl – Intel(R) LED control application for a storage enclosures."
---

<p>ledctl &#8211; Intel(R) LED control application for a storage enclosures.</p>
<h2>Synopsis</h2>
<p><code>ledctl</code> [<i></i><font SIZE="-1"><i>OPTIONS</i></font><i></i>] <i>pattern_name</i>=<i>list_of_devices</i> &#8230;</p>
<h2>Description</h2>
<p>The ledctl is an user space application designed to control LEDs associated with each slot in an enclosure or a drive bay. The LEDs of devices listed in <i>list_of_devices</i> are set to the given pattern <i>pattern_name</i> and all other LEDs are turned off. User must have root privileges to use this application. </p>
<p> There are two types of systems: 2-LEDs systems (Activity <font SIZE="-1">LED,</font> Status <font SIZE="-1">LED</font>) and 3-LEDs systems (Activity <font SIZE="-1">LED,</font> Locate <font SIZE="-1">LED,</font> Fail <font SIZE="-1">LED</font>). The ledctl application uses <font SIZE="-1">SGPIO</font> and <font SIZE="-1">SES-2</font> protocol to control LEDs. The program implements <font SIZE="-1">IBPI</font> patterns of <font SIZE="-1">SFF-8489</font> specification for <font SIZE="-1">SGPIO.</font> Please note some enclosures do not stick close to <font SIZE="-1">SFF-8489</font> specification. It might happen that enclosure&#8217;s processor will accept an <font SIZE="-1">IBPI</font> pattern but it will blink the LEDs at variance with <font SIZE="-1">SFF-8489</font> specification or it has limited number of patterns supported. </p>
<p> <font SIZE="-1">LED</font> management (<font SIZE="-1">AHCI</font>) and SAF-TE protocols are not supported. </p>
<p> The ledctl application has been verified to work with Intel(R) storage controllers (i.e. Intel(R) <font SIZE="-1">AHCI</font> controller and Intel(R) <font SIZE="-1">SAS</font> controller). The application might work with storage controllers of other vendors (especially <font SIZE="-1">SCSI/SAS</font> controllers). However, storage controllers of other vendors have not been tested. </p>
<p> The ledmon application has the highest priority when accessing LEDs. It means that some patterns set by ledctl may have no effect if ledmon is running (except Locate pattern). </p>
<p> The ledctl application is a part of Intel(R) Enclosure <font SIZE="-1">LED</font> Utilities.</p>
<h3>Pattern Names</h3>
<p>The ledctl application accepts the following names for <i>pattern_name</i> argument according to <font SIZE="-1">SFF-8489</font> specification.</p>
<dl>
<dt><code>locate</code></p>
<dd>Turns Locate <font SIZE="-1">LED</font> associated with the given device(s) or empty slot(s) on.</p>
<dt><code>locate_off</code></p>
<dd>Turns only Locate <font SIZE="-1">LED</font> off.</p>
<dt><code>normal</code></p>
<dd>Turns Status <font SIZE="-1">LED,</font> Failure <font SIZE="-1">LED</font> and Locate <font SIZE="-1">LED</font> off.</p>
<dt><code>off</code></p>
<dd>Turns only Status <font SIZE="-1">LED</font> and Failure <font SIZE="-1">LED</font> off.</p>
<dt><code>ica</code> or <code>degraded</code></p>
<dd>Visualizes &#8220;In a Critical Array&#8221; pattern.</p>
<dt><code>rebuild</code> or <code>rebuild_p</code></p>
<dd>Visualizes &#8220;Rebuild&#8221; pattern.</p>
<dt><code>ifa</code> or <code>failed_array</code></p>
<dd>Visualizes &#8220;In a Failed Array&#8221; pattern.</p>
<dt><code>hotspare</code></p>
<dd>Visualizes &#8220;Hotspare&#8221; pattern.</p>
<dt><code>pfa</code></p>
<dd>Visualizes &#8220;Predicted Failure Analysis&#8221; pattern.</p>
<dt><code>failure</code> or <code>disk_failed</code></p>
<dd>Visualizes &#8220;Failure&#8221; pattern.</p>
<dt><code>ses_abort</code></p>
<dd><font SIZE="-1">SES-2 R/R ABORD</font></p>
<dt><code>ses_rebuild</code></p>
<dd><font SIZE="-1">SES-2 REBUILD/REMAP</font></p>
<dt><code>ses_ifa</code></p>
<dd><font SIZE="-1">SES-2 IN FAILED ARRAY</font></p>
<dt><code>ses_ica</code></p>
<dd><font SIZE="-1">SES-2 IN CRIT ARRAY</font></p>
<dt><code>ses_cons_check</code></p>
<dd><font SIZE="-1">SES-2 CONS CHECK</font></p>
<dt><code>ses_hotspare</code></p>
<dd><font SIZE="-1">SES-2 HOT SPARE</font></p>
<dt><code>ses_rsvd_dev</code></p>
<dd><font SIZE="-1">SES-2 RSVD DEVICE</font></p>
<dt><code>ses_ok</code></p>
<dd><font SIZE="-1">SES-2 OK</font></p>
<dt><code>ses_ident</code></p>
<dd><font SIZE="-1">SES-2 IDENT</font></p>
<dt><code>ses_rm</code></p>
<dd><font SIZE="-1">SES-2 REMOVE</font></p>
<dt><code>ses_insert</code></p>
<dd><font SIZE="-1">SES-2 INSERT</font></p>
<dt><code>ses_missing</code></p>
<dd><font SIZE="-1">SES-2 MISSING</font></p>
<dt><code>ses_dnr</code></p>
<dd><font SIZE="-1">SES-2 DO NOT REMOVE</font></p>
<dt><code>ses_active</code></p>
<dd><font SIZE="-1">SES-2 ACTIVE</font></p>
<dt><code>ses_enbale_bb</code></p>
<dd><font SIZE="-1">SES-2 ENABLE BYP B</font></p>
<dt><code>ses_enable_ba</code></p>
<dd><font SIZE="-1">SES-2 ENABLE BYP A</font></p>
<dt><code>ses_devoff</code></p>
<dd><font SIZE="-1">SES-2 DEVICE OFF</font></p>
<dt><code>ses_fault</code></p>
<dd><font SIZE="-1">SES-2 FAULT</font></dl>
<h3>Patterns Translation</h3>
<p>When non <font SIZE="-1">SES-2</font> pattern is send to device in enclosure automatic translation is being done.</p>
<dl>
<dt><code>locate</code></p>
<dd><i>locate</i> is translated to <i>ses_ident</i></p>
<dt><code>locate_off</code></p>
<dd><i>locate_off</i> is translated to <i>~ses_ident</i></p>
<dt><code>normal</code></p>
<dd><i>normal</i> is translated to <i>ses_ok</i></p>
<dt><code>off</code></p>
<dd><i>off</i> is translated to <i>ses_ok</i></p>
<dt><code>degraded</code></p>
<dd><i>degraded</i> is translated to <i>ses_ica</i></p>
<dt><code>rebuild</code></p>
<dd><i>rebuild</i> is translated to <i>ses_rebuild</i></p>
<dt><code>rebuild_p</code></p>
<dd><i>rebuild_p</i> is translated to <i>ses_rebuild</i></p>
<dt><code>failed</code></p>
<dd><i>failed</i> is translated to <i>ses_ifa</i></p>
<dt><code>hotspare</code></p>
<dd><i>hotspare</i> is translated to <i>ses_hotspare</i></p>
<dt><code>pfa</code></p>
<dd><i>pfa</i> is translated to <i>ses_rsvd_dev</i></p>
<dt><code>failure</code></p>
<dd><i>failure</i> is translated to <i>ses_fault</i></p>
<dt><code>disk_failed</code></p>
<dd><i>disk_failed</i> is translated to <i>ses_fault</i></dl>
<h3>List of Devices</h3>
<p>The application accepts a list of devices in two formats. The first format is a list with comma separated elements. The second format is a list in curly braces and elements are separated by space. See examples section bellow for details. </p>
<p> A device is a path to file in /dev directory or in /sys/block directory. It may identify a block device, a <font SIZE="-1">RAID</font> device or a container device. In case of a <font SIZE="-1">RAID</font> device or a container device a state will be set for all block devices associated, respectively. </p>
<p> The LEDs of devices listed in <i>list_of_devices</i> are set to the given pattern <i>pattern_name</i> and all other LEDs are turned off.</p>
<h2>Options</h2>
<dl>
<dt><code>-c</code> or <code>&#8211;config</code>=<i>path</i></p>
<dd>Sets a path to local configuration file. If this option is specified the global configuration file and user configuration file has no effect.</p>
<dt><code>-l</code> or <code>&#8211;log</code>=<i>path</i></p>
<dd>Sets a path to local log file. If this option is specified the global log file <i>/var/log/ledctl.log</i> is not used.</p>
<dt><code>-h</code> or <code>&#8211;help</code></p>
<dd>Prints this text out and exits.</p>
<dt><code>-v</code> or <code>&#8211;version</code></p>
<dd>Displays version of ledctl and information about the license and exits.</dl>
<h2>Files</h2>
<dl>
<dt><i>/var/log/ledctl.log</i></p>
<dd>Global log file, used by all instances of ledctl application. To force logging to user defined file use <i>-l</i> option switch.</p>
<dt><i>~/.ledctl</i></p>
<dd>User configuration file, shared between ledmon and all ledctl application instances.</p>
<dt><i>/etc/ledcfg.conf</i></p>
<dd>Global configuration file, shared between ledmon and all ledctl application instances.</dl>
<h2>Examples</h2>
<p>The following example illustrates how to locate a single block device. </p>
<pre> ledctl locate=/dev/sda</pre>
<p>The following example illustrates how to turn Locate <font SIZE="-1">LED</font> off for the same block device. </p>
<pre> ledctl locate_off=/dev/sda</pre>
<p>The following example illustrates how to locate disks of a <font SIZE="-1">RAID</font> device and how to set rebuild pattern for two block devices at the same time. This example uses both formats of device list. </p>
<pre><code>ledctl locate=/dev/md127 rebuild={ /sys/block/sd[a-b] }</code></pre>
<p> The following example illustrates how to turn Status <font SIZE="-1">LED</font> and Failure <font SIZE="-1">LED</font> off for the given device(s). </p>
<pre><code>ledctl off={ /dev/sda /dev/sdb }</code></pre>
<p> The following example illustrates how to locate a three block devices. This example uses the first format of device list. </p>
<pre> ledctl locate=/dev/sda,/dev/sdb,/dev/sdc</pre>
<h2>License</h2>
<p>Copyright (c) 2009-2016 Intel Corporation. </p>
<p> This program is distributed under the terms of the <font SIZE="-1">GNU</font> General Public License as published by the Free Software Foundation. See the built-in help for details on the License and the lack of warranty.</p>
<h2>See Also</h2>
<p><i><a href="/docs/linux/man/8-ledmon/">ledmon</a></i>(8), <i><a href="/docs/linux/man/5-ledctl-conf/">ledctl.conf</a></i>(5)</p>
<h2>Author</h2>
<p>This manual page was written by Artur Wojcik &lt;artur.wojcik [at] intel.com&gt;. It may be used by others.</p>
