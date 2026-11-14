---
title: "fcrondyn(1)"
name: "fcrondyn"
section: "1"
letter: "f"
url: "/docs/linux/man/1-fcrondyn/"
---

<h2 class="name">NAME</h2>
 

 fcrondyn - dialog dyn-amically with a running fcron daemon 

<h2>SYNOPSIS</h2>

 

 <b>fcrondyn</b> [ <b>-c </b><i>file</i> ] [ <b>-i</b> ] 

 

 <b>fcrondyn</b> [ <b>-c </b><i>file</i> ] <b>-x </b><i>command</i> 

 

 <b>fcrondyn</b> [ <b>-h</b> ] 

<h2>DESCRIPTION</h2>

 

 <b>Fcrondyn</b> is a user tool intended to interact with a running fcron daemon. It can, for instance, list user's jobs loaded by fcron, run one of them, renice a running job, send a signal to a running job, etc.

<h2>OPTIONS</h2>

<dl>
<dt><b>-i</b>
<dd> Run <b>fcrondyn</b> in interactive mode. <b>fcrondyn</b> is also run in interactive mode when no option is given.
<dt><b>-x </b><i>command</i>
<dd> Run <i>command</i> and returns immediately. See below for syntax and a list of commands.
<dt><b>-c </b><i>file</i>
<dd> Make <b>fcrondyn</b> use config file <i>file</i> instead of default config file <i>/usr/local/etc/fcron.conf</i>. To interact with a running <b>fcron</b> process, <b>fcrondyn</b> must use the same config file as the process. That way, several <b>fcron</b> processes can run simultaneously on an only system.
<dt><b>-d</b>
<dd> Run in debug mode. In this mode, many informational messages will be output in order to check if anything went wrong.
<dt><b>-h</b>
<dd> Display a brief description of the options.
<dt><b>-V</b>
<dd> Display an informational message about <b>fcrondyn</b>, including its version and the license under which it is distributed.</dl>

<h2>COMMAND DESCRIPTION</h2>

 

 <b>Fcrondyn</b>'s command syntax is the following: 

<dl>
<dt>
<dd> 

 <b>command</b> <i>arg1</i> <i>arg2</i> [...]</dl>
 

 An argument of a <b>fcrondyn</b> command is of one of the following type: &quot;ARGUMENT TYPES OF FCRONDYN'S COMMANDS&quot;
<dl>
<dt><b>user</b>
<dd> A valid user name.
<dt><b>jobid</b>
<dd> A job id given by one of <b>fcrondyn</b>'s <b>ls*</b> commands (i.e. an integer).
<dt><b>sig</b>
<dd> A signal number, or its name (case does not matter). For instance, &quot;term&quot; or &quot;15&quot;.
<dt><b>niceval</b>
<dd> A job priority value. A <b>niceval</b> is an integer from -20 (highest priority) to 19 (lowest) (only root is allowed to use a negative value with this option).</dl>
 

 Last, but not least, the following commands are recognized (optional arguments are between []): &quot;VALID FCRONDYN'S COMMANDS&quot;
<dl>
<dt><b>help</b>
<dd>
<dt><b>h</b>
<dd> Print an help message about fcrondyn's commands.
<dt><b>quit</b>
<dd>
<dt><b>q</b>
<dd> In interactive mode, quit fcrondyn.
<dt><b>ls [user]</b>
<dd> List all jobs of user. When <b>ls</b> is run by root, all users are listed unless a user name is given as argument. See below for some explanations about the fields used by <b>ls*</b> commands.
<dt><b>ls_lavgq [user]</b>
<dd> Same as <b>ls</b>, but list only the jobs which are in the load-average queue (i.e. which are waiting for a lower load average to be run).
<dt><b>ls_serialq [user]</b>
<dd> Same as <b>ls</b>, but list only the jobs which are in the serial queue (i.e. which are waiting for other jobs to be finished).
<dt><b>ls_exeq [user]</b>
<dd> Same as <b>ls</b>, but list only the jobs which are running.
<dt><b>detail jobid</b>
<dd> Print details about a job. <b>jobid</b> is the one given by <b>ls</b>.
<dt><b>runnow jobid</b>
<dd> Instead of waiting for the next scheduled execution time, run the job now. The next execution time is changed as if the job had run on schedule.
<dt><b>run jobid</b>
<dd> Run the job now. Its next execution time is not changed.
<dt><b>kill sig jobid</b>
<dd> Send a signal to a running job.
<dt><b>renice niceval jobid</b>
<dd> Change the priority of a running job. &quot;FIELDS USED BY DETAIL AND LS* COMMANDS&quot;
<dt><b>ID</b>
<dd> Job's unique identification number.
<dt><b>USER</b>
<dd> User who owns this job.
<dt><b>PID</b>
<dd> The pid of the running job.
<dt><b>INDEX</b>
<dd> Index of the job in the serial queue (i.e. it will be run when all the jobs of an inferior index have been run)
<dt><b>R&amp;Q</b>
<dd> The job has this number instances of the given task which are either running or queued in the serial or lavg queue.
<dt><b>OPTIONS</b>
<dd> List of main options which are set for the task. L for the jobs which run only under a given system Load average (option lavg, lavg1, lavg5 and lavg15), LO (Load average Once) if only at most one instance of the task can be in the load average queue at a given time (option lavgonce), S for serialized jobs (option serial), SO for the jobs which will be serialized only for the next execution (Serial Once), and ES if several instances of the same job can run simultaneously (option exesev).
<dt><b>LAVG</b>
<dd> 3 values, corresponding to the 1, 5, and 15-minute (in this order) system load average values below which the job will be run, otherwise it will be queued until the system load average is appropriate (see lavg option).
<dt><b>UNTIL</b>
<dd> Field corresponding to the until option.
<dt><b>STRICT</b>
<dd> Field corresponding to the strict option. Y for yes, N for no.
<dt><b>SCHEDULE</b>
<dd> Next run is scheduled at this time and date. Please note that fcrondyn prints the next execution time and date in the time zone of the system where fcron is running, and not the time zone which can be defined for using option timezone.
<dt><b>CMD</b>
<dd> The command that will be executed.</dl>

<h2>RETURN VALUES</h2>

 

 <b>Fcrondyn</b> returns 0 on normal exit and 1 on error.

<h2>CONFORMING TO</h2>

 

 Should be POSIX compliant.

<h2>FILES</h2>

<dl>
<dt><i>/usr/local/etc/fcron.conf</i>
<dd> Configuration file for <b>fcron</b>, <b>fcrontab</b> and <b>fcrondyn</b>: contains paths (spool dir, pid file) and default programs to use (editor, shell, etc). See <b><a HREF="/docs/linux/man/5-fcron-conf/">fcron.conf</a></b>(5) for more details.
<dt><i>/usr/local/etc/fcron.allow</i>
<dd> Users allowed to use <b>fcrontab</b> and <b>fcrondyn</b> (one name per line, special name &quot;all&quot; acts for everyone)
<dt><i>/usr/local/etc/fcron.deny</i>
<dd> Users who are not allowed to use <b>fcrontab</b> and <b>fcrondyn</b> (same format as allow file)
<dt><i>/usr/local/etc/pam.d/fcron</i><b> (or </b><i>/usr/local/etc/pam.conf</i><b>)</b>
<dd> PAM configuration file for <b>fcron</b>. Take a look at <a HREF="/docs/linux/man/8-pam/">pam</a>(8) for more details.</dl>

<h2>SEE ALSO</h2>

 

 <b><a HREF="/docs/linux/man/1-fcrontab/">fcrontab</a></b>(1), 

 <b><a HREF="/docs/linux/man/1-fcrondyn/">fcrondyn</a></b>(1), 

 <b><a HREF="/docs/linux/man/5-fcrontab/">fcrontab</a></b>(5), 

 <b><a HREF="/docs/linux/man/5-fcron-conf/">fcron.conf</a></b>(5), 

 <b><a HREF="/docs/linux/man/8-fcron/">fcron</a></b>(8). 

 If you're learning how to use fcron from scratch, I suggest that you read the HTML version of the documentation (if your are not reading it right now! :) ): the content is the same, but it is easier to navigate thanks to the hyperlinks.

<h2>AUTHOR</h2>

 

 Thibault Godouet &lt;fcron [at] free.fr&gt; 

<h2>Index</h2>


