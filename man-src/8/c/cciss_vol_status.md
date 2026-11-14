---
title: "cciss_vol_status(8)"
name: "cciss_vol_status"
section: "8"
letter: "c"
url: "/docs/linux/man/8-cciss_vol_status/"
description: "cciss_vol_status – show status of logical drives attached to HP Smartarray controllers"
---

<p>cciss_vol_status &#8211; show status of logical drives attached to HP Smartarray controllers</p>
<h2>Synopsis</h2>
<p><code>cciss_vol_status</code> [<i>OPTION</i>] [<i>DEVICE</i>]&#8230;</p>
<h2>Description</h2>
<p>Shows the status of logical drives configured on HP Smartarray controllers.</p>
<h2>Options</h2>
<dl>
<dt><code>-p, &#8211;persnickety</code></p>
<dd>Without this option, device nodes which can&#8217;t be opened, or which are not found to be of the correct device type are silently ignored. This lets you use wildcards, e.g.: cciss_vol_status /dev/sg* /dev/cciss/c*d0, and the program will not complain as long as all devices which are found to be of the correct type are found to be ok. However, you may wish to explicitly list the devices you expect to be there, and be notified if they are not there (e.g. perhaps a PCI slot has died, and the system has rebooted, so that what was once /dev/cciss/c1d0 is no longer there at all). This option will cause the program to complain about any device node listed which does not appear to be the right device type, or is not openable.</p>
<dt><code>-C, &#8211;copyright</code></p>
<dd>If stderr is a terminal, Print out a copyright message, and exit.</p>
<dt><code>-q, &#8211;quiet</code></p>
<dd>This option doesn&#8217;t do anything. Previously, without this option and if stderr is a terminal, a copyright message precedes the normal program output. Now, the copyright message is only printed via the -C option.</p>
<dt><code>-s</code></p>
<dd>Query each physical drive for S.M.A.R.T data and report any drives in &quot;predictive failure&quot; state.</p>
<dt><code>-u, &#8211;try-unknown-devices</code></p>
<dd>If a device has an unrecognized board ID, normally the program will not attempt to communicate with it. In case you have some Smart Array controller which is newer than this program, the program may not recognize it. This option permits the program to attempt to interrogate the board even if it is unrecognized on the assumption that it is in fact a Smart Array of some kind.</p>
<dt><code>-v, &#8211;version</code></p>
<dd>Print the version number and exit.</p>
<dt><code>-V, &#8211;verbose</code></p>
<dd>Print out more information about the controllers and physical drives. For each controller, the board ID, number of logical drives, currently running firmware revision and ROM firmware revision are printed. For each physical drive, the location, vendor, model, serial number, and firmware revision are printed.</p>
<dt><code>-x, &#8211;exhaustive</code></p>
<dd>Deprecated. Previously, it &quot;exhaustively&quot; searched for logical drives, as, under some circumstances some logical drives might otherwise be missed. This option no longer does anything, as the algorithm for finding logical drives was changed to obviate the need for it.</dl>
<h2>Device</h2>
<p>The DEVICE argument indicates which RAID controller is to be queried. Note, that it indicates which RAID controller, not which logical drive. </p>
<p> For the cciss driver, the &quot;d0&quot; nodes matching &quot;/dev/cciss/c*d0&quot; are the nodes which correspond to the RAID controllers. (See note 1, below.) It is not necessary to invoke cciss_vol_status on each logical drive individually, though if you do this, each time it will report the status of ALL logical drives on the controller. </p>
<p> For the hpsa driver, or for fibre attached MSA1000 family devices, or for the hpahcisr sotware RAID driver which emulates Smart Arrays, the RAID controller is accessed via the scsi generic driver, and the device nodes will match &quot;/dev/sg*&quot; Some variants of the &quot;lsscsi&quot; tool will easily identify which device node corresponds to the RAID controller. Some variants may only report the SCSI nexus (controller/bus/target/lun tuple.) Some distros may not have the lsscsi tool. </p>
<p> Executing the following query to the /sys filesystem and correlating this with the contents of /proc/scsi/scsi or output of lsscsi can help in finding the right /dev/sg node to use with cciss_vol_status: </p>
<pre>wumpus:/home/scameron # ls -l /sys/class/scsi_generic/*
lrwxrwxrwx 1 root root 0 2009-11-18 12:31 /sys/class/scsi_generic/sg0 -&gt; ../../devices/pci0000:00/0000:00:02.0/0000:02:00.0/0000:03:03.0/host0/target0:0:0/0:0:0:0/scsi_generic/sg0
lrwxrwxrwx 1 root root 0 2009-11-18 12:31 /sys/class/scsi_generic/sg1 -&gt; ../../devices/pci0000:00/0000:00:1f.1/host2/target2:0:0/2:0:0:0/scsi_generic/sg1
lrwxrwxrwx 1 root root 0 2009-11-19 07:47 /sys/class/scsi_generic/sg2 -&gt; ../../devices/pci0000:00/0000:00:05.0/0000:0e:00.0/host4/target4:3:0/4:3:0:0/scsi_generic/sg2
wumpus:/home/scameron # cat /proc/scsi/scsi
Attached devices:
Host: scsi0 Channel: 00 Id: 00 Lun: 00
 Vendor: COMPAQ Model: BD03685A24 Rev: HPB6
 Type: Direct-Access ANSI SCSI revision: 03
Host: scsi2 Channel: 00 Id: 00 Lun: 00
 Vendor: SAMSUNG Model: CD-ROM SC-148A Rev: B408
 Type: CD-ROM ANSI SCSI revision: 05
Host: scsi4 Channel: 03 Id: 00 Lun: 00
 Vendor: HP Model: P800 Rev: 6.82
 Type: RAID ANSI SCSI revision: 00
wumpus:/home/scameron # lsscsi
[0:0:0:0] disk COMPAQ BD03685A24 HPB6 /dev/sda
[2:0:0:0] cd/dvd SAMSUNG CD-ROM SC-148A B408 /dev/sr0
[4:3:0:0] storage HP P800 6.82 - </pre>
<p>From the above you can see that /dev/sg2 corresponds to SCSI nexus 4:3:0:0, which corresponds to the HP P800 RAID controller listed in /proc/scsi/scsi.</p>
<h2>Example</h2>
<pre> [root [at] somehost]# cciss_vol_status -q /dev/cciss/c*d0
 /dev/cciss/c0d0: (Smart Array P800) RAID 0 Volume 0 status: OK.
 /dev/cciss/c0d0: (Smart Array P800) RAID 0 Volume 1 status: OK.
 /dev/cciss/c0d0: (Smart Array P800) RAID 1 Volume 2 status: OK.
 /dev/cciss/c0d0: (Smart Array P800) RAID 5 Volume 4 status: OK.
 /dev/cciss/c0d0: (Smart Array P800) RAID 5 Volume 5 status: OK.
 /dev/cciss/c0d0: (Smart Array P800) Enclosure MSA60 (S/N: USP6340B3F) on Bus 2, Physical Port 1E status: Power Supply Unit failed
 /dev/cciss/c1d0: (Smart Array P800) RAID 5 Volume 0 status: OK.
 /dev/cciss/c1d0: (Smart Array P800) RAID 5 Volume 1 status: OK.
 /dev/cciss/c1d0: (Smart Array P800) RAID 5 Volume 2 status: OK.
 /dev/cciss/c1d0: (Smart Array P800) RAID 5 Volume 3 status: OK.
 /dev/cciss/c1d0: (Smart Array P800) RAID 5 Volume 4 status: OK.
 /dev/cciss/c1d0: (Smart Array P800) RAID 5 Volume 5 status: OK.
 /dev/cciss/c1d0: (Smart Array P800) RAID 5 Volume 6 status: OK.
 /dev/cciss/c1d0: (Smart Array P800) RAID 5 Volume 7 status: OK.
 [root [at] someotherhost]# cciss_vol_status -q /dev/sg0 /dev/cciss/c*d0
 /dev/sg0: (MSA1000) RAID 1 Volume 0 status: OK. At least one spare drive.
 /dev/sg0: (MSA1000) RAID 5 Volume 1 status: OK.
 /dev/cciss/c0d0: (Smart Array P800) RAID 0 Volume 0 status: OK.
 [root [at] localhost]# ./cciss_vol_status -s /dev/sg1
 /dev/sda: (Smart Array P410i) RAID 0 Volume 0 status: OK. 
 connector 1I box 1 bay 1 HP DG072A9BB7 B365P6803PCP0633 HPD0 S.M.A.R.T. predictive failure.
 [root [at] localhost]# echo $?
 1
 [root [at] localhost]# ./cciss_vol_status -s /dev/cciss/c0d0
 /dev/cciss/c0d0: (Smart Array P800) RAID 0 Volume 0 status: OK. 
 connector 2E box 1 bay 8 HP DF300BB6C3 3LM08AP700009713RXUT HPD3 S.M.A.R.T. predictive failure.
 /dev/cciss/c0d0: (Smart Array P800) Enclosure MSA60 (S/N: USP6340B3F) on Bus 2, Physical Port 2E status: OK.
 [root [at] localhost cciss_vol_status]# ./cciss_vol_status --verbose /dev/sg0
 Controller: Smart Array P420i
 Board ID: 0x3354103c
 Logical drives: 1
 Running firmware: 3.42
 ROM firmware: 3.42
 /dev/sda: (Smart Array P420i) RAID 1 Volume 0 status: OK. 
 Physical drives: 2
 connector 1I box 2 bay 1 HP EG1200FCVBQ KZG21NVD HPD1 OK
 connector 2I box 2 bay 5 HP EG1200FCVBQ KZG20X7D HPD1 OK
 /dev/sg0(Smart Array P420i:0): Non-Volatile Cache status:
 Cache configured: Yes
 Read cache memory: 81 MiB
 Write cache memory: 735 MiB
 Write cache enabled: Yes
 Flash backed cache present</pre>
<h2>Diagnostics</h2>
<p>Normally, a logical drive in good working order should report a status of &quot;OK.&quot; Possible status values are:</p>
<dl>
<dt>&quot;OK.&quot; (0) &#8211; The logical drive is in good working order.</p>
<dd>
<dt>&quot;FAILED.&quot; (1) &#8211; The logical drive has failed, and no i/o to it is poosible.</p>
<dd>Additionally, failed drives will be identified by connector, box and bay, as well as vendor, model, serial number, and firmware revision.</p>
<dt>&quot;Using interim recovery mode.&quot; (3) &#8211; One or more drives has failed,</p>
<dd>but not so many that the logical drive can no longer operate. The failed drives should be replaced as soon as possible.</p>
<dt>&quot;Ready for recovery operation.&quot; (4) &#8211; Failed drive(s) have been</p>
<dd>replaced, and the controller is about to begin rebuilding redundant parity data.</p>
<dt>&quot;Currently recovering.&quot; (5) &#8211; Failed drive(s) have been replaced,</p>
<dd>and the controller is currently rebuilding redundant parity information.</p>
<dt>&quot;Wrong physical drive was replaced.&quot; (6) &#8211; A drive has failed, and</p>
<dd>another (working) drive was replaced.</p>
<dt>&quot;A physical drive is not properly connected.&quot; (7) &#8211; There is some</p>
<dd>cabling or backplane problem in the drive enclosure.</p>
<dt>(From fwspec<a rel="nofollow" href="http://www.doc">www.doc</a>, see cpqarray project on sourceforge.net):</p>
<dd>Note: If the unit_status value is 6 (Wrong physical drive was replaced) or 7 (A physical drive is not properly connected), the unit_status of all other configured logical drives will be marked as 1 (Logical drive failed). This is to force the user to correct the problem and to insure that once the problem is corrected, the data will not have been corrupted by any user action.</p>
<dt>&quot;Hardware is overheating.&quot; (8) &#8211; Hardware is too hot.</p>
<dd>
<dt>&quot;Hardware was overheated.&quot; (9) &#8211; At some point in the past,</p>
<dd>the hardware got too hot.</p>
<dt>&quot;Currently expannding.&quot; (10) &#8211; The controller is currently in the</p>
<dd>process of expanding a logical drive.</p>
<dt>&quot;Not yet available.&quot; (11) &#8211; The logical drive is not yet finished</p>
<dd>being configured.</p>
<dt>&quot;Queued for expansion.&quot; (12) &#8211; The logical drive will be expended</p>
<dd>when the controller is able to begin working on it.</dl>
<p> Additionally, the following messages may appear regarding spare drive status: </p>
<pre> &quot;At least one spare drive designated&quot;
 &quot;At least one spare drive activated and currently rebuilding&quot;
 &quot;At least one activated on-line spare drive is completely rebuilt on this logical drive&quot;
 &quot;At least one spare drive has failed&quot;
 &quot;At least one spare drive activated&quot;
 &quot;At least one spare drive remains available&quot;
Active spares will be identified by connector, box and bay, as well
as by vendor, model, serial number, and firmware revision.</pre>
<p>For each logical drive, the total number of failed physical drives, if more than zero, will be reported as:</p>
<dl>
<dt>
<pre><dd>&quot;Total of n failed physical drives detected on this logical drive.&quot;</pre>
</dl>
<p> with &quot;n&quot; replaced by the actual number, of course. </p>
<p> &quot;Replacement&quot; drives &#8212; newly inserted drives that replace a previously failed drive but are not yet finished rebuilding &#8212; are also identified by connector, box and bay, as well as by vendor, model, serial number, and firmware revision. </p>
<p> If the -s option is specified, each physical drive will be queried for S.M.A.R.T data, any any drives in predictive failure state will be reported, identified by connector, box and bay, as well as vendor, model, serial number, and firmware revision. </p>
<p> Additionally failure conditions of disk enclosure fans, power supplies, and temperature are reported as follows: </p>
<pre> &quot;Fan failed&quot;
 &quot;Temperature problem&quot;
 &quot;Door alert&quot;
 &quot;Power Supply Unit failed&quot;</pre>
<h2>Files</h2>
<p>/dev/cciss/c*d0 (Smart Array PCI controllers using the cciss driver)<br />
 /dev/sg* (Fibre attached MSA1000 controllers and Smart Array controllers using the hpsa driver or hpahcisr software RAID driver.)</p>
<h2>Exit Codes</h2>
<dl>
<dt>0 &#8211; All configured logical drives queried have status of &quot;OK.&quot;</p>
<dd>
<dt>1 &#8211; One or more configured logical drives queried have status other than &quot;OK.&quot;</p>
<dd></dl>
<h2>Bugs</h2>
<p>MSA500 G1 logical drive numbers may not be reported correctly. </p>
<p> I&#8217;ve seen enclosure serial numbers contain garbage. </p>
<p> Some Smart Arrays support more than 128 physical drives on a single RAID controller. cciss_vol_status does not.</p>
<h2>Author</h2>
<p>Written by Stephen M. Cameron</p>
<h2>Reporting Bugs</h2>
<p>Report bugs to &lt;scameron [at] beardog.cce.hp.com&gt;</p>
<h2>Copyright</h2>
<p>Copyright &#169; 2007 Hewlett-Packard Development Company, L.P.<br />
 This is free software; see the source for copying conditions. There is NO warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.</p>
<h2>See Also</h2>
<p><a rel="nofollow" href="http://cciss.sourceforge.net">http://cciss.sourceforge.net</a></p>
<h2>note 1</h2>
<p>The /dev/cciss/c*d0 device nodes of the cciss driver do double duty. They serve as an access point to both the RAID controllers, and to the first logical drive of each RAID controller. Notice that a /dev/cciss/c*d0 node will be present for each controller even if no logical drives are configured on that controller. It might be cleaner if the driver had a special device node just for the controller, instead of making these device nodes do double duty. It has been like that since the 2.2 linux kernel timeframe. At that time, device major and minor nodes were statically allocated at compile time, and were in short supply. Changing this behavior at this point would break lots of userland programs.</p>
