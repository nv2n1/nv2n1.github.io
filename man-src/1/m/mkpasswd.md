---

title: "mkpasswd(1)"
name: "mkpasswd"
section: "1"
letter: "m"
url: "/docs/linux/man/1-mkpasswd/"
description: "mkpasswd – Overfeatured front end to"
---

<p> <a href="/docs/linux/man/3-crypt/">crypt</a>(3)</p>
<p> <code>mkpasswd</code> <i>PASSWORD</i> [<i>SALT</i>]</p>
<p> <code>mkpasswd</code> encrypts the given password with the <code><a href="/docs/linux/man/3-crypt/">crypt</a></code>(3) libc function, using the given salt.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-S</code>,</dt>
<dd> <code>&#8211;salt=</code><i>STRING</i> Use the <i>STRING</i> as salt. If it begins with <i>$</i> then it will be passed straight to <code><a href="/docs/linux/man/3-crypt/">crypt</a></code>(3) without any checks.</dd>
<dt><code>-R</code>,</dt>
<dd> <code>&#8211;rounds=</code><i>NUMBER</i> Use <i>NUMBER</i> rounds. This argument is ignored if the method chosen does not support variable rounds. For the OpenBSD Blowfish method this is the logarithm of the number of rounds. The behavior is undefined if this option is used without <i>&#8211;method</i>.</dd>
<dt><code>-m</code>,</dt>
<dd> <code>&#8211;method=</code><i>TYPE</i> Compute the password using the <i>TYPE</i> method. If <i>TYPE</i> is <i>help</i> then the list of available methods is printed. If <i>TYPE</i> begins and end with <i>$</i> characters then the string is passed to <i><a href="/docs/linux/man/3-crypt_gensalt/">crypt_gensalt</a></i>(3) as-is.</dd>
<dt><code>-5</code></dt>
<dd> Like <i>&#8211;method=md5crypt</i>.</dd>
<dt><code>-P </code></dt>
<dd> <i>NUM</i>, <code>&#8211;password-fd=</code><i>NUM</i> Read the password from file descriptor <i>NUM</i> instead of using <i><a href="/docs/linux/man/3-getpass/">getpass</a></i>(3). If the file descriptor is not connected to a tty then no other text than the hashed password is printed on stdout.</dd>
<dt><code>-s</code>, <code>&#8211;stdin</code></dt>
<dd> Like <i>&#8211;password-fd=0</i>.</dd></dl>
<h2>ENVIRONMENT</h2>
<dl>
<dt>MKPASSWD_OPTIONS</dt>
<dd> A list of options which will be evaluated before the ones specified on the command line.</dd></dl>
<h2>BUGS</h2>
<p> If the <i>&#8211;stdin</i> option is used then passwords containing some control characters may not be read correctly. </p>
<p> This program suffers of a bad case of featuritis.</p>
<h2>SEE ALSO</h2>
<p> <i><a href="/docs/linux/man/1-passwd/">passwd</a></i>(1), <i><a href="/docs/linux/man/5-passwd/">passwd</a></i>(5), <i><a href="/docs/linux/man/3-crypt/">crypt</a></i>(3), <i><a href="/docs/linux/man/5-crypt/">crypt</a></i>(5), <i><a href="/docs/linux/man/3-crypt_gensalt/">crypt_gensalt</a></i>(3), <i><a href="/docs/linux/man/3-getpass/">getpass</a></i>(3).</p>
<h2>AUTHOR</h2>
<p> <code>mkpasswd</code> and this man page were written by Marco d&#8217;Itri &lt;<i>md [at] linux.it</i>&gt; and are licensed under the terms of the GNU General Public License, version 2 or higher. </p>
