---

title: "dspam_train(1)"
name: "dspam_train"
section: "1"
letter: "d"
url: "/docs/linux/man/1-dspam_train/"
description: "dspam_train – train a corpus of mail"
---

<p> <code>dspam_train</code> [<code>username</code>] [<code>&#8211;client</code>] [<code>-i&nbsp;<wbr></code>index|<code>spam_corpus</code>&nbsp;<wbr><code>nonspam_corpus</code>] </p>
<p> <code>dspam_train</code> is used to train and test a corpus of mail (in maildir or MBOX format). This tool will present each message to DSPAM for a classification and then retrain only if the message was incorrect. This provides close to real-world training and should be used to build pretrained databases. Upon execution, the tool will automatically determine the ratio of spam:nonspam and train based on that ratio to ensure both corpora are trained consecutively. This tool can also be used as a test jig to measure the efficiency and accuracy of a particular corpus against DSPAM in a given configuration. </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>&#8211;client</code></dt>
<dd> If specified, DSPAM is used in client-server mode. </dd>
<dt><code>username</code></dt>
<dd> Specifies the user to train, if omitted the current user name is used. </dd>
<dt><code>-i</code>&nbsp;<wbr>index</dt>
<dd> Use a index file instead of the usual spam_corpus and nonspam_corpus. </dd>
<p> <code>index</code> : Path to the index file having the following format per line:<br />
 [class] [path to message] </p>
<dt><code>spam_corpus</code></dt>
<dd> Specifies either the pathname to the directory containing the corpus of spam, with each in a separate file (e.g. maildir format) or a path to the mailbox in the traditional Unix MBOX format. </dd>
<dt><code>nonspam_corpus</code></dt>
<dd> Specifies either the pathname to the directory containing the corpus of nonspam with each message in a separate file or a path to the mailbox in the traditional Unix MBOX format. </dd>
</dl>
<h2>EXIT VALUE</h2>
<dl>
<dt><code>0</code></dt>
<dd> Operation was successful.</dd>
<dt><code>other</code></dt>
<dd> Operation resulted in an error. </dd>
</dl>
<h2>COPYRIGHT</h2>
<p> Copyright &#169; 2002-2012 DSPAM Project<br />
 All rights reserved. </p>
<p> For more information, see <a rel="nofollow" href="http://dspam.sourceforge.net.">http://dspam.sourceforge.net.</a> </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-dspam/">dspam</a></code>(1), <code><a href="/docs/linux/man/1-dspam_admin/">dspam_admin</a></code>(1), <code><a href="/docs/linux/man/1-dspam_clean/">dspam_clean</a></code>(1), <code><a href="/docs/linux/man/1-dspam_crc/">dspam_crc</a></code>(1), <code><a href="/docs/linux/man/1-dspam_dump/">dspam_dump</a></code>(1), <code><a href="/docs/linux/man/1-dspam_logrotate/">dspam_logrotate</a></code>(1), <code><a href="/docs/linux/man/1-dspam_merge/">dspam_merge</a></code>(1), <code><a href="/docs/linux/man/1-dspam_stats/">dspam_stats</a></code>(1) </p>
