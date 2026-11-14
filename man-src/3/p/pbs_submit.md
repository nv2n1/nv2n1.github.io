---
title: "pbs_submit(3)"
name: "pbs_submit"
section: "3"
letter: "p"
url: "/docs/linux/man/3-pbs_submit/"
description: "pbs_submit – submit a pbs batch job"
---

<p>pbs_submit &#8211; submit a pbs batch job</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;pbs_error.h&gt;

#include &lt;pbs_ifl.h&gt;</code></pre>
<pre>char *pbs_submit(int connect, struct attropl&nbsp;<wbr>*attrib,
char&nbsp;<wbr>*script, char&nbsp;<wbr>*destination, char&nbsp;<wbr>*extend)</pre>
<h2>Description</h2>
<p>Issue a batch request to submit a new batch job. A <i>Queue Job</i> batch request is generated and sent to the server over the connection specified by <i> which is the return value of </i><code>pbs_connect</code>(). The job will be submitted to the queue specified by <i> The parameter, is a list of attropl</i> structures which is defined in pbs_ifl.h as: </p>
<pre><code>struct attrl {
    char *name;
    char *resource;
    char *value;
    struct attrl *next;
    enum batch_op op;
};</code></pre>
<p> The <i> list is terminated by the first entry where </i><code> is a null pointer. The member points to a string which is the name of the attribute. The member points to a string which is the value of the attribute. The attribute names are defined in pbs_ifl.h: </p>
<dl>
<dd>
<dl>
<dt>#define ATTR_a Execution_Time</p>
<dd>Defines the job&#8217;s execution time.</p>
<dt>#define ATTR_A Account_Name</p>
<dd>Defines the account string.</p>
<dt>#define ATTR_c Checkpoint</p>
<dd>Defines the checkpoint interval.</p>
<dt>#define ATTR_e Error_Path</p>
<dd>Defines the path name for the standard error of the job.</p>
<dt>#define ATTR_g Group_List</p>
<dd>Defines the list of group names under which the job may execute.</p>
<dt>#define ATTR_h Hold_Types</p>
<dd>Defines the hold types, the only allowable value string is</p>
<dt>#define ATTR_j Join_Paths</p>
<dd>Defines whether standard error and standard output are joined (merged).</p>
<dt>#define ATTR_k Keep_Files</p>
<dd>Defines which output of the job is kept on the execution host.</p>
<dt>#define ATTR_l Resource_List</p>
<dd>Defines a resource required by the job.</p>
<dt>#define ATTR_m Mail_Points</p>
<dd>Defines the points at which the server will send mail about the job.</p>
<dt>#define ATTR_M Mail_Users</p>
<dd>Defines the list of users who would receive mail about the job.</p>
<dt>#define ATTR_N Job_Name</p>
<dd>Defines the job name.</p>
<dt>#define ATTR_o Output_Path</p>
<dd>Defines the path name for the standard output of the job.</p>
<dt>#define ATTR_p Priority</p>
<dd>Defines the priority of the job.</p>
<dt>#define ATTR_r Rerunable</p>
<dd>Defines the rerunable flag.</p>
<dt>#define ATTR_S Shell_Path_List</p>
<dd>Defines the path to the shell which will interpret the job script.</p>
<dt>#define ATTR_t job_array_request</p>
<dd>Requests specific array IDs. Makes this submission a job array submit.</p>
<dt>#define ATTR_u User_List</p>
<dd>Defines the list of user names under which the job may execute.</p>
<dt>#define ATTR_v Variable_List</p>
<dd>Defines the list of additional environment variables which are exported to the job.</p>
<dt>#define ATTR_depend depend</p>
<dd>Defines the inter-job dependencies.</p>
<dt>#define ATTR_stagein stagein</p>
<dd>Defines the list of files to be staged in prior to job execution.</p>
<dt>#define ATTR_stageout stageout</p>
<dd>Defines the list of files to be staged out after job execution.</dl>
</dl>
<p> If an attribute is not named in the </code><i> array, the default action will be taken. It will either be assigned the default value or will not be passed with the job. The action depends on the attribute. If itself is a null pointer, then the default action will be taken for each attribute. Associated with an attribute of type ATTR_l (the letter ell) is a resource name indicated by </i><code> in the </code><i>attrl</i> structure. All other attribute types should have a pointer to a null string for <code> The member is forced to a value of by pbs_submit(). The parameter, </code><i> is the path name to the job script. If the path name is relative, it will be expanded to the processes current working directory. If is a null pointer or the path name pointed to is specified as the null string, no script is passed with the job. The parameter specifies the destination for the job. It is specified as: </i><code> If </code><i> is the null string or the queue is not specified, the destination will be the default queue at the connected server. The parameter, is reserved for implementation defined extensions. The return value is a character string which is the assigned to the job by the server. The space for the string is allocated by </i><code>pbs_submit</code>() and should be released via a call to <code>free</code>() by the user when no longer needed.</p>
<h2>See Also</h2>
<p><a href="//www.systutorials.com/docs/linux/man/1B-qsub/">qsub</a>(1B) and <a href="//www.systutorials.com/docs/linux/man/3B-pbs_connect/">pbs_connect</a>(3B)</p>
<h2>Diagnostics</h2>
<p>When the batch request generated by pbs_submit() function has been completed successfully by a batch server, the routine will return a pointer to a character string which is the job identifier of the submitted batch job. Otherwise, a null pointer is returned and the error code is set in pbs_error.</p>
