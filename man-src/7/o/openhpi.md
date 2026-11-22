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
<p>OpenHPI is an implementation of the SA Forum&#8217;s Hardware Platform Interface, which provides a standard C library interface to manage, monitor, and control hardware (both local and remote). </p>
<p> Starting with release 2.14.0 OpenHPI implements the HPI B.03.02 specification. </p>
<p> The OpenHPI client library (libopenhpi) provides all the connection functionality needed by the client application to connect to the OpenHPI daemon running on the local or remote server. </p>
<p> The OpenHPI daemon runs as a background process and executes the requests. It loads plugins to adapt to the different hardware types. The plugins can be defined in the openhpi.conf file or can be loaded dynamically.</p>
<h2>Environmental Variables</h2>
<p>Some of OpenHPI&#8217;s functioning can be changed by setting environment variables. This documents all client environmental settings. Client environmental settings are evaluated in the openhpi library that is linked to the client. There are other environmental settings for the openhpi daemon.</p>
<dl>
<dt><code>OPENHPICLIENT_CONF</code>=&quot;filename&quot;</dt>
<dd>Location for the client&#8217;s configuration file that specifies the HPI domains and addresses of daemons serving the domains. If the variable is not set, OpenHPI will look for a file openhpiclient.conf in the directory specified during the build process (default /etc/openhpi).</dd>
<dt><code>OPENHPI_DAEMON_HOST</code>=URL</dt>
<dd>URL for the host running the daemon which the client wants to connect to. This can be an ip address or &#8220;localhost&#8221; (default) if the daemon is running on the same host as the client. The variable is only used if no default domain is defined via the client conf file.</dd>
<dt><code>OPENHPI_DAEMON_PORT</code>=PORT_NUMBER</dt>
<dd>The port number used by the daemon which the client wants to connect to. Default port is 4743. The variable is only used if no default domain is defined via the client conf file.</dd></dl>
<h2>Hardware Support</h2>
<p>OpenHPI provides a number of plugins that talk to different hardware types. The following is a list of plugins provided by the OpenHPI project.</p>
<dl>
<dt><code>ipmidirect</code></dt>
<dd>An IPMI plugin designed specifically for ATCA chassis. It implements IPMI commands directly in the plugin.</dd>
<dt><code>snmp_bc</code></dt>
<dd>An SNMP based plugin that can communicate with IBM BladeCenter, as well as IBM xSeries servers with RSA 1 adapters. </dd>
<p> SNMP_BC plugin depends on net-snmp &gt; 5.0.7.</p>
<dt><code>ilo2_ribcl</code></dt>
<dd>OpenHPI plugin supporting HP ProLiant Rack Mount Servers. This plug-in connects to iLO2 on HP ProLiant Rack Mount Server using a SSL connection and exchanges information via Remote Insight Board Command Language (RIBCL).</dd>
<dt><code>oa_soap</code></dt>
<dd>OpenHPI plug-in supporting HP BladeSystems c-Class. This plug-in connects to the OA of a c-Class chassis using an SSL connection and manages the system using an XML-encoded SOAP interface.</dd>
<dt><code>rtas</code></dt>
<dd>Run-Time Abstraction Services (RTAS) plug-in</dd>
<dt><code>sysfs</code></dt>
<dd>OpenHPI plugin that reads system information from sysfs. (LM sensors and I2C devices exported in sysfs requires kernel 2.6 or &gt;= 2.5.72)</dd>
<dt><code>watchdog</code></dt>
<dd>Linux watchdog device interface</dd></dl>
<p> The following plugins are provided to ease testing or support complex hardware architectures:</p>
<dl>
<dt><code>simulator</code></dt>
<dd>OpenHPI plugin that reports fakes hardware used for testing the core library.</dd>
<dt><code>dynamic_simulator</code></dt>
<dd>OpenHPI plugin that reports fakes hardware defined in the file simulation.data used for testing the core library.</dd>
<dt><code>slave</code></dt>
<dd>OpenHPI plug-in that allows to aggregate resources from different domains (slave domains) and to provide aggregated resources as part of the one domain (master domain).</dd>
<dt><code>test_agent</code></dt>
<dd>OpenHPI plug-in for advanced testing. Provides console for runtime configuration.</dd></dl>
<h2>Other Documentation</h2>
<p>The definitive guide to HPI is the SA Forum specification at <a rel="nofollow" href="http://saforum.org.">http://saforum.org.</a> </p>
<p> More info on OpenHPI can be found at our webpage (<a rel="nofollow" href="http://openhpi.org)">http://openhpi.org)</a> and in inline documentation.</p>
<h2>See Also</h2>
<p>The following man pages may also be of interest</p>
<dl>
<dt><code>openhpid</code></dt>
<dd>The openhpi daemon, providing OpenHPI data as a system service.</dd>
<dt><code>OpenHPI client programs</code></dt>
<dd>
<pre> hpialarms hpigensimdata hpireset hpitop
 hpidomain hpiinv hpisensor hpitree
 hpiel hpionIBMblade hpisettime hpiwdt
 hpievents hpipower hpithres hpixml
 ohdomainlist ohhandler ohparam
 hpi_shell</pre>
</dd></dl>
<h2>Authors</h2>
<p>Authors of this man page: </p>
<pre> Sean Dague (<a rel="nofollow" href="http://dague.net/sean)">http://dague.net/sean)</a>
 Renier Morales (renier [at] openhpi.org)
 Ulrich Kleber (ulikleber [at] users.sourceforge.net)
 Anton Pak (avpak [at] users.sourceforge.net)</pre>
