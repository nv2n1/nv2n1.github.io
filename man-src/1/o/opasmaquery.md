---
title: "opasmaquery(1)"
name: "opasmaquery"
section: "1"
letter: "o"
url: "/docs/linux/man/1-opasmaquery/"
description: "opasmaquery"
---

<h2>NAME</h2>
<p> opasmaquery </p>
<p> <code>(All)</code> Performs Intel(R) Omni-Path Architecture-defined SMA queries and displays the resulting response. Each query is issued directly to the SMA and does not involve SM interaction.</p>
<h2>Syntax</h2>
<p> opasmaquery [-v] [-d <i>detail</i>][-g] [-l <i>lid</i>] [-h <i>hfi</i>] [-p <i>port</i>] [-K <i>mkey</i>] [-o <i>otype</i>] [-m <i>port</i>| <i>port1,port2</i>] [-f <i>flid</i>] [-b <i>block[,count]</i>] [hop hop &#8230;]</p>
<h2>Options</h2>
<dl>
<dt>&#8211;help</p>
<dd> Produces full help text. </p>
<dt>-v</p>
<dd> Returns verbose output. Can be specified more than once for additional openib and libibumad debugging. </p>
<dt>-d <i>detail</i></p>
<dd> Output detail level for cableinfo only. Range = 0 &#8211; n. Default = 2. An upper limit for detail level is not enforced. After a maximum amount of output is reached, a larger detail value has no effect. </p>
<dt>-g</p>
<dd> Displays line-by-line format. Default is summary format. </p>
<dt>-l <i>lid</i></p>
<dd> Destination LID. Default is local port. </p>
<dt>-h <i>hfi</i></p>
<dd> HFI, numbered 1..n. Using 0 specifies that the -p <i>port</i> port is a system-wide port number. Default is 0. </p>
<dt>-p <i>port</i></p>
<dd> Port, numbered 1..n. If -h <i>hfi</i> is 0, then <i>port</i> is a system-wide port number. Default is 1. </p>
<dt>-K <i>mkey</i></p>
<dd> SM management key to access remote ports. </p>
<dt>-o <i>otype</i></p>
<dd> Output type. Default is nodeinfo. </p>
<dt>
<dd> Valid output types are:</p>
<dl>
<dt>
<dd>
<dl>
<dt>
<dd>
<p> bfrctrl Buffer control tables. </p>
<dt>
<dd> [-m dest_port] [-m port1,port2]</dl>
</dl>
<dl>
<dt>
<dd>
<dl>
<dt>
<dd>
<p> cableinfo Cable information. </p>
<dt>
<dd> [-d detail] [-m dest_port] [-b block[,count]]</dl>
</dl>
<dl>
<dt>
<dd>
<dl>
<dt>
<dd>
<p> conginfo Congestion information. </p>
</dl>
</dl>
<dl>
<dt>
<dd>
<dl>
<dt>
<dd>
<p> desc or nodedesc Node descriptions/names. </p>
</dl>
</dl>
<dl>
<dt>
<dd>
<dl>
<dt>
<dd>
<p> hficongcon HFI congestion control settings. </p>
<dt>
<dd> [-b block[,count]] [-f flid]</dl>
</dl>
<dl>
<dt>
<dd>
<dl>
<dt>
<dd>
<p> hficonglog HFI congestion logs. </p>
<dt>
<dd> [-b block[,count]]</dl>
</dl>
<dl>
<dt>
<dd>
<dl>
<dt>
<dd>
<p> hficongset HFI congestion settings. </p>
</dl>
</dl>
<dl>
<dt>
<dd>
<dl>
<dt>
<dd>
<p> linfdb Switch linear forwarding database (FDB) tables. </p>
<dt>
<dd> [-b block[,count]] [-f flid]</dl>
</dl>
<dl>
<dt>
<dd>
<dl>
<dt>
<dd>
<p> mcfdb Switch multicast FDB tables. </p>
<dt>
<dd> [-m dest_port] [-b block[,count]] [-f flid]</dl>
</dl>
<dl>
<dt>
<dd>
<dl>
<dt>
<dd>
<p> portgroup Adaptive Routing port groups. </p>
<dt>
<dd> [-b block[,count]]</dl>
</dl>
<dl>
<dt>
<dd>
<dl>
<dt>
<dd>
<p> portgroupfdb Adaptive Routing port group FWD tables. </p>
<dt>
<dd> [-b block[,count]] [-f flid]</dl>
</dl>
<dl>
<dt>
<dd>
<dl>
<dt>
<dd>
<p> nodeaggr Node information and node descriptions. </p>
</dl>
</dl>
<dl>
<dt>
<dd>
<dl>
<dt>
<dd>
<p> node or nodeinfo Node information. </p>
<dt>
<dd> [-m dest_port]</dl>
</dl>
<dl>
<dt>
<dd>
<dl>
<dt>
<dd>
<p> portinfo Port information. </p>
<dt>
<dd> [-m dest_port]</dl>
</dl>
<dl>
<dt>
<dd>
<dl>
<dt>
<dd>
<p> pstateinfo Switch port state information. </p>
<dt>
<dd> [-m dest_port] [-m port1,port2]</dl>
</dl>
<dl>
<dt>
<dd>
<dl>
<dt>
<dd>
<p> pkey P-Key tables. </p>
<dt>
<dd> [-m dest_port] [-b block[,count]]</dl>
</dl>
<dl>
<dt>
<dd>
<dl>
<dt>
<dd>
<p> slsc SL to SC mapping tables. </p>
</dl>
</dl>
<dl>
<dt>
<dd>
<dl>
<dt>
<dd>
<p> scsl SC to SL mapping tables. </p>
</dl>
</dl>
<dl>
<dt>
<dd>
<dl>
<dt>
<dd>
<p> scsc SC to SC mapping tables. </p>
<dt>
<dd> [-m dest_port] [-m port1,port2]</dl>
</dl>
<dl>
<dt>
<dd>
<dl>
<dt>
<dd>
<p> scvlt SC to VLt tables. </p>
<dt>
<dd> [-m dest_port] [-m port1,port2]</dl>
</dl>
<dl>
<dt>
<dd>
<dl>
<dt>
<dd>
<p> scvlnt SC to VLnt tables. </p>
<dt>
<dd> [-m dest_port] [-m port1,port2]</dl>
</dl>
<dl>
<dt>
<dd>
<dl>
<dt>
<dd>
<p> sminfo SM information. </p>
</dl>
</dl>
<dl>
<dt>
<dd>
<dl>
<dt>
<dd>
<p> swaggr Node information and switch information. </p>
</dl>
</dl>
<dl>
<dt>
<dd>
<dl>
<dt>
<dd>
<p> swconglog Switch congestion logs. </p>
<dt>
<dd> [-b block[,count]]</dl>
</dl>
<dl>
<dt>
<dd>
<dl>
<dt>
<dd>
<p> swcongset Switch congestion settings. </p>
</dl>
</dl>
<dl>
<dt>
<dd>
<dl>
<dt>
<dd>
<p> swinfo Switch information. </p>
</dl>
</dl>
<dl>
<dt>
<dd>
<dl>
<dt>
<dd>
<p> swportcong Switch congestion settings. </p>
<dt>
<dd> [-b block[,count]]</dl>
</dl>
<dl>
<dt>
<dd>
<dl>
<dt>
<dd>
<p> vlarb VL arbitration tables. </p>
<dt>
<dd> [-m dest_port]</dl>
</dl>
<dl>
<dt>
<dd>
<dl>
<dt>
<dd>
<p> ibnodeinfo IB node information. </p>
</dl>
</dl>
<dl>
<dt>
<dd>
<dl>
<dt>
<dd>
<p> ledinfo LED information. </p>
<dt>
<dd> [-m dest_port]</dl>
</dl>
</dl>
<h2>-h and -p options permit a variety of selections:</h2>
<dl>
<dt>-h 0</p>
<dd> First active port in system (default). </p>
<dt>-h 0 -p 0</p>
<dd> First active port in system. </p>
<dt>-h <i>x</i></p>
<dd> First active port on HFI <i>x</i>. </p>
<dt>-h <i>x</i>#8217#160;-p 0</p>
<dd> First active port on HFI <i>x</i>. </p>
<dt>-h 0 -p <i>y</i></p>
<dd> Port <i>y#8217#160;</i> within system (no matter which ports are active). </p>
<dt>-h <i>x</i>#8217#160;-p <i>y</i></p>
<dd> HFI <i>x</i>, port <i>y</i> </p>
</dl>
<h2>otype Options Vary by Report</h2>
<dl>
<dt>-m <i>port</i></p>
<dd> Port in destination device to query. </p>
<dt>-m <i>port1,port2</i></p>
<dd> For some reports, a range of ports between <i>port1</i> and <i>port2</i>. For others, this describes an inport/outport pair. </p>
<dt>-f <i>flid</i></p>
<dd> LID to look up in forwarding table to select which LFT or MFT block to display. Default is to show entire table. </p>
<dt>-b <i>block[,count]</i></p>
<dd> Block number of either GUIDs or pkey, and the number of blocks to display. Default is to show entire table. </p>
<dt>
<dd> For example:</p>
<dt>
<dd>
<dl>
<dt>
<dd>
<dl>
<dt>
<dd>
<p> -b <i>block</i> Displays all of block <i>block</i> of a larger table. </p>
</dl>
</dl>
<dl>
<dt>
<dd>
<dl>
<dt>
<dd>
<p> -b <i>block,count</i> Displays <i>count</i> blocks of data starting with block <i>block</i>. </p>
</dl>
</dl>
<dl>
<dt>
<dd>
<dl>
<dt>
<dd>
<p> -b, <i>count</i> Displays <i>count</i> blocks of data starting with block 0. </p>
</dl>
</dl>
</dl>
<h2>Examples</h2>
<p> opasmaquery -o desc -l 6<br />
 # get nodedesc via lid routed </p>
<p> opasmaquery -o nodedesc 1 3<br />
 # get nodedesc via directed route (2 dr hops) </p>
<p> opasmaquery -o nodeinfo -l 2 3<br />
 # get nodeinfo via a combination of lid routed and # directed route (1 dr hop) </p>
<p> opasmaquery -o portinfo<br />
 # get local port info </p>
<p> opasmaquery -o portinfo -l 6 -m 1<br />
 # get port info of port 1 of lid 6 </p>
<p> opasmaquery -o pkey -l 2 3<br />
 # get pkey table entries starting (lid routed to lid 2,<br />
 # then 1 dr hop to port 3) </p>
<p> opasmaquery -o vlarb -l 6<br />
 # get vlarb table entries from lid 6 </p>
<p> opasmaquery -o swinfo -l 2<br />
 # get switch info </p>
<p> opasmaquery -o sminfo -l 1<br />
 # get SM info </p>
<p> opasmaquery -o slsc -l 3<br />
 # get sl2sc table entries from lid 3 </p>
<p> opasmaquery -o scsl -l 3<br />
 # get sc2sl table entries from lid 3 </p>
<h2>Index</h2>
