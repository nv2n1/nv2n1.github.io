---
title: "sg_readcap(8)"
name: "sg_readcap"
section: "8"
letter: "s"
url: "/docs/linux/man/8-sg_readcap/"
---

sg_readcap - send SCSI READ CAPACITY command

<h2>Synopsis</h2>

<b>sg_readcap</b> [<i>--16</i>] [<i>--brief</i>] [<i>--help</i>] [<i>--hex</i>] [<i>--lba=LBA</i>] [<i>--long</i>] [<i>--pmi</i>] [<i>--raw</i>] [<i>--verbose</i>] [<i>--version</i>] <i>DEVICE</i> 

 <b>sg_readcap</b> [<i>-16</i>] [<i>-b</i>] [<i>-h</i>] [<i>-H</i>] [<i>-lba=LBA</i>] [<i>-pmi</i>] [<i>-r</i>] [<i>-v</i>] [<i>-V</i>] <i>DEVICE</i>

<h2>Description</h2>

The normal action of the SCSI READ CAPACITY command is to fetch the number of blocks (and block size) from the <i>DEVICE</i>. 

 The SCSI READ CAPACITY command (both 10 and 16 byte cdbs) actually yield the block address of the last block and the block size. The number of blocks is thus one plus the block address of the last block (as blocks are counted origin zero (i.e. starting at block zero)). This is the source of many &quot;off by one&quot; errors. 

 The READ CAPACITY(16) response provides additional information not found in the READ CAPACITY(10) response. This includes protection and logical block provisioning information, plus the number of logical blocks per physical block. So even though the media size may not exceed what READ CAPACITY(10) can show, it may still be useful to examine the response to READ CAPACITY(16). Sadly there are horrible SCSI command set implementations in the wild that crash when the READ CAPACITY(16) command is sent to them. 

 Device capacity is the product of the number of blocks by the block size. This utility outputs this figure in bytes, MiB (1048576 bytes per MiB) and GB (1000000000 bytes per GB). 

 If sg_readcap is called without the <i>--long</i> option then the 10 byte cdb version (i.e. READ CAPACITY (10)) is sent to the <i>DEVICE</i>. If the number of blocks in the response is reported as 0xffffffff (i.e. (2**32 - 1) ) and the <i>--hex</i> option has not been given, then READ CAPACITY (16) is called and its response is output. 

 This utility supports two command line syntaxes, the preferred one is shown first in the synopsis and explained in this section. A later section on the old command line syntax outlines the second group of options.

<h2>Options</h2>

Arguments to long options are mandatory for short options as well.
<dl><dt>
<dt><b>--16</b>
<dd><dd>Use the 16 byte cdb variant of the READ CAPACITY command. See the '--long' option. <b>-b</b>, <b>--brief</b> outputs two hex numbers (prefixed with '0x' and space separated) to stdout. The first number is the maximum number of blocks on the device (which is one plus the lba of the last accessible block). The second number is the size in bytes of each block. If the operation fails then &quot;0x0 0x0&quot; is written to stdout.
<dt><b>-h</b>, <b>--help</b>
<dd>print out the usage message then exit.
<dt><b>-H</b>, <b>--hex</b>
<dd>output the response to the READ CAPACITY command (either the 10 or 16 byte cdb variant) in ASCII hexadecimal on stdout.
<dt><b>-L</b>, <b>--lba</b>=<i>LBA</i>
<dd>used in conjunction with <i>--pmi</i> option. This variant of READ CAPACITY will yield the last block address after <i>LBA</i> prior to a delay. For a disk, given a <i>LBA</i> it yields the highest numbered block on the same cylinder (i.e. before the heads need to move). <i>LBA</i> is assumed to be decimal unless prefixed by &quot;0x&quot; or it has a trailing &quot;h&quot;. Defaults to 0. This option was made obsolete in SBC-3 revision 26.
<dt><b>-l</b>, <b>--long</b>
<dd>Use the 16 byte cdb variant of the READ CAPACITY command. The default action is to use the 10 byte cdb variant which limits the maximum block address to (2**32 - 2). When a 10 byte cdb READ CAPACITY command is used on a device whose size is too large then a last block address of 0xffffffff is returned (if the device complies with SBC-2 or later).
<dt><b>-O</b>, <b>--old</b>
<dd>switch to older style options.
<dt><b>-p</b>, <b>--pmi</b>
<dd>partial medium indicator: for finding the next block address prior to some delay (e.g. head movement). In the absence of this option, the total number of blocks and the block size of the device are output. Used in conjunction with the <i>--lba=LBA</i> option. This option was made obsolete in SBC-3 revision 26.
<dt><b>-r</b>, <b>--raw</b>
<dd>output response in binary to stdout.
<dt><b>-v</b>, <b>--verbose</b>
<dd>increase level of verbosity. Can be used multiple times.
<dt><b>-V</b>, <b>--version</b>
<dd>outputs version string then exits.</dl>

<h2>Notes</h2>

In the 2.4 series of Linux kernels the <i>DEVICE</i> must be a SCSI generic (sg) device. In the 2.6 series block devices (e.g. SCSI disks and DVD drives) can also be specified. For example &quot;sg_readcap /dev/sda&quot; and &quot;sg_readcap /dev/hdd&quot; (if /dev/hdd is a ATAPI CD/DVD device) will work in the 2.6 series kernels.

<h2>Exit Status</h2>

The exit status of sg_readcap is 0 when it is successful. Otherwise see the <a HREF="/docs/linux/man/8-sg3_utils/">sg3_utils</a>(8) man page.

<h2>Older Command Line Options</h2>

The options in this section were the only ones available prior to sg3_utils version 1.23 . In sg3_utils version 1.23 and later these older options can be selected by either setting the SG3_UTILS_OLD_OPTS environment variable or using '--old' (or '-O) as the first option.
<dl><dt><b>-16</b>
<dd>Use the 16 byte cdb variant of the READ CAPACITY command. Equivalent to <i>--long</i> in the main description.
<dt><b>-b</b>
<dd>utility outputs two hex numbers (prefixed with '0x' and space separated) to stdout. The first number is the maximum number of blocks on the device (which is one plus the lba of the last accessible block). The second number is the size of each block. If the operation fails then &quot;0x0 0x0&quot; is written to stdout. Equivalent to <i>--brief</i> in the main description.
<dt><b>-h</b>
<dd>output the usage message then exit. Giving the <i>-?</i> option also outputs the usage message then exits.
<dt><b>-H</b>
<dd>output the response to the READ CAPACITY command (either the 10 or 16 byte cdb variant) in ASCII hexadecimal on stdout.
<dt><b>-lba</b>=<i>LBA</i>
<dd>used in conjunction with <i>-pmi</i> option. This variant of READ CAPACITY will yield the last block address after <i>LBA</i> prior to a delay. Equivalent to <i>--lba=LBA</i> in the main description.
<dt><b>-N</b>
<dd>switch to the newer style options.
<dt><b>-pmi</b>
<dd>partial medium indicator: for finding the next block address prior to some delay (e.g. head movement). In the absence of this switch, the total number of blocks and the block size of the device are output. Equivalent to <i>--pmi</i> in the main description.
<dt><b>-r</b>
<dd>output response in binary (to stdout).
<dt><b>-v</b>
<dd>verbose: print out cdb of issued commands prior to execution. '-vv' and '-vvv' are also accepted yielding greater verbosity.
<dt><b>-V</b>
<dd>outputs version string then exits.</dl>

<h2>Authors</h2>

Written by Douglas Gilbert

<h2>Copyright</h2>

Copyright &#169; 1999-2013 Douglas Gilbert 
 This software is distributed under the GPL version 2. There is NO warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.

<h2>See Also</h2>

<b>sg_inq(sg3_utils)</b> 
