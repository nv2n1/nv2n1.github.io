---
title: "virt-xml-validate(1)"
name: "virt-xml-validate"
section: "1"
letter: "v"
url: "/docs/linux/man/1-virt-xml-validate/"
description: "virt-xml-validate – validate libvirt XML files against a schema"
---

<h2 class="name">NAME</h2>
<p> virt-xml-validate &#8211; validate libvirt XML files against a schema </p>
<h2>SYNOPSIS</h2>
<p> <code>virt-xml-validate</code> <i>XML-FILE</i> [<i>SCHEMA-NAME</i>] </p>
<p> <code>virt-xml-validate</code> <i></i><font SIZE="-1"><i>OPTION</i></font><i></i></p>
<h2>DESCRIPTION</h2>
<p> Validates a libvirt <font SIZE="-1">XML</font> for compliance with the published schema. The first compulsory argument is the path to the <font SIZE="-1">XML</font> file to be validated. The optional second argument is the name of the schema to validate against. If omitted, the schema name will be inferred from the name of the root element in the <font SIZE="-1">XML</font> document. </p>
<p> Valid schema names currently include</p>
<dl>
<dt>&quot;domainsnapshot&quot;</p>
<dd> The schema for the <font SIZE="-1">XML</font> format used by domain snapshot configuration</p>
<dt>&quot;domain&quot;</p>
<dd> The schema for the <font SIZE="-1">XML</font> format used by guest domains configuration</p>
<dt>&quot;network&quot;</p>
<dd> The schema for the <font SIZE="-1">XML</font> format used by virtual network configuration</p>
<dt>&quot;storagepool&quot;</p>
<dd> The schema for the <font SIZE="-1">XML</font> format used by storage pool configuration</p>
<dt>&quot;storagevol&quot;</p>
<dd> The schema for the <font SIZE="-1">XML</font> format used by storage volume descriptions</p>
<dt>&quot;nodedev&quot;</p>
<dd> The schema for the <font SIZE="-1">XML</font> format used by node device descriptions</p>
<dt>&quot;capability&quot;</p>
<dd> The schema for the <font SIZE="-1">XML</font> format used to declare driver capabilities</p>
<dt>&quot;nwfilter&quot;</p>
<dd> The schema for the <font SIZE="-1">XML</font> format used by network traffic filters</p>
<dt>&quot;secret&quot;</p>
<dd> The schema for the <font SIZE="-1">XML</font> format used by secrets descriptions</p>
<dt>&quot;interface&quot;</p>
<dd> The schema for the <font SIZE="-1">XML</font> format used by physical host interfaces</dl>
<h2>OPTIONS</h2>
<dl>
<dt><code>-h, &#8211;help</code></p>
<dd> Display command line help usage then exit.</p>
<dt><code>-V, &#8211;version</code></p>
<dd> Display version information then exit.</dl>
<h2>EXIT STATUS</h2>
<p> Upon successful validation, an exit status of 0 will be set. Upon failure a non-zero status will be set.</p>
<h2>AUTHOR</h2>
<p> Daniel P.Berrange</p>
<h2>BUGS</h2>
<p> Report any bugs discovered to the libvirt community via the mailing list &lt;<a rel="nofollow" href="http://libvirt.org/contact.html">http://libvirt.org/contact.html</a>&gt; or bug tracker &lt;<a rel="nofollow" href="http://libvirt.org/bugs.html">http://libvirt.org/bugs.html</a>&gt;. Alternatively report bugs to your software distributor / vendor.</p>
<h2>COPYRIGHT</h2>
<p> Copyright (C) 2009-2013 by Red Hat, Inc. Copyright (C) 2009 by Daniel P. Berrange</p>
<h2>LICENSE</h2>
<p> virt-xml-validate is distributed under the terms of the <font SIZE="-1">GNU GPL</font> v2+. This is free software; see the source for copying conditions. There is <font SIZE="-1">NO</font> warranty; not even for <font SIZE="-1">MERCHANTABILITY</font> or <font SIZE="-1">FITNESS FOR A PARTICULAR PURPOSE</font></p>
<h2>SEE ALSO</h2>
<p> <i><a href="/docs/linux/man/1-virsh/">virsh</a></i>(1), online <font SIZE="-1">XML</font> format descriptions &lt;<a rel="nofollow" href="http://libvirt.org/format.html">http://libvirt.org/format.html</a>&gt; </p>
<h2>Index</h2>
