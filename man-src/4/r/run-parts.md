---
title: "run-parts(4)"
name: "run-parts"
section: "4"
letter: "r"
url: "/docs/linux/man/4-run-parts/"
description: "crontabs – configuration and scripts for running periodical jobs"
---

<p>crontabs &#8211; configuration and scripts for running periodical jobs</p>
<h2>Synopsis</h2>
<p><code>run-parts </code> [<code>&#8211;list</code>|<code>&#8211;test</code>]<i>&lt;directory&gt;</i></p>
<h2>Description</h2>
<p>Crontabs is a historical name for the run-parts script and the system crontab. The run-parts script runs all executables in the specified directory. <code>Run-parts</code> runs all executables in the specified directory. The execution of files can be allowed or denied by creating file <code>jobs.allow</code> or <code>jobs.deny</code> which worked similar as other allow/deny config files. The file must be created in the specified directory.</p>
<dl>
<dt><code>&#8211;list</code></p>
<dd>print names of all files (not limited to executables), but don&#8217;t run them. This option can&#8217;t be used with <code>test</code> option.</p>
<dt><code>&#8211;test</code></p>
<dd>print names of files, which would be run. Randomization of jobs can be configured in the <i>/etc/sysconfig/run-parts</i> file. To enable randomization of jobs, set the RANDOMIZE parameter to 1 and set the RANDOM parameter to an integer which determines a random seed. Additionally, you may configure the RANDOMTIME parameter (again, by specifying an integer) to provide an additional level of randomization. Jobs are not randomized when the RANDOM and RANDOMTIME parameters are set to 0. Values in these two parameters must be set to 1 or larger to provide a good enough randomization. Randomization of cron jobs can be useful for shared networks, where multiple cron jobs executed at once can cause spikes in traffic, especially during daily jobs. With randomized jobs, the workload is evenly distributed throughout the day. </p>
<h2>Example Of Configuration File</h2>
<pre>RANDOMIZE=1
RANDOM=4
RANDOMTIME=8</pre>
<p>Historically the crontab file contained configuration which called <code>run-parts</code> on files in <i>cron.{daily,weekly,monthly}</i> directories. These jobs are now run indirectly through <code>anacron </code> to prevent conflicts between <code>cron </code> and <code>anacron.</code> That means the <code>anacron </code> package has to be installed if the jobs in these directories should be running. Refer to the <code><a href="/docs/linux/man/8-anacron/">anacron</a>(8) </code> how to limit the time of day of the job execution.</p>
<h2>Example</h2>
<p><i>/etc/cron.daily/jobs.deny</i> could contain for example <code>0logwatch </code> which forbid execution of this script.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-anacron/">anacron</a>(8), <a href="/docs/linux/man/5-crontab/">crontab</a>(5)</code> </p>
