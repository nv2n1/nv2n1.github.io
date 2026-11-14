---
title: "host_conf(5)"
name: "host_conf"
section: "5"
letter: "h"
url: "/docs/linux/man/5-host_conf/"
description: "host_conf – xxQS_NAMExx execution host configuration file format"
---

<p>host_conf &#8211; xxQS_NAMExx execution host configuration file format</p>
<h2>Description</h2>
<p><i>Host_conf</i> reflects the format of the template file for the execution host configuration. Via the <code>-ae</code> and <code>-me</code> options of the command, you can add execution hosts and modify the configuration of any execution host in the cluster. Default execution host entries are added automatically as soon as a registers to for the very first time from a certain host. The <code>-sel</code> switch can be used to display a list of execution hosts currently configured in your xxQS_NAMExx system. Via the <code>-se</code> option you can print the execution host configuration of a specified host. </p>
<p> The special hostname &quot;global&quot; can be used to define cluster global characteristics. </p>
<p> Note xxQS_NAMExx allows backslashes (\) be used to escape newline characters. The backslash and the newline are replaced with a space character before any interpretation.</p>
<h2>Format</h2>
<p>The format of a <i>host_conf</i> file is defined as follows:</p>
<h3><code>hostname</code></h3>
<p>The execution host&#8217;s name in the format for <i>host_name</i> in</p>
<h3><code>load_scaling</code></h3>
<p>A comma-separated list of scaling values to be applied to each or part of the load values being reported by the on the host. The load scaling factors are intended to level hardware or operating system-specific differences between execution hosts. </p>
<p> The syntax of a load factor specification is as follows: First the name of the load value (as defined in the &quot;host&quot; complex) is given and, separated by an equal sign, the load scaling value is provided. No blanks are allowed in the load_scaling value string. </p>
<p> The parameter <code>load_scaling</code> is not meaningful for the definition of the &quot;global&quot; host.</p>
<h3><code>complex_values</code></h3>
<p><code>complex_values</code> defines quotas for resource attributes managed via this host. Each complex attribute is followed by an &quot;=&quot; sign and the value specification compliant with the complex attribute type (see Quota specifications are separated by commas. </p>
<p> The quotas are related to the resource consumption of all jobs on a host in the case of consumable resources (see for details on consumable resources), or they are interpreted on a per-job slot basis in the case of non-consumable resources. Consumable resource attributes are commonly used to manage free memory, free disk space or available floating software licenses, while non-consumable attributes usually define distinctive characteristics like type of hardware installed. </p>
<p> For consumable resource attributes, an available resource amount is determined by subtracting the current resource consumption of all running jobs on the host from the quota in the <code>complex_values</code> list. Jobs can only be dispatched to a host if no resource requests exceed any corresponding resource availability obtained by this scheme. The quota definition in the <code>complex_values</code> list is automatically replaced by the current load value reported for this attribute, if load is monitored for this resource and if the reported load value is more stringent than the quota. This effectively avoids oversubscription of resources. </p>
<p> <code>Note:</code> Load values replacing the quota specifications may have become more stringent because they have been scaled (see <code>load_scaling</code> above) and/or load adjusted (see The <i>-F</i> option of and the load display in the queue control dialog (activated by clicking on a queue icon while the &quot;Shift&quot; key is pressed) provide detailed information on the actual availability of consumable resources and on the origin of the values taken into account currently. </p>
<p> <code>Note also:</code> The resource consumption of running jobs (used for the availability calculation) as well as the resource requests of the jobs waiting to be dispatched either may be derived from explicit user requests during job submission (see the <i>-l</i> option to or from a &quot;default&quot; value configured for an attribute by the administrator (see The <i>-r</i> option to can be used for retrieving full detail on the actual resource requests of all jobs in the system. </p>
<p> For non-consumable resources xxQS_NAMExx simply compares the job&#8217;s attribute requests with the corresponding specification in <code>complex_values</code> taking the relation operator of the complex attribute definition into account (see If the result of the comparison is &quot;true&quot;, the host is suitable for the job with respect to the particular attribute. For parallel jobs each job slot to be occupied by a parallel task is meant to provide the same resource attribute value. </p>
<p> <code>Note:</code> Only numeric complex attributes can be defined as consumable resources and hence non-numeric attributes are always handled on a per job slot basis. </p>
<p> The default value for this parameter is NONE, i.e. no administrator defined resource attribute quotas are associated with the host.</p>
<h3><code>load_values</code></h3>
<p>This entry cannot be configured but is only displayed in case of a <code>-se</code> command. All load values are displayed as reported by the on the host. The load values are shown in a comma-separated list. Each load value starts with its name, followed by an equal sign and the reported value.</p>
<h3><code>processors</code></h3>
<p><code>Note:</code> Deprecated, may be removed in future release.<br />
 This entry cannot be configured but is only displayed in case of a <code>-se</code> command. Its value is the number of &quot;processors&quot; which has been detected by on the corresponding host. This may include &quot;hardware threads&quot; reported by the operating system.</p>
<h3><code>usage_scaling</code></h3>
<p>The <code>usage_scaling</code> parameter scales the usage figures, but only for the purposes of share tree calculations, i.e. a scaling factor of 0 means that use of the relevant host(s) will be ignored for share tree purposes (e.g. if hosts are dedicated for a specific use). The format is equivalent to <code>load_scaling</code> (see above). However, the only valid attributes to be scaled are <code>cpu</code> for CPU time consumption, <code>mem</code> for memory consumption aggregated over the lifetime of jobs and <code>io</code> for data transferred via any I/O devices. The default NONE means &quot;no scaling&quot;, i.e. all scaling factors are 1.</p>
<h3><code>user_lists</code></h3>
<p>The <code>user_lists</code> parameter contains a comma-separated list of so called user access lists as described in Each user contained in at least one of the listed access lists has access to the host. If the <code>user_lists</code> parameter is set to NONE (the default), any user has access if not explicitly excluded via the <code>xuser_lists</code> parameter described below. If a user is contained both in an access list in <code>xuser_lists</code> and <code>user_lists</code> the user is denied access to the host.</p>
<h3><code>xuser_lists</code></h3>
<p>The <code>xuser_lists</code> parameter contains a comma-separated list of so called user access lists as described in Each user contained in at least one of the access lists is not allowed to access the host. If the <code>xuser_lists</code> parameter is set to NONE (the default), any user has access. If a user is contained both in <code>xuser_lists</code> and <code>user_lists</code>, the user is denied access to the host.</p>
<h3><code>projects</code></h3>
<p>The <code>projects</code> parameter contains a comma-separated list of projects that have access to the host. Any projects not in this list are denied access to the host. If set to NONE (the default), any project has access if not specifically excluded via the <code>xprojects</code> parameter described below. If a project is in both <code>projects</code> and <code>xprojects</code>, the project is denied access to the host.</p>
<h3><code>xprojects</code></h3>
<p>The <code>xprojects</code> parameter contains a comma-separated list of projects that are denied access to the host. If set to NONE (the default), no projects are denied access other than those denied access based on the <code>projects</code> parameter described above. If a project is in both <code>projects</code> and <code>xprojects</code>, the project is denied access to the host.</p>
<h3><code>report_variables</code></h3>
<p>The <code>report_variables</code> parameter contains a comma-separated list of variables that should be written to the reporting file. The variables listed here will be written to the reporting file when a load report arrives from an execution host. </p>
<p> Default settings can be done in the global host. Host-specific settings for report_variables will override settings from the global host.</p>
<h2>See Also</h2>
<p><i><a href="/docs/linux/man/1-uptime/">uptime</a></i>(1),</p>
<h2>Copyright</h2>
<p>See for a full statement of rights and permissions.</p>
