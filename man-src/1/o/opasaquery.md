---
title: "opasaquery(1)"
name: "opasaquery"
section: "1"
letter: "o"
url: "/docs/linux/man/1-opasaquery/"
description: "opasaquery"
---

<h2>NAME</h2>
<p> opasaquery </p>
<p> <code>(All)</code> Performs various queries of the subnet manager/subnet agent and provides detailed fabric information. </p>
<p> opareport and opareports can provide a more powerful tool, however, in some cases opasaquery is preferred, especially when dealing with virtual fabrics, service records, and multicast. </p>
<p> The command opasaquery is installed on all hosts as part of the Intel(R) Omni-Path Fabric Host Software, but it is also included in Intel(R) Omni-Path Fabric Suite FastFabric Toolset. </p>
<p> By default, opasaquery uses the first active port on the local system. However, if the node is connected to more than one fabric (for example, a subnet), the Intel(R) Omni-Path Host Fabric Interface (HFI) and port may be specified to select the fabric whose SA is to be queried.</p>
<h2>Syntax</h2>
<p> opasaquery [-v [-v] [-v]] [-I] [-h <i>hfi</i>] [-p <i>port</i>] [-o <i>type</i>] [-l <i>lid</i>]<br />
 [-t <i>type</i>] [-s <i>guid</i>] [-n <i>guid</i>] [-g <i>guid</i>] [-k <i>pkey</i>] [-i <i>vfIndex</i>]<br />
 [-S <i>serviceId</i>] [-L <i>sl</i>] [-u <i>gid</i>] [-m <i>gid</i>] [-d <i>name</i>] [-P &#8216;<i>guid guid</i>&#8216;]<br />
 [-G &#8216;<i>gid gid</i>&#8216;] [-a &#8216;<i>sguid</i>&#8230;; <i>dguid</i>&#8230;&#8217;] [-A#8217#160;&#8217;<i>sgid</i>&#8230;; <i>dgid</i>&#8230;&#8217;]</p>
<h2>Options</h2>
<dl>
<dt>&#8211;help</dt>
<dd> Produces full help text. </dd>
<dt>-v/&#8211;verbose</dt>
<dd> Returns verbose output. A second invocation activates openib debugging, a third invocation activates libibumad debugging. </dd>
<dt>-I/&#8211;IB</dt>
<dd> Issues query in legacy InfiniBand* format. </dd>
<dt>-h/&#8211;hfi <i>hfi</i></dt>
<dd> HFI, numbered 1..n. Using 0 specifies that the -p <i>port</i> is a system-wide port number. Default is 0. </dd>
<dt>-p/&#8211;port <i>port</i></dt>
<dd> Port, numbered 1..n. If 0, then <i>port</i> is a first active. Default is first active. </dd>
<dt>-o/&#8211;output <i>type</i></dt>
<dd> Output type for query (default is node). See <i>Output Types</i> for details. </dd>
<dt>-l/&#8211;lid <i>lid</i></dt>
<dd> Query a specific LID. </dd>
<dt>-t/&#8211;type <i>node_type</i></dt>
<dd> Query by node type. See <i>Node Types</i> for details. </dd>
<dt>-s/&#8211;sysguid <i>system_image_guid</i></dt>
<dd> Query by system image GUID. </dd>
<dt>-n/&#8211;nodeguid <i>node_guid</i></dt>
<dd> Query by node GUID. </dd>
<dt>-g/&#8211;portguid <i>port_guid</i></dt>
<dd> Query by port GUID. </dd>
<dt>-k/&#8211;pkey <i>pkey</i></dt>
<dd> Query a specific PKey. </dd>
<dt>-i/&#8211;vfindex <i>vfIndex</i></dt>
<dd> Query a specific vfindex. </dd>
<dt>-S/&#8211;serviceId <i>serviceId</i></dt>
<dd> Query a specific service ID. </dd>
<dt>-L/&#8211;SL <i>SL</i></dt>
<dd> Query by service level. </dd>
<dt>-u/&#8211;portgid <i>port_gid</i></dt>
<dd> Query by port GID. See <i>GIDs</i> for details. </dd>
<dt>-m/&#8211;mcgid <i>multicast_gid</i></dt>
<dd> Query by multicast GID. See <i>GIDs</i> for details. </dd>
<dt>-d/&#8211;desc <i>node_description</i></dt>
<dd> Query by node name/description. </dd>
<dt>-P/&#8211;guidpair <i>guid guid</i></dt>
<dd> Query by a pair of port GUIDs. </dd>
<dt>-G/&#8211;gidpair <i>gid gid</i></dt>
<dd> Query by a pair of GIDs. See <i>GIDs</i> for details. </dd>
<dt>-a/&#8211;guidlist <i>sguid &#8230;;dguid &#8230;</i></dt>
<dd> Query by a list of port GUIDs. </dd>
<dt>-A/&#8211;gidlist <i>sgid &#8230;;dgid &#8230;</i></dt>
<dd> Query by a list of GIDs. See <i>GIDs</i> for details. </dd>
</dl>
<h2>-h and -p options permit a variety of selections:</h2>
<dl>
<dt>-h 0</dt>
<dd> First active port in system (default). </dd>
<dt>-h 0 -p 0</dt>
<dd> First active port in system. </dd>
<dt>-h <i>x</i></dt>
<dd> First active port on HFI <i>x</i>. </dd>
<dt>-h <i>x</i>#8217#160;-p 0</dt>
<dd> First active port on HFI <i>x</i>. </dd>
<dt>-h 0 -p <i>y</i></dt>
<dd> Port <i>y</i>#8217#160;within system (no matter which ports are active). </dd>
<dt>-h <i>x</i>#8217#160;-p <i>y</i></dt>
<dd> HFI <i>x</i>, port <i>y</i>. </dd>
</dl>
<h2>Node Types</h2>
<dl>
<dt>fi</dt>
<dd> Fabric Interface </dd>
<dt>sw</dt>
<dd> Switch </dd>
</dl>
<h2>GIDs</h2>
<p> Specify a 64-bit subnet and 64-bit interface ID in the form: </p>
<p>&nbsp;<wbr><i>subnet</i>:&nbsp;<wbr><i>interface</i>&nbsp;<wbr> </p>
<p> <code>NOTE:</code> In the following example, the GID corresponds to a PortGID. In this case, the interface ID coincides with the lower 64-bits of the GUID of the card. The interface ID will be different if the GID is a MGID (that is, multicast GID). See opafm.xml for MGID examples. </p>
<p> 0xfe80000000000000:0x00117500a0000380 </p>
<h2>Output Types</h2>
<p> Default is node.</p>
<dl>
<dt>classportinfo</dt>
<dd> classportinfo of the SA. </dd>
<dt>systemguid</dt>
<dd> List of system image GUIDs. </dd>
<dt>nodeguid</dt>
<dd> List of node GUIDs. </dd>
<dt>portguid</dt>
<dd> List of port GUIDs. </dd>
<dt>lid</dt>
<dd> List of LIDs. </dd>
<dt>desc</dt>
<dd> List of node descriptions/names. </dd>
<dt>path</dt>
<dd> List of path records. </dd>
<dt>node</dt>
<dd> List of node records. </dd>
<dt>portinfo</dt>
<dd> List of port info records. </dd>
<dt>sminfo</dt>
<dd> List of SM info records. </dd>
<dt>swinfo</dt>
<dd> List of switch info records. </dd>
<dt>link</dt>
<dd> List of link records. </dd>
<dt>scsc</dt>
<dd> List of SC to SC mapping table records. </dd>
<dt>slsc</dt>
<dd> List of SL to SC mapping table records. </dd>
<dt>scsl</dt>
<dd> List of SC to SL mapping table records. </dd>
<dt>scvlt</dt>
<dd> List of SC to VLt table records. </dd>
<dt>scvlnt</dt>
<dd> List of SC to VLnt table records. </dd>
<dt>vlarb</dt>
<dd> List of VL arbitration table records. </dd>
<dt>pkey</dt>
<dd> List of PKey table records. </dd>
<dt>service</dt>
<dd> List of service records. </dd>
<dt>mcmember</dt>
<dd> List of multicast member records. </dd>
<dt>inform</dt>
<dd> List of inform info records. </dd>
<dt>linfdb</dt>
<dd> List of switch linear forwarding database (FDB) records. </dd>
<dt>mcfdb</dt>
<dd> List of switch multicast FDB records. </dd>
<dt>trace</dt>
<dd> List of trace records. </dd>
<dt>vfinfo</dt>
<dd> List of vFabrics. </dd>
<dt>vfinfocsv</dt>
<dd> List of vFabrics in CSV format. </dd>
<dt>vfinfocsv2</dt>
<dd> List of vFabrics in CSV format with enums. </dd>
<dt>fabricinfo</dt>
<dd> Summary of fabric devices. </dd>
<dt>quarantine</dt>
<dd> List of quarantined nodes. </dd>
<dt>conginfo</dt>
<dd> List of Congestion Info Records. </dd>
<dt>swcongset</dt>
<dd> List of Switch Congestion Settings. </dd>
<dt>swportcong</dt>
<dd> List of Switch Port Congestion Settings.</dd>
<dt>hficongset</dt>
<dd> List of HFI Congestion Settings. </dd>
<dt>hficongcon</dt>
<dd> List of HFI Congestion Control Settings. </dd>
<dt>bfrctrl</dt>
<dd> List of buffer control tables. </dd>
<dt>cableinfo</dt>
<dd> List of Cable Info records. </dd>
<dt>portgroup</dt>
<dd> List of AR Port Group records. </dd>
<dt>portgroupfdb</dt>
<dd> List of AR Port Group FWD records. </dd>
</dl>
<p> The vfinfocsv and vfinfocsv2 output formats are designed to make it easier to script vfinfo queries. One line is output per vFabric of the form: </p>
<p> name:index:pkey:sl:mtu:rate:optionflag </p>
<p> The only difference between these two formats is how the MTU and rate are output. vfinfocsv outputs MTU and rate in human/text readable format. vfinfocsv2 outputs MTU and rate as enumerations defined for the SMA protocol. The opagetvf command is based on this capability of opasaquery. For more information, see <i>opagetvf</i></p>
<h2>Example</h2>
<p> opasaquery -o desc -t fi<br />
 opasaquery -o portinfo -l 2<br />
 opasaquery -o sminfo<br />
 opasaquery -o pkey</p>
<h2>Input Options vs. Output Permitted</h2>
<p> The following list shows the input (assorted query by options) and outputs (-o) that are permitted.</p>
<dl>
<dt>None</dt>
<dd>
</dd><dl>
<dl>
<dt>
</dt><dd>
<p> -o output permitted systemguid, nodeguid, portguid, lid, desc, path, node, portinfo, sminfo, swinfo, link, vlarb, pkey, service, mcmember, inform, linfdb, mcfdb, vfinfo, vfinfocsv, vfinfocsv2, scsc, slsc, scvlt, scnlmt, linfdb, classportinfo, fabricinfo, quarantine, conginfo, swcongset, swportcong, hficongset, hficongcon, bfrctl, cableinfo, portgroup, portgroupfdb </p>
</dd></dl>
</dl>
<dl>
<dl>
<dt>
</dt><dd>
<p> -o output not permitted trace </p>
</dd></dl>
</dl>
<dt>-t <i>node_type</i></dt>
<dd>
</dd><dl>
<dl>
<dt>
</dt><dd>
<p> -o output permitted systemguid, nodeguid, portguid, lid, desc, node </p>
</dd></dl>
</dl>
<dl>
<dl>
<dt>
</dt><dd>
<p> -o output not permitted portinfo, sminfo, swinfo, vlarb, pkey, service, mcmember, inform, linfdb, mcfdb, trace, vfinfo, vfinfocsv, vfinfocsv2 </p>
</dd></dl>
</dl>
<dt>-l <i>lid</i></dt>
<dd>
</dd><dl>
<dl>
<dt>
</dt><dd>
<p> -o output permitted systemguid, nodeguid, portguid, lid, desc, path, node, portinfo, swinfo, slvl, vlarb, pkey, service, mcmember, linfdb, mcfdb </p>
</dd></dl>
</dl>
<dl>
<dl>
<dt>
</dt><dd>
<p> -o output not permitted sminfo, link, inform, trace, vfinfo, vfinfocsv, vfinfocsv2 </p>
</dd></dl>
</dl>
<dt>-k <i>pkey</i></dt>
<dd>
</dd><dl>
<dl>
<dt>
</dt><dd>
<p> -o output permitted mcmember, path, vfinfo, vfinfocsv, vfinfocsv2 </p>
</dd></dl>
</dl>
<dl>
<dl>
<dt>
</dt><dd>
<p> -o output not permitted systemimageguid, nodeguid, portguid, lid, desc, node, portinfo, sminfo, swinfo, link, vlarb, pkey, service, mcmember, inform, linfdb, mcfdb </p>
</dd></dl>
</dl>
<dt>-i</dt>
<dd> <i>vfindex</i> </dd>
<dl>
<dl>
<dt>
</dt><dd>
<p> -o output permitted vfinfo, vfinfocsv, vfinfocsv2 </p>
</dd></dl>
</dl>
<dl>
<dl>
<dt>
</dt><dd>
<p> -o output not permitted systemimageguid, nodeguid, portguid, lid, desc, node, portinfo, sminfo, swinfo, link, vlarb, pkey, service, mcmember, inform, linfdb, mcfdb </p>
</dd></dl>
</dl>
<dt>-s <i>system_image_guid</i></dt>
<dd>
</dd><dl>
<dl>
<dt>
</dt><dd>
<p> -o output permitted systemguid, nodeguid, portguid, lid, desc, node </p>
</dd></dl>
</dl>
<dl>
<dl>
<dt>
</dt><dd>
<p> -o output not permitted portinfo, sminfo, swinfo, link, vlarb, pkey, service, mcmember, inform, linfdb, mcfdb, trace, vfinfo, vfinfocsv, vfinfocsv2 </p>
</dd></dl>
</dl>
<dt>-n <i>node_guid</i></dt>
<dd>
</dd><dl>
<dl>
<dt>
</dt><dd>
<p> -o output permitted systemguid, nodeguid, portguid, lid, desc, node </p>
</dd></dl>
</dl>
<dl>
<dl>
<dt>
</dt><dd>
<p> -o output not permitted portinfo, sminfo, swinfo, link, vlarb, pkey, service, mcmember, inform, linfdb, mcfdb, trace, vfinfo, vfinfocsv, vfinfocsv2 </p>
</dd></dl>
</dl>
<dt>-g <i>port_guid</i></dt>
<dd>
</dd><dl>
<dl>
<dt>
</dt><dd>
<p> -o output permitted systemguid, nodeguid, portguid, lid, desc, path, node, service, mcmember, inform, trace </p>
</dd></dl>
</dl>
<dl>
<dl>
<dt>
</dt><dd>
<p> -o output not permitted portinfo, sminfo, swinfo, link, vlarb, pkey, linfdb, mcfdb, vfinfo, vfinfocsv, vfinfocsv2 </p>
</dd></dl>
</dl>
<dt>-u <i>port_gid</i></dt>
<dd>
</dd><dl>
<dl>
<dt>
</dt><dd>
<p> -o output permitted path, service, mcmember, inform, trace </p>
</dd></dl>
</dl>
<dl>
<dl>
<dt>
</dt><dd>
<p> -o output not permitted systemguid, nodeguid, portguid, lid, desc, node, portinfo, sminfo, swinfo, link, vlarb, pkey, linfdb, mcfdb, vfinfo, vfinfocsv, vfinfocsv2 </p>
</dd></dl>
</dl>
<dt>-m <i>multicast_gid</i></dt>
<dd>
</dd><dl>
<dl>
<dt>
</dt><dd>
<p> -o output permitted mcmember, vfinfo, vfinfocsv, vfinfocsv2 </p>
</dd></dl>
</dl>
<dl>
<dl>
<dt>
</dt><dd>
<p> -o output not permitted systemguid, nodeguid, portguid, lid, desc, path, node, portinfo, sminfo, swinfo, link, vlarb, pkey, service, inform, linfdb, mcfdb, trace </p>
</dd></dl>
</dl>
<dt>-d <i>name</i></dt>
<dd>
</dd><dl>
<dl>
<dt>
</dt><dd>
<p> -o output permitted systemguid, nodeguid, portguid, lid, desc, node </p>
</dd></dl>
</dl>
<dl>
<dl>
<dt>
</dt><dd>
<p> -o output not permitted trace </p>
</dd></dl>
</dl>
<dt>-P <i>port_guid_pair</i></dt>
<dd>
</dd><dl>
<dl>
<dt>
</dt><dd>
<p> -o output permitted path, trace </p>
</dd></dl>
</dl>
<dl>
<dl>
<dt>
</dt><dd>
<p> -o output not permitted systemguid, nodeguid, portguid, lid, desc, node, portinfo, sminfo, swinfo, link, vlarb, pkey, service, mcmember, inform, linfdb, mcfdb </p>
</dd></dl>
</dl>
<dt>-S <i>serviceId</i></dt>
<dd>
</dd><dl>
<dl>
<dt>
</dt><dd>
<p> -o output permitted path, vfinfo, vfinfocsv, vfinfocsv2 </p>
</dd></dl>
</dl>
<dl>
<dl>
<dt>
</dt><dd>
<p> -o output not permitted systemimageguid, nodeguid, portguid, lid, desc, node, portinfo, sminfo, swinfo, link, vlarb, pkey, service, mcmember, inform, linfdb, mcfdb </p>
</dd></dl>
</dl>
<dt>-L <i>SL</i></dt>
<dd>
</dd><dl>
<dl>
<dt>
</dt><dd>
<p> -o output permitted path, vfinfo, vfinfocsv, vfinfocsv2 </p>
</dd></dl>
</dl>
<dl>
<dl>
<dt>
</dt><dd>
<p> -o output not permitted systemimageguid, nodeguid, portguid, lid, desc, node, portinfo, sminfo, swinfo, link, vlarb, pkey, service, mcmember, inform, linfdb, mcfdb </p>
</dd></dl>
</dl>
<dt>-G <i>gid_pair</i></dt>
<dd>
</dd><dl>
<dl>
<dt>
</dt><dd>
<p> -o output permitted path, trace </p>
</dd></dl>
</dl>
<dl>
<dl>
<dt>
</dt><dd>
<p> -o output not permitted systemguid, nodeguid, portguid, lid, desc, node, portinfo, sminfo, swinfo, link, vlarb, pkey, service, mcmember, inform, linfdb, mcfdb </p>
</dd></dl>
</dl>
<dt>-a <i>port_guid_list</i></dt>
<dd>
</dd><dl>
<dl>
<dt>
</dt><dd>
<p> -o output permitted path </p>
</dd></dl>
</dl>
<dl>
<dl>
<dt>
</dt><dd>
<p> -o output not permitted systemguid, nodeguid, portguid, lid, desc, node, portinfo, sminfo, swinfo, link, vlarb, pkey, service, mcmember, inform, linfdb, mcfdb, trace </p>
</dd></dl>
</dl>
<dt>-A <i>gid_list</i></dt>
<dd>
</dd><dl>
<dl>
<dt>
</dt><dd>
<p> -o output permitted path </p>
</dd></dl>
</dl>
<dl>
<dl>
<dt>
</dt><dd>
<p> -o output not permitted systemguid, nodeguid, portguid, lid, desc, node, portinfo, sminfo, swinfo, link, vlarb, pkey, service, mcmember, inform, linfdb, mcfdb, trace </p>
</dd></dl>
</dl>
</dl>
<h2>Index</h2>
