---
title: "git-maintenance(1)"
name: "git-maintenance"
section: "1"
letter: "g"
url: "/docs/linux/man/1-git-maintenance/"
description: "git-maintenance – Run tasks to optimize Git repository data"
---

<h2 class="name">NAME</h2>
<p> git-maintenance &#8211; Run tasks to optimize Git repository data </p>
<h2>SYNOPSIS</h2>
<pre>
<i>git maintenance</i> run [&lt;options&gt;]
</pre>
<h2>DESCRIPTION</h2>
<p> Run tasks to optimize Git repository data, speeding up other Git commands and reducing storage requirements for the repository. </p>
<p> Git commands that add repository data, such as <code>git add</code> or <code>git fetch</code>, are optimized for a responsive user experience. These commands do not take time to optimize the Git data, since such optimizations scale with the full size of the repository while these user commands each perform a relatively small action. </p>
<p> The <code>git maintenance</code> command provides flexibility for how to optimize the Git repository.</p>
<h2>SUBCOMMANDS</h2>
<p> register</p>
<dl>
<dt>
<dd> Initialize Git config values so any scheduled maintenance will start running on this repository. This adds the repository to the <code>maintenance.repo</code> config variable in the current user&#8217;s global config and enables some recommended configuration values for <code>maintenance.&lt;task&gt;.schedule</code>. The tasks that are enabled are safe for running in the background without disrupting foreground processes. </p>
<p> The <code>register</code> subcommand will also set the <code>maintenance.strategy</code> config value to <code>incremental</code>, if this value is not previously set. The <code>incremental</code> strategy uses the following schedule for each maintenance task: </p>
<dl>
<dt>
<dd> &bull; <code>gc</code>: disabled.</dl>
<dl>
<dt>
<dd> &bull; <code>commit-graph</code>: hourly.</dl>
<dl>
<dt>
<dd> &bull; <code>prefetch</code>: hourly.</dl>
<dl>
<dt>
<dd> &bull; <code>loose-objects</code>: daily.</dl>
<dl>
<dt>
<dd> &bull; <code>incremental-repack</code>: daily.</dl>
<p> <code>git maintenance register</code> will also disable foreground maintenance by setting <code>maintenance.auto = false</code> in the current repository. This config setting will remain after a <code>git maintenance unregister</code> command.</dl>
<p> run</p>
<dl>
<dt>
<dd> Run one or more maintenance tasks. If one or more <code>&#8211;task</code> options are specified, then those tasks are run in that order. Otherwise, the tasks are determined by which <code>maintenance.&lt;task&gt;.enabled</code> config options are true. By default, only <code>maintenance.gc.enabled</code> is true.</dl>
<p> start</p>
<dl>
<dt>
<dd> Start running maintenance on the current repository. This performs the same config updates as the <code>register</code> subcommand, then updates the background scheduler to run <code>git maintenance run &#8211;scheduled</code> on an hourly basis.</dl>
<p> stop</p>
<dl>
<dt>
<dd> Halt the background maintenance schedule. The current repository is not removed from the list of maintained repositories, in case the background maintenance is restarted later.</dl>
<p> unregister</p>
<dl>
<dt>
<dd> Remove the current repository from background maintenance. This only removes the repository from the configured list. It does not stop the background maintenance processes from running.</dl>
<h2>TASKS</h2>
<p> commit-graph</p>
<dl>
<dt>
<dd> The <code>commit-graph</code> job updates the <code>commit-graph</code> files incrementally, then verifies that the written data is correct. The incremental write is safe to run alongside concurrent Git processes since it will not expire <code>.graph</code> files that were in the previous <code>commit-graph-chain</code> file. They will be deleted by a later run based on the expiration delay.</dl>
<p> prefetch</p>
<dl>
<dt>
<dd> The <code>prefetch</code> task updates the object directory with the latest objects from all registered remotes. For each remote, a <code>git fetch</code> command is run. The configured refspec is modified to place all requested refs within <code>refs/prefetch/</code>. Also, tags are not updated. </p>
<p> This is done to avoid disrupting the remote-tracking branches. The end users expect these refs to stay unmoved unless they initiate a fetch. With prefetch task, however, the objects necessary to complete a later real fetch would already be obtained, so the real fetch would go faster. In the ideal case, it will just become an update to a bunch of remote-tracking branches without any object transfer.</dl>
<p> gc</p>
<dl>
<dt>
<dd> Clean up unnecessary files and optimize the local repository. &quot;GC&quot; stands for &quot;garbage collection,&quot; but this task performs many smaller tasks. This task can be expensive for large repositories, as it repacks all Git objects into a single pack-file. It can also be disruptive in some situations, as it deletes stale data. See <code><a href="/docs/linux/man/1-git-gc/">git-gc</a></code>(1) for more details on garbage collection in Git.</dl>
<p> loose-objects</p>
<dl>
<dt>
<dd> The <code>loose-objects</code> job cleans up loose objects and places them into pack-files. In order to prevent race conditions with concurrent Git commands, it follows a two-step process. First, it deletes any loose objects that already exist in a pack-file; concurrent Git processes will examine the pack-file for the object data instead of the loose object. Second, it creates a new pack-file (starting with &quot;loose-&quot;) containing a batch of loose objects. The batch size is limited to 50 thousand objects to prevent the job from taking too long on a repository with many loose objects. The <code>gc</code> task writes unreachable objects as loose objects to be cleaned up by a later step only if they are not re-added to a pack-file; for this reason it is not advisable to enable both the <code>loose-objects</code> and <code>gc</code> tasks at the same time.</dl>
<p> incremental-repack</p>
<dl>
<dt>
<dd> The <code>incremental-repack</code> job repacks the object directory using the <code>multi-pack-index</code> feature. In order to prevent race conditions with concurrent Git commands, it follows a two-step process. First, it calls <code>git multi-pack-index expire</code> to delete pack-files unreferenced by the <code>multi-pack-index</code> file. Second, it calls <code>git multi-pack-index repack</code> to select several small pack-files and repack them into a bigger one, and then update the <code>multi-pack-index</code> entries that refer to the small pack-files to refer to the new pack-file. This prepares those small pack-files for deletion upon the next run of <code>git multi-pack-index expire</code>. The selection of the small pack-files is such that the expected size of the big pack-file is at least the batch size; see the <code>&#8211;batch-size</code> option for the <code>repack</code> subcommand in <code><a href="/docs/linux/man/1-git-multi-pack-index/">git-multi-pack-index</a></code>(1). The default batch-size is zero, which is a special case that attempts to repack all pack-files into a single pack-file.</dl>
<p> pack-refs</p>
<dl>
<dt>
<dd> The <code>pack-refs</code> task collects the loose reference files and collects them into a single file. This speeds up operations that need to iterate across many references. See <code><a href="/docs/linux/man/1-git-pack-refs/">git-pack-refs</a></code>(1) for more information.</dl>
<h2>OPTIONS</h2>
<p> &#8211;auto</p>
<dl>
<dt>
<dd> When combined with the <code>run</code> subcommand, run maintenance tasks only if certain thresholds are met. For example, the <code>gc</code> task runs when the number of loose objects exceeds the number stored in the <code>gc.auto</code> config setting, or when the number of pack-files exceeds the <code>gc.autoPackLimit</code> config setting. Not compatible with the <code>&#8211;schedule</code> option.</dl>
<p> &#8211;schedule</p>
<dl>
<dt>
<dd> When combined with the <code>run</code> subcommand, run maintenance tasks only if certain time conditions are met, as specified by the <code>maintenance.&lt;task&gt;.schedule</code> config value for each <code>&lt;task&gt;</code>. This config value specifies a number of seconds since the last time that task ran, according to the <code>maintenance.&lt;task&gt;.lastRun</code> config value. The tasks that are tested are those provided by the <code>&#8211;task=&lt;task&gt;</code> option(s) or those with <code>maintenance.&lt;task&gt;.enabled</code> set to true.</dl>
<p> &#8211;quiet</p>
<dl>
<dt>
<dd> Do not report progress or other information over <code>stderr</code>.</dl>
<p> &#8211;task=&lt;task&gt;</p>
<dl>
<dt>
<dd> If this option is specified one or more times, then only run the specified tasks in the specified order. If no <code>&#8211;task=&lt;task&gt;</code> arguments are specified, then only the tasks with <code>maintenance.&lt;task&gt;.enabled</code> configured as <code>true</code> are considered. See the <i>TASKS</i> section for the list of accepted <code>&lt;task&gt;</code> values.</dl>
<p> &#8211;scheduler=auto|crontab|systemd-timer|launchctl|schtasks</p>
<dl>
<dt>
<dd> When combined with the <code>start</code> subcommand, specify the scheduler for running the hourly, daily and weekly executions of <code>git maintenance run</code>. Possible values for <code>&lt;scheduler&gt;</code> are <code>auto</code>, <code>crontab</code> (POSIX), <code>systemd-timer</code> (Linux), <code>launchctl</code> (macOS), and <code>schtasks</code> (Windows). When <code>auto</code> is specified, the appropriate platform-specific scheduler is used; on Linux, <code>systemd-timer</code> is used if available, otherwise <code>crontab</code>. Default is <code>auto</code>.</dl>
<h2>TROUBLESHOOTING</h2>
<p> The <code>git maintenance</code> command is designed to simplify the repository maintenance patterns while minimizing user wait time during Git commands. A variety of configuration options are available to allow customizing this process. The default maintenance options focus on operations that complete quickly, even on large repositories. </p>
<p> Users may find some cases where scheduled maintenance tasks do not run as frequently as intended. Each <code>git maintenance run</code> command takes a lock on the repository&#8217;s object database, and this prevents other concurrent <code>git maintenance run</code> commands from running on the same repository. Without this safeguard, competing processes could leave the repository in an unpredictable state. </p>
<p> The background maintenance schedule runs <code>git maintenance run</code> processes on an hourly basis. Each run executes the &quot;hourly&quot; tasks. At midnight, that process also executes the &quot;daily&quot; tasks. At midnight on the first day of the week, that process also executes the &quot;weekly&quot; tasks. A single process iterates over each registered repository, performing the scheduled tasks for that frequency. Depending on the number of registered repositories and their sizes, this process may take longer than an hour. In this case, multiple <code>git maintenance run</code> commands may run on the same repository at the same time, colliding on the object database lock. This results in one of the two tasks not running. </p>
<p> If you find that some maintenance windows are taking longer than one hour to complete, then consider reducing the complexity of your maintenance tasks. For example, the <code>gc</code> task is much slower than the <code>incremental-repack</code> task. However, this comes at a cost of a slightly larger object database. Consider moving more expensive tasks to be run less frequently. </p>
<p> Expert users may consider scheduling their own maintenance tasks using a different schedule than is available through <code>git maintenance start</code> and Git configuration options. These users should be aware of the object database lock and how concurrent <code>git maintenance run</code> commands behave. Further, the <code>git gc</code> command should not be combined with <code>git maintenance run</code> commands. <code>git gc</code> modifies the object database but does not take the lock in the same way as <code>git maintenance run</code>. If possible, use <code>git maintenance run &#8211;task=gc</code> instead of <code>git gc</code>. </p>
<p> The following sections describe the mechanisms put in place to run background maintenance by <code>git maintenance start</code> and how to customize them.</p>
<h2>BACKGROUND MAINTENANCE ON POSIX SYSTEMS</h2>
<p> The standard mechanism for scheduling background tasks on POSIX systems is <a href="/docs/linux/man/8-cron/">cron</a>(8). This tool executes commands based on a given schedule. The current list of user-scheduled tasks can be found by running <code>crontab -l</code>. The schedule written by <code>git maintenance start</code> is similar to this: </p>
<dl>
<dt>
<dd>
<pre><code>
#BEGIN GIT MAINTENANCE SCHEDULE
#The following schedule was created by Git
#Any edits made in this region might be
#replaced in the future by a Git command.
0 1-23 * * * "/&lt;path&gt;/git" --exec-path="/&lt;path&gt;" for-each-repo --config=maintenance.repo maintenance run --schedule=hourly
0 0 * * 1-6 "/&lt;path&gt;/git" --exec-path="/&lt;path&gt;" for-each-repo --config=maintenance.repo maintenance run --schedule=daily
0 0 * * 0 "/&lt;path&gt;/git" --exec-path="/&lt;path&gt;" for-each-repo --config=maintenance.repo maintenance run --schedule=weekly
#END GIT MAINTENANCE SCHEDULE
</code></pre>
</dl>
<p> The comments are used as a region to mark the schedule as written by Git. Any modifications within this region will be completely deleted by <code>git maintenance stop</code> or overwritten by <code>git maintenance start</code>. </p>
<p> The <code>crontab</code> entry specifies the full path of the <code>git</code> executable to ensure that the executed <code>git</code> command is the same one with which <code>git maintenance start</code> was issued independent of <code>PATH</code>. If the same user runs <code>git maintenance start</code> with multiple Git executables, then only the latest executable is used. </p>
<p> These commands use <code>git for-each-repo &#8211;config=maintenance.repo</code> to run <code>git maintenance run &#8211;schedule=&lt;frequency&gt;</code> on each repository listed in the multi-valued <code>maintenance.repo</code> config option. These are typically loaded from the user-specific global config. The <code>git maintenance</code> process then determines which maintenance tasks are configured to run on each repository with each <code>&lt;frequency&gt;</code> using the <code>maintenance.&lt;task&gt;.schedule</code> config options. These values are loaded from the global or repository config values. </p>
<p> If the config values are insufficient to achieve your desired background maintenance schedule, then you can create your own schedule. If you run <code>crontab -e</code>, then an editor will load with your user-specific <code>cron</code> schedule. In that editor, you can add your own schedule lines. You could start by adapting the default schedule listed earlier, or you could read the <a href="/docs/linux/man/5-crontab/">crontab</a>(5) documentation for advanced scheduling techniques. Please do use the full path and <code>&#8211;exec-path</code> techniques from the default schedule to ensure you are executing the correct binaries in your schedule.</p>
<h2>BACKGROUND MAINTENANCE ON LINUX SYSTEMD SYSTEMS</h2>
<p> While Linux supports <code>cron</code>, depending on the distribution, <code>cron</code> may be an optional package not necessarily installed. On modern Linux distributions, systemd timers are superseding it. </p>
<p> If user systemd timers are available, they will be used as a replacement of <code>cron</code>. </p>
<p> In this case, <code>git maintenance start</code> will create user systemd timer units and start the timers. The current list of user-scheduled tasks can be found by running <code>systemctl &#8211;user list-timers</code>. The timers written by <code>git maintenance start</code> are similar to this: </p>
<dl>
<dt>
<dd>
$ systemctl&#8211; user list &#8211; timers NEXT LEFT LAST PASSED UNIT ACTIVATES Thu 2021 &#8211; 04 &#8211; 29 19 : 00 : 00 CEST 42min left Thu 2021 &#8211; 04 &#8211; 29 18 : 00 : 11 CEST 17min ago git &#8211; maintenance[at] hourly.timer git &#8211; maintenance[at] hourly.service Fri 2021 &#8211; 04 &#8211; 30 00 : 00 : 00 CEST 5h 42min left Thu 2021 &#8211; 04 &#8211; 29 00 : 00 : 11 CEST 18h ago git &#8211; maintenance[at] daily.timer git &#8211; maintenance[at] daily.service Mon 2021 &#8211; 05 &#8211; 03 00 : 00 : 00 CEST 3 days left Mon 2021 &#8211; 04 &#8211; 26 00 : 00 : 11 CEST 3 days ago git &#8211; maintenance[at] weekly.timer git &#8211; maintenance[at] weekly.service
</dl>
<p> One timer is registered for each <code>&#8211;schedule=&lt;frequency&gt;</code> option. </p>
<p> The definition of the systemd units can be inspected in the following files: </p>
<dl>
<dt>
<dd>
<pre><code>
~ /.config / systemd / user / git - maintenance[at].timer ~ /.config / systemd / user / git - maintenance[at].service ~ /.config / systemd / user / timers.target.wants / git - maintenance[at] hourly.timer ~ /.config / systemd / user / timers.target.wants / git - maintenance[at] daily.timer ~ /.config / systemd / user / timers.target.wants / git - maintenance[at] weekly.timer
</code></pre>
</dl>
<p> <code>git maintenance start</code> will overwrite these files and start the timer again with <code>systemctl &#8211;user</code>, so any customization should be done by creating a drop-in file, i.e. a <code>.conf</code> suffixed file in the <code>~/.config/systemd/user/git-maintenance [at] .service.d</code> directory. </p>
<p> <code>git maintenance stop</code> will stop the user systemd timers and delete the above mentioned files. </p>
<p> For more details, see <code><a href="/docs/linux/man/5-systemd-timer/">systemd.timer</a>(5)</code>.</p>
<h2>BACKGROUND MAINTENANCE ON MACOS SYSTEMS</h2>
<p> While macOS technically supports <code>cron</code>, using <code>crontab -e</code> requires elevated privileges and the executed process does not have a full user context. Without a full user context, Git and its credential helpers cannot access stored credentials, so some maintenance tasks are not functional. </p>
<p> Instead, <code>git maintenance start</code> interacts with the <code>launchctl</code> tool, which is the recommended way to schedule timed jobs in macOS. Scheduling maintenance through <code>git maintenance (start|stop)</code> requires some <code>launchctl</code> features available only in macOS 10.11 or later. </p>
<p> Your user-specific scheduled tasks are stored as XML-formatted <code>.plist</code> files in <code>~/Library/LaunchAgents/</code>. You can see the currently-registered tasks using the following command: </p>
<dl>
<dt>
<dd>
<pre>
$ ls ~/Library/LaunchAgents/org.git-scm.git*
org.git-scm.git.daily.plist
org.git-scm.git.hourly.plist
org.git-scm.git.weekly.plist
</pre>
</dl>
<p> One task is registered for each <code>&#8211;schedule=&lt;frequency&gt;</code> option. To inspect how the XML format describes each schedule, open one of these <code>.plist</code> files in an editor and inspect the <code>&lt;array&gt;</code> element following the <code>&lt;key&gt;StartCalendarInterval&lt;/key&gt;</code> element. </p>
<p> <code>git maintenance start</code> will overwrite these files and register the tasks again with <code>launchctl</code>, so any customizations should be done by creating your own <code>.plist</code> files with distinct names. Similarly, the <code>git maintenance stop</code> command will unregister the tasks with <code>launchctl</code> and delete the <code>.plist</code> files. </p>
<p> To create more advanced customizations to your background tasks, see <a href="/docs/linux/man/5-launchctl-plist/">launchctl.plist</a>(5) for more information.</p>
<h2>BACKGROUND MAINTENANCE ON WINDOWS SYSTEMS</h2>
<p> Windows does not support <code>cron</code> and instead has its own system for scheduling background tasks. The <code>git maintenance start</code> command uses the <code>schtasks</code> command to submit tasks to this system. You can inspect all background tasks using the Task Scheduler application. The tasks added by Git have names of the form <code>Git Maintenance (&lt;frequency&gt;)</code>. The Task Scheduler GUI has ways to inspect these tasks, but you can also export the tasks to XML files and view the details there. </p>
<p> Note that since Git is a console application, these background tasks create a console window visible to the current user. This can be changed manually by selecting the &quot;Run whether user is logged in or not&quot; option in Task Scheduler. This change requires a password input, which is why <code>git maintenance start</code> does not select it by default. </p>
<p> If you want to customize the background tasks, please rename the tasks so future calls to <code>git maintenance (start|stop)</code> do not overwrite your custom tasks.</p>
<h2>GIT</h2>
<p> Part of the <code><a href="/docs/linux/man/1-git/">git</a></code>(1) suite </p>
<h2>Index</h2>
