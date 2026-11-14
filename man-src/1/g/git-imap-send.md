---
title: "git-imap-send(1)"
name: "git-imap-send"
section: "1"
letter: "g"
url: "/docs/linux/man/1-git-imap-send/"
description: "git-imap-send – Send a collection of patches from stdin to an IMAP folder"
---

<h2 class="name">NAME</h2>
<p> git-imap-send &#8211; Send a collection of patches from stdin to an IMAP folder </p>
<h2>SYNOPSIS</h2>
<pre><code>
git imap - send[-v][-q][--[no - ] curl]
</code></pre>
<h2>DESCRIPTION</h2>
<p> This command uploads a mailbox generated with <i>git format-patch</i> into an IMAP drafts folder. This allows patches to be sent as other email is when using mail clients that cannot read mailbox files directly. The command also works with any general mailbox in which emails have the fields &quot;From&quot;, &quot;Date&quot;, and &quot;Subject&quot; in that order. </p>
<p> Typical usage is something like: </p>
<p> git format-patch &#8211;signoff &#8211;stdout &#8211;attach origin | git imap-send</p>
<h2>OPTIONS</h2>
<p> -v, &#8211;verbose</p>
<dl>
<dt>
<dd> Be verbose.</dl>
<p> -q, &#8211;quiet</p>
<dl>
<dt>
<dd> Be quiet.</dl>
<p> &#8211;curl</p>
<dl>
<dt>
<dd> Use libcurl to communicate with the IMAP server, unless tunneling into it. Ignored if Git was built without the USE_CURL_FOR_IMAP_SEND option set.</dl>
<p> &#8211;no-curl</p>
<dl>
<dt>
<dd> Talk to the IMAP server using git&#8217;s own IMAP routines instead of using libcurl. Ignored if Git was built with the NO_OPENSSL option set.</dl>
<h2>CONFIGURATION</h2>
<p> To use the tool, <code>imap.folder</code> and either <code>imap.tunnel</code> or <code>imap.host</code> must be set to appropriate values. </p>
<p> imap.folder</p>
<dl>
<dt>
<dd> The folder to drop the mails into, which is typically the Drafts folder. For example: &quot;INBOX.Drafts&quot;, &quot;INBOX/Drafts&quot; or &quot;[Gmail]/Drafts&quot;. Required.</dl>
<p> imap.tunnel</p>
<dl>
<dt>
<dd> Command used to setup a tunnel to the IMAP server through which commands will be piped instead of using a direct network connection to the server. Required when imap.host is not set.</dl>
<p> imap.host</p>
<dl>
<dt>
<dd> A URL identifying the server. Use an <code>imap://</code> prefix for non-secure connections and an <code>imaps://</code> prefix for secure connections. Ignored when imap.tunnel is set, but required otherwise.</dl>
<p> imap.user</p>
<dl>
<dt>
<dd> The username to use when logging in to the server.</dl>
<p> imap.pass</p>
<dl>
<dt>
<dd> The password to use when logging in to the server.</dl>
<p> imap.port</p>
<dl>
<dt>
<dd> An integer port number to connect to on the server. Defaults to 143 for imap:// hosts and 993 for imaps:// hosts. Ignored when imap.tunnel is set.</dl>
<p> imap.sslverify</p>
<dl>
<dt>
<dd> A boolean to enable/disable verification of the server certificate used by the SSL/TLS connection. Default is <code>true</code>. Ignored when imap.tunnel is set.</dl>
<p> imap.preformattedHTML</p>
<dl>
<dt>
<dd> A boolean to enable/disable the use of html encoding when sending a patch. An html encoded patch will be bracketed with &lt;pre&gt; and have a content type of text/html. Ironically, enabling this option causes Thunderbird to send the patch as a plain/text, format=fixed email. Default is <code>false</code>.</dl>
<p> imap.authMethod</p>
<dl>
<dt>
<dd> Specify authenticate method for authentication with IMAP server. If Git was built with the NO_CURL option, or if your curl version is older than 7.34.0, or if you&#8217;re running git-imap-send with the <code>&#8211;no-curl</code> option, the only supported method is <i>CRAM-MD5</i>. If this is not set then <i>git imap-send</i> uses the basic IMAP plaintext LOGIN command.</dl>
<h2>EXAMPLES</h2>
<p> Using tunnel mode: </p>
<dl>
<dt>
<dd>
[imap] folder = &#8220;INBOX.Drafts&#8221; tunnel = &#8220;ssh -q -C user [at] example.com /usr/bin/imapd ./Maildir 2&gt; /dev/null&#8221;
</dl>
<p> Using direct mode: </p>
<dl>
<dt>
<dd>
<pre>
[imap]
    folder = &quot;INBOX.Drafts&quot;
    host = <a href="imap://imap.example.com">imap://imap.example.com</a>
    user = bob
    pass = p4ssw0rd
</pre>
</dl>
<p> Using direct mode with SSL: </p>
<dl>
<dt>
<dd>
<pre>
[imap]
    folder = &quot;INBOX.Drafts&quot;
    host = <a href="imaps://imap.example.com">imaps://imap.example.com</a>
    user = bob
    pass = p4ssw0rd
    port = 123
    ; sslVerify = false
</pre>
</dl>
<dl>
<dt>
<dd>
 <font SIZE="+1"> <code>Note</code> </font> </p>
<p> You may want to use <code>sslVerify=false</code> while troubleshooting, if you suspect that the reason you are having trouble connecting is because the certificate you use at the private server <code>example.com</code> you are trying to set up (or have set up) may not be verified correctly. </p>
</dl>
<p> Using Gmail&#8217;s IMAP interface: </p>
<dl>
<dt>
<dd>
<pre><code>
[imap] folder = "[Gmail]/Drafts" host = imaps : // imap.gmail.com
                                                user = user[at] gmail.com
                                                           port = 993
</code></pre>
</dl>
<dl>
<dt>
<dd>
 <font SIZE="+1"> <code>Note</code> </font> </p>
<p> You might need to instead use: <code>folder = &quot;[Google Mail]/Drafts&quot;</code> if you get an error that the &quot;Folder doesn&#8217;t exist&quot;. </p>
</dl>
<dl>
<dt>
<dd>
 <font SIZE="+1"> <code>Note</code> </font> </p>
<p> If your Gmail account is set to another language than English, the name of the &quot;Drafts&quot; folder will be localized. </p>
</dl>
<p> Once the commits are ready to be sent, run the following command: </p>
<dl>
<dt>
<dd>
<pre>
$ git format-patch --cover-letter -M --stdout origin/master | git imap-send
</pre>
</dl>
<p> Just make sure to disable line wrapping in the email client (Gmail&#8217;s web interface will wrap lines no matter what, so you need to use a real IMAP client).</p>
<h2>CAUTION</h2>
<p> It is still your responsibility to make sure that the email message sent by your email program meets the standards of your project. Many projects do not like patches to be attached. Some mail agents will transform patches (e.g. wrap lines, send them as format=flowed) in ways that make them fail. You will get angry flames ridiculing you if you don&#8217;t check this. </p>
<p> Thunderbird in particular is known to be problematic. Thunderbird users may wish to visit this web page for more information: m[blue]<code><a rel="nofollow" href="http://kb.mozillazine.org/Plain_text_e-mail_-_Thunderbird#Completely_plain_email">http://kb.mozillazine.org/Plain_text_e-mail_-_Thunderbird#Completely_plain_email</a></code>m[]</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-git-format-patch/">git-format-patch</a></code>(1), <code><a href="/docs/linux/man/1-git-send-email/">git-send-email</a></code>(1), <a href="/docs/linux/man/5-mbox/">mbox</a>(5)</p>
<h2>GIT</h2>
<p> Part of the <code><a href="/docs/linux/man/1-git/">git</a></code>(1) suite </p>
<h2>Index</h2>
