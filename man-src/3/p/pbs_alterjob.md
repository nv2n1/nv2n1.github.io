---
title: "pbs_alterjob(3)"
name: "pbs_alterjob"
section: "3"
letter: "p"
url: "/docs/linux/man/3-pbs_alterjob/"
description: "pbs_alterjob – alter pbs batch job"
---

<p>pbs_alterjob &#8211; alter pbs batch job</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;pbs_error.h&gt;

#include &lt;pbs_ifl.h&gt;</code></pre>
<pre><code>int pbs_alterjob(int connect, char&nbsp;<wbr>*job_id, struct attrl&nbsp;<wbr>*attrib,
char&nbsp;<wbr>*extend)
int pbs_alterjob_async(int connect, char&nbsp;<wbr>*job_id, struct attrl&nbsp;<wbr>*attrib,
char&nbsp;<wbr>*extend)
</code></pre>
<h2>Description</h2>
<p>Issue a batch request to alter a batch job. A <i>Modify Job</i> batch request is generated and sent to the server over the connection specified by <i> which is the return value of </i><code>pbs_connect</code>(). When the asynchronous <code>pbs_alterjob_async</code>() call is used, the server will validate the request and reply before modifying the job. This version of the call can be used to reduce latency in scheduling, especially when the scheduler must modify a large number of jobs. The argument, <i> identifies which job is to be altered, it is specified in the form:<br />
 </i><code> &nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>sequence_number.server </code> The parameter, <i> is a pointer to an attrl</i> structure which is defined in pbs_ifl.h as: </p>
<pre><code>struct attrl {
    char *name;
    char *resource;
    char *value struct attrl *next;
};</code></pre>
<p> The <i> list is terminated by the first entry where </i><code> is a null pointer. The member points to a string which is the name of the attribute. The member points to a string which is the value of the attribute. The attribute names are defined in pbs_ifl.h: </p>
<dl>
<dd>
<dl>
<dt>#define ATTR_a Execution_Time</p>
<dd>Alter the job&#8217;s execution time.</p>
<dt>#define ATTR_A Account_Name</p>
<dd>Alter the account string.</p>
<dt>#define ATTR_c Checkpoint</p>
<dd>Alter the checkpoint interval.</p>
<dt>#define ATTR_e Error_Path</p>
<dd>Alter the path name for the standard error of the job.</p>
<dt>#define ATTR_g Group_List</p>
<dd>Alter the list of group names under which the job may execute.</p>
<dt>#define ATTR_h Hold_Types</p>
<dd>Alter the hold types.</p>
<dt>#define ATTR_j Join_Path</p>
<dd>Alter if standard error and standard output are joined (merged).</p>
<dt>#define ATTR_k Keep_Files</p>
<dd>Alter which output of the job is kept on the execution host.</p>
<dt>#define ATTR_l Resource_List</p>
<dd>Alter the value of a named resource.</p>
<dt>#define ATTR_m Mail_Points</p>
<dd>Alter the points at which the server will send mail about the job.</p>
<dt>#define ATTR_M Mail_Users</p>
<dd>Alter the list of users who would receive mail about the job.</p>
<dt>#define ATTR_N Job_Name</p>
<dd>Alter the job name.</p>
<dt>#define ATTR_o Output_Path</p>
<dd>Alter the path name for the standard output of the job.</p>
<dt>#define ATTR_p Priority</p>
<dd>Alter the priority of the job.</p>
<dt>#define ATTR_r Rerunable</p>
<dd>Alter the rerunable flag.</p>
<dt>#define ATTR_S Shell_Path_List</p>
<dd>Alter the path to the shell which will interprets the job script.</p>
<dt>#define ATTR_u User_List</p>
<dd>Alter the list of user names under which the job may execute.</p>
<dt>#define ATTR_v Variable_List</p>
<dd>Alter the list of environmental variables which are to be exported to the job.</p>
<dt>#define ATTR_depend depend</p>
<dd>Alter the inter-job dependencies.</p>
<dt>#define ATTR_stagein stagein</p>
<dd>Alter the list of files to be staged-in before job execution.</p>
<dt>#define ATTR_stageout stageout</p>
<dd>Alter the list of files to be staged-out after job execution.</dl>
</dl>
<p> If </code><i> itself is a null pointer, then no attributes are altered. Associated with an attribute of type ATTR_l (the letter ell) is a resource name indicated by </i><code> in the </code><i>attrl</i> structure. All other attribute types should have a pointer to a null string (&quot;&quot;) for <code> If the resource of the specified resource name is already present in the job&#8217;s </code><i> </i><font SIZE="-1"><i> attribute, it will be altered to the specified value. If the resource is not present in the attribute, it is added. Certain attributes of a job may or may not be alterable depending on the state of the job; see </i><code><a href="//www.systutorials.com/docs/linux/man/1B-qalter/">qalter</a></code>(1B). The parameter, <i> is reserved for implementation defined extensions. </i></font></p>
<h2>See Also</h2>
<p><a href="//www.systutorials.com/docs/linux/man/1B-qalter/">qalter</a>(1B), <a href="//www.systutorials.com/docs/linux/man/1B-qhold/">qhold</a>(1B), <a href="//www.systutorials.com/docs/linux/man/1B-qrls/">qrls</a>(1B), <a href="//www.systutorials.com/docs/linux/man/1B-qsub/">qsub</a>(1B), <a href="//www.systutorials.com/docs/linux/man/3B-pbs_connect/">pbs_connect</a>(3B), <a href="//www.systutorials.com/docs/linux/man/3B-pbs_holdjob/">pbs_holdjob</a>(3B), and <a href="//www.systutorials.com/docs/linux/man/3B-pbs_rlsjob/">pbs_rlsjob</a>(3B)</p>
<h2>Diagnostics</h2>
<p>When the batch request generated by the <code>pbs_alterjob</code>() or <code>pbs_alterjob_async</code>() function has been completed successfully by a batch server, the routine will return 0 (zero). Otherwise, a non zero error is returned. The error number is also set in pbs_errno.</p>
