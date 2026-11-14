---
title: "nodm(8)"
name: "nodm"
section: "8"
letter: "n"
url: "/docs/linux/man/8-nodm/"
description: "nodm – X display manager for automatic logins"
---

<p>nodm &#8211; X display manager for automatic logins</p>
<h2>Synopsis</h2>
<p><code>nodm</code> [<i>options</i>]</p>
<h2>Description</h2>
<p><code>nodm</code> is a minimal display manager that simply logs in as a given user and starts an X session, without asking for username or password. </p>
<p> On a normal computer, using <code>nodm</code> is a big security issue because it would give anyone access to the computer. </p>
<p> However, there are cases where automatic login is needed: for example in an embedded system such as a mobile phone, or in a kiosk setup, or in a control panel for industrial machinery. For those cases, <code>nodm</code> is simple to setup, lightweight, and it should do exactly the right thing.</p>
<h2>Options</h2>
<dl>
<dt><code>&#8211;help</code></p>
<dd>print this help message</p>
<dt><code>&#8211;version</code></p>
<dd>print nodm&#8217;s version number</p>
<dt><code>&#8211;verbose</code></p>
<dd>verbose outpout or logging</p>
<dt><code>&#8211;quiet</code></p>
<dd>only log warnings and errors</p>
<dt><code>&#8211;nested</code></p>
<dd>run a nested X server, does not require root. The server defaults to &quot;/usr/bin/Xnest :1&quot;, override with NODM_X_OPTIONS</p>
<dt><code>&#8211;[no-]syslog</code></p>
<dd>enable/disable logging to syslog</p>
<dt><code>&#8211;[no-]stderr</code></p>
<dd>enable/disable logging to stderr</dl>
<h2>Author</h2>
<p><code>nodm</code> is written and maintained by Enrico Zini &lt;enrico [at] enricozini.org&gt; and Joachim Breitner &lt;nomeata [at] debian.org&gt;.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-xinit/">xinit</a></code>(1), <code><a href="/docs/linux/man/1-xdm/">xdm</a></code>(1), <code><a href="/docs/linux/man/1-gdm/">gdm</a></code>(1), <code><a href="/docs/linux/man/1-kdm/">kdm</a></code>(1). </p>
