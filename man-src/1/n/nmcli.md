---
title: "nmcli(1)"
name: "nmcli"
section: "1"
letter: "n"
url: "/docs/linux/man/1-nmcli/"
description: "nmcli – command-line tool for controlling NetworkManager"
---

<h2 class="name">NAME</h2>
<p> nmcli &#8211; command-line tool for controlling NetworkManager </p>
<h2>SYNOPSIS</h2>
<dl>
<dt> <code>nmcli</code> [<i>OPTIONS</i>&#8230;] {<code>help</code> | <code>general</code> | <code>networking</code> | <code>radio</code> | <code>connection</code> | <code>device</code> | <code>agent</code> | <code>monitor</code>} [<i>COMMAND</i>] [<i>ARGUMENTS</i>&#8230;]</dl>
<h2>DESCRIPTION</h2>
<p> <code>nmcli</code></p>
<dd>is a command-line tool for controlling NetworkManager and reporting network status. It can be utilized as a replacement for <code>nm-applet</code> or other graphical clients. <code>nmcli</code> is used to create, display, edit, delete, activate, and deactivate network connections, as well as control and display network device status. See <code><a href="/docs/linux/man/7-nmcli-examples/">nmcli-examples</a></code>(7) for ready to run nmcli examples. </p>
<p> Typical uses include: </p>
<dl>
<dt>
<dd> &bull; Scripts: Utilize NetworkManager via <code>nmcli</code> instead of managing network connections manually. <code>nmcli</code> supports a terse output format which is better suited for script processing. Note that NetworkManager can also execute scripts, called &quot;dispatcher scripts&quot;, in response to network events. See <code><a href="/docs/linux/man/8-networkmanager/">NetworkManager</a></code>(8) for details about these dispatcher scripts.</dl>
<dl>
<dt>
<dd> &bull; Servers, headless machines, and terminals: <code>nmcli</code> can be used to control NetworkManager without a GUI, including creating, editing, starting and stopping network connections and viewing network status.</dl>
<h2>OPTIONS</h2>
<p> <code>-a</code> | <code>&#8211;ask</code></p>
<dl>
<dt>
<dd> When using this option <code>nmcli</code> will stop and ask for any missing required arguments, so do not use this option for non-interactive purposes like scripts. This option controls, for example, whether you will be prompted for a password if it is required for connecting to a network.</dl>
<p> <code>-c</code> | <code>&#8211;colors</code> {yes | no | auto}</p>
<dl>
<dt>
<dd> This option controls color output (using terminal escape sequences). yes enables colors, no disables them, auto only produces colors when standard output is directed to a terminal. The default value is auto. </p>
<p> The actual colors used are configured as described in <code><a href="/docs/linux/man/5-terminal-colors-d/">terminal-colors.d</a></code>(5). Please refer to the COLORS section for a list of color names supported by <code>nmcli</code>. </p>
<p> If the environment variable NO_COLOR is set (to any value), then coloring is disabled with mode &quot;auto&quot;. Explicitly enabling coloring overrides the environment variable.</dl>
<p> <code>&#8211;complete-args</code></p>
<dl>
<dt>
<dd> Instead of conducting the desired action, <code>nmcli</code> will list possible completions for the last argument. This is useful to implement argument completion in shell. </p>
<p> The exit status will indicate success or return a code 65 to indicate the last argument is a file name. </p>
<p> NetworkManager ships with command completion support for GNU Bash.</dl>
<p> <code>-e</code> | <code>&#8211;escape</code> {yes | no}</p>
<dl>
<dt>
<dd> Whether to escape : and \ characters in terse tabular mode. The escape character is \. </p>
<p> If omitted, default is yes.</dl>
<p> <code>-f</code> | <code>&#8211;fields</code> {<i>field1</i>,<i>field2</i>&#8230; | all | common}</p>
<dl>
<dt>
<dd> This option is used to specify what fields (column names) should be printed. Valid field names differ for specific commands. List available fields by providing an invalid value to the <code>&#8211;fields</code> option. all is used to print all valid field values of the command. common is used to print common field values of the command. </p>
<p> If omitted, default is common.</dl>
<p> <code>-g</code> | <code>&#8211;get-values</code> {<i>field1</i>,<i>field2</i>&#8230; | all | common}</p>
<dl>
<dt>
<dd> This option is used to print values from specific fields. It is basically a shortcut for &#8211;mode tabular &#8211;terse &#8211;fields and is a convenient way to retrieve values for particular fields. The values are printed one per line without headers. </p>
<p> If a section is specified instead of a field, the section name will be printed followed by colon separated values of the fields belonging to that section, all on the same line.</dl>
<p> <code>-h</code> | <code>&#8211;help</code></p>
<dl>
<dt>
<dd> Print help information.</dl>
<p> <code>-m</code> | <code>&#8211;mode</code> {tabular | multiline}</p>
<dl>
<dt>
<dd> Switch between tabular and multiline output: </p>
<p> tabular</p>
<dl>
<dt>
<dd> Output is a table where each line describes a single entry. Columns define particular properties of the entry.</dl>
<p> multiline</p>
<dl>
<dt>
<dd> Each entry comprises multiple lines, each property on its own line. The values are prefixed with the property name.</dl>
<p> If omitted, default is tabular for most commands. For the commands producing more structured information, that cannot be displayed on a single line, default is multiline. Currently, they are: </p>
<dl>
<dt>
<dd> &bull; nmcli connection show <i>ID</i></dl>
<dl>
<dt>
<dd> &bull; nmcli device show</dl>
</dl>
<p> <code>-p</code> | <code>&#8211;pretty</code></p>
<dl>
<dt>
<dd> Output is pretty. This causes <code>nmcli</code> to produce easily readable outputs for humans, i.e. values are aligned, headers are printed, etc.</dl>
<p> <code>-s</code> | <code>&#8211;show-secrets</code></p>
<dl>
<dt>
<dd> When using this option <code>nmcli</code> will display passwords and secrets that might be present in an output of an operation. This option also influences echoing passwords typed by user as an input.</dl>
<p> <code>-t</code> | <code>&#8211;terse</code></p>
<dl>
<dt>
<dd> Output is terse. This mode is designed and suitable for computer (script) processing.</dl>
<p> <code>-v</code> | <code>&#8211;version</code></p>
<dl>
<dt>
<dd> Show <code>nmcli</code> version.</dl>
<p> <code>-w</code> | <code>&#8211;wait</code> <i>seconds</i></p>
<dl>
<dt>
<dd> This option sets a timeout period for which <code>nmcli</code> will wait for NetworkManager to finish operations. It is especially useful for commands that may take a longer time to complete, e.g. connection activation. </p>
<p> Specifying a value of 0 instructs <code>nmcli</code> not to wait but to exit immediately with a status of success. The default value depends on the executed command.</dl>
<h2>GENERAL COMMANDS</h2>
<dl>
<dt> <code>nmcli general</code> {<code>status</code> | <code>hostname</code> | <code>permissions</code> | <code>logging</code> | <code>reload</code>} [<i>ARGUMENTS</i>&#8230;]</dl>
<dd>Use this command to show NetworkManager status and permissions. You can also get and change system hostname, as well as NetworkManager logging level and domains. </p>
<p> <code>status</code></p>
<dl>
<dt>
<dd> Show overall status of NetworkManager. This is the default action, when no additional command is provided for <code>nmcli general</code>.</dl>
<p> <code>hostname</code> [<i>hostname</i>]</p>
<dl>
<dt>
<dd> Get and change system hostname. With no arguments, this prints currently configured hostname. When you pass a hostname, it will be handed over to NetworkManager to be set as a new system hostname. </p>
<p> Note that the term &quot;system&quot; hostname may also be referred to as &quot;persistent&quot; or &quot;static&quot; by other programs or tools. The hostname is stored in /etc/hostname file in most distributions. For example, systemd-hostnamed service uses the term &quot;static&quot; hostname and it only reads the /etc/hostname file when it starts.</dl>
<p> <code>permissions</code></p>
<dl>
<dt>
<dd> Show the permissions a caller has for various authenticated operations that NetworkManager provides, like enable and disable networking, changing Wi-Fi and WWAN state, modifying connections, etc.</dl>
<p> <code>logging</code> [<code>level</code>&nbsp;<i>level</i>] [<code>domains</code>&nbsp;<i>domains</i>&#8230;]</p>
<dl>
<dt>
<dd> Get and change NetworkManager logging level and domains. Without any argument current logging level and domains are shown. In order to change logging state, provide <code>level</code> and, or, <code>domain</code> parameters. See <code><a href="/docs/linux/man/5-networkmanager-conf/">NetworkManager.conf</a></code>(5) for available level and domain values.</dl>
<p> <code>reload</code> [<i>flags</i>&#8230;]</p>
<dl>
<dt>
<dd> Reload NetworkManager&#8217;s configuration and perform certain updates, like flushing caches or rewriting external state to disk. This is similar to sending SIGHUP to NetworkManager but it allows for more fine-grained control over what to reload through the flags argument. It also allows non-root access via PolicyKit and contrary to signals it is synchronous. Available flags are: </p>
<p> <code>conf</code></p>
<dl>
<dt>
<dd> Reload the NetworkManager.conf configuration from disk. Note that this does not include connections, which can be reloaded through <code>nmcli connection reload</code> instead.</dl>
<p> <code>dns-rc</code></p>
<dl>
<dt>
<dd> Update DNS configuration, which usually involves writing /etc/resolv.conf anew. This is equivalent to sending the SIGUSR1 signal to the NetworkManager process.</dl>
<p> <code>dns-full</code></p>
<dl>
<dt>
<dd> Restart the DNS plugin. This is for example useful when using dnsmasq plugin, which uses additional configuration in /etc/NetworkManager/dnsmasq.d. If you edit those files, you can restart the DNS plugin. This action shortly interrupts name resolution.</dl>
<p> With no flags, everything that is supported is reloaded, which is identical to sending a SIGHUP. See <code><a href="/docs/linux/man/8-networkmanager/">NetworkManager</a></code>(8) for more details about signals.</dl>
<h2>NETWORKING CONTROL COMMANDS</h2>
<dl>
<dt> <code>nmcli networking</code> {<code>on</code> | <code>off</code> | <code>connectivity</code>} [<i>ARGUMENTS</i>&#8230;]</dl>
<dd>Query NetworkManager networking status, enable and disable networking. </p>
<p> <code>on</code>, <code>off</code></p>
<dl>
<dt>
<dd> Enable or disable networking control by NetworkManager. All interfaces managed by NetworkManager are deactivated when networking is disabled.</dl>
<p> <code>connectivity</code> [check]</p>
<dl>
<dt>
<dd> Get network connectivity state. The optional <code>check</code> argument tells NetworkManager to re-check the connectivity, else the most recent known connectivity state is displayed without re-checking. </p>
<p> Possible states are: </p>
<p> none</p>
<dl>
<dt>
<dd> the host is not connected to any network.</dl>
<p> portal</p>
<dl>
<dt>
<dd> the host is behind a captive portal and cannot reach the full Internet.</dl>
<p> limited</p>
<dl>
<dt>
<dd> the host is connected to a network, but it has no access to the Internet.</dl>
<p> full</p>
<dl>
<dt>
<dd> the host is connected to a network and has full access to the Internet.</dl>
<p> unknown</p>
<dl>
<dt>
<dd> the connectivity status cannot be found out.</dl>
</dl>
<h2>RADIO TRANSMISSION CONTROL COMMANDS</h2>
<dl>
<dt> <code>nmcli radio</code> {<code>all</code> | <code>wifi</code> | <code>wwan</code>} [<i>ARGUMENTS</i>&#8230;]</dl>
<dd>Show radio switches status, or enable and disable the switches. </p>
<p> <code>wifi</code> [on | off]</p>
<dl>
<dt>
<dd> Show or set status of Wi-Fi in NetworkManager. If no arguments are supplied, Wi-Fi status is printed; <code>on</code> enables Wi-Fi; <code>off</code> disables Wi-Fi.</dl>
<p> <code>wwan</code> [on | off]</p>
<dl>
<dt>
<dd> Show or set status of WWAN (mobile broadband) in NetworkManager. If no arguments are supplied, mobile broadband status is printed; <code>on</code> enables mobile broadband, <code>off</code> disables it.</dl>
<p> <code>all</code> [on | off]</p>
<dl>
<dt>
<dd> Show or set all previously mentioned radio switches at the same time.</dl>
<h2>ACTIVITY MONITOR</h2>
<dl>
<dt> <code>nmcli monitor</code></dl>
<dd>Observe NetworkManager activity. Watches for changes in connectivity state, devices or connection profiles. </p>
<p> See also <code>nmcli connection monitor</code> and <code>nmcli device monitor</code> to watch for changes in certain devices or connections.</p>
<h2>CONNECTION MANAGEMENT COMMANDS</h2>
<dl>
<dt> <code>nmcli connection</code> {<code>show</code> | <code>up</code> | <code>down</code> | <code>modify</code> | <code>add</code> | <code>edit</code> | <code>clone</code> | <code>delete</code> | <code>monitor</code> | <code>reload</code> | <code>load</code> | <code>import</code> | <code>export</code>} [<i>ARGUMENTS</i>&#8230;]</dl>
<dd>NetworkManager stores all network configuration as &quot;connections&quot;, which are collections of data (Layer2 details, IP addressing, etc.) that describe how to create or connect to a network. A connection is &quot;active&quot; when a device uses that connection&#8217;s configuration to create or connect to a network. There may be multiple connections that apply to a device, but only one of them can be active on that device at any given time. The additional connections can be used to allow quick switching between different networks and configurations. </p>
<p> Consider a machine which is usually connected to a DHCP-enabled network, but sometimes connected to a testing network which uses static IP addressing. Instead of manually reconfiguring eth0 each time the network is changed, the settings can be saved as two connections which both apply to eth0, one for DHCP (called default) and one with the static addressing details (called testing). When connected to the DHCP-enabled network the user would run <code>nmcli con up default</code> , and when connected to the static network the user would run <code>nmcli con up testing</code>. </p>
<p> <code>show</code> [<code>&#8211;active</code>] [<code>&#8211;order</code>&nbsp;[+-]<i>category</i>:&#8230;]</p>
<dl>
<dt>
<dd> List in-memory and on-disk connection profiles, some of which may also be active if a device is using that connection profile. Without a parameter, all profiles are listed. When <code>&#8211;active</code> option is specified, only the active profiles are shown. </p>
<p> The <code>&#8211;order</code> option can be used to get custom ordering of connections. The connections can be ordered by active status (active), name (name), type (type) or D-Bus path (path). If connections are equal according to a sort order category, an additional category can be specified. The default sorting order is equivalent to &#8211;order active:name:path. + or no prefix means sorting in ascending order (alphabetically or in numbers), &#8211; means reverse (descending) order. The category names can be abbreviated (e.g. &#8211;order -a:na).</dl>
<p> <code>show</code> [<code>&#8211;active</code>] [<code>id</code> | <code>uuid</code> | <code>path</code> | <code>apath</code>] <i>ID</i>&#8230;</p>
<dl>
<dt>
<dd> Show details for specified connections. By default, both static configuration and active connection data are displayed. When <code>&#8211;active</code> option is specified, only the active profiles are taken into account. Use global <code>&#8211;show-secrets</code> option to display secrets associated with the profile. </p>
<p> <code>id</code>, <code>uuid</code>, <code>path</code> and <code>apath</code> keywords can be used if <i>ID</i> is ambiguous. Optional <i>ID</i>-specifying keywords are: </p>
<p> <code>id</code></p>
<dl>
<dt>
<dd> the <i>ID</i> denotes a connection name.</dl>
<p> <code>uuid</code></p>
<dl>
<dt>
<dd> the <i>ID</i> denotes a connection UUID.</dl>
<p> <code>path</code></p>
<dl>
<dt>
<dd> the <i>ID</i> denotes a D-Bus static connection path in the format of /org/freedesktop/NetworkManager/Settings/<i>num</i> or just <i>num</i>.</dl>
<p> <code>apath</code></p>
<dl>
<dt>
<dd> the <i>ID</i> denotes a D-Bus active connection path in the format of /org/freedesktop/NetworkManager/ActiveConnection/<i>num</i> or just <i>num</i>.</dl>
<p> It is possible to filter the output using the global <code>&#8211;fields</code> option. Use the following values: </p>
<p> <code>profile</code></p>
<dl>
<dt>
<dd> only shows static profile configuration.</dl>
<p> <code>active</code></p>
<dl>
<dt>
<dd> only shows active connection data (when the profile is active).</dl>
<p> You can also specify particular fields. For static configuration, use setting and property names as described in <code><a href="/docs/linux/man/5-nm-settings-nmcli/">nm-settings-nmcli</a></code>(5) manual page. For active data use GENERAL, IP4, DHCP4, IP6, DHCP6, VPN. </p>
<p> When no command is given to the <code>nmcli connection</code>, the default action is <code>nmcli connection show</code>.</dl>
<p> <code>up</code> [<code>id</code> | <code>uuid</code> | <code>path</code>] <i>ID</i> [<code>ifname</code>&nbsp;<i>ifname</i>] [<code>ap</code>&nbsp;<i>BSSID</i>] [<code>passwd-file</code>&nbsp;<i>file</i>]</p>
<dl>
<dt>
<dd> Activate a connection. The connection is identified by its name, UUID or D-Bus path. If <i>ID</i> is ambiguous, a keyword <code>id</code>, <code>uuid</code> or <code>path</code> can be used. When requiring a particular device to activate the connection on, the <code>ifname</code> option with interface name should be given. If the <i>ID</i> is not given an <code>ifname</code> is required, and NetworkManager will activate the best available connection for the given <code>ifname</code>. In case of a VPN connection, the <code>ifname</code> option specifies the device of the base connection. The <code>ap</code> option specify what particular AP should be used in case of a Wi-Fi connection. </p>
<p> If <code>&#8211;wait</code> option is not specified, the default timeout will be 90 seconds. </p>
<p> See <code>connection show</code> above for the description of the <i>ID</i>-specifying keywords. </p>
<p> Available options are: </p>
<p> <code>ifname</code></p>
<dl>
<dt>
<dd> interface that will be used for activation.</dl>
<p> <code>ap</code></p>
<dl>
<dt>
<dd> BSSID of the AP which the command should connect to (for Wi-Fi connections).</dl>
<p> <code>passwd-file</code></p>
<dl>
<dt>
<dd> some networks may require credentials during activation. You can give these credentials using this option. Each line of the file should contain one password in the form: </p>
<dl>
<dt>
<dd>
<pre>
setting_name.property_name:the password
</pre>
</dl>
<p> For example, for WPA Wi-Fi with PSK, the line would be </p>
<dl>
<dt>
<dd>
<pre>
802-11-wireless-security.psk:secret12345
</pre>
</dl>
<p> For 802.1X password, the line would be </p>
<dl>
<dt>
<dd>
<pre>
802-1x.password:my 1X password
</pre>
</dl>
<p> <code>nmcli</code> also accepts wifi-sec and wifi strings instead of 802-11-wireless-security. When NetworkManager requires a password and it is not given, <code>nmcli</code> will ask for it when run with <code>&#8211;ask</code>. If <code>&#8211;ask</code> was not passed, NetworkManager can ask another secret agent that may be running (typically a GUI secret agent, such as nm-applet or gnome-shell).</dl>
</dl>
<p> <code>down</code> [<code>id</code> | <code>uuid</code> | <code>path</code> | <code>apath</code>] <i>ID</i>&#8230;</p>
<dl>
<dt>
<dd> Deactivate a connection from a device without preventing the device from further auto-activation. Multiple connections can be passed to the command. </p>
<p> Be aware that this command deactivates the specified active connection, but the device on which the connection was active, is still ready to connect and will perform auto-activation by looking for a suitable connection that has the &#8216;autoconnect&#8217; flag set. Note that the deactivating connection profile is internally blocked from autoconnecting again. Hence it will not autoconnect until reboot or until the user performs an action that unblocks autoconnect, like modifying the profile or explicitly activating it. </p>
<p> In most cases you may want to use <code>device down</code> command instead. </p>
<p> The connection is identified by its name, UUID or D-Bus path. If <i>ID</i> is ambiguous, a keyword <code>id</code>, <code>uuid</code>, <code>path</code> or <code>apath</code> can be used. </p>
<p> See <code>connection show</code> above for the description of the <i>ID</i>-specifying keywords. </p>
<p> If <code>&#8211;wait</code> option is not specified, the default timeout will be 10 seconds.</dl>
<p> <code>modify</code> [<code>&#8211;temporary</code>] [<code>id</code> | <code>uuid</code> | <code>path</code>] <i>ID</i> {<i>option</i>&nbsp;<i>value</i>&nbsp;|&nbsp;[+|-]<i>setting</i>.<i>property</i>&nbsp;<i>value</i>}&#8230;</p>
<dl>
<dt>
<dd> Add, modify or remove properties in the connection profile. </p>
<p> To set the property just specify the property name followed by the value. An empty value (&quot;&quot;) resets the property value to the default. </p>
<p> See <code><a href="/docs/linux/man/5-nm-settings-nmcli/">nm-settings-nmcli</a></code>(5) for complete reference of setting and property names, their descriptions and default values. The <i>setting</i> and <i>property</i> can be abbreviated provided they are unique. </p>
<p> If you want to append an item or a flag to the existing value, use + prefix for the property name or alias. If you want to remove items from a container-type or flag property, use &#8211; prefix. For certain properties you can also remove elements by specifying the zero-based index(es). The + and &#8211; modifiers only have a real effect for properties that support them. These are for example multi-value (container) properties or flags like ipv4.dns, ip4, ipv4.addresses, bond.options, 802-1x.phase1-auth-flags etc. </p>
<p> The connection is identified by its name, UUID or D-Bus path. If <i>ID</i> is ambiguous, a keyword <code>id</code>, <code>uuid</code> or <code>path</code> can be used.</dl>
<p> <code>modify</code> [<code>&#8211;temporary</code>] [<code>id</code> | <code>uuid</code> | <code>path</code>] <i>ID</i> <code>remove</code>&nbsp;<i>setting</i></p>
<dl>
<dt>
<dd> Removes a setting from the connection profile.</dl>
<p> <code>add</code> [<code>save</code>&nbsp;{yes | no}] {<i>option</i>&nbsp;<i>value</i>&nbsp;|&nbsp;[+|-]<i>setting</i>.<i>property</i>&nbsp;<i>value</i>}&#8230;</p>
<dl>
<dt>
<dd> Create a new connection using specified properties. </p>
<p> You need to describe the newly created connections with the property and value pairs. See <code><a href="/docs/linux/man/5-nm-settings-nmcli/">nm-settings-nmcli</a></code>(5) for the complete reference. The syntax is the same as of the <code>nmcli connection modify</code> command. </p>
<p> To construct a meaningful connection you at the very least need to set the <code>connection.type</code> property (or use the <code>type</code> alias) to one of known NetworkManager connection types: </p>
<dl>
<dt>
<dd> &bull; 6lowpan</dl>
<dl>
<dt>
<dd> &bull; 802-11-olpc-mesh (alias olpc-mesh)</dl>
<dl>
<dt>
<dd> &bull; 802-11-wireless (alias wifi)</dl>
<dl>
<dt>
<dd> &bull; 802-3-ethernet (alias ethernet)</dl>
<dl>
<dt>
<dd> &bull; adsl</dl>
<dl>
<dt>
<dd> &bull; bluetooth</dl>
<dl>
<dt>
<dd> &bull; bond</dl>
<dl>
<dt>
<dd> &bull; bond-slave (deprecated for ethernet with master)</dl>
<dl>
<dt>
<dd> &bull; bridge</dl>
<dl>
<dt>
<dd> &bull; bridge-slave (deprecated for ethernet with master)</dl>
<dl>
<dt>
<dd> &bull; cdma</dl>
<dl>
<dt>
<dd> &bull; dummy</dl>
<dl>
<dt>
<dd> &bull; generic</dl>
<dl>
<dt>
<dd> &bull; gsm</dl>
<dl>
<dt>
<dd> &bull; infiniband</dl>
<dl>
<dt>
<dd> &bull; ip-tunnel</dl>
<dl>
<dt>
<dd> &bull; macsec</dl>
<dl>
<dt>
<dd> &bull; macvlan</dl>
<dl>
<dt>
<dd> &bull; olpc-mesh</dl>
<dl>
<dt>
<dd> &bull; ovs-bridge</dl>
<dl>
<dt>
<dd> &bull; ovs-dpdk</dl>
<dl>
<dt>
<dd> &bull; ovs-interface</dl>
<dl>
<dt>
<dd> &bull; ovs-patch</dl>
<dl>
<dt>
<dd> &bull; ovs-port</dl>
<dl>
<dt>
<dd> &bull; pppoe</dl>
<dl>
<dt>
<dd> &bull; team</dl>
<dl>
<dt>
<dd> &bull; team-slave (deprecated for ethernet with master)</dl>
<dl>
<dt>
<dd> &bull; tun</dl>
<dl>
<dt>
<dd> &bull; veth</dl>
<dl>
<dt>
<dd> &bull; vlan</dl>
<dl>
<dt>
<dd> &bull; vpn</dl>
<dl>
<dt>
<dd> &bull; vrf</dl>
<dl>
<dt>
<dd> &bull; vxlan</dl>
<dl>
<dt>
<dd> &bull; wifi-p2p</dl>
<dl>
<dt>
<dd> &bull; wimax</dl>
<dl>
<dt>
<dd> &bull; wireguard</dl>
<dl>
<dt>
<dd> &bull; wpan</dl>
<p> The most typical uses are described in the EXAMPLES section. </p>
<p> Aside from the properties and values two special options are accepted: </p>
<p> <code>save</code></p>
<dl>
<dt>
<dd> Controls whether the connection should be persistent, i.e. NetworkManager should store it on disk (default: yes).</dl>
<p> <code>&#8212;</code></p>
<dl>
<dt>
<dd> If a single <code>&#8212;</code> argument is encountered it is ignored. This is for compatibility with older versions on <code>nmcli</code>.</dl>
</dl>
<p> <code>edit</code> {[<code>id</code>&nbsp;|&nbsp;<code>uuid</code>&nbsp;|&nbsp;<code>path</code>]&nbsp;<i>ID</i> | [<code>type</code>&nbsp;<i>type</i>]&nbsp;[<code>con-name</code>&nbsp;<i>name</i>] }</p>
<dl>
<dt>
<dd> Edit an existing connection or add a new one, using an interactive editor. </p>
<p> The existing connection is identified by its name, UUID or D-Bus path. If <i>ID</i> is ambiguous, a keyword <code>id</code>, <code>uuid</code>, or <code>path</code> can be used. See <code>connection show</code> above for the description of the <i>ID</i>-specifying keywords. Not providing an <i>ID</i> means that a new connection will be added. </p>
<p> The interactive editor will guide you through the connection editing and allow you to change connection parameters according to your needs by means of a simple menu-driven interface. The editor indicates what settings and properties can be modified and provides in-line help. </p>
<p> Available options: </p>
<p> <code>type</code></p>
<dl>
<dt>
<dd> type of the new connection; valid types are the same as for <code>connection add</code> command.</dl>
<p> <code>con-name</code></p>
<dl>
<dt>
<dd> name for the new connection. It can be changed later in the editor.</dl>
<p> See also <code><a href="/docs/linux/man/5-nm-settings-nmcli/">nm-settings-nmcli</a></code>(5) for all NetworkManager settings and property names, and their descriptions; and <code><a href="/docs/linux/man/7-nmcli-examples/">nmcli-examples</a></code>(7) for sample editor sessions.</dl>
<p> <code>clone</code> [<code>&#8211;temporary</code>] [<code>id</code> | <code>uuid</code> | <code>path</code>] <i>ID</i> <i>new_name</i></p>
<dl>
<dt>
<dd> Clone a connection. The connection to be cloned is identified by its name, UUID or D-Bus path. If <i>ID</i> is ambiguous, a keyword <code>id</code>, <code>uuid</code> or <code>path</code> can be used. See <code>connection show</code> above for the description of the <i>ID</i>-specifying keywords. <i>new_name</i> is the name of the new cloned connection. The new connection will be the exact copy except the connection.id (<i>new_name</i>) and connection.uuid (generated) properties. </p>
<p> The new connection profile will be saved as persistent unless <code>&#8211;temporary</code> option is specified, in which case the new profile won&#8217;t exist after NetworkManager restart.</dl>
<p> <code>delete</code> [<code>id</code> | <code>uuid</code> | <code>path</code>] <i>ID</i>&#8230;</p>
<dl>
<dt>
<dd> Delete a configured connection. The connection to be deleted is identified by its name, UUID or D-Bus path. If <i>ID</i> is ambiguous, a keyword <code>id</code>, <code>uuid</code> or <code>path</code> can be used. See <code>connection show</code> above for the description of the <i>ID</i>-specifying keywords. </p>
<p> If <code>&#8211;wait</code> option is not specified, the default timeout will be 10 seconds.</dl>
<p> <code>monitor</code> [<code>id</code> | <code>uuid</code> | <code>path</code>] <i>ID</i>&#8230;</p>
<dl>
<dt>
<dd> Monitor connection profile activity. This command prints a line whenever the specified connection changes. The connection to be monitored is identified by its name, UUID or D-Bus path. If <i>ID</i> is ambiguous, a keyword <code>id</code>, <code>uuid</code> or <code>path</code> can be used. See <code>connection show</code> above for the description of the <i>ID</i>-specifying keywords. </p>
<p> Monitors all connection profiles in case none is specified. The command terminates when all monitored connections disappear. If you want to monitor connection creation consider using the global monitor with <code>nmcli monitor</code> command.</dl>
<p> <code>reload</code></p>
<dl>
<dt>
<dd> Reload all connection files from disk. NetworkManager does not monitor changes to connection. So you need to use this command in order to tell NetworkManager to re-read the connection profiles from disk when a change was made to them.</dl>
<p> <code>load</code> <i>filename</i>&#8230;</p>
<dl>
<dt>
<dd> Load/reload one or more connection files from disk. Use this after manually editing a connection file to ensure that NetworkManager is aware of its latest state.</dl>
<p> <code>import</code> [<code>&#8211;temporary</code>] <code>type</code>&nbsp;<i>type</i> <code>file</code>&nbsp;<i>file</i></p>
<dl>
<dt>
<dd> Import an external/foreign configuration as a NetworkManager connection profile. The type of the input file is specified by <code>type</code> option. </p>
<p> Only VPN configurations are supported at the moment. The configuration is imported by NetworkManager VPN plugins. <code>type</code> values are the same as for <code>vpn-type</code> option in <code>nmcli connection add</code>. VPN configurations are imported by VPN plugins. Therefore the proper VPN plugin has to be installed so that <code>nmcli</code> could import the data. </p>
<p> The imported connection profile will be saved as persistent unless <code>&#8211;temporary</code> option is specified, in which case the new profile won&#8217;t exist after NetworkManager restart.</dl>
<p> <code>export</code> [<code>id</code> | <code>uuid</code> | <code>path</code>] <i>ID</i> [<i>file</i>]</p>
<dl>
<dt>
<dd> Export a connection. </p>
<p> Only VPN connections are supported at the moment. A proper VPN plugin has to be installed so that <code>nmcli</code> could export a connection. If no <i>file</i> is provided, the VPN configuration data will be printed to standard output.</dl>
<h2>DEVICE MANAGEMENT COMMANDS</h2>
<dl>
<dt> <code>nmcli device</code> {<code>status</code> | <code>show</code> | <code>set</code> | <code>up</code> | <code>connect</code> | <code>reapply</code> | <code>modify</code> | <code>down</code> | <code>disconnect</code> | <code>delete</code> | <code>monitor</code> | <code>wifi</code> | <code>lldp</code>} [<i>ARGUMENTS</i>&#8230;]</dl>
<dd>Show and manage network interfaces. </p>
<p> <code>status</code></p>
<dl>
<dt>
<dd> Print status of devices. </p>
<p> This is the default action if no command is specified to <code>nmcli device</code>.</dl>
<p> <code>show</code> [<i>ifname</i>]</p>
<dl>
<dt>
<dd> Show detailed information about devices. Without an argument, all devices are examined. To get information for a specific device, the interface name has to be provided.</dl>
<p> <code>set</code> [ifname] <i>ifname</i> [<code>autoconnect</code>&nbsp;{yes | no}] [<code>managed</code>&nbsp;{yes | no}]</p>
<dl>
<dt>
<dd> Set device properties.</dl>
<p> <code>up</code> <i>ifname</i></p>
<dl>
<dt>
<dd> Connect the device. NetworkManager will try to find a suitable connection that will be activated. It will also consider connections that are not set to auto connect. </p>
<p> If no compatible connection exists, a new profile with default settings will be created and activated. This differentiates <code>nmcli connection up ifname &quot;$DEVICE&quot;</code> from <code>nmcli device up &quot;$DEVICE&quot;</code> </p>
<p> If <code>&#8211;wait</code> option is not specified, the default timeout will be 90 seconds.</dl>
<p> <code>connect</code> <i>ifname</i></p>
<dl>
<dt>
<dd> Alias for command <code>up</code>. Before version 1.34.0 <code>up</code> was not supported.</dl>
<p> <code>reapply</code> <i>ifname</i></p>
<dl>
<dt>
<dd> Attempt to update device with changes to the currently active connection made since it was last applied.</dl>
<p> <code>modify</code> <i>ifname</i> {<i>option</i>&nbsp;<i>value</i>&nbsp;|&nbsp;[+|-]<i>setting</i>.<i>property</i>&nbsp;<i>value</i>}&#8230;</p>
<dl>
<dt>
<dd> Modify the settings currently active on the device. </p>
<p> This command lets you do temporary changes to a configuration active on a particular device. The changes are not preserved in the connection profile. </p>
<p> See <code><a href="/docs/linux/man/5-nm-settings-nmcli/">nm-settings-nmcli</a></code>(5) for the list of available properties. Please note that some properties can&#8217;t be changed on an already connected device.</dl>
<p> <code>down</code> <i>ifname</i>&#8230;</p>
<dl>
<dt>
<dd> Disconnect a device and prevent the device from automatically activating further connections without user/manual intervention. Note that disconnecting software devices may mean that the devices will disappear. </p>
<p> If <code>&#8211;wait</code> option is not specified, the default timeout will be 10 seconds.</dl>
<p> <code>disconnect</code> <i>ifname</i>&#8230;</p>
<dl>
<dt>
<dd> Alias for command <code>down</code>. Before version 1.34.0 <code>down</code> was not supported.</dl>
<p> <code>delete</code> <i>ifname</i>&#8230;</p>
<dl>
<dt>
<dd> Delete a device. The command removes the interface from the system. Note that this only works for software devices like bonds, bridges, teams, etc. Hardware devices (like Ethernet) cannot be deleted by the command. </p>
<p> If <code>&#8211;wait</code> option is not specified, the default timeout will be 10 seconds.</dl>
<p> <code>monitor</code> [<i>ifname</i>&#8230;]</p>
<dl>
<dt>
<dd> Monitor device activity. This command prints a line whenever the specified devices change state. </p>
<p> Monitors all devices in case no interface is specified. The monitor terminates when all specified devices disappear. If you want to monitor device addition consider using the global monitor with <code>nmcli monitor</code> command.</dl>
<p> <code>wifi</code> [<code>list</code>&nbsp;[<code>&#8211;rescan</code>&nbsp;|&nbsp;<code>auto</code>&nbsp;|&nbsp;<code>no</code>&nbsp;|&nbsp;<code>yes</code>]&nbsp;[<code>ifname</code>&nbsp;<i>ifname</i>]&nbsp;[<code>bssid</code>&nbsp;<i>BSSID</i>]]</p>
<dl>
<dt>
<dd> List available Wi-Fi access points. The <code>ifname</code> and <code>bssid</code> options can be used to list APs for a particular interface or with a specific BSSID, respectively. </p>
<p> By default, <code>nmcli</code> ensures that the access point list is no older than 30 seconds and triggers a network scan if necessary. The <code>&#8211;rescan</code> can be used to either force or disable the scan regardless of how fresh the access point list is.</dl>
<p> <code>wifi</code> <code>connect</code> <i>(B)SSID</i> [<code>password</code>&nbsp;<i>password</i>] [<code>wep-key-type</code>&nbsp;{key | phrase}] [<code>ifname</code>&nbsp;<i>ifname</i>] [<code>bssid</code>&nbsp;<i>BSSID</i>] [<code>name</code>&nbsp;<i>name</i>] [<code>private</code>&nbsp;{yes | no}] [<code>hidden</code>&nbsp;{yes | no}]</p>
<dl>
<dt>
<dd> Connect to a Wi-Fi network specified by SSID or BSSID. The command finds a matching connection or creates one and then activates it on a device. This is a command-line counterpart of clicking an SSID in a GUI client. If a connection for the network already exists, it is possible to bring up (activate) the existing profile as follows: <code>nmcli con up id </code><i>name</i>. Note that only open, WEP and WPA-PSK networks are supported if no previous connection exists. It is also assumed that IP configuration is obtained via DHCP. </p>
<p> If <code>&#8211;wait</code> option is not specified, the default timeout will be 90 seconds. </p>
<p> Available options are: </p>
<p> <code>password</code></p>
<dl>
<dt>
<dd> password for secured networks (WEP or WPA).</dl>
<p> <code>wep-key-type</code></p>
<dl>
<dt>
<dd> type of WEP secret, either <code>key</code> for ASCII/HEX key or <code>phrase</code> for passphrase.</dl>
<p> <code>ifname</code></p>
<dl>
<dt>
<dd> interface that will be used for activation.</dl>
<p> <code>bssid</code></p>
<dl>
<dt>
<dd> if specified, the created connection will be restricted just for the BSSID.</dl>
<p> <code>name</code></p>
<dl>
<dt>
<dd> if specified, the connection will use the name (else NM creates a name itself).</dl>
<p> <code>private</code></p>
<dl>
<dt>
<dd> if set to yes, the connection will only be visible to the user who created it. Otherwise, the connection is system-wide, which is the default.</dl>
<p> <code>hidden</code></p>
<dl>
<dt>
<dd> set to yes when connecting for the first time to an AP not broadcasting its SSID. Otherwise, the SSID would not be found and the connection attempt would fail.</dl>
</dl>
<p> <code>wifi</code> <code>hotspot</code> [<code>ifname</code>&nbsp;<i>ifname</i>] [<code>con-name</code>&nbsp;<i>name</i>] [<code>ssid</code>&nbsp;<i>SSID</i>] [<code>band</code>&nbsp;{a | bg}] [<code>channel</code>&nbsp;<i>channel</i>] [<code>password</code>&nbsp;<i>password</i>]</p>
<dl>
<dt>
<dd> Create a Wi-Fi hotspot. The command creates a hotspot connection profile according to Wi-Fi device capabilities and activates it on the device. The hotspot is secured with WPA if device/driver supports that, otherwise WEP is used. Use <code>connection down</code> or <code>device down</code> to stop the hotspot. </p>
<p> Parameters of the hotspot can be influenced by the optional parameters: </p>
<p> <code>ifname</code></p>
<dl>
<dt>
<dd> what Wi-Fi device is used.</dl>
<p> <code>con-name</code></p>
<dl>
<dt>
<dd> name of the created hotspot connection profile.</dl>
<p> <code>ssid</code></p>
<dl>
<dt>
<dd> SSID of the hotspot.</dl>
<p> <code>band</code></p>
<dl>
<dt>
<dd> Wi-Fi band to use.</dl>
<p> <code>channel</code></p>
<dl>
<dt>
<dd> Wi-Fi channel to use.</dl>
<p> <code>password</code></p>
<dl>
<dt>
<dd> password to use for the created hotspot. If not provided, <code>nmcli</code> will generate a password. The password is either WPA pre-shared key or WEP key. </p>
<p> Note that <code>&#8211;show-secrets</code> global option can be used to print the hotspot password. It is useful especially when the password was generated.</dl>
</dl>
<p> <code>wifi</code> <code>rescan</code> [<code>ifname</code>&nbsp;<i>ifname</i>] [<code>ssid</code>&nbsp;<i>SSID</i>&#8230;]</p>
<dl>
<dt>
<dd> Request that NetworkManager immediately re-scan for available access points. NetworkManager scans Wi-Fi networks periodically, but in some cases it can be useful to start scanning manually (e.g. after resuming the computer). By using <code>ssid</code>, it is possible to scan for a specific SSID, which is useful for APs with hidden SSIDs. You can provide multiple <code>ssid</code> parameters in order to scan more SSIDs. </p>
<p> This command does not show the APs, use <code>nmcli device wifi list</code> for that.</dl>
<p> <code>wifi</code> <code>show-password</code> [<code>ifname</code>&nbsp;<i>ifname</i>]</p>
<dl>
<dt>
<dd> Show the details of the active Wi-Fi networks, including the secrets.</dl>
<p> <code>lldp</code> [<code>list</code>&nbsp;[<code>ifname</code>&nbsp;<i>ifname</i>]]</p>
<dl>
<dt>
<dd> Display information about neighboring devices learned through the Link Layer Discovery Protocol (LLDP). The <code>ifname</code> option can be used to list neighbors only for a given interface. The protocol must be enabled in the connection settings.</dl>
<h2>SECRET AGENT</h2>
<dl>
<dt> <code>nmcli agent</code> {<code>secret</code> | <code>polkit</code> | <code>all</code>}</dl>
<dd>Run <code>nmcli</code> as a NetworkManager secret agent, or polkit agent. </p>
<p> <code>secret</code></p>
<dl>
<dt>
<dd> Register <code>nmcli</code> as a NetworkManager secret agent and listen for secret requests. You usually do not need this command, because <code>nmcli</code> can handle secrets when connecting to networks. However, you may find the command useful when you use another tool for activating connections and you do not have a secret agent available (like nm-applet).</dl>
<p> <code>polkit</code></p>
<dl>
<dt>
<dd> Register <code>nmcli</code> as a polkit agent for the user session and listen for authorization requests. You do not usually need this command, because <code>nmcli</code> can handle polkit actions related to NetworkManager operations (when run with <code>&#8211;ask</code>). However, you may find the command useful when you want to run a simple text based polkit agent and you do not have an agent of a desktop environment. Note that running this command makes <code>nmcli</code> handle all polkit requests, not only NetworkManager related ones, because only one polkit agent can run for the session.</dl>
<p> <code>all</code></p>
<dl>
<dt>
<dd> Runs <code>nmcli</code> as both NetworkManager secret and a polkit agent.</dl>
<h2>COLORS</h2>
<p> Implicit coloring can be disabled by an empty file /etc/terminal-colors.d/nmcli.disable. </p>
<p> See <code><a href="/docs/linux/man/5-terminal-colors-d/">terminal-colors.d</a></code>(5) for more details about colorization configuration. The logical color names supported by <code>nmcli</code> are: </p>
<p> <code>connection-activated</code></p>
<dl>
<dt>
<dd> A connection that is active.</dl>
<p> <code>connection-activating</code></p>
<dl>
<dt>
<dd> Connection that is being activated.</dl>
<p> <code>connection-disconnecting</code></p>
<dl>
<dt>
<dd> Connection that is being disconnected.</dl>
<p> <code>connection-external</code></p>
<dl>
<dt>
<dd> Connection representing configuration created externally to NetworkManager.</dl>
<p> <code>connection-invisible</code></p>
<dl>
<dt>
<dd> Connection whose details is the user not permitted to see.</dl>
<p> <code>connectivity-full</code></p>
<dl>
<dt>
<dd> Connectivity state when Internet is reachable.</dl>
<p> <code>connectivity-limited</code></p>
<dl>
<dt>
<dd> Connectivity state when only a local network reachable.</dl>
<p> <code>connectivity-none</code></p>
<dl>
<dt>
<dd> Connectivity state when the network is disconnected.</dl>
<p> <code>connectivity-portal</code></p>
<dl>
<dt>
<dd> Connectivity state when a captive portal hijacked the connection.</dl>
<p> <code>connectivity-unknown</code></p>
<dl>
<dt>
<dd> Connectivity state when a connectivity check didn&#8217;t run.</dl>
<p> <code>device-activated</code></p>
<dl>
<dt>
<dd> Device that is connected.</dl>
<p> <code>device-activating</code></p>
<dl>
<dt>
<dd> Device that is being configured.</dl>
<p> <code>device-disconnected</code></p>
<dl>
<dt>
<dd> Device that is not connected.</dl>
<p> <code>device-external</code></p>
<dl>
<dt>
<dd> Device configured externally to NetworkManager.</dl>
<p> <code>device-firmware-missing</code></p>
<dl>
<dt>
<dd> Warning of a missing device firmware.</dl>
<p> <code>device-plugin-missing</code></p>
<dl>
<dt>
<dd> Warning of a missing device plugin.</dl>
<p> <code>device-unavailable</code></p>
<dl>
<dt>
<dd> Device that is not available for activation.</dl>
<p> <code>device-disabled</code></p>
<dl>
<dt>
<dd> Device is disabled by software or hardware kill switch.</dl>
<p> <code>manager-running</code></p>
<dl>
<dt>
<dd> Notice that the NetworkManager daemon is available.</dl>
<p> <code>manager-starting</code></p>
<dl>
<dt>
<dd> Notice that the NetworkManager daemon is being initially connected.</dl>
<p> <code>manager-stopped</code></p>
<dl>
<dt>
<dd> Notice that the NetworkManager daemon is not available.</dl>
<p> <code>permission-auth</code></p>
<dl>
<dt>
<dd> An action that requires user authentication to get permission.</dl>
<p> <code>permission-no</code></p>
<dl>
<dt>
<dd> An action that is not permitted.</dl>
<p> <code>permission-yes</code></p>
<dl>
<dt>
<dd> An action that is permitted.</dl>
<p> <code>prompt</code></p>
<dl>
<dt>
<dd> Prompt in interactive mode.</dl>
<p> <code>state-asleep</code></p>
<dl>
<dt>
<dd> Indication that NetworkManager in suspended state.</dl>
<p> <code>state-connected-global</code></p>
<dl>
<dt>
<dd> Indication that NetworkManager in connected to Internet.</dl>
<p> <code>state-connected-local</code></p>
<dl>
<dt>
<dd> Indication that NetworkManager in local network.</dl>
<p> <code>state-connected-site</code></p>
<dl>
<dt>
<dd> Indication that NetworkManager in connected to networks other than Internet.</dl>
<p> <code>state-connecting</code></p>
<dl>
<dt>
<dd> Indication that NetworkManager is establishing a network connection.</dl>
<p> <code>state-disconnected</code></p>
<dl>
<dt>
<dd> Indication that NetworkManager is disconnected from a network.</dl>
<p> <code>state-disconnecting</code></p>
<dl>
<dt>
<dd> Indication that NetworkManager is being disconnected from a network.</dl>
<p> <code>wifi-signal-excellent</code></p>
<dl>
<dt>
<dd> Wi-Fi network with an excellent signal level.</dl>
<p> <code>wifi-signal-fair</code></p>
<dl>
<dt>
<dd> Wi-Fi network with a fair signal level.</dl>
<p> <code>wifi-signal-good</code></p>
<dl>
<dt>
<dd> Wi-Fi network with a good signal level.</dl>
<p> <code>wifi-signal-poor</code></p>
<dl>
<dt>
<dd> Wi-Fi network with a poor signal level.</dl>
<p> <code>wifi-signal-unknown</code></p>
<dl>
<dt>
<dd> Wi-Fi network that hasn&#8217;t been actually seen (a hidden AP).</dl>
<p> <code>disabled</code></p>
<dl>
<dt>
<dd> A property that is turned off.</dl>
<p> <code>enabled</code></p>
<dl>
<dt>
<dd> A property that is turned on.</dl>
<h2>ENVIRONMENT VARIABLES</h2>
<p> <code>nmcli</code>&#8216;s behavior is affected by the following environment variables. </p>
<p> <code>LC_ALL</code></p>
<dl>
<dt>
<dd> If set to a non-empty string value, it overrides the values of all the other internationalization variables.</dl>
<p> <code>LC_MESSAGES</code></p>
<dl>
<dt>
<dd> Determines the locale to be used for internationalized messages.</dl>
<p> <code>LANG</code></p>
<dl>
<dt>
<dd> Provides a default value for the internationalization variables that are unset or null.</dl>
<h2>INTERNATIONALIZATION NOTES</h2>
<p> Be aware that <code>nmcli</code> is localized and that is why the output depends on your environment. This is important to realize especially when you parse the output. </p>
<p> Call <code>nmcli</code> as <code>LC_ALL=C nmcli</code> to be sure the locale is set to C while executing in a script. </p>
<p> <code>LC_ALL</code>, <code>LC_MESSAGES</code>, <code>LANG</code> variables specify the <code>LC_MESSAGES</code> locale category (in that order), which determines the language that <code>nmcli</code> uses for messages. The C locale is used if none of these variables are set, and this locale uses English messages.</p>
<h2>EXIT STATUS</h2>
<p> <code>nmcli</code> exits with status 0 if it succeeds, a value greater than 0 is returned if an error occurs. </p>
<p> <code>0</code></p>
<dl>
<dt>
<dd> Success &#8211; indicates the operation succeeded.</dl>
<p> <code>1</code></p>
<dl>
<dt>
<dd> Unknown or unspecified error.</dl>
<p> <code>2</code></p>
<dl>
<dt>
<dd> Invalid user input, wrong <code>nmcli</code> invocation.</dl>
<p> <code>3</code></p>
<dl>
<dt>
<dd> Timeout expired (see <code>&#8211;wait</code> option).</dl>
<p> <code>4</code></p>
<dl>
<dt>
<dd> Connection activation failed.</dl>
<p> <code>5</code></p>
<dl>
<dt>
<dd> Connection deactivation failed.</dl>
<p> <code>6</code></p>
<dl>
<dt>
<dd> Disconnecting device failed.</dl>
<p> <code>7</code></p>
<dl>
<dt>
<dd> Connection deletion failed.</dl>
<p> <code>8</code></p>
<dl>
<dt>
<dd> NetworkManager is not running.</dl>
<p> <code>10</code></p>
<dl>
<dt>
<dd> Connection, device, or access point does not exist.</dl>
<p> <code>65</code></p>
<dl>
<dt>
<dd> When used with <code>&#8211;complete-args</code> option, a file name is expected to follow.</dl>
<h2>EXAMPLES</h2>
<p> This section presents various examples of <code>nmcli</code> usage. If you want even more, please refer to <code><a href="/docs/linux/man/7-nmcli-examples/">nmcli-examples</a></code>(7) manual page. </p>
<p> <code>nmcli -t -f RUNNING general</code></p>
<dl>
<dt>
<dd> tells you whether NetworkManager is running or not.</dl>
<p> <code>nmcli -t -f STATE general</code></p>
<dl>
<dt>
<dd> shows the overall status of NetworkManager.</dl>
<p> <code>nmcli radio wifi off</code></p>
<dl>
<dt>
<dd> switches Wi-Fi off.</dl>
<p> <code>nmcli connection show</code></p>
<dl>
<dt>
<dd> lists all connections NetworkManager has.</dl>
<p> <code>nmcli -p -m multiline -f all con show</code></p>
<dl>
<dt>
<dd> shows all configured connections in multi-line mode.</dl>
<p> <code>nmcli connection show &#8211;active</code></p>
<dl>
<dt>
<dd> lists all currently active connections.</dl>
<p> <code>nmcli -f name,autoconnect c s</code></p>
<dl>
<dt>
<dd> shows all connection profile names and their auto-connect property.</dl>
<p> <code>nmcli -p connection show &quot;My default em1&quot;</code></p>
<dl>
<dt>
<dd> shows details for &quot;My default em1&quot; connection profile.</dl>
<p> <code>nmcli &#8211;show-secrets connection show &quot;My Home Wi-Fi&quot;</code></p>
<dl>
<dt>
<dd> shows details for &quot;My Home Wi-Fi&quot; connection profile with all passwords. Without <code>&#8211;show-secrets</code> option, secrets would not be displayed.</dl>
<p> <code>nmcli -f active connection show &quot;My default em1&quot;</code></p>
<dl>
<dt>
<dd> shows details for &quot;My default em1&quot; active connection, like IP, DHCP information, etc.</dl>
<p> <code>nmcli -f profile con s &quot;My wired connection&quot;</code></p>
<dl>
<dt>
<dd> shows static configuration details of the connection profile with &quot;My wired connection&quot; name.</dl>
<p> <code>nmcli -p con up &quot;My wired connection&quot; ifname eth0</code></p>
<dl>
<dt>
<dd> activates the connection profile with name &quot;My wired connection&quot; on interface eth0. The -p option makes <code>nmcli</code> show progress of the activation.</dl>
<p> <code>nmcli con up 6b028a27-6dc9-4411-9886-e9ad1dd43761 ap 00:3A:98:7C:42:D3</code></p>
<dl>
<dt>
<dd> connects the Wi-Fi connection with UUID 6b028a27-6dc9-4411-9886-e9ad1dd43761 to the AP with BSSID 00:3A:98:7C:42:D3.</dl>
<p> <code>nmcli device status</code></p>
<dl>
<dt>
<dd> shows the status for all devices.</dl>
<p> <code>nmcli dev down em2</code></p>
<dl>
<dt>
<dd> disconnects a connection on interface em2 and marks the device as unavailable for auto-connecting. As a result, no connection will automatically be activated on the device until the device&#8217;s &#8216;autoconnect&#8217; is set to TRUE or the user manually activates a connection.</dl>
<p> <code>nmcli -f GENERAL,WIFI-PROPERTIES dev show wlan0</code></p>
<dl>
<dt>
<dd> shows details for wlan0 interface; only GENERAL and WIFI-PROPERTIES sections will be shown.</dl>
<p> <code>nmcli -f CONNECTIONS device show wlp3s0</code></p>
<dl>
<dt>
<dd> shows all available connection profiles for your Wi-Fi interface wlp3s0.</dl>
<p> <code>nmcli dev wifi</code></p>
<dl>
<dt>
<dd> lists available Wi-Fi access points known to NetworkManager.</dl>
<p> <code>nmcli dev wifi con &quot;Cafe Hotspot 1&quot; password caffeine name &quot;My cafe&quot;</code></p>
<dl>
<dt>
<dd> creates a new connection named &quot;My cafe&quot; and then connects it to &quot;Cafe Hotspot 1&quot; SSID using password &quot;caffeine&quot;. This is mainly useful when connecting to &quot;Cafe Hotspot 1&quot; for the first time. Next time, it is better to use <code>nmcli con up id &quot;My cafe&quot;</code> so that the existing connection profile can be used and no additional is created.</dl>
<p> <code>nmcli -s dev wifi hotspot con-name QuickHotspot</code></p>
<dl>
<dt>
<dd> creates a hotspot profile and connects it. Prints the hotspot password the user should use to connect to the hotspot from other devices.</dl>
<p> <code>nmcli dev modify em1 ipv4.method shared</code></p>
<dl>
<dt>
<dd> starts IPv4 connection sharing using em1 device. The sharing will be active until the device is disconnected.</dl>
<p> <code>nmcli dev modify em1 ipv6.address 2001:db8::a:bad:c0de</code></p>
<dl>
<dt>
<dd> temporarily adds an IP address to a device. The address will be removed when the same connection is activated again.</dl>
<p> <code>nmcli connection add type ethernet autoconnect no ifname eth0</code></p>
<dl>
<dt>
<dd> non-interactively adds an Ethernet connection tied to eth0 interface with automatic IP configuration (DHCP), and disables the connection&#8217;s autoconnect flag.</dl>
<p> <code>nmcli c a ifname Maxipes-fik type vlan dev eth0 id 55</code></p>
<dl>
<dt>
<dd> non-interactively adds a VLAN connection with ID 55. The connection will use eth0 and the VLAN interface will be named Maxipes-fik.</dl>
<p> <code>nmcli c a ifname eth0 type ethernet ipv4.method disabled ipv6.method link-local</code></p>
<dl>
<dt>
<dd> non-interactively adds a connection that will use eth0 Ethernet interface and only have an IPv6 link-local address configured.</dl>
<p> <code>nmcli connection edit ethernet-em1-2</code></p>
<dl>
<dt>
<dd> edits existing &quot;ethernet-em1-2&quot; connection in the interactive editor.</dl>
<p> <code>nmcli connection edit type ethernet con-name &quot;yet another Ethernet connection&quot;</code></p>
<dl>
<dt>
<dd> adds a new Ethernet connection in the interactive editor.</dl>
<p> <code>nmcli con mod ethernet-2 connection.autoconnect no</code></p>
<dl>
<dt>
<dd> modifies &#8216;autoconnect&#8217; property in the &#8216;connection&#8217; setting of &#8216;ethernet-2&#8217; connection.</dl>
<p> <code>nmcli con mod &quot;Home Wi-Fi&quot; wifi.mtu 1350</code></p>
<dl>
<dt>
<dd> modifies &#8216;mtu&#8217; property in the &#8216;wifi&#8217; setting of &#8216;Home Wi-Fi&#8217; connection.</dl>
<p> <code>nmcli con mod em1-1 ipv4.method manual ipv4.addr &quot;192.168.1.23/24 192.168.1.1, 10.10.1.5/8, 10.0.0.11&quot;</code></p>
<dl>
<dt>
<dd> sets manual addressing and the addresses in em1-1 profile.</dl>
<p> <code>nmcli con modify ABC +ipv4.dns 8.8.8.8</code></p>
<dl>
<dt>
<dd> appends a Google public DNS server to DNS servers in ABC profile.</dl>
<p> <code>nmcli con modify ABC -ipv4.addresses &quot;192.168.100.25/24 192.168.1.1&quot;</code></p>
<dl>
<dt>
<dd> removes the specified IP address from (static) profile ABC.</dl>
<p> <code>nmcli con import type openvpn file ~/Downloads/frootvpn.ovpn</code></p>
<dl>
<dt>
<dd> imports an OpenVPN configuration to NetworkManager.</dl>
<p> <code>nmcli con export corp-vpnc /home/joe/corpvpn.conf</code></p>
<dl>
<dt>
<dd> exports NetworkManager VPN profile corp-vpnc as standard Cisco (vpnc) configuration.</dl>
<h2>NOTES</h2>
<p> <code>nmcli</code> accepts abbreviations, as long as they are a unique prefix in the set of possible options. As new options get added, these abbreviations are not guaranteed to stay unique. For scripting and long term compatibility it is therefore strongly advised to spell out the full option names.</p>
<h2>BUGS</h2>
<p> There are probably some bugs. If you find a bug, please report it to your distribution or upstream at <a rel="nofollow" href="https://gitlab.freedesktop.org/NetworkManager/NetworkManager.">https://gitlab.freedesktop.org/NetworkManager/NetworkManager.</a></p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/7-nmcli-examples/">nmcli-examples</a></code>(7), <code><a href="/docs/linux/man/5-nm-settings-nmcli/">nm-settings-nmcli</a></code>(5), <code><a href="/docs/linux/man/1-nm-online/">nm-online</a></code>(1), <code><a href="/docs/linux/man/8-networkmanager/">NetworkManager</a></code>(8), <code><a href="/docs/linux/man/5-networkmanager-conf/">NetworkManager.conf</a></code>(5), <code><a href="/docs/linux/man/1-nm-applet/">nm-applet</a></code>(1), <code><a href="/docs/linux/man/1-nm-connection-editor/">nm-connection-editor</a></code>(1), <code><a href="/docs/linux/man/5-terminal-colors-d/">terminal-colors.d</a></code>(5). </p>
<h2>Index</h2>
