---
title: "shinken-broker(8)"
name: "shinken-broker"
section: "8"
letter: "s"
url: "/docs/linux/man/8-shinken-broker/"
description: "shinken-broker – Shinken broker daemon"
---

<p>shinken-broker &#8211; Shinken broker daemon</p>
<h2>Synopsis</h2>
<p>shinken-broker [-dr] [-c CONFIGFILE] [&#8212;debugfile DEBUGFILE]</p>
<h2>Description</h2>
<p>Shinken broker daemon. </p>
<p> The shinken-broker&#8217;s role is to export and manage data from schedulers (such as status). The management itself is done by modules. </p>
<p> The following management modules are included: * export into an NDO (Nagios Data Out) database (MySQL or Oracle backend) * export to MERLIN (Module for Effortless Redundancy and Loadbalancing In Nagios) database (MySQL backend) * service-perfdata export * export to CouchDB </p>
<p> Multiple modules can be enabled simultaneously</p>
<h2>Options</h2>
<dl>
<dt><code>&#8211;version</code></dt>
<dd>Show version number and exit</dd>
<dl>
<dd></dd></dl>
<dt><code>-c </code>CONFIGFILE, &#8211;config CONFIGFILE</dt>
<dd>Config file</dd>
<dl>
<dd></dd></dl>
<dt><code>-d, &#8211;daemon</code></dt>
<dd>Run in daemon mode</dd>
<dl>
<dd></dd></dl>
<dt><code>-r, &#8211;replace</code></dt>
<dd>Replace previously running broker</dd>
<dl>
<dd></dd></dl>
<dt><code>-h, &#8211;help</code></dt>
<dd>Print detailed help screen</dd>
<dl>
<dd></dd></dl>
<dt><code>&#8211;debugfile </code>DEBUGFILE</dt>
<dd>Enable debug logging to DEBUGFILE</dd>
<dl>
<dd></dd></dl>
</dl>
<h2>Authors</h2>
<p>David Hannequin. Arthur Gautier. Michael Leinartas.</p>
