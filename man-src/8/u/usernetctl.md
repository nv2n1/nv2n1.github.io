---
title: "usernetctl(8)"
name: "usernetctl"
section: "8"
letter: "u"
url: "/docs/linux/man/8-usernetctl/"
description: "usernetctl – allow a user to manipulate a network interface if permitted"
---

<p>usernetctl &#8211; allow a user to manipulate a network interface if permitted</p>
<h2>Synopsis</h2>
<p><code>usernetctl</code> <i>interface-name</i> up<i>|</i>down<i>|</i>report</p>
<h2>Description</h2>
<p><code>usernetctl</code> checks to see if users are allowed to manipulate the network interface specified by <i>interface-name</i>, and then tries to bring the network interface up or down, if up or down was specified on the command line, or returns true or false status (respectively) if the report option was specified. </p>
<p> <code>usernetctl</code> is not really meant to be called directly by users, though it currently works fine that way. It is used as a wrapper by the ifup and ifdown scripts, so that users can do exactly the same thing as root: </p>
<pre>ifup <i>interface-name</i>
ifdown <i>interface-name</i></pre>
<p>and <code>ifup</code> and <code>ifdown</code> will call usernetctl automatically to allow the interface status change.</p>
<h2>Options</h2>
<dl>
<dt><i>interface-name</i></p>
<dd>The name of the network interface to check; for example, &quot;ppp0&quot;. For backwards compatibility, &quot;ifcfg-ppp0&quot; and &quot;/etc/sysconfig/network-scripts/ifcfg-ppp0&quot; are also supported.</p>
<dt>up<i>|</i>down</p>
<dd>Attempt to bring the interface up or down.</p>
<dt>report</p>
<dd>Report on whether users can bring the interface up or down.</dl>
<h2>Notes</h2>
<p>Alternate device configurations may inherit the default configuration&#8217;s permissions. </p>
