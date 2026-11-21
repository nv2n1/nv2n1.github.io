---

title: "pbs(1)"
name: "pbs"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pbs/"
---

pbs - general information on pbs 

PBS stands for <i>Portable Batch System.</i> It is a networked subsystem for submitting, monitoring, and controlling a work load of batch jobs on one or more systems. More information about PBS is available in the PBS Users Guide. 

 <i>Batch</i> means that the job will be scheduled for execution at a time chosen by the subsystem according to a defined policy and the availability of resources. For a normal batch job, the standard output and standard error of the job will be returned to files available to the user when the job is complete. This differs from an interactive session where commands are executed when entered via the terminal and output is returned directly to the terminal. PBS also supports an <i>interactive batch</i> mode where the input and output is connected to the user's terminal, but the scheduling of the job is still under control of the batch system. 

 A <i>job</i> is typically a shell script and a set of attributes which provide resource and control information about the job. A job does not have to be submitted on the system where it will run, tt can be submitted on any system with the PBS commands and access to the execution system, see <i>qsub(1B).</i> Output will be returned to the system from which the job was submitted unless directed otherwise. 

 Attributes offer control over when a job is eligible to be run, what happens to the output when it is completed and how the user is notified when it completes. The attributes of the job may be specified on the command line or in the job script when the job is submitted. For information about job attributes, see qsub(1B) and <i>pbs_job_attributes(7B).</i> 

 One important attribute is the <i>resource list.</i> The list specifies the amount and type of resources needed by the job in order to execute. The list also implies a hard upper limit on usage of those resources. When the limit is reached, the job is terminated. The types of resources available to a job vary with the system architecture. For a list of resources supported on the default system, see <i>pbs_resources(7B).</i> There are man pages for other systems types as well, see <i>pbs_resources_aix4(7B),</i> <i>pbs_resources_fujitsu(7B),</i> <i>pbs_resources_irix5(7B),</i> <i>pbs_resources_solaris5(7B),</i> <i>pbs_resources_sp2(7B),</i> <i>pbs_resources_sunos4(7B),</i> or <i>pbs_resources_unicos8(7B).</i> 

 Once a job has been submitted, it may be monitored by use of the <i>qstat(1B) </i> command. Two forms of output are available with the qstat command. The default form is the short display. Information about a job is limited to a single line. Complete information about the job or jobs is available through qstat with the -f option. Information will be given about all jobs in the system, all jobs in specified queues, or only specified jobs. 

 When displaying status of jobs, you will see in which queue the job resides. In PBS a queue is just a collection point for jobs, it does not imply any execution ordering. That ordering is determined by a scheduling policy implemented by the system administration. 

 Other commands of interest which have man pages of their own are:
<dl>
<dt>qalter
</dt><dd> Alter a job's attributes.
</dd><dt>qdel
</dt><dd> Delete a job.
</dd><dt>qhold
</dt><dd> Place a hold on a job to keep it from being scheduled for running.
</dd><dt>qmove
</dt><dd> Move a job to a different queue or server.
</dd><dt>qmsg
</dt><dd> Append a message to the output of an executing job.
</dd><dt>qrerun
</dt><dd> Terminate an executing job and return it to a queue.
</dd><dt>qrls
</dt><dd> Remove a hold from a job.
</dd><dt>qselect
</dt><dd> Obtain a list of jobs that met certain criteria.
</dd><dt>qsig
</dt><dd> Send a signal to an executing job.</dd></dl>
 

<h2>SEE ALSO</h2>

 qalter(1B), qdel(1B), qhold(1B), qmove(1B), qmsg(1B), qrerun(1B), qrls(1B), qselect(1B), qsig(1B), qsub(1B) and the PBS User Guide. Starting with qsub(1B), you can find all other available PBS man pages by following references in the &quot;See Also&quot; section.
