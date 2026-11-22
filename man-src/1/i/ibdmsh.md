---

title: "ibdmsh(1)"
name: "ibdmsh"
section: "1"
letter: "i"
url: "/docs/linux/man/1-ibdmsh/"
description: "ibdmsh IB DATA MODEL – Extentended TCL shell"
---

<p> <code>ibdmsh</code> IB DATA MODEL &#8211; Extentended TCL shell</p>
<h2>DESCRIPTION</h2>
<p> <code>ibdmsh</code> is a TCL shell extended with interface for the IB data model. To use this shell you will write TCL code that directly access the IB data model objects and functions. </p>
<p> The following sub sections provide detailed definition for those objects and API.</p>
<h2>IBDM Constants</h2>
<p> <code>Node Types</code> </p>
<p> The following constants are used by the node object type field </p>
<dl>
<dt>
</dt><dd> [ Constant : int ] <tt>$IB_UNKNOWN_NODE_TYPE</tt> = IB_UNKNOWN_NODE_TYPE </dd>
<p> [ Constant : int ] <tt>$IB_SW_NODE</tt> = IB_SW_NODE </p>
<p> [ Constant : int ] <tt>$IB_CA_NODE</tt> = IB_CA_NODE</dl>
<p> <code>Log Verbosity Flags</code> </p>
<p> The following constants are used as argument bits for the global variable <tt>$FabricUtilsVerboseLevel</tt> </p>
<dl>
<dt>
</dt><dd> [ Constant : int ] <tt>$FABU_LOG_NONE</tt> = 0x0 </dd>
<p> [ Constant : int ] <tt>$FABU_LOG_ERROR</tt> = 0x1 </p>
<p> [ Constant : int ] <tt>$FABU_LOG_INFO</tt> = 0x2 </p>
<p> [ Constant : int ] <tt>$FABU_LOG_VERBOSE</tt> = 0x4</dl>
<h2>IBDM Globals</h2>
<p> Log level: set to FABU_LOG* values </p>
<dl>
<dt>
</dt><dd> [ Global : int ] <tt>$FabricUtilsVerboseLevel</tt></dd></dl>
<h2>IBDM Objects</h2>
<p> This section decribes the various object types exposed by IBDM. </p>
<p> IBDM exposes some of its internal objects. The objects identifiers returned by the various function calls are formatted according to the following rules: </p>
<p> Fabric: fabric:&lt;idx&gt; </p>
<p> System: system:&lt;fab idx&gt;:&lt;sys name&gt; </p>
<p> SysPort: sysport:&lt;fab idx&gt;:&lt;sys name&gt;:&lt;port name&gt; </p>
<p> Node: node:&lt;fab idx&gt;:&lt;node name&gt; </p>
<p> Port: port:&lt;fab idx&gt;:&lt;node name&gt;/&lt;port num&gt; </p>
<p> IBDM Objects are standard Swig-Tcl objects. As such they have two flavors for their usage: Variables, Objects. </p>
<p> <code>Variables/Pointers:</code><br/>
For each object attribute a&nbsp;<wbr>&#8220;get&#8221;&nbsp;<wbr>and&nbsp;<wbr>&#8220;set&#8221;&nbsp;<wbr>methods are provided.<br/>
The format of the methods is:&nbsp;<wbr>&lt;class&gt;_&lt;attribute&gt;_&lt;get|set&gt;.<br/>
The&nbsp;<wbr>&#8220;set&#8221;&nbsp;<wbr>method is only available for read/write attributes. </p>
<pre><code>
Example : set nodes[ibdm_get_nodes] set node[lindex $nodes 0] IBNode_numPorts_get $node
</code></pre>
<p> <code>Objects:</code><br/>
Given an object pointer one can convert it to a Tcl&nbsp;<wbr>&#8220;Object&#8221;<br/>
using the following command:<br/>
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
<p> The following are the different fields and methods of the IB Port class which describes an IB device (chip) physical port.</p>
<dl>
<dt>[ Member data: returns IBPort * ] -p_remotePort</dt>
<dd> Port connected on the other side of link</dd>
<dt>[ Member data: returns IBSysPort * ] -p_sysPort</dt>
<dd> The system port (if any) connected to</dd>
<dt>[ Member data: returns IBNode * ] -p_node</dt>
<dd> The node the port is part of.</dd>
<dt>[ Member data: returns int ] -num</dt>
<dd> Physical ports are identified by number.</dd>
<dt>[ Member data: returns unsigned int ] -base_lid</dt>
<dd> The base lid assigned to the port.</dd>
<dt>[ Member data: returns IBLinkWidth * ] -width</dt>
<dd> The link width of the port</dd>
<dt>[ Member data: returns IBLinkSpeed * ] -speed</dt>
<dd> The link speed of the port</dd>
<dt>[ Member data: returns unsigned int ] -counter1</dt>
<dd> A generic value to be used by various algorithms</dd>
<dt>[ Constructor: returns IBPort * ] IBPort name p_nodePtr number</dt>
<dd> IBPort constructor</dd>
<dt>[ Member : returns new_uint64_t ] guid_get</dt>
<dd> Obtain the guid of the port</dd>
<dt>[ Member : returns void ] guid_set guid</dt>
<dd> Modify the guid of the port</dd>
<dt>[ Member : returns new_string ] getName</dt>
<dd> Get the port name: A device port connected to system port (front pannel) returns the front pannel port name.</dd>
<dt>[ Member : returns void ] connect p_otherPort ?width? ?speed?</dt>
<dd> Connect the port to another node port with optional width and speed parameters</dd>
<dt>[ Member : returns int ] disconnect</dt>
<dd> Disconnect the port. Return 0 if successful
</dd></dl>
<p> <code>class IBNode</code> </p>
<p> The IB Node class represents a single IB Device (chip)</p>
<dl>
<dt>[ Member data: returns string * ] -name</dt>
<dd> Name of the node (instance name of the chip)</dd>
<dt>[ Member data: returns IBNodeType ] -type</dt>
<dd> Either a <tt>$IB_SW_NODE</tt> or <tt>$IB_CA_NODE</tt></dd>
<dt>[ Member data: returns uint16_t * ] -devId</dt>
<dd> The device ID of the node</dd>
<dt>[ Member data: returns uint16_t * ] -revId</dt>
<dd> The device revision Id.</dd>
<dt>[ Member data: returns uint16_t * ] -vendId</dt>
<dd> The device Vendor ID.</dd>
<dt>[ Member data: returns string * ] -attributes</dt>
<dd> Comma-sep string of arbitrary attributes k=v</dd>
<dt>[ Member data: returns uint8_t ] -rank</dt>
<dd> The rank of the node (0 is a root)</dd>
<dt>[ Member data: returns IBSystem * ] -p_system</dt>
<dd> What system we belong to</dd>
<dt>[ Member data: returns IBFabric * ] -p_fabric</dt>
<dd> What fabric we belong to.</dd>
<dt>[ Member data: returns unsigned int ] -numPorts</dt>
<dd> Number of physical ports</dd>
<dt>[ Member data: returns vec_pport * ] -Ports</dt>
<dd> Vector of all the ports</dd>
<dt>[ Member data: returns vec_vec_byte * ] -MinHopsTable</dt>
<dd> A table of the number of hops required to get from each port to each target LID</dd>
<dt>[ Member data: returns vec_byte * ] -LFT</dt>
<dd> The LFT of this node (for switches only) which is a long vector of target ports &#8211; index is the LID</dd>
<dt>[ Member : returns new_uint64_t ] guid_get</dt>
<dd> Obtain the node GUID</dd>
<dt>[ Member : returns void ] guid_set guid</dt>
<dd> Set the node GUID</dd>
<dt>[ Constructor: returns IBNode * ] IBNode name n p_fab p_sys t np</dt>
<dd> Constractor</dd>
<dt>[ Member : returns IBPort * ] makePort num</dt>
<dd> Create a new port by its number (if required) return the port pointer</dd>
<dt>[ Member : returns IBPort * ] getPort num</dt>
<dd> Get a port by number num = 1..N:</dd>
<dt>[ Member : returns void ] setHops p_port lid hops</dt>
<dd> Set the min hop for the given port (* is all) lid pair</dd>
<dt>[ Member : returns int ] getHops p_port lid</dt>
<dd> Get the min number of hops defined for the given port or all</dd>
<dt>[ Member : returns IBPort * ] getFirstMinHopPort lid</dt>
<dd> Scan the node ports and find the first port with min hop to the lid</dd>
<dt>[ Member : returns void ] setLFTPortForLid lid portNum</dt>
<dd> Set the Linear Forwarding Table for the given LID</dd>
<dt>[ Member : returns int ] getLFTPortForLid lid</dt>
<dd> Get the LFT for a given LID</dd>
<dt>[ Member : returns void ] repHopTable</dt>
<dd> Dump out the min hop table of the node
</dd></dl>
<p> <code>class IBSysPort</code> </p>
<p> The IBSysPort class represents an IB plug on the system front or back pannels</p>
<dl>
<dt>[ Member data: returns string * ] -name</dt>
<dd> The front pannel name (silk) of the port</dd>
<dt>[ Member data: returns IBSysPort * ] -p_remoteSysPort</dt>
<dd> If connected the other side sys port</dd>
<dt>[ Member data: returns IBSystem * ] -p_system</dt>
<dd> System it benongs to</dd>
<dt>[ Member data: returns IBPort * ] -p_nodePort</dt>
<dd> The node port it connects to.</dd>
<dt>[ Constructor: returns IBSysPort * ] IBSysPort name n p_sys</dt>
<dd> Constructor</dd>
<dt>[ Member : returns void ] connect p_otherSysPort ?width? ?speed?</dt>
<dd> Connect two SysPorts</dd>
<dt>[ Member : returns int ] disconnect</dt>
<dd> Disconnect the SysPort (and ports). Return 0 if successful
</dd></dl>
<p> <code>class IBSystem</code> </p>
<p> The IBSystem class represents an entire chassis</p>
<dl>
<dt>[ Member data: returns string * ] -name</dt>
<dd> The &#8220;host&#8221; name of the system</dd>
<dt>[ Member data: returns string * ] -type</dt>
<dd> What is the type i.e. Cougar, Buffalo, MTS2400, etc. A corresponding IBNL file should exist &#8211; defining this system type</dd>
<dt>[ Member data: returns IBFabric * ] -p_fabric</dt>
<dd> Fabric the system belongs to</dd>
<dt>[ Member data: returns map_str_pnode * ] -NodeByName</dt>
<dd> Provide the node pointer by its name</dd>
<dt>[ Member data: returns map_str_psysport * ] -PortByName</dt>
<dd> A map provising pointer to the SysPort by name</dd>
<dt>[ Constructor: returns IBSystem * ] IBSystem name n p_fab t</dt>
<dd> Constractor</dd>
<dt>[ Member : returns new_uint64_t ] guid_get</dt>
<dd> Obtain the system image GUID</dd>
<dt>[ Member : returns void ] guid_set guid</dt>
<dd> Set the system image GUID</dd>
<dt>[ Member : returns IBSysPort * ] makeSysPort pName</dt>
<dd> Make sure we got the port defined (so define it if not)</dd>
<dt>[ Member : returns IBPort * ] getSysPortNodePortByName sysPortName</dt>
<dd> Get the node port for the given sys port by name</dd>
<dt>[ Member : returns IBSysPort * ] getSysPort name</dt>
<dd> Get a Sys Port by name
</dd></dl>
<p> <code>class IBFabric</code> </p>
<p> Represents an entire IB subnet made of systems</p>
<dl>
<dt>[ Member data: returns map_str_pnode * ] -NodeByName</dt>
<dd> Provide a list of node name and pointer pairs</dd>
<dt>[ Member data: returns map_str_psys * ] -SystemByName</dt>
<dd> Provide a list of system name and pointer pairs</dd>
<dt>[ Member data: returns vec_pport * ] -PortByLid</dt>
<dd> Provides a list of system port name and pointer pairs</dd>
<dt>[ Member data: returns map_guid_pnode * ] -NodeByGuid</dt>
<dd> Provides a list of node guid and node pointer pairs</dd>
<dt>[ Member data: returns map_guid_psys * ] -SystemByGuid</dt>
<dd> Provides a list of system image guid and system pointer pairs</dd>
<dt>[ Member data: returns map_guid_pport * ] -PortByGuid</dt>
<dd> Provides a list of port guid and port pointer pairs</dd>
<dt>[ Member data: returns unsigned int ] -minLid</dt>
<dd> Track min lid used.</dd>
<dt>[ Member data: returns unsigned int ] -maxLid</dt>
<dd> Track max lid used.</dd>
<dt>[ Member data: returns unsigned int ] -lmc</dt>
<dd> LMC value used</dd>
<dt>[ Member : returns IBNode * ] makeNode n p_sys type numPorts</dt>
<dd> Get the node by its name (create one of does not exist)</dd>
<dt>[ Member : returns IBNode * ] getNode name</dt>
<dd> Get the node by its name</dd>
<dt>[ Member : returns list_pnode * ] getNodesByType type</dt>
<dd> Return the list of node pointers matching the required type</dd>
<dt>[ Member : returns IBSystem * ] makeGenericSystem name</dt>
<dd> Create a new generic system &#8211; basically an empty container for nodes&#8230;</dd>
<dt>[ Member : returns IBSystem * ] makeSystem name type</dt>
<dd> Create a new system &#8211; the type must have a registed factory.</dd>
<dt>[ Member : returns IBSystem * ] getSystem name</dt>
<dd> Get system by name</dd>
<dt>[ Member : returns IBSystem * ] getSystemByGuid guid</dt>
<dd> get the system by its guid</dd>
<dt>[ Member : returns IBNode * ] getNodeByGuid guid</dt>
<dd> get the node by its guid</dd>
<dt>[ Member : returns IBPort * ] getPortByGuid guid</dt>
<dd> get the port by its guid</dd>
<dt>[ Member : returns void ] addCable t1 n1 p1 t2 n2 p2 ?width? ?speed?</dt>
<dd> Adds a cable given two sets of node type, node name and port number. Optionally use a given width and speed for the connection</dd>
<dt>[ Member : returns int ] parseCables fn</dt>
<dd> Parse the cables file and build the fabric</dd>
<dt>[ Member : returns int ] parseTopology fn</dt>
<dd> Parse Topology File and build the fabric</dd>
<dt>[ Member : returns int ] addLink type1 numPorts1 sysGuid1 nodeGuid1 portGuid1 vend1 devId1 rev1 desc1 lid1 portNum1 type2 numPorts2 sysGuid2 nodeGuid2 portGuid2 vend2 devId2 rev2 desc2 lid2 portNum2 ?width? ?speed?</dt>
<dd> Add a link into the fabric &#8211; this will create system and nodes as required.</dd>
<dt>[ Member : returns int ] parseSubnetLinks fn</dt>
<dd> Parse the OpenSM subnet.lst file and build the fabric from it.</dd>
<dt>[ Member : returns int ] parseFdbFile fn</dt>
<dd> Parse OpenSM FDB dump file and fill in the switches LFT tables</dd>
<dt>[ Member : returns int ] parseMCFdbFile fn</dt>
<dd> Parse an OpenSM MCFDBs file and set the MFT table accordingly</dd>
<dt>[ Member : returns int ] parsePSLFile fn</dt>
<dd> Parse Path to SL mapping file. Each line with: src_node_guid DLID SL</dd></dl>
<p> Used by credit loop check</p>
<dl>
<dt>[ Member : returns int ] parseSLVLFile fn</dt>
<dd> Parse SLVL tables file. Each line holds: sw_node_guid in_port out_port 0x(sl0)(sl1) 0x(sl2)(sl3)&#8230;</dd>
<dt>[ Member : returns void ] setLidPort lid p_port</dt>
<dd> Set a lid port</dd>
<dt>[ Member : returns IBPort * ] getPortByLid lid</dt>
<dd> Get a port by lid</dd>
<dt>[ returns IBFabric * ] new_IBFabric</dt>
<dd> Construct a new fabric</dd>
<dt>[ returns void ] delete_IBFabric p_fabric</dt>
<dd> Destruct a fabric</dd></dl>
<h2>IBDM Functions</h2>
<p> This section provide the details about the functions IBDM exposes. The order follows the expected order in a regular IBDM flow. They all return 0 on succes. </p>
<p> <code>Subnet Utilities</code> </p>
<p> The file holds a set of utilities to be run on the subnet to mimic OpenSM initialization and analyze the results:</p>
<dl>
<dt>[ returns int ] ibdmAssignLids p_smNodePort ?lmc?</dt>
<dd> Assign LIDs with an optional LMC (multiple LID per port)</dd>
<dt>[ returns int ] ibdmCalcMinHopTables p_fabric</dt>
<dd> Calculate and populate the MinHopTables required for running OpenSM style routing.</dd>
<dt>[ returns int ] ibdmCalcUpDnMinHopTbls p_fabric rootNodesNameRex</dt>
<dd> Calculate and populate the MinHopTables following Up/Down rule.</dd>
<dt>[ returns int ] ibdmOsmRoute p_fabric</dt>
<dd> Route the fabric with OpenSM style routing</dd>
<dt>[ returns int ] ibdmEnhancedRoute p_fabric</dt>
<dd> Route the fabric with OpenSM style routing enhanced with better support for LMC &gt; 0</dd>
<dt>[ returns int ] ibdmFatTreeRoute p_fabric rootNodes</dt>
<dd> Route the fabric using algorithm that fits only full fat trees</dd>
<dt>[ returns int ] ibdmFatTreeAnalysis p_fabric</dt>
<dd> Analyze the fabric to see if it is a fat tree and route it if it is</dd>
<dt>[ returns int ] ibdmVerifyCAtoCARoutes p_fabric</dt>
<dd> Make sure all (H)CAs are connected to each other based on the LFT settings</dd>
<dt>[ returns int ] ibdmVerifyAllPaths p_fabric</dt>
<dd> Make sure all Switches and (H)CAs are connected to each other based on the LFT settings</dd>
<dt>[ returns int ] ibdmAnalyzeLoops p_fabric</dt>
<dd> A rigorous check for credit loops. This algorithm does a full and accurate check but its reporting of credit loop paths is hard to interpret. If you know the roots of the tree (or the tree is symmetrical) it is preferable to use the ibdmReportNonUpDownCa2CaPaths</dd>
<dt>[ returns list_pnode ] ibdmFindSymmetricalTreeRoots p_fabric</dt>
<dd> Analyze the tree topology and find the roots of the tree based on its symmetry</dd>
<dt>[ returns list_pnode ] ibdmFindRootNodesByMinHop p_fabric</dt>
<dd> Based on the MinHopTable find the roots of the tree. A 5% assymetry is allowed</dd>
<dt>[ returns int ] ibdmRankFabricByRoots p_fabric rootNodes</dt>
<dd> Given the list of root nodes (names) rank the nodes (root = 0)</dd>
<dt>[ returns int ] ibdmReportNonUpDownCa2CaPaths p_fabric rootNodes</dt>
<dd> Analyze the routes to make sure Up/Down rule is maintained</dd>
<dt>[ returns int ] ibdmCheckMulticastGroups p_fabric</dt>
<dd> Verify connectivity of multicast routing</dd>
<dt>[ returns int ] ibdmCheckFabricMCGrpsForCreditLoopPotential p_fabric rootNodes</dt>
<dd> Analyze multicast routing to make sure it obeys Up/Down rule</dd>
<dt>[ returns int ] ibdmLinkCoverageAnalysis p_fabric rootNodes</dt>
<dd> Prepare a schedule for transmission from a set of sources to destinations such that in each stage there are no links that are over subscribed and after all stages all the links of the fabric were excersized
</dd></dl>
<p> <code>Tracing Utilities</code> </p>
<p> These functions allows tracing paths reporting back the visited nodes</p>
<dl>
<dt>[ returns int ] ibdmTraceDRPathRoute p_smNodePort drPathPortNums</dt>
<dd> Trace a directed route path from the given port</dd>
<dt>[ returns int ] ibdmTraceRouteByMinHops p_fabric slid dlid</dt>
<dd> Trace a path along the MinHop from the source to destination LIDs</dd>
<dt>[ returns int ] ibdmTraceRouteByLFT p_fabric slid dlid hops p_nodesList</dt>
<dd> Trace a path following the LFT updating the hops and node list variables
</dd></dl>
<p> <code>Topology Matching Utilities</code> </p>
<p> The following utilities matches two fabrics providing both missmatch messages and a unified fabric</p>
<dl>
<dt>[ returns int ] ibdmMatchFabrics p_spec_fabric p_discovered_fabric anchorNodeName anchorPortNum anchorPortGuid</dt>
<dd> Match a topology based fabric with a discovered one starting at the enchor port</dd>
<dt>[ returns int ] ibdmBuildMergedFabric p_spec_fabric p_discovered_fabric p_merged_fabric</dt>
<dd> After matching using ibdmMatchFabrics populate the &#8220;merged fabric&#8221; with information merged for the matched nodes
</dd></dl>
<p> <code>Congestion Analysis Utilities</code> </p>
<p> Provide ability to track and report link oversubscription</p>
<dl>
<dt>[ returns int ] ibdmCongInit p_fabric</dt>
<dd> Initialize the tracking system</dd>
<dt>[ returns int ] ibdmCongCleanup p_fabric</dt>
<dd> Cleanup the counters and deallocate</dd>
<dt>[ returns int ] ibdmCongClear p_fabric</dt>
<dd> Cleanup counters</dd>
<dt>[ returns int ] ibdmCongTrace p_fabric srcLid dstLid</dt>
<dd> Trace a path between the LIDs updating link usage info</dd>
<dt>[ returns int ] ibdmCongReport p_fabric</dt>
<dd> Report the resulting congestion information</dd>
<dt>[ returns int ] ibdmCongDump p_fabric</dt>
<dd> Dump all congestion tracking info</dd></dl>
<h2>AUTHOR</h2>
<p> Eitan Zahavi, Mellanox Technologies LTD, eitan [at] mellanox.co.il </p>
