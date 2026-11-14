---
title: "startpar(8)"
name: "startpar"
section: "8"
letter: "s"
url: "/docs/linux/man/8-startpar/"
description: "startpar – start runlevel scripts in parallel"
---

<p>startpar &#8211; start runlevel scripts in parallel</p>
<h2>Synopsis</h2>
<p><code>startpar</code> [<code>-p</code> <i>par</i>] [<code>-i</code> <i>iorate</i>] [<code>-t</code> <i>timeout</i>] [<code>-T</code> <i>global_timeout</i>] [<code>-a</code> <i>arg</i>] <code>prg1</code> <code>prg2</code> <code>&#8230;</code><br />
 <code>startpar</code> [<code>-p</code> <i>par</i>] [<code>-i</code> <i>iorate</i>] [<code>-t</code> <i>timeout</i>] [<code>-T</code> <i>global_timeout</i>] <code>-M [</code> <i>boot</i>|<i>start</i>|<i>stop</i>] </p>
<h2>Description</h2>
<p>startpar is used to run multiple run-level scripts in parallel. The degree of parallelism on one <code>CPU</code> can be set with the <code>-p</code> option, the default is full parallelism. An argument to all of the scripts can be provided with the <code>-a</code> option. Processes blocked by pending <code>I/O</code> will cause new process creation to be weighted by the iorate factor <i>800</i>. To change this factor the option <code>-i</code> can be used to specify another value. The amount weight = (nblocked times iorate) / 1000 will be subtracted from the total number of processes which could be started, where nblocked is the number of processes currently blocked by pending I/O. The output of each script is buffered and written when the script exits, so output lines of different scripts won&#8217;t mix. You can modify this behaviour by setting a timeout. The timeout set with the <code>-t</code> option is used as buffer timeout. If the output buffer of a script is not empty and the last output was <i>timeout</i> seconds ago, startpar will flush the buffer. The <code>-T</code> option timeout works more globally. If no output is printed for more than <i>global_timeout</i> seconds, startpar will flush the buffer of the script with the oldest output. Afterwards it will only print output of this script until it is finished. The <code>-M</code> option switches <code>startpar</code> into a <code><a href="/docs/linux/man/1-make/">make</a></code>(1) like behaviour. This option takes three different arguments: <i>boot</i>, <i>start</i>, and <i>stop</i> for reading <i>.depend.boot</i> or <i>.depend.start</i> or <i>.depend.stop</i> respectively in the directory <i>/etc/init.d/</i>. By scanning the boot and runlevel directories in <i>/etc/init.d/</i> it then executes the appropriate scripts in parallel. </p>
<h2>Files</h2>
<p><i>/etc/init.d/.depend.boot</i><br />
 <i>/etc/init.d/.depend.start</i><br />
 <i>/etc/init.d/.depend.stop</i></p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-init/">init</a></code>(8) <code><a href="/docs/linux/man/8-insserv/">insserv</a></code>(8). </p>
<h2>Copyright</h2>
<p>2003,2004 SuSE Linux AG, Nuernberg, Germany.<br />
 2007 SuSE LINUX Products GmbH, Nuernberg, Germany.</p>
<h2>Author</h2>
<p>Michael Schroeder &lt;mls [at] suse.de&gt;<br />
 Takashi Iwai &lt;tiwai [at] suse.de&gt;<br />
 Werner Fink &lt;werner [at] suse.de&gt;</p>
