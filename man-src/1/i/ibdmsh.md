---
title: "ibdmsh(1)"
name: "ibdmsh"
section: "1"
letter: "i"
url: "/docs/linux/man/1-ibdmsh/"
description: "ibdmsh IB DATA MODEL – Extentended TCL shell"
---

<h2>NAME</h2>
<p> <code>ibdmsh</code> IB DATA MODEL &#8211; Extentended TCL shell</p>
<h2>DESCRIPTION</h2>
<p> <code>ibdmsh</code> is a <font SIZE="-1">TCL</font> shell extended with interface for the <font SIZE="-1">IB</font> data model. To use this shell you will write <font SIZE="-1">TCL</font> code that directly access the <font SIZE="-1">IB</font> data model objects and functions. </p>
<p> The following sub sections provide detailed definition for those objects and <font SIZE="-1">API</font>.</p>
<h2>IBDM Constants</h2>
<p> <code>Node Types</code> </p>
<p> The following constants are used by the node object type field </p>
<dl>
<dt>
<dd> [ Constant : int ] <tt>$IB_UNKNOWN_NODE_TYPE</tt> = <font SIZE="-1">IB_UNKNOWN_NODE_TYPE</font> </p>
<p> [ Constant : int ] <tt>$IB_SW_NODE</tt> = <font SIZE="-1">IB_SW_NODE</font> </p>
<p> [ Constant : int ] <tt>$IB_CA_NODE</tt> = <font SIZE="-1">IB_CA_NODE</font></dl>
<p> <code>Log Verbosity Flags</code> </p>
<p> The following constants are used as argument bits for the global variable <tt>$FabricUtilsVerboseLevel</tt> </p>
<dl>
<dt>
<dd> [ Constant : int ] <tt>$FABU_LOG_NONE</tt> = 0x0 </p>
<p> [ Constant : int ] <tt>$FABU_LOG_ERROR</tt> = 0x1 </p>
<p> [ Constant : int ] <tt>$FABU_LOG_INFO</tt> = 0x2 </p>
<p> [ Constant : int ] <tt>$FABU_LOG_VERBOSE</tt> = 0x4</dl>
<h2>IBDM Globals</h2>
<p> Log level: set to FABU_LOG* values </p>
<dl>
<dt>
<dd> [ Global : int ] <tt>$FabricUtilsVerboseLevel</tt></dl>
<h2>IBDM Objects</h2>
<p> This section decribes the various object types exposed by <font SIZE="-1">IBDM</font>. </p>
<p> <font SIZE="-1">IBDM</font> exposes some of its internal objects. The objects identifiers returned by the various function calls are formatted according to the following rules: </p>
<p> Fabric: fabric:&lt;idx&gt; </p>
<p> System: system:&lt;fab idx&gt;:&lt;sys name&gt; </p>
<p> SysPort: sysport:&lt;fab idx&gt;:&lt;sys name&gt;:&lt;port name&gt; </p>
<p> Node: node:&lt;fab idx&gt;:&lt;node name&gt; </p>
<p> Port: port:&lt;fab idx&gt;:&lt;node name&gt;/&lt;port num&gt; </p>
<p> <font SIZE="-1">IBDM</font> Objects are standard Swig-Tcl objects. As such they have two flavors for their usage: Variables, Objects. </p>
<p> <code>Variables/Pointers:</code><br />
For each object attribute a&nbsp;<wbr>&#8220;get&#8221;&nbsp;<wbr>and&nbsp;<wbr>&#8220;set&#8221;&nbsp;<wbr>methods are provided.<br />
The format of the methods is:&nbsp;<wbr>&lt;class&gt;_&lt;attribute&gt;_&lt;get|set&gt;.<br />
The&nbsp;<wbr>&#8220;set&#8221;&nbsp;<wbr>method is only available for read/write attributes. </p>
<pre><code>
Example : set nodes[ibdm_get_nodes] set node[lindex $nodes 0] IBNode_numPorts_get $node
</code></pre>
<p> <code>Objects:</code><br />
Given an object pointer one can convert it to a Tcl&nbsp;<wbr>&#8220;Object&#8221;<br />
using the following command:<br />
&lt;class&gt;&nbsp;<wbr>&lt;obj_name&gt;&nbsp;<wbr>-this&nbsp;<wbr>&lt;obj pointer&gt; </p>
<pre>
   Once declared the &lt;obj-name&gt; can be used in conjunction to
   with the standard &quot;configure&quot; and &quot;cget&quot; commands.
</pre>
<pre>
   Example (following the previous one):
   IBFabric VaTech -this $fabric
   VaTech cget -NodeByName
</pre>
<pre>
   To delete an object symbol (and enable its mapping to another
   pointer) use:
   rename &lt;obj name&gt; &quot;&quot;
   for example:
   rename VaTech &quot;&quot;
</pre>
<p> <code>class IBPort</code> </p>
<p> The following are the different fields and methods of the <font SIZE="-1">IB</font> Port class which describes an <font SIZE="-1">IB</font> device (chip) physical port.</p>
<dl>
<dt>[ Member data: returns IBPort * ] -p_remotePort</p>
<dd> Port connected on the other side of link</p>
<dt>[ Member data: returns IBSysPort * ] -p_sysPort</p>
<dd> The system port (if any) connected to</p>
<dt>[ Member data: returns IBNode * ] -p_node</p>
<dd> The node the port is part of.</p>
<dt>[ Member data: returns int ] -num</p>
<dd> Physical ports are identified by number.</p>
<dt>[ Member data: returns unsigned int ] -base_lid</p>
<dd> The base lid assigned to the port.</p>
<dt>[ Member data: returns IBLinkWidth * ] -width</p>
<dd> The link width of the port</p>
<dt>[ Member data: returns IBLinkSpeed * ] -speed</p>
<dd> The link speed of the port</p>
<dt>[ Member data: returns unsigned int ] -counter1</p>
<dd> A generic value to be used by various algorithms</p>
<dt>[ Constructor: returns IBPort * ] IBPort name p_nodePtr number</p>
<dd> IBPort constructor</p>
<dt>[ Member : returns new_uint64_t ] guid_get</p>
<dd> Obtain the guid of the port</p>
<dt>[ Member : returns void ] guid_set guid</p>
<dd> Modify the guid of the port</p>
<dt>[ Member : returns new_string ] getName</p>
<dd> Get the port name: A device port connected to system port (front pannel) returns the front pannel port name.</p>
<dt>[ Member : returns void ] connect p_otherPort ?width? ?speed?</p>
<dd> Connect the port to another node port with optional width and speed parameters</p>
<dt>[ Member : returns int ] disconnect</p>
<dd> Disconnect the port. Return 0 if successful
</dl>
<p> <code>class IBNode</code> </p>
<p> The <font SIZE="-1">IB</font> Node class represents a single <font SIZE="-1">IB</font> Device (chip)</p>
<dl>
<dt>[ Member data: returns string * ] -name</p>
<dd> Name of the node (instance name of the chip)</p>
<dt>[ Member data: returns IBNodeType ] -type</p>
<dd> Either a <tt>$IB_SW_NODE</tt> or <tt>$IB_CA_NODE</tt></p>
<dt>[ Member data: returns uint16_t * ] -devId</p>
<dd> The device <font SIZE="-1">ID</font> of the node</p>
<dt>[ Member data: returns uint16_t * ] -revId</p>
<dd> The device revision Id.</p>
<dt>[ Member data: returns uint16_t * ] -vendId</p>
<dd> The device Vendor <font SIZE="-1">ID</font>.</p>
<dt>[ Member data: returns string * ] -attributes</p>
<dd> Comma-sep string of arbitrary attributes k=v</p>
<dt>[ Member data: returns uint8_t ] -rank</p>
<dd> The rank of the node (0 is a root)</p>
<dt>[ Member data: returns IBSystem * ] -p_system</p>
<dd> What system we belong to</p>
<dt>[ Member data: returns IBFabric * ] -p_fabric</p>
<dd> What fabric we belong to.</p>
<dt>[ Member data: returns unsigned int ] -numPorts</p>
<dd> Number of physical ports</p>
<dt>[ Member data: returns vec_pport * ] -Ports</p>
<dd> Vector of all the ports</p>
<dt>[ Member data: returns vec_vec_byte * ] -MinHopsTable</p>
<dd> A table of the number of hops required to get from each port to each target <font SIZE="-1">LID</font></p>
<dt>[ Member data: returns vec_byte * ] -LFT</p>
<dd> The <font SIZE="-1">LFT</font> of this node (for switches only) which is a long vector of target ports &#8211; index is the <font SIZE="-1">LID</font></p>
<dt>[ Member : returns new_uint64_t ] guid_get</p>
<dd> Obtain the node <font SIZE="-1">GUID</font></p>
<dt>[ Member : returns void ] guid_set guid</p>
<dd> Set the node <font SIZE="-1">GUID</font></p>
<dt>[ Constructor: returns IBNode * ] IBNode name n p_fab p_sys t np</p>
<dd> Constractor</p>
<dt>[ Member : returns IBPort * ] makePort num</p>
<dd> Create a new port by its number (if required) return the port pointer</p>
<dt>[ Member : returns IBPort * ] getPort num</p>
<dd> Get a port by number num = 1..N:</p>
<dt>[ Member : returns void ] setHops p_port lid hops</p>
<dd> Set the min hop for the given port (* is all) lid pair</p>
<dt>[ Member : returns int ] getHops p_port lid</p>
<dd> Get the min number of hops defined for the given port or all</p>
<dt>[ Member : returns IBPort * ] getFirstMinHopPort lid</p>
<dd> Scan the node ports and find the first port with min hop to the lid</p>
<dt>[ Member : returns void ] setLFTPortForLid lid portNum</p>
<dd> Set the Linear Forwarding Table for the given <font SIZE="-1">LID</font></p>
<dt>[ Member : returns int ] getLFTPortForLid lid</p>
<dd> Get the <font SIZE="-1">LFT</font> for a given <font SIZE="-1">LID</font></p>
<dt>[ Member : returns void ] repHopTable</p>
<dd> Dump out the min hop table of the node
</dl>
<p> <code>class IBSysPort</code> </p>
<p> The IBSysPort class represents an <font SIZE="-1">IB</font> plug on the system front or back pannels</p>
<dl>
<dt>[ Member data: returns string * ] -name</p>
<dd> The front pannel name (silk) of the port</p>
<dt>[ Member data: returns IBSysPort * ] -p_remoteSysPort</p>
<dd> If connected the other side sys port</p>
<dt>[ Member data: returns IBSystem * ] -p_system</p>
<dd> System it benongs to</p>
<dt>[ Member data: returns IBPort * ] -p_nodePort</p>
<dd> The node port it connects to.</p>
<dt>[ Constructor: returns IBSysPort * ] IBSysPort name n p_sys</p>
<dd> Constructor</p>
<dt>[ Member : returns void ] connect p_otherSysPort ?width? ?speed?</p>
<dd> Connect two SysPorts</p>
<dt>[ Member : returns int ] disconnect</p>
<dd> Disconnect the SysPort (and ports). Return 0 if successful
</dl>
<p> <code>class IBSystem</code> </p>
<p> The IBSystem class represents an entire chassis</p>
<dl>
<dt>[ Member data: returns string * ] -name</p>
<dd> The &#8220;host&#8221; name of the system</p>
<dt>[ Member data: returns string * ] -type</p>
<dd> What is the type i.e. Cougar, Buffalo, <font SIZE="-1">MTS2400</font>, etc. A corresponding <font SIZE="-1">IBNL</font> file should exist &#8211; defining this system type</p>
<dt>[ Member data: returns IBFabric * ] -p_fabric</p>
<dd> Fabric the system belongs to</p>
<dt>[ Member data: returns map_str_pnode * ] -NodeByName</p>
<dd> Provide the node pointer by its name</p>
<dt>[ Member data: returns map_str_psysport * ] -PortByName</p>
<dd> A map provising pointer to the SysPort by name</p>
<dt>[ Constructor: returns IBSystem * ] IBSystem name n p_fab t</p>
<dd> Constractor</p>
<dt>[ Member : returns new_uint64_t ] guid_get</p>
<dd> Obtain the system image <font SIZE="-1">GUID</font></p>
<dt>[ Member : returns void ] guid_set guid</p>
<dd> Set the system image <font SIZE="-1">GUID</font></p>
<dt>[ Member : returns IBSysPort * ] makeSysPort pName</p>
<dd> Make sure we got the port defined (so define it if not)</p>
<dt>[ Member : returns IBPort * ] getSysPortNodePortByName sysPortName</p>
<dd> Get the node port for the given sys port by name</p>
<dt>[ Member : returns IBSysPort * ] getSysPort name</p>
<dd> Get a Sys Port by name
</dl>
<p> <code>class IBFabric</code> </p>
<p> Represents an entire <font SIZE="-1">IB</font> subnet made of systems</p>
<dl>
<dt>[ Member data: returns map_str_pnode * ] -NodeByName</p>
<dd> Provide a list of node name and pointer pairs</p>
<dt>[ Member data: returns map_str_psys * ] -SystemByName</p>
<dd> Provide a list of system name and pointer pairs</p>
<dt>[ Member data: returns vec_pport * ] -PortByLid</p>
<dd> Provides a list of system port name and pointer pairs</p>
<dt>[ Member data: returns map_guid_pnode * ] -NodeByGuid</p>
<dd> Provides a list of node guid and node pointer pairs</p>
<dt>[ Member data: returns map_guid_psys * ] -SystemByGuid</p>
<dd> Provides a list of system image guid and system pointer pairs</p>
<dt>[ Member data: returns map_guid_pport * ] -PortByGuid</p>
<dd> Provides a list of port guid and port pointer pairs</p>
<dt>[ Member data: returns unsigned int ] -minLid</p>
<dd> Track min lid used.</p>
<dt>[ Member data: returns unsigned int ] -maxLid</p>
<dd> Track max lid used.</p>
<dt>[ Member data: returns unsigned int ] -lmc</p>
<dd> <font SIZE="-1">LMC</font> value used</p>
<dt>[ Member : returns IBNode * ] makeNode n p_sys type numPorts</p>
<dd> Get the node by its name (create one of does not exist)</p>
<dt>[ Member : returns IBNode * ] getNode name</p>
<dd> Get the node by its name</p>
<dt>[ Member : returns list_pnode * ] getNodesByType type</p>
<dd> Return the list of node pointers matching the required type</p>
<dt>[ Member : returns IBSystem * ] makeGenericSystem name</p>
<dd> Create a new generic system &#8211; basically an empty container for nodes&#8230;</p>
<dt>[ Member : returns IBSystem * ] makeSystem name type</p>
<dd> Create a new system &#8211; the type must have a registed factory.</p>
<dt>[ Member : returns IBSystem * ] getSystem name</p>
<dd> Get system by name</p>
<dt>[ Member : returns IBSystem * ] getSystemByGuid guid</p>
<dd> get the system by its guid</p>
<dt>[ Member : returns IBNode * ] getNodeByGuid guid</p>
<dd> get the node by its guid</p>
<dt>[ Member : returns IBPort * ] getPortByGuid guid</p>
<dd> get the port by its guid</p>
<dt>[ Member : returns void ] addCable t1 n1 p1 t2 n2 p2 ?width? ?speed?</p>
<dd> Adds a cable given two sets of node type, node name and port number. Optionally use a given width and speed for the connection</p>
<dt>[ Member : returns int ] parseCables fn</p>
<dd> Parse the cables file and build the fabric</p>
<dt>[ Member : returns int ] parseTopology fn</p>
<dd> Parse Topology File and build the fabric</p>
<dt>[ Member : returns int ] addLink type1 numPorts1 sysGuid1 nodeGuid1 portGuid1 vend1 devId1 rev1 desc1 lid1 portNum1 type2 numPorts2 sysGuid2 nodeGuid2 portGuid2 vend2 devId2 rev2 desc2 lid2 portNum2 ?width? ?speed?</p>
<dd> Add a link into the fabric &#8211; this will create system and nodes as required.</p>
<dt>[ Member : returns int ] parseSubnetLinks fn</p>
<dd> Parse the OpenSM subnet.lst file and build the fabric from it.</p>
<dt>[ Member : returns int ] parseFdbFile fn</p>
<dd> Parse OpenSM <font SIZE="-1">FDB</font> dump file and fill in the switches <font SIZE="-1">LFT</font> tables</p>
<dt>[ Member : returns int ] parseMCFdbFile fn</p>
<dd> Parse an OpenSM MCFDBs file and set the <font SIZE="-1">MFT</font> table accordingly</p>
<dt>[ Member : returns int ] parsePSLFile fn</p>
<dd> Parse Path to <font SIZE="-1">SL</font> mapping file. Each line with: src_node_guid <font SIZE="-1">DLID</font> <font SIZE="-1">SL</font></dl>
<p> Used by credit loop check</p>
<dl>
<dt>[ Member : returns int ] parseSLVLFile fn</p>
<dd> Parse <font SIZE="-1">SLVL</font> tables file. Each line holds: sw_node_guid in_port out_port 0x(sl0)(sl1) 0x(sl2)(sl3)&#8230;</p>
<dt>[ Member : returns void ] setLidPort lid p_port</p>
<dd> Set a lid port</p>
<dt>[ Member : returns IBPort * ] getPortByLid lid</p>
<dd> Get a port by lid</p>
<dt>[ returns IBFabric * ] new_IBFabric</p>
<dd> Construct a new fabric</p>
<dt>[ returns void ] delete_IBFabric p_fabric</p>
<dd> Destruct a fabric</dl>
<h2>IBDM Functions</h2>
<p> This section provide the details about the functions <font SIZE="-1">IBDM</font> exposes. The order follows the expected order in a regular <font SIZE="-1">IBDM</font> flow. They all return 0 on succes. </p>
<p> <code>Subnet Utilities</code> </p>
<p> The file holds a set of utilities to be run on the subnet to mimic OpenSM initialization and analyze the results:</p>
<dl>
<dt>[ returns int ] ibdmAssignLids p_smNodePort ?lmc?</p>
<dd> Assign LIDs with an optional <font SIZE="-1">LMC</font> (multiple <font SIZE="-1">LID</font> per port)</p>
<dt>[ returns int ] ibdmCalcMinHopTables p_fabric</p>
<dd> Calculate and populate the MinHopTables required for running OpenSM style routing.</p>
<dt>[ returns int ] ibdmCalcUpDnMinHopTbls p_fabric rootNodesNameRex</p>
<dd> Calculate and populate the MinHopTables following Up/Down rule.</p>
<dt>[ returns int ] ibdmOsmRoute p_fabric</p>
<dd> Route the fabric with OpenSM style routing</p>
<dt>[ returns int ] ibdmEnhancedRoute p_fabric</p>
<dd> Route the fabric with OpenSM style routing enhanced with better support for <font SIZE="-1">LMC</font> &gt; 0</p>
<dt>[ returns int ] ibdmFatTreeRoute p_fabric rootNodes</p>
<dd> Route the fabric using algorithm that fits only full fat trees</p>
<dt>[ returns int ] ibdmFatTreeAnalysis p_fabric</p>
<dd> Analyze the fabric to see if it is a fat tree and route it if it is</p>
<dt>[ returns int ] ibdmVerifyCAtoCARoutes p_fabric</p>
<dd> Make sure all (H)CAs are connected to each other based on the <font SIZE="-1">LFT</font> settings</p>
<dt>[ returns int ] ibdmVerifyAllPaths p_fabric</p>
<dd> Make sure all Switches and (H)CAs are connected to each other based on the <font SIZE="-1">LFT</font> settings</p>
<dt>[ returns int ] ibdmAnalyzeLoops p_fabric</p>
<dd> A rigorous check for credit loops. This algorithm does a full and accurate check but its reporting of credit loop paths is hard to interpret. If you know the roots of the tree (or the tree is symmetrical) it is preferable to use the ibdmReportNonUpDownCa2CaPaths</p>
<dt>[ returns list_pnode ] ibdmFindSymmetricalTreeRoots p_fabric</p>
<dd> Analyze the tree topology and find the roots of the tree based on its symmetry</p>
<dt>[ returns list_pnode ] ibdmFindRootNodesByMinHop p_fabric</p>
<dd> Based on the MinHopTable find the roots of the tree. A 5% assymetry is allowed</p>
<dt>[ returns int ] ibdmRankFabricByRoots p_fabric rootNodes</p>
<dd> Given the list of root nodes (names) rank the nodes (root = 0)</p>
<dt>[ returns int ] ibdmReportNonUpDownCa2CaPaths p_fabric rootNodes</p>
<dd> Analyze the routes to make sure Up/Down rule is maintained</p>
<dt>[ returns int ] ibdmCheckMulticastGroups p_fabric</p>
<dd> Verify connectivity of multicast routing</p>
<dt>[ returns int ] ibdmCheckFabricMCGrpsForCreditLoopPotential p_fabric rootNodes</p>
<dd> Analyze multicast routing to make sure it obeys Up/Down rule</p>
<dt>[ returns int ] ibdmLinkCoverageAnalysis p_fabric rootNodes</p>
<dd> Prepare a schedule for transmission from a set of sources to destinations such that in each stage there are no links that are over subscribed and after all stages all the links of the fabric were excersized
</dl>
<p> <code>Tracing Utilities</code> </p>
<p> These functions allows tracing paths reporting back the visited nodes</p>
<dl>
<dt>[ returns int ] ibdmTraceDRPathRoute p_smNodePort drPathPortNums</p>
<dd> Trace a directed route path from the given port</p>
<dt>[ returns int ] ibdmTraceRouteByMinHops p_fabric slid dlid</p>
<dd> Trace a path along the MinHop from the source to destination LIDs</p>
<dt>[ returns int ] ibdmTraceRouteByLFT p_fabric slid dlid hops p_nodesList</p>
<dd> Trace a path following the <font SIZE="-1">LFT</font> updating the hops and node list variables
</dl>
<p> <code>Topology Matching Utilities</code> </p>
<p> The following utilities matches two fabrics providing both missmatch messages and a unified fabric</p>
<dl>
<dt>[ returns int ] ibdmMatchFabrics p_spec_fabric p_discovered_fabric anchorNodeName anchorPortNum anchorPortGuid</p>
<dd> Match a topology based fabric with a discovered one starting at the enchor port</p>
<dt>[ returns int ] ibdmBuildMergedFabric p_spec_fabric p_discovered_fabric p_merged_fabric</p>
<dd> After matching using ibdmMatchFabrics populate the &#8220;merged fabric&#8221; with information merged for the matched nodes
</dl>
<p> <code>Congestion Analysis Utilities</code> </p>
<p> Provide ability to track and report link oversubscription</p>
<dl>
<dt>[ returns int ] ibdmCongInit p_fabric</p>
<dd> Initialize the tracking system</p>
<dt>[ returns int ] ibdmCongCleanup p_fabric</p>
<dd> Cleanup the counters and deallocate</p>
<dt>[ returns int ] ibdmCongClear p_fabric</p>
<dd> Cleanup counters</p>
<dt>[ returns int ] ibdmCongTrace p_fabric srcLid dstLid</p>
<dd> Trace a path between the LIDs updating link usage info</p>
<dt>[ returns int ] ibdmCongReport p_fabric</p>
<dd> Report the resulting congestion information</p>
<dt>[ returns int ] ibdmCongDump p_fabric</p>
<dd> Dump all congestion tracking info</dl>
<h2>AUTHOR</h2>
<p> Eitan Zahavi, Mellanox Technologies <font SIZE="-1">LTD</font>, eitan [at] mellanox.co.il </p>
<h2>Index</h2>
