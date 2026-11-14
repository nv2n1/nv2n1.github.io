---
title: "ibis(1)"
name: "ibis"
section: "1"
letter: "i"
url: "/docs/linux/man/1-ibis/"
description: "ibis – IB management Inband Services – an extended TCL shell"
---

<h2>NAME</h2>
<p> <code>ibis</code> &#8211; IB management Inband Services &#8211; an extended TCL shell</p>
<h2>SYNOPSYS</h2>
<p> ibis [-port_num &lt;port number to attach to&gt;]</p>
<h2>DESCRIPTION</h2>
<p> <code>ibis</code> is a <font SIZE="-1">TCL</font> shell extended with interface for sending and receiving <font SIZE="-1">IB</font> management datagrams (<font SIZE="-1">MADS</font>). To use this shell you will write <font SIZE="-1">TCL</font> code that excersizes the regular <font SIZE="-1">TCL</font> command and the special <font SIZE="-1">API</font> provided by this extension. Interactive use is also possible and is greatly enhanced if tclreadline package is available on the machine. </p>
<p> The following sub sections provide detailed definition for the <font SIZE="-1">API</font> and global objects defined by the extension. The different MADs APIs are group by the management class.</p>
<h2>IBIS Constants</h2>
<p> These constants are provided by <font SIZE="-1">IBIS:</font> </p>
<p> <code>Log Verbosity Flags</code> </p>
<dl>
<dt>[ Constant : int ] $IBIS_LOG_NONE = 0x00</p>
<dd>
<dt>[ Constant : int ] $IBIS_LOG_ERROR = 0x01</p>
<dd>
<dt>[ Constant : int ] $IBIS_LOG_INFO = 0x02</p>
<dd>
<dt>[ Constant : int ] $IBIS_LOG_VERBOSE = 0x04</p>
<dd>
<dt>[ Constant : int ] $IBIS_LOG_DEBUG = 0x08</p>
<dd>
<dt>[ Constant : int ] $IBIS_LOG_FUNCS = 0x10</p>
<dd>
<dt>[ Constant : int ] $IBIS_LOG_FRAMES = 0x20</p>
<dd></dl>
<h2>IBIS Functions</h2>
<p> This section provide the details about the functions <font SIZE="-1">IBIS</font> exposes. They all return 0 on succes.</p>
<dl>
<dt>[return list] ibis_get_local_ports_info</p>
<dd> Return the list of available <font SIZE="-1">IB</font> ports with <font SIZE="-1">GUID</font>, <font SIZE="-1">LID</font>, state and port number.</p>
<dt>[ returns int ] ibis_init</p>
<dd> Initialize ibis object</p>
<dt>[ returns int ] ibis_set_verbosity level</p>
<dd> Change the log verbosity</p>
<dt>[ returns int ] ibis_set_port guid</p>
<dd> Set the port <font SIZE="-1">IBIS</font> is attached to and initialize all sub packages. Must be called once during ibis operation.</p>
<dt>[ returns new_uint64_t ] ibis_get_port</p>
<dd> Provide the <font SIZE="-1">GUID</font> of the port <font SIZE="-1">IBIS</font> is attached to</p>
<dt>[ returns int ] ibis_set_transaction_timeout timeout_ms</p>
<dd> Set the transaction time out in [msec]</p>
<dt>[ returns int ] ibis_exit</p>
<dd> Exit <font SIZE="-1">IBIS</font>.</p>
<dt>[ returns int ] ibis_puts verbosity msg</p>
<dd> Appends a message to the OpenSM log
</dl>
<p> <code><font SIZE="-1">IBIS</font> Options Object</code> </p>
<dl>
<dt>
<dd> The <font SIZE="-1">IBIS</font> options are available through the predefined object: ibis_opts. It can be manipulated using the standard Tcl methods: cget and configure. Examples: </p>
<pre>
   ibis_opts cget -force_log_flush
</pre>
<pre>
   ibis_opts configure -force_log_flush TRUE
</pre>
<p> The following are the different options that can be configured:</dl>
<dl>
<dt>[ Member data: returns boolean_t * ] -single_thread</p>
<dd> Run single threaded</p>
<dt>[ Member data: returns boolean_t * ] -force_log_flush</p>
<dd> If <font SIZE="-1">TRUE</font> &#8211; forces flash after each log message (<font SIZE="-1">TRUE</font>).</p>
<dt>[ Member data: returns uint8_t * ] -log_flags</p>
<dd> The log levels to be used</p>
<dt>[ Member data: returns char * ] -log_file</p>
<dd> The name of the log file to be used.Must be configured before <code>ibis_init</code> is used to make an affect</p>
<dt>[ Member data: returns uint64_t * ] -sm_key</p>
<dd> The SM_Key to be used when sending SubnetMgt and SubnetAdmin MADs</p>
<dt>[ Member data: returns uint64_t * ] -m_key</p>
<dd> The M_Key to be used when sending SubnetMgt</p>
<dt>[ Member data: returns uint64_t * ] -v_key</p>
<dd> The Vendor Key to be used when sending Vendor Specific MADs.</dl>
<h2>IBPM</h2>
<p> <font SIZE="-1">IBPM</font> stands for <font SIZE="-1">IB</font> Performance Monitoring MADs. <font SIZE="-1">IB</font> provides standard facilities for tracking statistics on every port. </p>
<p> This section provide the details about the functions <font SIZE="-1">IBPM</font> exposes. They all return 0 on succes.</p>
<dl>
<dt>[ returns int ] pmMultiMaxGet</p>
<dd> Obtain the maximal number of parallel queries that can be sent</p>
<dt>[ returns int ] pmGetPortCounters lid port_select</p>
<dd> Send a &#8220;PortCounters&#8221; query to teh given <font SIZE="-1">LID</font> and port</p>
<dt>[ returns int ] pmGetPortCountersMulti num lid_list port_select_list</p>
<dd> Send a batch of &#8220;PortCounters&#8221; queries to the given list of LIDs and ports. num &#8211; defines the number of elements in each list.</p>
<dt>[ returns int ] pmGetExtPortCountersMulti num lid_list port_select_list</p>
<dd> Send a batch of &#8220;ExtendedPortCounters&#8221; queries to the given list of LIDs and ports. num &#8211; defines the number of elements in each list.</p>
<dt>[ returns int ] pmClrAllCounters lid port_select</p>
<dd> Sends a command to &#8220;clear all counters&#8221; on the given <font SIZE="-1">LID</font> and port</p>
<dt>[ returns int ] pmClrAllCountersMulti num lid_list port_select_list</p>
<dd> Send a batch of &#8220;clear all counters&#8221; commands to the given list of LIDs and ports. num &#8211; defines the number of elements in each list.</dl>
<h2>IBSAC</h2>
<p> <font SIZE="-1">IBSAC</font> stands for <font SIZE="-1">IB</font> Subnet Administrator (<font SIZE="-1">SA</font>) Client. It provide means to query the <font SIZE="-1">SA</font> for information about the various objects it manages </p>
<p> The following sections describe the concepts behind the <font SIZE="-1">SAC</font> interface and then provides detailed description of each attribute that can be queried. </p>
<p> <code><font SIZE="-1">IBSAC</font> Objects</code> </p>
<dl>
<dt>
<dd> <font SIZE="-1">IBSAC</font> uses predefined global objects to facilitate <font SIZE="-1">SA</font> Queries. Such objects are named sac&lt;Attribute&gt;Query. Each such object exposes a standard set of methods:</dl>
<dl>
<dt>dump</p>
<dd> dump out all fields and values for the obejct</p>
<dt>cget -&lt;field&gt;:</p>
<dd> obtain the value of the given field</p>
<dt>configure -&lt;field&gt; &lt;value&gt;:</p>
<dd> set the field value</p>
<dt>get &lt;comp mask&gt;:</p>
<dd> query the <font SIZE="-1">SA</font> for one record using the component mask and field values as set on the query object</p>
<dt>getTable &lt;comp mask&gt;:</p>
<dd> query the <font SIZE="-1">SA</font> for all records matching component mask and field values as set on the query object </p>
<p> Some <font SIZE="-1">SA</font> maintained objects support the &#8220;set&#8221; and &#8220;delete&#8221; methods. In that case the following methods are made available on the corresponding query object:</p>
<dt>set &lt;comp mask&gt;:</p>
<dd> send a <code>set</code> method to the <font SIZE="-1">SA</font> with the component mask and field values as set on the query object</p>
<dt>delete &lt;comp mask&gt;:</p>
<dd> send a <code>delete</code> method to the <font SIZE="-1">SA</font> with the component mask and field values as set on the query object
</dl>
<p> <code>Returned Objects</code> </p>
<p> This section describes the values returned from the get/getTable/set/delete methods of the query objects: </p>
<p> Each query returns a list (or one) identifiers (pointers) for objects. There identifiers are formatted according to the type of object they point to using the following prefixes: </p>
<p> Queries embedding Subnet Management Attributes:</p>
<dl>
<dt>ni:&lt;idx&gt; = node info</p>
<dd>
<dt>nr:&lt;idx&gt; = node info record (<font SIZE="-1">SA</font> <font SIZE="-1">RID</font> + node info)</p>
<dd>
<dt>pi:&lt;idx&gt; = port info</p>
<dd>
<dt>pir:&lt;idx&gt; = port info record (<font SIZE="-1">SA</font> <font SIZE="-1">RID</font> + port info)</p>
<dd>
<dt>smi:&lt;idx&gt; = <font SIZE="-1">SM</font> info</p>
<dd>
<dt>smir:&lt;idx&gt; = <font SIZE="-1">SM</font> info record (<font SIZE="-1">SA</font> <font SIZE="-1">RID</font> + <font SIZE="-1">SM</font> info)</p>
<dd>
<dt>swi:&lt;idx&gt; = switch info</p>
<dd>
<dt>swir:&lt;idx&gt; = switch info record (<font SIZE="-1">SA</font> <font SIZE="-1">RID</font> + switch info)</p>
<dd>
<dt>slvt:&lt;idx&gt; = <font SIZE="-1">SL</font> to <font SIZE="-1">VL</font> table</p>
<dd>
<dt>slvr:&lt;idx&gt; = <font SIZE="-1">SL</font> to <font SIZE="-1">VL</font> table Record (<font SIZE="-1">SA</font> <font SIZE="-1">RID</font> + <font SIZE="-1">SL</font> to <font SIZE="-1">VL</font> table)</p>
<dd>
<dt>pkt:&lt;idx&gt; = PKey table</p>
<dd>
<dt>pkr:&lt;idx&gt; = PKey table record (<font SIZE="-1">SA</font> <font SIZE="-1">RID</font> + PKey table)</p>
<dd> Queries of non embedded attributes:</p>
<dt>link:&lt;idx&gt; = link record</p>
<dd>
<dt>path:&lt;idx&gt; = path record</p>
<dd>
<dt>lft:&lt;idx&gt; = Linear forwarding table</p>
<dd>
<dt>mcm:&lt;idx&gt; = Multicast Member Record</p>
<dd>
<dt>cpi:&lt;idx&gt; = <font SIZE="-1">SA</font> Class Port Info</p>
<dd>
<dt>info:&lt;idx&gt; = Inform info (registration of event forwarding)</p>
<dd>
<dt>svc:&lt;idx&gt; = Service Record</p>
<dd>
<dt>vlarb:&lt;idx&gt;= <font SIZE="-1">VL</font> Arbitration table record</p>
<dd>
</dl>
<p> <code><font SIZE="-1">NODE</font> <font SIZE="-1">INFO</font> <font SIZE="-1">RECORD</font></code> </p>
<dl>
<dt>
<dd> Component mask bits:</dl>
<dl>
<dt>[ Constant : int ] $IB_NR_COMPMASK_LID = 0x1</p>
<dd>
<dt>[ Constant : int ] $IB_NR_COMPMASK_RESERVED1 = 0x2</p>
<dd>
<dt>[ Constant : int ] $IB_NR_COMPMASK_BASEVERSION = 0x4</p>
<dd>
<dt>[ Constant : int ] $IB_NR_COMPMASK_CLASSVERSION = 0x8</p>
<dd>
<dt>[ Constant : int ] $IB_NR_COMPMASK_NODETYPE = 0x10</p>
<dd>
<dt>[ Constant : int ] $IB_NR_COMPMASK_NUMPORTS = 0x20</p>
<dd>
<dt>[ Constant : int ] $IB_NR_COMPMASK_SYSIMAGEGUID = 0x40</p>
<dd>
<dt>[ Constant : int ] $IB_NR_COMPMASK_NODEGUID = 0x80</p>
<dd>
<dt>[ Constant : int ] $IB_NR_COMPMASK_PORTGUID = 0x100</p>
<dd>
<dt>[ Constant : int ] $IB_NR_COMPMASK_PARTCAP = 0x200</p>
<dd>
<dt>[ Constant : int ] $IB_NR_COMPMASK_DEVID = 0x400</p>
<dd>
<dt>[ Constant : int ] $IB_NR_COMPMASK_REV = 0x800</p>
<dd>
<dt>[ Constant : int ] $IB_NR_COMPMASK_PORTNUM = 0x1000</p>
<dd>
<dt>[ Constant : int ] $IB_NR_COMPMASK_VENDID = 0x2000</p>
<dd>
<dt>[ Constant : int ] $IB_NR_COMPMASK_NODEDESC = 0x4000</p>
<dd> &#8212;- </p>
<p> <i>class sacNodeInfo</i> </p>
<p> Fields:</p>
<dt>[ Member data: returns uint8_t * ] -base_version</p>
<dd>
<dt>[ Member data: returns uint8_t * ] -class_version</p>
<dd>
<dt>[ Member data: returns uint8_t * ] -node_type</p>
<dd>
<dt>[ Member data: returns uint8_t * ] -num_ports</p>
<dd>
<dt>[ Member data: returns ib_net64_t * ] -sys_guid</p>
<dd>
<dt>[ Member data: returns ib_net64_t * ] -node_guid</p>
<dd>
<dt>[ Member data: returns ib_net64_t * ] -port_guid</p>
<dd>
<dt>[ Member data: returns ib_net16_t * ] -partition_cap</p>
<dd>
<dt>[ Member data: returns ib_net16_t * ] -device_id</p>
<dd>
<dt>[ Member data: returns ib_net32_t * ] -revision</p>
<dd>
<dt>[ Member data: returns ib_net32_t * ] -port_num_vendor_id</p>
<dd>
<dt>[ Member : returns void ] delete</p>
<dd> &#8212;- </p>
<p> <i>class sacNodeRec</i> </p>
<p> <font SIZE="-1">RID</font> Fields:</p>
<dt>[ Member data: returns ib_net16_t * ] -lid</p>
<dd>
<dt>[ Member data: returns sacNodeInfo * ] -node_info</p>
<dd>
<dt>[ Member data: returns ib_node_desc_t * ] -node_desc</p>
<dd> Methods:</p>
<dt>[ Member : returns char * ] get comp_mask</p>
<dd>
<dt>[ Member : returns char * ] getTable comp_mask</p>
<dd>
<dt>[ Member : returns void ] delete</p>
<dd>
</dl>
<p> <code><font SIZE="-1">PORT</font> <font SIZE="-1">INFO</font> <font SIZE="-1">RECORD</font></code> </p>
<dl>
<dt>
<dd> Component mask bits:</dl>
<dl>
<dt>[ Constant : char * ] $IB_PIR_COMPMASK_LID = 0x1</p>
<dd>
<dt>[ Constant : char * ] $IB_PIR_COMPMASK_PORTNUM = 0x2</p>
<dd>
<dt>[ Constant : char * ] $IB_PIR_COMPMASK_RESV1 = 0x4</p>
<dd>
<dt>[ Constant : char * ] $IB_PIR_COMPMASK_MKEY = 0x8</p>
<dd>
<dt>[ Constant : int ] $IB_PIR_COMPMASK_GIDPRE = 0x10</p>
<dd>
<dt>[ Constant : int ] $IB_PIR_COMPMASK_BASELID = 0x20</p>
<dd>
<dt>[ Constant : int ] $IB_PIR_COMPMASK_SMLID = 0x40</p>
<dd>
<dt>[ Constant : int ] $IB_PIR_COMPMASK_CAPMASK = 0x80</p>
<dd>
<dt>[ Constant : int ] $IB_PIR_COMPMASK_DIAGCODE = 0x100</p>
<dd>
<dt>[ Constant : int ] $IB_PIR_COMPMASK_MKEYLEASEPRD = 0x200</p>
<dd>
<dt>[ Constant : int ] $IB_PIR_COMPMASK_LOCALPORTNUM = 0x400</p>
<dd>
<dt>[ Constant : int ] $IB_PIR_COMPMASK_LNKWIDTHSUPPORT = 0x800</p>
<dd>
<dt>[ Constant : int ] $IB_PIR_COMPMASK_LNKWIDTHACTIVE = 0x1000</p>
<dd>
<dt>[ Constant : int ] $IB_PIR_COMPMASK_LINKWIDTHENABLED = 0x2000</p>
<dd>
<dt>[ Constant : int ] $IB_PIR_COMPMASK_LNKSPEEDSUPPORT = 0x4000</p>
<dd>
<dt>[ Constant : int ] $IB_PIR_COMPMASK_PORTSTATE = 0x10000</p>
<dd>
<dt>[ Constant : int ] $IB_PIR_COMPMASK_PORTPHYSTATE = 0x20000</p>
<dd>
<dt>[ Constant : int ] $IB_PIR_COMPMASK_LINKDWNDFLTSTATE = 0x40000</p>
<dd>
<dt>[ Constant : int ] $IB_PIR_COMPMASK_MKEYPROTBITS = 0x80000</p>
<dd>
<dt>[ Constant : int ] $IB_PIR_COMPMASK_LMC = 0x100000</p>
<dd>
<dt>[ Constant : int ] $IB_PIR_COMPMASK_LINKSPEEDACTIVE = 0x200000</p>
<dd>
<dt>[ Constant : int ] $IB_PIR_COMPMASK_LINKSPEEDENABLE = 0x400000</p>
<dd>
<dt>[ Constant : int ] $IB_PIR_COMPMASK_NEIGHBORMTU = 0x800000</p>
<dd>
<dt>[ Constant : int ] $IB_PIR_COMPMASK_MASTERSMSL = 0x1000000</p>
<dd>
<dt>[ Constant : int ] $IB_PIR_COMPMASK_VLCAP = 0x2000000</p>
<dd>
<dt>[ Constant : int ] $IB_PIR_COMPMASK_INITTYPE = 0x4000000</p>
<dd>
<dt>[ Constant : int ] $IB_PIR_COMPMASK_VLHIGHLIMIT = 0x8000000</p>
<dd>
<dt>[ Constant : int ] $IB_PIR_COMPMASK_VLARBHIGHCAP = 0x10000000</p>
<dd>
<dt>[ Constant : int ] $IB_PIR_COMPMASK_VLARBLOWCAP = 0x20000000</p>
<dd>
<dt>[ Constant : int ] $IB_PIR_COMPMASK_INITTYPEREPLY = 0x40000000</p>
<dd>
<dt>[ Constant : int ] $IB_PIR_COMPMASK_MTUCAP = 0x80000000</p>
<dd>
<dt>[ Constant : char * ] $IB_PIR_COMPMASK_VLSTALLCNT = 0x100000000</p>
<dd>
<dt>[ Constant : char * ] $IB_PIR_COMPMASK_HOQLIFE = 0x200000000</p>
<dd>
<dt>[ Constant : char * ] $IB_PIR_COMPMASK_OPVLS = 0x400000000</p>
<dd>
<dt>[ Constant : char * ] $IB_PIR_COMPMASK_PARENFIN = 0x800000000</p>
<dd>
<dt>[ Constant : char * ] $IB_PIR_COMPMASK_PARENFOUT = 0x1000000000</p>
<dd>
<dt>[ Constant : char * ] $IB_PIR_COMPMASK_FILTERRAWIN = 0x2000000000</p>
<dd>
<dt>[ Constant : char * ] $IB_PIR_COMPMASK_FILTERRAWOUT = 0x4000000000</p>
<dd>
<dt>[ Constant : char * ] $IB_PIR_COMPMASK_MKEYVIO = 0x8000000000</p>
<dd>
<dt>[ Constant : char * ] $IB_PIR_COMPMASK_PKEYVIO = 0x10000000000</p>
<dd>
<dt>[ Constant : char * ] $IB_PIR_COMPMASK_QKEYVIO = 0x20000000000</p>
<dd>
<dt>[ Constant : char * ] $IB_PIR_COMPMASK_GUIDCAP = 0x40000000000</p>
<dd>
<dt>[ Constant : char * ] $IB_PIR_COMPMASK_RESV2 = 0x80000000000</p>
<dd>
<dt>[ Constant : char * ] $IB_PIR_COMPMASK_SUBNTO = 0x100000000000</p>
<dd>
<dt>[ Constant : char * ] $IB_PIR_COMPMASK_RESV3 = 0x200000000000</p>
<dd>
<dt>[ Constant : char * ] $IB_PIR_COMPMASK_RESPTIME = 0x400000000000</p>
<dd>
<dt>[ Constant : char * ] $IB_PIR_COMPMASK_LOCALPHYERR = 0x800000000000</p>
<dd>
<dt>[ Constant : char * ] $IB_PIR_COMPMASK_OVERRUNERR = 0x1000000000000</p>
<dd> &#8212;- </p>
<p> <i>class sacPortInfo</i> </p>
<p> Fields:</p>
<dt>[ Member data: returns ib_net64_t * ] -m_key</p>
<dd>
<dt>[ Member data: returns ib_net64_t * ] -subnet_prefix</p>
<dd>
<dt>[ Member data: returns ib_net16_t * ] -base_lid</p>
<dd>
<dt>[ Member data: returns ib_net16_t * ] -master_sm_base_lid</p>
<dd>
<dt>[ Member data: returns ib_net32_t * ] -capability_mask</p>
<dd>
<dt>[ Member data: returns ib_net16_t * ] -diag_code</p>
<dd>
<dt>[ Member data: returns ib_net16_t * ] -m_key_lease_period</p>
<dd>
<dt>[ Member data: returns uint8_t * ] -local_port_num</p>
<dd>
<dt>[ Member data: returns uint8_t * ] -link_width_enabled</p>
<dd>
<dt>[ Member data: returns uint8_t * ] -link_width_supported</p>
<dd>
<dt>[ Member data: returns uint8_t * ] -link_width_active</p>
<dd>
<dt>[ Member data: returns uint8_t * ] -state_info1</p>
<dd> LinkSpeedSupported and PortState</p>
<dt>[ Member data: returns uint8_t * ] -state_info2</p>
<dd> PortPhysState and LinkDownDefaultState</p>
<dt>[ Member data: returns uint8_t * ] -mkey_lmc</p>
<dd>
<dt>[ Member data: returns uint8_t * ] -link_speed</p>
<dd> LinkSpeedEnabled and LinkSpeedActive</p>
<dt>[ Member data: returns uint8_t * ] -mtu_smsl</p>
<dd>
<dt>[ Member data: returns uint8_t * ] -vl_cap</p>
<dd> VlCap and InitType</p>
<dt>[ Member data: returns uint8_t * ] -vl_high_limit</p>
<dd>
<dt>[ Member data: returns uint8_t * ] -vl_arb_high_cap</p>
<dd>
<dt>[ Member data: returns uint8_t * ] -vl_arb_low_cap</p>
<dd>
<dt>[ Member data: returns uint8_t * ] -mtu_cap</p>
<dd>
<dt>[ Member data: returns uint8_t * ] -vl_stall_life</p>
<dd>
<dt>[ Member data: returns uint8_t * ] -vl_enforce</p>
<dd>
<dt>[ Member data: returns ib_net16_t * ] -m_key_violations</p>
<dd>
<dt>[ Member data: returns ib_net16_t * ] -p_key_violations</p>
<dd>
<dt>[ Member data: returns ib_net16_t * ] -q_key_violations</p>
<dd>
<dt>[ Member data: returns uint8_t * ] -guid_cap</p>
<dd>
<dt>[ Member data: returns uint8_t * ] -subnet_timeout</p>
<dd>
<dt>[ Member data: returns uint8_t * ] -resp_time_value</p>
<dd>
<dt>[ Member data: returns uint8_t * ] -error_threshold</p>
<dd>
<dt>[ Member : returns void ] delete</p>
<dd> &#8212;- </p>
<p> <i>class sacPortRec</i> </p>
<p> <font SIZE="-1">RID</font> Fields:</p>
<dt>[ Member data: returns ib_net16_t * ] -lid</p>
<dd>
<dt>[ Member data: returns uint8_t * ] -port_num</p>
<dd>
<dt>[ Member data: returns sacPortInfo * ] -port_info</p>
<dd> Methods:</p>
<dt>[ Member : returns char * ] get comp_mask</p>
<dd>
<dt>[ Member : returns char * ] getTable comp_mask</p>
<dd>
<dt>[ Member : returns void ] delete</p>
<dd>
</dl>
<p> <code><font SIZE="-1">SM</font> <font SIZE="-1">INFO</font> <font SIZE="-1">RECORD</font></code> </p>
<dl>
<dt>
<dd> Component mask bits:</dl>
<dl>
<dt>[ Constant : char * ] $IB_SMR_COMPMASK_LID = 0x1</p>
<dd>
<dt>[ Constant : char * ] $IB_SMR_COMPMASK_GUID = 0x2</p>
<dd>
<dt>[ Constant : char * ] $IB_SMR_COMPMASK_SM_KEY = 0x4</p>
<dd>
<dt>[ Constant : char * ] $IB_SMR_COMPMASK_ACT_COUNT = 0x8</p>
<dd>
<dt>[ Constant : int ] $IB_SMR_COMPMASK_STATE = 0x10</p>
<dd>
<dt>[ Constant : int ] $IB_SMR_COMPMASK_PRI = 0x20</p>
<dd> &#8212;- </p>
<p> <i>class sacSmInfo</i> </p>
<p> Fields:</p>
<dt>[ Member data: returns ib_net64_t * ] -guid</p>
<dd>
<dt>[ Member data: returns ib_net64_t * ] -sm_key</p>
<dd>
<dt>[ Member data: returns ib_net32_t * ] -act_count</p>
<dd>
<dt>[ Member data: returns uint8_t * ] -pri_state</p>
<dd>
<dt>[ Member : returns void ] delete</p>
<dd> &#8212;- </p>
<p> <i>class sacSmRec</i> </p>
<p> <font SIZE="-1">RID</font> Fields:</p>
<dt>[ Member data: returns ib_net16_t * ] -lid</p>
<dd>
<dt>[ Member data: returns sacSmInfo * ] -sm_info</p>
<dd> Methods:</p>
<dt>[ Member : returns char * ] get comp_mask</p>
<dd>
<dt>[ Member : returns char * ] getTable comp_mask</p>
<dd>
<dt>[ Member : returns void ] delete</p>
<dd>
</dl>
<p> <code><font SIZE="-1">SWITCH</font> <font SIZE="-1">INFO</font> <font SIZE="-1">RECORD</font></code> </p>
<dl>
<dt>
<dd> Component mask bits:</dl>
<dl>
<dt>[ Constant : char * ] $IB_SWR_COMPMASK_LID = 0x1</p>
<dd>
<dt>[ Constant : char * ] $IB_SWR_COMPMASK_LIN_CAP = 0x2</p>
<dd>
<dt>[ Constant : char * ] $IB_SWR_COMPMASK_RAND_CAP = 0x4</p>
<dd>
<dt>[ Constant : char * ] $IB_SWR_COMPMASK_MCAST_CAP = 0x8</p>
<dd>
<dt>[ Constant : char * ] $IB_SWR_COMPMASK_LIN_TOP = 0x10</p>
<dd>
<dt>[ Constant : char * ] $IB_SWR_COMPMASK_DEF_PORT = 0x20</p>
<dd>
<dt>[ Constant : char * ] $IB_SWR_COMPMASK_DEF_MCAST_PRI = 0x40</p>
<dd>
<dt>[ Constant : char * ] $IB_SWR_COMPMASK_DEF_MCAST_NOT = 0x80</p>
<dd>
<dt>[ Constant : char * ] $IB_SWR_COMPMASK_STATE = 0x100</p>
<dd>
<dt>[ Constant : char * ] $IB_SWR_COMPMASK_LIFE = 0x200</p>
<dd>
<dt>[ Constant : char * ] $IB_SWR_COMPMASK_LMC = 0x400</p>
<dd>
<dt>[ Constant : char * ] $IB_SWR_COMPMASK_ENFORCE_CAP = 0x800</p>
<dd>
<dt>[ Constant : char * ] $IB_SWR_COMPMASK_FLAGS = 0x1000</p>
<dd> &#8212;- </p>
<p> <i>class sacSwInfo</i> </p>
<p> Fields:</p>
<dt>[ Member data: returns ib_net16_t * ] -lin_cap</p>
<dd>
<dt>[ Member data: returns ib_net16_t * ] -rand_cap</p>
<dd>
<dt>[ Member data: returns ib_net16_t * ] -mcast_cap</p>
<dd>
<dt>[ Member data: returns ib_net16_t * ] -lin_top</p>
<dd>
<dt>[ Member data: returns uint8_t * ] -def_port</p>
<dd>
<dt>[ Member data: returns uint8_t * ] -def_mcast_pri_port</p>
<dd>
<dt>[ Member data: returns uint8_t * ] -def_mcast_not_port</p>
<dd>
<dt>[ Member data: returns uint8_t * ] -life_state</p>
<dd>
<dt>[ Member data: returns ib_net16_t * ] -lids_per_port</p>
<dd>
<dt>[ Member data: returns ib_net16_t * ] -enforce_cap</p>
<dd>
<dt>[ Member data: returns uint8_t * ] -flags</p>
<dd>
<dt>[ Member : returns void ] delete</p>
<dd> &#8212;- </p>
<p> <i>class sacSwRec</i> </p>
<p> <font SIZE="-1">RID</font> Fields:</p>
<dt>[ Member data: returns ib_net16_t * ] -lid</p>
<dd>
<dt>[ Member data: returns sacSwInfo * ] -switch_info</p>
<dd> Methods:</p>
<dt>[ Member : returns char * ] get comp_mask</p>
<dd>
<dt>[ Member : returns char * ] getTable comp_mask</p>
<dd>
<dt>[ Member : returns void ] delete</p>
<dd>
</dl>
<p> <code><font SIZE="-1">LINK</font> <font SIZE="-1">RECORD</font></code> </p>
<dl>
<dt>
<dd> Component mask bits:</dl>
<dl>
<dt>[ Constant : int ] $IB_LR_COMPMASK_FROM_LID = 0x1</p>
<dd>
<dt>[ Constant : int ] $IB_LR_COMPMASK_FROM_PORT = 0x2</p>
<dd>
<dt>[ Constant : int ] $IB_LR_COMPMASK_TO_PORT = 0x4</p>
<dd>
<dt>[ Constant : int ] $IB_LR_COMPMASK_TO_LID = 0x8</p>
<dd> &#8212;- </p>
<p> <i>class sacLinkRec</i> </p>
<p> Fields:</p>
<dt>[ Member data: returns ib_net16_t * ] -from_lid</p>
<dd>
<dt>[ Member data: returns uint8_t * ] -from_port_num</p>
<dd>
<dt>[ Member data: returns uint8_t * ] -to_port_num</p>
<dd>
<dt>[ Member data: returns ib_net16_t * ] -to_lid</p>
<dd> Methods:</p>
<dt>[ Member : returns char * ] get comp_mask</p>
<dd>
<dt>[ Member : returns char * ] getTable comp_mask</p>
<dd>
<dt>[ Member : returns void ] delete</p>
<dd>
</dl>
<p> <code><font SIZE="-1">PATH</font> <font SIZE="-1">RECORD</font></code> </p>
<dl>
<dt>
<dd> Component mask bits:</dl>
<dl>
<dt>[ Constant : int ] $IB_PR_COMPMASK_DGID = 0x4</p>
<dd>
<dt>[ Constant : int ] $IB_PR_COMPMASK_SGID = 0x8</p>
<dd>
<dt>[ Constant : int ] $IB_PR_COMPMASK_DLID = 0x10</p>
<dd>
<dt>[ Constant : int ] $IB_PR_COMPMASK_SLID = 0x20</p>
<dd>
<dt>[ Constant : int ] $IB_PR_COMPMASK_RAWTRAFIC = 0x40</p>
<dd>
<dt>[ Constant : int ] $IB_PR_COMPMASK_RESV0 = 0x80</p>
<dd>
<dt>[ Constant : int ] $IB_PR_COMPMASK_FLOWLABEL = 0x100</p>
<dd>
<dt>[ Constant : int ] $IB_PR_COMPMASK_HOPLIMIT = 0x200</p>
<dd>
<dt>[ Constant : int ] $IB_PR_COMPMASK_TCLASS = 0x400</p>
<dd>
<dt>[ Constant : int ] $IB_PR_COMPMASK_REVERSIBLE = 0x800</p>
<dd>
<dt>[ Constant : int ] $IB_PR_COMPMASK_NUMBPATH = 0x1000</p>
<dd>
<dt>[ Constant : int ] $IB_PR_COMPMASK_PKEY = 0x2000</p>
<dd>
<dt>[ Constant : int ] $IB_PR_COMPMASK_RESV1 = 0x4000</p>
<dd>
<dt>[ Constant : int ] $IB_PR_COMPMASK_SL = 0x8000</p>
<dd>
<dt>[ Constant : int ] $IB_PR_COMPMASK_MTUSELEC = 0x10000</p>
<dd>
<dt>[ Constant : int ] $IB_PR_COMPMASK_MTU = 0x20000</p>
<dd>
<dt>[ Constant : int ] $IB_PR_COMPMASK_RATESELEC = 0x40000</p>
<dd>
<dt>[ Constant : int ] $IB_PR_COMPMASK_RATE = 0x80000</p>
<dd>
<dt>[ Constant : int ] $IB_PR_COMPMASK_PKTLIFETIMESELEC = 0x100000</p>
<dd>
<dt>[ Constant : int ] $IB_PR_COMPMASK_PFTLIFETIME = 0x200000</p>
<dd> &#8212;- </p>
<p> <i>class sacPathRec</i> </p>
<p> Fields:</p>
<dt>[ Member data: returns ib_gid_t * ] -dgid</p>
<dd>
<dt>[ Member data: returns ib_gid_t * ] -sgid</p>
<dd>
<dt>[ Member data: returns ib_net16_t * ] -dlid</p>
<dd>
<dt>[ Member data: returns ib_net16_t * ] -slid</p>
<dd>
<dt>[ Member data: returns ib_net32_t * ] -hop_flow_raw</p>
<dd>
<dt>[ Member data: returns uint8_t * ] -tclass</p>
<dd>
<dt>[ Member data: returns uint8_t * ] -num_path</p>
<dd>
<dt>[ Member data: returns ib_net16_t * ] -pkey</p>
<dd>
<dt>[ Member data: returns ib_net16_t * ] -sl</p>
<dd>
<dt>[ Member data: returns uint8_t * ] -mtu</p>
<dd>
<dt>[ Member data: returns uint8_t * ] -rate</p>
<dd>
<dt>[ Member data: returns uint8_t * ] -pkt_life</p>
<dd>
<dt>[ Member data: returns uint8_t * ] -preference</p>
<dd> Methds:</p>
<dt>[ Member : returns char * ] get comp_mask</p>
<dd>
<dt>[ Member : returns char * ] getTable comp_mask</p>
<dd>
<dt>[ Member : returns void ] delete</p>
<dd>
</dl>
<p> <code><font SIZE="-1">LINEAR</font> <font SIZE="-1">FORWARDING</font> <font SIZE="-1">TABLE</font></code> </p>
<dl>
<dt>
<dd> Component mask bits:</dl>
<dl>
<dt>[ Constant : char * ] $IB_LFT_COMPMASK_LID = 0x1</p>
<dd>
<dt>[ Constant : char * ] $IB_LFT_COMPMASK_BLOCK = 0x2</p>
<dd> &#8212;- </p>
<p> <i>class sacLFTRec</i> </p>
<p> Fields:</p>
<dt>[ Member data: returns ib_net16_t * ] -lid</p>
<dd>
<dt>[ Member data: returns ib_net16_t * ] -block_num</p>
<dd>
<dt>[ Member data: returns ib_lft_t * ] -lft</p>
<dd> Methods:</p>
<dt>[ Member : returns char * ] get comp_mask</p>
<dd>
<dt>[ Member : returns char * ] getTable comp_mask</p>
<dd>
<dt>[ Member : returns void ] delete</p>
<dd>
</dl>
<p> <code><font SIZE="-1">MULTICAST</font> <font SIZE="-1">MEMBER</font> <font SIZE="-1">RECORD</font></code> </p>
<dl>
<dt>
<dd> Component mask bits:</dl>
<dl>
<dt>[ Constant : char * ] $IB_MCR_COMPMASK_GID = 0x1</p>
<dd>
<dt>[ Constant : char * ] $IB_MCR_COMPMASK_MGID = 0x1</p>
<dd>
<dt>[ Constant : char * ] $IB_MCR_COMPMASK_PORT_GID = 0x2</p>
<dd>
<dt>[ Constant : char * ] $IB_MCR_COMPMASK_QKEY = 0x4</p>
<dd>
<dt>[ Constant : char * ] $IB_MCR_COMPMASK_MLID = 0x8</p>
<dd>
<dt>[ Constant : char * ] $IB_MCR_COMPMASK_MTU_SEL = 0x10</p>
<dd>
<dt>[ Constant : char * ] $IB_MCR_COMPMASK_MTU = 0x20</p>
<dd>
<dt>[ Constant : char * ] $IB_MCR_COMPMASK_TCLASS = 0x40</p>
<dd>
<dt>[ Constant : char * ] $IB_MCR_COMPMASK_PKEY = 0x80</p>
<dd>
<dt>[ Constant : char * ] $IB_MCR_COMPMASK_RATE_SEL = 0x100</p>
<dd>
<dt>[ Constant : char * ] $IB_MCR_COMPMASK_RATE = 0x200</p>
<dd>
<dt>[ Constant : char * ] $IB_MCR_COMPMASK_LIFE_SEL = 0x400</p>
<dd>
<dt>[ Constant : char * ] $IB_MCR_COMPMASK_LIFE = 0x800</p>
<dd>
<dt>[ Constant : char * ] $IB_MCR_COMPMASK_SL = 0x1000</p>
<dd>
<dt>[ Constant : char * ] $IB_MCR_COMPMASK_FLOW = 0x2000</p>
<dd>
<dt>[ Constant : char * ] $IB_MCR_COMPMASK_HOP = 0x4000</p>
<dd>
<dt>[ Constant : char * ] $IB_MCR_COMPMASK_SCOPE = 0x8000</p>
<dd>
<dt>[ Constant : char * ] $IB_MCR_COMPMASK_JOIN_STATE = 0x10000</p>
<dd>
<dt>[ Constant : char * ] $IB_MCR_COMPMASK_PROXY = 0x20000</p>
<dd> &#8212;- </p>
<p> <i>class sacMCMRec</i> </p>
<p> Fields:</p>
<dt>[ Member data: returns ib_gid_t * ] -mgid</p>
<dd>
<dt>[ Member data: returns ib_gid_t * ] -port_gid</p>
<dd>
<dt>[ Member data: returns ib_net32_t * ] -qkey</p>
<dd>
<dt>[ Member data: returns ib_net16_t * ] -mlid</p>
<dd>
<dt>[ Member data: returns uint8_t * ] -mtu</p>
<dd>
<dt>[ Member data: returns uint8_t * ] -tclass</p>
<dd>
<dt>[ Member data: returns ib_net16_t * ] -pkey</p>
<dd>
<dt>[ Member data: returns uint8_t * ] -rate</p>
<dd>
<dt>[ Member data: returns uint8_t * ] -pkt_life</p>
<dd>
<dt>[ Member data: returns ib_net32_t * ] -sl_flow_hop</p>
<dd>
<dt>[ Member data: returns uint8_t * ] -scope_state</p>
<dd> Methods:</p>
<dt>[ Member : returns char * ] get comp_mask</p>
<dd>
<dt>[ Member : returns char * ] getTable comp_mask</p>
<dd>
<dt>[ Member : returns char * ] set comp_mask</p>
<dd>
<dt>[ Member : returns char * ] del comp_mask</p>
<dd>
<dt>[ Member : returns int ] proxy_join_get</p>
<dd> Instead of simple field cget</p>
<dt>[ Member : returns void ] proxy_join_set proxy_join</p>
<dd> Instead of simple field configure</p>
<dt>[ Member : returns void ] obj_delete</p>
<dd> Delete the object
</dl>
<p> <code><font SIZE="-1">SA</font> <font SIZE="-1">CLASS</font> <font SIZE="-1">PORT</font> <font SIZE="-1">INFO</font></code> </p>
<dl>
<dt>
<dd> &#8212;- </p>
<p> <i>class sacClassPortInfo</i> </p>
<p> Fields:</dl>
<dl>
<dt>[ Member data: returns uint8_t * ] -base_ver</p>
<dd>
<dt>[ Member data: returns uint8_t * ] -class_ver</p>
<dd>
<dt>[ Member data: returns ib_net16_t * ] -cap_mask</p>
<dd>
<dt>[ Member data: returns ib_net32_t * ] -resp_time_val</p>
<dd>
<dt>[ Member data: returns ib_gid_t * ] -redir_gid</p>
<dd>
<dt>[ Member data: returns ib_net32_t * ] -redir_tc_sl_fl</p>
<dd>
<dt>[ Member data: returns ib_net16_t * ] -redir_lid</p>
<dd>
<dt>[ Member data: returns ib_net16_t * ] -redir_pkey</p>
<dd>
<dt>[ Member data: returns ib_net32_t * ] -redir_qp</p>
<dd>
<dt>[ Member data: returns ib_net32_t * ] -redir_qkey</p>
<dd>
<dt>[ Member data: returns ib_gid_t * ] -trap_gid</p>
<dd>
<dt>[ Member data: returns ib_net32_t * ] -trap_tc_sl_fl</p>
<dd>
<dt>[ Member data: returns ib_net16_t * ] -trap_lid</p>
<dd>
<dt>[ Member data: returns ib_net16_t * ] -trap_pkey</p>
<dd>
<dt>[ Member data: returns ib_net32_t * ] -trap_hop_qp</p>
<dd>
<dt>[ Member data: returns ib_net32_t * ] -trap_qkey</p>
<dd> Methods:</p>
<dt>[ Member : returns char * ] get</p>
<dd>
<dt>[ Member : returns void ] delete</p>
<dd>
</dl>
<p> <code><font SIZE="-1">INFORM</font> <font SIZE="-1">INFO</font> <font SIZE="-1">RECORD</font></code> </p>
<dl>
<dt>
<dd> The inform Info is built with heirarchy of objects. So several classes are defined. </p>
<p> &#8212;- </p>
<p> <i>class sacInformInfo</i> </p>
<p> Fields:</dl>
<dl>
<dt>[ Member data: returns ib_gid_t * ] -gid</p>
<dd>
<dt>[ Member data: returns ib_net16_t * ] -lid_range_begin</p>
<dd>
<dt>[ Member data: returns ib_net16_t * ] -lid_range_end</p>
<dd>
<dt>[ Member data: returns ib_net16_t * ] -reserved1</p>
<dd>
<dt>[ Member data: returns uint8_t * ] -is_generic</p>
<dd>
<dt>[ Member data: returns uint8_t * ] -subscribe</p>
<dd>
<dt>[ Member data: returns ib_net16_t * ] -trap_type</p>
<dd>
<dt>[ Member data: returns sacInformInfo_g_or_v * ] -g_or_v</p>
<dd> Methods:</p>
<dt>[ Member : returns char * ] set</p>
<dd>
<dt>[ Member : returns void ] delete</p>
<dd> &#8212;- </p>
<p> <i>class sacInformInfo_g_or_v</i> </p>
<p> Fields:</p>
<dt>[ Member data: returns sacInformInfo_g_or_v_generic * ] -generic</p>
<dd>
<dt>[ Member data: returns sacInformInfo_g_or_v_vend * ] -vend</p>
<dd> &#8212;- </p>
<p> <i>class sacInformInfo_g_or_v_generic</i> </p>
<p> Fields:</p>
<dt>[ Member data: returns ib_net16_t * ] -trap_num</p>
<dd>
<dt>[ Member data: returns ib_net32_t * ] -qpn_resp_time_val</p>
<dd>
<dt>[ Member data: returns uint8_t * ] -reserved2</p>
<dd>
<dt>[ Member data: returns uint8_t * ] -node_type_msb</p>
<dd>
<dt>[ Member data: returns ib_net16_t * ] -node_type_lsb</p>
<dd> &#8212;- </p>
<p> <i>class sacInformInfo_g_or_v_vend</i> </p>
<p> Fields:</p>
<dt>[ Member data: returns ib_net16_t * ] -dev_id</p>
<dd>
<dt>[ Member data: returns ib_net32_t * ] -qpn_resp_time_val</p>
<dd>
<dt>[ Member data: returns uint8_t * ] -reserved2</p>
<dd>
<dt>[ Member data: returns uint8_t * ] -vendor_id_msb</p>
<dd>
<dt>[ Member data: returns ib_net16_t * ] -vendor_id_lsb</p>
<dd>
</dl>
<p> <code><font SIZE="-1">SERVICE</font> <font SIZE="-1">RECORD</font></code> </p>
<dl>
<dt>
<dd> Component mask bits:</dl>
<dl>
<dt>[ Constant : char * ] $IB_SR_COMPMASK_SID = 0x1</p>
<dd>
<dt>[ Constant : char * ] $IB_SR_COMPMASK_SGID = 0x1</p>
<dd>
<dt>[ Constant : char * ] $IB_SR_COMPMASK_SPKEY = 0x2</p>
<dd>
<dt>[ Constant : char * ] $IB_SR_COMPMASK_RES1 = 0x4</p>
<dd>
<dt>[ Constant : char * ] $IB_SR_COMPMASK_SLEASE = 0x8</p>
<dd>
<dt>[ Constant : char * ] $IB_SR_COMPMASK_SKEY = 0x10</p>
<dd>
<dt>[ Constant : char * ] $IB_SR_COMPMASK_SNAME = 0x20</p>
<dd>
<dt>[ Constant : char * ] $IB_SR_COMPMASK_SDATA8_0 = 0x40</p>
<dd>
<dt>[ Constant : char * ] $IB_SR_COMPMASK_SDATA8_1 = 0x80</p>
<dd>
<dt>[ Constant : char * ] $IB_SR_COMPMASK_SDATA8_2 = 0x100</p>
<dd>
<dt>[ Constant : char * ] $IB_SR_COMPMASK_SDATA8_3 = 0x200</p>
<dd>
<dt>[ Constant : char * ] $IB_SR_COMPMASK_SDATA8_4 = 0x400</p>
<dd>
<dt>[ Constant : char * ] $IB_SR_COMPMASK_SDATA8_5 = 0x800</p>
<dd>
<dt>[ Constant : char * ] $IB_SR_COMPMASK_SDATA8_6 = 0x1000</p>
<dd>
<dt>[ Constant : char * ] $IB_SR_COMPMASK_SDATA8_7 = 0x2000</p>
<dd>
<dt>[ Constant : char * ] $IB_SR_COMPMASK_SDATA8_8 = 0x4000</p>
<dd>
<dt>[ Constant : char * ] $IB_SR_COMPMASK_SDATA8_9 = 0x8000</p>
<dd>
<dt>[ Constant : char * ] $IB_SR_COMPMASK_SDATA8_10 = 0x10000</p>
<dd>
<dt>[ Constant : char * ] $IB_SR_COMPMASK_SDATA8_11 = 0x20000</p>
<dd>
<dt>[ Constant : char * ] $IB_SR_COMPMASK_SDATA8_12 = 0x40000</p>
<dd>
<dt>[ Constant : char * ] $IB_SR_COMPMASK_SDATA8_13 = 0x80000</p>
<dd>
<dt>[ Constant : char * ] $IB_SR_COMPMASK_SDATA8_14 = 0x100000</p>
<dd>
<dt>[ Constant : char * ] $IB_SR_COMPMASK_SDATA8_15 = 0x200000</p>
<dd>
<dt>[ Constant : char * ] $IB_SR_COMPMASK_SDATA16_0 = 0x400000</p>
<dd>
<dt>[ Constant : char * ] $IB_SR_COMPMASK_SDATA16_1 = 0x800000</p>
<dd>
<dt>[ Constant : char * ] $IB_SR_COMPMASK_SDATA16_2 = 0x1000000</p>
<dd>
<dt>[ Constant : char * ] $IB_SR_COMPMASK_SDATA16_3 = 0x2000000</p>
<dd>
<dt>[ Constant : char * ] $IB_SR_COMPMASK_SDATA16_4 = 0x4000000</p>
<dd>
<dt>[ Constant : char * ] $IB_SR_COMPMASK_SDATA16_5 = 0x8000000</p>
<dd>
<dt>[ Constant : char * ] $IB_SR_COMPMASK_SDATA16_6 = 0x10000000</p>
<dd>
<dt>[ Constant : char * ] $IB_SR_COMPMASK_SDATA16_7 = 0x20000000</p>
<dd>
<dt>[ Constant : char * ] $IB_SR_COMPMASK_SDATA32_0 = 0x40000000</p>
<dd>
<dt>[ Constant : char * ] $IB_SR_COMPMASK_SDATA32_1 = 0x80000000</p>
<dd>
<dt>[ Constant : char * ] $IB_SR_COMPMASK_SDATA32_2 = 0x100000000</p>
<dd>
<dt>[ Constant : char * ] $IB_SR_COMPMASK_SDATA32_3 = 0x200000000</p>
<dd>
<dt>[ Constant : char * ] $IB_SR_COMPMASK_SDATA64_0 = 0x400000000</p>
<dd>
<dt>[ Constant : char * ] $IB_SR_COMPMASK_SDATA64_1 = 0x800000000</p>
<dd> &#8212;- </p>
<p> <i>class sacServiceRec</i> </p>
<p> Fields:</p>
<dt>[ Member data: returns ib_net64_t * ] -service_id</p>
<dd>
<dt>[ Member data: returns ib_gid_t * ] -service_gid</p>
<dd>
<dt>[ Member data: returns ib_net16_t * ] -service_pkey</p>
<dd>
<dt>[ Member data: returns ib_net16_t * ] -resv</p>
<dd>
<dt>[ Member data: returns ib_net32_t * ] -service_lease</p>
<dd>
<dt>[ Member data: returns uint8_array_t * ] -service_key</p>
<dd>
<dt>[ Member data: returns ib_svc_name_t * ] -service_name</p>
<dd>
<dt>[ Member data: returns uint8_array_t * ] -service_data8</p>
<dd>
<dt>[ Member data: returns ib_net16_array_t * ] -service_data16</p>
<dd>
<dt>[ Member data: returns ib_net32_array_t * ] -service_data32</p>
<dd>
<dt>[ Member data: returns ib_net64_array_t * ] -service_data64</p>
<dd> Methods:</p>
<dt>[ Member : returns char * ] get comp_mask</p>
<dd>
<dt>[ Member : returns char * ] set comp_mask</p>
<dd>
<dt>[ Member : returns char * ] getTable comp_mask</p>
<dd>
<dt>[ Member : returns char * ] delete comp_mask</p>
<dd>
<dt>[ Member : returns void ] obj_delete</p>
<dd>
</dl>
<p> <code><font SIZE="-1">SL</font> to <font SIZE="-1">VL</font> <font SIZE="-1">TABLE</font> <font SIZE="-1">RECORD</font></code> </p>
<dl>
<dt>
<dd> Component mask bits:</dl>
<dl>
<dt>[ Constant : char * ] $IB_SLVL_COMPMASK_LID = 0x1</p>
<dd>
<dt>[ Constant : char * ] $IB_SLVL_COMPMASK_IN_PORT = 0x2</p>
<dd>
<dt>[ Constant : char * ] $IB_SLVL_COMPMASK_OUT_PORT = 0x4</p>
<dd> &#8212;- </p>
<p> <i>class sacSlVlTbl</i></p>
<dt>[ Member data: returns uint8_array_t * ] -raw_vl_by_sl</p>
<dd> &#8212;- </p>
<p> <i>class sacSlVlRec</i> </p>
<p> <font SIZE="-1">RID</font> Fields:</p>
<dt>[ Member data: returns ib_net16_t * ] -lid</p>
<dd> for <font SIZE="-1">CA:</font> lid of port, for switch lid of port 0</p>
<dt>[ Member data: returns uint8_t * ] -in_port_num</p>
<dd> reserved for <font SIZE="-1">CA</font>&#8216;s</p>
<dt>[ Member data: returns uint8_t * ] -out_port_num</p>
<dd> reserved for <font SIZE="-1">CA</font>&#8216;s</p>
<dt>[ Member data: returns uint32_t * ] -resv</p>
<dd>
<dt>[ Member data: returns sacSlVlTbl * ] -slvl_tbl</p>
<dd> Methods:</p>
<dt>[ Member : returns char * ] get comp_mask</p>
<dd>
<dt>[ Member : returns char * ] getTable comp_mask</p>
<dd>
<dt>[ Member : returns void ] delete</p>
<dd>
</dl>
<p> <code><font SIZE="-1">VL</font> <font SIZE="-1">ARBITRATION</font> <font SIZE="-1">TABLE</font> <font SIZE="-1">RECORD</font></code> </p>
<dl>
<dt>
<dd> Component mask bits:</dl>
<dl>
<dt>[ Constant : char * ] $IB_VLA_COMPMASK_LID = 0x1</p>
<dd>
<dt>[ Constant : char * ] $IB_VLA_COMPMASK_OUT_PORT = 0x2</p>
<dd>
<dt>[ Constant : char * ] $IB_VLA_COMPMASK_BLOCK = 0x4</p>
<dd> &#8212;- </p>
<p> <i>class sacVlArbRec</i> </p>
<p> Fields:</p>
<dt>[ Member data: returns ib_net16_t * ] -lid</p>
<dd> for <font SIZE="-1">CA:</font> lid of port, for switch lid of port 0</p>
<dt>[ Member data: returns uint8_t * ] -port_num</p>
<dd>
<dt>[ Member data: returns uint8_t * ] -block_num</p>
<dd>
<dt>[ Member data: returns uint32_t * ] -reserved</p>
<dd>
<dt>[ Member data: returns sac_vl_arb_tbl_t * ] -vl_arb_tbl</p>
<dd> Methods:</p>
<dt>[ Member : returns char * ] get comp_mask</p>
<dd>
<dt>[ Member : returns char * ] getTable comp_mask</p>
<dd>
<dt>[ Member : returns void ] delete</p>
<dd>
</dl>
<p> <code><font SIZE="-1">PKEY</font> <font SIZE="-1">TABLE</font> <font SIZE="-1">RECORD</font></code> </p>
<dl>
<dt>
<dd> Component mask bits:</dl>
<dl>
<dt>[ Constant : char * ] $IB_PKEY_COMPMASK_LID = 0x1</p>
<dd>
<dt>[ Constant : char * ] $IB_PKEY_COMPMASK_BLOCK = 0x2</p>
<dd>
<dt>[ Constant : char * ] $IB_PKEY_COMPMASK_PORT = 0x4</p>
<dd> &#8212;- </p>
<p> <i>class sacPKeyTbl</i> </p>
<p> Fields:</p>
<dt>[ Member data: returns ib_net16_array_t * ] -pkey_entry</p>
<dd> &#8212;- </p>
<p> <i>class sacPKeyRec</i> </p>
<p> <font SIZE="-1">RID</font> Fields:</p>
<dt>[ Member data: returns ib_net16_t * ] -lid</p>
<dd> for <font SIZE="-1">CA:</font> lid of port, for switch lid of port 0</p>
<dt>[ Member data: returns uint16_t * ] -block_num</p>
<dd>
<dt>[ Member data: returns uint8_t * ] -port_num</p>
<dd> for switch: port number, for <font SIZE="-1">CA:</font> reserved</p>
<dt>[ Member data: returns uint8_t * ] -reserved1</p>
<dd>
<dt>[ Member data: returns uint16_t * ] -reserved2</p>
<dd>
<dt>[ Member data: returns sacPKeyTbl * ] -pkey_tbl</p>
<dd> Methods:</p>
<dt>[ Member : returns char * ] get comp_mask</p>
<dd>
<dt>[ Member : returns char * ] getTable comp_mask</p>
<dd>
<dt>[ Member : returns void ] delete</p>
<dd></dl>
<h2>Subnet Management MADs (SMPs)</h2>
<p> The <font SIZE="-1">SM</font> interface supports sending Subnet Management Packets to the fabric devices. The specific attributes that can be access is provided in detail in each sub section below. </p>
<p> A set of object types is defined. The user can allocate a new attribute object. Then the object can be set using configure or the direct manipulation methods. Extra methods are provided for each object: =item setByDr &lt;dr&gt; &lt;attrMod&gt; </p>
<p> Set the attribute on the object accessible by the given directed route. A directed route is a list of port numbers to go out from.</p>
<dl>
<dt>getByDr &lt;dr&gt; &lt;attrMod&gt;</p>
<dd> Get the attribute value by traversing a directed route. </p>
<p> setByLid &lt;lid&gt; &lt;attrMod&gt; </p>
<p> Set the attribute on the object accessible by the given <font SIZE="-1">LID</font> </p>
<p> getByLid &lt;lid&gt; &lt;attrMod&gt; </p>
<p> get the attribute on the object accessible by the given <font SIZE="-1">LID</font>
</dl>
<p> <code>class smNodeInfo</code> </p>
<dl>
<dt>
<dd> Fields:</dl>
<dl>
<dt>[ Member data: returns uint8_t * ] -base_version</p>
<dd>
<dt>[ Member data: returns uint8_t * ] -class_version</p>
<dd>
<dt>[ Member data: returns uint8_t * ] -node_type</p>
<dd>
<dt>[ Member data: returns uint8_t * ] -num_ports</p>
<dd>
<dt>[ Member data: returns ib_net64_t * ] -sys_guid</p>
<dd>
<dt>[ Member data: returns ib_net64_t * ] -node_guid</p>
<dd>
<dt>[ Member data: returns ib_net64_t * ] -port_guid</p>
<dd>
<dt>[ Member data: returns ib_net16_t * ] -partition_cap</p>
<dd>
<dt>[ Member data: returns ib_net16_t * ] -device_id</p>
<dd>
<dt>[ Member data: returns ib_net32_t * ] -revision</p>
<dd>
<dt>[ Member data: returns ib_net32_t * ] -port_num_vendor_id</p>
<dd> Methods:</p>
<dt>[ Member : returns int ] getByDr dr</p>
<dd>
<dt>[ Member : returns int ] setByDr dr</p>
<dd>
<dt>[ Member : returns int ] getByLid lid</p>
<dd>
<dt>[ Member : returns int ] setByLid lid</p>
<dd></dl>
<h2>class smPortInfo</h2>
<p> Fields:</p>
<dl>
<dt>[ Member data: returns ib_net64_t * ] -m_key</p>
<dd>
<dt>[ Member data: returns ib_net64_t * ] -subnet_prefix</p>
<dd>
<dt>[ Member data: returns ib_net16_t * ] -base_lid</p>
<dd>
<dt>[ Member data: returns ib_net16_t * ] -master_sm_base_lid</p>
<dd>
<dt>[ Member data: returns ib_net32_t * ] -capability_mask</p>
<dd>
<dt>[ Member data: returns ib_net16_t * ] -diag_code</p>
<dd>
<dt>[ Member data: returns ib_net16_t * ] -m_key_lease_period</p>
<dd>
<dt>[ Member data: returns uint8_t * ] -local_port_num</p>
<dd>
<dt>[ Member data: returns uint8_t * ] -link_width_enabled</p>
<dd>
<dt>[ Member data: returns uint8_t * ] -link_width_supported</p>
<dd>
<dt>[ Member data: returns uint8_t * ] -link_width_active</p>
<dd>
<dt>[ Member data: returns uint8_t * ] -state_info1</p>
<dd> LinkSpeedSupported and PortState</p>
<dt>[ Member data: returns uint8_t * ] -state_info2</p>
<dd> PortPhysState and LinkDownDefaultState</p>
<dt>[ Member data: returns uint8_t * ] -mkey_lmc</p>
<dd>
<dt>[ Member data: returns uint8_t * ] -link_speed</p>
<dd> LinkSpeedEnabled and LinkSpeedActive</p>
<dt>[ Member data: returns uint8_t * ] -mtu_smsl</p>
<dd>
<dt>[ Member data: returns uint8_t * ] -vl_cap</p>
<dd> VlCap and InitType</p>
<dt>[ Member data: returns uint8_t * ] -vl_high_limit</p>
<dd>
<dt>[ Member data: returns uint8_t * ] -vl_arb_high_cap</p>
<dd>
<dt>[ Member data: returns uint8_t * ] -vl_arb_low_cap</p>
<dd>
<dt>[ Member data: returns uint8_t * ] -mtu_cap</p>
<dd>
<dt>[ Member data: returns uint8_t * ] -vl_stall_life</p>
<dd>
<dt>[ Member data: returns uint8_t * ] -vl_enforce</p>
<dd>
<dt>[ Member data: returns ib_net16_t * ] -m_key_violations</p>
<dd>
<dt>[ Member data: returns ib_net16_t * ] -p_key_violations</p>
<dd>
<dt>[ Member data: returns ib_net16_t * ] -q_key_violations</p>
<dd>
<dt>[ Member data: returns uint8_t * ] -guid_cap</p>
<dd>
<dt>[ Member data: returns uint8_t * ] -subnet_timeout</p>
<dd>
<dt>[ Member data: returns uint8_t * ] -resp_time_value</p>
<dd>
<dt>[ Member data: returns uint8_t * ] -error_threshold</p>
<dd> Methods:</p>
<dt>[ Member : returns int ] getByDr dr portNum</p>
<dd>
<dt>[ Member : returns int ] setByDr dr portNum</p>
<dd>
<dt>[ Member : returns int ] getByLid lid portNum</p>
<dd>
<dt>[ Member : returns int ] setByLid lid portNum</p>
<dd>
</dl>
<p> <code>class smSwInfo</code> </p>
<dl>
<dt>[ Member data: returns ib_net16_t * ] -lin_cap</p>
<dd>
<dt>[ Member data: returns ib_net16_t * ] -rand_cap</p>
<dd>
<dt>[ Member data: returns ib_net16_t * ] -mcast_cap</p>
<dd>
<dt>[ Member data: returns ib_net16_t * ] -lin_top</p>
<dd>
<dt>[ Member data: returns uint8_t * ] -def_port</p>
<dd>
<dt>[ Member data: returns uint8_t * ] -def_mcast_pri_port</p>
<dd>
<dt>[ Member data: returns uint8_t * ] -def_mcast_not_port</p>
<dd>
<dt>[ Member data: returns uint8_t * ] -life_state</p>
<dd>
<dt>[ Member data: returns ib_net16_t * ] -lids_per_port</p>
<dd>
<dt>[ Member data: returns ib_net16_t * ] -enforce_cap</p>
<dd>
<dt>[ Member data: returns uint8_t * ] -flags</p>
<dd>
<dt>[ Member : returns int ] getByDr dr</p>
<dd>
<dt>[ Member : returns int ] setByDr dr</p>
<dd>
<dt>[ Member : returns int ] getByLid lid</p>
<dd>
<dt>[ Member : returns int ] setByLid lid</p>
<dd>
</dl>
<p> <code>class smLftBlock</code> </p>
<dl>
<dt>[ Member data: returns uint8_array_t * ] -lft</p>
<dd>
<dt>[ Member : returns int ] getByDr dr blockNum</p>
<dd>
<dt>[ Member : returns int ] setByDr dr blockNum</p>
<dd>
<dt>[ Member : returns int ] getByLid lid blockNum</p>
<dd>
<dt>[ Member : returns int ] setByLid lid blockNum</p>
<dd>
</dl>
<p> <code>class smMftBlock</code> </p>
<dl>
<dt>[ Member data: returns ib_net16_array_t * ] -mft</p>
<dd>
<dt>[ Member : returns int ] getByDr dr startLid startPort</p>
<dd>
<dt>[ Member : returns int ] setByDr dr startLid startPort</p>
<dd>
<dt>[ Member : returns int ] getByLid lid startLid startPort</p>
<dd>
<dt>[ Member : returns int ] setByLid lid startLid startPort</p>
<dd>
</dl>
<p> <code>class smGuidInfo</code> </p>
<dl>
<dt>[ Member data: returns ib_net64_array_t * ] -guid</p>
<dd>
<dt>[ Member : returns int ] getByDr dr blockNum</p>
<dd>
<dt>[ Member : returns int ] setByDr dr blockNum</p>
<dd>
<dt>[ Member : returns int ] getByLid lid blockNum</p>
<dd>
<dt>[ Member : returns int ] setByLid lid blockNum</p>
<dd>
</dl>
<p> <code>class smPkeyTable</code> </p>
<dl>
<dt>[ Member data: returns ib_net16_array_t * ] -pkey_entry</p>
<dd>
<dt>[ Member : returns int ] getByDr dr portNum blockNum</p>
<dd>
<dt>[ Member : returns int ] setByDr dr portNum blockNum</p>
<dd>
<dt>[ Member : returns int ] getByLid lid portNum blockNum</p>
<dd>
<dt>[ Member : returns int ] setByLid lid portNum blockNum</p>
<dd>
</dl>
<p> <code>class smSlVlTable</code> </p>
<dl>
<dt>[ Member data: returns uint8_array_t * ] -raw_vl_by_sl</p>
<dd>
<dt>[ Member : returns int ] getByDr dr inPortNum outPortNum</p>
<dd>
<dt>[ Member : returns int ] setByDr dr inPortNum outPortNum</p>
<dd>
<dt>[ Member : returns int ] getByLid lid inPortNum outPortNum</p>
<dd>
<dt>[ Member : returns int ] setByLid lid inPortNum outPortNum</p>
<dd>
</dl>
<p> <code>class smVlArbTable</code> </p>
<dl>
<dt>[ Member data: returns ib_vl_arb_element_t * ] -vl_entry</p>
<dd>
<dt>[ Member : returns int ] getByDr dr portNum block</p>
<dd>
<dt>[ Member : returns int ] setByDr dr portNum block</p>
<dd>
<dt>[ Member : returns int ] getByLid lid portNum block</p>
<dd>
<dt>[ Member : returns int ] setByLid lid portNum block</p>
<dd>
</dl>
<p> <code>class smNodeDesc</code> </p>
<dl>
<dt>[ Member data: returns ibsm_node_desc_str_t * ] -description</p>
<dd>
<dt>[ Member : returns int ] getByDr dr</p>
<dd>
<dt>[ Member : returns int ] setByDr dr</p>
<dd>
<dt>[ Member : returns int ] getByLid lid</p>
<dd>
<dt>[ Member : returns int ] setByLid lid</p>
<dd>
</dl>
<p> <code>class smSMInfo</code> </p>
<dl>
<dt>[ Member data: returns ib_net64_t * ] -guid</p>
<dd>
<dt>[ Member data: returns ib_net64_t * ] -sm_key</p>
<dd>
<dt>[ Member data: returns ib_net32_t * ] -act_count</p>
<dd>
<dt>[ Member data: returns uint8_t * ] -pri_state</p>
<dd>
<dt>[ Member : returns int ] getByDr dr</p>
<dd>
<dt>[ Member : returns int ] setByDr dr</p>
<dd>
<dt>[ Member : returns int ] getByLid lid</p>
<dd>
<dt>[ Member : returns int ] setByLid lid</p>
<dd>
</dl>
<p> <code>class smNotice</code> </p>
<dl>
<dt>
<dd> The <font SIZE="-1">NOTICE</font> attribute is built out of several sub objects</dl>
<dl>
<dt>[ Member data: returns uint8_t * ] -generic_type</p>
<dd>
<dt>[ Member data: returns ib_net16_t * ] -issuer_lid</p>
<dd>
<dt>[ Member data: returns ib_net16_t * ] -toggle_count</p>
<dd>
<dt>[ Member data: returns ib_gid_t * ] -issuer_gid</p>
<dd>
<dt>[ Member data: returns smNotice_g_or_v * ] -g_or_v</p>
<dd>
<dt>[ Member data: returns smNotice_data_details * ] -data_details</p>
<dd>
<dt>[ Member : returns int ] trapByDr dr</p>
<dd>
<dt>[ Member : returns int ] trapByLid lid</p>
<dd> &#8212;- </p>
<p> <i>class smNotice_g_or_v</i></p>
<dt>[ Member data: returns smNotice_g_or_v_generic * ] -generic</p>
<dd>
<dt>[ Member data: returns smNotice_g_or_v_vend * ] -vend</p>
<dd> &#8212;- </p>
<p> <i>class smNotice_data_details</i></p>
<dt>[ Member data: returns smNotice_data_details_raw_data * ] -raw_data</p>
<dd>
<dt>[ Member data: returns smNotice_data_details_ntc_64_67 * ] -ntc_64_67</p>
<dd>
<dt>[ Member data: returns smNotice_data_details_ntc_128 * ] -ntc_128</p>
<dd>
<dt>[ Member data: returns smNotice_data_details_ntc_129_131 * ] -ntc_129_131</p>
<dd>
<dt>[ Member data: returns smNotice_data_details_ntc_144 * ] -ntc_144</p>
<dd>
<dt>[ Member data: returns smNotice_data_details_ntc_145 * ] -ntc_145</p>
<dd>
<dt>[ Member data: returns smNotice_data_details_ntc_256 * ] -ntc_256</p>
<dd>
<dt>[ Member data: returns smNotice_data_details_ntc_257_258 * ] -ntc_257_258</p>
<dd>
<dt>[ Member data: returns smNotice_data_details_ntc_259 * ] -ntc_259</p>
<dd> &#8212;- </p>
<p> <i>class smNotice_g_or_v_generic</i></p>
<dt>[ Member data: returns uint8_t * ] -prod_type_msb</p>
<dd>
<dt>[ Member data: returns ib_net16_t * ] -prod_type_lsb</p>
<dd>
<dt>[ Member data: returns ib_net16_t * ] -trap_num</p>
<dd> &#8212;- </p>
<p> <i>class smNotice_g_or_v_vend</i></p>
<dt>[ Member data: returns uint8_t * ] -vend_id_msb</p>
<dd>
<dt>[ Member data: returns ib_net16_t * ] -vend_id_lsb</p>
<dd>
<dt>[ Member data: returns ib_net16_t * ] -dev_id</p>
<dd> &#8212;- </p>
<p> <i>class smNotice_data_details_raw_data</i></p>
<dt>[ Member data: returns uint8_array_t * ] -details</p>
<dd> &#8212;- </p>
<p> <i>class smNotice_data_details_ntc_64_67</i></p>
<dt>[ Member data: returns uint8_array_t * ] -res</p>
<dd>
<dt>[ Member data: returns ib_gid_t * ] -gid</p>
<dd> the Node or Multicast Group that came in/out </p>
<p> &#8212;- </p>
<p> <i>class smNotice_data_details_ntc_128</i></p>
<dt>[ Member data: returns ib_net16_t * ] -sw_lid</p>
<dd> the sw lid of which link state changed </p>
<p> &#8212;- </p>
<p> <i>class smNotice_data_details_ntc_129_131</i></p>
<dt>[ Member data: returns ib_net16_t * ] -pad</p>
<dd>
<dt>[ Member data: returns ib_net16_t * ] -lid</p>
<dd> lid and port number of the violation</p>
<dt>[ Member data: returns uint8_t * ] -port_num</p>
<dd> &#8212;- </p>
<p> <i>class smNotice_data_details_ntc_144</i></p>
<dt>[ Member data: returns ib_net16_t * ] -pad1</p>
<dd>
<dt>[ Member data: returns ib_net16_t * ] -lid</p>
<dd> lid where capability mask changed</p>
<dt>[ Member data: returns ib_net16_t * ] -pad2</p>
<dd>
<dt>[ Member data: returns ib_net32_t * ] -new_cap_mask</p>
<dd> new capability mask </p>
<p> &#8212;- </p>
<p> <i>class smNotice_data_details_ntc_145</i></p>
<dt>[ Member data: returns ib_net16_t * ] -pad1</p>
<dd>
<dt>[ Member data: returns ib_net16_t * ] -lid</p>
<dd> lid where sys guid changed</p>
<dt>[ Member data: returns ib_net16_t * ] -pad2</p>
<dd>
<dt>[ Member data: returns ib_net64_t * ] -new_sys_guid</p>
<dd> new system image guid </p>
<p> &#8212;- </p>
<p> <i>class smNotice_data_details_ntc_256</i></p>
<dt>[ Member data: returns ib_net16_t * ] -pad1</p>
<dd>
<dt>[ Member data: returns ib_net16_t * ] -lid</p>
<dd>
<dt>[ Member data: returns ib_net16_t * ] -pad2</p>
<dd>
<dt>[ Member data: returns uint8_t * ] -method</p>
<dd>
<dt>[ Member data: returns uint8_t * ] -pad3</p>
<dd>
<dt>[ Member data: returns ib_net16_t * ] -attr_id</p>
<dd>
<dt>[ Member data: returns ib_net32_t * ] -attr_mod</p>
<dd>
<dt>[ Member data: returns ib_net64_t * ] -mkey</p>
<dd>
<dt>[ Member data: returns uint8_t * ] -dr_slid</p>
<dd>
<dt>[ Member data: returns uint8_t * ] -dr_trunc_hop</p>
<dd>
<dt>[ Member data: returns uint8_array_t * ] -dr_rtn_path</p>
<dd> &#8212;- </p>
<p> <i>class smNotice_data_details_ntc_257_258</i></p>
<dt>[ Member data: returns ib_net16_t * ] -pad1</p>
<dd>
<dt>[ Member data: returns ib_net16_t * ] -lid1</p>
<dd>
<dt>[ Member data: returns ib_net16_t * ] -lid2</p>
<dd>
<dt>[ Member data: returns ib_net32_t * ] -key</p>
<dd>
<dt>[ Member data: returns uint8_t * ] -sl</p>
<dd>
<dt>[ Member data: returns ib_net32_t * ] -qp1</p>
<dd>
<dt>[ Member data: returns ib_net32_t * ] -qp2</p>
<dd>
<dt>[ Member data: returns ib_gid_t * ] -gid1</p>
<dd>
<dt>[ Member data: returns ib_gid_t * ] -gid2</p>
<dd> &#8212;- </p>
<p> <i>class smNotice_data_details_ntc_259</i></p>
<dt>[ Member data: returns ib_net16_t * ] -data_valid</p>
<dd>
<dt>[ Member data: returns ib_net16_t * ] -lid1</p>
<dd>
<dt>[ Member data: returns ib_net16_t * ] -lid2</p>
<dd>
<dt>[ Member data: returns ib_net32_t * ] -key</p>
<dd>
<dt>[ Member data: returns uint8_t * ] -sl</p>
<dd>
<dt>[ Member data: returns ib_net32_t * ] -qp1</p>
<dd>
<dt>[ Member data: returns uint8_t * ] -qp2_msb</p>
<dd>
<dt>[ Member data: returns ib_net16_t * ] -qp2_lsb</p>
<dd>
<dt>[ Member data: returns ib_gid_t * ] -gid1</p>
<dd>
<dt>[ Member data: returns ib_gid_t * ] -gid2</p>
<dd>
<dt>[ Member data: returns ib_net16_t * ] -sw_lid</p>
<dd>
<dt>[ Member data: returns uint8_t * ] -port_no</p>
<dd></dl>
<h2>IBCR Functions</h2>
<p> Provides vendor specific access to the device internal coniguration space </p>
<p> This section provide the details about the functions <font SIZE="-1">IBCR</font> exposes. They all return 0 on succes.</p>
<dl>
<dt>[ returns int ] crMultiMaxGet</p>
<dd>
<dt>[ returns int ] crRead lid address</p>
<dd>
<dt>[ returns int ] crWrite lid data address</p>
<dd>
<dt>[ returns int ] crReadMulti num lid_list address</p>
<dd>
<dt>[ returns int ] crWriteMulti num lid_list data address</p>
<dd></dl>
<h2>IB Vendor Specific Functions</h2>
<p> <font SIZE="-1">IBVS</font> stands for Vendor Specific MADs. </p>
<p> This section provide the details about the functions <font SIZE="-1">IBVS</font> exposes. They all return 0 on succes.</p>
<dl>
<dt>[ returns int ] vsMultiMaxGet</p>
<dd>
<dt>[ returns int ] vsCpuRead lid size cpu_traget_size address</p>
<dd>
<dt>[ returns int ] vsCpuWrite lid size cpu_traget_size data address</p>
<dd>
<dt>[ returns int ] vsI2cRead lid port_num device_id size address</p>
<dd>
<dt>[ returns int ] vsI2cWrite lid port_num device_id size address data</p>
<dd>
<dt>[ returns int ] vsI2cReadMulti num lid_list port_num device_id size address</p>
<dd>
<dt>[ returns int ] vsI2cWriteMulti num lid_list port_num device_id size address data</p>
<dd>
<dt>[ returns int ] vsGpioRead lid</p>
<dd>
<dt>[ returns int ] vsGpioWrite lid gpio_mask gpio_data</p>
<dd>
<dt>[ returns int ] vsSWReset num lid_list</p>
<dd>
<dt>[ returns int ] vsFlashStartMulti num lid_list last size address data</p>
<dd>
<dt>[ returns int ] vsFlashStopMulti num lid_list force</p>
<dd>
<dt>[ returns int ] vsFlashSetBankMulti num lid_list address</p>
<dd>
<dt>[ returns int ] vsFlashEraseSectorMulti num lid_list address</p>
<dd>
<dt>[ returns int ] vsFlashReadSectorMulti num lid_list size address</p>
<dd>
<dt>[ returns int ] vsFlashWriteSectorMulti num lid_list size address data</p>
<dd>
<dt>[ returns int ] vsMirrorRead lid</p>
<dd>
<dt>[ returns int ] vsMirrorWrite lid rx_mirror tx_mirror</p>
<dd></dl>
<h2>IBBBM Functions</h2>
<p> This section provide the details about the functions <font SIZE="-1">IBBBM</font> exposes. They all return 0 on succes.</p>
<dl>
<dt>[ returns int ] bbmVpdRead lid vpd_device_selector bytes_num offset</p>
<dd>
<dt>[ returns int ] bbmVpdWrite lid vpd_device_selector bytes_num offset p_data</p>
<dd>
<dt>[ returns int ] bbmVSDRead lid</p>
<dd>
<dt>[ returns int ] bbmBSNRead lid</p>
<dd>
<dt>[ returns int ] bbmModRead lid</p>
<dd>
<dt>[ returns int ] bbmChaRead lid</p>
<dd>
<dt>[ returns int ] bbmFWVerRead lid</p>
<dd></dl>
<h2>AUTHOR</h2>
<p> Eitan Zahavi, Mellanox Technologies <font SIZE="-1">LTD</font>, eitan [at] mellanox.co.il </p>
<h2>Index</h2>
