---
title: "connman(8)"
name: "connman"
section: "8"
letter: "c"
url: "/docs/linux/man/8-connman/"
description: "ConnMan – network management daemon"
---

<p>ConnMan &#8211; network management daemon</p>
<h2>Synopsis</h2>
<p><code>connmand [&#8211;version] | [&#8211;help]</code> </p>
<p> <code>connmand [&#8211;config=&lt;filename&gt;] [&#8211;debug=&lt;file1&gt;:&lt;file2&gt;:&#8230;] [&#8211;device=&lt;interface1&gt;,&lt;interface2&gt;,&#8230;] [&#8211;nodevice=&lt;interface1&gt;,&lt;interface2&gt;,..] [&#8211;wifi=&lt;driver1&gt;,&lt;driver2&gt;,&#8230;] [&#8211;plugin=&lt;plugin1&gt;,&lt;plugin2&gt;,&#8230;] [&#8211;noplugin=&lt;plugin1&gt;,&lt;plugin2&gt;,&#8230;] [&#8211;nodaemon] [&#8211;nodnsproxy]</code></p>
<h2>Description</h2>
<p>The <i>ConnMan</i> provides a daemon for managing internet connections within devices running the Linux operating system. The Connection Manager is designed to be slim and to use as few resources as possible. It is a fully modular system that can be extended, through plug-ins, to support all kinds of wired or wireless technologies. Also, configuration methods, like DHCP and domain name resolving, are implemented using plug-ins. The plug-in approach allows for easy adaption and modification for various use cases. </p>
<h2>Options</h2>
<p>The following options are supported:</p>
<dl>
<dt><i>&#8211;version</i></p>
<dd>Print the ConnMan software version and exit.</p>
<dt><i>&#8211;help</i></p>
<dd>Print ConnMan&#8217;s available options and exit.</p>
<dt><i>&#8211;config=&lt;filename&gt;</i></p>
<dd>Specify configuration file to set up various settings for ConnMan. If not specified, the default value of &#8216;&lt;SYSCONFDIR&gt;/connman/main.conf&#8217; is used; where &lt;SYSCONFDIR&gt; is dependent on your distribution (usually it&#8217;s /etc). See <code><a href="/docs/linux/man/5-connman-conf/">connman.conf</a></code>(5) for more information on configuration file. The use of config file is optional and sane default values are used if config file is missing.</p>
<dt><i>&#8211;debug=&lt;file1&gt;:&lt;file2&gt;:&#8230;</i></p>
<dd>Sets how much information ConnMan sends to the log destination (usually syslog&#8217;s &quot;daemon&quot; facility). If the file options are omitted, then debugging information from all the source files are printed. If file options are present, then only debug prints from that source file are printed. Example: &#8211;debug=src/service.c:plugins/wifi.c</p>
<dt><i>&#8211;device=&lt;interface1&gt;,&lt;interface2&gt;,&#8230;</i></p>
<dd>Only manage these network interfaces. By default all network interfaces are managed.</p>
<dt><i>&#8211;nodevice=&lt;interface1&gt;,&lt;interface2&gt;,&#8230;</i></p>
<dd>Never manage these network interfaces.</p>
<dt><i>&#8211;plugin=&lt;plugin1&gt;,&lt;plugin2&gt;,&#8230;</i></p>
<dd>Load these plugins only. The option can be a pattern containing &quot;*&quot; and &quot;?&quot; characters.</p>
<dt><i>&#8211;noplugin=&lt;plugin1&gt;,&lt;plugin2&gt;,&#8230;</i></p>
<dd>Never load these plugins. The option can be a pattern containing &quot;*&quot; and &quot;?&quot; characters.</p>
<dt><i>&#8211;wifi=&lt;driver1&gt;,&lt;driver2&gt;,&#8230;</i></p>
<dd>Wifi driver that WiFi/Supplicant should use. If omitted, then the value of &quot;nl80211,wext&quot; is used by default.</p>
<dt><i>&#8211;nodaemon</i></p>
<dd>Do not daemonize. This is useful for debugging, and directs log output to the controlling terminal in addition to syslog.</p>
<dt><i>&#8211;nodnsproxy</i></p>
<dd>Do not act as a DNS proxy. By default ConnMan will direct all DNS traffic to itself by setting nameserver to 127.0.0.1 in <code><a href="/docs/linux/man/5-resolv-conf/">resolv.conf</a></code>(5) file. If this is not desired and you want that all programs call directly some DNS server, then you can use the &#8211;nodnsproxy option. If this option is used, then ConnMan is not able to cache the DNS queries because the DNS traffic is not going through ConnMan and that can cause some extra network traffic.</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/5-connman-conf/">connman.conf</a></code>(5). </p>
