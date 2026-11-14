---
title: "sge_types(1)"
name: "sge_types"
section: "1"
letter: "s"
url: "/docs/linux/man/1-sge_types/"
description: "sge_types – Grid Engine type descriptions"
---

<h2 class="name">NAME</h2>
<p> sge_types &#8211; Grid Engine type descriptions </p>
<h2>DESCRIPTION</h2>
<p> The Grid Engine user interface consists of several programs and files. Some command-line switches and several file attributes are types. The syntax for these types is explained in this page. </p>
<h2>OBJECT TYPES</h2>
<p> These types are used for defining Grid Engine configuration:</p>
<h3><code>calendar_name</code></h3>
<p> A calendar name is the name of a Grid Engine calendar described in </p>
<p> <i>calendar_name</i> := <i>object_name</i></p>
<h3><code>ckpt_name</code></h3>
<p> A &quot;ckpt_name&quot; is the name of a Grid Engine checkpointing interface described in </p>
<p> <i>ckpt_name</i> := <i>object_name</i></p>
<h3><code>complex_name</code></h3>
<p> A complex name is the name of a Grid Engine resource attribute described in </p>
<p> <i>complex_name</i> := <i>object_name</i></p>
<h3><code>host_identifier</code></h3>
<p> A host identifier can be either a host name or a host group name. </p>
<p> <i>host_identifier</i> := <i>host_name</i> | <i>hostgroup_name</i></p>
<h3><code>hostgroup_name</code></h3>
<p> A host group name is the name of a Grid Engine host group described in Note, to allow host group names easily be differed from host names a &quot;@&quot; prefix is used. </p>
<p> <i>hostgroup_name</i> := @<i>object_name</i> </p>
<h3><code>host_name</code></h3>
<p> A host name is the official name of a host node. Host names with a domain specification such as &quot;gridmaster.sun.com&quot; are called fully-qualified host names, whereas host names like &quot;gridmaster&quot; are called short host names. Note, there are the install time parameters default_domain and ignore_fqdn (see which affect how Grid Engine deals with host names in general.</p>
<h3><code>jsv_url</code></h3>
<p> The <code>jsv_url</code> has following format: </p>
<p> <i>jsv_url</i> := <i>jsv_client_url</i> | <i>jsv_server_url</i> </p>
<p> <i>jsv_server_url</i> := [ <i>type</i> &#8216;<code>:</code>&#8216; ] [ <i>user</i> &#8216;<code>@</code>&#8216; ] <i>path</i> </p>
<p> <i>jsv_client_url</i> := [ <i>type</i> &#8216;<code>:</code>&#8216; ] <i>path</i> </p>
<p> <i>type</i> := &#8216;<code>script</code>&#8216; </p>
<p> In the moment only the <i>type</i> <code>script</code> is allowed. This means that <i>path</i> is either the path to a script or to a binary application which will be used to instantiate a JSV process. The <i>type</i> is optional till other <i>types</i> are supported by Grid Engine. </p>
<p> Specifying a <i>user</i> is only allowed for server JSV&#8217;s. Client JSV&#8217;s will automatically be started as submit user and server JSV&#8217;s as admin user if not other specified. </p>
<p> The <i>path</i> has always to be the absolute path to a binary or application. </p>
<h3><code>memory_specifier</code></h3>
<p> Memory specifiers are positive decimal, hexadecimal or octal integer constants which may be followed by a multiplier letter. Valid multiplier letters are k, K, m, M, g and G, where k means multiply the value by 1000, K multiply by 1024, m multiply by 1000*1000, M multiply by 1024*1024, g multiply by 1000*1000*1000 and G multiply by 1024*1024*1024. If no multiplier is present, the value is just counted in bytes.</p>
<h3><code>pe_name</code></h3>
<p> A &quot;pe_name&quot; is the name of a Grid Engine parallel environment described in </p>
<p> <i>pe_name</i> := <i>object_name</i></p>
<h3><code>project_name</code></h3>
<p> A project name is the name of a Grid Engine project described in </p>
<p> <i>project_name</i> := <i>object_name</i></p>
<h3><code>queue_name</code></h3>
<p> A queue name is the name of a Grid Engine queue described in </p>
<p> <i>queue_name </i> := <i>object_name</i></p>
<h3><code>time_specifier</code></h3>
<p> A time specifier either consists of a positive decimal, hexadecimal or octal integer constant, in which case the value is interpreted to be in seconds, or is built by 3 decimal integer numbers separated by colon signs where the first number counts the hours, the second the minutes and the third the seconds. If a number would be zero it can be left out but the separating colon must remain (e.g. 1:0:1 = 1::1 means 1 hours and 1 second).</p>
<h3><code>user_name</code></h3>
<p> A user name can be the name of a user or of the Grid Engine user object described in </p>
<p> <i>user_name</i> := <i>object_name</i></p>
<h3><code>userset_name</code></h3>
<p> A user set name is the name of an Grid Engine access list or department described in </p>
<p> <i>userset_name</i> := <i>object_name</i></p>
<h3><code>object_name</code></h3>
<p> An object name is a sequence of up to 512 ASCII string characters except &quot;
&quot;, &quot;	&quot;, &quot;&quot;, &quot; &quot;, &quot;/&quot;, &quot;:&quot;, &quot;&#8217;&quot;, &quot;\&quot;, &quot;[&quot;, &quot;]&quot;, &quot;{&quot;, &quot;}&quot;, &quot;|&quot;, &quot;(&quot;, &quot;)&quot;, &quot;@&quot;, &quot;%&quot;, &quot;,&quot; or the &quot; character itself.</p>
<h2>MATCHING TYPES</h2>
<p> These types are used for matching Grid Engine configuration:</p>
<h3><code>expression</code></h3>
<p> A wildcard expression is a regular boolean expression that consists of one or more <i>pattern</i>s joined by boolean operators. When a wildcard expression is used, the following definition applies: </p>
<pre><code>
expression = ["!"]["("] valExp[")"][AND_OR expression] *valExp = pattern | expression
                                                                               AND_OR = "&amp;" | "|"
</code></pre>
<p> where: </p>
<p>&#8220;!&#8221; not operator&#8211; negate the following pattern or expression<br />
    &#8220;&amp;&#8221; and<br />
    operator&#8211; logically and with the following expression<br />
    &#8220;|&#8221; or<br />
    operator&#8211; logically or with the following expression<br />
    &#8220;(&#8221; open bracket&#8211; begin an inner expression.&#8221;)&#8221; close bracket&#8211; end an inner expression.&#8221;pattern&#8221; see the pattern definition that&#8217;s follow</p>
<p> The expression itself should be put inside quotes (&#8216;&quot;&#8217;) to ensure that clients receive the complete expression. </p>
<p> e.g.</p>
<dl>
<dt>
<dd>
<pre>
&quot;(lx*|sol*)&amp;*64*&quot; any string beginning with either &quot;lx&quot; or
                  &quot;sol&quot; and containing &quot;64&quot;
&quot;rh_3*&amp;!rh_3.1&quot;   any string beginning with &quot;rh_3&quot;, except
                  &quot;rh_3.1&quot;
</pre>
</dl>
<h3><code>pattern</code></h3>
<p> When patterns are used the following definitions apply: </p>
<pre><code>
"*" matches any character and any number of characters(between 0 and inv)."?" matches any character.It cannot be no character "." is the character ".".It has no other meaning "\"     escape character. "\" = "\", "\* " = " * ", "\? " = " ? "
                                                                                                                                                                                                                                                "[...]" specifies an array
                                                                                                                                                                                                                                                    or a range of allowed
                                                                                                                                                                                                                                                           characters for one character at a specific position.Character ranges may be specified using the a -
                                                                                                                                                                                                                                                           z notation.The caret symbol(^) is not interpreted as a logical not ;
it is interpreted literally.For more details please see
</code></pre>
<p> The pattern itself should be put inside quotes (&#8216;&quot;&#8217;) to ensure that clients receive the complete pattern. </p>
<h3><code>range</code></h3>
<p> The task range specifier has the form </p>
<p> n[-m[:s]][,n[-m[:s]], &#8230;] or n[-m[:s]][ n[-m[:s]] &#8230;] </p>
<p> and thus consists of a comma or blank separated list of range specifiers n[-m[:s]]. The ranges are concatenated to the complete task id range. Each range may be a single number, a simple range of the form n-m or a range with a step size. </p>
<h3><code>wc_ar</code></h3>
<p> The wildcard advance reservation (AR) specification is a placeholder for AR ids, AR names including AR name patterns. An AR id always references one AR, while the name and pattern might reference multiple ARs. </p>
<p> wc_ar := ar_id | ar_name | pattern </p>
<h3><code>wc_ar_list</code></h3>
<p> The wildcard advance reservation (AR) list specification allows to reference multiple ARs with one command. </p>
<p> wc_ar_list := wc_ar [ , wc_ar , &#8230;] </p>
<h3><code>wc_host</code></h3>
<p> A wildcard host specification (<i>wc_host</i>) is a wildcard expression which might match one or more hosts used in the cluster. The first character of that string never begins with an at-character (&#8216;@&#8217;), even if the expression begins with a wildcard character. </p>
<pre>
e.g.
<dl><dt><dd>
*            all hosts
a*           all host beginning with an 'a'
</pre>
</dl>
<h3><code>wc_hostgroup</code></h3>
<p> A wildcard hostgroup specification (<i>wc_hostgroup</i>) is a wildcard expression which might match one or more hostgroups. The first character of that string is always an at-character (&#8216;@&#8217;). </p>
<p> More information concerning hostgroups can be found in </p>
<pre>
e.g.
<dl><dt><dd>
@*           all hostgroups in the cluster
@solaris     the @solaris hostgroup
</pre>
</dl>
<h3><code>wc_job</code></h3>
<p> The wildcard job specification is a placeholder for job ids, job names including job name patterns. A job id always references one job, while the name and pattern might reference multiple jobs. </p>
<p> wc_job := job-id | job-name | pattern </p>
<h3><code>wc_job_range</code></h3>
<p> The wildcard job range specification allows to reference specific array tasks for one or multiple jobs. The job is referenced via wc_job and in addition gets a range specifier for the array tasks. </p>
<p> wc_job_range := wc_job [ -t range] </p>
<h3><code>wc_job_list</code></h3>
<p> The wildcard job list specification allows to reference multiple jobs with one command. </p>
<p> wc_job_list := wc_job [ , wc_job , &#8230;] </p>
<h3><code>wc_job_range_list</code></h3>
<p> The wildcard job range list (<i>wc_job_range_list</i>) is specified by one of the following forms: </p>
<p>&nbsp;<wbr><i>wc_job[&nbsp;<wbr>-t range][{,&nbsp;<wbr>}wc_job[&nbsp;<wbr>-t range]{,&nbsp;<wbr>}&#8230;]</i> </p>
<p> If present, the <i>task_range</i> restricts the effect of the <i>qmod</i> operation to the array job task range specified as suffix to the job id (see the <code>-t</code> option to for further details on array jobs). </p>
<h3><code>wc_qdomain</code></h3>
<p> <i>wc_qdomain</i> := <i>wc_cqueue</i> &quot;@&quot; <i>wc_hostgroup</i> </p>
<p> A wildcard expression queue domain specification (<i>wc_qdomain</i>) starts with a wildcard expression cluster queue name (<i>wc_cqueue</i>) followed by an at-character &#8216;@&#8217; and a wildcard expression hostgroup specification (<i>wc_hostgroup</i>). </p>
<p> <i>wc_qdomain</i> are used to address a group of queue instances. All queue instances residing on a hosts which is part of matching hostgroups will be addressed. Please note, that <i>wc_hostgroup</i> always begins with an at-character. </p>
<pre>
e.g.
<dl><dt><dd>
*@@*         all queue instances whose underlying
             host is part of at least one hostgroup
a*@@e*       all queue instances begins with a whose underlying
             host is part of at least one hostgroup begin with e
*@@solaris   all queue instances on hosts part of
             the @solaris hostgroup
</pre>
</dl>
<h3><code>wc_cqueue</code></h3>
<p> A wildcard expression cluster queue specification (<i>wc_cqueue</i>) is a wildcard expression which might match one or more cluster queues used in the cluster. That string never contains an at-character (&#8216;@&#8217;), even if the expression begins with a wildcard character. </p>
<pre>
e.g.
<dl><dt><dd>
*            all cluster queues
a*           all cluster queues beginning with an 'a'
a*&amp;!adam     all cluster queues beginning with an 'a',but not adam
</pre>
</dl>
<h3><code>wc_qinstance</code></h3>
<p> <i>wc_qinstance</i> := <i>wc_cqueue</i> &quot;@&quot; <i>wc_host</i> </p>
<p> A wildcard expression queue instance specification (<i>wc_qinstance</i>) starts with a wildcard expression cluster queue name (<i>wc_cqueue</i>) followed by an at-character &#8216;@&#8217; and a wildcard expression hostname (<i>wc_host</i>). </p>
<p> <i>wc_qinstance</i> expressions are used to address a group of queue instances whose underlying hostname matches the given expression. Please note that the first character of <i>wc_host</i> does never match the at-character &#8216;@&#8217;. </p>
<pre>
e.g.
<dl><dt><dd>
*@*          all queue instances in the cluster
*@b*         all queue instances whose 
             hostname begins with a 'b'
*@b*|c*      all queue instances whose 
             hostname begins with a 'b' or 'c'
</pre>
</dl>
<h3><code>wc_queue</code></h3>
<p> <i>wc_queue</i> := <i>wc_cqueue</i> | <i>wc_qdomain</i> | <i>wc_qinstance</i> </p>
<p> A wildcard queue expression (<i>wc_queue</i>) might either be a wildcard expression cluster queue specification (<i>wc_cqueue</i>) or a wildcard expression queue domain specification (<i>wc_qdomain</i>) or a wildcard expression queue instance specification (<i>wc_qinstance</i>). </p>
<pre>
e.g.
<dl><dt><dd>
big_*1           cluster queues which begin with 
                 &quot;big_&quot; and end with &quot;1&quot; 
big_*&amp;!*1        cluster queues which begin with 
                 &quot;big_&quot; ,but does not end with &quot;1&quot; 
*@fangorn        all qinstances residing on host 
                 fangorn
</pre>
</dl>
<h3><code>wc_queue_list</code></h3>
<p> <i>wc_queue_list</i> := <i>wc_queue</i> [&quot;,&quot; <i>wc_queue</i> &quot;,&quot; &#8230;] </p>
<p> Comma separated list of wc_queue elements. </p>
<p> e.g.</p>
<dl>
<dt>
<dd> big, medium_*@@sol*, *@fangorn.sun.com </p>
</dl>
<h3><code>wc_user</code></h3>
<p> A wildcard user name pattern is either a wildcard user name specification or a full user name. </p>
<p> wc_user := user_name | pattern </p>
<h3>wc_user_list</h3>
<p> A list of user names. </p>
<p> wc_user_list := wc_user [ , wc_user , &#8230;] </p>
<h3><code>wc_project</code></h3>
<p> A wildcard project name pattern is either a wildcard project name specification or a full project name. </p>
<p> wc_project := project | pattern </p>
<h3><code>wc_pe_name</code></h3>
<p> A wildcard parallel environment name pattern is either a wildcard pe name specification or a full pe name. </p>
<p> wc_pe_name := pe_name | pattern </p>
<h3><code>parallel_env</code> <code>n</code>[<code>&#8211;</code>[<code>m</code>]]|[<code>&#8211;</code>]<code>m</code>,&#8230;</h3>
<p> Parallel programming environment (PE) to select for an AR. The range descriptor behind the PE name specifies the number of parallel processes to be run. Grid Engine will allocate the appropriate resources as available. The manual page contains information about the definition of PEs and about how to obtain a list of currently valid PEs. </p>
<p> You can specify a PE name which uses the wildcard character, &quot;*&quot;. Thus the request &quot;pvm*&quot; will match any parallel environment with a name starting with the string &quot;pvm&quot;. In the case of multiple parallel environments whose names match the name string, the parallel environment with the most available slots is chosen. </p>
<p> The range specification is a list of range expressions of the form &quot;n-m&quot;, where n and m are positive, non-zero integers. The form &quot;n&quot; is equivalent to &quot;n-n&quot;. The form &quot;-m&quot; is equivalent to &quot;1-m&quot;. The form &quot;n-&quot; is equivalent to &quot;n-infinity&quot;. The range specification is processed as follows: The largest number of queues requested is checked first. If enough queues meeting the specified attribute list are available, all are reserved. If not, the next smaller number of queues is checked, and so forth. </p>
<h3><code>date_time</code></h3>
<p> The <code>date_time</code> value must conform to [[CC]]YY]MMDDhhmm[.SS], where: </p>
<pre>
e.g.
<dl><dt><dd>
CC           denotes the century in 2 digits.
YY           denotes the year in 2 digits.
MM           denotes the month in 2 digits.
DD           denotes the day in 2 digits.
hh           denotes the hour in 2 digits.
mm           denotes the minute in 2 digits.
ss           denotes the seconds in 2 digits (default 00).
</pre>
</dl>
<h3><code>time</code></h3>
<p> The <code>time</code> value must conform to hh:mm:ss, or seconds where: </p>
<pre>
e.g.
<dl><dt><dd>
hh denotes the hour in 2 digits.
mm denotes the minute in 2 digits.
ss denotes the seconds in 2 digits (default 00).
seconds  is a number of seconds (is used for duration values)
</pre>
<p> If any of the optional date fields are omitted, the corresponding value of the current date is assumed. If CC is not specified, a YY of &lt; 70 means 20YY.<br />
 Use of this option may cause unexpected results if the clocks of the hosts in the Grid Engine pool are out of sync. Also, the proper behavior of this option very much depends on the correct setting of the appropriate timezone, e.g. in the TZ environment variable (see for details), when the Grid Engine daemons and are invoked.</dl>
<h3><code>name</code></h3>
<p> The <code>name</code> may be any arbitrary alphanumeric ASCII string, but may not contain &quot;
&quot;, &quot;	&quot;, &quot;&quot;, &quot;/&quot;, &quot;:&quot;, &quot;@&quot;, &quot;\&quot;, &quot;*&quot;, or &quot;?&quot;. </p>
<h2>SEE ALSO</h2>
<h2>COPYRIGHT</h2>
<p> Copyright: 2004-2007 by Sun Microsystems, Inc. </p>
<h2>Index</h2>
<dt><a href="#lbAT">MATCHING TYPES</a></p>
<dd>
<dt><a href="#lbBS">SEE ALSO</a></p>
<dd>
<dt><a href="#lbBT">COPYRIGHT</a></p>
<dd></dl>
