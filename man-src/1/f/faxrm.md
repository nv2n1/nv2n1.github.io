---
title: "faxrm(1)"
name: "faxrm"
section: "1"
letter: "f"
url: "/docs/linux/man/1-faxrm/"
description: "faxrm – remove fax jobs queued by"
---

<h2 class="name">NAME</h2>
<p> faxrm &#8211; remove fax jobs queued by </p>
<p><a href="/docs/linux/man/1-faxspool/">faxspool</a>(1)</p>
<h2>SYNOPSIS</h2>
<p> <code>faxrm</code> [<code>-i</code>] [job-ids<i>&#8230;]</i></p>
<h2>DESCRIPTION</h2>
<p> Remove job(s) from the fax queue set up by <a href="/docs/linux/man/1-faxspool/">faxspool</a>(1). </p>
<p> <i>faxrm </i> removes queued fax jobs. Call with a list of job-IDs to remove specific jobs. Call with no job IDs to be asked interactively about all jobs you own (if run by root, all jobs). For job-id, use the strings returned by <a href="/docs/linux/man/1-faxq/">faxq</a>(1) (e.g. F000015), without the &#8220;/JOB&#8221; extention. </p>
<p> If you are not the owner of the fax job (as per the &#8216;user xyz&#8217; statement inside the JOB file), you are not allowed to remove the fax job. Only root is permitted to remove another user&#8217;s faxes. </p>
<p> If the job is locked (most likely because <a href="/docs/linux/man/8-sendfax/">sendfax</a>(8) is active sending it), <i>faxrm</i> doesn&#8217;t attempt to remove it. Instead, it prints a warning message on stderr and goes on to the next job. </p>
<h2>EXAMPLES</h2>
<p> faxrm F000005 F000033 </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-i</code></p>
<dd> (interactive mode) Tells <i>faxrm</i> to ask for confirmation before removing the job (UNIMPLEMENTED). </p>
</dl>
<h2>BUGS</h2>
<p> <i>faxrm</i> doesn&#8217;t return diagnostic exit codes yet. </p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-faxrunq/">faxrunq</a>(1), <a href="/docs/linux/man/8-faxrunq/">faxrunq</a>(8), <a href="/docs/linux/man/1-faxspool/">faxspool</a>(1), <a href="/docs/linux/man/1-faxq/">faxq</a>(1), <a href="/docs/linux/man/5-faxqueue/">faxqueue</a>(5)</p>
<h2>AUTHOR</h2>
<p> <i>faxrm</i> is Copyright (C) 1993-2002 by Gert Doering, &lt;gert [at] greenie.muc.de&gt;. </p>
<h2>Index</h2>
