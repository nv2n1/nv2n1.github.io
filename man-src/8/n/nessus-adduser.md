---
title: "nessus-adduser(8)"
name: "nessus-adduser"
section: "8"
letter: "n"
url: "/docs/linux/man/8-nessus-adduser/"
description: "nessus-adduser – add a user in the nessusd userbase"
---

<p>nessus-adduser &#8211; add a user in the nessusd userbase </p>
<h2>Synopsis</h2>
<p><code>nessus-adduser</code> </p>
<h2>Description</h2>
<p>The <code>Nessus Security Scanner</code> comes with its own user base which contains the list of who can use the services of <code>nessusd</code>, and what restriction (or <i>rules</i>) each user has. <code>nessus-adduser</code> is a simple program which will add a user in the proper <code>nessusd</code> configuration files, and will send a signal to <code>nessusd</code> if it is running to notify it of the changes. The program is straightforward and asks for the following items:</p>
<dl>
<dt>* Login</p>
<dd>the login name of the <code>nessusd </code> user to add</p>
<dt>* Password</p>
<dd>the password that the user will use to connect to <code>nessusd</code></p>
<dt>* Authentification type</p>
<dd>the authentification method the client will use. The recommended method is &#8220;cipher&#8221;. However, if you compiled <code>nessusd </code> without the cipher support or if you are using a Nessus client which does not support the cipher layer, you&#8217;ll have to use &#8220;plaintext&#8221;</p>
<dt>* Rules</p>
<dd>the set of rules to apply to the user. See below. </p>
<h2>Rules</h2>
<p>Each user has his own set of rules. Rules are here to restrict the rights of the users. For instance, you can add user &#8220;joe&#8221; so that he can only test the host &#8220;192.168.1.1&#8221;, whereas you can add user &#8220;bob&#8221; so that he can test whatever IP address he wishes. </p>
<p> Each rule fits on one line. A user can have an unlimited amount of rules (and can even have no rule at all). </p>
<p> The syntax is:</p>
<dl>
<dd>accept|deny ip/mask</dl>
<p> and</p>
<dl>
<dd>default accept|deny</dl>
<p> Where <i>mask</i> is the CIDR netmask of the rule. </p>
<p> The <i>default</i> statement must be the last rule and defines the policy of the user. </p>
<p> The following rule set will allow the user to test 192.168.1.0/24, 192.168.3.0/24 and 172.22.0.0/16, but nothing else:</p>
<dl>
<dd>accept 192.168.1.0/24<br />
 accept 192.168.3.0/24<br />
 accept 172.22.0.0/16<br />
 default deny</dl>
<p> The following rule set will allow the user to test whatever he wants, except the network 192.168.1.0/24:</p>
<dl>
<dd>deny 192.168.1.0/24<br />
 default accept</dl>
<p> The keyword <i>client_ip</i> has been defined, and is replaced at run time by the IP address of the <code>nessusd </code> user. For instance, if you want your users to be able to only be able to scan the system they come from, then you want them to have the following ruleset:</p>
<dl>
<dd>accept client_ip<br />
 default deny</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-nessus-rmuser/">nessus-rmuser</a></code>(8),&nbsp;<wbr><code><a href="/docs/linux/man/8-nessusd/">nessusd</a></code>(8),&nbsp;<wbr><code><a href="/docs/linux/man/1-nessus/">nessus</a></code>(1) </p>
<h2>More Information About The Nessus Project</h2>
<p>The canonical places where you will find more information about the Nessus project are:</p>
<dl>
<dd><a rel="nofollow" href="http://www.nessus.org/">http://www.nessus.org/</a> (Official site)<br />
 <a rel="nofollow" href="http://cvs.nessus.org">http://cvs.nessus.org</a> (Developers site)</dl>
<h2>Author</h2>
<p><code>nessus-adduser </code> was quickly written by Renaud Deraison &lt;deraison [at] cvs.nessus.org&gt;</p>
<h2>Bugs</h2>
<p><code>nessus-adduser </code> creates temporary files in <i>$TMPDIR/</i>. If this variable is not set, then it will use <i>/var/tmp </i> which may be a security risk depending of your configuration. If you set your TMPDIR variable to <i>/tmp</i>, then you are in trouble. </p>
