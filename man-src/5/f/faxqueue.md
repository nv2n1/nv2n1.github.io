---
title: "faxqueue(5)"
name: "faxqueue"
section: "5"
letter: "f"
url: "/docs/linux/man/5-faxqueue/"
description: "faxqueue – sendfax fax spool queue control files"
---

<p>faxqueue &#8211; sendfax fax spool queue control files</p>
<h2>Synopsis</h2>
<p><code>/var/spool/fax/outgoing/F*/JOB</code></p>
<h2>Description</h2>
<p>The <i>JOB</i> files in the subdirectories of the outgoing fax spool directory, <i>/var/spool/fax/outgoing</i> build up a queue of faxes to be sent by <a href="/docs/linux/man/1-faxrunq/">faxrunq</a>(1). They are created by <a href="/docs/linux/man/1-faxspool/">faxspool</a>(1), can be viewed with <a href="/docs/linux/man/1-faxq/">faxq</a>(1), and be deleted by <a href="/docs/linux/man/1-faxrm/">faxrm</a>(1). </p>
<h2>Format</h2>
<p>The format of the JOB file is as follows: </p>
<p> Each line consists of a leading keyword and associated data (rest of the line). Some are required, some others are optional. The currently implemented keywords are:</p>
<dl>
<dt><code>phone &lt;number&gt;</code></p>
<dd>The telephone number to send the fax to. Required.</p>
<dt><code>user &lt;user&gt;</code></p>
<dd>The originating user name (on the local machine). If no &quot;mail&quot; field is present, this user will get the status mail about the fax. Required.</p>
<dt><code>mail &lt;email&gt;</code></p>
<dd>If this field is present, <a href="/docs/linux/man/1-faxrunq/">faxrunq</a>(1) will send its status mail to the address given here. If not, <a href="/docs/linux/man/1-faxrunq/">faxrunq</a>(1) will use the &quot;user&quot; field. Optional.</p>
<dt><code>input &lt;file(s)&gt;</code></p>
<dd>The file names passed to <a href="/docs/linux/man/1-faxspool/">faxspool</a>(1). Optional, used only by <a href="/docs/linux/man/1-faxq/">faxq</a>(1).</p>
<dt><code>pages &lt;file(s)&gt;</code></p>
<dd>The file names, relative to the directory where the JOB file is found, that are to be sent with <a href="/docs/linux/man/8-sendfax/">sendfax</a>(8). The files have to exist, and be readable by the user that runs <a href="/docs/linux/man/1-faxrunq/">faxrunq</a>(1). Required, except if &quot;poll&quot; is used, then it&#8217;s optional.</p>
<dt><code>priority &lt;0-9&gt;</code></p>
<dd>This can be used to set the priority for this job in the fax queue (higher priority jobs get sent before all lower-pri jobs). So far, only <i>faxrunqd</i> uses this field, <i>faxrunq</i> does NOT. 9 is the highest, 0 the lowest priority. 5 is the default.</p>
<dt><code>Status &lt;message&gt;</code></p>
<dd>Automatically appended by <a href="/docs/linux/man/1-faxrunq/">faxrunq</a>(1) after each run, tells the reader about successful and unsuccessful tries to send this job. If more than five &quot;FATAL&quot; errors are listed, the fax job is removed from the queue.</p>
<dt><code>verbose_to &lt;blurb&gt;</code></p>
<dd>A plain-text description of the receiver of the fax. Is returned, if present, in the mail messages &quot;your fax to &lt;blurb&gt;&quot;. Optional.</p>
<dt><code>time &lt;hhmm&gt;</code></p>
<dd>If present, <i>faxrunq</i> won&#8217;t send this job before the given time. The format must be exactly &quot;hhmm&quot;, in 24-hr-format, otherwise faxrunq won&#8217;t understand it. Optional.</p>
<dt><code>poll</code></p>
<dd>Flag token. If present, faxrunq will try to poll the given phone number for documents (see &quot;sendfax -p&quot;).</p>
<dt><code>normal_res</code></p>
<dd>Flag token. If present, faxrunq will transmit all pages using normal resolution (see &quot;sendfax -n&quot;).</p>
<dt><code>acct_handle &lt;arbitrary string&gt;</code></p>
<dd>This is a pure comment field, but <a href="/docs/linux/man/8-sendfax/">sendfax</a>(8) will log it into its transaction log file. So this can be used as a customer handle, a job number, whatever you need to get the phone bills charged to the customer (the programs won&#8217;t look at it, just pass it through). Optional.</p>
<dt><code>subject &lt;arbitrary string&gt;</code></p>
<dd>This is also a pure comment field, used only for informational purposes. <i>faxrunq</i> will return it in the sucess/failure mail. If you use <i>faxspool -s &lt;subj&gt;,</i> it will put this string on the cover page and in the JOB file. </p>
</dl>
<h2>Permissions</h2>
<p>Starting with mgetty 1.1.29, the fax spool directory /var/spool/fax/outgoing is no longer world-writeable. It should be owned by the user &#8216;fax&#8217; and be mode 755. The <a href="/docs/linux/man/1-faxrunq/">faxrunq</a>(1) and <a href="/docs/linux/man/1-faxrunqd/">faxrunqd</a>(1) programs should also be run under that user ID if possible. </p>
<p> If the fax spool directory is world- or group-writeable, there are a number of denial of service or file overwrite / file access attacks possible that it&#8217;s very hard to guard against. So don&#8217;t do this! </p>
<p> If the fax spool directory has the proper permissions, there are currently no known attacks against faxrunq/faxrunqd, even if they run as &quot;root&quot;, but it&#8217;s always more safe to run as untrusted user.</p>
<h2>Processing</h2>
<p>While a given JOB file is processed by <a href="/docs/linux/man/1-faxrunq/">faxrunq</a>(1), it&#8217;s locked against sending it multiple times by temporarily renaming it to <i>JOB.locked,</i> thus it may happen that a <a href="/docs/linux/man/1-faxq/">faxq</a>(1) command doesn&#8217;t show this job. ( <i><a href="/docs/linux/man/8-faxrunqd/">faxrunqd</a>(8)</i> is a bit smarter and does the locking by creating a hard link). </p>
<p> When a job is successfully sent, it&#8217;s not deleted but the JOB file is renamed to <i>JOB.done.</i> Because of this, you can still see old jobs with &quot;faxq -o&quot;. You should regularly clean up the outgoing fax directory, removing old faxes. If you don&#8217;t want this behaviour, edit the <a href="/docs/linux/man/1-faxrunq/">faxrunq</a>(1) config file and enable the option <i>delete-sent-jobs yes</i> </p>
<p> When a job cannot be sent after several tries (excluding normal difficulties like the called number being busy or the modem being in use), the JOB file is renamed to <i>JOB.suspended.</i> To re-queue this job, call <i>faxq -r</i> &#8212; this renames the JOB file back.</p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/1-faxrunq/">faxrunq</a>(1), <a href="/docs/linux/man/1-faxspool/">faxspool</a>(1), <a href="/docs/linux/man/1-faxrm/">faxrm</a>(1), <a href="/docs/linux/man/1-faxq/">faxq</a>(1), <a href="/docs/linux/man/8-faxrunqd/">faxrunqd</a>(8) </p>
