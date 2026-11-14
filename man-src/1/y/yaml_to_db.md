---
title: "yaml_to_db(1)"
name: "yaml_to_db"
section: "1"
letter: "y"
url: "/docs/linux/man/1-yaml_to_db/"
description: "yaml_to_db – convert a subset of YAML into fsdb"
---

<h2 class="name">NAME</h2>
<p> yaml_to_db &#8211; convert a subset of YAML into fsdb </p>
<h2>SYNOPSIS</h2>
<pre>
    yaml_to_db &lt;source.yaml
</pre>
<h2>DESCRIPTION</h2>
<p> Converts a <i>very limited</i> subset of <font SIZE="-1">YAML</font> into Fsdb format. </p>
<p> The input is YAML-format (<i>not</i> fsdb). The input is parsed as <font SIZE="-1">YAML, </font> assuming the file is an array of dictionary entries. We extract the dictionary names and output this as an fsdb table. </p>
<p> The output is tab-separated fsdb. (Someday more general field separators should be supported.)</p>
<h2>OPTIONS</h2>
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
        - name: ACM
          role: sponsor
          alttext: ACM, the Association for Computing Machinery
          image: logos/acm-small.jpg
          link:  <a rel="nofollow" href="https://www.acm.org/">https://www.acm.org/</a>
          date: 2016-01-01
        
        - name: SIGCOMM
          role: sponsor
          alttext: SIGCOMM, ACM'S Special Interest Group on Communication
          image: logos/sigcommlogo.png
          link:  <a rel="nofollow" href="http://sigcomm.org">http://sigcomm.org</a>
          date: 2016-01-02
        
        - name: SIGMETRICS
          role: sponsor
          alttext: SIGMETRICS, ACM'S Special Interest Group on Performance Evaluation
          image: logos/sigmetrics-small.png
          link:  <a rel="nofollow" href="http://www.sigmetrics.org">http://www.sigmetrics.org</a>
          date: 2016-01-03
</pre>
<h3>Command:</h3>
<pre>
        yaml_to_db &lt;gnupod.yaml
</pre>
<h3>Output:</h3>
<pre>
        #fsdb -F t alttext date image link name role
        ACM, the Association for Computing Machinery    2016-01-01      logos/acm-small.jpg     <a rel="nofollow" href="https://www.acm.org/">https://www.acm.org/</a>    ACM     sponsor
        SIGCOMM, ACM'S Special Interest Group on Communication  2016-01-02      logos/sigcommlogo.png   <a rel="nofollow" href="http://sigcomm.org">http://sigcomm.org</a>      SIGCOMM sponsor
        SIGMETRICS, ACM'S Special Interest Group on Performance Evaluation      2016-01-03      logos/sigmetrics-small.png      <a rel="nofollow" href="http://www.sigmetrics.org">http://www.sigmetrics.org</a>       SIGMETRICS      sponsor
        #   | yaml_to_db
</pre>
<h2>SEE ALSO</h2>
<p> Fsdb.</p>
<h2>AUTHOR and COPYRIGHT</h2>
<p> Copyright (C) 2011-2016 by John Heidemann &lt;johnh [at] isi.edu&gt; </p>
<p> This program is distributed under terms of the <font SIZE="-1">GNU</font> general public license, version 2. See the file <font SIZE="-1">COPYING</font> with the distribution for details. </p>
<h2>Index</h2>
