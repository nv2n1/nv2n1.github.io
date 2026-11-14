---
title: "capiplugin(8)"
name: "capiplugin"
section: "8"
letter: "c"
url: "/docs/linux/man/8-capiplugin/"
description: "capiplugin – Plugin for pppd (Point-to-Point Protocol daemon)"
---

<p>capiplugin &#8211; Plugin for pppd (Point-to-Point Protocol daemon) </p>
<h2>Synopsis</h2>
<p><code>pppd</code> [<i>options</i>] <code>plugin</code> <code>capiplugin.so</code> [<i>options for capiplugin</i>]<br />
 before pppd 2.4.1:<br />
 <code>pppd</code> [<i>options</i>] <code>plugin</code> <code>/usr/lib/pppd/</code><i>&lt;pppd-version&gt;</i>/capiplugin.so [<i>options for capiplugin</i>] </p>
<h2>Description</h2>
<p>The capiplugin provides a method to use PPP over ISDN with ISDN controllers that provide a CAPI2.0 interface. The plugin is responsible for the call setup with CAPI2.0. You can dial out, wait for incoming calls and set up communication over leased lines. It implements a feature to reject an incoming call and callback. This feature can also be used when dialing out. In this case, the party called has to reject the call and call back soon. When using dial-on-demand it is possible let both parties setup the connection, that means while the pppd is in dial-on-demand mode not only an outgoing packet but also an incoming call can trigger the connection setup. This can also combined with callback to assign the cost to one side only (COSO). </p>
<h2>Pppd Versions</h2>
<p>The plugin interface of the pppd is binary incompatible between different version of the pppd. So you need a different capiplugin for every version of the pppd. The different plugins will be in the directory /usr/lib/ppp/<i>&lt;pppd-version&gt;</i>. Since 2.4.1 pppd checks if the version of the plugin matches and also search the plugins in these directories. With pppd versions before 2.4.1 you need to specify the absolute pathname of the plugin.</p>
<h2>How It Works</h2>
<p>The capiplugin registers a new_phase_notifier and its own options to the pppd when loaded. When the pppd goes into phase SERIALCONN, the capiplugin set up a connection and sets the global variable devnam. The capiplugin will register a timer function that is called every second to handle the CAPI messages while pppd is running. To notify pppd when CAPI messages arrive, the CAPI file descriptor is added to the list of file descriptors which the pppd monitors for input. Once the connection is set up the pppd will start PPP negotiation on device devnam. When the pppd enters the DEAD phase, the connection will be dropped (if it is still active) When operating in dial-on-demand mode with wakeup on incoming calls, in phase DORMANT the plugin will setup CAPI2.0 to accept incoming calls. To wakeup pppd when an incoming call arrives, the plugin will generate an UDP packet to the discard port (9) of the gateway, so don&#8217;t filter this packet or wakeup by incoming a call will not work.</p>
<h2>Modes Of Operation</h2>
<dl>
<dt><code>normal dial out</code></p>
<dd>Simply make a connection, for example to your Internet provider.<br />
 Required options: <i>number</i>.<br />
 Recommended options: <i>msn</i>.<br />
 Other possible options: <i>controller</i>, <i>dialmax</i>, <i>dialtimeout</i>, <i>protocol</i> and <i>redialdelay</i>. </p>
<dt><code>dial out with callback</code></p>
<dd>Call a given number, the called party rejects the call and then calls back.<br />
 Required options: <i>number</i> and <i>coso remote</i>.<br />
 Recommended options: <i>cli</i> and <i>msn</i> or <i>inmsn</i>.<br />
 Other possible options: <i>cbwait</i>, <i>controller</i>, <i>connectdelay</i>, <i>dialtimeout</i>, <i>protocol</i> </p>
<dt><code>dial out on demand</code></p>
<dd>Initiate the connection only on demand, i.e. when data traffic is present and drop the connection after a fix amount of idle time.<br />
 Required options: <i>number</i>.<br />
 Required pppd options: <i>demand</i>, <i>connect</i>, <i>idle</i>.<br />
 Recommended options: <i>msn</i>.<br />
 Other possible options: <i>controller</i>, <i>dialmax</i>, <i>dialtimeout</i>, <i>protocol</i> and <i>redialdelay</i>. </p>
<dt><code>dial out on demand on an incoming phone call </code></p>
<dd>Initiate the connection only on demand, i.e. when data traffic is present or an incoming phone call is detected and drop the connection after a fix amount of idle time. This is useful if you are not at home and you want your computer to make an connection to the Internet.<br />
 Required options: <i>number</i> and <i>cli</i>.<br />
 Required options: <i>number</i>, <i>voicecallwakeup</i> and <i>inmsn</i> and/or <i>cli</i>.<br />
 Required pppd options: <i>demand</i>, <i>connect</i>, <i>idle</i>.<br />
 Recommended options: <i>msn</i>. Other possible options: <i>controller</i>, <i>dialmax</i>, <i>dialtimeout</i>, <i>protocol</i>, <i>redialdelay</i> and <i>inmsn</i>. </p>
<dt><code>wait for dial in</code></p>
<dd>Wait for calls and accept incoming calls.<br />
 Recommended options: <i>cli</i> and <i>msn</i> or <i>inmsn</i>.<br />
 Possible options: <i>connectdelay</i>, <i>controller</i>, <i>dialtimeout</i>, <i>protocol</i> </p>
<dt><code>wait for dial in and call back.</code></p>
<dd>Wait for calls, reject the call and then call back.<br />
 Required options: <i>cbnumber</i>.<br />
 Recommended options: <i>cli</i> and <i>msn</i> or <i>inmsn</i>.<br />
 Other possible options: <i>cbdelay</i>, <i>connectdelay</i>, <i>controller</i>, <i>dialtimeout</i>, <i>protocol</i> </p>
<dt><code>dial on demand and also wait for dial in</code></p>
<dd>Initiate the connection only on demand, i.e. when data traffic is present or when the other side dial in and drop the connection after a fix amount of idle time.<br />
 Required options: <i>number</i> and <i>inmsn</i> and/or <i>cli</i>.<br />
 Recommended options: <i>cli</i> and <i>msn</i> or <i>inmsn</i>.<br />
 Optional options: <i>coso caller</i>.<br />
 Other possible options: <i>cbdelay</i>, <i>connectdelay</i>, <i>controller</i>, <i>dialtimeout</i>, <i>protocol</i> </p>
<dt><code>dial on demand and also wait for dial in with COSO.</code></p>
<dd>Initiate the connection only on demand, i.e. when data traffic is present or when the other side dial in and drop the connection after a fix amount of idle time. If option <i>coso local</i> is set, pppd will reject an incoming call from the remote party and will callback. With the option <i>coso remote</i> set, the remote party should reject the incoming call and call back.<br />
 Required options: <i>number</i>, <i>inmsn</i> and/or <i>cli</i>, <i>coso local</i> or <i>coso remote</i>.<br />
 Recommended options: <i>cli</i> and <i>msn</i> or <i>inmsn</i>.<br />
 Other possible options: <i>cbdelay</i>, <i>connectdelay</i>, <i>controller</i>, <i>dialtimeout</i>, <i>protocol</i> </p>
<dt><code>leased line</code></p>
<dd>set up a leased line connection, with or without CAPI channel bundling.<br />
 Required options: <i>channels</i>. Other possible options:<br />
 <i>connectdelay</i>, <i>controller</i>, <i>dialtimeout</i> and <i>protocol</i> </p>
</dl>
<h2>Options</h2>
<dl>
<dt><code>avmadsl</code></p>
<dd>make an DSL connection with the Fritz!Card DSL controller. The parameters for the DSL connection will be loaded from file /etc/drdsl/adsl.conf. This file can be edited or will be created by the program drdsl. </p>
<dt><code>cbdelay </code><i>&lt;seconds&gt;</i></p>
<dd>Number of seconds to wait before callback, when acting as dial-in server with callback. Default value is 2 seconds. </p>
<dt><code>cbnumber </code><i>&lt;phone numbers&gt;</i></p>
<dd>List of phone numbers for callback, separated by commas, when acting as dial-in server with callback. </p>
<dt><code>cbwait </code><i>&lt;seconds&gt;</i></p>
<dd>Time to wait for callback before giving up. Default value is 60 seconds. </p>
<dt><code>channels </code><i>&lt;channel specification&gt;</i></p>
<dd>List of b-channels or ranges to activate leased line mode, separated by commas. </p>
<dt><code>cli </code><i>&lt;phone numbers&gt;</i></p>
<dd>List of numbers from which incoming calls will be accepted, separated by commas. </p>
<dt><code>clicb</code></p>
<dd>The option is retained for compatibility reasons only. Use option <i>coso local</i> or <i>coso remote</i> instead.<br />
 Enable callback mode. When option <i>number</i> is set, call number and wait for callback. When option <i>number</i> is not set, wait for incoming call, reject the call and call back. This option is optional if the <i>cbnumber</i> option is set. </p>
<dt><code>connectdelay </code><i>&lt;seconds&gt;</i></p>
<dd>Number of seconds to wait after a connection is set up, before PPP negotiation starts. Default value is 0 seconds. This option is useful when connecting with protocol <i>modem</i>. Some Internet access servers will hang up if they receive data immediately after the connection is established. </p>
<dt><code>controller </code><i>&lt;controller specification&gt;</i></p>
<dd>For point-to-multipoint <i>&lt;controller specification&gt;</i> is only the CAPI 2.0 controller number, default is 1. For point-to-point, specify <i>&lt;controller number&gt;</i>,<i>&lt;ddi&gt;</i>,<i>&lt;length of internal numbers&gt; </p>
<dt></i><code>controller[1-3] </code><i>&lt;controller specification&gt;</i></p>
<dd>Like option <i>controller</i>. Used to specify more than one controller </p>
<dt><code>coso caller</code></p>
<dd>No callback is done, the costs are assigned to the caller. </p>
<dt><code>coso local</code></p>
<dd>The costs are assigned to the local party. On an incoming call pppd will reject the call and callback. </p>
<dt><code>coso remote</code></p>
<dd>The costs are assigned to the remote party. On an outgoing call the remote party will reject the call and callback. </p>
<dt><code>dialmax </code><i>&lt;times&gt;</i></p>
<dd>Maximum number of times the list of phone numbers is tried before giving up. Default value is 4. </p>
<dt><code>dialtimeout </code><i>&lt;seconds&gt;</i></p>
<dd>Time to wait for the connection to be established or fail before giving up. Default value is 60 seconds. </p>
<dt><code>inmsn </code><i>&lt;msn&gt;</i></p>
<dd>List of phone numbers to monitor for calls, separated by commas. If this option is not set, the value of option <i>msn</i> is used. </p>
<dt><code>inmsn[1-3] </code><i>&lt;msn&gt;</i></p>
<dd>List of phone numbers to monitor for calls on controller specified by option <i>controller[1-3]</i>, separated by commas. If this option is not set, the value of option <i>msn[1-3]</i> is used. </p>
<dt><code>msn </code><i>&lt;msn&gt;</i></p>
<dd>Phone number used to make outgoing calls. Also used for incoming calls if option <i>inmsn</i> is not set. </p>
<dt><code>msn[1-3] </code><i>&lt;msn&gt;</i></p>
<dd>Phone number used to make outgoing calls on controller specified by option <i>controller[1-3]</i>. Also used for incoming calls if option <i>inmsn[1-3]</i> is not set. </p>
<dt><code>number </code><i>&lt;phone numbers&gt;</i></p>
<dd>List of phone numbers to call, separated by commas. Every number in the list is called until a connection can be established. When the end of the list is reached, the first number is called again. See option <i>dialmax</i>. </p>
<dt><code>numberprefix </code><i>&lt;prefix&gt;</i></p>
<dd>phone number to dial to access an outside line. For example, <i>numberprefix 0</i>. </p>
<dt><code>numberprefix[1-3] </code><i>&lt;prefix&gt;</i></p>
<dd>phone number to dial to access an outside line for controller specified by option <i>controller[1-3]</i>. For example, <i>numberprefix1 0</i>. </p>
<dt><code>protocol </code><i>hdlc</i> | <i>x75</i> | <i>v42bis</i> | <i>modem</i> | <i>analogmodem</i> | <i>v110async</i> | <i>v120async</i></p>
<dd>ISDN protocol to use. With <i>hdlc</i> and <i>adskpppoe</i>, the <i>sync</i> option must be added to the pppd. With <i>x75</i>, <i>v42bis</i>, <i>modem</i>, <i>v110async</i> and <i>v120async</i> the <i>sync</i> option MUST NOT be enabled. Default value is <i>hdlc</i>. Not all controllers support <i>v42bis</i>, <i>modem</i> and <i>v120async</i>. Use <a href="/docs/linux/man/8-capiinfo/">capiinfo</a>(8) to view which features your controller supports. </p>
<dt><code>redialdelay </code><i>&lt;seconds&gt;</i></p>
<dd>Number of seconds to wait between redialing. Default value is 5 seconds. </p>
<dt><code>voicewakeup</code></p>
<dd>With this option a incoming voicecall can trigger an outgoing connection setup. </p>
</dl>
<h2>Example For Normal Dial Out</h2>
<p>Probably the most common use of pppd is to dial out to an ISP. This can be specified with a command like</p>
<dl>
<dd>pppd call isp</dl>
<p> where the /etc/ppp/peers/isp file is set up by the system administrator to resemble the following:</p>
<dl>
<dd>sync<br />
 noauth<br />
 defaultroute<br />
 name USERNAME<br />
 plugin capiplugin.so msn MSN<br />
 number PHONENUMBER<br />
 protocol hdlc<br />
 ipcp-accept-local<br />
 ipcp-accept-remote<br />
 /dev/null</dl>
<p> and where the files /etc/ppp/pap-secrets and /etc/ppp/chap-secrets are set up by the system administrator to resemble the following:</p>
<dl>
<dd>USERNAME * PASSWORD * </p>
</dl>
<h2>Example Of Dial Out With Callback</h2>
<p>Dial out with callback can be specified with a command like</p>
<dl>
<dd>pppd call isp-callback</dl>
<p> where the /etc/ppp/peers/isp-callback file is set up by the system administrator to resemble the following:</p>
<dl>
<dd>sync<br />
 noauth<br />
 defaultroute<br />
 name USERNAME<br />
 plugin capiplugin.so<br />
 msn MSN<br />
 number PHONENUMBER<br />
 coso remote<br />
 cli PHONENUMBER<br />
 protocol hdlc<br />
 ipcp-accept-local<br />
 ipcp-accept-remote<br />
 /dev/null</dl>
<p> and where the files /etc/ppp/pap-secrets and /etc/ppp/chap-secrets are set up by the system administrator to resemble the following:<br />
 USERNAME * PASSWORD *</p>
<h2>Example Dial Out On Demand</h2>
<p>To dial out on demand and drop the link after 120 seconds idle time on the link add this line to the /etc/inittab file:</p>
<dl>
<dd>isp:23:respawn:/usr/sbin/pppd call isp demand connect &quot;&quot; idle 120</dl>
<p> where the /etc/ppp/peers/isp file is set up by the system administrator to resemble the following:</p>
<dl>
<dd>sync<br />
 noauth<br />
 defaultroute<br />
 name USERNAME<br />
 plugin capiplugin.so msn MSN<br />
 number PHONENUMBER<br />
 protocol hdlc<br />
 ipcp-accept-local<br />
 ipcp-accept-remote<br />
 /dev/null</dl>
<p> and where the files /etc/ppp/pap-secrets and /etc/ppp/chap-secrets are set up by the system administrator to resemble the following:</p>
<dl>
<dd>USERNAME * PASSWORD * </p>
</dl>
<h2>Example Dial Out On Demand And On An Incoming Phone Call</h2>
<p>To dial out on demand or on an incoming phone call and drop the link after 120 seconds idle time on the link add this line to the /etc/inittab file:</p>
<dl>
<dd>isp:23:respawn:/usr/sbin/pppd call isp demand connect &quot;&quot; idle 120</dl>
<p> where the /etc/ppp/peers/isp file is set up by the system administrator to resemble the following:</p>
<dl>
<dd>sync<br />
 noauth<br />
 defaultroute<br />
 name USERNAME<br />
 plugin capiplugin.so<br />
 msn MSN<br />
 number PHONENUMBER<br />
 cli VOICEPHONENUMBER<br />
 voicecallwakeup<br />
 protocol hdlc<br />
 ipcp-accept-local<br />
 ipcp-accept-remote<br />
 /dev/null</dl>
<p> and where the files /etc/ppp/pap-secrets and /etc/ppp/chap-secrets are set up by the system administrator to resemble the following:</p>
<dl>
<dd>USERNAME * PASSWORD * </p>
</dl>
<h2>Example Dial Out On Demand And Also Accept An Incoming Data Call</h2>
<p>To dial out on demand or on an incoming data call and drop the link after 120 seconds idle time on the link add this line to the /etc/inittab file:</p>
<dl>
<dd>isp:23:respawn:/usr/sbin/pppd call isp demand connect &quot;&quot; idle 120</dl>
<p> where the /etc/ppp/peers/isp file is set up by the system administrator to resemble the following:</p>
<dl>
<dd>sync<br />
 noauth<br />
 defaultroute<br />
 name USERNAME<br />
 plugin capiplugin.so<br />
 msn MSN<br />
 number PHONENUMBER<br />
 inmsn MSN<br />
 protocol hdlc<br />
 ipcp-accept-local<br />
 ipcp-accept-remote<br />
 /dev/null</dl>
<p> and where the files /etc/ppp/pap-secrets and /etc/ppp/chap-secrets are set up by the system administrator to resemble the following:</p>
<dl>
<dd>USERNAME * PASSWORD * </p>
</dl>
<h2>Example Of Wait For Dial In Without Cli Authentication</h2>
<p>Wait for incoming calls, accept them according to options <i>msn</i>, <i>inmsn</i>, and <i>protocol. </p>
<p> Do not provide option cli</i> to the capiplugin. Start a pppd for every b channel. Authorization is checked using PAP or CHAP and the IP addresses are assigned according to the /etc/ppp/pap-secrets or /etc/ppp/chap-secrets file. Assume that the server has IP address 192.168.0.1, the clients are to be assigned IP addresses starting from 192.168.0.2, and the hostname of the server is &quot;dialinserver&quot;. Add these two lines to the /etc/inittab file:</p>
<dl>
<dd>p0:23:respawn:/usr/sbin/pppd call incoming-noncli<br />
 p1:23:respawn:/usr/sbin/pppd call incoming-noncli</dl>
<p> where the /etc/ppp/peers/incoming-noncli file is set up to resemble the following:</p>
<dl>
<dd>sync<br />
 auth<br />
 plugin capiplugin.so<br />
 inmsn MSN<br />
 protocol hdlc 192.168.0.1:</dl>
<p> with the files /etc/ppp/pap-secrets and /etc/ppp/chap-secrets set up to resemble the following:</p>
<dl>
<dd>user1 dialinserver PASSWORD1 192.168.0.2<br />
 user2 dialinserver PASSWORD2 192.168.0.3 </p>
</dl>
<h2>Example Of Wait For Dial In With Cli Authentication</h2>
<p>Wait for incoming calls, accept them according to options <i>msn</i>, <i>inmsn</i>, <i>cli</i> and <i>protocol. </p>
<p> Start a pppd for every client. Assume that the server has IP address 192.168.0.1 and the clients are to be assigned IP addresses starting from 192.168.0.2. Add these three lines to the /etc/inittab file:</p>
<dl>
<dd>p0:23:respawn:/usr/sbin/pppd call incoming-cli cli 04711 192.168.0.1:192.168.0.2<br />
 p1:23:respawn:/usr/sbin/pppd call incoming-cli cli 04712 192.168.0.1:192.168.0.3<br />
 p2:23:respawn:/usr/sbin/pppd call incoming-cli cli 04713 192.168.0.1:192.168.0.4 </p>
</dl>
<p> where the /etc/ppp/peers/incoming-cli file is set up to resemble the following:</p>
<dl>
<dd>sync<br />
 noauth<br />
 plugin capiplugin.so<br />
 inmsn MSN<br />
 protocol hdlc </p>
</dl>
<p> </i></p>
<h2>Example Of Wait For Dial In With Cli Authentication And Callback</h2>
<p>Wait for incoming calls, accept them according to options <i>msn</i>, <i>inmsn</i>, <i>cli</i> and <i>protocol, reject incoming calls and call back. </p>
<p> Start a pppd for every client. Assume that the server has IP address 192.168.0.1 and the clients are to be assigned IP addresses starting from 192.168.0.2. Add these three lines to the /etc/inittab file.</p>
<dl>
<dd>p0:23:respawn:/usr/sbin/pppd call incoming-cli cli 04711 cbnumber 4711 192.168.0.1:192.168.0.2<br />
 p1:23:respawn:/usr/sbin/pppd call incoming-cli cli 04712 cbnumber 4712 192.168.0.1:192.168.0.3<br />
 p2:23:respawn:/usr/sbin/pppd call incoming-cli cli 04713 cbnumber 4713 192.168.0.1:192.168.0.4</dl>
<p> where the /etc/ppp/peers/incoming-cli file is set up to resemble the following:</p>
<dl>
<dd>sync<br />
 noauth<br />
 plugin capiplugin.so<br />
 inmsn MSN<br />
 protocol hdlc </p>
</dl>
<p> </i></p>
<h2>Example Of A Leased Line Connection With Hdlc</h2>
<p>Assume that the server has IP address 192.168.0.1 and the peer has the IP address 192.168.0.2. Add this line to the /etc/inittab file:</p>
<dl>
<dd>p0:23:respawn:/usr/sbin/pppd call leased-hdlc controller 1 channels 1 192.168.0.1:192.168.0.2</dl>
<p> where the /etc/ppp/peers/leased-hdlc file is set up to resemble the following:</p>
<dl>
<dd>sync<br />
 noauth<br />
 lcp-echo-interval 5<br />
 lcp-echo-failure 3<br />
 lcp-max-configure 50<br />
 lcp-max-terminate 2<br />
 noccp<br />
 noipx<br />
 persist<br />
 plugin capiplugin.so<br />
 protocol hdlc </p>
</dl>
<h2>Example Of A Leased Line Connection With V42Bis</h2>
<p>Assume that the server has IP address 192.168.0.1 and the peer has the IP address 192.168.0.2. Add this line to the /etc/inittab file for server 1 (192.168.0.1):</p>
<dl>
<dd>p0:23:respawn:/usr/sbin/pppd call leased-v42bis controller 1 channels 1 192.168.0.1:192.168.0.2</dl>
<p> and this line to the /etc/inittab file for server 1 (192.168.0.2):</p>
<dl>
<dd>p0:23:respawn:/usr/sbin/pppd call leased-v42bis controller 1 channels p1 192.168.0.2:192.168.0.1</dl>
<p> where the /etc/ppp/peers/leased-v42bis file is set up to resemble the following:</p>
<dl>
<dd>sync<br />
 noauth<br />
 lcp-echo-interval 5<br />
 lcp-echo-failure 3<br />
 lcp-max-configure 50<br />
 lcp-max-terminate 2<br />
 noccp<br />
 noipx<br />
 persist<br />
 plugin capiplugin.so<br />
 protocol v42bis </p>
</dl>
<h2>Caveats</h2>
<p>Every pppd awaiting incoming calls can receive an incoming call first. So when two pppds are started to monitor the same MSN, one with CLI Authentication and the other without, the following can happen:</p>
<dl>
<dd>The Client with the CLI specified to the first pppd calls, but the pppd without the <i>cli</i> option receives the call first and accepts it.</dl>
<p> To combine CLI Authentication and PAP/CHAP Authentication, use one MSN for CLI authenticated calls and another for the PAP/CHAP authenticated calls.</p>
<h2>Diagnostics</h2>
<p>Messages are sent to the syslog daemon just as in normal pppd operation; see the pppd manual page.</p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/8-pppd/">pppd</a>(8), <a href="/docs/linux/man/8-capiinfo/">capiinfo</a>(8), <a href="/docs/linux/man/8-capiinit/">capiinit</a>(8), <a href="/docs/linux/man/8-capictrl/">capictrl</a>(8) </p>
<h2>Authors</h2>
<p>Carsten Paeth (calle [at] calle.in-berlin.de)<br />
 AVM GmbH Berlin (info [at] avm.de)</p>
