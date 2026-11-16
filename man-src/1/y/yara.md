---
title: "yara(1)"
name: "yara"
section: "1"
letter: "y"
url: "/docs/linux/man/1-yara/"
description: "yara – find files matching patterns and rules written in a special-purpose language."
---

<h2>NAME</h2>
<p> yara &#8211; find files matching patterns and rules written in a special-purpose language.</p>
<h2>SYNOPSIS</h2>
<p> <code>yara</code> [OPTION]&#8230; RULES_FILE FILE | DIR | PID</p>
<h2>DESCRIPTION</h2>
<p> yara scans the given FILE, all files contained in directory DIR, or the process indentified by PID looking for matches of patterns and rules provided in a special purpose-language. The rules are read from RULES_FILE. </p>
<p> The options to <i><a href="/docs/linux/man/1-yara/">yara</a></i>(1) are:</p>
<dl>
<dt><code>-t</code><i> tag</i><code> &#8211;tag=</code><i>tag</i></dt>
<dd> Print rules tagged as <i>tag</i> and ignore the rest. This option can be used multiple times.</dd>
<dt><code>-i</code><i> identifier</i><code> &#8211;identifier=</code><i>identifier</i></dt>
<dd> Print rules named <i>identifier</i> and ignore the rest. This option can be used multiple times.</dd>
<dt><code>-n &#8211;negate</code></dt>
<dd> Print rules that doesn&#8217;t apply (negate)</dd>
<dt><code>-D &#8211;print-module-data</code></dt>
<dd> Print module data.</dd>
<dt><code>-g &#8211;print-tags</code></dt>
<dd> Print the tags associated to the rule.</dd>
<dt><code>-m &#8211;print-meta</code></dt>
<dd> Print metadata associated to the rule.</dd>
<dt><code>-s &#8211;print-strings</code></dt>
<dd> Print strings found in the file.</dd>
<dt><code>-p</code><i> number</i><code> &#8211;threads=</code><i>number</i></dt>
<dd> Use the specified <i>number</i> of threads to scan a directory.</dd>
<dt><code>-l</code><i> number</i><code> &#8211;max-rules=</code><i>number</i></dt>
<dd> Abort scanning after a <i>number</i> of rules matched.</dd>
<dt><code>-a</code><i> seconds</i><code> &#8211;timeout=</code><i>seconds</i></dt>
<dd> Abort scanning after a number of <i>seconds</i> has elapsed.</dd>
<dt><code>-k</code><i> slots</i><code> &#8211;stack-size=</code><i>slots</i></dt>
<dd> Set maximum stack size to the specified number of <i>slots.</i></dd>
<dt><code>-d</code><i> identifier=value</i></dt>
<dd> Define an external variable. This option can be used multiple times.</dd>
<dt><code>-x</code><i> module=file</i></dt>
<dd> Pass file&#8217;s content as extra data to module. This option can be used multiple times.</dd>
<dt><code>-r &#8211;recursive</code></dt>
<dd> Scan files in directories recursively.</dd>
<dt><code>-f &#8211;fast-scan</code></dt>
<dd> Speeds up scanning by searching only for the first occurrence of each pattern.</dd>
<dt><code>-w &#8211;no-warnings</code></dt>
<dd> Disable warnings.</dd>
<dt><code>-v &#8211;version</code></dt>
<dd> Show version information.</dd></dl>
<h2>EXAMPLES</h2>
<p> $ yara /foo/bar/rules1 /foo/bar/rules2 .</p>
<dl>
<dt>
</dt><dd>
<p> Apply rules on <i>/foo/bar/rules1</i> and <i>/foo/bar/rules2</i> to all files on current directory. Subdirectories are not scanned.</dd></dl>
<p> $ yara -t Packer -t Compiler /foo/bar/rules bazfile</p>
<dl>
<dt>
</dt><dd>
<p> Apply rules on <i>/foo/bar/rules</i> to <i>bazfile.</i> Only reports rules tagged as <i>Packer</i> or <i>Compiler.</i></dd></dl>
<p> $ cat /foo/bar/rules1 | yara -r /foo</p>
<dl>
<dt>
</dt><dd>
<p> Scan all files in the <i>/foo</i> directory and its subdirectories. Rules are read from standard input.</dd></dl>
<p> $ yara -d mybool=true -d myint=5 -d mystring=&quot;my string&quot; /foo/bar/rules bazfile</p>
<dl>
<dt>
</dt><dd>
<p> Defines three external variables <i>mybool</i> <i>myint</i> and <i>mystring.</i></dd></dl>
<p> $ yara -x cuckoo=cuckoo_json_report /foo/bar/rules bazfile</p>
<dl>
<dt>
</dt><dd>
<p> Apply rules on <i>/foo/bar/rules</i> to <i>bazfile</i> while passing the content of <i>cuckoo_json_report</i> to the cuckoo module.</dd></dl>
<h2>AUTHOR</h2>
<p> Victor M. Alvarez &lt;plusvic [at] gmail.com&gt;;&lt;vmalvarez [at] virustotal.com&gt; </p>
<h2>Index</h2>
</p>