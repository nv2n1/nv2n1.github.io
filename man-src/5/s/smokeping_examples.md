---
title: "smokeping_examples(5)"
name: "smokeping_examples"
section: "5"
letter: "s"
url: "/docs/linux/man/5-smokeping_examples/"
---

smokeping_examples - Examples of Smokeping configuration

<h2>Overview</h2>

This document provides some examples of Smokeping configuration files. All the examples can be found in the <tt>&quot;examples&quot;</tt> directory in the Smokeping documentation. Note that the <font SIZE="-1">DNS</font> names in the examples are non-functional. 

 Details of the syntax and all the variables are found in smokeping_config and in the documentation of the corresponding probe, if applicable. 

 This manual is automatically generated from the Smokeping source code, specifically the Smokeping::Examples module.

<h2>Description</h2>

Currently the examples differ only in the <tt>&quot;Probes&quot;</tt> and <tt>&quot;Targets&quot;</tt> sections. The other sections are taken from the <tt>&quot;etc/config.dist&quot;</tt> configuration template in the Smokeping distribution so that the example files are complete. 

 If you would like to provide more examples, document the other sections or enhance the existing examples, please do so, preferably by sending the proposed changes to the smokeping-users mailing list.

<h3>Example 1: config.simple</h3>

<dl><dt>Probe configuration
<dd><pre> *** Probes ***
 +FPing
 binary = /usr/bin/fping</pre><dt>Probe explanation
<dd>Here we have just one probe, fping, pinging four hosts. 

 The fping probe is using the default parameters, some of them supplied from the Database section (``step'' and ``pings''), and some of them by the probe module.
<dt>Target configuration
<dd><pre> *** Targets ***
 probe = FPing
 
 menu = Top
 title = Network Latency Grapher
 remark = Welcome to this SmokePing website.
 
 + mysite1
 menu = Site 1
 title = Hosts in Site 1
 
 ++ myhost1
 host = myhost1.mysite1.example
 ++ myhost2
 host = myhost2.mysite1.example
 
 + mysite2
 menu = Site 2
 title = Hosts in Site 2
 
 ++ myhost3
 host = myhost3.mysite2.example
 ++ myhost4
 host = myhost4.mysite2.example</pre><dt>Target explanation
<dd>The hosts are located in two sites of two hosts each, and the configuration has been divided to site sections ('+') and host subsections ('++') accordingly.</dl>

<h3>Example 2: config.multiple-probes</h3>

<dl><dt>Probe configuration
<dd><pre> *** Probes ***
 + FPing
 binary = /usr/bin/fping
 packetsize = 1000
 
 + DNS
 binary = /usr/bin/dig
 lookup = name.example
 pings = 5
 step = 180
 
 + EchoPingHttp
 pings = 5
 url = /test-url</pre><dt>Probe explanation
<dd>Here we have three probes: FPing for the regular <font SIZE="-1">ICMP</font> pings, <font SIZE="-1">DNS</font> for name server latency measurement and EchoPingHttp for web servers. 

 The FPing probe runs with the default parameters, except that the <font SIZE="-1">ICMP</font> packet size is 1000 bytes instead of the default 56 bytes. 

 The <font SIZE="-1">DNS</font> and EchoPingHttp probes have been configured to be a bit more gentle with the servers, as they only do 5 queries (pings) instead of the default 20 (or whatever is specified in the Database section). However, <font SIZE="-1">DNS</font> queries are made more often: 5 queries every 3 minutes instead of every 5 minutes.
<dt>Target configuration
<dd><pre> *** Targets ***
 probe = FPing
 menu = Top
 title = Network Latency Grapher
 remark = Welcome to this SmokePing website.
 
 + network
 menu = Net latency
 title = Network latency (ICMP pings)
 
 ++ myhost1
 host = myhost1.example
 ++ myhost2
 host = myhost2.example
 
 + services
 menu = Service latency
 title = Service latency (DNS, HTTP)
 
 ++ DNS
 probe = DNS
 menu = DNS latency
 title = Service latency (DNS)
 
 +++ dns1
 host = dns1.example
 
 +++ dns2
 host = dns2.example
 
 ++ HTTP
 menu = HTTP latency
 title = Service latency (HTTP)
 
 +++ www1
 host = www1.example
 
 +++ www2
 host = www2.example</pre><dt>Target explanation
<dd>The target tree has been divided by the probe used. This does not have to be the case: every target (sub)section can use a different probe, and the same probe can be used in different parts of the config tree.</dl>

<h3>Example 3: config.fping-instances</h3>

<dl><dt>Probe configuration
<dd><pre> *** Probes ***
 + FPing
 binary = /usr/bin/fping
 
 ++ FPingNormal
 offset = 0%
 
 ++ FPingLarge
 packetsize = 5000
 offset = 50%</pre><dt>Probe explanation
<dd>This example demonstrates the concept of probe instances. The FPingLarge and FPingNormal probes are independent of each other, they just use the same module, FPing. FPingNormal uses the default parameters, and so does FPingLarge except for the 5 kilobyte packetsize. Both use the same fping binary, and its path is configured FPing top section. 

 The 'offset' parameters make sure the probes don't run at the same time - FPingNormal is run every 'full' 5 minutes (eg. 8:00, 8:05, 8:10 and so on, in wallclock time) while FPingLarge is run halfway through these intervals (eg. 8:02:30, 8:07:30 etc.) 

 The top FPing section does not define a probe in itself because it has subsections. If we really wanted to have one probe named ``FPing'', we could do so by making a subsection by that name.
<dt>Target configuration
<dd><pre> *** Targets ***
 probe = FPingNormal
 menu = Top
 title = Network Latency Grapher
 remark = Welcome to this SmokePing website.
 
 + network
 menu = Net latency
 title = Network latency (ICMP pings)
 
 ++ myhost1
 menu = myhost1
 title = ICMP latency for myhost1
 
 +++ normal
 title = Normal packetsize (56 bytes)
 probe = FPingNormal
 host = myhost1.example
 
 +++ large
 title = Large packetsize (5000 bytes)
 probe = FPingLarge
 host = myhost1.example
 
 ++ myhost2
 menu = myhost2
 title = ICMP latency for myhost2
 
 +++ normal
 title = Normal packetsize (56 bytes)
 probe = FPingNormal
 host = myhost2.example
 
 +++ large
 title = Large packetsize (5000 bytes)
 probe = FPingLarge
 host = myhost2.example</pre><dt>Target explanation
<dd>The target section shows two host, myhost1.example and myhost2.example, being pinged with two differently sized <font SIZE="-1">ICMP</font> packets. This time the tree is divided by the target host rather than the probe.</dl>

<h3>Example 4: config.targetvars-with-Curl</h3>

<dl><dt>Probe configuration
<dd><pre> *** Probes ***
 + Curl
 # probe-specific variables
 binary = /usr/bin/curl
 step = 60
 
 # a default for this target-specific variable
 urlformat = <a rel="nofollow" HREF="http://%host%/">http://%host%/</a></pre><dt>Probe explanation
<dd>This example explains the difference between probe- and target-specific variables. We use the Curl probe for this. 

 Every probe supports at least some probe-specific variables. The values of these variables are common to all the targets of the probe, and they can only be configured in the Probes section. In this case, the probe-specific variables are ``binary'' and ``step''. 

 Target-specific variables are supported by most probes, the most notable exception being the FPing probe and its derivatives. Target-specific variables can have different values for different targets. They can be configured in both Probes and Targets sections. The values assigned in the Probes section function become default values that can be overridden in the Targets section. 

 The documentation of each probe states which of its variables are probe-specific and which are target-specific. 

 In this case the ``urlformat'' variable is a target-specific one. It is also quite uncommon, because it can contain a placeholder for the ``host'' variable in the Targets section. This is not a general feature, its usage is only limited to the ``urlformat'' variable and the ``%host%'' escape. 

 (The reason why the FPing probe does not support target-specific variables is simply the fact that the fping program measures all its targets in one go, so they all have the same parameters. The other probes ping their targets one at a time.)
<dt>Target configuration
<dd><pre> *** Targets ***
 probe = Curl
 menu = Top
 title = Network Latency Grapher
 remark = Welcome to this SmokePing website.
 
 + HTTP
 menu = http
 title = HTTP latency 
 
 ++ myhost1
 menu = myhost1
 title = HTTP latency for myhost1
 host = myhost1.example
 
 ++ myhost2
 menu = myhost2
 title = HTTP latency for myhost2
 host = myhost2.example
 
 ++ myhost3
 menu = myhost3
 title = HTTP latency for myhost3 (port 8080!)
 host = myhost3.example
 urlformat = <a rel="nofollow" HREF="http://%host%:8080/">http://%host%:8080/</a>
 
 + FTP
 menu = ftp
 title = FTP latency
 urlformat = <a HREF="ftp://%host%/">ftp://%host%/</a>
 
 ++ myhost1
 menu = myhost1
 title = FTP latency for myhost1
 host = myhost1.example
 
 ++ myhost2
 menu = myhost2
 title = FTP latency for myhost2
 host = myhost2.example</pre><dt>Target explanation
<dd>The target tree is divided into an <font SIZE="-1">HTTP</font> branch and an <font SIZE="-1">FTP</font> one. The servers ``myhost1.example'' and ``myhost2.example'' are probed in both. The third server, ``myhost3.example'', only has an <font SIZE="-1">HTTP</font> server, and it's in a non-standard port (8080). 

 The ``urlformat'' variable is specified for the whole <font SIZE="-1">FTP</font> branch as ``<a HREF="ftp://%host%/''.">ftp://%host%/''.</a> For the <font SIZE="-1">HTTP</font> branch, the default from the Probes section is used, except for myhost3, which overrides it to tag the port number into the <font SIZE="-1">URL. </font> 

 The myhost3 assignment could just as well have included the hostname verbatim (ie. urlformat = <a rel="nofollow" HREF="http://myhost3.example:8080/)">http://myhost3.example:8080/)</a> instead of using the <tt>%host</tt>% placeholder, but the host variable would still have been required (even though it wouldn't have been used for anything).</dl>

<h3>Example 5: config.echoping</h3>

<dl><dt>Probe configuration
<dd><pre> *** Probes ***
 + FPing
 binary = /usr/bin/fping
 
 # these expect to find echoping in /usr/bin
 # if not, you'll have to specify the location separately for each probe
 # + EchoPing # uses TCP or UDP echo (port 7)
 # + EchoPingDiscard # uses TCP or UDP discard (port 9)
 # + EchoPingChargen # uses TCP chargen (port 19)
 + EchoPingSmtp # SMTP (25/tcp) for mail servers
 + EchoPingHttps # HTTPS (443/tcp) for web servers
 + EchoPingHttp # HTTP (80/tcp) for web servers and caches
 + EchoPingIcp # ICP (3130/udp) for caches
 # these need at least echoping 6 with the corresponding plugins
 + EchoPingDNS # DNS (53/udp or tcp) servers
 + EchoPingLDAP # LDAP (389/tcp) servers
 + EchoPingWhois # Whois (43/tcp) servers</pre><dt>Probe explanation
<dd>This example shows most of the echoping-derived probes in action.
<dt>Target configuration
<dd><pre> *** Targets ***
 # default probe
 probe = FPing
 
 menu = Top
 title = Network Latency Grapher
 remark = Welcome to this SmokePing website.
 
 + MyServers
 
 menu = My Servers
 title = My Servers 
 
 ++ www-server
 menu = www-server
 title = Web Server (www-server) / ICMP
 # probe = FPing propagated from top
 host = www-server.example
 
 +++ http
 menu = http
 title = Web Server (www-server) / HTTP
 probe = EchoPingHttp
 host = www-server.example 
 # default url is /
 
 +++ https
 menu = https
 title = Web Server (www-server) / HTTPS
 probe = EchoPingHttps
 host = www-server.example
 
 ++ cache
 menu = www-cache
 title = Web Cache (www-cache) / ICMP
 host = www-cache.example
 
 +++ http
 menu = http
 title = www-cache / HTTP
 probe = EchoPingHttp
 host = www-cache.example
 port = 8080 # use the squid port
 url = <a rel="nofollow" HREF="http://www.somehost.example/">http://www.somehost.example/</a>
 
 +++ icp
 menu = icp
 title = www-cache / ICP
 probe = EchoPingIcp
 host = www-cache.example
 url = <a rel="nofollow" HREF="http://www.somehost.example/">http://www.somehost.example/</a>
 
 ++ mail
 menu = mail-server
 title = Mail Server (mail-server) / ICMP
 host = mail-server.example
 
 +++ smtp
 menu = mail-server / SMTP
 title = Mail Server (mail-server) / SMTP
 probe = EchoPingSmtp
 host = mail-server.example
 
 ++ ldap-server
 menu = ldap-server
 title = ldap-server / ICMP
 host = ldap-server.example
 
 +++ ldap
 menu = ldap-server / LDAP
 title = LDAP Server (ldap-server) / LDAP
 probe = EchoPingLDAP
 ldap_request = (objectclass=*)
 host = ldap-server.example
 
 ++ name-server
 menu = name-server
 title = name-server / ICMP
 host = name-server.example
 
 +++ DNS
 menu = name-server / DNS
 title = DNS Server (name-server) / DNS
 probe = EchoPingDNS
 dns_request = name.example
 host = name-server.example
 
 ++ whois-server
 menu = whois-server
 title = whois-server / ICMP
 host = whois-server.example
 
 +++ Whois
 menu = whois-server / Whois
 title = Whois Server (whois-server) / Whois
 probe = EchoPingWhois
 whois_request = domain.example
 host = whois-server.example</pre><dt>Target explanation
<dd>All the servers are pinged both with <font SIZE="-1">ICMP </font>(the FPing probe) and their respective echoping probe. The proxy server, www-cache, is probed with both <font SIZE="-1">HTTP</font> requests and <font SIZE="-1">ICP</font> requests for the same <font SIZE="-1">URL.</font></dl>

<h3>Example 6: config.template</h3>

<dl><dt>Probe configuration
<dd><pre> *** Probes ***
 
 + FPing
 
 binary = /usr/sbin/fping
 
 *** Slaves ***
 secrets=/etc/smokeping/smokeping_secrets
 +boomer
 display_name=boomer
 color=0000ff
 
 +slave2
 display_name=another
 color=00ff00</pre><dt>Probe explanation
<dd>This is the template configuration file distributed with Smokeping. It is included in the examples as well for the sake of completeness.
<dt>Target configuration
<dd><pre> *** Targets ***
 
 #menuextra = &lt;a target='_blank' href='/smokeping/tr.html{HOST}' class='{CLASS}' \
 # onclick=&quot;window.open(this.href,this.target, \
 # 'width=800,height=500,toolbar=no,location=no,status=no,scrollbars=no'); \
 # return false;&quot;&gt;*&lt;/a&gt;
 #
 probe = FPing
 
 menu = Top
 title = Network Latency Grapher
 remark = Welcome to the SmokePing website of &lt;b&gt;Insert Company Name Here&lt;/b&gt;. \
 Here you will learn all about the latency of our network.
 
 + Ping
 
 menu = Fedora
 title = Fedora Pings
 
 ++ FedoraprojectOrg
 
 menu = fedoraproject.org
 title = Fedora Webserver
 host = fedoraproject.org
 
 ++ DocsFedoraprojectOrg
 
 menu = docs.fedoraproject.org
 title = Fedora Docs Webserver
 host = docs.fedoraproject.org
 
 ++ PlanetFedora
 
 menu = planet.fedoraproject.org
 title = Planet Fedora
 host = planet.fedoraproject.org
 
 #
 # Lots of more options are available, please have a look in the included documentation.
 #
 
 
 #++ James
 
 #menu = James
 #title =James
 #alerts = someloss
 #slaves = boomer slave2
 #host = james.address
 
 #++ MultiHost
 
 #menu = Multihost
 #title = James and James as seen from Boomer
 #host = /Test/James /Test/James~boomer</pre><dt>Target explanation
<dd>This is the template configuration file distributed with Smokeping. It is included in the examples as well for the sake of completeness.</dl>

<h2>Copyright</h2>

Copyright 2005 by Niko Tyni.

<h2>License</h2>

This program is free software; you can redistribute it and/or modify it under the terms of the <font SIZE="-1">GNU</font> General Public License as published by the Free Software Foundation; either version 2 of the License, or (at your option) any later version. 

 This program is distributed in the hope that it will be useful, but <font SIZE="-1">WITHOUT ANY WARRANTY</font>; without even the implied warranty of <font SIZE="-1">MERCHANTABILITY</font> or <font SIZE="-1">FITNESS FOR A PARTICULAR PURPOSE. </font> See the <font SIZE="-1">GNU</font> General Public License for more details. 

 You should have received a copy of the <font SIZE="-1">GNU</font> General Public License along with this program; if not, write to the Free Software Foundation, Inc., 675 Mass Ave, Cambridge, <font SIZE="-1">MA 02139, USA.</font>

<h2>Author</h2>

Niko Tyni &lt;ntyni [at] iki.fi&gt;

<h2>See Also</h2>

The other Smokeping documents, especially smokeping_config. 
