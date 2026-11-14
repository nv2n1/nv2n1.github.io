---
title: "corosync-xml(5)"
name: "corosync-xml"
section: "5"
letter: "c"
url: "/docs/linux/man/5-corosync-xml/"
description: "corosync.xml – XML version of corosync executive configuration file"
---

<p>corosync.xml &#8211; XML version of corosync executive configuration file </p>
<h2>Synopsis</h2>
<p>/etc/corosync/corosync.xml </p>
<h2>Description</h2>
<p>The corosync.xml is XML version of corosync.conf file. It is processed by <code>corosync-xmlproc (8)</code> to generate valid conf file. File must be valid XML. File starts with root element <code>corosync</code> which can contain same arguments as described in <code>corosync.conf (5).</code> Within corosync tag are other tags which are processed as follows:</p>
<dl>
<dt>&#8211; Every tag is start of new directive</p>
<dd>
<dt>&#8211; Every tag attribute is one of options in directive</p>
<dd>
<dt>&#8211; Directive is automatically closed</p>
<dd>
<dt>&#8211; Sub-tags are processed same and stays within directive</p>
<dd></dl>
<p> For example, see /etc/corosync/corosync.xml.example </p>
<h2>Files</h2>
<dl>
<dt>/etc/corosync/corosync.xml</p>
<dd>XML version of the corosync executive configuration file. </p>
</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-corosync_overview/">corosync_overview</a></code>(8), <code><a href="/docs/linux/man/5-corosync-conf/">corosync.conf</a></code>(5), <code><a href="/docs/linux/man/8-corosync-xmlproc/">corosync-xmlproc</a></code>(8) </p>
