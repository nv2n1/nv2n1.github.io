---
title: "lnst-pool-wizard(1)"
name: "lnst-pool-wizard"
section: "1"
letter: "l"
url: "/docs/linux/man/1-lnst-pool-wizard/"
description: "lnst-pool-wizard – Linux Network Stack Test Pool Wizard"
---

<h2 class="name">NAME</h2>
<p> lnst-pool-wizard &#8211; Linux Network Stack Test Pool Wizard </p>
<h2>SYNOPSIS</h2>
<p> <code>lnst-pool-wizard</code> [<code>-h</code>] [<i>MODE</i>] [<code>-p </code><i>pool_dir</i>] [<i>HOSTNAME[:PORT]</i>&#8230;]</p>
<h2>DESCRIPTION</h2>
<p> Linux Network Stack Test is a tool that supports development and execution of automated and portable network tests. For detailed description of the architecture of LNST please refer to project website (link listed on <code>INTERNET RESOURCES</code> bellow). </p>
<p> <code>lnst-pool-wizard</code> is a script that runs wizard for creating slave machine description XML files</p>
<h2>MODES</h2>
<dl>
<dt><code>-i, &#8211;interactive</code></p>
<dd> If any hostnames are specified, wizard will try to connect to them, get available interfaces and ask user which of the interfaces should be added to the result description XML file. If no hostname is specified, wizard will ask for hostname via prompt.</p>
<dt><code>-n, &#8211;noninteractive</code></p>
<dd> Wizard will try to connect to all hostnames specified in arguments and for each one create XML file with all available interfaces.</p>
<dt><code>-v, &#8211;virtual</code></p>
<dd> This mode is for virtual hosts created by libvirt. Wizard queries user for libvirt domain and tries to retrieve IP address from DHCP Leases. This IP address will be used as hostname in Slave Description XML file.</dl>
<h2>OPTIONS</h2>
<dl>
<dt><code>-h, &#8211;help</code></p>
<dd> Display usage of this command.</p>
<dt><code>-p, &#8211;pool_dir=</code><i>directory</i></p>
<dd> Directory where result XML files will be stored. If none is entered default location will be used (~/.lnst/pool)</dl>
<h2>INTERNET RESOURCES</h2>
<p> Project Homepage: <a rel="nofollow" href="http://lnst-project.org/">http://lnst-project.org/</a><br />
 Online Documentation: <a rel="nofollow" href="https://github.com/jpirko/lnst/wiki#learn">https://github.com/jpirko/lnst/wiki#learn</a><br />
 Git Source Tree: <a rel="nofollow" href="https://github.com/jpirko/lnst">https://github.com/jpirko/lnst</a><br />
 Mailing List: &lt;lnst-developers [at] lists.fedorahosted.org&gt; </p>
<h2>AUTHORS</h2>
<p> <code>Jiri Pirko</code> &lt;jiri [at] resnulli.us&gt;<br />
 <code>Jan Tluka</code> &lt;jtluka [at] redhat.com&gt;<br />
 <code>Ondrej Lichtner</code> &lt;olichtne [at] redhat.com&gt;<br />
 <code>Jiri Prochazka</code> &lt;jprochaz [at] redhat.com&gt;<br />
 <code>Jiri Zupka</code> &lt;jzupka [at] redhat.com&gt;<br />
 <code>Radek Pazdera</code> &lt;radek [at] pazdera.co.uk&gt;</p>
<h2>COPYRIGHT</h2>
<p> Copyright (C) 2011-2015 Red Hat, Inc. </p>
<p> LNST is distributed under GNU General Public License version 2. See the file &quot;COPYING&quot; in the source distribution for information on terms &amp; conditions for accessing and otherwise using LNST. </p>
<h2>Index</h2>
