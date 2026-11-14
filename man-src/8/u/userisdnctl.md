---
title: "userisdnctl(8)"
name: "userisdnctl"
section: "8"
letter: "u"
url: "/docs/linux/man/8-userisdnctl/"
description: "userisdnctl – Control and setup ISDN parameters"
---

<p>userisdnctl &#8211; Control and setup ISDN parameters</p>
<h2>Synopsis</h2>
<pre><code>userisdnctl interface options</code></pre>
<h2>Description</h2>
<p>This tool fetches the interface configuration parameters for the ISDN and then calls the apropriate scripts to take the requested action, or report the interface status.</p>
<h2>Options</h2>
<dl>
<dt><code>interface</code></p>
<dd>The interface to be used (will search interface parameters at /etc/sysconfig/ifcfg-INTERFACE)</p>
<dt><code>dial </code></p>
<dd>Dial a connection calling the isdndial</p>
<dt><code>hangup </code></p>
<dd>Finish an existing connection using the isdnhangup</p>
<dt><code>status </code></p>
<dd>Show the status of an existing connection calling the isdnstatus</p>
<dt><code>report </code></p>
<dd>Report the interface status by returning 0 if the interface status looks good and 1 otherwise</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/4-isdnctrl/">isdnctrl</a></code>(4), <code><a href="/docs/linux/man/4-isdninfo/">isdninfo</a></code>(4) </p>
<h2>Security</h2>
<p><code>userisdnctl</code> needs to be setuid root</p>
<h2>Author</h2>
<p>Manpage written by Rodrigo Rubira Branco &lt;rrbranco [at] br.ibm.com&gt;</p>
