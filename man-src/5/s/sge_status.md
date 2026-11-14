---
title: "sge_status(5)"
name: "sge_status"
section: "5"
letter: "s"
url: "/docs/linux/man/5-sge_status/"
description: "sge_status – xxQS_NAMExx job status values"
---

<p>sge_status &#8211; xxQS_NAMExx job status values</p>
<h2>Description</h2>
<h3>Job state</h3>
<p>The following table lists the job states shown by and returned by The DRMAA <i>state</i> corresponds to the <code>DRMAA_PS_</code><i>state</i> value that may be returned by </p>
<table BORDER>
<tr VALIGN=top>
<td ALIGN=center><code>Category</code></td>
<td ALIGN=center><code>State</code></td>
<td ALIGN=center><code>SGE</code></td>
<td ALIGN=center><code>DRMAA state</code>
</td>
</tr>
<tr VALIGN=top>
<td ROWSPAN=2>Pending</td>
<td>pending</td>
<td>qw, Rq</td>
<td>QUEUED_ACTIVE
</td>
</tr>
<tr VALIGN=top>
<td>pending, user hold</td>
<td>hqw</td>
<td>USER_ON_HOLD</td>
</tr>
<tr VALIGN=top>
<td>pending, system hold</td>
<td>hqw</td>
<td>SYSTEM_ON_HOLD</td>
</tr>
<tr VALIGN=top>
<td> pending, user and system hold </td>
<td>hqw</td>
<td>USER_SYSTEM_ON_HOLD</td>
</tr>
<tr VALIGN=top>
<td> pending, user hold, re-queue </td>
<td>hRwq</td>
<td>USER_ON_HOLD</td>
</tr>
<tr VALIGN=top>
<td> pending, system hold, re-queue </td>
<td>hRwq</td>
<td>SYSTEM_ON_HOLD</td>
</tr>
<tr VALIGN=top>
<td> pending, user and system hold, re-queue </td>
<td>hRwq</td>
<td>USER_SYSTEM_ON_HOLD</td>
</tr>
<tr VALIGN=top>
<td ROWSPAN=2> Running / transferring </td>
<td>running, transferring</td>
<td>r, hr, t</td>
<td>RUNNING
</td>
</tr>
<tr VALIGN=top>
<td> running, re-run / transferring </td>
<td>Rr, Rt</td>
<td>RUNNING</td>
</tr>
<tr VALIGN=top>
<td ROWSPAN=2>Suspended</td>
<td>job suspended</td>
<td>s, ts</td>
<td>USER_SUSPENDED
</td>
</tr>
<tr VALIGN=top>
<td>queue suspended</td>
<td>S, tS</td>
<td>SYSTEM_SUSPENDED</td>
</tr>
<tr VALIGN=top>
<td> queue suspended by alarm </td>
<td>T, tT</td>
<td>SYSTEM_SUSPENDED</td>
</tr>
<tr VALIGN=top>
<td> all suspended with re-run </td>
<td> Rs, Rts, RS, RtS, RT, RtT </td>
<td>SYSTEM_SUSPENDED</td>
</tr>
<tr VALIGN=top>
<td>Error</td>
<td> all pending states with error </td>
<td> Eqw, Ehqw, EhRqw </td>
<td>FAILED
</td>
</tr>
<tr VALIGN=top>
<td>Deleting</td>
<td> all running and suspended states with deletion </td>
<td> dr, dt, dRr, dRt, ds, dS, dT, dRs, dRS, dRT </td>
<td> same as equivalent DRMAA states without the &quot;d&quot;
</td>
</tr>
<tr VALIGN=top>
<td>Finished</td>
<td> job finished normally </td>
<td>z</td>
<td>DONE
</td>
</tr>
<tr VALIGN=top>
<td>Unkown</td>
<td> status cannot be determined </td>
<td></td>
<td>UNDETERMINED
</td>
</tr>
</table>
<h3>The following table lists the &quot;failed&quot; values reported by</h3>
<p>(see their description, also reported by <i>qacct</i>, whether the resource usage accounting data are valid for the job (&quot;OK&quot;), and an explanation. The host&#8217;s messages file or the shepherd trace file (preserved with <code>execd_params</code> <code>KEEP_ACTIVE</code> in may provide more information about errors. </p>
<table BORDER>
<tr VALIGN=top>
<td><code>Code</code></td>
<td><code>Description</code></td>
<td><code>OK</code></td>
<td><code>Explanation</code>
</td>
</tr>
<tr VALIGN=top>
<td>0</td>
<td>no failure</td>
<td>Y</td>
<td>ran and exited normally
</td>
</tr>
<tr VALIGN=top>
<td>1</td>
<td>assumedly before job</td>
<td>N</td>
<td>failed early in execd
</td>
</tr>
<tr VALIGN=top>
<td>3</td>
<td>before writing config</td>
<td>N</td>
<td>failed before execd set up local spool
</td>
</tr>
<tr VALIGN=top>
<td>4</td>
<td>before writing PID</td>
<td>N</td>
<td>shepherd failed to record its pid &#8211; filesystem problem?
</td>
</tr>
<tr VALIGN=top>
<td>6</td>
<td>setting processor set</td>
<td>N</td>
<td>failed setting up processor set (obsolete)
</td>
</tr>
<tr VALIGN=top>
<td>7</td>
<td>before prolog</td>
<td>N</td>
<td>failed before prolog
</td>
</tr>
<tr VALIGN=top>
<td>8</td>
<td>in prolog</td>
<td>N</td>
<td>failed in prolog
</td>
</tr>
<tr VALIGN=top>
<td>9</td>
<td>before pestart</td>
<td>N</td>
<td>failed before starting PE
</td>
</tr>
<tr VALIGN=top>
<td>10</td>
<td>in pestart</td>
<td>N</td>
<td>failed in PE starter
</td>
</tr>
<tr VALIGN=top>
<td>11</td>
<td>before job</td>
<td>N</td>
<td> failed in shepherd before starting job
</td>
</tr>
<tr VALIGN=top>
<td>12</td>
<td>before pestop</td>
<td>Y</td>
<td> ran, but failed before calling PE stop procedure
</td>
</tr>
<tr VALIGN=top>
<td>13</td>
<td>in pestop</td>
<td>Y</td>
<td> ran, but PE stop procedure failed
</td>
</tr>
<tr VALIGN=top>
<td>14</td>
<td>before epilog</td>
<td>Y</td>
<td> ran, but failed before calling epilog
</td>
</tr>
<tr VALIGN=top>
<td>15</td>
<td>in epilog</td>
<td>Y</td>
<td> ran, but failed in epilog
</td>
</tr>
<tr VALIGN=top>
<td>16</td>
<td>releasing processor set</td>
<td>Y</td>
<td> ran, but processor set could not be released (obsolete)
</td>
</tr>
<tr VALIGN=top>
<td>17</td>
<td>through signal</td>
<td>Y</td>
<td> job killed by signal (possibly qdel)
</td>
</tr>
<tr VALIGN=top>
<td>18</td>
<td>shepherd returned error</td>
<td>N</td>
<td>shepherd died somehow
</td>
</tr>
<tr VALIGN=top>
<td>19</td>
<td>before writing exit_status</td>
<td>N</td>
<td> shepherd didn&#8217;t write reports correctly &#8211; probably program or machine crash
</td>
</tr>
<tr VALIGN=top>
<td>20</td>
<td>found unexpected error file</td>
<td>?</td>
<td> shepherd encountered a problem
</td>
</tr>
<tr VALIGN=top>
<td>21</td>
<td>in recognizing job</td>
<td>N</td>
<td> qmaster asked about an unknown job (not in accounting?)
</td>
</tr>
<tr VALIGN=top>
<td>24</td>
<td> migrating (checkpointing jobs) </td>
<td>Y</td>
<td>ran, will be migrated
</td>
</tr>
<tr VALIGN=top>
<td>25</td>
<td>rescheduling</td>
<td>Y</td>
<td> ran, will be rescheduled
</td>
</tr>
<tr VALIGN=top>
<td>26</td>
<td>opening output file</td>
<td>N</td>
<td> failed opening stderr/stdout file
</td>
</tr>
<tr VALIGN=top>
<td>27</td>
<td>searching requested shell</td>
<td>N</td>
<td>failed finding specified shell
</td>
</tr>
<tr VALIGN=top>
<td>28</td>
<td> changing to working directory </td>
<td>N</td>
<td> failed changing to start directory
</td>
</tr>
<tr VALIGN=top>
<td>29</td>
<td>AFS setup</td>
<td>N</td>
<td>failed setting up AFS security
</td>
</tr>
<tr VALIGN=top>
<td>30</td>
<td>application error returned</td>
<td>Y</td>
<td> ran and exited 100 &#8211; maybe re-scheduled
</td>
</tr>
<tr VALIGN=top>
<td>31</td>
<td>accessing sgepasswd file</td>
<td>N</td>
<td> failed because sgepasswd not readable (MS Windows)
</td>
</tr>
<tr VALIGN=top>
<td>32</td>
<td> entry is missing in password file </td>
<td>N</td>
<td> failed because user not in sgepasswd (MS Windows)
</td>
</tr>
<tr VALIGN=top>
<td>33</td>
<td>wrong password</td>
<td>N</td>
<td> failed because of wrong password against sgepasswd (MS Windows)
</td>
</tr>
<tr VALIGN=top>
<td>34</td>
<td> communicating with Grid Engine Helper Service </td>
<td>N</td>
<td> failed because of failure of helper service (MS Windows)
</td>
</tr>
<tr VALIGN=top>
<td>35</td>
<td> before job in Grid Engine Helper Service </td>
<td>N</td>
<td> failed because of failure running helper service (MS Windows)
</td>
</tr>
<tr VALIGN=top>
<td>36</td>
<td>checking configured daemons</td>
<td>N</td>
<td> failed because of configured remote startup daemon
</td>
</tr>
<tr VALIGN=top>
<td>37</td>
<td> qmaster enforced h_rt, h_cpu, or h_vmem limit </td>
<td>Y</td>
<td> ran, but killed due to exceeding run time limit
</td>
</tr>
<tr VALIGN=top>
<td>38</td>
<td>adding supplementary group</td>
<td>N</td>
<td> failed adding supplementary gid to job
</td>
</tr>
<tr VALIGN=top>
<td>100</td>
<td>assumedly after job</td>
<td>Y</td>
<td> ran, but killed by a signal (perhaps due to exceeding resources), task died, shepherd died (e.g. node crash), etc.
</td>
</tr>
</table>
<p> See for the effect of non-zero return codes from the various methods (prolog etc.) executed by the shepherd.</p>
<h2>See Also</h2>
