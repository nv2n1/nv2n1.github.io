---
title: "ledmon(8)"
name: "ledmon"
section: "8"
letter: "l"
url: "/docs/linux/man/8-ledmon/"
description: "ledmon – Intel(R) LED monitor service for storage enclosures."
---

<p>ledmon &#8211; Intel(R) LED monitor service for storage enclosures.</p>
<h2>Synopsis</h2>
<p><code>ledmon</code> [<i></i><i>OPTIONS</i><i></i>]</p>
<h2>Description</h2>
<p>The ledmon application is a daemon process used to monitor a state of software RAID devices (md only) or a state of block devices. The state is visualizing on LEDs associated to each slot in an enclosure or a drive bay. There are two types of system: 2-LEDs system (Activity LED, Status LED) and 3-LEDs system (Activity LED, Locate LED, Fail LED). This application has the highest priority when accessing the LEDs. </p>
<p> The ledmon application uses SGPIO and SES-2 protocol to control LEDs. The program implements IBPI patterns of SFF-8489 specification for SGPIO. Please note some enclosures do not stick close to SFF-8489 specification. It might happen that enclosure processor will accept IBPI pattern but it will blink LEDs not according to SFF-8489 specification or it has limited number of patterns supported. </p>
<p> LED management (AHCI) and SAF-TE protocols are not supported. </p>
<p> There&#8217;s no method provided to specify which RAID volume should be monitored and which not. The ledmon application monitors all RAID devices and visualizes their state. </p>
<p> The ledmon application has been verified to work with Intel(R) storage controllers (i.e. Intel(R) AHCI controller and Intel(R) SAS controller). The application might work with storage controllers of other vendors (especially SAS/SCSI controllers). However storage controllers of other vendors have not been tested. </p>
<p> The ledmon application is part of Intel(R) Enclosure LED Utilities. Only single instance of the application is allowed.</p>
<h2>Options</h2>
<dl>
<dt><code>-c</code> or <code>&#8211;config</code>=<i>path</i></dt>
<dd>Sets a path to local configuration file. If this option is specified the global configuration file and user configuration file has no effect.</dd>
<dt><code>-l</code> or <code>&#8211;log</code>=<i>path</i></dt>
<dd>Sets a path to local log file. If this option is specified the global log file <i>/var/log/ledmon.log</i> is not used.</dd>
<dt><code>-t</code> or <code>&#8211;interval</code>=<i>seconds</i></dt>
<dd>Sets time interval between scans of sysfs. The value is given in seconds. The minimum is 5 seconds the maximum is not specified.</dd>
<dt><code>&#8211;quiet</code> or <code>&#8211;error</code> or <code>&#8211;warning</code> or <code>&#8211;info</code> or <code>&#8211;debug</code> or <code>&#8211;all</code></dt>
<dd>Verbose level &#8211; &#8216;quiet&#8217; means no logging at all and &#8216;all&#8217; means to log everything. The levels are given in order. If user specifies more then one verbose option the last option comes into effect.</dd>
<dt><code>-h</code> or <code>&#8211;help</code></dt>
<dd>Prints this text out and exits.</dd>
<dt><code>-v</code> or <code>&#8211;version</code></dt>
<dd>Displays version of ledmon and information about the license and exits.</dd></dl>
<h2>Files</h2>
<dl>
<dt><i>/var/log/ledmon.log</i></dt>
<dd>Global log file, used by ledmon application. To force logging to user defined file use <i>-l</i> option switch.</dd>
<dt><i>~/.ledctl</i></dt>
<dd>User configuration file, shared between ledmon and all ledctl application instances.</dd>
<dt><i>/etc/ledcfg.conf</i></dt>
<dd>Global configuration file, shared between ledmon and all ledctl application instances.</dd></dl>
<h2>License</h2>
<p>Copyright (c) 2009-2016 Intel Corporation. </p>
<p> This program is distributed under the terms of the GNU General Public License as published by the Free Software Foundation. See the build-in help for details on the License and the lack of warranty.</p>
<h2>Bugs</h2>
<p>The ledmon application does not recognize PFA state (Predicted Failure Analysis), hence the PFA pattern from SFF-8489 specification is not visualized.</p>
<h2>See Also</h2>
<p><i><a href="/docs/linux/man/8-ledctl/">ledctl</a></i>(8), <i><a href="/docs/linux/man/5-ledctl-conf/">ledctl.conf</a></i>(5)</p>
<h2>Author</h2>
<p>This manual page was written by Artur Wojcik &lt;artur.wojcik [at] intel.com&gt;. It may be used by others.</p>
