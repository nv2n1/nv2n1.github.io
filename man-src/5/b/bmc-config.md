---
title: "bmc-config(5)"
name: "bmc-config"
section: "5"
letter: "b"
url: "/docs/linux/man/5-bmc-config/"
description: "bmc-config – BMC configuration file format and details"
---

<p>bmc-config &#8211; BMC configuration file format and details</p>
<h2>Description</h2>
<p>Before many IPMI tools can be used over a network, a machine&#8217;s Baseboard Management Controller (BMC) must be configured. The configuration of a BMC can be quite daunting for those who do not know much about IPMI. This manpage hopes to provide enough information on BMC configuration so that you can configure the BMC for your system. When appropriate, typical BMC configurations will be suggested. The following is an example BMC configuration file partially generated from the <code><a href="/docs/linux/man/1-bmc-config/">bmc-config</a>(1)</code> command. This example configuration should be sufficient for most users after the appropriate local IP and MAC addresses are input. Following this example, separate sections of this manpage will discuss the different sections of the BMC configuration file in more detail with explanations of how the BMC can be configured for different environments. Note that many options may or may not be available on your particular machine. For example, Serial-Over-Lan (SOL) is available only on IPMI 2.0 machines. Therefore, if you are looking to configure an IPMI 1.5 machine, many of the SOL or IPMI 2.0 related options will be be unavailable to you. The number of configurable users may also vary for your particular machine. The below configuration file and most of this manpage assume the user is interested in configuring a BMC for use with IPMI over LAN. Various configuration options from <code><a href="/docs/linux/man/1-bmc-config/">bmc-config</a>(1)</code> have been left out or skipped because it is considered unnecessary. Future versions of this manpage will try to include more information.<br />
&nbsp;<wbr>&nbsp;<wbr>Section User1<br />
##&nbsp;<wbr>Give username<br />
##&nbsp;<wbr>Username NULL<br />
##&nbsp;<wbr>Give password or leave it blank to clear password<br />
Password mypassword<br />
##&nbsp;<wbr>Give password for IPMI 2.0 or blank to clear. MAX 20 chars.<br />
&nbsp;<wbr>##&nbsp;<wbr>Password20<br />
##&nbsp;<wbr>Possible values: Yes/No or blank to not set<br />
Enable_User Yes<br />
##&nbsp;<wbr>Possible values: Yes/No<br />
Lan_Enable_Ipmi_Msgs Yes<br />
##&nbsp;<wbr>Possible values: Callback/User/Operator/Administrator/OEM_Proprietary/No_Access<br />
Lan_Privilege_Limit Administrator<br />
&nbsp;<wbr>&nbsp;<wbr>##&nbsp;<wbr>Possible values: 0-17, 0 is unlimited;&nbsp;<wbr>May be reset to 0 if not specified<br />
&nbsp;<wbr>&nbsp;<wbr>##&nbsp;<wbr>Lan_Session_Limit<br />
##&nbsp;<wbr>Possible values: Yes/No<br />
SOL_Payload_Access Yes<br />
&nbsp;<wbr>&nbsp;<wbr>EndSection<br />
&nbsp;<wbr>&nbsp;<wbr>Section User2<br />
##&nbsp;<wbr>Give username<br />
Username user2<br />
##&nbsp;<wbr>Give password or leave it blank to clear password<br />
Password userpass<br />
##&nbsp;<wbr>Give password for IPMI 2.0 or blank to clear. MAX 20 chars.<br />
##&nbsp;<wbr>Password20<br />
##&nbsp;<wbr>Possible values: Yes/No or blank to not set<br />
Enable_User No<br />
##&nbsp;<wbr>Possible values: Yes/No<br />
Lan_Enable_Ipmi_Msgs No<br />
##&nbsp;<wbr>Possible values: Callback/User/Operator/Administrator/OEM_Proprietary/No_Access<br />
Lan_Privilege_Limit No_Access<br />
&nbsp;<wbr>&nbsp;<wbr>##&nbsp;<wbr>Possible values: 0-17, 0 is unlimited;&nbsp;<wbr>May be reset to 0 if not specified<br />
&nbsp;<wbr>&nbsp;<wbr>##&nbsp;<wbr>Lan_Session_Limit<br />
&nbsp;<wbr>&nbsp;<wbr>##&nbsp;<wbr>Possible values: Yes/No<br />
&nbsp;<wbr>&nbsp;<wbr>SOL_Payload_Access No<br />
&nbsp;<wbr>&nbsp;<wbr>EndSection<br />
&nbsp;<wbr>&nbsp;<wbr>Section Lan_Channel<br />
##&nbsp;<wbr>Possible values: Disabled/Pre_Boot_Only/Always_Available/Shared<br />
Volatile_Access_Mode Always_Available<br />
##&nbsp;<wbr>Possible values: Yes/No<br />
Volatile_Enable_User_Level_Auth Yes<br />
##&nbsp;<wbr>Possible values: Yes/No<br />
Volatile_Enable_Per_Message_Auth Yes<br />
##&nbsp;<wbr>Possible values: Yes/No<br />
Volatile_Enable_Pef_Alerting No<br />
##&nbsp;<wbr>Possible values: Callback/User/Operator/Administrator/OEM_Proprietary/No_Access<br />
Volatile_Channel_Privilege_Limit Administrator<br />
##&nbsp;<wbr>Possible values: Disabled/Pre_Boot_Only/Always_Available/Shared<br />
Non_Volatile_Access_Mode Always_Available<br />
##&nbsp;<wbr>Possible values: Yes/No<br />
Non_Volatile_Enable_User_Level_Auth Yes<br />
##&nbsp;<wbr>Possible values: Yes/No<br />
Non_Volatile_Enable_Per_Message_Auth Yes<br />
##&nbsp;<wbr>Possible values: Yes/No<br />
Non_Volatile_Enable_Pef_Alerting No<br />
##&nbsp;<wbr>Possible values: Callback/User/Operator/Administrator/OEM_Proprietary/No_Access<br />
Non_Volatile_Channel_Privilege_Limit Administrator<br />
&nbsp;<wbr>&nbsp;<wbr>EndSection<br />
&nbsp;<wbr>&nbsp;<wbr>Section Lan_Conf<br />
##&nbsp;<wbr>Possible values: Unspecified/Static/Use_DHCP/Use_BIOS/Use_Others<br />
Ip_Address_Source Static<br />
##&nbsp;<wbr>Give valid IP Address<br />
Ip_Address 192.168.1.100<br />
##&nbsp;<wbr>Give valid MAC Address<br />
Mac_Address 00:0E:0E:FF:AA:12<br />
##&nbsp;<wbr>Give valid Subnet mask<br />
Subnet_Mask 255.255.255.0<br />
##&nbsp;<wbr>Give valid IP Address<br />
Default_Gateway_Ip_Address 192.168.1.1<br />
##&nbsp;<wbr>Give valid MAC Address<br />
Default_Gateway_Mac_Address 00:0E:0E:FF:AA:18<br />
##&nbsp;<wbr>Give valid IP Address<br />
Backup_Gateway_Ip_Address 192.168.1.2<br />
##&nbsp;<wbr>Give valid MAC Address<br />
Backup_Gateway_Mac_Address 00:0E:0E:FF:AA:15<br />
&nbsp;<wbr>&nbsp;<wbr>EndSection<br />
&nbsp;<wbr>&nbsp;<wbr>Section Lan_Conf_Auth<br />
##&nbsp;<wbr>Possible values: Yes/No<br />
Callback_Enable_Auth_Type_None No<br />
##&nbsp;<wbr>Possible values: Yes/No<br />
Callback_Enable_Auth_Type_Md2 No<br />
##&nbsp;<wbr>Possible values: Yes/No<br />
Callback_Enable_Auth_Type_Md5 No<br />
##&nbsp;<wbr>Possible values: Yes/No<br />
Callback_Enable_Auth_Type_Straight_Password No<br />
##&nbsp;<wbr>Possible values: Yes/No<br />
Callback_Enable_Auth_Type_Oem_Proprietary No<br />
##&nbsp;<wbr>Possible values: Yes/No<br />
User_Enable_Auth_Type_None No<br />
##&nbsp;<wbr>Possible values: Yes/No<br />
User_Enable_Auth_Type_Md2 Yes<br />
##&nbsp;<wbr>Possible values: Yes/No<br />
User_Enable_Auth_Type_Md5 Yes<br />
##&nbsp;<wbr>Possible values: Yes/No<br />
User_Enable_Auth_Type_Straight_Password No<br />
##&nbsp;<wbr>Possible values: Yes/No<br />
User_Enable_Auth_Type_Oem_Proprietary No<br />
##&nbsp;<wbr>Possible values: Yes/No<br />
Operator_Enable_Auth_Type_None No<br />
##&nbsp;<wbr>Possible values: Yes/No<br />
Operator_Enable_Auth_Type_Md2 Yes<br />
##&nbsp;<wbr>Possible values: Yes/No<br />
Operator_Enable_Auth_Type_Md5 Yes<br />
##&nbsp;<wbr>Possible values: Yes/No<br />
Operator_Enable_Auth_Type_Straight_Password No<br />
##&nbsp;<wbr>Possible values: Yes/No<br />
Operator_Enable_Auth_Type_Oem_Proprietary No<br />
##&nbsp;<wbr>Possible values: Yes/No<br />
Admin_Enable_Auth_Type_None No<br />
##&nbsp;<wbr>Possible values: Yes/No<br />
Admin_Enable_Auth_Type_Md2 Yes<br />
##&nbsp;<wbr>Possible values: Yes/No<br />
Admin_Enable_Auth_Type_Md5 Yes<br />
##&nbsp;<wbr>Possible values: Yes/No<br />
Admin_Enable_Auth_Type_Straight_Password No<br />
##&nbsp;<wbr>Possible values: Yes/No<br />
Admin_Enable_Auth_Type_Oem_Proprietary No<br />
##&nbsp;<wbr>Possible values: Yes/No<br />
Oem_Enable_Auth_Type_None No<br />
##&nbsp;<wbr>Possible values: Yes/No<br />
Oem_Enable_Auth_Type_Md2 No<br />
##&nbsp;<wbr>Possible values: Yes/No<br />
Oem_Enable_Auth_Type_Md5 No<br />
##&nbsp;<wbr>Possible values: Yes/No<br />
Oem_Enable_Auth_Type_Straight_Password No<br />
##&nbsp;<wbr>Possible values: Yes/No<br />
Oem_Enable_Auth_Type_Oem_Proprietary No<br />
&nbsp;<wbr>&nbsp;<wbr>EndSection<br />
&nbsp;<wbr>&nbsp;<wbr>Section Lan_Conf_Security_Keys<br />
&nbsp;<wbr>&nbsp;<wbr>##&nbsp;<wbr>Give string or blank to clear. Max 20 chars<br />
&nbsp;<wbr>&nbsp;<wbr>K_G<br />
&nbsp;<wbr>&nbsp;<wbr>EndSection<br />
&nbsp;<wbr>&nbsp;<wbr>Section Lan_Conf_Misc<br />
##&nbsp;<wbr>Possible values: Yes/No<br />
Enable_Gratuitous_Arps Yes<br />
##&nbsp;<wbr>Possible values: Yes/No<br />
Enable_Arp_Response No<br />
##&nbsp;<wbr>Give valid number. Intervals are 500 ms.<br />
Gratuitous_Arp_Interval 4<br />
&nbsp;<wbr>&nbsp;<wbr>EndSection<br />
&nbsp;<wbr>&nbsp;<wbr>Section Rmcpplus_Conf_Privilege<br />
##&nbsp;<wbr>Possible values: Unused/User/Operator/Administrator/OEM_Proprietary<br />
Maximum_Privilege_Cipher_Suite_Id_0 Unused<br />
##&nbsp;<wbr>Possible values: Unused/User/Operator/Administrator/OEM_Proprietary<br />
Maximum_Privilege_Cipher_Suite_Id_1 Unused<br />
##&nbsp;<wbr>Possible values: Unused/User/Operator/Administrator/OEM_Proprietary<br />
Maximum_Privilege_Cipher_Suite_Id_2 Unused<br />
##&nbsp;<wbr>Possible values: Unused/User/Operator/Administrator/OEM_Proprietary<br />
Maximum_Privilege_Cipher_Suite_Id_3 Administrator<br />
##&nbsp;<wbr>Possible values: Unused/User/Operator/Administrator/OEM_Proprietary<br />
Maximum_Privilege_Cipher_Suite_Id_4 Administrator<br />
##&nbsp;<wbr>Possible values: Unused/User/Operator/Administrator/OEM_Proprietary<br />
Maximum_Privilege_Cipher_Suite_Id_5 Administrator<br />
##&nbsp;<wbr>Possible values: Unused/User/Operator/Administrator/OEM_Proprietary<br />
Maximum_Privilege_Cipher_Suite_Id_6 Unused<br />
##&nbsp;<wbr>Possible values: Unused/User/Operator/Administrator/OEM_Proprietary<br />
Maximum_Privilege_Cipher_Suite_Id_7 Unused<br />
##&nbsp;<wbr>Possible values: Unused/User/Operator/Administrator/OEM_Proprietary<br />
Maximum_Privilege_Cipher_Suite_Id_8 Administrator<br />
##&nbsp;<wbr>Possible values: Unused/User/Operator/Administrator/OEM_Proprietary<br />
Maximum_Privilege_Cipher_Suite_Id_9 Administrator<br />
##&nbsp;<wbr>Possible values: Unused/User/Operator/Administrator/OEM_Proprietary<br />
Maximum_Privilege_Cipher_Suite_Id_10 Administrator<br />
##&nbsp;<wbr>Possible values: Unused/User/Operator/Administrator/OEM_Proprietary<br />
Maximum_Privilege_Cipher_Suite_Id_11 Unused<br />
##&nbsp;<wbr>Possible values: Unused/User/Operator/Administrator/OEM_Proprietary<br />
Maximum_Privilege_Cipher_Suite_Id_12 Administrator<br />
##&nbsp;<wbr>Possible values: Unused/User/Operator/Administrator/OEM_Proprietary<br />
Maximum_Privilege_Cipher_Suite_Id_13 Administrator<br />
##&nbsp;<wbr>Possible values: Unused/User/Operator/Administrator/OEM_Proprietary<br />
Maximum_Privilege_Cipher_Suite_Id_14 Administrator<br />
&nbsp;<wbr>&nbsp;<wbr>EndSection<br />
&nbsp;<wbr>&nbsp;<wbr>Section SOL_Conf<br />
##&nbsp;<wbr>Possible values: Yes/No<br />
Enable_SOL Yes<br />
##&nbsp;<wbr>Possible values: Callback/User/Operator/Administrator/OEM_Proprietary<br />
SOL_Privilege_Level Administrator<br />
##&nbsp;<wbr>Possible values: Yes/No<br />
Force_SOL_Payload_Authentication Yes<br />
##&nbsp;<wbr>Possible values: Yes/No<br />
Force_SOL_Payload_Encryption Yes<br />
##&nbsp;<wbr>Give a valid integer. Each unit is 5ms<br />
Character_Accumulate_Interval 50<br />
##&nbsp;<wbr>Give a valid number<br />
Character_Send_Threshold 100<br />
##&nbsp;<wbr>Give a valid integer<br />
SOL_Retry_Count 5<br />
##&nbsp;<wbr>Give a valid integer. Interval unit is 10ms<br />
SOL_Retry_Interval 50<br />
##&nbsp;<wbr>Possible values: Serial/9600/19200/38400/57600/115200<br />
Non_Volatile_Bit_Rate 115200<br />
##&nbsp;<wbr>Possible values: Serial/9600/19200/38400/57600/115200<br />
Volatile_Bit_Rate 115200<br />
&nbsp;<wbr>&nbsp;<wbr>EndSection<br />
&nbsp;<wbr>&nbsp;<wbr>Section Misc<br />
##&nbsp;<wbr>Possible Values: Off_State_AC_Apply/Restore_State_AC_Apply/On_State_AC_Apply<br />
Power_Restore_Policy Restore_State_Ac_Apply<br />
&nbsp;<wbr>&nbsp;<wbr>EndSection </p>
<h2>Section User1, User2, &#8230;</h2>
<p>The <i>User</i> sections of the BMC configuration file are for username configuration for IPMI over LAN communication. The number of users available to be configured on your system will vary by manufacturer. With the exception of the Username for User1, all sections are identical. </p>
<p> The username(s) you wish to configure the BMC with are defined with <i>Username</i>. The first username under Section User1 is typically the NULL username and cannot be modified. The password for the username can be specified with <i>Password</i>. It can be left empty to define a NULL password. Each user you wish to enable must be enabled through the <i>Enable_User</i> configuration option. It is recommended that all usernames have non-NULL passwords or be disabled for security reasons. </p>
<p> Under IPMI 2.0 (including Serial-over-LAN), additional 20 byte password support was added. <i>Password20</i> can be used to set longer passwords. Under most circumstances though, it isn&#8217;t necessary. In the above configuration, we have chosen not to set <i>Password20</i> by leaving it commented out. If your machine does not support IPMI 2.0, this field will not be configurable. </p>
<p> <i>Lan_Enable_Ipmi_Msgs</i> is used to enable or disable IPMI over LAN access for the user. This should be set to &quot;Yes&quot; to allow IPMI over LAN tools to work. </p>
<p> <i>Lan_Privilege_Limit</i> specifies the maximum privilege level limit the user is allowed. Different IPMI commands have different privilege restrictions. For example, determining the power status of a machine only requires the &quot;User&quot; privilege level. However, power cycling requires the &quot;Operator&quot; privilege. Typically, you will want to assign atleast one user with a privilege limit of &quot;Administrator&quot; so that all system functions are available to atleast one user via IPMI over LAN. </p>
<p> <i>Lan_Session_Limit</i> specifies the number of simultaneous IPMI sessions allowed for the user. Most users will wish to set this to &quot;0&quot; to allow unlimited simultaneous IPMI sessions. This field is considered optional by IPMI standards, and may result in errors when attempting to configure it to a non-zero value. If errors to occur, setting the value back to 0 should resolve problems. </p>
<p> <i>SOL_Payload_Access</i> specifies if a particular user is allowed to connect with Serial-Over-LAN (SOL). This should be set to &quot;Yes&quot; to allow this username to use SOL. </p>
<p> The example configuration above disables &quot;User2&quot; but enables the default &quot;NULL&quot; (i.e. anonymous) user. Many IPMI tools (both open-source and vendor) do not allow the user to input a username and assume the NULL username by default. If the tools you are interested in using allow usernames to be input, then it is recommended that one of the non-NULL usernames be enabled and the NULL username disabled for security reasons. It is recommeneded that you disable the NULL username in section User1, so that users are required to specify a username for IPMI over LAN communication. </p>
<p> Some motherboards may require a <i>Username</i> to be configured prior to other fields being read/written. If this is the case, those fields will be set to <i>&lt;username-not-set-yet&gt;</i>.</p>
<h2>Section Lan_Channel</h2>
<p>The Lan_Channel section configures a variety of IPMI over LAN configuration parameters. Both <i>Volatile</i> and <i>Non_Volatile</i> configurations can be set. <i>Volatile</i> configurations are immediately configured onto the BMC and will have immediate effect on the system. <i>Non_Volatile</i> configurations are only available after the next system reset. Generally, both the <i>Volatile</i> and <i>Non_Volatile</i> should be configured identically. </p>
<p> The <i>Access_Mode</i> parameter configures the availability of IPMI over LAN on the system. Typically this should be set to &quot;Always_Available&quot; to enable IPMI over LAN. </p>
<p> The <i>Privilege_Limit</i> sets the maximum privilege any user of the system can have when performing IPMI over LAN. This should be set to the maximum privilege level configured to a username. Typically, this should be set to &quot;Administrator&quot;. </p>
<p> Typically <i>User_Level_Auth</i> and <i>Per_Message_Auth</i> should be set to &quot;Yes&quot; for additional security. Disabling <i>User_Level_Auth</i> allows &quot;User&quot; privileged IPMI commands to be executed without authentication. Disabling <i>Per_Message_Auth</i> allows fewer individual IPMI messages to require authentication.</p>
<h2>Section Lan_Conf</h2>
<p>Those familiar with setting up networks should find most of the fields in this section self explanatory. The example BMC configuration above illustrates the setup of a static IP address. The field <i>IP_Address_Source</i> is configured with &quot;Static&quot;. The IP address, subnet mask, and gateway IP addresses of the machine are respecitvely configured with the <i>IP_Address</i>, <i>Subnet_Mask</i>, <i>Default_Gateway_Ip_Address</i>, and <i>Backup_Gateway_Ip_Address</i> fields. The respective MAC addresses for the IP addresses are configured under <i>Mac_Address</i>, <i>Default_Gateway_Mac_Address</i>, and <i>Backup_Gateway_Mac_Address</i>. </p>
<p> It is not required to setup the BMC <i>IP_Address</i> to be the same <i>P_Address</i> used by your operating system for that network interface. However, if you choose to use a different address, an alternate ARP configuration may need to be setup. </p>
<p> To instead setup your BMC network information via DHCP, the field <i>IP_Address_Source</i> should be configured with &quot;Use_DHCP&quot;. </p>
<p> It is recommended that static IP addresses be configured for address resolution reasons. See <code>Lan_Conf_Misc</code> below for a more detailed explanation.</p>
<h2>Section Lan_Conf_Auth</h2>
<p>This section determines what types of password authentication mechanisms are allowed for users at different privilege levels under the IPMI 1.5 protocol. The currently supported authentication methods for IPMI 1.5 are <i>None</i> (no username/password required), <i>Straight_Password</i> (passwords are sent in the clear), <i>MD2</i> (passwords are MD2 hashed), and <i>MD5</i> (passwords are MD5 hashed). Different usernames at different privilege levels may be allowed to authenticate differently through this configuration. For example, a username with &quot;User&quot; privileges may be allowed to authenticate with a straight password, but a username with &quot;Administrator&quot; privileges may be allowed only authenticate with MD5. </p>
<p> The above example configuration supports <i>MD2</i> and <i>MD5</i> authentication for all users at the &quot;User&quot;, &quot;Operator&quot;, and &quot;Administrator&quot; privilege levels. All authentication mechanisms have been disabled for the &quot;Callback&quot; privilege level. </p>
<p> Generally speaking, you do not want to allow any user to authenticate with <i>None</i> or <i>Straight_Password</i> for security reasons. <i>MD2</i> and <i>MD5</i> are digital signature algorithms that can minimally encrypt passwords. If you have chosen to support the NULL username (enabled User1) and NULL passwords (NULL password for User1), you will have to enable the <i>None</i> authentication fields above to allow users to connect via <i>None</i>.</p>
<h2>Section Lan_Conf_Security_Keys</h2>
<p>This section supports configuration of the IPMI 2.0 (including Serial-over-LAN) K_g key. If your machine does not support IPMI 2.0, this field will not be configurable. </p>
<p> The key is used for two-key authentication in IPMI 2.0. In most tools, when doing IPMI 2.0, the K_g can be optionally specified. It is not required for IPMI 2.0 operation. </p>
<p> In the above example, we have elected to leave this field blank so the K_g key is not used.</p>
<h2>Section Lan_Conf_Misc</h2>
<p>This section lists miscellaneous IPMI over LAN configuration options. These are optional IPMI configuration options that are not implemented on all BMCs. </p>
<p> Normally, a client cannot resolve the ethernet MAC address without the remote operating system running. However, IPMI over LAN would not work when a machine is powered off or if the IP address used by the operating system for that network interface differs from the BMC IP Address. One way to work around this is through gratuitous ARPs. Gratuitous ARPs are ARP packets generated by the BMC and sent out to advertise the BMC&#8217;s IP and MAC address. Other machines on the network can store this information in their local ARP cache for later IP/hostname resolution. This would allow IPMI over LAN to work when the remote machine is powered off. The <i>Enable_Gratuitous_Arps</i> option allows you to enable or disable this feature. The <i>Gratuitous_Arp_Interval</i> option allows you to configure the frequency at which gratuitous ARPs are sent onto the network. </p>
<p> Instead of gratuitous ARPs some BMCs are able to respond to ARP requests, even when powered off. If offerred, this feature can be enabled through the <i>Enable_Arp_Response</i> option. </p>
<p> Generally speaking, turning on gratuitous ARPs is acceptable. However, it will increase traffic on your network. If you are using IPMI on a large cluster, the gratuitous ARPs may easily flood your network. They should be tuned to occur less frequently or disabled. If disabled, the remote machine&#8217;s MAC address should be permanently stored in the local ARP cache through <code><a href="/docs/linux/man/8-arp/">arp</a>(8).</code> </p>
<p> See <code><a href="/docs/linux/man/8-bmc-watchdog/">bmc-watchdog</a>(8)</code> for a method which allows gratuitous ARPs to be disabled when the operating system is running, but enabled when the system is down.</p>
<h2>Section Rmcpplus_Conf_Privilege</h2>
<p>This section supports configuration of the IPMI 2.0 (including Serial-over-LAN) cipher suite IDs. If your machine does not support IPMI 2.0, the fields will not be configurable. </p>
<p> Each cipher suite ID describes a combination of an authentication algorithm, integrity algorithm, and encryption algorithm for IPMI 2.0. The authentication algorithm is used for user authentication with the BMC. The integrity algorithm is used for generating signatures on IPMI packets. The confidentiality algorithm is used for encrypting data. The configuration in this section enables certain cipher suite IDs to be enabled or disabled, and the maximum privilege level a username can authenticate with. </p>
<p> The following table shows the cipher suite ID to algorithms mapping: </p>
<p> 0 &#8211; Authentication Algorithm = None; Integrity Algorithm = None; Confidentiality Algorithm = None </p>
<p> 1 &#8211; Authentication Algorithm = HMAC-SHA1; Integrity Algorithm = None; Confidentiality Algorithm = None </p>
<p> 2 &#8211; Authentication Algorithm = HMAC-SHA1; Integrity Algorithm = HMAC-SHA1-96; Confidentiality Algorithm = None </p>
<p> 3 &#8211; Authentication Algorithm = HMAC-SHA1; Integrity Algorithm = HMAC-SHA1-96; Confidentiality Algorithm = AES-CBC-128 </p>
<p> 4 &#8211; Authentication Algorithm = HMAC-SHA1; Integrity Algorithm = HMAC-SHA1-96; Confidentiality Algorithm = xRC4-128 </p>
<p> 5 &#8211; Authentication Algorithm = HMAC-SHA1; Integrity Algorithm = HMAC-SHA1-96; Confidentiality Algorithm = xRC4-40 </p>
<p> 6 &#8211; Authentication Algorithm = HMAC-MD5; Integrity Algorithm = None; Confidentiality Algorithm = None </p>
<p> 7 &#8211; Authentication Algorithm = HMAC-MD5; Integrity Algorithm = HMAC-MD5-128; Confidentiality Algorithm = None </p>
<p> 8 &#8211; Authentication Algorithm = HMAC-MD5; Integrity Algorithm = HMAC-MD5-128; Confidentiality Algorithm = AES-CBC-128 </p>
<p> 9 &#8211; Authentication Algorithm = HMAC-MD5; Integrity Algorithm = HMAC-MD5-128; Confidentiality Algorithm = xRC4-128 </p>
<p> 10 &#8211; Authentication Algorithm = HMAC-MD5; Integrity Algorithm = HMAC-MD5-128; Confidentiality Algorithm = xRC4-40 </p>
<p> 11 &#8211; Authentication Algorithm = HMAC-MD5; Integrity Algorithm = MD5-128; Confidentiality Algorithm = None </p>
<p> 12 &#8211; Authentication Algorithm = HMAC-MD5; Integrity Algorithm = MD5-128; Confidentiality Algorithm = AES-CBC-128 </p>
<p> 13 &#8211; Authentication Algorithm = HMAC-MD5; Integrity Algorithm = MD5-128; Confidentiality Algorithm = xRC4-128 </p>
<p> 14 &#8211; Authentication Algorithm = HMAC-MD5; Integrity Algorithm = MD5-128; Confidentiality Algorithm = xRC4-40 </p>
<p> Generally speaking, HMAC-SHA1 based algorithms are stronger than HMAC-MD5, which are better than MD5-128 algorithms. AES-CBC-128 confidentiality algorithms are stronger than xRC4-128 algorithms, which are better than xRC4-40 algorithms. Cipher suite ID 3 is therefore typically considered the most secure. Some users may wish to set cipher suite ID 3 to a privilege level and disable all remaining cipher suite IDs. </p>
<p> The above example configuration has decided to allow any user with &quot;Administrator&quot; privileges use any Cipher Suite algorithm suite which requires an authentication, integrity, and confidentiality algorithm. Typically, the maximum privilege level configured to a username should be set for atleast one cipher suite ID. Typically, this is the &quot;Administrator&quot; privilege. </p>
<p> A number of cipher suite IDs are optionally implemented, so the available cipher suite IDs available your system may vary.</p>
<h2>Section SOL_Conf</h2>
<p>This section is for setting up Serial-Over-Lan (SOL) and will only be available for configuration on those machines. SOL can be enabled with the <i>Enable_SOL</i> field. The minimum privilege level required for connecting with SOL is specified by <i>SOL_Privilege_Level</i>. This should be set to the maximum privilege level configured to a username that has SOL enabled. Typically, this is the &quot;Administrator&quot; privilege. Authentication and Encryption can be forced or not using the fields <i>Force_SOL_Payload_Authentication</i> and <i>Force_SOL_Payload_Encryption</i> respectively. It is recommended that these be set on. However, forced authentication and/or encryption support depend on the cipher suite IDs supported. </p>
<p> The <i>Character_Accumulate_Interval</i>, <i>Character_Send_Threshold</i> , <i>SOL_Retry_Count</i> and , <i>SOL_Retry_Interval</i> options are used to set SOL character output speeds. <i>Character_Accumulate_Interval</i> determines how often serial data should be regularly sent and <i>Character_Send_Threshold</i> indicates the character count that if passed, will force serial data to be sent. <i>SOL_Retry_Count</i> indicates how many times packets must be retransmitted if acknowledgements are not received. <i>SOL_Retry_Interval</i> indicates the timeout interval. Generally, the manufacturer recommended numbers will be sufficient. However, you may wish to experiment with these values for faster SOL throughput. </p>
<p> The <i>Non_Volatile_Bit_Rate</i> and <i>Volatile_Bit_Rate</i> determine the baudrate the BMC should use. This should match the baudrate set in the BIOS and operating system, such as <code><a href="/docs/linux/man/8-agetty/">agetty</a>(8).</code> Generally speaking, both the <i>Volatile</i> and <i>Non_Volatile</i> options should be set identically. </p>
<p> In addition to enabling SOL in this section, individual users most also be capable of connecting with SOL. See the section <code>Section User1, User2, &#8230;</code> above for details.</p>
<h2>Section Misc</h2>
<p>The <i>Power_Restore_Policy</i> determines the behavior of the machine when AC power returns after a power loss. The behavior can be set to always power on the machine (&quot;On_State_AC_Apply&quot;), power off the machine (&quot;Off_State_AC_Apply&quot;), or return the power to the state that existed before the power loss (&quot;Restore_State_AC_Apply&quot;).</p>
<h2>Reporting Bugs</h2>
<p>Report bugs to &lt;freeipmi-users [at] gnu.org&gt; or &lt;freeipmi-devel [at] gnu.org&gt;.</p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/7-freeipmi/">freeipmi</a>(7), <a href="/docs/linux/man/8-bmc-config/">bmc-config</a>(8), <a href="/docs/linux/man/8-bmc-watchdog/">bmc-watchdog</a>(8), <a href="/docs/linux/man/8-agetty/">agetty</a>(8) <a rel="nofollow" href="http://www.gnu.org/software/freeipmi/">http://www.gnu.org/software/freeipmi/</a> </p>
