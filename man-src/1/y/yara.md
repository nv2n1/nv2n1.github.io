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
<dt><code>-t</code><i> tag</i><code> &#8211;tag=</code><i>tag</i></p>
<dd> Print rules tagged as <i>tag</i> and ignore the rest. This option can be used multiple times.</p>
<dt><code>-i</code><i> identifier</i><code> &#8211;identifier=</code><i>identifier</i></p>
<dd> Print rules named <i>identifier</i> and ignore the rest. This option can be used multiple times.</p>
<dt><code>-n &#8211;negate</code></p>
<dd> Print rules that doesn&#8217;t apply (negate)</p>
<dt><code>-D &#8211;print-module-data</code></p>
<dd> Print module data.</p>
<dt><code>-g &#8211;print-tags</code></p>
<dd> Print the tags associated to the rule.</p>
<dt><code>-m &#8211;print-meta</code></p>
<dd> Print metadata associated to the rule.</p>
<dt><code>-s &#8211;print-strings</code></p>
<dd> Print strings found in the file.</p>
<dt><code>-p</code><i> number</i><code> &#8211;threads=</code><i>number</i></p>
<dd> Use the specified <i>number</i> of threads to scan a directory.</p>
<dt><code>-l</code><i> number</i><code> &#8211;max-rules=</code><i>number</i></p>
<dd> Abort scanning after a <i>number</i> of rules matched.</p>
<dt><code>-a</code><i> seconds</i><code> &#8211;timeout=</code><i>seconds</i></p>
<dd> Abort scanning after a number of <i>seconds</i> has elapsed.</p>
<dt><code>-k</code><i> slots</i><code> &#8211;stack-size=</code><i>slots</i></p>
<dd> Set maximum stack size to the specified number of <i>slots.</i></p>
<dt><code>-d</code><i> identifier=value</i></p>
<dd> Define an external variable. This option can be used multiple times.</p>
<dt><code>-x</code><i> module=file</i></p>
<dd> Pass file&#8217;s content as extra data to module. This option can be used multiple times.</p>
<dt><code>-r &#8211;recursive</code></p>
<dd> Scan files in directories recursively.</p>
<dt><code>-f &#8211;fast-scan</code></p>
<dd> Speeds up scanning by searching only for the first occurrence of each pattern.</p>
<dt><code>-w &#8211;no-warnings</code></p>
<dd> Disable warnings.</p>
<dt><code>-v &#8211;version</code></p>
<dd> Show version information.</dl>
<h2>EXAMPLES</h2>
<p> $ yara /foo/bar/rules1 /foo/bar/rules2 .</p>
<dl>
<dt>
<dd>
<p> Apply rules on <i>/foo/bar/rules1</i> and <i>/foo/bar/rules2</i> to all files on current directory. Subdirectories are not scanned.</dl>
<p> $ yara -t Packer -t Compiler /foo/bar/rules bazfile</p>
<dl>
<dt>
<dd>
<p> Apply rules on <i>/foo/bar/rules</i> to <i>bazfile.</i> Only reports rules tagged as <i>Packer</i> or <i>Compiler.</i></dl>
<p> $ cat /foo/bar/rules1 | yara -r /foo</p>
<dl>
<dt>
<dd>
<p> Scan all files in the <i>/foo</i> directory and its subdirectories. Rules are read from standard input.</dl>
<p> $ yara -d mybool=true -d myint=5 -d mystring=&quot;my string&quot; /foo/bar/rules bazfile</p>
<dl>
<dt>
<dd>
<p> Defines three external variables <i>mybool</i> <i>myint</i> and <i>mystring.</i></dl>
<p> $ yara -x cuckoo=cuckoo_json_report /foo/bar/rules bazfile</p>
<dl>
<dt>
<dd>
<p> Apply rules on <i>/foo/bar/rules</i> to <i>bazfile</i> while passing the content of <i>cuckoo_json_report</i> to the cuckoo module.</dl>
<h2>AUTHOR</h2>
<p> Victor M. Alvarez &lt;plusvic [at] gmail.com&gt;;&lt;vmalvarez [at] virustotal.com&gt; </p>
<h2>Index</h2>
