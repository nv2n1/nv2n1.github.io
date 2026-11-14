---
title: "wvdial(5)"
name: "wvdial"
section: "5"
letter: "w"
url: "/docs/linux/man/5-wvdial/"
description: "wvdial.conf – wvdial configuration file"
---

<p>wvdial.conf &#8211; wvdial configuration file</p>
<h2>Description</h2>
<p>When <code>wvdial</code> starts, it first loads its configuration from <i>/etc/wvdial.conf</i>, which contains basic information about the modem port, speed, and init string, along with information about your Internet Service Provider (ISP), such as the phone number, your username, and your password. </p>
<p> The configuration file <i>/etc/wvdial.conf</i> is in Windows &quot;ini&quot; file format, with <code>sections</code> named in square brackets and a number of <code>variable = value</code> pairs within each section. </p>
<p> Here is a sample configuration file: </p>
<dl>
<dd>[Dialer Defaults]<br />
 Modem = /dev/ttyS2<br />
 Baud = 57600<br />
 Init = ATZ<br />
 Init2 = AT S11=50<br />
 Phone = 555-4242<br />
 Username = apenwarr<br />
 Password = my-password </p>
<p> [Dialer phone2]<br />
 Phone = 555-4243 </p>
<p> [Dialer shh]<br />
 Init3 = ATM0 </p>
<p> [Dialer pulse]<br />
 Dial Command = ATDP</dl>
<p> The sample configuration file above contains all of the options necessary to run the two sample command lines given above. Here is a complete list of settings that <code>wvdial</code> understands:</p>
<dl>
<dt><i>Modem</i></p>
<dd>The location of the device that <code>wvdial</code> should use as your modem. The default is <code>/dev/modem</code>.</p>
<dt><i>Baud</i></p>
<dd>The speed at which <code>wvdial</code> will communicate with your modem. The default is 57600 baud.</p>
<dt><i>Init1 &#8230; Init9</i></p>
<dd><code>wvdial</code> can use up to nine initialization strings to set up your modem. Before dialing, these strings are sent to the modem in numerical order. These are particularly useful when specifying multiple sections. See above for an example that uses Init3 to turn the modem&#8217;s speaker off. The default is &quot;ATZ&quot; for Init1.</p>
<dt><i>Phone</i></p>
<dd>The phone number you want <code>wvdial</code> to dial. You can add up to 9 other phone numbers that <code>wvdial</code> will dial in order, by adding:</p>
<dt><i>Phone1</i></p>
<dd>
<dt><i>Phone2</i></p>
<dd>
<dt><i>Phone3</i></p>
<dd>
<dt><i>Phone4</i></p>
<dd>
<dt><i>Phone5</i></p>
<dd>
<dt><i>Phone6</i></p>
<dd>
<dt><i>Phone7</i></p>
<dd>
<dt><i>Phone8</i></p>
<dd>
<dt><i>Phone9</i></p>
<dd>
<dt><i>Dial Prefix</i></p>
<dd><code>wvdial</code> will insert this string after the dial command and before the phone number. For example, to disable call waiting (in North America, anyway) set this to &quot;*70,&quot;.</p>
<dt><i>Dial Command</i></p>
<dd><code>wvdial</code> will use this string to tell the modem to dial. The default is &quot;ATDT&quot;.</p>
<dt><i>Username</i></p>
<dd>You must set this to the username you use at your ISP.</p>
<dt><i>Login Prompt</i></p>
<dd>If your ISP has an unusual login procedure that <code>wvdial</code> is unable to figure out, you can use this option to specify a login prompt. When this prompt is received from your ISP, <code>wvdial</code> will send the <code>Login</code> string.</p>
<dt><i>Password</i></p>
<dd>You must set this to the password you use at your ISP.</p>
<dt><i>Ask Password</i></p>
<dd>By setting this option <code>wvdial</code> will prompt for your password on every dialin. Thus you don&#8217;t have to save your password in <i>/etc/wvdial.conf</i>. (Option added by SuSE.)</p>
<dt><i>Password Prompt</i></p>
<dd>If your ISP has an unusual login procedure that <code>wvdial</code> is unable to figure out, you can use this option to specify a password prompt. When this prompt is received from you ISP, <code>wvdial</code> will send the <code>Password</code> string.</p>
<dt><i>PPPD Path</i></p>
<dd>If your system has pppd somewhere other than <code>/usr/sbin/pppd</code>, you will need to set this option.</p>
<dt><i>Auto DNS</i></p>
<dd>Try to get the Domain Nameserver (DNS) from the provider. This option is &quot;on&quot; by default. (Option added by SuSE.)</p>
<dt><i>Check DNS</i></p>
<dd>Check the Domain Nameserver (DNS) after the connection has been set up. This option is &quot;on&quot; by default. (Option added by SuSE.)</p>
<dt><i>DNS Test1</i></p>
<dd>First DNS lookup for DNS check. (Option added by SuSE.)</p>
<dt><i>DNS Test2</i></p>
<dd>Second DNS lookup for DNS check. (Option added by SuSE.)</p>
<dt><i>Check Def Route</i></p>
<dd>Check the default route after the connection has been set up. This option is &quot;on&quot; by default. (Option added by SuSE.)</p>
<dt><i>Force Address</i></p>
<dd>This option only applies if you have a static IP address at your ISP, and even then you probably don&#8217;t need it. Some ISP&#8217;s don&#8217;t send the IP address as part of the PPP negotiation. This option forces pppd to use the address you give it.</p>
<dt><i>Remote Name</i></p>
<dd>If your ISP uses PAP or CHAP authentication, you might need to change this to your ISP&#8217;s authentication name. In most cases, however, it&#8217;s safe to use the default value, &quot;*&quot;.</p>
<dt><i>Carrier Check</i></p>
<dd><code>wvdial</code> checks your modem during the connection process to ensure that it is actually online. If you have a weird modem that insists its carrier line is always down, you can disable the carrier check by setting this option to &quot;no&quot;.</p>
<dt><i>Stupid Mode</i></p>
<dd>When <code>wvdial</code> is in Stupid Mode, it does not attempt to interpret any prompts from the terminal server. It starts pppd immediately after the modem connects. Apparently there are ISP&#8217;s that actually give you a login prompt, but work only if you start PPP, rather than logging in. Go figure. Stupid Mode is (naturally) disabled by default.</p>
<dt><i>New PPPD</i></p>
<dd>You need this option if you have pppd version 2.3.0 or newer, to make wvdial create the file <code>/etc/ppp/peers/wvdial</code>. This option is enabled by default, thus if you have older pppd you need to set it to `no&#8217; (or upgrade pppd).</p>
<dt><i>Default Reply</i></p>
<dd>When <code>wvdial</code> detects a prompt, and it hasn&#8217;t seen any clues that indicate what it should send as a response to the prompt, it defaults to sending &quot;ppp&quot;. Sometimes this is inadequate. Use this option to override <code>wvdial</code>&#8216;s default prompt response.</p>
<dt><i>Auto Reconnect</i></p>
<dd>If enabled, <code>wvdial</code> will attempt to automatically reestablish a connection if you are randomly disconnected by the other side. This option is &quot;on&quot; by default.</p>
<dt><i>Idle Seconds</i></p>
<dd>Set the hangup timeout in seconds. If there is inactivity for the given time the connection is shut down. A hangup timeout of 0 disables this feature.</p>
<dt><i>Abort on Busy</i></p>
<dd>If enabled, <code>wvdial</code> will not retry the connection if the modem says that the line is busy. This option is &quot;off&quot; by default.</p>
<dt><i>Abort on No Dialtone</i></p>
<dd>If enabled, <code>wvdial</code> will not retry the connection if the modem says that there is no dialtone. This option is &quot;on&quot; by default.</p>
<dt><i>Dial Attempts</i></p>
<dd>If value is set, <code>wvdial</code> will quit after that many tries .If set to 0, <code>wvdial</code> will happily keep dialling forever.</p>
<dt><i>Dial Timeout</i></p>
<dd>The maximum time in seconds that <code>wvdial</code> will wait for a connection to be made. Default value is 60 seconds.</dl>
<p> The <code><a href="/docs/linux/man/1-wvdialconf/">wvdialconf</a></code>(1) program can be used to detect your modem and fill in the Modem, Baud, and Init/Init2 options automatically.</p>
<h2>Authors</h2>
<p>Dave Coombs and Avery Pennarun for Net Integration Technologies Inc. Great contributions have been made by many people, including SuSE and RedHat. Thanks guys!</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-wvdial/">wvdial</a></code>(1), <code><a href="/docs/linux/man/1-wvdialconf/">wvdialconf</a></code>(1), <code><a href="/docs/linux/man/8-pppd/">pppd</a></code>(8). </p>
