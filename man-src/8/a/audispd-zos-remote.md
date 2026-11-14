---
title: "audispd-zos-remote(8)"
name: "audispd-zos-remote"
section: "8"
letter: "a"
url: "/docs/linux/man/8-audispd-zos-remote/"
description: "audispd-zos-remote – z/OS Remote-services Audit dispatcher plugin"
---

<p>audispd-zos-remote &#8211; z/OS Remote-services Audit dispatcher plugin</p>
<h2>Synopsis</h2>
<p><code>audispd-zos-remote [</code> <i>config-file</i> <code>]</code></p>
<h2>Description</h2>
<p><code>audispd-zos-remote</code> is a remote-auditing plugin for the Audit subsystem. It should be started by the <code><a href="/docs/linux/man/8-audispd/">audispd</a></code>(8) daemon and will forward all incoming audit events, as they happen, to a configured z/OS SMF (Service Management Facility) database, through an IBM Tivoli Directory Server (ITDS) set for Remote Audit service. See <code>SMF MAPPING</code> section below for more information about the resulting SMF record format. <code><a href="/docs/linux/man/8-audispd/">audispd</a></code>(8) must be configured to start the plugin. This is done by a configuration file usually located at <i>/etc/audisp/plugins.d/audispd-zos-remote.conf</i>, but multiple instances can be spawned by having multiple configuration files in <i>/etc/audisp/plugins.d</i> for the same plugin executable (see <code><a href="/docs/linux/man/8-audispd/">audispd</a></code>(8)). Each instance needs a configuration file, located by default at <i>/etc/audisp/zos-remote.conf</i>. Check <code><a href="/docs/linux/man/5-zos-remote-conf/">zos-remote.conf</a></code>(5) for details about the plugin configuration. </p>
<h2>Options</h2>
<dl>
<dt>config-file</p>
<dd>Use an alternate configuration file instead of <i>/etc/audisp/zos-remote.conf</i>. </p>
</dl>
<h2>Signals</h2>
<p><code>audispd-zos-remote</code> reacts to SIGTERM and SIGHUP signals (according to the <code><a href="/docs/linux/man/8-audispd/">audispd</a></code>(8) specification):</p>
<dl>
<dt><code>SIGHUP</code></p>
<dd>Instructs the <code>audispd-zos-remote</code> plugin to re-read it&#8217;s configuration and flush existing network connections.</p>
<dt><code>SIGTERM</code></p>
<dd>Performs a clean exit. <code>audispd-zos-remote</code> will wait up to 10 seconds if there are queued events to be delivered, dropping any remaining queued events after that time. </p>
</dl>
<h2>IBM z/OS ITDS Server and RACF configuration</h2>
<p>In order to use this plugin, you must have an IBM z/OS v1R8 (or higher) server with IBM Tivoli Directory Server (ITDS) configured for Remote Audit service. For more detailed information about how to configure the z/OS server for Remote Auditing, refer to <code>z/OS V1R8.0-9.0 Intergrated Security Services Enterprise Identity Mapping (EIM) Guide and Reference</code> </p>
<pre>(<i><a rel="nofollow" href="http://publibz.boulder.ibm.com/cgi-bin/bookmgr_OS390/FRAMESET/EIMA1140/CCONTENTS?DT=20070827115119">http://publibz.boulder.ibm.com/cgi-bin/bookmgr_OS390/FRAMESET/EIMA1140/CCONTENTS?DT=20070827115119</a></i>),
chapter &quot;2.0 - Working with remote services&quot;.</pre>
<h3>Enable ITDS to process Remote Audit requests</h3>
<p>To enable ITSD to process Remote Audit requests, the user ID associated with ITDS must be granted READ access to the IRR.AUDITX FACILITY Class profile (the profile used to protect the R_Auditx service). This user ID can usually be found in the STARTED Class profile for the ITDS started procedure. If the identity associated with ITDS is <i>ITDSUSER</i>, the administrator can configure RACF to grant Remote Auditing processing to ITDS with the following TSO commands:</p>
<dl>
<dt><i>TSO Commands: Grant ITDSUSER READ access to IRR.AUDITX FACILITY Class profile</i></p>
<dd>
<pre>rdefine FACILITY IRR.RAUDITX uacc(none)
permit IRR.RAUDITX class(FACILITY) id(ITDSUSER) access(READ)</pre>
</dl>
<h3>Create/enable RACF user ID to perform Remote Audit requests</h3>
<p>A z/OS RACF user ID is needed by the plugin &#8211; Every Audit request performed by the plugin will use a RACF user ID, as configured in the plugin configuration <code><a href="/docs/linux/man/5-zos-remote-conf/">zos-remote.conf</a></code>(5). This user ID needs READ access to FACILITY Class resource IRR.LDAP.REMOTE.AUDIT. If the user ID is <i>BINDUSER</i>, the administrator can configure RACF to enable this user to perform Remote Auditing requests with the following TSO commands:</p>
<dl>
<dt><i>TSO Commands: Enable BINDUSER to perform Remote Audit requests</i></p>
<dd>
<pre>rdefine FACILITY IRR.LDAP.REMOTE.AUDIT uacc(none)
permit IRR.LDAP.REMOTE.AUDIT class(FACILITY) id(BINDUSER) access(READ)</pre>
</dl>
<h3>Add @LINUX Class to RACF</h3>
<p>When performing remote auditing requests, the <code>audispd-zos-remote</code> plugin will use the special <code>@LINUX </code> <i>CDT Class </i> and the audit record type (eg.: <code>SYSCALL</code>, <code>AVC</code>, <code>PATH</code>&#8230;) as the <i>CDT Resource Class</i> for all events processed. To make sure events are logged, the RACF server must be configured with a Dynamic CDT Class named <code>@LINUX</code> with correct sizes and attributes. The following TSO commands can be used to add this class:</p>
<dl>
<dt><i>TSO Commands: Add @LINUX CDT Class</i></p>
<dd>
<pre>rdefine cdt @LINUX cdtinfo(posit(493) FIRST(alpha,national,numeric,special) OTHER(alpha,national,numeric,special) RACLIST(REQUIRED) case(asis) generic(allowed) defaultuacc(none) maxlength(246))
setr classact(cdt)
setr raclist(cdt)
setr raclist(cdt) refresh
setr classact(@LINUX)
setr raclist(@LINUX)
setr generic(@LINUX)</pre>
</dl>
<h3>Add profiles to the @LINUX Class</h3>
<p>Once the CDT Class has been defined, you can add profiles to it, specifying resources (wildcards allowed) to log or ignore. The following are examples:</p>
<dl>
<dt><i>TSO Commands: Log only AVC records (One generic and one discrete profile):</i></p>
<dd>
<pre>rdefine @LINUX * uacc(none) audit(none(read)) 
rdefine @LINUX AVC uacc(none) audit(all(read)) 
setr raclist(@LINUX) refresh</pre>
<dt><i>TSO Commands: Log everything (One generic profile):</i></p>
<dd>
<pre>rdefine @LINUX * uacc(none) audit(all(read))
setr raclist(@LINUX) refresh</pre>
</dl>
<p> Resources always match the single profile with the <i>best</i> match. </p>
<p> There are many other ways to define logging in RACF. Please refer to the server documentation for more details.</p>
<h2>SMF Mapping</h2>
<p>The ITDS Remote Audit service will cut SMF records of type 83 subtype 4 everytime it processes a request. This plugin will issue a remote audit request for every incoming Linux Audit record (meaning that one Linux record will map to one SMF record), and fill this type&#8217;s records with the following:</p>
<h3>Link Value</h3>
<p>The Linux event serial number, encoded in network-byte order hexadecimal representation. Records within the same Event share the same Link Value.</p>
<h3>Violation</h3>
<p>Always zero (0) &#8211; <i>False</i></p>
<h3>Event Code</h3>
<p>Always two (2) &#8211; <i>Authorization</i> event</p>
<h3>Event Qualifier</h3>
<p>Zero (0) &#8211; <i>Success</i>, if the event reported <code>success=yes</code> or <code>res=success</code>, Three (3) &#8211; <i>Fail</i>, if the event reported <code>success=no</code> or <code>res=failed</code>, or One (1) &#8211; <i>Info</i> otherwise.</p>
<h3>Class</h3>
<p>Always <i>@LINUX</i></p>
<h3>Resource</h3>
<p>The Linux record type for the processed record. e.g.: <i>SYSCALL</i>,<i>AVC</i>,<i>PATH</i>,<i>CWD</i> etc.</p>
<h3>Log String</h3>
<p>Textual message bringing the RACF user ID used to perform the request, plus the Linux hostname and the record type for the first record in the processed event. e.g.: <i>Remote audit request from RACFUSER. Linux (hostname.localdomain):USER_AUTH </i></p>
<h3>Data Field List</h3>
<p>Also known as <i>relocates</i>, this list will bring all the field names and values in a <code>fieldname=value</code> format, as a type 114 (<code>Appication specific Data</code>) relocate. The plug-in will try to interpret those fields (i.e.: use human-readable username <code>root</code> instead of numeric userid <code>0</code>) whenever possible. Currently, this plugin will also add a relocate type 113 (<code>Date And Time Security Event Occurred</code>) with the Event Timestamp in the format as returned by <code><a href="/docs/linux/man/3-ctime/">ctime</a></code>(3).</p>
<h2>Errors</h2>
<p>Errors and warnings are reported to syslog (under DAEMON facility). In situations where the event was submitted but the z/OS server returned an error condition, the logged message brings a name followed by a human-readable description. Below are some common errors conditions:</p>
<dl>
<dt><code>NOTREQ &#8211; No logging required</code></p>
<dd>Resource (audit record type) is not set to be logged in the RACF server &#8211; The @LINUX Class profile governing this audit record type is set to ignore. See <code>IBM z/OS RACF Server configuration</code></p>
<dt><code>UNDETERMINED &#8211; Undetermined result</code></p>
<dd>No profile found for specified resource. There is no @LINUX Class configured or no @LINUX Class profile associated with this audit record type. See <code>IBM z/OS RACF Server configuration</code></p>
<dt><code>UNAUTHORIZED &#8211; The user does not have authority the R_auditx service</code></p>
<dd>The user ID associated with the ITDS doesn&#8217;t have READ access to the IRR.AUDITX FACILITY Class profile. See <code>IBM z/OS RACF Server configuration</code></p>
<dt><code>UNSUF_AUTH &#8211; The user has unsuficient authority for the requested function</code></p>
<dd>The RACF user ID used to perform Remote Audit requests (as configured in <code><a href="/docs/linux/man/5-zos-remote-conf/">zos-remote.conf</a></code>(5)) don&#8217;t have access to the IRR.LDAP.REMOTE.AUDIT FACILITY Class profile. See <code>IBM z/OS RACF Server configuration</code> </p>
<h2>Bugs</h2>
<p>The plugin currently does remote auditing in a best-effort basis, and will dischard events in case the z/OS server cannot be contacted (network failures) or in any other case that event submission fails. </p>
<h2>Files</h2>
<p>/etc/audisp/plugins.d/audispd-zos-remote.conf /etc/audisp/zos-remote.conf</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-auditd/">auditd</a></code>(8), <code><a href="/docs/linux/man/5-zos-remote-conf/">zos-remote.conf</a></code>(5).</p>
<h2>Author</h2>
<p>Klaus Heinrich Kiwi &lt;klausk [at] br.ibm.com&gt;</p>
