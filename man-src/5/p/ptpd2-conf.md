---
title: "ptpd2-conf(5)"
name: "ptpd2-conf"
section: "5"
letter: "p"
url: "/docs/linux/man/5-ptpd2-conf/"
description: "ptpd2.conf – Precision Time Protocol daemon config file"
---

<p>ptpd2.conf &#8211; Precision Time Protocol daemon config file </p>
<h2>Configuration File Format</h2>
<p>Settings in the PTPd configuration file are grouped into sections and take the form of <i>section:key=&quot;value&quot;</i> variables. The configuration file can either be formatted that way (preferred) or in .ini file style where a series of <i>key=&quot;value&quot;</i> variables is grouped into sections using <code>[</code><i>section</i><code>]</code> headers. Every setting listed here can also be specified as a command line parameter <code>(</code><i>&#8211;section:key=value</i><code>)</code>. Quotation marks are optional. <code>NOTE:</code> the configuration file must end with a newline.</p>
<h2>Reloading Configuration</h2>
<p>Only a small number of configuration file settings (SNMP, lock file configuration) requires a restart of the PTPd process to take effect. All other settings can be changed while ptpd is running &#8211; configuration file is reloaded and checked for changes when PTPd receives the SIGHUP signal. When reloading configuration, PTPd will always attempt to test settings before applying them and once running, will never exit as a result of configuration errors. If it does exit during config refresh, this is most likely a bug.</p>
<h2>Priority</h2>
<p>Any setting passed as a command line parameter will always take priority over the configuration file, so once ptpd is running, those settings cannot be changed &#8211; a warning will be logged on every attempt to change those settings using the configuration file.</p>
<h2>Configuration Sections</h2>
<dl>
<dt><code>ptpengine</code></p>
<dd>PTP protocol specific configuration</p>
<dt><code>clock</code></p>
<dd>Clock related settings</p>
<dt><code>servo</code></p>
<dd>Clock control PI servo configuration</p>
<dt><code>global</code></p>
<dd>Global configuration &#8211; logging, etc.</p>
<dt><code>ntpengine</code></p>
<dd>NTP control configuration</p>
<dd></dl>
<h2>Configuration Variables</h2>
<dl>
<dt>
<dl>
<dd>
<dd>
<dl>
<dt><code>ptpengine:interface [</code><i>STRING</i><code>]</code></p>
<dd>
<dl>
<dd>
<dl>
<dt><code>usage</code></p>
<dd>Network interface to use &#8211; eth0, igb0 etc. (<code>required</code>).</p>
<dt><code>default</code></p>
<dd><i>[none]</i> </p>
</dl>
</dl>
</dl>
</dl>
<dl>
<dd>
<dl>
<dt><code>ptpengine:backup_interface [</code><i>STRING</i><code>]</code></p>
<dd>
<dl>
<dd>
<dl>
<dt><code>usage</code></p>
<dd>Backup network interface to use &#8211; eth0, igb0 etc. When no GM available, slave will keep alternating between primary and secondary until a GM is found.</p>
<dt><code>default</code></p>
<dd><i>[none]</i> </p>
</dl>
</dl>
</dl>
</dl>
<dl>
<dd>
<dl>
<dt><code>ptpengine:preset [</code><i>SELECT</i><code>]</code></p>
<dd>
<dl>
<dd>
<dl>
<dt><code>options</code></p>
<dd><i>none slaveonly masteronly masterslave </i></p>
<dt><code>usage</code></p>
<dd>PTP engine preset:</p>
<dl>
<dd>
<dl>
<dt><i>none</i></p>
<dd>Defaults, no clock class restrictions</p>
<dt><i>slaveonly</i></p>
<dd>Slave only (clock class 255 only)</p>
<dt><i>masteronly</i></p>
<dd>Master, passive when not best master (clock class 0..127)</p>
<dt><i>masterslave</i></p>
<dd>Full IEEE 1588 implementation: Master, slave when not best master (clock class 128..254)</dl>
</dl>
<dt><code>default</code></p>
<dd><i>slaveonly</i></p>
<dt><code>NOTE:</code></p>
<dd>Presets affect the following settings: <i>ptpengine:slave_only</i>, <i>clock_no_adjust</i> and <i>ptpengine:clock_class</i> (range and default value). To see all preset settings, run ptpd2 <i>-H</i> (<i>&#8211;long-help</i>) </p>
</dl>
</dl>
</dl>
</dl>
<dl>
<dd>
<dl>
<dt><code>ptpengine:transport [</code><i>SELECT</i><code>]</code></p>
<dd>
<dl>
<dd>
<dl>
<dt><code>options</code></p>
<dd><i>ipv4 ethernet</i></p>
<dt><code>usage</code></p>
<dd>Transport type for PTP packets. <code>NOTE:</code> Ethernet transport requires building with <i>libpcap</i> and is not supported on Solaris as of 2.3.1, and cannot be enabled on those systems unless ptpd is compiled with <code>&#8211;enable-experimental-options</code>.</p>
<dt><code>default</code></p>
<dd><i>ipv4</i> </p>
</dl>
</dl>
</dl>
</dl>
<dl>
<dd>
<dl>
<dt><code>ptpengine:dot2as [</code><i>BOOLEAN</i><code>]</code></p>
<dd>
<dl>
<dd>
<dl>
<dt><code>usage</code></p>
<dd>Enable IEEE 802.1AS / AVB compatibility (transportSpecific field in PTP message headers). Requires Ethernet transport as this is the only mapping used by 802.1AS that PTP supports</p>
<dt><code>default</code></p>
<dd><i>N</i> </p>
</dl>
</dl>
</dl>
</dl>
<dl>
<dd>
<dl>
<dt><code>ptpengine:ip_mode [</code><i>SELECT</i><code>]</code></p>
<dd>
<dl>
<dd>
<dl>
<dt><code>options</code></p>
<dd><i>multicast unicast hybrid </i></p>
<dt><code>usage</code></p>
<dd>IP transmission mode (requires IP transport):</p>
<dl>
<dd>
<dl>
<dt><i>multicast</i></p>
<dd>uses multicast for all messages</p>
<dt><i>hybrid</i></p>
<dd>uses multicast for sync and announce, and unicast for delay request and response</p>
<dt><i>unicast</i></p>
<dd>uses unicast for all transmission. When unicast mode is selected, destination IP(s) (<i>ptpengine:unicast_destinations</i>) must be configured depending on unicast negotiation setting (<i>ptpengine:unicast_negotiation</i>) and master or slave role (see: <i>ptpengine:unicast_destinations</i>)</dl>
</dl>
<dt><code>default</code></p>
<dd><i>multicast</i> </p>
</dl>
</dl>
</dl>
</dl>
<dl>
<dd>
<dl>
<dt><code>ptpengine:unicast_negotiation [</code><i>BOOLEAN</i><code>]</code></p>
<dd>
<dl>
<dd>
<dl>
<dt><code>usage</code></p>
<dd>Enable unicast negotiation support using signaling messages &#8211; as used by the Telecom profile (ITU-T G.8265.1).</p>
<dt><code>default</code></p>
<dd><i>N</i> </p>
</dl>
</dl>
</dl>
</dl>
<dl>
<dd>
<dl>
<dt><code>ptpengine:unicast_grant_duration [</code><i>INT</i><code>: 30 .. 604800]</code></p>
<dd>
<dl>
<dd>
<dl>
<dt><code>usage</code></p>
<dd>Duration (seconds) for which the transmission of unicast messages is granted by a master, or requested by a slave when unicast negotiation is used (<i>ptpengine:unicast_negotiation</i>). When using PTPd with other PTP implementations, PTPd will never refuse to grant a message based on the requested duration: it will grant for 30 seconds if requested for any less than 30 seconds, and will grant for 7 days (604800) if requested for any longer.</p>
<dt><code>default</code></p>
<dd><i>300</i> </p>
</dl>
</dl>
</dl>
</dl>
<dl>
<dd>
<dl>
<dt><code>ptpengine:disable_bmca [</code><i>BOOLEAN</i><code>]</code></p>
<dd>
<dl>
<dd>
<dl>
<dt><code>usage</code></p>
<dd>Disable Best Master Clock Algorithm for unicast masters. Only effective for masteronly preset &#8211; all Announce messages will be ignored and the cock will transition directly into MASTER state and remain an active master. This behaviour is required for Telecom profile operation.</p>
<dt><code>default</code></p>
<dd><i>N</i> </p>
</dl>
</dl>
</dl>
</dl>
<dl>
<dd>
<dl>
<dt><code>ptpengine:use_libpcap [</code><i>BOOLEAN</i><code>]</code></p>
<dd>
<dl>
<dd>
<dl>
<dt><code>usage</code></p>
<dd>Use libpcap for sending and receiving traffic (automatically enabled in Ethernet mode). Requires building with libpcap &#8211; builds made with <code>&#8211;disable-pcap</code> cannot use this feature, and as of 2.3.1, Solaris systems will not attempt to use libpcap unless compiled with <code>&#8211;enable-experimental-options</code></p>
<dt><code>default</code></p>
<dd><i>N</i> </p>
</dl>
</dl>
</dl>
</dl>
<dl>
<dd>
<dl>
<dt><code>ptpengine:delay_mechanism [</code><i>SELECT</i><code>]</code></p>
<dd>
<dl>
<dd>
<dl>
<dt><code>options</code></p>
<dd><i>E2E P2P DELAY_DISABLED </i></p>
<dt><code>usage</code></p>
<dd>Delay detection mode used &#8211; use DELAY_DISABLED for syntonisation only (no synchronisation).</p>
<dt><code>default</code></p>
<dd><i>E2E</i> </p>
</dl>
</dl>
</dl>
</dl>
<dl>
<dd>
<dl>
<dt><code>ptpengine:domain [</code><i>INT</i><code>: 0 .. 127]</code></p>
<dd>
<dl>
<dd>
<dl>
<dt><code>usage</code></p>
<dd>PTP domain number.</p>
<dt><code>default</code></p>
<dd><i>0</i> </p>
</dl>
</dl>
</dl>
</dl>
<dl>
<dd>
<dl>
<dt><code>ptpengine:any_domain [</code><i>BOOLEAN</i><code>]</code></p>
<dd>
<dl>
<dd>
<dl>
<dt><code>usage</code></p>
<dd>Usability extension: if enabled, a slave-only clock will accept masters from any domain, while preferring the configured domain, and preferring lower domain number. This option should be used for slave-only clocks and should not be used with unicast negotiation. <code>NOTE:</code> this behaviour is not part of the standard.</p>
<dt><code>default</code></p>
<dd><i>N</i> </p>
</dl>
</dl>
</dl>
</dl>
<dl>
<dd>
<dl>
<dt><code>ptpengine:port_number [</code><i>INT</i><code>: 1 .. 65534]</code></p>
<dd>
<dl>
<dd>
<dl>
<dt><code>usage</code></p>
<dd>PTP port number (part of PTP Port Identity &#8211; not UDP port). For ordinary clocks (single port), the default should be used, but when running multiple instances to simulate a boundary clock, The port number can be changed.</p>
<dt><code>default</code></p>
<dd><i>1</i> </p>
</dl>
</dl>
</dl>
</dl>
<dl>
<dd>
<dl>
<dt><code>ptpengine:slave_only [</code><i>BOOLEAN</i><code>]</code></p>
<dd>
<dl>
<dd>
<dl>
<dt><code>usage</code></p>
<dd>Slave only mode (sets clock class to 255, overriding value from preset).</p>
<dt><code>default</code></p>
<dd><i>Y</i> </p>
</dl>
</dl>
</dl>
</dl>
<dl>
<dd>
<dl>
<dt><code>ptpengine:inbound_latency [</code><i>INT</i><code>]</code></p>
<dd>
<dl>
<dd>
<dl>
<dt><code>usage</code></p>
<dd>Specify latency correction (nanoseconds) for incoming packets.</p>
<dt><code>default</code></p>
<dd><i>0</i> </p>
</dl>
</dl>
</dl>
</dl>
<dl>
<dd>
<dl>
<dt><code>ptpengine:outbound_latency [</code><i>INT</i><code>]</code></p>
<dd>
<dl>
<dd>
<dl>
<dt><code>usage</code></p>
<dd>Specify latency correction (nanoseconds) for outgoing packets.</p>
<dt><code>default</code></p>
<dd><i>0</i> </p>
</dl>
</dl>
</dl>
</dl>
<dl>
<dd>
<dl>
<dt><code>ptpengine:offset_shift [</code><i>INT</i><code>]</code></p>
<dd>
<dl>
<dd>
<dl>
<dt><code>usage</code></p>
<dd>Apply an arbitrary shift (nanoseconds) to offset from master when in slave state. Value can be positive or negative &#8211; useful for correcting for of antenna latencies, delay assymetry and IP stack latencies. This will not be visible in the offset from master value &#8211; only in the resulting clock correction.</p>
<dt><code>default</code></p>
<dd><i>0</i> </p>
</dl>
</dl>
</dl>
</dl>
<dl>
<dd>
<dl>
<dt><code>ptpengine:always_respect_utc_offset [</code><i>BOOLEAN</i><code>]</code></p>
<dd>
<dl>
<dd>
<dl>
<dt><code>usage</code></p>
<dd>Compatibility option: In slave state, always respect UTC offset announced by best master, even if the the<br />
&nbsp;<wbr>currrentUtcOffsetValid flag is announced FALSE.&nbsp;<wbr><code>NOTE</code>: this behaviour is not part of the standard.</p>
<dt><code>default</code></p>
<dd><i>N</i> </p>
</dl>
</dl>
</dl>
</dl>
<dl>
<dd>
<dl>
<dt><code>ptpengine:prefer_utc_offset_valid [</code><i>BOOLEAN</i><code>]</code></p>
<dd>
<dl>
<dd>
<dl>
<dt><code>usage</code></p>
<dd>Compatibility extension to BMC algorithm: when enabled, BMC for both master and save clocks will prefer masters announcing currrentUtcOffsetValid as TRUE.<br />
&nbsp;<wbr><code>NOTE</code>: this behaviour is not part of the standard.</p>
<dt><code>default</code></p>
<dd><i>N</i> </p>
</dl>
</dl>
</dl>
</dl>
<dl>
<dd>
<dl>
<dt><code>ptpengine:require_utc_offset_valid [</code><i>BOOLEAN</i><code>]</code></p>
<dd>
<dl>
<dd>
<dl>
<dt><code>usage</code></p>
<dd>Compatibility option: when enabled, ptpd2 will ignore Announce messages from masters announcing currentUtcOffsetValid as FALSE. <code>NOTE</code>: this behaviour is not part of the standard.</p>
<dt><code>default</code></p>
<dd><i>N</i> </p>
</dl>
</dl>
</dl>
</dl>
<dl>
<dd>
<dl>
<dt><code>ptpengine:log_announce_interval [</code><i>INT</i><code>: -4 .. 7]</code></p>
<dd>
<dl>
<dd>
<dl>
<dt><code>usage</code></p>
<dd>PTP announce message interval in master state. When using unicast negotiation (<i>ptpengine:unicast_negotiation</i>), for slaves this is the initial (minimum) interval requested and for masters this is the minimum interval granted. (expressed as log 2 i.e. -1=0.5s, 0=1s, 1=2s etc.)</p>
<dt><code>default</code></p>
<dd><i>1</i> </p>
</dl>
</dl>
</dl>
</dl>
<dl>
<dd>
<dl>
<dt><code>ptpengine:log_announce_interval_max [</code><i>INT</i><code>: -1 .. 7]</code></p>
<dd>
<dl>
<dd>
<dl>
<dt><code>usage</code></p>
<dd>When using unicast negtiation (<i>ptpengine:unicast_negotiation</i>), this is the maximum announce interval granted by a master, and the maximum interval a slave will attempt to request. (expressed as log 2 i.e. -1=0.5s, 0=1s, 1=2s etc.)</p>
<dt><code>default</code></p>
<dd><i>5</i> </p>
</dl>
</dl>
</dl>
</dl>
<dl>
<dd>
<dl>
<dt><code>ptpengine:announce_receipt_timeout [</code><i>INT</i><code>: 2 .. 255]</code></p>
<dd>
<dl>
<dd>
<dl>
<dt><code>usage</code></p>
<dd>PTP announce receipt timeout announced in master state.</p>
<dt><code>default</code></p>
<dd><i>6</i> </p>
</dl>
</dl>
</dl>
</dl>
<dl>
<dd>
<dl>
<dt><code>ptpengine:announce_receipt_grace_period [</code><i>INT</i><code>: 0 .. 20]</code></p>
<dd>
<dl>
<dd>
<dl>
<dt><code>usage</code></p>
<dd>PTP announce receipt timeout grace period in slave state: when announce receipt timeout occurs, disqualify current best GM,<br />
&nbsp;<wbr>then wait n times announce receipt timeout before resetting. Allows for a seamless GM failover when standby GMs are slow<br />
&nbsp;<wbr>to react. When set to 0, this option is not used.</p>
<dt><code>default</code></p>
<dd><i>0</i> </p>
</dl>
</dl>
</dl>
</dl>
<dl>
<dd>
<dl>
<dt><code>ptpengine:log_sync_interval [</code><i>INT</i><code>: -7 .. 7]</code></p>
<dd>
<dl>
<dd>
<dl>
<dt><code>usage</code></p>
<dd>PTP sync message interval in master state. When using unicast negotiation (<i>ptpengine:unicast_negotiation</i>), for slaves this is the initial (minimum) interval requested and for masters this is the minimum interval granted. <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>(expressed as log 2 i.e. -1=0.5s, 0=1s, 1=2s etc.)</p>
<dt><code>default</code></p>
<dd><i>0</i> </p>
</dl>
</dl>
</dl>
</dl>
<dl>
<dd>
<dl>
<dt><code>ptpengine:log_sync_interval_max [</code><i>INT</i><code>: -1 .. 7]</code></p>
<dd>
<dl>
<dd>
<dl>
<dt><code>usage</code></p>
<dd>When using unicast negtiation (<i>ptpengine:unicast_negotiation</i>), this is the maximum sync interval granted by a master, and the maximum interval a slave will attempt to request. (expressed as log 2 i.e. -1=0.5s, 0=1s, 1=2s etc.)</p>
<dt><code>default</code></p>
<dd><i>5</i> </p>
</dl>
</dl>
</dl>
</dl>
<dl>
<dd>
<dl>
<dt><code>ptpengine:log_delayreq_override [</code><i>BOOLEAN</i><code>]</code></p>
<dd>
<dl>
<dd>
<dl>
<dt><code>usage</code></p>
<dd>Override the Delay Request interval provided by best master.</p>
<dt><code>default</code></p>
<dd><i>N</i> </p>
</dl>
</dl>
</dl>
</dl>
<dl>
<dd>
<dl>
<dt><code>ptpengine:log_delayreq_auto [</code><i>BOOLEAN</i><code>]</code></p>
<dd>
<dl>
<dd>
<dl>
<dt><code>usage</code></p>
<dd>Automatically override the Delay Request interval (with <i> ptpengine:log_delayreq_interval</i>) if the received value is 127 (0X7F), such as in unicast messages, unless using unicast negotiation (<i>ptpengine:unicast_negotiation</i>)</p>
<dt><code>default</code></p>
<dd><i>Y</i> </p>
</dl>
</dl>
</dl>
</dl>
<dl>
<dd>
<dl>
<dt><code>ptpengine:log_delayreq_interval_initial [</code><i>INT</i><code>: -7 .. 7]</code></p>
<dd>
<dl>
<dd>
<dl>
<dt><code>usage</code></p>
<dd>Delay request interval used before receiving first delay response <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>(expressed as log 2 i.e. -1=0.5s, 0=1s, 1=2s etc.)</p>
<dt><code>default</code></p>
<dd><i>0</i> </p>
</dl>
</dl>
</dl>
</dl>
<dl>
<dd>
<dl>
<dt><code>ptpengine:log_delayreq_interval [</code><i>INT</i><code>: -7 .. 7]</code></p>
<dd>
<dl>
<dd>
<dl>
<dt><code>usage</code></p>
<dd>Minimum delay request interval announced when in master state, in slave state overrides the master interval.<br />
&nbsp;<wbr>(expressed as log 2 i.e. -1=0.5s, 0=1s, 1=2s etc.). When using unicast negotiation&nbsp;<wbr>(<i>ptpengine:unicast_negotiation</i>), for slaves this is the initial (minimum) interval requested and for masters this is the minimum interval granted.</p>
<dt><code>default</code></p>
<dd><i>0</i> </p>
</dl>
</dl>
</dl>
</dl>
<dl>
<dd>
<dl>
<dt><code>ptpengine:log_delayreq_interval_max [</code><i>INT</i><code>: -1 .. 7]</code></p>
<dd>
<dl>
<dd>
<dl>
<dt><code>usage</code></p>
<dd>When using unicast negtiation (<i>ptpengine:unicast_negotiation</i>), this is the maximum delay request interval granted by a master, and the maximum interval a slave will attempt to request.<br />
&nbsp;<wbr>(expressed as log 2 i.e. -1=0.5s, 0=1s, 1=2s etc.).&nbsp;<wbr></p>
<dt><code>default</code></p>
<dd><i>5</i> </p>
</dl>
</dl>
</dl>
</dl>
<dl>
<dd>
<dl>
<dt><code>ptpengine:log_peer_delayreq_interval [</code><i>INT</i><code>: -7 .. 7]</code></p>
<dd>
<dl>
<dd>
<dl>
<dt><code>usage</code></p>
<dd>Minimum peer delay request message interval in peer to peer delay mode (expressed as log 2 i.e. -1=0.5s, 0=1s, 1=2s etc.). When using unicast negotiation (<i>ptpengine:unicast_negotiation</i>), this is the initial (minimum) interval requested by a node from its peer and this is the minimum interval granted for a peer.</p>
<dt><code>default</code></p>
<dd><i>1</i> </p>
</dl>
</dl>
</dl>
</dl>
<dl>
<dd>
<dl>
<dt><code>ptpengine:log_peer_delayreq_interval_max [</code><i>INT</i><code>: -1 .. 7]</code></p>
<dd>
<dl>
<dd>
<dl>
<dt><code>usage</code></p>
<dd>When using unicast negtiation (<i>ptpengine:unicast_negotiation</i>), this is the maximum peer delay request interval granted by a node, and the maximum interval a node will attempt to request from its peer.<br />
&nbsp;<wbr>(expressed as log 2 i.e. -1=0.5s, 0=1s, 1=2s etc.).&nbsp;<wbr></p>
<dt><code>default</code></p>
<dd><i>5</i> </p>
</dl>
</dl>
</dl>
</dl>
<dl>
<dd>
<dl>
<dt><code>ptpengine:foreignrecord_capacity [</code><i>INT</i><code>: 5 .. 10]</code></p>
<dd>
<dl>
<dd>
<dl>
<dt><code>usage</code></p>
<dd>Foreign master record size (Maximum number of foreign masters).</p>
<dt><code>default</code></p>
<dd><i>5</i> </p>
</dl>
</dl>
</dl>
</dl>
<dl>
<dd>
<dl>
<dt><code>ptpengine:ptp_allan_variance [</code><i>INT</i><code>: 0 .. 65535]</code></p>
<dd>
<dl>
<dd>
<dl>
<dt><code>usage</code></p>
<dd>Specify Allan variance announced in master state.</p>
<dt><code>default</code></p>
<dd><i>28768</i> </p>
</dl>
</dl>
</dl>
</dl>
<dl>
<dd>
<dl>
<dt><code>ptpengine:ptp_clock_accuracy [</code><i>SELECT</i><code>]</code></p>
<dd>
<dl>
<dd>
<dl>
<dt><code>options</code></p>
<dd><i>ACC_25NS ACC_100NS ACC_250NS ACC_1US ACC_2.5US ACC_10US ACC_25US ACC_100US ACC_250US ACC_1MS ACC_2.5MS ACC_10MS ACC_25MS ACC_100MS ACC_250MS ACC_1S ACC_10S ACC_10SPLUS ACC_UNKNOWN </i></p>
<dt><code>usage</code></p>
<dd>Clock accuracy range announced in master state.</p>
<dt><code>default</code></p>
<dd><i>ACC_UNKNOWN</i> </p>
</dl>
</dl>
</dl>
</dl>
<dl>
<dd>
<dl>
<dt><code>ptpengine:utc_offset [</code><i>INT</i><code>]</code></p>
<dd>
<dl>
<dd>
<dl>
<dt><code>usage</code></p>
<dd>Underlying time source UTC offset announced in master state.</p>
<dt><code>default</code></p>
<dd><i>0</i> </p>
</dl>
</dl>
</dl>
</dl>
<dl>
<dd>
<dl>
<dt><code>ptpengine:utc_offset_valid [</code><i>BOOLEAN</i><code>]</code></p>
<dd>
<dl>
<dd>
<dl>
<dt><code>usage</code></p>
<dd>Underlying time source UTC offset validity announced in master state.</p>
<dt><code>default</code></p>
<dd><i>N</i> </p>
</dl>
</dl>
</dl>
</dl>
<dl>
<dd>
<dl>
<dt><code>ptpengine:time_traceable [</code><i>BOOLEAN</i><code>]</code></p>
<dd>
<dl>
<dd>
<dl>
<dt><code>usage</code></p>
<dd>Underlying time source time traceability announced in master state.</p>
<dt><code>default</code></p>
<dd><i>N</i> </p>
</dl>
</dl>
</dl>
</dl>
<dl>
<dd>
<dl>
<dt><code>ptpengine:frequency_traceable [</code><i>BOOLEAN</i><code>]</code></p>
<dd>
<dl>
<dd>
<dl>
<dt><code>usage</code></p>
<dd>Underlying time source frequency traceability announced in master state.</p>
<dt><code>default</code></p>
<dd><i>N</i> </p>
</dl>
</dl>
</dl>
</dl>
<dl>
<dd>
<dl>
<dt><code>ptpengine:ptp_timescale [</code><i>SELECT</i><code>]</code></p>
<dd>
<dl>
<dd>
<dl>
<dt><code>options</code></p>
<dd><i>PTP ARB </i></p>
<dt><code>usage</code></p>
<dd>Time scale announced in master state (with ARB, UTC properties are ignored by slaves). When clock class is set to 13 (application specific), this value is ignored and ARB is used.</p>
<dt><code>default</code></p>
<dd><i>ARB</i> </p>
</dl>
</dl>
</dl>
</dl>
<dl>
<dd>
<dl>
<dt><code>ptpengine:ptp_timesource [</code><i>SELECT</i><code>]</code></p>
<dd>
<dl>
<dd>
<dl>
<dt><code>options</code></p>
<dd><i>ATOMIC_CLOCK GPS TERRESTRIAL_RADIO PTP NTP HAND_SET OTHER INTERNAL_OSCILLATOR </i></p>
<dt><code>usage</code></p>
<dd>Time source announced in master state.</p>
<dt><code>default</code></p>
<dd><i>INTERNAL_OSCILLATOR</i> </p>
</dl>
</dl>
</dl>
</dl>
<dl>
<dd>
<dl>
<dt><code>ptpengine:clock_class [</code><i>INT</i><code>: 0 .. 255]</code></p>
<dd>
<dl>
<dd>
<dl>
<dt><code>usage</code></p>
<dd>Clock class &#8211; announced in master state. Always 255 for slave-only. Minimum, maximum and default values are controlled by presets. If set to 13 (application specific time source), announced time scale is always set to ARB. This setting controls the states a PTP port can be in. If below 128, port will only be in MASTER or PASSIVE states (master only). If above 127, port will be in MASTER or SLAVE states.</p>
<dt><code>default</code></p>
<dd><i>255</i> </p>
</dl>
</dl>
</dl>
</dl>
<dl>
<dd>
<dl>
<dt><code>ptpengine:priority1 [</code><i>INT</i><code>: 0 .. 248]</code></p>
<dd>
<dl>
<dd>
<dl>
<dt><code>usage</code></p>
<dd>Priority 1 announced in master state,used for Best Master <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt> Clock selection.</p>
<dt><code>default</code></p>
<dd><i>128</i> </p>
</dl>
</dl>
</dl>
</dl>
<dl>
<dd>
<dl>
<dt><code>ptpengine:priority2 [</code><i>INT</i><code>: 0 .. 248]</code></p>
<dd>
<dl>
<dd>
<dl>
<dt><code>usage</code></p>
<dd>Priority 2 announced in master state, used for Best Master <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt> Clock selection.</p>
<dt><code>default</code></p>
<dd><i>128</i> </p>
</dl>
</dl>
</dl>
</dl>
<dl>
<dd>
<dl>
<dt><code>ptpengine:max_listen [</code><i>INT</i><code>: min: 1 ]</code></p>
<dd>
<dl>
<dd>
<dl>
<dt><code>usage</code></p>
<dd>Number of consecutive protocol resets to LISTENING before full network reset.</p>
<dt><code>default</code></p>
<dd><i>5</i> </p>
</dl>
</dl>
</dl>
</dl>
<dl>
<dd>
<dl>
<dt><code>ptpengine:unicast_destinations [</code><i>STRING</i><code>]</code></p>
<dd>
<dl>
<dd>
<dl>
<dt><code>usage</code></p>
<dd>An IPv4 address or list of IPv4 addresses to be used as unicast destinations. When unicast negotiation (<i>ptpengine:unicast_negotiation</i>) is enabled, setting this is mandatory for slaves as they must be aware of which GMs to request messages from. When unicast negotiation is disabled, setting this is mandatory for GMs, as they must deliver messages to a pre-configured group of slaves.</p>
<dt><code>default</code></p>
<dd><i>[none]</i> </p>
</dl>
</dl>
</dl>
</dl>
<dl>
<dd>
<dl>
<dt><code>ptpengine:unicast_domains [</code><i>STRING</i><code>]</code></p>
<dd>
<dl>
<dd>
<dl>
<dt><code>usage</code></p>
<dd>Specify PTP domain number for each configured unicast destination (<i>ptpengine:unicast_destinations</i>). This is only used by slave-only clocks using unicast destinations to allow for each master to be in a separate domain, such as with Telecom Profile. The number of entries should match the number of unicast destinations, otherwise unconfigured domains or domains set to 0 are set to domain configured in <i>ptpengine:domain</i>. The format is a comma, tab or space-separated list of 8-bit unsigned integers (0 .. 255).</p>
<dt><code>default</code></p>
<dd><i>[none]</i> </p>
</dl>
</dl>
</dl>
</dl>
<dl>
<dd>
<dl>
<dt><code>ptpengine:unicast_local_preference [</code><i>STRING</i><code>]</code></p>
<dd>
<dl>
<dd>
<dl>
<dt><code>usage</code></p>
<dd>Specify a local preference for each configured unicast destination (<i>ptpengine:unicast_destinations</i>). This is only used by slave-only clocks using unicast destinations to allow for each master&#8217;s BMC selection to be influenced locally by the slave, such as with Telecom Profile. The number of entries should match the number of unicast destinations, otherwise unconfigured preference is set to 0 (highest). The format is a comma, tab or space-separated list of 8-bit unsigned integers (0 .. 255).</p>
<dt><code>default</code></p>
<dd><i>[none]</i> </p>
</dl>
</dl>
</dl>
</dl>
<dl>
<dd>
<dl>
<dt><code>ptpengine:unicast_peer_destination [</code><i>STRING</i><code>]</code></p>
<dd>
<dl>
<dd>
<dl>
<dt><code>usage</code></p>
<dd>When using IP unicast mode (<i>ptpengine:ip_mode=unicast</i>) and Peer to Peer delay mechanism (<i>ptpengine:delay_mechanism=P2P</i>), a peer unicast destination must be configured to request the peer delay from. Format is a single unicast IPv4 address.</p>
<dt><code>default</code></p>
<dd><i>[none]</i> </p>
</dl>
</dl>
</dl>
</dl>
<dl>
<dd>
<dl>
<dt><code>ptpengine:management_enable [</code><i>BOOLEAN</i><code>]</code></p>
<dd>
<dl>
<dd>
<dl>
<dt><code>usage</code></p>
<dd>Enable handling of PTP management messages. Only GET messages are processed by default. See <i>ptpengine:management_set_enable</i>.</p>
<dt><code>default</code></p>
<dd><i>Y</i> </p>
</dl>
</dl>
</dl>
</dl>
<dl>
<dd>
<dl>
<dt><code>ptpengine:management_set_enable [</code><i>BOOLEAN</i><code>]</code></p>
<dd>
<dl>
<dd>
<dl>
<dt><code>usage</code></p>
<dd>Accept SET and COMMAND management messages.</p>
<dt><code>default</code></p>
<dd><i>N</i> </p>
</dl>
</dl>
</dl>
</dl>
<dl>
<dd>
<dl>
<dt><code>ptpengine:igmp_refresh [</code><i>BOOLEAN</i><code>]</code></p>
<dd>
<dl>
<dd>
<dl>
<dt><code>usage</code></p>
<dd>Send explicit IGMP joins between engine resets and periodically <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt> in master state.</p>
<dt><code>default</code></p>
<dd><i>Y</i> </p>
</dl>
</dl>
</dl>
</dl>
<dl>
<dd>
<dl>
<dt><code>ptpengine:master_igmp_refresh_interval [</code><i>INT</i><code>: 0 .. 255]</code></p>
<dd>
<dl>
<dd>
<dl>
<dt><code>usage</code></p>
<dd>Periodic IGMP join interval (seconds) in master state when running IPv4 multicast: when set below 10 or when ptpengine:igmp_refresh is disabled, this setting has no effect.</p>
<dt><code>default</code></p>
<dd><i>60</i> </p>
</dl>
</dl>
</dl>
</dl>
<dl>
<dd>
<dl>
<dt><code>ptpengine:multicast_ttl [</code><i>INT</i><code>: 1 .. 64]</code></p>
<dd>
<dl>
<dd>
<dl>
<dt><code>usage</code></p>
<dd>Multicast time to live for multicast PTP packets (ignored and set to 1 for peer to peer messages).</p>
<dt><code>default</code></p>
<dd><i>64</i> </p>
</dl>
</dl>
</dl>
</dl>
<dl>
<dd>
<dl>
<dt><code>ptpengine:ip_dscp [</code><i>INT</i><code>: 0 .. 63]</code></p>
<dd>
<dl>
<dd>
<dl>
<dt><code>usage</code></p>
<dd>DiffServ CodepPoint for packet prioritisation (decimal). When set to zero, this option is not used. Use 46 for Expedited Forwarding (0x2e).</p>
<dt><code>default</code></p>
<dd><i>0</i> </p>
</dl>
</dl>
</dl>
</dl>
<dl>
<dd>
<dl>
<dt><code>ptpengine:sync_stat_filter_enable [</code><i>BOOLEAN</i><code>]</code></p>
<dd>
<dl>
<dd>
<dl>
<dt><code>usage</code></p>
<dd>Enable statistical filter for Sync messages</p>
<dt><code>default</code></p>
<dd><i>N</i> </p>
</dl>
</dl>
</dl>
</dl>
<dl>
<dd>
<dl>
<dt><code>ptpengine:sync_stat_filter_type [</code><i>SELECT</i><code>]</code></p>
<dd>
<dl>
<dd>
<dl>
<dt><code>options</code></p>
<dd><i>none mean min max absmin absmax median </i></p>
<dt><code>usage</code></p>
<dd>Type of filter used for Sync message filtering:</p>
<dl>
<dd>
<dl>
<dt><i>none</i></p>
<dd>no filtering &#8211; pass-through</p>
<dt><i>mean</i></p>
<dd>mean (average) &#8211; smooth results but influenced by outliers</p>
<dt><i>min</i></p>
<dd>minimal value &#8211; useful for high packet delay variation (&quot;lucky packets&quot;)</p>
<dt><i>max</i></p>
<dd>maximal value &#8211; useful for testing worst case scenarios</p>
<dt><i>absmin</i></p>
<dd>absolute minimum &#8211; value closest to zero. Also useful for test purposes.</p>
<dt><i>absmax</i></p>
<dd>absolute maximun value farthest away from zero</p>
<dt><i>median</i></p>
<dd>median (middle value) &#8211; more robust than mean, not influenced by outliers</dl>
</dl>
<dt><code>default</code></p>
<dd><i>min</i> </p>
</dl>
</dl>
</dl>
</dl>
<dl>
<dd>
<dl>
<dt><code>ptpengine:sync_stat_filter_window [</code><i>INT</i><code>: 3 .. 128]</code></p>
<dd>
<dl>
<dd>
<dl>
<dt><code>usage</code></p>
<dd>Number of samples used for the Sync statistical filter</p>
<dt><code>default</code></p>
<dd><i>4</i> </p>
</dl>
</dl>
</dl>
</dl>
<dl>
<dd>
<dl>
<dt><code>ptpengine:sync_stat_filter_window_type [</code><i>SELECT</i><code>]</code></p>
<dd>
<dl>
<dd>
<dl>
<dt><code>options</code></p>
<dd><i>sliding interval</i></p>
<dt><code>usage</code></p>
<dd>Sampling window behaviour for the Sync statistical filter:</p>
<dl>
<dd>
<dl>
<dt><i>sliding</i></p>
<dd>sliding window &#8211; a value is output every time the filter runs, which can result in duplicates</p>
<dt><i>interval</i></p>
<dd>only output a value every n-th sample (full window) &#8211; independent sampling periods</dl>
</dl>
<dt><code>default</code></p>
<dd><i>sliding</i> </p>
</dl>
</dl>
</dl>
</dl>
<dl>
<dd>
<dl>
<dt><code>ptpengine:delay_stat_filter_enable [</code><i>BOOLEAN</i><code>]</code></p>
<dd>
<dl>
<dd>
<dl>
<dt><code>usage</code></p>
<dd>Enable statistical filter for Delay messages</p>
<dt><code>default</code></p>
<dd><i>N</i> </p>
</dl>
</dl>
</dl>
</dl>
<dl>
<dd>
<dl>
<dt><code>ptpengine:delay_stat_filter_type [</code><i>SELECT</i><code>]</code></p>
<dd>
<dl>
<dd>
<dl>
<dt><code>options</code></p>
<dd><i>none mean min max absmin absmax median </i></p>
<dt><code>usage</code></p>
<dd>Type of filter used for Delay message filtering:</p>
<dl>
<dd>
<dl>
<dt><i>none</i></p>
<dd>no filtering &#8211; pass-through</p>
<dt><i>mean</i></p>
<dd>mean (average) &#8211; smooth results but influenced by outliers</p>
<dt><i>min</i></p>
<dd>minimal value &#8211; useful for high packet delay variation (&quot;lucky packets&quot;)</p>
<dt><i>max</i></p>
<dd>maximal value &#8211; useful for testing worst case scenarios</p>
<dt><i>absmin</i></p>
<dd>absolute minimum &#8211; value closest to zero. Also useful for test purposes.</p>
<dt><i>absmax</i></p>
<dd>absolute maximun value farthest away from zero</p>
<dt><i>median</i></p>
<dd>median (middle value) &#8211; more robust than mean, not influenced by outliers</dl>
</dl>
<dt><code>default</code></p>
<dd><i>min</i> </p>
</dl>
</dl>
</dl>
</dl>
<dl>
<dd>
<dl>
<dt><code>ptpengine:delay_stat_filter_window [</code><i>INT</i><code>: 3 .. 128]</code></p>
<dd>
<dl>
<dd>
<dl>
<dt><code>usage</code></p>
<dd>Number of samples used for the Delay statistical filter</p>
<dt><code>default</code></p>
<dd><i>4</i> </p>
</dl>
</dl>
</dl>
</dl>
<dl>
<dd>
<dl>
<dt><code>ptpengine:delay_stat_filter_window_type [</code><i>SELECT</i><code>]</code></p>
<dd>
<dl>
<dd>
<dl>
<dt><code>options</code></p>
<dd><i>sliding interval</i></p>
<dt><code>usage</code></p>
<dd>Sampling window behaviour for the Delay statistical filter:</p>
<dl>
<dd>
<dl>
<dt><i>sliding</i></p>
<dd>sliding window &#8211; a value is output every time the filter runs, which can result in duplicates</p>
<dt><i>interval</i></p>
<dd>only output a value every n-th sample (full window) &#8211; independent sampling periods</dl>
</dl>
<dt><code>default</code></p>
<dd><i>sliding</i> </p>
</dl>
</dl>
</dl>
</dl>
<dl>
<dd>
<dl>
<dt><code>ptpengine:delay_outlier_filter_enable [</code><i>BOOLEAN</i><code>]</code></p>
<dd>
<dl>
<dd>
<dl>
<dt><code>usage</code></p>
<dd>Enable outlier filter for the Delay Response component in slave state</p>
<dt><code>default</code></p>
<dd><i>N</i> </p>
</dl>
</dl>
</dl>
</dl>
<dl>
<dd>
<dl>
<dt><code>ptpengine:delay_outlier_filter_action [</code><i>SELECT</i><code>]</code></p>
<dd>
<dl>
<dd>
<dl>
<dt><code>options</code></p>
<dd><i>discard filter </i></p>
<dt><code>usage</code></p>
<dd>Delay Response outlier filter action. If set to &#8216;filter&#8217;, outliers are <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt> replaced with moving average.</p>
<dt><code>default</code></p>
<dd><i>discard</i> </p>
</dl>
</dl>
</dl>
</dl>
<dl>
<dd>
<dl>
<dt><code>ptpengine:delay_outlier_filter_capacity [</code><i>INT</i><code>: 4 .. 60]</code></p>
<dd>
<dl>
<dd>
<dl>
<dt><code>usage</code></p>
<dd>Number of samples in the Delay Response outlier filter buffer</p>
<dt><code>default</code></p>
<dd><i>20</i> </p>
</dl>
</dl>
</dl>
</dl>
<dl>
<dd>
<dl>
<dt><code>ptpengine:delay_outlier_filter_threshold [</code><i>FLOAT</i><code>: 0.001000 .. 1000.000000]</code></p>
<dd>
<dl>
<dd>
<dl>
<dt><code>usage</code></p>
<dd>Delay Response outlier filter threshold: multiplier for Peirce&#8217;s maximum <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt> standard deviation. When set below 1.0, filter is tighter, when set above<br />
 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt> 1.0, filter is looser than standard Peirce&#8217;s test.</p>
<dt><code>default</code></p>
<dd><i>1.000000</i> </p>
</dl>
</dl>
</dl>
</dl>
<dl>
<dd>
<dl>
<dt><code>ptpengine:delay_outlier_filter_always_filter [</code><i>BOOLEAN</i><code>]</code></p>
<dd>
<dl>
<dd>
<dl>
<dt><code>usage</code></p>
<dd>Always run the Delay Response outlier filter, even if clock is being slewed at maximum rate</p>
<dt><code>default</code></p>
<dd><i>N</i> </p>
</dl>
</dl>
</dl>
</dl>
<dl>
<dd>
<dl>
<dt><code>ptpengine:delay_outlier_filter_autotune_enable [</code><i>BOOLEAN</i><code>]</code></p>
<dd>
<dl>
<dd>
<dl>
<dt><code>usage</code></p>
<dd>Enable automatic threshold control for Delay Response outlier filter.</p>
<dt><code>default</code></p>
<dd><i>Y</i> </p>
</dl>
</dl>
</dl>
</dl>
<dl>
<dd>
<dl>
<dt><code>ptpengine:delay_outlier_filter_autotune_minpercent [</code><i>INT</i><code>: 0 .. 99]</code></p>
<dd>
<dl>
<dd>
<dl>
<dt><code>usage</code></p>
<dd>Delay Response outlier filter autotune low watermark &#8211; minimum percentage of discarded samples in the update period before filter is tightened by the autotune step value</p>
<dt><code>default</code></p>
<dd><i>20</i> </p>
</dl>
</dl>
</dl>
</dl>
<dl>
<dd>
<dl>
<dt><code>ptpengine:delay_outlier_filter_autotune_maxpercent [</code><i>INT</i><code>: 1 .. 100]</code></p>
<dd>
<dl>
<dd>
<dl>
<dt><code>usage</code></p>
<dd>Delay Response outlier filter autotune high watermark &#8211; maximum percentage of discarded samples in the update period before filter is loosened by the autotune step value</p>
<dt><code>default</code></p>
<dd><i>95</i> </p>
</dl>
</dl>
</dl>
</dl>
<dl>
<dd>
<dl>
<dt><code>ptpengine:delay_outlier_filter_autotune_step [</code><i>FLOAT</i><code>: 0.010000 .. 10.000000]</code></p>
<dd>
<dl>
<dd>
<dl>
<dt><code>usage</code></p>
<dd>The value the Delay Response outlier filter threshold is increased or decreased by when auto-tuning</p>
<dt><code>default</code></p>
<dd><i>0.100000</i> </p>
</dl>
</dl>
</dl>
</dl>
<dl>
<dd>
<dl>
<dt><code>ptpengine:delay_outlier_filter_autotune_minthreshold [</code><i>FLOAT</i><code>: 0.010000 .. 10.000000]</code></p>
<dd>
<dl>
<dd>
<dl>
<dt><code>usage</code></p>
<dd>Minimum Delay Response filter threshold value used when auto-tuning</p>
<dt><code>default</code></p>
<dd><i>0.100000</i> </p>
</dl>
</dl>
</dl>
</dl>
<dl>
<dd>
<dl>
<dt><code>ptpengine:delay_outlier_filter_autotune_maxthreshold [</code><i>FLOAT</i><code>: 0.010000 .. 10.000000]</code></p>
<dd>
<dl>
<dd>
<dl>
<dt><code>usage</code></p>
<dd>Maximum Delay Response filter threshold value used when auto-tuning</p>
<dt><code>default</code></p>
<dd><i>5.000000</i> </p>
</dl>
</dl>
</dl>
</dl>
<dl>
<dd>
<dl>
<dt><code>ptpengine:delay_outlier_weight [</code><i>FLOAT</i><code>: 0.010000 .. 2.000000]</code></p>
<dd>
<dl>
<dd>
<dl>
<dt><code>usage</code></p>
<dd>Delay Response outlier weight: if an outlier is detected, determines <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt> the amount of its deviation from mean that is used to build the standard<br />
 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt> deviation statistics and influence further outlier detection.<br />
 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt> When set to 1.0, the outlier is used as is.</p>
<dt><code>default</code></p>
<dd><i>1.000000</i> </p>
</dl>
</dl>
</dl>
</dl>
<dl>
<dd>
<dl>
<dt><code>ptpengine:delay_outlier_filter_stepdetect_enable [</code><i>BOOLEAN</i><code>]</code></p>
<dd>
<dl>
<dd>
<dl>
<dt><code>usage</code></p>
<dd>Enable Delay Response filter step detection (delaySM) to block when certain level exceeded</p>
<dt><code>default</code></p>
<dd><i>N</i> </p>
</dl>
</dl>
</dl>
</dl>
<dl>
<dd>
<dl>
<dt><code>ptpengine:delay_outlier_filter_stepdetect_threshold [</code><i>INT</i><code>: 50000 .. 999999999]</code></p>
<dd>
<dl>
<dd>
<dl>
<dt><code>usage</code></p>
<dd>Delay step detection threshold. Step detection is performed only when delaySM is below this threshold (nanoseconds)</p>
<dt><code>default</code></p>
<dd><i>1000000</i> </p>
</dl>
</dl>
</dl>
</dl>
<dl>
<dd>
<dl>
<dt><code>ptpengine:delay_outlier_filter_stepdetect_level [</code><i>INT</i><code>: 50000 .. 999999999]</code></p>
<dd>
<dl>
<dd>
<dl>
<dt><code>usage</code></p>
<dd>Delay step level. When step detection enabled and operational, delaySM above this level (nanoseconds) is considered a clock step and updates are paused</p>
<dt><code>default</code></p>
<dd><i>500000</i> </p>
</dl>
</dl>
</dl>
</dl>
<dl>
<dd>
<dl>
<dt><code>ptpengine:delay_outlier_filter_stepdetect_credit [</code><i>INT</i><code>: 50 .. 1000]</code></p>
<dd>
<dl>
<dd>
<dl>
<dt><code>usage</code></p>
<dd>Initial credit (number of samples) the Delay step detection filter can block for. When credit is exhausted, filter stops blocking. Credit is gradually restored (see <i>ptpengine:delay_outlier_filter_stepdetect_credit_increment</i>)</p>
<dt><code>default</code></p>
<dd><i>200</i> </p>
</dl>
</dl>
</dl>
</dl>
<dl>
<dd>
<dl>
<dt><code>ptpengine:delay_outlier_filter_stepdetect_credit_increment [</code><i>INT</i><code>: 1 .. 100]</code></p>
<dd>
<dl>
<dd>
<dl>
<dt><code>usage</code></p>
<dd>Amount of credit for the Delay step detection filter restored every full sample window</p>
<dt><code>default</code></p>
<dd><i>10</i> </p>
</dl>
</dl>
</dl>
</dl>
<dl>
<dd>
<dl>
<dt><code>ptpengine:sync_outlier_filter_enable [</code><i>BOOLEAN</i><code>]</code></p>
<dd>
<dl>
<dd>
<dl>
<dt><code>usage</code></p>
<dd>Enable outlier filter for the Sync component in slave state.</p>
<dt><code>default</code></p>
<dd><i>N</i> </p>
</dl>
</dl>
</dl>
</dl>
<dl>
<dd>
<dl>
<dt><code>ptpengine:sync_outlier_filter_action [</code><i>SELECT</i><code>]</code></p>
<dd>
<dl>
<dd>
<dl>
<dt><code>options</code></p>
<dd><i>discard filter </i></p>
<dt><code>usage</code></p>
<dd>Sync outlier filter action. If set to &#8216;filter&#8217;, outliers are replaced <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt> with moving average.</p>
<dt><code>default</code></p>
<dd><i>discard</i> </p>
</dl>
</dl>
</dl>
</dl>
<dl>
<dd>
<dl>
<dt><code>ptpengine:sync_outlier_filter_capacity [</code><i>INT</i><code>: 4 .. 60]</code></p>
<dd>
<dl>
<dd>
<dl>
<dt><code>usage</code></p>
<dd>Number of samples in the Sync outlier filter buffer.</p>
<dt><code>default</code></p>
<dd><i>20</i> </p>
</dl>
</dl>
</dl>
</dl>
<dl>
<dd>
<dl>
<dt><code>ptpengine:sync_outlier_filter_threshold [</code><i>FLOAT</i><code>: 0.001000 .. 1000.000000]</code></p>
<dd>
<dl>
<dd>
<dl>
<dt><code>usage</code></p>
<dd>Sync outlier filter threshold: multiplier for the Peirce&#8217;s maximum standard <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt> deviation. When set below 1.0, filter is tighter, when set above 1.0,<br />
 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt> filter is looser than standard Peirce&#8217;s test.</p>
<dt><code>default</code></p>
<dd><i>1.000000</i> </p>
</dl>
</dl>
</dl>
</dl>
<dl>
<dd>
<dl>
<dt><code>ptpengine:sync_outlier_filter_always_filter [</code><i>BOOLEAN</i><code>]</code></p>
<dd>
<dl>
<dd>
<dl>
<dt><code>usage</code></p>
<dd>Always run the Sync outlier filter, even if clock is being slewed at maximum rate</p>
<dt><code>default</code></p>
<dd><i>N</i> </p>
</dl>
</dl>
</dl>
</dl>
<dl>
<dd>
<dl>
<dt><code>ptpengine:sync_outlier_filter_autotune_enable [</code><i>BOOLEAN</i><code>]</code></p>
<dd>
<dl>
<dd>
<dl>
<dt><code>usage</code></p>
<dd>Enable automatic threshold control for Sync outlier filter.</p>
<dt><code>default</code></p>
<dd><i>Y</i> </p>
</dl>
</dl>
</dl>
</dl>
<dl>
<dd>
<dl>
<dt><code>ptpengine:sync_outlier_filter_autotune_minpercent [</code><i>INT</i><code>: 0 .. 99]</code></p>
<dd>
<dl>
<dd>
<dl>
<dt><code>usage</code></p>
<dd>Sync outlier filter autotune low watermark &#8211; minimum percentage of discarded samples in the update period before filter is tightened by the autotune step value</p>
<dt><code>default</code></p>
<dd><i>20</i> </p>
</dl>
</dl>
</dl>
</dl>
<dl>
<dd>
<dl>
<dt><code>ptpengine:sync_outlier_filter_autotune_maxpercent [</code><i>INT</i><code>: 1 .. 100]</code></p>
<dd>
<dl>
<dd>
<dl>
<dt><code>usage</code></p>
<dd>Sync outlier filter autotune high watermark &#8211; maximum percentage of discarded samples in the update period before filter is loosened by the autotune step value</p>
<dt><code>default</code></p>
<dd><i>95</i> </p>
</dl>
</dl>
</dl>
</dl>
<dl>
<dd>
<dl>
<dt><code>ptpengine:sync_outlier_filter_autotune_step [</code><i>FLOAT</i><code>: 0.010000 .. 10.000000]</code></p>
<dd>
<dl>
<dd>
<dl>
<dt><code>usage</code></p>
<dd>The value the Sync outlier filter threshold is increased or decreased by when auto-tuning</p>
<dt><code>default</code></p>
<dd><i>0.100000</i> </p>
</dl>
</dl>
</dl>
</dl>
<dl>
<dd>
<dl>
<dt><code>ptpengine:sync_outlier_filter_autotune_minthreshold [</code><i>FLOAT</i><code>: 0.010000 .. 10.000000]</code></p>
<dd>
<dl>
<dd>
<dl>
<dt><code>usage</code></p>
<dd>Minimum Sync filter threshold value used when auto-tuning</p>
<dt><code>default</code></p>
<dd><i>0.100000</i> </p>
</dl>
</dl>
</dl>
</dl>
<dl>
<dd>
<dl>
<dt><code>ptpengine:sync_outlier_filter_autotune_maxthreshold [</code><i>FLOAT</i><code>: 0.010000 .. 10.000000]</code></p>
<dd>
<dl>
<dd>
<dl>
<dt><code>usage</code></p>
<dd>Maximum Sync filter threshold value used when auto-tuning</p>
<dt><code>default</code></p>
<dd><i>5.000000</i> </p>
</dl>
</dl>
</dl>
</dl>
<dl>
<dd>
<dl>
<dt><code>ptpengine:sync_outlier_weight [</code><i>FLOAT</i><code>: 0.010000 .. 2.000000]</code></p>
<dd>
<dl>
<dd>
<dl>
<dt><code>usage</code></p>
<dd>Sync outlier weight: if an outlier is detected, this value determines the<br />
&nbsp;<wbr>amount of its deviation from mean that is used to build the standard&nbsp;<wbr><br />
&nbsp;<wbr>deviation statistics and influence further outlier detection.<br />
&nbsp;<wbr>When set to 1.0, the outlier is used as is</p>
<dt><code>default</code></p>
<dd><i>1.000000</i> </p>
</dl>
</dl>
</dl>
</dl>
<dl>
<dd>
<dl>
<dt><code>ptpengine:sync_outlier_filter_stepdetect_enable [</code><i>BOOLEAN</i><code>]</code></p>
<dd>
<dl>
<dd>
<dl>
<dt><code>usage</code></p>
<dd>Enable Sync filter step detection (delayMS) to block when certain level exceeded</p>
<dt><code>default</code></p>
<dd><i>N</i> </p>
</dl>
</dl>
</dl>
</dl>
<dl>
<dd>
<dl>
<dt><code>ptpengine:sync_outlier_filter_stepdetect_threshold [</code><i>INT</i><code>: 50000 .. 999999999]</code></p>
<dd>
<dl>
<dd>
<dl>
<dt><code>usage</code></p>
<dd>Sync step detection threshold. Step detection is performed only when delayMS is below this threshold (nanoseconds)</p>
<dt><code>default</code></p>
<dd><i>1000000</i> </p>
</dl>
</dl>
</dl>
</dl>
<dl>
<dd>
<dl>
<dt><code>ptpengine:sync_outlier_filter_stepdetect_level [</code><i>INT</i><code>: 50000 .. 999999999]</code></p>
<dd>
<dl>
<dd>
<dl>
<dt><code>usage</code></p>
<dd>Sync step level. When step detection enabled and operational, delayMS above this level (nanoseconds) is considered a clock step and updates are paused</p>
<dt><code>default</code></p>
<dd><i>500000</i> </p>
</dl>
</dl>
</dl>
</dl>
<dl>
<dd>
<dl>
<dt><code>ptpengine:sync_outlier_filter_stepdetect_credit [</code><i>INT</i><code>: 50 .. 1000]</code></p>
<dd>
<dl>
<dd>
<dl>
<dt><code>usage</code></p>
<dd>Initial credit (number of samples) the Sync step detection filter can block for. When credit is exhausted, filter stops blocking. Credit is gradually restored (see <i>ptpengine:sync_outlier_filter_stepdetect_credit_increment</i>)</p>
<dt><code>default</code></p>
<dd><i>200</i> </p>
</dl>
</dl>
</dl>
</dl>
<dl>
<dd>
<dl>
<dt><code>ptpengine:sync_outlier_filter_stepdetect_credit_increment [</code><i>INT</i><code>: 1 .. 100]</code></p>
<dd>
<dl>
<dd>
<dl>
<dt><code>usage</code></p>
<dd>Amount of credit for the Sync step detection filter restored every full sample window</p>
<dt><code>default</code></p>
<dd><i>10</i> </p>
</dl>
</dl>
</dl>
</dl>
<dl>
<dd>
<dl>
<dt><code>ptpengine:sync_sequence_checking [</code><i>BOOLEAN</i><code>]</code></p>
<dd>
<dl>
<dd>
<dl>
<dt><code>usage</code></p>
<dd>When enabled, Sync messages will only be accepted if sequence ID is increasing. <code>note:</code> This can cause the slave to temporarily lock up if GM restarts before announce timeout, so this is limited to 50 consecutive sequence errors. Alternatively, <i>ptpengine:clock_update_timeout</i> can be used to reset the slave beforehand.</p>
<dt><code>default</code></p>
<dd><i>N</i> </p>
</dl>
</dl>
</dl>
</dl>
<dl>
<dd>
<dl>
<dt><code>ptpengine:clock_update_timeout [</code><i>INT</i><code>: 0 .. 3600]</code></p>
<dd>
<dl>
<dd>
<dl>
<dt><code>usage</code></p>
<dd>If set to non-zero, time (seconds) before slave is reset back into PTP_LISTENING, if thetre were no clock updates. This is useful for situations where slave is in SLAVE state (receiving Announce) but is not receiving or not accepting Sync messages.</p>
<dt><code>default</code></p>
<dd><i>0</i> </p>
</dl>
</dl>
</dl>
</dl>
<dl>
<dd>
<dl>
<dt><code>ptpengine:calibration_delay [</code><i>INT</i><code>: 0 .. 300]</code></p>
<dd>
<dl>
<dd>
<dl>
<dt><code>usage</code></p>
<dd>Delay between moving to slave state and enabling clock updates (seconds). This allows mean path delay to stabilise before starting clock updates. Activated when going into slave state and during slave&#8217;s GM failover. 0 &#8211; not used.</p>
<dt><code>default</code></p>
<dd><i>0</i> </p>
</dl>
</dl>
</dl>
</dl>
<dl>
<dd>
<dl>
<dt><code>ptpengine:idle_timeout [</code><i>INT</i><code>: 10 .. 3600]</code></p>
<dd>
<dl>
<dd>
<dl>
<dt><code>usage</code></p>
<dd>PTP idle timeout (seconds): if PTPd is in SLAVE state and there have been no clock updates for this amout of time, PTPd releases clock control.</p>
<dt><code>default</code></p>
<dd>0 </p>
</dl>
</dl>
</dl>
</dl>
<dl>
<dd>
<dl>
<dt><code>ptpengine:panic_mode [</code><i>BOOLEAN</i><code>]</code></p>
<dd>
<dl>
<dd>
<dl>
<dt><code>usage</code></p>
<dd>Enable panic mode: when offset from master is above 1 second, stop updating the clock for a period of time and then step the clock if offset remains above 1 second.</p>
<dt><code>default</code></p>
<dd><i>N</i> </p>
</dl>
</dl>
</dl>
</dl>
<dl>
<dd>
<dl>
<dt><code>ptpengine:panic_mode_duration [</code><i>INT</i><code>: 1 .. 60]</code></p>
<dd>
<dl>
<dd>
<dl>
<dt><code>usage</code></p>
<dd>Duration (minutes) of the panic mode period (no clock updates) when offset above 1 second detected.</p>
<dt><code>default</code></p>
<dd><i>2</i> </p>
</dl>
</dl>
</dl>
</dl>
<dl>
<dd>
<dl>
<dt><code>ptpengine:panic_mode_release_clock [</code><i>BOOLEAN</i><code>]</code></p>
<dd>
<dl>
<dd>
<dl>
<dt><code>usage</code></p>
<dd>When entering panic mode, release clock control while panic mode lasts. If not set, PTP will hold clock control during panic mode. If set together with ntpengine:* configured, this will fail over to NTP.</p>
<dt><code>default</code></p>
<dd><i>N</i> </p>
</dl>
</dl>
</dl>
</dl>
<dl>
<dd>
<dl>
<dt><code>ptpengine:panic_mode_exit_threshold [</code><i>INT</i><code>: 0 .. 999999999]</code></p>
<dd>
<dl>
<dd>
<dl>
<dt><code>usage</code></p>
<dd>Do not exit panic mode until offset drops below this value (nanoseconds). 0 = not used.</p>
<dt><code>default</code></p>
<dd><i>0</i> </p>
</dl>
</dl>
</dl>
</dl>
<dl>
<dd>
<dl>
<dt><code>ptpengine:pid_as_clock_identity [</code><i>BOOLEAN</i><code>]</code></p>
<dd>
<dl>
<dd>
<dl>
<dt><code>usage</code></p>
<dd>Use PTPd&#8217;s process ID as the middle part of the PTP clock ID &#8211; useful for running multiple instances.</p>
<dt><code>default</code></p>
<dd><i>N</i> </p>
</dl>
</dl>
</dl>
</dl>
<dl>
<dd>
<dl>
<dt><code>ptpengine:ntp_failover [</code><i>BOOLEAN</i><code>]</code></p>
<dd>
<dl>
<dd>
<dl>
<dt><code>usage</code></p>
<dd>Fail over to NTP when PTP time sync not available &#8211; requires ntpengine:enabled, but does not require the rest of NTP configuration: will warn instead of failing over if cannot control ntpd.</p>
<dt><code>default</code></p>
<dd><i>N</i> </p>
</dl>
</dl>
</dl>
</dl>
<dl>
<dd>
<dl>
<dt><code>ptpengine:ntp_failover_timeout [</code><i>INT</i><code>: 0 .. 1800]</code></p>
<dd>
<dl>
<dd>
<dl>
<dt><code>usage</code></p>
<dd>NTP failover timeout in seconds: time between PTP slave going into LISTENING state, and failing over to NTP. 0 = fail over immediately. This setting controls the time provider election hold time.</p>
<dt><code>default</code></p>
<dd><i>60</i> </p>
</dl>
</dl>
</dl>
</dl>
<dl>
<dd>
<dl>
<dt><code>ptpengine:prefer_ntp [</code><i>BOOLEAN</i><code>]</code></p>
<dd>
<dl>
<dd>
<dl>
<dt><code>usage</code></p>
<dd>Prefer NTP time synchronisation. Only use PTP when NTP not available. Could be used when NTP runs with a local GPS receiver or another hardware reference.</p>
<dt><code>default</code></p>
<dd><i>N</i> </p>
</dl>
</dl>
</dl>
</dl>
<dl>
<dd>
<dl>
<dt><code>ptpengine:panic_mode_ntp [</code><i>BOOLEAN</i><code>]</code></p>
<dd>
<dl>
<dd>
<dl>
<dt><code>usage</code></p>
<dd>Deprecated as of 2.3.1, but still supported: see <i>ptppengine:panic_mode_release_clock</i>.</p>
<dt><code>default</code></p>
<dd><i>N</i> </p>
</dl>
</dl>
</dl>
</dl>
<dl>
<dd>
<dl>
<dt><code>ptpengine:sigusr2_clears_counters [</code><i>BOOLEAN</i><code>]</code></p>
<dd>
<dl>
<dd>
<dl>
<dt><code>usage</code></p>
<dd>Clear counters after dumping all counter values on SIGUSR2.</p>
<dt><code>default</code></p>
<dd><i>N</i> </p>
</dl>
</dl>
</dl>
</dl>
<dl>
<dd>
<dl>
<dt><code>ptpengine:timing_acl_permit [</code><i>STRING</i><code>]</code></p>
<dd>
<dl>
<dd>
<dl>
<dt><code>usage</code></p>
<dd>Permit access control list for timing and signaling messages. Format is a series of network prefixes and/or IP addresses separated by commas, spaces, tabs or semicolons. Accepted format is CIDR notation (a.b.c.d/mm), single IP address (a.b.c.d), or full network/mask (a.b.c.d/m.m.m.m). Shortcuts can be used: 172.16/12 is expanded to 172.16.0.0/12; 192.168/255.255 is expanded to 192.168.0.0/255.255.0.0, etc. The match is performed on the source IP address of the incoming messages. IP access lists are only supported when using the IP transport.</p>
<dt><code>default</code></p>
<dd><i>[none]</i> </p>
</dl>
</dl>
</dl>
</dl>
<dl>
<dd>
<dl>
<dt><code>ptpengine:timing_acl_deny [</code><i>STRING</i><code>]</code></p>
<dd>
<dl>
<dd>
<dl>
<dt><code>usage</code></p>
<dd>Deny access control list for timing and signaling messages. Format is a series of network prefixes and/or IP addresses separated by commas, spaces, tabs or semicolons. Accepted format is CIDR notation (a.b.c.d/mm), single IP address (a.b.c.d), or full network/mask (a.b.c.d/m.m.m.m). Shortcuts can be used: 172.16/12 is expanded to 172.16.0.0/12; 192.168/255.255 is expanded to 192.168.0.0/255.255.0.0, etc. The match is performed on the source IP address of the incoming messages. IP access lists are only supported when using the IP transport.</p>
<dt><code>default</code></p>
<dd><i>[none]</i> </p>
</dl>
</dl>
</dl>
</dl>
<dl>
<dd>
<dl>
<dt><code>ptpengine:management_acl_permit [</code><i>STRING</i><code>]</code></p>
<dd>
<dl>
<dd>
<dl>
<dt><code>usage</code></p>
<dd>Permit access control list for management messages. Format is a series of network prefixes and/or IP addresses separated by commas, spaces, tabs or semicolons. Accepted format is CIDR notation (a.b.c.d/mm), single IP address (a.b.c.d), or full network/mask (a.b.c.d/m.m.m.m). Shortcuts can be used: 172.16/12 is expanded to 172.16.0.0/12; 192.168/255.255 is expanded to 192.168.0.0/255.255.0.0, etc. The match is performed on the source IP address of the incoming messages. IP access lists are only supported when using the IP transport.</p>
<dt><code>default</code></p>
<dd><i>[none]</i> </p>
</dl>
</dl>
</dl>
</dl>
<dl>
<dd>
<dl>
<dt><code>ptpengine:management_acl_deny [</code><i>STRING</i><code>]</code></p>
<dd>
<dl>
<dd>
<dl>
<dt><code>usage</code></p>
<dd>Deny access control list for management messages. Format is a series of network prefixes and/or IP addresses separated by commas, spaces, tabs or semicolons. Accepted format is CIDR notation (a.b.c.d/mm), single IP address (a.b.c.d), or full network/mask (a.b.c.d/m.m.m.m). Shortcuts can be used: 172.16/12 is expanded to 172.16.0.0/12; 192.168/255.255 is expanded to 192.168.0.0/255.255.0.0, etc. The match is performed on the source IP address of the incoming messages. IP access lists are only supported when using the IP transport.</p>
<dt><code>default</code></p>
<dd><i>[none]</i> </p>
</dl>
</dl>
</dl>
</dl>
<dl>
<dd>
<dl>
<dt><code>ptpengine:timing_acl_order [</code><i>SELECT</i><code>]</code></p>
<dd>
<dl>
<dd>
<dl>
<dt><code>options</code></p>
<dd><i>permit-deny deny-permit </i></p>
<dt><code>usage</code></p>
<dd>Order in which permit and deny access lists are evaluated for timing and signaling messages, the evaluation process is the same as for Apache httpd. <code>See: </code><i><a rel="nofollow" href="http://httpd.apache.org/docs/current/mod/mod_access_compat.html#order">http://httpd.apache.org/docs/current/mod/mod_access_compat.html#order</a></i></p>
<dt><code>default</code></p>
<dd><i>deny-permit</i> </p>
</dl>
</dl>
</dl>
</dl>
<dl>
<dd>
<dl>
<dt><code>ptpengine:management_acl_order [</code><i>SELECT</i><code>]</code></p>
<dd>
<dl>
<dd>
<dl>
<dt><code>options</code></p>
<dd><i>permit-deny deny-permit </i></p>
<dt><code>usage</code></p>
<dd>Order in which permit and deny access lists are evaluated for management messages, the evaluation process is the same as for Apache httpd. <code>See: </code><i><a rel="nofollow" href="http://httpd.apache.org/docs/current/mod/mod_access_compat.html#order">http://httpd.apache.org/docs/current/mod/mod_access_compat.html#order</a></i></p>
<dt><code>default</code></p>
<dd><i>deny-permit</i> </p>
</dl>
</dl>
</dl>
</dl>
<dl>
<dd>
<dl>
<dt><code>clock:no_adjust [</code><i>BOOLEAN</i><code>]</code></p>
<dd>
<dl>
<dd>
<dl>
<dt><code>usage</code></p>
<dd>Do not adjust the clock.</p>
<dt><code>default</code></p>
<dd><i>N</i> </p>
</dl>
</dl>
</dl>
</dl>
<dl>
<dd>
<dl>
<dt><code>clock:no_reset [</code><i>BOOLEAN</i><code>]</code></p>
<dd>
<dl>
<dd>
<dl>
<dt><code>usage</code></p>
<dd>Do not reset the clock &#8211; only slew.</p>
<dt><code>default</code></p>
<dd><i>N</i> </p>
</dl>
</dl>
</dl>
</dl>
<dl>
<dd>
<dl>
<dt><code>clock:step_startup_force [</code><i>BOOLEAN</i><code>]</code></p>
<dd>
<dl>
<dd>
<dl>
<dt><code>usage</code></p>
<dd>Force clock step on first sync after startup regardless of offset and <i>clock:no_reset</i></p>
<dt><code>default</code></p>
<dd><i>N</i> </p>
</dl>
</dl>
</dl>
</dl>
<dl>
<dd>
<dl>
<dt><code>clock:step_startup [</code><i>BOOLEAN</i><code>]</code></p>
<dd>
<dl>
<dd>
<dl>
<dt><code>usage</code></p>
<dd>Step clock on startup only if offset &gt;= 1 second, ignoring panic mode and <i>clock:no_reset</i></p>
<dt><code>default</code></p>
<dd><i>N</i> </p>
</dl>
</dl>
</dl>
</dl>
<dl>
<dd>
<dl>
<dt><code>clock:set_rtc_on_step [</code><i>BOOLEAN</i><code>]</code></p>
<dd>
<dl>
<dd>
<dl>
<dt><code>usage</code></p>
<dd>Attempt setting the RTC when stepping clock (Linux only &#8211; FreeBSD does this for us. <code>WARNING:</code> this will always set the RTC to OS clock time, regardless of time zones, so this assumes that RTC runs in UTC or otherwise in the same timescale as PTP. True at least on most single-boot x86 Linux systems.</p>
<dt><code>default</code></p>
<dd><i>N</i> </p>
</dl>
</dl>
</dl>
</dl>
<dl>
<dd>
<dl>
<dt><code>clock:drift_handling [</code><i>SELECT</i><code>]</code></p>
<dd>
<dl>
<dd>
<dl>
<dt><code>options</code></p>
<dd><i>reset preserve file </i></p>
<dt><code>usage</code></p>
<dd>Observed drift handling method between servo restarts:</p>
<dl>
<dd>
<dl>
<dt><i>reset</i></p>
<dd>set to zero (not recommended)</p>
<dt><i>preserve</i></p>
<dd>use kernel value</p>
<dt><i>file</i></p>
<dd>load/save to drift file on startup/shutdown, use kernel value inbetween. To specify drift file, use the <code>clock:drift_file</code> setting.</dl>
</dl>
<dt><code>default</code></p>
<dd><i>preserve</i> </p>
</dl>
</dl>
</dl>
</dl>
<dl>
<dd>
<dl>
<dt><code>clock:drift_file [</code><i>STRING</i><code>]</code></p>
<dd>
<dl>
<dd>
<dl>
<dt><code>usage</code></p>
<dd>Specify drift file</p>
<dt><code>default</code></p>
<dd><i>/etc/ptpd2_kernelclock.drift</i> </p>
</dl>
</dl>
</dl>
</dl>
<dl>
<dd>
<dl>
<dt><code>clock:leap_seconds_file [</code><i>STRING</i><code>]</code></p>
<dd>
<dl>
<dd>
<dl>
<dt><code>usage</code></p>
<dd>Specify leap second file location (up to date version can be downloaded from: <a rel="nofollow" href="http://www.ietf.org/timezones/data/leap-seconds.list">http://www.ietf.org/timezones/data/leap-seconds.list</a>). When configured, PTP master will use data from this file to announce leap flags and UTC offset, overriding OS information, and PTP slave will use data from this file as well as information supplied by the GM. If configured, this file is always reloaded on configuration reload (SIGHUP), reloaded on clock step and reloaded after a leap second event to ensure the information is up to date. As of ptpd 2.3.1, the file is bundled with ptpd and is installed into (prefix)/share/ptpd/leap-seconds.list.ddMMMyyyy where ddMMMyyyy is the leap seconds file expiry date.</p>
<dt><code>default</code></p>
<dd><i>[none]</i> </p>
</dl>
</dl>
</dl>
</dl>
<dl>
<dd>
<dl>
<dt><code>clock:leap_second_pause_period [</code><i>INT</i><code>: 5 .. 600]</code></p>
<dd>
<dl>
<dd>
<dl>
<dt><code>usage</code></p>
<dd>Time (seconds) before and after midnight that clock updates should be suspended for during a leap second event. The total duration of the pause is twice the configured duration. Clock updates are suspended when there is a leap second event pending and time to midnight is less than or equal to this value and resumed no earlier than this value after midnight. Clock updates are resumed in a controlled manner &#8211; after a control message, such as PTP announce. This ensures that the updated UTC offset is received before any further clock updates.</p>
<dt><code>default</code></p>
<dd><i>5</i> </p>
</dl>
</dl>
</dl>
</dl>
<dl>
<dd>
<dl>
<dt><code>clock:leap_second_notice_period [</code><i>INT</i><code>: 3600 .. 86400]</code></p>
<dd>
<dl>
<dd>
<dl>
<dt><code>usage</code></p>
<dd>Time (seconds) before midnight that PTPd starts announcing the leap second if it&#8217;s running as master. The IEEE 1588 standard suggests 12 hours notice and this is the default, but it may be changed to allow more flexibility.</p>
<dt><code>default</code></p>
<dd><i>43200</i> </p>
</dl>
</dl>
</dl>
</dl>
<dl>
<dd>
<dl>
<dt><code>clock:leap_second_handling [</code><i>SELECT</i><code>]</code></p>
<dd>
<dl>
<dd>
<dl>
<dt><code>options</code></p>
<dd><i>accept ignore step smear</i></p>
<dt><code>usage</code></p>
<dd>Clock sync behaviour during leap second events:</p>
<dl>
<dd>
<dl>
<dt><i>accept</i></p>
<dd>Inform OS kernel about the leap second and let the kernel insert or delete the leap second</p>
<dt><i>ignore</i></p>
<dd>Do not inform the kernel &#8211; this ends with a +/-1-second offset which is then slewed back down</p>
<dt><i>step</i></p>
<dd>Do not inform the kernel and step the clock immediately after the leap second event</p>
<dt><i>smear</i></p>
<dd>Gradually introduce an extra offset over a period of time before the leap second event, which accumulates to +/-1 second (see <i>clock:leap_second_smear_period</i>). Once the clock stabilises, this results in a clock frequency shift which is taken off after the event. Once the leap second event is over, the extra offset is also removed and time is back in line with master time.</dl>
</dl>
<dt><code>default</code></p>
<dd><i>accept</i> </p>
</dl>
</dl>
</dl>
</dl>
<dl>
<dd>
<dl>
<dt><code>clock:leap_second_smear_period [</code><i>INT</i><code>: 3600 .. 86400]</code></p>
<dd>
<dl>
<dd>
<dl>
<dt><code>usage</code></p>
<dd>When <i>clock:leap_second_handling</i> is set to <i>smear</i>, this setting defines the period (in seconds) before the leap second event, over which the leap second offset is gradually added. Example: when set to 24 hours (86400), an extra +/-11.5 microseconds is added every second (11.5 ppm clock frequency offset).</p>
<dt><code>default</code></p>
<dd><i>86400</i> </p>
</dl>
</dl>
</dl>
</dl>
<dl>
<dd>
<dl>
<dt><code>clock:max_offset_ppm [</code><i>INT</i><code>: 500 .. 1000]</code></p>
<dd>
<dl>
<dd>
<dl>
<dt><code>usage</code></p>
<dd>Maximum absolute frequency shift which can be applied to the clock servo <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt> when slewing the clock. Expressed in parts per million (1 ppm = shift of<br />
 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt> 1 us per second. Values above 512 will use the tick duration correction<br />
 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt> to allow even faster slewing. Default maximum is 512 without using tick.</p>
<dt><code>default</code></p>
<dd><i>500</i> </p>
</dl>
</dl>
</dl>
</dl>
<dl>
<dd>
<dl>
<dt><code>servo:delayfilter_stiffness [</code><i>INT</i><code>]</code></p>
<dd>
<dl>
<dd>
<dl>
<dt><code>usage</code></p>
<dd>Mean Path Delay filter stiffness.</p>
<dt><code>default</code></p>
<dd><i>6</i> </p>
</dl>
</dl>
</dl>
</dl>
<dl>
<dd>
<dl>
<dt><code>servo:kp [</code><i>FLOAT</i><code>: min: 0.000001 ]</code></p>
<dd>
<dl>
<dd>
<dl>
<dt><code>usage</code></p>
<dd>Clock servo PI controller proportional component gain (kP).</p>
<dt><code>default</code></p>
<dd><i>0.100000</i> </p>
</dl>
</dl>
</dl>
</dl>
<dl>
<dd>
<dl>
<dt><code>servo:ki [</code><i>FLOAT</i><code>: min: 0.000001 ]</code></p>
<dd>
<dl>
<dd>
<dl>
<dt><code>usage</code></p>
<dd>Clock servo PI controller integral component gain (kI).</p>
<dt><code>default</code></p>
<dd><i>0.001000</i> </p>
</dl>
</dl>
</dl>
</dl>
<dl>
<dd>
<dl>
<dt><code>servo:dt_method [</code><i>SELECT</i><code>]</code></p>
<dd>
<dl>
<dd>
<dl>
<dt><code>options</code></p>
<dd><i>none constant measured </i></p>
<dt><code>usage</code></p>
<dd>How servo update interval (delta t) is calculated:</p>
<dl>
<dd>
<dl>
<dt><i>none</i></p>
<dd>servo not corrected for update interval (dt always 1),</p>
<dt><i>constant</i></p>
<dd>constant value (target servo update rate) &#8211; sync interval for PTP,</p>
<dt><i>measured</i></p>
<dd>servo measures how often it&#8217;s updated and uses this interval.</dl>
</dl>
<dt><code>default</code></p>
<dd><i>constant</i> </p>
</dl>
</dl>
</dl>
</dl>
<dl>
<dd>
<dl>
<dt><code>servo:dt_max [</code><i>FLOAT</i><code>: 1.500000 .. 100.000000]</code></p>
<dd>
<dl>
<dd>
<dl>
<dt><code>usage</code></p>
<dd>Maximum servo update interval (delta t) when using measured servo update interval (<i>servo:dt_method</i> = <code>measured</code>), specified as sync interval multiplier</p>
<dt><code>default</code></p>
<dd><i>5.000000</i> </p>
</dl>
</dl>
</dl>
</dl>
<dl>
<dd>
<dl>
<dt><code>servo:stability_detection [</code><i>BOOLEAN</i><code>]</code></p>
<dd>
<dl>
<dd>
<dl>
<dt><code>usage</code></p>
<dd>Enable clock synchronisation servo stability detection (based on standard deviation of the observed drift value) &#8211; drift will be saved to drift file / cached when considered stable, also clock stability status will be logged.</p>
<dt><code>default</code></p>
<dd><i>N</i> </p>
</dl>
</dl>
</dl>
</dl>
<dl>
<dd>
<dl>
<dt><code>servo:stability_threshold [</code><i>FLOAT</i><code>: 1.000000 .. 10000.000000]</code></p>
<dd>
<dl>
<dd>
<dl>
<dt><code>usage</code></p>
<dd>Specify the observed drift standard deviation threshold in parts per billion (ppb) &#8211; if stanard deviation is within the threshold, servo is considered stable.</p>
<dt><code>default</code></p>
<dd><i>5.000000</i> </p>
</dl>
</dl>
</dl>
</dl>
<dl>
<dd>
<dl>
<dt><code>servo:stability_period [</code><i>INT</i><code>: 1 .. 100]</code></p>
<dd>
<dl>
<dd>
<dl>
<dt><code>usage</code></p>
<dd>Specify for how many statistics update intervals the observed drift standard deviation has to stay within threshold to be considered stable.</p>
<dt><code>default</code></p>
<dd><i>3</i> </p>
</dl>
</dl>
</dl>
</dl>
<dl>
<dd>
<dl>
<dt><code>servo:stability_timeout [</code><i>INT</i><code>: 1 .. 60]</code></p>
<dd>
<dl>
<dd>
<dl>
<dt><code>usage</code></p>
<dd>Specify after how many minutes without stabilisation servo is considered unstable. Assists with logging servo stability information and allows to preserve observed drift if servo cannot stabilise.</p>
<dt><code>default</code></p>
<dd><i>10</i> </p>
</dl>
</dl>
</dl>
</dl>
<dl>
<dd>
<dl>
<dt><code>servo:max_delay [</code><i>INT</i><code>: 0 .. 999999999]</code></p>
<dd>
<dl>
<dd>
<dl>
<dt><code>usage</code></p>
<dd>Do not accept master to slave delay (delayMS &#8211; from Sync message) or slave to master delay (delaySM &#8211; from Delay Response message) if greater than this value (nanoseconds). 0 = not used.</p>
<dt><code>default</code></p>
<dd><i>0</i> </p>
</dl>
</dl>
</dl>
</dl>
<dl>
<dd>
<dl>
<dt><code>servo:max_delay_max_rejected [</code><i>INT</i><code>: min: 0 ]</code></p>
<dd>
<dl>
<dd>
<dl>
<dt><code>usage</code></p>
<dd>Maximum number of consecutive rejected delay measurements exceeding the maxDelay threshold (<i>servo:max_delay</i>), before slave is reset. 0 = not checked.</p>
<dt><code>default</code></p>
<dd><i>0</i> </p>
</dl>
</dl>
</dl>
</dl>
<dl>
<dd>
<dl>
<dt><code>servo:max_delay_stable_only [</code><i>BOOLEAN</i><code>]</code></p>
<dd>
<dl>
<dd>
<dl>
<dt><code>usage</code></p>
<dd>If <code>servo:max_delay</code> is set, perform the check only if clock servo has stabilised.</p>
<dt><code>default</code></p>
<dd><i>N</i> </p>
</dl>
</dl>
</dl>
</dl>
<dl>
<dd>
<dl>
<dt><code>servo:max_offset [</code><i>INT</i><code>: 0 .. 999999999]</code></p>
<dd>
<dl>
<dd>
<dl>
<dt><code>usage</code></p>
<dd>Do not reset the clock if offset from master is greater than this value (nanoseconds). 0 = not used.</p>
<dt><code>default</code></p>
<dd><i>0</i> </p>
</dl>
</dl>
</dl>
</dl>
<dl>
<dd>
<dl>
<dt><code>global:enable_snmp [</code><i>BOOLEAN</i><code>]</code></p>
<dd>
<dl>
<dd>
<dl>
<dt><code>usage</code></p>
<dd>Enable SNMP agent (if compiled with PTPD_SNMP).</p>
<dt><code>default</code></p>
<dd><i>N</i> </p>
</dl>
</dl>
</dl>
</dl>
<dl>
<dd>
<dl>
<dt><code>global:use_syslog [</code><i>BOOLEAN</i><code>]</code></p>
<dd>
<dl>
<dd>
<dl>
<dt><code>usage</code></p>
<dd>Send log messages to syslog. Disabling this sends all messages to stdout (or speficied log file).</p>
<dt><code>default</code></p>
<dd><i>N</i> </p>
</dl>
</dl>
</dl>
</dl>
<dl>
<dd>
<dl>
<dt><code>global:lock_file [</code><i>STRING</i><code>]</code></p>
<dd>
<dl>
<dd>
<dl>
<dt><code>usage</code></p>
<dd>Lock file location</p>
<dt><code>default</code></p>
<dd><i>[none]</i> </p>
</dl>
</dl>
</dl>
</dl>
<dl>
<dd>
<dl>
<dt><code>global:auto_lockfile [</code><i>BOOLEAN</i><code>]</code></p>
<dd>
<dl>
<dd>
<dl>
<dt><code>usage</code></p>
<dd>Use mode specific and interface specific lock file (overrides <code>global:lock_file</code>).</p>
<dt><code>default</code></p>
<dd><i>N</i> </p>
</dl>
</dl>
</dl>
</dl>
<dl>
<dd>
<dl>
<dt><code>global:lock_directory [</code><i>STRING</i><code>]</code></p>
<dd>
<dl>
<dd>
<dl>
<dt><code>usage</code></p>
<dd>Lock file directory: used with automatic mode-specific lock files, also used when no lock file is specified. When lock file is specified, it&#8217;s expected to be an absolute path.</p>
<dt><code>default</code></p>
<dd><i>/var/run</i> </p>
</dl>
</dl>
</dl>
</dl>
<dl>
<dd>
<dl>
<dt><code>global:ignore_lock [</code><i>BOOLEAN</i><code>]</code></p>
<dd>
<dl>
<dd>
<dl>
<dt><code>usage</code></p>
<dd>Skip lock file checking and locking.</p>
<dt><code>default</code></p>
<dd><i>N</i> </p>
</dl>
</dl>
</dl>
</dl>
<dl>
<dd>
<dl>
<dt><code>global:quality_file [</code><i>STRING</i><code>]</code></p>
<dd>
<dl>
<dd>
<dl>
<dt><code>usage</code></p>
<dd>File used to record data about sync packets. Enables recording when set.</p>
<dt><code>default</code></p>
<dd><i>[none]</i> </p>
</dl>
</dl>
</dl>
</dl>
<dl>
<dd>
<dl>
<dt><code>global:quality_file_max_size [</code><i>INT</i><code>: min: 0 ]</code></p>
<dd>
<dl>
<dd>
<dl>
<dt><code>usage</code></p>
<dd>Maximum sync packet record file size (in kB) &#8211; file will be truncated if size exceeds the limit. 0 &#8211; no limit.</p>
<dt><code>default</code></p>
<dd><i>0</i> </p>
</dl>
</dl>
</dl>
</dl>
<dl>
<dd>
<dl>
<dt><code>global:quality_file_max_files [</code><i>INT</i><code>: 0 .. 100]</code></p>
<dd>
<dl>
<dd>
<dl>
<dt><code>usage</code></p>
<dd>Enable log rotation of the sync packet record file up to n files. 0 &#8211; do not rotate.</p>
<dt><code>default</code></p>
<dd><i>0</i> </p>
</dl>
</dl>
</dl>
</dl>
<dl>
<dd>
<dl>
<dt><code>global:quality_file_truncate [</code><i>BOOLEAN</i><code>]</code></p>
<dd>
<dl>
<dd>
<dl>
<dt><code>usage</code></p>
<dd>Truncate the sync packet record file every time it is (re) opened: startup and SIGHUP.</p>
<dt><code>default</code></p>
<dd><i>N</i> </p>
</dl>
</dl>
</dl>
</dl>
<dl>
<dd>
<dl>
<dt><code>global:status_file [</code><i>STRING</i><code>]</code></p>
<dd>
<dl>
<dd>
<dl>
<dt><code>usage</code></p>
<dd>File used to log ptpd2 status information.</p>
<dt><code>default</code></p>
<dd><i>/var/run/ptpd2.status</i> </p>
</dl>
</dl>
</dl>
</dl>
<dl>
<dd>
<dl>
<dt><code>global:log_status [</code><i>BOOLEAN</i><code>]</code></p>
<dd>
<dl>
<dd>
<dl>
<dt><code>usage</code></p>
<dd>Enable / disable writing status information to file.</p>
<dt><code>default</code></p>
<dd><i>N</i> </p>
</dl>
</dl>
</dl>
</dl>
<dl>
<dd>
<dl>
<dt><code>global:status_update_interval [</code><i>INT</i><code>: 1 .. 30]</code></p>
<dd>
<dl>
<dd>
<dl>
<dt><code>usage</code></p>
<dd>Status file update interval in seconds.</p>
<dt><code>default</code></p>
<dd><i>1</i> </p>
</dl>
</dl>
</dl>
</dl>
<dl>
<dd>
<dl>
<dt><code>global:log_file [</code><i>STRING</i><code>]</code></p>
<dd>
<dl>
<dd>
<dl>
<dt><code>usage</code></p>
<dd>Specify log file path (event log). Setting this enables logging to file.</p>
<dt><code>default</code></p>
<dd><i>[none]</i> </p>
</dl>
</dl>
</dl>
</dl>
<dl>
<dd>
<dl>
<dt><code>global:log_file_max_size [</code><i>INT</i><code>: min: 0 ]</code></p>
<dd>
<dl>
<dd>
<dl>
<dt><code>usage</code></p>
<dd>Maximum log file size (in kB) &#8211; log file will be truncated if size exceeds the limit. 0 &#8211; no limit.</p>
<dt><code>default</code></p>
<dd><i>0</i> </p>
</dl>
</dl>
</dl>
</dl>
<dl>
<dd>
<dl>
<dt><code>global:log_file_max_files [</code><i>INT</i><code>: 0 .. 100]</code></p>
<dd>
<dl>
<dd>
<dl>
<dt><code>usage</code></p>
<dd>Enable log rotation of the sync packet record file up to n files. 0 &#8211; do not rotate. </p>
<dt><code>default</code></p>
<dd><i>0</i> </p>
</dl>
</dl>
</dl>
</dl>
<dl>
<dd>
<dl>
<dt><code>global:log_file_truncate [</code><i>BOOLEAN</i><code>]</code></p>
<dd>
<dl>
<dd>
<dl>
<dt><code>usage</code></p>
<dd>Truncate the log file every time it is (re) opened: startup and SIGHUP.</p>
<dt><code>default</code></p>
<dd><i>N</i> </p>
</dl>
</dl>
</dl>
</dl>
<dl>
<dd>
<dl>
<dt><code>global:log_level [</code><i>SELECT</i><code>]</code></p>
<dd>
<dl>
<dd>
<dl>
<dt><code>options</code></p>
<dd><i>LOG_ERR LOG_WARNING LOG_NOTICE LOG_INFO LOG_ALL </i></p>
<dt><code>usage</code></p>
<dd>Specify log level (only messages at this priority or higer will be logged). The minimal level is LOG_ERR. LOG_ALL enables debug output if compiled with RUNTIME_DEBUG.</p>
<dt><code>default</code></p>
<dd><i>LOG_ALL</i> </p>
</dl>
</dl>
</dl>
</dl>
<dl>
<dd>
<dl>
<dt><code>global:statistics_file [</code><i>STRING</i><code>]</code></p>
<dd>
<dl>
<dd>
<dl>
<dt><code>usage</code></p>
<dd>Specify statistics log file path. Setting this enables logging of statistics, but can be overriden with <code>global:log_statistics</code>.</p>
<dt><code>default</code></p>
<dd><i>[none]</i> </p>
</dl>
</dl>
</dl>
</dl>
<dl>
<dd>
<dl>
<dt><code>global:statistics_log_interval [</code><i>INT</i><code>: min: 0 ]</code></p>
<dd>
<dl>
<dd>
<dl>
<dt><code>usage</code></p>
<dd>Log timing statistics every n seconds for Sync and Delay messages (0 &#8211; log all).</p>
<dt><code>default</code></p>
<dd><i>0</i> </p>
</dl>
</dl>
</dl>
</dl>
<dl>
<dd>
<dl>
<dt><code>global:statistics_file_max_size [</code><i>INT</i><code>: min: 0 ]</code></p>
<dd>
<dl>
<dd>
<dl>
<dt><code>usage</code></p>
<dd>Maximum statistics log file size (in kB) &#8211; log file will be truncated if size exceeds the limit. 0 &#8211; no limit.</p>
<dt><code>default</code></p>
<dd><i>0</i> </p>
</dl>
</dl>
</dl>
</dl>
<dl>
<dd>
<dl>
<dt><code>global:statistics_file_max_files [</code><i>INT</i><code>: 0 .. 100]</code></p>
<dd>
<dl>
<dd>
<dl>
<dt><code>usage</code></p>
<dd>Enable log rotation of the statistics file up to n files. 0 &#8211; do not rotate.</p>
<dt><code>default</code></p>
<dd><i>0</i> </p>
</dl>
</dl>
</dl>
</dl>
<dl>
<dd>
<dl>
<dt><code>global:statistics_file_truncate [</code><i>BOOLEAN</i><code>]</code></p>
<dd>
<dl>
<dd>
<dl>
<dt><code>usage</code></p>
<dd>Truncate the statistics file every time it is (re) opened: startup and SIGHUP.</p>
<dt><code>default</code></p>
<dd><i>N</i> </p>
</dl>
</dl>
</dl>
</dl>
<dl>
<dd>
<dl>
<dt><code>global:dump_packets [</code><i>BOOLEAN</i><code>]</code></p>
<dd>
<dl>
<dd>
<dl>
<dt><code>usage</code></p>
<dd>Dump the contents of every PTP packet.</p>
<dt><code>default</code></p>
<dd><i>N</i> </p>
</dl>
</dl>
</dl>
</dl>
<dl>
<dd>
<dl>
<dt><code>global:verbose_foreground [</code><i>BOOLEAN</i><code>]</code></p>
<dd>
<dl>
<dd>
<dl>
<dt><code>usage</code></p>
<dd>Run in foreground with statistics and all messages logged to stdout. Overrides log file and statistics file settings and disables syslog. </p>
<dt><code>default</code></p>
<dd><i>N</i> </p>
</dl>
</dl>
</dl>
</dl>
<dl>
<dd>
<dl>
<dt><code>global:foreground [</code><i>BOOLEAN</i><code>]</code></p>
<dd>
<dl>
<dd>
<dl>
<dt><code>usage</code></p>
<dd>Run in foreground &#8211; ignored when global:verbose_foreground is set.</p>
<dt><code>default</code></p>
<dd><i>N</i> </p>
</dl>
</dl>
</dl>
</dl>
<dl>
<dd>
<dl>
<dt><code>global:log_statistics [</code><i>BOOLEAN</i><code>]</code></p>
<dd>
<dl>
<dd>
<dl>
<dt><code>usage</code></p>
<dd>Log timing statistics for every PTP packet received. Output is in CSV format and field headers are always printed when starting or refreshing the statistics log.</p>
<dt><code>default</code></p>
<dd><i>N</i> </p>
</dl>
</dl>
</dl>
</dl>
<dl>
<dd>
<dl>
<dt><code>global:statistics_timestamp_format [</code><i>SELECT</i><code>]</code></p>
<dd>
<dl>
<dd>
<dl>
<dt><code>options</code></p>
<dd><i>datetime unix both </i></p>
<dt><code>usage</code></p>
<dd>Timestamp format used when logging timing statistics (when <code>global:log_statistics</code> is enabled):</p>
<dl>
<dd>
<dl>
<dt><i>datetime</i></p>
<dd>Formatted date and time: <code>YYYY-MM-DD hh:mm:ss.uuuuuu</code></p>
<dt><i>unix</i></p>
<dd>Unix timestamp with nanoseconds: <code>s.ns</code></p>
<dt><i>both</i></p>
<dd>Formatted date and time followed by unix timestamp (adds one extra field to the log)</dl>
</dl>
<dt><code>default</code></p>
<dd><i>datetime</i> </p>
</dl>
</dl>
</dl>
</dl>
<dl>
<dd>
<dl>
<dt><code>global:periodic_updates [</code><i>BOOLEAN</i><code>]</code></p>
<dd>
<dl>
<dd>
<dl>
<dt><code>usage</code></p>
<dd>Log a status update every time statistics are updated (<i>global:statistics_update_interval</i>). This update is written to the main log target. Status updates are logged even if ptpd is configured without support for statistics.</p>
<dt><code>default</code></p>
<dd><i>N</i> </p>
</dl>
</dl>
</dl>
</dl>
<dl>
<dd>
<dl>
<dt><code>global:cpuaffinity_cpucore [</code><i>INT</i><code>: -1 .. 255]</code></p>
<dd>
<dl>
<dd>
<dl>
<dt><code>usage</code></p>
<dd>Bind ptpd2 process to a selected CPU core number. 0 = first CPU core, etc. -1 = do not bind to a single core.</p>
<dt><code>default</code></p>
<dd><i>0</i> </p>
</dl>
</dl>
</dl>
</dl>
<dl>
<dd>
<dl>
<dt><code>global:statistics_update_interval [</code><i>INT</i><code>: 1 .. 60]</code></p>
<dd>
<dl>
<dd>
<dl>
<dt><code>usage</code></p>
<dd>Clock synchronisation statistics update interval in seconds. Also controls how often periodic status information is logged (when using <i>global:statistics_update_interval</i>).</p>
<dt><code>default</code></p>
<dd><i>30</i> </p>
</dl>
</dl>
</dl>
</dl>
<dl>
<dd>
<dl>
<dt><code>global:timingdomain_election_delay [</code><i>INT</i><code>: 0 .. 3600 ]</code></p>
<dd>
<dl>
<dd>
<dl>
<dt><code>usage</code></p>
<dd>Delay (seconds) before releasing a time service (NTP or PTP) and electing a new one to control a clock. 0 = elect immediately</p>
<dt><code>default</code></p>
<dd><i>15</i> </p>
</dl>
</dl>
</dl>
</dl>
<dl>
<dd>
<dl>
<dt><code>ntpengine:enabled [</code><i>BOOLEAN</i><code>]</code></p>
<dd>
<dl>
<dd>
<dl>
<dt><code>usage</code></p>
<dd>Enable NTPd integration</p>
<dt><code>default</code></p>
<dd><i>N</i> </p>
</dl>
</dl>
</dl>
</dl>
<dl>
<dd>
<dl>
<dt><code>ntpengine:control_enabled [</code><i>BOOLEAN</i><code>]</code></p>
<dd>
<dl>
<dd>
<dl>
<dt><code>usage</code></p>
<dd>Enable control over local NTPd daemon</p>
<dt><code>default</code></p>
<dd><i>N</i> </p>
</dl>
</dl>
</dl>
</dl>
<dl>
<dd>
<dl>
<dt><code>ntpengine:check_interval [</code><i>INT</i><code>: 5 .. 600]</code></p>
<dd>
<dl>
<dd>
<dl>
<dt><code>usage</code></p>
<dd>NTP control check interval in seconds</p>
<dt><code>default</code></p>
<dd><i>15</i> </p>
</dl>
</dl>
</dl>
</dl>
<dl>
<dd>
<dl>
<dt><code>ntpengine:key_id [</code><i>INT</i><code>: 0 .. 65535]</code></p>
<dd>
<dl>
<dd>
<dl>
<dt><code>usage</code></p>
<dd>NTP key number &#8211; must be configured as a trusted control key in ntp.conf, and be non-zero for the ntpengine:control_enabled setting to take effect.</p>
<dt><code>default</code></p>
<dd><i>0</i> </p>
</dl>
</dl>
</dl>
</dl>
<dl>
<dd>
<dl>
<dt><code>ntpengine:key [</code><i>STRING</i><code>]</code></p>
<dd>
<dl>
<dd>
<dl>
<dt><code>usage</code></p>
<dd>NTP key (plain text, max. 20 characters) &#8211; must match the key configured in ntpd&#8217;s keys file, and must be non-zero for the ntpengine:control_enabled setting to take effect.</p>
<dt><code>default</code></p>
<dd><i>[none]</i> </p>
</dl>
</dl>
</dl>
</dl>
</dl>
<h2>Bugs</h2>
<p>Configuration file support has only been introduced in version 2.3. There may still be some inconsistencies in the way some settings are parsed and while order should not make any difference, for some complex behaviours it may still be the case. Please report any bugs using the bug tracker on the SourceForge page: <a rel="nofollow" href="http://sourceforge.net/projects/ptpd/">http://sourceforge.net/projects/ptpd/</a> </p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/8-ptpd2/">ptpd2</a>(8) </p>
<h2>Authors</h2>
<p>Steven Kreuzer &lt;skreuzer [at] freebsd.org&gt; </p>
<p> Gael Mace &lt;gael_mace [at] users.sourceforge.net&gt; </p>
<p> George Neville-Neil &lt;gnn [at] freebsd.org&gt; </p>
<p> Wojciech Owczarek &lt;wojciech [at] owczarek.co.uk&gt; </p>
<p> Alexandre Van Kempen </p>
<p> <code><a href="/docs/linux/man/5-ptpd2-conf/">ptpd2.conf</a>(5)</code> man page first written by Wojciech Owczarek for ptpd 2.3.0 in November 2013</p>
