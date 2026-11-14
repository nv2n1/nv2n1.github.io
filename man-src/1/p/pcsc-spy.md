---
title: "pcsc-spy(1)"
name: "pcsc-spy"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pcsc-spy/"
description: "pcsc-spy – A PC/SC spy command"
---

<h2 class="name">NAME</h2>
<p> pcsc-spy &#8211; A PC/SC spy command </p>
<h2>SYNOPSIS</h2>
<p> pcsc-spy [<code>-n</code>|<code>&#8211;nocolor</code>] [<code>-d</code>|<code>&#8211;diffable</code>] [<code>-h</code>|<code>&#8211;help</code>] [<i>fifo_filename</i>]</p>
<h2>DESCRIPTION</h2>
<p> pcsc-spy displays <font SIZE="-1">PC/SC</font> calls of an application. It must be used with the <i>libpcscspy.so</i> library. </p>
<p> To be able to spy the <font SIZE="-1">PC/SC</font> layer, the application flow must be modified so that all <font SIZE="-1">PC/SC</font> calls are redirected. Two options are available:</p>
<dl>
<dt>&#8211; the application is linked with <i>libpcsclite.so.1</i></p>
<dd>
<dt>&#8211; the application loads the <i>libpcsclite.so.1</i> library using <i><a href="/docs/linux/man/3-dlopen/">dlopen</a></i>(3)</p>
<dd></dl>
<h2>OPTIONS</h2>
<dl>
<dt><code>-d</code>, <code>&#8211;diffable</code></p>
<dd> Demove the variable parts (like handler values) from the output so that two execution can be more easily compared.</p>
<dt><code>-h</code>, <code>&#8211;help</code></p>
<dd> Display a short help text.</p>
<dt><code>-n</code>, <code>&#8211;nocolor</code></p>
<dd> Disable the output colorization (if you want redirect the output in a file for example).</p>
<dt><code>-v</code>, <code>&#8211;version</code></p>
<dd> Print the version of the <i>pcsc-spy</i> program plus a copyright, a list of authors.</dl>
<h2>EXAMPLES</h2>
<h3>Applications linked with libpcsclite.so.1</h3>
<p> We will use the standard <font SIZE="-1">LD_PRELOAD</font> loader option to load our spying library. </p>
<p> Example:<br />
&nbsp;<wbr>LD_PRELOAD=/usr/lib/libpcscspy.so pcsc_scan</p>
<h3>Application loading libpcsclite.so.1</h3>
<p> This is the case for the <font SIZE="-1">PC/SC</font> wrappers like pyscard (for Python) and pcsc-perl (for Perl). The <font SIZE="-1">LD_PRELOAD</font> mechanism can&#8217;t be used. Instead we replace the <i>libpcsclite.so.1</i> library by the spying one. </p>
<p> You may use <i>install_spy.sh</i> and <i>uninstall_spy.sh</i> to install and uninstall the spying library. </p>
<p> Using the spying library without <i>pcsc-spy</i> is not a problem but has side effects: </p>
<p> &#8211; a line &#8220;libpcsclite_nospy.so.1: cannot open shared object file: No such file or directory&#8221; will be displayed </p>
<p> &#8211; some <font SIZE="-1">CPU</font> time will be lost because of the <font SIZE="-1">PC/SC</font> calls redirection</p>
<h3>Starting the spy tool</h3>
<pre>
 pcsc-spy
</pre>
<p> If a command argument is passed we use it instead of the default <i>~/pcsc-spy</i> <font SIZE="-1">FIFO</font> file. It is then possible to record an execution log and use pcsc-spy multiple times on the same log. </p>
<p> To create the log file just do: </p>
<pre>
 mkfifo ~/pcsc-spy
 cat ~/pcsc-spy &gt; logfile
</pre>
<p> and run your <font SIZE="-1">PC/SC</font> application.</p>
<h3>Mac <font SIZE="-1">OS X</font></h3>
<p> The installation is not automatic. In the pcsc-lite/src/spy directory do:<br />
&nbsp;<wbr>make framework </p>
<p> Then copy the <font SIZE="-1">PCSC</font>.framework directory in /tmp<br />
&nbsp;<wbr>cp -a&nbsp;<wbr><font SIZE="-1">PCSC</font>.framework&nbsp;<wbr>/tmp </p>
<p> Copy the official <font SIZE="-1">PCSC</font>.framework (binary only) in /tmp<br />
&nbsp;<wbr>cp&nbsp;<wbr>/System/Library/Frameworks/PCSC.framework/PCSC&nbsp;<wbr>/tmp </p>
<p> Run the application to debug as:<br />
&nbsp;<wbr>DYLD_FRAMEWORK_PATH=/tmp pcsctest</p>
<h2>FILES</h2>
<p> <i>~/pcsc-spy</i> <font SIZE="-1">FIFO</font> file is used by <i>libpcsclite.so.1</i> to send the raw log lines</p>
<h2>SEE ALSO</h2>
<p> <i><a href="/docs/linux/man/8-pcscd/">pcscd</a></i>(8)</p>
<h2>AUTHOR</h2>
<p> This manual page was written by Ludovic Rousseau &lt;rousseau [at] free.fr&gt; </p>
<h2>Index</h2>
<dt><a href="#lbAK">FILES</a></p>
<dd>
<dt><a href="#lbAL">SEE ALSO</a></p>
<dd>
<dt><a href="#lbAM">AUTHOR</a></p>
<dd></dl>
