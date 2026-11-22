---

title: "yacg(1)"
name: "yacg"
section: "1"
letter: "y"
url: "/docs/linux/man/1-yacg/"
description: "yacg – Yet Another Configuration Generator"
---

<p> yacg &#8211; Yet Another Configuration Generator </p>
<h2>SYNOPSIS</h2>
<p> <code>yacg</code> [<i></i><i>OPTIONS</i><i></i>] <i></i><i>PATH</i><i></i> </p>
<p> <code>yacg</code> <code>&#8211;help</code>|<code>&#8211;manual</code>|<code>&#8211;version</code></p>
<h2>DESCRIPTION</h2>
<p> <code>yacg</code> reads the given high-level configuration file, carefully validates it and generates ready-to-use (configuration) files. </p>
<p> The high-level configuration file can be altered using the <code>&#8211;set</code>, <code>&#8211;unset</code> and <code>&#8211;merge</code> options. It can be inspected using the <code>&#8211;dump</code> option. </p>
<p> The files can be generated at their final location (by default) or elsewhere (using the <code>&#8211;rootdir</code> option). <code>yacg</code> can also be instructed to check the files without changing them via the <code>&#8211;noaction</code> option. </p>
<p> <code>yacg</code> can use a &#8220;manifest&#8221; file to keep track of which files it generated so that it can later remove the files that it does not generate anymore, see the <code>&#8211;manifest</code> and <code>&#8211;clean</code> options. </p>
<p> <code>yacg</code> by itself does not know how to generate files. The <code>&#8211;home</code> option (and optionally the <code>&#8211;include</code> option) must be used to tell the program where to find domain specific modules knowing how to translate the high-level configuration into individual ready-to-use files.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>&#8211;clean</code></dt>
<dd> remove the files present in the old &#8220;manifest&#8221; file but not in the new one</dd>
<dt><code>&#8211;debug</code>, <code>-d</code></dt>
<dd> show debugging information</dd>
<dt><code>&#8211;dump</code></dt>
<dd> instead of generating files, dump the high-level configuration; this option can be given multiple times:</dd>
<dl>
<dl>
<dt>1: dump after loading the configuration</dt>
<dd>
</dd><dt>2: dump after hacking the configuration</dt>
<dd>
</dd><dt>3: dump after validating the configuration</dt>
<dd></dd></dl>
</dl>
<dl>
</dl>
<dt><code>&#8211;dump-format</code> <i></i><i>NAME</i><i></i></dt>
<dd> set the output format for the <code>&#8211;dump</code> option; possible values: <tt>&quot;Config::General&quot;</tt> (default) and <tt>&quot;JSON&quot;</tt></dd>
<dt><code>&#8211;help</code>, <code>-h</code>, <code>-?</code></dt>
<dd> show some help</dd>
<dt><code>&#8211;home</code>, <code>-H</code> <i></i><i>PATH</i><i></i></dt>
<dd> set the home directory where the <tt>&quot;cfg&quot;</tt>, <tt>&quot;lib&quot;</tt> and <tt>&quot;tpl&quot;</tt> sub-directories may be located</dd>
<dt><code>&#8211;include</code>, <code>-I</code> <i></i><i>PATH</i><i></i></dt>
<dd> add the given directory to the list of paths that will be looked at to find configuration files, Config::Generator modules or templates; this option can be given multiple times</dd>
<dt><code>&#8211;manifest</code> <i></i><i>PATH</i><i></i></dt>
<dd> store the list of files that <code>yacg</code> handled in the given &#8220;manifest&#8221; file</dd>
<dt><code>&#8211;manual</code>, <code>-m</code></dt>
<dd> show this manual</dd>
<dt><code>&#8211;merge</code> <i></i><i>PATH</i><i></i>=<i></i><i>VALUE</i><i></i></dt>
<dd> hack the loaded configuration to merge the given value at the given path</dd>
<dt><code>&#8211;noaction</code>, <code>-n</code></dt>
<dd> print what would be done but do not actually touch the generated files</dd>
<dt><code>&#8211;quiet</code>, <code>-q</code></dt>
<dd> set the verbosity level to 0</dd>
<dt><code>&#8211;rndfile</code> <i></i><i>PATH</i><i></i></dt>
<dd> set the path of the file that will be used as seed to generate random data</dd>
<dt><code>&#8211;rootdir</code> <i></i><i>PATH</i><i></i></dt>
<dd> set the path specifying where the generated files will be put</dd>
<dt><code>&#8211;set</code> <i></i><i>PATH</i><i></i>=<i></i><i>VALUE</i><i></i></dt>
<dd> hack the loaded configuration to set the given value at the given path</dd>
<dt><code>&#8211;spec</code> <i></i><i>PATH</i><i></i></dt>
<dd> store the list of files that <code>yacg</code> handled in the given &#8220;spec&#8221; file (same format as rpm&#8217;s spec <tt>%files</tt>)</dd>
<dt><code>&#8211;unset</code> <i></i><i>PATH</i><i></i></dt>
<dd> hack the loaded configuration to unset the given path</dd>
<dt><code>&#8211;verbose</code>, <code>-v</code></dt>
<dd> increase the verbosity level (default: 1)</dd>
<dt><code>&#8211;version</code></dt>
<dd> display version information</dd></dl>
<h2>SEE ALSO</h2>
<p> Config-Generator.</p>
<h2>AUTHOR</h2>
<p> Lionel Cons &lt;<a rel="nofollow" href="http://cern.ch/lionel.cons">http://cern.ch/lionel.cons</a>&gt; </p>
<p> Copyright (C) CERN 2013-2016 </p>
