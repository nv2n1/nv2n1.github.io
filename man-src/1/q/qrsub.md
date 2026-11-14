---
title: "qrsub(1)"
name: "qrsub"
section: "1"
letter: "q"
url: "/docs/linux/man/1-qrsub/"
description: "qrsub – Submit an Advance Reservation (AR) to xxQS_NAMExx."
---

<h2 class="name">NAME</h2>
<p> qrsub &#8211; Submit an Advance Reservation (AR) to xxQS_NAMExx. </p>
<h2>SYNTAX</h2>
<p> <code>qrsub</code> [<code>-a</code> <i>date_time</i>] [<code>-A</code> <i>account_string</i>] [<code>-ckpt</code> <i>ckpt_name</i>] [<code>-d</code> <i>time</i>] [<code>-e</code> <i>date_time</i>] [<code>-he</code> <i>yes</i>|<i>no</i>] [<code>-help</code>] [<code>-l</code> <i>resource_list</i>] [<code>-now</code>] [<code>-M</code> <i>user</i>[@<i>host</i>],&#8230;] [<code>-N</code> <i>ar_name</i>] [<code>-w</code> <i>e|v</i>] [<code>-pe</code> <i>pe_name slot_range</i>] [<code>-q</code> <i>wc_queue_list</i>] [<code>-u</code> <i>wc_user_list</i>]</p>
<h2>DESCRIPTION</h2>
<p> <i>Qrsub</i> provides a means for operators, managers or users referenced in the ACL (see &quot;<code>arusers</code>&quot; to create an Advance Reservation (AR) in the xxQS_NAMExx queuing system. ARs allow reserving particular consumable resources for future use. These reserved resources are only available for jobs requesting the AR, and the scheduler ensures the availability of the resources when the start time is reached. Jobs requesting the AR can only use the reserved consumable resources. </p>
<p> During AR submit time the xxQS_NAMExx queuing system selects the best suited queues for the AR request and then reserves the desired amount of resources. For a reservation, all queues that are not in orphaned state are considered as suited. Only if the AR request can be fulfilled will the AR be granted. </p>
<p> ARs will be deleted either automatically when the end time is reached, or manually using In both cases, first all jobs requesting the AR will be removed and then the AR itself. Already granted ARs can be shown with </p>
<p> Note: To make AR behavior predictable, it is necessary to have reserved resources available at the time of AR start. This is done by keeping jobs with a unlimited runtime limit separated from ARs, and not considering resources used by such jobs for reservation. </p>
<p> Note: Resource Quotas are not considered for AR queue selection, nor for jobs requesting an AR. </p>
<p> When an AR was successfully added to the xxQS_NAMExx queuing system <i>qrsub</i> returns a unique integer ID referring to the the newly created AR. The highest AR ID is 9999999. If the highest ID is reached, a wraparound happens and the next unused ID, starting with 1, will be used. </p>
<p> For <i>qrsub</i>, the administrator and the user may define default request files (analogous to xxQS_NAMExx_request for qsub), which can contain any of the possible command line options.<br />
 A cluster wide default request file is optional. If such a default request file is used, it must be placed under<br />
 $xxQS_NAME_Sxx_ROOT/$xxQS_NAME_Sxx_CELL/common/sge_ar_request (global defaults file).<br />
 A user private default request file is optional. If it is used, it must be placed under<br />
 $HOME/.sge_ar_request (user private defaults file).</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-a</code> <i>date_time</i></p>
<dd> Defines the activation (start) date and time of an AR. The option is not mandatory. If omitted, the current date_time is assumed. Either a duration or end <i>date_time</i> must also be specified. For details of the <i>date_time</i> definition please see</p>
<dt><code>-A</code> <i>account_string</i></p>
<dd> Identifies the account to which the resource reservation of the AR should be charged. For &quot;<i>account_string</i>&quot; value details please see the &quot;<code>name</code>&quot; definition in In the absence of this parameter xxQS_NAMExx will place the default account string &quot;xxqs_name_sxx&quot; in the accounting record of the AR.</p>
<dt><code>-ckpt</code> <i>ckpt_name</i></p>
<dd> Selects the checkpointing environment (see the AR jobs may request. Using this option guarantees that only queues providing this checkpoint environment will be reserved.</p>
<dt><code>-d</code> <i>date_time</i></p>
<dd> Defines the duration of the AR. The use of &quot;<code>-d</code>&quot; is optional if &quot;<code>-e</code> <i>date_time</i>&quot; is requested. For details of the &quot;<i>date_time</i>&quot; definition please see</p>
<dt><code>-e</code> <i>date_time</i></p>
<dd> Defines the end date and time of an AR. The use of &quot;<code>-e date_time</code>&quot; is optional if &quot;<code>-d time</code>&quot; is requested. For details about &quot;<code>date_time</code>&quot; definition please see</p>
<dt><code>-he y</code>[<code>es</code>]|<code>n</code>[<code>o</code>]</p>
<dd> Specifies the behavior when the AR goes into an error state. The AR goes into error state when a reserved host goes into unknown state, a queue error happens, or when a queue is disabled or suspended. </p>
<p> A hard error, &quot;<code>-he yes</code>&quot;, means as long as the AR is in error state no jobs using the AR will be scheduled. If soft error, &quot;<code>-he no</code>&quot;, is specified the AR stays usable with the remaining resources.<br />
 By default soft error handling is used. </p>
<dt><code>-help</code></p>
<dd> Prints a list of all options.</p>
<dt><code>-l</code> <i>resource</i><code>=</code><i>value</i><code>,</code>&#8230;</p>
<dd> Creates an AR in a xxQS_NAMExx queue, providing the given resource request list. describes how a list of available resources and their associated valid value specifiers can be obtained.<br />
 There may be multiple <code>-l</code> switches in a single command.</p>
<dt><code>-m b</code>|<code>e</code>|<code>a</code>|<code>n</code></p>
<dd> Defines or redefines under which circumstances mail is to be sent to the AR owner or to the users defined with the <code>-M</code> option described below. The option arguments have the following meaning: </p>
<pre>
<code>b</code>     Mail is sent at the beginning of the AR
<code>e</code>     Mail is sent at the end of the AR
<code>a</code>     Mail is sent when the AR goes into error state
<code>n</code>     No mail is sent, default for <i>qrsub</i>
</pre>
<dt><code>-M</code> <i>user</i>[<code>@</code><i>host</i>]<code>,</code>&#8230;</p>
<dd> Defines or redefines the list of users to which the qmaster sends mail.</p>
<dt><code>-masterq</code> <i>wc_queue_list</i></p>
<dd> Only meaningful for a parallel AR request together with the -pe option. </p>
<p> This option is used to reserve the proper queues to match this request if it would be requested by a qsub. A more detailed description of <i>wc_queue_list</i> can be found in</p>
<dt><code>-now y</code>[<code>es</code>]|<code>n</code>[<code>o</code>]</p>
<dd> This option affects the queue selection for reservation.<br />
 With the &quot;<code>-now y</code>&quot; option, only queues with the qtype &quot;INTERACTIVE&quot; assigned will be considered for reservation. &quot;<code>-now n</code>&quot; is the default for <i>qrsub</i>.</p>
<dt><code>-N</code> <i>name</i></p>
<dd> The name of the AR. The name, if requested, must conform to &quot;<i>name</i>&quot; as defined in Invalid names will be denied at submit time.</p>
<dt><code>-w e</code>|<code>v</code></p>
<dd> Specifies the validation level applied to the AR request. </p>
<p> The specifiers e and v define the following validation modes: </p>
<pre>
<code>v</code>    verify - does not submit the AR but prints
     an extensive validation report
<code>e</code>    error - rejects request if requirements cannot
     be fulfilled, default for <i>qrsub</i>
</pre>
<dt><code>-pe</code> <i>parallel_env n</i>[<code>&#8211;</code>[<i>m</i>]]|[<code>&#8211;</code>]<i>m</i>,&#8230;</p>
<dd> Parallel programming environment (PE) to select for the AR queue reservation. Please see the details of a PE in</p>
<dt><code>-q</code> <i>wc_queue_list</i></p>
<dd> Defines or redefines a list of cluster queues, queue domains or queue instances that may be reserved by the AR. Please find a description of <i>wc_queue_list</i> in This parameter has all the properties of a resource request and will be merged with requirements derived from the <code>-l</code> option described above.</p>
<dt><code>-u</code> [<i>username</i>|<code>@</code><i>access_list</i>],&#8230;</p>
<dd> Defines the users allowed to submit jobs requesting the AR. The access is specified by a comma-separated list containing UNIX users or ACLs (see An ACL is differentiated from a UNIX user name by prefixing the ACL name with an &#8216;@&#8217; sign.<br />
 By default only the AR owner is allowed to submit jobs requesting the AR. </p>
<p> Note: Only queues where all users specified in the list have access are considered for reservation (see</dl>
<h2>ENVIRONMENT VARIABLES</h2>
<dl>
<dt><code>xxQS_NAME_Sxx_ROOT</code></p>
<dd> Specifies the location of the xxQS_NAMExx standard configuration files.</p>
<dt><code>xxQS_NAME_Sxx_CELL</code></p>
<dd> If set, specifies the default xxQS_NAMExx cell. To address a xxQS_NAMExx cell, <i>qsub</i>, <i>qsh</i>, <i>qlogin</i> or <i>qalter</i> use (in the order of precedence): </p>
<dl>
<dt>
<dd>
<dl>
<dt>
<dd> The name of the cell specified in the environment variable xxQS_NAME_Sxx_CELL, if it is set. </p>
<p> The name of the default cell, i.e. <code>default</code>.</dl>
</dl>
<dt><code>xxQS_NAME_Sxx_DEBUG_LEVEL</code></p>
<dd> If set, specifies that debug information should be written to stderr. In addition the level of detail in which debug information is generated is defined.</p>
<dt><code>xxQS_NAME_Sxx_QMASTER_PORT</code></p>
<dd> If set, specifies the TCP port on which is expected to listen for communication requests. Most installations will use a services map entry for the service &quot;sge_qmaster&quot; instead of defining the port.</dl>
<h2>FILES</h2>
<pre>
<i>$xxQS_NAME_Sxx_ROOT/$xxQS_NAME_Sxx_CELL/common/sge_ar_request</i>
                         global defaults file
<i>$HOME/.sge_ar_request</i>
                         user private defaults file
</pre>
<h2>SEE ALSO</h2>
<h2>COPYRIGHT</h2>
<p> See for a full statement of rights and permissions. </p>
<h2>Index</h2>
