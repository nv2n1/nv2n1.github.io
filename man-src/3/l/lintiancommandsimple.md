---
title: "lintiancommandsimple(3)"
name: "lintiancommandsimple"
section: "3"
letter: "l"
url: "/docs/linux/man/3-lintiancommandsimple/"
description: "Lintian::Command::Simple – Run commands without pipes"
---

<p>Lintian::Command::Simple &#8211; Run commands without pipes </p>
<h2>Synopsis</h2>
<pre> use Lintian::Command::Simple qw(wait_any);
 my %pid_info;
 my $pid = fork() // die(&quot;fork: $!&quot;);
 exec('do', 'something') if $pid == 0;
 $pid_info{$pid} = &quot;A useful value associated with $pid&quot;;
 my ($termiated_pid, $value) = wait_any(\%pid_info);
 ...;</pre>
<h2>Description</h2>
<p>Lintian::Command::Simple allows running commands with the capability of running them &#8220;in the background&#8221; (asynchronously.) </p>
<p> Pipes are not handled at all, except for those handled internally by the shell. See &#8216;perldoc -f exec&#8217;s note about shell metacharacters. If you want to pipe to/from Perl, look at Lintian::Command instead.</p>
<dl COMPACT>
<dt>wait_any (hashref[, nohang])</p>
<dd>When starting multiple processes asynchronously, it is common to wait until the first is done. While the <code>CORE::wait()</code> function is usually used for that very purpose, it does not provide the desired results when the processes were started via the <font SIZE="-1">OO</font> interface. </p>
<p> To help with this task, <code>wait_any()</code> can take a hash ref where the key of each entry is the pid of that command. There are no requirements for the value (which can be used for any application specific purpose). </p>
<p> Under this mode, <code>wait_any()</code> waits until any child process is done. The key (and value) associated the pid of the reaped child will then be removed from the hashref. The exitcode of the child is available via <tt>$?</tt> as usual. </p>
<p> The results and return value are undefined when under this mode <code>wait_any()</code> &#8220;accidentally&#8221; reaps a process not listed in the hashref. </p>
<p> The return value in scalar context is value associated with the pid of the reaped processed. In list context, the pid and value are returned as a pair. </p>
<p> Whenever <code>waitpid()</code> would return -1, <code>wait_any()</code> returns undef or a null value so that it is safe to: </p>
<pre> while($cmd = wait_any(\%hash)) { something; }</pre>
<p>The same is true whenever the hash reference points to an empty hash. </p>
<p> If <tt>&quot;nohang&quot;</tt> is also given, wait_any will attempt to reap any child process non-blockingly. If no child can be reaped, it will immediately return (like there were no more processes left) instead of waiting.</p>
<dt>kill_all(hashref[, signal])</p>
<dd>In a similar way to <code>wait_any()</code>, it is possible to pass a hash reference to <code>kill_all()</code>. It will then kill all of the processes (default signal being &#8220;<font SIZE="-1">TERM&#8221;</font>) followed by a reaping of the processes. All reaped processes (and their values) will be removed from the set. </p>
<p> Any entries remaining in the hashref are processes that did not terminate (or did not terminate yet).</dl>
<h2>Notes</h2>
<p>Unless specified by prefixing the package name, every reference to a function/method in this documentation refers to the functions/methods provided by this package itself.</p>
<h2>Caveats</h2>
<p>Combining asynchronous jobs (e.g. via Lintian::Command) and calls to <code>wait_any()</code> can lead to unexpected results.</p>
<h2>Author</h2>
<p>Originally written by Raphael Geissert &lt;atomo64 [at] gmail.com&gt; for Lintian.</p>
