---
title: "sg_start(8)"
name: "sg_start"
section: "8"
letter: "s"
url: "/docs/linux/man/8-sg_start/"
description: "sg_start – send SCSI START STOP UNIT command: start, stop, load or eject medium"
---

<p>sg_start &#8211; send SCSI START STOP UNIT command: start, stop, load or eject medium</p>
<h2>Synopsis</h2>
<p><code>sg_start</code> [<i>0</i>] [<i>1</i>] [<i>&#8211;eject</i>] [<i>&#8211;help</i>] [<i>&#8211;fl=FL</i>] [<i>&#8211;immed</i>] [<i>&#8211;load</i>] [<i>&#8211;loej</i>] [<i>&#8211;mod=PC_MOD</i>] [<i>&#8211;noflush</i>] [<i>&#8211;pc=PC</i>] [<i>&#8211;readonly</i>] [<i>&#8211;start</i>] [<i>&#8211;stop</i>] [<i>&#8211;verbose</i>] [<i>&#8211;version</i>] <i>DEVICE</i> </p>
<p> <code>sg_start</code> [<i>&#8211;eject</i>] [<i>&#8211;fl=FL</i>] [<i>-i</i>] [<i>&#8211;imm=0|1</i>] [<i>&#8211;load</i>] [<i>&#8211;loej</i>] [<i>&#8211;mod=PC_MOD</i>] [<i>&#8211;noflush</i>] [<i>&#8211;pc=PC</i>] [<i>-r</i>] [<i>&#8211;start</i>] [<i>&#8211;stop</i>] [<i>-v</i>] [<i>-V</i>] [<i>0|1</i>] <i>DEVICE</i></p>
<h2>Description</h2>
<p>sg_start sends a SCSI START STOP UNIT command to the <i>DEVICE</i> with the selected options. The most used options are <i>&#8211;stop</i> to spin down a disk and <i>&#8211;start</i> to spin up a disk. Using <i>&#8211;start</i> on a disk that is already spinning is harmless. There is also finer grain control with &quot;power condition&quot;: active, idle or standby. This is set with the <i>&#8211;pc=PC</i> option. In some contexts the &quot;stop&quot; state can be considered an additional power condition. </p>
<p> Devices that contain removable media such as cd/dvds can use the <i>&#8211;loej</i> option to load the medium when used in conjunction with <i>&#8211;start</i> (i.e. load medium then spin up). Alternatively <i>&#8211;loej</i> may be used to eject the medium when used in conjunction with <i>&#8211;stop</i> (i.e. spin down then eject medium). More simply, the loading or ejecting of a removable medium can be requested with the <i>&#8211;load</i> or <i>&#8211;eject</i>&#8216; option. </p>
<p> If no option or argument is given then a <i>&#8211;start</i> is assumed; as the utility&#8217;s name suggests. </p>
<p> This utility supports two command line syntaxes, the preferred one is shown first in the synopsis and explained in this section. A later section on the old command line syntax outlines the second group of options.</p>
<h2>Options</h2>
<p>Arguments to long options are mandatory for short options as well.</p>
<dl>
<dt><code>0</code></p>
<dd>same action as <i>&#8211;stop</i>.</p>
<dt><code>1</code></p>
<dd>same action as <i>&#8211;start</i>.</p>
<dt><code>-e</code>, <code>&#8211;eject</code></p>
<dd>stop the medium and eject it from the drive. Only appropriate for a device with removable medium. Might be ignored (prevented), see below.</p>
<dt><code>-h</code>, <code>&#8211;help</code></p>
<dd>print out the usage message then exit.</p>
<dt><code>-f</code>, <code>&#8211;fl</code>=<i>FL</i></p>
<dd>sets the format layer number for the disc to &quot;jump&quot; to (defined in MMC-5). Values of <i>FL</i> can be 0 to 3. When this option is chosen, the FL, LoEj and Start bits are set in the cdb as required by MMC-5; thus the user does not need to set the <i>&#8211;start</i> and/or <i>&#8211;load</i> options.</p>
<dt><code>-i</code>, <code>&#8211;immed</code></p>
<dd>sets the IMM bit on the START STOP UNIT command so this utility will return immediately and not wait for the media to complete the requested action. The default is to wait until the media to complete the requested action before returning.</p>
<dt><code>-l</code>, <code>&#8211;load</code></p>
<dd>load the medium in the drive and start it. Only appropriate for a removable medium.</p>
<dt><code>-L</code>, <code>&#8211;loej</code></p>
<dd>sets the LOEJ bit on the START STOP UNIT command. This loads the media when the unit is started or eject it when the unit is stopped (i.e. works in conjunction with START bit in cdb). This option is ignored if &#8216;pc &gt; 0&#8217;. Default is off (i.e. don&#8217;t attempt to load or eject media). If a start/start indication is not given (i.e. neither <i>&#8211;start</i> nor <i>&#8211;stop</i>) and this option is given then a load and start action is assumed.</p>
<dt><code>-m</code>, <code>&#8211;mod</code>=<i>PC_MOD</i></p>
<dd>where <i>PC_MOD</i> is the &#8216;power condition modifier&#8217; value. 0 to 15 (inclusive) are valid and 0 is the default. This &#8216;power condition modifier&#8217; field in the cdb was added after sbc3r13.</p>
<dt><code>-n</code>, <code>&#8211;noflush</code></p>
<dd>do not perform a flush to media (e.g. like SYNCHRONIZE CACHE does) before a variant of this utility that limits access to the media. Using the <code>&#8211;stop</code> option is an example of something that limits access to the media. This &#8216;noflush&#8217; field in the cdb was added after sbc3r13.</p>
<dt><code>-O</code>, <code>&#8211;old</code></p>
<dd>switch to older style options.</p>
<dt><code>-p</code>, <code>&#8211;pc</code>=<i>PC</i></p>
<dd>where <i>PC</i> is the &#8216;power conditions&#8217; value. 0 to 15 (inclusive) are valid. Default value is 0. When &#8216;&#8211;pc=0&#8217; then <code>&#8211;eject</code>, <code>&#8211;load</code>, <code>&#8211;loej</code>, <code>&#8211;start</code> and <code>&#8211;stop</code> are active. Some common values are 1 for the &quot;active&quot; power condition (SBC); 2 for the idle power condition; 3 for the standby power condition; 5 for sleep power condition (MMC); 7 for LU_CONTROL (SBC), 0xa (decimal 10) for FORCE_IDLE_0 (SBC) and 0xb (decimal 11) for FORCE_STANDBY_0 (SBC). See recent SBC-3, MMC-5 and SAS drafts at <a rel="nofollow" href="http://www.t10.org">www.t10.org</a> for more information.</p>
<dt><code>-r</code>, <code>&#8211;readonly</code></p>
<dd>open the <i>DEVICE</i> in read-only mode. Maybe required in Linux to stop a nuisance spin-up if the <i>DEVICE</i> is an ATA disk. The nuisance spin-up may occur at the end of this command negating the effect of the <i>&#8211;stop</i> option.</p>
<dt><code>-s</code>, <code>&#8211;start</code></p>
<dd>start (spin-up) the <i>DEVICE</i>. This sets the START bit in the cdb. Using this option on an already started device is harmless. In the absence of other options, this option defaults (i.e. set the START cdb bit).</p>
<dt><code>-S</code>, <code>&#8211;stop</code></p>
<dd>stop (spin-down) the <i>DEVICE</i>. This clears the START bit in the cdb.</p>
<dt><code>-v</code>, <code>&#8211;verbose</code></p>
<dd>increase the level of verbosity. Can be used multiple times.</p>
<dt><code>-V</code>, <code>&#8211;version</code></p>
<dd>print out version string then exit.</dl>
<h2>Notes</h2>
<p>To avoid confusion, only one of <i>0</i>, <i>1</i> <i>&#8211;eject</i>, <i>&#8211;load</i>, <i>&#8211;start</i> and <i>&#8211;stop</i> should be given. </p>
<p> There is an associated &quot;power condition&quot; mode page (0x1a) in which timer values can be set for transitioning to either idle or standby state after a period of inactivity. The sdparm utility can be used to view the power condition mode page and if required change it. If a <i>DEVICE</i> is in either idle or standby power condition state then a REQUEST SENSE command (see the sg_requests utility) should yield a sense key of &quot;no sense&quot; and an additional sense code of &quot;Low power condition on&quot; on recent SCSI devices. </p>
<p> Ejection of removable media (e.g. &#8216;sg_start &#8211;eject /dev/hdd&#8217; where the <i>DEVICE</i> is an ATAPI cd/dvd drive) may be prevented by a prior SCSI PREVENT ALLOW MEDIUM REMOVAL command (see sg_prevent). In this case this utility should fail with an error generated by the device: illegal request / medium removal prevented. This can be overridden using sg_prevent or, for example, &#8216;sdparm &#8211;command=unlock /dev/hdd&#8217;. </p>
<p> The SCSI TEST UNIT READY command can be used to find out whether a <i>DEVICE</i> is ready to transfer data. If rotating media is stopped or still coming up to speed, then the TEST UNIT READY command will yield a &quot;not ready&quot; sense key and an more informative additional sense code. See the sg_turs utility. </p>
<p> In the 2.4 series of Linux kernels the <i>DEVICE</i> must be a SCSI generic (sg) device. In the 2.6 series block devices (e.g. SCSI disks and DVD drives) can also be specified. For example &quot;sg_start 0 /dev/sda&quot; will work in the 2.6 series kernels. </p>
<p> In the Linux 2.6 series, especially with ATA disks, using this utility to stop (spin down) a disk may not be sufficient and other mechanisms will start the disk again some time later. The user might additionally mark the disk as &quot;offline&quot; with &#8216;echo offline &gt; /sys/block/sda/device/state&#8217; where sda is the block name of the disk. To restart the disk &quot;offline&quot; can be replaced with &quot;running&quot;. Note that once the &#8216;state&#8217; is set to offline, no SCSI commands can be sent to the device until it is set back to running. Also stopping a disk via a pass-through interface (e.g. /dev/sg1 or /dev/bsg/1:0:0:0) may reduce unwanted side effects (such as restarting it again when this utility completes).</p>
<h2>Exit Status</h2>
<p>The exit status of sg_start is 0 when it is successful. Otherwise see the <a href="/docs/linux/man/8-sg3_utils/">sg3_utils</a>(8) man page.</p>
<h2>Older Command Line Options</h2>
<p>The options in this section were the only ones available prior to sg3_utils version 1.23 . In sg3_utils version 1.23 and later these older options can be selected by either setting the SG3_UTILS_OLD_OPTS environment variable or using &#8216;&#8211;old&#8217; (or &#8216;-O) as the first option. </p>
<p> Note that the action of <i>&#8211;loej</i> is slightly different in the older interface: when neither <i>&#8211;start</i> nor <i>&#8211;stop</i> (nor proxies for them) are given, <i>&#8211;loej</i> performs an eject operation. In the same situation the newer interface will perform a load operation. </p>
<p> Earlier versions of sg_start had a &#8216;-s&#8217; option to perform a SYNCHRONIZE CACHE command before the START STOP UNIT command was issued. According to recent SBC-2 drafts this is done implicitly if required. Hence the &#8216;-s&#8217; option has been dropped. </p>
<p> All options, other than &#8216;-v&#8217; and &#8216;-V&#8217;, can be given with a single &quot;-&quot;. For example: &quot;sg_start -stop /dev/sda&quot; and &quot;sg_start &#8211;stop /dev/sda&quot; are equivalent. The single &quot;-&quot; form is for backward compatibility.</p>
<dl>
<dt><code>0</code></p>
<dd>stop (spin-down) <i>DEVICE</i>.</p>
<dt><code>1</code></p>
<dd>start (spin-up) <i>DEVICE</i>.</p>
<dt><code>&#8211;eject</code></p>
<dd>stop the medium and eject it from the drive.</p>
<dt><code>&#8211;fl</code>=<i>FL</i></p>
<dd>sets the format layer number for the disc to &quot;jump&quot; to (defined in MMC-5).</p>
<dt><code>-i</code></p>
<dd>sets the IMM bit on the START STOP UNIT command so this utility will return immediately and not wait for the media to spin down. Same effect as &#8216;&#8211;imm=1&#8217;. The default action (without this option or a &#8216;&#8211;imm=1&#8217; option) is to wait until the media spins down before returning.</p>
<dt><code>&#8211;imm</code>=<i>0|1</i></p>
<dd>when the immediate bit is 1 then this utility returns immediately after the <i>DEVICE</i> has received the command. When this option is 0 (the default) then the utility returns once the command has completed its action (i.e. it waits until the device is started or stopped).</p>
<dt><code>&#8211;load</code></p>
<dd>load the medium in the drive and start it.</p>
<dt><code>&#8211;loej</code></p>
<dd>sets the LOEJ bit in the START STOP UNIT cdb. When a &quot;start&quot; operation is indicated, then a load and start is performed. When a &quot;stop&quot; operation is indicated, then a stop and eject is performed. When neither a &quot;start&quot; or &quot;stop&quot; operation is indicated does a stop and eject. [Note that the last action differs from the new interface in which the option of this name defaults to load and start.]</p>
<dt><code>-N</code></p>
<dd>switch to the newer style options.</p>
<dt><code>&#8211;mod</code>=<i>PC_MOD</i></p>
<dd>where <i>PC_MOD</i> is the &#8216;power condition modifier&#8217; value. 0 to 15 (inclusive) are valid and 0 is the default. This field was added after sbc3r13.</p>
<dt><code>&#8211;noflush</code></p>
<dd>do not perform a flush to media (e.g. like SYNCHRONIZE CACHE does) before a variant of this utility that limits access to the media. Using the <code>&#8211;stop</code> option is an example of something that limits access to the media. This field was added after sbc3r13.</p>
<dt><code>&#8211;pc</code>=<i>PC</i></p>
<dd>where <i>PC</i> is the &#8216;power condition&#8217; value (in hex). 0 to f (inclusive) are valid. Default value is 0.</p>
<dt><code>-r</code></p>
<dd>see the <i>&#8211;readonly</i> option above. May be useful for ATA disks.</p>
<dt><code>&#8211;start</code></p>
<dd>start (spin-up) <i>DEVICE</i>.</p>
<dt><code>&#8211;stop</code></p>
<dd>stop (spin-down) <i>DEVICE</i>. Same meaning as &quot;0&quot; argument.</p>
<dt><code>-v</code></p>
<dd>verbose: outputs SCSI command in hex to console before with executing it. &#8216;-vv&#8217; and &#8216;-vvv&#8217; are also accepted yielding greater verbosity.</p>
<dt><code>-V</code></p>
<dd>print out version string then exit.</dl>
<h2>Author</h2>
<p>Written by K. Garloff and D. Gilbert</p>
<h2>Reporting Bugs</h2>
<p>Report bugs to &lt;dgilbert at interlog dot com&gt;.</p>
<h2>Copyright</h2>
<p>Copyright &#169; 2002-2012 Kurt Garloff, Douglas Gilbert<br />
 This software is distributed under the GPL version 2. There is NO warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.</p>
<h2>See Also</h2>
<p><code>sg_prevent(sg3_utils), sg_requests(sg3_utils), sg_turs(sg3_utils)</code> <code>sdparm(sdparm)</code> </p>
