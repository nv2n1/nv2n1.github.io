---
title: "pwquality(5)"
name: "pwquality"
section: "5"
letter: "p"
url: "/docs/linux/man/5-pwquality/"
description: "pwquality.conf – configuration for the libpwquality library"
---

<p>pwquality.conf &#8211; configuration for the libpwquality library</p>
<h2>Synopsis</h2>
<p><code>/etc/security/pwquality.conf</code></p>
<h2>Description</h2>
<p><code>pwquality.conf</code> provides a way to configure the default password quality requirements for the system passwords. This file is read by the libpwquality library and utilities that use this library for checking and generating passwords. The file has a very simple <i>name = value</i> format with possible comments starting with <code>#</code> character. The whitespace at the beginning of line, end of line, and around the <code>=</code> sign is ignored. </p>
<h2>Options</h2>
<p>The possible options in the file are:</p>
<dl>
<dd><code>difok</code></p>
<dl>
<dd>Number of characters in the new password that must not be present in the old password. (default 5)</dl>
<p> <code>minlen</code></p>
<dl>
<dd>Minimum acceptable size for the new password (plus one if credits are not disabled which is the default). (See <i><a href="/docs/linux/man/8-pam_pwquality/">pam_pwquality</a>(8)</i>.) Cannot be set to lower value than 6. (default 9)</dl>
<p> <code>dcredit</code></p>
<dl>
<dd>The maximum credit for having digits in the new password. If less than 0 it is the minimum number of digits in the new password. (default 1)</dl>
<p> <code>ucredit</code></p>
<dl>
<dd>The maximum credit for having uppercase characters in the new password. If less than 0 it is the minimum number of uppercase characters in the new password. (default 1)</dl>
<p> <code>lcredit</code></p>
<dl>
<dd>The maximum credit for having lowercase characters in the new password. If less than 0 it is the minimum number of lowercase characters in the new password. (default 1)</dl>
<p> <code>ocredit</code></p>
<dl>
<dd>The maximum credit for having other characters in the new password. If less than 0 it is the minimum number of other characters in the new password. (default 1)</dl>
<p> <code>minclass</code></p>
<dl>
<dd>The minimum number of required classes of characters for the new password (digits, uppercase, lowercase, others). (default 0)</dl>
<p> <code>maxrepeat</code></p>
<dl>
<dd>The maximum number of allowed same consecutive characters in the new password. The check is disabled if the value is 0. (default 0)</dl>
<p> <code>maxsequence</code></p>
<dl>
<dd>The maximum length of monotonic character sequences in the new password. Examples of such sequence are &#8216;12345&#8217; or &#8216;fedcb&#8217;. Note that most such passwords will not pass the simplicity check unless the sequence is only a minor part of the password. The check is disabled if the value is 0. (default 0)</dl>
<p> <code>maxclassrepeat</code></p>
<dl>
<dd>The maximum number of allowed consecutive characters of the same class in the new password. The check is disabled if the value is 0. (default 0)</dl>
<p> <code>gecoscheck</code></p>
<dl>
<dd>If nonzero, check whether the words longer than 3 characters from the GECOS field of the user&#8217;s passwd entry are contained in the new password. The check is disabled if the value is 0. (default 0)</dl>
<p> <code>badwords</code></p>
<dl>
<dd>Space separated list of words that must not be contained in the password. These are additional words to the cracklib dictionary check. This setting can be also used by applications to emulate the gecos check for user accounts that are not created yet.</dl>
<p> <code>dictpath</code></p>
<dl>
<dd>Path to the cracklib dictionaries. Default is to use the cracklib default.</dl>
</dl>
<h2>See Also</h2>
<p><a href="/docs/linux/man/1-pwscore/">pwscore</a>(1), <a href="/docs/linux/man/1-pwmake/">pwmake</a>(1), <a href="/docs/linux/man/8-pam_pwquality/">pam_pwquality</a>(8) </p>
<h2>Authors</h2>
<pre>Tomas Mraz &lt;tmraz [at] redhat.com&gt;</pre>
