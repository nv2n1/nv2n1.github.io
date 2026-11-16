---
title: "ibmssh(1)"
name: "ibmssh"
section: "1"
letter: "i"
url: "/docs/linux/man/1-ibmssh/"
description: "ibmssh IB MANAGEMENT SIMULATOR – Extentended TCL shell"
---

<h2>NAME</h2>
<p> <code>ibmssh</code> IB MANAGEMENT SIMULATOR &#8211; Extentended TCL shell</p>
<h2>DESCRIPTION</h2>
<p> <code>ibmssh</code> is a <font SIZE="-1">TCL</font> shell extended with interface for the <font SIZE="-1">IB</font> Management Simulator facilities. Normally you will not run this shell directly &#8211; but instead it will be invoked by the <code>IBMgtSim</code> utility. However, in order to write simulation flows that interacts closely with the simulated model, a simulation flow should be provided. This flow is loaded by IBMgtSim and excersize the <font SIZE="-1">API</font> provided by this shell. </p>
<p> The following sub sections provide detailed definition for those objects and <font SIZE="-1">API</font>.</p>
<h2>IBMgtSim Constants</h2>
<p> These constants are provided by IBMgtSim </p>
<p> <code>Massage Manager Log Verbosity Flags</code> </p>
<dl>
<dt>[ Constant : int ] $MsgShowFatal = 0x01</dt>
<dd>
</dd><dt>[ Constant : int ] $MsgShowError = 0x02</dt>
<dd>
</dd><dt>[ Constant : int ] $MsgShowWarning = 0x04</dt>
<dd>
</dd><dt>[ Constant : int ] $MsgShowInfo = 0x08</dt>
<dd>
</dd><dt>[ Constant : int ] $MsgShowVerbose = 0x10</dt>
<dd>
</dd><dt>[ Constant : int ] $MsgShowContext = 0x20</dt>
<dd>
</dd><dt>[ Constant : int ] $MsgShowSource = 0x40</dt>
<dd>
</dd><dt>[ Constant : int ] $MsgShowTime = 0x80</dt>
<dd>
</dd><dt>[ Constant : int ] $MsgShowModule = 0x100</dt>
<dd>
</dd><dt>[ Constant : int ] $MsgShowMads = 0x200</dt>
<dd>
</dd><dt>[ Constant : int ] $MsgShowFrames = 0x400</dt>
<dd>
</dd><dt>[ Constant : int ] $MsgShowAll = 0xffff</dt>
<dd>
</dd><dt>[ Constant : int ] $MsgDefault = 0x62f</dt>
<dd></dd></dl>
<h2>Message Manager Objects</h2>
<p> <code>class msgManager</code> </p>
<dl>
<dt>
</dt><dd> This is the Message Manager class</dd></dl>
<dl>
<dt>[ Member : returns int ] getVerbLevel ?module?</dt>
<dd>
</dd><dt>[ Member : returns int ] clrVerbLevel ?module?</dt>
<dd>
</dd><dt>[ Member : returns void ] setVerbLevel vl ?module?</dt>
<dd>
</dd><dt>[ Member : returns int ] outstandingMsgCount ?vl?</dt>
<dd>
</dd><dt>[ Member : returns string ] outstandingMsgs ?vl?</dt>
<dd>
</dd><dt>[ Member : returns string ] getNextMessage</dt>
<dd>
</dd><dt>[ Member : returns void ] nullOutstandingMsgs</dt>
<dd>
</dd><dt>[ Member : returns int ] setLogFile fileName</dt>
<dd></dd></dl>
<h2>Random Manager Functions</h2>
<dl>
<dt>[ returns float ] rmRand</dt>
<dd> obtain a random number in the range 0.0 &#8211; 1.0</dd>
<dt>[ returns int ] rmSeed seed</dt>
<dd> initialize the seed for the random manager
</dd></dl>
<p> <code>class ib_node_info_t</code> </p>
<dl>
<dt>[ Member data: returns uint8_t * ] -base_version</dt>
<dd>
</dd><dt>[ Member data: returns uint8_t * ] -class_version</dt>
<dd>
</dd><dt>[ Member data: returns uint8_t * ] -node_type</dt>
<dd>
</dd><dt>[ Member data: returns uint8_t * ] -num_ports</dt>
<dd>
</dd><dt>[ Member data: returns ib_net64_t * ] -sys_guid</dt>
<dd>
</dd><dt>[ Member data: returns ib_net64_t * ] -node_guid</dt>
<dd>
</dd><dt>[ Member data: returns ib_net64_t * ] -port_guid</dt>
<dd>
</dd><dt>[ Member data: returns ib_net16_t * ] -partition_cap</dt>
<dd>
</dd><dt>[ Member data: returns ib_net16_t * ] -device_id</dt>
<dd>
</dd><dt>[ Member data: returns ib_net32_t * ] -revision</dt>
<dd>
</dd><dt>[ Member data: returns ib_net32_t * ] -port_num_vendor_id</dt>
<dd>
</dd></dl>
<p> <code>class ib_switch_info_t</code> </p>
<dl>
<dt>[ Member data: returns ib_net16_t * ] -lin_cap</dt>
<dd>
</dd><dt>[ Member data: returns ib_net16_t * ] -rand_cap</dt>
<dd>
</dd><dt>[ Member data: returns ib_net16_t * ] -mcast_cap</dt>
<dd>
</dd><dt>[ Member data: returns ib_net16_t * ] -lin_top</dt>
<dd>
</dd><dt>[ Member data: returns uint8_t * ] -def_port</dt>
<dd>
</dd><dt>[ Member data: returns uint8_t * ] -def_mcast_pri_port</dt>
<dd>
</dd><dt>[ Member data: returns uint8_t * ] -def_mcast_not_port</dt>
<dd>
</dd><dt>[ Member data: returns uint8_t * ] -life_state</dt>
<dd>
</dd><dt>[ Member data: returns ib_net16_t * ] -lids_per_port</dt>
<dd>
</dd><dt>[ Member data: returns ib_net16_t * ] -enforce_cap</dt>
<dd>
</dd><dt>[ Member data: returns uint8_t * ] -flags</dt>
<dd>
</dd></dl>
<p> <code>class ib_port_info_t</code> </p>
<dl>
<dt>[ Member data: returns ib_net64_t * ] -m_key</dt>
<dd>
</dd><dt>[ Member data: returns ib_net64_t * ] -subnet_prefix</dt>
<dd>
</dd><dt>[ Member data: returns ib_net16_t * ] -base_lid</dt>
<dd>
</dd><dt>[ Member data: returns ib_net16_t * ] -master_sm_base_lid</dt>
<dd>
</dd><dt>[ Member data: returns ib_net32_t * ] -capability_mask</dt>
<dd>
</dd><dt>[ Member data: returns ib_net16_t * ] -diag_code</dt>
<dd>
</dd><dt>[ Member data: returns ib_net16_t * ] -m_key_lease_period</dt>
<dd>
</dd><dt>[ Member data: returns uint8_t * ] -local_port_num</dt>
<dd>
</dd><dt>[ Member data: returns uint8_t * ] -link_width_enabled</dt>
<dd>
</dd><dt>[ Member data: returns uint8_t * ] -link_width_supported</dt>
<dd>
</dd><dt>[ Member data: returns uint8_t * ] -link_width_active</dt>
<dd>
</dd><dt>[ Member data: returns uint8_t * ] -state_info1</dt>
<dd>
</dd><dt>[ Member data: returns uint8_t * ] -state_info2</dt>
<dd> LinkSpeedSupported and PortState</dd>
<dt>[ Member data: returns uint8_t * ] -mkey_lmc</dt>
<dd> PortPhysState and LinkDownDefaultState</dd>
<dt>[ Member data: returns uint8_t * ] -link_speed</dt>
<dd>
</dd><dt>[ Member data: returns uint8_t * ] -mtu_smsl</dt>
<dd> LinkSpeedEnabled and LinkSpeedActive</dd>
<dt>[ Member data: returns uint8_t * ] -vl_cap</dt>
<dd>
</dd><dt>[ Member data: returns uint8_t * ] -vl_high_limit</dt>
<dd> VlCap and InitType</dd>
<dt>[ Member data: returns uint8_t * ] -vl_arb_high_cap</dt>
<dd>
</dd><dt>[ Member data: returns uint8_t * ] -vl_arb_low_cap</dt>
<dd>
</dd><dt>[ Member data: returns uint8_t * ] -mtu_cap</dt>
<dd>
</dd><dt>[ Member data: returns uint8_t * ] -vl_stall_life</dt>
<dd>
</dd><dt>[ Member data: returns uint8_t * ] -vl_enforce</dt>
<dd>
</dd><dt>[ Member data: returns ib_net16_t * ] -m_key_violations</dt>
<dd>
</dd><dt>[ Member data: returns ib_net16_t * ] -p_key_violations</dt>
<dd>
</dd><dt>[ Member data: returns ib_net16_t * ] -q_key_violations</dt>
<dd>
</dd><dt>[ Member data: returns uint8_t * ] -guid_cap</dt>
<dd>
</dd><dt>[ Member data: returns uint8_t * ] -subnet_timeout</dt>
<dd>
</dd><dt>[ Member data: returns uint8_t * ] -resp_time_value</dt>
<dd>
</dd><dt>[ Member data: returns uint8_t * ] -error_threshold</dt>
<dd>
</dd></dl>
<p> <code>class ib_node_desc_t</code> </p>
<dl>
<dt>[ Member data: returns uint8_array_t * ] -description</dt>
<dd> Node String is an array of <font SIZE="-1">UTF-8</font> character that describes the node in text format Note that this string is <font SIZE="-1">NOT</font> <font SIZE="-1">NULL</font> <font SIZE="-1">TERMINATED</font>!
</dd></dl>
<p> <code>class ib_lft_record_t</code> </p>
<dl>
<dt>[ Member data: returns ib_net16_t * ] -lid</dt>
<dd>
</dd><dt>[ Member data: returns ib_net16_t * ] -block_num</dt>
<dd>
</dd><dt>[ Member data: returns uint32_t * ] -resv0</dt>
<dd>
</dd><dt>[ Member data: returns uint8_array_t * ] -lft</dt>
<dd>
</dd></dl>
<p> <code>class ib_pm_counters_t</code> </p>
<dl>
<dt>[ Member data: returns ib_mad_t * ] -mad_header</dt>
<dd>
</dd><dt>[ Member data: returns uint32_array_t * ] -reserved0</dt>
<dd>
</dd><dt>[ Member data: returns uint8_t * ] -reserved1</dt>
<dd>
</dd><dt>[ Member data: returns uint8_t * ] -port_select</dt>
<dd>
</dd><dt>[ Member data: returns ib_net16_t * ] -counter_select</dt>
<dd>
</dd><dt>[ Member data: returns ib_net16_t * ] -symbol_error_counter</dt>
<dd>
</dd><dt>[ Member data: returns uint8_t * ] -link_error_recovery_counter</dt>
<dd>
</dd><dt>[ Member data: returns uint8_t * ] -link_down_counter</dt>
<dd>
</dd><dt>[ Member data: returns ib_net16_t * ] -port_rcv_errors</dt>
<dd>
</dd><dt>[ Member data: returns ib_net16_t * ] -port_rcv_remote_physical_errors</dt>
<dd>
</dd><dt>[ Member data: returns ib_net16_t * ] -port_rcv_switch_relay_errors</dt>
<dd>
</dd><dt>[ Member data: returns ib_net16_t * ] -port_xmit_discard</dt>
<dd>
</dd><dt>[ Member data: returns uint8_t * ] -port_xmit_constraint_errors</dt>
<dd>
</dd><dt>[ Member data: returns uint8_t * ] -port_rcv_constraint_errors</dt>
<dd>
</dd><dt>[ Member data: returns uint8_t * ] -reserved2</dt>
<dd>
</dd><dt>[ Member data: returns uint8_t * ] -lli_errors_exc_buf_errors</dt>
<dd>
</dd><dt>[ Member data: returns ib_net16_t * ] -reserved3</dt>
<dd>
</dd><dt>[ Member data: returns ib_net16_t * ] -vl15_dropped</dt>
<dd>
</dd><dt>[ Member data: returns ib_net32_t * ] -port_xmit_data</dt>
<dd>
</dd><dt>[ Member data: returns ib_net32_t * ] -port_rcv_data</dt>
<dd>
</dd><dt>[ Member data: returns ib_net32_t * ] -port_xmit_pkts</dt>
<dd>
</dd><dt>[ Member data: returns ib_net32_t * ] -port_rcv_pkts</dt>
<dd>
</dd><dt>[ Member data: returns uint32_array_t * ] -reserved5</dt>
<dd></dd></dl>
<h2>IBMgtSim Simulator Objects</h2>
<p> <code>class IBMgtSim</code> </p>
<dl>
<dt>[ Member : returns IBFabric * ] getFabric</dt>
<dd>
</dd><dt>[ Member : returns IBMSServer * ] getServer</dt>
<dd>
</dd><dt>[ Member : returns IBMSDispatcher * ] getDispatcher</dt>
<dd>
</dd><dt>[ Member : returns int ] init topoFileName serverPortNum numWorkers</dt>
<dd>
</dd></dl>
<p> <code>class IBMSNode</code> </p>
<dl>
<dt>[ Member : returns IBNode * ] getIBNode</dt>
<dd> get the IBNode of the IBMSNode</dd>
<dt>[ Member : returns int ] getLinkStatus outPortNum</dt>
<dd> get the link status of the given port</dd>
<dt>[ Member : returns int ] setPhyPortErrProfile portNum errProfileIn</dt>
<dd> set a particular port err profile</dd>
<dt>[ Member : returns int ] getPhyPortErrProfile portNum</dt>
<dd> get a particular port err profile</dd>
<dt>[ Member : returns int ] setPhyPortPMCounter portNum counterSelect countersVal</dt>
<dd> set a specific port counter</dd>
<dt>[ Member : returns ib_pm_counters_t * ] getPhyPortPMCounter portNum counterSelect get a specific port counter</dt>
<dd>
</dd><dt>[ Member : returns ib_port_info_t * ] getPortInfo portNum</dt>
<dd> get a specific port info</dd>
<dt>[ Member : returns int ] setLinkStatus portNum newState</dt>
<dd> set the Link status including sending trap128</dd>
<dt>[ Member : returns ib_node_info_t * ] getNodeInfo</dt>
<dd> get the node info</dd>
<dt>[ Member : returns ib_switch_info_t * ] getSwitchInfo</dt>
<dd> get the switch info</dd>
<dt>[ Member : returns ib_pkey_table_t * ] getPKeyTblBlock portNum blockNum</dt>
<dd> get pkey table block</dd>
<dt>[ Member : returns int ] setPKeyTblBlock portNum blockNum tbl</dt>
<dd> set pkey table block</dd>
<dt>[ Member : returns int ] setCrSpace startAddr length data</dt>
<dd> set <font SIZE="-1">CR</font> Space Value</dd>
<dt>[ Member : returns int ] getCrSpace startAddr length data</dt>
<dd> get <font SIZE="-1">CR</font> Space Value</dd>
<dt>[ Member : returns int ] getMFTBlock blockIdx portIdx</dt>
<dd> get <font SIZE="-1">MFT</font> block</dd>
<dt>[ Member : returns int ] setMFTBlock blockIdx portIdx inMftBlock</dt>
<dd> set <font SIZE="-1">MFT</font> block
</dd></dl>
<p> <code>class madMcMemberRec</code> </p>
<dl>
<dt>[ Constructor: returns madMcMemberRec * ] madMcMemberRec name</dt>
<dd>
</dd><dt>[ Destructor: returns void ] rename obj {}</dt>
<dd>
</dd><dt>[ Member data: returns ib_gid_t * ] -mgid</dt>
<dd>
</dd><dt>[ Member data: returns ib_gid_t * ] -port_gid</dt>
<dd>
</dd><dt>[ Member data: returns ib_net32_t * ] -qkey</dt>
<dd>
</dd><dt>[ Member data: returns ib_net16_t * ] -mlid</dt>
<dd>
</dd><dt>[ Member data: returns uint8_t * ] -mtu</dt>
<dd>
</dd><dt>[ Member data: returns uint8_t * ] -tclass</dt>
<dd>
</dd><dt>[ Member data: returns ib_net16_t * ] -pkey</dt>
<dd>
</dd><dt>[ Member data: returns uint8_t * ] -rate</dt>
<dd>
</dd><dt>[ Member data: returns uint8_t * ] -pkt_life</dt>
<dd>
</dd><dt>[ Member data: returns ib_net32_t * ] -sl_flow_hop</dt>
<dd>
</dd><dt>[ Member data: returns uint8_t * ] -scope_state</dt>
<dd>
</dd><dt>[ Member : returns int ] send_set pFromNode fromPort destLid comp_mask</dt>
<dd>
</dd><dt>[ Member : returns int ] send_get pFromNode fromPort destLid comp_mask</dt>
<dd>
</dd><dt>[ Member : returns int ] send_del pFromNode fromPort destLid comp_mask</dt>
<dd>
</dd></dl>
<p> <code>class madPathRec</code> </p>
<dl>
<dt>[ Constructor: returns madPathRec * ] madPathRec name</dt>
<dd>
</dd><dt>[ Destructor: returns void ] rename obj {}</dt>
<dd>
</dd><dt>[ Member data: returns uint8_array_t * ] -resv0</dt>
<dd>
</dd><dt>[ Member data: returns ib_gid_t * ] -dgid</dt>
<dd>
</dd><dt>[ Member data: returns ib_gid_t * ] -sgid</dt>
<dd>
</dd><dt>[ Member data: returns ib_net16_t * ] -dlid</dt>
<dd>
</dd><dt>[ Member data: returns ib_net16_t * ] -slid</dt>
<dd>
</dd><dt>[ Member data: returns ib_net32_t * ] -hop_flow_raw</dt>
<dd>
</dd><dt>[ Member data: returns uint8_t * ] -tclass</dt>
<dd>
</dd><dt>[ Member data: returns uint8_t * ] -num_path</dt>
<dd>
</dd><dt>[ Member data: returns ib_net16_t * ] -pkey</dt>
<dd>
</dd><dt>[ Member data: returns ib_net16_t * ] -sl</dt>
<dd>
</dd><dt>[ Member data: returns uint8_t * ] -mtu</dt>
<dd>
</dd><dt>[ Member data: returns uint8_t * ] -rate</dt>
<dd>
</dd><dt>[ Member data: returns uint8_t * ] -pkt_life</dt>
<dd>
</dd><dt>[ Member data: returns uint8_t * ] -preference</dt>
<dd>
</dd><dt>[ Member data: returns uint8_array_t * ] -resv2</dt>
<dd>
</dd><dt>[ Member : returns int ] send_get pFromNode fromPort destLid comp_mask</dt>
<dd>
</dd></dl>
<p> <code>class madServiceRec</code> </p>
<dl>
<dt>[ Constructor: returns madServiceRec * ] madServiceRec name</dt>
<dd>
</dd><dt>[ Destructor: returns void ] rename obj {}</dt>
<dd>
</dd><dt>[ Member data: returns ib_net64_t * ] -service_id</dt>
<dd>
</dd><dt>[ Member data: returns ib_gid_t * ] -service_gid</dt>
<dd>
</dd><dt>[ Member data: returns ib_net16_t * ] -service_pkey</dt>
<dd>
</dd><dt>[ Member data: returns ib_net16_t * ] -resv</dt>
<dd>
</dd><dt>[ Member data: returns ib_net32_t * ] -service_lease</dt>
<dd>
</dd><dt>[ Member data: returns uint8_array_t * ] -service_key</dt>
<dd>
</dd><dt>[ Member data: returns uint8_array_t * ] -service_name</dt>
<dd>
</dd><dt>[ Member data: returns uint8_array_t * ] -service_data8</dt>
<dd>
</dd><dt>[ Member data: returns uint16_array_t * ] -service_data16</dt>
<dd>
</dd><dt>[ Member data: returns uint32_array_t * ] -service_data32</dt>
<dd>
</dd><dt>[ Member data: returns uint64_array_t * ] -service_data64</dt>
<dd>
</dd><dt>[ Member : returns int ] send_set pFromNode fromPort destLid comp_mask</dt>
<dd>
</dd><dt>[ Member : returns int ] send_get pFromNode fromPort destLid comp_mask</dt>
<dd>
</dd><dt>[ Member : returns int ] send_del pFromNode fromPort destLid comp_mask</dt>
<dd>
</dd></dl>
<p> <code>class madNotice128</code> </p>
<dl>
<dt>[ Constructor: returns madNotice128 * ] madNotice128 name</dt>
<dd>
</dd><dt>[ Destructor: returns void ] rename obj {}</dt>
<dd>
</dd><dt>[ Member data: returns uint8_t * ] -generic_type</dt>
<dd>
</dd><dt>[ Member data: returns uint8_t * ] -prod_type_msb</dt>
<dd>
</dd><dt>[ Member data: returns ib_net16_t * ] -prod_type_lsb</dt>
<dd>
</dd><dt>[ Member data: returns ib_net16_t * ] -trap_num</dt>
<dd>
</dd><dt>[ Member data: returns ib_net16_t * ] -issuer_lid</dt>
<dd>
</dd><dt>[ Member data: returns ib_net16_t * ] -toggle_count</dt>
<dd>
</dd><dt>[ Member data: returns ib_net16_t * ] -sw_lid</dt>
<dd> the sw lid of which link state changed &#8211; for 128 only</dd>
<dt>[ Member data: returns ib_gid_t * ] -issuer_gid</dt>
<dd>
</dd><dt>[ Member : returns int ] send_trap pFromNode fromPort destLid</dt>
<dd>
</dd></dl>
<p> <code>class madNotice129</code> </p>
<dl>
<dt>[ Constructor: returns madNotice129 * ] madNotice129 name</dt>
<dd>
</dd><dt>[ Destructor: returns void ] rename obj {}</dt>
<dd>
</dd><dt>[ Member data: returns uint8_t * ] -generic_type</dt>
<dd>
</dd><dt>[ Member data: returns uint8_t * ] -prod_type_msb</dt>
<dd>
</dd><dt>[ Member data: returns ib_net16_t * ] -prod_type_lsb</dt>
<dd>
</dd><dt>[ Member data: returns ib_net16_t * ] -trap_num</dt>
<dd>
</dd><dt>[ Member data: returns ib_net16_t * ] -issuer_lid</dt>
<dd>
</dd><dt>[ Member data: returns ib_net16_t * ] -toggle_count</dt>
<dd>
</dd><dt>[ Member data: returns ib_net16_t * ] -pad</dt>
<dd>
</dd><dt>[ Member data: returns ib_net16_t * ] -lid</dt>
<dd> lid and port number of the violation</dd>
<dt>[ Member data: returns uint8_t * ] -port_num</dt>
<dd>
</dd><dt>[ Member data: returns ib_gid_t * ] -issuer_gid</dt>
<dd>
</dd><dt>[ Member : returns int ] send_trap pFromNode fromPort destLid</dt>
<dd>
</dd></dl>
<p> <code>class madNotice144</code> </p>
<dl>
<dt>[ Constructor: returns madNotice144 * ] madNotice144 name</dt>
<dd>
</dd><dt>[ Destructor: returns void ] rename obj {}</dt>
<dd>
</dd><dt>[ Member data: returns uint8_t * ] -generic_type</dt>
<dd>
</dd><dt>[ Member data: returns uint8_t * ] -prod_type_msb</dt>
<dd>
</dd><dt>[ Member data: returns ib_net16_t * ] -prod_type_lsb</dt>
<dd>
</dd><dt>[ Member data: returns ib_net16_t * ] -trap_num</dt>
<dd>
</dd><dt>[ Member data: returns ib_net16_t * ] -issuer_lid</dt>
<dd>
</dd><dt>[ Member data: returns ib_net16_t * ] -toggle_count</dt>
<dd>
</dd><dt>[ Member data: returns ib_net16_t * ] -pad1</dt>
<dd>
</dd><dt>[ Member data: returns ib_net16_t * ] -lid</dt>
<dd> lid where capability mask changed</dd>
<dt>[ Member data: returns ib_net16_t * ] -pad2</dt>
<dd>
</dd><dt>[ Member data: returns ib_net32_t * ] -new_cap_mask</dt>
<dd> new capability mask</dd>
<dt>[ Member data: returns ib_gid_t * ] -issuer_gid</dt>
<dd>
</dd><dt>[ Member : returns int ] send_trap pFromNode fromPort destLid</dt>
<dd></dd></dl>
<h2>AUTHOR</h2>
<p> Eitan Zahavi, Mellanox Technologies <font SIZE="-1">LTD</font>, eitan [at] mellanox.co.il </p>
<h2>Index</h2>
