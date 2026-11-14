---
title: "pam_pwquality(8)"
name: "pam_pwquality"
section: "8"
letter: "p"
url: "/docs/linux/man/8-pam_pwquality/"
description: "pam_pwquality – PAM module to perform password quality checking"
---

<p>pam_pwquality &#8211; PAM module to perform password quality checking</p>
<h2>Synopsis</h2>
<p><code>pam_pwquality.so</code> [<i>&#8230;</i>]</p>
<h2>Description</h2>
<p>This module can be plugged into the <i>password</i> stack of a given service to provide some plug-in strength-checking for passwords. The code was originally based on pam_cracklib module and the module is backwards compatible with its options. </p>
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
<p> These checks are configurable either by use of the module arguments or by modifying the <code>/etc/security/pwquality.conf</code> configuration file.</p>
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
<dd>This argument will change the default of <i>5</i> for the number of changes in the new password from the old password.</dl>
<p> <code>minlen=</code><i>N</i></p>
<dl>
<dd>The minimum acceptable size for the new password (plus one if credits are not disabled which is the default). In addition to the number of characters in the new password, credit (of +1 in length) is given for each different kind of character (<i>other</i>, <i>upper</i>, <i>lower</i> and <i>digit</i>). The default for this parameter is <i>9</i> . Note that there is a pair of length limits also in <i>Cracklib</i>, which is used for dictionary checking, a &quot;way too short&quot; limit of 4 which is hard coded in and a build time defined limit (6) that will be checked without reference to <code>minlen</code>.</dl>
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
<p> <code>gecoscheck=</code><i>N</i></p>
<dl>
<dd>If nonzero, check whether the individual words longer than 3 characters from the <code>passwd GECOS</code> field of the user are contained in the new password. The default is 0 which means that this check is disabled.</dl>
<p> <code>badwords=</code><i>&lt;list of words&gt;</i></p>
<dl>
<dd>The words more than 3 characters long from this space separated list are individually searched for and forbidden in the new password. By default the list is empty which means that this check is disabled.</dl>
<p> <code>enforce_for_root</code></p>
<dl>
<dd>The module will return error on failed check even if the user changing the password is root. This option is off by default which means that just the message about the failed check is printed but root can change the password anyway. Note that root is not asked for an old password so the checks that compare the old and new password are not performed.</dl>
<p> <code>local_users_only</code></p>
<dl>
<dd>The module will not test the password quality for users that are not present in the <i>/etc/passwd</i> file. The module still asks for the password so the following modules in the stack can use the <code>use_authtok</code> option. This option is off by default.</dl>
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
# pam_pwquality.
#
passwd password required pam_pwquality.so retry=3
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
password required pam_pwquality.so \
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
password required pam_pwquality.so \
 dcredit=-1 ucredit=-1 ocredit=-1 lcredit=0 minlen=8
password required pam_unix.so use_authtok nullok md5</pre>
</dl>
<h2>See Also</h2>
<p><a href="/docs/linux/man/1-pwscore/">pwscore</a>(1), <a href="/docs/linux/man/5-pwquality-conf/">pwquality.conf</a>(5), <a href="/docs/linux/man/8-pam_pwquality/">pam_pwquality</a>(8), <a href="/docs/linux/man/5-pam-conf/">pam.conf</a>(5), <a href="/docs/linux/man/8-pam/">PAM</a>(8) </p>
<h2>Authors</h2>
<pre>Tomas Mraz &lt;tmraz [at] redhat.com&gt;
Original author of pam_cracklib module Cristian Gafton &lt;gafton [at] redhat.com&gt;</pre>
