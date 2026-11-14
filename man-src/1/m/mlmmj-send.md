---
title: "mlmmj-send(1)"
name: "mlmmj-send"
section: "1"
letter: "m"
url: "/docs/linux/man/1-mlmmj-send/"
description: "mlmmj-send – send mail to a mailinglist or similar"
---

<h2>NAME</h2>
<p> mlmmj-send &#8211; send mail to a mailinglist or similar</p>
<h2>SYNOPSIS</h2>
<p> <code>mlmmj-send</code> [<i>-L</i> /path/to/list | <i>-l</i> listctrl] <i>-m</i> /path/to/mail [<i>-a</i>] [<i>-D</i>] [<i>-F</i>] [<i>-h</i>] [<i>-o</i>] [<i>-r</i>] [<i>-R</i>] [<i>-s</i>] [<i>-T</i>] [<i>-V</i>]</p>
<dl>
<dt> <code>-a</code>: Don&#8217;t archive the mail</p>
<dt> <code>-D</code>: Don&#8217;t delete the mail after it&#8217;s sent</p>
<dt> <code>-F</code>: What to use as MAIL FROM:</p>
<dt> <code>-h</code>: This help</p>
<dt> <code>-l</code>: List control variable.</p>
<dt> <code>-L</code>: Full path to list directory</p>
<dt> <code>-m</code>: Full path to mail file</p>
<dt> <code>-o</code>: Address to omit from distribution (normal mail only)</p>
<dt> <code>-r</code>: Relayhost IP address (defaults to 127.0.0.1)</p>
<dt> <code>-R</code>: What to use as Reply-To: header</p>
<dt> <code>-s</code>: Subscribers file name</p>
<dt> <code>-T</code>: What to use as RCPT TO:</p>
<dt> <code>-V</code>: Print version</dl>
<h2>DESCRIPTION</h2>
<dd>This binary is used to send all kinds of mail to mlmmj managed mailinglists, but can potentially be used standalone for sending mails. </p>
<p> The only option that is not self explanatory is the <code>-l</code> list control option:</p>
<dl>
<dt>
<dd> &#8216;1&#8217; means &#8216;send a single mail&#8217; </p>
<p> This is used together with <code>-F</code> and <code>-T</code> to send one mail to one recipient. </p>
<p> &#8216;2&#8217; means &#8216;mail to moderators&#8217; </p>
<p> Used for sending mails to the moderators of a list. </p>
<p> &#8216;3&#8217; means &#8216;resend failed list mail&#8217; </p>
<p> &#8216;4&#8217; means &#8216;send to file with recipients&#8217; </p>
<p> &#8216;5&#8217; means &#8216;bounceprobe&#8217; </p>
<p> &#8216;6&#8217; means &#8216;single listmail to single recipient&#8217; </p>
</dl>
<h2>BUGS</h2>
<p> This manual page is very scarce documentation of the mlmmj-send binary. The reason for this is that it&#8217;s really not supposed to be used by any human, but only supposed to be invoked from other mlmmj binaries. So in case more documentation is needed, please read the source.</p>
<h2>AUTHORS</h2>
<p> This manual page was written by the following persons:</p>
<dl>
<dt>
<dd>S&oslash;ren Boll Overgaard &lt;boll [at] debian.org&gt; (based on html2man output)</p>
<dt>
<dd>Mads Martin J&oslash;rgensen &lt;mmj [at] mmj.dk&gt; </p>
</dl>
<h2>Index</h2>
