---
title: "opafequery(8)"
name: "opafequery"
section: "8"
letter: "o"
url: "/docs/linux/man/8-opafequery/"
description: "opafequery"
---

<p>opafequery </p>
<p> <code>(All)</code> Used for testing or debugging performance administration (PA) operations to the Fabric Executive (FE). This tool performs custom PA client/server queries. The output formats and arguments are very similar to opapaquery.</p>
<h2>Syntax</h2>
<p>opafequery [-v] [-a <i>ipAddr</i>| -h <i>hostName</i>] [-E] [-T paramsfile] -o <i>type</i>[SA options | PA options]</p>
<h2>General Options</h2>
<dl>
<dt>&#8211;help</p>
<dd>Produce this help text. </p>
<dt>-v / &#8211;verbose</p>
<dd>Verbose output.</p>
<dt>-a / &#8211;ipAddr <i>ipAddr</i></p>
<dd>IP address of node running the FE.</p>
<dt>-h / &#8211;hostName <i>hostName</i></p>
<dd>Host name of node running the FE.</p>
<dt>-o / &#8211;output <i>output</i></p>
<dd>Output type. See <i>SA Output Types</i> and <i>PA Output Types</i> for details.</p>
<dt>-E / &#8211;feEsm <i>ESMName</i></p>
<dd>ESM FE name.</p>
<dt>-T / &#8211;sslParmsFile <i>filename</i></p>
<dd>SSL/TLS parameters XML file. Default = /etc/sysconfig/opa/opaff.xml</dl>
<h2>SA Specific Options</h2>
<dl>
<dt>-I / &#8211;IB</p>
<dd>Issues query in legacy InfiniBand* format.</p>
<dt>-l / &#8211;lid <i>lid</i></p>
<dd>Queries a specific LID.</p>
<dt>-k / &#8211;pkey <i>pkey</i></p>
<dd>Queries a specific pkey.</p>
<dt>-i / &#8211;vfindex <i>vfindex</i></p>
<dd>Queries a specific vfindex.</p>
<dt>-S / &#8211;serviceId <i>serviceId</i></p>
<dd>Queries a specific service ID.</p>
<dt>-L / &#8211;SL <i>SL</i></p>
<dd>Queries by service level.</p>
<dt>-t / &#8211;type <i>type</i></p>
<dd>Queries by node type.</p>
<dt>-s / &#8211;sysguid <i>guid</i></p>
<dd>Queries by system image GUID.</p>
<dt>-n / &#8211;nodeguid <i>guid</i></p>
<dd>Queries by node GUID.</p>
<dt>-p / &#8211;portguid <i>guid</i></p>
<dd>Queries by port GUID.</p>
<dt>-u / &#8211;portgid <i>gid</i></p>
<dd>Queries by port GID.</p>
<dt>-m / &#8211;mcgid <i>gid</i></p>
<dd>Queries by multicast GID.</p>
<dt>-d / &#8211;desc <i>name</i></p>
<dd>Queries by node name/description.</p>
<dt>-P / &#8211;guidpair <i>&#8216;guid guid&#8217;</i></p>
<dd>Queries by a pair of port GUIDs.</p>
<dt>-G / &#8211;gidpair <i>&#8216;gid gid&#8217;</i></p>
<dd>Queries by a pair of GIDs.</p>
<dt>-B / &#8211;guidlist <i>&#8216;sguid &#8230;;dguid &#8230;&#8217;</i></p>
<dd>Queries by a list of port GUIDs.</p>
<dt>-A / &#8211;gidlist <i>&#8216;sgid &#8230;;dgid &#8230;&#8217;</i></p>
<dd>Queries by a list of GIDs.</p>
<dt>-x / &#8211;sourcegid <i>gid</i></p>
<dd>Specifies a source GID for certain queries.</dl>
<h2>PA Specific Options</h2>
<dl>
<dt>-g / &#8211;groupName <i>groupName</i></p>
<dd>Group name for groupInfo query.</p>
<dt>-l / &#8211;lid <i>lid</i></p>
<dd>LID of node for portCounters query.</p>
<dt>-N / &#8211;portNumber</p>
<dd>Port number for portCounters query.</p>
<dt>-f / &#8211;delta</p>
<dd>Delta flag for portCounters query. Values include: 0 or 1.</p>
<dt>-U / &#8211;userCntrs</p>
<dd>User-controlled counters flag for portCounters query.</p>
<dt>-e / &#8211;select</p>
<dd>32-bit select flag for clearing port counters select bits. 0 is least significant (rightmost).Bit descriptions are listed below in the order &quot;mask &#8211; bit &#8211; location&quot;: </p>
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
<dd>0x00001000 &#8211; 12 &#8211; Receive Remote Phys. Errors </p>
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
<dt>-c / &#8211;focus <i>focus</i></p>
<dd>Focus select value for getting focus ports. Values include:</p>
<dl>
<dd>
<dl>
<dd>utilhigh Sorted by utilization &#8211; highest first.</dl>
</dl>
<dl>
<dd>
<dl>
<dd>pktrate Sorted by packet rate &#8211; highest first.</dl>
</dl>
<dl>
<dd>
<dl>
<dd>utillow Sorted by utilization &#8211; lowest first.</dl>
</dl>
<dl>
<dd>
<dl>
<dd>integrity Sorted by integrity errors &#8211; highest first.</dl>
</dl>
<dl>
<dd>
<dl>
<dd>congestion Sorted by congestion errors &#8211; highest first.</dl>
</dl>
<dl>
<dd>
<dl>
<dd>smacongesion Sorted by SMA congestion errors &#8211; highest first.</dl>
</dl>
<dl>
<dd>
<dl>
<dd>bubbles Sorted by bubble errors &#8211; highest first.</dl>
</dl>
<dl>
<dd>
<dl>
<dd>security Sorted by security errors &#8211; highest first.</dl>
</dl>
<dl>
<dd>
<dl>
<dd>routing Sorted by routing errors &#8211; highest first.</dl>
</dl>
<dt>-w / &#8211;start</p>
<dd>Start of window for focus ports &#8211; should always be 0.</p>
<dt>-r / &#8211;range <i>range</i></p>
<dd>Size of window for focus ports list.</p>
<dt>-b / &#8211;imgNum</p>
<dd>64-bit image number. May be used with groupInfo, groupConfig, portCounters (delta) outputs.</p>
<dt>-O / &#8211;imgOff</p>
<dd>Image offset. May be used with groupInfo, groupConfig, portCounters (delta) outputs.</p>
<dt>-F / &#8211;moveImgNum</p>
<dd>64-bit image number. Used with moveFreeze output to move a freeze image.</p>
<dt>-M / &#8211;moveImgOff <i>ImgOff</i></p>
<dd>Image offset. May be used with moveFreeze output to move a freeze image.</p>
<dt>-V / &#8211;vfName</p>
<dd>VF name for vfInfo query.</dl>
<h2>SA Output Types</h2>
<p>Output types include:</p>
<dl>
<dt>saclassPortInfo</p>
<dd>Class port info.</p>
<dt>systemguid</p>
<dd>List of system image GUIDs.</p>
<dt>nodeguid</p>
<dd>List of node GUIDs.</p>
<dt>portguid</p>
<dd>List of port GUIDs.</p>
<dt>lid</p>
<dd>List of LIDs.</p>
<dt>desc</p>
<dd>List of node descriptions/names.</p>
<dt>path</p>
<dd>List of path records.</p>
<dt>node</p>
<dd>List of node records.</p>
<dt>portinfo</p>
<dd>List of port info records.</p>
<dt>sminfo</p>
<dd>List of SM info records.</p>
<dt>swinfo</p>
<dd>List of switch info records.</p>
<dt>link</p>
<dd>List of link records.</p>
<dt>scsc</p>
<dd>List of SC to SC mapping table records.</p>
<dt>slsc</p>
<dd>List of SL to SC mapping table records.</p>
<dt>scsl</p>
<dd>List of SC to SL mapping table records.</p>
<dt>scvlt</p>
<dd>List of SC to VLt table records.</p>
<dt>scvlnt</p>
<dd>List of SC to VLnt table records.</p>
<dt>vlarb</p>
<dd>List of VL arbitration table records.</p>
<dt>pkey</p>
<dd>List of PKey table records.</p>
<dt>service</p>
<dd>List of service records.</p>
<dt>mcmember</p>
<dd>List of multicast member records.</p>
<dt>inform</p>
<dd>List of inform info records.</p>
<dt>linfdb</p>
<dd>List of switch linear forwarding database (FDB) records.</p>
<dt>mcfdb</p>
<dd>List of switch multicast FDB records.</p>
<dt>trace</p>
<dd>List of trace records.</p>
<dt>vfinfo</p>
<dd>List of vFabrics.</p>
<dt>vfinfocsv</p>
<dd>List of vFabrics in CSV format.</p>
<dt>vfinfocsv2</p>
<dd>List of vFabrics in CSV format with enums.</p>
<dt>fabricinfo</p>
<dd>Summary of fabric devices.</p>
<dt>quarantine</p>
<dd>List of quarantined nodes.</p>
<dt>conginfo</p>
<dd>List of Congestion Info Records.</p>
<dt>swcongset</p>
<dd>List of Switch Congestion Settings.</p>
<dt>hficongset</p>
<dd>List of HFI Congestion Settings.</p>
<dt>hficongcon</p>
<dd>List of HFI Congestion Control Settings.</p>
<dt>bfrctrl</p>
<dd>List of buffer control tables.</p>
<dt>cableinfo</p>
<dd>List of Cable Info records.</p>
<dt>portgroup</p>
<dd>List of AR Port Group records.</p>
<dt>portgroupfdb</p>
<dd>List of AR Port Group FWD records.</dl>
<h2>PA Output Types</h2>
<dl>
<dt>paclassPortInfo</p>
<dd>Class port info.</p>
<dt>groupList</p>
<dd>List of PA groups.</p>
<dt>groupInfo</p>
<dd>Summary statistics of a PA group. Requires -g option for <i>groupName</i>.</p>
<dt>groupConfig</p>
<dd>Configuration of a PA group. Requires -g option for <i>groupName</i>.</p>
<dt>portCounters</p>
<dd>Port counters of fabric port. Requires -l <i>lid</i> and -N <i>port</i> options. Optionally, use the -f <i>delta</i> option.</p>
<dt>clrPortCounters</p>
<dd>Clears port counters of fabric port. Requires -l <i>lid</i>, -N <i>port</i>, and -e <i>select</i> options.</p>
<dt>clrAllPortCounters</p>
<dd>Clears all port counters in fabric.</p>
<dt>pmConfig</p>
<dd>Retrieves PM configuration information.</p>
<dt>freezeImage</p>
<dd>Creates freeze frame for image ID. Requires -b <i>imgNum</i>.</p>
<dt>releaseImage</p>
<dd>Releases freeze frame for image ID. Requires -b <i>imgNum</i>.</p>
<dt>renewImage</p>
<dd>Renews lease for freeze frame for image ID. Requires -b#8217#160; <i>imgNum</i>.</p>
<dt>moveFreeze</p>
<dd>Moves freeze frame from image ID to new image ID. Requires -b#8217#160; <i>imgNum</i> and -F <i>moveImgNum</i>.</p>
<dt>focusPorts</p>
<dd>Gets sorted list of ports using utilization or error values (from group buckets).</p>
<dt>imageInfo</p>
<dd>Gets information about a PA image (timestamps and other details). Requires -b <i>imgNum</i>.</p>
<dt>vfList</p>
<dd>List of virtual fabrics.</p>
<dt>vfInfo</p>
<dd>Summary statistics of a virtual fabric. Requires -V <i>vfName</i> option.</p>
<dt>vfConfig</p>
<dd>Configuration of a virtual fabric. Requires -V <i>vfName</i> option.</p>
<dt>vfPortCounters</p>
<dd>Port counters of fabric port. Requires -V <i>vfName</i>, -l <i>lid</i>, and -N <i>port</i> options. Optionally, use the -f <i>delta</i> option.</p>
<dt>vfFocusPorts</p>
<dd>Gets sorted list of virtual fabric ports usingutilization or error values (from VF buckets). Requires -V <i>vfName</i> option.</p>
<dt>clrVfPortCounters</p>
<dd>Clears VF port counters of fabric port. Requires -l <i>lid</i>, -N <i>port</i>, -e <i>select</i>, and -V <i>vfName</i> options.</dl>
<h2>Examples</h2>
<p>opafequery -o saclassPortInfo<br />
 opafequery -h stewie -o paclassPortInfo<br />
 opafequery -a 172.21.2.155 -o saclassPortInfo<br />
 opafequery -o groupList<br />
 opafequery -o groupInfo -g All<br />
 opafequery -o groupConfig -g All<br />
 opafequery -h stewie -o groupInfo -g All<br />
 opafequery -a 172.21.2.155 -o groupInfo -g All<br />
 opafequery -o portCounters -l 1 -N 1 -d 1<br />
 opafequery -o portCounters -l 1 -N 1 -d 1 -e 0x20000000d02 -O 1<br />
 opafequery -o pmConfig<br />
 opafequery -o freezeImage 0x20000000d02<br />
 opafequery -o releaseImage -b 0xd01<br />
 opafequery -o renewImage -b 0xd01<br />
 opafequery -o moveFreeze -b 0xd01 -m 0x20000000d02 -M -2<br />
 opafequery -o focusPorts -g All -f 0x00030001 -w 0 -r 20<br />
 opafequery -o imageInfo -b 0x20000000d02 </p>
