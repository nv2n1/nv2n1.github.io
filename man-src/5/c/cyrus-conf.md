---
title: "cyrus-conf(5)"
name: "cyrus-conf"
section: "5"
letter: "c"
url: "/docs/linux/man/5-cyrus-conf/"
description: "cyrus.conf – Cyrus configuration file"
---

<p>&nbsp;<wbr>*</p>
<h2>Name</h2>
<p>cyrus.conf &#8211; Cyrus configuration file</p>
<h2>Description</h2>
<p><code>/etc/cyrus.conf</code> is the configuration file for the Cyrus <code>master</code> process. It defines the startup procedures, services and events to be spawned by <code>master</code>. </p>
<p> The <code>/etc/cyrus.conf</code> file consists of a series of entries divided into sections of the form </p>
<dl>
<dd><i>section</i> {</p>
<dl>
<dd><i>name arguments<br />
 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>&#8230;</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>&#8230;</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>&#8230;<br />
 </i></dl>
<p> }</dl>
<p> where <i>section</i> is the name of the section, <i>name</i> is the name of the entry and <i>arguments</i> is the whitespace-separated list of arguments for the entry. </p>
<p> Blank lines and lines beginning with &#8220;#&#8221; are ignored.</p>
<h2>Section Descriptions</h2>
<p>The paragraphs below detail the three sections (<code>START</code>, <code>SERVICES</code>, <code>EVENTS</code>) that can be placed in the <code>/etc/cyrus.conf</code> file. The arguments that are available for each entry within the section are described, and each argument&#8217;s default value is shown. </p>
<p> Arguments can appear in any order. Some arguments have no default value, these are listed with &#8220;&lt;no default&gt;&#8221;. For string arguments, the value MUST be enclosed in double quotes.</p>
<h3>Start</h3>
<p>This section lists the processes to run before any <code>SERVICES</code> are spawned. This section is typically used to initialize databases and start long running daemons.</p>
<dl>
<dt><code>cmd=</code>&lt;no default&gt;</p>
<dd>The command (with options) to spawn as a child process. This string argument is required.</dl>
<h3>Services</h3>
<p>This section is the heart of the <code>/etc/cyrus.conf</code> file. It lists the processes that should be spawned to handle client connections made on certain Internet/UNIX sockets.</p>
<dl>
<dt><code>babysit=</code>0</p>
<dd>Integer value &#8211; if non-zero, will make sure at least one process is pre-forked, and will set the maxforkrate to 10 if it&#8217;s zero.</p>
<dt><code>cmd=</code>&lt;no default&gt;</p>
<dd>The command (with options) to spawn as a child process. This string argument is required.</p>
<dt><code>listen=</code>&lt;no default&gt;</p>
<dd>The UNIX or internet socket to listen on. This string field is required and takes one of the following forms: </p>
<p> <i>path</i><br />
 [ <i>host</i> <code>: </code>] <i>port</i> </p>
<p> where <i>path</i> is the explicit path to a UNIX socket, <i>host</i> is either the hostname or bracket-enclosed IP address of a network interface, and <i>port</i> is either a port number or service name (as listed in <code>/etc/services</code>).</p>
<dt><code>proto=</code>tcp</p>
<dd>The protocol used for this service (<i>tcp</i>, <i>tcp4</i>, <i>tcp6</i>, <i>udp</i>, <i>udp4</i>, <i>udp6</i>). This string argument is optional. </p>
<p> <code>tcp4</code>, <code>udp4</code>: These arguments are used to bind the service to IPv4 only.<br />
 <code>tcp6</code>, <code>udp6</code>: These arguments are used to bind the service to IPv6 only, if the operating system supports this.<br />
 <code>tcp</code>, <code>udp</code>: These arguments are used to bind to both IPv4 and IPv6 if possible.</p>
<dt><code>prefork=</code>0</p>
<dd>The number of instances of this service to always have running and waiting for a connection (for faster initial response time). This integer value is optional. Note that if you are listening on multiple network types (i.e. ipv4 and ipv6) then one process will be forked for each address, causing twice as many processes as you might expect.</p>
<dt><code>maxchild=</code>-1</p>
<dd>The maximum number of instances of this service to spawn. A value of -1 means unlimited. This integer value is optional.</p>
<dt><code>maxfds=</code>256</p>
<dd>The maximum number of file descriptors to which to limit this process. This integer value is optional.</p>
<dt><code>maxforkrate=</code>0</p>
<dd>Maximum number of processes to fork per second &#8211; the master will insert sleeps to ensure it doesn&#8217;t fork faster than this on average.</dl>
<h3>Events</h3>
<p>This section lists processes that should be run at specific intervals, similar to cron jobs. This section is typically used to perform scheduled cleanup/maintenance.</p>
<dl>
<dt><code>cmd=</code>&lt;no default&gt;</p>
<dd>The command (with options) to spawn as a child process. This string argument is required.</p>
<dt><code>period=</code>0</p>
<dd>The interval (in minutes) at which to run the command. This integer value is optional, but SHOULD be a positive integer &gt; 10.</p>
<dt><code>at=</code>&lt;hhmm&gt;</p>
<dd>The time (24-hour format) at which to run the command each day. If set to a valid time (0000-2359), period is automatically set to 1440. This string argument is optional.</dl>
<h2>Example</h2>
<p># example cyrus.conf </p>
<pre><code>START {
    recover       cmd=&quot;ctl_cyrusdb -r&quot;

}
SERVICES {
    imap          cmd=&quot;imapd&quot; listen=&quot;imap&quot; prefork=1
    imaps         cmd=&quot;imapd -s&quot; listen=&quot;imaps&quot; prefork=0
    lmtpunix      cmd=&quot;lmtpd&quot; listen=&quot;/var/imap/socket/lmtp&quot;
    lmtp          cmd=&quot;lmtpd&quot; listen=&quot;localhost:lmtp&quot;

}
EVENTS {
    checkpoint    cmd=&quot;ctl_cyrusdb -c&quot; period=30
    delprune      cmd=&quot;cyr_expire -E 3&quot; at=0400
    tlsprune      cmd=&quot;tls_prune&quot; at=0400

}</code></pre>
<h2>Access Control</h2>
<p>When TCP Wrappers is used to control access to Cyrus services, the <i>name</i> of the service entry should be used as the process name in the <code><a href="/docs/linux/man/5-hosts_access/">hosts_access</a>(5)</code> table. For instance, in the example above, &quot;imap&quot;, &quot;imaps&quot;, &quot;lmtpunix&quot; and &quot;lmtp&quot; would be used as the process names. This allows a single daemon such as imapd to be run in different modes or configurations (i.e., SSL and non-SSL enabled) yet still have separate access control rules.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-cyrus-master/">cyrus-master</a>(8)</code>, <code><a href="/docs/linux/man/8-imapd/">imapd</a>(8)</code>, <code><a href="/docs/linux/man/8-pop3d/">pop3d</a>(8)</code>, <code><a href="/docs/linux/man/8-lmtpd/">lmtpd</a>(8)</code>, <code><a href="/docs/linux/man/8-timsieved/">timsieved</a>(8)</code>, <code><a href="/docs/linux/man/8-idled/">idled</a>(8)</code>, <code><a href="/docs/linux/man/8-notifyd/">notifyd</a>(8)</code>, <code><a href="/docs/linux/man/8-ctl_cyrusdb/">ctl_cyrusdb</a>(8)</code>, <code><a href="/docs/linux/man/8-ctl_deliver/">ctl_deliver</a>(8)</code>, <code><a href="/docs/linux/man/8-tls_prune/">tls_prune</a>(8)</code>, <code><a href="/docs/linux/man/5-hosts_access/">hosts_access</a>(5)</code> </p>
