---
title: "passwd(1)"
name: "passwd"
section: "1"
letter: "p"
url: "/docs/linux/man/1-passwd/"
description: "passwd – change user password"
---

<h2 class="name">NAME</h2>
<p> passwd &#8211; change user password </p>
<h2>SYNOPSIS</h2>
<dl>
<dt> <code>passwd</code> [<i>options</i>] [<i>LOGIN</i>]</dl>
<h2>DESCRIPTION</h2>
<dd>The <code>passwd</code> command changes passwords for user accounts. A normal user may only change the password for their own account, while the superuser may change the password for any account. <code>passwd</code> also changes the account or associated password validity period.</p>
<h3>Password Changes</h3>
<p> The user is first prompted for their old password, if one is present. This password is then encrypted and compared against the stored password. The user has only one chance to enter the correct password. The superuser is permitted to bypass this step so that forgotten passwords may be changed. </p>
<p> After the password has been entered, password aging information is checked to see if the user is permitted to change the password at this time. If not, <code>passwd</code> refuses to change the password and exits. </p>
<p> The user is then prompted twice for a replacement password. The second entry is compared against the first and both are required to match in order for the password to be changed. </p>
<p> Then, the password is tested for complexity. As a general guideline, passwords should consist of 6 to 8 characters including one or more characters from each of the following sets: </p>
<dl>
<dt>
<dd> &bull; lower case alphabetics</dl>
<dl>
<dt>
<dd> &bull; digits 0 thru 9</dl>
<dl>
<dt>
<dd> &bull; punctuation marks</dl>
<p> Care must be taken not to include the system default erase or kill characters. <code>passwd</code> will reject any password which is not suitably complex.</p>
<h3>Hints for user passwords</h3>
<p> The security of a password depends upon the strength of the encryption algorithm and the size of the key space. The legacy <i>UNIX</i> System encryption method is based on the NBS DES algorithm. More recent methods are now recommended (see <code>ENCRYPT_METHOD</code>). The size of the key space depends upon the randomness of the password which is selected. </p>
<p> Compromises in password security normally result from careless password selection or handling. For this reason, you should not select a password which appears in a dictionary or which must be written down. The password should also not be a proper name, your license number, birth date, or street address. Any of these may be used as guesses to violate system security. </p>
<p> You can find advice on how to choose a strong password on <a rel="nofollow" href="http://en.wikipedia.org/wiki/Password_strength">http://en.wikipedia.org/wiki/Password_strength</a></p>
<h2>OPTIONS</h2>
<p> The options which apply to the <code>passwd</code> command are: </p>
<p> <code>-a</code>, <code>&#8211;all</code></p>
<dl>
<dt>
<dd> This option can be used only with <code>-S</code> and causes show status for all users.</dl>
<p> <code>-d</code>, <code>&#8211;delete</code></p>
<dl>
<dt>
<dd> Delete a user&#8217;s password (make it empty). This is a quick way to disable a password for an account. It will set the named account passwordless.</dl>
<p> <code>-e</code>, <code>&#8211;expire</code></p>
<dl>
<dt>
<dd> Immediately expire an account&#8217;s password. This in effect can force a user to change their password at the user&#8217;s next login.</dl>
<p> <code>-h</code>, <code>&#8211;help</code></p>
<dl>
<dt>
<dd> Display help message and exit.</dl>
<p> <code>-i</code>, <code>&#8211;inactive</code>&nbsp;<i>INACTIVE</i></p>
<dl>
<dt>
<dd> This option is used to disable an account after the password has been expired for a number of days. After a user account has had an expired password for <i>INACTIVE</i> days, the user may no longer sign on to the account.</dl>
<p> <code>-k</code>, <code>&#8211;keep-tokens</code></p>
<dl>
<dt>
<dd> Indicate password change should be performed only for expired authentication tokens (passwords). The user wishes to keep their non-expired tokens as before.</dl>
<p> <code>-l</code>, <code>&#8211;lock</code></p>
<dl>
<dt>
<dd> Lock the password of the named account. This option disables a password by changing it to a value which matches no possible encrypted value (it adds a &acute;!&acute; at the beginning of the password). </p>
<p> Note that this does not disable the account. The user may still be able to login using another authentication token (e.g. an SSH key). To disable the account, administrators should use <code>usermod &#8211;expiredate 1</code> (this set the account&#8217;s expire date to Jan 2, 1970). </p>
<p> Users with a locked password are not allowed to change their password.</dl>
<p> <code>-n</code>, <code>&#8211;mindays</code>&nbsp;<i>MIN_DAYS</i></p>
<dl>
<dt>
<dd> Set the minimum number of days between password changes to <i>MIN_DAYS</i>. A value of zero for this field indicates that the user may change their password at any time.</dl>
<p> <code>-q</code>, <code>&#8211;quiet</code></p>
<dl>
<dt>
<dd> Quiet mode.</dl>
<p> <code>-r</code>, <code>&#8211;repository</code>&nbsp;<i>REPOSITORY</i></p>
<dl>
<dt>
<dd> change password in <i>REPOSITORY</i> repository</dl>
<p> <code>-R</code>, <code>&#8211;root</code>&nbsp;<i>CHROOT_DIR</i></p>
<dl>
<dt>
<dd> Apply changes in the <i>CHROOT_DIR</i> directory and use the configuration files from the <i>CHROOT_DIR</i> directory.</dl>
<p> <code>-S</code>, <code>&#8211;status</code></p>
<dl>
<dt>
<dd> Display account status information. The status information consists of 7 fields. The first field is the user&#8217;s login name. The second field indicates if the user account has a locked password (L), has no password (NP), or has a usable password (P). The third field gives the date of the last password change. The next four fields are the minimum age, maximum age, warning period, and inactivity period for the password. These ages are expressed in days.</dl>
<p> <code>-u</code>, <code>&#8211;unlock</code></p>
<dl>
<dt>
<dd> Unlock the password of the named account. This option re-enables a password by changing the password back to its previous value (to the value before using the <code>-l</code> option).</dl>
<p> <code>-w</code>, <code>&#8211;warndays</code>&nbsp;<i>WARN_DAYS</i></p>
<dl>
<dt>
<dd> Set the number of days of warning before a password change is required. The <i>WARN_DAYS</i> option is the number of days prior to the password expiring that a user will be warned that their password is about to expire.</dl>
<p> <code>-x</code>, <code>&#8211;maxdays</code>&nbsp;<i>MAX_DAYS</i></p>
<dl>
<dt>
<dd> Set the maximum number of days a password remains valid. After <i>MAX_DAYS</i>, the password is required to be changed. </p>
<p> Passing the number <i>-1</i> as <i>MAX_DAYS</i> will remove checking a password&#8217;s validity.</dl>
<h2>CAVEATS</h2>
<p> Password complexity checking may vary from site to site. The user is urged to select a password as complex as he or she feels comfortable with. </p>
<p> Users may not be able to change their password on a system if NIS is enabled and they are not logged into the NIS server. </p>
<p> <code>passwd</code> uses PAM to authenticate users and to change their passwords.</p>
<h2>FILES</h2>
<p> /etc/passwd</p>
<dl>
<dt>
<dd> User account information.</dl>
<p> /etc/shadow</p>
<dl>
<dt>
<dd> Secure user account information.</dl>
<p> /etc/pam.d/passwd</p>
<dl>
<dt>
<dd> PAM configuration for <code>passwd</code>.</dl>
<h2>EXIT VALUES</h2>
<p> The <code>passwd</code> command exits with the following values: </p>
<p> <i>0</i></p>
<dl>
<dt>
<dd> success</dl>
<p> <i>1</i></p>
<dl>
<dt>
<dd> permission denied</dl>
<p> <i>2</i></p>
<dl>
<dt>
<dd> invalid combination of options</dl>
<p> <i>3</i></p>
<dl>
<dt>
<dd> unexpected failure, nothing done</dl>
<p> <i>4</i></p>
<dl>
<dt>
<dd> unexpected failure, passwd file missing</dl>
<p> <i>5</i></p>
<dl>
<dt>
<dd> passwd file busy, try again</dl>
<p> <i>6</i></p>
<dl>
<dt>
<dd> invalid argument to option</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/8-chpasswd/">chpasswd</a></code>(8), <code><a href="/docs/linux/man/5-passwd/">passwd</a></code>(5), <code><a href="/docs/linux/man/5-shadow/">shadow</a></code>(5), <code><a href="/docs/linux/man/8-usermod/">usermod</a></code>(8). </p>
<h2>Index</h2>
