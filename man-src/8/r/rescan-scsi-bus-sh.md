---
title: "rescan-scsi-bus-sh(8)"
name: "rescan-scsi-bus-sh"
section: "8"
letter: "r"
url: "/docs/linux/man/8-rescan-scsi-bus-sh/"
description: "rescan-scsi-bus.sh – script for adding and removing SCSI devices without rebooting"
---

<p>rescan-scsi-bus.sh &#8211; script for adding and removing SCSI devices without rebooting</p>
<h2>Synopsis</h2>
<p><code>rescan-scsi-bus.sh</code> [<i>options</i>] [<i>host </i>[<i>host </i>&#8230;]]</p>
<h2>Options</h2>
<dl>
<dt><code>-a</code>, <code>&#8211;alltargets</code></p>
<dd>scan all targets, not just currently existing [default: disabled]</p>
<dt><code>-d</code></p>
<dd>enable debug [default: 0]</p>
<dt><code>-l</code></p>
<dd>activates scanning for LUNs 0&#8211;7 [default: 0]</p>
<dt><code>-L</code> NUM</p>
<dd>activates scanning for LUNs 0&#8211;NUM [default: 0]</p>
<dt><code>-w</code>, <code>&#8211;wide</code></p>
<dd>scan for target device IDs 0&#8211;15 [default: 0&#8211;7]</p>
<dt><code>-c</code></p>
<dd>enables scanning of channels 0 1 [default: 0 / all detected ones]</p>
<dt><code>-r</code>, <code>&#8211;remove</code></p>
<dd>enables removing of devices [default: disabled]</p>
<dt><code>-f</code>, <code>&#8211;flush</code></p>
<dd>flush failed multipath devices [default: disabled]</p>
<dt><code>-i</code>, <code>&#8211;issue-lip</code></p>
<dd>issue a FibreChannel LIP reset [default: disabled]</p>
<dt><code>-m</code>, <code>&#8211;multipath</code></p>
<dd>update multipath devices [default: disabled]</p>
<dt><code>-u</code>, <code>&#8211;update</code></p>
<dd>look for existing disks that have been remapped</p>
<dt><code>-s</code>, <code>&#8211;resize</code></p>
<dd>look for resized disks and reload associated multipath devices, if applicable</p>
<dt><code>&#8211;forcerescan</code></p>
<dd>rescan existing devices</p>
<dt><code>&#8211;forceremove</code></p>
<dd>remove and readd every device (DANGEROUS)</p>
<dt><code>&#8211;nooptscan</code></p>
<dd>don&#8217;t stop looking for LUNs if 0 is not found</p>
<dt><code>&#8211;color</code></p>
<dd>use coloured prefixes OLD/NEW/DEL</p>
<dt><code>&#8211;hosts</code>=<i>LIST</i></p>
<dd>scan only host(s) in <i>LIST</i></p>
<dt><code>&#8211;channels</code>=<i>LIST</i></p>
<dd>scan only channel(s) in <i>LIST</i></p>
<dt><code>&#8211;ids</code>=<i>LIST</i></p>
<dd>scan only target ID(s) in <i>LIST</i></p>
<dt><code>&#8211;luns</code>=<i>LIST</i></p>
<dd>scan only lun(s) in <i>LIST</i></p>
<dt><code>&#8211;sync</code>, <code>&#8211;nosync</code></p>
<dd>issue a sync / no sync [default: sync if remove]</p>
<dt><code>&#8211;attachpq3</code></p>
<dd>tell kernel to attach sg to LUN 0 that reports PQ=3</p>
<dt><code>&#8211;reportlun2</code></p>
<dd>tell kernel to try REPORT_LUN even on SCSI2 devices</p>
<dt><code>&#8211;largelun</code></p>
<dd>tell kernel to support LUNs &gt; 7 even on SCSI2 devs</p>
<dt><code>&#8211;sparselun</code></p>
<dd>tell kernel to support sparse LUN numbering</p>
<dd>Host numbers may thus be specified either directly on cmd line (deprecated) or or with the <code>&#8211;hosts</code>=<i>LIST</i> parameter (recommended).</dl>
<p> <i>LIST</i>: A[-B][,C[-D]]&#8230; is a comma separated list of single values and ranges (No spaces allowed.)</p>
<h2>See Also</h2>
<p><code>rescan-scsi-bus.sh</code> Homepage: <code><a rel="nofollow" href="http://www.garloff.de/kurt/linux/#rescan-scsi">http://www.garloff.de/kurt/linux/#rescan-scsi</a></code> <code>sg3_utils</code> Homepage: <code><a rel="nofollow" href="http://sg.danny.cz/sg">http://sg.danny.cz/sg</a></code> </p>
