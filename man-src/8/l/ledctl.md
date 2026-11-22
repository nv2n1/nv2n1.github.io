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
<p><code>ledctl</code> [<i></i><i>OPTIONS</i><i></i>] <i>pattern_name</i>=<i>list_of_devices</i> &#8230;</p>
<h2>Description</h2>
<p>The ledctl is an user space application designed to control LEDs associated with each slot in an enclosure or a drive bay. The LEDs of devices listed in <i>list_of_devices</i> are set to the given pattern <i>pattern_name</i> and all other LEDs are turned off. User must have root privileges to use this application. </p>
<p> There are two types of systems: 2-LEDs systems (Activity LED, Status LED) and 3-LEDs systems (Activity LED, Locate LED, Fail LED). The ledctl application uses SGPIO and SES-2 protocol to control LEDs. The program implements IBPI patterns of SFF-8489 specification for SGPIO. Please note some enclosures do not stick close to SFF-8489 specification. It might happen that enclosure&#8217;s processor will accept an IBPI pattern but it will blink the LEDs at variance with SFF-8489 specification or it has limited number of patterns supported. </p>
<p> LED management (AHCI) and SAF-TE protocols are not supported. </p>
<p> The ledctl application has been verified to work with Intel(R) storage controllers (i.e. Intel(R) AHCI controller and Intel(R) SAS controller). The application might work with storage controllers of other vendors (especially SCSI/SAS controllers). However, storage controllers of other vendors have not been tested. </p>
<p> The ledmon application has the highest priority when accessing LEDs. It means that some patterns set by ledctl may have no effect if ledmon is running (except Locate pattern). </p>
<p> The ledctl application is a part of Intel(R) Enclosure LED Utilities.</p>
<h3>Pattern Names</h3>
<p>The ledctl application accepts the following names for <i>pattern_name</i> argument according to SFF-8489 specification.</p>
<dl>
<dt><code>locate</code></dt>
<dd>Turns Locate LED associated with the given device(s) or empty slot(s) on.</dd>
<dt><code>locate_off</code></dt>
<dd>Turns only Locate LED off.</dd>
<dt><code>normal</code></dt>
<dd>Turns Status LED, Failure LED and Locate LED off.</dd>
<dt><code>off</code></dt>
<dd>Turns only Status LED and Failure LED off.</dd>
<dt><code>ica</code> or <code>degraded</code></dt>
<dd>Visualizes &#8220;In a Critical Array&#8221; pattern.</dd>
<dt><code>rebuild</code> or <code>rebuild_p</code></dt>
<dd>Visualizes &#8220;Rebuild&#8221; pattern.</dd>
<dt><code>ifa</code> or <code>failed_array</code></dt>
<dd>Visualizes &#8220;In a Failed Array&#8221; pattern.</dd>
<dt><code>hotspare</code></dt>
<dd>Visualizes &#8220;Hotspare&#8221; pattern.</dd>
<dt><code>pfa</code></dt>
<dd>Visualizes &#8220;Predicted Failure Analysis&#8221; pattern.</dd>
<dt><code>failure</code> or <code>disk_failed</code></dt>
<dd>Visualizes &#8220;Failure&#8221; pattern.</dd>
<dt><code>ses_abort</code></dt>
<dd>SES-2 R/R ABORD</dd>
<dt><code>ses_rebuild</code></dt>
<dd>SES-2 REBUILD/REMAP</dd>
<dt><code>ses_ifa</code></dt>
<dd>SES-2 IN FAILED ARRAY</dd>
<dt><code>ses_ica</code></dt>
<dd>SES-2 IN CRIT ARRAY</dd>
<dt><code>ses_cons_check</code></dt>
<dd>SES-2 CONS CHECK</dd>
<dt><code>ses_hotspare</code></dt>
<dd>SES-2 HOT SPARE</dd>
<dt><code>ses_rsvd_dev</code></dt>
<dd>SES-2 RSVD DEVICE</dd>
<dt><code>ses_ok</code></dt>
<dd>SES-2 OK</dd>
<dt><code>ses_ident</code></dt>
<dd>SES-2 IDENT</dd>
<dt><code>ses_rm</code></dt>
<dd>SES-2 REMOVE</dd>
<dt><code>ses_insert</code></dt>
<dd>SES-2 INSERT</dd>
<dt><code>ses_missing</code></dt>
<dd>SES-2 MISSING</dd>
<dt><code>ses_dnr</code></dt>
<dd>SES-2 DO NOT REMOVE</dd>
<dt><code>ses_active</code></dt>
<dd>SES-2 ACTIVE</dd>
<dt><code>ses_enbale_bb</code></dt>
<dd>SES-2 ENABLE BYP B</dd>
<dt><code>ses_enable_ba</code></dt>
<dd>SES-2 ENABLE BYP A</dd>
<dt><code>ses_devoff</code></dt>
<dd>SES-2 DEVICE OFF</dd>
<dt><code>ses_fault</code></dt>
<dd>SES-2 FAULT</dd></dl>
<h3>Patterns Translation</h3>
<p>When non SES-2 pattern is send to device in enclosure automatic translation is being done.</p>
<dl>
<dt><code>locate</code></dt>
<dd><i>locate</i> is translated to <i>ses_ident</i></dd>
<dt><code>locate_off</code></dt>
<dd><i>locate_off</i> is translated to <i>~ses_ident</i></dd>
<dt><code>normal</code></dt>
<dd><i>normal</i> is translated to <i>ses_ok</i></dd>
<dt><code>off</code></dt>
<dd><i>off</i> is translated to <i>ses_ok</i></dd>
<dt><code>degraded</code></dt>
<dd><i>degraded</i> is translated to <i>ses_ica</i></dd>
<dt><code>rebuild</code></dt>
<dd><i>rebuild</i> is translated to <i>ses_rebuild</i></dd>
<dt><code>rebuild_p</code></dt>
<dd><i>rebuild_p</i> is translated to <i>ses_rebuild</i></dd>
<dt><code>failed</code></dt>
<dd><i>failed</i> is translated to <i>ses_ifa</i></dd>
<dt><code>hotspare</code></dt>
<dd><i>hotspare</i> is translated to <i>ses_hotspare</i></dd>
<dt><code>pfa</code></dt>
<dd><i>pfa</i> is translated to <i>ses_rsvd_dev</i></dd>
<dt><code>failure</code></dt>
<dd><i>failure</i> is translated to <i>ses_fault</i></dd>
<dt><code>disk_failed</code></dt>
<dd><i>disk_failed</i> is translated to <i>ses_fault</i></dd></dl>
<h3>List of Devices</h3>
<p>The application accepts a list of devices in two formats. The first format is a list with comma separated elements. The second format is a list in curly braces and elements are separated by space. See examples section bellow for details. </p>
<p> A device is a path to file in /dev directory or in /sys/block directory. It may identify a block device, a RAID device or a container device. In case of a RAID device or a container device a state will be set for all block devices associated, respectively. </p>
<p> The LEDs of devices listed in <i>list_of_devices</i> are set to the given pattern <i>pattern_name</i> and all other LEDs are turned off.</p>
<h2>Options</h2>
<dl>
<dt><code>-c</code> or <code>&#8211;config</code>=<i>path</i></dt>
<dd>Sets a path to local configuration file. If this option is specified the global configuration file and user configuration file has no effect.</dd>
<dt><code>-l</code> or <code>&#8211;log</code>=<i>path</i></dt>
<dd>Sets a path to local log file. If this option is specified the global log file <i>/var/log/ledctl.log</i> is not used.</dd>
<dt><code>-h</code> or <code>&#8211;help</code></dt>
<dd>Prints this text out and exits.</dd>
<dt><code>-v</code> or <code>&#8211;version</code></dt>
<dd>Displays version of ledctl and information about the license and exits.</dd></dl>
<h2>Files</h2>
<dl>
<dt><i>/var/log/ledctl.log</i></dt>
<dd>Global log file, used by all instances of ledctl application. To force logging to user defined file use <i>-l</i> option switch.</dd>
<dt><i>~/.ledctl</i></dt>
<dd>User configuration file, shared between ledmon and all ledctl application instances.</dd>
<dt><i>/etc/ledcfg.conf</i></dt>
<dd>Global configuration file, shared between ledmon and all ledctl application instances.</dd></dl>
<h2>Examples</h2>
<p>The following example illustrates how to locate a single block device. </p>
<pre> ledctl locate=/dev/sda</pre>
<p>The following example illustrates how to turn Locate LED off for the same block device. </p>
<pre> ledctl locate_off=/dev/sda</pre>
<p>The following example illustrates how to locate disks of a RAID device and how to set rebuild pattern for two block devices at the same time. This example uses both formats of device list. </p>
<pre><code>ledctl locate=/dev/md127 rebuild={ /sys/block/sd[a-b] }</code></pre>
<p> The following example illustrates how to turn Status LED and Failure LED off for the given device(s). </p>
<pre><code>ledctl off={ /dev/sda /dev/sdb }</code></pre>
<p> The following example illustrates how to locate a three block devices. This example uses the first format of device list. </p>
<pre> ledctl locate=/dev/sda,/dev/sdb,/dev/sdc</pre>
<h2>License</h2>
<p>Copyright (c) 2009-2016 Intel Corporation. </p>
<p> This program is distributed under the terms of the GNU General Public License as published by the Free Software Foundation. See the built-in help for details on the License and the lack of warranty.</p>
<h2>See Also</h2>
<p><i><a href="/docs/linux/man/8-ledmon/">ledmon</a></i>(8), <i><a href="/docs/linux/man/5-ledctl-conf/">ledctl.conf</a></i>(5)</p>
<h2>Author</h2>
<p>This manual page was written by Artur Wojcik &lt;artur.wojcik [at] intel.com&gt;. It may be used by others.</p>
