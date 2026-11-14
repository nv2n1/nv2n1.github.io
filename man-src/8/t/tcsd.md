---
title: "tcsd(8)"
name: "tcsd"
section: "8"
letter: "t"
url: "/docs/linux/man/8-tcsd/"
description: "tcsd – daemon that manages Trusted Computing resources"
---

<p>TCG Software Stack<br />
 </center></p>
<h2>Name</h2>
<p>tcsd &#8211; daemon that manages Trusted Computing resources</p>
<h2>Synopsis</h2>
<p><code>tcsd</code> [<code>-f</code>] [<code>-e</code>] [<code>-c&nbsp;<wbr>&lt;configfile&gt;&nbsp;<wbr>]</code> [<code>-h</code>] </p>
<h2>Description</h2>
<p>Trousers is an open-source TCG Software Stack (TSS), released under the BSD License. Trousers aims to be compliant with the current (1.1b) and upcoming (1.2) TSS specifications available from the Trusted Computing Group website: <a rel="nofollow" href="http://www.trustedcomputinggroup.org.">http://www.trustedcomputinggroup.org.</a> <code>tcsd</code> is a user space daemon that should be (according to the TSS spec) the only portal to the TPM device driver. At boot time, <code>tcsd</code> should be started, it should open the TPM device driver and from that point on, all requests to the TPM should go through the TSS stack. The <code>tcsd</code> manages TPM resources and handles requests from TSP&#8217;s both local and remote.</p>
<dl>
<dt><code>-f, &#8211;foreground</code></p>
<dd>run the daemon in the foreground</p>
<dt><code>-e</code></p>
<dd>attempt to connect to software TPMs over TCP</p>
<dt><code>-c, &#8211;config &lt;configfile&gt;</code></p>
<dd>use the provided configuration file rather than the default configuration file</p>
<dt><code>-h, &#8211;help</code></p>
<dd>display help message </p>
<h2>Access Control</h2>
<p>There are two types of access control for the <code>tcsd</code>, access to the daemon&#8217;s socket itself and access to specific commands internal to the <code>tcsd</code>. Access to the <code>tcsd</code>&#8216;s port should be controlled by the system administrator using firewall rules. If using iptables, the following rule will allow a specific host access to the tcsd: </p>
<p> # iptables -A INPUT -s $IP_ADDRESS -p tcp &#8211;destination-port 30003 -j ACCEPT </p>
<p> Access to individual commands internal to the tcsd is configured by the <code>tcsd</code> configuration file&#8217;s &quot;remote_ops&quot; directive. Each function call in the TCS API is reachable by a unique ordinal. Each labeled &quot;remote op&quot; actually defines a set of ordinals (usually more than one) necessary to accomplish the operation. So, for example, the &quot;random&quot; operation enables the ordinals for opening and closing a context, calling TCS_StirRandom and TCS_GetRandom, as well as TCS_FreeMemory. By default, connections from localhost will allow any ordinals.</p>
<h2>Data Files</h2>
<p>TSS applications have access to 2 different kinds of &#8216;persistant&#8217; storage. &#8216;User&#8217; persistant storage has the lifetime of that of the application using it and therefore is destroyed when an application exits. User PS is controlled by the TSP of the application. &#8216;System&#8217; persistent storage is controlled by the TCS and stays valid across application lifetimes, <code>tcsd</code> restarts and system resets. Data registered in system PS stays valid until an application requests that it be removed. User PS files are by default stored as /var/lib/tpm/user.{pid} and the system PS file by default is /var/lib/tpm/system.data. The system PS file is initially created when ownership of the TPM is first taken.</p>
<h2>Configuration</h2>
<p><code>tcsd</code> configuration is stored by default in /etc/tcsd.conf</p>
<h2>Debug Output</h2>
<p>If TrouSerS has been compiled with debugging enabled, the debugging output can be supressed by setting the TSS_DEBUG_OFF environment variable.</p>
<h2>Device Drivers</h2>
<p><code>tcsd</code> is compatible with the IBM Research TPM device driver available from <a rel="nofollow" href="http://ibmswtpm.sourceforge.net/">http://ibmswtpm.sourceforge.net/</a> and the TPM device driver available from <a rel="nofollow" href="http://sf.net/projects/tpmdd,">http://sf.net/projects/tpmdd,</a> which is also available in the upstream Linux kernel and many Linux distros.</p>
<h2>Conforming To</h2>
<p><code>tcsd</code> conforms to the Trusted Computing Group Software Specification version 1.1 Golden </p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/5-tcsd-conf/">tcsd.conf</a></code>(5) </p>
<h2>Author</h2>
<p>Kent Yoder</p>
<h2>Reporting Bugs</h2>
<p>Report bugs to &lt;trousers-tech [at] lists.sf.net&gt;</p>
