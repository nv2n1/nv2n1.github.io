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
<dt><code>&#8211;version</code></dt>
<dd> displays the net-snmp version number</dd>
<dt><code>&#8211;indent-options</code></dt>
<dd> displays the indent options from the Coding Style</dd>
<dt><code>&#8211;debug-tokens</code></dt>
<dd> displays a example command line to search to source code for a list of available debug tokens</dd></dl>
<p> SNMP Setup commands:</p>
<dl>
<dt><code>&#8211;create-snmpv3-user</code> [-ro] [-a authpass] [-x privpass]</dt>
<dd> [-X DES|AES] [-A MD5|SHA] [username]</dd></dl>
<p> These options produce the various compilation flags needed when building external SNMP applications:</p>
<dl>
<dt><code>&#8211;base-cflags</code></dt>
<dd> lists additional compilation flags needed for external applications (excludes <code>-I</code>. and extra developer warning flags, if any)</dd>
<dt><code>&#8211;cflags</code></dt>
<dd> lists additional compilation flags needed</dd>
<dt><code>&#8211;libs</code></dt>
<dd> lists libraries needed for building applications</dd>
<dt><code>&#8211;agent-libs</code></dt>
<dd> lists libraries needed for building subagents</dd>
<dt><code>&#8211;netsnmp-libs</code></dt>
<dd> lists netsnmp specific libraries</dd>
<dt><code>&#8211;external-libs</code></dt>
<dd> lists libraries needed by netsnmp libs</dd>
<dt><code>&#8211;netsnmp-agent-libs</code></dt>
<dd> lists netsnmp specific agent libraries</dd>
<dt> <code>&#8211;external-agent-libs</code> lists libraries needed by netsnmp libs</dt></dl>
<dd>Automated subagent building (produces an OUTPUTNAME binary file): [This feature has not been extensively tested, use at your own risk.]</dd>
<dl>
<dt><code>&#8211;compile-subagent</code> OUTPUTNAME [&#8211;norm] [&#8211;cflags flags]</dt>
<dd> [&#8211;ldflags flags] mibmodule1.c [&#8230;]]</dd>
<dt><code>&#8211;norm</code></dt>
<dd> leave the generated .c file around to read.</dd>
<dt><code>&#8211;cflags</code> flags</dt>
<dd> extra cflags to use (e.g. <code>-I</code>&#8230;).</dd>
<dt><code>&#8211;ldflags</code> flags</dt>
<dd> extra ld flags to use (e.g. <code>-L</code>&#8230; <code>-l</code>&#8230;).</dd>
<dt>
</dt><dd> Details on how the net-nsmp package was compiled:</dd>
<dt><code>&#8211;configure-options</code></dt>
<dd> Display original configure arguments</dd>
<dt><code>&#8211;snmpd-module-list</code></dt>
<dd> Display the modules compiled into the agent</dd>
<dt><code>&#8211;prefix</code></dt>
<dd> Display the installation prefix </dd>
</dl>
<h2>Index</h2>
