---

title: "ipmitool(1)"
name: "ipmitool"
section: "1"
letter: "i"
url: "/docs/linux/man/1-ipmitool/"
description: "ipmitool – utility for controlling IPMI-enabled devices"
---

<p> ipmitool &#8211; utility for controlling IPMI-enabled devices</p>
<h2>SYNOPSIS</h2>
<p> ipmitool [ &lt;options&gt; ] &lt;command&gt; [ &lt;sub-commands and sub-options&gt; ] </p>
<p> &lt;options&gt; := [ &lt;general-options&gt; | &lt;conditional-opts&gt; ]<br />
 Any recognized option is accepted. Conditional options may be ignored or it&#8217;s usage postponed until shell or exec processes relevant command. </p>
<p> &lt;general-options&gt; := [ -h | -V | -v | -I &lt;interface&gt; | -H &lt;address&gt; |<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>-d&nbsp;<wbr>&lt;N&gt;&nbsp;<wbr>| -p&nbsp;<wbr>&lt;port&gt;&nbsp;<wbr>| -c | -U&nbsp;<wbr>&lt;username&gt;&nbsp;<wbr>|<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>-L&nbsp;<wbr>&lt;privlvl&gt;&nbsp;<wbr>| -l&nbsp;<wbr>&lt;lun&gt;&nbsp;<wbr>| -m&nbsp;<wbr>&lt;local_address&gt;&nbsp;<wbr>|<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>-N&nbsp;<wbr>&lt;sec&gt;&nbsp;<wbr>| -R&nbsp;<wbr>&lt;count&gt;&nbsp;<wbr>|&nbsp;<wbr>&lt;password-option&gt;&nbsp;<wbr>|<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&lt;oem-option&gt;&nbsp;<wbr>|&nbsp;<wbr>&lt;bridge-options&gt;&nbsp;<wbr>] </p>
<p> &lt;conditional-opts&gt; := [ &lt;lan-options&gt; | &lt;lanplus-options&gt; |<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&lt;command-options&gt;&nbsp;<wbr>]<br />
 Bridging:<br />
 &lt;bridge-options&gt; := -t &lt;target_address&gt; [ -b &lt;channel&gt; |<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>[&nbsp;<wbr>-T&nbsp;<wbr>&lt;address&gt;&nbsp;<wbr>| -B&nbsp;<wbr>&lt;channel&gt;&nbsp;<wbr>]&nbsp;<wbr>] </p>
<p> Options used with -I lan:<br />
 &lt;lan-options&gt; := [ -A &lt;authtype&gt; ] </p>
<p> Options used with -I lanplus:<br />
 &lt;lanplus-options&gt; := [ -C &lt;ciphersuite&gt; | &lt;key-option&gt; ] </p>
<p> Option groups setting same value:<br />
 &lt;key-option&gt; := [ -k &lt;key&gt; | -K | -y &lt;hex_key&gt; | -Y ]<br />
 &lt;password-option&gt; := [ -f &lt;password_file&gt; | -a | -P &lt;password&gt; | -E ]<br />
 &lt;oem-option&gt; := [ -o &lt;oemtype&gt; | -g | -s ] </p>
<p> Options used with specific command &lt;command-options&gt;:<br />
 &lt;options-sdr&gt; := [ -S &lt;sdr_cache_file&gt; ]<br />
 &lt;options-sel&gt; := [ -O &lt;sel_oem&gt; ]<br />
 &lt;options-sol&gt; := [ -e &lt;sol_escape_char&gt; ] </p>
<h2>DESCRIPTION</h2>
<p> This program lets you manage Intelligent Platform Management Interface (IPMI) functions of either the local system, via a kernel device driver, or a remote system, using IPMI v1.5 and IPMI v2.0. These functions include printing FRU information, LAN configuration, sensor readings, and remote chassis power control. </p>
<p> IPMI management of a local system interface requires a compatible IPMI kernel driver to be installed and configured. On Linux this driver is called <i>OpenIPMI</i> and it is included in standard distributions. On Solaris this driver is called <i>BMC</i> and is included in Solaris 10. Management of a remote station requires the IPMI-over-LAN interface to be enabled and configured. Depending on the particular requirements of each system it may be possible to enable the LAN interface using ipmitool over the system interface.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-a</code></dt>
<dd> Prompt for the remote server password.</dd>
<dt><code>-A</code> &lt;<i>authtype</i>&gt;</dt>
<dd> Specify an authentication type to use during IPMIv1.5 <i>lan</i> session activation. Supported types are NONE, PASSWORD, MD2, MD5, or OEM.</dd>
<dt><code>-b</code> &lt;<i>channel</i>&gt;</dt>
<dd> Set destination channel for bridged request.</dd>
<dt><code>-B</code> &lt;<i>channel</i>&gt;</dt>
<dd> Set transit channel for bridged request (dual bridge).</dd>
<dt><code>-b</code> &lt;<i>channel</i>&gt;</dt>
<dd> Set destination channel for bridged request.</dd>
<dt><code>-B</code> &lt;<i>channel</i>&gt;</dt>
<dd> Set transit channel for bridged request. (dual bridge)</dd>
<dt><code>-c</code></dt>
<dd> Present output in CSV (comma separated variable) format. This is not available with all commands.</dd>
<dt><code>-C</code> &lt;<i>ciphersuite</i>&gt;</dt>
<dd> The remote server authentication, integrity, and encryption algorithms to use for IPMIv2.0 <i>lanplus</i> connections. See table 22-19 in the IPMIv2.0 specification. The default is 3 which specifies RAKP-HMAC-SHA1 authentication, HMAC-SHA1-96 integrity, and AES-CBC-128 encryption algorithms.</dd>
<dt><code>-d </code><i>N</i></dt>
<dd> Use device number N to specify the /dev/ipmiN (or /dev/ipmi/N or /dev/ipmidev/N) device to use for in-band BMC communication. Used to target a specific BMC on a multi-node, multi-BMC system through the ipmi device driver interface. Default is 0.</dd>
<dt><code>-e</code> &lt;<i>sol_escape_char</i>&gt;</dt>
<dd> Use supplied character for SOL session escape character. The default is to use <i>~</i> but this can conflict with ssh sessions.</dd>
<dt><code>-E</code></dt>
<dd> The remote server password is specified by the environment variable <i>IPMI_PASSWORD</i> or <i>IPMITOOL_PASSWORD</i>. The <i>IPMITOOL_PASSWORD</i> takes precedence.</dd>
<dt><code>-f</code> &lt;<i>password_file</i>&gt;</dt>
<dd> Specifies a file containing the remote server password. If this option is absent, or if password_file is empty, the password will default to NULL.</dd>
<dt><code>-g</code></dt>
<dd> Deprecated. Use: -o intelplus</dd>
<dt><code>-h</code></dt>
<dd> Get basic usage help from the command line.</dd>
<dt><code>-H</code> &lt;<i>address</i>&gt;</dt>
<dd> Remote server address, can be IP address or hostname. This option is required for <i>lan</i> and <i>lanplus</i> interfaces.</dd>
<dt><code>-I</code> &lt;<i>interface</i>&gt;</dt>
<dd> Selects IPMI interface to use. Supported interfaces that are compiled in are visible in the usage help output.</dd>
<dt><code>-k</code> &lt;<i>key</i>&gt;</dt>
<dd> Use supplied Kg key for IPMIv2.0 authentication. The default is not to use any Kg key.</dd>
<dt><code>-K</code></dt>
<dd> Read Kg key from IPMI_KGKEY environment variable.</dd>
<dt><code>-l</code> &lt;<i>lun</i>&gt;</dt>
<dd> Set destination lun for raw commands.</dd>
<dt><code>-L</code> &lt;<i>privlvl</i>&gt;</dt>
<dd> Force session privilege level. Can be CALLBACK, USER, OPERATOR, ADMINISTRATOR. Default is ADMINISTRATOR. This value is ignored and always set to ADMINISTRATOR when combined with <i>-t target address</i>.</dd>
<dt><code>-m</code> &lt;<i>local_address</i>&gt;</dt>
<dd> Set the local IPMB address. The local address defaults to 0x20 or is auto discovered on PICMG platforms when -m is not specified. There should be no need to change the local address for normal operation.</dd>
<dt><code>-N</code> &lt;<i>sec</i>&gt;</dt>
<dd> Specify nr. of seconds between retransmissions of lan/lanplus messages. Defaults are 2 seconds for lan and 1 second for lanplus interfaces. Command <i>raw</i> uses fixed value of 15 seconds. Command <i>sol</i> uses fixed value of 1 second.</dd>
<dt><code>-o</code> &lt;<i>oemtype</i>&gt;</dt>
<dd> Select OEM type to support. This usually involves minor hacks in place in the code to work around quirks in various BMCs from various manufacturers. Use <i>-o list</i> to see a list of current supported OEM types.</dd>
<dt><code>-O</code> &lt;<i>sel oem</i>&gt;</dt>
<dd> Open selected file and read OEM SEL event descriptions to be used during SEL listings. See examples in contrib dir for file format.</dd>
<dt><code>-p</code> &lt;<i>port</i>&gt;</dt>
<dd> Remote server UDP port to connect to. Default is 623.</dd>
<dt><code>-P</code> &lt;<i>password</i>&gt;</dt>
<dd> Remote server password is specified on the command line. If supported it will be obscured in the process list. <code>Note!</code> Specifying the password as a command line option is not recommended.</dd>
<dt><code>-R</code> &lt;<i>count</i>&gt;</dt>
<dd> Set the number of retries for lan/lanplus interface (default=4). Command <i>raw</i> uses fixed value of one try (no retries). Command <i>hpm</i> uses fixed value of 10 retries.</dd>
<dt><code>-s</code></dt>
<dd> Deprecated. Use: -o supermicro</dd>
<dt><code>-S</code> &lt;<i>sdr_cache_file</i>&gt;</dt>
<dd> Use local file for remote SDR cache. Using a local SDR cache can drastically increase performance for commands that require knowledge of the entire SDR to perform their function. Local SDR cache from a remote system can be created with the <i>sdr dump</i> command.</dd>
<dt><code>-t</code> &lt;<i>target_address</i>&gt;</dt>
<dd> Bridge IPMI requests to the remote target address. Default is 32. The <i>-L privlvl</i> option is always ignored and value set to ADMINISTRATOR.</dd>
<dt><code>-T</code> &lt;<i>address</i>&gt;</dt>
<dd> Set transit address for bridge request (dual bridge).</dd>
<dt><code>-T</code> &lt;<i>transmit_address</i>&gt;</dt>
<dd> Set transit address for bridge request. (dual bridge)</dd>
<dt><code>-U</code> &lt;<i>username</i>&gt;</dt>
<dd> Remote server username, default is NULL user.</dd>
<dt><code>-v</code></dt>
<dd> Increase verbose output level. This option may be specified multiple times to increase the level of debug output. If given three times you will get hexdumps of all incoming and outgoing packets. Using it five times provides details on request and expected reply procesing. The <i>hpm</i> commands <i>targetcap</i> <i>compprop</i> <i>abort</i> <i>upgstatus</i> <i>rollback</i> <i>rollbackstatus</i> <i>selftestresult</i> increases the verbosity level</dd>
<dt><code>-V</code></dt>
<dd> Display version information.</dd>
<dt><code>-y</code> &lt;<i>hex key</i>&gt;</dt>
<dd> Use supplied Kg key for IPMIv2.0 authentication. The key is expected in hexadecimal format and can be used to specify keys with non-printable characters. E.g. &#8216;-k PASSWORD&#8217; and &#8216;-y 50415353574F5244&#8217; are equivalent. The default is not to use any Kg key.</dd>
<dt><code>-Y</code></dt>
<dd> Prompt for the Kg key for IPMIv2.0 authentication.</dd>
<dt><code>-z</code> &lt;<i>size</i>&gt;</dt>
<dd> Change Size of Communication Channel. (OEM) </dd>
</dl>
<p> If no password method is specified then ipmitool will prompt the user for a password. If no password is entered at the prompt, the remote server password will default to NULL.</p>
<h2>SECURITY</h2>
<p> There are several security issues be be considered before enabling the IPMI LAN interface. A remote station has the ability to control a system&#8217;s power state as well as being able to gather certain platform information. To reduce vulnerability it is strongly advised that the IPMI LAN interface only be enabled in &#8216;trusted&#8217; environments where system security is not an issue or where there is a dedicated secure &#8216;management network&#8217;. </p>
<p> Further it is strongly advised that you should not enable IPMI for remote access without setting a password, and that that password should not be the same as any other password on that system. </p>
<p> When an IPMI password is changed on a remote machine with the IPMIv1.5 <i>lan</i> interface the new password is sent across the network as clear text. This could be observed and then used to attack the remote system. It is thus recommended that IPMI password management only be done over IPMIv2.0 <i>lanplus</i> interface or the system interface on the local station. </p>
<p> For IPMI v1.5, the maximum password length is 16 characters. Passwords longer than 16 characters will be truncated. </p>
<p> For IPMI v2.0, the maximum password length is 20 characters; longer passwords are truncated.</p>
<h2>COMMANDS</h2>
<dl>
<dt><i>help</i></dt>
<dd> This can be used to get command-line help on ipmitool commands. It may also be placed at the end of commands to get option usage help. </dd>
<p> ipmitool help<br />
 Commands:<br />
&nbsp;<wbr>&nbsp;<wbr>bmc&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Deprecated. Use mc<br />
&nbsp;<wbr>&nbsp;<wbr>channel&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Configure Management Controller channels<br />
&nbsp;<wbr>&nbsp;<wbr>chassis&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Get chassis status and set power state<br />
&nbsp;<wbr>&nbsp;<wbr>dcmi&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Data Center Management Interface<br />
&nbsp;<wbr>&nbsp;<wbr>delloem&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Manage Dell OEM Extensions.<br />
&nbsp;<wbr>&nbsp;<wbr>echo&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Used to echo lines to stdout in scripts<br />
&nbsp;<wbr>&nbsp;<wbr>ekanalyzer&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>run FRU-Ekeying analyzer using FRU files<br />
&nbsp;<wbr>&nbsp;<wbr>event&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Send events to MC<br />
&nbsp;<wbr>&nbsp;<wbr>exec&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Run list of commands from file<br />
&nbsp;<wbr>&nbsp;<wbr>firewall&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Configure Firmware Firewall<br />
&nbsp;<wbr>&nbsp;<wbr>fru&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Print built-in FRU and scan for FRU locators<br />
&nbsp;<wbr>&nbsp;<wbr>fwum&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Update IPMC using Kontron OEM Firmware Update Manager<br />
&nbsp;<wbr>&nbsp;<wbr>gendev&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Read/Write Device associated with Generic Device locators sdr<br />
&nbsp;<wbr>&nbsp;<wbr>hpm&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Update HPM components using PICMG HPM.1 file<br />
&nbsp;<wbr>&nbsp;<wbr>i2c&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Send an I2C Master Write-Read command and print response<br />
&nbsp;<wbr>&nbsp;<wbr>ime&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Upgrade/Query Intel ME firmware<br />
&nbsp;<wbr>&nbsp;<wbr>isol&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Configure and connect Intel IPMIv1.5 Serial-over-LAN<br />
&nbsp;<wbr>&nbsp;<wbr>kontronoem&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Manage Kontron OEM Extensions<br />
&nbsp;<wbr>&nbsp;<wbr>lan&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Configure LAN Channels<br />
&nbsp;<wbr>&nbsp;<wbr>mc&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Management Controller status and global enables<br />
&nbsp;<wbr>&nbsp;<wbr>nm&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Node Manager<br />
&nbsp;<wbr>&nbsp;<wbr>pef&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Configure Platform Event Filtering&nbsp;<wbr>(PEF)<br />
&nbsp;<wbr>&nbsp;<wbr>picmg&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Run a PICMG/ATA extended command<br />
&nbsp;<wbr>&nbsp;<wbr>power&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Shortcut to chassis power commands<br />
&nbsp;<wbr>&nbsp;<wbr>raw&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Send a RAW IPMI request and print response<br />
&nbsp;<wbr>&nbsp;<wbr>sdr&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Print Sensor Data Repository entries and readings<br />
&nbsp;<wbr>&nbsp;<wbr>sel&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Print System Event Log&nbsp;<wbr>(SEL)<br />
&nbsp;<wbr>&nbsp;<wbr>sensor&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Print detailed sensor information<br />
&nbsp;<wbr>&nbsp;<wbr>session&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Print session information<br />
&nbsp;<wbr>&nbsp;<wbr>set&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Set runtime variable for shell and exec<br />
&nbsp;<wbr>&nbsp;<wbr>shell&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Launch interactive IPMI shell<br />
&nbsp;<wbr>&nbsp;<wbr>sol&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Configure and connect IPMIv2.0 Serial-over-LAN<br />
&nbsp;<wbr>&nbsp;<wbr>spd&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Print SPD info from remote I2C device<br />
&nbsp;<wbr>&nbsp;<wbr>sunoem&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Manage Sun OEM Extensions<br />
&nbsp;<wbr>&nbsp;<wbr>tsol&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Configure and connect Tyan IPMIv1.5 Serial-over-LAN<br />
&nbsp;<wbr>&nbsp;<wbr>user&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Configure Management Controller users </p>
<dt><i>channel</i></dt>
<dd>
</dd><dl>
<dl>
<dt><i>authcap</i> &lt;<code>channel number</code>&gt; &lt;<code>max priv</code>&gt;</dt>
<dd>
<p> Displays information about the authentication capabilities of the selected channel at the specified privilege level.</p>
</dd><dl>
<dl>
<dt>Possible privilege levels are:</dt>
<dd>
 <i>1</i> Callback level<br />
 <i>2</i> User level<br />
 <i>3</i> Operator level<br />
 <i>4</i> Administrator level<br />
 <i>5</i> OEM Proprietary level<br />
 <i>15</i> No access</dd></dl>
</dl>
<dt><i>info</i> [<code>channel number</code>]</dt>
<dd>
<p> Displays information about the selected channel. If no channel is given it will display information about the currently used channel.</p>
</dd><dl>
<dt>
</dt><dd>
<p> &gt; ipmitool channel info<br />
 Channel 0xf info: </p>
<p>&nbsp;<wbr>&nbsp;<wbr>Channel Medium Type&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>: System Interface </p>
<p>&nbsp;<wbr>&nbsp;<wbr>Channel Protocol Type : KCS </p>
<p>&nbsp;<wbr>&nbsp;<wbr>Session Support&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>: session-less </p>
<p>&nbsp;<wbr>&nbsp;<wbr>Active Session Count&nbsp;<wbr>&nbsp;<wbr>: 0 </p>
<p>&nbsp;<wbr>&nbsp;<wbr>Protocol Vendor ID&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>: 7154</dd></dl>
<dt><i>getaccess</i> &lt;<code>channel number</code>&gt; [&lt;<code>userid</code>&gt;]</dt>
<dd>
</dd><dl>
<dt>
</dt><dd>
<p> Configure the given userid as the default on the given channel number. When the given channel is subsequently used, the user is identified implicitly by the given userid.</p>
</dd><dl>
<dt><i>setaccess</i> &lt;<code>channel number</code>&gt; &lt;<code>userid</code>&gt; [&lt;<i>callin</i>=<code>on</code>|<code>off</code>&gt;]</dt>
<dd> [&lt;<i>ipmi</i>=<code>on</code>|<code>off</code>&gt;] [&lt;<i>link</i>=<code>on</code>|<code>off</code>&gt;] [&lt;<i>privilege</i>=<code>level</code>&gt;] </dd>
<p> Configure user access information on the given channel for the given userid.</p>
<dt><i>getciphers</i> &lt;<i>ipmi</i>|<i>sol</i>&gt; [&lt;<code>channel</code>&gt;]</dt>
<dd>
<p> Displays the list of cipher suites supported for the given application (ipmi or sol) on the given channel.</p>
</dd><dt><i>setkg</i> &lt;<i>hex</i>|<i>plain</i>&gt; &lt;<code>key</code>&gt; [&lt;<code>channel</code>&gt;]</dt>
<dd>
<p> Sets K_g key to given value. Use <i>plain</i> to specify <code>key</code> as simple ASCII string. Use <i>hex</i> to specify <code>key</code> as sequence of hexadecimal codes of ASCII charactes. I.e. following two examples are equivalent: </p>
</dd><dl>
<dt>
</dt><dd> ipmitool channel setkg plain PASSWORD </dd>
<p> ipmitool channel setkg hex 50415353574F5244</dl>
</dl>
</dl>
</dl>
</dl>
<dt><i>chassis</i></dt>
<dd>
</dd><dl>
<dl>
<dt><i>status</i></dt>
<dd>
<p> Status information related to power, buttons, cooling, drives and faults.</p>
</dd><dl>
</dl>
<dt><i>power</i></dt>
<dd>
</dd><dl>
<dl>
<dt><i>status</i></dt>
<dd>
</dd><dl>
</dl>
<dt><i>on</i></dt>
<dd>
</dd><dl>
</dl>
<dt><i>off</i></dt>
<dd>
</dd><dl>
</dl>
<dt><i>cycle</i></dt>
<dd>
</dd><dl>
</dl>
<dt><i>reset</i></dt>
<dd>
</dd><dl>
</dl>
<dt><i>diag</i></dt>
<dd>
</dd><dl>
</dl>
<dt><i>soft</i></dt>
<dd>
</dd><dl>
</dl>
</dl>
</dl>
<dt><i>identify</i> [&lt;seconds&gt;|force]</dt>
<dd>
<p> Identify interval.<br />
 Default is 15 seconds.<br />
 0 &#8211; Off<br />
 force &#8211; To turn on indefinitely</p>
</dd><dl>
</dl>
<dt><i>policy</i></dt>
<dd>
<p> What to do when power is restored.</p>
</dd><dl>
<dl>
<dt><i>list</i></dt>
<dd>
<p> Show available options.</p>
</dd><dl>
</dl>
<dt><i>always-on</i></dt>
<dd>
</dd><dl>
</dl>
<dt><i>previous</i></dt>
<dd>
</dd><dl>
</dl>
<dt><i>always-off</i></dt>
<dd>
</dd><dl>
</dl>
</dl>
</dl>
<dt><i>restart_cause</i></dt>
<dd>
<p> Last restart cause.</p>
</dd><dl>
</dl>
<dt><i>poh</i></dt>
<dd>
<p> Get power on hours.</p>
</dd><dl>
</dl>
<dt><i>bootdev</i></dt>
<dd>
</dd><dl>
<dl>
<dt><i>none</i></dt>
<dd>
<p> Do not change boot device order.</p>
</dd><dl>
</dl>
<dt><i>pxe</i></dt>
<dd>
<p> Force PXE boot.</p>
</dd><dl>
</dl>
<dt><i>disk</i></dt>
<dd>
<p> Force boot from default Hard-drive.</p>
</dd><dl>
</dl>
<dt><i>safe</i></dt>
<dd>
<p> Force boot from default Hard-drive, request Safe Mode.</p>
</dd><dl>
</dl>
<dt><i>diag</i></dt>
<dd>
<p> Force boot from Diagnostic Partition.</p>
</dd><dl>
</dl>
<dt><i>cdrom</i></dt>
<dd>
<p> Force boot from CD/DVD.</p>
</dd><dl>
</dl>
<dt><i>bios</i></dt>
<dd>
<p> Force boot into BIOS Setup.</p>
</dd><dl>
</dl>
<dt><i>floppy</i></dt>
<dd>
<p> Force boot from Floppy/primary removable media.</p>
</dd><dl>
</dl>
</dl>
</dl>
<dt><i>bootparam</i></dt>
<dd>
</dd><dl>
<dl>
<dt><i>force_pxe</i></dt>
<dd>
<p> Force PXE boot</p>
</dd><dl>
</dl>
<dt><i>force_disk</i></dt>
<dd>
<p> Force boot from default Hard-drive</p>
</dd><dl>
</dl>
<dt><i>force_safe</i></dt>
<dd>
<p> Force boot from default Hard-drive, request Safe Mode</p>
</dd><dl>
</dl>
<dt><i>force_diag</i></dt>
<dd>
<p> Force boot from Diagnostic Partition</p>
</dd><dl>
</dl>
<dt><i>force_cdrom</i></dt>
<dd>
<p> Force boot from CD/DVD</p>
</dd><dl>
</dl>
<dt><i>force_bios</i></dt>
<dd>
<p> Force boot into BIOS Setup</p>
</dd><dl>
</dl>
</dl>
</dl>
<dt><i>selftest</i></dt>
<dd>
</dd><dl>
</dl>
</dl>
</dl>
<dt><i>dcmi</i></dt>
<dd>
</dd><dl>
<dl>
<dt><i>discover</i></dt>
<dd>
<p> This command is used to discover supported capabilities in DCMI. </p>
</dd><dt><i>power</i> &lt;<code>command</code>&gt;</dt>
<dd>
<p> Platform power limit command options are: </p>
</dd><dl>
<dl>
<dt><i>reading</i></dt>
<dd>
<p> Get power related readings from the system.</p>
</dd><dt><i>get_limit</i></dt>
<dd>
<p> Get the configured power limits.</p>
</dd><dt><i>set_limit</i> &lt;<code>parameter</code>&gt; &lt;<code>value</code>&gt;</dt>
<dd>
<p> Set a power limit option. </p>
</dd><dl>
<dl>
<dt>Possible parameters/values are:</dt>
<dd>
</dd><dt><i>action</i> &lt;<code>No Action | Hard Power Off &amp; Log Event to SEL | Log Event to SEL</code>&gt;</dt>
<dd>
<p> Exception Actions are taken as &quot;No Action&quot;, &quot;Hard Power Off system and log events to SEL&quot;, or &quot;Log event to SEL only&quot;.</p>
</dd><dt><i>limit</i> &lt;<code>number in Watts</code>&gt;</dt>
<dd>
<p> Power Limit Requested in Watts.</p>
</dd><dt><i>correction</i> &lt;<code>number in milliseconds</code>&gt;</dt>
<dd>
<p> Correction Time Limit in milliseconds.</p>
</dd><dt><i>sample</i> &lt;<code>number in seconds</code>&gt;</dt>
<dd>
<p> Statistics Sampling period in seconds. </p>
</dd></dl>
</dl>
<dt><i>activate</i></dt>
<dd>
<p> Activate the set power limit.</p>
</dd><dt><i>deactivate</i></dt>
<dd>
<p> Deactivate the set power limit.</dd></dl>
</dl>
<dt><i>sensors</i></dt>
<dd>
<p> Prints the available DCMI sensors.</p>
</dd><dt><i>asset_tag</i></dt>
<dd>
<p> Prints the platforms asset tag.</p>
</dd><dt><i>set_asset_tag</i> &lt;<code>string</code>&gt;</dt>
<dd>
<p> Sets the platforms asset tag</p>
</dd><dt><i>get_mc_id_string</i></dt>
<dd>
<p> Get management controller identifier string.</p>
</dd><dt><i>set_mc_id_string</i> &lt;<code>string</code>&gt;</dt>
<dd>
<p> Set management controller identifier string. The maximum length is 64 bytes including a null terminator.</p>
</dd><dt><i>thermalpolicy</i> [&lt;<code>get</code> | <code>set</code>&gt;]</dt>
<dd>
<p> Thermal Limit policy get/set. </p>
</dd><dl>
<dl>
<dt>The commands are:</dt>
<dd>
</dd><dt><i>Get</i> &lt;<code>entityID</code>&gt; &lt;<code>instanceID</code>&gt;</dt>
<dd>
<p> Get Thermal Limit values. </p>
<p> <code>entityID</code> is the physical entity that a sensor or device is associated with. <code>instanceID</code> is a particular instance of an entity. Entity Instance can be in one of two ranges, system-relative or device-relative. For example, a system with four processors could use an Entity Instance value of &quot;0&quot; to identify the first processor.</p>
</dd><dt><i>Set</i> &lt;<code>entityID</code>&gt; &lt;<code>instanceID</code>&gt;</dt>
<dd>
<p> Set Thermal Limit values. </p>
<p> <code>entityID</code> is the physical entity that a sensor or device is associated with. <code>instanceID</code> is a particular instance of an entity. Entity Instance can be in one of two ranges, system-relative or device-relative. For example, a system with four processors could use an Entity Instance value of &quot;0&quot; to identify the first processor.</dd></dl>
</dl>
<dt><i>get_temp_reading</i></dt>
<dd>
<p> Get Temperature Sensor Readings.</p>
</dd><dt><i>get_conf_param</i></dt>
<dd>
<p> Get DCMI Configuration Parameters.</p>
</dd><dt><i>set_conf_param</i> &lt;<code>parameters</code>&gt;</dt>
<dd>
<p> Set DCMI Configuration Parameters.</p>
</dd><dl>
<dl>
<dt>The Configuration Parameters are:</dt>
<dd>
</dd><dt><i>activate_dhcp</i></dt>
<dd>
<p> Activate/restart DHCP</p>
</dd><dt><i>dhcp_config</i></dt>
<dd>
<p> Discover DHCP Configuration.</p>
</dd><dt><i>init</i></dt>
<dd>
<p> Set DHCP Initial timeout interval, in seconds. The recommended default is four seconds.</p>
</dd><dt><i>timeout</i></dt>
<dd>
<p> Set DHCP Server contact timeout interval, in seconds. The recommended default timeout is two minutes.</p>
</dd><dt><i>retry</i></dt>
<dd>
<p> Set DHCP Server contact retry interval, in seconds. The recommended default timeout is sixty-four seconds.</dd></dl>
</dl>
<dt><i>oob_discover</i></dt>
<dd>
<p> Ping/Pong Message for DCMI Discovery. </p>
</dd></dl>
</dl>
<dt><i>delloem</i></dt>
<dd>
</dd><dl>
<dt>
</dt><dd>
<p> The delloem commands provide information on Dell-specific features.</p>
</dd><dl>
<dt><i>setled {b:d.f} {state..}</i></dt>
<dd>
</dd><dl>
<dt>
</dt><dd>
<p> Sets the drive backplane LEDs for a device.<br />
 {b:d.f} = PCI Address of device (eg. 06:00.0)<br />
 {state} = one or more of the following:</p>
</dd><dl>
<dt>
</dt><dd> <i>online | present | hotspare | identify | rebuilding | fault | predict | critical | failed</i>
</dd></dl>
</dl>
<dt><i>lcd</i></dt>
<dd>
</dd><dl>
<dt>
</dt><dd>
 <i>set {mode}</i>|<i>{lcdqualifier}</i>|<i>{errordisplay}</i></dd>
<dl>
<dt>
</dt><dd>
<p> Allows you to set the LCD mode and user-defined string.</dd></dl>
<dl>
<dt><i>lcd set mode</i></dt>
<dd>
</dd><dl>
<dt>
</dt><dd>
 <i>{none}</i>|<i>{modelname}</i>|<i>{ipv4address}</i>|<i>{macaddress}</i>|<br />
 <i>{systemname}</i>|<i>{servicetag}</i>|<i>{ipv6address}</i>|<br />
 <i>{ambienttemp}</i>|<i>{systemwatt}</i>|<i>{assettag}</i>|<br />
 <i>{userdefined}&lt;text&gt;</i> </dd>
<p> Allows you to set the LCD display mode to any of the preceding parameters. </p>
</dl>
<dt><i>lcd set lcdqualifier</i></dt>
<dd>
</dd><dl>
<dt>
</dt><dd>
 <i>{watt}</i>|<i>{btuphr}</i>|<br />
 <i>{celsius}</i>|<i>{fahrenheit}</i> </dd>
<p> Allows you to set the unit for the system ambient temperature mode. </p>
</dl>
<dt><i>lcd set errordisplay</i></dt>
<dd>
</dd><dl>
<dt>
</dt><dd>
 <i>{sel}</i>|<i>{simple}</i> </dd>
<p> Allows you to set the error display.</dl>
<dt><i>lcd info</i></dt>
<dd>
</dd><dl>
<dt>
</dt><dd>
<p> Displays the LCD screen information.</dd></dl>
<dt><i>lcd set vkvm</i></dt>
<dd>
</dd><dl>
<dt>
</dt><dd> <i>{active}</i>|<i>{inactive}</i> </dd>
<p> Allows you to set the vKVM status to active or inactive. When it is active and session is in progress, a message appears on LCD.</dl>
<dt><i>lcd status</i></dt>
<dd>
</dd><dl>
<dt>
</dt><dd>
<p> Displays the LCD status for vKVM display active or inactive and Front Panel access mode (viewandmodify, view-only or disabled).</dd></dl>
</dl>
</dl>
<dt><i>mac</i></dt>
<dd>
</dd><dl>
<dt>
</dt><dd>
<p> Displays the information about the system NICs.</p>
</dd><dl>
<dt><i>mac list</i></dt>
<dd>
<p> Displays the NIC MAC address and status of all NICs. It also displays the DRAC/iDRAC MAC address. </p>
</dd><dt><i>mac get</i></dt>
<dd>
</dd><dl>
<dt>
</dt><dd> <i>&lt;NIC number&gt;</i> </dd>
<p> Displays the selected NICs MAC address and status.</dl>
</dl>
</dl>
<dt><i>lan</i></dt>
<dd>
</dd><dl>
<dt>
</dt><dd>
 Displays the information of Lan. </dd>
<dl>
<dt><i>lan set</i></dt>
<dd>
</dd><dl>
<dt>
</dt><dd> <i>&lt;Mode&gt;</i> </dd>
<p> Sets the NIC selection mode (dedicated, shared with lom1, shared with lom2,shared with lom3,shared with lom4,shared with failover lom1,shared with failover lom2,shared with failover lom3,shared with failover lom4,shared with Failover all loms, shared with Failover None).</dl>
<dt><i>lan get</i></dt>
<dd>
<p> Returns the current NIC selection mode (dedicated, shared with lom1, shared with lom2, shared with lom3, shared with lom4,shared with failover lom1, shared with failover lom2,shared with failover lom3,shared with failover lom4,shared with Failover all loms,shared with Failover None). </p>
</dd><dt><i>lan get active</i></dt>
<dd>
<p> Returns the current active NIC (dedicated, LOM1, LOM2, LOM3 or LOM4).</dd></dl>
</dl>
<dt><i>powermonitor</i></dt>
<dd>
</dd><dl>
<dt>
</dt><dd>
<p> Displays power tracking statistics. </p>
</dd><dl>
<dt><i>powermonitor clear cumulativepower</i></dt>
<dd>
</dd><dl>
<dt>
</dt><dd>
<p> Reset cumulative power reading.</dd></dl>
<dt><i>powermonitor clear peakpower</i></dt>
<dd>
</dd><dl>
<dt>
</dt><dd>
<p> Reset peak power reading.</dd></dl>
<dt><i>powermonitor powerconsumption</i></dt>
<dd>
</dd><dl>
<dt>
</dt><dd> <i>&lt;watt&gt;</i>|<i>&lt;btuphr&gt;</i><br />
 Displays the power consumption in watt or btuphr.</dd></dl>
<dt><i>powermonitor powerconsumptionhistory</i></dt>
<dd>
</dd><dl>
<dt>
</dt><dd> <i>&lt;watt&gt;</i>|<i>&lt;btuphr&gt;</i><br />
 Displays the power consumption history in watt or btuphr.</dd></dl>
<dt><i>powermonitor getpowerbudget</i></dt>
<dd>
</dd><dl>
<dt>
</dt><dd> <i>&lt;watt&gt;</i>|<i>&lt;btuphr&gt;</i><br />
 Displays the power cap in watt or btuphr.</dd></dl>
<dt><i>powermonitor setpowerbudget</i></dt>
<dd>
</dd><dl>
<dt>
</dt><dd> <i>&lt;val&gt;</i><i>&lt;watt</i>|<i>btuphr</i>|<i>percent&gt;</i><br />
 Allows you to set the power cap in watt, BTU/hr or percentage.</dd></dl>
<dt><i>powermonitor enablepowercap</i></dt>
<dd>
</dd><dl>
<dt>
</dt><dd>
 Enables set power cap.</dd></dl>
<dt><i>powermonitor disablepowercap</i></dt>
<dd>
</dd><dl>
<dt>
</dt><dd>
<p> Disables set power cap.</dd></dl>
</dl>
</dl>
</dl>
</dl>
<dl>
<dl>
<dt><i>vFlash info Card</i></dt>
<dd>
</dd><dl>
<dt>
</dt><dd>
<p> Shows Extended SD Card information.</dd></dl>
</dl>
</dl>
<dt><i>echo</i></dt>
<dd>
<p> For echoing lines to stdout in scripts.</p>
</dd><dl>
</dl>
<dt><i>ekanalyzer</i> &lt;<code>command</code>&gt; &lt;<code>xx=filename1</code>&gt; &lt;<code>xx=filename2</code>&gt; [&lt;<code>rc=filename3</code>&gt;] <code>&#8230;</code></dt>
<dd>
</dd><dl>
<dl>
<dt>
</dt><dd> <i>NOTE</i> : This command can support a maximum of 8 files per command line</dd>
<dt>
</dt><dd> <i>filename1</i> : binary file that stores FRU data of a Carrier or an AMC module</dd>
<dt>
</dt><dd> <i>filename2</i> : binary file that stores FRU data of an AMC module.<br />
These binary files can be generated from command:<br />
<i>ipmitool fru read&nbsp;<wbr>&lt;id&gt;&nbsp;<wbr>&lt;filename&gt;</i></dd>
<dt>
</dt><dd> <i>filename3</i> : configuration file used for configuring On-Carrier Device ID or OEM GUID. This file is optional.</dd>
<dt>
</dt><dd> <i>xx</i> : indicates the type of the file. It can take the following value:</dd>
<dl>
<dl>
<dt>
</dt><dd> <i>oc</i> : On-Carrier device</dd>
<dt>
</dt><dd> <i>a1</i> : AMC slot A1</dd>
<dt>
</dt><dd> <i>a2</i> : AMC slot A2</dd>
<dt>
</dt><dd> <i>a3</i> : AMC slot A3</dd>
<dt>
</dt><dd> <i>a4</i> : AMC slot A4</dd>
<dt>
</dt><dd> <i>b1</i> : AMC slot B1</dd>
<dt>
</dt><dd> <i>b2</i> : AMC slot B2</dd>
<dt>
</dt><dd> <i>b3</i> : AMC slot B3</dd>
<dt>
</dt><dd> <i>b4</i> : AMC slot B4</dd>
<dt>
</dt><dd> <i>sm</i> : Shelf Manager </dd>
</dl>
</dl>
<dt>
</dt><dd> The available commands for ekanalyzer are: </dd>
</dl>
</dl>
<dl>
<dl>
<dt><i>print</i> [&lt;<code>carrier</code> | <code>power</code> | <code>all</code>&gt;]</dt>
<dd>
</dd><dl>
<dl>
<dt><i>carrier</i> (default) &lt;<code>oc=filename1</code>&gt; &lt;<code>oc=filename2</code>&gt; <code>&#8230;</code></dt>
<dd>
<p> Display point to point physical connectivity between carriers and AMC modules.<br />
&nbsp;<wbr>Example:<br />
&gt;&nbsp;<wbr>ipmitool ekanalyzer print carrier oc=fru oc=carrierfru<br />
From Carrier file: fru<br />
Number of AMC bays supported by Carrier: 2&nbsp;<wbr><br />
AMC slot B1 topology:<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Port 0&nbsp;<wbr>=====&gt;&nbsp;<wbr>On Carrier Device ID 0, Port 16<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Port 1&nbsp;<wbr>=====&gt;&nbsp;<wbr>On Carrier Device ID 0, Port 12<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Port 2&nbsp;<wbr>=====&gt;&nbsp;<wbr>AMC slot B2, Port 2<br />
AMC slot B2 topology:<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Port 0&nbsp;<wbr>=====&gt;&nbsp;<wbr>On Carrier Device ID 0, Port 3<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Port 2&nbsp;<wbr>=====&gt;&nbsp;<wbr>AMC slot B1, Port 2<br />
*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*<br />
From Carrier file: carrierfru<br />
On Carrier Device ID 0 topology:<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Port 0&nbsp;<wbr>=====&gt;&nbsp;<wbr>AMC slot B1, Port 4<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Port 1&nbsp;<wbr>=====&gt;&nbsp;<wbr>AMC slot B1, Port 5<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Port 2&nbsp;<wbr>=====&gt;&nbsp;<wbr>AMC slot B2, Port 6<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Port 3&nbsp;<wbr>=====&gt;&nbsp;<wbr>AMC slot B2, Port 7<br />
AMC slot B1 topology:<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Port 0&nbsp;<wbr>=====&gt;&nbsp;<wbr>AMC slot B2, Port 0<br />
AMC slot B1 topology:<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Port 1&nbsp;<wbr>=====&gt;&nbsp;<wbr>AMC slot B2, Port 1<br />
Number of AMC bays supported by Carrier: 2 </p>
</dd><dt><i>power</i> &lt;<code>xx=filename1</code>&gt; &lt;<code>xx=filename2</code>&gt; <code>&#8230;</code></dt>
<dd>
<p> Display power supply information between carrier and AMC modules.</p>
</dd><dt><i>all</i> &lt;<code>xx=filename</code>&gt; &lt;<code>xx=filename</code>&gt; <code>&#8230;</code></dt>
<dd>
<p> Display both physical connectivity and power supply of each carrier and AMC modules. </p>
</dd></dl>
</dl>
<dt><i>frushow</i> &lt;<code>xx=filename</code>&gt;</dt>
<dd>
 Convert a binary FRU file into human readable text format. Use -v option to get more display information. </dd>
</dl>
</dl>
<dl>
<dl>
<dt><i>summary</i> [&lt;<code>match</code> | <code>unmatch</code> | <code>all</code>&gt;]</dt>
<dd>
</dd><dl>
<dl>
<dt><i>match</i> (default) &lt;<code>xx=filename</code>&gt; &lt;<code>xx=filename</code>&gt; <code>&#8230;</code></dt>
<dd>
 Display only matched results of Ekeying match between an On-Carrier device and an AMC module or between 2 AMC modules. Example:<br />
&nbsp;<wbr>&gt;&nbsp;<wbr>ipmitool ekanalyzer summary match oc=fru b1=amcB1 a2=amcA2<br />
&nbsp;<wbr>On-Carrier Device vs AMC slot B1<br />
&nbsp;<wbr>&nbsp;<wbr>AMC slot B1 port 0&nbsp;<wbr>==&gt;&nbsp;<wbr>On-Carrier Device 0 port 16<br />
Matching Result<br />
&#8211; From On-Carrier Device ID 0<br />
&nbsp;<wbr>-Channel ID 11 || Lane 0: enable<br />
&nbsp;<wbr>-Link Type: AMC.2 Ethernet<br />
&nbsp;<wbr>-Link Type extension: 1000BASE-BX&nbsp;<wbr>(SerDES Gigabit)&nbsp;<wbr>Ethernet link<br />
&nbsp;<wbr>-Link Group ID: 0 || Link Asym. Match: exact match<br />
&#8211; To AMC slot B1<br />
&nbsp;<wbr>-Channel ID 0 || Lane 0: enable<br />
&nbsp;<wbr>-Link Type: AMC.2 Ethernet<br />
&nbsp;<wbr>-Link Type extension: 1000BASE-BX&nbsp;<wbr>(SerDES Gigabit)&nbsp;<wbr>Ethernet link<br />
&nbsp;<wbr>-Link Group ID: 0 || Link Asym. Match: exact match<br />
*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*<br />
&nbsp;<wbr>&nbsp;<wbr>AMC slot B1 port 1&nbsp;<wbr>==&gt;&nbsp;<wbr>On-Carrier Device 0 port 12<br />
Matching Result<br />
&#8211; From On-Carrier Device ID 0<br />
&nbsp;<wbr>-Channel ID 6 || Lane 0: enable<br />
&nbsp;<wbr>-Link Type: AMC.2 Ethernet<br />
&nbsp;<wbr>-Link Type extension: 1000BASE-BX&nbsp;<wbr>(SerDES Gigabit)&nbsp;<wbr>Ethernet link<br />
&nbsp;<wbr>-Link Group ID: 0 || Link Asym. Match: exact match<br />
&#8211; To AMC slot B1<br />
&nbsp;<wbr>-Channel ID 1 || Lane 0: enable<br />
&nbsp;<wbr>-Link Type: AMC.2 Ethernet<br />
&nbsp;<wbr>-Link Type extension: 1000BASE-BX&nbsp;<wbr>(SerDES Gigabit)&nbsp;<wbr>Ethernet link<br />
&nbsp;<wbr>-Link Group ID: 0 || Link Asym. Match: exact match<br />
*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*<br />
&nbsp;<wbr>On-Carrier Device vs AMC slot A2<br />
&nbsp;<wbr>&nbsp;<wbr>AMC slot A2 port 0&nbsp;<wbr>==&gt;&nbsp;<wbr>On-Carrier Device 0 port 3<br />
Matching Result<br />
&#8211; From On-Carrier Device ID 0<br />
&nbsp;<wbr>-Channel ID 9 || Lane 0: enable<br />
&nbsp;<wbr>-Link Type: AMC.2 Ethernet<br />
&nbsp;<wbr>-Link Type extension: 1000BASE-BX&nbsp;<wbr>(SerDES Gigabit)&nbsp;<wbr>Ethernet link<br />
&nbsp;<wbr>-Link Group ID: 0 || Link Asym. Match: exact match<br />
&#8211; To AMC slot A2<br />
&nbsp;<wbr>-Channel ID 0 || Lane 0: enable<br />
&nbsp;<wbr>-Link Type: AMC.2 Ethernet<br />
&nbsp;<wbr>-Link Type extension: 1000BASE-BX&nbsp;<wbr>(SerDES Gigabit)&nbsp;<wbr>Ethernet link<br />
&nbsp;<wbr>-Link Group ID: 0 || Link Asym. Match: exact match<br />
*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*<br />
&nbsp;<wbr>AMC slot B1 vs AMC slot A2<br />
&nbsp;<wbr>&nbsp;<wbr>AMC slot A2 port 2&nbsp;<wbr>==&gt;&nbsp;<wbr>AMC slot B1 port 2<br />
Matching Result<br />
&#8211; From AMC slot B1<br />
&nbsp;<wbr>-Channel ID 2 || Lane 0: enable<br />
&nbsp;<wbr>-Link Type: AMC.3 Storage<br />
&nbsp;<wbr>-Link Type extension: Serial Attached SCSI&nbsp;<wbr>(SAS/SATA)<br />
&nbsp;<wbr>-Link Group ID: 0 || Link Asym. Match: FC or SAS interface&nbsp;<wbr>{exact match}<br />
&#8211; To AMC slot A2<br />
&nbsp;<wbr>-Channel ID 2 || Lane 0: enable<br />
&nbsp;<wbr>-Link Type: AMC.3 Storage<br />
&nbsp;<wbr>-Link Type extension: Serial Attached SCSI&nbsp;<wbr>(SAS/SATA)<br />
&nbsp;<wbr>-Link Group ID: 0 || Link Asym. Match: FC or SAS interface&nbsp;<wbr>{exact match}<br />
&nbsp;<wbr>*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*</dd>
<dt><i>unmatch</i> &lt;<code>xx=filename</code>&gt; &lt;<code>xx=filename</code>&gt; <code>&#8230;</code></dt>
<dd>
<p> Display the unmatched results of Ekeying match between an On-Carrier device and an AMC module or between 2 AMC modules</p>
</dd><dt><i>all</i> &lt;<code>xx=filename</code>&gt; &lt;<code>xx=filename</code>&gt; <code>&#8230;</code></dt>
<dd>
<p> Display both matched result and unmatched results of Ekeying match between two cards or two modules.</dd></dl>
</dl>
</dl>
</dl>
<dt><i>event</i></dt>
<dd>
</dd><dl>
<dl>
<dt>&lt;<code>predefined event number</code> <i>N</i>&gt;</dt>
<dd>
<p> Send a pre-defined test event to the System Event Log. The following events are included as a means to test the functionality of the System Event Log component of the BMC (an entry will be added each time the event <i>N</i> command is executed). </p>
<p> Currently supported values for <i>N</i> are:<br />
 <i>1</i><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>Temperature: Upper Critical: Going High</p>
<p> <i>2</i><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>Voltage Threshold: Lower Critical: Going Low</p>
<p> <i>3</i><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>Memory: Correctable ECC </p>
<p> <code>NOTE</code>: These pre-defined events will likely not produce &quot;accurate&quot; SEL records for a particular system because they will not be correctly tied to a valid sensor number, but they are sufficient to verify correct operation of the SEL. </p>
</dd><dt><i>file</i> &lt;<code>filename</code>&gt;</dt>
<dd>
<p> Event log records specified in &lt;<code>filename</code>&gt; will be added to the System Event Log. </p>
<p> The format of each line in the file is as follows: </p>
<p> &lt;{<i>EvM Revision</i>} {<i>Sensor Type</i>} {<i>Sensor Num</i>} {<i>Event Dir/Type</i>} {<i>Event Data 0</i>} {<i>Event Data 1</i>} {<i>Event Data 2</i>}&gt;[<i># COMMENT</i>] </p>
<p> e.g.: 0x4 0x2 0x60 0x1 0x52 0x0 0x0 # Voltage threshold: Lower Critical: Going Low </p>
<p> <i>EvM Revision</i> &#8211; The &quot;Event Message Revision&quot; is 0x04 for messages that comply with the IPMI 2.0 Specification and 0x03 for messages that comply with the IPMI 1.0 Specification. </p>
<p> <i>Sensor Type</i> &#8211; Indicates the Event Type or Class. </p>
<p> <i>Sensor Num</i> &#8211; Represents the &#8216;sensor&#8217; within the management controller that generated the Event Message. </p>
<p> <i>Event Dir/Type</i> &#8211; This field is encoded with the event direction as the high bit (bit 7) and the event type as the low 7 bits. Event direction is 0 for an assertion event and 1 for a deassertion event. </p>
<p> See the IPMI 2.0 specification for further details on the definitions for each field. </p>
</dd><dt>&lt;<code>sensorid</code>&gt; &lt;<code>list</code>&gt;</dt>
<dd>
<p> Get a list of all the possible Sensor States and pre-defined Sensor State Shortcuts available for a particular sensor. <code>sensorid</code> is the character string representation of the sensor and must be enclosed in double quotes if it includes white space. Several different commands including <i>ipmitool sensor list</i> may be used to obtain a list that includes the <code>sensorid</code> strings representing the sensors on a given system.</p>
</dd><dl>
<dt>
</dt><dd>
<p> &gt; ipmitool -I open event &quot;PS 2T Fan Fault&quot; list<br />
 Finding sensor PS 2T Fan Fault&#8230; ok<br />
 Sensor States: </p>
<p>&nbsp;<wbr>&nbsp;<wbr>State Deasserted </p>
<p>&nbsp;<wbr>&nbsp;<wbr>State Asserted<br />
 Sensor State Shortcuts: </p>
<p>&nbsp;<wbr>&nbsp;<wbr>present&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>absent </p>
<p>&nbsp;<wbr>&nbsp;<wbr>assert&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>deassert </p>
<p>&nbsp;<wbr>&nbsp;<wbr>limit&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>nolimit </p>
<p>&nbsp;<wbr>&nbsp;<wbr>fail&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>nofail </p>
<p>&nbsp;<wbr>&nbsp;<wbr>yes&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>no </p>
<p>&nbsp;<wbr>&nbsp;<wbr>on&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>off </p>
<p>&nbsp;<wbr>&nbsp;<wbr>up&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>down </p>
</dd></dl>
<dt>&lt;<code>sensorid</code>&gt; &lt;<code>sensor state</code>&gt; [&lt;<code>direction</code>&gt;]</dt>
<dd>
<p> Generate a custom event based on existing sensor information. The optional event <code>direction can be either </code><i>assert</i> (the default) or <i>deassert</i>. </p>
</dd><dl>
<dt>
</dt><dd>
<p> &gt; ipmitool event &quot;PS 2T Fan Fault&quot; &quot;State Asserted&quot;<br />
 Finding sensor PS 2T Fan Fault&#8230; ok </p>
<p>0 | Pre-Init Time-stamp&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>| Fan PS 2T Fan Fault | State Asserted</dd></dl>
<dl>
<dt>
</dt><dd>
<p> &gt; ipmitool event &quot;PS 2T Fan Fault&quot; &quot;State Deasserted&quot;<br />
 Finding sensor PS 2T Fan Fault&#8230; ok </p>
<p>0 | Pre-Init Time-stamp&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>| Fan PS 2T Fan Fault | State Desserted</dd></dl>
<dl>
</dl>
</dl>
</dl>
<dt><i>exec</i> &lt;<code>filename</code>&gt;</dt>
<dd>
</dd><dl>
<dt>
</dt><dd> Execute ipmitool commands from <i>filename</i>. Each line is a complete command. The syntax of the commands are defined by the COMMANDS section in this manpage. Each line may have an optional comment at the end of the line, delimited with a `#&#8217; symbol. </dd>
<p> e.g., a command file with two lines: </p>
<p> sdr list # get a list of sdr records<br />
 sel list # get a list of sel records</dl>
<dt><i>firewall</i></dt>
<dd>
<p> This command supports the Firmware Firewall capability. It may be used to add or remove security-based restrictions on certain commands/command sub-functions or to list the current firmware firewall restrictions set on any commands. For each firmware firewall command listed below, parameters may be included to cause the command to be executed with increasing granularity on a specific LUN, for a specific NetFn, for a specific IPMI Command, and finally for a specific command&#8217;s sub-function (see Appendix H in the IPMI 2.0 Specification for a listing of any sub-function numbers that may be associated with a particular command). </p>
<p> Parameter syntax and dependencies are as follows: </p>
<p> [&lt;<i>channel</i> <code>H</code>&gt;] [&lt;<i>lun</i> <code>L</code>&gt; [ &lt;<i>netfn</i> <code>N</code>&gt; [&lt;<i>command</i> <code>C</code> [&lt;<i>subfn</i> <code>S</code>&gt;]]]] </p>
<p> Note that if &quot;netfn &lt;<code>N</code>&gt;&quot; is specified, then &quot;lun &lt;<code>L</code>&gt;&quot; must also be specified; if &quot;command &lt;<code>C</code>&gt;&quot; is specified, then &quot;netfn &lt;<code>N</code>&gt;&quot; (and therefore &quot;lun &lt;<code>L</code>&gt;&quot;) must also be specified, and so forth. </p>
<p> &quot;channel &lt;<code>H</code>&gt;&quot; is an optional and standalone parameter. If not specified, the requested operation will be performed on the current channel. Note that command support may vary from channel to channel. </p>
<p> Firmware firewall commands:</p>
</dd><dl>
<dl>
<dt><i>info</i> [&lt;<code>Parms as described above</code>&gt;]</dt>
<dd>
<p> List firmware firewall information for the specified LUN, NetFn, and Command (if supplied) on the current or specified channel. Listed information includes the support, configurable, and enabled bits for the specified command or commands. </p>
<p> Some usage examples:</p>
</dd><dl>
<dl>
<dt><i>info</i> [&lt;<code>channel H</code>&gt;] [&lt;<code>lun L</code>&gt;]</dt>
<dd>
<p> This command will list firmware firewall information for all NetFns for the specified LUN on either the current or the specified channel.</p>
</dd><dt><i>info</i> [&lt;<code>channel H</code>&gt;] [&lt;<code>lun L</code>&gt; [ &lt;<code>netfn N</code>&gt; ]</dt>
<dd>
<p> This command will print out all command information for a single LUN/NetFn pair.</p>
</dd><dt><i>info</i> [&lt;<code>channel H</code>&gt;] [&lt;<code>lun L</code>&gt; [ &lt;<code>netfn N</code>&gt; [&lt;<code>command C</code>] ]]</dt>
<dd>
<p> This prints out detailed, human-readable information showing the support, configurable, and enabled bits for the specified command on the specified LUN/NetFn pair. Information will be printed about each of the command subfunctions.</p>
</dd><dt><i>info</i> [&lt;<code>channel H</code>&gt;] [&lt;<code>lun L</code>&gt; [ &lt;<code>netfn N</code>&gt; [&lt;<code>command C</code> [&lt;<code>subfn S</code>&gt;]]]]</dt>
<dd>
<p> Print out information for a specific sub-function.</dd></dl>
</dl>
<dt><i>enable</i> [&lt;<code>Parms as described above</code>&gt;]</dt>
<dd>
<p> This command is used to enable commands for a given NetFn/LUN combination on the specified channel.</p>
</dd><dt><i>disable</i> [&lt;<code>Parms as described above</code>&gt;] [<code>force</code>]</dt>
<dd>
<p> This command is used to disable commands for a given NetFn/LUN combination on the specified channel. Great care should be taken if using the &quot;force&quot; option so as not to disable the &quot;Set Command Enables&quot; command.</p>
</dd><dt><i>reset</i> [&lt;<code>Parms as described above</code>&gt;]</dt>
<dd>
<p> This command may be used to reset the firmware firewall back to a state where all commands and command sub-functions are enabled.</dd></dl>
</dl>
<dt><i>fru</i></dt>
<dd>
</dd><dl>
<dl>
<dt><i>print</i></dt>
<dd>
<p> Read all Field Replaceable Unit (FRU) inventory data and extract such information as serial number, part number, asset tags, and short strings describing the chassis, board, or product.</p>
</dd><dt><i>read</i> &lt;<code>fru id</code>&gt; &lt;<code>fru file</code>&gt;</dt>
<dd>
<p> <code>fru id</code> is the digit ID of the FRU (see output of &#8216;fru print&#8217;). <code>fru file</code> is the absolute pathname of a file in which to dump the binary FRU data pertaining to the specified FRU entity.</p>
</dd><dt><i>write</i> &lt;<code>fru id</code>&gt; &lt;<code>fru file</code>&gt;</dt>
<dd>
<p> <code>fru id</code> is the digit ID of the FRU (see output of &#8216;fru print&#8217;). <code>fru file</code> is the absolute pathname of a file from which to pull the binary FRU data before uploading it to the specified FRU.</p>
</dd><dt><i>upgEkey</i> &lt;<code>fru id</code>&gt; &lt;<code>fru file</code>&gt;</dt>
<dd>
<p> Update a multirecord FRU location. <code>fru id</code> is the digit ID of the FRU (see output of &#8216;fru print&#8217;). <code>fru file</code> is the absolute pathname of a file from which to pull the binary FRU data to upload into the specified multirecord FRU entity. </p>
</dd><dt><i>edit</i> &lt;<code>fru id</code>&gt;</dt>
<dd>
<p> This command provides interactive editing of some supported records, namely PICMG Carrier Activation Record. <code>fru id</code> is the digit ID of the FRU (see output of &#8216;fru print&#8217;); default is 0. </p>
</dd><dt><i>edit</i> &lt;<code>fru id</code>&gt; <code>field</code> &lt;<code>section</code>&gt; &lt;<code>index</code>&gt; &lt;<code>string</code>&gt;</dt>
<dd>
<p> This command may be used to set a field string to a new value. It replaces the FRU data found at <code>index</code> in the specified <code>section</code> with the supplied <code>string</code>. </p>
</dd><dl>
<dl>
<dt><code>fru id</code> is the digit ID of the FRU (see output of &#8216;fru print&#8217;).</dt>
<dd>
</dd><dt>&lt;<code>section</code>&gt; is a string which refers to FRU Inventory Information</dt>
<dd> Storage Areas and may be refer to:</dd>
<dl>
<dl>
<dt><i>c</i> FRU Inventory Chassis Info Area</dt>
<dd>
</dd><dt><i>b</i> FRU Inventory Board Info Area</dt>
<dd>
</dd><dt><i>p</i> FRU Inventory Product Info Area</dt>
<dd>
</dd></dl>
</dl>
<dt>&lt;<code>index</code>&gt; specifies the field number. Field numbering starts on the first &#8216;english text&#8217; field type. For instance in the &lt;<code>board</code>&gt; info area field &#8216;0&#8217; is &lt;<code>Board Manufacturer</code>&gt; and field &#8216;2&#8217; is &lt;<code>Board Serial Number</code>&gt;; see IPMI Platform Management FRU Information Storage Definition v1.0 R1.1 for field locations.</dt>
<dd>
</dd><dt>&lt;<code>string</code>&gt; must be the same length as the string being replaced and must be 8-bit ASCII (0xCx).</dt>
<dd>
</dd></dl>
</dl>
<dt><i>edit</i> &lt;<code>fru id</code>&gt; <code>oem</code> <code>iana</code> &lt;<code>record</code>&gt; &lt;<code>format</code>&gt; [&lt;<code>args</code>&gt;]</dt>
<dd>
<p> This command edits the data found in the multirecord area. Support for OEM specific records is limited.</dd></dl>
</dl>
<dt><i>fwum</i></dt>
<dd>
</dd><dl>
<dt>
</dt><dd> Update IPMC using Kontron OEM Firmware Update Manager.</dd>
<dl>
<dt><i>info</i></dt>
<dd>
 Show information about current firmware. </dd>
<dt><i>status</i></dt>
<dd>
 Show status of each firmware bank present in the hardware. </dd>
<dt><i>download</i> &lt;<code>filename</code>&gt;</dt>
<dd>
<p> Download specified firmware. </p>
</dd><dt><i>upgrade</i> [<code>filename</code>]</dt>
<dd>
<p> Install firmware upgrade. If the filename is specified, the file is downloaded first, otherwise the last firmware downloaded is used. </p>
</dd><dt><i>rollback</i></dt>
<dd>
<p> Ask IPMC to rollback to previous version. </p>
</dd><dt><i>tracelog</i></dt>
<dd>
<p> Show firmware upgrade log. </p>
</dd></dl>
</dl>
<dt><i>gendev</i></dt>
<dd>
</dd><dl>
<dl>
<dt><i>list</i></dt>
<dd>
<p> List All Generic Device Locators.</p>
</dd><dl>
</dl>
<dt><i>read</i> &lt;<code>sdr name</code>&gt; &lt;<code>file</code>&gt;</dt>
<dd>
<p> Read to file eeprom specify by Generic Device Locators.</p>
</dd><dl>
</dl>
<dt><i>write</i> &lt;<code>sdr name</code>&gt; &lt;<code>file</code>&gt;</dt>
<dd>
<p> Write from file eeprom specify by Generic Device Locators</p>
</dd><dl>
</dl>
</dl>
</dl>
<dt><i>hpm</i></dt>
<dd>
</dd><dl>
<dt>
</dt><dd> PICMG HPM.1 Upgrade Agent</dd>
<dl>
<dt><i>check</i></dt>
<dd>
 Check the target information. </dd>
<dt><i>check</i> &lt;<code>filename</code>&gt;</dt>
<dd>
 Display both the existing target version and image version on the screen. </dd>
<dt><i>download</i> &lt;<code>filename</code>&gt;</dt>
<dd>
<p> Download specified firmware. </p>
</dd><dt><i>upgrade</i> &lt;<code>filename</code>&gt; [<code>all</code>] [<code>component &lt;x&gt;</code>] [<code>activate</code>]</dt>
<dd>
 Upgrade the firmware using a valid HPM.1 image file. If no option is specified, the firmware versions are checked first and the firmware is upgraded only if they are different. </dd>
<dl>
<dl>
<dt><i>all</i></dt>
<dd>
 Upgrade all components even if the firmware versions are the same (use this only after using &quot;check&quot; command). </dd>
<dt><i>component</i> &lt;<code>x</code>&gt;</dt>
<dd>
 Upgrade only given component from the given file.<br />
 component 0 &#8211; BOOT<br />
 component 1 &#8211; RTK </dd>
<dt><i>activate</i></dt>
<dd>
 Activate new firmware right away. </dd>
</dl>
</dl>
<dt><i>activate</i></dt>
<dd>
<p> Activate the newly uploaded firmware. </p>
</dd><dt><i>targetcap</i></dt>
<dd>
<p> Get the target upgrade capabilities. </p>
</dd><dt><i>compprop</i> &lt;<code>id</code>&gt; &lt;<code>select</code>&gt;</dt>
<dd>
 Get the specified component properties. Valid component <code>id</code>: 0-7. <code>Select</code> can be one of following:<br />
 0 &#8211; General properties<br />
 1 &#8211; Current firmware version<br />
 2 &#8211; Description string<br />
 3 &#8211; Rollback firmware version<br />
 4 &#8211; Deferred firmware version </dd>
<dt><i>abort</i></dt>
<dd>
<p> Abort the on-going firmware upgrade. </p>
</dd><dt><i>upgstatus</i></dt>
<dd>
 Show status of the last long duration command. </dd>
<dt><i>rollback</i></dt>
<dd>
 Perform manual rollback on the IPM Controller firmware. </dd>
<dt><i>rollbackstatus</i></dt>
<dd>
<p> Show the rollback status. </p>
</dd><dt><i>selftestresult</i></dt>
<dd>
<p> Query the self test results. </p>
</dd></dl>
</dl>
<dt><i>i2c</i> &lt;<code>i2caddr</code>&gt; &lt;<code>read bytes</code>&gt; [&lt;<code>write data</code>&gt;]</dt>
<dd>
<p> This command may be used to execute raw I2C commands with the Master Write-Read IPMI command.</p>
</dd><dt><i>ime</i></dt>
<dd>
</dd><dl>
<dl>
<dt><i>help</i></dt>
<dd>
<p> Print usage information</p>
</dd><dt><i>info</i></dt>
<dd>
<p> Displays information about the Manageability Engine (ME)</p>
</dd><dt><i>update</i> &lt;<code>file</code>&gt;</dt>
<dd>
<p> Upgrade the ME firmware with the specified image file<br />
 <code>WARNING</code> You MUST use a supported image provided by your board vendor </p>
</dd><dt><i>rollback</i></dt>
<dd>
<p> Perform manual rollback of the ME firmware </p>
</dd></dl>
</dl>
<dt><i>isol</i></dt>
<dd>
</dd><dl>
<dl>
<dt><i>info</i></dt>
<dd>
<p> Retrieve information about the Intel IPMI v1.5 Serial-Over-LAN configuration.</p>
</dd><dt><i>set</i> &lt;<code>parameter</code>&gt; &lt;<code>value</code>&gt;</dt>
<dd>
<p> Configure parameters for Intel IPMI v1.5 Serial-over-LAN.</p>
</dd><dl>
<dl>
<dt>Valid parameters and values are:</dt>
<dd>
</dd><dt><i>enabled</i></dt>
<dd> true, false.</dd>
<dt><i>privilege-level</i></dt>
<dd> user, operator, admin, oem.</dd>
<dt><i>bit-rate</i></dt>
<dd> 9.6, 19.2, 38.4, 57.6, 115.2.</dd></dl>
</dl>
<dt><i>activate</i></dt>
<dd>
<p> Causes ipmitool to enter Intel IPMI v1.5 Serial Over LAN mode. An RMCP+ connection is made to the BMC, the terminal is set to raw mode, and user input is sent to the serial console on the remote server. On exit, the SOL payload mode is deactivated and the terminal is reset to its original settings.</p>
</dd><dl>
<dt>
</dt><dd>
<p> Special escape sequences are provided to control the SOL session:</p>
</dd><dl>
<dl>
<dt><i>~.</i> Terminate connection</dt>
<dd>
</dd><dt><i>~^Z</i> Suspend ipmitool</dt>
<dd>
</dd><dt><i>~^X</i> Suspend ipmitool, but don&#8217;t restore tty on restart</dt>
<dd>
</dd><dt><i>~B</i> Send break</dt>
<dd>
</dd><dt><i>~~</i> Send the escape character by typing it twice</dt>
<dd>
</dd><dt><i>~?</i> Print the supported escape sequences</dt>
<dd></dd></dl>
</dl>
<p> Note that escapes are only recognized immediately after newline.</dl>
</dl>
</dl>
<dt><i>kontronoem</i></dt>
<dd>
</dd><dl>
<dt>
</dt><dd>
<p> OEM commands specific to Kontron devices.</p>
</dd><dl>
<dt><i>setsn</i></dt>
<dd>
<p> Set FRU serial number.</p>
</dd><dt><i>setmfgdate</i></dt>
<dd>
<p> Set FRU manufacturing date.</p>
</dd><dt><i>nextboot</i> &lt;<code>boot device</code>&gt;</dt>
<dd>
<p> Select the next boot order on the Kontron CP6012.</dd></dl>
</dl>
<dt><i>lan</i></dt>
<dd>
</dd><dl>
<dt>
</dt><dd>
<p> These commands will allow you to configure IPMI LAN channels with network information so they can be used with the ipmitool <i>lan</i> and <i>lanplus</i> interfaces. <i>NOTE</i>: To determine on which channel the LAN interface is located, issue the `channel info <i>number</i>&#8216; command until you come across a valid 802.3 LAN channel. For example: </p>
<p> &gt; ipmitool -I open channel info 1<br />
 Channel 0x1 info: </p>
<p>&nbsp;<wbr>&nbsp;<wbr>Channel Medium Type&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>: 802.3 LAN<br />
&nbsp;<wbr>&nbsp;<wbr>Channel Protocol Type : IPMB-1.0<br />
&nbsp;<wbr>&nbsp;<wbr>Session Support&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>: session-based<br />
&nbsp;<wbr>&nbsp;<wbr>Active Session Count&nbsp;<wbr>&nbsp;<wbr>: 8<br />
&nbsp;<wbr>&nbsp;<wbr>Protocol Vendor ID&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>: 7154 </p>
</dd><dl>
<dt><i>print</i> [&lt;<code>channel</code>&gt;]</dt>
<dd>
<p> Print the current configuration for the given channel. The default will print information on the first found LAN channel.</p>
</dd><dt><i>set</i> &lt;<code>channel number</code>&gt; &lt;<code>command</code>&gt; &lt;<code>parameter</code>&gt;</dt>
<dd>
<p> Set the given command and parameter on the specified channel. Valid command/parameter options are:</p>
</dd><dl>
<dl>
<dt><i>ipaddr</i> &lt;<code>x.x.x.x</code>&gt;</dt>
<dd>
<p> Set the IP address for this channel.</p>
</dd><dt><i>netmask</i> &lt;<code>x.x.x.x</code>&gt;</dt>
<dd>
<p> Set the netmask for this channel.</p>
</dd><dt><i>macaddr</i> &lt;<code>xx:xx:xx:xx:xx:xx</code>&gt;</dt>
<dd>
<p> Set the MAC address for this channel.</p>
</dd><dt><i>defgw ipaddr</i> &lt;<code>x.x.x.x</code>&gt;</dt>
<dd>
<p> Set the default gateway IP address.</p>
</dd><dt><i>defgw macaddr</i> &lt;<code>xx:xx:xx:xx:xx:xx</code>&gt;</dt>
<dd>
<p> Set the default gateway MAC address.</p>
</dd><dt><i>bakgw ipaddr</i> &lt;<code>x.x.x.x</code>&gt;</dt>
<dd>
<p> Set the backup gateway IP address.</p>
</dd><dt><i>bakgw macaddr</i> &lt;<code>xx:xx:xx:xx:xx:xx</code>&gt;</dt>
<dd>
<p> Set the backup gateway MAC address.</p>
</dd><dt><i>password</i> &lt;<code>pass</code>&gt;</dt>
<dd>
<p> Set the null user password.</p>
</dd><dt><i>snmp</i> &lt;<code>community string</code>&gt;</dt>
<dd>
<p> Set the SNMP community string.</p>
</dd><dt><i>user</i></dt>
<dd>
<p> Enable user access mode for userid 1 (issue the `user&#8217; command to display information about userids for a given channel).</p>
</dd><dt><i>access</i> &lt;<code>on|off</code>&gt;</dt>
<dd>
<p> Set LAN channel access mode.</p>
</dd><dt><i>alert</i> &lt;<code>on|off</code>&gt;</dt>
<dd>
<p> Enable or disable PEF alerting for this channel.</p>
</dd><dt><i>ipsrc</i> &lt;<code>source</code>&gt;</dt>
<dd>
<p> Set the IP address source:<br />
 <i>none</i><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>unspecified</p>
<p> <i>static</i><tt>&nbsp;<wbr></tt>manually configured static IP address</p>
<p> <i>dhcp</i><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>address obtained by BMC running DHCP</p>
<p> <i>bios</i><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>address loaded by BIOS or system software</p>
</dd><dt><i>arp respond</i> &lt;<code>on</code>|<code>off</code>&gt;</dt>
<dd>
<p> Set BMC generated ARP responses.</p>
</dd><dt><i>arp generate</i> &lt;<code>on</code>|<code>off</code>&gt;</dt>
<dd>
<p> Set BMC generated gratuitous ARPs.</p>
</dd><dt><i>arp interval</i> &lt;<code>seconds</code>&gt;</dt>
<dd>
<p> Set BMC generated gratuitous ARP interval.</p>
</dd><dt><i>vlan id</i> &lt;<code>off</code>|<code>id</code>&gt;</dt>
<dd>
<p> Disable VLAN operation or enable VLAN and set the ID.<br />
 ID: value of the virtual lan identifier between 1 and 4094 inclusive.</p>
</dd><dt><i>vlan priority</i> &lt;<code>priority</code>&gt;</dt>
<dd>
<p> Set the priority associated with VLAN frames.<br />
 ID: priority of the virtual lan frames between 0 and 7 inclusive.</p>
</dd><dt><i>auth</i> &lt;<code>level</code>,<code>&#8230;</code>&gt; &lt;<code>type</code>,<code>&#8230;</code>&gt;</dt>
<dd>
<p> Set the valid authtypes for a given auth level.<br />
 Levels: callback, user, operator, admin<br />
 Types: none, md2, md5, password, oem</p>
</dd><dt><i>cipher_privs</i> &lt;<code>privlist</code>&gt;</dt>
<dd>
<p> Correlates cipher suite numbers with the maximum privilege level that is allowed to use it. In this way, cipher suites can restricted to users with a given privilege level, so that, for example, administrators are required to use a stronger cipher suite than normal users. </p>
<p> The format of <i>privlist</i> is as follows. Each character represents a privilege level and the character position identifies the cipher suite number. For example, the first character represents cipher suite 0, the second represents cipher suite 1, and so on. <i>privlist</i> must be 15 characters in length. </p>
<p> Characters used in <i>privlist</i> and their associated privilege levels are: </p>
<p> <i>X</i><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>Cipher Suite Unused</p>
<p> <i>c</i><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>CALLBACK</p>
<p> <i>u</i><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>USER</p>
<p> <i>o</i><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>OPERATOR</p>
<p> <i>a</i><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>ADMIN</p>
<p> <i>O</i><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>OEM</p>
<p> So, to set the maximum privilege for cipher suite 0 to USER and suite 1 to ADMIN, issue the following command: </p>
<p> &gt; ipmitool -I <i>interface</i> lan set <i>channel</i> cipher_privs uaXXXXXXXXXXXXX </p>
</dd><dt>
</dt><dd> <i>bad_pass_thresh</i> &lt;<code>thresh_num</code>&gt; &lt;<code>1|0</code>&gt; &lt;<code>reset_interval</code>&gt; &lt;<code>lockout_interval</code>&gt; </dd>
<p> Sets the Bad Password Threshold. </p>
<p> &lt;<code>thresh_num</code>&gt; If non-zero, this value determines the number of sequential bad passwords that will be allowed to be entered for the identified user before the user is automatically disabled from access on the channel. </p>
<p> &lt;<code>1|0</code>&gt; 1 = generate a Session Audit sensor &quot;Invalid password disable&quot; event message. 0 = do not generate an event message when the user is disabled. </p>
<p> &lt;<code>reset_interval</code>&gt; Attempt Count Reset Interval. The interval, in tens of seconds, for which the accumulated count of bad password attempts is retained before being automatically reset to zero. </p>
<p> &lt;<code>lockout_interval</code>&gt; User Lockout Interval. The interval, in tens of seconds, that the user will remain disabled after being disabled because the Bad Password Threshold number was reached. </p>
</dl>
</dl>
<dt><i>alert</i> <i>print</i> [&lt;<code>channel</code>&gt;] [&lt;<code>alert destination</code>&gt;]</dt>
<dd>
<p> Print alert information for the specified channel and destination. The default will print all alerts for all alert destinations on the first found LAN channel. </p>
</dd><dt><i>alert</i> <i>set</i> &lt;<code>channel number</code>&gt; &lt;<code>alert destination</code>&gt; &lt;<code>command</code>&gt; &lt;<code>parameter</code>&gt;</dt>
<dd>
<p> Set an alert on the given LAN channel and destination. Alert Destinations are listed via the &#8216;<i>lan alert print</i>&#8216; command. Valid command/parameter options are:</p>
</dd><dl>
<dl>
<dt><i>ipaddr</i> &lt;<code>x.x.x.x</code>&gt;</dt>
<dd>
<p> Set alert IP address.</p>
</dd><dt><i>macaddr</i> &lt;<code>xx:xx:xx:xx:xx:xx</code>&gt;</dt>
<dd>
<p> Set alert MAC address.</p>
</dd><dt><i>gateway</i> &lt;<code>default | backup</code>&gt;</dt>
<dd>
<p> Set the channel gateway to use for alerts.</p>
</dd><dt><i>ack</i> &lt;<code>on | off</code>&gt;</dt>
<dd>
<p> Set Alert Acknowledge on or off.</p>
</dd><dt><i>type</i> &lt;<code>pet | oem1 | oem2</code>&gt;</dt>
<dd>
<p> Set the destination type as PET or OEM.</p>
</dd><dt><i>time</i> &lt;<code>seconds</code>&gt;</dt>
<dd>
<p> Set ack timeout or unack retry interval.</p>
</dd><dt><i>retry</i> &lt;<code>number</code>&gt;</dt>
<dd>
<p> Set the number of alert retries.</dd></dl>
</dl>
<dt><i>stats</i> <i>get</i> [&lt;<code>channel number</code>&gt;]</dt>
<dd>
<p> Retrieve information about the IP connections on the specified channel. The default will retrieve statistics on the first found LAN channel.</p>
</dd><dt><i>stats</i> <i>clear</i> [&lt;<code>channel number</code>&gt;]</dt>
<dd>
<p> Clear all IP/UDP/RMCP Statistics to 0 on the specified channel. The default will clear statistics on the first found LAN channel.</dd></dl>
</dl>
<dt><i>mc | bmc</i></dt>
<dd>
</dd><dl>
<dl>
<dt><i>reset</i> &lt;<code>warm</code>|<code>cold</code>&gt;</dt>
<dd>
<p> Instructs the BMC to perform a warm or cold reset.</p>
</dd><dt><i>guid</i></dt>
<dd>
<p> Display the Management Controller Globally Unique IDentifier.</p>
</dd><dt><i>info</i></dt>
<dd>
<p> Displays information about the BMC hardware, including device revision, firmware revision, IPMI version supported, manufacturer ID, and information on additional device support.</p>
</dd><dt><i>watchdog</i></dt>
<dd>
<p> These commands allow a user to view and change the current state of the watchdog timer.</p>
</dd><dl>
<dl>
<dt><i>get</i></dt>
<dd>
<p> Show current Watchdog Timer settings and countdown state.</p>
</dd><dt><i>reset</i></dt>
<dd>
<p> Reset the Watchdog Timer to its most recent state and restart the countdown timer.</p>
</dd><dt><i>off</i></dt>
<dd>
<p> Turn off a currently running Watchdog countdown timer.</dd></dl>
</dl>
<dt><i>selftest</i></dt>
<dd>
<p> Check on the basic health of the BMC by executing the Get Self Test results command and report the results.</p>
</dd><dt><i>getenables</i></dt>
<dd>
<p> Displays a list of the currently enabled options for the BMC. </p>
</dd><dt><i>setenables</i> &lt;<code>option</code>&gt;=[<i>on</i>|<i>off</i>]</dt>
<dd>
<p> Enables or disables the given <i>option</i>. This command is only supported over the system interface according to the IPMI specification. Currently supported values for <i>option</i> include:</p>
</dd><dl>
<dl>
<dt><i>recv_msg_intr</i></dt>
<dd>
<p> Receive Message Queue Interrupt</p>
</dd><dt><i>event_msg_intr</i></dt>
<dd>
<p> Event Message Buffer Full Interrupt</p>
</dd><dt><i>event_msg</i></dt>
<dd>
<p> Event Message Buffer</p>
</dd><dt><i>system_event_log</i></dt>
<dd>
<p> System Event Logging</p>
</dd><dt><i>oem0</i></dt>
<dd>
<p> OEM-Defined option #0</p>
</dd><dt><i>oem1</i></dt>
<dd>
<p> OEM-Defined option #1</p>
</dd><dt><i>oem2</i></dt>
<dd>
<p> OEM-Defined option #2 </p>
</dd></dl>
</dl>
<dt><i>getsysinfo</i> &lt;<code>argument</code>&gt;</dt>
<dd> Retrieves system info from bmc for given argument.<br />
 See <i>setsysinfo</i> for argument definitions</dd>
<dt><i>setsysinfo</i> &lt;<code>argument</code>&gt; &lt;<code>string</code>&gt;</dt>
<dd> Stores system info string to bmc for given argument</dd>
<dl>
<dl>
<dt>Possible arguments are:</dt>
<dd>
</dd><dl>
<dl>
<dt><i>primary_os_name</i> Primary Operating System Name</dt>
<dd>
</dd><dt><i>os_name</i> Operating System Name</dt>
<dd>
</dd><dt><i>system_name</i> System Name of Server</dt>
<dd>
</dd><dt><i>delloem_os_version</i> Running version of operating system</dt>
<dd>
</dd><dt><i>delloem_URL</i> URL of BMC Webserver</dt>
<dd></dd></dl>
</dl>
</dl>
</dl>
<dt><i>chassis</i></dt>
<dd>
</dd><dl>
<dl>
<dt><i>status</i></dt>
<dd>
<p> Displays information regarding the high-level status of the system chassis and main power subsystem.</p>
</dd><dt><i>poh</i></dt>
<dd>
<p> This command will return the Power-On Hours counter.</p>
</dd><dt><i>identify</i> &lt;<code>interval</code>&gt;</dt>
<dd>
<p> Control the front panel identify light. Default interval is 15 seconds. Use 0 to turn off. Use &quot;force&quot; to turn on indefinitely.</p>
</dd><dt><i>restart_cause</i></dt>
<dd>
<p> Query the chassis for the cause of the last system restart.</p>
</dd><dt><i>selftest</i></dt>
<dd>
<p> Check on the basic health of the BMC by executing the Get Self Test results command and report the results.</p>
</dd><dt><i>policy</i></dt>
<dd>
<p> Set the chassis power policy in the event power failure.</p>
</dd><dl>
<dl>
<dt><i>list</i></dt>
<dd>
<p> Return supported policies.</p>
</dd><dt><i>always-on</i></dt>
<dd>
<p> Turn on when power is restored.</p>
</dd><dt><i>previous</i></dt>
<dd>
<p> Returned to previous state when power is restored.</p>
</dd><dt><i>always-off</i></dt>
<dd>
<p> Stay off after power is restored.</dd></dl>
</dl>
<dt><i>power</i></dt>
<dd>
<p> Performs a chassis control command to view and change the power state.</p>
</dd><dl>
<dl>
<dt><i>status</i></dt>
<dd>
<p> Show current chassis power status.</p>
</dd><dt><i>on</i></dt>
<dd>
<p> Power up chassis.</p>
</dd><dt><i>off</i></dt>
<dd>
<p> Power down chassis into soft off (S4/S5 state). <code>WARNING</code>: This command does not initiate a clean shutdown of the operating system prior to powering down the system.</p>
</dd><dt><i>cycle</i></dt>
<dd>
<p> Provides a power off interval of at least 1 second. No action should occur if chassis power is in S4/S5 state, but it is recommended to check power state first and only issue a power cycle command if the system power is on or in lower sleep state than S4/S5.</p>
</dd><dt><i>reset</i></dt>
<dd>
<p> This command will perform a hard reset.</p>
</dd><dt><i>diag</i></dt>
<dd>
<p> Pulse a diagnostic interrupt (NMI) directly to the processor(s).</p>
</dd><dt><i>soft</i></dt>
<dd>
<p> Initiate a soft-shutdown of OS via ACPI. This can be done in a number of ways, commonly by simulating an overtemperture or by simulating a power button press. It is necessary for there to be Operating System support for ACPI and some sort of daemon watching for events for this soft power to work.</dd></dl>
</dl>
<dt><i>bootdev</i> &lt;<code>device</code>&gt; [&lt;<i>clear-cmos</i>=<code>yes</code>|<code>no</code>&gt;] [&lt;<i>options</i>=<code>help,&#8230;</code>&gt;]</dt>
<dd>
<p> Request the system to boot from an alternate boot device on next reboot. The <i>clear-cmos</i> option, if supplied, will instruct the BIOS to clear its CMOS on the next reboot. Various options may be used to modify the boot device settings. Run <i>&quot;bootdev none options=help&quot;</i> for a list of available boot device modifiers/options. </p>
</dd><dl>
<dl>
<dt>Currently supported values for &lt;device&gt; are:</dt>
<dd>
</dd><dt><i>none</i></dt>
<dd>
<p> Do not change boot device</p>
</dd><dt><i>pxe</i></dt>
<dd>
<p> Force PXE boot</p>
</dd><dt><i>disk</i></dt>
<dd>
<p> Force boot from BIOS default boot device</p>
</dd><dt><i>safe</i></dt>
<dd>
<p> Force boot from BIOS default boot device, request Safe Mode</p>
</dd><dt><i>diag</i></dt>
<dd>
<p> Force boot from diagnostic partition</p>
</dd><dt><i>cdrom</i></dt>
<dd>
<p> Force boot from CD/DVD</p>
</dd><dt><i>bios</i></dt>
<dd>
<p> Force boot into BIOS setup</p>
</dd><dt><i>floppy</i></dt>
<dd>
<p> Force boot from Floppy/primary removable media</dd></dl>
</dl>
<dt><i>bootparam</i></dt>
<dd>
<p> Get or set various system boot option parameters.</p>
</dd><dl>
<dl>
<dt><i>get</i> &lt;<code>param #</code>&gt;</dt>
<dd>
<p> Get boot parameter. Currently supported values for &lt;<code>param #</code>&gt; are: </p>
<p> <i>0</i> &#8211; Set In Progress </p>
<p> <i>1</i> &#8211; Service Partition Selector </p>
<p> <i>2</i> &#8211; Service Partition Scan </p>
<p> <i>3</i> &#8211; BMC Boot Flag Valid Bit Clearing </p>
<p> <i>4</i> &#8211; Boot Info Acknowledge </p>
<p> <i>5</i> &#8211; Boot Flags </p>
<p> <i>6</i> &#8211; Boot Initiator Info </p>
<p> <i>7</i> &#8211; Boot Initiator Mailbox </p>
</dd><dt><i>set</i> &lt;<code>device</code>&gt; [&lt;<i>options</i>=<code>help,&#8230;</code>&gt;]</dt>
<dd>
<p> Set boot device parameter used for next boot. Various options may be used to change when the the next boot device is cleared. Run <i>&quot;options=help&quot;</i> for a list of available bootparam set device options. </p>
</dd><dl>
<dl>
<dt>Currently supported bootparam <code>device</code> settings are:</dt>
<dd>
</dd><dt><i>force_pxe</i></dt>
<dd>
<p> Force PXE boot</p>
</dd><dt><i>force_disk</i></dt>
<dd>
<p> Force boot from default hard-drive</p>
</dd><dt><i>force_safe</i></dt>
<dd>
<p> Force boot from default hard-drive, request Safe Mode</p>
</dd><dt><i>force_diag</i></dt>
<dd>
<p> Force boot from diagnostic partition</p>
</dd><dt><i>force_cdrom</i></dt>
<dd>
<p> Force boot from CD/DVD</p>
</dd><dt><i>force_bios</i></dt>
<dd>
<p> Force boot into BIOS setup </p>
</dd></dl>
</dl>
<dl>
<dl>
<dt>Currently supported bootparam <code>options</code> settings are associated with BMC Boot Valid Bit Clearing and are as follows: Any option can be prefixed with &quot;no-&quot; to invert the sense of the operation.</dt>
<dd>
</dd><dt><i>PEF</i></dt>
<dd>
<p> Clear valid bit on reset/power cycle caused by PEF</p>
</dd><dt><i>timeout</i></dt>
<dd>
<p> Automatically clear boot flag valid bit if Chassis Control command is not received within 60 seconds.</p>
</dd><dt><i>watchdog</i></dt>
<dd>
<p> Clear valid bit on reset/power cycle caused by watchdog timeout</p>
</dd><dt><i>reset</i></dt>
<dd>
<p> Clear valid bit on push button reset / soft-reset</p>
</dd><dt><i>power</i></dt>
<dd>
<p> Clear valid bit on power up via power push button or wake event </p>
</dd></dl>
</dl>
</dl>
</dl>
</dl>
</dl>
</dl>
</dl>
<dt><i>nm</i></dt>
<dd>
</dd><dl>
<dl>
<dt><i>alert</i></dt>
<dd>
</dd><dl>
<dl>
<dt><i>clear dest</i> &lt;<code>dest</code>&gt;</dt>
<dd>
<p> Clear the Node Manager Alert lan destination. </p>
</dd></dl>
</dl>
<dl>
<dl>
<dt><i>get</i></dt>
<dd>
 Get the Node Manager Alert settings. </dd>
</dl>
</dl>
<dl>
<dl>
<dt><i>set chan</i> &lt;<code>chan</code>&gt; <i>dest</i> &lt;<code>dest</code>&gt; <i>string</i> &lt;<code>string</code>&gt;</dt>
<dd>
<p> Set the Node Manager alert channel, lan destination, and alert string number. </p>
</dd></dl>
</dl>
<dt><i>capability</i></dt>
<dd>
<p> Obtain the Node Manager power control capabilities and ranges. </p>
</dd><dt><i>control</i></dt>
<dd>
</dd><dl>
<dl>
<dt><i>enable</i>|<i>disable </i></dt>
<dd>
</dd><dl>
<dl>
<dt><i>global</i></dt>
<dd>
<p> Enable/disable all policies for all domains.</p>
</dd><dt><i>per_domain</i> &lt;platform|CPU|Memory&gt;</dt>
<dd>
<p> Enable/disable all policies of the specified domain.</p>
</dd><dt><i>per_policy</i> &lt;0-7&gt;</dt>
<dd>
<p> Enable/disable the policy for the specified domain/policy combination.</dd></dl>
</dl>
</dl>
</dl>
<dt><i>discover</i></dt>
<dd>
<p> Discover Node Manager presence as well as the Node Manager version, revision, and patch number. </p>
</dd><dt><i>policy</i></dt>
<dd>
</dd><dl>
<dl>
<dt><i>add</i></dt>
<dd>
</dd><dl>
<dl>
<dt><i>power</i> &lt;watts&gt; <i>policy_id</i> &lt;0-7&gt; [<i>correction</i> auto|soft|hard] <i>trig_lim</i> &lt;seconds&gt; <i>stats</i> &lt;seconds&gt; [<i>domain</i> &lt;platform|CPU|Memory&gt;] <i>enable</i>|<i>disable</i></dt>
<dd>
<p> Add a new power policy, or overwrite an existing policy. The <i>correction</i> parameter is the agressiveness of frequency limiting, default is auto. The <i>trig_lim</i> is the correction time limit and must be at least 6000 and not greater than 65535. The <i>stats</i> setting is the averaging period in seconds and ranges from 1-65535. If domain is not supplied a default of platform is used. </p>
</dd><dt><i>inlet</i> &lt;temp&gt; <i>policy_id</i> &lt;0-7&gt; [<i>correction</i> auto|soft|hard] <i>trig_lim</i> &lt;seconds&gt; <i>stats</i> &lt;seconds&gt; [<i>domain</i> &lt;platform|CPU|Memory&gt;] <i>enable</i>|<i>disable</i></dt>
<dd>
<p> Add a new inlet temp policy, or overwrite an existing policy. The <i>correction</i> parameter is the agressiveness of frequency limiting, default is auto. The <i>trig_lim</i> is the correction time limit and must be at least 6000 and not greater than 65535. The <i>stats</i> setting is the averaging period in seconds and ranges from 1-65535. If domain is not supplied a default of platform is used. </p>
</dd></dl>
</dl>
<dt><i>get</i> <i>policy_id</i> &lt;0-7&gt;</dt>
<dd>
<p> Get a previously stored policy.</p>
</dd><dt><i>limiting</i></dt>
<dd>
<p> Report policy number if any policy is limiting power.</p>
</dd><dt><i>remove</i> <i>policy_id</i> &lt;0-7&gt; [<i>domain</i> &lt;platform|CPU|Memory&gt;]</dt>
<dd>
<p> Remove a policy. If domain is not supplied a default of platform is used.</dd></dl>
</dl>
<dt><i>power</i> <i>min</i> &lt;minimum&gt; <i>max</i> &lt;maximum&gt; [<i>domain</i> &lt;platform|CPU|Memory&gt;]</dt>
<dd>
<p> Configure Node Manager power minimum and maximum power draw limits. The <i>min</i> and <i>max</i> values must be in the range of 0-65535. If domain is not supplied a default of platform is used. </p>
</dd></dl>
</dl>
<dl>
<dl>
<dt><i>reset</i></dt>
<dd>
</dd><dl>
<dl>
<dt><i>comm</i> <i>policy_id</i> &lt;0-7&gt; [<i>domain</i> &lt;platform|CPU|Memory&gt;]</dt>
<dd>
<p> Reset Node Manager communication statistics. If domain is not supplied a default of platform is used. </p>
</dd><dt><i>global</dt>
<dd>
<p> Reset Node Manager global statistics. </p>
</dd><dt>memory</i> <i>policy_id</i> &lt;0-7&gt; [<i>domain</i> &lt;platform|CPU|Memory&gt;]</dt>
<dd>
<p> Reset Node Manager memory throttling statistics. If domain is not supplied a default of platform is used. </p>
</dd><dt><i>per_policy</i> <i>policy_id</i> &lt;0-7&gt; [<i>domain</i> &lt;platform|CPU|Memory&gt;]</dt>
<dd>
<p> Reset Node Manager per policy statistics. If domain is not supplied a default of platform is used. </p>
</dd><dt><i>requests</i> <i>policy_id</i> &lt;0-7&gt; [<i>domain</i> &lt;platform|CPU|Memory&gt;]</dt>
<dd>
<p> Reset Node Manager unhandled requests statistics. If domain is not supplied a default of platform is used. </p>
</dd><dt><i>response</i> <i>policy_id</i> &lt;0-7&gt; [<i>domain</i> &lt;platform|CPU|Memory&gt;]</dt>
<dd>
<p> Reset Node Manager response time statistics. If domain is not supplied a default of platform is used. </p>
</dd><dt><i>throttling</i> <i>policy_id</i> &lt;0-7&gt; [<i>domain</i> &lt;platform|CPU|Memory&gt;]</dt>
<dd>
<p> Reset Node Manager throttling statistics. If domain is not supplied a default of platform is used. </p>
</dd></dl>
</dl>
<dt><i>statistics</i></dt>
<dd>
</dd><dl>
<dl>
<dt><i>comm_fail</i></dt>
<dd>
<p> Report Node Manager communication failure statistics. </p>
</dd><dt><i>cpu_throttling</i></dt>
<dd>
<p> Report Node Manager cpu throttling statistics. </p>
</dd><dt><i>mem_throttling</i></dt>
<dd>
<p> Report Node Manager memory throttling statistics. </p>
</dd><dt><i>policy_power</i> <i>policy_id</i> &lt;0-7&gt; [<i>domain</i> &lt;platform|CPU|Memory&gt;]</dt>
<dd>
<p> Report Node Manager per policy power statistics (policy must be a power limit type policy). If domain is not supplied a default of platform is used. </p>
</dd><dt><i>policy_temps</i> <i>policy_id</i> &lt;0-7&gt; [<i>domain</i> &lt;platform|CPU|Memory&gt;]</dt>
<dd>
<p> Report Node Manager per policy temp statistics (policy must be an inlet temp limit policy). If domain is not supplied a default of platform is used. </p>
</dd><dt><i>policy_throt</i> <i>policy_id</i> &lt;0-7&gt; [<i>domain</i> &lt;platform|CPU|Memory&gt;]</dt>
<dd>
<p> Report Node Manager per policy throttling statistics. If domain is not supplied a default of platform is used. </p>
</dd><dt><i>requests</i></dt>
<dd>
<p> Report Node Manager unhandled requests statistics. </p>
</dd><dt><i>response</i></dt>
<dd>
<p> Report Node Manager response time statistics. </p>
</dd></dl>
</dl>
<dt><i>suspend</i></dt>
<dd>
</dd><dl>
<dl>
<dt><i>get</i> <i>policy_id</i> &lt;0-7&gt; [<i>domain</i> &lt;platform|CPU|Memory&gt;]</dt>
<dd>
<p> Get Node Manager policy suspend periods. If domain is not supplied a default of platform is used. </p>
</dd><dt><i>set</i> <i>policy_id</i> &lt;0-7&gt; [<i>domain</i> &lt;platform|CPU|Memory&gt;] &lt;start&gt; &lt;stop&gt; &lt;repeat&gt;</dt>
<dd>
<p> Set Node Manager policy suspend periods. If domain is not supplied a default of platform is used. The &lt;start&gt; and &lt;stop&gt; values must be in the range of 0-239, which is the number of minutes past midnight divided by 6. The &lt;repeat&gt; value is the daily recurrence pattern. Bit 0 is repeat every Monday, bit 1 is repeat every Tuesday, on through bit 6 for Sunday. </p>
</dd></dl>
</dl>
<dt><i>threshold</i></dt>
<dd>
</dd><dl>
<dl>
<dt><i>get</i> <i>policy_id</i> &lt;0-7&gt; [<i>domain</i> &lt;platform|CPU|Memory&gt;]</dt>
<dd>
<p> Get Node Manager policy Alert Threshold settings. If domain is not supplied a default of platform is used. </p>
</dd><dt><i>set</i> <i>policy_id</i> &lt;0-7&gt; [<i>domain</i> &lt;platform|CPU|Memory&gt;] <i>thresh_array</i></dt>
<dd>
<p> Set Node Manager policy Alert Threshold values. If domain is not supplied a default of platform is used. The <i>thresh_array</i> is 1, 2, or 3 integers that set three alert threshold settings. The setting type is a power or temperature value which must match the type of policy. </p>
</dd></dl>
</dl>
</dl>
</dl>
<dt><i>pef</i></dt>
<dd>
</dd><dl>
<dl>
<dt><i>info</i></dt>
<dd>
<p> This command will query the BMC and print information about the PEF supported features.</p>
</dd><dt><i>status</i></dt>
<dd>
<p> This command prints the current PEF status (the last SEL entry processed by the BMC, etc).</p>
</dd><dt><i>policy</i></dt>
<dd>
<p> This command lists the PEF policy table entries. Each policy entry describes an alert destination. A policy set is a collection of table entries. PEF alert actions reference policy sets.</p>
</dd><dt><i>list</i></dt>
<dd>
<p> This command lists the PEF table entries. Each PEF entry relates a sensor event to an action. When PEF is active, each platform event causes the BMC to scan this table for entries matching the event, and possible actions to be taken. Actions are performed in priority order (higher criticality first).</dd></dl>
</dl>
<dt><i>picmg</i> &lt;<code>properties</code>&gt;</dt>
<dd>
</dd><dl>
<dt>
</dt><dd>
<p> Run a PICMG/ATA extended command. Get PICMG properties may be used to obtain and print Extension major version information, PICMG identifier, FRU Device ID and Max FRU Device ID.</p>
</dd><dl>
<dt><i>addrinfo</i></dt>
<dd>
<p> Get address information. This command may return information on the Hardware address, IPMB-0 Address, FRU ID, Site/Entity ID, and Site/Entity Type.</p>
</dd><dt><i>frucontrol</i> &lt;<code>fru id</code>&gt; &lt;<code>options</code>&gt;</dt>
<dd>
<p> Set various control options:</p>
</dd><dl>
<dl>
<dt><i>0x00</i> &#8211; Cold Reset</dt>
<dd>
</dd><dt><i>0x01</i> &#8211; Warm Reset</dt>
<dd>
</dd><dt><i>0x02</i> &#8211; Graceful Reboot</dt>
<dd>
</dd><dt><i>0x03</i> &#8211; Issue Diagnostic Interrupt</dt>
<dd>
</dd><dt><i>0x04</i> &#8211; Quiesce [AMC only]</dt>
<dd>
</dd><dt><i>0x05-0xFF</i> &#8211; Cold Reset</dt>
<dd>
</dd></dl>
</dl>
<dt><i>activate</i> &lt;<code>fru id</code>&gt;</dt>
<dd>
<p> Activate the specified FRU.</p>
</dd><dt><i>deactivate</i> &lt;<code>fru id</code>&gt;</dt>
<dd>
<p> Deactivate the specified FRU.</p>
</dd><dt><i>policy</i> <i>get</i> &lt;<code>fru id</code>&gt;</dt>
<dd>
<p> Get FRU activation policy.</p>
</dd><dt><i>policy</i> <i>set</i> &lt;<code>fru id</code>&gt; &lt;<code>lockmask</code>&gt; &lt;<code>lock</code>&gt;</dt>
<dd>
<p> Set FRU activation policy. <code>lockmask</code> is 1 or 0 to indicate action on the deactivation or activation locked bit respectively. <code>lock</code> is 1 or 0 to set/clear locked bit.</p>
</dd><dt><i>portstate</i> <code>set</code>|<code>getall</code>|<code>getgranted</code>|<code>getdenied</code> &lt;<code>parameters</code>&gt;</dt>
<dd>
 Get or set various port states. See usage for parameter details.</dd></dl>
</dl>
<dt><i>power</i> &lt;<code>chassis power command</code>&gt;</dt>
<dd>
<p> Shortcut to the <i>chassis power</i> commands. See the <i>chassis power</i> commands for usage information.</p>
</dd><dt><i>raw</i> &lt;<code>netfn</code>&gt; &lt;<code>cmd</code>&gt; [&lt;<code>data</code>&gt;]</dt>
<dd>
<p> This will allow you to execute raw IPMI commands. For example to query the POH counter with a raw command: </p>
<p> &gt; ipmitool -v raw 0x0 0xf<br />
 RAW REQ (netfn=0x0 cmd=0xf data_len=0)<br />
 RAW RSP (5 bytes)<br />
 3c 72 0c 00 00 </p>
<p> <code>Note</code> that the OpenIPMI driver provided by the Linux kernel will reject the Get Message, Send Message and Read Event Message Buffer commands because it handles the message sequencing internally.</p>
</dd><dt><i>sdr</i></dt>
<dd>
</dd><dl>
<dl>
<dt><i>get</i> &lt;<code>id</code>&gt; &#8230; [&lt;<code>id</code>&gt;]</dt>
<dd>
<p> Prints information for sensor data records specified by sensor id.</p>
</dd><dt><i>info</i></dt>
<dd>
<p> This command will query the BMC for Sensor Data Record (SDR) Repository information.</p>
</dd><dt><i>type</i> [&lt;<code>sensor type</code>&gt;]</dt>
<dd>
<p> This command will display all records from the SDR Repository of a specific type. Run with type <i>list</i> (or simply with no type) to see the list of available types. For example to query for all Temperature sensors: </p>
<p> &gt; ipmitool sdr type Temperature<br />
 Baseboard Temp | 30h | ok | 7.1 | 28 degrees C<br />
 FntPnl Amb Temp | 32h | ok | 12.1 | 24 degrees C<br />
 Processor1 Temp | 98h | ok | 3.1 | 57 degrees C<br />
 Processor2 Temp | 99h | ok | 3.2 | 53 degrees C </p>
</dd><dt><i>list</i> | <i>elist</i> [&lt;<code>all</code>|<code>full</code>|<code>compact</code>|<code>event</code>|<code>mcloc</code>|<code>fru</code>|<code>generic</code>&gt;]</dt>
<dd>
<p> This command will read the Sensor Data Records (SDR) and extract sensor information of a given type, then query each sensor and print its name, reading, and status. If invoked as <i>elist</i> then it will also print sensor number, entity id and instance, and asserted discrete states. </p>
<p> The default output will only display <i>full</i> and <i>compact</i> sensor types, to see all sensors use the <i>all</i> type with this command.</p>
</dd><dl>
<dl>
<dt>Valid types are:</dt>
<dd>
</dd><dl>
<dl>
<dt><i>all</i></dt>
<dd>
<p> All SDR records (Sensor and Locator)</p>
</dd><dt><i>full</i></dt>
<dd>
<p> Full Sensor Record</p>
</dd><dt><i>compact</i></dt>
<dd>
<p> Compact Sensor Record</p>
</dd><dt><i>event</i></dt>
<dd>
<p> Event-Only Sensor Record</p>
</dd><dt><i>mcloc</i></dt>
<dd>
<p> Management Controller Locator Record</p>
</dd><dt><i>fru</i></dt>
<dd>
<p> FRU Locator Record</p>
</dd><dt><i>generic</i></dt>
<dd>
<p> Generic SDR records</dd></dl>
</dl>
</dl>
</dl>
<dt><i>entity</i> &lt;<code>id</code>&gt;[.&lt;<code>instance</code>&gt;]</dt>
<dd>
<p> Displays all sensors associated with an entity. Get a list of valid entity ids on the target system by issuing the <i>sdr elist</i> command. A list of all entity ids can be found in the IPMI specifications.</p>
</dd><dt><i>dump</i> &lt;<code>file</code>&gt;</dt>
<dd>
<p> Dumps raw SDR data to a file. This data file can then be used as a local SDR cache of the remote managed system with the <i>-S &lt;file&gt;</i> option on the ipmitool command line. This can greatly improve performance over system interface or remote LAN.</p>
</dd><dt><i>fill</i> <i>sensors</i></dt>
<dd>
<p> Create the SDR Repository for the current configuration. Will perform a &#8216;Clear SDR Repository&#8217; command so be careful.</p>
</dd><dt><i>fill</i> <i>file</i> &lt;<code>filename</code>&gt;</dt>
<dd>
<p> Fill the SDR Repository using records stored in a binary data file. Will perform a &#8216;Clear SDR Repository&#8217; command so be careful.</dd></dl>
</dl>
<dt><i>sel</i></dt>
<dd>
<p> NOTE: System Event Log (SEL) entry-times are displayed as `Pre-Init Time-stamp&#8217; if the SEL clock needs to be set. Ensure that the SEL clock is accurate by invoking the <i>sel time get</i> and <i>sel time set &lt;time string&gt;</i> commands.</p>
</dd><dl>
<dl>
<dt><i>info</i></dt>
<dd>
<p> This command will query the BMC for information about the System Event Log (SEL) and its contents.</p>
</dd><dt><i>clear</i></dt>
<dd>
<p> This command will clear the contents of the SEL. It cannot be undone so be careful.</p>
</dd><dt><i>list</i> | <i>elist</i></dt>
<dd>
<p> When this command is invoked without arguments, the entire contents of the System Event Log are displayed. If invoked as <i>elist</i> (extended list) it will also use the Sensor Data Record entries to display the sensor ID for the sensor that caused each event. <code>Note</code> this can take a long time over the system interface. </p>
</dd><dl>
<dl>
<dt>&lt;<code>count</code>&gt; | <i>first</i> &lt;<code>count</code>&gt;</dt>
<dd>
<p> Displays the first <i>count</i> (least-recent) entries in the SEL. If <i>count</i> is zero, all entries are displayed.</p>
</dd><dt><i>last</i> &lt;<code>count</code>&gt;</dt>
<dd>
<p> Displays the last <i>count</i> (most-recent) entries in the SEL. If <i>count</i> is zero, all entries are displayed.</dd></dl>
</dl>
<dt><i>delete</i> &lt;<code>SEL Record ID</code>&gt; &#8230; &lt;<code>SEL Record ID</code>&gt;</dt>
<dd>
<p> Delete one or more SEL event records.</p>
</dd><dt><i>add</i> &lt;<code>filename ID</code>&gt;</dt>
<dd>
<p> Read event entries from a file and add them to the SEL. New SEL entries area added onto the SEL after the last record in the SEL. Record added is of type 2 and is automatically timestamped.</p>
</dd><dt><i>get</i> &lt;<code>SEL Record ID</code>&gt;</dt>
<dd>
<p> Print information on the specified SEL Record entry.</p>
</dd><dt><i>save</i> &lt;<code>file</code>&gt;</dt>
<dd>
<p> Save SEL records to a text file that can be fed back into the <i>event file</i> ipmitool command. This can be useful for testing Event generation by building an appropriate Platform Event Message file based on existing events. Please see the available help for the &#8216;event file &#8230;&#8217; command for a description of the format of this file.</p>
</dd><dt><i>writeraw</i> &lt;<code>file</code>&gt;</dt>
<dd>
<p> Save SEL records to a file in raw, binary format. This file can be fed back to the <i>sel readraw</i> ipmitool command for viewing.</p>
</dd><dt><i>readraw</i> &lt;<code>file</code>&gt;</dt>
<dd>
<p> Read and display SEL records from a binary file. Such a file can be created using the <i>sel writeraw</i> ipmitool command.</p>
</dd><dt><i>time</i></dt>
<dd>
</dd><dl>
<dl>
<dt><i>get</i></dt>
<dd>
 Displays the SEL clock&#8217;s current time.</dd>
<dt><i>set</i> &lt;<code>time string</code>&gt;</dt>
<dd>
<p> Sets the SEL clock. Future SEL entries will use the time set by this command. &lt;<code>time string</code>&gt; is of the form &quot;MM/DD/YYYY HH:MM:SS&quot;. Note that hours are in 24-hour form. It is recommended that the SEL be cleared before setting the time.</dd></dl>
</dl>
</dl>
</dl>
<dt><i>sensor</i></dt>
<dd>
</dd><dl>
<dl>
<dt><i>list</i></dt>
<dd>
<p> Lists sensors and thresholds in a wide table format.</p>
</dd><dt><i>get</i> &lt;<code>id</code>&gt; &#8230; [&lt;<code>id</code>&gt;]</dt>
<dd>
<p> Prints information for sensors specified by name.</p>
</dd><dt><i>thresh</i> &lt;<code>id</code>&gt; &lt;<code>threshold</code>&gt; &lt;<code>setting</code>&gt;</dt>
<dd>
<p> This allows you to set a particular sensor threshold value. The sensor is specified by name.</p>
</dd><dl>
<dl>
<dt>Valid <i>thresholds</i> are:</dt>
<dd>
 <i>unr</i><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>Upper Non-Recoverable</dd>
<p> <i>ucr</i><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>Upper Critical</p>
<p> <i>unc</i><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>Upper Non-Critical</p>
<p> <i>lnc</i><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>Lower Non-Critical</p>
<p> <i>lcr</i><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>Lower Critical</p>
<p> <i>lnr</i><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>Lower Non-Recoverable
</dl>
</dl>
<dt><i>thresh</i> &lt;<code>id</code>&gt; <i>lower</i> &lt;<code>lnr</code>&gt; &lt;<code>lcr</code>&gt; &lt;<code>lnc</code>&gt;</dt>
<dd>
<p> This allows you to set all lower thresholds for a sensor at the same time. The sensor is specified by name and the thresholds are listed in order of Lower Non-Recoverable, Lower Critical, and Lower Non-Critical.</p>
</dd><dt><i>thresh</i> &lt;<code>id</code>&gt; <i>upper</i> &lt;<code>unc</code>&gt; &lt;<code>ucr</code>&gt; &lt;<code>unr</code>&gt;</dt>
<dd>
<p> This allows you to set all upper thresholds for a sensor at the same time. The sensor is specified by name and the thresholds are listed in order of Upper Non-Critical, Upper Critical, and Upper Non-Recoverable.</dd></dl>
</dl>
<dt><i>session</i></dt>
<dd>
</dd><dl>
<dl>
<dt><i>info</i> &lt;<code>active</code>|<code>all</code>|<code>id 0xnnnnnnnn</code>|<code>handle 0xnn</code>&gt;</dt>
<dd>
<p> Get information about the specified session(s). You may identify sessions by their id, by their handle number, by their active status, or by using the keyword `all&#8217; to specify all sessions.</dd></dl>
</dl>
<dt><i>set</i></dt>
<dd>
</dd><dl>
<dl>
<dt><i>hostname</i> &lt;<code>host</code>&gt;</dt>
<dd>
<p> Session hostname.</p>
</dd><dl>
</dl>
<dt><i>username</i> &lt;<code>user</code>&gt;</dt>
<dd>
<p> Session username.</p>
</dd><dl>
</dl>
<dt><i>password</i> &lt;<code>pass</code>&gt;</dt>
<dd>
<p> Session password.</p>
</dd><dl>
</dl>
<dt><i>privlvl</i> &lt;<code>level</code>&gt;</dt>
<dd>
<p> Session privilege level force.</p>
</dd><dl>
</dl>
<dt><i>authtype</i> &lt;<code>type</code>&gt;</dt>
<dd>
<p> Authentication type force.</p>
</dd><dl>
</dl>
<dt><i>localaddr</i> &lt;<code>addr</code>&gt;</dt>
<dd>
<p> Local IPMB address.</p>
</dd><dl>
</dl>
<dt><i>targetaddr</i> &lt;<code>addr</code>&gt;</dt>
<dd>
<p> Remote target IPMB address.</p>
</dd><dl>
</dl>
<dt><i>port</i> &lt;<code>port</code>&gt;</dt>
<dd>
<p> Remote RMCP port.</p>
</dd><dl>
</dl>
<dt><i>csv</i> [<code>level</code>]</dt>
<dd>
<p> Enable output in comma separated format. Affects following commands: <i>user</i>, <i>channel</i>, <i>isol</i>, <i>sunoem</i>, <i>sol</i>, <i>sensor</i>, <i>sdr</i>, <i>sel</i>, <i>session</i>.</p>
</dd><dl>
</dl>
<dt><i>verbose</i> [<code>verbose</code>]</dt>
<dd>
<p> Verbosity level.</p>
</dd><dl>
</dl>
</dl>
</dl>
<dt><i>shell</i></dt>
<dd>
</dd><dl>
<dt>
</dt><dd> This command will launch an interactive shell which you can use to send multiple ipmitool commands to a BMC and see the responses. This can be useful instead of running the full ipmitool command each time. Some commands will make use of a Sensor Data Record cache and you will see marked improvement in speed if these commands are able to reuse the same cache in a shell session. LAN sessions will send a periodic keepalive command to keep the IPMI session from timing out.</dd></dl>
<dt><i>sol</i></dt>
<dd>
</dd><dl>
<dl>
<dt><i>info</i> [&lt;<code>channel number</code>&gt;]</dt>
<dd>
<p> Retrieve information about the Serial-Over-LAN configuration on the specified channel. If no channel is given, it will display SOL configuration data for the currently used channel.</p>
</dd><dt><i>payload</i> &lt;<i>enable</i> | <i>disable</i> | <i>status</i>&gt; &lt;<code>channel number</code>&gt; &lt;<code>userid</code>&gt;</dt>
<dd>
<p> Enable, disable or show status of SOL payload for the user on the specified channel.</p>
</dd><dt><i>set</i> &lt;<code>parameter</code>&gt; &lt;<code>value</code>&gt; [&lt;<code>channel</code>&gt;]</dt>
<dd>
<p> Configure parameters for Serial Over Lan. If no channel is given, it will display SOL configuration data for the currently used channel. Configuration parameter updates are automatically guarded with the updates to the set-in-progress parameter.</p>
</dd><dl>
<dl>
<dt>Valid parameters and values are:</dt>
<dd>
</dd><dt><i>set-in-progress</i></dt>
<dd> set-complete set-in-progress commit-write</dd>
<dt><i>enabled</i></dt>
<dd> true false</dd>
<dt><i>force-encryption</i></dt>
<dd> true false</dd>
<dt><i>force-authentication</i></dt>
<dd> true false</dd>
<dt><i>privilege-level</i></dt>
<dd> user operator admin oem</dd>
<dt><i>character-accumulate-level</i></dt>
<dd> Decimal number given in 5 milliseconds increments</dd>
<dt><i>character-send-threshold</i></dt>
<dd> Decimal number</dd>
<dt><i>retry-count</i></dt>
<dd> Decimal number. 0 indicates no retries after packet is transmitted.</dd>
<dt><i>retry-interval</i></dt>
<dd> Decimal number in 10 millisecond increments. 0 indicates that retries should be sent back to back.</dd>
<dt><i>non-volatile-bit-rate</i></dt>
<dd> serial, 19.2, 38.4, 57.6, 115.2. Setting this value to serial indicates that the BMC should use the setting used by the IPMI over serial channel.</dd>
<dt><i>volatile-bit-rate</i></dt>
<dd> serial, 19.2, 38.4, 57.6, 115.2. Setting this value to serial indicates that the BMC should use the setting used by the IPMI over serial channel.</dd></dl>
</dl>
<dt><i>activate</i> [<i>usesolkeepalive</i> | <i>nokeepalive</i>] [<i>instance=&lt;number&gt;</i>]</dt>
<dd>
<p> Causes ipmitool to enter Serial Over LAN mode, and is only available when using the lanplus interface. An RMCP+ connection is made to the BMC, the terminal is set to raw mode, and user input is sent to the serial console on the remote server. On exit, the the SOL payload mode is deactivated and the terminal is reset to its original settings. </p>
<p> If the instance is given, it will activate using the given instance number. The default is 1.</p>
</dd><dl>
<dt>
</dt><dd>
<p> Special escape sequences are provided to control the SOL session:</p>
</dd><dl>
<dl>
<dt><i>~.</i><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>Terminate connection</dt>
<dd>
</dd><dt><i>~^Z</i><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>Suspend ipmitool</dt>
<dd>
</dd><dt><i>~^X</i><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>Suspend ipmitool, but don&#8217;t restore tty on restart</dt>
<dd>
</dd><dt><i>~B</i><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>Send break</dt>
<dd>
</dd><dt><i>~~</i><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>Send the escape character by typing it twice</dt>
<dd>
</dd><dt><i>~?</i><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>Print the supported escape sequences</dt>
<dd></dd></dl>
</dl>
<p> Note that escapes are only recognized immediately after newline.</dl>
<dt><i>deactivate</i> [<i>instance=&lt;number&gt;</i>]</dt>
<dd>
<p> Deactivates Serial Over LAN mode on the BMC. Exiting Serial Over LAN mode should automatically cause this command to be sent to the BMC, but in the case of an unintentional exit from SOL mode, this command may be necessary to reset the state of the BMC. </p>
<p> If the instance is given, it will deactivate the given instance number. The default is 1.</dd></dl>
</dl>
<dt><i>spd</i> &lt;<code>i2cbus</code>&gt; &lt;<code>i2caddr</code>&gt; [&lt;<code>channel</code>&gt;] [&lt;axread&gt;]</dt>
<dd>
<p> This command may be used to read SPD (Serial Presence Detect) data using the I2C Master Write-Read IPMI command. </p>
</dd><dt><i>sunoem</i></dt>
<dd>
</dd><dl>
<dl>
<dt><i>cli</i> [&lt;<code>command string</code>&gt; &#8230;]</dt>
<dd>
<p> Execute the service processor command line interface commands. Without any command string, an interactive session is started in the service processor command line environment. If a command string is specified, the command string is executed on the service processor and the connection is closed.</p>
</dd><dt><i>led</i></dt>
<dd>
</dd><dl>
<dt>
</dt><dd>
<p> These commands provide a way to get and set the status of LEDs on a Sun Microsystems server. Use &#8216;sdr list generic&#8217; to get a list of devices that are controllable LEDs. The <i>ledtype</i> parameter is optional and not necessary to provide on the command line unless it is required by hardware.</p>
</dd><dl>
<dt><i>get</i> &lt;<code>sensorid</code>&gt; [&lt;<code>ledtype</code>&gt;]</dt>
<dd>
<p> Get status of a particular LED described by a Generic Device Locator record in the SDR. A sensorid of <i>all</i> will get the status of all available LEDS.</p>
</dd><dt><i>set</i> &lt;<code>sensorid</code>&gt; &lt;<code>ledmode</code>&gt; [&lt;<code>ledtype</code>&gt;]</dt>
<dd>
<p> Set status of a particular LED described by a Generic Device Locator record in the SDR. A sensorid of <i>all</i> will set the status of all available LEDS to the specified <i>ledmode</i> and <i>ledtype</i>.</p>
</dd><dt>LED Mode is required for set operations:</dt>
<dd>
 <i>OFF</i> Off<br />
 <i>ON</i> Steady On<br />
 <i>STANDBY</i> 100ms on 2900ms off blink rate<br />
 <i>SLOW</i> 1HZ blink rate<br />
 <i>FAST</i> 4HZ blink rate</dd>
<dt>LED Type is optional:</dt>
<dd>
 <i>OK2RM</i> Ok to Remove<br />
 <i>SERVICE</i> Service Required<br />
 <i>ACT</i> Activity<br />
 <i>LOCATE</i> Locate </dd>
</dl>
</dl>
<dt><i>nacname</i> &lt;<code>ipmi name</code>&gt;</dt>
<dd>
<p> Return the full NAC name of a target identified by ipmi name.</p>
</dd><dt><i>ping</i> &lt;<code>count</code>&gt; [&lt;<code>q</code>&gt;]</dt>
<dd>
<p> Send and receive count packets. Each packet is 64 bytes. </p>
<p> q &#8211; Quiet. Displays output only at the start and end of the process.</p>
</dd><dt><i>getval</i> &lt;<code>property name</code>&gt;</dt>
<dd>
<p> Returns value of specified ILOM property.</p>
</dd><dt><i>setval</i> &lt;<code>property name</code>&gt; &lt;<code>property value</code>&gt; [&lt;<code>timeout</code>&gt;]</dt>
<dd>
<p> Sets value of ILOM property. If timeout is not specified, the default value is 5 seconds. NOTE: setval must be executed locally on host!</p>
</dd><dt><i>sshkey</i></dt>
<dd>
</dd><dl>
<dl>
<dt><i>set</i> &lt;<code>userid</code>&gt; &lt;<code>keyfile</code>&gt;</dt>
<dd>
<p> This command will allow you to specify an SSH key to use for a particular user on the Service Processor. This key will be used for CLI logins to the SP and not for IPMI sessions. View available users and their userids with the &#8216;user list&#8217; command.</p>
</dd><dt><i>del</i> &lt;<code>userid</code>&gt;</dt>
<dd>
<p> This command will delete the SSH key for a specified userid.</dd></dl>
</dl>
<dt><i>version</i></dt>
<dd>
<p> Display the version of ILOM firmware.</p>
</dd><dt><i>getfile</i> &lt;<code>file identifier</code>&gt; &lt;<code>destination file name</code>&gt;</dt>
<dd>
<p> This command will return various files from service processor and store them in specified destination file. Note that some files may not be present or be supported by your SP. </p>
</dd><dl>
<dt>
</dt><dd> File identifiers:</dd>
<dl>
<dt>
</dt><dd>
 <i>SSH_PUBKEYS</i><br />
 <i>DIAG_PASSED</i><br />
 <i>DIAG_FAILED</i><br />
 <i>DIAG_END_TIME</i><br />
 <i>DIAG_INVENTORY</i><br />
 <i>DIAG_TEST_LOG</i><br />
 <i>DIAG_START_TIME</i><br />
 <i>DIAG_UEFI_LOG</i><br />
 <i>DIAG_TEST_LOG</i><br />
 <i>DIAG_LAST_LOG</i><br />
 <i>DIAG_LAST_CMD</i></dd></dl>
</dl>
<dt><i>getbehavior</i> &lt;<code>feature identifier</code>&gt;</dt>
<dd>
<p> This command will test if various ILOM features are enabled. </p>
</dd><dl>
<dt>
</dt><dd> Feature identifiers:</dd>
<dl>
<dt>
</dt><dd>
 <i>SUPPORTS_SIGNED_PACKAGES</i><br />
 <i>REQUIRES_SIGNED_PACKAGES</i></dd></dl>
</dl>
</dl>
</dl>
<dt><i>tsol</i></dt>
<dd>
</dd><dl>
<dt>
</dt><dd>
<p> This command allows Serial-over-LAN sessions to be established with Tyan IPMIv1.5 SMDC such as the M3289 or M3290. The default command run with no arguments will establish default SOL session back to local IP address. Optional arguments may be supplied in any order. </p>
</dd><dl>
<dt><i>&lt;ipaddr&gt;</i></dt>
<dd>
<p> Send receiver IP address to SMDC which it will use to send serial traffic to. By default this detects the local IP address and establishes two-way session. Format of ipaddr is XX.XX.XX.XX </p>
</dd><dt><i>port=NUM</i></dt>
<dd>
<p> Configure UDP port to receive serial traffic on. By default this is 6230. </p>
</dd><dt><i>ro|rw</i></dt>
<dd>
<p> Confiure SOL session as read-only or read-write. Sessions are read-write by default. </p>
</dd></dl>
</dl>
<dt><i>user</i></dt>
<dd>
</dd><dl>
<dl>
<dt><i>summary</i></dt>
<dd>
<p> Displays a summary of userid information, including maximum number of userids, the number of enabled users, and the number of fixed names defined.</p>
</dd><dt><i>list</i></dt>
<dd>
<p> Displays a list of user information for all defined userids.</p>
</dd><dt><i>set</i></dt>
<dd>
</dd><dl>
<dl>
<dt><i>name</i> &lt;<code>userid</code>&gt; &lt;<code>username</code>&gt;</dt>
<dd>
<p> Sets the username associated with the given userid.</p>
</dd><dt><i>password</i> &lt;<code>userid</code>&gt; [&lt;<code>password</code>&gt;]</dt>
<dd>
<p> Sets the password for the given userid. If no password is given, the password is cleared (set to the NULL password). Be careful when removing passwords from administrator-level accounts.</dd></dl>
</dl>
<dt><i>disable</i> &lt;<code>userid</code>&gt;</dt>
<dd>
<p> Disables access to the BMC by the given userid.</p>
</dd><dt><i>enable</i> &lt;<code>userid</code>&gt;</dt>
<dd>
<p> Enables access to the BMC by the given userid.</p>
</dd><dt><i>priv</i> &lt;<code>userid</code>&gt; &lt;<code>privilege level</code>&gt; [&lt;<code>channel number</code>&gt;]</dt>
<dd>
<p> Set user privilege level on the specified channel. If the channel is not specified, the current channel will be used.</p>
</dd><dt><i>test</i> &lt;<code>userid</code>&gt; &lt;<code>16</code>|<code>20</code>&gt; [&lt;<code>password</code>&gt;]</dt>
<dd>
<p> Determine whether a password has been stored as 16 or 20 bytes.</dd></dl>
</dl>
</dl>
<h2>OPEN INTERFACE</h2>
<p> The ipmitool <i>open</i> interface utilizes the OpenIPMI kernel device driver. This driver is present in all modern 2.4 and all 2.6 kernels and it should be present in recent Linux distribution kernels. There are also IPMI driver kernel patches for different kernel versions available from the OpenIPMI homepage. </p>
<p> The required kernel modules is different for 2.4 and 2.6 kernels. The following kernel modules must be loaded on a 2.4-based kernel in order for ipmitool to work:</p>
<dl>
<dt><code>ipmi_msghandler</code></dt>
<dd> Incoming and outgoing message handler for IPMI interfaces.</dd>
<dt><code>ipmi_kcs_drv</code></dt>
<dd> An IPMI Keyboard Controller Style (KCS) interface driver for the message handler.</dd>
<dt><code>ipmi_devintf</code></dt>
<dd> Linux character device interface for the message handler.</dd></dl>
<p> The following kernel modules must be loaded on a 2.6-based kernel in order for ipmitool to work:</p>
<dl>
<dt><code>ipmi_msghandler</code></dt>
<dd> Incoming and outgoing message handler for IPMI interfaces.</dd>
<dt><code>ipmi_si</code></dt>
<dd> An IPMI system interface driver for the message handler. This module supports various IPMI system interfaces such as KCS, BT, SMIC, and even SMBus in 2.6 kernels.</dd>
<dt><code>ipmi_devintf</code></dt>
<dd> Linux character device interface for the message handler.</dd></dl>
<p> Once the required modules are loaded there will be a dynamic character device entry that must exist at <code>/dev/ipmi0</code>. For systems that use devfs or udev this will appear at <code>/dev/ipmi/0</code>. </p>
<p> To create the device node first determine what dynamic major number it was assigned by the kernel by looking in <code>/proc/devices</code> and checking for the <i>ipmidev</i> entry. Usually if this is the first dynamic device it will be major number <code>254</code> and the minor number for the first system interface is <code>0</code> so you would create the device entry with: </p>
<p> <i>mknod /dev/ipmi0 c 254 0</i> </p>
<p> ipmitool includes some sample initialization scripts that can perform this task automatically at start-up. </p>
<p> In order to have ipmitool use the OpenIPMI device interface you can specify it on the command line: </p>
<p> ipmitool <code>-I</code> <i>open</i> &lt;<i>command</i>&gt;</p>
<h2>BMC INTERFACE</h2>
<p> The ipmitool bmc interface utilizes the <i>bmc</i> device driver as provided by Solaris 10 and higher. In order to force ipmitool to make use of this interface you can specify it on the command line: </p>
<p> ipmitool <code>-I</code> <i>bmc</i> &lt;<i>command</i>&gt; </p>
<p> The following files are associated with the bmc driver: </p>
<dl>
<dt><code>/platform/i86pc/kernel/drv/bmc</code></dt>
<dd> 32-bit <code>ELF</code> kernel module for the bmc driver.</dd>
<dt><code>/platform/i86pc/kernel/drv/amd64/bmc</code></dt>
<dd> 64-bit <code>ELF</code> kernel module for the bmc driver.</dd>
<dt><code>/dev/bmc</code></dt>
<dd> Character device node used to communicate with the bmc driver.</dd></dl>
<h2>LIPMI INTERFACE</h2>
<p> The ipmitool <i>lipmi</i> interface uses the Solaris 9 IPMI kernel device driver. It has been superceeded by the <i>bmc</i> interface on Solaris 10. You can tell ipmitool to use this interface by specifying it on the command line. </p>
<p> ipmitool <code>-I</code> <i>lipmi</i> &lt;<i>expression</i>&gt;</p>
<h2>LAN INTERFACE</h2>
<p> The ipmitool <i>lan</i> interface communicates with the BMC over an Ethernet LAN connection using UDP under IPv4. UDP datagrams are formatted to contain IPMI request/response messages with a IPMI session headers and RMCP headers. </p>
<p> IPMI-over-LAN uses version 1 of the Remote Management Control Protocol (RMCP) to support pre-OS and OS-absent management. RMCP is a request-response protocol delivered using UDP datagrams to port 623. </p>
<p> The LAN interface is an authentication multi-session connection; messages delivered to the BMC can (and should) be authenticated with a challenge/response protocol with either straight password/key or MD5 message-digest algorithm. ipmitool will attempt to connect with administrator privilege level as this is required to perform chassis power functions. </p>
<p> You can tell ipmitool to use the lan interface with the <code>-I</code> <i>lan</i> option: </p>
<p> ipmitool <code>-I</code> <i>lan</i> <code>-H</code> &lt;<i>hostname</i>&gt; [<code>-U</code> &lt;<i>username</i>&gt;] [<code>-P</code> &lt;<i>password</i>&gt;] &lt;<i>command</i>&gt; </p>
<p> A hostname must be given on the command line in order to use the lan interface with ipmitool. The password field is optional; if you do not provide a password on the command line, ipmitool will attempt to connect without authentication. If you specify a password it will use MD5 authentication if supported by the BMC and straight password/key otherwise, unless overridden with a command line option.</p>
<h2>LANPLUS INTERFACE</h2>
<p> Like the <i>lan</i> interface, the <i>lanplus</i> interface communicates with the BMC over an Ethernet LAN connection using UDP under IPv4. The difference is that the <i>lanplus</i> interface uses the RMCP+ protocol as described in the IPMI v2.0 specification. RMCP+ allows for improved authentication and data integrity checks, as well as encryption and the ability to carry multiple types of payloads. Generic Serial Over LAN support requires RMCP+, so the ipmitool <i>sol activate</i> command requires the use of the <i>lanplus</i> interface. </p>
<p> RMCP+ session establishment uses a symmetric challenge-response protocol called RAKP (<code>Remote Authenticated Key-Exchange Protocol</code>) which allows the negotiation of many options. ipmitool does not yet allow the user to specify the value of every option, defaulting to the most obvious settings marked as required in the v2.0 specification. Authentication and integrity HMACS are produced with SHA1, and encryption is performed with AES-CBC-128. Role-level logins are not yet supported. </p>
<p> ipmitool must be linked with the <i>OpenSSL</i> library in order to perform the encryption functions and support the <i>lanplus</i> interface. If the required packages are not found it will not be compiled in and supported. </p>
<p> You can tell ipmitool to use the lanplus interface with the <code>-I</code> <i>lanplus</i> option: </p>
<p> ipmitool <code>-I</code> <i>lanplus</i> <code>-H</code> &lt;<i>hostname</i>&gt; [<code>-U</code> &lt;<i>username</i>&gt;] [<code>-P</code> &lt;<i>password</i>&gt;] &lt;<i>command</i>&gt; </p>
<p> A hostname must be given on the command line in order to use the lan interface with ipmitool. With the exception of the <code>-A</code> and <code>-C</code> options the rest of the command line options are identical to those available for the <i>lan</i> interface. </p>
<p> The <code>-C</code> option allows you specify the authentication, integrity, and encryption algorithms to use for for <i>lanplus</i> session based on the cipher suite ID found in the IPMIv2.0 specification in table 22-19. The default cipher suite is <i>3</i> which specifies RAKP-HMAC-SHA1 authentication, HMAC-SHA1-96 integrity, and AES-CBC-128 encryption algorightms. </p>
<h2>FREE INTERFACE</h2>
<p> The ipmitool <i>free</i> interface utilizes the FreeIPMI libfreeipmi drivers. </p>
<p> You can tell ipmitool to use the FreeIPMI interface with the -I option: </p>
<p> ipmitool <code>-I</code> <i>free</i> &lt;<i>command</i>&gt; </p>
<h2>IMB INTERFACE</h2>
<p> The ipmitool <i>imb</i> interface supports the Intel IMB (Intel Inter-module Bus) Interface through the /dev/imb device. </p>
<p> You can tell ipmitool to use the IMB interface with the -I option: </p>
<p> ipmitool <code>-I</code> <i>imb</i> &lt;<i>command</i>&gt; </p>
<h2>EXAMPLES</h2>
<dl>
<dt><i>Example 1</i>: Listing remote sensors</dt>
<dd>
<p> &gt; ipmitool -I lan -H 1.2.3.4 -f passfile sdr list<br />
 Baseboard 1.25V | 1.24 Volts | ok<br />
 Baseboard 2.5V | 2.49 Volts | ok<br />
 Baseboard 3.3V | 3.32 Volts | ok</p>
</dd><dt><i>Example 2</i>: Displaying status of a remote sensor</dt>
<dd>
<p> &gt; ipmitool -I lan -H 1.2.3.4 -f passfile sensor get &quot;Baseboard 1.25V&quot;<br />
 Locating sensor record&#8230;<br />
 Sensor ID : Baseboard 1.25V (0x10)<br />
 Sensor Type (Analog) : Voltage<br />
 Sensor Reading : 1.245 (+/- 0.039) Volts<br />
 Status : ok<br />
 Lower Non-Recoverable : na<br />
 Lower Critical : 1.078<br />
 Lower Non-Critical : 1.107<br />
 Upper Non-Critical : 1.382<br />
 Upper Critical : 1.431<br />
 Upper Non-Recoverable : na</p>
</dd><dt><i>Example 3</i>: Displaying the power status of a remote chassis</dt>
<dd>
<p> &gt; ipmitool -I lan -H 1.2.3.4 -f passfile chassis power status<br />
 Chassis Power is on</p>
</dd><dt><i>Example 4</i>: Controlling the power on a remote chassis</dt>
<dd>
<p> &gt; ipmitool -I lan -H 1.2.3.4 -f passfile chassis power on<br />
 Chassis Power Control: Up/On <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>
</dd></dl>
<h2>AUTHOR</h2>
<p> Duncan Laurie &lt;duncan [at] iceblink.org&gt;</p>
<h2>SEE ALSO</h2>
<dl>
<dt>IPMItool Homepage</dt>
<dd> <a rel="nofollow" href="http://ipmitool.sourceforge.net">http://ipmitool.sourceforge.net</a></dd>
<dt>Intelligent Platform Management Interface Specification</dt>
<dd> <a rel="nofollow" href="http://www.intel.com/design/servers/ipmi">http://www.intel.com/design/servers/ipmi</a></dd>
<dt>OpenIPMI Homepage</dt>
<dd> <a rel="nofollow" href="http://openipmi.sourceforge.net">http://openipmi.sourceforge.net</a></dd>
<dt>FreeIPMI Homepage</dt>
<dd> <a rel="nofollow" href="http://www.gnu.org/software/freeipmi/">http://www.gnu.org/software/freeipmi/</a> </dd>
</dl>
