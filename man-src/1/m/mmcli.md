---
title: "mmcli(1)"
name: "mmcli"
section: "1"
letter: "m"
url: "/docs/linux/man/1-mmcli/"
description: "mmcli – Control and monitor the ModemManager"
---

<h2 class="name">NAME</h2>
<p> mmcli &#8211; Control and monitor the ModemManager</p>
<h2>SYNOPSIS</h2>
<p> <code>mmcli</code> [<i>OPTION</i>&#8230;] </p>
<h2>DESCRIPTION</h2>
<p> ModemManager is a DBus-powered Linux daemon which provides a unified high level API for communicating with (mobile broadband) modems. It acts as a standard RIL (Radio Interface Layer) and may be used by different connection managers, like NetworkManager. Thanks to the built-in plugin architecture, ModemManager talks to very different kinds of modems with very different kinds of ports. In addition to the standard AT serial ports, Qualcomm-based QCDM and QMI ports are also supported. </p>
<h2>HELP OPTIONS</h2>
<dl>
<dt><code>-h, &#8211;help</code></p>
<dd> Show summary of options by group.</p>
<dt><code>&#8211;help-all</code></p>
<dd> Show all groups and options.</p>
<dt><code>&#8211;help-manager</code></p>
<dd> Show manager specific options.</p>
<dt><code>&#8211;help-common</code></p>
<dd> Show common options. These are used for defining the device an option operates on. For example, modems, bearers, SIMs, SMS&#8217;, etc.</p>
<dt><code>&#8211;help-modem</code></p>
<dd> Show modem specific options.</p>
<dt><code>&#8211;help-3gpp</code></p>
<dd> Show 3GPP specific options.</p>
<dt><code>&#8211;help-cdma</code></p>
<dd> Show CDMA specific options.</p>
<dt><code>&#8211;help-simple</code></p>
<dd> Show simple options. These are useful for getting connected or disconnected and understanding the state of things as fast as possible without worrying so much about the details.</p>
<dt><code>&#8211;help-location</code></p>
<dd> Show location or positioning specific options.</p>
<dt><code>&#8211;help-messaging</code></p>
<dd> Show messaging specific options. See also <code>&#8211;help-sms</code> which is related.</p>
<dt><code>&#8211;help-time</code></p>
<dd> Show time specific options.</p>
<dt><code>&#8211;help-firmware</code></p>
<dd> Show firmware specific options.</p>
<dt><code>&#8211;help-oma</code></p>
<dd> Show OMA specific options.</p>
<dt><code>&#8211;help-sim</code></p>
<dd> Show SIM card specific options.</p>
<dt><code>&#8211;help-bearer</code></p>
<dd> Show bearer specific options.</p>
<dt><code>&#8211;help-sms</code></p>
<dd> Show SMS specific options. See also <code>&#8211;help-messaging</code> which is related. </p>
</dl>
<h2>MANAGER OPTIONS</h2>
<dl>
<dt><code>-B, &#8211;get-daemon-version</code></p>
<dd> Retrieve the version of the currently running ModemManager daemon.</p>
<dt><code>-G, &#8211;set-logging=[ERR|WARN|INFO|DEBUG]</code></p>
<dd> Set the logging level in ModemManager daemon. For debugging information you can supply <code>DEBUG</code>. Each value above <code>DEBUG</code> provides less detail. In most cases <code>ERR</code> (for displaying errors) are the important messages. </p>
<p> The default mode is <code>ERR</code>.</p>
<dt><code>-L, &#8211;list-modems</code></p>
<dd> List available modems.</p>
<dt><code>-M, &#8211;monitor-modems</code></p>
<dd> List available modems and monitor modems added or removed.</p>
<dt><code>-S, &#8211;scan-modems</code></p>
<dd> Scan for any potential new modems. This is only useful when expecting pure RS232 modems, as they are not notified automatically by the kernel.</p>
<dt><code>-I, &#8211;inhibit-device=[UID]</code></p>
<dd> Inhibit the specific device from being used by ModemManager. The <code>UID</code> that should be given is the value of the <code>Device</code> property exposed by a given modem (i.e. equal to the <code>ID_MM_PHYSDEV_UID</code> if one set, or otherwise equal to the full device sysfs path). </p>
<p> This command will not exit right away, as that would implicitly remove the inhibition. The user must make sure to stop the mmcli process hitting Ctrl+C in order to un-inhibit the device. </p>
<p> When a device is inhibited via this method, ModemManager will disable the modem (therefore stopping any ongoing connection) and will no longer use it until it is uninhibited.</p>
<dt><code>&#8211;report-kernel-event=[&#8216;KEY1=VALUE1,KEY2=VALUE2,&#8230;&#8217;]</code></p>
<dd> Manually report kernel events, instead of relying on udev (e.g. if the daemon is running with <code>&#8211;no-auto-scan</code> or if the system was built without udev support). </p>
<p> The supported <code>KEY</code>s are:</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>&#8216;action&#8217;</code></p>
<dd> Action to report, one of &#8216;add&#8217; or &#8216;remove&#8217;. Required.</p>
<dt><code>&#8216;subsystem&#8217;</code></p>
<dd> Subsystem of the specific port being reported, e.g. &#8216;tty&#8217; (for serial ports),</p>
<dt><code>&#8216;name&#8217;</code></p>
<dd> Name of the port being reported, e.g. &#8216;ttyACM0&#8217;, &#8216;wwan0&#8217; or &#8216;cdc-wdm0&#8217;.</p>
<dt><code>&#8216;uid&#8217;</code></p>
<dd> The specific UID of the device, equivalent to the <code>ID_MM_PHYSDEV_UID</code> udev tag. All ports reported with the same &#8216;UID&#8217; value will be considered part of the same device, which may be useful for e.g. modems with multiple platform TTYs.</dl>
</dl>
<dt><code>&#8211;report-kernel-event-auto-scan</code></p>
<dd> When built with udev support but the daemon is running with <code>&#8211;no-auto-scan</code>, this method may be used to automatically report kernel events based on udev. </p>
<p> This command will not exit right away. The user must make sure to stop the mmcli process hitting Ctrl+C in order to stopping monitoring for new events. </p>
</dl>
<h2>COMMON OPTIONS</h2>
<p> All options below take a <code>PATH</code> or <code>INDEX</code> argument. If no action is provided, the default information about the modem, bearer, etc. is shown instead. </p>
<p> The <code>PATH</code> and <code>INDEX</code> are created automatically when the modem is plugged in. They can be found using <code>mmcli -L</code>. This produces something like (for modems only): </p>
<dl>
<dt>
<dd> Found 1 modems:<br />
&nbsp;<wbr>&nbsp;/org/freedesktop/ModemManager1/Modem/<code>4</code></dl>
<p> In this case, the <code>INDEX</code> is <code>4</code> and the <code>PATH</code> is the entire string above. </p>
<p> However, for the bearers, SIMs and SMS cases, the <code>PATH</code> is slightly different. The <i>Modem</i> is replaced with the object name in use, like <i>Bearer</i>. For example: </p>
<dl>
<dt>
<dd> /org/freedesktop/ModemManager1/<i>Bearer</i>/4</dl>
<dl>
<dt><code>-m, &#8211;modem=[PATH|INDEX]</code></p>
<dd> Specify a modem.</p>
<dt><code>-b, &#8211;bearer=[PATH|INDEX]</code></p>
<dd> Specify a bearer.</p>
<dt><code>-i, &#8211;sim=[PATH|INDEX]</code></p>
<dd> Specify a SIM card.</p>
<dt><code>-s, &#8211;sms=[PATH|INDEX]</code></p>
<dd> Specify an SMS. </p>
</dl>
<h2>MODEM OPTIONS</h2>
<p> All of the modem options below make use of the <code>&#8211;modem</code> or <code>-m</code> switch to specify the modem to act on. </p>
<p> Some operations require a <code>MODE</code>. <code>MODE</code> can be any combination of the modes actually supported by the modem. In the perfect case, the following are possible: </p>
<pre>
  <code>'2G'</code>  - 2G technologies, e.g. EDGE, CDMA1x
  <code>'3G'</code>  - 3G technologies, e.g. HSPA, EV-DO
  <code>'4G'</code>  - 4G technologies, e.g. LTE
  <code>'ANY'</code> - for all supported modes.
</pre>
<dl>
<dt><code>-w, &#8211;monitor-state</code></p>
<dd> Monitor the state of a given modem.</p>
<dt><code>-e, &#8211;enable</code></p>
<dd> Enable a given modem. </p>
<p> This powers the antenna, starts the automatic registration process and in general prepares the modem to be connected.</p>
<dt><code>-d, &#8211;disable</code></p>
<dd> Disable a given modem. </p>
<p> This disconnects the existing connection(s) for the modem and puts it into a low power mode.</p>
<dt><code>-r, &#8211;reset</code></p>
<dd> Resets the modem to the settings it had when it was power cycled.</p>
<dt><code>&#8211;factory-reset=CODE</code></p>
<dd> Resets the modem to its original factory default settings. </p>
<p> The <code>CODE</code> provided is vendor specific. Without the correct vendor code, it&#8217;s unlikely this operation will succeed. This is not a common user action.</p>
<dt><code>&#8211;command=COMMAND</code></p>
<dd> Send an AT <code>COMMAND</code> to the given modem. For example, <code>COMMAND</code> could be &#8216;AT+GMM&#8217; to probe for phone model information. This operation is only available when ModemManager is run in debug mode.</p>
<dt><code>&#8211;create-bearer=[&#8216;KEY1=VALUE1,KEY2=VALUE2,&#8230;&#8217;]</code></p>
<dd> Create a new packet data bearer for a given modem. The <code>KEY</code>s and some <code>VALUE</code>s are listed below:</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>&#8216;apn&#8217;</code></p>
<dd> Access Point Name. Required in 3GPP.</p>
<dt><code>&#8216;ip-type&#8217;</code></p>
<dd> Addressing type. Given as a MMBearerIpFamily value (e.g. &#8216;ipv4&#8217;, &#8216;ipv6&#8217;, &#8216;ipv4v6&#8217;). Optional in 3GPP and CDMA.</p>
<dt><code>&#8216;allowed-auth&#8217;</code></p>
<dd> Authentication method to use. Given as a MMBearerAllowedAuth value (e.g. &#8216;none|pap|chap|mschap|mschapv2|eap&#8217;). Optional in 3GPP.</p>
<dt><code>&#8216;user&#8217;</code></p>
<dd> User name (if any) required by the network. Optional in 3GPP.</p>
<dt><code>&#8216;password&#8217;</code></p>
<dd> Password (if any) required by the network. Optional in 3GPP.</p>
<dt><code>&#8216;allow-roaming&#8217;</code></p>
<dd> Flag to tell whether connection is allowed during roaming, given as a boolean value (i.e &#8216;yes&#8217; or &#8216;no&#8217;). Optional in 3GPP.</p>
<dt><code>&#8216;rm-protocol&#8217;</code></p>
<dd> Protocol of the Rm interface, given as a MMModemCdmaRmProtocol value (e.g. &#8216;async&#8217;, &#8216;packet-relay&#8217;, &#8216;packet-network-ppp&#8217;, &#8216;packet-network-slip&#8217;, &#8216;stu-iii&#8217;). Optional in CDMA.</p>
<dt><code>&#8216;number&#8217;</code></p>
<dd> Telephone number to dial. Required in POTS.</dl>
</dl>
<dt><code>&#8211;delete-bearer=[PATH|INDEX]</code></p>
<dd> Delete bearer from a given modem.</p>
<dt><code>&#8211;set-allowed-modes=[MODE1|MODE2|&#8230;]</code></p>
<dd> Set allowed modes for a given modem. For possible modes, see the beginning of this section.</p>
<dt><code>&#8211;set-preferred-mode=MODE</code></p>
<dd> Set the preferred <code>MODE</code> for the given modem. The <code>MODE</code> <i>MUST</i> be one of the allowed modes as set with the <code>&#8211;set-allowed-modes</code> option. Possible <code>MODE</code> arguments are detailed at the beginning of this section.</p>
<dt><code>&#8211;set-current-bands=[BAND1|BAND2|&#8230;]</code></p>
<dd> Set bands to be used for a given modem. These are frequency ranges the modem should use. There are quite a number of supported bands and listing them all here would be quite extensive. For details, see the MMModemBand documentation. </p>
<p> An example would be: &#8216;egsm|dcs|pcs|g850&#8217; to select all the GSM frequency bands.</p>
<dt><code>&#8211;set-primary-sim-slot=[SLOT]</code></p>
<dd> Request to switch the primary SIM slot. </p>
<p> The given <code>SLOT</code> must be a valid slot number in the [1,N] range, where N is the amount of SIM slots available in the system.</p>
<dt><code>&#8211;inhibit</code></p>
<dd> Inhibit the specific modem from being used by ModemManager. This method is completely equivalent to <code>&#8211;inhibit-device</code>, with the only difference being that in this case, the modem must be managed by the daemon at the time the inhibition is requested. </p>
<p> This command will not exit right away, as that would implicitly remove the inhibition. The user must make sure to stop the mmcli process hitting Ctrl+C in order to un-inhibit the device. </p>
<p> When a device is inhibited via this method, ModemManager will disable the modem (therefore stopping any ongoing connection) and will no longer use it until it is uninhibited. </p>
</dl>
<h2>3GPP OPTIONS</h2>
<p> The 3rd Generation Partnership Project (3GPP) is a collaboration between groups of telecommunications associations. These options pertain to devices which support 3GPP. </p>
<p> Included are options to control USSD (Unstructured Supplementary Service Data) sessions. </p>
<p> All of the 3GPP options below make use of the <code>&#8211;modem</code> or <code>-m</code> switch to specify the modem to act on.</p>
<dl>
<dt><code>&#8211;3gpp-scan</code></p>
<dd> Scan for available 3GPP networks.</p>
<dt><code>&#8211;3gpp-register-home</code></p>
<dd> Request a given modem to register in its home network. </p>
<p> This registers with the default network(s) specified by the modem,</p>
<dt><code>&#8211;3gpp-register-in-operator=MCCMNC</code></p>
<dd> Request a given modem to register on the network of the given <code>MCCMNC</code> (Mobile Country Code, Mobile Network Code) based operator. This code is used for GSM/LTE, CDMA, iDEN, TETRA and UMTS public land mobile networks and some satellite mobile networks. The ITU-T Recommendation E.212 defines mobile country codes.</p>
<dt><code>&#8211;3gpp-ussd-status</code></p>
<dd> Request the status of <i>ANY</i> ongoing USSD session.</p>
<dt><code>&#8211;3gpp-ussd-initiate=COMMAND</code></p>
<dd> Request the given modem to initiate a USSD session with <code>COMMAND</code>. </p>
<p> For example, <code>COMMAND</code> could be &#8216;*101#&#8217; to give your current pre-pay balance.</p>
<dt><code>&#8211;3gpp-ussd-respond=RESPONSE</code></p>
<dd> When initiating an USSD session, a RESPONSE may be needed by a network-originated request. This option allows for that.</p>
<dt><code>&#8211;3gpp-ussd-cancel</code></p>
<dd> Cancel an ongoing USSD session for a given modem.</p>
<dt><code>&#8211;3gpp-disable-facility-lock=FACILITY,CONTROL_KEY</code></p>
<dd> Disable selected facility lock using provided control key.</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>&#8216;FACILITY&#8217;</code></p>
<dd> One of the following types of lock: </p>
<pre>
  <code>'net-pers'</code>  - network personalization
  <code>'net-sub-pers'</code>  - network subset personalization
  <code>'provider-pers'</code> - provider personalization
  <code>'corp-pers'</code> - corporate personalization
</pre>
<dt><code>&#8216;CONTROL_KEY&#8217;</code></p>
<dd> Alphanumeric code to unlock facility.</dl>
</dl>
</dl>
<h2>CDMA OPTIONS</h2>
<p> All CDMA (Code Division Multiple Access) options require the <code>&#8211;modem</code> or <code>-m</code> option. </p>
<dl>
<dt><code>&#8211;cdma-activate=CARRIER</code></p>
<dd> Activate the given modem using OTA (Over the Air) settings. The <code>CARRIER</code> is a code provided by the network for the default settings they provide. </p>
</dl>
<h2>SIMPLE OPTIONS</h2>
<p> All simple options must be used with <code>&#8211;modem</code> or <code>-m</code>. </p>
<dl>
<dt><code>&#8211;simple-connect=[&#8216;KEY1=VALUE1,KEY2=VALUE2,&#8230;&#8217;]</code></p>
<dd> Run a full connection sequence using <code>KEY</code> / <code>VALUE</code> pairs. You can use the <code>&#8211;create-bearer</code> options, plus any of the following ones:</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>&#8216;pin&#8217;</code></p>
<dd> SIM-PIN unlock code.</p>
<dt><code>&#8216;operator-id&#8217;</code></p>
<dd> ETSI MCC-MNC of a network to force registration.</dl>
</dl>
<dt><code>&#8211;simple-disconnect</code></p>
<dd> Disconnect <i>ALL</i> connected bearers for a given modem. </p>
</dl>
<h2>LOCATION OPTIONS</h2>
<p> These options detail how to discover your location using Global Positioning System (GPS) or directly from your mobile network infrastructure (either 3GPP or 3GPP2). </p>
<p> All location options must be used with <code>&#8211;modem</code> or <code>-m</code>. </p>
<dl>
<dt><code>&#8211;location-status</code></p>
<dd> Show the current status for discovering our location.</p>
<dt><code>&#8211;location-get</code></p>
<dd> Show all location information available.</p>
<dt><code>&#8211;location-enable-3gpp</code></p>
<dd> Enable location discovery using the 3GPP network.</p>
<dt><code>&#8211;location-disable-3gpp</code></p>
<dd> Disable location discovery using the 3GPP network.</p>
<dt><code>&#8211;location-enable-agps-msa</code></p>
<dd> Enable A-GPS (MSA) support. This command does not implicitly start the GPS engine, it just specifies that A-GPS should be enabled when the engine is started. Therefore, the user should request enabling A-GPS before the raw or NMEA outputs are enabled with <code>&#8211;location-enable-gps-raw</code> or <code>&#8211;location-enable-gps-nmea</code>.</p>
<dt><code>&#8211;location-disable-agps-msa</code></p>
<dd> Disable A-GPS (MSA) support.</p>
<dt><code>&#8211;location-enable-agps-msb</code></p>
<dd> Enable A-GPS (MSB) support. This command does not implicitly start the GPS engine, it just specifies that A-GPS should be enabled when the engine is started. Therefore, the user should request enabling A-GPS before the raw or NMEA outputs are enabled with <code>&#8211;location-enable-gps-raw</code> or <code>&#8211;location-enable-gps-nmea</code>.</p>
<dt><code>&#8211;location-disable-agps-msb</code></p>
<dd> Disable A-GPS (MSB) support.</p>
<dt><code>&#8211;location-enable-gps-nmea</code></p>
<dd> Enable location discovery using GPS and reported with NMEA traces. </p>
<p> This command will start the GPS engine, if it isn&#8217;t started already.</p>
<dt><code>&#8211;location-disable-gps-nmea</code></p>
<dd> Disable location discovery using GPS and NMEA traces. </p>
<p> If the raw output is not enabled at the same time, the GPS engine will be stopped.</p>
<dt><code>&#8211;location-enable-gps-raw</code></p>
<dd> Enable location discovery using GPS and reported with raw (i.e. longitude/latitude) values. </p>
<p> This command will start the GPS engine, if it isn&#8217;t started already.</p>
<dt><code>&#8211;location-disable-gps-raw</code></p>
<dd> Disable location discovery using GPS and raw values. </p>
<p> If the NMEA output is not enabled at the same time, the GPS engine will be stopped.</p>
<dt><code>&#8211;location-enable-cdma-bs</code></p>
<dd> Enable location discovery using the 3GPP2 network.</p>
<dt><code>&#8211;location-disable-cdma-bs</code></p>
<dd> Disable location discovery using the 3GPP2 network.</p>
<dt><code>&#8211;location-enable-gps-unmanaged</code></p>
<dd> Enable location discovery using GPS but without taking control of the NMEA tty port. This allows other programs, e.g. gpsd, to use the NMEA tty once the GPS engine has been enabled.</p>
<dt><code>&#8211;location-disable-gps-unmanaged</code></p>
<dd> Disable location discovery using GPS and unmanaged port.</p>
<dt><code>&#8211;location-set-gps-refresh-rate=SEC</code></p>
<dd> Set the location refresh rate on the DBus interface to SEC seconds. If set to 0, the new location is published on the DBus interface as soon as ModemManager detects it.</p>
<dt><code>&#8211;location-set-supl-server=[IP:PORT] or &#8211;location-set-supl-server=[FQDN:PORT]</code></p>
<dd> Configure the location of the A-GPS SUPL server, either specifying the IP address (<code>IP:PORT</code>) or specifyng a fully qualified domain name (<code>[FQDN:PORT]</code>).</p>
<dt><code>&#8211;location-inject-assistance-data=[PATH]</code></p>
<dd> Inject assistance data into the GNSS module, loaded from a local file at <code>PATH</code>. The assistance data should be in a format expected by the device, e.g. downloaded from the URLs exposed by the &#8216;AssistanceDataServers&#8217; property.</p>
<dt><code>&#8211;location-set-enable-signal</code></p>
<dd> Enable reporting location updates via DBus property signals. This is required if applications rely on listening to &#8216;Location&#8217; property updates, instead of explicit queries with the policy-protected &#8216;GetLocation&#8217; method. </p>
<p> This DBus property signal updates are by default disabled.</p>
<dt><code>&#8211;location-set-disable-signal</code></p>
<dd> Disable reporting location updates via DBus property signals. </p>
</dl>
<h2>MESSAGING OPTIONS</h2>
<p> All messaging options must be used with <code>&#8211;modem</code> or <code>-m</code>. </p>
<dl>
<dt><code>&#8211;messaging-status</code></p>
<dd> Show the status of the messaging support.</p>
<dt><code>&#8211;messaging-list-sms</code></p>
<dd> List SMS messages available on a given modem.</p>
<dt><code>&#8211;messaging-create-sms=[&#8216;KEY1=VALUE1,&#8230;&#8217;]</code></p>
<dd> Create a new SMS on a given modem. <code>KEY</code>s can be any of the following:</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>&#8216;number&#8217;</code></p>
<dd>
&nbsp;Number to which the message is addressed.</p>
<dt><code>&#8216;text&#8217;</code></p>
<dd> Message text, in UTF-8. When sending, if the text is larger than the limit of the technology or modem, the message will be broken into multiple parts or messages. Note that text and data are never given at the same time.</p>
<dt><code>&#8216;smsc&#8217;</code></p>
<dd> Indicates the SMS service center number.</p>
<dt><code>&#8216;validity&#8217;</code></p>
<dd> Specifies when the SMS expires in the SMSC.</p>
<dt><code>&#8216;class&#8217;</code></p>
<dd> 3GPP message class (0..3).</p>
<dt><code>&#8216;delivery-report-request&#8217;</code></p>
<dd> Specifies whether delivery report is requested when sending the SMS (&#8216;yes&#8217; or &#8216;no&#8217;)</p>
<dt><code>&#8216;storage&#8217;</code></p>
<dd> Specifies the storage where this message is kept. Storages may be &#8216;sm&#8217;, &#8216;me&#8217;, &#8216;mt&#8217;, &#8216;sr&#8217;, &#8216;bm&#8217;, &#8216;ta&#8217;.</dl>
</dl>
<dt><code>&#8211;messaging-create-sms-with-data=PATH</code></p>
<dd> Use <code>PATH</code> to a filename as the data to create a new SMS.</p>
<dt><code>&#8211;messaging-delete-sms=[PATH|INDEX]</code></p>
<dd> Delete an SMS from a given modem. </p>
</dl>
<h2>TIME OPTIONS</h2>
<p> All time operations require the <code>&#8211;modem</code> or <code>-m</code> option. </p>
<dl>
<dt><code>&#8211;time</code></p>
<dd> Display the current network time from the operator. This includes the timezone which is usually of importance. </p>
</dl>
<h2>VOICE OPTIONS</h2>
<p> All voice operations require the <code>&#8211;modem</code> or <code>-m</code> option. </p>
<dl>
<dt><code>&#8211;voice-list-calls</code></p>
<dd> List calls managed (initiated, received, ongoing) on a given modem.</p>
<dt><code>&#8211;voice-create-call=[&#8216;KEY1=VALUE1,&#8230;&#8217;]</code></p>
<dd> Create a new outgoing call on a given modem. <code>KEY</code>s can be any of the following:</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>&#8216;number&#8217;</code></p>
<dd> Number to call.</dl>
</dl>
<dt><code>&#8211;voice-delete-call=[PATH|INDEX]</code></p>
<dd> Delete a call from a given modem. </p>
</dl>
<h2>FIRMWARE OPTIONS</h2>
<p> All firmware options require the <code>&#8211;modem</code> or <code>-m</code> option. </p>
<dl>
<dt><code>&#8211;firmware-status</code></p>
<dd> Show firmware update specific details and properties.</p>
<dt><code>&#8211;firmware-list</code></p>
<dd> List all the firmware images installed on a given modem.</p>
<dt><code>&#8211;firmware-select=ID</code></p>
<dd> Select a firmware image from those installed on a given modem. A list of available firmware images can be seen using the <code>&#8211;firmware-list</code> option. </p>
<p> The <code>ID</code> provided is a <i>UNIQUE</i> identifier for the firmware. </p>
</dl>
<h2>SIGNAL OPTIONS</h2>
<p> All signal options require the <code>&#8211;modem</code> or <code>-m</code> option. </p>
<dl>
<dt><code>&#8211;signal-setup=[Rate]</code></p>
<dd> Setup extended signal quality information retrieval at the specified rate (in seconds). </p>
<p> By default this is disabled (rate set to 0).</p>
<dt><code>&#8211;signal-get</code></p>
<dd> Retrieve the last extended signal quality information loaded. </p>
</dl>
<h2>OMA OPTIONS</h2>
<p> All OMA options require the <code>&#8211;modem</code> or <code>-m</code> option. </p>
<dl>
<dt><code>&#8211;oma-status</code></p>
<dd> Show the status of the OMA device management subsystem.</p>
<dt><code>&#8211;oma-start-client-initiated-session=[SESSION TYPE]</code></p>
<dd> Request to start a client initiated session. </p>
<p> The given session type must be one of:<br />
&nbsp;&#8216;client-initiated-device-configure&#8217;<br />
&nbsp;&#8216;client-initiated-prl-update&#8217;<br />
&nbsp;&#8216;client-initiated-hands-free-activation&#8217;</p>
<dt><code>&#8211;oma-accept-network-initiated-session=[SESSION ID]</code></p>
<dd> Request to accept a network initiated session.</p>
<dt><code>&#8211;oma-reject-network-initiated-session=[SESSION ID]</code></p>
<dd> Request to reject a network initiated session.</p>
<dt><code>&#8211;oma-cancel-session</code></p>
<dd> Request to cancel current OMA session, if any. </p>
</dl>
<h2>SIM OPTIONS</h2>
<dl>
<dt><code>&#8211;pin=PIN</code></p>
<dd> Send <code>PIN</code> code to a given SIM card.</p>
<dt><code>&#8211;puk=PUK</code></p>
<dd> Send <code>PUK</code> code to a given SIM card. This must be used <i>WITH</i> <code>&#8211;pin</code>.</p>
<dt><code>&#8211;enable-pin</code></p>
<dd> Enable PIN request for a given SIM card. This must be used <i>WITH</i> <code>&#8211;pin</code>.</p>
<dt><code>&#8211;disable-pin</code></p>
<dd> Disable PIN request for a given SIM card. This must be used <i>WITH</i> <code>&#8211;pin</code>.</p>
<dt><code>&#8211;change-pin=PIN</code></p>
<dd> Change the PIN for a given SIM card. It will be set to <code>PIN</code>. This must be used <i>WITH</i> <code>&#8211;pin</code> to supply the old PIN number. </p>
</dl>
<h2>BEARER OPTIONS</h2>
<p> All bearer options require the <code>&#8211;bearer</code> or <code>-b</code> option. </p>
<dl>
<dt><code>-c, &#8211;connect</code></p>
<dd> Connect to a given bearer.</p>
<dt><code>-x, &#8211;disconnect</code></p>
<dd> Disconnect from a given bearer. </p>
</dl>
<h2>SMS OPTIONS</h2>
<p> All SMS options require the <code>&#8211;sms</code> or <code>-s</code> option. </p>
<dl>
<dt><code>&#8211;send</code></p>
<dd> Send an SMS.</p>
<dt><code>&#8211;store</code></p>
<dd> This option will store the SMS in the default storage defined by the modem, which may be either modem-memory or SMS-memory. To know what the existing default storage is, see the <code>&#8211;messaging-status</code> option. </p>
<dt><code>&#8211;store-in-storage=STORAGE</code></p>
<dd> This option states which <code>STORAGE</code> to use for SMS messages. Possible values for <code>STORAGE</code> include:</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>&#8216;sm&#8217;</code></p>
<dd> SIM card storage area.</p>
<dt><code>&#8216;me&#8217;</code></p>
<dd> Mobile equipment storage area.</p>
<dt><code>&#8216;mt&#8217;</code></p>
<dd> Sum of SIM and Mobile equipment storages</p>
<dt><code>&#8216;sr&#8217;</code></p>
<dd> Status report message storage area.</p>
<dt><code>&#8216;bm&#8217;</code></p>
<dd> Broadcast message storage area.</p>
<dt><code>&#8216;ta&#8217;</code></p>
<dd> Terminal adaptor message storage area.</dl>
</dl>
<dt><code>&#8211;create-file-with-data=PATH</code></p>
<dd> This option takes an SMS that has <i>DATA</i> (not <i>TEXT</i>) and will create a local file described by <code>PATH</code> and store the content of the SMS there. </p>
</dl>
<h2>CALL OPTIONS</h2>
<dl>
<dt><code>&#8211;start</code></p>
<dd> Initiate an outgoing call.</p>
<dt><code>&#8211;accept</code></p>
<dd> Accept an incoming call.</p>
<dt><code>&#8211;hangup</code></p>
<dd> Reject an incoming call or hangup an ongoing one.</p>
<dt><code>&#8211;send-dtmf=[0-9A-D*#]</code></p>
<dd> Send a DTMF sequence through an ongoing call. </p>
</dl>
<h2>APPLICATION OPTIONS</h2>
<dl>
<dt><code>-J, &#8211;output-json</code></p>
<dd> Run action with machine-friendly JSON output, to be used e.g. by shell scripts that rely on mmcli operations.</p>
<dt><code>-K, &#8211;output-keyvalue</code></p>
<dd> Run action with machine-friendly key-value output, to be used e.g. by shell scripts that rely on mmcli operations.</p>
<dt><code>-v, &#8211;verbose</code></p>
<dd> Perform actions with more details reported and/or logged.</p>
<dt><code>-V, &#8211;version</code></p>
<dd> Returns the version of this program.</p>
<dt><code>-a, &#8211;async</code></p>
<dd> Use asynchronous methods. This is purely a development tool and has no practical benefit to most user operations.</p>
<dt><code>&#8211;timeout=SECONDS</code></p>
<dd> Use <code>SECONDS</code> for the timeout when performing operations with this command. This option is useful when executing long running operations, like <code>&#8211;3gpp-scan</code>. </p>
</dl>
<h2>EXAMPLES</h2>
<h3>Send the PIN to the SIM card</h3>
<p> You&#8217;ll need first to know which the proper path/index is for the SIM in your modem: </p>
<pre>
    $ mmcli -m 0 -K | grep &quot;modem.generic.sim&quot; | awk -F &quot;: &quot; '{ print $2 }'
    /org/freedesktop/ModemManager1/SIM/0
</pre>
<p> And after that, you can just use the SIM index: </p>
<pre>
    $ sudo mmcli -i 0 --pin=1234
    successfully sent PIN code to the SIM
</pre>
<h3>Simple connect and disconnect</h3>
<p> You can launch the simple connection process like: </p>
<pre>
    $ sudo mmcli -m 0 --simple-connect=&quot;pin=1234,apn=internet&quot;
    successfully connected the modem
</pre>
<p> Then, you can disconnect it like: </p>
<pre>
    $ sudo mmcli -m 0 --simple-disconnect
    successfully disconnected all bearers in the modem
</pre>
<h3>3GPP network scan</h3>
<p> Scanning for 3GPP networks may really take a long time, so a specific timeout must be given: </p>
<pre><code>
$ sudo mmcli - m 0 --3gpp-scan --timeout = 300 -- -- -- -- -- -- -- -- -- -- -3GPP scan | networks : 21403 - Orange SP(gprs, unknown) | 21407 - Movistar(gprs, unknown) | 21404 - YOIGO(gprs, unknown) | 21401 - vodafone ES(gprs, unknown)
</code></pre>
<h3>Creating a new SMS message &amp; storing it</h3>
<p> Using the “sm” (SIM), you can do this using: </p>
<p>$ sudo mmcli &#8211; m 0 &#8211;messaging &#8211; create &#8211; sms = &#8220;text=&#8217;Hello world&#8217;,number=&#8217;+1234567890&#8242;&#8221; Successfully created new SMS : / org / freedesktop / ModemManager1 / SMS / 21(unknown)$ sudo mmcli &#8211; s 21 &#8211;store &#8211; in &#8211; storage = &#8220;sm&#8221; successfully stored the SMS<br />
                                                                                                                                                                                                                                     $ sudo mmcli &#8211;<br />
                                                                                                                                                                                                                                 s 21 &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; -General |<br />
                                                                                                                                                                                                                             dbus path : / org / freedesktop / ModemManager1 / SMS / 21 &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; -Content | number : +1234567890 | text : Hello world&#8211; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; -Properties | PDU type : submit | state : stored | smsc : unknown | validity : 0 | class : 0 | storage : sm | delivery report : not requested | message reference : 0 $ sudo mmcli &#8211; m 0 &#8211;messaging &#8211; status&#8211; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8211;Messaging | supported storages : sm,<br />
                                          me | default storage : me</p>
<h3>Sending binary SMS messages from files</h3>
<p> As you can see below, the important part is the <code>&#8211;messaging-create-sms-with-data</code> and the <code>PATH</code> provided. </p>
<pre>
    $ sudo mmcli -m 0 \
           --messaging-create-sms=&quot;number='+1234567890'&quot; \
           --messaging-create-sms-with-data=/path/to/your/file
    Successfully created new SMS:
        /org/freedesktop/ModemManager1/SMS/22 (unknown)
    $ sudo mmcli -s 22 --send
    successfully sent the SMS
</pre>
<h3>Listing SMS messages</h3>
<p> When the receiver gets all the parts of the message, they can now recover the sent file with another <code>mmcli</code> command in their ModemManager setup: </p>
<pre>
    $&gt; sudo mmcli -m 0 --messaging-list-sms
        /org/freedesktop/ModemManager1/SMS/0 (received)
    $&gt; sudo mmcli -s 0 --create-file-with-data=/path/to/the/output/file
</pre>
<h3>GPS location status</h3>
<p> You first need to check whether the modem has GPS-specific location capabilities. Note that we’ll assume the modem is exposed as index 0; if you have more than one modem, just use &#8211;list-modems to check the proper modem index: </p>
<p>$ mmcli &#8211; m 0 &#8211;location &#8211; status&#8211; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8211;Location | capabilities : 3gpp-lac &#8211; ci, gps &#8211; raw, gps &#8211; nmea | enabled : none | signals : no</p>
<p> The output says that the modem supports 3GPP Location area code/Cell ID, GPS raw and GPS-NMEA location sources. None is enabled yet, as we didn’t enable the modem, which we can do issuing: </p>
<p>$ sudo mmcli &#8211; m 0 &#8211;enable successfully enabled the modem $ mmcli &#8211; m 0 &#8211;location &#8211; status&#8211; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8211;Location | capabilities : 3gpp-lac &#8211; ci, gps &#8211; raw, gps &#8211; nmea | enabled : 3gpp-lac &#8211; ci | signals : no</p>
<h3>GPS location technology enabling</h3>
<p> We can start the GPS engine by enabling the RAW or NMEA GPS location sources: </p>
<pre>
    $ sudo mmcli -m 0 \
                 --location-enable-gps-raw \
                 --location-enable-gps-nmea
    successfully setup location gathering
</pre>
<p> If we do check again the status, we’ll see the GPS-specific locations are enabled: </p>
<p>$ mmcli &#8211; m 0 &#8211;location &#8211; status&#8211; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8211;Location | capabilities : 3gpp-lac &#8211; ci, gps &#8211; raw, gps &#8211; nmea | enabled : 3gpp-lac &#8211; ci, gps &#8211; raw, gps &#8211; nmea | signals : no</p>
<h3>GPS location retrieval</h3>
<p> You can query all location information at the same time with a single command. If any of the specific outputs is not available, the corresponding section will be omitted from the output. </p>
<p>$ sudo mmcli &#8211; m 0 &#8211;location &#8211; get&#8211; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; -3GPP location | Mobile country code : 214 | Mobile network code : 3 | Location area code : 21071 | Cell ID : 7033737 &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; -GPS NMEA traces | $GPGGA, , , , , , 0, , , , , , , , *66 | $GPRMC, , V, , , , , , , , , , N * 53 | $GPGSA, A, 1, , , , , , , , , , , , , , , *1E | $GPGSV, 4, 1, 16, 24, , , , 29, , , , 05, , , , 18, , , *7A | $GPGSV, 4, 2, 16, 22, , , , 14, , , , 11, , , , 17, , , *7B | $GPGSV, 4, 3, 16, 03, , , , 12, , , , 30, , , , 13, , , *78 | $GPGSV, 4, 4, 16, 23, , , , 15, , , , 27, , , , 07, , , *79 | $GPVTG, , T, , M, , N, , K, N * 2C</p>
<h3>A-GPS support</h3>
<p> If A-GPS is enabled before starting the GPS engine, and if a data connection is available in the modem, the configured SUPL servers may be used to obtain a faster initial position fix. </p>
<p> Note that the GPS engine will not be started when just A-GPS capability is enabled. An explicit output (RAW or NMEA) is required to be enabled in order to start the GPS engine. </p>
<p>$ mmcli &#8211; m 0 &#8211;location &#8211; status&#8211; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8211;Location | capabilities : 3gpp-lac &#8211; ci, gps &#8211; raw, gps &#8211; nmea, agps &#8211; msa, agps &#8211; msb | enabled : 3gpp-lac &#8211; ci | signals : no&#8211; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; -GPS | refresh rate : 30 seconds | a &#8211; gps supl server : supl.google.com : 7276 $ sudo mmcli &#8211; m 0 &#8211;location &#8211; enable &#8211; agps &#8211; msa successfully setup location gathering $ sudo mmcli &#8211; m 0 &#8211;location &#8211; enable &#8211; gps &#8211; nmea successfully setup location gathering $ sudo mmcli &#8211; m 0 &#8211;location &#8211; enable &#8211; gps &#8211; raw successfully setup location gathering</p>
<h3>Injecting assistance data</h3>
<p> If the modem device does not have an ongoing connection (e.g. no mobile network coverage) but the system has other means to access the Internet (e.g. WiFi), the user may be able to download location assistance data and inject it in the module. </p>
<p> E.g. If the device supports XTRA assistance data, the user may download it from one of the servers listed by ModemManager and manually inject it afterwards. The XTRA assistance data is usually valid for several days. </p>
<p>$ mmcli &#8211; m 0 &#8211;location &#8211; status&#8211; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8211;Location | capabilities : 3gpp-lac &#8211; ci, gps &#8211; raw, gps &#8211; nmea, agps &#8211; msa, agps &#8211; msb | enabled : 3gpp-lac &#8211; ci | signals : no&#8211; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8211;GPS | refresh rate : 30 seconds | a &#8211; gps supl server : supl.google.com : 7276 | supported assistance : xtra | assistance servers : https : // xtrapath3.izatcloud.net/xtra3grcej.bin<br />
                                                                                                                                                                                                                                                                                                                                                                                                          |<br />
                                                                                                                                                                                                                                                                                                                                                                                                          https : // xtrapath1.izatcloud.net/xtra3grcej.bin<br />
                                                                                                                                                                                                                                                                                                                                                                                                                  |<br />
                                                                                                                                                                                                                                                                                                                                                                                                                  https : // xtrapath2.izatcloud.net/xtra3grcej.bin<br />
                                                                                                                                                                                                                                                                                                                                                                                                                          $ wget &#8211;<br />
                                                                                                                                                                                                                                                                                                                                                                                                                          q https : // xtrapath3.izatcloud.net/xtra3grcej.bin<br />
                                                                                                                                                                                                                                                                                                                                                                                                                                    $ sudo mmcli &#8211;<br />
                                                                                                                                                                                                                                                                                                                                                                                                                                    m 0 &#8211;location &#8211; inject &#8211; assistance &#8211; data =./ xtra3grcej.bin successfully injected assistance data $ sudo mmcli &#8211; m 0 &#8211;location &#8211; enable &#8211; gps &#8211; nmea successfully setup location gathering $ sudo mmcli &#8211; m 0 &#8211;location &#8211; enable &#8211; gps &#8211; raw successfully setup location gathering</p>
<h3>Key-Value output</h3>
<p> Writing shell scripts that use mmcli to perform operations with the modem is easy when using the <code>&#8211;output-keyvalue</code> option. For example, you could gather all the main status information of the modem with a single call and then parse it to read single fields: </p>
<pre><code>
$ STATUS = $(mmcli - m 0 --output - keyvalue)
               $ echo "${STATUS}" |
           grep "modem.generic.state " | awk - F ": " '{ print $2 }' failed $ echo "${STATUS}" | grep "modem.generic.state-failed-reason " | awk - F ": " '{ print $2 }' sim - missing
</code></pre>
<h2>AUTHORS</h2>
<p> Written by Martyn Russell &lt;martyn [at] lanedo.com&gt; and Aleksander Morgado &lt;aleksander [at] aleksander.es&gt; </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/8-modemmanager/">ModemManager</a></code>(8), <code><a href="/docs/linux/man/8-networkmanager/">NetworkManager</a></code>(8) </p>
<p> AT (<a rel="nofollow" href="http://en.wikipedia.org/wiki/AT_commands">http://en.wikipedia.org/wiki/AT_commands</a>). </p>
<p> 3GPP (<a rel="nofollow" href="http://en.wikipedia.org/wiki/3GPP">http://en.wikipedia.org/wiki/3GPP</a>). </p>
<p> MCCMNC (<a rel="nofollow" href="http://en.wikipedia.org/wiki/Mobile_Network_Code">http://en.wikipedia.org/wiki/Mobile_Network_Code</a>). </p>
<p> USSD (<a rel="nofollow" href="http://en.wikipedia.org/wiki/Unstructured_Supplementary_Service_Data">http://en.wikipedia.org/wiki/Unstructured_Supplementary_Service_Data</a>). </p>
<p> CDMA (<a rel="nofollow" href="http://en.wikipedia.org/wiki/Code_division_multiple_access">http://en.wikipedia.org/wiki/Code_division_multiple_access</a>). </p>
<p> OTA (<a rel="nofollow" href="http://en.wikipedia.org/wiki/Over-the-air_programming">http://en.wikipedia.org/wiki/Over-the-air_programming</a>). </p>
<p> GPS (<a rel="nofollow" href="http://en.wikipedia.org/wiki/Global_Positioning_System)">http://en.wikipedia.org/wiki/Global_Positioning_System)</a> </p>
<p> NMEA (<a rel="nofollow" href="http://en.wikipedia.org/wiki/NMEA_0183)">http://en.wikipedia.org/wiki/NMEA_0183)</a> </p>
<h2>Index</h2>
