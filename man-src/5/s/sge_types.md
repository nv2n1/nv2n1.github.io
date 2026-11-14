---
title: "sge_types(5)"
name: "sge_types"
section: "5"
letter: "s"
url: "/docs/linux/man/5-sge_types/"
description: "sge_types – xxQS_NAMExx type descriptions"
---

<p>sge_types &#8211; xxQS_NAMExx type descriptions</p>
<h2>Description</h2>
<p>The xxQS_NAMExx user interface consists of several programs and files. Some command-line switches and several file attributes are types. The syntax for these types is explained in this page. </p>
<h2>Object Types</h2>
<p>These types are used for defining xxQS_NAMExx configuration:</p>
<h3><code>object_name</code></h3>
<p>An object name is a sequence of up to 512 ASCII printing characters except SPACE, &quot;/&quot;, &quot;:&quot;, &quot;&#8217;&quot;, &quot;\&quot;, &quot;[&quot;, &quot;]&quot;, &quot;{&quot;, &quot;}&quot;, &quot;|&quot;, &quot;(&quot;, &quot;)&quot;, &quot;@&quot;, &quot;%&quot;, &quot;,&quot; or the &#8216;&quot;&#8217; character itself.</p>
<h3><code>calendar_name</code></h3>
<p>A calendar name is the name of a xxQS_NAMExx calendar described in </p>
<pre><i>calendar_name</i> := <i>object_name</i></pre>
<h3><code>ckpt_name</code></h3>
<p>A &quot;ckpt_name&quot; is the name of a xxQS_NAMExx checkpointing interface described in </p>
<pre><i>ckpt_name</i> := <i>object_name</i></pre>
<h3><code>complex_name</code></h3>
<p>A complex name is the name of a xxQS_NAMExx resource attribute described in </p>
<pre><i>complex_name</i> := <i>object_name</i></pre>
<h3><code>host_identifier</code></h3>
<p>A host identifier can be either a host name or a host group name. </p>
<pre><i>host_identifier</i> := <i>host_name</i> | <i>hostgroup_name</i></pre>
<h3><code>hostgroup_name</code></h3>
<p>A host group name is the name of a xxQS_NAMExx host group described in Note, to allow host group names to be distinguished easily from host names, a &quot;@&quot; prefix is used. </p>
<pre><i>hostgroup_name</i> := @<i>object_name</i></pre>
<h3><code>host_name</code></h3>
<p>A host name is the official name of a host node. Host names with a domain specification such as &quot;gridmaster.sun.com&quot; are called fully-qualified host names, whereas host names like &quot;gridmaster&quot; are called short host names. Note that the install time parameters <code>default_domain</code> and <code>ignore_fqdn</code> (see affect how xxQS_NAMExx deals with host names in general. </p>
<p> The following host names are generally invalid or reserved: <code>global</code>,&nbsp;<code>template</code>,&nbsp;<code>all</code>,&nbsp;<code>default</code>,&nbsp;<code>unknown</code>,&nbsp;<code>none</code>. However, it may sometimes be useful to define a dummy host name of <code>global</code> for convenient use of</p>
<h3><code>jsv_url</code></h3>
<p>The <code>jsv_url</code> has following format: </p>
<p> <i>jsv_url</i> := <i>jsv_client_url</i> | <i>jsv_server_url</i> </p>
<p> <i>jsv_server_url</i> := [ <i>type</i> &#8216;<code>:</code>&#8216; ] [ <i>user</i> &#8216;<code>@</code>&#8216; ] <i>path</i> </p>
<p> <i>jsv_client_url</i> := [ <i>type</i> &#8216;<code>:</code>&#8216; ] <i>path</i> </p>
<p> <i>type</i> := &#8216;<code>script</code>&#8216; </p>
<p> At the moment only the <i>type</i> <code>script</code> is allowed. This means that <i>path</i> is either the path to a script or to a binary application which will be used to instantiate a JSV process. The <i>type</i> is optional until other <i>types</i> are supported by xxQS_NAMExx. </p>
<p> Specifying a <i>user</i> is only allowed for server JSVs. Client JSVs will automatically be started as the submit user, and server JSVs as the admin user if not otherwise specified. </p>
<p> The <i>path</i> has always to be the absolute path to a binary or application.</p>
<h3><code>memory_specifier</code></h3>
<p>Memory specifiers are positive decimal, hexadecimal or octal integer constants which may be followed by a multiplier letter. Valid multiplier letters are <code>k</code>,&nbsp;<code>K</code>,&nbsp;<code>m</code>,&nbsp;<code>M</code>,&nbsp;<code>g</code>,&nbsp;<code>G</code>,&nbsp;<code>t</code>, and <code>T</code>, where <code>k</code> means multiply the value by 1000, <code>K</code> multiply by 1024, <code>m</code> multiply by 1000&#215;1000, <code>M</code> multiply by 1024&#215;1024, <code>g</code> multiply by 1000&#215;1000&#215;1000, <code>G</code> multiply by 1024&#215;1024&#215;1024, <code>t</code> multiply by 1000&#215;1000&#215;1000&#215;1000, and <code>T</code> multiply by 1024&#215;1024&#215;1024&#215;1024. If no multiplier is present, the value is just counted in bytes. Whether memory values above the 32-bit limit are representable on 32-bit systems, even for disk space, is system-dependent.</p>
<h3><code>pe_name</code></h3>
<p>A PE name is the name of a xxQS_NAMExx parallel environment described in </p>
<pre><i>pe_name</i> := <i>object_name</i></pre>
<h3><code>project_name</code></h3>
<p>A project name is the name of a xxQS_NAMExx project described in </p>
<pre><i>project_name</i> := <i>object_name</i></pre>
<h3><code>queue_name</code></h3>
<p>A queue name is the name of a xxQS_NAMExx queue described in </p>
<pre><i>queue_name </i> := <i>object_name</i></pre>
<h3><code>time_specifier</code></h3>
<p>A time specifier either consists of a positive decimal, hexadecimal or octal integer constant, in which case the value is interpreted to be in seconds, or is built from 3 decimal integer numbers separated by colon signs, where the first number counts the hours, the second the minutes and the third the seconds. If a number would be zero it can be left out but the separating colon must remain (e.g. <code>1:0:1</code> = 1::1 means 1 hour and 1 second).</p>
<h3><code>user_name</code></h3>
<p>A user name can be the name of a user or of the xxQS_NAMExx user object described in </p>
<pre><i>user_name</i> := <i>object_name</i></pre>
<h3><code>userset_name</code></h3>
<p>A user set name is the name of a xxQS_NAMExx access list or department described in </p>
<pre><i>userset_name</i> := <i>object_name</i></pre>
<h3><code>date_time</code></h3>
<p>A <i>date_time</i> value must conform to [[<i>CC</i>]<i>YY</i>]<i>MMDDhhmm</i>[<code>.</code><i>SS</i>], where: </p>
<pre><dl><dt><dd><i>CC</i> denotes the century in 2 digits.
<i>YY</i> denotes the year in 2 digits.
<i>MM</i> denotes the month in 2 digits.
<i>DD</i> denotes the day in 2 digits.
<i>hh</i> denotes the hour in 2 digits.
<i>mm</i> denotes the minute in 2 digits.
<i>ss</i> denotes the seconds in 2 digits (default 00).</pre>
<p>If any of the optional date fields are omitted, the corresponding value of the current date is assumed. If <i>CC</i> is not specified, a <i>YY</i> of &lt;70 means 20<i>YY</i>.<br />
 Use of this option may cause unexpected results if the clocks of the hosts in the xxQS_NAMExx pool are out of sync. Also, the proper behavior of this option very much depends on the correct setting of the appropriate timezone, e.g. in the TZ environment variable (see <i><a href="/docs/linux/man/1-date/">date</a></i>(1) for details), when the xxQS_NAMExx daemons and are invoked.</dl>
<h3><code>time</code></h3>
<p>A <i>time</i> value must conform to <i>hh</i><code>:</code><i>mm</i><code>:</code><i>ss</i>, or <i>seconds</i> where: </p>
<pre><dl><dt><dd><i>hh</i> denotes the hour in 2 digits.
<i>mm</i> denotes the minute in 2 digits.
<i>ss</i> denotes the seconds in 2 digits (default 00).
<i>seconds</i> is a number of seconds (used for duration values)</pre>
</dl>
<h3><code>name</code></h3>
<p>A <i>name</i> is an arbitrary string of ASCII printing characters, but may not contain &quot;/&quot;, &quot;:&quot;, &quot;@&quot;, &quot;\&quot;, &quot;*&quot;, or &quot;?&quot;.</p>
<h3><code>account_name</code></h3>
<p>Identifies the account to which the resource consumption of a job should be charged. </p>
<pre><i>account_name</i> := <i>name</i></pre>
<h3><code>job_name</code></h3>
<p>A job name is a <i>name</i> as above, with the restriction that it cannot start with a digit (to avoid ambiguity with a job number in some contexts).</p>
<h3><code>ar_name</code></h3>
<p>An advance reservation name is a <i>name</i> as above, with the restriction that it cannot start with a digit (to avoid ambiguity with an AR number in some contexts).</p>
<h2>Matching Types</h2>
<p>These types are used for matching xxQS_NAMExx configuration:</p>
<h3><code>expression</code></h3>
<p>A wildcard expression is a regular boolean expression that consists of one or more <i>pattern</i>s joined by boolean operators. When a wildcard expression is used, the following definition applies: </p>
<pre>expression= [&quot;!&quot;] [&quot;(&quot;] valExp [&quot;)&quot;] [ AND_OR expression ]*
valExp = pattern | expression
AND_OR = &quot;&amp;&quot; | &quot;|&quot;</pre>
<p>where: </p>
<pre>&quot;!&quot; not operator: negate the following pattern or expression
&quot;&amp;&quot; and operator: logically and with the following expression
&quot;|&quot; or operator: logically or with the following expression
&quot;(&quot; open bracket: begin an inner expression.
&quot;)&quot; close bracket: end an inner expression.
&quot;pattern&quot; see the <code>pattern</code> definition that follows</pre>
<p>If typed at a shell, the expression itself should be quoted to ensure that it is not expanded by the shell. </p>
<p> e.g.</p>
<dl>
<dd>
<pre>&quot;(lx*|sol*)&amp;*64*&quot; any string beginning with either &quot;lx&quot; or
 &quot;sol&quot; and containing &quot;64&quot;
&quot;rh_3*&amp;!rh_3.1&quot; any string beginning with &quot;rh_3&quot;, except
 &quot;rh_3.1&quot;</pre>
</dl>
<h3><code>pattern</code></h3>
<p>When patterns are used the following definitions apply: </p>
<pre>&quot;*&quot; matches any character and any number of characters 
 (between 0 and infinity).
&quot;?&quot; matches any single character.
&quot;.&quot; is the character &quot;.&quot;. It has no other meaning.
&quot;\&quot; escape character, making the following character match literally;
 &quot;\&quot; matches &quot;\&quot;, &quot;\*&quot; matches &quot;*&quot;, &quot;\?&quot; matches &quot;?&quot;.
&quot;[...]&quot; specifies an array or a range of allowed 
 characters for one character at a specific position.
 Character ranges may be specified using the a-z notation.
 The caret symbol (<code>^</code>) is <i>not</i> interpreted as a logical
 not; it is interpreted literally.</pre>
<p>For more details please see <i><a href="/docs/linux/man/5-fnmatch/">fnmatch</a></i>(5), <i><a href="/docs/linux/man/7-glob/">glob</a></i>(7). </p>
<p> A pattern on a shell command line should normally be quoted to avoid it being interpreted by the shell as a file match.</p>
<h3><code>range</code></h3>
<p>The task range specifier has the form </p>
<p> <i>n</i>[<i></i><code>&#8211;</code>m[<i></i><code>:</code>s]][<i></i><code>,</code>n[<i></i><code>&#8211;</code>m[<i></i><code>:</code>s]]<i></i><code>,</code>&#8230;] or <i>n</i>[<i></i><code>&#8211;</code>m[<i></i><code>:</code>s]][&nbsp;<i>n</i>[<i></i><code>&#8211;</code>m[<i></i><code>:</code>s]]<i>&nbsp;</i>&#8230;] </p>
<p> and thus consists of a comma- or blank-separated list of range specifiers <i>n</i>[<i></i><code>&#8211;</code>m[<i></i><code>:</code>s]]. The ranges are concatenated to the complete task id range. Each range may be a single number, a simple range of the form <i>n</i><code>&#8211;</code><i>m</i>, or a range with a step size.</p>
<h3><code>wc_ar</code></h3>
<p>The wildcard advance reservation (AR) specification is a placeholder for AR ids and AR names including AR name patterns. An AR id always references one AR, while the name and pattern might reference multiple ARs. </p>
<p> <i>wc_ar</i> := <i>ar_id</i> | <i>ar_name</i> | <i>pattern</i></p>
<h3><code>wc_ar_list</code></h3>
<p>The wildcard advance reservation (AR) list specification allows referencing multiple ARs with one command. </p>
<p> <i>wc_ar_list</i> := <i>wc_ar</i>[<code>,</code> <i>wc_ar</i> <code>,</code> &#8230;]</p>
<h3><code>wc_host</code></h3>
<p>A wildcard host specification (<i>wc_host</i>) is a wildcard expression which might match one or more hosts used in the cluster. The first character of that string never begins with an at-character (&#8216;@&#8217;), even if the expression begins with a wildcard character. </p>
<pre>e.g.
<dl><dt><dd>* all hosts
a* all host beginning with an 'a'</pre>
</dl>
<h3><code>wc_hostgroup</code></h3>
<p>A wildcard hostgroup specification (<i>wc_hostgroup</i>) is a wildcard expression which might match one or more hostgroups. The first character of that string is always an at-character (&#8216;@&#8217;). </p>
<p> More information concerning hostgroups can be found in </p>
<pre>e.g.
<dl><dt><dd>@* all hostgroups in the cluster
@solaris the @solaris hostgroup</pre>
</dl>
<h3><code>wc_job</code></h3>
<p>The wildcard job specification is a placeholder for job ids, and job names including job name patterns. A job id always references one job, while the name and pattern might reference multiple jobs. </p>
<p> <i>wc_job</i> := <i>job-id</i> | <i>job_name</i> | <i>pattern</i></p>
<h3><code>wc_job_range</code></h3>
<p>The wildcard job range specification allows referencing specific array tasks for one or multiple jobs. The job is referenced via <i>wc_job</i> and in addition gets a range specifier for the array tasks. </p>
<p> <i>wc_job_range</i> := <i>wc_job</i> [<code>-t</code> <i>range</i>] </p>
<p> If present, the <i>task_range</i> restricts the effect of the <i>qalter</i> etc. operation to the array job task range specified as a suffix to the job id. (See the <code>-t</code> option to for further details on array jobs.)</p>
<h3><code>wc_job_list</code></h3>
<p>The wildcard job list specification allows referencing multiple jobs with one command. </p>
<p> <i>wc_job_list</i> := <i>wc_job</i>[<code>,</code> <i>wc_job</i>, &#8230;]</p>
<h3><code>wc_job_range_list</code></h3>
<p>The wildcard job range list (<i>wc_job_range_list</i>) allows referencing multiple job ranges with one command. one of the following forms: </p>
<p> <i>wc_job_range_list</i> := <i>wc_job_range</i>[<code>,</code><i>wc_job_range</i>&#8230;]</p>
<h3><code>wc_qdomain</code></h3>
<p><i>wc_qdomain</i> := <i>wc_cqueue</i> &quot;@&quot; <i>wc_hostgroup</i> </p>
<p> A wildcard expression queue domain specification (<i>wc_qdomain</i>) starts with a wildcard expression cluster queue name (<i>wc_cqueue</i>) followed by an at-character &#8216;@&#8217; and a wildcard expression hostgroup specification (<i>wc_hostgroup</i>). </p>
<p> A <i>wc_qdomain</i> is used to address a group of queue instances. All queue instances residing on a host which is part of matching hostgroups will be addressed. Please note, that <i>wc_hostgroup</i> always begins with an at-character. </p>
<pre>e.g.
<dl><dt><dd>*@@* all queue instances whose underlying
 host is part of at least one hostgroup
a*@@e* all queue instances beginning with a whose underlying
 host is part of at least one hostgroup beginning with e
*@@solaris all queue instances on hosts in
 the @solaris hostgroup</pre>
</dl>
<h3><code>wc_cqueue</code></h3>
<p>A wildcard expression cluster queue specification (<i>wc_cqueue</i>) is a wildcard expression which might match one or more cluster queues used in the cluster. That string never contains an at-character (&#8216;@&#8217;), even if the expression begins with a wildcard character. </p>
<pre>e.g.
<dl><dt><dd>* all cluster queues
a* all cluster queues beginning with an 'a'
a*&amp;!adam all cluster queues beginning with an 'a', but not adam</pre>
</dl>
<h3><code>wc_qinstance</code></h3>
<p><i>wc_qinstance</i> := <i>wc_cqueue</i> &quot;@&quot; <i>wc_host</i> </p>
<p> A wildcard expression queue instance specification (<i>wc_qinstance</i>) starts with a wildcard expression cluster queue name (<i>wc_cqueue</i>) followed by an at-character &#8216;@&#8217; and a wildcard expression hostname (<i>wc_host</i>). </p>
<p> <i>wc_qinstance</i> expressions are used to address a group of queue instances whose underlying hostname matches the given expression. Please note that the first character of <i>wc_host</i> never matches the at-character &#8216;@&#8217;. </p>
<pre>e.g.
<dl><dt><dd>*@* all queue instances in the cluster
*@b* all queue instances whose 
 hostname begins with a 'b'
*@b*|c* all queue instances whose 
 hostname begins with a 'b' or 'c'</pre>
</dl>
<h3><code>wc_queue</code></h3>
<p><i>wc_queue</i> := <i>wc_cqueue</i> | <i>wc_qdomain</i> | <i>wc_qinstance</i> </p>
<p> A wildcard queue expression (<i>wc_queue</i>) might either be a wildcard expression, cluster queue specification (<i>wc_cqueue</i>), a wildcard expression queue domain specification (<i>wc_qdomain</i>), or a wildcard expression queue instance specification (<i>wc_qinstance</i>). </p>
<pre>e.g.
<dl><dt><dd>big_*1 cluster queues which begin with 
 &quot;big_&quot; and end with &quot;1&quot; 
big_*&amp;!*1 cluster queues which begin with 
 &quot;big_&quot;, but do not end with &quot;1&quot;
*@fangorn all qinstances residing on host 
 fangorn</pre>
</dl>
<h3><code>wc_queue_list</code></h3>
<p><i>wc_queue_list</i> := <i>wc_queue</i> [&quot;,&quot; <i>wc_queue</i> &quot;,&quot; &#8230;] </p>
<p> Comma-separated list of <i>wc_queue</i> elements. </p>
<p> e.g.</p>
<dl>
<dd>big, medium_*@@sol*, *@fangorn.sun.com </p>
</dl>
<h3><code>wc_user</code></h3>
<p>A wildcard user name pattern is either a wildcard user name specification or a full user name. </p>
<p> <i>wc_user</i> := <i>user_name</i> | <i>pattern</i></p>
<h3><code>wc_user_list</code></h3>
<p>A list of user names. </p>
<p> <i>wc_user_list</i> := <i>wc_user</i>[<code>,</code><i>wc_user</i><code>,</code>&#8230;]</p>
<h3><code>wc_project</code></h3>
<p>A wildcard project name pattern is either a wildcard project name specification or a full project name. </p>
<p> <i>wc_project</i> := <i>project</i><code> | </code><i>pattern</i></p>
<h3><code>wc_pe_name</code></h3>
<p>A wildcard parallel environment name pattern is either a wildcard PE name specification or a full PE name. </p>
<p> <i>wc_pe_name</i> := <i>pe_name</i> | <i>pattern</i></p>
<h3><code>parallel_env</code></h3>
<p>The <code>parallel_env</code> specification has the format </p>
<p> <i>wc_pe_name</i> <i>n</i>[<code>&#8211;</code>[<i>m</i>]]|[<code>&#8211;</code>]<i>m</i>,&#8230; </p>
<p> specifying a parallel programming environment (PE) to select for a submitted job or an AR. The range descriptor following the wildcard PE name specifies the number of slots to allocate, which is usually equivalent to the total number of parallel processes to be run (for simple distributed memory jobs) or the number of threads (for shared memory or mixed distributed/threaded jobs), as implied by the PE definition. xxQS_NAMExx will allocate the appropriate resources, as available. contains information about the definition of PEs. </p>
<p> You can specify a PE name which uses wildcards. Thus the request &quot;mpi*&quot; will match any parallel environment with a name starting with the string &quot;mpi&quot;. In the case of multiple parallel environments whose names match a name string, when it is required to select one the one with the most available slots is chosen. </p>
<p> The range specification is a list of range expressions of the form &quot;<i>n</i><code>&#8211;</code><i>m</i>&quot;, where <i>n</i> and <i>m</i> are positive, non-zero integers. The form &quot;<i>n</i>&quot; is equivalent to &quot;<i>n</i><code>&#8211;</code><i>n</i>&quot;. The form &quot;<code>&#8211;</code><i>m</i>&quot; is equivalent to &quot;<code>1-</code><i>m</i>&quot;. The form &quot;<i>n</i><code>&#8211;</code>&quot; is equivalent to &quot;<i>n</i><code>&#8211;</code>infinity&quot;. The range specification is processed as follows: The largest number of queues requested is checked first. If enough queues meeting the specified attribute list are available, all are reserved. If not, the next smaller number of queues is checked, and so forth.</p>
<h2>See Also</h2>
<h2>Copyright</h2>
<p>See for a full statement of rights and permissions.</p>
