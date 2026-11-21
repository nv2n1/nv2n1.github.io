---

title: "sosreport(1)"
name: "sosreport"
section: "1"
letter: "s"
url: "/docs/linux/man/1-sosreport/"
description: "sosreport – Collect and package diagnostic and support data"
---

<p> sosreport &#8211; Collect and package diagnostic and support data</p>
<h2>SYNOPSIS</h2>
<p> <code>sosreport</code><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>[-l|&#8211;list-plugins]<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>[-n|&#8211;skip-plugins plugin-names]<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>[-e|&#8211;enable-plugins plugin-names]<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>[-o|&#8211;only-plugins plugin-names]<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>[-a|&#8211;alloptions]&nbsp;<wbr>[-v|&#8211;verbose]<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>[-k plug.opt|&#8211;plugin-option plug.opt]<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>[&#8211;no-report]&nbsp;<wbr>[&#8211;config-file conf]<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>[&#8211;batch]&nbsp;<wbr>[&#8211;build]&nbsp;<wbr>[&#8211;debug]<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>[&#8211;name name]&nbsp;<wbr>[&#8211;case-id id]&nbsp;<wbr>[&#8211;ticket-number nr]<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>[-s|&#8211;sysroot SYSROOT]<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>[-c|&#8211;chroot&nbsp;<wbr>{auto|always|never}<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>[&#8211;tmp-dir directory]<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>[-p|&#8211;profile profile-name]<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>[&#8211;list-profiles]<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>[&#8211;verify]<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>[&#8211;log-size]<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>[&#8211;all-logs]<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>[-z|&#8211;compression-type method]<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>[&#8211;experimental]<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>[-h|&#8211;help] </p>
<h2>DESCRIPTION</h2>
<p> <code>sosreport</code> generates an archive of configuration and diagnostic information from the running system. The archive may be stored locally or centrally for recording or tracking purposes or may be sent to technical support representatives, developers or system administrators to assist with technical fault-finding and debugging. </p>
<p> Sos is modular in design and is able to collect data from a wide range of subsystems and packages that may be installed. An XML or HTML report summarizing the collected information is optionally generated and stored within the archive.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-l, &#8211;list-plugins</code></dt>
<dd> List all available plugins and their options. Plug-ins that would not be enabled by the current configuration are listed separately.</dd>
<dt><code>-n, &#8211;skip-plugins PLUGNAME[,PLUGNAME]</code></dt>
<dd> Disable the specified plugin(s). Multiple plug-ins may be specified by repeating the option or as a comma-separated list.</dd>
<dt><code>-e, &#8211;enable-plugins PLUGNAME[,PLUGNAME]</code></dt>
<dd> Enable the specified plugin(s). Multiple plug-ins may be specified by repeating the option or as a comma-separated list.</dd>
<dt><code>-o, &#8211;only-plugins PLUGNAME[,PLUGNAME]</code></dt>
<dd> Enable the specified plugin(s) only (all other plugins should be disabled). Multiple plugins may be specified by repeating the option or as a comma-separated list.</dd>
<dt><code>-k PLUGNAME.PLUGOPT[=VALUE], &#8211;plugin-option=PLUGNAME.PLUGOPT[=VALUE]</code></dt>
<dd> Specify plug-in options. The option PLUGOPT is enabled, or set to the specified value in the plug-in PLUGNAME.</dd>
<dt><code>-a, &#8211;alloptions</code></dt>
<dd> Set all boolean options to True for all enabled plug-ins.</dd>
<dt><code>-v, &#8211;verbose</code></dt>
<dd> Increase logging verbosity. May be specified multiple times to enable additional debugging messages.</dd>
<dt><code>-q, &#8211;quiet</code></dt>
<dd> Only log fatal errors to stderr.</dd>
<dt><code>&#8211;no-report</code></dt>
<dd> Disable HTML/XML report writing.</dd>
<dt><code>&#8211;config-file CONFIG</code></dt>
<dd> Specify alternate configuration file.</dd>
<dt><code>-s, &#8211;sysroot SYSROOT</code></dt>
<dd> Specify an alternate root file system path. Useful for collecting reports from containers and images.</dd>
<dt><code>-c, &#8211;chroot {auto|always|never}</code></dt>
<dd> Set the chroot mode. When &#8211;sysroot is used commands default to executing with SYSROOT as the root directory (unless disabled by a specific plugin). This can be overriden by setting &#8211;chroot to &quot;always&quot; (alwyas chroot) or &quot;never&quot; (always run in the host namespace).</dd>
<dt><code>&#8211;tmp-dir DIRECTORY</code></dt>
<dd> Specify alternate temporary directory to copy data as well as the compressed report.</dd>
<dt><code>&#8211;list-profiles</code></dt>
<dd> Display a list of available profiles and the plugins that they enable.</dd>
<dt><code>-p, &#8211;profile NAME</code></dt>
<dd> Only run plugins that correspond to the given profile. Multple profiles may be specified as a comma-separated list; the set of plugins executed is the union of each of the profile&#8217;s plugin sets. Currently defined profiles include: boot, cluster, desktop, debug, hardware, identity, network, openstack, packagemanager, security, services, storage, sysmgmt, system, performance, virt, and webserver.</dd>
<dt><code>&#8211;verify</code></dt>
<dd> Instructs plugins to perform plugin-specific verification during data collection. This may include package manager verification, log integrity testing or other plugin defined behaviour. Use of &#8211;verify may cause the time taken to generate a report to be considerably longer.</dd>
<dt><code>&#8211;log-size</code></dt>
<dd> Places a global limit on the size (in MiB) of any collected set of logs. The limit is applied separately for each set of logs collected by any plugin.</dd>
<dt><code>&#8211;all-logs</code></dt>
<dd> Tell plugins to collect all possible log data ignoring any size limits and including logs in non-default locations. This option may significantly increase the size of reports.</dd>
<dt><code>-z, &#8211;compression-type METHOD</code></dt>
<dd> Override the default compression type specified by the active policy.</dd>
<dt>
</dt><dt><code>&#8211;batch</code></dt>
<dd>
</dd><dd> Generate archive without prompting for interactive input.</dd>
<dt><code>&#8211;name NAME</code></dt>
<dd> Specify a name to be used for the archive.</dd>
<dt><code>&#8211;case-id NUMBER</code></dt>
<dd> Specify a case identifier to associate with the archive. Identifiers may include alphanumeric characters, commas and periods (&#8216;.&#8217;). Synonymous with &#8211;ticket-number.</dd>
<dt><code>&#8211;ticket-number NUMBER</code></dt>
<dd> Specify a ticket number or other identifier to associate with the archive. Identifiers may include alphanumeric characters, commas and periods (&#8216;.&#8217;). Synonymous with &#8211;case-id.</dd>
<dt><code>&#8211;build</code></dt>
<dd> Do not archive copied data. Causes sosreport to leave an uncompressed archive as a temporary file or directory tree.</dd>
<dt><code>&#8211;debug</code></dt>
<dd> Enable interactive debugging using the python debugger. Exceptions in sos or plug-in code will cause a trap to the pdb shell.</dd>
<dt><code>&#8211;experimental</code></dt>
<dd> Enable plugins marked as experimental. Experimental plugins may not have been tested for this port or may still be under active development.</dd>
<dt><code>&#8211;help</code></dt>
<dd> Display usage message.</dd></dl>
<h2>MAINTAINER</h2>
<pre>
Bryn M. Reeves &lt;bmr [at] redhat.com&gt;
</pre>
<h2>AUTHORS &amp; CONTRIBUTORS</h2>
<p> See <code>AUTHORS</code> file in /usr/share/doc/sosreport.</p>
<h2>TRANSLATIONS</h2>
<pre>
Translations are handled by transifex (<a rel="nofollow" href="https://fedorahosted.org/transifex/)">https://fedorahosted.org/transifex/)</a>
</pre>
