---
title: "ettercap_curses(8)"
name: "ettercap_curses"
section: "8"
letter: "e"
url: "/docs/linux/man/8-ettercap_curses/"
description: "ettercap NG-0.7.3 – Man page for the Ncurses GUI."
---

<p><code>ettercap NG-0.7.3 &#8211; Man page for the Ncurses GUI.</code> </p>
<h2>General Description</h2>
<p>The curses GUI is quite simple and intuitive.<br />
 It is menu-driven. Every flag or function can be modified/called through the upper menu. All user messages are printed in the bottom window. If you want to see the old messages, you can scroll the window buffer by pressing the UP, DOWN, PPAGE, NPAGE keys. The middle part is used to display information or dialogs for the user. </p>
<p> The menus can be opened by pressing the relative hotkey. For the menus the hotkey is represented by the uppercase initial letter of the title (e.g. &#8216;S&#8217; for Sniffing, &#8216;T&#8217; for Targets). The functions within a menu can be called by pressing the hotkey depicted near the function name on the right. Hotkeys prefixed with &#8216;C-&#8216; are to be used in conjunction with the CTRL key (e.g. &#8216;C-f&#8217; means CTRL+f). </p>
<p> You can switch the focus between the objects on the screen by pressing the TAB key or by clicking on it with the mouse (if you are running ettercap within an xterm). Mouse events are supported only through the xterm. You can use the mouse to select objects, open a menu, choose a function, scroll the elevators for the scrolling windows, etc etc. </p>
<p> When you open multiple windows in the middle part, they will overlap. Use the TAB key to switch between them. Use CTRL+Q to close the focused window.<br />
 You can also use CTRL+Q to close the input dialog if you want to cancel the requested input. (i.e. you have selected the wrong function and you want to go back). </p>
<p> To have a quick help on the shortcuts you can use against a particular window press the SPACE key. A help window will be displayed with a list of shortcuts that can be used. If the window does not appear, no shortcuts are available.</p>
<h2>How To Select It</h2>
<p>To use the ncurses GUI you have to: </p>
<p> &#8211; compile ettercap with ncurses support (obviously)<br />
 &#8211; run it with the -C flag </p>
<p> Passing the -C flag is sufficient, but if you want you can pass other flags that will be automatically set for the ncurses GUI. You will be able to override them using the menu to change the options.</p>
<h2>Once Started</h2>
<p>As soon as ettercap is launched with the Ncurses GUI, you will be prompted with multiple choices. The first screen lets you select if you want to open a pcap file or dump the sniffed traffic to a file, if you want unified sniffing or bridged one, permits you to set a pcap file on the captured traffic and enables you to log all the sniffed data. </p>
<p> Once you have selected a sniffing method (from file, unified or bridged) this screen will not be reachable anymore. The only way is to restart ettercap. </p>
<p> Let&#8217;s analyze each menu in the start screen: </p>
<dl>
<dt><code>File</code></p>
<dd>
<dl>
<dd>
<dl>
<dt><code>Open&#8230; </code></p>
<dd>Open a pcap file and analyze it. All the functionalities available for live sniffing are in place except for those sending or forwarding packets (mitm attacks and so on&#8230;).</p>
<dt><code>Dump to file&#8230;</code></p>
<dd>All the traffic sniffed by the live capture will be dumped to that file. The filters, not the targets, have effects on this file, as all the packets received by pcap will be dumped. The only way to not dump a certain packet is to set a proper pcap filter (see below).</p>
<dt><code>Exit</code></p>
<dd>Exits from ettercap and returns to the command prompt.</dl>
</dl>
<dt><code>Sniff</code></p>
<dd>
<dl>
<dd>
<dl>
<dt><code>Unified sniffing&#8230; </code></p>
<dd>Choosing this function you will be prompted to select the network interface to be used for sniffing. The first up and running interface is suggested in the input box. For an explanation of what unified sniffing is, refer to <a href="/docs/linux/man/8-ettercap/">ettercap</a>(8).<br />
 TIP: if you use the &#8216;u&#8217; hotkey, this step will be skipped and the default interface is automatically selected.</p>
<dt><code>Bridged sniffing&#8230; </code></p>
<dd>After selecting the two interfaces to be used, you will enter the Bridged sniffing mode. For an explanation of what bridged sniffing is, refer to <a href="/docs/linux/man/8-ettercap/">ettercap</a>(8).</p>
<dt><code>Set pcap filter&#8230;</code></p>
<dd>Here you can insert a tcpdump-like filter for the capturing process.<br />
 IMPORTANT: if you manage to use a mitm attack, remember that if ettercap does not see a packet, it will NOT be forwarded. So be sure of what you are doing by setting a pcap filter.</dl>
</dl>
<dt><code>Options</code></p>
<dd>
<dl>
<dd>
<dl>
<dt><code>Unoffensive </code></p>
<dd>This enable/disable the unoffensive flag. The asterisk &#8216;*&#8217; means &quot;the option is enabled&quot;. Otherwise the option is not enabled.</p>
<dt><code>Promisc mode</code></p>
<dd>Enable/disable the promisc mode for the live capture on a network interface. This is an &quot;asterisk-option&quot; as the unoffensive one.</p>
<dt><code>Set netmask</code></p>
<dd>Use the specified netmask instead of the one associated with the current iface. This option is useful if you have the NIC with an associated netmask of class B and you want to scan (with the arp scan) only a C class.</dl>
</dl>
</dl>
<h2>The Interesting Part</h2>
<p>Once you have selected an offline sniffing or a live capture, the upper menu is modified and you can start to do the interesting things&#8230;<br />
 Some of the following menu are only available in live capture. </p>
<dl>
<dt><code>Start</code></p>
<dd>
<dl>
<dd>
<dl>
<dt><code>Start sniffing</code></p>
<dd>Starts the sniffing process depending on what you have selected on startup (live or from file)</p>
<dt><code>Stop sniffing</code></p>
<dd>Stops the sniffing thread.</p>
<dt><code>Exit</code></p>
<dd>Returns to your favourite shell ;)</dl>
</dl>
<dt><code>Targets</code></p>
<dd>
<dl>
<dd>
<dl>
<dt><code>Current Targets</code></p>
<dd>Displays a list of hosts in each TARGET. You can selectively remove a host by selecting it and press &#8216;d&#8217; or add a new host pressing &#8216;a&#8217;. To switch between the two lists, use the ARROWS keys.</p>
<dt><code>Select TARGET(s)</code></p>
<dd>Lets you select the TARGET(s) as explained in <a href="/docs/linux/man/8-ettercap/">ettercap</a>(8). The syntax is the same as for the command line specification.</p>
<dt><code>Protocol&#8230;</code></p>
<dd>You can choose to sniff only TCP, only UDP or both (ALL).</p>
<dt><code>Reverse matching</code></p>
<dd>Reverse the matching of a packet. It is equivalent to a NOT before the target specification.</p>
<dt><code>Wipe Targets</code></p>
<dd>Restores both TARGETS to ANY/ANY/ANY</dl>
</dl>
<dt><code>Hosts</code></p>
<dd>
<dl>
<dd>
<dl>
<dt><code>Hosts list</code></p>
<dd>Displays the list of hosts detected through an ARP scan or converted from the passive profiles. This list is used by MITM attacks when the ANY target is selected, so if you want to exclude a host from the attack, simply delete it from the list.<br />
 You can remove a host from the list by pressing &#8216;d&#8217;, add it to TARGET1 by pressing &#8216;1&#8217; or add it to TARGET2 by pressing &#8216;2&#8217;.</p>
<dt><code>Scan for hosts</code></p>
<dd>Perform the ARP scan of the netmask if no TARGETS are selected. If TARGETS was specified it only scans for those hosts.</p>
<dt><code>Load from file&#8230;</code></p>
<dd>Loads the hosts list from a file previously saved with &quot;save to file&quot; or hand crafted.</p>
<dt><code>Save to file&#8230;</code></p>
<dd>Save the current hosts list to a file.</dl>
</dl>
<dt><code>View</code></p>
<dd>
<dl>
<dd>
<dl>
<dt><code>Connections</code></p>
<dd>Displays the connection list. To see detailed information about a connection press &#8216;d&#8217;, or press &#8216;k&#8217; to kill it. To see the traffic for a specific connection, select it and press enter. Once the two-panel interface is displayed you can move the focus with the arrow keys. Press &#8216;j&#8217; to switch between joined and splitted visualization. Press &#8216;k&#8217; to kill the connection. Press &#8216;y&#8217; to inject interactively and &#8216;Y&#8217; to inject a file. Note that it is important which panel has the focus as the injected data will be sent to that address.<br />
 HINT: connections marked with an asterisk contain account(s) information.</p>
<dt><code>Profiles</code></p>
<dd>Diplays the passive profile hosts list. Selecting a host will display the relative details (including account with user and pass for that host).<br />
 You can convert the passive profile list into the hosts list by pressing &#8216;c&#8217;. To purge remote hosts, press &#8216;l&#8217;. To purge local hosts, press &#8216;r&#8217;. You can also dump the current profile to a file by pressing &#8216;d&#8217;; the dumped file can be opened with <a href="/docs/linux/man/8-etterlog/">etterlog</a>(8).<br />
 HINT: profiles marked with an asterisk contain account(s) information.</p>
<dt><code>Statistics</code></p>
<dd>Displays some statistics about the sniffing process.</p>
<dt><code>Resolve IP addresses</code></p>
<dd>Enables DNS resolution for all the sniffed IP address. CAUTION: this will extremely slow down ettercap. By the way the passive dns resolution is always active. It sniffs dns replies and stores them in a cache. If an ip address is present in that cache, it will be automatically resolved. It is dns resolution for free&#8230; ;)</p>
<dt><code>Visualization method</code></p>
<dd>Change the visualization method for the sniffed data. Available methods: ascii, hex, ebcdic, text, html.</p>
<dt><code>Visualization regex</code></p>
<dd>Set the visualization regular expression. Only packets matching this regex will be displayed in the connection data window.</p>
<dt><code>Set the WEP key</code></p>
<dd>Set the WEP key used to decrypt WiFi encrypted packets. See <a href="/docs/linux/man/8-ettercap/">ettercap</a>(8) for the format of the key.</dl>
</dl>
<dt><code>Mitm</code></p>
<dd>
<dl>
<dd>
<dl>
<dt><code>[&#8230;]</code></p>
<dd>For each type of attack, a menu entry is displayed. Simply select the attack you want and fill the arguments when asked. You can activate more than one attack at a time.</p>
<dt><code>Stop mitm attack(s)</code></p>
<dd>Stops all the mitm attacks currently active.</dl>
</dl>
<dt><code>Filters</code></p>
<dd>
<dl>
<dd>
<dl>
<dt><code>Load a filter&#8230;</code></p>
<dd>Load a precompiled filter file. The file must be compiled with <a href="/docs/linux/man/8-etterfilter/">etterfilter</a>(8) before it can be loaded.</p>
<dt><code>Stop filtering</code></p>
<dd>Unload the filter and stop filtering the connections.</dl>
</dl>
<dt><code>Logging</code></p>
<dd>
<dl>
<dd>
<dl>
<dt><code>Log all packets and infos&#8230;</code></p>
<dd>Given a file name, it will create two files: filename.eci (for information about hosts) and filename.ecp (for all the interesting packets). This is the same as the -L option.</p>
<dt><code>Log only infos&#8230;</code></p>
<dd>This is used only to sniff information about hosts (same as the -l option).</p>
<dt><code>Stop logging info</code></p>
<dd>Come on&#8230; it is self explanatory.</p>
<dt><code>Log user messages&#8230;</code></p>
<dd>Will log all the messages appearing in the bottom window (same as -m option).</p>
<dt><code>Compressed file</code></p>
<dd>Asterisk-option to control whether or not the logfile should be compressed.</dl>
</dl>
<dt><code>Plugins</code></p>
<dd>
<dl>
<dd>
<dl>
<dt><code>Manage the plugins</code></p>
<dd>Opens the plugin management window. You can select a plugin and activate it by pressing &#8216;enter&#8217;. Plugins already active can be recognized by the [1] symbol instead of [0]. If you select an active plugin, it will be deactivated.</p>
<dt><code>Load a plugin&#8230;</code></p>
<dd>You can load a plugin file that is not in the default search path. (remember that you can browse directories with EC_UID permissions).</dl>
</dl>
</dl>
<h2>See Also</h2>
<p><i><a href="/docs/linux/man/8-ettercap/">ettercap</a>(8)</i> <i><a href="/docs/linux/man/8-ettercap_plugins/">ettercap_plugins</a>(8)</i> <i><a href="/docs/linux/man/8-etterlog/">etterlog</a>(8)</i> <i><a href="/docs/linux/man/8-etterfilter/">etterfilter</a>(8)</i> <i><a href="/docs/linux/man/5-etter-conf/">etter.conf</a>(5)</i> </p>
