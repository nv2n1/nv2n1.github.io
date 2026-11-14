---
title: "opapaquery(8)"
name: "opapaquery"
section: "8"
letter: "o"
url: "/docs/linux/man/8-opapaquery/"
description: "opapaquery"
---

<p>opapaquery </p>
<p> <code>(All)</code> Performs various queries of the performance management (PM)/performance administration (PA) agent and provides details about fabric performance. Refer to the <i>Intel(R) Omni-Path Fabric Suite Fabric Manager User Guide</i> </p>
<p> for a description of the operation and client services of the PM/PA. </p>
<p> By default, opapaquery queries the most recent data. However, if an image number ( <i>imgNum</i>) and/or image offset ( <i>imgOff</i>) is provided, the query returns previous sweep data. Queries that access previous sweep data return with the absolute image number representing that data, and therefore have an image offset of zero. </p>
<p> opapaquery #8217#8217;s operation is dependent on an Intel(R) Omni-Path Fabric Suite Fabric Manager version 6.0 or greater running as master SM/PM in the fabric. </p>
<p> By default, opapaquery uses the first active port on the local system. However, if the Fabric Management Node is connected to more than one fabric (for example, a subnet), the HFI and port may be specified to select the fabric whose PA is to be queried.</p>
<h2>Syntax</h2>
<p>opapaquery [-v] [-h <i>hfi</i>] [-p <i>port</i>] -o <i>type</i>[-g <i>groupName</i>] [-l <i>nodeLid</i>]<br />
 [-P <i>portNumber</i>] [-d <i>delta</i>] [-s <i>select</i>] [-f <i>focus</i>] [-S <i>start</i>]<br />
 [-r <i>range</i>] [-n <i>imgNum</i>] [-O <i>imgOff</i>] [-m <i>moveImgNum</i>] [-M <i>moveImgOff</i>]<br />
 [-V vfName]</p>
<h2>Options</h2>
<dl>
<dt>-v/&#8211;verbose</p>
<dd>Verbose output. </p>
<dt>-h/&#8211;hfi <i>hfi</i></p>
<dd>HFI, numbered 1..n. Using 0 specifies that the -p <i>port</i> port is a system-wide port number. (Default is 0.) </p>
<dt>-p/&#8211;port <i>port</i></p>
<dd>Port, numbered 1..n. If -h <i>hfi</i> is 0, then <i>port</i> is a system-wide port number. (Default is 1.) </p>
<dt>-o/&#8211;output <i>type</i></p>
<dd>Output type, default is groupList. See <i>Output Types</i> </p>
<dt>-g/&#8211;groupName <i>groupName</i></p>
<dd>Group name for groupInfo query. </p>
<dt>-l/&#8211;lid <i>lid</i></p>
<dd>LID of node for portCounters query. </p>
<dt>-P/&#8211;portNumber <i>portNumber</i></p>
<dd>Port number for portCounters query. </p>
<dt>-d/&#8211;delta <i>delta</i></p>
<dd>Delta flag for portCounters query &#8211; 0 or 1. </p>
<dt>-s/&#8211;select <i>select</i></p>
<dd>32-bit select flag for clearing port counters. </p>
<dd>Select bits for clrPortCounters. 0 is least significant (rightmost).</p>
<dd>clrPortCounters bit descriptions listed in the order &quot;mask &#8211; bit &#8211; location&quot;:</p>
<dl>
<dd>
<dl>
<dt>&bull;</p>
<dd>0x80000000 &#8211; 31 &#8211; Transmit Data </p>
<dt>&bull;</p>
<dd>0x40000000 &#8211; 30 &#8211; Receive Data </p>
<dt>&bull;</p>
<dd>0x20000000 &#8211; 29 &#8211; Transmit Packets </p>
<dt>&bull;</p>
<dd>0x10000000 &#8211; 28 &#8211; Receive Packets </p>
<dt>&bull;</p>
<dd>0x08000000 &#8211; 27 &#8211; Multicast Transmit Packets </p>
<dt>&bull;</p>
<dd>0x04000000 &#8211; 26 &#8211; Multicast Receive Packets </p>
<dt>&bull;</p>
<dd>0x02000000 &#8211; 25 &#8211; Transmit Wait </p>
<dt>&bull;</p>
<dd>0x01000000 &#8211; 24 &#8211; Congestion Discards </p>
<dt>&bull;</p>
<dd>0x00800000 &#8211; 23 &#8211; Receive FECN </p>
<dt>&bull;</p>
<dd>0x00400000 &#8211; 22 &#8211; Receive BECN </p>
<dt>&bull;</p>
<dd>0x00200000 &#8211; 21 &#8211; Transmit Time Cong. </p>
<dt>&bull;</p>
<dd>0x00100000 &#8211; 20 &#8211; Transmit Time Wasted BW </p>
<dt>&bull;</p>
<dd>0x00080000 &#8211; 19 &#8211; Transmit Time Wait Data </p>
<dt>&bull;</p>
<dd>0x00040000 &#8211; 18 &#8211; Receive Bubble </p>
<dt>&bull;</p>
<dd>0x00020000 &#8211; 17 &#8211; Mark FECN </p>
<dt>&bull;</p>
<dd>0x00010000 &#8211; 16 &#8211; Receive Constraint Errors </p>
<dt>&bull;</p>
<dd>0x00008000 &#8211; 15 &#8211; Receive Switch Relay </p>
<dt>&bull;</p>
<dd>0x00004000 &#8211; 14 &#8211; Transmit Discards </p>
<dt>&bull;</p>
<dd>0x00002000 &#8211; 13 &#8211; Transmit Constraint Errors </p>
<dt>&bull;</p>
<dd>0x00001000 &#8211; 12 &#8211; Receive Remote Physical Errors </p>
<dt>&bull;</p>
<dd>0x00000800 &#8211; 11 &#8211; Local Link Integrity </p>
<dt>&bull;</p>
<dd>0x00000400 &#8211; 10 &#8211; Receive Errors </p>
<dt>&bull;</p>
<dd>0x00000200 &#8211; 9 &#8211; Exc. Buffer Overrun </p>
<dt>&bull;</p>
<dd>0x00000100 &#8211; 8 &#8211; FM Configuration Errors </p>
<dt>&bull;</p>
<dd>0x00000080 &#8211; 7 &#8211; Link Error Recovery </p>
<dt>&bull;</p>
<dd>0x00000040 &#8211; 6 &#8211; Link Error Downed </p>
<dt>&bull;</p>
<dd>0x00000020 &#8211; 5 &#8211; Uncorrectable Errors </p>
</dl>
</dl>
<dd>Select bits for clrVfPortCounters. 0 is least significant (rightmost).</p>
<dd>clrVfPortCounters bit descriptions listed in the order &quot;mask &#8211; bit &#8211; location&quot;:</p>
<dl>
<dd>
<dl>
<dt>&bull;</p>
<dd>0x80000000 &#8211; 31 &#8211; VLXmitData </p>
<dt>&bull;</p>
<dd>0x40000000 &#8211; 30 &#8211; VLRcvData </p>
<dt>&bull;</p>
<dd>0x20000000 &#8211; 29 &#8211; VLXmitPkts </p>
<dt>&bull;</p>
<dd>0x10000000 &#8211; 28 &#8211; VLRcvPkts </p>
<dt>&bull;</p>
<dd>0x08000000 &#8211; 27 &#8211; VLXmitDiscards </p>
<dt>&bull;</p>
<dd>0x04000000 &#8211; 26 &#8211; VLCongDiscards </p>
<dt>&bull;</p>
<dd>0x02000000 &#8211; 25 &#8211; VLXmitWait </p>
<dt>&bull;</p>
<dd>0x01000000 &#8211; 24 &#8211; VLRcvFECN </p>
<dt>&bull;</p>
<dd>0x00800000 &#8211; 23 &#8211; VLRcvBECN </p>
<dt>&bull;</p>
<dd>0x00400000 &#8211; 22 &#8211; VLXmitTimeCong </p>
<dt>&bull;</p>
<dd>0x00200000 &#8211; 21 &#8211; VLXmitWastedBW </p>
<dt>&bull;</p>
<dd>0x00100000 &#8211; 20 &#8211; VLXmitWaitData </p>
<dt>&bull;</p>
<dd>0x00080000 &#8211; 19 &#8211; VLRcvBubble </p>
<dt>&bull;</p>
<dd>0x00040000 &#8211; 18 &#8211; VLMarkFECN </p>
<dt>&bull;</p>
<dd>Bits 17-0 reserved </p>
</dl>
</dl>
<dt>-f/&#8211;focus <i>focus</i></p>
<dd>Focus select value for getting <i>focus</i> ports. </p>
<dd>&nbsp;<wbr><i>focus</i>&nbsp;<wbr>select values:</p>
<dl>
<dd>
<dl>
<dd>utilhigh Sorted by utilization &#8211; highest first. </p>
</dl>
</dl>
<dl>
<dd>
<dl>
<dd>pktrate Sorted by packet rate &#8211; highest first. </p>
</dl>
</dl>
<dl>
<dd>
<dl>
<dd>utillow Sorted by utilization &#8211; lowest first. </p>
</dl>
</dl>
<dl>
<dd>
<dl>
<dd>integrity Sorted by integrity errors &#8211; highest first. </p>
</dl>
</dl>
<dl>
<dd>
<dl>
<dd>congestion Sorted by congestion errors &#8211; highest first. </p>
</dl>
</dl>
<dl>
<dd>
<dl>
<dd>smacongestion Sorted by SMA congestion errors &#8211; highest first. </p>
</dl>
</dl>
<dl>
<dd>
<dl>
<dd>bubbles Sorted by bubble errors &#8211; highest first.</dl>
</dl>
<dl>
<dd>
<dl>
<dd>security Sorted by security errors &#8211; highest first. </p>
</dl>
</dl>
<dl>
<dd>
<dl>
<dd>routing Sorted by routing errors &#8211; highest first. </p>
</dl>
</dl>
<dt>-S/&#8211;start <i>start</i></p>
<dd>Start of window for focus ports, should always be 0. </p>
<dt>-r/&#8211;range <i>range</i></p>
<dd>Size of window for focus ports list. </p>
<dt>-n/&#8211;imgNum <i>imgNum</i></p>
<dd>64-bit image number. Can be used with groupInfo, groupConfig, portCounters (delta). </p>
<dt>-O/&#8211;imgOff <i>imgOff</i></p>
<dd>Image offset. Can be used with groupInfo, groupConfig, portCounters (delta). </p>
<dt>-m/&#8211;moveImgNum <i>moveImgNum</i></p>
<dd>64-bit image number. Used with moveFreeze to move a freeze image. </p>
<dt>-M/&#8211;moveImgOff <i>moveImgOff</i></p>
<dd>Image offset. Can be used with moveFreeze to move a freeze image. </p>
<dt>-V/&#8211;vfName <i>vfName</i></p>
<dd>VF name for vfInfo query. </p>
<dt><code>-h and -p options permit a variety of selections:</code></p>
<dd>
<dt>-h 0</p>
<dd>First active port in system (default). </p>
<dt>-h 0 -p 0</p>
<dd>First active port in system. </p>
<dt>-h <i>x</i></p>
<dd>First active port on HFI <i>x</i>. </p>
<dt>-h <i>x</i>#8217#160;-p 0</p>
<dd>First active port on HFI <i>x</i>. </p>
<dt>-h 0 -p <i>y</i></p>
<dd>Port <i>y</i>#8217#160;within system (no matter which ports are active). </p>
<dt>-h <i>x</i>#8217#160;-p <i>y</i></p>
<dd>HFI <i>x</i>, port <i>y</i>. </p>
</dl>
<h2>Output Types</h2>
<dl>
<dt>classPortInfo</p>
<dd>Class port info. </p>
<dt>groupList</p>
<dd>List of PA groups. </p>
<dt>groupInfo</p>
<dd>Summary statistics of a PA group. Requires -g option for <i>groupName</i>. </p>
<dt>groupConfig</p>
<dd>Configuration of a PA group. Requires -g option for <i>groupName</i>. </p>
<dt>portCounters</p>
<dd>Port counters of fabric port. Requires -l <i>lid</i> and -P <i>port</i> options, -d <i>delta</i> is optional. </p>
<dt>clrPortCounters</p>
<dd>Clears port counters of fabric port. Requires -l <i>lid</i> and -P#8217#160; <i>port</i>, and -s <i>select</i> options. </p>
<dt>clrAllPortCounters</p>
<dd>Clears all port counters in fabric. </p>
<dt>pmConfig</p>
<dd>Retrieves PM configuration information. </p>
<dt>freezeImage</p>
<dd>Creates freeze frame for image ID. Requires -n <i>imgNum</i>. </p>
<dt>releaseImage</p>
<dd>Releases freeze frame for image ID. Requires -n <i>imgNum</i>. </p>
<dt>renewImage</p>
<dd>Renews lease for freeze frame for image ID. Requires -n <i>imgNum</i>. </p>
<dt>moveFreeze</p>
<dd>Moves freeze frame from image ID to new image ID. Requires -n#8217#160; <i>imgNum</i> and -m <i>moveImgNum</i>. </p>
<dt>focusPorts</p>
<dd>Gets sorted list of ports using utilization or error values (from group buckets). Requires -g <i>groupname</i>, -f <i>focus</i>, -S <i>start</i>, -r <i>range</i>. </p>
<dt>imageInfo</p>
<dd>Gets configuration of a PA image (timestamps, etc.). Requires -n#8217#160; <i>imgNum</i>. </p>
<dt>vfList</p>
<dd>List of virtual fabrics. </p>
<dt>vfInfo</p>
<dd>Summary statistics of a virtual fabric. Requires -V option for <i>vfName</i>. </p>
<dt>vfConfig</p>
<dd>Configuration of a virtual fabric. Requires -V option for <i>vfName</i>. </p>
<dt>vfPortCounters</p>
<dd>Port counters of fabric port. Requires -V <i>vfName</i>, -l <i>lid</i> and -P <i>port</i> options, -d <i>delta</i> is optional. </p>
<dt>vfFocusPorts</p>
<dd>Gets sorted list of virtual fabric ports using utilization or error values (from VF buckets). Requires -V <i>vfname</i>, -f <i>focus</i>, -S <i>start</i>, -r <i>range</i>. </p>
<dt>clrVfPortCounters</p>
<dd>Clears VF port counters of fabric port. Requires -l <i>lid</i>, -P <i>port</i>, -s <i>select</i>, and -V <i>vfname</i> options. </p>
</dl>
<h2>Examples</h2>
<p>opapaquery -o classPortInfo<br />
 opapaquery -o groupList<br />
 opapaquery -o groupInfo -g All<br />
 opapaquery -o groupConfig -g All<br />
 opapaquery -o portCounters -l 1 -P 1 -d 1<br />
 opapaquery -o portCounters -l 1 -P 1 -d 1 -n 0x20000000d02 -O 1<br />
 opapaquery -o clrPortCounters -l 1 -P 1 -s 0xC0000000<br />
 #8217#160; #clears XmitData &amp; RcvData<br />
 opapaquery -o clrAllPortCounters -s 0xC0000000<br />
 #8217#160; #clears XmitData &amp; RcvData on all ports<br />
 opapaquery -o PMConfig<br />
 opapaquery -o freezeImage -n 0x20000000d02<br />
 opapaquery -o releaseImage -n 0xd01<br />
 opapaquery -o renewImage -n 0xd01<br />
 opapaquery -o moveFreeze -n 0xd01 -m 0x20000000d02 -M -2<br />
 opapaquery -o focusPorts -g All -f 0x00030001 -S 0 -r 20<br />
 opapaquery -o imageInfo -n 0x20000000d02<br />
 opapaquery -o vfList<br />
 opapaquery -o vfInfo -V Default<br />
 opapaquery -o vfConfig -V Default<br />
 opapaquery -o vfPortCounters -l 1 -P 1 -d 1 -V Default<br />
 opapaquery -o clrVfPortCounters -l 1 -P 1 -s 0xC0000000<br />
 #8217#160; #clears VLXmitData &amp; VLRcvData<br />
 opapaquery -o vfFocusPorts -V Default -f 0x00030001 -S 0 -r 20 </p>
