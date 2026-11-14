---
title: "nutscan_scan_snmp(3)"
name: "nutscan_scan_snmp"
section: "3"
letter: "n"
url: "/docs/linux/man/3-nutscan_scan_snmp/"
description: "nutscan_scan_snmp – Scan network for SNMP devices."
---

<p>nutscan_scan_snmp &#8211; Scan network for SNMP devices.</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;nut-scan.h&gt;</code></pre>
<pre>nutscan_device_t * nutscan_scan_snmp(const char * start_ip,const char * stop_ip,long timeout, nutscan_snmp_t * sec);</pre>
<h2>Description</h2>
<p>The <code>nutscan_scan_snmp()</code> function try to detect NUT compatible SNMP devices. It tries SNMP queries on every IP ranging from <i>start_ip</i> to <i>stop_ip</i>. Those IP may be either IPv4 or IPv6 addresses or host names. You MUST call <code><a href="/docs/linux/man/3-nutscan_init/">nutscan_init</a></code>(3) before using this function. This function waits up to <i>timeout</i> microseconds before considering an IP address does not respond to SNMP queries. A valid nutscan_snmp_t structure must be passed to this function. The nutscan_snmp_t structure contains the following members which must be filled as described below: </p>
<pre><code>char * 'community';
char * 'secLevel';
char * 'secName';
char * 'authPassword';
char * 'privPassword';
char * 'authProtocol';
char * 'privProtocol';</code></pre>
<p> If <i>community</i> is not NULL, SNMP v1 request are sent using this <i>community</i>. If <i>community</i> is NULL and <i>secLevel</i> is NULL, SNMP v1 is selected and <i>community</i> is set to &quot;public&quot;. In the other cases, SNMP v3 is used. <i>secLevel</i> may be one of SNMP_SEC_LEVEL_NOAUTH, SNMP_SEC_LEVEL_AUTHNOPRIV or SNMP_SEC_LEVEL_AUTHPRIV. <i>secName</i> is the security name and must be non NULL. If <i>secLevel</i> is set to SNMP_SEC_LEVEL_AUTHNOPRIV, <i>authPassword</i> must be non NULL. If <i>secLevel</i> is set to SNMP_SEC_LEVEL_AUTHPRIV, <i>authPassword</i> and <i>privPassword</i> must be non NULL. If <i>authProtocol</i> is NULL, MD5 protocol is used. Else you can set <i>authProtocol</i> to either &quot;MD5&quot; or &quot;SHA&quot;. If <i>privProtocol</i> is NULL, DES protocol is used. Else you can set <i>privProtocol</i> to either &quot;AES&quot; or &quot;DES&quot;. <i>peername</i> and <i>handle</i> are used internally and do not need any initialization.</p>
<h2>Return Value</h2>
<p>The <code>nutscan_scan_snmp()</code> function returns a pointer to a nutscan_device_t structure containing all found devices or NULL if an error occurs or no device is found.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-nutscan_init/">nutscan_init</a></code>(3), <code><a href="/docs/linux/man/3-nutscan_scan_usb/">nutscan_scan_usb</a></code>(3), <code><a href="/docs/linux/man/3-nutscan_scan_xml_http/">nutscan_scan_xml_http</a></code>(3), <code><a href="/docs/linux/man/3-nutscan_scan_nut/">nutscan_scan_nut</a></code>(3), <code><a href="/docs/linux/man/3-nutscan_scan_avahi/">nutscan_scan_avahi</a></code>(3), <code><a href="/docs/linux/man/3-nutscan_scan_ipmi/">nutscan_scan_ipmi</a></code>(3), <code><a href="/docs/linux/man/3-nutscan_display_ups_conf/">nutscan_display_ups_conf</a></code>(3), <code><a href="/docs/linux/man/3-nutscan_display_parsable/">nutscan_display_parsable</a></code>(3), <code><a href="/docs/linux/man/3-nutscan_new_device/">nutscan_new_device</a></code>(3), <code><a href="/docs/linux/man/3-nutscan_free_device/">nutscan_free_device</a></code>(3), <code><a href="/docs/linux/man/3-nutscan_add_option_to_device/">nutscan_add_option_to_device</a></code>(3), <code><a href="/docs/linux/man/3-nutscan_add_device_to_device/">nutscan_add_device_to_device</a></code>(3), <code><a href="/docs/linux/man/3-nutscan_scan_eaton_serial/">nutscan_scan_eaton_serial</a></code>(3), <code><a href="/docs/linux/man/3-nutscan_cidr_to_ip/">nutscan_cidr_to_ip</a></code>(3) </p>
