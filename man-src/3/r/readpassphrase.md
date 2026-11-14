---
title: "readpassphrase(3)"
name: "readpassphrase"
section: "3"
letter: "r"
url: "/docs/linux/man/3-readpassphrase/"
description: "readpassphrase – get a passphrase from the user"
---

<p><code>readpassphrase</code> &#8211; get a passphrase from the user</p>
<h2>Library</h2>
<p>Lb libbsd</p>
<h2>Synopsis</h2>
<pre><code>Fd #include &lt;bsd/readpassphrase.h&gt;

Ft char *

Fn readpassphrase const char *prompt char *buf size_t bufsiz int flags</code></pre>
<h2>Description</h2>
<p>The Fn readpassphrase function displays a prompt to, and reads in a passphrase from, /dev/tty If this file is inaccessible and the <code>RPP_REQUIRE_TTY</code> flag is not set, Fn readpassphrase displays the prompt on the standard error output and reads from the standard input. In this case it is generally not possible to turn off echo. </p>
<p> Up to Fa bufsiz &#8211; 1 characters (one is for the NUL) are read into the provided buffer Fa buf . Any additional characters and the terminating newline (or return) character are discarded. </p>
<p> Fn readpassphrase takes the following optional Fa flags : </p>
<blockquote>
<pre>RPP_ECHO_OFF turn off echo (default behavior)
RPP_ECHO_ON leave echo on
RPP_REQUIRE_TTY fail if there is no tty
RPP_FORCELOWER force input to lower case
RPP_FORCEUPPER force input to upper case
RPP_SEVENBIT strip the high bit from input
RPP_STDIN force read of passphrase from stdin</pre>
</blockquote>
<p> The calling process should zero the passphrase as soon as possible to avoid leaving the cleartext passphrase visible in the process&#8217;s address space.</p>
<h2>Return Values</h2>
<p>Upon successful completion, Fn readpassphrase returns a pointer to the NUL-terminated passphrase. If an error is encountered, the terminal state is restored and a null pointer is returned.</p>
<h2>Files</h2>
<dl>
<dt><code>/dev/tty </code></p>
<dd></dl>
<h2>Examples</h2>
<p>The following code fragment will read a passphrase from /dev/tty into the buffer Fa passbuf . </p>
<blockquote>
<pre>char passbuf[1024];
...
if (readpassphrase(&quot;Response: &quot;, passbuf, sizeof(passbuf),
 RPP_REQUIRE_TTY) == NULL)
 errx(1, &quot;unable to read passphrase&quot;);
if (compare(transform(passbuf), epass) != 0)
 errx(1, &quot;bad passphrase&quot;);
...
memset(passbuf, 0, sizeof(passbuf));</pre>
</blockquote>
<h2>Errors</h2>
<dt><code>Bq </code>Er EINTR</p>
<dd>The Fn readpassphrase function was interrupted by a signal.</p>
<dt><code>Bq </code>Er EINVAL</p>
<dd>The <i>bufsiz</i> argument was zero.</p>
<dt><code>Bq </code>Er EIO</p>
<dd>The process is a member of a background process attempting to read from its controlling terminal, the process is ignoring or blocking the <code>SIGTTIN</code> signal, or the process group is orphaned.</p>
<dt><code>Bq </code>Er EMFILE</p>
<dd>The process has already reached its limit for open file descriptors.</p>
<dt><code>Bq </code>Er ENFILE</p>
<dd>The system file table is full.</p>
<dt><code>Bq </code>Er ENOTTY</p>
<dd>There is no controlling terminal and the <code>RPP_REQUIRE_TTY</code> flag was specified.</dl>
<h2>Signals</h2>
<p>Fn readpassphrase will catch the following signals: </p>
<blockquote>
<pre>SIGALRM SIGHUP SIGINT
SIGPIPE SIGQUIT SIGTERM
SIGTSTP SIGTTIN SIGTTOU</pre>
</blockquote>
<p> When one of the above signals is intercepted, terminal echo will be restored if it had previously been turned off. If a signal handler was installed for the signal when Fn readpassphrase was called, that handler is then executed. If no handler was previously installed for the signal then the default action is taken as per <a href="/docs/linux/man/2-sigaction/">sigaction</a>(2). </p>
<p> The <code>SIGTSTP</code> <code>SIGTTIN</code> and <code>SIGTTOU</code> signals (stop signals generated from keyboard or due to terminal I/O from a background process) are treated specially. When the process is resumed after it has been stopped, Fn readpassphrase will reprint the prompt and the user may then enter a passphrase.</p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/2-sigaction/">sigaction</a>(2), <a href="/docs/linux/man/3-getpass/">getpass</a>(3)</p>
<h2>Standards</h2>
<p>The Fn readpassphrase function is an Ox extension and should not be used if portability is desired.</p>
<h2>History</h2>
<p>The Fn readpassphrase function first appeared in Ox 2.9 .</p>
