---
title: "mlmmj-bounce(1)"
name: "mlmmj-bounce"
section: "1"
letter: "m"
url: "/docs/linux/man/1-mlmmj-bounce/"
description: "mlmmj-bounce – bounce handling utility for mlmmj"
---

<h2>NAME</h2>
<p> mlmmj-bounce &#8211; bounce handling utility for mlmmj</p>
<h2>SYNOPSIS</h2>
<p> <code>mlmmj-bounce</code> <i>-L /path/to/list </i>[<i>-a john=doe.org | -d</i>]<i> </i>[<i>-n num | -p</i>]</p>
<dl>
<dt> <code>-a</code>: Address string that bounces</p>
<dt> <code>-d</code>: Parse the mail to extract the address via the DSN (RFC1891)</p>
<dt> <code>-h</code>: This help</p>
<dt> <code>-L</code>: Full path to list directory</p>
<dt> <code>-n</code>: Message number in the archive that bounced</p>
<dt> <code>-p</code>: Send out a probe</p>
<dt> <code>-V</code>: Print version</dl>
<h2>DESCRIPTION</h2>
<dd>mlmmj-bounce is used to handle mails that are bouncing. When a mail arrives to the system, mlmmj-bounce will register in &lt;listdir&gt;/bounce/&lt;addrstring&gt; info about which number that bounced at what time. An example of such a line could be: </p>
<p> 109:1094409801 # Sun Sep 5 20:43:21 2004 </p>
<p> The above shows that message number 109 bounced 1094409801 seconds after epoch which is in human date stamps is Sunday September 5th 20:43:21 2004. </p>
<p> The last bounce mail received to the address is saved in &lt;listdir&gt;/bounce/&lt;addrstring&gt;.lastmsg. </p>
<p> When the <code>-p</code> option is used it sends out a probe email including info that it&#8217;s a bounce probe and a list of the bounced message numbers. The existance of a &lt;listdir&gt;/bounce/&lt;addrstring&gt;.probe file indicates that a probe have been sent out.</p>
<h2>AUTHORS</h2>
<p> This manual page was written by the following persons:</p>
<dl>
<dt>
<dd>S&oslash;ren Boll Overgaard &lt;boll [at] debian.org&gt; (based on html2man output)</p>
<dt>
<dd>Mads Martin J&oslash;rgensen &lt;mmj [at] mmj.dk&gt; </p>
</dl>
<h2>Index</h2>
