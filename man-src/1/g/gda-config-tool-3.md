---
title: "gda-config-tool-3(1)"
name: "gda-config-tool-3"
section: "1"
letter: "g"
url: "/docs/linux/man/1-gda-config-tool-3/"
description: "gda-config-tool-3.0 – Tool for managing libgda configuration file."
---

<h2>NAME</h2>
<p> gda-config-tool-3.0 &#8211; Tool for managing libgda configuration file.</p>
<h2>SYNOPSIS</h2>
<p> <code>gda-config-tool-3.0 [OPTIONS]</code></p>
<h2>DESCRIPTION</h2>
<p> The <i>gda-config-tool-3.0</i> program can be used create/edit/remove a libgda provider. It can be used both as a command line program and an interactive program.</p>
<h2>OPTIONS</h2>
<p> The following options are supported:</p>
<dl>
<dt><code>-?</code>, <code>&#8211;help</code></dt>
<dd> Displays command line options.</dd>
<dt><code>&#8211;usage</code></dt>
<dd> Display brief usage message.</dd>
<dt><code>&#8211;l</code>, <code>&#8211;list-providers</code></dt>
<dd> Lists installed providers.</dd>
<dt><code>&#8211;L</code>, <code>&#8211;list-datasources</code></dt>
<dd> Lists configured data sources.</dd>
<dt><code>&#8211;n</code>, <code>&#8211;name=NAME</code></dt>
<dd> User-assigned name for the provider and connection settings.</dd>
<dt><code>&#8211;u</code>, <code>&#8211;user=NAME</code></dt>
<dd> User name to pass to the provider when connecting.</dd>
<dt><code>&#8211;p</code>, <code>&#8211;password=NAME</code></dt>
<dd> Password for the given user to pass to the DB backend.</dd>
<dt><code>&#8211;P</code>, <code>&#8211;provider=NAME</code></dt>
<dd> Provider name.</dd>
<dt><code>&#8211;d</code>, <code>&#8211;DSN=&quot;NAME=VALUE;&#8230;&quot;</code></dt>
<dd> Semi-colon separated list of parameter=value option to pass to the provider.</dd></dl>
<h2>ENVIRONMENT VARIABLES</h2>
<dl>
<dt>NONE</dt>
<dd></dd></dl>
<h2>FILES</h2>
<p> $(sysconfdir)/libgda/config</p>
<dl>
<dt>
</dt><dd> Global configurations settings read for every user.</dd></dl>
<p> ${HOME}/.libgda/config</p>
<dl>
<dt>
</dt><dd> User settings. Override global settings.</dd></dl>
<h2>SEE ALSO</h2>
<p> <code>mergeant(1),</code> <code>gda-config-3.0(5)</code> </p>
<h2>SYNOPSIS</h2>
<p> <code>gda-config-tool-3.0 [OPTIONS]</code></p>
<h2>DESCRIPTION</h2>
<p> The <i>gda-config-tool-3.0</i> program can be used create/edit/remove a libgda provider. It can be used both as a command line program and an interactive program.</p>
<h2>OPTIONS</h2>
<p> The following options are supported:</p>
<dl>
<dt><code>-?</code>, <code>&#8211;help</code></dt>
<dd> Displays command line options.</dd>
<dt><code>&#8211;usage</code></dt>
<dd> Display brief usage message.</dd>
<dt><code>&#8211;l</code>, <code>&#8211;list-providers</code></dt>
<dd> Lists installed providers.</dd>
<dt><code>&#8211;L</code>, <code>&#8211;list-datasources</code></dt>
<dd> Lists configured data sources.</dd>
<dt><code>&#8211;n</code>, <code>&#8211;name=NAME</code></dt>
<dd> User-assigned name for the provider and connection settings.</dd>
<dt><code>&#8211;u</code>, <code>&#8211;user=NAME</code></dt>
<dd> User name to pass to the provider when connecting.</dd>
<dt><code>&#8211;p</code>, <code>&#8211;password=NAME</code></dt>
<dd> Password for the given user to pass to the DB backend.</dd>
<dt><code>&#8211;P</code>, <code>&#8211;provider=NAME</code></dt>
<dd> Provider name.</dd>
<dt><code>&#8211;d</code>, <code>&#8211;DSN=&quot;NAME=VALUE;&#8230;&quot;</code></dt>
<dd> Semi-colon separated list of parameter=value option to pass to the provider.</dd></dl>
<h2>ENVIRONMENT VARIABLES</h2>
<dl>
<dt>NONE</dt>
<dd></dd></dl>
<h2>FILES</h2>
<p> $(sysconfdir)/libgda/config</p>
<dl>
<dt>
</dt><dd> Global configurations settings read for every user.</dd></dl>
<p> ${HOME}/.libgda/config</p>
<dl>
<dt>
</dt><dd> User settings. Override global settings.</dd></dl>
<h2>SEE ALSO</h2>
<p> <code>mergeant(1),</code> <code>gda-config-3.0(5)</code> </p>
