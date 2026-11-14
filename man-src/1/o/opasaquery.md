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
<dt>&#8211;help</p>
<dd> Produces full help text. </p>
<dt>-v/&#8211;verbose</p>
<dd> Returns verbose output. A second invocation activates openib debugging, a third invocation activates libibumad debugging. </p>
<dt>-I/&#8211;IB</p>
<dd> Issues query in legacy InfiniBand* format. </p>
<dt>-h/&#8211;hfi <i>hfi</i></p>
<dd> HFI, numbered 1..n. Using 0 specifies that the -p <i>port</i> is a system-wide port number. Default is 0. </p>
<dt>-p/&#8211;port <i>port</i></p>
<dd> Port, numbered 1..n. If 0, then <i>port</i> is a first active. Default is first active. </p>
<dt>-o/&#8211;output <i>type</i></p>
<dd> Output type for query (default is node). See <i>Output Types</i> for details. </p>
<dt>-l/&#8211;lid <i>lid</i></p>
<dd> Query a specific LID. </p>
<dt>-t/&#8211;type <i>node_type</i></p>
<dd> Query by node type. See <i>Node Types</i> for details. </p>
<dt>-s/&#8211;sysguid <i>system_image_guid</i></p>
<dd> Query by system image GUID. </p>
<dt>-n/&#8211;nodeguid <i>node_guid</i></p>
<dd> Query by node GUID. </p>
<dt>-g/&#8211;portguid <i>port_guid</i></p>
<dd> Query by port GUID. </p>
<dt>-k/&#8211;pkey <i>pkey</i></p>
<dd> Query a specific PKey. </p>
<dt>-i/&#8211;vfindex <i>vfIndex</i></p>
<dd> Query a specific vfindex. </p>
<dt>-S/&#8211;serviceId <i>serviceId</i></p>
<dd> Query a specific service ID. </p>
<dt>-L/&#8211;SL <i>SL</i></p>
<dd> Query by service level. </p>
<dt>-u/&#8211;portgid <i>port_gid</i></p>
<dd> Query by port GID. See <i>GIDs</i> for details. </p>
<dt>-m/&#8211;mcgid <i>multicast_gid</i></p>
<dd> Query by multicast GID. See <i>GIDs</i> for details. </p>
<dt>-d/&#8211;desc <i>node_description</i></p>
<dd> Query by node name/description. </p>
<dt>-P/&#8211;guidpair <i>guid guid</i></p>
<dd> Query by a pair of port GUIDs. </p>
<dt>-G/&#8211;gidpair <i>gid gid</i></p>
<dd> Query by a pair of GIDs. See <i>GIDs</i> for details. </p>
<dt>-a/&#8211;guidlist <i>sguid &#8230;;dguid &#8230;</i></p>
<dd> Query by a list of port GUIDs. </p>
<dt>-A/&#8211;gidlist <i>sgid &#8230;;dgid &#8230;</i></p>
<dd> Query by a list of GIDs. See <i>GIDs</i> for details. </p>
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
<dd> Port <i>y</i>#8217#160;within system (no matter which ports are active). </p>
<dt>-h <i>x</i>#8217#160;-p <i>y</i></p>
<dd> HFI <i>x</i>, port <i>y</i>. </p>
</dl>
<h2>Node Types</h2>
<dl>
<dt>fi</p>
<dd> Fabric Interface </p>
<dt>sw</p>
<dd> Switch </p>
</dl>
<h2>GIDs</h2>
<p> Specify a 64-bit subnet and 64-bit interface ID in the form: </p>
<p>&nbsp;<wbr><i>subnet</i>:&nbsp;<wbr><i>interface</i>&nbsp;<wbr> </p>
<p> <code>NOTE:</code> In the following example, the GID corresponds to a PortGID. In this case, the interface ID coincides with the lower 64-bits of the GUID of the card. The interface ID will be different if the GID is a MGID (that is, multicast GID). See opafm.xml for MGID examples. </p>
<p> 0xfe80000000000000:0x00117500a0000380 </p>
<h2>Output Types</h2>
<p> Default is node.</p>
<dl>
<dt>classportinfo</p>
<dd> classportinfo of the SA. </p>
<dt>systemguid</p>
<dd> List of system image GUIDs. </p>
<dt>nodeguid</p>
<dd> List of node GUIDs. </p>
<dt>portguid</p>
<dd> List of port GUIDs. </p>
<dt>lid</p>
<dd> List of LIDs. </p>
<dt>desc</p>
<dd> List of node descriptions/names. </p>
<dt>path</p>
<dd> List of path records. </p>
<dt>node</p>
<dd> List of node records. </p>
<dt>portinfo</p>
<dd> List of port info records. </p>
<dt>sminfo</p>
<dd> List of SM info records. </p>
<dt>swinfo</p>
<dd> List of switch info records. </p>
<dt>link</p>
<dd> List of link records. </p>
<dt>scsc</p>
<dd> List of SC to SC mapping table records. </p>
<dt>slsc</p>
<dd> List of SL to SC mapping table records. </p>
<dt>scsl</p>
<dd> List of SC to SL mapping table records. </p>
<dt>scvlt</p>
<dd> List of SC to VLt table records. </p>
<dt>scvlnt</p>
<dd> List of SC to VLnt table records. </p>
<dt>vlarb</p>
<dd> List of VL arbitration table records. </p>
<dt>pkey</p>
<dd> List of PKey table records. </p>
<dt>service</p>
<dd> List of service records. </p>
<dt>mcmember</p>
<dd> List of multicast member records. </p>
<dt>inform</p>
<dd> List of inform info records. </p>
<dt>linfdb</p>
<dd> List of switch linear forwarding database (FDB) records. </p>
<dt>mcfdb</p>
<dd> List of switch multicast FDB records. </p>
<dt>trace</p>
<dd> List of trace records. </p>
<dt>vfinfo</p>
<dd> List of vFabrics. </p>
<dt>vfinfocsv</p>
<dd> List of vFabrics in CSV format. </p>
<dt>vfinfocsv2</p>
<dd> List of vFabrics in CSV format with enums. </p>
<dt>fabricinfo</p>
<dd> Summary of fabric devices. </p>
<dt>quarantine</p>
<dd> List of quarantined nodes. </p>
<dt>conginfo</p>
<dd> List of Congestion Info Records. </p>
<dt>swcongset</p>
<dd> List of Switch Congestion Settings. </p>
<dt>swportcong</p>
<dd> List of Switch Port Congestion Settings.</p>
<dt>hficongset</p>
<dd> List of HFI Congestion Settings. </p>
<dt>hficongcon</p>
<dd> List of HFI Congestion Control Settings. </p>
<dt>bfrctrl</p>
<dd> List of buffer control tables. </p>
<dt>cableinfo</p>
<dd> List of Cable Info records. </p>
<dt>portgroup</p>
<dd> List of AR Port Group records. </p>
<dt>portgroupfdb</p>
<dd> List of AR Port Group FWD records. </p>
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
<dt>None</p>
<dd>
<dl>
<dt>
<dd>
<dl>
<dt>
<dd>
<p> -o output permitted systemguid, nodeguid, portguid, lid, desc, path, node, portinfo, sminfo, swinfo, link, vlarb, pkey, service, mcmember, inform, linfdb, mcfdb, vfinfo, vfinfocsv, vfinfocsv2, scsc, slsc, scvlt, scnlmt, linfdb, classportinfo, fabricinfo, quarantine, conginfo, swcongset, swportcong, hficongset, hficongcon, bfrctl, cableinfo, portgroup, portgroupfdb </p>
</dl>
</dl>
<dl>
<dt>
<dd>
<dl>
<dt>
<dd>
<p> -o output not permitted trace </p>
</dl>
</dl>
<dt>-t <i>node_type</i></p>
<dd>
<dl>
<dt>
<dd>
<dl>
<dt>
<dd>
<p> -o output permitted systemguid, nodeguid, portguid, lid, desc, node </p>
</dl>
</dl>
<dl>
<dt>
<dd>
<dl>
<dt>
<dd>
<p> -o output not permitted portinfo, sminfo, swinfo, vlarb, pkey, service, mcmember, inform, linfdb, mcfdb, trace, vfinfo, vfinfocsv, vfinfocsv2 </p>
</dl>
</dl>
<dt>-l <i>lid</i></p>
<dd>
<dl>
<dt>
<dd>
<dl>
<dt>
<dd>
<p> -o output permitted systemguid, nodeguid, portguid, lid, desc, path, node, portinfo, swinfo, slvl, vlarb, pkey, service, mcmember, linfdb, mcfdb </p>
</dl>
</dl>
<dl>
<dt>
<dd>
<dl>
<dt>
<dd>
<p> -o output not permitted sminfo, link, inform, trace, vfinfo, vfinfocsv, vfinfocsv2 </p>
</dl>
</dl>
<dt>-k <i>pkey</i></p>
<dd>
<dl>
<dt>
<dd>
<dl>
<dt>
<dd>
<p> -o output permitted mcmember, path, vfinfo, vfinfocsv, vfinfocsv2 </p>
</dl>
</dl>
<dl>
<dt>
<dd>
<dl>
<dt>
<dd>
<p> -o output not permitted systemimageguid, nodeguid, portguid, lid, desc, node, portinfo, sminfo, swinfo, link, vlarb, pkey, service, mcmember, inform, linfdb, mcfdb </p>
</dl>
</dl>
<dt>-i</p>
<dd> <i>vfindex</i> </p>
<dl>
<dt>
<dd>
<dl>
<dt>
<dd>
<p> -o output permitted vfinfo, vfinfocsv, vfinfocsv2 </p>
</dl>
</dl>
<dl>
<dt>
<dd>
<dl>
<dt>
<dd>
<p> -o output not permitted systemimageguid, nodeguid, portguid, lid, desc, node, portinfo, sminfo, swinfo, link, vlarb, pkey, service, mcmember, inform, linfdb, mcfdb </p>
</dl>
</dl>
<dt>-s <i>system_image_guid</i></p>
<dd>
<dl>
<dt>
<dd>
<dl>
<dt>
<dd>
<p> -o output permitted systemguid, nodeguid, portguid, lid, desc, node </p>
</dl>
</dl>
<dl>
<dt>
<dd>
<dl>
<dt>
<dd>
<p> -o output not permitted portinfo, sminfo, swinfo, link, vlarb, pkey, service, mcmember, inform, linfdb, mcfdb, trace, vfinfo, vfinfocsv, vfinfocsv2 </p>
</dl>
</dl>
<dt>-n <i>node_guid</i></p>
<dd>
<dl>
<dt>
<dd>
<dl>
<dt>
<dd>
<p> -o output permitted systemguid, nodeguid, portguid, lid, desc, node </p>
</dl>
</dl>
<dl>
<dt>
<dd>
<dl>
<dt>
<dd>
<p> -o output not permitted portinfo, sminfo, swinfo, link, vlarb, pkey, service, mcmember, inform, linfdb, mcfdb, trace, vfinfo, vfinfocsv, vfinfocsv2 </p>
</dl>
</dl>
<dt>-g <i>port_guid</i></p>
<dd>
<dl>
<dt>
<dd>
<dl>
<dt>
<dd>
<p> -o output permitted systemguid, nodeguid, portguid, lid, desc, path, node, service, mcmember, inform, trace </p>
</dl>
</dl>
<dl>
<dt>
<dd>
<dl>
<dt>
<dd>
<p> -o output not permitted portinfo, sminfo, swinfo, link, vlarb, pkey, linfdb, mcfdb, vfinfo, vfinfocsv, vfinfocsv2 </p>
</dl>
</dl>
<dt>-u <i>port_gid</i></p>
<dd>
<dl>
<dt>
<dd>
<dl>
<dt>
<dd>
<p> -o output permitted path, service, mcmember, inform, trace </p>
</dl>
</dl>
<dl>
<dt>
<dd>
<dl>
<dt>
<dd>
<p> -o output not permitted systemguid, nodeguid, portguid, lid, desc, node, portinfo, sminfo, swinfo, link, vlarb, pkey, linfdb, mcfdb, vfinfo, vfinfocsv, vfinfocsv2 </p>
</dl>
</dl>
<dt>-m <i>multicast_gid</i></p>
<dd>
<dl>
<dt>
<dd>
<dl>
<dt>
<dd>
<p> -o output permitted mcmember, vfinfo, vfinfocsv, vfinfocsv2 </p>
</dl>
</dl>
<dl>
<dt>
<dd>
<dl>
<dt>
<dd>
<p> -o output not permitted systemguid, nodeguid, portguid, lid, desc, path, node, portinfo, sminfo, swinfo, link, vlarb, pkey, service, inform, linfdb, mcfdb, trace </p>
</dl>
</dl>
<dt>-d <i>name</i></p>
<dd>
<dl>
<dt>
<dd>
<dl>
<dt>
<dd>
<p> -o output permitted systemguid, nodeguid, portguid, lid, desc, node </p>
</dl>
</dl>
<dl>
<dt>
<dd>
<dl>
<dt>
<dd>
<p> -o output not permitted trace </p>
</dl>
</dl>
<dt>-P <i>port_guid_pair</i></p>
<dd>
<dl>
<dt>
<dd>
<dl>
<dt>
<dd>
<p> -o output permitted path, trace </p>
</dl>
</dl>
<dl>
<dt>
<dd>
<dl>
<dt>
<dd>
<p> -o output not permitted systemguid, nodeguid, portguid, lid, desc, node, portinfo, sminfo, swinfo, link, vlarb, pkey, service, mcmember, inform, linfdb, mcfdb </p>
</dl>
</dl>
<dt>-S <i>serviceId</i></p>
<dd>
<dl>
<dt>
<dd>
<dl>
<dt>
<dd>
<p> -o output permitted path, vfinfo, vfinfocsv, vfinfocsv2 </p>
</dl>
</dl>
<dl>
<dt>
<dd>
<dl>
<dt>
<dd>
<p> -o output not permitted systemimageguid, nodeguid, portguid, lid, desc, node, portinfo, sminfo, swinfo, link, vlarb, pkey, service, mcmember, inform, linfdb, mcfdb </p>
</dl>
</dl>
<dt>-L <i>SL</i></p>
<dd>
<dl>
<dt>
<dd>
<dl>
<dt>
<dd>
<p> -o output permitted path, vfinfo, vfinfocsv, vfinfocsv2 </p>
</dl>
</dl>
<dl>
<dt>
<dd>
<dl>
<dt>
<dd>
<p> -o output not permitted systemimageguid, nodeguid, portguid, lid, desc, node, portinfo, sminfo, swinfo, link, vlarb, pkey, service, mcmember, inform, linfdb, mcfdb </p>
</dl>
</dl>
<dt>-G <i>gid_pair</i></p>
<dd>
<dl>
<dt>
<dd>
<dl>
<dt>
<dd>
<p> -o output permitted path, trace </p>
</dl>
</dl>
<dl>
<dt>
<dd>
<dl>
<dt>
<dd>
<p> -o output not permitted systemguid, nodeguid, portguid, lid, desc, node, portinfo, sminfo, swinfo, link, vlarb, pkey, service, mcmember, inform, linfdb, mcfdb </p>
</dl>
</dl>
<dt>-a <i>port_guid_list</i></p>
<dd>
<dl>
<dt>
<dd>
<dl>
<dt>
<dd>
<p> -o output permitted path </p>
</dl>
</dl>
<dl>
<dt>
<dd>
<dl>
<dt>
<dd>
<p> -o output not permitted systemguid, nodeguid, portguid, lid, desc, node, portinfo, sminfo, swinfo, link, vlarb, pkey, service, mcmember, inform, linfdb, mcfdb, trace </p>
</dl>
</dl>
<dt>-A <i>gid_list</i></p>
<dd>
<dl>
<dt>
<dd>
<dl>
<dt>
<dd>
<p> -o output permitted path </p>
</dl>
</dl>
<dl>
<dt>
<dd>
<dl>
<dt>
<dd>
<p> -o output not permitted systemguid, nodeguid, portguid, lid, desc, node, portinfo, sminfo, swinfo, link, vlarb, pkey, service, mcmember, inform, linfdb, mcfdb, trace </p>
</dl>
</dl>
</dl>
<h2>Index</h2>
