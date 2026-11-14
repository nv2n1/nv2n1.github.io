---
title: "stg-mail(1)"
name: "stg-mail"
section: "1"
letter: "s"
url: "/docs/linux/man/1-stg-mail/"
description: "stg-mail – Send a patch or series of patches by e-mail"
---

<h2 class="name">NAME</h2>
<p> stg-mail &#8211; Send a patch or series of patches by e-mail </p>
<h2>SYNOPSIS</h2>
<pre><code>
stg mail[options][--][&lt;patch1&gt;][&lt;patch2&gt;][&lt;patch3&gt;..&lt;patch4&gt;]
</code></pre>
<h2>DESCRIPTION</h2>
<p> Send a patch or a range of patches by e-mail using the SMTP server specified by the <i>stgit.smtpserver</i> configuration option, or the <i>&#8211;smtp-server</i> command line option. This option can also be an absolute path to <i>sendmail</i> followed by command line arguments. </p>
<p> The From address and the e-mail format are generated from the template file passed as argument to <i>&#8211;template</i> (defaulting to <i>.git/patchmail.tmpl</i> or <i>~/.stgit/templates/patchmail.tmpl</i> or <i>/usr/share/stgit/templates/patchmail.tmpl</i>). A patch can be sent as attachment using the &#8211;attach option in which case the <i>mailattch.tmpl</i> template will be used instead of <i>patchmail.tmpl</i>. </p>
<p> The To/Cc/Bcc addresses can either be added to the template file or passed via the corresponding command line options. They can be e-mail addresses or aliases which are automatically expanded to the values stored in the [mail &quot;alias&quot;] section of GIT configuration files. </p>
<p> A preamble e-mail can be sent using the <i>&#8211;cover</i> and/or <i>&#8211;edit-cover</i> options. The first allows the user to specify a file to be used as a template. The latter option will invoke the editor on the specified file (defaulting to <i>.git/covermail.tmpl</i> or <i>~/.stgit/templates/covermail.tmpl</i> or <i>/usr/share/stgit/templates/covermail.tmpl</i>). </p>
<p> All the subsequent e-mails appear as replies to the first e-mail sent (either the preamble or the first patch). E-mails can be seen as replies to a different e-mail by using the <i>&#8211;in-reply-to</i> option. </p>
<p> SMTP authentication is also possible with <i>&#8211;smtp-user</i> and <i>&#8211;smtp-password</i> options, also available as configuration settings: <i>smtpuser</i> and <i>smtppassword</i>. TLS encryption can be enabled by <i>&#8211;smtp-tls</i> option and <i>smtptls</i> setting. </p>
<p> The following variables are accepted by both the preamble and the patch e-mail templates: </p>
<dl>
<dt>
<dd>
<pre>
%(diffstat)s     - diff statistics
%(number)s       - empty if only one patch is sent or 'patchnr/totalnr'
%(snumber)s      - stripped version of '%(number)s'
%(nspace)s       - ' ' if %(number)s is non-empty, otherwise empty string
%(patchnr)s      - patch number
%(sender)s       - 'sender'  or 'authname &lt;authemail&gt;' as per the config file
%(totalnr)s      - total number of patches to be sent
%(version)s      - 'version' string passed on the command line (or empty)
%(vspace)s       - ' ' if %(version)s is non-empty, otherwise empty string
</pre>
</dl>
<p> In addition to the common variables, the preamble e-mail template accepts the following: </p>
<dl>
<dt>
<dd>
<pre>
%(shortlog)s     - first line of each patch description, listed by author
</pre>
</dl>
<p> In addition to the common variables, the patch e-mail template accepts the following: </p>
<dl>
<dt>
<dd>
<pre>
%(authdate)s     - patch creation date
%(authemail)s    - author's email
%(authname)s     - author's name
%(commemail)s    - committer's e-mail
%(commname)s     - committer's name
%(diff)s         - unified diff of the patch
%(fromauth)s     - 'From: author

' if different from sender
%(longdescr)s    - the rest of the patch description, after the first line
%(patch)s        - patch name
%(prefix)s       - 'prefix' string passed on the command line
%(pspace)s       - ' ' if %(prefix)s is non-empty, otherwise empty string
%(shortdescr)s   - the first line of the patch description
</pre>
</dl>
<h2>OPTIONS</h2>
<p> -a, &#8211;all</p>
<dl>
<dt>
<dd> E-mail all the applied patches.</dl>
<p> &#8211;to TO</p>
<dl>
<dt>
<dd> Add TO to the To: list.</dl>
<p> &#8211;cc CC</p>
<dl>
<dt>
<dd> Add CC to the Cc: list.</dl>
<p> &#8211;bcc BCC</p>
<dl>
<dt>
<dd> Add BCC to the Bcc: list.</dl>
<p> &#8211;auto</p>
<dl>
<dt>
<dd> Automatically cc the patch signers.</dl>
<p> &#8211;no-thread</p>
<dl>
<dt>
<dd> Do not send subsequent messages as replies.</dl>
<p> &#8211;unrelated</p>
<dl>
<dt>
<dd> Send patches without sequence numbering.</dl>
<p> &#8211;attach</p>
<dl>
<dt>
<dd> Send a patch as attachment.</dl>
<p> &#8211;attach-inline</p>
<dl>
<dt>
<dd> Send a patch inline and as an attachment.</dl>
<p> -v VERSION, &#8211;version VERSION</p>
<dl>
<dt>
<dd> Add VERSION to the [PATCH &#8230;] prefix.</dl>
<p> &#8211;prefix PREFIX</p>
<dl>
<dt>
<dd> Add PREFIX to the [&#8230; PATCH &#8230;] prefix.</dl>
<p> -t FILE, &#8211;template FILE</p>
<dl>
<dt>
<dd> Use FILE as the message template.</dl>
<p> -c FILE, &#8211;cover FILE</p>
<dl>
<dt>
<dd> Send FILE as the cover message.</dl>
<p> -e, &#8211;edit-cover</p>
<dl>
<dt>
<dd> Edit the cover message before sending.</dl>
<p> -E, &#8211;edit-patches</p>
<dl>
<dt>
<dd> Edit each patch before sending.</dl>
<p> -s SECONDS, &#8211;sleep SECONDS</p>
<dl>
<dt>
<dd> Sleep for SECONDS between e-mails sending.</dl>
<p> &#8211;in-reply-to REFID</p>
<dl>
<dt>
<dd> Use REFID as the reference id.</dl>
<p> &#8211;smtp-server HOST[:PORT] or &quot;/path/to/sendmail -t -i&quot;</p>
<dl>
<dt>
<dd> SMTP server or command to use for sending mail.</dl>
<p> -u USER, &#8211;smtp-user USER</p>
<dl>
<dt>
<dd> Username for SMTP authentication.</dl>
<p> -p PASSWORD, &#8211;smtp-password PASSWORD</p>
<dl>
<dt>
<dd> Password for SMTP authentication.</dl>
<p> -T, &#8211;smtp-tls</p>
<dl>
<dt>
<dd> Use SMTP with TLS encryption.</dl>
<p> -b BRANCH, &#8211;branch BRANCH</p>
<dl>
<dt>
<dd> Use BRANCH instead of the default branch.</dl>
<p> -m, &#8211;mbox</p>
<dl>
<dt>
<dd> Generate an mbox file instead of sending.</dl>
<p> &#8211;git</p>
<dl>
<dt>
<dd> Use git send-email (EXPERIMENTAL).</dl>
<p> -O OPTIONS, &#8211;diff-opts OPTIONS</p>
<dl>
<dt>
<dd> Extra options to pass to &quot;git diff&quot;.</dl>
<h2>STGIT</h2>
<p> Part of the StGit suite &#8211; see <code><a href="/docs/linux/man/1-stg/">stg</a></code>(1) </p>
<h2>Index</h2>
