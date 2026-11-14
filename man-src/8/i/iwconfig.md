---
title: "iwconfig(8)"
name: "iwconfig"
section: "8"
letter: "i"
url: "/docs/linux/man/8-iwconfig/"
description: "iwconfig – configure a wireless network interface"
---

<p>iwconfig &#8211; configure a wireless network interface</p>
<h2>Synopsis</h2>
<p><code>iwconfig [</code><i>interface</i><code>]</code><br />
 <code>iwconfig </code><i>interface</i><code> [essid </code><i>X</i><code>] [nwid </code><i>N</i><code>] [mode </code><i>M</i><code>] [freq </code><i>F</i><code>]</code><br />
 <code> [channel </code><i>C</i><code>]</code><i>[sens</i><code> S ]</code><i>[ap</i><code> A ]</code><i>[nick</i><code> NN ]</code><br />
 <code> [rate </code><i>R</i><code>] [rts </code><i>RT</i><code>] [frag </code><i>FT</i><code>] [txpower </code><i>T</i><code>]</code><br />
 <code> [enc </code><i>E</i><code>] [key </code><i>K</i><code>] [power </code><i>P</i><code>] [retry </code><i>R</i><code>]</code><br />
 <code> [modu </code><i>M</i><code>] [commit]</code><br />
 <code>iwconfig &#8211;help</code><br />
 <code>iwconfig &#8211;version</code></p>
<h2>Description</h2>
<p><code>Iwconfig</code> is similar to <i><a href="/docs/linux/man/8-ifconfig/">ifconfig</a></i>(8), but is dedicated to the wireless interfaces. It is used to set the parameters of the network interface which are specific to the wireless operation (for example : the frequency). <code>Iwconfig</code> may also be used to display those parameters, and the wireless statistics (extracted from <i>/proc/net/wireless</i>). </p>
<p> All these parameters and statistics are device dependent. Each driver will provide only some of them depending on hardware support, and the range of values may change. Please refer to the man page of each device for details.</p>
<h2>Parameters</h2>
<dl>
<dt><code>essid</code></p>
<dd>Set the ESSID (or Network Name &#8211; in some products it may also be called Domain ID). The ESSID is used to identify cells which are part of the same virtual network.<br />
 As opposed to the AP Address or NWID which define a single cell, the ESSID defines a group of cells connected via repeaters or infrastructure, where the user may roam transparently.<br />
 With some cards, you may disable the ESSID checking (ESSID promiscuous) with <i>off</i> or <i>any</i> (and <i>on</i> to reenable it).<br />
 If the ESSID of your network is one of the special keywords (<i>off</i>, <i>on</i> or <i>any</i>), you should use <i>&#8212;</i> to escape it.<br />
 <code>Examples :</code><br />
 <i><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>iwconfig eth0 essid any</i><br />
 <i><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>iwconfig eth0 essid My Network</i><br />
 <i><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>iwconfig eth0 essid &#8212; ANY</i></p>
<dt><code>nwid</code></p>
<dd>Set the Network ID. As all adjacent wireless networks share the same<br />
 medium, this parameter is used to differentiate them (create logical colocated networks) and identify nodes belonging to the same cell.<br />
 This parameter is only used for pre-802.11 hardware, the 802.11 protocol uses the ESSID and AP Address for this function.<br />
 With some cards, you may disable the Network ID checking (NWID promiscuous) with <i>off</i> (and <i>on</i> to reenable it).<br />
 <code>Examples :</code><br />
 <i><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>iwconfig eth0 nwid AB34</i><br />
 <i><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>iwconfig eth0 nwid off</i></p>
<dt><code>nick</code>[name]</p>
<dd>Set the nickname, or the station name. Some 802.11 products do define<br />
 it, but this is not used as far as the protocols (MAC, IP, TCP) are concerned and completely useless as far as configuration goes. Only some wireless diagnostic tools may use it.<br />
 <code>Example :</code><br />
 <i><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>iwconfig eth0 nickname My Linux Node</i></p>
<dt><code>mode</code></p>
<dd>Set the operating mode of the device, which depends on the network<br />
 topology. The mode can be <i>Ad-Hoc</i> (network composed of only one cell and without Access Point), <i>Managed</i> (node connects to a network composed of many Access Points, with roaming), <i>Master</i> (the node is the synchronisation master or acts as an Access Point), <i>Repeater</i> (the node forwards packets between other wireless nodes), <i>Secondary</i> (the node acts as a backup master/repeater), <i>Monitor</i> (the node is not associated with any cell and passively monitor all packets on the frequency) or <i>Auto</i>.<br />
 <code>Example :</code><br />
 <i><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>iwconfig eth0 mode Managed</i><br />
 <i><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>iwconfig eth0 mode Ad-Hoc</i></p>
<dt><code>freq</code>/<code>channel</code></p>
<dd>Set the operating frequency or channel in the device. A value below<br />
 1000 indicates a channel number, a value greater than 1000 is a frequency in Hz. You may append the suffix k, M or G to the value (for example, &quot;2.46G&quot; for 2.46 GHz frequency), or add enough &#8216;0&#8217;.<br />
 Channels are usually numbered starting at 1, and you may use <i><a href="/docs/linux/man/8-iwlist/">iwlist</a></i>(8) to get the total number of channels, list the available frequencies, and display the current frequency as a channel. Depending on regulations, some frequencies/channels may not be available.<br />
 When using Managed mode, most often the Access Point dictates the channel and the driver may refuse the setting of the frequency. In Ad-Hoc mode, the frequency setting may only be used at initial cell creation, and may be ignored when joining an existing cell.<br />
 You may also use <i>off</i> or <i>auto</i> to let the card pick up the best channel (when supported).<br />
 <code>Examples :</code><br />
 <i><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>iwconfig eth0 freq 2422000000</i><br />
 <i><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>iwconfig eth0 freq 2.422G</i><br />
 <i><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>iwconfig eth0 channel 3</i><br />
 <i><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>iwconfig eth0 channel auto</i></p>
<dt><code>ap</code></p>
<dd>Force the card to register to the Access Point given by the address,<br />
 if it is possible. This address is the cell identity of the Access Point, as reported by wireless scanning, which may be different from its network MAC address. If the wireless link is point to point, set the address of the other end of the link. If the link is ad-hoc, set the cell identity of the ad-hoc network.<br />
 When the quality of the connection goes too low, the driver may revert back to automatic mode (the card selects the best Access Point in range).<br />
 You may also use <i>off</i> to re-enable automatic mode without changing the current Access Point, or you may use <i>any</i> or <i>auto</i> to force the card to reassociate with the currently best Access Point.<br />
 <code>Example :</code><br />
 <i><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>iwconfig eth0 ap 00:60:1D:01:23:45</i><br />
 <i><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>iwconfig eth0 ap any</i><br />
 <i><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>iwconfig eth0 ap off</i></p>
<dt><code>rate</code>/<code>bit</code>[rate]</p>
<dd>For cards supporting multiple bit rates, set the bit-rate in b/s. The<br />
 bit-rate is the speed at which bits are transmitted over the medium, the user speed of the link is lower due to medium sharing and various overhead.<br />
 You may append the suffix k, M or G to the value (decimal multiplier : 10^3, 10^6 and 10^9 b/s), or add enough &#8216;0&#8217;. Values below 1000 are card specific, usually an index in the bit-rate list. Use <i>auto</i> to select automatic bit-rate mode (fallback to lower rate on noisy channels), which is the default for most cards, and <i>fixed</i> to revert back to fixed setting. If you specify a bit-rate value and append <i>auto</i>, the driver will use all bit-rates lower and equal than this value.<br />
 <code>Examples :</code><br />
 <i><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>iwconfig eth0 rate 11M</i><br />
 <i><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>iwconfig eth0 rate auto</i><br />
 <i><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>iwconfig eth0 rate 5.5M auto</i></p>
<dt><code>txpower</code></p>
<dd>For cards supporting multiple transmit powers, sets the transmit power<br />
 in dBm. If <i>W</i> is the power in Watt, the power in dBm is <i>P = 30 + 10.log(W)</i>. If the value is postfixed by <i>mW</i>, it will be automatically converted to dBm.<br />
 In addition, <i>on</i> and <i>off</i> enable and disable the radio, and <i>auto</i> and <i>fixed</i> enable and disable power control (if those features are available).<br />
 <code>Examples :</code><br />
 <i><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>iwconfig eth0 txpower 15</i><br />
 <i><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>iwconfig eth0 txpower 30mW</i><br />
 <i><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>iwconfig eth0 txpower auto</i><br />
 <i><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>iwconfig eth0 txpower off</i></p>
<dt><code>sens</code></p>
<dd>Set the sensitivity threshold. This define how sensitive is the card<br />
 to poor operating conditions (low signal, interference). Positive values are assumed to be the raw value used by the hardware or a percentage, negative values are assumed to be dBm. Depending on the hardware implementation, this parameter may control various functions.<br />
 On modern cards, this parameter usually control handover/roaming threshold, the lowest signal level for which the hardware remains associated with the current Access Point. When the signal level goes below this threshold the card starts looking for a new/better Access Point. Some cards may use the number of missed beacons to trigger this. For high density of Access Points, a higher threshold make sure the card is always associated with the best AP, for low density of APs, a lower threshold minimise the number of failed handoffs.<br />
 On more ancient card this parameter usually controls the defer threshold, the lowest signal level for which the hardware considers the channel busy. Signal levels above this threshold make the hardware inhibits its own transmission whereas signals weaker than this are ignored and the hardware is free to transmit. This is usually strongly linked to the receive threshold, the lowest signal level for which the hardware attempts packet reception. Proper setting of these thresholds prevent the card to waste time on background noise while still receiving weak transmissions. Modern designs seems to control those thresholds automatically. </p>
<p> <code>Example :</code><br />
 <i><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>iwconfig eth0 sens -80</i><br />
 <i><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>iwconfig eth0 sens 2</i></p>
<dt><code>retry</code></p>
<dd>Most cards have MAC retransmissions, and some allow to set the<br />
 behaviour of the retry mechanism.<br />
 To set the maximum number of retries, enter <i>limit `value&#8217;</i>. This is an absolute value (without unit), and the default (when nothing is specified). To set the maximum length of time the MAC should retry, enter <i>lifetime `value&#8217;</i>. By defaults, this value is in seconds, append the suffix m or u to specify values in milliseconds or microseconds.<br />
 You can also add the <i>short</i>, <i>long</i>, <i>min</i> and <i>max</i> modifiers. If the card supports automatic mode, they define the bounds of the limit or lifetime. Some other cards define different values depending on packet size, for example in 802.11 <i>min limit</i> is the short retry limit (non RTS/CTS packets).<br />
 <code>Examples :</code><br />
 <i><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>iwconfig eth0 retry 16</i><br />
 <i><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>iwconfig eth0 retry lifetime 300m</i><br />
 <i><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>iwconfig eth0 retry short 12</i><br />
 <i><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>iwconfig eth0 retry min limit 8</i></p>
<dt><code>rts</code>[_threshold]</p>
<dd>RTS/CTS adds a handshake before each packet transmission to make sure<br />
 that the channel is clear. This adds overhead, but increases performance in case of hidden nodes or a large number of active nodes. This parameter sets the size of the smallest packet for which the node sends RTS ; a value equal to the maximum packet size disables the mechanism. You may also set this parameter to <i>auto</i>, <i>fixed</i> or <i>off</i>.<br />
 <code>Examples :</code><br />
 <i><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>iwconfig eth0 rts 250</i><br />
 <i><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>iwconfig eth0 rts off</i></p>
<dt><code>frag</code>[mentation_threshold]</p>
<dd>Fragmentation allows to split an IP packet in a burst of smaller<br />
 fragments transmitted on the medium. In most cases this adds overhead, but in a very noisy environment this reduces the error penalty and allow packets to get through interference bursts. This parameter sets the maximum fragment size which is always lower than the maximum packet size.<br />
 This parameter may also control Frame Bursting available on some cards, the ability to send multiple IP packets together. This mechanism would be enabled if the fragment size is larger than the maximum packet size.<br />
 You may also set this parameter to <i>auto</i>, <i>fixed</i> or <i>off</i>.<br />
 <code>Examples :</code><br />
 <i><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>iwconfig eth0 frag 512</i><br />
 <i><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>iwconfig eth0 frag off</i></p>
<dt><code>key</code>/<code>enc</code>[ryption]</p>
<dd>Used to manipulate encryption or scrambling keys and security mode.</p>
<p> To set the current encryption key, just enter the key in hex digits as <i>XXXX-XXXX-XXXX-XXXX</i> or <i>XXXXXXXX</i>. To set a key other than the current key, prepend or append <i>[index]</i> to the key itself (this won&#8217;t change which is the active key). You can also enter the key as an ASCII string by using the <i>s:</i> prefix. Passphrase is currently not supported.<br />
 To change which key is the currently active key, just enter <i>[index]</i> (without entering any key value).<br />
 <i>off</i> and <i>on</i> disable and reenable encryption.<br />
 The security mode may be <i>open</i> or <i>restricted</i>, and its meaning depends on the card used. With most cards, in <i>open</i> mode no authentication is used and the card may also accept non-encrypted sessions, whereas in <i>restricted</i> mode only encrypted sessions are accepted and the card will use authentication if available.<br />
 If you need to set multiple keys, or set a key and change the active key, you need to use multiple <code>key</code> directives. Arguments can be put in any order, the last one will take precedence.<br />
 <code>Examples :</code><br />
 <i><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>iwconfig eth0 key 0123-4567-89</i><br />
 <i><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>iwconfig eth0 key [3] 0123-4567-89</i><br />
 <i><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>iwconfig eth0 key s:password [2]</i><br />
 <i><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>iwconfig eth0 key [2]</i><br />
 <i><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>iwconfig eth0 key open</i><br />
 <i><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>iwconfig eth0 key off</i><br />
 <i><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>iwconfig eth0 key restricted [3] 0123456789</i><br />
 <i><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>iwconfig eth0 key 01-23 key 45-67 [4] key [4]</i></p>
<dt><code>power</code></p>
<dd>Used to manipulate power management scheme parameters and mode.</p>
<p> To set the period between wake ups, enter <i>period `value&#8217;</i>. To set the timeout before going back to sleep, enter <i>timeout `value&#8217;</i>. To set the generic level of power saving, enter <i>saving `value&#8217;</i>. You can also add the <i>min</i> and <i>max</i> modifiers. By default, those values are in seconds, append the suffix m or u to specify values in milliseconds or microseconds. Sometimes, those values are without units (number of beacon periods, dwell, percentage or similar).<br />
 <i>off</i> and <i>on</i> disable and reenable power management. Finally, you may set the power management mode to <i>all</i> (receive all packets), <i>unicast</i> (receive unicast packets only, discard multicast and broadcast) and <i>multicast</i> (receive multicast and broadcast only, discard unicast packets).<br />
 <code>Examples :</code><br />
 <i><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>iwconfig eth0 power period 2</i><br />
 <i><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>iwconfig eth0 power 500m unicast</i><br />
 <i><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>iwconfig eth0 power timeout 300u all</i><br />
 <i><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>iwconfig eth0 power saving 3</i><br />
 <i><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>iwconfig eth0 power off</i><br />
 <i><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>iwconfig eth0 power min period 2 power max period 4</i></p>
<dt><code>modu</code>[lation]</p>
<dd>Force the card to use a specific set of modulations. Modern cards<br />
 support various modulations, some which are standard, such as 802.11b or 802.11g, and some proprietary. This command force the card to only use the specific set of modulations listed on the command line. This can be used to fix interoperability issues.<br />
 The list of available modulations depend on the card/driver and can be displayed using <i>iwlist modulation</i>. Note that some card/driver may not be able to select each modulation listed independently, some may come as a group. You may also set this parameter to <i>auto</i> let the card/driver do its best.<br />
 <code>Examples :</code><br />
 <i><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>iwconfig eth0 modu 11g</i><br />
 <i><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>iwconfig eth0 modu CCK OFDMa</i><br />
 <i><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>iwconfig eth0 modu auto</i></p>
<dt><code>commit</code></p>
<dd>Some cards may not apply changes done through Wireless Extensions<br />
 immediately (they may wait to aggregate the changes or apply it only when the card is brought up via <i>ifconfig</i>). This command (when available) forces the card to apply all pending changes.<br />
 This is normally not needed, because the card will eventually apply the changes, but can be useful for debugging.</dl>
<h2>Display</h2>
<p>For each device which supports wireless extensions, <i>iwconfig</i> will display the name of the <code>MAC protocol</code> used (name of device for proprietary protocols), the <code>ESSID</code> (Network Name), the <code>NWID</code>, the <code>frequency</code> (or channel), the <code>sensitivity</code>, the <code>mode</code> of operation, the <code>Access Point</code> address, the <code>bit-rate</code>, the <code>RTS threshold</code>, the <code>fragmentation threshold</code>, the <code>encryption key</code> and the <code>power management</code> settings (depending on availability). </p>
<p> The parameters displayed have the same meaning and values as the parameters you can set, please refer to the previous part for a detailed explanation of them.<br />
 Some parameters are only displayed in short/abbreviated form (such as encryption). You may use <i><a href="/docs/linux/man/8-iwlist/">iwlist</a></i>(8) to get all the details.<br />
 Some parameters have two modes (such as bitrate). If the value is prefixed by `<code>=</code>&#8216;, it means that the parameter is fixed and forced to that value, if it is prefixed by `<code>:</code>&#8216;, the parameter is in automatic mode and the current value is shown (and may change).</p>
<dl>
<dt><code>Access Point</code>/<code>Cell</code></p>
<dd>An address equal to 00:00:00:00:00:00 means that the card failed to associate with an Access Point (most likely a configuration issue). The <code>Access Point</code> parameter will be shown as <code>Cell</code> in ad-hoc mode (for obvious reasons), but otherwise works the same.</dl>
<p> If <i>/proc/net/wireless</i> exists, <i>iwconfig</i> will also display its content. Note that those values will depend on the driver and the hardware specifics, so you need to refer to your driver documentation for proper interpretation of those values.</p>
<dl>
<dt><code>Link quality</code></p>
<dd>Overall quality of the link. May be based on the level of contention or interference, the bit or frame error rate, how good the received signal is, some timing synchronisation, or other hardware metric. This is an aggregate value, and depends totally on the driver and hardware.</p>
<dt><code>Signal level</code></p>
<dd>Received signal strength (RSSI &#8211; how strong the received signal is). May be arbitrary units or dBm, <i>iwconfig</i> uses driver meta information to interpret the raw value given by <i>/proc/net/wireless</i> and display the proper unit or maximum value (using 8 bit arithmetic). In <i>Ad-Hoc</i> mode, this may be undefined and you should use <i>iwspy</i>.</p>
<dt><code>Noise level</code></p>
<dd>Background noise level (when no packet is transmitted). Similar comments as for <code>Signal level</code>.</p>
<dt><code>Rx invalid nwid</code></p>
<dd>Number of packets received with a different NWID or ESSID. Used to detect configuration problems or adjacent network existence (on the same frequency).</p>
<dt><code>Rx invalid crypt</code></p>
<dd>Number of packets that the hardware was unable to decrypt. This can be used to detect invalid encryption settings.</p>
<dt><code>Rx invalid frag</code></p>
<dd>Number of packets for which the hardware was not able to properly re-assemble the link layer fragments (most likely one was missing).</p>
<dt><code>Tx excessive retries</code></p>
<dd>Number of packets that the hardware failed to deliver. Most MAC protocols will retry the packet a number of times before giving up.</p>
<dt><code>Invalid misc</code></p>
<dd>Other packets lost in relation with specific wireless operations.</p>
<dt><code>Missed beacon</code></p>
<dd>Number of periodic beacons from the Cell or the Access Point we have missed. Beacons are sent at regular intervals to maintain the cell coordination, failure to receive them usually indicates that the card is out of range.</dl>
<h2>Author</h2>
<p>Jean Tourrilhes &#8211; jt [at] hpl.hp.com</p>
<h2>Files</h2>
<p><i>/proc/net/wireless</i></p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-ifconfig/">ifconfig</a></code>(8), <code><a href="/docs/linux/man/8-iwspy/">iwspy</a></code>(8), <code><a href="/docs/linux/man/8-iwlist/">iwlist</a></code>(8), <code><a href="/docs/linux/man/8-iwevent/">iwevent</a></code>(8), <code><a href="/docs/linux/man/8-iwpriv/">iwpriv</a></code>(8), <code><a href="/docs/linux/man/7-wireless/">wireless</a></code>(7). </p>
