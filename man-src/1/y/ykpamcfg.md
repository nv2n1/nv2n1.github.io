---
title: "ykpamcfg(1)"
name: "ykpamcfg"
section: "1"
letter: "y"
url: "/docs/linux/man/1-ykpamcfg/"
description: "ykpamcfg – Manage user settings for the Yubico PAM module"
---

<h2 class="name">NAME</h2>
<p> ykpamcfg &#8211; Manage user settings for the Yubico PAM module </p>
<h2>SYNOPSIS</h2>
<p> <code>ykmapcfg</code> [-1 | -2] [-A] [-p] [-i] [-v] [-V] [-h]</p>
<h2>OPTIONS</h2>
<p> <code>-1</code></p>
<dl>
<dt>
<dd> use slot 1. This is the default.</dl>
<p> <code>-2</code></p>
<dl>
<dt>
<dd> use slot 2.</dl>
<p> <code>-A</code> <i>action</i></p>
<dl>
<dt>
<dd> choose action to perform. See ACTIONS below.</dl>
<p> <code>-p</code> <i>path</i></p>
<dl>
<dt>
<dd> specify output file for, default is ~/.yubico/challenge</dl>
<p> <code>-i</code> <i>iterations</i></p>
<dl>
<dt>
<dd> number of iterations to use for pbkdf2 of expected response</dl>
<p> <code>-v</code></p>
<dl>
<dt>
<dd> enable verbose mode.</dl>
<p> <code>-V</code></p>
<dl>
<dt>
<dd> display version and exit</dl>
<p> <code>-h</code></p>
<dl>
<dt>
<dd> display help and exit</dl>
<h2>ACTIONS</h2>
<h3>add_hmac_chalresp</h3>
<p> The PAM module can utilize the HMAC-SHA1 Challenge-Response mode found in YubiKeys starting with version 2.2 for <code>offline authentication</code>. This action creates the initial state information with the C/R to be issued at the next logon. </p>
<p> The utility currently outputs the state information to a file in the current user&#8217;s home directory (<i>~/.yubico/challenge-123456</i> for a YubiKey with serial number API readout enabled, and <i>~/.yubico/challenge</i> for one without). </p>
<p> The PAM module supports a system wide directory for these state files (in case the user&#8217;s home directories are encrypted), but in a system wide directory, the <i>challenge</i> part should be replaced with the username. Example : <i>/var/yubico/challenges/alice-123456</i>. </p>
<p> To use the system-wide mode, you currently have to move the generated state files manually and configure the PAM module accordingly.</p>
<h2>EXAMPLES</h2>
<p> First, program a YubiKey for challenge response on Slot 2 : </p>
<dl>
<dt>
<dd>
<pre>
$ ykpersonalize -2 -ochal-resp -ochal-hmac -ohmac-lt64 -oserial-api-visible
...
Commit? (y/n) [n]: y
</pre>
</dl>
<p> Now, set the current user to require this YubiKey for logon : </p>
<dl>
<dt>
<dd>
<pre>
$ ykpamcfg -2 -v
...
Stored initial challenge and expected response in '/home/alice/.yubico/challenge-123456'.
</pre>
</dl>
<p> Then, configure authentication with PAM for example like this (<i>make a backup first</i>) : </p>
<p> <i>/etc/pam.d/common-auth</i> (from Ubuntu 10.10) : </p>
<dl>
<dt>
<dd>
<pre>
auth  required        pam_unix.so nullok_secure try_first_pass
auth  [success=1 new_authtok_reqd=ok ignore=ignore default=die] pam_yubico.so mode=challenge-response
auth  requisite       pam_deny.so
auth  required        pam_permit.so
auth  optional        pam_ecryptfs.so unwrap
</pre>
</dl>
<h2>BUGS</h2>
<p> Report ykpamcfg bugs in the issue tracker: <a rel="nofollow" href="https://github.com/Yubico/yubico-pam/issues">https://github.com/Yubico/yubico-pam/issues</a></p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/8-pam_yubico/">pam_yubico</a></code>(8) </p>
<p> The yubico-pam home page: <a rel="nofollow" href="https://developers.yubico.com/yubico-pam/">https://developers.yubico.com/yubico-pam/</a> </p>
<p> YubiKeys can be obtained from Yubico: <a rel="nofollow" href="http://www.yubico.com/">http://www.yubico.com/</a> </p>
<h2>Index</h2>
