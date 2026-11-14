---
title: "combined_log_format_to_db(1)"
name: "combined_log_format_to_db"
section: "1"
letter: "c"
url: "/docs/linux/man/1-combined_log_format_to_db/"
description: "combined_log_format_to_db – convert Apache Combined Log Format to Fsdb"
---

<h2 class="name">NAME</h2>
<p> combined_log_format_to_db &#8211; convert Apache Combined Log Format to Fsdb </p>
<h2>SYNOPSIS</h2>
<pre>
    combined_log_format_to_db &lt; access_log &gt; access_log.fsdb
</pre>
<h2>DESCRIPTION</h2>
<p> Converts logs in Apache Combined-Log-Format into Fsdb format.</p>
<h2>OPTIONS</h2>
<p> No program-specific options. </p>
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
<pre><code>
foo.example.com - -[01 / Jan / 2007:00:00:01 - 0800] "GET /~moll/wedding/index.html HTTP/1.0" 200 2390 "-"
                                                                                                       "Mozilla/5.0 (compatible; Yahoo! Slurp; http://help.yahoo.com/help/us/ysearch/slurp)" 127.0.0.1 -
    -[01 / Jan / 2007:00:00:02 - 0800] "GET /hpdc2007/ HTTP/1.1" 304 - "http://grid.hust.edu.cn:8080/call/cfp.jsp"
                                                                       "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; InfoPath.1; InfoPath.2)" bar.example.com -
    -[31 / Dec / 2006:23:51:40 - 0800] "GET /nsnam/dist/ns-allinone-2.29.2.tar.gz HTTP/1.1" 206 58394090 "file://D:\�ҵ��ĵ�\ns2\XP_Using_Cygwin.htm#Windows_Support_for_Ns-2.27_and_Earlier"
                                                                                                         "Mozilla/4.0 (compatible; MSIE 5.00; Windows 98)" 127.0.0.1 -
    -[01 / Jan / 2007:00:00:02 - 0800] "GET /hpdc2007/hpdc.css HTTP/1.1" 304 - "http://www.isi.edu/hpdc2007/"
                                                                               "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; InfoPath.1; InfoPath.2)"
</code></pre>
<h3>Command:</h3>
<pre>
    combined_log_format_to_db
</pre>
<h3>Output:</h3>
<pre><code>
#fsdb - F S client identity userid time method resource protocol status size refer useragent
foo.example.com - -[01 / Jan / 2007:00:00:01 - 0800] GET / ~moll / wedding / index.html HTTP / 1.0 200 2390 "-"
                                                                                                            "Mozilla/5.0 (compatible; Yahoo! Slurp; http://help.yahoo.com/help/us/ysearch/slurp)" 127.0.0.1 -
    -[01 / Jan / 2007:00:00:02 - 0800] GET / hpdc2007 / HTTP / 1.1 304 - "http://grid.hust.edu.cn:8080/call/cfp.jsp"
                                                                         "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; InfoPath.1; InfoPath.2)" bar.example.com -
    -[31 / Dec / 2006:23:51:40 - 0800] GET / nsnam / dist / ns - allinone - 2.29.2.tar.gz HTTP / 1.1 206 58394090 "file://D:\�ҵ��ĵ�\ns2\XP_Using_Cygwin.htm#Windows_Support_for_Ns-2.27_and_Earlier"
                                                                                                                  "Mozilla/4.0 (compatible; MSIE 5.00; Windows 98)" 127.0.0.1 -
    -[01 / Jan / 2007:00:00:02 - 0800] GET / hpdc2007 / hpdc.css HTTP / 1.1 304 - "http://www.isi.edu/hpdc2007/"
                                                                                  "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; InfoPath.1; InfoPath.2)"
#| combined_log_format_to_db
</code></pre>
<h2>SEE ALSO</h2>
<p> Fsdb. &lt;<a rel="nofollow" href="http://httpd.apache.org/docs/2.0/logs.html">http://httpd.apache.org/docs/2.0/logs.html</a>&gt;</p>
<h2>AUTHOR and COPYRIGHT</h2>
<p> Copyright (C) 2008 by John Heidemann &lt;johnh [at] isi.edu&gt; </p>
<p> This program is distributed under terms of the <font SIZE="-1">GNU</font> general public license, version 2. See the file <font SIZE="-1">COPYING</font> with the distribution for details. </p>
<h2>Index</h2>
