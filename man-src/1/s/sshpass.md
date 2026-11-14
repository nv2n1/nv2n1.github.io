---
title: "sshpass(1)"
name: "sshpass"
section: "1"
letter: "s"
url: "/docs/linux/man/1-sshpass/"
description: "sshpass – noninteractive ssh password provider"
---

<h2 class="name">NAME</h2>
<p> sshpass &#8211; noninteractive ssh password provider </p>
<h2>SYNOPSIS</h2>
<p> <code>sshpass</code> [<code>-f</code><i>filename</i>|<code>-d</code><i>num</i>|<code>-p</code><i>password</i>|<code>-e</code>] [<i>options</i>]<i> command arguments</i> </p>
<h2>DESCRIPTION</h2>
<p> This manual page documents the <code>sshpass</code> command. </p>
<p> <code>sshpass</code> is a utility designed for running <code>ssh</code> using the mode referred to as &quot;keyboard-interactive&quot; password authentication, but in non-interactive mode. </p>
<p> ssh uses direct TTY access to make sure that the password is indeed issued by an interactive keyboard user. Sshpass runs ssh in a dedicated tty, fooling it into thinking it is getting the password from an interactive user. </p>
<p> The command to run is specified after sshpass&#8217; own options. Typically it will be &quot;ssh&quot; with arguments, but it can just as well be any other command. The password prompt used by ssh is, however, currently hardcoded into sshpass.</p>
<h2>Options</h2>
<p> If no option is given, sshpass reads the password from the standard input. The user may give at most one alternative source for the password:</p>
<dl>
<dt><code>-p</code><i>password</i></p>
<dd> The password is given on the command line. Please note the section titled &quot;<code>SECURITY CONSIDERATIONS</code>&quot;.</p>
<dt><code>-f</code><i>filename</i></p>
<dd> The password is the first line of the file <i>filename</i>.</p>
<dt><code>-d</code><i>number</i></p>
<dd> <i>number</i> is a file descriptor inherited by sshpass from the runner. The password is read from the open file descriptor.</p>
<dt><code>-e</code></p>
<dd> The password is taken from the environment variable &quot;SSHPASS&quot;.</p>
<dt><code>-P</code></p>
<dd> Set the password prompt. Sshpass searched for this prompt in the program&#8217;s output to the TTY as an indication when to send the password. By default sshpass looks for the string &quot;assword:&quot; (which matches both &quot;Password:&quot; and &quot;password:&quot;). If your client&#8217;s prompt does not fall under either of these, you can override the default with this option.</p>
<dt><code>-v</code></p>
<dd> Be verbose. sshpass will output to stderr information that should help debug cases where the connection hangs, seemingly for no good reason.</dl>
<h2>SECURITY CONSIDERATIONS</h2>
<p> First and foremost, users of sshpass should realize that ssh&#8217;s insistance on only getting the password interactively is not without reason. It is close to impossible to securely store the password, and users of sshpass should consider whether ssh&#8217;s public key authentication provides the same end-user experience, while involving less hassle and being more secure. </p>
<p> The -p option should be considered the least secure of all of sshpass&#8217;s options. All system users can see the password in the command line with a simple &quot;ps&quot; command. Sshpass makes a minimal attempt to hide the password, but such attempts are doomed to create race conditions without actually solving the problem. Users of sshpass are encouraged to use one of the other password passing techniques, which are all more secure. </p>
<p> In particular, people writing programs that are meant to communicate the password programatically are encouraged to use an anonymous pipe and pass the pipe&#8217;s reading end to sshpass using the -d option.</p>
<h2>RETURN VALUES</h2>
<p> As with any other program, sshpass returns 0 on success. In case of failure, the following return codes are used:</p>
<dl>
<dt>1</p>
<dd> Invalid command line argument</p>
<dt>2</p>
<dd> Conflicting arguments given</p>
<dt>3</p>
<dd> General runtime error</p>
<dt>4</p>
<dd> Unrecognized response from ssh (parse error)</p>
<dt>5</p>
<dd> Invalid/incorrect password</p>
<dt>6</p>
<dd> Host public key is unknown. sshpass exits without confirming the new key.</dl>
<p> In addition, ssh might be complaining about a man in the middle attack. This complaint does not go to the tty. In other words, even with sshpass, the error message from ssh is printed to standard error. In such a case ssh&#8217;s return code is reported back. This is typically an unimaginative (and non-informative) &quot;255&quot; for all error cases.</p>
<h2>EXAMPLES</h2>
<p> Run rsync over SSH using password authentication, passing the password on the command line: </p>
<p> rsync &#8211;rsh=&#8217;sshpass -p 12345 ssh -l test&#8217; host.example.com:path . </p>
<p> To do the same from a bourne shell script in a marginally less exposed way: </p>
<p> SSHPASS=12345 rsync &#8211;rsh=&#8217;sshpass -e ssh -l test&#8217; host.example.com:path .</p>
<h2>BUGS</h2>
<p> Sshpass is in its infancy at the moment. As such, bugs are highly possible. In particular, if the password is read from stdin (no password option at all), it is possible that some of the input aimed to be passed to ssh will be read by sshpass and lost. </p>
<p> Sshpass utilizes the <code><a href="/docs/linux/man/7-pty/">pty</a></code>(7) interface to control the TTY for ssh. This interface, at least on Linux, has a misfeature where if no slave file descriptors are open, the master pty returns <code>EIO</code>. This is the normal behavior, except a slave pty may be born at any point by a program opening <code>/dev/tty</code>. This makes it impossible to reliably wait for events without consuming 100% of the CPU. </p>
<p> Over the various versions different approaches were attempted at solving this problem. Any given version of sshpass is released with the belief that it is working, but experience has shown that these things do, occasionally, break. This happened with OpenSSH version 5.6. As of this writing, it is believed that sshpass is, again, working properly. </p>
<h2>Index</h2>
