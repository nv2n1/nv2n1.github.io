---

title: "gt5(1)"
name: "gt5"
section: "1"
letter: "g"
url: "/docs/linux/man/1-gt5/"
description: "gt5 – a diff-capable ‘du-browser’"
---

<p> gt5 &#8211; a diff-capable &#8216;du-browser&#8217;</p>
<h2>SYNOPSIS</h2>
<p> <code>gt5</code> [ dir | file | dir file | file file2 ] [options]</p>
<h2>DESCRIPTION</h2>
<p> <code>gt5</code> reads the output of <code>du</code>, compares it with a du-log saved by the last run, converts it into HTML and opens the resulting file with a <code>textbrowser</code>. </p>
<p> If files are given on the commandline they are expected to be (optionally <i>gzip</i>/<i>bzip2</i>-compressed) logfiles of <code>du -akx /some/dir</code>. It is up to you to take care that the given directories/files represent the same directory. <i>gt5</i> will show lots of new files if you don&#8217;t. ;-)</p>
<h2>OPTIONS</h2>
<dl>
<dt>&#8211;cut-at float</dt>
<dd> Files and directories that are below <i>float</i> percent of their parents are not shown. Default is <i>0.1</i>, gt5 will accept values between 0.01 and 30.</dd>
<dt>&#8211;diff-dir directory</dt>
<dd> Use <i>directory</i> instead of <i>~/.gt5-diffs/</i> to read/store du-logs. This switch is ignored if gt5 is only used with files.</dd>
<dt>&#8211;discard</dt>
<dd> Do not save the current state, in other words: be able to diff against the old state again. This feature is disabled if gt5 is only used with files.</dd>
<dt>&#8211;link-files</dt>
<dd> Also insert links to files to access them from within gt5. This can be very handy if your browser is configured to handle the files MIME-type correctly. This feature is disabled if gt5 is only used with files.</dd>
<dt>&#8211;max-depth int</dt>
<dd> Do not show anything below a depth of <i>int</i> directories. Default is <i>5</i> (also see <code>BUGS</code> below).</dd>
<dt>&#8211;max-lines int</dt>
<dd> Only consider the <i>int</i> biggest files and directories within the output of <i>du</i>.</dd>
<dt>&#8211;no-diffs</dt>
<dd> Use this if you are not interested in the history of the directories processed, for example in /tmp.</dd>
<dt>&#8211;save-as file</dt>
<dd> DEPRECATED, use <code>du -akx</code> or <code>du -ak</code> (see <code>&#8211;with-mounts</code>), save the output to a file and run gt5 against one (ore two) of these files later.</dd>
<dt>&#8211;save-state</dt>
<dd> Force saving current state, overwriting a previous <i>&#8211;discard</i>. (Some people seem to have gt5 aliased to <i>&#8216;gt5 &#8211;discard&#8217;</i>.)</dd>
<dt>&#8211;with-mounts</dt>
<dd> By default gt5 calls <code>du</code> with <code>-akx</code> to ignore mounted filesystems. Use this to inspect mounted partitions too, i.e. call <code>du</code> with <code>-ak</code></dd></dl>
<h2>HELPERS</h2>
<p> If <i>gawk</i> or a <i>textbrowser</i> are missing and you want to install them into <i>~/bin </i>(or <i>/usr/local/bin </i>if you have write access there), <i>gt5</i> comes with the following helpers:</p>
<dl>
<dt>&#8211;get-gawk</dt>
<dd> Download, compile and install a copy of <i>gawk</i>.</dd>
<dt>&#8211;get-links</dt>
<dd> Download, compile and install a copy of <i>links</i>.</dd>
<dt>&#8211;get-links2</dt>
<dd> Download, compile and install a copy of <i>links2</i>.</dd>
<dt>&#8211;get-elinks</dt>
<dd> Download, compile and install a copy of <i>elinks</i>.</dd></dl>
<h2>TEXTBROWSERS</h2>
<p> It is recommended to use <i>links </i>with <i>gt5</i>. Other textbrowsers are also possible but there are several good reasons why links is given priority over the others:</p>
<dl>
<dt>elinks:</dt>
<dd> links is <i>much</i> faster on startup/exit</dd>
<dt>lynx:</dt>
<dd> does not honor a documents <i>coloring</i></dd>
<dt>netrik:</dt>
<dd> no colors, <i>unfavourable cursor navigation</i></dd>
<dt>retawq:</dt>
<dd> no colors, <i>can&#8217;t</i> handle &lt;a name&gt;-tags</dd>
<dt>w3m:</dt>
<dd> <i>unfavourable</i> handling of &lt;a name&gt;-tag, <i>unfavourable cursor navigation</i> and no colors</dd></dl>
<p> Only <i>links</i>/<i>links2</i>, <i>elinks </i>and <i>lynx</i> are now considered usable (and also chosen in that order). See <code>ENVIRONMENT</code>/<code>GT5_BROWSER</code> below.</p>
<h2>FILES</h2>
<p> <i>~/.gt5.html</i></p>
<dl>
<dt>
</dt><dd> contains a copy of the last run</dd></dl>
<p> <i>~/.gt5-diffs/</i></p>
<dl>
<dt>
</dt><dd> compressed du-logs are stored here</dd></dl>
<h2>ENVIRONMENT</h2>
<dl>
<dt>GT5_BROWSER</dt>
<dd> force using a (specific) textbrowser</dd>
<dt>GT5_CHARSET</dt>
<dd> force using a (specific) charset for HTML header instead of using <i>$LANG</i></dd></dl>
<h2>BUGS</h2>
<p> Directories at depth <code>max-depth</code> are not browsable and so look like files.</p>
<h2>AUTHOR</h2>
<p> Thomas Sattler &lt;gt5 at gmx dot net&gt;</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-du/">du</a></code>(1), <code>links</code>(1), <code><a href="/docs/linux/man/1-elinks/">elinks</a></code>(1), <code><a href="/docs/linux/man/1-lynx/">lynx</a></code>(1) </p>
