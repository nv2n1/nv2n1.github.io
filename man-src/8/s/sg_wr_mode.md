---
title: "sg_wr_mode(8)"
name: "sg_wr_mode"
section: "8"
letter: "s"
url: "/docs/linux/man/8-sg_wr_mode/"
description: "sg_wr_mode – write (modify) SCSI mode page"
---

<p>sg_wr_mode &#8211; write (modify) SCSI mode page</p>
<h2>Synopsis</h2>
<p><code>sg_wr_mode</code> [<i>&#8211;contents=H,H&#8230;</i>] [<i>&#8211;dbd</i>] [<i>&#8211;force</i>] [<i>&#8211;help</i>] [<i>&#8211;len=</i>10|6] [<i>&#8211;mask=M,M&#8230;</i>] [<i>&#8211;page=PG[,SPG]</i>] [<i>&#8211;save</i>] [<i>&#8211;verbose</i>] [<i>&#8211;version</i>] <i>DEVICE</i></p>
<h2>Description</h2>
<p>Writes a modified mode page to <i>DEVICE</i>. Uses the SCSI MODE SENSE (6 or 10 byte variant) command to fetch the existing mode data which includes a mode page (or subpage). It then combines that with the contents, potentially masked, and writes the modified mode page with the SCSI MODE SELECT (6 or 10 byte variant) command. This utility does not modify the block descriptor(s); if any block descriptors are fetched by the MODE SENSE command then the same block descriptors are written back with the following MODE SELECT command. </p>
<p> If a contents argument is not given then the various components (i.e. header, block descriptor(s) and mode page) of the &quot;current&quot; values of the existing mode page are printed out. In this case the mode page is not altered on the device. </p>
<p> If the contents are specified, and a mask is not specified, then the contents must match the existing mode page in various aspects unless the <i>&#8211;force</i> option is given. These include length, mode page code and subpage code if applicable. If all is well then the contents string is written to <i>DEVICE</i> as the new mode page. </p>
<p> If both contents and mask strings are specified then only bit positions in the contents corresponding to set bits in the mask are taken while the existing mode page supplies bit positions corresponding to clear bits. When a mask is given then the mask and/or the contents may be shorter than the existing mode page. If the mask is shorter than the contents then the remaining bytes are taken from the contents. If the contents are shorter than the existing mode page then the remaining bytes are taken from the existing mod page. </p>
<p> The force option allows the contents string to be written as the new mode page without any prior checks on the existing mode page. This should only be required for vendor specific mode pages. The existing mode data is ignored apart from the block descriptors which can be suppressed with the <i>&#8211;dbd</i> option if need be. </p>
<p> Changing individual fields in a mode page is probably more easily done with the sdparm utility. Fields can be identified by acronym or by a numerical descriptor.</p>
<h2>Options</h2>
<p>Arguments to long options are mandatory for short options as well.</p>
<dl>
<dt><code>-c</code>, <code>&#8211;contents</code>=<i>H,H&#8230;</i></p>
<dd>where <i>H,H&#8230;</i> is a string of comma separated hex numbers each of which should resolve to a byte value (i.e. 0 to ff inclusive). A (single) space separated string of hex numbers is also allowed but the list needs to be in quotes. This is the new contents of the mode page to be written to <i>DEVICE</i>, potentially filtered by the mask string.</p>
<dt><code>-c</code>, <code>&#8211;contents</code>=-</p>
<dd>reads contents string from stdin. The hex numbers in the string may be comma, space, tab or linefeed (newline) separated. If a line contains &quot;#&quot; then the remaining characters on that line are ignored. Otherwise each non separator character should resolve to a byte value (i.e. 0 to ff inclusive). This forms the new contents of the mode page to be written to <i>DEVICE</i>, potentially filtered by the mask string.</p>
<dt><code>-d</code>, <code>&#8211;dbd</code></p>
<dd>disable block descriptors (DBD flag in cdb). Some device types include block descriptors in the mode data returned by a MODE SENSE command. If so the same block descriptors are written by the MODE SELECT command. This option instructs the MODE SENSE command not to return any block descriptors. This would be a sensible default for this utility apart from the fact that not all SCSI devices support the DBD bit in the cdb.</p>
<dt><code>-f</code>, <code>&#8211;force</code></p>
<dd>force the contents string to be taken as the new mode page, or at least doesn&#8217;t do checks on the existing mode page. Note that <i>DEVICE</i> may still reject the new contents for the mode page. Cannot be given with the <i>&#8211;mask=M,M&#8230;</i> option.</p>
<dt><code>-h</code>, <code>&#8211;help</code></p>
<dd>output the usage message then exit.</p>
<dt><code>-l</code>, <code>&#8211;len</code>=10 | 6</p>
<dd>length of the SCSI commands (cdb) sent to <i>DEVICE</i>. The default is 10 so 10 byte MODE SENSE and MODE SELECT commands are issued. Some old devices don&#8217;t support the 10 byte variants hence this option.</p>
<dt><code>-m</code>, <code>&#8211;mask</code>=<i>M,M&#8230;</i></p>
<dd>where <i>M,M&#8230;</i> is a string of comma separated hex numbers each of which should resolve to a byte value (i.e. 0 to ff inclusive). A (single) space separated string of hex numbers is also allowed but the list needs to be in quotes. The mask chooses (bit by bit) whether the new mode page comes from the contents (mask bit set) or from the existing mode page (mask bit clear). If the mask string is shorter than the contents string then the remaining bytes are taken from the contents string. If the contents string is shorter than the existing mode page then the remaining bytes are taken from the existing mode page (i.e. they are left unaltered).</p>
<dt><code>-p</code>, <code>&#8211;page</code>=<i>PG</i></p>
<dd>where <i>PG</i> is the page code value to fetch and modify. The page code is in hex and should be between 0 and 3e inclusive. Notice that page code 3f to fetch all mode pages is disallowed.</p>
<dt><code>-p</code>, <code>&#8211;page</code>=<i>PG,SPG</i></p>
<dd>where <i>PG</i> is the page code value and <i>SPG</i> is the subpage code value to fetch and modify. Both values are in hex. The subpage code should be between 0 and fe inclusive. Notice that subpage code ff to fetch all mode subpages (for a given mode page or all mode pages in the case of 3f,ff) is disallowed.</p>
<dt><code>-s</code>, <code>&#8211;save</code></p>
<dd>changes the &quot;saved&quot; mode page when MODE SELECT is successful. By default (i.e. when <i>&#8211;save</i> is not used) only the &quot;current&quot; mode page values are changed when MODE SELECT is successful. In this case the new mode page will stay in effect until the device is reset (e.g. power cycled). When it restarts the &quot;saved&quot; values for the mode page will be re-instated. So to make changes permanent use the <i>&#8211;save</i> option.</p>
<dt><code>-v</code>, <code>&#8211;verbose</code></p>
<dd>increase the level of verbosity, (i.e. debug output).</p>
<dt><code>-V</code>, <code>&#8211;version</code></p>
<dd>print the version string and then exit.</dl>
<h2>Notes</h2>
<p>This utility does not check whether the contents string is trying to modify parts of the mode page which are changeable. The device should do that and if some part is not changeable then it should report: &quot;Invalid field in parameter list&quot;. </p>
<p> Some mode pages are not saveable. If so an attempt to use the <i>&#8211;save</i> option should cause an error to be reported from the device: &quot;Illegal field in cdb&quot;. </p>
<p> The device is required to do various checks before it accepts a new mode page. If these checks fail then the mode page is not altered and either a &quot;parameter list length error&quot; or an &quot;invalid field in parameter list&quot; error is returned by the device in the sense data. </p>
<p> The recommended way to modify a mode page is to read it with a MODE SENSE, modify some part of it then write it back to the device with a MODE SELECT command. For example, reading an existing mode page can be accomplished with &#8216;sg_modes -p=1a -r /dev/sdb &gt; mp_1a.txt&#8217; (the power condition mode page). The mp_1a.txt file can be edited and then used as the contents string to this utility (e.g. &#8216;sg_wr_mode -p 1a -s -c &#8211; /dev/sdb &lt; mp_1a.txt&#8217;). </p>
<p> Two fields differ between what is read from the device with MODE SENSE and what is written to the device with MODE SELECT: the mode data length is reserved (i.e. zero(es)) in a MODE SELECT command while the PS bit ((sub)page byte 0 bit 7) in each mode (sub)page is reserved (zero) in a MODE SELECT command. The PS bit given in the contents string is zeroed unless the <i>&#8211;force</i> option is selected.</p>
<h2>Examples</h2>
<p>This utility can be used together with the sg_modes utility. To re-instate the default mode page values (i.e. the mode page values chosen by the manufacturer of the device) as both the current and saved mode page values the following sequence could be used: </p>
<pre><code>$ sg_modes --control=2 --page=1a -r /dev/sda &gt; t

$ sg_wr_mode --page=1a --contents=- --save /dev/sda &lt; t</code></pre>
<p> Next is an example of using a mask to modify the &quot;idle condition counter&quot; of the &quot;power condition&quot; mode page (0x1a) from 0x28 to 0x37. Note that the change is not saved so the &quot;idle condition counter&quot; will revert to 0x28 after the next power cycle. The output from sg_modes is abridged. </p>
<pre><code>$ sg_modes --page=1a /dev/hdc


&gt;&gt; Power condition (mmc), page_control: current


00     1a 0a 00 03 00 00 00 28  00 00 01 2c</code></pre>
<p>&nbsp;<wbr>$&nbsp;<wbr>sg_wr_mode -p 1a -c 0,0,0,0,0,0,0,37 -m 0,0,0,0,0,0,0,ff&nbsp;<wbr>/dev/hdc<br />
&nbsp;<wbr>$&nbsp;<wbr>sg_modes -p 1a&nbsp;<wbr>/dev/hdc </p>
<p>&nbsp;<wbr>&gt;&gt;&nbsp;<wbr>Power condition&nbsp;<wbr>(mmc), page_control: current </p>
<p>&nbsp;<wbr>00&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>1a 0a 00 03 00 00 00 37&nbsp;<wbr>&nbsp;<wbr>00 00 01 2c</p>
<h2>Exit Status</h2>
<p>The exit status of sg_wr_mode is 0 when it is successful. Otherwise see the <a href="/docs/linux/man/8-sg3_utils/">sg3_utils</a>(8) man page.</p>
<h2>Authors</h2>
<p>Written by Douglas Gilbert.</p>
<h2>Reporting Bugs</h2>
<p>Report bugs to &lt;dgilbert at interlog dot com&gt;.</p>
<h2>Copyright</h2>
<p>Copyright &#169; 2004-2012 Douglas Gilbert<br />
 This software is distributed under a FreeBSD license. There is NO warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.</p>
<h2>See Also</h2>
<p><code>sdparm(sdparm), sg_modes(sg3_utils), sginfo(sg3_utils)</code> </p>
