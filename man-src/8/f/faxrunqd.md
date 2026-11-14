---
title: "faxrunqd(8)"
name: "faxrunqd"
section: "8"
letter: "f"
url: "/docs/linux/man/8-faxrunqd/"
description: "faxrunqd – daemon to send fax jobs queued by"
---

<p>faxrunqd &#8211; daemon to send fax jobs queued by </p>
<p><a href="/docs/linux/man/1-faxspool/">faxspool</a>(1)</p>
<h2>Synopsis</h2>
<p><code>faxrunqd [-v] [-d] [-l &lt;ttys&gt;] [-u &lt;user&gt;] [-V]</code></p>
<h2>Description</h2>
<p>Runs in the background, and regularily checks the fax queue set up by <a href="/docs/linux/man/1-faxspool/">faxspool</a>(1). Sends all jobs that are due, records results, and takes appropriate action (notify mails etc). <i>faxrunqd</i> basically does the same as <a href="/docs/linux/man/1-faxrunq/">faxrunq</a>(1), just more so. Please read the <a href="/docs/linux/man/1-faxrunq/">faxrunq</a>(1) man page if you&#8217;re not already familiar with the concept. The advantages of <i>faxrunqd</i> are: &#8211; runs all the time, so you don&#8217;t have to set up a cron job (but you have to set up an entry in /etc/inittab or start it from /etc/rc*) &#8211; quicker response to new faxes in queue &#8211; can sensibly handle more than one modem &#8211; can handle prioritized fax jobs &#8211; can do &#8216;policy routing&#8217; of faxes depending on the fax number The disadvantages are: &#8211; needs more system ressources if you have only little fax traffic &#8211; requires Perl 5.004 &#8211; more tricky to set up and to debug </p>
<h2>Setup</h2>
<p><i>faxrunqd</i> is started at system boot from /etc/rc.*, or from /etc/inittab. You can also start it from the command line. It does <code>not</code> put itself in the background, so you have to start it with an &quot;&amp;&quot;, or from a &quot;:respawn:&quot; line in /etc/inittab. Using /etc/inittab has the advantage that <i>faxrunqd</i> is restarted automatically if something goes wrong and faxrunqd is stopped. </p>
<p> <i>faxrunqd</i> will first read a global configuration file (see below), then (optionally) the faxrunqd policy file (see further below). From then on, it will sit in a loop. It will check the fax queue every 60 seconds for new jobs, and will then distribute them over all available modems. If the job is sent, or fails, it will do the same thing <i><a href="/docs/linux/man/1-faxrunq/">faxrunq</a>(1)</i> would do (send a mail, delete the JOB directory, execute a named program, etc.). Both programs are fully compatible in this respect. </p>
<p> <code>faxrunqd [-v] [-d] [-l &lt;ttys&gt;] [-u &lt;user&gt;] [-V]</code></p>
<h2>Options</h2>
<dl>
<dt><code>-v</code></p>
<dd>Tells <i>faxrunqd</i> to write progress information to the log file.</p>
<dt><code>-d</code></p>
<dd>Tells <i>faxrunqd</i> to write debugging information to stdout and the log file (usually used together with -v)</p>
<dt><code>-l &lt;ttyS&gt;</code></p>
<dd>Specifies the list of modem devices to use. Multiple devices are separated with &#8216;:&#8217;, e.g. &#8216;-l ttyS0:ttyS1&#8217;.</p>
<dt><code>-u &lt;user&gt;</code></p>
<dd><i>faxrunqd</i> can now (since 1.1.29) run as unprivileged user. If you start it as root from /etc/inittab or from one of the /etc/rc* scripts, it&#8217;s strongly recommended to use &#8216;-u fax&#8217; (to be precise: the user that is owning the outgoing fax spool directory). This will make <i>faxrunqd</i> drop all its privileges at startup, and run as the specified user. Running <i>faxrunqd</i> as root user might lead to security problems &#8211; don&#8217;t do it.</p>
<dt><code>-V</code></p>
<dd>print version number and exit </p>
</dl>
<h2>Configuration File</h2>
<p>Some aspects of the behaviour of <i>faxrunqd</i> can be controlled by a configuration file, usually named /etc/mgetty+sendfax/faxrunq.config (this is the same file that <i><a href="/docs/linux/man/1-faxrunq/">faxrunq</a>(1)</i> uses, but there are additional options for <i>faxrunqd). In</i> this file, you can use the following options:</p>
<dl>
<dt><code>success-send-mail [y/n]</code></p>
<dd>A boolean parameter that controls whether a mail will be sent after successful completition of the fax job. </p>
<dt><code>failure-send-mail [y/n]</code></p>
<dd>A boolean parameter that controls whether a mail will be sent after the fax job has failed more than the maximum number of times. </p>
<dt><code>success-call-program &lt;name&gt;</code></p>
<dd>Here, you can specify a program that will be run when the fax has been successfully sent. It will be passed two command line parameters. The first is the full path to the fax JOB file (see <a href="/docs/linux/man/5-faxq/">faxq</a>(5)), the second is the last exit code from <i>sendfax</i> (for success-call-program, this is always &quot;0&quot;). </p>
<dt><code>failure-call-program &lt;name&gt;</code></p>
<dd>Similar to the &quot;success-call-program&quot;, this program will be run when the fax has been failed too often and <i>faxrunqd</i> gives up. This script could, for example, print out the fax on a printer so that it can be sent manually on a paper fax machine. </p>
<dt><code>update-call-program &lt;name&gt;</code></p>
<dd>This is, again, similar to &quot;success-call-program&quot;. It will be called for interim status updates (&quot;we&#8217;ve tried and it was BUSY&quot;), so that frontend programs can display this information. &quot;update-call-program&quot; will only be called for jobs that will be <i>kept</i> in the fax queue for at least one more try. </p>
<dt><code>maxfail-costly &lt;n&gt;</code></p>
<dd>This specifies the number of times that a fax may fail &quot;fatally&quot;, that is, causing telephone costs (explained above). The default value is 5. </p>
<dt><code>maxfail-total &lt;m&gt;</code></p>
<dd>This is the absolute maximum number of times that <i>faxrunqd</i> will try to send any given fax. The default value is 10. </p>
<dt><code>delete-sent-jobs [y/n]</code></p>
<dd>Determines whether <i>faxrunqd</i> should delete jobs after sending, or leave them in the fax queue (while moving the &quot;JOB&quot; file to &quot;JOB.done&quot;) so that they can be seen at by &quot;faxq -o&quot;. The default value is &quot;do not delete sent faxes&quot;. </p>
<dt><code>acct-log &lt;path&gt;</code></p>
<dd>Specifies where <i>faxrunqd</i> should protocol success and failure of each try to send a fax job. The default location is /var/spool/fax/outgoing/acct.log. </p>
</dl>
<p> The options that are specific to <i>faxrunqd</i> are: </p>
<dl>
<dt><code>fax-devices [tty(s)]</code></p>
<dd>Specifies which ttys should be used for sending jobs. <i>faxrunqd</i> will always explicitely tell <i>sendfax</i> which modem to use, so the settings in sendfax.config are ignored. If you use policy routing (see below), this applies only to fax jobs that do not have a tty set by faxrunqd.policy. </p>
<dt><code>faxrunqd-log [filename]</code></p>
<dd>Specifies where logging information is written to. This is only used if <i>faxrunqd</i> is called with the <code>-v</code> or <code>-d</code> option. </p>
<dt><code>policy-config [filename]</code></p>
<dd>Specifies a file containing rules for &quot;policy routing&quot;, see below. Default is &quot;no file&quot;. </p>
<dt><code>faxrunqd-max-pages [n]</code></p>
<dd>If this is set to something greater 1 (default is 10), <i>faxrunqd</i> will combine multiple jobs to the same receipient telephone number into one telephone call. The maximum number of pages that the resulting job may have is specified here. Usually it makes no sense to increase this, but in some surroundings it might make sense to turn off this feature by setting it to 1. </p>
<dt><code>sendfax-tty-map [tty] [program path] [args]</code></p>
<dd>Some special cases might require running a non-default <i>sendfax</i> binary for specific ttys (like &quot;testing new version&quot; or &quot;some other call-compatible sendfax applications for non-class-2 modems&quot;). If you want mappings for more than one &quot;special&quot; tty devices, just use the option multiple times. Example: </p>
<p> sendfax-tty-map capi0 /usr/sbin/sendfax.capi </p>
<dt><code>queue-length-high [number] [program path] [args]</code></p>
<dd>run the specified command when the number of jobs in the fax queue exceeds <i>number</i> (this could be used to send out a warning by syslog or e-mail when too many modems fail on a busy system, and faxes get stuck). The script will be run only once, unless the queue length falls below the &#8220;low water mark&#8221; threshold and rises again later on. </p>
<dt><code>queue-length-low [number] [program path] [args]</code></p>
<dd>run the specified command when the queue length has been over the &#8220;high water&#8221; threshold, and is back below this number. This can be used to send &#8220;everything is back to normal&#8221; e-mails, or just to reset the alarm threshold. </p>
<dt><code>modem-error-threshold [number] [program path] [args]</code></p>
<dd>this script is called whenever a given modem has more than <i>number</i> consecutive errors. Every successfully sent fax always resets the counter for a given modem to 0. This can be used to notify the sysadmin when a modem breaks (by default, <i>faxrunqd</i> just phases out a problematic modem, but will not report the problem). </p>
</dl>
<h2>Policy Routing</h2>
<p><i>faxrunqd</i> can do some things differently, depending on the phone number where the fax is supposed to be sent to. For example, this might be useful to: </p>
<p> &#8211; send in-house faxes over a specific modem connected to a PABX (to avoid paying telco charges) </p>
<p> &#8211; send long-distance faxes to the US over a special LD provider, that is, use a specific dial-prefix for those </p>
<p> &#8211; use extra high debugging when sending to a known-to-be problematic receipient </p>
<p> etc. </p>
<p> This feature is controlled by a file, containing match / substitute rules. The name of the file is specified with the &quot;policy-config&quot; option in faxrunq.config. </p>
<p> The file is read from top to bottom. Each line starting with a &quot;#&quot; sign is a comment, and is skipped. In every other line, the first field of the line is interpreted as a &quot;match&quot; clause, and compared to the telefone number of an to-be-sent fax job. Regular expressions can be used (see <a href="/docs/linux/man/1-perlre/">perlre</a>(1)). </p>
<p> If the telefone number is matched, the second field is used to substitute parts of the telefone number, for example, cut off a local prefix, or change a digit, or whatever. If you do not want any substitutions, put a &quot;-&quot; in that field. </p>
<p> The third field specifies the tty lines to use for faxes matched by this line (for example, you might have one modem connected to a long-distance provider, and others for local use or so). Put a &quot;-&quot; in this field if you want to use the default fax modems. </p>
<p> The remaining part of the line are appended to the sendfax command line. With those, you can set a different dial-string (&quot;-D ATD&quot;), or a higher debug level (&quot;-x 9&quot;), or whatever else you can imagine. Do NOT set a tty to use here (&quot;-l ttyS1&quot;), because that would confuse the internal tty handling of <i>faxrunqd,</i> leading to weird effects processing the fax queue!! </p>
<p> Examples: </p>
<p> # 12345-nnn is sent to &quot;nnn&quot; over a local PABX, modem on tty2 </p>
<p> ^12345<tt>&nbsp;<wbr>&nbsp;<wbr></tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>s/12345//<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>tty2</p>
<p> # fax to 56789 (exact match) is sent with higher debugging </p>
<p> ^56789$<tt>&nbsp;<wbr></tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>&#8211;<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>&#8211;<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>-x 8</p>
<h2>Files</h2>
<dl>
<dt><code>/var/spool/fax/outgoing/stop</code></p>
<dd>if this file exists, <i>faxrunqd</i> will stop whatever it&#8217;s doing at the moment, wait for all outstanding jobs, and then fall asleep until the file is removed. You can use this to stop queue processing while testing something, or if you know that the modem(s) are unavailable and do not want to run into any error messages, etc. </p>
<dt><code>/var/spool/fax/outgoing/faxqueue_done</code></p>
<dd>Every time <i>faxrunqd</i> runs the fax queue, a time stamp is written into that file. It is used by <i>faxspool</i> to display a warning if the queue hasn&#8217;t been run recently (so faxes may get stuck). </p>
</dl>
<h2>Signals</h2>
<p>To control <i>faxrunqd&#8217;s </i> behaviour, you can send it the following signals: </p>
<dl>
<dt><code>SIGINT</code></p>
<dd>
<dt><code>SIGTERM</code></p>
<dd>remove lock file, remove pid file, terminate immediately. </p>
<dt><code>SIGHUP</code></p>
<dd>finish all fax jobs that are currently being sent, then terminate (this is used to signal faxrunqd &quot;I want you to terminate&quot; without disturbing the normal flow of operation &#8211; SIGINT/TERM etc. can lead to some faxes being sent twice). </p>
<dt><code>SIGUSR1</code></p>
<dd>close, roll, and re-open log file. </p>
<dt><code>SIGUSR2</code></p>
<dd>dump current modem success/failure statistics to log file. </p>
</dl>
<h2>Bugs</h2>
<p><i>faxrunqd</i> does not report if a modem goes bad &#8211; instead it will just stop using it (which is good for reliable faxing, but bad for error recovery). </p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/1-faxspool/">faxspool</a>(1), <a href="/docs/linux/man/8-sendfax/">sendfax</a>(8), <a href="/docs/linux/man/1-faxq/">faxq</a>(1), <a href="/docs/linux/man/1-faxrunq/">faxrunq</a>(1), <a href="/docs/linux/man/5-faxqueue/">faxqueue</a>(5)</p>
<h2>Author</h2>
<p><i>faxrunqd</i> is Copyright (C) 1997-2004 by Gert Doering, &lt;gert [at] greenie.muc.de&gt;. It was inspired by Bodo Bauer&#8217;s initial faxrunqd, but completely rewritten.</p>
