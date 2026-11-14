---
title: "ipmi-oem(8)"
name: "ipmi-oem"
section: "8"
letter: "i"
url: "/docs/linux/man/8-ipmi-oem/"
description: "ipmi-oem – IPMI OEM utility"
---

<p>ipmi-oem &#8211; IPMI OEM utility</p>
<h2>Synopsis</h2>
<p><code>ipmi-oem</code> [<i>OPTION</i>&#8230;] &lt;<i>OEMID</i>&gt; &lt;<i>OEMCOMMAND</i>&gt; [<i>OEMOPTION</i>&#8230;]</p>
<h2>Description</h2>
<p><code>Ipmi-oem</code> is used to execute OEM specific IPMI commands. It is intended to provide a better user interface for OEM specific IPMI commands rather than using <code><a href="/docs/linux/man/8-ipmi-raw/">ipmi-raw</a>(8).</code> Please see SUPPORTED OEM IDS and COMMANDS below for a list of supported OEM specific IPMI commands. A list of supported OEM specific commands may also be generated using the <code>&#8211;list</code> option. There are no guarantees that the below OEM commands will work on any particular motherboard. OEM extensions may or may not exist on particular hardware revisions and/or firmware revisions of motherboards. The extensions may or may not function for other lines of motherboards from the same manufacturer. </p>
<p> Listed below are general IPMI options, tool specific options, trouble shooting information, workaround information, examples, and known issues. For a general introduction to FreeIPMI please see <code><a href="/docs/linux/man/7-freeipmi/">freeipmi</a>(7).</code></p>
<h2>General Options</h2>
<p>The following options are general options for configuring IPMI communication and executing general tool commands.</p>
<dl>
<dt><code>-D</code> <i>IPMIDRIVER</i>, <code>&#8211;driver-type</code>=<i>IPMIDRIVER</i></p>
<dd>Specify the driver type to use instead of doing an auto selection. The currently available outofband drivers are LAN and LAN_2_0, which perform IPMI 1.5 and IPMI 2.0 respectively. The currently available inband drivers are KCS, SSIF, OPENIPMI, and SUNBMC.</p>
<dt><code>&#8211;disable-auto-probe</code></p>
<dd>Do not probe in-band IPMI devices for default settings.</p>
<dt><code>&#8211;driver-address</code>=<i>DRIVER-ADDRESS</i></p>
<dd>Specify the in-band driver address to be used instead of the probed value. <i>DRIVER-ADDRESS</i> should be prefixed with &quot;0x&quot; for a hex value and &#8216;0&#8217; for an octal value.</p>
<dt><code>&#8211;driver-device</code>=<i>DEVICE</i></p>
<dd>Specify the in-band driver device path to be used instead of the probed path.</p>
<dt><code>&#8211;register-spacing</code>=<i>REGISTER-SPACING</i></p>
<dd>Specify the in-band driver register spacing instead of the probed value. Argument is in bytes (i.e. 32bit register spacing = 4)</p>
<dt><code>&#8211;target-channel-number</code>=<i>CHANNEL-NUMBERFR</p>
<dd>Specify the in-band driver target channel number to send IPMI requests to.</p>
<dt></i><code>&#8211;target-slave-address</code>=<i>SLAVE-ADDRESSFR</p>
<dd>Specify the in-band driver target slave number to send IPMI requests to.</p>
<dt></i><code>-h</code> <i>IPMIHOST1,IPMIHOST2,&#8230;</i>, <code>&#8211;hostname</code>=<i>IPMIHOST1[:PORT],IPMIHOST2[:PORT],&#8230;</i></p>
<dd>Specify the remote host(s) to communicate with. Multiple hostnames may be separated by comma or may be specified in a range format; see HOSTRANGED SUPPORT below. An optional port can be specified with each host, which may be useful in port forwarding or similar situations.</p>
<dt><code>-u</code> <i>USERNAME</i>, <code>&#8211;username</code>=<i>USERNAME</i></p>
<dd>Specify the username to use when authenticating with the remote host. If not specified, a null (i.e. anonymous) username is assumed. The required user privilege will depend on the oem commands executed.</p>
<dt><code>-p</code> <i>PASSWORD</i>, <code>&#8211;password</code>=<i>PASSWORD</i></p>
<dd>Specify the password to use when authenticationg with the remote host. If not specified, a null password is assumed. Maximum password length is 16 for IPMI 1.5 and 20 for IPMI 2.0.</p>
<dt><code>-P</code>, <code>&#8211;password-prompt</code></p>
<dd>Prompt for password to avoid possibility of listing it in process lists.</p>
<dt><code>-k</code> <i>K_G</i>, <code>&#8211;k-g</code>=<i>K_G</i></p>
<dd>Specify the K_g BMC key to use when authenticating with the remote host for IPMI 2.0. If not specified, a null key is assumed. To input the key in hexadecimal form, prefix the string with &#8216;0x&#8217;. E.g., the key &#8216;abc&#8217; can be entered with the either the string &#8216;abc&#8217; or the string &#8216;0x616263&#8217;</p>
<dt><code>-K</code>, <code>&#8211;k-g-prompt</code></p>
<dd>Prompt for k-g to avoid possibility of listing it in process lists.</p>
<dt><code>&#8211;session-timeout</code>=<i>MILLISECONDS</i></p>
<dd>Specify the session timeout in milliseconds. Defaults to 20000 milliseconds (20 seconds) if not specified.</p>
<dt><code>&#8211;retransmission-timeout</code>=<i>MILLISECONDS</i></p>
<dd>Specify the packet retransmission timeout in milliseconds. Defaults to 1000 milliseconds (1 second) if not specified. The retransmission timeout cannot be larger than the session timeout.</p>
<dt><code>-a</code> <i>AUTHENTICATION-TYPE</i>, <code>&#8211;authentication-type</code>=<i>AUTHENTICATION-TYPE</i></p>
<dd>Specify the IPMI 1.5 authentication type to use. The currently available authentication types are NONE, STRAIGHT_PASSWORD_KEY, MD2, and MD5. Defaults to MD5 if not specified.</p>
<dt><code>-I</code> <i>CIPHER-SUITE-ID</i>, <code>&#8211;cipher-suite-id</code>=<i>CIPHER-SUITE-ID</i></p>
<dd>Specify the IPMI 2.0 cipher suite ID to use. The Cipher Suite ID identifies a set of authentication, integrity, and confidentiality algorithms to use for IPMI 2.0 communication. The authentication algorithm identifies the algorithm to use for session setup, the integrity algorithm identifies the algorithm to use for session packet signatures, and the confidentiality algorithm identifies the algorithm to use for payload encryption. Defaults to cipher suite ID 3 if not specified. The following cipher suite ids are currently supported: </p>
<p> 0 &#8211; Authentication Algorithm = None; Integrity Algorithm = None; Confidentiality Algorithm = None </p>
<p> 1 &#8211; Authentication Algorithm = HMAC-SHA1; Integrity Algorithm = None; Confidentiality Algorithm = None </p>
<p> 2 &#8211; Authentication Algorithm = HMAC-SHA1; Integrity Algorithm = HMAC-SHA1-96; Confidentiality Algorithm = None </p>
<p> 3 &#8211; Authentication Algorithm = HMAC-SHA1; Integrity Algorithm = HMAC-SHA1-96; Confidentiality Algorithm = AES-CBC-128 </p>
<p> 6 &#8211; Authentication Algorithm = HMAC-MD5; Integrity Algorithm = None; Confidentiality Algorithm = None </p>
<p> 7 &#8211; Authentication Algorithm = HMAC-MD5; Integrity Algorithm = HMAC-MD5-128; Confidentiality Algorithm = None </p>
<p> 8 &#8211; Authentication Algorithm = HMAC-MD5; Integrity Algorithm = HMAC-MD5-128; Confidentiality Algorithm = AES-CBC-128 </p>
<p> 11 &#8211; Authentication Algorithm = HMAC-MD5; Integrity Algorithm = MD5-128; Confidentiality Algorithm = None </p>
<p> 12 &#8211; Authentication Algorithm = HMAC-MD5; Integrity Algorithm = MD5-128; Confidentiality Algorithm = AES-CBC-128 </p>
<p> 15 &#8211; Authentication Algorithm = HMAC-SHA256; Integrity Algorithm = None; Confidentiality Algorithm = None </p>
<p> 16 &#8211; Authentication Algorithm = HMAC-SHA256; Integrity Algorithm = HMAC_SHA256_128; Confidentiality Algorithm = None </p>
<p> 17 &#8211; Authentication Algorithm = HMAC-SHA256; Integrity Algorithm = HMAC_SHA256_128; Confidentiality Algorithm = AES-CBC-128</p>
<dt><code>-l</code> <i>PRIVILEGE-LEVEL</i>, <code>&#8211;privilege-level</code>=<i>PRIVILEGE-LEVEL</i></p>
<dd>Specify the privilege level to be used. The currently available privilege levels are USER, OPERATOR, and ADMIN. Defaults to ADMIN if not specified.</p>
<dt><code>&#8211;config-file</code>=<i>FILE</i></p>
<dd>Specify an alternate configuration file.</p>
<dt><code>-W</code> <i>WORKAROUNDS</i>, <code>&#8211;workaround-flags</code>=<i>WORKAROUNDS</i></p>
<dd>Specify workarounds to vendor compliance issues. Multiple workarounds can be specified separated by commas. A special command line flag of &quot;none&quot;, will indicate no workarounds (may be useful for overriding configured defaults). See WORKAROUNDS below for a list of available workarounds.</p>
<dt><code>&#8211;debug</code></p>
<dd>Turn on debugging.</p>
<dt><code>-?</code>, <code>&#8211;help</code></p>
<dd>Output a help list and exit.</p>
<dt><code>&#8211;usage</code></p>
<dd>Output a usage message and exit.</p>
<dt><code>-V</code>, <code>&#8211;version</code></p>
<dd>Output the program version and exit.</dl>
<h2>Sdr Cache Options</h2>
<p>This tool requires access to the sensor data repository (SDR) cache for general operation. By default, SDR data will be downloaded and cached on the local machine. The following options apply to the SDR cache.</p>
<dl>
<dt><code>-f</code>, <code>&#8211;flush-cache</code></p>
<dd>Flush a cached version of the sensor data repository (SDR) cache. The SDR is typically cached for faster subsequent access. However, it may need to be flushed and re-generated if the SDR has been updated on a system.</p>
<dt><code>-Q</code>, <code>&#8211;quiet-cache</code></p>
<dd>Do not output information about cache creation/deletion. May be useful in scripting.</p>
<dt><code>&#8211;sdr-cache-recreate</code></p>
<dd>If the SDR cache is out of date or invalid, automatically recreate the sensor data repository (SDR) cache. This option may be useful for scripting purposes.</p>
<dt><code>&#8211;sdr-cache-file</code>=<i>FILE</i></p>
<dd>Specify a specific sensor data repository (SDR) cache file to be stored or read from. If this option is used when multiple hosts are specified, the same SDR cache file will be used for all hosts.</p>
<dt><code>&#8211;sdr-cache-directory</code>=<i>DIRECTORY</i></p>
<dd>Specify an alternate directory for sensor data repository (SDR) caches to be stored or read from. Defaults to the home directory if not specified.</dl>
<h2>Hostranged Options</h2>
<p>The following options manipulate hostranged output. See HOSTRANGED SUPPORT below for additional information on hostranges.</p>
<dl>
<dt><code>-B</code>, <code>&#8211;buffer-output</code></p>
<dd>Buffer hostranged output. For each node, buffer standard output until the node has completed its IPMI operation. When specifying this option, data may appear to output slower to the user since the the entire IPMI operation must complete before any data can be output. See HOSTRANGED SUPPORT below for additional information.</p>
<dt><code>-C</code>, <code>&#8211;consolidate-output</code></p>
<dd>Consolidate hostranged output. The complete standard output from every node specified will be consolidated so that nodes with identical output are not output twice. A header will list those nodes with the consolidated output. When this option is specified, no output can be seen until the IPMI operations to all nodes has completed. If the user breaks out of the program early, all currently consolidated output will be dumped. See HOSTRANGED SUPPORT below for additional information.</p>
<dt><code>-F</code> <i>NUM</i>, <code>&#8211;fanout</code>=<i>NUM</i></p>
<dd>Specify multiple host fanout. A &quot;sliding window&quot; (or fanout) algorithm is used for parallel IPMI communication so that slower nodes or timed out nodes will not impede parallel communication. The maximum number of threads available at the same time is limited by the fanout. The default is 64.</p>
<dt><code>-E</code>, <code>&#8211;eliminate</code></p>
<dd>Eliminate hosts determined as undetected by <code>ipmidetect.</code> This attempts to remove the common issue of hostranged execution timing out due to several nodes being removed from service in a large cluster. The <code>ipmidetectd</code> daemon must be running on the node executing the command.</p>
<dt><code>&#8211;always-prefix</code></p>
<dd>Always prefix output, even if only one host is specified or communicating in-band. This option is primarily useful for scripting purposes. Option will be ignored if specified with the <code>-C</code> option.</dl>
<h2>Ipmi-Oem Options</h2>
<p>The following options are specific to <code>Ipmi-oem.</code></p>
<dl>
<dt><code>-L</code>, <code>&#8211;list</code></p>
<dd>List supported OEM IDs and Commands.</p>
<dt><code>-v</code>, <code>&#8211;verbose</code></p>
<dd>Output verbose information. Additional output will depend on specific OEM ID and OEM COMMANDS specified.</dl>
<h2>SUPPORTED OEM IDS and COMMANDS</h2>
<p>The currently supported OEM IDs and COMMANDs are listed below. The special OEM ID of <code>list</code> may be passed into the list all supported OEM IDs and Commands. The special OEM command <code>list</code> may be passed to any OEM ID to list commands supported by that OEM ID.</p>
<dl>
<dt><code>Dell</code></p>
<dd>
<dl>
<dd>
<dl>
<dt><code>get-system-info </code><i>KEY</i></p>
<dd>This OEM command can retrieve the motherboard system information. Valid keys are <i>guid</i>, <i>asset-tag</i>, <i>service-tag</i>, <i>chassis-service-tag</i>, <i>chassis-related-service-tag</i>, <i>board-revision</i>, <i>platform-model-name</i>, <i>blade-slot-info</i>, <i>system-revision</i>, <i>idrac-info</i>, <i>idrac-ipv4-url</i>, <i>idrac-gui-webserver-control</i>, <i>cmc-info</i>, <i>cmc-ipv4-url</i>, <i>cmc-ipv6-info</i>, <i>cmc-ipv6-url</i>, <i>mac-addresses</i>. Command confirmed to work on Dell Poweredge 2900, 2950, R610, R710, R720, M600, M610, M610X, M910, and R905. However, individual system information options may not be readable or available on every system.</p>
<dt><code>get-nic-selection</code></p>
<dd>This OEM command will determine the current NIC selection for IPMI as dedicated, shared, shared w/ failover to NIC2, or shared w/ failover to all. Dedicated indicates IPMI is only available on an expansion card, shared indicates IPMI is available on NIC1, shared w/ failover to NIC2 indicates IPMI is available on NIC1 w/ failover to NIC2 on NIC1&#8217;s failure, and shared w/ failover to all indicates IPMI is available on NIC1 w/ failover to all other NICs in the event of NIC failure. Command confirmed to work on Dell Poweredge 2900, 2950, R610, R710, and R905.</p>
<dt><code>set-nic-section </code><i>dedicated|shared|shared_failover_nic2|shared_failover_all</i></p>
<dd>This OEM command will set the current NIC selection to dedicated, shared, shared_failover_nic2, or shared_failover_all. (See <i>get-nic-selection</i> above for description on inputs.) On older Poweredge systems, <i>shared_failover_nic2</i> may have been documented as just <i>failover</i>. Command confirmed to work on Dell Poweredge 2900, 2950, R610, R710, and R905.</p>
<dt><code>get-nic-selection-failover</code></p>
<dd>This OEM command will determine the current NIC selection for IPMI and the failover NIC. Command confirmed to work on Dell Poweredge R720 (Dell 12G Poweredge systems).</p>
<dt><code>set-nic-section-failover </code><i>dedicated|lom1|lom2|lom3|lom4</i> <i>none|lom1|lom2|lom3|lom4|all</i></p>
<dd>This OEM command will set the current NIC selection for IPMI and the failover NIC. The first option sets the IPMI NIC and the second option the failover NIC. Command confirmed to work on Dell Poweredge R720 (Dell 12G Poweredge systems).</p>
<dt><code>get-active-lom-status </code><i>[v1|v2]</i></p>
<dd>This OEM command will get the current NIC being used for out of band management and possibly additional information. Users may specify if version 1 or version 2 of this extension should be executed. If no version is specified, version 1 is exectued. Version 1 of this command confirmed to work on Dell Poweredge R610 and R710 (Dell 11G Poweredge systems). Version 2 of this command confirmed to work on Dell Poweredge R720 (Dell 12G Poweredge systems).</p>
<dt><code>get-ssh-config</code></p>
<dd>This OEM command will get the current SSH configuration on the IPMI card. Command confirmed to work on Dell Poweredge R610 and R710 (Dell 11G Poweredge systems).</p>
<dt><code>set-ssh-config </code><i>KEY=VALUE &#8230;</i></p>
<dd>This OEM command will set the current SSH configuration on the IPMI card. The possible keys and values are <i>ssh=enable|disable</i>, <i>idletimeout=seconds</i>, and <i>portnumber=num</i>. Multiple key=value pairs may be specified. If no key=value pairs are specifed, available pairs are output. Some fields may be read-only on specific Poweredge systems. Command confirmed to work on Dell Poweredge R610 and R710 (Dell 11G Poweredge systems).</p>
<dt><code>get-telnet-config</code></p>
<dd>This OEM command will get the current telnet configuration on the IPMI card. Command confirmed to work on Dell Poweredge R610 and R710 (Dell 11G Poweredge systems).</p>
<dt><code>set-telnet-config </code><i>KEY=VALUE &#8230;</i></p>
<dd>This OEM command will set the current Telnet configuration on the IPMI card. The possible keys and values are <i>telnet=enable|disable</i>, <i>sessiontimeout=seconds</i>, <i>portnumber=num</i>, and <i>7fls=enable|disable</i>. Multiple key=value pairs may be specified. If no key=value pairs are specifed, available pairs are output. Some fields may be read-only on specific Poweredge systems. Command confirmed to work on Dell Poweredge R610 and R710 (Dell 11G Poweredge systems).</p>
<dt><code>get-web-server-config</code></p>
<dd>This OEM command will get the current web server configuration on the IPMI card. Command confirmed to work on Dell Poweredge R610 and R710 (Dell 11G Poweredge systems).</p>
<dt><code>set-web-server-config </code><i>KEY=VALUE &#8230;</i></p>
<dd>This OEM command will set the current Web Server configuration on the IPMI card. The possible keys and values are <i>webserver=enable|disable</i>, <i>sessiontimeout=seconds</i>, <i>httpportnumber=num</i>, and <i>httpsportnumber=num</i>. Multiple key=value pairs may be specified. If no key=value pairs are specifed, available pairs are output. Some fields may be read-only on specific Poweredge systems. Command confirmed to work on Dell Poweredge R610 and R710 (Dell 11G Poweredge systems).</p>
<dt><code>get-active-directory-config</code></p>
<dd>This OEM command will get the current active directory configuration on the IPMI card. Command confirmed to work on Dell Poweredge R610 and R710 (Dell 11G Poweredge systems).</p>
<dt><code>set-active-directory-config</code></p>
<dd>This OEM command will set the current Web Server configuration on the IPMI card. The possible keys and values are <i>activedirectory=enable|disable</i>, <i>timeout=seconds</i>, <i>type=extended|standard</i>, <i>sso=enable|disable</i>, and <i>certificatevalidation=enable|disable</i>. If no key=value pairs are specifed, available pairs are output. Some fields may be read-only on specific Poweredge systems. Command confirmed to work on Dell Poweredge R610 and R710 (Dell 11G Poweredge systems).</p>
<dt><code>reset-to-defaults</code></p>
<dd>This OEM command will reset the BMC configuration back to default values. The command will spin until the reset is confirmed to be complete. Command confirmed to work on Dell Poweredge R610 and R710 (Dell 11G Poweredge systems).</p>
<dt><code>get-power-consumption-data</code></p>
<dd>This OEM command can retrieve power consumption data. Command confirmed to work on Dell Poweredge R610, R710, R905, M610, M610x, and M910.</p>
<dt><code>reset-power-consumption-data </code><i>cumulative|peak</i></p>
<dd>This OEM command can reset the cumulative or peak power consumption data (viewed via <code>get-power-consumption-data</code>). Command confirmed to work on Dell Poweredge R610, R710, R905, M610, M610x, and M910.</p>
<dt><code>power-supply-info</code></p>
<dd>This OEM command can read and output power supply ratings and other information. This OEM command requires access to the SDR. Command confirmed to work on Dell Poweredge R610, R710, and M610.</p>
<dt><code>get-instantaneous-power-consumption-data </code><i>power_supply_instance</i></p>
<dd>This OEM command can read instantaneous power consumption data. If a power supply instance number is specified, only data for that instance will be gathered. Otherwise, collective power consumption will be gathered. Command confirmed to work on Dell Poweredge R610, R710, M610, M610x, and M910.</p>
<dt><code>get-power-head-room</code></p>
<dd>This OEM command can read power head room. Command confirmed to work on Dell Poweredge R610 and R710 (Dell 11G Poweredge systems).</p>
<dt><code>get-power-consumption-statistics </code><i>average|max|min</i></p>
<dd>This OEM command can read average, max, or min power consumption history. Command confirmed to work on Dell Poweredge R610, R710, M610, M610x, and M910.</p>
<dt><code>get-power-capacity</code></p>
<dd>This OEM command can read the current power capacity. Command confirmed to work on Dell Poweredge R610, R710, M610, M610x, and M910.</p>
<dt><code>set-power-capacity </code><i>power-capacity</i></p>
<dd>This OEM command can write the current power capacity (specified in Watts). Command confirmed to work on Dell Poweredge R610 and R710 (Dell 11G Poweredge systems).</p>
<dt><code>get-power-capacity-status</code></p>
<dd>This OEM command can determine if the current power capacity is enabled or disabled. Command confirmed to work on Dell Poweredge R610, R710, M610, M610x, and M910.</p>
<dt><code>set-power-capacity-status </code><i>enable|disable</i></p>
<dd>This OEM command can configure the current power capacity to be enabled or disabled. Command confirmed to work on Dell Poweredge R610 and R710 (Dell 11G Poweredge systems).</p>
<dt><code>get-chassis-identify-status</code></p>
<dd>This OEM command will retrieve the current chassis identify (i.e. LED) status. Command confirmed to work on Dell Poweredge 2900, 2950, R610, R710, R905, M600, M610, M610x, and M910.</p>
<dt><code>power-monitoring-over-interval </code><i>interval</i> <i>systempower|cpu1|cpu2|cpu3|cpu4|memory1|memory2|memory3|memory4|drives|fans|pciecards|gpucables</i></p>
<dd>This OEM command will retrieve power consumption information from a specified subsystem for a specified interval time. If the interval is between 30 and 900s, the average, minimum, and maximum power value can also be retrieved. If the interval is between 5 and 30 seconds, only the average power consumption can be returned. See <i>power-monitoring-interval-range</i> below to determine legal intervals for each subsystem. Command confirmed to work on Dell Poweredge R720 (Dell 12G Poweredge systems).</p>
<dt><code>power-monitoring-interval-range </code><i>systempower|cpu1|cpu2|cpu3|cpu4|memory1|memory2|memory3|memory4|drives|fans|pciecards|gpucables</i></p>
<dd>This OEM command will retrieve the monitoring intervals for a specified subsystem. Command confirmed to work on Dell Poweredge R720 (Dell 12G Poweredge systems).</p>
<dt><code>get-last-post-code</code></p>
<dd>This OEM command will retrieve the last POST code and error string for it. Command confirmed to work on Dell Poweredge R720.</p>
<dt><code>slot-power-toggle </code><i>slot-number</i></p>
<dd>This OEM command will perform a power toggle on a PCIe slot. The PCIe slot number can range from 1 to 16. Command confirmed to work on Dell Poweredge C410x.</p>
<dt><code>slot-power-control </code><i>platform-model</i> <i>on|off|status</i> <i>slot-number</i></p>
<dd>This OEM command will perform a power control action on a PCIe slot. This OEM extension is tied very closely to a platform, so a supported platform must be specified. The currently supported <i>platform-model</i> options are <i>C410x</i>. The <i>on</i> action powers on a slot, <i>off</i> powers off a slot, and <i>status</i> returns if the current power is on or off. If the current power status is on, an <i>on</i> action does nothing. Similarly, if the current power status is off, an <i>off</i> action does nothing. The <i>on</i>, <i>off</i>, and <i>status</i> slot power actions are not native and are emulated through a combination of a power toggle (using <i>slot-power-toggle</i> above) and the reading of PCIe slot watt sensors. The PCIe slot number can range from 1 to 16. Command confirmed to work on Dell Poweredge C410x.</p>
<dt><code>get-port-map</code></p>
<dd>This OEM command will retrieve the current iPASS mapping to PCIe controllers/slots. Command confirmed to work on Dell Poweredge C410x.</p>
<dt><code>set-port-map </code><i>jumper|bmc</i> <i>ipass-mapping</i> <i>1:2|1:4|1:8</i></p>
<dd>This OEM command will set an iPass mapping to PCIe controllers/slots. <i>jumper</i> or <i>bmc</i> must be specified to indicate if iPass mappings will be controlled via jumpers on the system or via a BMC/IPMI. In order for reconfiguration to be done via <code>ipmi-oem</code>, the user must select <i>bmc</i>. The <i>ipass-mapping</i> determines which iPass ports will be mapped. <i>1:2</i>, <i>1:4</i>, and <i>1:8</i> determine the mapping that should be set. See details below for specific platforms. Command confirmed to work on Dell Poweredge C410x. For the Dell Poweredge C410x, the <i>ipass-mapping</i> ranges from 1 to 4. <i>1</i> refers to iPass 1 and 5, <i>2</i> to 2 and 6, <i>3</i> to 3 and 7, and <i>4</i> to 4 and 8. For the platform <i>C410x</i>, PCIe slots 1, 2, 3, 4, 13, 14, 15, and 16 are attached to iPass 1, 2, 3, and 4. PCIe slots 5, 6, 7, 8, 9, 10, 11, and 12 are attached to iPass 5, 6, 7, and 8. For example, if <i>1:2</i> is set on <i>mapping-number</i> <i>1</i>, PCIe slots 1 and 15 will be assigned to iPass 1 and slots 2 and 16 will be assigned to iPass 5. if <i>1:4</i> is chosen, PCIe slots 1, 2, 15, and 16 will be assigned to iPass 1 and iPass 5 will not be used.</dl>
</dl>
<dt><code>Fujitsu</code></p>
<dd>
<dl>
<dd>
<dl>
<dt><code>get-power-on-source</code></p>
<dd>This OEM command will return the reason for the most recent Power On. Command confirmed to work on Fujitsu RX100 S5.</p>
<dt><code>get-power-off-source</code></p>
<dd>This OEM command will return the reason for the most recent Power Off. Command confirmed to work on Fujitsu RX100 S5.</p>
<dt><code>get-remote-storage-status </code><i>connection_number</i></p>
<dd>This OEM command will return the connection and/or status of remote storage. <i>connection_number</i> currently supports a range of 0-1. Command confirmed to work on Fujitsu RX100 S5.</p>
<dt><code>get-system-status</code></p>
<dd>This OEM command will return the current system status. Command confirmed to work on Fujitsu RX100 S5.</p>
<dt><code>get-eeprom-version-info </code><i>eeprom_number</i></p>
<dd>This OEM command will return the current version info for various hardware elements, including firmware, SDR, and boot revision. <i>eeprom_number</i> currently supports a range of 0-1. Command confirmed to work on Fujitsu RX100 S5.</p>
<dt><code>get-identify-led</code></p>
<dd>This OEM command will get the current identify LED status. Command confirmed to work on Fujitsu RX100 S5.</p>
<dt><code>set-identify-led </code><i>on|off</i></p>
<dd>This OEM command will set the current identify LED status. Command confirmed to work on Fujitsu RX100 S5.</p>
<dt><code>get-error-led</code></p>
<dd>This OEM command will get the current error LED status. Command confirmed to work on Fujitsu RX100 S5.</p>
<dt><code>get-sel-entry-long-text </code><i>sel_record_id</i></p>
<dd>This OEM command will retrieve the Fujitsu specific string interpretation of a SEL record. This command may be useful for interpreting Fujitsu OEM hex codes found in the SEL. A specific SEL record ID must be specified. Please see <code><a href="/docs/linux/man/8-ipmi-sel/">ipmi-sel</a>(8),</code> for retrieving SEL records. Command confirmed to work on Fujitsu RX100 S5.</dl>
</dl>
<dt><code>IBM</code></p>
<dd>
<dl>
<dd>
<dl>
<dt><code>get-led</code></p>
<dd>This OEM command will get the current LED status. This OEM command requires access to the SDR. Command confirmed to work on IBM x3755.</dl>
</dl>
<dt><code>Intel</code></p>
<dd>
<dl>
<dd>
<dl>
<dt><code>get-smtp-config </code><i>[channel-number]</i></p>
<dd>This OEM command will get the current SMTP configuration on the IPMI card. By default, configuration for every LAN channel will be output. If a <i>channel-number</i> is specified, only that specific channel number&#8217;s configuration will be output. Command confirmed to work on Intel S5500WB (Penguin Computing Relion 700) and Intel S2600JF (Appro 512X).</p>
<dt><code>set-smtp-config </code><i>[channel-number]</i> <i>KEY=VALUE &#8230;</i></p>
<dd>This OEM command will set the current SMTP configuration on the IPMI card. By default, configuration will be done for all LAN channels. If a <i>channel-number</i> is specified, only that specific channel number&#8217;s configuration will be configured. The possible keys and values are <i>smtp=enable|disable</i>, <i>smtpserveraddress=ipaddress</i>, <i>smtpusername=string</i>, <i>userpassword=string</i>, <i>emailaddress=string</i>, <i>subject=string</i>, <i>messagecontent=string</i>, <i>senderemailaddress=string</i>, and <i>smtphostname=string</i>. Multiple key=value pairs may be specified. If no key=value pairs are specifed, available pairs are output. Command confirmed to work on Intel S5500WB (Penguin Computing Relion 700) and Intel S2600JF (Appro 512X).</p>
<dt><code>get-power-restore-delay</code></p>
<dd>This OEM command will retrieve the power on delay. The power on delay is a delay that occurs whenever the BMC turns on the system according to the Power Restore Policy setting. It does not take effect otherwise (i.e. power button or Chassis Control). Command confirmed to work on Intel S2600JF (Appro 512X).</p>
<dt><code>set-power-restore-delay </code><i>seconds</i></p>
<dd>This OEM command will set the power on delay. (See <i>get-power-restore-delay</i> above for description on power restore delay). Command confirmed to work on Intel S2600JF (Appro 512X).</p>
<dt><code>restore-configuration</code></p>
<dd>This OEM command will restore BMC configuration values back to default values. The command will spin until the restore is confirmed to be complete. Command configured to work on Intel S5500WB (Penguin Computing Relion 700) and Intel S2600JF (Appro 512X). After running this command, the BMC must be reset to return it to functioning status. This may be accomplished by executing a cold-reset with <code><a href="/docs/linux/man/8-bmc-device/">bmc-device</a>(8).</code></dl>
</dl>
<dt><code>IntelNM (Intel Node Manager)</code></p>
<dd></dl>
<p> The following OEM commands operate on Intel chipsets with Node Manager support. They all require access to the SDR. They may work on multiple vendors motherboards. </p>
<dl>
<dd>
<dl>
<dt><code>get-node-manager-statistics </code><i>[domainid=num]</i> <i>[policyid=num]</i></p>
<dd>This OEM command will output the Intel Node Manager statistics. The user may optionally specify a <i>domainid</i> or <i>policyid</i>. The default <i>domainid</i> is 0. If a <i>policyid</i> is specified, per policy statistics will be output, otherwise global statistics will be output. Command confirmed to work on Intel S5500WB (Penguin Computing Relion 700), Inventec 5441/5442 (Dell Xanadu II/III), Quanta S99Q (Dell FS12-TY), Quanta QSSC-S4R (Appro GB812X-CN), Supermicro X9DRi-F, Intel S2600JF (Appro 512X).</p>
<dt><code>reset-node-manager-statistics </code><i>[domainid=num]</i> <i>[policyid=num]</i></p>
<dd>This OEM command will reset the Intel Node Manager statistics. The user may optionally specify a <i>domainid</i> or <i>policyid</i>. The default <i>domainid</i> is 0. If a <i>policyid</i> is specified, per policy statistics will be reset, otherwise global statistics will be reset. Command confirmed to work on Intel S5500WB (Penguin Computing Relion 700), Inventec 5441/5442 (Dell Xanadu II/III), Quanta S99Q (Dell FS12-TY), Quanta QSSC-S4R (Appro GB812X-CN), Supermicro X9DRi-F, Intel S2600JF (Appro 512X).</p>
<dt><code>get-node-manager-capabilities </code><i>[domainid=num]</i> <i>[policytrigger=none|inlet]</i> <i>[policytype=powercontrol]</i></p>
<dd>This OEM command will output the current capabilities of the Intel Node manager. The user may optionally specify a <i>domainid</i>, <i>policytrigger</i>, or <i>policytype</i>. The default <i>domainid</i> is 0. If any particular option is not specified, all permutations of the remaining options will be used in an attempt to output all capabilities of the system. Command confirmed to work on Intel S2600JF (Appro 512X).</p>
<dt><code>node-manager-policy-control </code><i>&lt;enable|disable&gt;</i> <i>[domainid=num]</i> <i>[policyid=num]</i></p>
<dd>This OEM command will enable or disable the current global, domain, or policies used by the Intel Node Manager. If no <i>domainid</i> is specified, then the Node Manager will be enabled or globally disabled. If a <i>domainid</i> is specified, only that domain will be enabled or disabled. If both a <i>domainid</i> and <i>policyid</i> are specified, only that specific policy within the domain will be specified. This OEM command will be required to enable or disable policies before many of the commands below can be used for configuration or use. Command confirmed to work on Intel S2600JF (Appro 512X).</p>
<dt><code>get-node-manager-policy </code><i>[domainid=num]</i> <i>[policyid=num]</i></p>
<dd>This OEM command will get the current node manager policy. If no <i>domainid</i> is specified, all policies for all domain IDs and policy Ids will be attempted to be output. If a <i>domainid</i> is specified but a <i>policyid</i> is not, all policies within a domain will be attempted to be output. If the verbose option is set, additional error messages will be output as valid policies are being searched for. Command confirmed to work on Intel S2600JF (Appro 512X).</p>
<dt><code>set-node-manager-policy </code><i>domainid=num</i> <i>policyid=num</i> <i>policytrigger=none|inlet</i> <i>powerlimit=watts</i> <i>correctiontimelimit=ms</i> <i>policytriggerlimit=num</i> <i>statisticsreportingperiod=seconds</i> <i>[policystate=enable|disable]</i> <i>[policyexceptionaction=alert|shutdown]</i></p>
<dd>This OEM command will add or modify an indicated policy ID from the domain ID. Most of the fields above are required, although they can be listed in any order. By default any created/modified policy will be enabled, however this can be overridden by <i>policystate</i>. <i>policyexceptionaction</i> may be specified multiple times to configure multiple actions or can be skipped to configure no actions. When the <i>policytrigger</i> is configured as <i>none</i>, the trigger that will lead to exception actions is the value specified by the <i>powerlimit</i>. When the <i>policytrigger</i> is <i>inlet</i>, the tigger that will lead to exception actions is the value specified by <i>policytriggerlimit</i>. The units of the <i>policytriggerlimit</i> will depend on the <i>policytrigger</i> selected. Most notably, if the <i>policytrigger</i> is <i>inlet</i>, which refers to inlet temperature, the units of policytriggerlimit will be in Celsius. When the <i>policytrigger</i> is <i>none</i>, the <i>policytriggerlimit</i> is ignored internally by the Intel Node Manager, but a value must still be specified for configuration. Typically configuring it to 0 is more than sufficient. The <i>correctiontimelimit</i> specifies the time the Node Manager must take corrective actions to bring back the system within limits before taking the actions specified in <i>policyexceptionaction</i>. <i>statisticsreportingperiod</i> is the number of seconds that measured power will be averaged for reporting. Please see <code>get-node-manager-policy</code> to determine proper ranges for <i>powerlimit</i>, <i>correctiontimelimit</i>, <i>policytriggerlimit</i>, and <i>statisticsreportingperiod</i>. Command confirmed to work on Intel S2600JF (Appro 512X).</p>
<dt><code>remove-node-manager-policy </code><i>domainid=num</i> <i>policyid=num</i></p>
<dd>This OEM command will remove the indicated policy ID from the domain ID. Both the <i>domainid</i> and <i>policyid</i> are required. Command confirmed to work on Intel S2600JF (Appro 512X).</p>
<dt><code>get-node-manager-alert-thresholds </code><i>[domainid=num]</i> <i>[policyid=num]</i></p>
<dd>This OEM command will get the current alert thresholds. If no <i>domainid</i> is specified, all alert thresholds for domain IDs and policy Ids will be attempted to be output. If a <i>domainid</i> is specified but a <i>policyid</i> is not, all alert thresholds within a domain will be attempted to be output. The units of the thresholds will depend on the configuration of the current policy. If the verbose option is set, additional error messages will be output as valid policies are being searched for. Command confirmed to work on Intel S2600JF (Appro 512X).</p>
<dt><code>set-node-manager-alert-thresholds </code><i>domainid=num</i> <i>policyid=num</i> <i>[threshold1=num]</i> <i>[threshold2=num]</i> <i>[threshold3=num]</i></p>
<dd>This OEM command will set the alert thresholds for a given domain ID and policy ID. Up to three thresholds can be specified, The units of the thresholds will depend on the configuration of the current policy. Command confirmed to work on Intel S2600JF (Appro 512X).</p>
<dt><code>get-node-manager-policy-suspend-periods </code><i>[domainid=num]</i> <i>[policyid=num]</i></p>
<dd>This OEM command will get the current policy suspend periods. Suspend periods will temporarily disable Intel Node Manager policies at configured times. If no <i>domainid</i> is specified, all suspend periods for domain IDs and policy Ids will be attempted to be output. If a <i>domainid</i> is specified but a <i>policyid</i> is not, all suspend periods within a domain will be attempted to be output. If the verbose option is set, additional error messages will be output as valid policies are being searched for. Suspend start and stop times are output in 24 hour format. Command confirmed to work on Intel S2600JF (Appro 512X).</p>
<dt><code>set-node-manager-policy-suspend-periods </code><i>domainid=num</i> <i>policyid=num</i> <i>suspendperiodstart1=time</i> <i>suspendperiodstop1=time</i> <i>suspendperiodrepeat1=monday|tuesday|wednesday|thursday|friday|saturday|sunday</i> &#8230;</p>
<dd>This OEM command will set the policy suspend periods for a policy. Suspend periods will temporarily disable Intel Node Manager policies at configured times. Up to 5 suspend periods can be specified by <i>suspendperiodstartX</i>, <i>suspendperiodstopX</i>, <i>suspendperiodrepeatX</i>. <i>suspendperiodstart</i> and <i>suspendperiodstop</i> specify the start and stop time since midnight for a suspend period. The time should be specified in 24 hour format (i.e. 02:00 or 13:40). Note that suspend periods are configured in multiples of 6 minutes, therefore the stored configuration may be rounded to a slightly alternate configuration. <i>suspendperiodrepeat</i> indicates the days in which the suspend period shall be enabled. The option can be specified multiple times to configure multiple times. Command confirmed to work on Intel S2600JF (Appro 512X).</p>
<dt><code>set-node-manager-power-draw-range </code><i>domainid=num</i> <i>minpowerdrawrange=watts</i> <i>maxpowerdrawrange=watts</i></p>
<dd>This OEM command will set the power draw range for a given domain ID. After this configuration, any policies within the domain ID that are outside of this range will be disabled as needed. The current power draw range can be read via the <code>get-node-manager-capabilities</code> above. Command confirmed to work on Intel S2600JF (Appro 512X).</p>
<dt><code>get-node-manager-version</code></p>
<dd>This OEM command will output the current Intel Node Manager version information. Command confirmed to work on Intel S5500WB (Penguin Computing Relion 700), Inventec 5441/5442 (Dell Xanadu II/III), Quanta S99Q (Dell FS12-TY), Quanta QSSC-S4R (Appro GB812X-CN), Intel S2600JF (Appro 512X).</dl>
</dl>
<dl>
<dt><code>Inventec</code></p>
<dd>
<dl>
<dd>
<dl>
<dt><code>get-nic-mode</code></p>
<dd>This OEM command will determine the current NIC mode as dedicated or shared. Dedicated indicates IPMI is only available on the dedicated management port. Shared indicates IPMI is also available on one of the primary ethernet ports. Command confirmed to work on Inventec 5441/5442 (Dell Xanadu II/III).</p>
<dt><code>set-nic-mode </code><i>dedicated|shared</i></p>
<dd>This OEM command will set the current NIC mode to dedicated or shared. (See <i>get-nic-mode</i> above for description on dedicated vs. shared mode.) This OEM command may internally reset the BMC, making the BMC unusable for awhile. Command confirmed to work on Inventec 5441/5442 (Dell Xanadu II/III).</p>
<dt><code>get-mac-address</code></p>
<dd>This command will retrieve the BMC MAC address. This is actually not an OEM command, but rather the normal IPMI MAC address command (identical to what is used in the <code><a href="/docs/linux/man/8-bmc-config/">bmc-config</a>(8)</code> tool). This command is placed here for convenience.</p>
<dt><code>set-mac-address </code><i>dedicated|shared</i> <i>MACADDR</i></p>
<dd>This OEM command will set the dedicated or shared BMC MAC address. (See <i>get-nic-mode</i> above for description on dedicated vs. shared mode.) The BMC MAC address cannot be set through the normal IPMI MAC address command (what is used in the <code><a href="/docs/linux/man/8-bmc-config/">bmc-config</a>(8)</code> tool). The MACADDR should be specified in XX:XX:XX:XX:XX:XX form. A shared BMC MAC address may conflict with normal communication ethernet communication on the primary ethernet port. Users may wish to configuration an alternate MAC address instead. After configuration of the MAC address, the BMC must be reset. This may be accomplished by executing a cold-reset with <code><a href="/docs/linux/man/8-bmc-device/">bmc-device</a>(8).</code> Command confirmed to work on Inventec 5441/5442 (Dell Xanadu II/III).</p>
<dt><code>get-bmc-services</code></p>
<dd>This OEM command will display the currently enabled BMC services. Command confirmed to work on Inventec 5441/5442 (Dell Xanadu II/III).</p>
<dt><code>set-bmc-services </code><i>enable|disable</i> <i>all|kvm|http|ssh</i></p>
<dd>This OEM command will enable or disable other BMC services besides IPMI. <i>all</i> can be specified to enable/disable all services, <i>kvm</i> specifies KVM and Virtual Storage, <i>http</i> specifies HTTP and HTTPS, and <i>ssh</i> specifies both SSH and Telnet. Command confirmed to work on Inventec 5441/5442 (Dell Xanadu II/III).</p>
<dt><code>get-authentication-config</code></p>
<dd>This OEM command will display additional OEM authentication settings. (See <i>set-authentication-config</i> below for description on outputs.) Command confirmed to work on Inventec 5441/5442 (Dell Xanadu II/III).</p>
<dt><code>set-authentication-config </code><i>KEY=VALUE &#8230;</i></p>
<dd>This OEM command will set additional OEM authentication settings on the IPMI card. The possible keys and values are <i>maxauthenticationfailures=count</i>, <i>lockoutwindow=seconds</i>, <i>lockouttime=seconds</i>, and <i>httpsportnumber=num</i>. <i>maxauthenticationfailures</i> specifies the maximum number of allowed authentication failures. <i>lockoutwindow</i> specifies the window of time the authentication failure count can be reached in to disable a user. <i>lockouttime</i> specifies the time period a user is disabled if the authentication failure count is reached. Setting 0 to any of the settings will disable the lockout feature. Each time any of these settings is modified, the authentication failure count of each enabled user is reset to 0. Multiple key=value pairs may be specified. If no key=value pairs are specifed, available pairs are output. Command confirmed to work on Inventec 5441/5442 (Dell Xanadu II/III).</p>
<dt><code>get-account-status</code></p>
<dd>This OEM command will output the current account status of users on the BMC. This command is particularly usefor for determinining which users in the system may have been locked out via authentication failures configured via <i>set-authentication-config</i>. Command confirmed to work on Inventec 5441/5442 (Dell Xanadu II/III).</p>
<dt><code>get-dns-config</code></p>
<dd>This OEM command will display additional OEM DNS settings. (See <i>set-dns-config</i> below for description on outputs.) Command confirmed to work on Inventec 5441/5442 (Dell Xanadu II/III).</p>
<dt><code>set-dns-config </code><i>KEY=VALUE &#8230;</i></p>
<dd>This OEM command will set additional OEM DNS settings on the IPMI card. The possible keys and values are <i>dnsdhcp=enable|disable</i>, <i>dnsserver1=ipaddress</i>, <i>dnsserver2=ipaddress</i>, <i>dnsregisterbmc=enable|disable</i>, <i>dnsbmchostname=string</i>, <i>dnsdomainnamedhcp=enable|disable</i>, and <i>dnsdomainname=string</i>. <i>dnsdhcp</i> specifies if the DNS server IP addresses should be assigned from the DHCP server. <i>dnsserver1</i> and <i>dnsserver2</i> specify the IP addess for server 1 and 2 respectively. These fields are read only if <i>dnsdhcp</i> and DHCP are enabled. <i>dnsregisterbmc</i> specifies if the BMC host name is registered via the DNS server. <i>dnsbmchostname</i> specifies the BMC host name. This field is read only if <i>dnsregisterbmc</i> is enabled. <i>dnsdomainnamedhcp</i> specifies if the DNS domainname should be assigned from the DHCP server. <i>dnsdomainname</i> specifies the DNS domain name string. This field is read only if <i>dnsdomainnamedhcp</i> is enabled. Multiple key=value pairs may be specified. If no key=value pairs are specifed, available pairs are output. Command confirmed to work on Inventec 5441/5442 (Dell Xanadu II/III).</p>
<dt><code>get-web-server-config</code></p>
<dd>This OEM command will get the current web server configuration on the IPMI card. Command confirmed to work on Inventec 5441/5442 (Dell Xanadu II/III).</p>
<dt><code>set-web-server-config </code><i>KEY=VALUE &#8230;</i></p>
<dd>This OEM command will set the current web server configuration on the IPMI card. The possible keys and values are <i>webserver=enable|disable</i>, <i>webservertimeout=seconds</i>, <i>httpportnumber=num</i>, and <i>httpsportnumber=num</i>. Multiple key=value pairs may be specified. If no key=value pairs are specifed, available pairs are output. Command confirmed to work on Inventec 5441/5442 (Dell Xanadu II/III).</p>
<dt><code>get-power-management-config</code></p>
<dd>This OEM command will get the current power management configuration on the IPMI card. Command confirmed to work on Inventec 5441/5442 (Dell Xanadu II/III).</p>
<dt><code>set-power-management-config </code><i>KEY=VALUE &#8230;</i></p>
<dd>This OEM command will set the current power management configuration on the IPMI card. The possible keys and values are <i>dpnmpowermanagement=enable|disable</i>, <i>powerstaggeringacrecovery=immediate|auto|user</i>, <i>powerondelay=seconds</i>, and <i>maxpowerondelay=seconds</i>. <i>dpnmpowermanagement</i> enables or diables DPNM, Dynamic Power Node Management. For <i>powerstaggeringacrecovery</i>, <i>immediate</i> specifies no delay, <i>auto</i> generates a delay time between the minimum and maximum configured, and <i>user</i> uses the user defined time defined by <i>powerondelay</i>. <i>powerondelay</i> must be within the minimum and maximum power on delay times. Multiple key=value pairs may be specified. If no key=value pairs are specifed, available pairs are output. Command confirmed to work on Inventec 5441/5442 (Dell Xanadu II/III).</p>
<dt><code>get-sol-idle-timeout</code></p>
<dd>This OEM command will get the SOL idle timeout. Command confirmed to work on Inventec 5441/5442 (Dell Xanadu II/III).</p>
<dt><code>set-sol-idle-timeout </code><i>idle-timeout</i></p>
<dd>This OEM command will set the SOL idle timeout. The <i>idle-timeout</i> is one-based, max of 65535, in 1 minute increments (e.g. 1 = 1 minute), 0 or &quot;none&quot; will configure no timeout. Command confirmed to work on Inventec 5441/5442 (Dell Xanadu II/III).</p>
<dt><code>get-telnet-ssh-redirect-status</code></p>
<dd>This OEM command will get the telnet/SSH redirect status. Command confirmed to work on Inventec 5442 (Dell Xanadu III).</p>
<dt><code>set-telnet-ssh-redirect-status </code><i>enable|disable</i></p>
<dd>This OEM command will enable or disable telnet/SSH redirect status. Command confirmed to work on Inventec 5442 (Dell Xanadu III).</p>
<dt><code>get-board-id</code></p>
<dd>This OEM command can get the board ID. Command confirmed to work on Inventec 5441/5442 (Dell Xanadu II/III).</p>
<dt><code>set-board-id </code><i>ID</i></p>
<dd>This OEM command can set the board ID. Command confirmed to work on Inventec 5441/5442 (Dell Xanadu II/III).</p>
<dt><code>get-fcb-version</code></p>
<dd>This OEM command can get the fan control board (FCB) version number. Command confirmed to work on Inventec 5441/5442 (Dell Xanadu II/III).</p>
<dt><code>set-fcb-version </code><i>majorversion</i> <i>minorversion</i></p>
<dd>This OEM command can set the fan control board (FCB) version number. The <i>majorversion</i> and <i>minorversion</i> must be specified in hex. Command confirmed to work on Inventec 5441/5442 (Dell Xanadu II/III).</p>
<dt><code>get-sol-inactivity-timeout</code></p>
<dd>This OEM command will retrieve the SOL inactivity timeout. Command confirmed to work on Inventec 5441/5442 (Dell Xanadu II/III).</p>
<dt><code>set-sol-inactivity-timeout </code><i>inactivity-timeout</i></p>
<dd>This OEM command will set the SOL inactivity timeout. The <i>inactivity-timeout</i> is one-based, max of 65535, in 1 minute increments (e.g. 1 = 1 minute), 0 or &quot;none&quot; will configure no timeout. Command confirmed to work on Inventec 5441/5442 (Dell Xanadu II/III).</p>
<dt><code>restore-to-defaults </code><i>all|user|lan|sol|serial|pef</i></p>
<dd>This OEM command will restore certain BMC configuration sections back to default values. The command will spin until the reset is confirmed to be complete. Command confirmed to work on Inventec 5442 (Dell Xanadu III). After running this command, the BMC must be reset to return it to functioning status. This may be accomplished by executing a cold-reset with <code><a href="/docs/linux/man/8-bmc-device/">bmc-device</a>(8).</code></p>
<dt><code>read-eeprom </code><i>at24c256n</i></p>
<dd>This OEM command will read the specified eeprom. Command confirmed to work on Inventec 5441 (Dell Xanadu II) for <i>at24c256</i>.</p>
<dt><code>clear-eeprom </code><i>at24c256n</i></p>
<dd>This OEM command will clear the specified eeprom, overwriting all bytes with 0xFF. If the verbose option is set, progress percent will be output as the clearing is being done. Command confirmed to work on Inventec 5441 (Dell Xanadu II) for <i>at24c256</i>.</dl>
</dl>
<dt><code>Quanta</code></p>
<dd>
<dl>
<dd>
<dl>
<dt><code>get-nic-mode</code></p>
<dd>This OEM command will determine the current NIC mode as dedicated or shared. Dedicated indicates IPMI is only available on the dedicated management port. Shared indicates IPMI is also available on one of the primary ethernet ports. Command confirmed to work on Quanta S99Q (Dell FS12-TY).</p>
<dt><code>set-nic-mode </code><i>dedicated|shared</i></p>
<dd>This OEM command will set the current NIC mode to dedicated or shared. (See <i>get-nic-mode</i> above for description on dedicated vs. shared mode.) This OEM command may internally reset the BMC, making the BMC unusable for awhile. Command confirmed to work on Quanta S99Q (Dell FS12-TY).</p>
<dt><code>get-bmc-services</code></p>
<dd>This OEM command will display the currently enabled BMC services. Command confirmed to work on Quanta S99Q (Dell FS12-TY).</p>
<dt><code>set-bmc-services </code><i>enable|disable</i> <i>all|kvm|http|ssh</i></p>
<dd>This OEM command will enable or disable other BMC services besides IPMI. <i>all</i> can be specified to enable/disable all services, <i>kvm</i> specifies KVM and Virtual Storage, <i>http</i> specifies HTTP and HTTPS, and <i>ssh</i> specifies both SSH and Telnet. Command confirmed to work on Quanta S99Q (Dell FS12-TY).</p>
<dt><code>get-account-status</code></p>
<dd>This OEM command will output the current account status of users on the BMC. This command is particularly usefor for determinining which users in the system may have been locked out via authentication failures. Command confirmed to work on Quanta S99Q (Dell FS12-TY).</p>
<dt><code>get-dns-config</code></p>
<dd>This OEM command will display additional OEM DNS settings. (See <i>set-dns-config</i> below for description on outputs.) Command confirmed to work on Quanta S99Q (Dell FS12-TY).</p>
<dt><code>set-dns-config </code><i>KEY=VALUE &#8230;</i></p>
<dd>This OEM command will set additional OEM DNS settings on the IPMI card. The possible keys and values are <i>dnsdhcp=enable|disable</i>, <i>dnsserver1=ipaddress</i>, <i>dnsserver2=ipaddress</i>, <i>dnsregisterbmc=enable|disable</i>, <i>dnsbmchostname=string</i>, <i>dnsdomainnamedhcp=enable|disable</i>, and <i>dnsdomainname=string</i>. <i>dnsdhcp</i> specifies if the DNS server IP addresses should be assigned from the DHCP server. <i>dnsserver1</i> and <i>dnsserver2</i> specify the IP addess for server 1 and 2 respectively. These fields are read only if <i>dnsdhcp</i> and DHCP are enabled. <i>dnsregisterbmc</i> specifies if the BMC host name is registered via the DNS server. <i>dnsbmchostname</i> specifies the BMC host name. This field is read only if <i>dnsregisterbmc</i> is enabled. <i>dnsdomainnamedhcp</i> specifies if the DNS domainname should be assigned from the DHCP server. <i>dnsdomainname</i> specifies the DNS domain name string. This field is read only if <i>dnsdomainnamedhcp</i> is enabled. Multiple key=value pairs may be specified. If no key=value pairs are specifed, available pairs are output. Command confirmed to work on Quanta S99Q (Dell FS12-TY).</p>
<dt><code>get-web-server-config</code></p>
<dd>This OEM command will get the current web server configuration on the IPMI card. Command confirmed to work on Quanta S99Q (Dell FS12-TY).</p>
<dt><code>set-web-server-config </code><i>KEY=VALUE &#8230;</i></p>
<dd>This OEM command will set the current web server configuration on the IPMI card. The possible keys and values are <i>webserver=enable|disable</i>, <i>webservertimeout=seconds</i>, <i>httpportnumber=num</i>, and <i>httpsportnumber=num</i>. Multiple key=value pairs may be specified. If no key=value pairs are specifed, available pairs are output. Command confirmed to work on Quanta S99Q (Dell FS12-TY).</p>
<dt><code>get-power-management-config</code></p>
<dd>This OEM command will get the current power management configuration on the IPMI card. Command confirmed to work on Quanta S99Q (Dell FS12-TY).</p>
<dt><code>set-power-management-config </code><i>KEY=VALUE &#8230;</i></p>
<dd>This OEM command will set the current power management configuration on the IPMI card. The possible keys and values are <i>dpnmpowermanagement=enable|disable</i>, <i>powerstaggeringacrecovery=immediate|auto|user</i>, <i>powerondelay=seconds</i>, and <i>maxpowerondelay=seconds</i>. <i>dpnmpowermanagement</i> enables or diables DPNM, Dynamic Power Node Management. For <i>powerstaggeringacrecovery</i>, <i>immediate</i> specifies no delay, <i>auto</i> generates a delay time between the minimum and maximum configured, and <i>user</i> uses the user defined time defined by <i>powerondelay</i>. <i>powerondelay</i> must be within the minimum and maximum power on delay times. Multiple key=value pairs may be specified. If no key=value pairs are specifed, available pairs are output. Command confirmed to work on Quanta S99Q (Dell FS12-TY).</p>
<dt><code>get-sol-idle-timeout</code></p>
<dd>This OEM command will get the SOL idle timeout. Command confirmed to work on Quanta S99Q (Dell FS12-TY).</p>
<dt><code>set-sol-idle-timeout </code><i>idle-timeout</i></p>
<dd>This OEM command will set the SOL idle timeout. The <i>idle-timeout</i> is one-based, max of 65535, in 1 minute increments (e.g. 1 = 1 minute), 0 or &quot;none&quot; will configure no timeout. Command confirmed to work on Quanta S99Q (Dell FS12-TY).</p>
<dt><code>get-telnet-ssh-redirect-status</code></p>
<dd>This OEM command will get the telnet/SSH redirect status. Command confirmed to work on Quanta S99Q (Dell FS12-TY).</p>
<dt><code>set-telnet-ssh-redirect-status </code><i>enable|disable</i></p>
<dd>This OEM command will enable or disable telnet/SSH redirect status. Command confirmed to work on Quanta S99Q (Dell FS12-TY).</p>
<dt><code>reset-to-defaults </code><i>all|user|lan|sol|serial|pef</i></p>
<dd>This OEM command will reset certain BMC configuration sections back to default values. The command will spin until the reset is confirmed to be complete. Command confirmed to work on Quanta S99Q (Dell FS12-TY). After running this command, the BMC must be reset to return it to functioning status. This may be accomplished by executing a cold-reset with <code><a href="/docs/linux/man/8-bmc-device/">bmc-device</a>(8).</code></p>
<dt><code>get-processor-information </code><i>[processor-index]</i></p>
<dd>This OEM command will determine system processor information. By default, information about each processor will be output. If a <i>processor-index</i> is specified, only that specific processor will be output. Command confirmed to work on Quanta S99Q (Dell FS12-TY).</p>
<dt><code>read-mac-address </code><i>s99q</i> <i>dedicated|shared</i></p>
<dd>This command will read the currently configured dedicated or shared MAC address for a specified motherboard. It will read the MAC address directly from the BMC eeprom. Command confirmed to work on Quanta S99Q (Dell FS12-TY) for <i>s99q</i>.</p>
<dt><code>write-mac-address </code><i>s99q</i> <i>dedicated|shared</i> <i>MACADDR</i></p>
<dd>This OEM command will set the dedicated or shared BMC MAC address for a specified motherboard. It will be written directly to the BMC eeprom. (See <i>get-nic-mode</i> above for description on dedicated vs. shared mode.) The BMC MAC address cannot be set through the normal IPMI MAC address command (what is used in the <code><a href="/docs/linux/man/8-bmc-config/">bmc-config</a>(8)</code> tool). The MACADDR should be specified in XX:XX:XX:XX:XX:XX form. A shared BMC MAC address may conflict with normal communication ethernet communication on the primary ethernet port. Users may wish to configuration an alternate MAC address instead. After configuration of the MAC address, the BMC must be reset. This may be accomplished by executing a cold-reset with <code><a href="/docs/linux/man/8-bmc-device/">bmc-device</a>(8).</code> Command confirmed to work on Quanta S99Q (Dell FS12-TY) for <i>s99q</i>.</dl>
</dl>
<dt><code>Sun</code></p>
<dd>
<dl>
<dd>
<dl>
<dt><code>get-led</code></p>
<dd>This OEM command will output current LED mode. <i>off</i> indicates the LED is steady off, <i>on</i> indicates the LED is steady on, <i>standby</i> indicates the LED blinks at a 100ms on, 2900ms off rate, <i>slow</i> indicates the LED is blinking at 1Hz, and <i>fast</i> indicates the LED is blinking at 4Hz. If the verbose option is set, sensor names will be output with their entity ID and instance when appropriate. (Similar to the <i>&#8211;entity-sensor-names</i> option in <code>ipmi-sensors.)</code> This OEM command requires access to the SDR. Command confirmed to work on Sun Fire 4140 with ILOM.</p>
<dt><code>set-led </code><i>record_id</i> <i>off|on|standby|slow|fast</i></p>
<dd>This OEM command will configure LED modes. (See <i>get-led</i> above for description on LED modes.) This OEM command requires access to the SDR. Command confirmed to work on Sun Fire 4140 with ILOM.</dl>
</dl>
<dt><code>Supermicro</code></p>
<dd>
<dl>
<dd>
<dl>
<dt><code>extra-firmware-info</code></p>
<dd>This OEM command will output additional firmware version information. Command confirmed to work on Supermicro H8QME.</p>
<dt><code>reset-intrusion</code></p>
<dd>This OEM command will reset the motherboard intrusion flag after it has been triggered. For example, in <code>ipmi-sensors</code> or <code>ipmi-sel,</code> you may notice a &#8216;General Chassis Intrusion&#8217; if the motherboard chassis is not open, but was opened in the past. Command confirmed to work on Supermicro H8QME.</p>
<dt><code>get-bmc-services-status</code></p>
<dd>This OEM command will determine if non-IPMI services (e.g. ssh, http, https, vnc, etc.) are currently enabled or disabled on the BMC. Command confirmed to work on Supermicro X8DTG.</p>
<dt><code>set-bmc-services-status </code><i>enable|disable</i></p>
<dd>This OEM command will enable or disable all non-IPMI services on the BMC. This command can be used to enable or disable non-IPMI services such as ssh, http, https, and vnc. Command confirmed to work on Supermicro X8DTG.</dl>
</dl>
<dt><code>Wistron</code></p>
<dd>
<dl>
<dd>
<dl>
<dt><code>get-system-info </code><i>KEY</i></p>
<dd>This OEM command can retrieve the motherboard system information. Valid keys are <i>asset-tag</i>, <i>service-tag</i>, <i>product-name</i>. Command confirmed to work on Wistron / Dell Poweredge C6220.</p>
<dt><code>get-nic-mode</code></p>
<dd>This OEM command will determine the current NIC mode as dedicated or shared. Dedicated indicates IPMI is only available on the dedicated management port. Shared indicates IPMI is also available on one of the primary ethernet ports. Command confirmed to work on Wistron / Dell Poweredge C6220.</p>
<dt><code>set-nic-mode </code><i>dedicated|shared</i></p>
<dd>This OEM command will set the current NIC mode to dedicated or shared. (See <i>get-nic-mode</i> above for description on dedicated vs. shared mode.) After running this command, the BMC may need to be reset to finalize the configuration. This may be accomplished by executing a cold-reset with <code><a href="/docs/linux/man/8-bmc-device/">bmc-device</a>(8).</code> Command confirmed to work on Wistron / Dell Poweredge C6220.</p>
<dt><code>get-shared-nic-selection</code></p>
<dd>This OEM command will determine the current NIC IPMI is shared with if the mode is <i>shared</i>. (See <i>get-nic-mode</i> above for description on dedicated vs. shared mode.) Command confirmed to work on Wistron / Dell Poweredge C6220.</p>
<dt><code>set-shared-nic-selection </code><i>nic1|nic2|nic3|nic4|clear</i></p>
<dd>This OEM command will set the current NIC sharing selection. If the current NIC mode is <i>dedicated</i> it is advisable to clear this setting with the <i>clear</i> option. Command confirmed to work on Wistron / Dell Poweredge C6220.</p>
<dt><code>get-bmc-services</code></p>
<dd>This OEM command will display the currently enabled BMC services. Command confirmed to work on Wistron / Dell Poweredge C6220.</p>
<dt><code>set-bmc-services </code><i>enable|disable</i> <i>all|kvm|http|ssh|snmp|telnet</i></p>
<dd>This OEM command will enable or disable other BMC services besides IPMI. <i>all</i> can be specified to enable/disable all services, <i>kvm</i> specifies KVM and Virtual Storage, <i>http</i> specifies HTTP and HTTPS. Command confirmed to work on Wistron / Dell Poweredge C6220.</p>
<dt><code>get-account-status</code></p>
<dd>This OEM command will output the current account status of users on the BMC. This command is particularly usefor for determinining which users in the system may have been locked out via authentication failures. Command confirmed to work on Wistron / Dell Poweredge C6220.</p>
<dt><code>get-dns-config</code></p>
<dd>This OEM command will display additional OEM DNS settings. (See <i>set-dns-config</i> below for description on outputs.) Command confirmed to work on Wistron / Dell Poweredge C6220.</p>
<dt><code>set-dns-config </code><i>KEY=VALUE &#8230;</i></p>
<dd>This OEM command will set additional OEM DNS settings on the IPMI card. The possible keys and values are <i>dnsdhcp=enable|disable</i>, <i>dnsserver1=ipaddress</i>, <i>dnsserver2=ipaddress</i>, <i>dnsregisterbmc=enable|disable</i>, <i>dnsbmchostname=string</i>, <i>dnsdomainnamedhcp=enable|disable</i>, <i>dnsdomainname=string</i>, and <i>dnsregistrationdelay=seconds</i>. <i>dnsdhcp</i> specifies if the DNS server IP addresses should be assigned from the DHCP server. <i>dnsserver1</i> and <i>dnsserver2</i> specify the IP addess for server 1 and 2 respectively. These fields are read only if <i>dnsdhcp</i> and DHCP are enabled. <i>dnsregisterbmc</i> specifies if the BMC host name is registered via the DNS server. <i>dnsbmchostname</i> specifies the BMC host name. This field is read only if <i>dnsregisterbmc</i> is enabled. <i>dnsdomainnamedhcp</i> specifies if the DNS domainname should be assigned from the DHCP server. <i>dnsdomainname</i> specifies the DNS domain name string. This field is read only if <i>dnsdomainnamedhcp</i> is enabled. <i>dnsregistrationdelay</i> specifies the delay the BMC should take after the IPMI process is up and running. Multiple key=value pairs may be specified. If no key=value pairs are specifed, available pairs are output. Command confirmed to work on Wistron / Dell Poweredge C6220.</p>
<dt><code>get-web-server-config</code></p>
<dd>This OEM command will get the current web server configuration on the IPMI card. Command confirmed to work on Wistron / Dell Poweredge C6220.</p>
<dt><code>set-web-server-config </code><i>KEY=VALUE &#8230;</i></p>
<dd>This OEM command will set the current web server configuration on the IPMI card. The possible keys and values are <i>webserver=enable|disable</i>, <i>webservertimeout=seconds</i>, <i>httpportnumber=num</i>, and <i>httpsportnumber=num</i>. Multiple key=value pairs may be specified. If no key=value pairs are specifed, available pairs are output. Command confirmed to work on Wistron / Dell Poweredge C6220.</p>
<dt><code>get-power-management-config</code></p>
<dd>This OEM command will get the current power management configuration on the IPMI card. Command confirmed to work on Wistron / Dell Poweredge C6220.</p>
<dt><code>set-power-management-config </code><i>KEY=VALUE &#8230;</i></p>
<dd>This OEM command will set the current power management configuration on the IPMI card. The possible keys and values are <i>powerstaggeringacrecovery=immediate|auto|user</i>, <i>powerondelay=seconds</i>, and <i>maxpowerondelay=seconds</i>. For <i>powerstaggeringacrecovery</i>, <i>immediate</i> specifies no delay, <i>auto</i> generates a delay time between the minimum and maximum configured, and <i>user</i> uses the user defined time defined by <i>powerondelay</i>. <i>powerondelay</i> must be within the minimum and maximum power on delay times. Multiple key=value pairs may be specified. If no key=value pairs are specifed, available pairs are output. Command confirmed to work on Wistron / Dell Poweredge C6220.</p>
<dt><code>get-ipv6-settings</code></p>
<dd>This OEM command will get the current IPv6 settings on the IPMI card. Command confirmed to work on Wistron / Dell Poweredge C6220.</p>
<dt><code>set-ipv6-settings </code><i>KEY=VALUE &#8230;</i></p>
<dd>This OEM command will set the current IPv6 settings on the IPMI card. The possible keys and values are <i>ipv6=enable|disable</i>, <i>ipv6address=ipaddress</i>, <i>ipv6gatewayaddress=ipaddress</i>, <i>ipv6prefixlength=length</i>, <i>ipv6autoconfig=enable|disable</i>, <i>ipv6autodns=enable|disable</i>, <i>ipv6dnsserver1=ipaddress</i>, and <i>ipv6dnsserver2=ipaddress</i>. If no key=value pairs are specifed, available pairs are output. Some fields may be read-only on specific Poweredge systems. Command confirmed to work on Wistron / Dell Poweredge C6220.</p>
<dt><code>get-ipv6-trap-settings</code></p>
<dd>This OEM command will get the current IPv6 SNMP trap settings on the IPMI card. Command confirmed to work on Wistron / Dell Poweredge C6220.</p>
<dt><code>set-ipv6-trap-settings </code><i>index</i> <i>KEY=VALUE &#8230;</i></p>
<dd>This OEM command will set the current IPv6 SNMP trap settings on the IPMI card. The <i>index</i> indicates the index position for the configuration. It is followed by a set of configuration keys and values. The possible keys and values are <i>destinationtype=pet|oem1|oem2</i>, <i>alertacktimeout=seconds</i>, <i>retries=count</i>, and <i>ipv6snmptrapaddress=ipaddress</i>. If no key=value pairs are specifed, available pairs are output. Some fields may be read-only on specific Poweredge systems. Command confirmed to work on Wistron / Dell Poweredge C6220.</p>
<dt><code>get-sol-idle-timeout</code></p>
<dd>This OEM command will get the SOL idle timeout. Command confirmed to work on Wistron / Dell Poweredge C6220.</p>
<dt><code>set-sol-idle-timeout </code><i>idle-timeout</i></p>
<dd>This OEM command will set the SOL idle timeout. The <i>idle-timeout</i> is one-based, max of 65535, in 1 minute increments (e.g. 1 = 1 minute), 0 or &quot;none&quot; will configure no timeout. Command confirmed to work on Wistron / Dell Poweredge C6220.</p>
<dt><code>get-telnet-redirect-function</code></p>
<dd>This OEM command will get the telnet redirect function. Command confirmed to work on Wistron / Dell Poweredge C6220.</p>
<dt><code>set-telnet-redirect-function </code><i>disable|solenable|smashenable</i></p>
<dd>This OEM command will enable or disable telnet redirect function. Command confirmed to work on Wistron / Dell Poweredge C6220.</p>
<dt><code>get-dhcp-retry</code></p>
<dd>This OEM command will retrieve DHCP retry information. Wistron / Dell Poweredge C6220.</p>
<dt><code>set-dhcp-retry </code><i>retry-count</i> <i>retry-interval</i> <i>retry-timeout</i></p>
<dd>This OEM command will set DHCP retry information. The <i>retry-count</i> is one-based, max of 254, 0 or &quot;none&quot; will configure no retries, 255 or &quot;indefinite&quot; will configure constant retries. The <i>retry-interval</i> is one-based, in 10 second increments (e.g. 1 = 10 seconds). The <i>retry-timeout</i> is one-based, in 1 minute increments (e.g. 1 = 1 minute). After running this command, the BMC may need to be reset to finalize the configuration. This may be accomplished by executing a cold-reset with <code><a href="/docs/linux/man/8-bmc-device/">bmc-device</a>(8).</code> Command confirmed to work on Wistron / Dell Poweredge C6220.</p>
<dt><code>get-link-status-change-control</code></p>
<dd>This OEM command will get the current link status change control. If it reports &quot;Link Down Resilience Enabled&quot;, BMC firmware will do nothing upon detecting Link Status Change until the DHCP lease is expired. If it reports &quot;DHCP Re-Discovery Enabled&quot;, BMC firmware will perform DHCP Discovery upon detecting link status going down than back up. Command confirmed to work on Wistron / Dell Poweredge C6220..</p>
<dt><code>set-link-status-change-control </code><i>link_resilience|dhcp_rediscovery</i></p>
<dd>This OEM command will set the current NIC link status change control setting. (See <i>set-link-status-change-control</i> above for description of arguments). After running this command, the BMC may need to be reset to finalize the configuration. This may be accomplished by executing a cold-reset with <code><a href="/docs/linux/man/8-bmc-device/">bmc-device</a>(8).</code> Command confirmed to work on Wistron / Dell Poweredge C6220.</p>
<dt><code>set-password-policy &lt;enable|disable&gt;</code></p>
<dd>This OEM command will set the current password policy enforcement. If password policy is enabled, BMC passwords must meet the following requirements: Not contain the user&#8217;s name, be 8-14 characters long, and contain three of the following four, an English uppercase character (A-Z), an English lowercase character (a-z), a digit (0-9), a special character (!, $, #, %, etc.). Command confirmed to work on Wistron / Dell Poweredge C6220.</p>
<dt><code>read-proprietary-string</code></p>
<dd>This OEM command will read the proprietary string stored in the FRU. The proprietary string is a string the user may set for any management purpose. It can also be read via <code>ipmi-fru.</code> Command confirmed to work on Wistron / Dell Poweredge C6220.</p>
<dt><code>set-proprietary-string &lt;string&gt;</code></p>
<dd>This OEM command will write the proprietary string stored in the FRU. The maximum length string is 80 characters. Command confirmed to work on Wistron / Dell Poweredge C6220.</p>
<dt><code>clear-proprietary-string</code></p>
<dd>This OEM command will clear the proprietary string stored in the FRU. Command confirmed to work on Wistron / Dell Poweredge C6220.</dl>
</dl>
</dl>
<h2>Hostranged Support</h2>
<p>Multiple hosts can be input either as an explicit comma separated lists of hosts or a range of hostnames in the general form: prefix[n-m,l-k,&#8230;], where n &lt; m and l &lt; k, etc. The later form should not be confused with regular expression character classes (also denoted by []). For example, foo[19] does not represent foo1 or foo9, but rather represents a degenerate range: foo19. </p>
<p> This range syntax is meant only as a convenience on clusters with a prefixNN naming convention and specification of ranges should not be considered necessary &#8212; the list foo1,foo9 could be specified as such, or by the range foo[1,9]. </p>
<p> Some examples of range usage follow: </p>
<pre> foo[01-05] instead of foo01,foo02,foo03,foo04,foo05
 foo[7,9-10] instead of foo7,foo9,foo10
 foo[0-3] instead of foo0,foo1,foo2,foo3</pre>
<p>As a reminder to the reader, some shells will interpret brackets ([ and ]) for pattern matching. Depending on your shell, it may be necessary to enclose ranged lists within quotes. </p>
<p> When multiple hosts are specified by the user, a thread will be executed for each host in parallel up to the configured fanout (which can be adjusted via the <code>-F</code> option). This will allow communication to large numbers of nodes far more quickly than if done in serial. </p>
<p> By default, standard output from each node specified will be output with the hostname prepended to each line. Although this output is readable in many situations, it may be difficult to read in other situations. For example, output from multiple nodes may be mixed together. The <code>-B</code> and <code>-C</code> options can be used to change this default. </p>
<p> In-band IPMI Communication will be used when the host &quot;localhost&quot; is specified. This allows the user to add the localhost into the hostranged output.</p>
<h2>General Troubleshooting</h2>
<p>Most often, IPMI problems are due to configuration problems. </p>
<p> IPMI over LAN problems involve a misconfiguration of the remote machine&#8217;s BMC. Double check to make sure the following are configured properly in the remote machine&#8217;s BMC: IP address, MAC address, subnet mask, username, user enablement, user privilege, password, LAN privilege, LAN enablement, and allowed authentication type(s). For IPMI 2.0 connections, double check to make sure the cipher suite privilege(s) and K_g key are configured properly. The <code><a href="/docs/linux/man/8-bmc-config/">bmc-config</a>(8)</code> tool can be used to check and/or change these configuration settings. </p>
<p> Inband IPMI problems are typically caused by improperly configured drivers or non-standard BMCs. </p>
<p> In addition to the troubleshooting tips below, please see WORKAROUNDS below to also if there are any vendor specific bugs that have been discovered and worked around. </p>
<p> Listed below are many of the common issues for error messages. For additional support, please e-mail the &lt;freeipmi-users [at] gnu.org&gt; mailing list. </p>
<p> &quot;username invalid&quot; &#8211; The username entered (or a NULL username if none was entered) is not available on the remote machine. It may also be possible the remote BMC&#8217;s username configuration is incorrect. </p>
<p> &quot;password invalid&quot; &#8211; The password entered (or a NULL password if none was entered) is not correct. It may also be possible the password for the user is not correctly configured on the remote BMC. </p>
<p> &quot;password verification timeout&quot; &#8211; Password verification has timed out. A &quot;password invalid&quot; error (described above) or a generic &quot;session timeout&quot; (described below) occurred. During this point in the protocol it cannot be differentiated which occurred. </p>
<p> &quot;k_g invalid&quot; &#8211; The K_g key entered (or a NULL K_g key if none was entered) is not correct. It may also be possible the K_g key is not correctly configured on the remote BMC. </p>
<p> &quot;privilege level insufficient&quot; &#8211; An IPMI command requires a higher user privilege than the one authenticated with. Please try to authenticate with a higher privilege. This may require authenticating to a different user which has a higher maximum privilege. </p>
<p> &quot;privilege level cannot be obtained for this user&quot; &#8211; The privilege level you are attempting to authenticate with is higher than the maximum allowed for this user. Please try again with a lower privilege. It may also be possible the maximum privilege level allowed for a user is not configured properly on the remote BMC. </p>
<p> &quot;authentication type unavailable for attempted privilege level&quot; &#8211; The authentication type you wish to authenticate with is not available for this privilege level. Please try again with an alternate authentication type or alternate privilege level. It may also be possible the available authentication types you can authenticate with are not correctly configured on the remote BMC. </p>
<p> &quot;cipher suite id unavailable&quot; &#8211; The cipher suite id you wish to authenticate with is not available on the remote BMC. Please try again with an alternate cipher suite id. It may also be possible the available cipher suite ids are not correctly configured on the remote BMC. </p>
<p> &quot;ipmi 2.0 unavailable&quot; &#8211; IPMI 2.0 was not discovered on the remote machine. Please try to use IPMI 1.5 instead. </p>
<p> &quot;connection timeout&quot; &#8211; Initial IPMI communication failed. A number of potential errors are possible, including an invalid hostname specified, an IPMI IP address cannot be resolved, IPMI is not enabled on the remote server, the network connection is bad, etc. Please verify configuration and connectivity. </p>
<p> &quot;session timeout&quot; &#8211; The IPMI session has timed out. Please reconnect. If this error occurs often, you may wish to increase the retransmission timeout. Some remote BMCs are considerably slower than others. </p>
<p> &quot;device not found&quot; &#8211; The specified device could not be found. Please check configuration or inputs and try again. </p>
<p> &quot;driver timeout&quot; &#8211; Communication with the driver or device has timed out. Please try again. </p>
<p> &quot;message timeout&quot; &#8211; Communication with the driver or device has timed out. Please try again. </p>
<p> &quot;BMC busy&quot; &#8211; The BMC is currently busy. It may be processing information or have too many simultaneous sessions to manage. Please wait and try again. </p>
<p> &quot;could not find inband device&quot; &#8211; An inband device could not be found. Please check configuration or specify specific device or driver on the command line. </p>
<p> &quot;driver timeout&quot; &#8211; The inband driver has timed out communicating to the local BMC or service processor. The BMC or service processor may be busy or (worst case) possibly non-functioning.</p>
<h2>Workarounds</h2>
<p>With so many different vendors implementing their own IPMI solutions, different vendors may implement their IPMI protocols incorrectly. The following describes a number of workarounds currently available to handle discovered compliance issues. When possible, workarounds have been implemented so they will be transparent to the user. However, some will require the user to specify a workaround be used via the -W option. </p>
<p> The hardware listed below may only indicate the hardware that a problem was discovered on. Newer versions of hardware may fix the problems indicated below. Similar machines from vendors may or may not exhibit the same problems. Different vendors may license their firmware from the same IPMI firmware developer, so it may be worthwhile to try workarounds listed below even if your motherboard is not listed. </p>
<p> If you believe your hardware has an additional compliance issue that needs a workaround to be implemented, please contact the FreeIPMI maintainers on &lt;freeipmi-users [at] gnu.org&gt; or &lt;freeipmi-devel [at] gnu.org&gt;. </p>
<p> <i>assumeio</i> &#8211; This workaround flag will assume inband interfaces communicate with system I/O rather than being memory-mapped. This will work around systems that report invalid base addresses. Those hitting this issue may see &quot;device not supported&quot; or &quot;could not find inband device&quot; errors. Issue observed on HP ProLiant DL145 G1. </p>
<p> <i>spinpoll</i> &#8211; This workaround flag will inform some inband drivers (most notably the KCS driver) to spin while polling rather than putting the process to sleep. This may significantly improve the wall clock running time of tools because an operating system scheduler&#8217;s granularity may be much larger than the time it takes to perform a single IPMI message transaction. However, by spinning, your system may be performing less useful work by not contexting out the tool for a more useful task. </p>
<p> <i>authcap</i> &#8211; This workaround flag will skip early checks for username capabilities, authentication capabilities, and K_g support and allow IPMI authentication to succeed. It works around multiple issues in which the remote system does not properly report username capabilities, authentication capabilities, or K_g status. Those hitting this issue may see &quot;username invalid&quot;, &quot;authentication type unavailable for attempted privilege level&quot;, or &quot;k_g invalid&quot; errors. Issue observed on Asus P5M2/P5MT-R/RS162-E4/RX4, Intel SR1520ML/X38ML, and Sun Fire 2200/4150/4450 with ELOM. </p>
<p> <i>nochecksumcheck</i> &#8211; This workaround flag will tell FreeIPMI to not check the checksums returned from IPMI command responses. It works around systems that return invalid checksums due to implementation errors, but the packet is otherwise valid. Users are cautioned on the use of this option, as it removes validation of packet integrity in a number of circumstances. However, it is unlikely to be an issue in most situations. Those hitting this issue may see &quot;connection timeout&quot;, &quot;session timeout&quot;, or &quot;password verification timeout&quot; errors. On IPMI 1.5 connections, the &quot;noauthcodecheck&quot; workaround may also needed too. Issue observed on Supermicro X9SCM-iiF, Supermicro X9DRi-F, and Supermicro X9DRFR. </p>
<p> <i>idzero</i> &#8211; This workaround flag will allow empty session IDs to be accepted by the client. It works around IPMI sessions that report empty session IDs to the client. Those hitting this issue may see &quot;session timeout&quot; errors. Issue observed on Tyan S2882 with M3289 BMC. </p>
<p> <i>unexpectedauth</i> &#8211; This workaround flag will allow unexpected non-null authcodes to be checked as though they were expected. It works around an issue when packets contain non-null authentication data when they should be null due to disabled per-message authentication. Those hitting this issue may see &quot;session timeout&quot; errors. Issue observed on Dell PowerEdge 2850,SC1425. Confirmed fixed on newer firmware. </p>
<p> <i>forcepermsg</i> &#8211; This workaround flag will force per-message authentication to be used no matter what is advertised by the remote system. It works around an issue when per-message authentication is advertised as disabled on the remote system, but it is actually required for the protocol. Those hitting this issue may see &quot;session timeout&quot; errors. Issue observed on IBM eServer 325. </p>
<p> <i>endianseq</i> &#8211; This workaround flag will flip the endian of the session sequence numbers to allow the session to continue properly. It works around IPMI 1.5 session sequence numbers that are the wrong endian. Those hitting this issue may see &quot;session timeout&quot; errors. Issue observed on some Sun ILOM 1.0/2.0 (depends on service processor endian). </p>
<p> <i>noauthcodecheck</i> &#8211; This workaround flag will tell FreeIPMI to not check the authentication codes returned from IPMI 1.5 command responses. It works around systems that return invalid authentication codes due to hashing or implementation errors. Users are cautioned on the use of this option, as it removes an authentication check verifying the validity of a packet. However, in most organizations, this is unlikely to be a security issue. Those hitting this issue may see &quot;connection timeout&quot;, &quot;session timeout&quot;, or &quot;password verification timeout&quot; errors. Issue observed on Xyratex FB-H8-SRAY. </p>
<p> <i>intel20</i> &#8211; This workaround flag will work around several Intel IPMI 2.0 authentication issues. The issues covered include padding of usernames, and password truncation if the authentication algorithm is HMAC-MD5-128. Those hitting this issue may see &quot;username invalid&quot;, &quot;password invalid&quot;, or &quot;k_g invalid&quot; errors. Issue observed on Intel SE7520AF2 with Intel Server Management Module (Professional Edition). </p>
<p> <i>supermicro20</i> &#8211; This workaround flag will work around several Supermicro IPMI 2.0 authentication issues on motherboards w/ Peppercon IPMI firmware. The issues covered include handling invalid length authentication codes. Those hitting this issue may see &quot;password invalid&quot; errors. Issue observed on Supermicro H8QME with SIMSO daughter card. Confirmed fixed on newerver firmware. </p>
<p> <i>sun20</i> &#8211; This workaround flag will work work around several Sun IPMI 2.0 authentication issues. The issues covered include invalid lengthed hash keys, improperly hashed keys, and invalid cipher suite records. Those hitting this issue may see &quot;password invalid&quot; or &quot;bmc error&quot; errors. Issue observed on Sun Fire 4100/4200/4500 with ILOM. This workaround automatically includes the &quot;opensesspriv&quot; workaround. </p>
<p> <i>opensesspriv</i> &#8211; This workaround flag will slightly alter FreeIPMI&#8217;s IPMI 2.0 connection protocol to workaround an invalid hashing algorithm used by the remote system. The privilege level sent during the Open Session stage of an IPMI 2.0 connection is used for hashing keys instead of the privilege level sent during the RAKP1 connection stage. Those hitting this issue may see &quot;password invalid&quot;, &quot;k_g invalid&quot;, or &quot;bad rmcpplus status code&quot; errors. Issue observed on Sun Fire 4100/4200/4500 with ILOM, Inventec 5441/Dell Xanadu II, Supermicro X8DTH, Supermicro X8DTG, Intel S5500WBV/Penguin Relion 700, Intel S2600JF/Appro 512X, and Quanta QSSC-S4R/Appro GB812X-CN. This workaround is automatically triggered with the &quot;sun20&quot; workaround. </p>
<p> <i>integritycheckvalue</i> &#8211; This workaround flag will work around an invalid integrity check value during an IPMI 2.0 session establishment when using Cipher Suite ID 0. The integrity check value should be 0 length, however the remote motherboard responds with a non-empty field. Those hitting this issue may see &quot;k_g invalid&quot; errors. Issue observed on Supermicro X8DTG, Supermicro X8DTU, and Intel S5500WBV/Penguin Relion 700, and Intel S2600JF/Appro 512X. </p>
<p> <i>assumemaxsdrrecordcount</i> &#8211; This workaround will inform SDR reading to stop reading after a known maximum numer of SDR records have been read. This will work around systems that have mis-implemented SDR reading functions that. Those hitting this issue may see &quot;SDR record count invalid&quot; errors. Issue observed on unspecified Inspur motherboard. </p>
<p> No IPMI 1.5 Support &#8211; Some motherboards that support IPMI 2.0 have been found to not support IPMI 1.5. Those hitting this issue may see &quot;ipmi 2.0 unavailable&quot; or &quot;connection timeout&quot; errors. This issue can be worked around by using IPMI 2.0 instead of IPMI 1.5 by specifying <code>&#8211;driver-type</code>=<i>LAN_2_0</i>. Issue observed on HP Proliant DL 145.</p>
<h2>Diagnostics</h2>
<p>Upon successful execution, exit status is 0. On error, exit status is 1. </p>
<p> If multiple hosts are specified for communication, the exit status is 0 if and only if all targets successfully execute. Otherwise the exit status is 1.</p>
<h2>Known Issues</h2>
<p>On older operating systems, if you input your username, password, and other potentially security relevant information on the command line, this information may be discovered by other users when using tools like the <code><a href="/docs/linux/man/1-ps/">ps</a>(1)</code> command or looking in the /proc file system. It is generally more secure to input password information with options like the -P or -K options. Configuring security relevant information in the FreeIPMI configuration file would also be an appropriate way to hide this information. </p>
<p> In order to prevent brute force attacks, some BMCs will temporarily &quot;lock up&quot; after a number of remote authentication errors. You may need to wait awhile in order to this temporary &quot;lock up&quot; to pass before you may authenticate again.</p>
<h2>Reporting Bugs</h2>
<p>Report bugs to &lt;freeipmi-users [at] gnu.org&gt; or &lt;freeipmi-devel [at] gnu.org&gt;.</p>
<h2>Copyright</h2>
<p>Copyright &#169; 2008-2012 FreeIPMI Core Team </p>
<p> This program is free software; you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation; either version 3 of the License, or (at your option) any later version.</p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/7-freeipmi/">freeipmi</a>(7), <a href="/docs/linux/man/8-bmc-config/">bmc-config</a>(8), <a href="/docs/linux/man/8-bmc-device/">bmc-device</a>(8), <a href="/docs/linux/man/8-ipmi-pef-config/">ipmi-pef-config</a>(8), <a href="/docs/linux/man/8-ipmi-raw/">ipmi-raw</a>(8) <a rel="nofollow" href="http://www.gnu.org/software/freeipmi/">http://www.gnu.org/software/freeipmi/</a> </p>
