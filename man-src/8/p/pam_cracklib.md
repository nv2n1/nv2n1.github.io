---
title: "pam_cracklib(8)"
name: "pam_cracklib"
section: "8"
letter: "p"
url: "/docs/linux/man/8-pam_cracklib/"
description: "pam_cracklib – PAM module to check the password against dictionary words"
---

<p>pam_cracklib &#8211; PAM module to check the password against dictionary words</p>
<h2>Synopsis</h2>
<dl>
<dt> <code>pam_cracklib.so</code> [<i>&#8230;</i>]</dl>
<h2>Description</h2>
<dd>This module can be plugged into the <i>password</i> stack of a given application to provide some plug-in strength-checking for passwords. </p>
<p> The action of this module is to prompt the user for a password and check its strength against a system dictionary and a set of rules for identifying poor choices. </p>
<p> The first action is to prompt for a single password, check its strength and then, if it is considered strong, prompt for the password a second time (to verify that it was typed correctly on the first occasion). All being well, the password is passed on to subsequent modules to be installed as the new authentication token. </p>
<p> The strength checks works in the following manner: at first the <code>Cracklib</code> routine is called to check if the password is part of a dictionary; if this is not the case an additional set of strength checks is done. These checks are: </p>
<p> Palindrome</p>
<dl>
<dd>Is the new password a palindrome?</dl>
<p> Case Change Only</p>
<dl>
<dd>Is the new password the the old one with only a change of case?</dl>
<p> Similar</p>
<dl>
<dd>Is the new password too much like the old one? This is primarily controlled by one argument, <code>difok</code> which is a number of character changes (inserts, removals, or replacements) between the old and new password that are enough to accept the new password. This defaults to 5 changes.</dl>
<p> Simple</p>
<dl>
<dd>Is the new password too small? This is controlled by 6 arguments <code>minlen</code>, <code>maxclassrepeat</code>, <code>dcredit</code>, <code>ucredit</code>, <code>lcredit</code>, and <code>ocredit</code>. See the section on the arguments for the details of how these work and there defaults.</dl>
<p> Rotated</p>
<dl>
<dd>Is the new password a rotated version of the old password?</dl>
<p> Same consecutive characters</p>
<dl>
<dd>Optional check for same consecutive characters.</dl>
<p> Too long monotonic character sequence</p>
<dl>
<dd>Optional check for too long monotonic character sequence.</dl>
<p> Contains user name</p>
<dl>
<dd>Optional check whether the password contains the user&#8217;s name in some form.</dl>
<p> This module with no arguments will work well for standard unix password encryption. With md5 encryption, passwords can be longer than 8 characters and the default settings for this module can make it hard for the user to choose a satisfactory new password. Notably, the requirement that the new password contain no more than 1/2 of the characters in the old password becomes a non-trivial constraint. For example, an old password of the form &quot;the quick brown fox jumped over the lazy dogs&quot; would be difficult to change&#8230; In addition, the default action is to allow passwords as small as 5 characters in length. For a md5 systems it can be a good idea to increase the required minimum size of a password. One can then allow more credit for different kinds of characters but accept that the new password may share most of these characters with the old password.</p>
<h2>Options</h2>
<p><code>debug</code></p>
<dl>
<dd>This option makes the module write information to <code><a href="/docs/linux/man/3-syslog/">syslog</a></code>(3) indicating the behavior of the module (this option does not write password information to the log file).</dl>
<p> <code>authtok_type=</code><i>XXX</i></p>
<dl>
<dd>The default action is for the module to use the following prompts when requesting passwords: &quot;New UNIX password: &quot; and &quot;Retype UNIX password: &quot;. The example word <i>UNIX</i> can be replaced with this option, by default it is empty.</dl>
<p> <code>retry=</code><i>N</i></p>
<dl>
<dd>Prompt user at most <i>N</i> times before returning with error. The default is <i>1</i>.</dl>
<p> <code>difok=</code><i>N</i></p>
<dl>
<dd>This argument will change the default of <i>5</i> for the number of character changes in the new password that differentiate it from the old password.</dl>
<p> <code>minlen=</code><i>N</i></p>
<dl>
<dd>The minimum acceptable size for the new password (plus one if credits are not disabled which is the default). In addition to the number of characters in the new password, credit (of +1 in length) is given for each different kind of character (<i>other</i>, <i>upper</i>, <i>lower</i> and <i>digit</i>). The default for this parameter is <i>9</i> which is good for a old style UNIX password all of the same type of character but may be too low to exploit the added security of a md5 system. Note that there is a pair of length limits in <i>Cracklib</i> itself, a &quot;way too short&quot; limit of 4 which is hard coded in and a defined limit (6) that will be checked without reference to <code>minlen</code>. If you want to allow passwords as short as 5 characters you should not use this module.</dl>
<p> <code>dcredit=</code><i>N</i></p>
<dl>
<dd>(N &gt;= 0) This is the maximum credit for having digits in the new password. If you have less than or <i>N</i> digits, each digit will count +1 towards meeting the current <code>minlen</code> value. The default for <code>dcredit</code> is 1 which is the recommended value for <code>minlen</code> less than 10. </p>
<p> (N &lt; 0) This is the minimum number of digits that must be met for a new password.</dl>
<p> <code>ucredit=</code><i>N</i></p>
<dl>
<dd>(N &gt;= 0) This is the maximum credit for having upper case letters in the new password. If you have less than or <i>N</i> upper case letters each letter will count +1 towards meeting the current <code>minlen</code> value. The default for <code>ucredit</code> is <i>1</i> which is the recommended value for <code>minlen</code> less than 10. </p>
<p> (N &lt; 0) This is the minimum number of upper case letters that must be met for a new password.</dl>
<p> <code>lcredit=</code><i>N</i></p>
<dl>
<dd>(N &gt;= 0) This is the maximum credit for having lower case letters in the new password. If you have less than or <i>N</i> lower case letters, each letter will count +1 towards meeting the current <code>minlen</code> value. The default for <code>lcredit</code> is 1 which is the recommended value for <code>minlen</code> less than 10. </p>
<p> (N &lt; 0) This is the minimum number of lower case letters that must be met for a new password.</dl>
<p> <code>ocredit=</code><i>N</i></p>
<dl>
<dd>(N &gt;= 0) This is the maximum credit for having other characters in the new password. If you have less than or <i>N</i> other characters, each character will count +1 towards meeting the current <code>minlen</code> value. The default for <code>ocredit</code> is 1 which is the recommended value for <code>minlen</code> less than 10. </p>
<p> (N &lt; 0) This is the minimum number of other characters that must be met for a new password.</dl>
<p> <code>minclass=</code><i>N</i></p>
<dl>
<dd>The minimum number of required classes of characters for the new password. The default number is zero. The four classes are digits, upper and lower letters and other characters. The difference to the <code>credit</code> check is that a specific class if of characters is not required. Instead <i>N</i> out of four of the classes are required.</dl>
<p> <code>maxrepeat=</code><i>N</i></p>
<dl>
<dd>Reject passwords which contain more than N same consecutive characters. The default is 0 which means that this check is disabled.</dl>
<p> <code>maxsequence=</code><i>N</i></p>
<dl>
<dd>Reject passwords which contain monotonic character sequences longer than N. The default is 0 which means that this check is disabled. Examples of such sequence are &#8216;12345&#8217; or &#8216;fedcb&#8217;. Note that most such passwords will not pass the simplicity check unless the sequence is only a minor part of the password.</dl>
<p> <code>maxclassrepeat=</code><i>N</i></p>
<dl>
<dd>Reject passwords which contain more than N consecutive characters of the same class. The default is 0 which means that this check is disabled.</dl>
<p> <code>reject_username</code></p>
<dl>
<dd>Check whether the name of the user in straight or reversed form is contained in the new password. If it is found the new password is rejected.</dl>
<p> <code>gecoscheck</code></p>
<dl>
<dd>Check whether the words from the GECOS field (usualy full name of the user) longer than 3 characters in straight or reversed form are contained in the new password. If any such word is found the new password is rejected.</dl>
<p> <code>enforce_for_root</code></p>
<dl>
<dd>The module will return error on failed check also if the user changing the password is root. This option is off by default which means that just the message about the failed check is printed but root can change the password anyway. Note that root is not asked for an old password so the checks that compare the old and new password are not performed.</dl>
<p> <code>use_authtok</code></p>
<dl>
<dd>This argument is used to <i>force</i> the module to not prompt the user for a new password but use the one provided by the previously stacked <i>password</i> module.</dl>
<p> <code>dictpath=</code><i>/path/to/dict</i></p>
<dl>
<dd>Path to the cracklib dictionaries.</dl>
<h2>Module Types Provided</h2>
<p>Only the <code>password</code> module type is provided.</p>
<h2>Return Values</h2>
<p>PAM_SUCCESS</p>
<dl>
<dd>The new password passes all checks.</dl>
<p> PAM_AUTHTOK_ERR</p>
<dl>
<dd>No new password was entered, the username could not be determined or the new password fails the strength checks.</dl>
<p> PAM_AUTHTOK_RECOVERY_ERR</p>
<dl>
<dd>The old password was not supplied by a previous stacked module or got not requested from the user. The first error can happen if <code>use_authtok</code> is specified.</dl>
<p> PAM_SERVICE_ERR</p>
<dl>
<dd>A internal error occurred.</dl>
<h2>Examples</h2>
<p>For an example of the use of this module, we show how it may be stacked with the password component of <code><a href="/docs/linux/man/8-pam_unix/">pam_unix</a></code>(8)</p>
<dl>
<dd>
<pre>#
# These lines stack two password type modules. In this example the
# user is given 3 opportunities to enter a strong password. The
# &quot;use_authtok&quot; argument ensures that the pam_unix module does not
# prompt for a password, but instead uses the one provided by
# pam_cracklib.
#
passwd password required pam_cracklib.so retry=3
passwd password required pam_unix.so use_authtok</pre>
</dl>
<p> Another example (in the /etc/pam.d/passwd format) is for the case that you want to use md5 password encryption:</p>
<dl>
<dd>
<pre>#%PAM-1.0
#
# These lines allow a md5 systems to support passwords of at least 14
# bytes with extra credit of 2 for digits and 2 for others the new
# password must have at least three bytes that are not present in the
# old password
#
password required pam_cracklib.so \
 difok=3 minlen=15 dcredit= 2 ocredit=2
password required pam_unix.so use_authtok nullok md5</pre>
</dl>
<p> And here is another example in case you don&#8217;t want to use credits:</p>
<dl>
<dd>
<pre>#%PAM-1.0
#
# These lines require the user to select a password with a minimum
# length of 8 and with at least 1 digit number, 1 upper case letter,
# and 1 other character
#
password required pam_cracklib.so \
 dcredit=-1 ucredit=-1 ocredit=-1 lcredit=0 minlen=8
password required pam_unix.so use_authtok nullok md5</pre>
</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/5-pam-conf/">pam.conf</a></code>(5), <code><a href="/docs/linux/man/5-pam-d/">pam.d</a></code>(5), <code><a href="/docs/linux/man/8-pam/">pam</a></code>(8)</p>
<h2>Author</h2>
<p>pam_cracklib was written by Cristian Gafton &lt;gafton [at] redhat.com&gt;</p>
