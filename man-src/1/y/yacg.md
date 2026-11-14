---
title: "yacg(1)"
name: "yacg"
section: "1"
letter: "y"
url: "/docs/linux/man/1-yacg/"
description: "yacg – Yet Another Configuration Generator"
---

<h2 class="name">NAME</h2>
<p> yacg &#8211; Yet Another Configuration Generator </p>
<h2>SYNOPSIS</h2>
<p> <code>yacg</code> [<i></i><font SIZE="-1"><i>OPTIONS</i></font><i></i>] <i></i><font SIZE="-1"><i>PATH</i></font><i></i> </p>
<p> <code>yacg</code> <code>&#8211;help</code>|<code>&#8211;manual</code>|<code>&#8211;version</code></p>
<h2>DESCRIPTION</h2>
<p> <code>yacg</code> reads the given high-level configuration file, carefully validates it and generates ready-to-use (configuration) files. </p>
<p> The high-level configuration file can be altered using the <code>&#8211;set</code>, <code>&#8211;unset</code> and <code>&#8211;merge</code> options. It can be inspected using the <code>&#8211;dump</code> option. </p>
<p> The files can be generated at their final location (by default) or elsewhere (using the <code>&#8211;rootdir</code> option). <code>yacg</code> can also be instructed to check the files without changing them via the <code>&#8211;noaction</code> option. </p>
<p> <code>yacg</code> can use a &#8220;manifest&#8221; file to keep track of which files it generated so that it can later remove the files that it does not generate anymore, see the <code>&#8211;manifest</code> and <code>&#8211;clean</code> options. </p>
<p> <code>yacg</code> by itself does not know how to generate files. The <code>&#8211;home</code> option (and optionally the <code>&#8211;include</code> option) must be used to tell the program where to find domain specific modules knowing how to translate the high-level configuration into individual ready-to-use files.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>&#8211;clean</code></p>
<dd> remove the files present in the old &#8220;manifest&#8221; file but not in the new one</p>
<dt><code>&#8211;debug</code>, <code>-d</code></p>
<dd> show debugging information</p>
<dt><code>&#8211;dump</code></p>
<dd> instead of generating files, dump the high-level configuration; this option can be given multiple times:</p>
<dl>
<dt>
<dd>
<dl>
<dt>1: dump after loading the configuration</p>
<dd>
<dt>2: dump after hacking the configuration</p>
<dd>
<dt>3: dump after validating the configuration</p>
<dd></dl>
</dl>
<dl>
<dt>
<dd></dl>
<dt><code>&#8211;dump-format</code> <i></i><font SIZE="-1"><i>NAME</i></font><i></i></p>
<dd> set the output format for the <code>&#8211;dump</code> option; possible values: <tt>&quot;Config::General&quot;</tt> (default) and <tt>&quot;JSON&quot;</tt></p>
<dt><code>&#8211;help</code>, <code>-h</code>, <code>-?</code></p>
<dd> show some help</p>
<dt><code>&#8211;home</code>, <code>-H</code> <i></i><font SIZE="-1"><i>PATH</i></font><i></i></p>
<dd> set the home directory where the <tt>&quot;cfg&quot;</tt>, <tt>&quot;lib&quot;</tt> and <tt>&quot;tpl&quot;</tt> sub-directories may be located</p>
<dt><code>&#8211;include</code>, <code>-I</code> <i></i><font SIZE="-1"><i>PATH</i></font><i></i></p>
<dd> add the given directory to the list of paths that will be looked at to find configuration files, Config::Generator modules or templates; this option can be given multiple times</p>
<dt><code>&#8211;manifest</code> <i></i><font SIZE="-1"><i>PATH</i></font><i></i></p>
<dd> store the list of files that <code>yacg</code> handled in the given &#8220;manifest&#8221; file</p>
<dt><code>&#8211;manual</code>, <code>-m</code></p>
<dd> show this manual</p>
<dt><code>&#8211;merge</code> <i></i><font SIZE="-1"><i>PATH</i></font><i></i>=<i></i><font SIZE="-1"><i>VALUE</i></font><i></i></p>
<dd> hack the loaded configuration to merge the given value at the given path</p>
<dt><code>&#8211;noaction</code>, <code>-n</code></p>
<dd> print what would be done but do not actually touch the generated files</p>
<dt><code>&#8211;quiet</code>, <code>-q</code></p>
<dd> set the verbosity level to 0</p>
<dt><code>&#8211;rndfile</code> <i></i><font SIZE="-1"><i>PATH</i></font><i></i></p>
<dd> set the path of the file that will be used as seed to generate random data</p>
<dt><code>&#8211;rootdir</code> <i></i><font SIZE="-1"><i>PATH</i></font><i></i></p>
<dd> set the path specifying where the generated files will be put</p>
<dt><code>&#8211;set</code> <i></i><font SIZE="-1"><i>PATH</i></font><i></i>=<i></i><font SIZE="-1"><i>VALUE</i></font><i></i></p>
<dd> hack the loaded configuration to set the given value at the given path</p>
<dt><code>&#8211;spec</code> <i></i><font SIZE="-1"><i>PATH</i></font><i></i></p>
<dd> store the list of files that <code>yacg</code> handled in the given &#8220;spec&#8221; file (same format as rpm&#8217;s spec <tt>%files</tt>)</p>
<dt><code>&#8211;unset</code> <i></i><font SIZE="-1"><i>PATH</i></font><i></i></p>
<dd> hack the loaded configuration to unset the given path</p>
<dt><code>&#8211;verbose</code>, <code>-v</code></p>
<dd> increase the verbosity level (default: 1)</p>
<dt><code>&#8211;version</code></p>
<dd> display version information</dl>
<h2>SEE ALSO</h2>
<p> Config-Generator.</p>
<h2>AUTHOR</h2>
<p> Lionel Cons &lt;<a rel="nofollow" href="http://cern.ch/lionel.cons">http://cern.ch/lionel.cons</a>&gt; </p>
<p> Copyright (C) <font SIZE="-1">CERN 2013-2016</font> </p>
<h2>Index</h2>
