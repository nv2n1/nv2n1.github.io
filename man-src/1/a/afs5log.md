---
title: "afs5log(1)"
name: "afs5log"
section: "1"
letter: "a"
url: "/docs/linux/man/1-afs5log/"
description: "afs5log – AFS token initializer"
---

<h2 class="name">NAME</h2>
<p> afs5log &#8211; AFS token initializer</p>
<h2>SYNOPSIS</h2>
<p> afs5log [ [-v] [-5] [-k] [-p <i>path</i>] [cell[=principal] ] ] [&#8230;] </p>
<h2>DESCRIPTION</h2>
<p> The <i>afs5log</i> command uses Kerberos to obtain AFS tokens for the named cells. If no cell is named, tokens are obtained for the local cell. If the principal name of the <i>afs</i> service for the cell is known, the cell name may also be given in the form <i>cell</i>=<i>principal_name</i>. Attempts are made to obtain Kerberos IV credentials first, and if that fails, <i>afs5log</i> will create Kerberos 5 (<i>2b-style</i>) tokens. </p>
<h2>ARGUMENTS</h2>
<dl>
<dt>-v</p>
<dd> Turns on verbose mode. <i>afs5log</i> will print debugging messages while it does its work. Use more than once to get more detail.</p>
<dt>-p <i>path</i></p>
<dd> Determine which cell the specified <i>path</i> resides in, and obtain tokens for that cell.</p>
<dt>-s <i>strategy</i></p>
<dd> Overrides the default token-setting strategy (&quot;<i>2b</i>&quot;) with the named strategy. Recognized strategy names include:<br />
&nbsp;<wbr><i>rxk5</i>&nbsp;<wbr>&nbsp;<wbr>rxk5&nbsp;<wbr>(requires OpenAFS 1.6 or later)<br />
&nbsp;<wbr><i>2b</i>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>rxkad&nbsp;<wbr>&quot;2b&quot;&nbsp;<wbr>(requires OpenAFS 1.2.8 or later)</p>
<dt>-5</p>
<dd> Skip attempts to use Kerberos IV and just use <i>2b</i>-style tokens, which are only supported by OpenAFS 1.2.8 and later.</p>
<dt>-k</p>
<dd> Skip attempts to use Kerberos IV and use <i>rxk5</i>-style tokens, which are only supported by OpenAFS 1.6 and later.</p>
<dt>-n</p>
<dd> Assume that, if a cell name and a realm name differ only by case, that the name of the AFS service&#8217;s principal name doesn&#8217;t include an instance. </p>
</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/5-pam_krb5/">pam_krb5</a></code>(5) <code><a href="/docs/linux/man/5-krb5-conf/">krb5.conf</a></code>(5) </p>
<h2>BUGS</h2>
<p> Probably, but let&#8217;s hope not. If you find any, please file them in the bug database at <a rel="nofollow" href="http://bugzilla.redhat.com/">http://bugzilla.redhat.com/</a> against the &quot;pam_krb5&quot; component. </p>
<h2>AUTHOR</h2>
<p> Nalin Dahyabhai &lt;nalin [at] redhat.com&gt; </p>
<h2>Index</h2>
