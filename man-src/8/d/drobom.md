---
title: "drobom(8)"
name: "drobom"
section: "8"
letter: "d"
url: "/docs/linux/man/8-drobom/"
description: "drobom – CLI for managing data robotics (drobo) storage units"
---

<p>drobom &#8211; CLI for managing data robotics (drobo) storage units</p>
<h2>Synopsis</h2>
<p><code>drobom</code> [ <i>options</i> ] <i>&lt;command&gt; </i>[ <i>arguments</i>&#8230; ]</p>
<h2>Description</h2>
<h3>options is one of:</h3>
<dl>
<dt>-c, &#8211;command</p>
<dd>the command to execute.</p>
<dt>-d, &#8211;device</p>
<dd>the device to operate on (default searches all devices and picks first one found.)</p>
<dt>-h, &#8211;help</p>
<dd>print a usage message</p>
<dt>-n, &#8211;no</p>
<dd>answer all questions no (generally does not do any damage)</p>
<dt>-s, &#8211;string &lt;string&gt;</p>
<dd>sometimes new models are not recognized by drobom. See documentation.</p>
<dt>-v, &#8211;verbose</p>
<dd>verbosity, a bit-field to trigger increased output as needed, mostly for debugging. 1 &#8211; General, 2 &#8211; Hardware Dialog, 4 &#8211; Initiation, 8 &#8211; Raw returns, 16- Detection 64 will print everything&#8230; (default: 0, as terse as possible.) 128 enables simulation mode (for testing when no Drobo is available. Dangerous!)</p>
<dt>-V, &#8211;version</p>
<dd>print the version id.</p>
<dt>
&nbsp;<wbr>-y, &#8211;yes&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></p>
<dd>answer all questions yes (generally overwrites stuff)</dl>
<h3>command is one of:</h3>
<dl>
<dt>blink</p>
<dd>identify the drobo by making the lights blink</p>
<dt>diag</p>
<dd>dump diagnostics file into /tmp directory</p>
<dt>diagprint &lt;diagdumpfile&gt;</p>
<dd>print diagnostics file to standard output<br />
 &lt;diagdumpfile&gt; the diagnostic dump file to read.</p>
<dt>fwcheck query drobo.com for updates to firmware for the given Drobo</p>
<dd>
<dt>fwload &lt;fwimage&gt;</p>
<dd>load a specific firmware for the given Drobo. Arguments:<br />
 &lt;fwimage&gt; the firmware file to load.</p>
<dt>fwupgrade</p>
<dd>upgrade the firmware to the latest and greatest, recommended by DRI</p>
<dt>help</p>
<dd>print this text</p>
<dt>info &lt;toprint&gt;</p>
<dd>print information on a Drobo. The &lt;toprint&gt; argument is a comma separated list of the values below (default is to print all of them): config, capacity, protocol, settings, slots, firmware, status, options, luns, scsi</p>
<dt>list</p>
<dd>show device files for all Drobos found.</p>
<dt>set &lt;options&gt; &lt;value&gt;</p>
<dd>set firmware options, such as ipaddress, etc&#8230; use &#8216;info settings&#8217;</p>
<dt>set name &lt;newname&gt;</p>
<dd>Set the name of the Drobo to the given value ( only firmware &gt; 1.3.0 supports this command )</p>
<dt>set lunsize Set the size of LUNS on device. Arguments:</p>
<dd>&lt;sz&gt; integer number of TiB to set the lunsize to Note: After execution, Drobo reboots, wait a few minutes before accessing again</p>
<dt>set time &#8211; sets various Drobo&#8217;s clock to UTC</p>
<dd>
<dt>shutdown</p>
<dd>shutdown drobo (DRI calls this &#8216;standby&#8217;)</p>
<dt>status</p>
<dd>report how is the Drobo doing</dl>
<h3>device</h3>
<p>raw block device of a drobo (i.e. /dev/sdz) . If not given, assumes all attached drobos.</p>
<dl>
<dt>view</p>
<dd>Start up the graphical user interface. </p>
<h2>Author</h2>
<p>This manual page was written by Chris AtLee &lt;chris [at] atlee.ca&gt; for the Debian project (but may be used by others).</p>
