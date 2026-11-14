---
title: "lockfile(1)"
name: "lockfile"
section: "1"
letter: "l"
url: "/docs/linux/man/1-lockfile/"
description: "lockfile – conditional semaphore-file creator"
---

<h2 class="name">NAME</h2>
<p> lockfile &#8211; conditional semaphore-file creator </p>
<h2>SYNOPSIS</h2>
<p> <code>lockfile</code> <i></i><code>&#8211;</code>sleeptime | <i></i><code>-r </code>retries |<br />
 &nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp; <i></i><code>-l </code>locktimeout | <i></i><code>-s </code>suspend | <code>-!</code> | <code>-ml</code> | <code>-mu</code> | <i>filename</i> &#8230; </p>
<h2>DESCRIPTION</h2>
<p> <code>lockfile</code> can be used to create one or more <i>semaphore</i> <i>files</i>. If lockfile can&#8217;t create all the specified files (in the specified order), it waits <i>sleeptime</i> (defaults to 8) seconds and retries the last file that didn&#8217;t succeed. You can specify the number of <i>retries</i> to do until failure is returned. If the number of <i>retries</i> is -1 (default, i.e., <code>-r-1</code>) lockfile will retry forever. </p>
<p> If the number of <i>retries</i> expires before all files have been created, lockfile returns failure and removes all the files it created up till that point. </p>
<p> Using lockfile as the condition of a loop in a shell script can be done easily by using the <code>-!</code> flag to invert the exit status. To prevent infinite loops, failures for any reason other than the lockfile already existing are not inverted to success but rather are still returned as failures. </p>
<p> All flags can be specified anywhere on the command line, they will be processed when encountered. The command line is simply parsed from left to right. </p>
<p> All files created by lockfile will be read-only, and therefore will have to be removed with <code>rm</code> <code>-f</code>. </p>
<p> If you specify a <i>locktimeout</i> then a lockfile will be removed by force after locktimeout seconds have passed since the lockfile was last modified/created (most likely by some other program that unexpectedly died a long time ago, and hence could not clean up any leftover lockfiles). Lockfile is clock skew immune. After a lockfile has been removed by force, a suspension of <i>suspend</i> seconds (defaults to 16) is taken into account, in order to prevent the inadvertent immediate removal of any newly created lockfile by another program (compare <code>SUSPEND</code> in <code><a href="/docs/linux/man/1-procmail/">procmail</a></code>(1)). </p>
<h3>Mailbox locks</h3>
<p> If the permissions on the system mail spool directory allow it, or if lockfile is suitably setgid, it will be able to lock and unlock your system mailbox by using the options <code>-ml</code> and <code>-mu</code> respectively. </p>
<h2>EXAMPLES</h2>
<p> Suppose you want to make sure that access to the file &quot;important&quot; is serialised, i.e., no more than one program or shell script should be allowed to access it. For simplicity&#8217;s sake, let&#8217;s suppose that it is a shell script. In this case you could solve it like this: </p>
<pre>
<dl><dt><dd>...
lockfile important.lock
...
access_&quot;important&quot;_to_your_hearts_content
...
rm -f important.lock
...
</dl>
</pre>
<p> Now if all the scripts that access &quot;important&quot; follow this guideline, you will be assured that at most one script will be executing between the `lockfile&#8217; and the `rm&#8217; commands. </p>
<h2>ENVIRONMENT</h2>
<p> Tp 2.3i <code>LOGNAME</code> used as a hint to determine the invoker&#8217;s loginname </p>
<h2>FILES</h2>
<p> Tp 2.3i <code>/etc/passwd</code> to verify and/or correct the invoker&#8217;s loginname (and to find out his HOME directory, if needed)<br />
 Tp <code>/var/mail/$LOGNAME.lock</code> lockfile for the system mailbox, the environment variables present in here will not be taken from the environment, but will be determined by looking in /etc/passwd </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-rm/">rm</a></code>(1), <code><a href="/docs/linux/man/1-mail/">mail</a></code>(1), <code><a href="/docs/linux/man/8-sendmail/">sendmail</a></code>(8), <code><a href="/docs/linux/man/1-procmail/">procmail</a></code>(1) </p>
<h2>DIAGNOSTICS</h2>
<p> Tp 2.3i Filename too long, &#8230; Use shorter filenames.<br />
 Tp Forced unlock denied on &quot;x&quot; No write permission in the directory where lockfile &quot;x&quot; resides, or more than one lockfile trying to force a lock at exactly the same time.<br />
 Tp Forcing lock on &quot;x&quot; Lockfile &quot;x&quot; is going to be removed by force because of a timeout (compare <code>LOCKTIMEOUT</code> in <code><a href="/docs/linux/man/1-procmail/">procmail</a></code>(1)).<br />
 Tp Out of memory, &#8230; The system is out of swap space.<br />
 Tp Signal received, &#8230; Lockfile will remove anything it created till now and terminate.<br />
 Tp Sorry, &#8230; The <i>retries</i> limit has been reached.<br />
 Tp Truncating &quot;x&quot; and retrying lock &quot;x&quot; does not seem to be a valid filename.<br />
 Tp Try praying, &#8230; Missing subdirectories or insufficient privileges. </p>
<h2>BUGS</h2>
<p> Definitely less than one. </p>
<h2>WARNINGS</h2>
<p> The behavior of the <code>-!</code> flag, while useful, is not necessarily intuitive or consistent. When testing lockfile&#8217;s return value, shell script writers should consider carefully whether they want to use the <code>-!</code> flag, simply reverse the test, or do a switch on the exact exitcode. In general, the <code>-!</code> flag should only be used when lockfile is the conditional of a loop. </p>
<h2>MISCELLANEOUS</h2>
<p> Lockfile is NFS-resistant and eight-bit clean. </p>
<h2>NOTES</h2>
<p> Calling up lockfile with the -h or -? options will cause it to display a command-line help page. Calling it up with the -v option will cause it to display its version information. </p>
<p> Multiple <code>-!</code> flags will toggle the return status. </p>
<p> Since flags can occur anywhere on the command line, any filename starting with a &#8216;-&#8216; has to be preceded by &#8216;./&#8217;. </p>
<p> The number of <i>retries</i> will not be reset when any following file is being created (i.e., they are simply used up). It can, however, be reset by specifying -r<i>newretries</i> after every file on the command line. </p>
<p> Although files with any name can be used as lockfiles, it is common practice to use the extension `.lock&#8217; to lock mailfolders (it is appended to the mailfolder name). In case one does not want to have to worry about too long filenames and does not have to conform to any other lockfilename convention, then an excellent way to generate a lockfilename corresponding to some already existing file is by taking the prefix `lock.&#8217; and appending the i-node number of the file which is to be locked.</p>
<h2>SOURCE</h2>
<p> This program is part of the <i>procmail mail-processing-package</i> (v3.23pre) available at <a rel="nofollow" href="http://www.procmail.org/">http://www.procmail.org/</a> or <a href="ftp://ftp.procmail.org">ftp.procmail.org</a> in <code>pub/procmail/</code>.</p>
<h2>MAILINGLIST</h2>
<p> There exists a mailinglist for questions relating to any program in the procmail package: </p>
<pre>
<dl><dt><dd>&lt;procmail-users [at] procmail.org&gt;
<dl><dt><dd>for submitting questions/answers.
</dl>
</pre>
<p> &lt;procmail-users-request [at] procmail.org&gt; </p>
<pre>
<dl><dt><dd>for subscription requests.
</dl>
</pre>
</dl>
<p> If you would like to stay informed about new versions and official patches send a subscription request to </p>
<pre>
<dl><dt><dd>procmail-announce-request [at] procmail.org
</dl>
</pre>
<p> (this is a readonly list). </p>
<h2>AUTHORS</h2>
<p> Stephen R. van den Berg </p>
<pre>
<dl><dt><dd>&lt;srb [at] cuci.nl&gt;
</dl>
</pre>
<p> Philip A. Guenther </p>
<pre>
<dl><dt><dd>&lt;guenther [at] sendmail.com&gt;
</dl>
</pre>
<h2>Index</h2>
