---
title: "init-checkconf(8)"
name: "init-checkconf"
section: "8"
letter: "i"
url: "/docs/linux/man/8-init-checkconf/"
description: "init-checkconf – manual page for init-checkconf"
---

<p>init-checkconf &#8211; manual page for init-checkconf</p>
<h2>Synopsis</h2>
<p><code>init-checkconf</code> [<i>OPTIONS</i>]<i> file </i> </p>
<p> <code>init-checkconf</code> [<i>OPTIONS</i>]<i> </i>-f<i> file </i></p>
<h2>Description</h2>
<p>Determine if specified Upstart <code><a href="/docs/linux/man/8-init/">init</a></code>(8) job configuration file is valid. By default, two checks are performed:</p>
<dl>
<dt>&bull;</p>
<dd>Ensure Upstart can parse overall file successfully</p>
<dt>&bull;</p>
<dd>Ensure all script sections are parseable by shell</dl>
<h2>Options</h2>
<dl>
<dt><code>-d</code> , <code>&#8211;debug</code></p>
<dd>Show some debug output.</p>
<dt><code>-f</code> <i>file</i><code> , </code>&#8211;file=<i>file</i></p>
<dd>Specify job configuration file to check.</p>
<dt><code>-i</code> <i>path</i><code> , </code>&#8211;initctl-path=<i>path</i></p>
<dd>Specify path to <code><a href="/docs/linux/man/8-initctl/">initctl</a></code>(8) binary.</p>
<dt><code>-s</code> , <code>&#8211;noscript</code></p>
<dd>Do not check script sections.</p>
<dt><code>-x</code> <i>path</i><code> , </code>&#8211;upstart-path=<i>path</i></p>
<dd>Specify path to <code><a href="/docs/linux/man/8-init/">init</a></code>(8) binary.</p>
<dt><code>-h</code> , <code>&#8211;help</code></p>
<dd>Display usage statement.</dl>
<h2>Author</h2>
<p>Written by James Hunt &lt;<code>james.hunt [at] ubuntu.com</code>&gt;</p>
<h2>Limitations</h2>
<dl>
<dt>&bull;</p>
<dd><code>exec</code> stanzas containing shell meta-characters will not be checked as scripts.</dl>
<h2>Reporting Bugs</h2>
<p>Report bugs at &lt;<code><a rel="nofollow" href="https://launchpad.net/upstart/+bugs">https://launchpad.net/upstart/+bugs</a></code>&gt;</p>
<h2>Copyright</h2>
<p>Copyright &#169; 2011-2013 Canonical Ltd.<br />
 This is free software; see the source for copying conditions. There is NO warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-sh/">sh</a></code>(1) <code><a href="/docs/linux/man/5-init/">init</a></code>(5) <code><a href="/docs/linux/man/8-init/">init</a></code>(8) </p>
