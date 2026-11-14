---
title: "qrdel(1)"
name: "qrdel"
section: "1"
letter: "q"
url: "/docs/linux/man/1-qrdel/"
description: "qrdel – delete xxQS_NAMExx Advance Reservations (AR)"
---

<h2 class="name">NAME</h2>
<p> qrdel &#8211; delete xxQS_NAMExx Advance Reservations (AR) </p>
<h2>SYNTAX</h2>
<p> <code>qrdel</code> [<code>-f</code>] [<code>-help</code>] [<code>-u</code> <i>wc_user_list</i>] <i>wc_ar_list</i></p>
<h2>DESCRIPTION</h2>
<p> <i>Qrdel</i> provides a means for a user/operator/manager to delete one or more Advance Reservations (AR) referenced by numeric id or name. A manager/operator can delete ARs belonging to any user, while regular users can only delete their own ARs. If a manager wants to delete another user&#8217;s AR, the manager can specify the AR id. By default, &quot;qrdel wc_ar_name&quot; will delete only the ARs belonging to that user. A manager is able to delete another user&#8217;s AR via &quot;-u wc_user_list&quot;. Jobs referring to an AR tagged for deletion will also be removed. Only if all jobs referring to an AR are removed from the xxQS_NAMExx database will the AR also be removed. <i>Qrdel</i> deletes ARs in the order in which the AR identifiers are presented. Find additional information concerning <i>wc_user_list</i> and <i>wc_ar_list</i> in</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-f</code></p>
<dd> Force action. The AR and the jobs using the AR are deleted from the xxQS_NAMExx queuing system even if the controlling the AR jobs does not respond to the delete request sent by the<br />
 Users who have with neither xxQS_NAMExx manager nor operator status can only use the <code>-f</code> option for their own ARs.</p>
<dt><code>-help</code></p>
<dd> Prints a list of all options.</p>
<dt><code>-u wc_user_list</code></p>
<dd> Deletes only those ARs which were submitted by users specified in the list of usernames. For managers, it is possible to use <code>qrdel -u &quot;*&quot;</code> to delete all ARs for all users. To delete a specific AR for a user, a manager has to specify the user and the AR id. If no AR is specified, all ARs belonging to that user are deleted.</p>
<dt><code>wc_ar_list</code></p>
<dd> A list of ARs that should be deleted (either numeric or names assigned with <code>qrsub -N</code>).</dl>
<h2>ENVIRONMENT VARIABLES</h2>
<dl>
<dt><code>xxQS_NAME_Sxx_ROOT</code></p>
<dd> Specifies the location of the xxQS_NAMExx standard configuration files.</p>
<dt><code>xxQS_NAME_Sxx_CELL</code></p>
<dd> If set, specifies the default xxQS_NAMExx cell. To address a xxQS_NAMExx cell <i>qrdel</i> uses (in the order of precedence): </p>
<dl>
<dt>
<dd>
<dl>
<dt>
<dd> The name of the cell specified in the environment variable xxQS_NAME_Sxx_CELL, if it is set. </p>
<p> The name of the default cell, i.e. <code>default</code>. </p>
</dl>
</dl>
<dt><code>xxQS_NAME_Sxx_DEBUG_LEVEL</code></p>
<dd> If set, specifies that debug information should be written to stderr. In addition the level of detail in which debug information is generated is defined.</p>
<dt><code>xxQS_NAME_Sxx_QMASTER_PORT</code></p>
<dd> If set, specifies the tcp port on which the is expected to listen for communication requests. Most installations will use a service map entry for the service &quot;sge_qmaster&quot; instead of defining the port.</dl>
<h2>FILES</h2>
<pre>
<i>&lt;xxqs_name_sxx_root&gt;/&lt;cell&gt;/common/act_qmaster</i>
                          xxQS_NAMExx master host file
</pre>
<h2>SEE ALSO</h2>
<h2>COPYRIGHT</h2>
<p> See for a full statement of rights and permissions. </p>
<h2>Index</h2>
