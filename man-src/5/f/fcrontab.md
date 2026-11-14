---
title: "fcrontab(5)"
name: "fcrontab"
section: "5"
letter: "f"
url: "/docs/linux/man/5-fcrontab/"
description: "fcrontab – tables for driving fcron"
---

<p>fcrontab &#8211; tables for driving fcron</p>
<h2>Description</h2>
<p>A <code>fcrontab</code> is a file containing all tables used by the <code><a href="/docs/linux/man/8-fcron/">fcron</a></code>(8) daemon. In other words, it is the means for a user to tell the daemon &quot;execute this command at this moment&quot;. Each user has his own <code>fcrontab</code>, whose commands are executed as his owner (only root can run a job as another using the option runas (see below)). Blank lines, line beginning by a hash sign (#) (which are considered comments), leading blanks and tabs are ignored. Each line in a fcrontab file can be either</p>
<dl>
<dt>*</p>
<dd>an environment setting,</p>
<dt>*</p>
<dd>an option setting,</p>
<dt>*</p>
<dd>entries based on elapsed system up time,</p>
<dt>*</p>
<dd>entries based on absolute time (like normal crontab entries), or</p>
<dt>*</p>
<dd>entries run periodically.</dl>
<p> Any logical line (an entry or an assignment) can be divided into several real lines (the lines which end by a newline character) by placing a backslash (\) before the newline character (
).</p>
<h3>The Environment Settings</h3>
<p>The environment settings are of the form  name = value</dl>
<p> where the blanks around equal-sign (=) are ignored and optional. Trailing blanks are also ignored, but you can place the value in quotes (simple or double, but matching) to preserve any blanks in the value. When <code>fcron</code> executes a command, it always sets <code>USER</code>, and <code>HOME</code> as defined in <i>/etc/passwd</i> for the owner of the <code>fcrontab</code> from which the command is extracted. TZ is also defined to the value of the option timezone when this option is used. It also defines <code>SHELL</code> to the value of the SHELL used to run the command. <code>Fcron</code> uses the value of <code>SHELL</code> from the fcrontab if any, otherwise it uses the value from <i>fcron.conf</i> if any, or in last resort the value from <i>/etc/passwd</i>. <code>HOME</code> and <code>SHELL</code> may be overridden by settings in the <code>fcrontab</code>, but <code>USER</code> may not. Every other environment assignments defined in the user <code>fcrontab</code> are then made, and the command is executed. Plus, the special variable MAILTO allows you to tell <code>fcron</code> to whom it has to mail the command&#8217;s output. Note that MAILTO is in fact equivalent to a global declaration of the option mailto (see below). It is only used for backward compatibility, so you should use the option mailto directly.</p>
<h3>Entries Based On Elapsed System Up Time</h3>
<p>The entries of commands which have to be run once every m minutes of <code>fcron</code>&#8216;s execution (which is normally the same as m minutes of system&#8217;s execution) are of the form </p>
<pre>@options frequency command</pre>
<p>where frequency is a time value of the form value*multiplier+value*multiplier+&#8230;+value-in-minutes as &quot;12h02&quot; or &quot;3w2d5h1&quot;. The first means &quot;12 hours and 2 minutes of fcron execution&quot; while the second means &quot;3 weeks, 2 days, 5 hours and 1 minute of fcron execution&quot;. The only valid multipliers are: &quot;VALID TIME MULTIPLIERS&quot; meaning: multipliers: months (4 weeks): m weeks (7 days): w days (24 hours): d hours (60 minutes): h seconds: s In place of <i>options</i>, user can put a time value: it will be interpreted as @first(<i>&lt;time&gt;</i>). If first option is not set, the value of &quot;frequency&quot; is used. This kind of entry does not guarantee a time and date of execution (as the job is delayed at each startup by the time elapsed since the shutdown), but should be useful for jobs depending on the number of things done by the users (for instance, the filesystem should better be checked after a certain amount of use by the users rather than every x days, as the system may run from 1 day to x days during that x days interval). The time remaining before next execution is saved every 1800 seconds (to limit damages caused by a crash) and when <code>fcron</code> exits after having received a SIGTERM signal, i.e. when systems go down. Thus, this kind of entries is particularly useful for systems that don&#8217;t run regularly. The syntax being very simple, it may also useful for tasks which don&#8217;t need to be run at a specific time and date. <code>See also</code>: options first, mail, nolog, serial, lavg, nice, runas (see below).</p>
<h3>Some Examples Of Lines Based On Elapsed System Up Time</h3>
<pre># Get our mails every 30 minutes 
@ 30 getmails -all 
# make some security tests every 48 hours of system up time, 
# force a mail to be sent to root even if there is no output 
@mailto(root),forcemail 2d /etc/security/msec/cron-sh/security.sh</pre>
<h3>Entries Based On Time And Date</h3>
<p>The second type of <code>fcrontab</code>&#8216;s entries begins by an optional &quot;&amp;&quot;, which can be immediately followed by an optional number defining the frequency of execution (this is equivalent to option runfreq) or a declaration of options; it has five time and date fields, and a shell command : </p>
<pre>&amp;options min hrs day-of-month month day-of-week command</pre>
<p>Note that the shell command may be preceded by a user name, which is equivalent to runas(<i>&lt;user&gt;</i>): as it is only here for backward compatibility you should use option runas (see below) instead. The frequency is interpreted as: &quot;run this command after x matches of time and date fields&quot;. The time and date fields are: &quot;TIME AND DATE FIELDS&quot; field: allowed values: minute: 0-59 hour: 0-23 day of month: 1-31 month: 1-12 (or names, see below) day of week: 0-7 (0 and 7 are both Sunday, or names) A field is always filled by either an asterisk (*), which acts as &quot;first-last&quot; range, a single number or a list. List are numbers or range separated with commas (,). For instance: &quot;2,5,15,23&quot;. Ranges of number are of the form &quot;<i>&lt;begin&gt;</i>&#8211;<i>&lt;end&gt;</i>&quot;, where &quot;<i>begin</i>&quot; and &quot;<i>end</i>&quot; are included. For example, &quot;3-5&quot; specifies the values 3, 4 and 5. You can also add an optional &quot;/<i>number</i>&quot; to a range, where the <i>number</i> specifies skips of the <i>number</i>&#8216;s value through the range. For example, &quot;0-23/2&quot; can be used in the hours field to specify command execution every other hour. Finally, one or several &quot;~<i>number</i>&quot; can be added to turn off some specific values in a range. For example, &quot;5-8~6~7&quot; is equivalent to &quot;5,8&quot;. The final form of a field is:  a[-b[/c][~d][~e][&#8230;]][,f[-g[/h][~i][~j][&#8230;]]][,&#8230;]</dl>
<p> where the letters are integers. You can also use an asterisk (*) in a field. It acts for &quot;first-last&quot;. For example, a &quot;*&quot; in the field minute means all minutes from minute 0 down to minute 59. Ranges can be included in a list as a single number. For instance: &quot;2,5-10/2~6,15,20-25,30&quot;. Names can also be used for the &quot;month&quot; and &quot;day of week&quot; fields. To do so, use the first three letters of the particular day or month (case doesn&#8217;t matter). Please note that names are used exactly as numbers: you can use them in a list or a range. If a day of month and a day of week are given, the command will execute only when <code>both</code> match with the current time and date unless option dayor is set. For example, with the line </p>
<pre>5 10 31 * 7 echo ''</pre>
<p>echo will only be executed days which are a Sunday AND a 31th, at 10:05. <code>See also</code>: options dayor, bootrun, runfreq, mail, nolog, serial, lavg, nice, runas (see below).</p>
<h3>Some Examples Of Entries Based On Time And Date</h3>
<pre># run mycommand at 12:05, 12:35, 13:05, 13:35, 
# 14:05 *and* 14:35 everyday 
&amp; 05,35 12-14 * * * mycommand -u me -o file 
# get mails every hour past 20, 21, 22, and 24 minutes. 
20-24~23 * * * * getmail 
# save our work of the day every night at 03:45 with a low priority 
# unless we are sunday, mail the output to jim and run that job 
# at startup if computer was down at 03:45
&amp;nice(10),mailto(jim),bootrun 45 03 * * *~0 &quot;save --our work&quot; </pre>
<h3>Entries Run Periodically</h3>
<p>The third type of <code>fcrontab</code>&#8216;s entries begin by a &quot;%&quot;, followed by a keyword from one of 3 different lists, and optional options.</p>
<h3>*Ly Keywords</h3>
<p>Those keywords are: <i>hourly </i>, <i>daily </i>, <i>monthly </i>, <i>weekly </i> Those keywords tell <code>fcron</code> to run the command once from the beginning of the corresponding time interval to the end of that time interval. A time interval is, for example, the time from Monday 16:20 to Wednesday 01h43. For instance, the keyword <i>weekly</i> tells <code>fcron</code> to run a command once between Monday and Sunday each week. With this two kind of keywords, user must give the needed time fields (as defined in &quot;Entries based on time and date&quot; (see above)) to specify when the command should be run during each time interval: &quot;NEEDED TIME FIELDS FOR EACH KEYWORD&quot; Keywords: must be followed by the fields: <i> hourly</i>, <i>midhourly</i>: minutes.<i> daily</i>, <i>middaily</i>, <i>nightly</i>, <i>weekly</i>, <i>midweekly</i>: minutes and hours.<i> monthly</i>, <i>midmonthly</i>: minutes, hours and days.</p>
<h3>Mid*Ly Keywords</h3>
<p>They are similar to the &quot;*ly&quot; ones: <i>midhourly </i>, <i>middaily </i>, <i>nightly </i>, <i>midmonthly </i>, <i>midweekly </i> They work exactly has the &quot;*ly&quot; keywords, except that the time intervals are defined from middle to middle of the corresponding &quot;*ly&quot; intervals: <i>midweekly</i> will run a command once from Thursday to Wednesday. Note that <i>nightly</i> is equivalent to <i>middaily</i>. For example: </p>
<pre>%nightly,mail(no) * 21-23,3-5 echo &quot;a nigthly entry&quot;</pre>
<p>will run the command once each night either between 21:00 and 23:59, or between 3:00 and 5:59 (it will run as soon as possible. To change that, use option random) and won&#8217;t send mail (because option mail is set to &quot;no&quot;). <code>See also</code>: options lavg, noticenotrun, strict, mail, nolog, serial, nice, runas, random (see below).</p>
<h3>*S Keywords</h3>
<p>They are: <i>mins </i>, <i>hours </i>, <i>days </i>, <i>mons </i>, <i>dow </i> Those keywords act differently, as follows: run this command once during EACH time interval specified, ignoring the fields below the keyword in the time interval definition (a <i>hours</i> prevents the mins field to be considered as a time interval, but it will be used to determine when the line should be run during an interval: see the note below) (<i>dow</i> means &quot;day of week&quot;). Such a keyword is followed by 5 time and date fields (the same fields used for a line based on absolute time (see above)). Furthermore, there must be some non-matching time and dates in the lines with that kind of keyword (i.e. the following is not allowed : </p>
<pre>%hours * 0-23 * * * echo &quot;INCORRECT line!&quot;</pre>
<p>but </p>
<pre>%hours * 0-22 * * * echo &quot;Ok.&quot;</pre>
<p>is allowed).</p>
<dl>
<dd><code>Note:</code> a single number in a field is considered as a time interval: </p>
<pre>%mins 15 2-4 * * * echo</pre>
<p>will run at 2:15, 3:15 AND 4:15 every day. But all fields below the keywords are ignored in time interval definition: </p>
<pre>%hours 15 2-4 * * * echo</pre>
<p>will run only ONCE either at 2:15, 3:15 OR 4:15.</dl>
<p> <code>See also</code>: option random (see below).</p>
<h3>Options</h3>
<p>The options can be set either for every line below the declaration or for an individual line. In the first case, the setting is done on a whole line immediately after an exclamation mark (!), while it is done after a &quot;&amp;&quot;, a &quot;%&quot; or a &quot;@&quot; depending on the type of scheduling in the second case. Note that an option declaration in a schedule overrides the global declaration of that same option. Options are separated by commas (,) and their arguments, if any, are placed in parentheses (&quot;(&quot; and &quot;)&quot;) and separated by commas. No spaces are allowed. A declaration of options is of the form  <i>option</i>[(<i>arg1</i>[,<i>arg2</i>][&#8230;])][,<i>option</i>[(<i>arg1</i>[&#8230;])]][&#8230;]</dl>
<p> where option is either the name of an option or its abbreviation. The options are (default value in parentheses): &quot;VALID OPTIONS IN A FCRONTAB&quot;</p>
<dl>
<dt><code>bootrun</code></p>
<dd>
<dt><code>b</code></p>
<dd><code>boolean</code>(false) Run a &amp;-line at <code>fcron</code>&#8216;s startup if it should have be run during system down time.</p>
<dt><code>dayand</code></p>
<dd><code>boolean</code>(true) Perform a logic AND between week and month day. <code>See also</code>: options dayor.</p>
<dt><code>dayor</code></p>
<dd><code>boolean</code>(false) Perform a logic OR between week and month day. <code>See also</code>: options dayand.</p>
<dt><code>erroronlymail</code></p>
<dd><code>boolean</code>(false) Mail output only if job exited with a non-zero status. <code>See also</code>: options mail, mailto, forcemail, nolog.</p>
<dt><code>exesev</code></p>
<dd><code>boolean</code>(false) Can a job be executed several times simultaneously ? <code>See also</code>: options serialonce, lavgonce.</p>
<dt><code>first</code></p>
<dd>
<dt><code>f</code></p>
<dd><code>time-value</code> Delay before first execution of a job based on system up time (&quot;@&quot;-lines). Useful in the following case: you have several jobs running, say, every hour. By setting different first value for each job, you can avoid them to run simultaneously everytime. You can also set it to 0, which is useful when used in conjunction with option volatile.</p>
<dt><code>forcemail</code></p>
<dd><code>boolean</code>(false) Mail output even if zero-length. <code>See also</code>: options mail, mailto, erroronlymail, nolog.</p>
<dt><code>lavg</code></p>
<dd><code>real</code>(0) <code>real</code>(0) <code>real</code>(0) Set the values of the 1, 5 and 15-minute (in this order) system load average values below which the job should run. The values have a maximum of 1 decimal (i.e. &quot;2.3&quot;): if there are more than 1 decimal, the value will be round off. Set a value to 0 to ignore the corresponding load average (or all of the values to run the job regardless of the load average). <code>See also</code>: options lavg1, lavg5, lavg15, until, lavgonce, lavgor, lavgand, strict, noticenotrun.</p>
<dt><code>lavg1</code></p>
<dd>
<dt><code>lavg5</code></p>
<dd>
<dt><code>lavg15</code></p>
<dd><code>real</code>(0) Set the threshold of, respectively, the 1, 5 or 15 minutes system load average value. Set one of them to 0 to ignore the corresponding load average. <code>See also</code>: options lavg.</p>
<dt><code>lavgand</code></p>
<dd><code>boolean</code>(true) Perform a logic AND between the 1, 5 and 15 minutes system load average values. <code>See also</code>: options lavg, lavgor.</p>
<dt><code>lavgonce</code></p>
<dd><code><a href="/docs/linux/man/1-boolean/">boolean</a></code>(1) Can a job be queued several times in lavg queue simultaneously? <code>See also</code>: options lavg.</p>
<dt><code>lavgor</code></p>
<dd><code>boolean</code>(false) Perform a logic OR between the 1, 5 and 15 minutes system load average values. <code>See also</code>: options lavg, lavgand.</p>
<dt><code>mail</code></p>
<dd>
<dt><code>m</code></p>
<dd><code>boolean</code>(true) Mail output (if any) or not. <code>See also</code>: options mailto, forcemail, erroronlymail, nolog.</p>
<dt><code>mailto</code></p>
<dd><code>email-address</code>(name of file&#8217;s owner) Mail output (if needed) to &quot;<i>email-address</i>&quot;. It can be either a single user-name or a fully qualified email address. A mailto declared and empty (string &quot;&quot;) is equivalent to &quot;mail(false)&quot;. <code>See also</code>: options mail, forcemail, erroronlymail, nolog.</p>
<dt><code>nice</code></p>
<dd>
<dt><code>n</code></p>
<dd><code>nice-value</code> Change job priority. A <code>nice-value</code> is an integer from -20 (highest priority) to 19 (lowest) (only root is allowed to use a negative value with this option).</p>
<dt><code>nolog</code></p>
<dd><code>boolean</code>(false) If set to true, log only errors for the corresponding job(s). May be useful for jobs running very often, and/or to reduce disk access on a laptop. <code>See also</code>: options mail, mailto, erroronlymail, forcemail.</p>
<dt><code>noticenotrun</code></p>
<dd><code>boolean</code>(false) Should <code>fcron</code> mail user to report the non-execution of a %-job or a &amp;-job? (because of system down state for both or a too high system load average for the latter) <code>See also</code>: options lavg, strict.</p>
<dt><code>random</code></p>
<dd><code>boolean</code>(false) In a line run periodically, this option answers the question: should this job be run as soon as possible in its time interval of execution (safer), or should fcron set a random time of execution in that time interval? Note that if this option is set, the job may not run if fcron is not running during the <code>whole</code> execution interval. Besides, you must know that the random scheme may be quite easy to guess for skilled people: thus, you shouldn&#8217;t rely on this option to make important things secure. However, it shouldn&#8217;t be a problem for most uses.</p>
<dt><code>reset</code></p>
<dd><code>boolean</code> Reset all the options to default.</p>
<dt><code>runas</code></p>
<dd><code>user-name</code> Run with &quot;<i>user-name</i>&quot; permissions and environment (only root is allowed to use this option).</p>
<dt><code>runfreq</code></p>
<dd>
<dt><code>r</code></p>
<dd><code>integer</code> Run every &quot;<i>runfreq</i>&quot; matches of time and date. (this option is ignored for lines based on elapsed system up time).</p>
<dt><code>serial</code></p>
<dd>
<dt><code>s</code></p>
<dd><code>boolean</code>(false) <code>Fcron</code> runs at most 1 serial jobs (ie. for which the option serial is set to true), and the same number of lavg serial jobs (ie. for which both option serial and lavg (or lavg1 or lavg5 or lavg15) are set to true) simultaneously. This value may be modified by <code>fcron</code>&#8216;s option <code>-m</code>. This option is especially useful when used with big jobs in order to limit the system overload. <code>See also</code>: options serialonce, lavg.</p>
<dt><code>serialonce</code></p>
<dd><code>boolean</code>(0) Can a job be queued several times in serial queue simultaneously? <code>See also</code>: options exesev, lavgonce.</p>
<dt><code>stdout</code></p>
<dd><code>boolean</code>(false) If fcron is running in the foreground, then also let jobs print to stderr/stdout instead of mailing or discarding it. <code>See also</code>: fcron&#8217;s option <code>&#8211;once</code> in <code><a href="/docs/linux/man/8-fcron/">fcron</a></code>(8).</p>
<dt><code>strict</code></p>
<dd><code>boolean</code>(true) When a lavg %-job is at the end of a time interval of execution, should it be removed from the lavg queue (strict(true), so the job is not run) or be let there until the system load average allows its execution (strict(false))? <code>See also</code>: options lavg, noticenotrun.</p>
<dt><code>timezone</code></p>
<dd><code>timezone-name</code>(time zone of the system) Run the job in the given time zone. timezone-name is a string which is valid for the environment variable TZ: see the documentation of your system for more details. For instance, &quot;Europe/Paris&quot; is valid on a Linux system. This option handles daylight saving time changes correctly. The TZ environ,ment variable is set to the value of timezone when a job defining this option is run. Please note that if you give an erroneous timezone-name argument, it will be SILENTLY ignored, and the job will run in the time zone of the system. WARNING: do *not* use option timezone and option tzdiff simultaneously! There is no need to do so, and timezone is cleverer than tzdiff. <code>See also</code>: options tzdiff.</p>
<dt><code>tzdiff</code></p>
<dd><code>integer</code>(0) WARNING: this option is deprecated: use option timezone instead! Time zone difference (in hours, between -24 and 24) between the system time, and the local real time. This option allows a user to define its &amp; and %-lines in the local time. Note that this value is set for a whole fcrontab file, and only the last definition is taken into account. tzdiff is quite stupid: it doesn&#8217;t handle daylight saving changes, while option timezone does, so you should use the latter. <code>See also</code>: options timezone.</p>
<dt><code>until</code></p>
<dd><code>time-value</code>(0) Set the timeout of the waiting of the wanted system load average values. If the timeout is exceeded, the job runs no matter the load average. Set until to 0 to remove the timeout. <code>See also</code>: options lavg.</p>
<dt><code>volatile</code></p>
<dd><code>boolean</code>(false) When set to true, the job is based on a &quot;volatile&quot; system up time, i.e. restart counting each time fcron is started, which is useful when fcron is started by a script running only, for instance, during a dialup connection: the &quot;volatile&quot; system up time then refers to the dialup connection time. You may also want to use option first if you use fcron that way. <code>See also</code>: options first, stdout, lines based on elapsed system up time, fcron&#8217;s option <code>&#8211;once</code> in <code><a href="/docs/linux/man/8-fcron/">fcron</a></code>(8).</dl>
<p> A <code>boolean</code> argument can be non-existent, in which case parentheses are not used and it means true; the string &quot;true&quot;, &quot;yes&quot; or 1 to mean true; and the string &quot;false&quot;, &quot;no&quot; or 0 to mean false. See above for explanations about time value (section &quot;entries based on elapsed system up time&quot;). Note that dayand and dayor are in fact the same option: a false value to dayand is equivalent to a true to dayor, and reciprocally a false value to dayor is equivalent a true value to dayand. It is the same for lavgand and lavgor. Note a special case to be handled: A job should be entered into the serial queue, *but* the previous entry for this job has not been completed yet, because of high system load or some external event. Option serialonce answers the question: should the new entry of the job be ignored? This way one can distinguish between jobs required to run a certain number of times, preferably at specified times, and tasks to be performed irrespective of their number (-&gt; serialonce(true)), which make the system respond faster. The same considerations apply for the load average queue, and can be expressed with option lavgonce. Moreover, if the serial or the lavg queue contains respectively more than 30 and 30 jobs, any new job is refused and not run to avoid an overwhelming of system resources. In this case, an error message is logged through syslog. Finally, if jobs remain in the lavg or serial queues when fcron stops, they will be put once in the corresponding queue on startup (their order may not be conserved).</p>
<h3>An Example Of An Option Declaration:</h3>
<pre>!reset,serial(true),dayor,bootrun(0),mailto(root),lavg(.5,2,1.5)</pre>
<h2>Examples</h2>
<h3>An Example Of A User Fcrontab</h3>
<pre><code># use /bin/bash to run commands, ignoring what /etc/passwd says
SHELL=/bin/bash

# mail output to thib, no matter whose fcrontab this is
!mailto(thib)

# define a variable which is equivalent to &quot; Hello thib and paul! &quot;
# here the newline characters are escaped by a backslash (\)
# and quotes are used to force to keep leading and trailing blanks
TEXT= &quot; Hello\
thib and\
paul! &quot;

# we want to use serial but not bootrun:
!serial(true),b(0)

# run after five minutes of execution the first time,
# then run every hour
@first(5) 1h   echo &quot;Run every hour&quot;

# run every day
@ 1d echo &quot;fcron daily&quot;

# run once between in the morning and once in the afternoon
#  if systems is running at any moment of these time intervals
%hours * 8-12,14-18 * * * echo &quot;Hey boss, I'm working today!&quot;

# run once a week during our lunch
%weekly * 12-13 echo &quot;I left my system on at least once \
at lunch time this week.&quot;

# run every Sunday and Saturday at 9:05
5 9 * * sat,sun echo &quot;Good morning Thibault!&quot;

# run every even days of march at 18:00, except on 16th
0 18 2-30/2~16 Mar * echo &quot;It's time to go back home!&quot;

# the line above is equivalent to
&amp; 0 18 2-30/2~16 Mar * echo &quot;It's time to go back home!&quot;

# reset options to default and set runfreq for lines below
!reset,runfreq(7)

# run once every 7 matches (thanks to the declaration above),
# so if system is running every day at 10:00, this will be
# run once a week
&amp; 0 10 * * * echo &quot;if you got this message last time 7 days ago,\
this computer has been running every day at 10:00 last week.\
If you got the message 8 days ago, then the system has been down \
one day at 10:00 since you got it, etc&quot;

# wait every hour for a 5 minutes load average under 0.9
@lavg5(0.9) 1h echo &quot;The system load average is low&quot;

# wait a maximum of 5 hours every day for a fall of the load average
@lavgand,lavg(1,2.0,3.0),until(5h) 1d echo &quot;Load average is going down&quot;

# wait for the best moment to run a heavy job
@lavgor,lavg(0.8,1.2,1.5),nice(10) 1w echo &quot;This is a heavy job&quot;

# run once every night between either 21:00 and 23:00 or
#   between 3:00 and 6:00
%nightly,lavg(1.5,2,2) * 21-23,3-6 echo &quot;It's time to retrieve \
the latest release of Mozilla!&quot;</code></pre>
<h2>Files</h2>
<dl>
<dt><i>/usr/local/etc/fcron.conf</i></p>
<dd>Configuration file for <code>fcron</code>, <code>fcrontab</code> and <code>fcrondyn</code>: contains paths (spool dir, pid file) and default programs to use (editor, shell, etc). See <code><a href="/docs/linux/man/5-fcron-conf/">fcron.conf</a></code>(5) for more details.</p>
<dt><i>/usr/local/etc/fcron.allow</i></p>
<dd>Users allowed to use <code>fcrontab</code> and <code>fcrondyn</code> (one name per line, special name &quot;all&quot; acts for everyone)</p>
<dt><i>/usr/local/etc/fcron.deny</i></p>
<dd>Users who are not allowed to use <code>fcrontab</code> and <code>fcrondyn</code> (same format as allow file)</p>
<dt><i>/usr/local/etc/pam.d/fcron</i><code> (or </code><i>/usr/local/etc/pam.conf</i><code>)</code></p>
<dd>PAM configuration file for <code>fcron</code>. Take a look at <a href="/docs/linux/man/8-pam/">pam</a>(8) for more details.</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-fcrontab/">fcrontab</a></code>(1), </p>
<p> <code><a href="/docs/linux/man/1-fcrondyn/">fcrondyn</a></code>(1), </p>
<p> <code><a href="/docs/linux/man/5-fcrontab/">fcrontab</a></code>(5), </p>
<p> <code><a href="/docs/linux/man/5-fcron-conf/">fcron.conf</a></code>(5), </p>
<p> <code><a href="/docs/linux/man/8-fcron/">fcron</a></code>(8). </p>
<p> If you&#8217;re learning how to use fcron from scratch, I suggest that you read the HTML version of the documentation (if your are not reading it right now! :) ): the content is the same, but it is easier to navigate thanks to the hyperlinks.</p>
<h2>Author</h2>
<p>Thibault Godouet &lt;fcron [at] free.fr&gt;</p>
