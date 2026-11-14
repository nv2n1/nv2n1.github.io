---
title: "ckpasswd(8)"
name: "ckpasswd"
section: "8"
letter: "c"
url: "/docs/linux/man/8-ckpasswd/"
description: "ckpasswd – nnrpd password authenticator"
---

<p>ckpasswd &#8211; nnrpd password authenticator</p>
<h2>Synopsis</h2>
<p><code>ckpasswd</code> [<code>-gs</code>] [<code>-d</code> <i>database</i>] [<code>-f</code> <i>filename</i>] [<code>-u</code> <i>username</i> <code>-p</code> <i>password</i>]</p>
<h2>Description</h2>
<p><code>ckpasswd</code> is the basic password authenticator for <code>nnrpd</code>, suitable for being run from an auth stanza in <i>readers.conf</i>. See <i><a href="/docs/linux/man/5-readers-conf/">readers.conf</a></i>(5) for more information on how to configure an <code>nnrpd</code> authenticator. </p>
<p> <code>ckpasswd</code> accepts a username and password from <code>nnrpd</code> and tells <i><a href="/docs/linux/man/8-nnrpd/">nnrpd</a></i>(8) whether that&#8217;s the correct password for that username. By default, when given no arguments, it tries to check the password using <font SIZE="-1">PAM</font> if support for <font SIZE="-1">PAM</font> was found when <font SIZE="-1">INN</font> was built. Failing that, it tries to check the password against the password field returned by <i><a href="/docs/linux/man/3-getpwnam/">getpwnam</a></i>(3). Note that these days most systems no longer make real passwords available via <i><a href="/docs/linux/man/3-getpwnam/">getpwnam</a></i>(3) (some still do if and only if the program calling <i><a href="/docs/linux/man/3-getpwnam/">getpwnam</a></i>(3) is running as root). </p>
<p> When using <font SIZE="-1">PAM</font>, <code>ckpasswd</code> identifies itself as <tt>&quot;nnrpd&quot;</tt>, not as <tt>&quot;ckpasswd&quot;</tt>, and the <font SIZE="-1">PAM</font> configuration must be set up accordingly. The details of <font SIZE="-1">PAM</font> configuration are different on different operating systems (and even different Linux distributions); see <font SIZE="-1">EXAMPLES</font> below for help getting started, and look for a <i><a href="/docs/linux/man/7-pam/">pam</a></i>(7) or <i><a href="/docs/linux/man/4-pam-conf/">pam.conf</a></i>(4) manual page on your system. </p>
<p> When using any method other than <font SIZE="-1">PAM</font>, <code>ckpasswd</code> expects all passwords to be stored encrypted by the system <i><a href="/docs/linux/man/3-crypt/">crypt</a></i>(3) function and calls <i><a href="/docs/linux/man/3-crypt/">crypt</a></i>(3) on the supplied password before comparing it to the expected password. If you&#8217;re using a different password hash scheme (like <font SIZE="-1">MD5</font>), you must use <font SIZE="-1">PAM</font>.</p>
<h2>Options</h2>
<dl>
<dt><code>-d</code> <i>database</i></p>
<dd>Read passwords from a database (ndbm, gdbm or dbm format depending on what your system has) rather than by using <i><a href="/docs/linux/man/3-getpwnam/">getpwnam</a></i>(3). <code>ckpasswd</code> expects <i>database</i>.dir and <i>database</i>.pag to exist and to be a database keyed by username with the encrypted passwords as the values. </p>
<p> While <font SIZE="-1">INN</font> doesn&#8217;t come with a program intended specifically to create such databases, on most systems it&#8217;s fairly easy to write a Perl script to do so. Something like: </p>
<pre> #!/usr/bin/perl
 use NDBM_File;
 use Fcntl;
 tie (%db, 'NDBM_File', '/path/to/database', O_RDWR|O_CREAT, 0640)
 or die &quot;Cannot open /path/to/database: $!
&quot;;
 $| = 1;
 print &quot;Username: &quot;;
 my $user = &lt;STDIN&gt;;
 chomp $user;
 print &quot;Password: &quot;;
 my $passwd = &lt;STDIN&gt;;
 chomp $passwd;
 my @alphabet = ('.', '/', 0..9, 'A'..'Z', 'a'..'z');
 my $salt = join '', @alphabet[rand 64, rand 64];
 $db{$user} = crypt ($passwd, $salt);
 untie %db;</pre>
<p>Note that this will echo back the password when typed; there are obvious improvements that could be made to this, but it should be a reasonable start. Sometimes a program like this will be available with the name <code>dbmpasswd</code>. </p>
<p> This option will not be available on systems without ndbm, gdbm or dbm libraries.</p>
<dt><code>-f</code> <i>filename</i></p>
<dd>Read passwords from the given file rather than using <i><a href="/docs/linux/man/3-getpwnam/">getpwnam</a></i>(3). The file is expected to be formatted like a system password file, at least vaguely. That means each line should look something like: </p>
<pre> username:pdIh9NCNslkq6</pre>
<p>(and each line may have an additional colon after the encrypted password and additional data; that data will be ignored by <code>ckpasswd</code>). Lines starting with a number sign (<tt>&quot;#&quot;</tt>) are ignored. <font SIZE="-1">INN</font> does not come with a utility to create the encrypted passwords, but <code>htpasswd</code> (which comes with Apache) can do so and it&#8217;s a quick job with Perl (see the example script under <code>-d</code>, or also below). If using Apache&#8217;s <code>htpasswd</code> program, be sure to give it the <code>-d</code> option so that it will use <i><a href="/docs/linux/man/3-crypt/">crypt</a></i>(3). </p>
<p> A line in <i>filename</i> for the user <tt>&quot;user&quot;</tt> with the password <tt>&quot;pass&quot;</tt> would be <tt>&quot;user:LIfOpbjNaEQYE&quot;</tt> as obtained by the following commands: </p>
<pre> % htpasswd -nbd user pass
 user:LIfOpbjNaEQYE
 % perl -e 'print &quot;user:&quot;.crypt(&quot;pass&quot;, &quot;LI&quot;).&quot;
&quot;;'
 user:LIfOpbjNaEQYE</pre>
<dt><code>-g</code></p>
<dd>Attempt to look up system group corresponding to username and return a string like <tt>&quot;user [at] group&quot;</tt> to be matched against in <i>readers.conf</i>. This option is incompatible with the <code>-d</code> and <code>-f</code> options.</p>
<dt><code>-p</code> <i>password</i></p>
<dd>Use <i>password</i> as the password for authentication rather than reading a password using the <code>nnrpd</code> authenticator protocol. This option is useful only for testing your authentication system (particularly since it involves putting a password on the command line), and does not work when <code>ckpasswd</code> is run by <code>nnrpd</code>. If this option is given, <code>-u</code> must also be given.</p>
<dt><code>-s</code></p>
<dd>Check passwords against the result of <i><a href="/docs/linux/man/3-getspnam/">getspnam</a></i>(3) instead of <i><a href="/docs/linux/man/3-getpwnam/">getpwnam</a></i>(3). This function, on those systems that supports it, reads from <i>/etc/shadow</i> or similar more restricted files. If you want to check passwords supplied to <i><a href="/docs/linux/man/8-nnrpd/">nnrpd</a></i>(8) against system account passwords, you will probably have to use this option on most systems. </p>
<p> Most systems require special privileges to call <i><a href="/docs/linux/man/3-getspnam/">getspnam</a></i>(3), so in order to use this option you may need to make <code>ckpasswd</code> setgid to some group (like group <tt>&quot;shadow&quot;</tt>) or even setuid root. <code>ckpasswd</code> has not been specifically audited for such uses! It is, however, a very small program that you should be able to check by hand for security. </p>
<p> This configuration is not recommended if it can be avoided, for serious security reasons. See &#8220;<font SIZE="-1">SECURITY</font> <font SIZE="-1">CONSIDERATIONS</font>&#8221; in <i><a href="/docs/linux/man/5-readers-conf/">readers.conf</a></i>(5) for discussion.</p>
<dt><code>-u</code> <i>username</i></p>
<dd>Authenticate as <i>username</i>. This option is useful only for testing (so that you can test your authentication system easily) and does not work when <code>ckpasswd</code> is run by <code>nnrpd</code>. If this option is given, <code>-p</code> must also be given.</dl>
<h2>Examples</h2>
<p>See <i><a href="/docs/linux/man/5-readers-conf/">readers.conf</a></i>(5) for examples of <i><a href="/docs/linux/man/8-nnrpd/">nnrpd</a></i>(8) authentication configuration that uses <code>ckpasswd</code> to check passwords. </p>
<p> An example <font SIZE="-1">PAM</font> configuration for <i>/etc/pam.conf</i> that tells <code>ckpasswd</code> to check usernames and passwords against system accounts is: </p>
<pre> nnrpd auth required pam_unix.so
 nnrpd account required pam_unix.so</pre>
<p>Your system may want you to instead create a file named <i>nnrpd</i> in <i>/etc/pam.d</i> with lines like: </p>
<pre> auth required pam_unix.so
 account required pam_unix.so</pre>
<p>This is only the simplest configuration. You may be able to include common shared files, and you may want to stack other modules, either to allow different authentication methods or to apply restrictions like lists of users who can&#8217;t authenticate using <code>ckpasswd</code>. The best guide is the documentation for your system and the other <font SIZE="-1">PAM</font> configurations you&#8217;re already using. </p>
<p> To test to make sure that <code>ckpasswd</code> is working correctly, you can run it manually and then give it the username (prefixed with <tt>&quot;ClientAuthname:&quot;</tt>) and password (prefixed with <tt>&quot;ClientPassword:&quot;</tt>) on standard input. For example: </p>
<pre> (echo 'ClientAuthname: test' ; echo 'ClientPassword: testing') \
 | ckpasswd -f /path/to/passwd/file</pre>
<p>will check a username of <tt>&quot;test&quot;</tt> and a password of <tt>&quot;testing&quot;</tt> against the username and passwords stored in <i>/path/to/passwd/file</i>. On success, <code>ckpasswd</code> will print <tt>&quot;User:test&quot;</tt> and exit with status <tt>0</tt>. On failure, it will print some sort of error message and exit a non-zero status.</p>
<h2>History</h2>
<p>Written by Russ Allbery &lt;eagle [at] eyrie.org&gt; for InterNetNews. </p>
<p> <tt>$Id:</tt> ckpasswd.pod 9768 2014-12-07 21:22:57Z iulius $</p>
<h2>See Also</h2>
<p><i><a href="/docs/linux/man/3-crypt/">crypt</a></i>(3), <i><a href="/docs/linux/man/8-nnrpd/">nnrpd</a></i>(8), <i><a href="/docs/linux/man/7-pam/">pam</a></i>(7), <i><a href="/docs/linux/man/5-readers-conf/">readers.conf</a></i>(5). </p>
