---
title: "puppet-device(8)"
name: "puppet-device"
section: "8"
letter: "p"
url: "/docs/linux/man/8-puppet-device/"
description: "puppet-device – Manage remote network devices"
---

<p><code>puppet-device</code> &#8211; Manage remote network devices</p>
<h2>Synopsis</h2>
<p>Retrieves all configurations from the puppet master and apply them to the remote devices configured in /etc/puppet/device.conf. </p>
<p> Currently must be run out periodically, using cron or something similar.</p>
<h2>Usage</h2>
<p>puppet device [-d|&#8211;debug] [&#8211;detailed-exitcodes] [-V|&#8211;version]</p>
<dl>
<dd>
<pre> [-h|--help] [-l|--logdest syslog|&lt;file&gt;|console]
 [-v|--verbose] [-w|--waitforcert &lt;seconds&gt;]</pre>
<dd></dl>
<h2>Description</h2>
<p>Once the client has a signed certificate for a given remote device, it will retrieve its configuration and apply it.</p>
<h2>Usage Notes</h2>
<p>One need a /etc/puppet/device.conf file with the following content: </p>
<p> [remote.device.fqdn] type <i>type</i> url <i>url</i> </p>
<p> where: * type: the current device type (the only value at this time is cisco) * url: an url allowing to connect to the device </p>
<p> Supported url must conforms to: <a href="scheme://user:password@hostname/?query">scheme://user:password@hostname/?query</a> </p>
<p> with: * scheme: either ssh or telnet * user: username, can be omitted depending on the switch/router configuration * password: the connection password * query: this is device specific. Cisco devices supports an enable parameter whose value would be the enable password.</p>
<h2>Options</h2>
<p>Note that any configuration parameter that&#8217;s valid in the configuration file is also a valid long argument. For example, &#8216;server&#8217; is a valid configuration parameter, so you can specify &#8216;&#8211;server <i>servername</i>&#8216; as an argument.</p>
<dl>
<dt>&#8211;debug</p>
<dd>Enable full debugging.</p>
<dt>&#8211;detailed-exitcodes</p>
<dd>Provide transaction information via exit codes. If this is enabled, an exit code of &#8216;2&#8217; means there were changes, an exit code of &#8216;4&#8217; means there were failures during the transaction, and an exit code of &#8216;6&#8217; means there were both changes and failures.</p>
<dt>&#8211;help</p>
<dd>Print this help message</p>
<dt>&#8211;logdest</p>
<dd>Where to send messages. Choose between syslog, the console, and a log file. Defaults to sending messages to syslog, or the console if debugging or verbosity is enabled.</p>
<dt>&#8211;verbose</p>
<dd>Turn on verbose reporting.</p>
<dt>&#8211;waitforcert</p>
<dd>This option only matters for daemons that do not yet have certificates and it is enabled by default, with a value of 120 (seconds). This causes +puppet agent+ to connect to the server every 2 minutes and ask it to sign a certificate request. This is useful for the initial setup of a puppet client. You can turn off waiting for certificates by specifying a time of 0.</dl>
<h2>Example</h2>
<pre> $ puppet device --server puppet.domain.com</pre>
<h2>Author</h2>
<p>Brice Figureau</p>
<h2>Copyright</h2>
<p>Copyright (c) 2011 Puppet Labs, LLC Licensed under the Apache 2.0 License</p>
