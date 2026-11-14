---
title: "openhpi(7)"
name: "openhpi"
section: "7"
letter: "o"
url: "/docs/linux/man/7-openhpi/"
description: "openhpi – an implementation of the SA Forum’s Hardware Platform Interface"
---

<p>openhpi &#8211; an implementation of the SA Forum&#8217;s Hardware Platform Interface</p>
<h2>Description</h2>
<p>OpenHPI is an implementation of the <font SIZE="-1">SA</font> Forum&#8217;s Hardware Platform Interface, which provides a standard C library interface to manage, monitor, and control hardware (both local and remote). </p>
<p> Starting with release 2.14.0 OpenHPI implements the <font SIZE="-1">HPI B.03.02</font> specification. </p>
<p> The OpenHPI client library (libopenhpi) provides all the connection functionality needed by the client application to connect to the OpenHPI daemon running on the local or remote server. </p>
<p> The OpenHPI daemon runs as a background process and executes the requests. It loads plugins to adapt to the different hardware types. The plugins can be defined in the openhpi.conf file or can be loaded dynamically.</p>
<h2>Environmental Variables</h2>
<p>Some of OpenHPI&#8217;s functioning can be changed by setting environment variables. This documents all client environmental settings. Client environmental settings are evaluated in the openhpi library that is linked to the client. There are other environmental settings for the openhpi daemon.</p>
<dl>
<dt><font SIZE="-1"><code>OPENHPICLIENT_CONF</code></font>=&quot;filename&quot;</p>
<dd>Location for the client&#8217;s configuration file that specifies the <font SIZE="-1">HPI</font> domains and addresses of daemons serving the domains. If the variable is not set, OpenHPI will look for a file openhpiclient.conf in the directory specified during the build process (default /etc/openhpi).</p>
<dt><font SIZE="-1"><code>OPENHPI_DAEMON_HOST</code></font>=URL</p>
<dd><font SIZE="-1">URL</font> for the host running the daemon which the client wants to connect to. This can be an ip address or &#8220;localhost&#8221; (default) if the daemon is running on the same host as the client. The variable is only used if no default domain is defined via the client conf file.</p>
<dt><font SIZE="-1"><code>OPENHPI_DAEMON_PORT</code></font>=PORT_NUMBER</p>
<dd>The port number used by the daemon which the client wants to connect to. Default port is 4743. The variable is only used if no default domain is defined via the client conf file.</dl>
<h2>Hardware Support</h2>
<p>OpenHPI provides a number of plugins that talk to different hardware types. The following is a list of plugins provided by the OpenHPI project.</p>
<dl>
<dt><code>ipmidirect</code></p>
<dd>An <font SIZE="-1">IPMI</font> plugin designed specifically for <font SIZE="-1">ATCA</font> chassis. It implements <font SIZE="-1">IPMI</font> commands directly in the plugin.</p>
<dt><code>snmp_bc</code></p>
<dd>An <font SIZE="-1">SNMP</font> based plugin that can communicate with <font SIZE="-1">IBM</font> BladeCenter, as well as <font SIZE="-1">IBM</font> xSeries servers with <font SIZE="-1">RSA 1</font> adapters. </p>
<p> <font SIZE="-1">SNMP_BC</font> plugin depends on net-snmp &gt; 5.0.7.</p>
<dt><code>ilo2_ribcl</code></p>
<dd>OpenHPI plugin supporting <font SIZE="-1">HP</font> ProLiant Rack Mount Servers. This plug-in connects to iLO2 on <font SIZE="-1">HP</font> ProLiant Rack Mount Server using a <font SIZE="-1">SSL</font> connection and exchanges information via Remote Insight Board Command Language (<font SIZE="-1">RIBCL</font>).</p>
<dt><code>oa_soap</code></p>
<dd>OpenHPI plug-in supporting <font SIZE="-1">HP</font> BladeSystems c-Class. This plug-in connects to the <font SIZE="-1">OA</font> of a c-Class chassis using an <font SIZE="-1">SSL</font> connection and manages the system using an XML-encoded <font SIZE="-1">SOAP</font> interface.</p>
<dt><code>rtas</code></p>
<dd>Run-Time Abstraction Services (<font SIZE="-1">RTAS</font>) plug-in</p>
<dt><code>sysfs</code></p>
<dd>OpenHPI plugin that reads system information from sysfs. (<font SIZE="-1">LM</font> sensors and I2C devices exported in sysfs requires kernel 2.6 or &gt;= 2.5.72)</p>
<dt><code>watchdog</code></p>
<dd>Linux watchdog device interface</dl>
<p> The following plugins are provided to ease testing or support complex hardware architectures:</p>
<dl>
<dt><code>simulator</code></p>
<dd>OpenHPI plugin that reports fakes hardware used for testing the core library.</p>
<dt><code>dynamic_simulator</code></p>
<dd>OpenHPI plugin that reports fakes hardware defined in the file simulation.data used for testing the core library.</p>
<dt><code>slave</code></p>
<dd>OpenHPI plug-in that allows to aggregate resources from different domains (slave domains) and to provide aggregated resources as part of the one domain (master domain).</p>
<dt><code>test_agent</code></p>
<dd>OpenHPI plug-in for advanced testing. Provides console for runtime configuration.</dl>
<h2>Other Documentation</h2>
<p>The definitive guide to <font SIZE="-1">HPI</font> is the <font SIZE="-1">SA</font> Forum specification at <a rel="nofollow" href="http://saforum.org.">http://saforum.org.</a> </p>
<p> More info on OpenHPI can be found at our webpage (<a rel="nofollow" href="http://openhpi.org)">http://openhpi.org)</a> and in inline documentation.</p>
<h2>See Also</h2>
<p>The following man pages may also be of interest</p>
<dl>
<dt><code>openhpid</code></p>
<dd>The openhpi daemon, providing OpenHPI data as a system service.</p>
<dt><code>OpenHPI client programs</code></p>
<dd>
<pre> hpialarms hpigensimdata hpireset hpitop
 hpidomain hpiinv hpisensor hpitree
 hpiel hpionIBMblade hpisettime hpiwdt
 hpievents hpipower hpithres hpixml
 ohdomainlist ohhandler ohparam
 hpi_shell</pre>
</dl>
<h2>Authors</h2>
<p>Authors of this man page: </p>
<pre> Sean Dague (<a rel="nofollow" href="http://dague.net/sean)">http://dague.net/sean)</a>
 Renier Morales (renier [at] openhpi.org)
 Ulrich Kleber (ulikleber [at] users.sourceforge.net)
 Anton Pak (avpak [at] users.sourceforge.net)</pre>
