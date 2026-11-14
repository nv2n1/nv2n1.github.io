---
title: "pbs_selstat(3)"
name: "pbs_selstat"
section: "3"
letter: "p"
url: "/docs/linux/man/3-pbs_selstat/"
description: "pbs_selstat – obtain status of selected pbs batch jobs"
---

<p>pbs_selstat &#8211; obtain status of selected pbs batch jobs</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;pbs_error.h&gt;

#include &lt;pbs_ifl.h&gt;</code></pre>
<pre>struct batch_status *pbs_selstat(int connect, struct attropl&nbsp;<wbr>*sel_list,
char&nbsp;<wbr>*extend)
void pbs_statfree(struct batch_status *psj)</pre>
<h2>Description</h2>
<p>Issue a batch request to examine the status of jobs which meet certain criteria. <code>pbs_selstat</code>() returns a list of batch_status structures for those jobs which met the selection criteria. This function is a combination of <code>pbs_selectjobs</code>() and <code>pbs_statjob</code>(). It is an extension to the POSIX Batch standard. Initially all batch jobs are selected for which the user is authorized to query status. This set may be reduced or filtered by specifying certain attributes of the jobs. A <i>Select Status</i> batch request is generated and sent to the server over the connection specified by <i> which is the return value of </i><code>pbs_connect</code>(). The parameter, <i> is a pointer to an attropl </i> structure which is defined in pbs_ifl.h as: struct attrl {<br />
    struct attrl *next;<br />
    char *name;<br />
    char *resource;<br />
    char *value;<br />
}; The <i> </i> list is terminated by the first entry where <code> is a null pointer. The member points to a string which is the name of the attribute. Not all of the job attributes may be used as a selection criteria. The member points to a string which is the name of a resource. This member is only used when is set to ATTR_l, otherwise it should be a pointer to a null string. The member points to a string which is the value of the attribute or resource. The attribute names are defined in pbs_ifl.h: </p>
<dl>
<dd>
<dl>
<dt>#define ATTR_a Execution_Time</p>
<dd>Select based upon the job&#8217;s execution time.</p>
<dt>#define ATTR_A Account_Name</p>
<dd>Select (E) based upon the account string.</p>
<dt>#define ATTR_c Checkpoint</p>
<dd>Select based upon the checkpoint interval.</p>
<dt>#define ATTR_e Error_Path</p>
<dd>Select (E) based upon the name of the standard error file.</p>
<dt>#define ATTR_g Group_List</p>
<dd>Select (E) based upon the list of group names under which the job may execute.</p>
<dt>#define ATTR_h Hold_Types</p>
<dd>Select (E) based upon the hold types.</p>
<dt>#define ATTR_j Join_Paths</p>
<dd>Select (E) based upon the value of the join list.</p>
<dt>#define ATTR_k Keep_Files</p>
<dd>Select (E) based upon the value of the keep files list.</p>
<dt>#define ATTR_l Resource_List</p>
<dd>Select based upon the value of the resource named in</p>
<dt>#define ATTR_m Mail_Points</p>
<dd>Select (E) based upon the setting of the mail points attribute.</p>
<dt>#define ATTR_M Mail_Users</p>
<dd>Select (E) based upon the list of user names to which mail will be sent.</p>
<dt>#define ATTR_N Job_Name</p>
<dd>Select (E) based upon the job name.</p>
<dt>#define ATTR_o Output_Path</p>
<dd>Select (E) based upon the name of the standard output file.</p>
<dt>#define ATTR_p Priority</p>
<dd>Select based upon the priority of the job.</p>
<dt>#define ATTR_q destination</p>
<dd>Select based upon the specified destination. Jobs selected are restricted to those residing in the named queue. If destination is the null string, the default queue at the server is assumed.</p>
<dt>#define ATTR_r Rerunable</p>
<dd>Select (E) based upon the rerunable flag.</p>
<dt>#define ATTR_session session_id</p>
<dd>Select based upon the session id assigned to running jobs.</p>
<dt>#define ATTR_S Shell_Path_List</p>
<dd>Select (E) based upon the execution shell list.</p>
<dt>#define ATTR_u User_List</p>
<dd>Select (E) based upon the owner of the jobs.</p>
<dt>#define ATTR_v Variable_List</p>
<dd>Select (E) based upon the list of environment variables.</p>
<dt>#define ATTR_ctime ctime</p>
<dd>Select based upon the creation time of the job.</p>
<dt>#define ATTR_depend depend</p>
<dd>Select based upon the list of job dependencies.</p>
<dt>#define ATTR_mtime mtime</p>
<dd>Select based upon the last modification time of the job.</p>
<dt>#define ATTR_qtime qtime</p>
<dd>Select based upon the time of the job was placed into the current queue.</p>
<dt>#define ATTR_qtype queue_type</p>
<dd>Select (E) base on the type of queue in which the job resides.</p>
<dt>#define ATTR_stagein stagein</p>
<dd>Select based upon the list of files to be staged-in.</p>
<dt>#define ATTR_stageout stageout</p>
<dd>Select based upon the list of files to be staged-out.</p>
<dt>#define ATTR_state job_state</p>
<dd>Select based upon the state of the jobs. State is not a job attribute, but is included here to allow selection.</dl>
</dl>
<p> The member defines the operator in the logical expression: </p>
<p> The logical expression must evaluate as true for the job to be selected. The permissible values of are defined in pbs_ifl.h as: The attributes marked with (E) in the description above may only be selected with the equal, EQ, or not equal, NE, operators. If </code><i> itself is a null pointer, then no selection is done on the basis of attributes. The return value is a pointer to a list of batch_status</i> structures or the null pointer if no jobs can be queried for status. The batch_status structure is defined in pbs_ifl.h as struct attrl {<br />
    struct attrl *next;<br />
    char *name;<br />
    char *resource;<br />
    char *value;<br />
}; The entry, <code> is a pointer to a list of attrl structures defined in pbs_ifl.h as: </p>
<pre><code>struct attrl {
    struct attrl *next;
    char *name;
    char *resource;
    char *value;
};</code></pre>
<p> It is up the user to free the list of batch_status structures when no longer needed, by calling <code>pbs_statfree</code>(). The parameter, <i> is reserved for implementation defined extensions. TORQUE 2.0.0p1 added the #define&#8217;d constant string EXECQUEONLY to only retrieve jobs in execution queues. </i></p>
<h2>See Also</h2>
<p><a href="//www.systutorials.com/docs/linux/man/1B-qselect/">qselect</a>(1B), <a href="//www.systutorials.com/docs/linux/man/3B-pbs_alterjob/">pbs_alterjob</a>(3B), <a href="//www.systutorials.com/docs/linux/man/3B-pbs_connect/">pbs_connect</a>(3B), <a href="//www.systutorials.com/docs/linux/man/3B-pbs_statjob/">pbs_statjob</a>(3B), and <a href="//www.systutorials.com/docs/linux/man/3B-pbs_selectjob/">pbs_selectjob</a>(3B).</p>
<h2>Diagnostics</h2>
<p>When the batch request generated by pbs_selstat() function has been completed successfully by a batch server, the routine will return a pointer to the list of batch_status structures. If no jobs met the criteria or an error occurred, the return will be the null pointer. If an error occurred, the global integer pbs_errno will be set to a non-zero value.</p>
