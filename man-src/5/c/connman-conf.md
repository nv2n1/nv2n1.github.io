---
title: "connman-conf(5)"
name: "connman-conf"
section: "5"
letter: "c"
url: "/docs/linux/man/5-connman-conf/"
description: "main.conf – ConnMan configuration file"
---

<p>main.conf &#8211; ConnMan configuration file</p>
<h2>Synopsis</h2>
<p>/etc/connman/main.conf<br />
 or<br />
 <i>&lt;SYSCONFDIR&gt;</i>/connman/main.conf<br />
 where &lt;SYSCONFDIR&gt; depends on your distribution or build.</p>
<h2>Description</h2>
<p><i>main.conf</i> is a configuration file for ConnMan. The configuration file is optional but it can be used to set up various aspects of ConnMan&#8217;s behavior. The location of the file may be changed through use of the &quot;&#8211;config=&quot; argument for <code>connman</code> (8).</p>
<h2>File Format</h2>
<p>The configuration file format is key file format. It consists of sections (groups) of key-value pairs. Lines beginning with a &#8216;#&#8217; and blank lines are considered comments. Sections are started by a header line containing the section enclosed in &#8216;[&#8216; and &#8216;]&#8217;, and ended implicitly by the start of the next section or the end of the file. Each key-value pair must be contained in a section. </p>
<p> Description of sections and available keys follows:</p>
<h3>[General]</h3>
<p>This section is the only mandatory section of the configuration file.</p>
<dl>
<dt><code>InputRequestTimeout=</code>secs</p>
<dd>Set input request timeout. Default is 120 seconds The request for inputs like passphrase will timeout after certain amount of time. Use this setting to increase the value in case of different user interface designs.</p>
<dt><code>BrowserLaunchTimeout=</code>secs</p>
<dd>Set browser launch timeout. Default is 300 seconds The request for launching a browser for portal pages will timeout after certain amount of time. Use this setting to increase the value in case of different user interface designs.</p>
<dt><code>BackgroundScanning=</code>true|false</p>
<dd>Enable background scanning. Default is true. Background scanning will start every 5 minutes unless the scan list is empty. In that case, a simple backoff mechanism starting from 10s up to 5 minutes will run.</p>
<dt><code>FallbackTimeservers=</code>server1,server2,&#8230;</p>
<dd>List of Fallback timeservers separated by &quot;,&quot;. These timeservers are used for NTP sync when there are no timeserver set by the user or by the service. These can contain mixed combination of fully qualified domain names, IPv4 and IPv6 addresses.</p>
<dt><code>FallbackNameservers=</code>server1,server2,&#8230;</p>
<dd>List of fallback nameservers separated by &quot;,&quot; appended to the list of nameservers given by the service. The nameserver entries must be in numeric format, host names are ignored.</p>
<dt><code>DefaultAutoConnectTechnologies=</code>technology1,technology2,&#8230;</p>
<dd>List of technologies that are marked autoconnectable by default, separated by commas &quot;,&quot;. The default value for this entry when empty is ethernet,wifi,cellular. Services that are automatically connected must have been set up and saved to storage beforehand.</p>
<dt><code>PreferredTechnologies=</code>technology1,technology2,&#8230;</p>
<dd>List of preferred technologies from the most preferred one to the least preferred one separated by commas &quot;,&quot;. Services of the listed technology type will be tried one by one in the order given, until one of them gets connected or they are all tried. A service of a preferred technology type in state &#8216;ready&#8217; will get the default route when compared to another preferred type further down the list with state &#8216;ready&#8217; or with a non-preferred type; a service of a preferred technology type in state &#8216;online&#8217; will get the default route when compared to either a non-preferred type or a preferred type further down in the list.</p>
<dt><code>NetworkInterfaceBlacklist=</code>interface1,interface2,&#8230;</p>
<dd>List of blacklisted network interfaces separated by &quot;,&quot;. Found interfaces will be compared to the list and will not be handled by connman, if their first characters match any of the list entries. Default value is vmnet,vboxnet,virbr,ifb.</p>
<dt><code>AllowHostnameUpdates=</code>true|false</p>
<dd>Allow connman to change the system hostname. This can happen for example if we receive DHCP hostname option. Default value is true.</p>
<dt><code>SingleConnectedTechnology=</code>true|false</p>
<dd>Keep only a single connected technology at any time. When a new service is connected by the user or a better one is found according to PreferredTechnologies, the new service is kept connected and all the other previously connected services are disconnected. With this setting it does not matter whether the previously connected services are in &#8216;online&#8217; or &#8216;ready&#8217; states, the newly connected service is the only one that will be kept connected. A service connected by the user will be used until going out of network coverage. With this setting enabled applications will notice more network breaks than normal. Default value is false.</p>
<dt><code>TetheringTechnologies=</code>technology1,technology2,&#8230;</p>
<dd>List of technologies that are allowed to enable tethering separated by &quot;,&quot;. The default value is wifi,bluetooth,gadget. Only those technologies listed here are used for tethering. If one wants to tether ethernet, then add &quot;ethernet&quot; in the list. NOTE that if ethernet tethering is enabled, then a DHCP server is started on all ethernet interfaces. Tethered ethernet should never be connected to corporate or home network as it will disrupt normal operation of these networks. Due to this ethernet is not tethered by default. Do not activate ethernet tethering unless you really know what you are doing.</p>
<dt><code>PersistentTetheringMode=</code>true|false</p>
<dd>Restore earlier tethering status when returning from offline mode, re-enabling a technology, and after restarts and reboots. Default value is false.</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-connman/">Connman</a></code>(8) </p>
