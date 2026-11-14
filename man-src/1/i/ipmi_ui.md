---
title: "ipmi_ui(1)"
name: "ipmi_ui"
section: "1"
letter: "i"
url: "/docs/linux/man/1-ipmi_ui/"
description: "ipmi_ui – Crude interface to an IPMI system"
---

<h2 class="name">NAME</h2>
<p> ipmi_ui &#8211; Crude interface to an IPMI system</p>
<h2>SYNOPSIS</h2>
<p> <code>ipmi_ui</code> [<code>-dmsg</code>] [<code>-dmem</code>] [<code>-c</code>] <i>connection-1</i>[<i>connection-2</i>] </p>
<p> The connections are specified as either: </p>
<p> <code>smi&nbsp;<wbr></code><i>smi-num</i> </p>
<p> or </p>
<p> <code>lan&nbsp;<wbr></code><i>IP-addr</i> <i>port&nbsp;<wbr></i>[<i>IP-addr-2</i> <i>port-2</i>] <i>auth privilege username password</i> </p>
<h2>DESCRIPTION</h2>
<p> The <code>ipmi_ui</code> program connects to an IPMI system, and allows access to IPMI entities and sensors and OpenIPMI controls. It&#8217;s rather crude, and primarily for testing OpenIPMI, but it has some use beyond that so it is provided. </p>
<p> Normally, <code>ipmi_ui</code> starts up in a full-screen format. The left window shows the output of commands, the right window shows the logs from OpenIPMI. Both windows are scrollable with page up and page down keys, press the &quot;<code>F1</code>&quot; key to choose the left window to scroll, the &quot;<code>F2</code>&quot; key to choose the right window to scroll. </p>
<p> Note that you must set your environment <code>TERM</code> variable properly for your terminal, or <code>ipmi_ui</code> will display garbage on the screen. </p>
<p> Note that you can put two connection specifications on the command line, and ipmi_ui will make two connection. You can only do this if the connections are to the same IPMI domain through different management controllers. Also, each LAN connection may have two IP addresses. These are two different addresses to the same management controller. So you may have a total of 4 IP addresses to an IPMI domain, two management controllers and two IP addresses to each management controller. </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-dmsg</code></p>
<dd> Turn on message debugging, this will dump all messages to the log window.</p>
<dt><code>-dmem</code></p>
<dd> Turn on memory debugging, this will cause memory allocation and deallocations to be checked. When the program terminates, it will dump all memory that was not properly freed (leaked).</p>
<dt><code>-snmp</code></p>
<dd> Enable the SNMP trap handler. <code>ipmi_ui</code> must be compiled with SNMP code enabled for this option to be available.</p>
<dt><code>-c</code></p>
<dd> Run the program in command-line mode. This is useful for scripting. All output goes to standard output, there is no windowing. </p>
<dt><i>smi-num</i></p>
<dd> The SMI number to connect to, for systems with more than on system interface. Generally, this is &#8216;<code>0</code>&#8216;. </p>
<dt><i>IP-addr</i></p>
<dd> The IP address of the LAN interface. </p>
<dt><i>port</i></p>
<dd> The UDP port of the LAN interface, general <code>623</code>. </p>
<dt><i>IP-addr-2</i></p>
<dd> Some systems support multiple IP connections, this specified the second address and is optional. If specified, OpenIPMI will use both IP addresses and fail over to the working one if one of them fails. </p>
<dt><i>port-2</i></p>
<dd> The port for the second IP connection, generally <code>623</code>. </p>
<dt><i>auth</i></p>
<dd> The authorization to use for the connection, either &quot;<code>none</code>&quot;, &quot;<code>straight</code>&quot;, &quot;<code>md5</code>&quot;, or &quot;<code>md2</code>&quot;. </p>
<dt><i>privilege</i></p>
<dd> The privilege to use for the connection, either &quot;<code>callback</code>&quot;, &quot;<code>user</code>&quot;, &quot;<code>operator</code>&quot;, or &quot;<code>admin</code>&quot;. Note that some IPMI operations will fail without the correct privilege. </p>
<dt><i>username</i></p>
<dd> The user name to use for the connection. If using this anonymous user, this should be the empty string &quot;&quot;. </p>
<dt><i>password</i></p>
<dd> The password to use for the connection. </p>
</dl>
<h2>ENTITIES</h2>
<p> Entities are listed by their entity id (the type of entity they are) and their entity instance. Entities may be active or inactive in the system, the standard IPMI algorithm for determining this is used. Commands on entities are: </p>
<dl>
<dt><code>entities</code></p>
<dd> List all the entities in the system. The output is the entity specifier, followed by an optional entity name in parenthesis, followed by &quot;present&quot; or &quot;not present&quot;. </p>
<dt><code>check_presence</code></p>
<dd> For the check of presence for all entities. </p>
<dt><code>fru&nbsp;<wbr></code><i>entity</i></p>
<dd> List the FRU information associated with the entity. </p>
<dt><code>dump_fru&nbsp;<wbr></code><i>is_logical device_address device_id lun private_bus channel</i></p>
<dd> Dump raw information from the specified FRU device. </p>
</dl>
<h2>SENSORS</h2>
<p> Sensors define input devices that OpenIPMI can monitor. </p>
<dl>
<dt><code>sensors&nbsp;<wbr></code><i>entity</i></p>
<dd> List all the sensors that monitor the given entity. The output is the sensor specifier (the entity specifier followed by the sensor name, with spaces converted to ~). followed by the sensor name. </p>
<dt><code>sensor&nbsp;<wbr></code><i>sensor</i></p>
<dd> Pull up the given sensor and display all its information. In full-screen mode, the sensor will be re-queried every second. </p>
<dt><code>rearm</code> <i>global</i> [<i>assertion-mask</i> <i>deassertion-mask</i>]</p>
<dd> Rearm the given sensor. If <i>global</i> is <code>1</code>, then the whole sensor is rearmed. If <i>global</i> is <code>0</code>, then the <i>assertion-mask</i> and <i>deassertion-mask</i> must be specified telling which thresholds or states to rearm. </p>
<dt><code>events_enable</code> <i>events</i> <i>scanning</i> <i>assertion-bitmask</i> <i>deassertion-bitmask</i></p>
<dd> Enable or disable events for the given sensor. <i>events</i> turns events on or off from the sensor (<code>0</code> or <code>1</code>). <i>scanning</i> turns scanning on or off for the sensor (<code>0</code> or <code>1</code>). <i>assertion-bitmask</i> specifies the bitmask of thresholds or states that should be enabled or disabled when a threshold or state is asserted. It is a bunch of 0&#8217;s and 1&#8217;s, where the first one is for threshold/state 0, the second for threshold/state 1, etc. <i>deassertion-bitmask</i> specifies the bitmask of thresholds or states that should be enabled or disabled when a threshold or state is deasserted. </p>
</dl>
<h2>CONTROLS</h2>
<p> Controls are output devices that can control things like LEDs, power, reset lines and such. </p>
<dl>
<dt><code>controls&nbsp;<wbr></code><i>entity</i></p>
<dd> List all the controls that control the given entity. The output is the control specifier (the entity specifier followed by the control name, with spaces converted to ~). followed by the control name. </p>
<dt><code>control&nbsp;<wbr></code><i>control</i></p>
<dd> Pull up the given control and display it&#8217;s current state. </p>
<dt><code>set_control</code> <i>val1</i> [<i>val2</i> &#8230;]</p>
<dd> Change the value of a control. Note that for controls with multiple values, <code>every</code> value must be specified. </p>
</dl>
<h2>EVENTS</h2>
<p> Events are asynchronous messages from sensors that tell the user that a sensor has done something. Events are generally stored in a system event log (SEL); OpenIPMI will fetch the events from the SELs in the system. </p>
<p> Since multiple SELs may exist, an event is specified by the MC it came from in the format &quot;(channel addr)&quot; and a log number. The same log number may exist in multiple MCs. </p>
<p> Events are displayed in the log window as they come in. If they can be correlated with a sensor, they will be display with as much information as possible. </p>
<dl>
<dt><code>delevent&nbsp;<wbr></code><i>channel mc-addr log-num</i></p>
<dd> Delete the given event. Note that many SELs do not support individual deletes, so this may only delete the local copy of the event, not the one in the SEL. In this case, to delete events in the SEL, you must delete <code>all</code> the events in the SEL and wait about 10 seconds for OpenIPMI to do a full SEL clear. </p>
<dt><code>clear_sel</code></p>
<dd> Delete all events in the SEL. This process may take some time, so if you do this and quit immediately it may not be complete. </p>
<dt><code>list_sel</code></p>
<dd> List all events in the local copy of the SELs. This is only the local copy, if the copies in the actual have change, this won&#8217;t be reflected. </p>
<dt><code>get_sel_time&nbsp;<wbr></code><i>channel mc-num</i></p>
<dd> Get the time in the SEL for the given MC. </p>
</dl>
<h2>MANAGMENT CONTROLLERS (MCs)</h2>
<p> In OpenIPMI, you normally don&#8217;t deal with management controllers. They are considered internal to the system. However, for debugging, information about them is provided. </p>
<dl>
<dt><code>mcs</code></p>
<dd> List all the MCs in the system and whether they are active. MCs are displayed in the format &quot;(channel address)&quot;. </p>
<dt><code>mc&nbsp;<wbr></code><i>channel mc-addr</i></p>
<dd> Display a boatload of information about the MC, mostly coming from the get device id command. </p>
<dt><code>mccmd</code> <i>channel</i> <i>mc-addr</i> <i>LUN</i> <i>NetFN</i> <i>Cmd</i> [<i>data</i> &#8230;]</p>
<dd> Send an IPMI command to the given MC. The MC must exist and be active to do this. </p>
<dt><code>mc_reset</code> <i>channel</i> <i>mc-addr</i> [<code>warm</code> | <code>cold</code>]</p>
<dd> Send a warm or cold reset command to the given MC. The action the MC takes is system-specific. </p>
<dt><code>scan&nbsp;<wbr></code><i>channel mc-addr</i></p>
<dd> Scan for an MC at the given address. If the MC exists but OpenIPMI didn&#8217;t know about it, it will be added. If the MC no longer exists, then it will be removed. </p>
<dt><code>mc_events_enable&nbsp;<wbr></code><i>channel mc-num enabled</i></p>
<dd> Enable or disable event generation for the given MC. </p>
<dt><code>mc_events_enabled&nbsp;<wbr></code><i>channel mc-num</i></p>
<dd> Prints out if the events are enabled for the given MC. </p>
</dl>
<h2>LAN Parameter Configuration</h2>
<p> OpenIPMI has functions that make it easier to configure the LAN parameters of a LAN connection. Note that the LAN parameters have a lock that OpenIPMI attempts to use. If you read the LAN parameters, they will be locked until you either write them or clear the lock. </p>
<dl>
<dt><code>readlanparm&nbsp;<wbr></code><i>channel mc-num channel</i></p>
<dd> Read lanparm information from an MC and display it in the display window. </p>
<dt><code>viewlanparm</code></p>
<dd> Show current lanparm information in the display window. </p>
<dt><code>writelanparm&nbsp;<wbr></code><i>channel mc-num channel</i></p>
<dd> Write the current LANPARM information to an MC. Note that this must be the MC that the parameters were read from. </p>
<dt><code>clearlanparmlock</code> [<i>channel</i> <i>mc-num</i> <i>channel</i>]</p>
<dd> Clear a LANPARM lock. If the MC is given, then the LANPARM lock is directly cleared. If not given, then the LANPARM lock for the current parms is cleared. </p>
<dt><code>setlanparm</code> <i>config</i> [<i>selector</i>] <i>value</i></p>
<dd> Set the given config item to the value. The optional selector is used for items that take a selector, like &quot;auth&quot; or any of the items in &quot;destination&quot;. </p>
</dl>
<h2>Platform Event Filter (PEF)</h2>
<p> OpenIPMI contains function to help manage the PEF settings on a BMC. Note that the PEF parameters have a lock that OpenIPMI attempts to use. If you read the PEF parameters, they will be locked until you either write them or clear the lock. </p>
<dl>
<dt><code>readpef&nbsp;<wbr></code><i>channel mc-num</i></p>
<dd> Read the PEF information from an MC. </p>
<dt><code>clearpeflock</code> [<i>channel</i> <i>mc-num</i>]</p>
<dd> Clear a PEF lock. If the MC is given, then the PEF lock on that MC is directly cleared. If no MC is given, then the current PEF&#8217;s lock is cleared. </p>
<dt><code>viewpef</code></p>
<dd> Show current pef information in the display window. </p>
<dt><code>writepef&nbsp;<wbr></code><i>channel mc-num</i></p>
<dd> Write the current PEF information to an MC. </p>
<dt><code>setpef</code> <i>config</i> [<i>selector</i>] <i>value</i></p>
<dd> Set the given config item to the value. The optional selector is used for items that take a selector, like anything in the event filters, alert policies, or alert strings. </p>
<dt><code>pet</code> <i>connection</i> <i>channel</i> <i>ip-addr</i> <i>mac_addr</i> <i>eft-selector</i> <i>policy-num</i> <i>apt-selector</i> <i>lan-dest-selector</i></p>
<dd> Set up the connection for the domain to send PET traps from the given connection to the given IP/MAC address over the given channel. This does all the LAN and PEF configuration required to configure a system to send event traps. </p>
</dl>
<h2>CONNECTIONS</h2>
<p> OpenIPMI can maintain multiple connections to a single domain. It will generally only use one of these at a time (although the other will constantly be under test). This is the &quot;active&quot; connection. You can query and set which connection is active. </p>
<p> The connection number is the connection from the command line. You can specify two connections on the command line (the part beginning with &quot;<code>lan</code><i>&quot;, &quot;</i><code>smi</code><i>&quot;, etc.). The first connection you specify is connection zero, the second is connection 1. </p>
<dl>
<dt></i><code>is_con_active&nbsp;<wbr></code><i>connection</i></p>
<dd> Print out if the given connection is active or not. </p>
<dt><code>activate_con&nbsp;<wbr></code><i>connection</i></p>
<dd> Activate the given connection. </p>
</dl>
<h2>OTHER COMMANDS</h2>
<dl>
<dt><code>msg</code> <i>channel</i> <i>IPMB-addr</i> <i>LUN</i> <i>NetFN</i> <i>Cmd</i> [<i>data</i> &#8230;]</p>
<dd> Send an IPMI command to the given IPMB address. This is available in case the given MC cannot be found or enabled. </p>
<dt><code>sdrs&nbsp;<wbr></code><i>channel mc-addr do-sensors</i></p>
<dd> Dump all the sdrs from the given MC. If <i>do-sensors</i> is <code>true</code>, then dump the device SDR. If it is <code>false</code>, dump the main SDR repository on the MC. </p>
<dt><code>scan&nbsp;<wbr></code><i>channel IPMB-addr</i></p>
<dd> Perform an IPMB bus scan for the given IPMB, to try to detect an MC at the given address. IPMB bus scanning can be slow, this can help speed things up if you already know the address. </p>
<dt><code>quit</code></p>
<dd> Leave the program. </p>
<dt><code>reconnect</code></p>
<dd> Attempt to disconnect and reconnect to the IPMI controller. This is primarily for testing. </p>
<dt><code>display_win</code></p>
<dd> Set the display window (left window) for scrolling, just in case the &quot;<code>F1</code>&quot; key doesn&#8217;t work. </p>
<dt><code>log_win</code></p>
<dd> Set the log window (right window) for scrolling, just in case the &quot;<code>F2</code>&quot; key doesn&#8217;t work. </p>
<dt><code>help</code></p>
<dd> Dump some terse help output about all the commands. </p>
</dl>
<h2>ERROR OUTPUT</h2>
<p> All error output goes to the log window. </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/8-ipmilan/">ipmilan</a></code>(8) </p>
<h2>KNOWN PROBLEMS</h2>
<p> Our name is legion. </p>
<h2>AUTHOR</h2>
<p> Corey Minyard &lt;cminyard [at] mvista.org&gt; </p>
<h2>Index</h2>
