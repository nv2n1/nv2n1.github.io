---
title: "globus_gram_job_manager_rsl(3)"
name: "globus_gram_job_manager_rsl"
section: "3"
letter: "g"
url: "/docs/linux/man/3-globus_gram_job_manager_rsl/"
description: "globus_gram_job_manager_rsl – RSL Attributes This page contains a list of all RSL attributes which are supported by the GRAM Job Manager."
---

<h2 class="name">NAME</h2>
<p> globus_gram_job_manager_rsl &#8211; RSL Attributes This page contains a list of all RSL attributes which are supported by the GRAM Job Manager. </p>
<p>&nbsp;<wbr> </p>
<p> <code>arguments</code></p>
<dl>
<dt>
<dd> The command line arguments for the executable. Use quotes, if a space is required in a single argument.</dl>
<p>&nbsp;<wbr> </p>
<p> <code>count</code></p>
<dl>
<dt>
<dd> The number of executions of the executable.</dl>
<p>&nbsp;<wbr> </p>
<p> <code>directory</code></p>
<dl>
<dt>
<dd> Specifies the path of the directory the jobmanager will use as the default directory for the requested job.</dl>
<p>&nbsp;<wbr> </p>
<p> <code>dry_run</code></p>
<dl>
<dt>
<dd> If dryrun = yes then the jobmanager will not submit the job for execution and will return success.</dl>
<p>&nbsp;<wbr> </p>
<p> <code>environment</code></p>
<dl>
<dt>
<dd> The environment variables that will be defined for the executable in addition to default set that is given to the job by the jobmanager.</dl>
<p>&nbsp;<wbr> </p>
<p> <code>executable</code></p>
<dl>
<dt>
<dd> The name of the executable file to run on the remote machine. If the value is a GASS URL, the file is transferred to the remote gass cache before executing the job and removed after the job has terminated.</dl>
<p>&nbsp;<wbr> </p>
<p> <code>file_clean_up</code></p>
<dl>
<dt>
<dd> Specifies a list of files which will be removed after the job is completed.</dl>
<p>&nbsp;<wbr> </p>
<p> <code>file_stage_in</code></p>
<dl>
<dt>
<dd> Specifies a list of (&#8216;remote URL&#8217; &#8216;local file&#8217;) pairs which indicate files to be staged to the nodes which will run the job.</dl>
<p>&nbsp;<wbr> </p>
<p> <code>file_stage_in_shared</code></p>
<dl>
<dt>
<dd> Specifies a list of (&#8216;remote URL&#8217; &#8216;local file&#8217;) pairs which indicate files to be staged into the cache. A symlink from the cache to the &#8216;local file&#8217; path will be made.</dl>
<p>&nbsp;<wbr> </p>
<p> <code>file_stage_out</code></p>
<dl>
<dt>
<dd> Specifies a list of (&#8216;local file&#8217; &#8216;remote URL&#8217;) pairs which indicate files to be staged from the job to a GASS-compatible file server.</dl>
<p>&nbsp;<wbr> </p>
<p> <code>gass_cache</code></p>
<dl>
<dt>
<dd> Specifies location to override the GASS cache location.</dl>
<p>&nbsp;<wbr> </p>
<p> <code>gram_my_job</code></p>
<dl>
<dt>
<dd> Obsolete and ignored.</dl>
<p>&nbsp;<wbr> </p>
<p> <code>host_count</code></p>
<dl>
<dt>
<dd> Only applies to clusters of SMP computers, such as newer IBM SP systems. Defines the number of nodes (&#8216;pizza boxes&#8217;) to distribute the &#8216;count&#8217; processes across.</dl>
<p>&nbsp;<wbr> </p>
<p> <code>job_type</code></p>
<dl>
<dt>
<dd> This specifies how the jobmanager should start the job. Possible values are single (even if the count &gt; 1, only start 1 process or thread), multiple (start count processes or threads), mpi (use the appropriate method (e.g. mpirun) to start a program compiled with a vendor-provided MPI library. Program is started with count nodes), and condor (starts condor jobs in the &#8216;condor&#8217; universe.)</dl>
<p>&nbsp;<wbr> </p>
<p> <code>library_path</code></p>
<dl>
<dt>
<dd> Specifies a list of paths to be appended to the system-specific library path environment variables.</dl>
<p>&nbsp;<wbr> </p>
<p> <code>max_cpu_time</code></p>
<dl>
<dt>
<dd> Explicitly set the maximum cputime for a single execution of the executable. The units is in minutes. The value will go through an atoi() conversion in order to get an integer. If the GRAM scheduler cannot set cputime, then an error will be returned.</dl>
<p>&nbsp;<wbr> </p>
<p> <code>max_memory</code></p>
<dl>
<dt>
<dd> Explicitly set the maximum amount of memory for a single execution of the executable. The units is in Megabytes. The value will go through an atoi() conversion in order to get an integer. If the GRAM scheduler cannot set maxMemory, then an error will be returned.</dl>
<p>&nbsp;<wbr> </p>
<p> <code>max_time</code></p>
<dl>
<dt>
<dd> The maximum walltime or cputime for a single execution of the executable. Walltime or cputime is selected by the GRAM scheduler being interfaced. The units is in minutes. The value will go through an atoi() conversion in order to get an integer.</dl>
<p>&nbsp;<wbr> </p>
<p> <code>max_wall_time</code></p>
<dl>
<dt>
<dd> Explicitly set the maximum walltime for a single execution of the executable. The units is in minutes. The value will go through an atoi() conversion in order to get an integer. If the GRAM scheduler cannot set walltime, then an error will be returned.</dl>
<p>&nbsp;<wbr> </p>
<p> <code>min_memory</code></p>
<dl>
<dt>
<dd> Explicitly set the minimum amount of memory for a single execution of the executable. The units is in Megabytes. The value will go through an atoi() conversion in order to get an integer. If the GRAM scheduler cannot set minMemory, then an error will be returned.</dl>
<p>&nbsp;<wbr> </p>
<p> <code>project</code></p>
<dl>
<dt>
<dd> Target the job to be allocated to a project account as defined by the scheduler at the defined (remote) resource.</dl>
<p>&nbsp;<wbr> </p>
<p> <code>proxy_timeout</code></p>
<dl>
<dt>
<dd> Obsolete and ignored. Now a job-manager-wide setting.</dl>
<p>&nbsp;<wbr> </p>
<p> <code>queue</code></p>
<dl>
<dt>
<dd> Target the job to a queue (class) name as defined by the scheduler at the defined (remote) resource.</dl>
<p>&nbsp;<wbr> </p>
<p> <code>remote_io_url</code></p>
<dl>
<dt>
<dd> Writes the given value (a URL base string) to a file, and adds the path to that file to the environment throught the GLOBUS_REMOTE_IO_URL environment variable. If this is specified as part of a job restart RSL, the job manager will update the file&#8217;s contents. This is intended for jobs that want to access files via GASS, but the URL of the GASS server has changed due to a GASS server restart.</dl>
<p>&nbsp;<wbr> </p>
<p> <code>restart</code></p>
<dl>
<dt>
<dd> Start a new job manager, but instead of submitting a new job, start managing an existing job. The job manager will search for the job state file created by the original job manager. If it finds the file and successfully reads it, it will become the new manager of the job, sending callbacks on status and streaming stdout/err if appropriate. It will fail if it detects that the old jobmanager is still alive (via a timestamp in the state file). If stdout or stderr was being streamed over the network, new stdout and stderr attributes can be specified in the restart RSL and the jobmanager will stream to the new locations (useful when output is going to a GASS server started by the client that&#8217;s listening on a dynamic port, and the client was restarted). The new job manager will return a new contact string that should be used to communicate with it. If a jobmanager is restarted multiple times, any of the previous contact strings can be given for the restart attribute.</dl>
<p>&nbsp;<wbr> </p>
<p> <code>rsl_substitution</code></p>
<dl>
<dt>
<dd> Specifies a list of values which can be substituted into other rsl attributes&#8217; values through the mechanism.</dl>
<p>&nbsp;<wbr> </p>
<p> <code>save_state</code></p>
<dl>
<dt>
<dd> Causes the jobmanager to save it&#8217;s job state information to a persistent file on disk. If the job manager exits or is suspended, the client can later start up a new job manager which can continue monitoring the job.</dl>
<p>&nbsp;<wbr> </p>
<p> <code>savejobdescription</code></p>
<dl>
<dt>
<dd> Save a copy of the job description to $HOME</dl>
<p>&nbsp;<wbr> </p>
<p> <code>scratch_dir</code></p>
<dl>
<dt>
<dd> Specifies the location to create a scratch subdirectory in. A SCRATCH_DIRECTORY RSL substitution will be filled with the name of the directory which is created.</dl>
<p>&nbsp;<wbr> </p>
<p> <code>stderr</code></p>
<dl>
<dt>
<dd> The name of the remote file to store the standard error from the job. If the value is a GASS URL, the standard error from the job is transferred dynamically during the execution of the job. There are two accepted forms of this value. It can consist of a single destination: stderr = URL, or a sequence of destinations: stderr = (DESTINATION) (DESTINATION). In the latter case, the DESTINATION may itself be a URL or a sequence of an x-gass-cache URL followed by a cache tag.</dl>
<p>&nbsp;<wbr> </p>
<p> <code>stderr_position</code></p>
<dl>
<dt>
<dd> Specifies where in the file remote standard error streaming should be restarted from. Must be 0.</dl>
<p>&nbsp;<wbr> </p>
<p> <code>stdin</code></p>
<dl>
<dt>
<dd> The name of the file to be used as standard input for the executable on the remote machine. If the value is a GASS URL, the file is transferred to the remote gass cache before executing the job and removed after the job has terminated.</dl>
<p>&nbsp;<wbr> </p>
<p> <code>stdout</code></p>
<dl>
<dt>
<dd> The name of the remote file to store the standard output from the job. If the value is a GASS URL, the standard output from the job is transferred dynamically during the execution of the job. There are two accepted forms of this value. It can consist of a single destination: stdout = URL, or a sequence of destinations: stdout = (DESTINATION) (DESTINATION). In the latter case, the DESTINATION may itself be a URL or a sequence of an x-gass-cache URL followed by a cache tag.</dl>
<p>&nbsp;<wbr> </p>
<p> <code>stdout_position</code></p>
<dl>
<dt>
<dd> Specifies where in the file remote output streaming should be restarted from. Must be 0.</dl>
<p>&nbsp;<wbr> </p>
<p> <code>two_phase</code></p>
<dl>
<dt>
<dd> Use a two-phase commit for job submission and completion. The job manager will respond to the initial job request with a WAITING_FOR_COMMIT error. It will then wait for a signal from the client before doing the actual job submission. The integer supplied is the number of seconds the job manager should wait before timing out. If the job manager times out before receiving the commit signal, or if a client issues a cancel signal, the job manager will clean up the job&#8217;s files and exit, sending a callback with the job status as GLOBUS_GRAM_PROTOCOL_JOB_STATE_FAILED. After the job manager sends a DONE or FAILED callback, it will wait for a commit signal from the client. If it receives one, it cleans up and exits as usual. If it times out and save_state was enabled, it will leave all of the job&#8217;s files in place and exit (assuming the client is down and will attempt a job restart later). The timeoutvalue can be extended via a signal. When one of the following errors occurs, the job manager does not delete the job state file when it exits: GLOBUS_GRAM_PROTOCOL_ERROR_COMMIT_TIMED_OUT, GLOBUS_GRAM_PROTOCOL_ERROR_TTL_EXPIRED, GLOBUS_GRAM_PROTOCOL_ERROR_JM_STOPPED, GLOBUS_GRAM_PROTOCOL_ERROR_USER_PROXY_EXPIRED. In these cases, it can not be restarted, so the job manager will not wait for the commit signal after sending the FAILED callback</dl>
<p>&nbsp;<wbr> </p>
<p> <code>username</code></p>
<dl>
<dt>
<dd> Verify that the job is running as this user.</dl>
<hr>
<h2>Index</h2>
