---
title: "complex(5)"
name: "complex"
section: "5"
letter: "c"
url: "/docs/linux/man/5-complex/"
description: "complex – xxQS_NAMExx complexes configuration file format"
---

<p>complex &#8211; xxQS_NAMExx complexes configuration file format</p>
<h2>Description</h2>
<p><i>Complex</i> reflects the format of the xxQS_NAMExx complex configuration. The definition of complex attributes provides all pertinent information concerning the resource attributes a user may request for a xxQS_NAMExx job via the <code>-l</code> option, and for the interpretation of these parameters within the xxQS_NAMExx system. The xxQS_NAMExx complex object defines all entries which are used for configuring the global, host, and queue objects. The system has a set of pre-defined entries, which are assigned to a host or queue by default. In addition, the user can define new entries and assign them to one or more objects. Each load value has to have a corresponding complex entry object, which defines the type and the relational operator for it.</p>
<h3><code>Defining resource attributes</code></h3>
<p>The complex configuration should not be accessed directly. In order to add or modify complex entries, the options -Mc and -mc should be used instead. While the -Mc option takes a <i>complex</i> configuration file as an argument and overrides the current configuration, the -mc option brings up an editor filled in with the current <i>complex</i> configuration. The provided list contains all definitions of resource attributes in the system. Adding a new entry means to provide: name, shortcut, type, relop, requestable, consumable, default, and urgency. The fields are described below. Changing one is easily done by updating the field to change, and removing an entry by deleting its definition. An attribute can only be removed when it is not referenced in a host or queue object anymore. Also the system has a set of default resource attributes which are always attached to a host or queue. They cannot be deleted, nor can the type of such an attribute be changed.</p>
<h3><code>Working with resource attributes</code></h3>
<p>Before a user can request a resource attribute it has to be attached to the global, host, or queue object. The resource attribute exists only for the objects to which it was attached. If it is attached to the global object (qconf -me global), it exists system-wide. Attached to a host object (qconf -me <i>host</i>), it exists only on that host, and attached to queue object (qconf -mq <i>queue</i>), only on that queue. When an administrator attaches a resource attribute to an object, they also have to assign a value to it: the resource limit. A load sensor may be run to adjust the value presented by a host down from that limit. For instance, to support requests for free space in the /tmp filesystem, set up a load sensor to report the value (probably using and attach a sufficiently high limit to each host, e.g. </p>
<pre>qconf -aattr exechost complex_values tmp_free=10T $(qconf -sel)</pre>
<h3><code>Default queue resource attributes</code></h3>
<p>By default there is a selection of parameters in the queue configuration as defined in The principal queue configuration parameters requestable for a job by the user are: </p>
<pre><dl><dt><dd>qname
hostname
notify
calendar
min_cpu_interval 
tmpdir
seq_no
s_rt
h_rt
s_cpu
h_cpu
s_data
h_data
s_stack
h_stack
s_core
h_core
s_rss
h_rss
</dl></pre>
<h3><code>Default host resource attributes</code></h3>
<p>The standard set of host-related attributes consists of two categories. The first category is built by several queue configuration attributes which are particularly suitable to be managed on a host basis. These attributes are: </p>
<pre><dl><dt><dd>slots
s_vmem
h_vmem
s_fsize
h_fsize
</dl></pre>
<p>(Please refer to for details.) <code>Note:</code> Defining these attributes in the host complex is no contradiction to having them also in the queue configuration. It allows maintaining the corresponding resources on a host level, and at the same time on a queue level. Total virtual free memory (h_vmem) can be managed for a host, for example, and a subset of the total amount can be associated with a queue on that host. The second attribute category in the standard host complex is that of the default load values every periodically reports load to The reported load values are either the standard xxQS_NAMExx load values, such as the CPU load average (see <i><a href="/docs/linux/man/1-uptime/">uptime</a></i>(1)), or load values defined by the xxQS_NAMExx administration (see the <code>load_sensor</code> parameter in the cluster or host configuration (see for details). The definition of characteristics for the standard load values is part of the default host complex, while administrator-defined load values require extension of the host complex. Please refer to for detailed information on the standard set of load values.</p>
<h3><code>Overriding attributes</code></h3>
<p>An attribute can be assigned to the global object, host object, and queue object at the same time. On the host level it might get its value from the user-defined resource limit and a load sensor. If the attribute is a consumable, we have, in addition to the resource limit and its load report at host level, also the internal usage which the system keeps track of. The merge is done as follows: In general an attribute can be overridden on a lower level<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;&#8211; global by hosts and queues<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;&#8211; hosts by queues and load values or resource limits on the same level. We have one limitation for overriding attributes based on their relational operator: <code>!=</code> and <code>==</code> operators can only be overridden on the same level, not on a lower level. The user-defined value always overrides the load value. <code>&gt;=</code>, <code>&gt;</code>, <code>&lt;=</code>, and <code>&lt;</code> operators can only be overridden when the new value is more restrictive than the old one. In the case of a consumable at host level which has also a load sensor, the system checks for the current usage, and if the internal accounting is more restrictive than the load sensor report, the internal value is kept; if the load sensor report is more restrictive, that one is kept. </p>
<h2>Format</h2>
<p>The principal format of a <i>complex</i> configuration is that of a tabulated list. Each line starting with a &#8216;#&#8217; character is a comment line. Each non-comment line defines one element of the complex. Backslashes (\) be used to escape newline characters. The backslash and the newline are replaced with a space character before any interpretation. </p>
<p> An element definition line consists of the following 8 column entries per line (in order of appearance):</p>
<h3><code>name</code></h3>
<p>The name of the complex element to be used to request this attribute for a job in the <code>-l</code> option. A complex attribute name (see <i>complex_name</i> in may appear only once across all complexes, i.e. the complex attribute definition is unique.</p>
<h3><code>shortcut</code></h3>
<p>A shortcut for <code>name</code> which may also be used to request this attribute for a job in the <code>-l</code> option. A given shortcut may appear only once across all complexes, so as to avoid the possibility of ambiguous complex attribute references.</p>
<h3><code>type</code></h3>
<p>This setting determines how the corresponding values are to be treated by xxQS_NAMExx internally in comparisons or in load scaling for the load complex entries:</p>
<dl>
<dt>&bull;</p>
<dd>With <code>INT</code> only raw integers are allowed.</p>
<dt>&bull;</p>
<dd>With <code>DOUBLE</code> floating point numbers in double precision (decimal and scientific notation) can be specified.</p>
<dt>&bull;</p>
<dd>With <code>TIME</code> time specifiers are allowed. Refer to for a format description.</p>
<dt>&bull;</p>
<dd>With <code>MEMORY</code> memory size specifiers are allowed. Refer to for a format description.</p>
<dt>&bull;</p>
<dd>With <code>BOOL</code> the strings TRUE and FALSE are allowed. When used in a load formula (refer to TRUE and FALSE get mapped into &#8216;1&#8217; and &#8216;0&#8217;.</p>
<dt>&bull;</p>
<dd>With <code>STRING</code> all strings are allowed and are used for wildcard regular boolean expression matching. Please see the man page for <code>expression</code> definition. </p>
<pre><dl><dt><dd>Examples:
 -l arch=&quot;*x*|sol*&quot; :
 results in &quot;arch=lx-x86&quot; OR &quot;arch=lx-amd64&quot;
 OR &quot;arch=sol-amd64&quot; OR ...
 -l arch=&quot;sol-x??&quot; :
 results in &quot;arch=sol-x86&quot; OR &quot;arch=sol-x64&quot; OR ...
 -l arch=&quot;lx2[246]-x86&quot; :
 results in &quot;arch=lx22-x86&quot; OR &quot;arch=lx24-x86&quot;
 OR &quot;arch=lx26-x86&quot;
 -l arch=&quot;lx2[4-6]-x86&quot; :
 results in &quot;arch=lx24-x86&quot; OR &quot;arch=lx25-x86&quot;
 OR &quot;arch=lx26-x86&quot;
 -l arch=&quot;lx2[24-6]-x86&quot; :
 results in &quot;arch=lx22-x86&quot; OR &quot;arch=lx24-x86&quot;
 OR &quot;arch=lx25-x86&quot; OR &quot;arch=lx26-x86&quot;
 -l arch=&quot;!lx-x86&amp;!sol-amd64&quot; :
 results in NEITHER &quot;arch=lx-x86&quot; NOR &quot;arch=sol-amd64&quot;
 -l arch=&quot;lx2[4|6]-amd64&quot; :
 results in &quot;arch=lx24-amd64&quot; OR &quot;arch=lx26-amd64&quot;
</dl></pre>
<dt>&bull;</p>
<dd><code>CSTRING</code> is like <code>STRING</code> except comparisons are case insensitive.</p>
<dt>&bull;</p>
<dd><code>RESTRING</code> is the same as <code>STRING</code> for historical compatibility, but is deprecated and may be removed in future..</p>
<dt>&bull;</p>
<dd><code>HOST</code> is like <code>CSTRING</code> but the expression must match a valid host name.</dl>
<h3><code>relop</code></h3>
<p>The relation operator is used when the value requested by the user for this parameter is compared against the corresponding value configured for the considered queues. If the result of the comparison is false, the job cannot run in this queue. Possible relation operators are &quot;==&quot;, &quot;&lt;&quot;, &quot;&gt;&quot;, &quot;&lt;=&quot;, &quot;&gt;=&quot; and &quot;EXCL&quot;. The only valid operator for string type attributes is &quot;==&quot;. </p>
<p> The &quot;EXCL&quot; relation operator implements exclusive scheduling and is only valid for consumable boolean type attributes. Exclusive means the result of the comparison is only true if a job requests to be exclusive, and no other exclusive or non-exclusive job uses the complex. If the job does not request to be exclusive and no other exclusive job uses the complex the comparison is also true.</p>
<h3><code>requestable</code></h3>
<p>The entry can be used in a resource request if this field is set to &#8216;y&#8217; or &#8216;yes&#8217;. If set to &#8216;n&#8217; or &#8216;no&#8217; this entry cannot be used by a user in order to request a queue or a class of queues. If the entry is set to &#8216;forced&#8217; or &#8216;f&#8217; the attribute has to be requested by a job, or it is rejected. </p>
<p> To enable resource request enforcement the existence of the resource has to be defined. This can be done on a cluster global, per host and per queue basis. The definition of resource availability is performed with the complex_values entry in and</p>
<h3><code>consumable</code></h3>
<p>The <code>consumable</code> parameter can be set to either &#8216;yes&#8217; (&#8216;y&#8217; abbreviated), &#8216;no&#8217; (&#8216;n&#8217;) or &#8216;JOB&#8217; (&#8216;j&#8217;). It can be set to &#8216;yes&#8217; and &#8216;JOB&#8217; only for numeric attributes (INT, DOUBLE, MEMORY, TIME &#8211; see <code>type</code> above). If set to &#8216;yes&#8217; or &#8216;JOB&#8217; the consumption of the corresponding resource can be managed by xxQS_NAMExx internal bookkeeping. In this case xxQS_NAMExx accounts for the consumption of this resource for all running jobs and ensures that jobs are only dispatched if the xxQS_NAMExx internal bookkeeping indicates enough available consumable resources. Consumables are an efficient means to manage limited resources such as available memory, free space on a file system, network bandwidth or floating software licenses. </p>
<p> A consumable defined by &#8216;y&#8217; is a per-slot consumable, which means the limit is multiplied by the number of slots being used by the job before being applied. In case of &#8216;j&#8217; the consumable is a per-job consumable. This resource is debited as requested (without multiplication) from the allocated master queue. The resource need not be available for the slave task queues. </p>
<p> Consumables can be combined with default or user-defined load parameters (see and i.e. load values can be reported for consumable attributes, or the consumable flag can be set for load attributes. The xxQS_NAMExx consumable resource management takes both the load (measuring availability of the resource) and the internal bookkeeping into account in this case, and makes sure that neither exceeds a given limit. </p>
<p> To enable consumable resource management, the basic availability of a resource has to be defined. This can be done on a cluster global, per host and per queue basis, and these categories may supersede each other in the given order (i.e. a host can restrict availability of a cluster resource and a queue can restrict host and cluster resources). The definition of resource availability is performed with the <code>complex_values</code> entry in and The <code>complex_values</code> definition of the &quot;global&quot; host specifies cluster global consumable settings. To each consumable complex attribute in a <code>complex_values</code> list, a value is assigned which denotes the maximum available amount for that resource. The internal bookkeeping will subtract from this total the assumed resource consumption by all running jobs as expressed through the jobs&#8217; resource requests. </p>
<p> <code>Note:</code> Jobs can be forced to request a resource and thus to specify their assumed consumption via a <code>forced</code> value of the <code>requestable </code> parameter (see above). </p>
<p> <code>Note also:</code> A default resource consumption value can be pre-defined by the administrator for consumable attributes not explicitly requested by the job (see the <code>default</code> parameter below). This is meaningful only if requesting the attribute is not enforced as explained above.</p>
<h3><code>default</code></h3>
<p>Meaningful only for consumable complex attributes (see <code>consumable</code> parameter above) and must be specified as 0 otherwise. xxQS_NAMExx assumes the resource amount denoted in the <code>default</code> parameter implicitly to be consumed by jobs being dispatched to a host or queue managing the consumable attribute. Jobs explicitly requesting the attribute via the <code>-l</code> option to override this default value.</p>
<h3><code>urgency</code></h3>
<p>The urgency value allows influencing job priorities on a per-resource base. The urgency value effects the addend for each resource when determining the resource request-related urgency contribution. For numeric type resource requests the addend is the product of the urgency value, the job&#8217;s assumed slot allocation, and the per-slot request as specified via the <code>-l</code> option to For string type requests the resource&#8217;s urgency value is directly used as addend. Urgency values are of type real. See under for an overview of job priorities.</p>
<h2>See Also</h2>
<h2>Copyright</h2>
<p>See for a full statement of rights and permissions.</p>
