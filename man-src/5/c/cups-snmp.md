---
title: "cups-snmp(5)"
name: "cups-snmp"
section: "5"
letter: "c"
url: "/docs/linux/man/5-cups-snmp/"
---

snmp.conf - snmp configuration file for cups

<h2>Description</h2>

The <i>snmp.conf</i> file configures how the standard CUPS network backends (http, https, ipp, ipps, lpd, snmp, and socket) access printer information using SNMPv1 and is normally located in the <i>/etc/cups</i> directory. Each line in the file can be a configuration directive, a blank line, or a comment. Comment lines start with the # character. 

 The Community and DebugLevel directives are used by all backends. The remainder apply only to the SNMP backend (<i><a HREF="/docs/linux/man/8-cups-snmp/">cups-snmp</a>(8)</i>).

<h2>Directives</h2>

The following directives are understood by the CUPS network backends. Consult the on-line help for detailed descriptions:
<dl><dt>Address @IF(<i>name</i>)
</dt><dd></dd><dt>Address @LOCAL
</dt><dd></dd><dt>Address <i>address</i>
</dt><dd>Sends SNMP broadcast queries to the specified address(es). There is no default for the broadcast address.
</dd><dt>Community <i>name</i>
</dt><dd>Specifies the community name to use. Only a single community name may be specified. The default community name is &quot;public&quot;.
</dd><dt>DebugLevel number
</dt><dd>Specifies the logging level from 0 (none) to 3 (everything). Typically only used for debugging (thus the name). The default debug level is 0.
</dd><dt>DeviceURI &quot;regular expression&quot; device-uri [... device-uri]
</dt><dd>Specifies one or more device URIs that should be used for a given make and model string. The regular expression is used to match the detected make and model, and the device URI strings must be of the form &quot;<a HREF="scheme://%s[:port]/[path]">scheme://%s[:port]/[path]</a>&quot;, where &quot;%s&quot; represents the detected address or hostname. There are no default device URI matching rules.
</dd><dt>HostNameLookups on
</dt><dd></dd><dt>HostNameLookups off
</dt><dd>Specifies whether the addresses of printers should be converted to hostnames or left as numeric IP addresses. The default is &quot;off&quot;.
</dd><dt>MaxRunTime <i>seconds</i>
</dt><dd>Specifies the maximum number of seconds that the SNMP backend will scan the network for printers. The default is 120 seconds (2 minutes).</dd></dl>

<h2>See Also</h2>

<a HREF="/docs/linux/man/8-cups-snmp/">cups-snmp</a>(8), 
 <a rel="nofollow" HREF="http://localhost:631/help">http://localhost:631/help</a>

<h2>Copyright</h2>

Copyright 2007-2013 by Apple Inc.
