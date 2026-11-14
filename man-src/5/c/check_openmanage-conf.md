---
title: "check_openmanage-conf(5)"
name: "check_openmanage-conf"
section: "5"
letter: "c"
url: "/docs/linux/man/5-check_openmanage-conf/"
description: "check_openmanage.conf – Configuration file for check_openmanage"
---

<p>check_openmanage.conf &#8211; Configuration file for check_openmanage</p>
<h2>File Format</h2>
<p>The file has an ini-style syntax and consists of sections and parameters. A section begins with the name of the section in square brackets and continues until the next section begins. An example of section with two keywords and parameters: </p>
<dl>
<dd>
<pre> <i>[section]</i>
 <i>key1</i> = <i>boolean</i>
 <i>key2</i> = <i>string</i></pre>
</dl>
<p> The data types used are string (no quotes needed) and bool (with values of &#8220;TRUE/FALSE&#8221;). For boolean values, &#8220;1&#8221;, &#8220;on&#8221; and &#8220;true&#8221; are equivalent, likewise for &#8220;0&#8221;, &#8220;off&#8221; and &#8220;false&#8221;. They are also case insensitive. </p>
<p> The root section or global section has no section name in brackets: </p>
<dl>
<dd>
<pre> <i>key1</i> = <i>value1</i>
 <i>key2</i> = <i>value2</i>
 
 <i>[section]</i>
 <i>key3</i> = <i>value3</i>
 <i>key4</i> = <i>value4</i></pre>
</dl>
<p> The values set in a bracket section will override those set in the root section, in case of conflicts. </p>
<p> Lines starting with &#8220;#&#8221; or &#8220;;&#8221; are considered comments and ignored, as are blank lines. </p>
<p> The configuration file must be a regular file. Owner and group does not matter, but the Nagios user must have read access.</p>
<h2>Sections And Ordering</h2>
<p>The section name should correspond to the hostname, i.e. the value passed to the <code>-H</code> or <code>&#8211;hostname</code> command line option. The section name itself can be either an exact match to the hostname, or a glob pattern. </p>
<p> The sections are read in order of significance. The root section is read first. Then any sections with glob patterns that match the hostname are read (alphabetically). Any section whose name is an exact match to the hostname is read last. </p>
<p> For boolean values, any conflicts are resolved by letting the section with the most significance (closest match to the hostname) override any previous definitions. For string values, they are simply added together. </p>
<p> Normal shell globbing may be used for the section names. This is limited to &#8220;*&#8221;, &#8220;?&#8221; and &#8220;[]&#8221;. Some examples: </p>
<dl>
<dd>
<pre> [web*.example.com]
 # matches e.g. webmail.example.com
 [pgsql-[34].example.com]
 # matches pgsql-3.example.com and pgsql-4.example.com
 [login?.example.com]
 # matches e.g. login1.example.com</pre>
</dl>
<p> <i>CAUTION</i>: Be careful not to have more than one glob pattern section match any single host. This may lead to unpredictable results.</p>
<h2>Configuration</h2>
<p>All configuration file options have a corresponding command line option. Usually, the command line option will override the configuration file option, if used simultaneously. </p>
<p> Each option is described briefly. For more information about syntax, legal values etc. refer to the corresponding command line option in <code><a href="/docs/linux/man/8-check_openmanage/">check_openmanage</a></code>(8).</p>
<h3>Check control configuration options</h3>
<p>Any keyword to the <code>&#8211;check</code> command line option are accepted in the configuration file, as &#8220;check_&lt;<i>keyword</i>&gt;&#8221;. These options take boolean values (&#8220;true&#8221; or &#8220;false&#8221;). The following keywords are accepted for check control, listed here with their default values: </p>
<p> <i>check_storage</i></p>
<dl>
<dd>Check storage subsystem (controllers, disks etc.). Default: TRUE</dl>
<p> <i>check_memory</i></p>
<dl>
<dd>Check memory (dimms). Default: TRUE</dl>
<p> <i>check_fans</i></p>
<dl>
<dd>Check chassis fans. Default: TRUE</dl>
<p> <i>check_power</i></p>
<dl>
<dd>Check power supplies. Default: TRUE</dl>
<p> <i>check_temp</i></p>
<dl>
<dd>Check temperature sensors. Default: TRUE</dl>
<p> <i>check_cpu</i></p>
<dl>
<dd>Check CPUs. Default: TRUE</dl>
<p> <i>check_voltage</i></p>
<dl>
<dd>Check voltage sensors. Default: TRUE</dl>
<p> <i>check_batteries</i></p>
<dl>
<dd>Check system batteries. Default: TRUE</dl>
<p> <i>check_amperage</i></p>
<dl>
<dd>Check amperage probes. Default: TRUE</dl>
<p> <i>check_intrusion</i></p>
<dl>
<dd>Check chassis intrusion. Default: TRUE</dl>
<p> <i>check_sdcard</i></p>
<dl>
<dd>Check SD cards. Default: TRUE</dl>
<p> <i>check_esmhealth</i></p>
<dl>
<dd>Check the ESM log health, i.e. fill grade. Default: TRUE</dl>
<p> <i>check_servicetag</i></p>
<dl>
<dd>Check that the service tag (serial number) is sane and not empty. Default: TRUE</dl>
<p> <i>check_esmlog</i></p>
<dl>
<dd>Check the ESM log content. Default: FALSE</dl>
<p> <i>check_alertlog</i></p>
<dl>
<dd>Check the alert log content. Default: FALSE</dl>
<p> <i>check_everything</i></p>
<dl>
<dd>Special option that turns on all checks. Setting this option to &quot;true&quot; will effectively negate any other check options. This option corresponds to the <code>-a</code> or <code>&#8211;all</code> command line option.</dl>
<p> If used together with the <code>&#8211;check</code> command line option, the command line option will override the configuration file, if there is a conflict. </p>
<p> For more information about check control, see the CHECK CONTROL section in <code><a href="/docs/linux/man/8-check_openmanage/">check_openmanage</a></code>(8).</p>
<h3>General configuration options</h3>
<p><i>blacklist</i> (string)</p>
<dl>
<dd>Blacklist components. The argument is a string that uses the same syntax as the <code>-b</code> or <code>&#8211;blacklist</code> command line option. </p>
<p> If used together with the <code>-b</code> or <code>&#8211;blacklist</code> command line option, the two blacklists from the config file and command line are merged together. </p>
<p> For more information about blacklisting, including syntax, see the BLACKLISTING section in <code><a href="/docs/linux/man/8-check_openmanage/">check_openmanage</a></code>(8).</dl>
<p> <i>timeout</i> (integer)</p>
<dl>
<dd>The plugin timeout. The argument is number of seconds and should be a positive integer. </p>
<p> Corresponding command line option: <code>-t</code>, <code>&#8211;timeout</code></dl>
<p> <i>performance_data</i> (boolean or string)</p>
<dl>
<dd>Turn on/off performance data reporting. Accepted values are boolean (TRUE/FALSE) or either of the keywords &#8220;minimal&#8221; and &#8220;multiline&#8221;. </p>
<p> Corresponding command line option: <code>-p</code>, <code>&#8211;perfdata</code></dl>
<p> <i>legacy_performance_data</i> (boolean)</p>
<dl>
<dd>With version 3.7.0, performance data output changed. The new format is not compatible with the old format. Users who wish to postpone switching to the new performance data API may use this option. This option takes a boolean value. </p>
<p> Corresponding command line option: <code>&#8211;legacy-perfdata</code></dl>
<p> <i>temperature_unit</i> (char)</p>
<dl>
<dd>The temperature unit used for reporting, performance data etc. can be set with the this option. </p>
<p> Corresponding command line option: <code>&#8211;tempunit</code> </p>
<p> <i>NOTE</i>: The command line option <code>-F</code> or <code>&#8211;fahrenheit</code> will override both the command line option and the configuration file option.</dl>
<p> <i>temp_threshold_warning</i> (string)</p>
<dl>
<dd>Custom temperature warning limits. </p>
<p> Corresponding command line option: <code>-w</code>, <code>&#8211;warning</code></dl>
<p> <i>temp_threshold_critical</i> (string)</p>
<dl>
<dd>Custom temperature critical limits. </p>
<p> Corresponding command line option: <code>-c</code>, <code>&#8211;critical</code></dl>
<p> <i>vdisk_critical</i> (boolean)</p>
<dl>
<dd>Make all alerts concerning virtual disks appear as critical. </p>
<p> Corresponding command line option: <code>&#8211;vdisk-critical</code></dl>
<h3>SNMP configuration options</h3>
<p>Several SNMP related options may be set in the configuration file. The configuration file may contain the following SNMP options: </p>
<p> <i>snmp_community</i> (string)</p>
<dl>
<dd>The SNMP community string. </p>
<p> Corresponding command line option: <code>-C</code>, <code>&#8211;community</code></dl>
<p> <i>snmp_version</i> (string)</p>
<dl>
<dd>The SNMP protocol version. </p>
<p> Corresponding command line option: <code>-P</code>, <code>&#8211;protocol</code></dl>
<p> <i>snmp_port</i> (integer)</p>
<dl>
<dd>The remote port number used with SNMP. </p>
<p> Corresponding command line option: <code>&#8211;port</code></dl>
<p> <i>snmp_use_ipv6</i> (boolean)</p>
<dl>
<dd>Toggle using IPv6 instead of IPv4. </p>
<p> Corresponding command line option: <code>-6</code>, <code>&#8211;ipv6</code></dl>
<p> <i>snmp_use_tcp</i> (boolean)</p>
<dl>
<dd>Toggle using TCP instead of UDP as transport protocol. </p>
<p> Corresponding command line option: <code>&#8211;tcp</code></dl>
<p> <i>snmp_timeout</i> (integer)</p>
<dl>
<dd>Set timeout in seconds for the SNMP object of Net::SNMP. </p>
<p> Corresponding command line option: <code>&#8211;snmp-timeout</code></dl>
<h3>Output configuration options</h3>
<p>These options gives some control over the output given by the plugin. </p>
<p> <i>output_servicetag</i> (boolean)</p>
<dl>
<dd>Toggle inclusion of the service tag (serial number) of the monitored host in alerts. </p>
<p> Corresponding command line option: <code>-i</code>, <code>&#8211;info</code></dl>
<p> <i>output_servicestate</i> (boolean)</p>
<dl>
<dd>Toggle inclusion of the service state in alerts. </p>
<p> Corresponding command line option: <code>-s</code>, <code>&#8211;state</code></dl>
<p> <i>output_servicestate_abbr</i> (boolean)</p>
<dl>
<dd>Toggle inclusion of the abbreviated service state in alerts. </p>
<p> Corresponding command line option: <code>-S</code>, <code>&#8211;short-state</code></dl>
<p> <i>output_sysinfo</i> (boolean)</p>
<dl>
<dd>Toggle inclusion of a short system information summary in case of alerts. </p>
<p> Corresponding command line option: <code>-e</code>, <code>&#8211;extinfo</code></dl>
<p> <i>output_blacklist</i> (boolean)</p>
<dl>
<dd>Toggle showing any blacklistings in the OK output. </p>
<p> Corresponding command line option: <code>-B</code>, <code>&#8211;show-blacklist</code></dl>
<p> <i>output_ok_verbosity</i> (integer)</p>
<dl>
<dd>This option specifies how much information is shown in the OK output. </p>
<p> Corresponding command line option: <code>-o</code>, <code>&#8211;ok-info</code></dl>
<p> <i>output_html</i> (boolean or code)</p>
<dl>
<dd>This option toggles HTML output. Argument is either a boolean value, or a country or area code. Se <code><a href="/docs/linux/man/8-check_openmanage/">check_openmanage</a></code>(8) for more information and list of supported country and area codes. </p>
<p> Corresponding command line option: <code>-I</code>, <code>&#8211;htmlinfo</code></dl>
<p> <i>output_post_message</i> (string)</p>
<dl>
<dd>Specify one line of information to be shown after alerts. </p>
<p> Corresponding command line option: <code>&#8211;postmsg</code></dl>
<p> <i>output_hide_servicetag</i> (boolean)</p>
<dl>
<dd>This option toggles censoring of the service tag (serial number) in any output from the plugin. </p>
<p> Corresponding command line option: <code>&#8211;hide-servicetag</code></dl>
<h2>Example</h2>
<p>The following example shows a typical check_openmanage config, with a global section and a few host sections.</p>
<dl>
<dd>
<pre># Global definitions
output_blacklist = true
output_ok_verbosity = 3
output_sysinfo = true
output_html = us
# Local definitions (exact or glob pattern)
[esx??.example.com]
 blacklist = ctrl_fw=all
 check_storage = false
[mysql01.example.com]
 performance_data = true
[web0[123].example.com]
 performance_data = true
 blacklist = ctrl_driver=all
[*.hpc.example.com]
 performance_data = true</pre>
</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-check_openmanage/">check_openmanage</a></code>(8), <a rel="nofollow" href="http://folk.uio.no/trondham/software/check_openmanage.html">http://folk.uio.no/trondham/software/check_openmanage.html</a></p>
<h2>Authors</h2>
<p><code>Trond Hasle Amundsen &lt;t.h.amundsen [at] usit.uio.no&gt;</code></p>
