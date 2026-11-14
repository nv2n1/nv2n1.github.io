---
title: "net-snmp-config(1)"
name: "net-snmp-config"
section: "1"
letter: "n"
url: "/docs/linux/man/1-net-snmp-config/"
description: "net-snmp-config – returns information about installed net-snmp libraries and binaries"
---

<h2>NAME</h2>
<p> net-snmp-config &#8211; returns information about installed net-snmp libraries and binaries</p>
<h2>SYNOPSIS</h2>
<p> <code>net-snmp-config</code> [OPTIONS]</p>
<h2>DESCRIPTION</h2>
<p> The <i>net-snmp-config</i> shell script is designed to retrieve the configuration information about the libraries and binaries dealing with the Simple Network Management Protocol (SNMP), built from the <code>net-snmp </code> source package. The information is particularly useful for applications that need to link against the SNMP libraries and hence must know about any other libraries that must be linked in as well. </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>&#8211;version</code></p>
<dd> displays the net-snmp version number</p>
<dt><code>&#8211;indent-options</code></p>
<dd> displays the indent options from the Coding Style</p>
<dt><code>&#8211;debug-tokens</code></p>
<dd> displays a example command line to search to source code for a list of available debug tokens</dl>
<p> SNMP Setup commands:</p>
<dl>
<dt><code>&#8211;create-snmpv3-user</code> [-ro] [-a authpass] [-x privpass]</p>
<dd> [-X DES|AES] [-A MD5|SHA] [username]</dl>
<p> These options produce the various compilation flags needed when building external SNMP applications:</p>
<dl>
<dt><code>&#8211;base-cflags</code></p>
<dd> lists additional compilation flags needed for external applications (excludes <code>-I</code>. and extra developer warning flags, if any)</p>
<dt><code>&#8211;cflags</code></p>
<dd> lists additional compilation flags needed</p>
<dt><code>&#8211;libs</code></p>
<dd> lists libraries needed for building applications</p>
<dt><code>&#8211;agent-libs</code></p>
<dd> lists libraries needed for building subagents</p>
<dt><code>&#8211;netsnmp-libs</code></p>
<dd> lists netsnmp specific libraries</p>
<dt><code>&#8211;external-libs</code></p>
<dd> lists libraries needed by netsnmp libs</p>
<dt><code>&#8211;netsnmp-agent-libs</code></p>
<dd> lists netsnmp specific agent libraries</p>
<dt> <code>&#8211;external-agent-libs</code> lists libraries needed by netsnmp libs</dl>
<dd>Automated subagent building (produces an OUTPUTNAME binary file): [This feature has not been extensively tested, use at your own risk.]</p>
<dl>
<dt><code>&#8211;compile-subagent</code> OUTPUTNAME [&#8211;norm] [&#8211;cflags flags]</p>
<dd> [&#8211;ldflags flags] mibmodule1.c [&#8230;]]</p>
<dt><code>&#8211;norm</code></p>
<dd> leave the generated .c file around to read.</p>
<dt><code>&#8211;cflags</code> flags</p>
<dd> extra cflags to use (e.g. <code>-I</code>&#8230;).</p>
<dt><code>&#8211;ldflags</code> flags</p>
<dd> extra ld flags to use (e.g. <code>-L</code>&#8230; <code>-l</code>&#8230;).</p>
<dt>
<dd> Details on how the net-nsmp package was compiled:</p>
<dt><code>&#8211;configure-options</code></p>
<dd> Display original configure arguments</p>
<dt><code>&#8211;snmpd-module-list</code></p>
<dd> Display the modules compiled into the agent</p>
<dt><code>&#8211;prefix</code></p>
<dd> Display the installation prefix </p>
</dl>
<h2>Index</h2>
