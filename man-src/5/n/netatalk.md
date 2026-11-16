---
title: "netatalk(5)"
name: "netatalk"
section: "5"
letter: "n"
url: "/docs/linux/man/5-netatalk/"
description: "netatalk.conf – Configuration file used by"
---

<p>netatalk.conf &#8211; Configuration file used by </p>
<p>netatalk(8) to determine its general configuration</p>
<h2>Description</h2>
<p><code>/etc/atalk//netatalk.conf</code> is the configuration file used by afpd to determine what portions of the file system will be shared via Appletalk, as well as their behaviors. Any line not prefixed with <code>#</code> is interpreted. The configuration lines are composed like: <i>option</i> <code>=</code> <i>value</i> The possible options and their meanings are: <code>AFPD_GUEST</code></p>
<dl>
<dd>Sets the id of the guest user to a local user on the system.</dd></dl>
<p> <code>AFPD_MAX_CLIENTS</code></p>
<dl>
<dd>Sets the maximum number of clients that can simultaneously connect to the server.</dd></dl>
<p> <code>AFPD_RUN</code></p>
<dl>
<dd>Enables the afpd daemon if set to &quot;yes&quot;. This should be enabled if you are planning on using netatalk as a file server.</dd></dl>
<p> <code>AFPD_UAM_LIST</code></p>
<dl>
<dd>Sets the default UAMs for afpd (and papd, if printer authentication is compiled in) to use. </dd>
<pre><code>Example:
AFPD_UAMLIST=&quot;-U uams_guest.so,uams_randnum.so&quot;</code></pre>
<p> <code>CNID_METAD_RUN</code></p>
<dl>
<dd>Enables the cnid_metad daemon if set to &quot;yes&quot;. This should be enabled if you are going to use the dbd CNID backend.</dd></dl>
<p> <code>ATALK_BGROUND</code></p>
<dl>
<dd>&quot;yes&quot; will set netatalk to initialize in the background, and &quot;no&quot; will cause normal initialization.</dd></dl>
<p> <code>ATALK_NAME</code></p>
<dl>
<dd>Sets the machines&#8217; Appletalk name.</dd></dl>
<p> <code>ATALK_ZONE</code></p>
<dl>
<dd>Sets the machines&#8217; Appletalk zone.</dd></dl>
<p> <code>ATALKD_RUN</code></p>
<dl>
<dd>Enables the atalkd daemon if set to &quot;yes&quot;. This should be enabled if you are planning on providing Appletalk services.</dd></dl>
<p> <code>PAPD_RUN</code></p>
<dl>
<dd>Enables the papd daemon if set to &quot;yes&quot;. This should be enabled if you are planning on using netatalk as a print server.</dd></dl>
<p> <code>ATALK_MAC_CHARSET</code></p>
<dl>
<dd>Set the Mac client codepage, used by atalkd and papd to convert extended characters from the Unix to the Mac codepage.</dd></dl>
<p> <code>ATALK_UNIX_CHARSET</code></p>
<dl>
<dd>Set the Unix codepage, used by atalkd and papd to convert extended characters from the Unix to the Mac codepage. Has to match the codepage of the configuration files.</dd></dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-atalkd/">atalkd</a></code>(8), <code>atalkd.conf</code>(5) </p>
</dl>