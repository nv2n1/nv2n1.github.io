---
title: "cups-snmp-conf(5)"
name: "cups-snmp-conf"
section: "5"
letter: "c"
url: "/docs/linux/man/5-cups-snmp-conf/"
description: "snmp.conf – snmp configuration file for cups (deprecated)"
---

<p>snmp.conf &#8211; snmp configuration file for cups (deprecated)</p>
<h2>Description</h2>
<p>The <code>snmp.conf</code> file configures how the standard CUPS network backends (http, https, ipp, ipps, lpd, snmp, and socket) access printer information using SNMPv1 and is normally located in the <i>/etc/cups</i> directory. Each line in the file can be a configuration directive, a blank line, or a comment. Comment lines start with the # character. </p>
<p> The Community and DebugLevel directives are used by all backends. The remainder apply only to the SNMP backend &#8211; <code><a href="/docs/linux/man/8-cups-snmp/">cups-snmp</a></code>(8).</p>
<h2>Directives</h2>
<p>The following directives are understood by the CUPS network backends:</p>
<dl>
<dt><code>Address @IF(</code><i>name</i><code>)</code></p>
<dd>
<dt><code>Address @LOCAL</code></p>
<dd>
<dt><code>Address </code><i>address</i></p>
<dd>Sends SNMP broadcast queries (for discovery) to the specified address(es). There is no default for the broadcast address.</p>
<dt><code>Community </code><i>name</i></p>
<dd>Specifies the community name to use. Only a single community name may be specified. The default community name is &quot;public&quot;. If no name is specified, all SNMP functions are disabled.</p>
<dt><code>DebugLevel </code><i>number</i></p>
<dd>Specifies the logging level from 0 (none) to 3 (everything). Typically only used for debugging (thus the name). The default debug level is 0.</p>
<dt><code>DeviceURI &quot;</code><i>regular expression</i><code>&quot; </code><i>device-uri </i>[&#8230; <i>device-uri</i>]</p>
<dd>Specifies one or more device URIs that should be used for a given make and model string. The regular expression is used to match the detected make and model, and the device URI strings must be of the form &quot;<a href="scheme://%s[:port]/[path]">scheme://%s[:port]/[path]</a>&quot;, where &quot;%s&quot; represents the detected address or hostname. There are no default device URI matching rules.</p>
<dt><code>HostNameLookups on</code></p>
<dd>
<dt><code>HostNameLookups off</code></p>
<dd>Specifies whether the addresses of printers should be converted to hostnames or left as numeric IP addresses. The default is &quot;off&quot;.</p>
<dt><code>MaxRunTime </code><i>seconds</i></p>
<dd>Specifies the maximum number of seconds that the SNMP backend will scan the network for printers. The default is 120 seconds (2 minutes).</dl>
<h2>Notes</h2>
<p>CUPS backends are deprecated and will no longer be supported in a future feature release of CUPS. Printers that do not support IPP can be supported using applications such as <code><a href="/docs/linux/man/1-ippeveprinter/">ippeveprinter</a></code>(1).</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-cups-snmp/">cups-snmp</a></code>(8), CUPS Online Help (<a rel="nofollow" href="http://localhost:631/help)">http://localhost:631/help)</a></p>
<h2>Copyright</h2>
<p>Copyright &#169; 2021-2022 by OpenPrinting.</p>
