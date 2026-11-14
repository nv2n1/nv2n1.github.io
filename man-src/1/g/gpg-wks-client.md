---
title: "gpg-wks-client(1)"
name: "gpg-wks-client"
section: "1"
letter: "g"
url: "/docs/linux/man/1-gpg-wks-client/"
description: "gpg-wks-client – Client for the Web Key Service"
---

<h2 class="name">NAME</h2>
<p> <code>gpg-wks-client</code> &#8211; Client for the Web Key Service </p>
<h2>SYNOPSIS</h2>
<p> <code>gpg-wks-client</code> [<i>options</i>] <code>&#8211;supported</code> <i>user-id</i><br />
 <code>gpg-wks-client</code> [<i>options</i>] <code>&#8211;check</code> <i>user-id</i><br />
 <code>gpg-wks-client</code> [<i>options</i>] <code>&#8211;create</code> <i>fingerprint</i> <i>user-id</i><br />
 <code>gpg-wks-client</code> [<i>options</i>] <code>&#8211;receive</code><br />
 <code>gpg-wks-client</code> [<i>options</i>] <code>&#8211;read</code> </p>
<h2>DESCRIPTION</h2>
<p> The <code>gpg-wks-client</code> is used to send requests to a Web Key Service provider. This is usuallay done to upload a key into a Web Key Directory. </p>
<p> With the <code>&#8211;supported</code> command the caller can test whether a site supports the Web Key Service. The argument is an arbitrary address in the to be tested domain. For example &#8216;<i>foo [at] example.net</i>&#8216;. The command returns success if the Web Key Service is supported. The operation is silent; to get diagnostic output use the option <code>&#8211;verbose</code>. See option <code>&#8211;with-colons</code> for a variant of this command. </p>
<p> With the <code>&#8211;check</code> command the caller can test whether a key exists for a supplied mail address. The command returns success if a key is available. </p>
<p> The <code>&#8211;create</code> command is used to send a request for publication in the Web Key Directory. The arguments are the fingerprint of the key and the user id to publish. The output from the command is a properly formatted mail with all standard headers. This mail can be fed to <code><a href="/docs/linux/man/8-sendmail/">sendmail</a>(8)</code> or any other tool to actually send that mail. If <code><a href="/docs/linux/man/8-sendmail/">sendmail</a>(8)</code> is installed the option <code>&#8211;send</code> can be used to directly send the created request. If the provider request a &#8216;mailbox-only&#8217; user id and no such user id is found, <code>gpg-wks-client</code> will try an additional user id. </p>
<p> The <code>&#8211;receive</code> and <code>&#8211;read</code> commands are used to process confirmation mails as send from the service provider. The former expects an encrypted MIME messages, the latter an already decrypted MIME message. The result of these commands are another mail which can be send in the same way as the mail created with <code>&#8211;create</code>. </p>
<p> The command <code>&#8211;install-key</code> manually installs a key into a local directory (see option <code>-C</code>) reflecting the structure of a WKD. The arguments are a file with the keyblock and the user-id to install. If the first argument resembles a fingerprint the key is taken from the current keyring; to force the use of a file, prefix the first argument with &quot;./&quot;. If no arguments are given the parameters are read from stdin; the expected format are lines with the fingerprint and the mailbox separated by a space. The command <code>&#8211;remove-key</code> removes a key from that directory, its only argument is a user-id. </p>
<p> The command <code>&#8211;print-wkd-hash</code> prints the WKD user-id identifiers and the corresponding mailboxes from the user-ids given on the command line or via stdin (one user-id per line). </p>
<p> The command <code>&#8211;print-wkd-url</code> prints the URLs used to fetch the key for the given user-ids from WKD. The meanwhile preferred format with sub-domains is used here. </p>
<p> <code>gpg-wks-client</code> is not commonly invoked directly and thus it is not installed in the bin directory. Here is an example how it can be invoked manually to check for a Web Key Directory entry for &#8216;<i>foo [at] example.org</i>&#8216;: </p>
<dl>
<dt>
<dd>
<pre><code>
$(gpgconf-- list - dirs libexecdir) / gpg - wks - client-- check foo[at] example.net
</code></pre>
</dl>
<h2>OPTIONS</h2>
<p> <code>gpg-wks-client</code> understands these options: </p>
<dl>
<dt><code>&#8211;send</code></p>
<dd> Directly send created mails using the <code>sendmail</code> command. Requires installation of that command. </p>
<dt><code>&#8211;with-colons</code></p>
<dd> This option has currently only an effect on the <code>&#8211;supported</code> command. If it is used all arguments on the command line are taken as domain names and tested for WKD support. The output format is one line per domain with colon delimited fields. The currently specified fields are (future versions may specify additional fields): </p>
<dl>
<dt>
<dd>
<dl>
<dt><code>1 &#8211; domain</code></p>
<dd> This is the domain name. Although quoting is not required for valid domain names this field is specified to be quoted in standard C manner. </p>
<dt><code>2 &#8211; WKD</code></p>
<dd> If the value is true the domain supports the Web Key Directory. </p>
<dt><code>3 &#8211; WKS</code></p>
<dd> If the value is true the domain supports the Web Key Service protocol to upload keys to the directory. </p>
<dt><code>4 &#8211; error-code</code></p>
<dd> This may contain an gpg-error code to describe certain failures. Use &#8216;gpg-error CODE&#8217; to explain the code. </p>
<dt><code>5 &#8211; protocol-version</code></p>
<dd> The minimum protocol version supported by the server. </p>
<dt><code>6 &#8211; auth-submit</code></p>
<dd> The auth-submit flag from the policy file of the server. </p>
<dt><code>7 &#8211; mailbox-only</code></p>
<dd> The mailbox-only flag from the policy file of the server.</dl>
</dl>
<dt><code>&#8211;output </code><i>file</i></p>
<dd> <code>-o</code> Write the created mail to <i>file</i> instead of stdout. Note that the value <code>&#8211;</code> for <i>file</i> is the same as writing to stdout. </p>
<dt><code>&#8211;status-fd </code><i>n</i></p>
<dd> Write special status strings to the file descriptor <i>n</i>. This program returns only the status messages SUCCESS or FAILURE which are helpful when the caller uses a double fork approach and can&#8217;t easily get the return code of the process. </p>
<dt><code>-C </code><i>dir</i></p>
<dd> <code>&#8211;directory </code><i>dir</i> Use <i>dir</i> as top level directory for the commands <code>&#8211;install-key</code> and <code>&#8211;remove-key</code>. The default is &#8216;<i>openpgpkey</i>&#8216;. </p>
<dt><code>&#8211;verbose</code></p>
<dd> Enable extra informational output. </p>
<dt><code>&#8211;quiet</code></p>
<dd> Disable almost all informational output. </p>
<dt><code>&#8211;version</code></p>
<dd> Print version of the program and exit. </p>
<dt><code>&#8211;help</code></p>
<dd> Display a brief help page and exit. </p>
</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-gpg-wks-server/">gpg-wks-server</a></code>(1) </p>
<h2>Index</h2>
