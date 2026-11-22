---
title: "pwquality-conf(5)"
name: "pwquality-conf"
section: "5"
letter: "p"
url: "/docs/linux/man/5-pwquality-conf/"
description: "pwquality.conf – configuration for the libpwquality library"
---

<p>pwquality.conf &#8211; configuration for the libpwquality library</p>
<h2>Synopsis</h2>
<p><i>/etc/security/pwquality.conf</i> </p>
<p> <i>/etc/security/pwquality.conf.d/*.conf</i></p>
<h2>Description</h2>
<p><code>pwquality.conf</code> provides a way to configure the default password quality requirements for the system passwords. This file is read by the libpwquality library and utilities that use this library for checking and generating passwords. </p>
<p> The file has a very simple <i>name = value</i> format with possible comments starting with <tt>&quot;#&quot;</tt> character. The whitespace at the beginning of line, end of line, and around the <tt>&quot;=&quot;</tt> sign is ignored. </p>
<p> The libpwquality library also first reads all <i>*.conf</i> files from the <i>/etc/security/pwquality.conf.d</i> directory in ASCII sorted order. The values of the same settings are overridden in the order the files are parsed.</p>
<h2>Options</h2>
<p>The possible options in the file are:</p>
<dl>
<dt><code>difok</code></dt>
<dd>Number of characters in the new password that must not be present in the old password. (default 1) </dd>
<p> The special value of 0 disables all checks of similarity of the new password with the old password except the new password being exactly the same as the old one.</p>
<dt><code>minlen</code></dt>
<dd>Minimum acceptable size for the new password (plus one if credits are not disabled which is the default). (See <code><a href="/docs/linux/man/8-pam_pwquality/">pam_pwquality</a></code>(8).) Cannot be set to lower value than 6. (default 8)</dd>
<dt><code>dcredit</code></dt>
<dd>The maximum credit for having digits in the new password. If less than 0 it is the minimum number of digits in the new password. (default 0)</dd>
<dt><code>ucredit</code></dt>
<dd>The maximum credit for having uppercase characters in the new password. If less than 0 it is the minimum number of uppercase characters in the new password. (default 0)</dd>
<dt><code>lcredit</code></dt>
<dd>The maximum credit for having lowercase characters in the new password. If less than 0 it is the minimum number of lowercase characters in the new password. (default 0)</dd>
<dt><code>ocredit</code></dt>
<dd>The maximum credit for having other characters in the new password. If less than 0 it is the minimum number of other characters in the new password. (default 0)</dd>
<dt><code>minclass</code></dt>
<dd>The minimum number of required classes of characters for the new password (digits, uppercase, lowercase, others). (default 0)</dd>
<dt><code>maxrepeat</code></dt>
<dd>The maximum number of allowed same consecutive characters in the new password. The check is disabled if the value is 0. (default 0)</dd>
<dt><code>maxsequence</code></dt>
<dd>The maximum length of monotonic character sequences in the new password. Examples of such sequence are &#8216;12345&#8217; or &#8216;fedcb&#8217;. Note that most such passwords will not pass the simplicity check unless the sequence is only a minor part of the password. The check is disabled if the value is 0. (default 0)</dd>
<dt><code>maxclassrepeat</code></dt>
<dd>The maximum number of allowed consecutive characters of the same class in the new password. The check is disabled if the value is 0. (default 0)</dd>
<dt><code>gecoscheck</code></dt>
<dd>If nonzero, check whether the words longer than 3 characters from the <i></i><i>GECOS</i><i></i> field of the user&#8217;s <code><a href="/docs/linux/man/5-passwd/">passwd</a></code>(5) entry are contained in the new password. The check is disabled if the value is 0. (default 0)</dd>
<dt><code>dictcheck</code></dt>
<dd>If nonzero, check whether the password (with possible modifications) matches a word in a dictionary. Currently the dictionary check is performed using the cracklib library. (default 1)</dd>
<dt><code>usercheck=</code><i>N</i></dt>
<dd>If nonzero, check whether the password (with possible modifications) contains the user name in some form. It is not performed for user names shorter than 3 characters. (default 1)</dd>
<dt><code>usersubstr=</code><i>N</i></dt>
<dd>If greater than 3 (due to the minimum length in usercheck), check whether the password contains a substring of at least <i>N</i> length in some form. (default 0)</dd>
<dt><code>enforcing=</code><i>N</i></dt>
<dd>If nonzero, reject the password if it fails the checks, otherwise only print the warning. This setting applies only to the pam_pwquality module and possibly other applications that explicitly change their behavior based on it. It does not affect <code><a href="/docs/linux/man/1-pwmake/">pwmake</a></code>(1) and <code><a href="/docs/linux/man/1-pwscore/">pwscore</a></code>(1). (default 1)</dd>
<dt><code>badwords</code></dt>
<dd>Space separated list of words that must not be contained in the password. These are additional words to the cracklib dictionary check. This setting can be also used by applications to emulate the gecos check for user accounts that are not created yet.</dd>
<dt><code>dictpath</code></dt>
<dd>Path to the cracklib dictionaries. Default is to use the cracklib default.</dd>
<dt><code>retry=</code><i>N</i></dt>
<dd>Prompt user at most <i>N</i> times before returning with error. The default is <i>1</i>.</dd>
<dt><code>enforce_for_root</code></dt>
<dd>The module will return error on failed check even if the user changing the password is root. This option is off by default which means that just the message about the failed check is printed but root can change the password anyway. Note that root is not asked for an old password so the checks that compare the old and new password are not performed.</dd>
<dt><code>local_users_only</code></dt>
<dd>The module will not test the password quality for users that are not present in the <i>/etc/passwd</i> file. The module still asks for the password so the following modules in the stack can use the <code>use_authtok</code> option. This option is off by default.</dd></dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-pwscore/">pwscore</a></code>(1), <code><a href="/docs/linux/man/1-pwmake/">pwmake</a></code>(1), <code><a href="/docs/linux/man/8-pam_pwquality/">pam_pwquality</a></code>(8)</p>
<h2>Authors</h2>
<p>Tomas Mraz &lt;tmraz [at] redhat.com&gt;</p>
