---
title: "sg_luns(8)"
name: "sg_luns"
section: "8"
letter: "s"
url: "/docs/linux/man/8-sg_luns/"
---

sg_luns - send SCSI REPORT LUNS command or decode given LUN

<h2>Synopsis</h2>

<b>sg_luns</b> [<i>--decode</i>] [<i>--help</i>] [<i>--hex</i>] [<i>--linux</i>] [<i>--maxlen=LEN</i>] [<i>--quiet</i>] [<i>--raw</i>] [<i>--select=SR</i>] [<i>--verbose</i>] [<i>--version</i>] <i>DEVICE</i> 

 <b>sg_luns</b> <i>--test=ALUN</i> [<i>--hex</i>] [<i>--verbose</i>]

<h2>Description</h2>

In the first form shown in the SYNOPSIS this utility sends the SCSI REPORT LUNS command to the <i>DEVICE</i> and outputs the response. The response should be a list of LUNs (&quot;a LUN inventory&quot;) for the I_T nexus associated with the <i>DEVICE</i>. Roughly speaking that is all LUNs that share the target device that the REPORT LUNS command is sent through. In the SPC-3 and SPC-4 SCSI standards support for the REPORT LUNS command is mandatory. 

 When the <i>--test=ALUN</i> option is given (the second form in the SYNOPSIS), then the <i>ALUN</i> value is decoded as outlined in SAM-3, SAM-4 and SAM-5 (revision 13, section 4.7) . 

 Where required below the first form shown in the SYNOPSIS is called &quot;device mode&quot; and the second form is called &quot;test mode&quot;.

<h2>Options</h2>

Arguments to long options are mandatory for short options as well.
<dl><dt><b>-d</b>, <b>--decode</b>
<dd>decode LUNs into their component parts, as described in the LUN section of SAM-3, SAM-4 and SAM-5.
<dt><b>-h</b>, <b>--help</b>
<dd>output the usage message then exit.
<dt><b>-H</b>, <b>--hex</b>
<dd>[device mode] when given once this utility will output the SCSI response (i.e. the data-out buffer) to the REPORT LUNS command in ASCII hex then exit. When given twice it causes <i>--decode</i> to output component fields in hex rather than decimal.
<dt><b>-H</b>, <b>--hex</b>
<dd>[test mode] when this option is given, then decoded component fields of <i>ALUN</i> are output in hex.
<dt><b>-l</b>, <b>--linux</b>
<dd>this option is only available in Linux. After the T10 representation of each 64 bit LUN (in 16 hexadecimal digits), if this option is given then to the right, in square brackets, is the Linux LUN integer in decimal. If the <i>--hex</i> option is given twice (e.g. -HH) as well then the Linux LUN integer is output in hexadecimal.
<dt><b>-m</b>, <b>--maxlen</b>=<i>LEN</i>
<dd>where <i>LEN</i> is the (maximum) response length in bytes. It is placed in the cdb's &quot;allocation length&quot; field. If not given (or <i>LEN</i> is zero) then 8192 is used. The maximum allowed value of <i>LEN</i> is 1048576.
<dt><b>-q</b>, <b>--quiet</b>
<dd>output only the ASCII hex rendering of each report LUN, one per line. Without the <i>--quiet</i> option, there is header information printed before the LUN listing.
<dt><b>-r</b>, <b>--raw</b>
<dd>output the SCSI response (i.e. the data-out buffer) in binary (to stdout).
<dt><b>-s</b>, <b>--select</b>=<i>SR</i>
<dd>this option sets the SELECT REPORT field (<i>SR</i>) in the SCSI REPORT LUNS command. The default value is 0. For detailed information see the REPORT LUNS command in SPC (most recent is SPC-4 revision 36e in section 6.33). To simplify, for the I_T nexus associated with the <i>DEVICE</i>, the meanings of the <i>SR</i> values defined to date for SPC-4 are: 
 
&nbsp;<wbr>&nbsp;<wbr><b>0</b>&nbsp;<wbr>: all LUNs excluding well known logical units 
 
&nbsp;<wbr>&nbsp;<wbr><b>1</b>&nbsp;<wbr>: well known logical units 
 
&nbsp;<wbr>&nbsp;<wbr><b>2</b>&nbsp;<wbr>: all LUNs 
 Values between 0xf8 and 0xff (inclusive) are vendor specific (SPC-4 rev 36e), other values greater than 2 are reserved. This utility will accept any value between 0 and 255 (0xff) for <i>SR</i> .
<dt><b>-t</b>, <b>--test</b>=<i>ALUN</i>
<dd><i>ALUN</i> is assumed to be a hexadecimal number in ASCII hex or the letter 'L' followed by a decimal number (see below). The hexadecimal number can be up to 64 bits in size (i.e. 16 hexadecimal digits) and is padded to the right if less than 16 hexadecimal digits are given (e.g. <i>--test=0122003a</i> represents T10 LUN 0122003a00000000). <i>ALUN</i> may be prefixed by '0x' or '0X' (e.g. the previous example could have been <i>--test=0x0122003a</i>). <i>ALUN</i> may also be given with spaces or tabs between each byte (or other grouping) but then <i>ALUN</i> would need to be surrounded by single or double quotes. In the decimal number case (i.e. following a 'L') that number is assumed to be a Linux &quot;word flipped&quot; LUN which is converted into a T10 LUN representation and printed. In both cases the number is interpreted as a LUN and decoded as if the <i>--decode</i> option had been given. Also when <i>ALUN</i> is a hexadecimal number it can have a trailing 'L' in which case the corresponding Linux &quot;word flipped&quot; LUN value is output. The LUN is decoded in all cases.
<dt><b>-v</b>, <b>--verbose</b>
<dd>increase the level of verbosity, (i.e. debug output).
<dt><b>-V</b>, <b>--version</b>
<dd>print the version string and then exit.</dl>

<h2>Notes</h2>

The SCSI REPORT LUNS command is important for Logical Unit (LU) discovery. After a target device is discovered (usually via some transport specific mechanism), a REPORT LUNS command should either be sent to LUN 0 (which is Peripheral device addressing method with bus_id=0 and target/lun=0) or to the REPORT LUNS well known LUN (i.e. 0xc101000000000000). SAM-5 requires that one of these responds with an inventory of LUNS that are contained in this target device. 

 In test mode, if the <i>--hex</i> option is given once then in the decoded output, some of the component fields are printed in hex with leading zeros. The leading zeros are to indicate the size of the component field. For example: in the Peripheral device addressing method (16 bits overall), the bus ID is 6 bits wide and the target/LUN field is 8 bits wide; so both are shown with two hex digits (e.g. bus_id=0x02, target=0x3a).

<h2>Examples</h2>

Typically by the time user space programs get to run, SCSI LUs have been discovered. In Linux the lsscsi utility lists the LUs that are currently present. The LUN of a device (LU) is the fourth element in the tuple at the beginning of each line. Below we see a target (or &quot;I_T Nexus&quot;: &quot;6:0:0&quot;) has two LUNS: 1 and 49409. If 49409 is converted into T10 LUN format it is 0xc101000000000000 which is the REPORT LUNS well known LUN. 
&nbsp;<wbr>&nbsp;<wbr>#&nbsp;<wbr>lsscsi -g 
 
&nbsp;<wbr>&nbsp;<wbr>[6:0:0:1]&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>disk&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Linux&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>scsi_debug&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>0004&nbsp;<wbr>&nbsp;<wbr>/dev/sdb&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>/dev/sg1 
 
&nbsp;<wbr>&nbsp;<wbr>[6:0:0:49409]wlun&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Linux&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>scsi_debug&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>0004&nbsp;<wbr>&nbsp;<wbr>-&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>/dev/sg2 We could send a REPORT LUNS command to either /dev/sdb, /dev/sg1 or /dev/sg2 and get the same result. Below we use /dev/sg1 : <pre><code># sg_luns /dev/sg1

Lun list length = 8 which imples 1 lun entry

Report luns [select_report=0x0]:


0001000000000000</code></pre> That is a bit noisy so cut down the clutter with <i>--quiet</i>: 
&nbsp;<wbr>&nbsp;<wbr>#&nbsp;<wbr>sg_luns -q&nbsp;<wbr>/dev/sg1 
 
&nbsp;<wbr>&nbsp;<wbr>0001000000000000 Now decode that LUN into its component parts: # sg_luns -d -q /dev/sg1

0001000000000000

Peripheral device addressing: lun=1 Would like to see how wide that component LUN field is: 
&nbsp;<wbr>&nbsp;<wbr>#&nbsp;<wbr>sg_luns -d -q -HH&nbsp;<wbr>/dev/sg1 
 
&nbsp;<wbr>&nbsp;<wbr>0001000000000000 
 
&nbsp;<wbr>&nbsp;<wbr>Peripheral device addressing: lun=0x01 So it is 8 bits wide (actually between 5 and 8 bits wide, inclusive). Now use <i>--select=1</i> to find out if there are any well known LUNs: 
&nbsp;<wbr>&nbsp;<wbr>#&nbsp;<wbr>sg_luns -q -s 1&nbsp;<wbr>/dev/sg1 
 
&nbsp;<wbr>&nbsp;<wbr>c101000000000000 So how many LUNs do we have all together (associated with the current I_T Nexus): 
&nbsp;<wbr>&nbsp;<wbr>#&nbsp;<wbr>sg_luns -q -s 2&nbsp;<wbr>/dev/sg1 
 
&nbsp;<wbr>&nbsp;<wbr>0001000000000000 
 
&nbsp;<wbr>&nbsp;<wbr>c101000000000000 # sg_luns -q -s 2 -d /dev/sg1

0001000000000000

Peripheral device addressing: lun=1

c101000000000000

REPORT LUNS well known logical unit The following example uses the <i>--linux</i> option and is not available in other operating systems. The extra number in square brackets is the Linux version of T10 LUN shown at the start of the line. 
&nbsp;<wbr>&nbsp;<wbr>#&nbsp;<wbr>sg_luns -q -s 2 -l&nbsp;<wbr>/dev/sg1 
 
&nbsp;<wbr>&nbsp;<wbr>0001000000000000&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>[1] 
 
&nbsp;<wbr>&nbsp;<wbr>c101000000000000&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>[49409] Now we use the <i>--test=</i> option to decode LUNS input on the command line (rather than send a REPORT LUNS command and act on the response): # sg_luns --test=0001000000000000

Decoded LUN:


Peripheral device addressing: lun=1
# sg_luns --test=&quot;c1 01&quot;

Decoded LUN:


REPORT LUNS well known logical unit
# sg_luns -t 0x023a004b -H

Decoded LUN:


Peripheral device addressing: bus_id=0x02, target=0x3a


&gt;&gt;Second level addressing:


Peripheral device addressing: lun=0x4b The next example is Linux specific as we try to find out what the Linux LUN 49409 translates to in the T10 world: <pre><code># sg_luns --test=L49409

64 bit LUN in T10 preferred (hex) format:  c1 01 00 00 00 00 00 00

Decoded LUN:


REPORT LUNS well known logical unit</code></pre> And the mapping between T10 and Linux LUN representations can be done the other way: 
&nbsp;<wbr>&nbsp;<wbr>#&nbsp;<wbr>sg_luns -t c101L 
 
&nbsp;<wbr>&nbsp;<wbr>Linux&nbsp;<wbr>'word flipped'&nbsp;<wbr>integer LUN representation: 49409 
 
&nbsp;<wbr>&nbsp;<wbr>Decoded LUN: 
 
&nbsp;<wbr>REPORT LUNS well known logical unit

<h2>Exit Status</h2>

The exit status of sg_luns is 0 when it is successful. Otherwise see the <a HREF="/docs/linux/man/8-sg3_utils/">sg3_utils</a>(8) man page.

<h2>Authors</h2>

Written by Douglas Gilbert.

<h2>Reporting Bugs</h2>

Report bugs to &lt;dgilbert at interlog dot com&gt;.

<h2>Copyright</h2>

Copyright &#169; 2004-2013 Douglas Gilbert 
 This software is distributed under a FreeBSD license. There is NO warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.

<h2>See Also</h2>

<b><a HREF="/docs/linux/man/8-sg_inq/">sg_inq</a>(8)</b> 
