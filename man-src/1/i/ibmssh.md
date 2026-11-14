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
<dt>[ Constant : int ] $MsgShowFatal = 0x01</p>
<dd>
<dt>[ Constant : int ] $MsgShowError = 0x02</p>
<dd>
<dt>[ Constant : int ] $MsgShowWarning = 0x04</p>
<dd>
<dt>[ Constant : int ] $MsgShowInfo = 0x08</p>
<dd>
<dt>[ Constant : int ] $MsgShowVerbose = 0x10</p>
<dd>
<dt>[ Constant : int ] $MsgShowContext = 0x20</p>
<dd>
<dt>[ Constant : int ] $MsgShowSource = 0x40</p>
<dd>
<dt>[ Constant : int ] $MsgShowTime = 0x80</p>
<dd>
<dt>[ Constant : int ] $MsgShowModule = 0x100</p>
<dd>
<dt>[ Constant : int ] $MsgShowMads = 0x200</p>
<dd>
<dt>[ Constant : int ] $MsgShowFrames = 0x400</p>
<dd>
<dt>[ Constant : int ] $MsgShowAll = 0xffff</p>
<dd>
<dt>[ Constant : int ] $MsgDefault = 0x62f</p>
<dd></dl>
<h2>Message Manager Objects</h2>
<p> <code>class msgManager</code> </p>
<dl>
<dt>
<dd> This is the Message Manager class</dl>
<dl>
<dt>[ Member : returns int ] getVerbLevel ?module?</p>
<dd>
<dt>[ Member : returns int ] clrVerbLevel ?module?</p>
<dd>
<dt>[ Member : returns void ] setVerbLevel vl ?module?</p>
<dd>
<dt>[ Member : returns int ] outstandingMsgCount ?vl?</p>
<dd>
<dt>[ Member : returns string ] outstandingMsgs ?vl?</p>
<dd>
<dt>[ Member : returns string ] getNextMessage</p>
<dd>
<dt>[ Member : returns void ] nullOutstandingMsgs</p>
<dd>
<dt>[ Member : returns int ] setLogFile fileName</p>
<dd></dl>
<h2>Random Manager Functions</h2>
<dl>
<dt>[ returns float ] rmRand</p>
<dd> obtain a random number in the range 0.0 &#8211; 1.0</p>
<dt>[ returns int ] rmSeed seed</p>
<dd> initialize the seed for the random manager
</dl>
<p> <code>class ib_node_info_t</code> </p>
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
<dd>
</dl>
<p> <code>class ib_switch_info_t</code> </p>
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
</dl>
<p> <code>class ib_port_info_t</code> </p>
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
<dd>
<dt>[ Member data: returns uint8_t * ] -state_info2</p>
<dd> LinkSpeedSupported and PortState</p>
<dt>[ Member data: returns uint8_t * ] -mkey_lmc</p>
<dd> PortPhysState and LinkDownDefaultState</p>
<dt>[ Member data: returns uint8_t * ] -link_speed</p>
<dd>
<dt>[ Member data: returns uint8_t * ] -mtu_smsl</p>
<dd> LinkSpeedEnabled and LinkSpeedActive</p>
<dt>[ Member data: returns uint8_t * ] -vl_cap</p>
<dd>
<dt>[ Member data: returns uint8_t * ] -vl_high_limit</p>
<dd> VlCap and InitType</p>
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
</dl>
<p> <code>class ib_node_desc_t</code> </p>
<dl>
<dt>[ Member data: returns uint8_array_t * ] -description</p>
<dd> Node String is an array of <font SIZE="-1">UTF-8</font> character that describes the node in text format Note that this string is <font SIZE="-1">NOT</font> <font SIZE="-1">NULL</font> <font SIZE="-1">TERMINATED</font>!
</dl>
<p> <code>class ib_lft_record_t</code> </p>
<dl>
<dt>[ Member data: returns ib_net16_t * ] -lid</p>
<dd>
<dt>[ Member data: returns ib_net16_t * ] -block_num</p>
<dd>
<dt>[ Member data: returns uint32_t * ] -resv0</p>
<dd>
<dt>[ Member data: returns uint8_array_t * ] -lft</p>
<dd>
</dl>
<p> <code>class ib_pm_counters_t</code> </p>
<dl>
<dt>[ Member data: returns ib_mad_t * ] -mad_header</p>
<dd>
<dt>[ Member data: returns uint32_array_t * ] -reserved0</p>
<dd>
<dt>[ Member data: returns uint8_t * ] -reserved1</p>
<dd>
<dt>[ Member data: returns uint8_t * ] -port_select</p>
<dd>
<dt>[ Member data: returns ib_net16_t * ] -counter_select</p>
<dd>
<dt>[ Member data: returns ib_net16_t * ] -symbol_error_counter</p>
<dd>
<dt>[ Member data: returns uint8_t * ] -link_error_recovery_counter</p>
<dd>
<dt>[ Member data: returns uint8_t * ] -link_down_counter</p>
<dd>
<dt>[ Member data: returns ib_net16_t * ] -port_rcv_errors</p>
<dd>
<dt>[ Member data: returns ib_net16_t * ] -port_rcv_remote_physical_errors</p>
<dd>
<dt>[ Member data: returns ib_net16_t * ] -port_rcv_switch_relay_errors</p>
<dd>
<dt>[ Member data: returns ib_net16_t * ] -port_xmit_discard</p>
<dd>
<dt>[ Member data: returns uint8_t * ] -port_xmit_constraint_errors</p>
<dd>
<dt>[ Member data: returns uint8_t * ] -port_rcv_constraint_errors</p>
<dd>
<dt>[ Member data: returns uint8_t * ] -reserved2</p>
<dd>
<dt>[ Member data: returns uint8_t * ] -lli_errors_exc_buf_errors</p>
<dd>
<dt>[ Member data: returns ib_net16_t * ] -reserved3</p>
<dd>
<dt>[ Member data: returns ib_net16_t * ] -vl15_dropped</p>
<dd>
<dt>[ Member data: returns ib_net32_t * ] -port_xmit_data</p>
<dd>
<dt>[ Member data: returns ib_net32_t * ] -port_rcv_data</p>
<dd>
<dt>[ Member data: returns ib_net32_t * ] -port_xmit_pkts</p>
<dd>
<dt>[ Member data: returns ib_net32_t * ] -port_rcv_pkts</p>
<dd>
<dt>[ Member data: returns uint32_array_t * ] -reserved5</p>
<dd></dl>
<h2>IBMgtSim Simulator Objects</h2>
<p> <code>class IBMgtSim</code> </p>
<dl>
<dt>[ Member : returns IBFabric * ] getFabric</p>
<dd>
<dt>[ Member : returns IBMSServer * ] getServer</p>
<dd>
<dt>[ Member : returns IBMSDispatcher * ] getDispatcher</p>
<dd>
<dt>[ Member : returns int ] init topoFileName serverPortNum numWorkers</p>
<dd>
</dl>
<p> <code>class IBMSNode</code> </p>
<dl>
<dt>[ Member : returns IBNode * ] getIBNode</p>
<dd> get the IBNode of the IBMSNode</p>
<dt>[ Member : returns int ] getLinkStatus outPortNum</p>
<dd> get the link status of the given port</p>
<dt>[ Member : returns int ] setPhyPortErrProfile portNum errProfileIn</p>
<dd> set a particular port err profile</p>
<dt>[ Member : returns int ] getPhyPortErrProfile portNum</p>
<dd> get a particular port err profile</p>
<dt>[ Member : returns int ] setPhyPortPMCounter portNum counterSelect countersVal</p>
<dd> set a specific port counter</p>
<dt>[ Member : returns ib_pm_counters_t * ] getPhyPortPMCounter portNum counterSelect get a specific port counter</p>
<dd>
<dt>[ Member : returns ib_port_info_t * ] getPortInfo portNum</p>
<dd> get a specific port info</p>
<dt>[ Member : returns int ] setLinkStatus portNum newState</p>
<dd> set the Link status including sending trap128</p>
<dt>[ Member : returns ib_node_info_t * ] getNodeInfo</p>
<dd> get the node info</p>
<dt>[ Member : returns ib_switch_info_t * ] getSwitchInfo</p>
<dd> get the switch info</p>
<dt>[ Member : returns ib_pkey_table_t * ] getPKeyTblBlock portNum blockNum</p>
<dd> get pkey table block</p>
<dt>[ Member : returns int ] setPKeyTblBlock portNum blockNum tbl</p>
<dd> set pkey table block</p>
<dt>[ Member : returns int ] setCrSpace startAddr length data</p>
<dd> set <font SIZE="-1">CR</font> Space Value</p>
<dt>[ Member : returns int ] getCrSpace startAddr length data</p>
<dd> get <font SIZE="-1">CR</font> Space Value</p>
<dt>[ Member : returns int ] getMFTBlock blockIdx portIdx</p>
<dd> get <font SIZE="-1">MFT</font> block</p>
<dt>[ Member : returns int ] setMFTBlock blockIdx portIdx inMftBlock</p>
<dd> set <font SIZE="-1">MFT</font> block
</dl>
<p> <code>class madMcMemberRec</code> </p>
<dl>
<dt>[ Constructor: returns madMcMemberRec * ] madMcMemberRec name</p>
<dd>
<dt>[ Destructor: returns void ] rename obj {}</p>
<dd>
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
<dd>
<dt>[ Member : returns int ] send_set pFromNode fromPort destLid comp_mask</p>
<dd>
<dt>[ Member : returns int ] send_get pFromNode fromPort destLid comp_mask</p>
<dd>
<dt>[ Member : returns int ] send_del pFromNode fromPort destLid comp_mask</p>
<dd>
</dl>
<p> <code>class madPathRec</code> </p>
<dl>
<dt>[ Constructor: returns madPathRec * ] madPathRec name</p>
<dd>
<dt>[ Destructor: returns void ] rename obj {}</p>
<dd>
<dt>[ Member data: returns uint8_array_t * ] -resv0</p>
<dd>
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
<dd>
<dt>[ Member data: returns uint8_array_t * ] -resv2</p>
<dd>
<dt>[ Member : returns int ] send_get pFromNode fromPort destLid comp_mask</p>
<dd>
</dl>
<p> <code>class madServiceRec</code> </p>
<dl>
<dt>[ Constructor: returns madServiceRec * ] madServiceRec name</p>
<dd>
<dt>[ Destructor: returns void ] rename obj {}</p>
<dd>
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
<dt>[ Member data: returns uint8_array_t * ] -service_name</p>
<dd>
<dt>[ Member data: returns uint8_array_t * ] -service_data8</p>
<dd>
<dt>[ Member data: returns uint16_array_t * ] -service_data16</p>
<dd>
<dt>[ Member data: returns uint32_array_t * ] -service_data32</p>
<dd>
<dt>[ Member data: returns uint64_array_t * ] -service_data64</p>
<dd>
<dt>[ Member : returns int ] send_set pFromNode fromPort destLid comp_mask</p>
<dd>
<dt>[ Member : returns int ] send_get pFromNode fromPort destLid comp_mask</p>
<dd>
<dt>[ Member : returns int ] send_del pFromNode fromPort destLid comp_mask</p>
<dd>
</dl>
<p> <code>class madNotice128</code> </p>
<dl>
<dt>[ Constructor: returns madNotice128 * ] madNotice128 name</p>
<dd>
<dt>[ Destructor: returns void ] rename obj {}</p>
<dd>
<dt>[ Member data: returns uint8_t * ] -generic_type</p>
<dd>
<dt>[ Member data: returns uint8_t * ] -prod_type_msb</p>
<dd>
<dt>[ Member data: returns ib_net16_t * ] -prod_type_lsb</p>
<dd>
<dt>[ Member data: returns ib_net16_t * ] -trap_num</p>
<dd>
<dt>[ Member data: returns ib_net16_t * ] -issuer_lid</p>
<dd>
<dt>[ Member data: returns ib_net16_t * ] -toggle_count</p>
<dd>
<dt>[ Member data: returns ib_net16_t * ] -sw_lid</p>
<dd> the sw lid of which link state changed &#8211; for 128 only</p>
<dt>[ Member data: returns ib_gid_t * ] -issuer_gid</p>
<dd>
<dt>[ Member : returns int ] send_trap pFromNode fromPort destLid</p>
<dd>
</dl>
<p> <code>class madNotice129</code> </p>
<dl>
<dt>[ Constructor: returns madNotice129 * ] madNotice129 name</p>
<dd>
<dt>[ Destructor: returns void ] rename obj {}</p>
<dd>
<dt>[ Member data: returns uint8_t * ] -generic_type</p>
<dd>
<dt>[ Member data: returns uint8_t * ] -prod_type_msb</p>
<dd>
<dt>[ Member data: returns ib_net16_t * ] -prod_type_lsb</p>
<dd>
<dt>[ Member data: returns ib_net16_t * ] -trap_num</p>
<dd>
<dt>[ Member data: returns ib_net16_t * ] -issuer_lid</p>
<dd>
<dt>[ Member data: returns ib_net16_t * ] -toggle_count</p>
<dd>
<dt>[ Member data: returns ib_net16_t * ] -pad</p>
<dd>
<dt>[ Member data: returns ib_net16_t * ] -lid</p>
<dd> lid and port number of the violation</p>
<dt>[ Member data: returns uint8_t * ] -port_num</p>
<dd>
<dt>[ Member data: returns ib_gid_t * ] -issuer_gid</p>
<dd>
<dt>[ Member : returns int ] send_trap pFromNode fromPort destLid</p>
<dd>
</dl>
<p> <code>class madNotice144</code> </p>
<dl>
<dt>[ Constructor: returns madNotice144 * ] madNotice144 name</p>
<dd>
<dt>[ Destructor: returns void ] rename obj {}</p>
<dd>
<dt>[ Member data: returns uint8_t * ] -generic_type</p>
<dd>
<dt>[ Member data: returns uint8_t * ] -prod_type_msb</p>
<dd>
<dt>[ Member data: returns ib_net16_t * ] -prod_type_lsb</p>
<dd>
<dt>[ Member data: returns ib_net16_t * ] -trap_num</p>
<dd>
<dt>[ Member data: returns ib_net16_t * ] -issuer_lid</p>
<dd>
<dt>[ Member data: returns ib_net16_t * ] -toggle_count</p>
<dd>
<dt>[ Member data: returns ib_net16_t * ] -pad1</p>
<dd>
<dt>[ Member data: returns ib_net16_t * ] -lid</p>
<dd> lid where capability mask changed</p>
<dt>[ Member data: returns ib_net16_t * ] -pad2</p>
<dd>
<dt>[ Member data: returns ib_net32_t * ] -new_cap_mask</p>
<dd> new capability mask</p>
<dt>[ Member data: returns ib_gid_t * ] -issuer_gid</p>
<dd>
<dt>[ Member : returns int ] send_trap pFromNode fromPort destLid</p>
<dd></dl>
<h2>AUTHOR</h2>
<p> Eitan Zahavi, Mellanox Technologies <font SIZE="-1">LTD</font>, eitan [at] mellanox.co.il </p>
<h2>Index</h2>
