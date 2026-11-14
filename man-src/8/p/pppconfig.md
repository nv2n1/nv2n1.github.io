---
title: "pppconfig(8)"
name: "pppconfig"
section: "8"
letter: "p"
url: "/docs/linux/man/8-pppconfig/"
description: "pppconfig – configure pppd to connect to the Internet"
---

<p>pppconfig &#8211; configure pppd to connect to the Internet</p>
<h2>Synopsis</h2>
<p><code>pppconfig</code> [&#8211;version] | [&#8211;help] | [[&#8211;dialog] | [&#8211;whiptail] | [&#8211;gdialog] [&#8211;noname] | [providername]]</p>
<h2>Description</h2>
<p><code>pppconfig</code> is a <code>dialog</code> based interactive, menu driven utility to help automate setting up a dial out ppp connection. It provides extensive explanations at each step. pppconfig supports PAP, CHAP, and chat methods of authentication. It uses the standard ppp configuration files and sets ppp up so that the standard pon and poff commands can be used to control ppp. Some features supported by pppconfig are:<br />
 &#8211; Multiple ISP&#8217;s with separate nameservers.<br />
 &#8211; Modem detection.<br />
 &#8211; Dynamic DNS.<br />
 &#8211; Dial on demand.<br />
 &#8211; Allow non-root users to run ppp.<br />
 &#8211; Uses the gdialog GUI dialog replacement if possible. Before running pppconfig you should know what sort of authentication your isp requires, the username and password that they want you to use, and the phone number. If they require you to use chat authentication, you will also need to know the login and password prompts and any other prompts and responses required for login. If you can&#8217;t get this information from your isp you could try dialing in with minicom and working through the procedure until you get the garbage that indicates that ppp has started on the other end. <code>pppconfig</code> allows you to configure connections to multiple providers. For example, you might call your isp &#8216;provider&#8217;, your employer &#8216;theoffice&#8217; and your university &#8216;theschool&#8217;. Then you can connect to your isp with &#8216;pon&#8217;, your office with &#8216;pon theoffice&#8217;, and your university with &#8216;pon theschool&#8217;. It can determine which serial port your modem is on, but the serial port must already be configured. This is normally done when installing Linux. It can help you set your nameservers, or, if your ISP uses &#8216;dynamic DNS&#8217;, it can set up ppp to use that. It can configure ppp for demand dialing, so that your ppp connection will come up automatically. It will not, however, start pppd for you. You must still start pppd yourself (&#8216;pon&#8217; will do it). Pppd will then wait in the background for you to attempt to access the Net and bring up the link. If you select &quot;Static&quot; in the &quot;Configure Nameservers&quot; screen pppconfig will create a file in the /etc/ppp/resolv directory named after the provider you are configuring and containing &quot;nameserver&quot; lines for each of the IP numbers you gave. This file will be substituted for /etc/resolv.conf when the connection comes up. The provider name is passed in the ipparam variable so that 0dns-up knows which file to use. The original resolv.conf will be put back when the connection goes down. You can edit this file if you wish and add such things as &quot;search&quot; or &quot;domain&quot; directives or additional nameservers. Be sure and read the resolv.conf man page first, though. The &quot;search&quot; and &quot;domain&quot; directives probably do not do what you think they do. If you select &quot;dynamic&quot; in the &quot;Configure Nameservers&quot; screen pppconfig will configure pppd for &#8216;dynamic DNS&#8217; and create a file in the /etc/ppp/resolv directory named after the provider you are configuring but containing nothing. When the connection comes up the nameservers supplied by your ISP will be added and the file substituted for /etc/resolv.conf. You can edit this file if you wish and add such things as &quot;search&quot; or &quot;domain&quot; directives or additional nameservers. If you select &quot;None&quot; in the &quot;Configure Nameservers&quot; screen pppconfig will create no file in /etc/ppp/resolv and will leave /etc/resolv.conf alone. ipparam is not set to the provider name and so is free for the administrator to use. </p>
<h2>Files</h2>
<p><code>/etc/ppp/peers/provider</code> is the standard pppd options file for the default service provider. </p>
<p> <code>/etc/ppp/peers/&lt;name&gt;</code> is the pppd options file for the provider that you have named &lt;name&gt;. </p>
<p> <code>/etc/ppp/peers/provider.bak</code> is a backup copy of /etc/ppp/peers/provider. </p>
<p> <code>/etc/chatscripts/provider</code> is the standard chat script for the default service provider. </p>
<p> <code>/etc/chatscripts/&lt;name&gt;</code> is the chat script for the provider that you have named &lt;name&gt;. </p>
<p> <code>/etc/chatscripts/provider.bak</code> is a backup copy of /etc/chatscripts/provider. </p>
<p> <code>/etc/ppp/resolv</code> is a directory where resolv.conf files for each provider are stored. </p>
<p> <code>/etc/ppp/ip-up.d/0dns-up</code> is a script that arranges for the correct resolv.conf file to be copied into place when a connection comes up. </p>
<p> <code>/etc/ppp/ip-down.d/0dns-down</code> is a script that arranges for the original resolv.conf file to be copied into place when a connection goes down. </p>
<p> <code>/etc/init.d/dns-clean</code> is a script that runs 0dns-down at bootup to clean up any mess left by a crash. </p>
<p> <code>/var/run/pppconfig</code> is a directory where temporary files created by 0dns-up are stored. </p>
<p> <code>/var/run/pppconfig/resolv.conf.bak.&lt;provider&gt; </code> is a backup copy of the original resolv.conf file. 0dns-down restores /etc/resolv.conf from it. </p>
<p> <code>/var/run/pppconfig/0dns.&lt;provider&gt;</code> is a backup copy of the resolv.conf file for &lt;provider&gt;. 0dns-down uses it to determine if /etc/resolv.conf has been overwritten by another process. </p>
<p> <code>/etc/ppp/pap-secrets</code> and <code>/etc/ppp/chap-secrets</code> are described in the pppd documentation. pppconfig may add lines to these files and will change lines that it previously added.</p>
<h2>Notes</h2>
<p><code>pppconfig</code> requires pppd 2.3.7 or higher.</p>
<h2>To Do</h2>
<p>Add full support for MSCHAP.</p>
<h2>Bugs</h2>
<p>Don&#8217;t tell pppconfig to find your modem while pppd is running.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-chat/">chat</a>(8), <a href="/docs/linux/man/1-gpppon/">gpppon</a>(1), <a href="/docs/linux/man/1-plog/">plog</a>(1), <a href="/docs/linux/man/1-poff/">poff</a>(1), <a href="/docs/linux/man/1-pon/">pon</a>(1), <a href="/docs/linux/man/8-pppd/">pppd</a>(8), </code> and <code><a href="/docs/linux/man/1-whiptail/">whiptail</a>(1).</code></p>
<h2>Author</h2>
<p><code>pppconfig</code> was written by John Hasler &lt;jhasler [at] debian.org&gt;.</p>
<h2>Copyright</h2>
<p><code>This man page may be treated as if it were</code> <code>in the public domain. I waive all rights.</code></p>
