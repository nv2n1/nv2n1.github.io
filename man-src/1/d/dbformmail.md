---
title: "dbformmail(1)"
name: "dbformmail"
section: "1"
letter: "d"
url: "/docs/linux/man/1-dbformmail/"
description: "dbformmail – write a shell script that will send e-mail to many people"
---

<h2 class="name">NAME</h2>
<p> dbformmail &#8211; write a shell script that will send e-mail to many people </p>
<h2>SYNOPSIS</h2>
<p> dbformmail [-m <font SIZE="-1">MECHANISM</font>] format_file.txt</p>
<h2>DESCRIPTION</h2>
<p> Read a &#8220;form mail&#8221; message from the file <font SIZE="-1">FORMAT_FILE.TXT,</font> filling in underscore-preceded column-names with data. Output a shell script which will send each message through some mail transport <font SIZE="-1">MECHANISM.</font> </p>
<p> Do not use this program for evil or I will have to come over and have words with you. </p>
<p> Note that this program does <font SIZE="-1">NOT</font> actually <font SIZE="-1">SEND</font> the mail. It writes a shell script that will send the mail for you. I recommend you save it to a file, check it (one last time!), then run it with sh. </p>
<p> Unlike most Fsdb programs, this program does <i>not</i> output a <font SIZE="-1">FSDB</font> file.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-m </code><font SIZE="-1"><code>MECHANISM</code></font></p>
<dd> Select the mail-sending mechanism. Choose &#8220;Mail&#8221; or &#8220;sendmail&#8221;. Defaults to &#8220;Mail&#8221;.</dl>
<p> This module also supports the standard fsdb options:</p>
<dl>
<dt><code>-d</code></p>
<dd> Enable debugging output.</p>
<dt><code>-i</code> or <code>&#8211;input</code> InputSource</p>
<dd> Read from InputSource, typically a file name, or <tt>&quot;-&quot;</tt> for standard input, or (if in Perl) a IO::Handle, Fsdb::IO or Fsdb::BoundedQueue objects.</p>
<dt><code>-o</code> or <code>&#8211;output</code> OutputDestination</p>
<dd> Write to OutputDestination, typically a file name, or <tt>&quot;-&quot;</tt> for standard output, or (if in Perl) a IO::Handle, Fsdb::IO or Fsdb::BoundedQueue objects.</p>
<dt><code>&#8211;autorun</code> or <code>&#8211;noautorun</code></p>
<dd> By default, programs process automatically, but Fsdb::Filter objects in Perl do not run until you invoke the <i>run()</i> method. The <tt>&quot;--(no)autorun&quot;</tt> option controls that behavior within Perl.</p>
<dt><code>&#8211;help</code></p>
<dd> Show help.</p>
<dt><code>&#8211;man</code></p>
<dd> Show full manual.</dl>
<h2>SAMPLE USAGE</h2>
<h3>Input:</h3>
<pre>
    #fsdb account passwd uid gid fullname homedir shell
    johnh * 2274 134 John_Heidemann /home/johnh /bin/bash
    greg * 2275 134 Greg_Johnson /home/greg /bin/bash
    root * 0 0 Root /root /bin/bash
    # this is a simple database
</pre>
<p> Sample form (in the file form.txt): </p>
<pre>
    To: _account
    From: the sysadmin &lt;root&gt;
    Subject: time to change your password
    Please change your password regularly.
    Doesn't this message make you feel safer?
</pre>
<h3>Command:</h3>
<pre>
    cat DATA/passwd.fsdb | dbformmail form.txt &gt;outgoing.sh
</pre>
<h3>Output (in outgoing.sh):</h3>
<pre>
    #!/bin/sh
    sendmail 'johnh' &lt;&lt;'END'
    To: johnh
    From: the sysadmin &lt;root&gt;
    Subject: time to change your password
    
    Please change your password regularly.
    Doesn't this message make you feel safer?
    END
    sendmail 'greg' &lt;&lt;'END'
    (etc.)
</pre>
<p> And to send the mail, run </p>
<pre>
    sh outgoing.sh
</pre>
<h2>SEE ALSO</h2>
<p> Fsdb.</p>
<h2>AUTHOR and COPYRIGHT</h2>
<p> Copyright (C) 1991-2015 by John Heidemann &lt;johnh [at] isi.edu&gt; </p>
<p> This program is distributed under terms of the <font SIZE="-1">GNU</font> general public license, version 2. See the file <font SIZE="-1">COPYING</font> with the distribution for details. </p>
<h2>Index</h2>
