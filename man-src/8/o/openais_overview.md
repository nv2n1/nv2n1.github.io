---
title: "openais_overview(8)"
name: "openais_overview"
section: "8"
letter: "o"
url: "/docs/linux/man/8-openais_overview/"
---

<h2>Overview</h2>
<p>The openais project is a project to implement a production quality &quot;Revised BSD&quot; licensed implementation of the most recent SA Forum&#8217;s Application Interface Specification. The Application Interface Specification is a software API and policies which are used to develop applications that maintain service during faults. The API consists of Availability Management Framework (AMF) which provides application failover, Cluster Membership (CLM), Checkpointing (CKPT), Eventing (EVT), Messaging (MSG), and Distributed Locking (DLOCK). </p>
<p> Currently Messaging is unimplemented. </p>
<p> Faults occur for various reasons: </p>
<p> * Application Faults </p>
<p> * Middleware Faults </p>
<p> * Operating System Faults </p>
<p> * Hardware Faults </p>
<p> The major focus of high availability in the past has been to mask hardware faults. Faults in other components of the system have gone unsolved until AIS. AIS can mask many types of faults in applications, middleware, operating systems, or even hardware by providing a simple framework for allowing developers to create redundant applications. These redundant applications can be distributed over multiple nodes such that if any one node faults, another node can recover. </p>
<p> Application programmers develop applications to periodically record their state using the checkpointing service. When an active application fails, a standby application recovers the state of the application. This technique, called stateful application failover, provides the fundamental difference between openais and other systems that have come before it. With stateful application failover, the end-application user doesn&#8217;t have to reload the application or redial a telephone. The full state is recorded, so the end-application user sees no interruption in service. </p>
<p> Because programmers can now distribute applications across multiple processes or nodes, a mechanism must exist for them to communicate. This mechanism is provided by two services. The event service provides a publish/subscribe model for events. The messaging service provides end to end messaging. Finally a mechanism to synchronize access is provided by the distributed lock service. </p>
<p> The openais project also provides a group messaging toolkit called EVS. The EVS service implements a messaging model known as Extended Virtual Synchrony. This model allows one sender to transmit to many receivers. Certain guarantees are provided for message and membership delivery which make virtual synchrony ideal for developing distributed applications.</p>
<h2>Quickstart</h2>
<p>The openais executive must be configured. In the directory conf in the source distribution are several files that must be copied to the /etc/ais directory. If openais is packaged by a distro, this may be complete. </p>
<p> The directory contains the file openais.conf. Please read the <a href="/docs/linux/man/5-openais-conf/">openais.conf</a>(5) man page for details on the configuration options. The openais project will work out of the box with the default configuration options, although the administrator may desire different options. </p>
<p> An user and group of the name &quot;ais&quot; must be added to the system. If openais is packaged from a distro, this step should already be completed. This can be achieved by executing: </p>
<p> [root [at] slickdeal root]# adduser ais -g ais </p>
<p> The openais executive uses cryptographic techniques to ensure authenticity and privacy of the messages. In order for openais to be secure and operate, a private key must be generated and shared to all processors. </p>
<p> First generate the key on one of the nodes: </p>
<p> unix# ais-keygen openais authentication key generator. </p>
<p> Gathering 1024 bits for key from /dev/random. </p>
<p> Writing openais key to /etc/ais/authkey. </p>
<p> After this operation, a private key will be in the file /etc/ais/authkey. This private key must be copied to every processor in the cluster. If the private key isn&#8217;t the same for every node, those nodes with nonmatching private keys will not be able to join the same configuration. </p>
<p> Copy the key to some security transportable storage or use ssh to transmit the key from node to node. Then install the key with the command: </p>
<p> unix#: install -D &#8211;group=0 &#8211;owner=0 &#8211;mode=0400 /path_to_authkey/authkey /etc/ais/authkey </p>
<p> If a message &quot;Invalid digest&quot; appears from the openais executive, the keys are not consistent between processors. </p>
<p> Finally run the openais executive. If openais is packaged from a distro, it may be set to start on system start. It may also be turned off by default in which case the init script for openais must be enabled. </p>
<p> After running aisexec, a list of all processors IP addresses running the ais executive and configured on the same multicast address will appear. If they don&#8217;t appear, there may be a problem with multicast in the distro or hardware. If this happens, participation in the openais mailing list may help solve the problem. The email address is openais [at] lists.osdl.org.</p>
<h2>Using Libraries</h2>
<p>The openais AIS libraries have header files which must be included in the developer&#8217;s application. Once the header file is included, the developer can reference the AIS interfaces. </p>
<p> The openais project recommends to distros to place include files in /usr/include/openais. The following include lines must be added to the application to use each of the following services: </p>
<p> #include &lt;<a href="file:/usr/include/openais/saClm.h">openais/saClm.h</a>&gt; For the Cluster Membership B.01.01 service. </p>
<p> #include &lt;<a href="file:/usr/include/openais/saCkpt.h">openais/saCkpt.h</a>&gt; For the Checkpointing B.01.01 service. </p>
<p> #include &lt;<a href="file:/usr/include/openais/saEvt.h">openais/saEvt.h</a>&gt; For the Eventing B.01.01 service. </p>
<p> #include &lt;<a href="file:/usr/include/openais/ais_amf.h">openais/ais_amf.h</a>&gt; For the AMF A.01.01 service. </p>
<p> The openais project recommends to distros to place library files in /usr/lib. The following link lines must be added to the LDFLAGS section of the makefile. </p>
<p> -lsaClm For the Cluster Membership B.01.01 service </p>
<p> -lsaCkpt For the Checkpointing B.01.01 service </p>
<p> -lsaEvt For the Eventing B.01.01 service </p>
<p> -lsaAmf For the AMF A.01.01 service </p>
<p> -lais Specify this to get access to all AIS libraries without specifying each library individually.</p>
<h2>IPv6</h2>
<p>The openais project supports both IPv4 and IPv6 network addresses. The entire cluster must use either IPv4 or IPv6 for the cluster communication mechanism. In order to use IPv6, IPv6 addresses must be specified in the bindnetaddr and mcastaddr fields in the configuration file. The nodeid field must also be set. </p>
<p> An example of this is: nodeid: 2 bindnetaddr: fec0::1:a800:4ff:fe00:20 mcastaddr: ff05::1 </p>
<p> To configure a host for IPv6, use the ifconfig program to add interfaces: box20: ifconfig eth0 add fec0::1:a800:4ff:fe00:20/64 box30: ifconfig eth0 add fec0::1:a800:4ff:fe00:30/64 </p>
<p> If the /64 is not specified, a route for the IPv6 network will not be configured which will cause significant problems. Make sure a route is available for IPv6 traffic.</p>
<h2>Architecture</h2>
<p>The AIS libraries are a thin IPC interface to the openais executive. The openais executive provides services for the SA Forum AIS libraries as well as the EVS and CPG libraries. </p>
<p> The openais executive uses the Totem extended virtual synchrony protocol. The advantage to the end user is excellent performance characteristics and a proven protocol with excellent reliability. This protocol connects the processors in a configuration together so they may communicate.</p>
<h2>Environment Variables</h2>
<p>The openais executive process uses four environment variables during startup. If these environment variables are not set, defaults will be used. </p>
<dl>
<dt>OPENAIS_MAIN_CONFIG_FILE</p>
<dd>This specifies the fully qualified path to the openais configuration file. </p>
<p> The default is /etc/ais/openais.conf. </p>
<dt>OPENAIS_AMF_CONFIG_FILE</p>
<dd>This specifies the fully qualified path to the openais Availability Management Framework configuration file. </p>
<p> The default is /etc/ais/amf.conf. </p>
<dt>OPENAIS_DEFAULT_CONFIG_IFACE</p>
<dd>This specifies the LCRSO that is used to parse the configuration file. This allows other configuration file parsers to be implemented within the system. </p>
<p> The default is to use the default openais configuration file parser which parses the format specified in openais.conf (5). </p>
<dt>OPENAIS_TOTEM_AUTHKEY_FILE</p>
<dd>This specifies the fully qualified path to the shared key used to authenticate and encrypt data used within the Totem protocol. </p>
<p> The default is /etc/ais/authkey. </p>
</dl>
<h2>Security</h2>
<p>The openais executive optionally encrypts all messages sent over the network using the SOBER-128 stream cipher. The openais executive uses HMAC and SHA1 to authenticate all messages. The openais executive library uses SOBER-128 as a pseudo random number generator. The EVS library feeds the PRNG using the /dev/random Linux device. </p>
<p> If membership messages can be captured by intruders, it is possible to execute a denial of service attack on the cluster. In this scenario, the cluster is likely already compromised and a DOS attack is the least of the administration&#8217;s worries. </p>
<p> The security in openais does not offer perfect forward secrecy because the keys are reused. It may be possible for an intruder by capturing packets in an automated fashion to determine the shared key. No such automated attack has been published as of yet. In this scenario, the cluster is likely already compromised to allow the long-term capture of transmitted data. </p>
<p> For security reasons, the openais executive binary aisexec should NEVER be setuid or setgid in the filesystem.</p>
<h2>Saftest Compliance</h2>
<p>The openais libraries are now nearly compliant with every aspect of the SA Forum&#8217;s AIS specification. The AMF service, however, is not compliant with the B.01.01 specification. The remaining services pass most of the tests of the saftest suite against the B.01.01 specification.</p>
<h2>Bugs</h2>
<p>The messaging service is partially implemented and not suitable for deployment. The distributed locking service is buggy and not suitable for deployment. The Availability Management Framework is under development and not suitable for deployment.. </p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/5-openais-conf/">openais.conf</a></code>(5) </p>
