---
title: "gpg-wks-server(1)"
name: "gpg-wks-server"
section: "1"
letter: "g"
url: "/docs/linux/man/1-gpg-wks-server/"
description: "gpg-wks-server – Server providing the Web Key Service"
---

<h2 class="name">NAME</h2>
<p> <code>gpg-wks-server</code> &#8211; Server providing the Web Key Service </p>
<h2>SYNOPSIS</h2>
<p> <code>gpg-wks-server</code> [<i>options</i>] <code>&#8211;receive</code><br />
 <code>gpg-wks-server</code> [<i>options</i>] <code>&#8211;cron</code><br />
 <code>gpg-wks-server</code> [<i>options</i>] <code>&#8211;list-domains</code><br />
 <code>gpg-wks-server</code> [<i>options</i>] <code>&#8211;check-key</code> <i>user-id</i><br />
 <code>gpg-wks-server</code> [<i>options</i>] <code>&#8211;install-key</code> <i>file</i> <i>user-id</i><br />
 <code>gpg-wks-server</code> [<i>options</i>] <code>&#8211;remove-key</code> <i>user-id</i><br />
 <code>gpg-wks-server</code> [<i>options</i>] <code>&#8211;revoke-key</code> <i>user-id</i> </p>
<h2>DESCRIPTION</h2>
<p> The <code>gpg-wks-server</code> is a server site implementation of the Web Key Service. It receives requests for publication, sends confirmation requests, receives confirmations, and published the key. It also has features to ease the setup and maintenance of a Web Key Directory. </p>
<p> When used with the command <code>&#8211;receive</code> a single Web Key Service mail is processed. Commonly this command is used with the option <code>&#8211;send</code> to directly send the crerated mails back. See below for an installation example. </p>
<p> The command <code>&#8211;cron</code> is used for regualr cleanup tasks. For example non-confirmed requested should be removed after their expire time. It is best to run this command once a day from a cronjob. </p>
<p> The command <code>&#8211;list-domains</code> prints all configured domains. Further it creates missing directories for the configuration and prints warnings pertaining to problems in the configuration. </p>
<p> The command <code>&#8211;check-key</code> (or just <code>&#8211;check</code>) checks whether a key with the given user-id is installed. The process returns success in this case; to also print a diagnostic use the option <code>-v</code>. If the key is not installed a diagnostic is printed and the process returns failure; to suppress the diagnostic, use option <code>-q</code>. More than one user-id can be given; see also option <code>with-file</code>. </p>
<p> The command <code>&#8211;install-key</code> manually installs a key into the WKD. The arguments are a file with the keyblock and the user-id to install. If the first argument resembles a fingerprint the key is taken from the current keyring; to force the use of a file, prefix the first argument with &quot;./&quot;. If no arguments are given the parameters are read from stdin; the expected format are lines with the fingerprint and the mailbox separated by a space. </p>
<p> The command <code>&#8211;remove-key</code> uninstalls a key from the WKD. The process returns success in this case; to also print a diagnostic, use option <code>-v</code>. If the key is not installed a diagnostic is printed and the process returns failure; to suppress the diagnostic, use option <code>-q</code>. </p>
<p> The command <code>&#8211;revoke-key</code> is not yet functional. </p>
<h2>OPTIONS</h2>
<p> <code>gpg-wks-server</code> understands these options: </p>
<dl>
<dt><code>-C </code><i>dir</i></p>
<dd> <code>&#8211;directory </code><i>dir</i> Use <i>dir</i> as top level directory for domains. The default is &#8216;<i>/var/lib/gnupg/wks</i>&#8216;. </p>
<dt><code>&#8211;from </code><i>mailaddr</i></p>
<dd> Use <i>mailaddr</i> as the default sender address. </p>
<dt><code>&#8211;header </code><i>name</i>=<i>value</i></p>
<dd> Add the mail header &quot;<i>name</i>: <i>value</i>&quot; to all outgoing mails. </p>
<dt><code>&#8211;send</code></p>
<dd> Directly send created mails using the <code>sendmail</code> command. Requires installation of that command. </p>
<dt><code>-o </code><i>file</i></p>
<dd> <code>&#8211;output </code><i>file</i> Write the created mail also to <i>file</i>. Note that the value <code>&#8211;</code> for <i>file</i> would write it to stdout. </p>
<dt><code>&#8211;with-dir</code></p>
<dd> When used with the command <code>&#8211;list-domains</code> print for each installed domain the domain name and its directory name. </p>
<dt><code>&#8211;with-file</code></p>
<dd> When used with the command <code>&#8211;check-key</code> print for each user-id, the address, &#8216;i&#8217; for installed key or &#8216;n&#8217; for not installed key, and the filename. </p>
<dt><code>&#8211;verbose</code></p>
<dd> Enable extra informational output. </p>
<dt><code>&#8211;quiet</code></p>
<dd> Disable almost all informational output. </p>
<dt><code>&#8211;version</code></p>
<dd> Print version of the program and exit. </p>
<dt><code>&#8211;help</code></p>
<dd> Display a brief help page and exit. </p>
</dl>
<h2>EXAMPLES</h2>
<p> The Web Key Service requires a working directory to store keys pending for publication. As root create a working directory: </p>
<dl>
<dt>
<dd>
<pre>
  # mkdir /var/lib/gnupg/wks
  # chown webkey:webkey /var/lib/gnupg/wks
  # chmod 2750 /var/lib/gnupg/wks
</pre>
</dl>
<p> Then under your webkey account create directories for all your domains. Here we do it for &quot;example.net&quot;: </p>
<dl>
<dt>
<dd>
<pre>
  $ mkdir /var/lib/gnupg/wks/example.net
</pre>
</dl>
<p> Finally run </p>
<dl>
<dt>
<dd>
<pre>
  $ gpg-wks-server --list-domains
</pre>
</dl>
<p> to create the required sub-directories with the permissions set correctly. For each domain a submission address needs to be configured. All service mails are directed to that address. It can be the same address for all configured domains, for example: </p>
<dl>
<dt>
<dd>
<pre>
  $ cd /var/lib/gnupg/wks/example.net
  $ echo key-submission [at] example.net &gt;submission-address
</pre>
</dl>
<p> The protocol requires that the key to be published is send with an encrypted mail to the service. Thus you need to create a key for the submission address: </p>
<dl>
<dt>
<dd>
<pre><code>
$ gpg-- batch-- passphrase '' --quick - gen - key key - submission[at] example.net $ gpg - K key - submission[at] example.net
</code></pre>
</dl>
<p> The output of the last command looks similar to this: </p>
<dl>
<dt>
<dd>
sec rsa3072 2016 &#8211; 08 &#8211; 30 [SC] C0FCF8642D830C53246211400346653590B3795B uid[ultimate] key &#8211; submission[at] example.net ssb rsa3072 2016 &#8211; 08 &#8211; 30 [E]
</dl>
<p> Take the fingerprint from that output and manually publish the key: </p>
<dl>
<dt>
<dd>
<pre>
  $ gpg-wks-server --install-key C0FCF8642D830C53246211400346653590B3795B \
  &gt;                key-submission [at] example.net
</pre>
</dl>
<p> Finally that submission address needs to be redirected to a script running <code>gpg-wks-server</code>. The <code>procmail</code> command can be used for this: Redirect the submission address to the user &quot;webkey&quot; and put this into webkey&#8217;s &#8216;<i>.procmailrc</i>&#8216;: </p>
<dl>
<dt>
<dd>
<pre><code>
:0
* !^From: webkey [at] example.net
* !^X-WKS-Loop: webkey.example.net
|gpg-wks-server -v --receive \
     --header X-WKS-Loop=webkey.example.net \
     --from webkey [at] example.net --send
</code></pre>
</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-gpg-wks-client/">gpg-wks-client</a></code>(1) </p>
<h2>Index</h2>
