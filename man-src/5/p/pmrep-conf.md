---
title: "pmrep-conf(5)"
name: "pmrep-conf"
section: "5"
letter: "p"
url: "/docs/linux/man/5-pmrep-conf/"
description: "pmrep.conf – pmrep configuration file"
---

<p><code>pmrep.conf</code> &#8211; pmrep configuration file</p>
<h2>Description</h2>
<p><code>pmrep</code> is a customizable performance metrics reporting tool. Any available performance metric, live or archived, system and/or application, can be selected for reporting using one of the available output alternatives together with applicable formatting options. </p>
<p> The metrics of interest are named in the <i>metricspec</i> argument(s) on the <code>pmrep</code> command line. These metricspecs define individual metrics or pre-defined performance metric sets to be read from the configuration file described below. For command line argument details see <code><a href="/docs/linux/man/1-pmrep/">pmrep</a></code>(1). </p>
<p> The <code>pmrep.conf</code> configuration file allows setting default runtime values and defining any number of custom <i>metricsets</i> for <code>pmrep</code>. A metricset is a user-defined set of arbitrary performance metrics. This allows the user to create specifically crafted metricsets particularly relevant for their application or environment. Instead of being dependent on what existing tools provide or collecting the needed data with several disjoint utilities the user can create and modify custom metricsets by editing <code>pmrep.conf</code>. See below for the <i>metricset</i> specification. </p>
<p> Configuration file parameters override the corresponding built-in default values (if any). Command line parameters override the corresponding configuration file parameters (if any).</p>
<h2>File Format</h2>
<p>The file has an ini-style syntax and consists of sections and parameters. A section begins with the name of the section in square brackets and continues until the next section begins. An example section with two parameters follows: </p>
<dl>
<dd>
<pre><i>[section]</i>
<i>key</i> = <i>value</i>
<i>key2</i> = <i>value2</i></pre>
</dl>
<p> The data types used are string (no quotes needed), integer, and bool (with values of <i>yes</i> or <i>no</i>). </p>
<p> A line comment starts with a hash sign (&#8220;#&#8221;) or a semicolon (&#8220;;&#8221;). Inline comments are not supported. </p>
<p> <code>pmrep.conf</code> must be readable by the user invoking <code>pmrep</code>. </p>
<p> Any parameter described below with a corresponding command line parameter contains additional description in <code><a href="/docs/linux/man/1-pmrep/">pmrep</a></code>(1).</p>
<h2>Special Sections</h2>
<h3>The [options] section</h3>
<p>The <code>[options]</code> section is read every time <code>pmrep</code> is run and it defines the default runtime values (which may be overridden by the corresponding command line options). Metric specifications are not allowed in this section. </p>
<p> <code>Section parameters</code> </p>
<p> version (integer)</p>
<dl>
<dd>Indicates the configuration file version. Defaults to <code>1</code>. The only currently supported value is <code>1</code>.</dl>
<p> source (string)</p>
<dl>
<dd>Indicates the source for metrics. Interpreted as a PCP archive if the string contains a slash (&#8220;/&#8221;), otherwise interpreted as a hostname. Corresponding command line paraters are <code>-a</code> and <code>-h</code>. Defaults to <code>local:</code> (see <code><a href="/docs/linux/man/1-pcpintro/">PCPIntro</a></code>(1)).</dl>
<p> output (string)</p>
<dl>
<dd>Indicates the output target. Corresponding command line parameter is <code>-o</code>. For supported output targets, see <code><a href="/docs/linux/man/1-pmrep/">pmrep</a></code>(1). Defaults to <code>stdout</code>.</dl>
<p> derived (string)</p>
<dl>
<dd>Derived metric specifications. Corresponding command line parameter is <code>-e</code>. For syntax description, see <code><a href="/docs/linux/man/1-pmrep/">pmrep</a></code>(1). Undefined by default.</dl>
<p> header (bool)</p>
<dl>
<dd>Indicates whether to print headers. Corresponding command line parameter is <code>-H</code>. Defaults to <code>yes</code>.</dl>
<p> unitinfo (bool)</p>
<dl>
<dd>Indicates whether to include unit information as part of headers. Corresponding command line parameter is <code>-U</code>. Defaults to <code>yes</code>.</dl>
<p> globals (bool)</p>
<dl>
<dd>Indicates whether to include metrics from the <code>[global]</code> section (see below) for reporting. Corresponding command line parameter is <code>-G</code>. Defaults to <code>yes</code>.</dl>
<p> timestamp (bool)</p>
<dl>
<dd>Indicates whether to print the timestamp. Corresponding command line parameter is <code>-p</code>. Defaults to <code>no</code>.</dl>
<p> samples (integer)</p>
<dl>
<dd>Indicates the number of samples to print. Corresponding command line parameter is <code>-s</code>. Undefined by default (meaning unlimited number of samples if not limited by other options).</dl>
<p> interval (string)</p>
<dl>
<dd>Indicates the interval between samples. Corresponding command line parameter is <code>-o</code>. Follows the time syntax described in <code><a href="/docs/linux/man/1-pcpintro/">PCPIntro</a></code>(1). Defaults to <code>1s</code>.</dl>
<p> delay (bool)</p>
<dl>
<dd>Indicates whether to pause between samples when replaying from an archive rather than replaying at full speed. Corresponding command line parameter is <code>-d</code>. Defaults to <code>no</code>.</dl>
<p> type (string)</p>
<dl>
<dd>Indicates whether to output raw metric values by disabling all rate conversions or convert cumulative counters to rates (default). Corresponding command line parameter is <code>-r</code>. Allowed values are <code>default</code> or <code>raw</code>.</dl>
<p> width (integer)</p>
<dl>
<dd>Indicates the width of stdout output columns. Corresponding command line parameter is <code>-w</code>. Forced minimum is <code>3</code>. Defaults to the shortest width that can fit the metric label.</dl>
<p> precision (integer)</p>
<dl>
<dd>Indicates how many decimals to use for numeric non-integer output values. Corresponding command line parameter is <code>-P</code>. Defaults to <code>3</code>.</dl>
<p> delimiter (string)</p>
<dl>
<dd>Indicates the column separator. Corresponding command line parameter is <code>-l</code>. Default depends on the output target, see <code><a href="/docs/linux/man/1-pmrep/">pmrep</a></code>(1).</dl>
<p> extheader (bool)</p>
<dl>
<dd>Indicates whether to print extended header. Corresponding command line parameter is <code>-x</code>. Defaults to <code>no</code>.</dl>
<p> repeat_header (integer)</p>
<dl>
<dd>Indicates how often to repeat the header. Corresponding command line parameter is <code>-E</code>. Defaults to <code>0</code>.</dl>
<p> timefmt (string)</p>
<dl>
<dd>Indicates the format string for formatting the timestamp. Corresponding command line parameter is <code>-f</code>. Defaults to <code>%H:%M:%S</code>.</dl>
<p> interpol (bool)</p>
<dl>
<dd>Indicates whether to interpolate reported archive values. Corresponding command line parameter is <code>-u</code>. See <code><a href="/docs/linux/man/1-pmrep/">pmrep</a></code>(1) for complete description. Defaults to <code>yes</code>.</dl>
<p> count_scale (string)</p>
<dl>
<dd>Indicates the unit/scale for counter metrics. Corresponding command line parameter is <code>-q</code>. For supported syntax, see <code><a href="/docs/linux/man/1-pmrep/">pmrep</a></code>(1). Undefined (no scaling) by default.</dl>
<p> space_scale (string)</p>
<dl>
<dd>Indicates the unit/scale for space metrics. Corresponding command line parameter is <code>-b</code>. For supported syntax, see <code><a href="/docs/linux/man/1-pmrep/">pmrep</a></code>(1). Undefined (no scaling) by default.</dl>
<p> time_scale (string)</p>
<dl>
<dd>Indicates the unit/scale for time metrics. Corresponding command line parameter is <code>-y</code>. For supported syntax, see <code><a href="/docs/linux/man/1-pmrep/">pmrep</a></code>(1). Undefined (no scaling) by default.</dl>
<p> <code>Output target specific parameters</code> </p>
<dl>
<dd>The following parameters are also accepted in the <code>[options]</code> section but are typically used only in custom sections as they are applicable only to certain output targets.</dl>
<p> zabbix_server (string) (zabbix output target only)</p>
<dl>
<dd>Hostname or IP address of Zabbix server to send the metrics to. If a host is monitored by a proxy, proxy hostname or IP address should be used instead. Undefined by default.</dl>
<p> zabbix_port (integer) (zabbix output target only)</p>
<dl>
<dd>Specify port number of server trapper running on the server. Default is <code>10051</code>.</dl>
<p> zabbix_host (string) (zabbix output target only)</p>
<dl>
<dd>Specify agent hostname as registered in Zabbix frontend. Host IP address and DNS name will not work. Undefined by default.</dl>
<p> zabbix_interval (string) (zabbix output target only)</p>
<dl>
<dd>Indicates the interval to send the metrics to the Zabbix server. This can be longer than the generic <i>interval</i> to minimize the overhead when communicating with the server (as each send creates a new connection). Follows the time syntax described in <code><a href="/docs/linux/man/1-pcpintro/">PCPIntro</a></code>(1). Defaults to the generic <i>interval</i>. Zabbix tools send at most 250 metrics at a time. Ignored when reading metrics from PCP archives, in which case metrics will be sent roughly at 250 metric batches.</dl>
<h3>The [global] section</h3>
<p>The <code>[global]</code> section is used to define metrics that will be reported in addition to any other separately defined metrics or metricsets. Configuration parameters are not allowed in this section. Global metrics are reported by default, the command line option <code>-G</code> or the configuration file parameter <code>globals</code> can be used to disable global metrics. </p>
<p> <code>Section parameters</code> </p>
<dl>
<dd>No predefined parameters, only <i>metricspecs</i> allowed in this section. See below for the metricspec specification.</dl>
<h2>Custom Sections</h2>
<p>Any other section than <code>[options]</code> or <code>[global]</code> will be interpreted as a new <i>metricset</i> specification. The section name is arbitrary, typically a reference to its coverage or purpose. A custom section can contain options, metricspecs, or both. </p>
<p> All the metrics specified in a custom section will be reported when <code>pmrep</code> is instructed to use the particular custom section. <code>pmrep</code> can be executed with more than one custom section (i.e., metricset) defined in which case the combination of all the metrics specified in them will be reported. </p>
<p> <code>Section parameters</code> </p>
<dl>
<dd>Any option valid in the <code>[options]</code> section is also valid in a custom section. Any option or metric defined in the custom section will override the same option or metric possibly defined earlier in the <code>[options]</code> section. See below for the metricspec specification.</dl>
<h2>Metricset Specification</h2>
<p>There are three forms of the <i>metricspec</i>. First, on the command line a metricspec can start with a colon (&#8220;:&#8221;) to indicate a reference to a <i>metricset</i> to be read from the <code>pmrep</code> configuration file. Second, the <i>compact form</i> of a metricspec is a one-line metric specification which can be used both on the command line and in the <code>[global]</code> and custom sections of the configuration file. The only difference of its usage in the configuration file is that the metric name is used as the key and the optional specifiers as values. The compact form of the metricspec is specified in detail in <code><a href="/docs/linux/man/1-pmrep/">pmrep</a></code>(1). The third, <i>verbose form</i> of a metricspec is valid only in the configuration file. </p>
<p> A key containing a dot (&#8220;.&#8221;) is interpreted as a metric name (see above), a non-option key not containing a dot is interpreted as an identifier (see below). </p>
<p> The verbose form of a metricspec starts with a declaration consisting of a mandatory <i>identifier</i> as the key and the actual performance metric name (a PMNS leaf node) as its value. This equals to the compact form of the metricspec defining the same performance metric without any of optional specifiers defined. The identifier is arbitrary and is not used otherwise except for binding the below specifiers and the metric together. </p>
<p> The following specifiers are optional in the verbose form and can be used as keys in any order with an earlier declared identifier followed by a dot and the specifier (as in <i>identifier</i>.<i>specifier</i>):</p>
<dl>
<dd>
<dl>
<dt><i>label</i></p>
<dd>Defines a text label for the metric used by supporting output targets.</p>
<dt><i>formula</i></p>
<dd>Defines the needed arithmetic expression for the metric. For details see <code><a href="/docs/linux/man/3-pmregisterderived/">pmRegisterDerived</a></code>(3).</p>
<dt><i>instance</i></p>
<dd>This specifier is currently recognized but not implemented.</p>
<dt><i>unit</i></p>
<dd>Defines the unit/scale conversion for the metric. Needs to be dimension-compatible and is used with non-string and (currently) non-raw metrics. For allowed values, see <code><a href="/docs/linux/man/1-pmrep/">pmrep</a></code>(1).</p>
<dt><i>type</i></p>
<dd>If set to <code>raw</code> rate conversion for the metric will be disabled.</p>
<dt><i>width</i></p>
<dd>Defines the width of the output column for the metric.</dl>
</dl>
<h2>Example</h2>
<p>The following example contains a short <code>[options]</code> section setting some locally wanted default values. It then goes on to define the global metrics <code>kernel.all.sysfork</code> using the <i>compact form</i> and <code>mem.util.allcache</code> using the <i>verbose form</i> of a metricspec. The latter is a derived metric using the later specified formula. Both of these metrics will be included in reporting unless disabled with <code>-G</code> or <code>globals = no</code>. Three different <i>metricsets</i> are also specified: <code>db1</code>, <code>db2</code>, and <code>sar-w</code>. The DB sets define a host to be used as the source for the metrics. Both use the <i>verbose form</i> of a metricspec (as the non-option key <code>set</code> does not contain the dot) to include all <code>postgresql</code> related metrics. The <code>sar-w</code> set is an example how to mimic an existing tool with <code>pmrep</code>.</p>
<dl>
<dd>
<pre>[options]
timestamp = yes
interval = 2s
extheader = yes
repeat_header = 20
space_scale = MB
[global]
kernel.all.sysfork = forks,,,,8
allcache = mem.util.allcache
allcache.formula = mem.util.bufmem + mem.util.cached + mem.util.slab
[db1]
source = db-host1.example.com
set = postgresql
[db2]
source = db-host2.example.com
set = postgresql
[sar-w]
header = yes
unitinfo = no
globals = no
timestamp = yes
interval = 1s
extheader = no
precision = 2
sysfork = kernel.all.sysfork
sysfork.label = proc/s
sysfork.width = 11
pswitch = kernel.all.pswitch
pswitch.label = cswch/s
pswitch.width = 8</pre>
</dl>
<h2>Files</h2>
<dl>
<dt><code>./pmrep.conf</code></p>
<dd>Default configuration file.</p>
<dt><code>/etc/pcp/pmrep/pmrep.conf</code></p>
<dd>Example configuration file.</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-pcpintro/">PCPIntro</a></code>(1), <code><a href="/docs/linux/man/1-pmrep/">pmrep</a></code>(1), <code><a href="/docs/linux/man/3-pmregisterderived/">pmRegisterDerived</a></code>(3) and <code><a href="/docs/linux/man/3-zbxpcp/">zbxpcp</a></code>(3). </p>
