---
title: "scsi-rescan(8)"
name: "scsi-rescan"
section: "8"
letter: "s"
url: "/docs/linux/man/8-scsi-rescan/"
description: "rescan-scsi-bus.sh – script for adding and removing SCSI devices without rebooting"
---

<p>rescan-scsi-bus.sh &#8211; script for adding and removing SCSI devices without rebooting</p>
<h2>Synopsis</h2>
<p><code>rescan-scsi-bus.sh</code> [<i>options</i>] [<i>host </i>[<i>host </i>&#8230;]]</p>
<h2>Options</h2>
<dl>
<dt><code>-a</code>, <code>&#8211;alltargets</code></dt>
<dd>scan all targets, not just currently existing [default: disabled]</dd>
<dt><code>-d</code></dt>
<dd>enable debug [default: 0]</dd>
<dt><code>-l</code></dt>
<dd>activates scanning for LUNs 0&#8211;7 [default: 0]</dd>
<dt><code>-L</code> NUM</dt>
<dd>activates scanning for LUNs 0&#8211;NUM [default: 0]</dd>
<dt><code>-w</code>, <code>&#8211;wide</code></dt>
<dd>scan for target device IDs 0&#8211;15 [default: 0&#8211;7]</dd>
<dt><code>-c</code></dt>
<dd>enables scanning of channels 0 1 [default: 0 / all detected ones]</dd>
<dt><code>-r</code>, <code>&#8211;remove</code></dt>
<dd>enables removing of devices [default: disabled]</dd>
<dt><code>-f</code>, <code>&#8211;flush</code></dt>
<dd>flush failed multipath devices [default: disabled]</dd>
<dt><code>-i</code>, <code>&#8211;issue-lip</code></dt>
<dd>issue a FibreChannel LIP reset [default: disabled]</dd>
<dt><code>-m</code>, <code>&#8211;multipath</code></dt>
<dd>update multipath devices [default: disabled]</dd>
<dt><code>-u</code>, <code>&#8211;update</code></dt>
<dd>look for existing disks that have been remapped</dd>
<dt><code>-s</code>, <code>&#8211;resize</code></dt>
<dd>look for resized disks and reload associated multipath devices, if applicable</dd>
<dt><code>&#8211;forcerescan</code></dt>
<dd>rescan existing devices</dd>
<dt><code>&#8211;forceremove</code></dt>
<dd>remove and readd every device (DANGEROUS)</dd>
<dt><code>&#8211;nooptscan</code></dt>
<dd>don&#8217;t stop looking for LUNs if 0 is not found</dd>
<dt><code>&#8211;color</code></dt>
<dd>use coloured prefixes OLD/NEW/DEL</dd>
<dt><code>&#8211;hosts</code>=<i>LIST</i></dt>
<dd>scan only host(s) in <i>LIST</i></dd>
<dt><code>&#8211;channels</code>=<i>LIST</i></dt>
<dd>scan only channel(s) in <i>LIST</i></dd>
<dt><code>&#8211;ids</code>=<i>LIST</i></dt>
<dd>scan only target ID(s) in <i>LIST</i></dd>
<dt><code>&#8211;luns</code>=<i>LIST</i></dt>
<dd>scan only lun(s) in <i>LIST</i></dd>
<dt><code>&#8211;sync</code>, <code>&#8211;nosync</code></dt>
<dd>issue a sync / no sync [default: sync if remove]</dd>
<dt><code>&#8211;attachpq3</code></dt>
<dd>tell kernel to attach sg to LUN 0 that reports PQ=3</dd>
<dt><code>&#8211;reportlun2</code></dt>
<dd>tell kernel to try REPORT_LUN even on SCSI2 devices</dd>
<dt><code>&#8211;largelun</code></dt>
<dd>tell kernel to support LUNs &gt; 7 even on SCSI2 devs</dd>
<dt><code>&#8211;sparselun</code></dt>
<dd>tell kernel to support sparse LUN numbering</dd>
<dd>Host numbers may thus be specified either directly on cmd line (deprecated) or or with the <code>&#8211;hosts</code>=<i>LIST</i> parameter (recommended).</dd></dl>
<p> <i>LIST</i>: A[-B][,C[-D]]&#8230; is a comma separated list of single values and ranges (No spaces allowed.)</p>
<h2>See Also</h2>
<p><code>rescan-scsi-bus.sh</code> Homepage: <code><a rel="nofollow" href="http://www.garloff.de/kurt/linux/#rescan-scsi">http://www.garloff.de/kurt/linux/#rescan-scsi</a></code> <code>sg3_utils</code> Homepage: <code><a rel="nofollow" href="http://sg.danny.cz/sg">http://sg.danny.cz/sg</a></code> </p>
