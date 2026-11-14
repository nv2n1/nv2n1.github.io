---
title: "nessus-rmuser(8)"
name: "nessus-rmuser"
section: "8"
letter: "n"
url: "/docs/linux/man/8-nessus-rmuser/"
description: "nessus-rmuser – removes a user from the nessusd userbase"
---

<p>nessus-rmuser &#8211; removes a user from the nessusd userbase </p>
<h2>Synopsis</h2>
<p><code>nessus-rmuser&nbsp;<wbr>[</code><i>&lt;login&gt;</i><code>]</code> </p>
<h2>Description</h2>
<p>The <code>Nessus Security Scanner</code> comes with its own user base which contains the list of who can use the services of <code>nessusd</code>, and what restriction (or <i>rules</i>) each user has. <code>nessus-rmuser</code> is a simple program which will remove user from the proper nessusd configuration files, as well as its data (saved KBs and saved sessions). </p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-nessus-adduser/">nessus-adduser</a></code>(8),&nbsp;<wbr><code><a href="/docs/linux/man/8-nessusd/">nessusd</a></code>(8),&nbsp;<wbr><code><a href="/docs/linux/man/1-nessus/">nessus</a></code>(1) </p>
<h2>More Information About The Nessus Project</h2>
<p>The canonical places where you will find more information about the Nessus project are: </p>
<dl>
<dd><a rel="nofollow" href="http://www.nessus.org/">http://www.nessus.org/</a> (Official site)<br />
 <a rel="nofollow" href="http://cvs.nessus.org/">http://cvs.nessus.org/</a> (Developers site)</dl>
<h2>Author</h2>
<p><code>nessus-rmuser </code> was quickly written by Renaud Deraison &lt;deraison [at] cvs.nessus.org&gt;</p>
