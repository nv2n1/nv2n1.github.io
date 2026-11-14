---
title: "ypdomainname(1)"
name: "ypdomainname"
section: "1"
letter: "y"
url: "/docs/linux/man/1-ypdomainname/"
description: "hostname – show or set the system’s host name domainname – show or set the system’s NIS/YP domain name ypdomainname – show or set the system’s NIS/YP domain name nisdomainname – show or set the sys..."
---

<h2 class="name">NAME</h2>
<p> hostname &#8211; show or set the system&#8217;s host name<br />
 domainname &#8211; show or set the system&#8217;s NIS/YP domain name<br />
 ypdomainname &#8211; show or set the system&#8217;s NIS/YP domain name<br />
 nisdomainname &#8211; show or set the system&#8217;s NIS/YP domain name<br />
 dnsdomainname &#8211; show the system&#8217;s DNS domain name </p>
<h2>SYNOPSIS</h2>
<p> <code>hostname</code> [<code>-a|&#8211;alias</code>] [<code>-d|&#8211;domain</code>] [<code>-f|&#8211;fqdn|&#8211;long</code>] [<code>-A|&#8211;all-fqdns</code>] [<code>-i|&#8211;ip-address</code>] [<code>-I|&#8211;all-ip-addresses</code>] [<code>-s|&#8211;short</code>] [<code>-y|&#8211;yp|&#8211;nis</code>]<br />
 <code>hostname</code> [<code>-b|&#8211;boot</code>] [<code>-F|&#8211;file filename</code>] [<code>hostname</code>]<br />
 <code>hostname</code> [<code>-h|&#8211;help</code>] [<code>-V|&#8211;version</code>] </p>
<p> <code>domainname</code> [<code>nisdomain</code>] [<code>-F file</code>]<br />
 <code>ypdomainname</code> [<code>nisdomain</code>] [<code>-F file</code>]<br />
 <code>nisdomainname</code> [<code>nisdomain</code>] [<code>-F file</code>] </p>
<p> <code>dnsdomainname</code> </p>
<h2>DESCRIPTION</h2>
<p> <code>Hostname</code> is used to display the system&#8217;s DNS name, and to display or set its hostname or NIS domain name. </p>
<h3>GET NAME</h3>
<p> When called without any arguments, the program displays the current names: </p>
<p> <code>hostname</code> will print the name of the system as returned by the <code><a href="/docs/linux/man/2-gethostname/">gethostname</a></code>(2) function. </p>
<p> <code>domainname</code> will print the NIS domainname of the system. <code>domainname</code> uses the <code><a href="/docs/linux/man/2-gethostname/">gethostname</a></code>(2) function, while <code>ypdomainname</code> and <code>nisdomainname</code> use the <code><a href="/docs/linux/man/2-getdomainname/">getdomainname</a></code>(2). </p>
<p> <code>dnsdomainname</code> will print the domain part of the FQDN (Fully Qualified Domain Name). The complete FQDN of the system is returned with <code>hostname &#8211;fqdn</code> (but see the warnings in section <code>THE FQDN</code> below). </p>
<h3>SET NAME</h3>
<p> When called with one argument or with the <code>&#8211;file</code> option, the commands set the host name or the NIS/YP domain name. <code>hostname</code> uses the <code><a href="/docs/linux/man/2-sethostname/">sethostname</a></code>(2) function, while all of the three <code>domainname</code>, <code>ypdomainname</code> and <code>nisdomainname</code> use <code><a href="/docs/linux/man/2-setdomainname/">setdomainname</a></code>(2). Note, that this is effective only until the next reboot. Edit /etc/hostname for permanent change. </p>
<p> Note, that only the super-user can change the names. </p>
<p> It is not possible to set the FQDN or the DNS domain name with the <code>dnsdomainname</code> command (see <code>THE FQDN</code> below). </p>
<p> The host name is usually set once at system startup in <i>/etc/init.d/hostname.sh</i> (normally by reading the contents of a file which contains the host name, e.g. <i>/etc/hostname</i>). </p>
<h3>THE FQDN</h3>
<p> The FQDN (Fully Qualified Domain Name) of the system is the name that the <code><a href="/docs/linux/man/3-resolver/">resolver</a></code>(3) returns for the host name, such as, <i>ursula.example.com</i>. It is usually the hostname followed by the DNS domain name (the part after the first dot). You can check the FQDN using <code>hostname &#8211;fqdn</code> or the domain name using <code>dnsdomainname</code>. </p>
<p> You cannot change the FQDN with <code>hostname</code> or <code>dnsdomainname</code>. </p>
<p> The recommended method of setting the FQDN is to make the hostname be an alias for the fully qualified name using <i>/etc/hosts</i>, DNS, or NIS. For example, if the hostname was &quot;ursula&quot;, one might have a line in <i>/etc/hosts</i> which reads </p>
<dl>
<dt>
<dd> 127.0.1.1 ursula.example.com ursula</dl>
<p> Technically: The FQDN is the name <code><a href="/docs/linux/man/3-getaddrinfo/">getaddrinfo</a></code>(3) returns for the host name returned by <code><a href="/docs/linux/man/2-gethostname/">gethostname</a></code>(2). The DNS domain name is the part after the first dot. </p>
<p> Therefore it depends on the configuration of the resolver (usually in <i>/etc/host.conf</i>) how you can change it. Usually the hosts file is parsed before DNS or NIS, so it is most common to change the FQDN in <i>/etc/hosts</i>. </p>
<p> If a machine has multiple network interfaces/addresses or is used in a mobile environment, then it may either have multiple FQDNs/domain names or none at all. Therefore avoid using <code>hostname &#8211;fqdn</code>, <code>hostname &#8211;domain</code> and <code>dnsdomainname</code>. <code>hostname &#8211;ip-address</code> is subject to the same limitations so it should be avoided as well. </p>
<h2>OPTIONS</h2>
<dl>
<dt><i>-a, &#8211;alias</i></p>
<dd> Display the alias name of the host (if used). This option is deprecated and should not be used anymore.</p>
<dt><i>-A, &#8211;all-fqdns</i></p>
<dd> Displays all FQDNs of the machine. This option enumerates all configured network addresses on all configured network interfaces, and translates them to DNS domain names. Addresses that cannot be translated (i.e. because they do not have an appropriate reverse IP entry) are skipped. Note that different addresses may resolve to the same name, therefore the output may contain duplicate entries. Do not make any assumptions about the order of the output.</p>
<dt><i>-b, &#8211;boot</i></p>
<dd> Always set a hostname; this allows the file specified by <i>-F</i> to be non-existent or empty, in which case the default hostname <i>localhost</i> will be used if none is yet set.</p>
<dt><i>-d, &#8211;domain</i></p>
<dd> Display the name of the DNS domain. Don&#8217;t use the command <code>domainname</code> to get the DNS domain name because it will show the NIS domain name and not the DNS domain name. Use <code>dnsdomainname</code> instead. See the warnings in section <code>THE FQDN</code> above, and avoid using this option.</p>
<dt><i>-f, &#8211;fqdn, &#8211;long</i></p>
<dd> Display the FQDN (Fully Qualified Domain Name). A FQDN consists of a short host name and the DNS domain name. Unless you are using bind or NIS for host lookups you can change the FQDN and the DNS domain name (which is part of the FQDN) in the <i>/etc/hosts</i> file. See the warnings in section <code>THE FQDN</code> above und use <code>hostname &#8211;all-fqdns</code> instead wherever possible.</p>
<dt><i>-F, &#8211;file filename</i></p>
<dd> Read the host name from the specified file. Comments (lines starting with a `#&#8217;) are ignored.</p>
<dt><i>-i, &#8211;ip-address</i></p>
<dd> Display the network address(es) of the host name. Note that this works only if the host name can be resolved. Avoid using this option; use <code>hostname &#8211;all-ip-addresses</code> instead.</p>
<dt><i>-I, &#8211;all-ip-addresses</i></p>
<dd> Display all network addresses of the host. This option enumerates all configured addresses on all network interfaces. The loopback interface and IPv6 link-local addresses are omitted. Contrary to option <i>-i</i>, this option does not depend on name resolution. Do not make any assumptions about the order of the output.</p>
<dt><i>-s, &#8211;short</i></p>
<dd> Display the short host name. This is the host name cut at the first dot.</p>
<dt><i>-V, &#8211;version</i></p>
<dd> Print version information on standard output and exit successfully.</p>
<dt><i>-y, &#8211;yp, &#8211;nis</i></p>
<dd> Display the NIS domain name. If a parameter is given (or <code>&#8211;file name</code> ) then root can also set a new NIS domain.</p>
<dt><i>-h, &#8211;help</i></p>
<dd> Print a usage message and exit.</dl>
<h2>NOTES</h2>
<p> The address families <code>hostname</code> tries when looking up the FQDN, aliases and network addresses of the host are determined by the configuration of your resolver. For instance, on GNU Libc systems, the resolver can be instructed to try IPv6 lookups first by using the <code>inet6</code> option in <code>/etc/resolv.conf</code>.</p>
<h2>FILES</h2>
<p> <code>/etc/hostname</code> Historically this file was supposed to only contain the hostname and not the full canonical FQDN. Nowadays most software is able to cope with a full FQDN here. This file is read at boot time by the system initialization scripts to set the hostname. </p>
<p> <code>/etc/hosts</code> Usually, this is where one sets the domain name by aliasing the host name to the FQDN.</p>
<h2>AUTHORS</h2>
<p> Peter Tobias, &lt;tobias [at] et-inf.fho-emden.de&gt;<br />
 Bernd Eckenfels, &lt;net-tools [at] lina.inka.de&gt; (NIS and manpage).<br />
 Michael Meskes, &lt;meskes [at] debian.org&gt; </p>
<h2>Index</h2>
