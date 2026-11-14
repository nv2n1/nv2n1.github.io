---
title: "cups-snmp(8)"
name: "cups-snmp"
section: "8"
letter: "c"
url: "/docs/linux/man/8-cups-snmp/"
description: "snmp – cups snmp backend (deprecated)"
---

<p>snmp &#8211; cups snmp backend (deprecated)</p>
<h2>Synopsis</h2>
<p><code>/usr/lib/cups/backend/snmp</code> <i>ip-address-or-hostname</i><br />
 <code>/usr/libexec/cups/backend/snmp</code> <i>ip-address-or-hostname</i><br />
 <code>lpinfo</code> <code>-v</code> <code>&#8211;include-schemes</code> snmp</p>
<h2>Description</h2>
<p>The <code>DEPRECATED</code> CUPS SNMP backend provides legacy discovery and identification of network printers using SNMPv1. When used for discovery through the scheduler, the backend will list all printers that respond to a broadcast SNMPv1 query with the &quot;public&quot; community name. Additional queries are then sent to printers that respond in order to determine the correct device URI, make and model, and other information needed for printing. </p>
<p> In the first form, the SNMP backend is run directly by the user to look up the device URI and other information when you have an IP address or hostname. This can be used for programs that need to configure print queues where the user has supplied an address but nothing else. </p>
<p> In the second form, the SNMP backend is run indirectly using the <code><a href="/docs/linux/man/8-lpinfo/">lpinfo</a></code>(8) command. The output provides all printers detected via SNMP on the configured broadcast addresses. <i>Note: no broadcast addresses are configured by default.</i></p>
<h2>Environment</h2>
<p>The DebugLevel value can be overridden using the CUPS_DEBUG_LEVEL environment variable. The MaxRunTime value can be overridden using the CUPS_MAX_RUN_TIME environment variable.</p>
<h2>Files</h2>
<p>The SNMP backend reads the <i>/etc/cups/snmp.conf</i> configuration file, if present, to set the default broadcast address, community name, and logging level.</p>
<h2>Notes</h2>
<p>The CUPS SNMP backend is deprecated and will no longer be supported in a future version of CUPS.</p>
<h2>Conforming To</h2>
<p>The CUPS SNMP backend uses the information from the Host, Printer, and Port Monitor MIBs along with some vendor private MIBs and intelligent port probes to determine the correct device URI and make and model for each printer.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/7-backend/">backend</a></code>(7), <code><a href="/docs/linux/man/5-cups-snmp-conf/">cups-snmp.conf</a></code>(5), <code><a href="/docs/linux/man/8-cupsd/">cupsd</a></code>(8), <code><a href="/docs/linux/man/8-lpinfo/">lpinfo</a></code>(8), CUPS Online Help (<a rel="nofollow" href="http://localhost:631/help)">http://localhost:631/help)</a></p>
<h2>Copyright</h2>
<p>Copyright &#169; 2021-2022 by OpenPrinting.</p>
