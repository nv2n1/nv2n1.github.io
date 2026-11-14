---
title: "corosync_overview(8)"
name: "corosync_overview"
section: "8"
letter: "c"
url: "/docs/linux/man/8-corosync_overview/"
description: "corosync_overview – Corosync overview"
---

<p>corosync_overview &#8211; Corosync overview</p>
<h2>Overview</h2>
<p>The corosync project&#8217;s purpose is to implement and support a production quality Revised BSD licensed implementation of a high performance low overhead high availability development toolkit. </p>
<p> Faults occur for various reasons: </p>
<p> * Application Faults </p>
<p> * Middleware Faults </p>
<p> * Operating System Faults </p>
<p> * Hardware Faults </p>
<p> The major focus of high availability in the past has been to mask hardware faults. Faults in other components of the system have gone unsolved until Corosync. Corosync is designed for applications to replicate their state to up to 16 processors. The processors all contain a replica of the application state. </p>
<p> The corosync project provides a group message API called CPG. The project developers recommend CPG be used for most applications. The CPG service implements a closed group messaging model presenting extended virtual synchrony guarantees. </p>
<p> To manage conditions where the process executing the CPG application exchange fails, we provide the Simple Availability Manager (sam) to provide simple application restart.</p>
<h2>Quickstart</h2>
<p>The corosync executive must be configured. In the directory conf in the source distribution are several files that must be copied to the /etc/corosync directory. If corosync is packaged by a distro, this may be complete. </p>
<p> The directory contains the file corosync.conf. Please read the <a href="/docs/linux/man/5-corosync-conf/">corosync.conf</a>(5) man page for details on the configuration options. The corosync project will work out of the box with the default configuration options, although the administrator may desire different options. </p>
<p> The corosync executive uses cryptographic techniques to ensure authenticity and privacy of the messages. In order for corosync to be secure and operate, a private key must be generated and shared to all processors. </p>
<p> First generate the key on one of the nodes: </p>
<p> unix# corosync-keygen<br />
 Corosync Cluster Engine Authentication key generator.<br />
 Gathering 1024 bits for key from /dev/random.<br />
 Press keys on your keyboard to generate entropy.<br />
 Writing corosync key to /etc/corosync/authkey. </p>
<p> After this operation, a private key will be in the file /etc/corosync/authkey. This private key must be copied to every processor in the cluster. If the private key isn&#8217;t the same for every node, those nodes with nonmatching private keys will not be able to join the same configuration. </p>
<p> Copy the key to some security transportable storage or use ssh to transmit the key from node to node. Then install the key with the command: </p>
<p> unix#: install -D &#8211;group=0 &#8211;owner=0 &#8211;mode=0400 /path_to_authkey/authkey /etc/corosync/authkey </p>
<p> If a message &quot;Invalid digest&quot; appears from the corosync executive, the keys are not consistent between processors. </p>
<p> Finally run the corosync executive. If corosync is packaged from a distro, it may be set to start on system start. It may also be turned off by default in which case the init script for corosync must be enabled.</p>
<h2>Using Libraries</h2>
<p>The corosync libraries have header files which must be included in the developer&#8217;s application. Once the header file is included, the developer can reference the corosync interfaces. </p>
<p> The corosync project recommends to distros to place include files in /usr/include/corosync.</p>
<h2>IPv6</h2>
<p>The corosync project supports both IPv4 and IPv6 network addresses. The entire cluster must use either IPv4 or IPv6 for the cluster communication mechanism. In order to use IPv6, IPv6 addresses must be specified in the bindnetaddr and mcastaddr fields in the configuration file. The nodeid field must also be set. </p>
<p> An example of this is: nodeid: 2 bindnetaddr: fec0::1:a800:4ff:fe00:20 mcastaddr: ff05::1 </p>
<p> To configure a host for IPv6, use the ifconfig program to add interfaces: box20: ifconfig eth0 add fec0::1:a800:4ff:fe00:20/64 box30: ifconfig eth0 add fec0::1:a800:4ff:fe00:30/64 </p>
<p> If the /64 is not specified, a route for the IPv6 network will not be configured which will cause significant problems. Make sure a route is available for IPv6 traffic.</p>
<h2>Architecture</h2>
<p>The corosync libraries are a thin IPC interface to the corosync executive. The corosync executive implements the functionality of the corosync APIs for distributed coming. </p>
<p> The corosync executive uses the Totem extended virtual synchrony protocol. The advantage to the end user is excellent performance characteristics and a proven protocol with excellent reliability. This protocol connects the processors in a configuration together so they may communicate.</p>
<h2>Environment Variables</h2>
<p>The corosync executive process uses four environment variables during startup. If these environment variables are not set, defaults will be used. </p>
<dl>
<dt>COROSYNC_MAIN_CONFIG_FILE</p>
<dd>This specifies the fully qualified path to the corosync configuration file. </p>
<p> The default is /etc/corosync/corosync.conf. </p>
<dt>COROSYNC_TOTEM_AUTHKEY_FILE</p>
<dd>This specifies the fully qualified path to the shared key used to authenticate and encrypt data used within the Totem protocol. </p>
<p> The default is /etc/corosync/authkey. </p>
</dl>
<h2>Security</h2>
<p>The corosync executive optionally encrypts all messages sent over the network using the AES-128 cipher. The corosync executive uses HMAC and SHA1 to authenticate all messages. The corosync executive library uses NSS as a pseudo random number generator. </p>
<p> If membership messages can be captured by intruders, it is possible to execute a denial of service attack on the cluster. In this scenario, the cluster is likely already compromised and a DOS attack is the least of the administration&#8217;s worries. </p>
<p> The security in corosync does not offer perfect forward secrecy because the keys are reused. It may be possible for an intruder by capturing packets in an automated fashion to determine the shared key. No such automated attack has been published as of yet. In this scenario, the cluster is likely already compromised to allow the long-term capture of transmitted data. </p>
<p> For security reasons, the corosync executive binary should NEVER be setuid or setgid in the filesystem.</p>
<h2>Bugs</h2>
<p>None that are known. </p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/5-corosync-conf/">corosync.conf</a></code>(5), <code><a href="/docs/linux/man/8-corosync-keygen/">corosync-keygen</a></code>(8), <code><a href="/docs/linux/man/8-cpg_overview/">cpg_overview</a></code>(8), <code><a href="/docs/linux/man/8-sam_overview/">sam_overview</a></code>(8) </p>
