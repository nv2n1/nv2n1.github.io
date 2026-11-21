---

title: "foomatic-printjob(1)"
name: "foomatic-printjob"
section: "1"
letter: "f"
url: "/docs/linux/man/1-foomatic-printjob/"
description: "foomatic-printjob – manage printer jobs in a spooler-independent fashion"
---

<h2>NAME</h2>
<p> foomatic-printjob &#8211; manage printer jobs in a spooler-independent fashion</p>
<p> <code>foomatic-printjob [ -s spooler ] [ -P queuename ] </code> <code>[ -o option1=value1 -o option2 &#8230; ] [ -i ] </code> <code>[ file1 file2 &#8230; ]</code> </p>
<p> <code>foomatic-printjob -Q [ -s spooler ] [ -P queuename ] [ -i ] [ -a ]</code> <code>[ user1 user2 &#8230; ]</code> </p>
<p> <code>foomatic-printjob -R [ -s spooler ] [ -P queuename ] [ -i ] </code> <code>[ &#8211; | jobid1 jobid2 &#8230; ]</code> </p>
<p> <code>foomatic-printjob -C [ -s spooler ] [ -i ] command [ arguments ]</code> </p>
<p> <code>foomatic-printjob -S [ -s spooler ] [ -i ]</code> </p>
<p> <code>foomatic-printjob -h [ -s spooler ] [ -P queuename ] [ -i ]</code> </p>
<p> <code>foomatic-printjob</code> provides a spooler-independent interface to creating and managing printer jobs and print queues. Note that the first argument changes the mode of the command, as it combines the functionality of several System V-style printing commands. </p>
<h3>OPTIONS</h3>
<dl>
<dt><code>-s</code><i>spooler</i></dt>
<dd> Explicit spooler type. </dd>
<dt><code>-P</code><i>queuename</i></dt>
<dd> Any commands specified should apply to this queue instead of the default. </dd>
<dt><code>-o</code><i>option=value</i></dt>
<dd> Set option to value </dd>
<dt><code>-o</code><i>option</i></dt>
<dd> Set the switch option </dd>
<dt><code>-#</code><i>n</i></dt>
<dd> Print n copies </dd>
<dt><code>file1&nbsp;<wbr>&nbsp;<wbr>file2&nbsp;<wbr>&nbsp;<wbr>&#8230;</code></dt>
<dd> Files to be printed, when no file is given, standard input will be printed </dd>
<dt><code>-Q</code></dt>
<dd> Query the jobs in a queue. If a list of users is specified, only those users&#8217; jobs will be queried. </dd>
<dt><code>-Q -a</code></dt>
<dd> Query the jobs in all queues. If a list of users is specified, only those users&#8217; jobs will be queried. </dd>
<dt><code>-R&nbsp;<wbr>[&nbsp;<wbr>&#8211; | jobid1 jobid2 &#8230;&nbsp;<wbr>]</code></dt>
<dd> Remove a job from a queue. Using <i>&#8211;</i> will remove all jobs. </dd>
<dt><code>-C command&nbsp;<wbr>[&nbsp;<wbr>arguments&nbsp;<wbr>]</code></dt>
<dd> Execute control commands for queue/job manipulation. The commands are the ones of the BSD &quot;lpc&quot; utility. Use the control command &quot;help&quot; to get a list of supported commands. Note: the amount of commands varies with the spooler, but the same commands given under different spoolers do the same thing. </dd>
<dt><code>-i</code></dt>
<dd> Interactive mode: You will be asked if foomatic-printjob is in doubt about something. Otherwise foomatic-printjob uses auto-detection or quits with an error. </dd>
<dt><code>-S</code></dt>
<dd> Save the chosen spooler as the default spooler </dd>
<dt><code>-h</code></dt>
<dd> Show this message or show a list of available options if a queue is specified </dd>
</dl>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-foomatic-configure/">foomatic-configure</a>(1) and the documentation for your print spooler. </p>
<h2>AUTHOR</h2>
<p> Manfred Wassmann &lt;<i>manolo [at] NCC-1701.B.Shuttle.de</i>&gt; and Chris Lawrence &lt;<i>lawrencc [at] debian.org</i>&gt; for the foomatic project using output from the associated binary. </p>
<h2>BUGS</h2>
<p> This manpage still needs some editing. </p>
