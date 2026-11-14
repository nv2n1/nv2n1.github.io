---
title: "findmnt(8)"
name: "findmnt"
section: "8"
letter: "f"
url: "/docs/linux/man/8-findmnt/"
description: "findmnt – find a filesystem"
---

<p>findmnt &#8211; find a filesystem</p>
<h2>Synopsis</h2>
<p><code>findmnt</code> [options] </p>
<p> <code>findmnt</code> [options] <i>device</i>|<i>mountpoint</i> </p>
<p> <code>findmnt</code> [options] [<code>&#8211;source</code>] <i>device</i> [<code>&#8211;target</code> <i>path</i>|<code>&#8211;mountpoint</code> <i>mountpoint</i>]</p>
<h2>Description</h2>
<p><code>findmnt</code> will list all mounted filesystems or search for a filesystem. The <code>findmnt</code> command is able to search in <i>/etc/fstab</i>, <i>/etc/mtab</i> or <i>/proc/self/mountinfo</i>. If <i>device</i> or <i>mountpoint</i> is not given, all filesystems are shown. </p>
<p> The device may be specified by device name, major:minor numbers, filesystem label or UUID, or partition label or UUID. Note that <code>findmnt</code> follows <code><a href="/docs/linux/man/8-mount/">mount</a></code>(8) behavior where a device name may be interpreted as a mountpoint (and vice versa) if the <code>&#8211;target</code>, <code>&#8211;mountpoint</code> or <code>&#8211;source</code> options are not specified. </p>
<p> The command-line option <code>&#8211;target</code> accepts any file or directory and then <code>findmnt</code> displays the filesystem for the given path. </p>
<p> The command prints all mounted filesystems in the tree-like format by default.</p>
<h2>Options</h2>
<p><code>-A</code>, <code>&#8211;all</code></p>
<dl>
<dd>Disable all built-in filters and print all filesystems.</dl>
<p> <code>-a</code>, <code>&#8211;ascii</code></p>
<dl>
<dd>Use ascii characters for tree formatting.</dl>
<p> <code>-b</code>, <code>&#8211;bytes</code></p>
<dl>
<dd>Print the SIZE, USED and AVAIL columns in bytes rather than in a human-readable format.</dl>
<p> <code>-C</code>, <code>&#8211;nocanonicalize</code></p>
<dl>
<dd>Do not canonicalize paths at all. This option affects the comparing of paths and the evaluation of tags (LABEL, UUID, etc.).</dl>
<p> <code>-c</code>, <code>&#8211;canonicalize</code></p>
<dl>
<dd>Canonicalize all printed paths.</dl>
<p> <code>-D</code>, <code>&#8211;df</code></p>
<dl>
<dd>Imitate the output of <code><a href="/docs/linux/man/1-df/">df</a></code>(1). This option is equivalent to <code>-o SOURCE,FSTYPE,SIZE,USED,AVAIL,USE%,TARGET</code> but excludes all pseudo filesystems. Use <code>&#8211;all</code> to print all filesystems.</dl>
<p> <code>-d</code>, <code>&#8211;direction</code> <i>word</i></p>
<dl>
<dd>The search direction, either <code>forward</code> or <code>backward</code>.</dl>
<p> <code>-e</code>, <code>&#8211;evaluate</code></p>
<dl>
<dd>Convert all tags (LABEL, UUID, PARTUUID or PARTLABEL) to the corresponding device names.</dl>
<p> <code>-F</code>, <code>&#8211;tab-file</code> <i>path</i></p>
<dl>
<dd>Search in an alternative file. If used with <code>&#8211;fstab</code>, <code>&#8211;mtab</code> or <code>&#8211;kernel</code>, then it overrides the default paths. If specified more than once, then tree-like output is disabled (see the <code>&#8211;list</code> option).</dl>
<p> <code>-f</code>, <code>&#8211;first-only</code></p>
<dl>
<dd>Print the first matching filesystem only.</dl>
<p> <code>-h</code>, <code>&#8211;help</code></p>
<dl>
<dd>Display help text and exit.</dl>
<p> <code>-i</code>, <code>&#8211;invert</code></p>
<dl>
<dd>Invert the sense of matching.</dl>
<p> <code>-J</code>, <code>&#8211;json</code></p>
<dl>
<dd>Use JSON output format.</dl>
<p> <code>-k</code>, <code>&#8211;kernel</code></p>
<dl>
<dd>Search in <i>/proc/self/mountinfo</i>. The output is in the tree-like format. This is the default. The output contains only mount options maintained by kernel (see also <code>&#8211;mtab)</code>.</dl>
<p> <code>-l</code>, <code>&#8211;list</code></p>
<dl>
<dd>Use the list output format. This output format is automatically enabled if the output is restricted by the <code>-t</code>, <code>-O</code>, <code>-S</code> or <code>-T</code> option and the option <code>&#8211;submounts</code> is not used or if more that one source file (the option <code>-F</code>) is specified.</dl>
<p> <code>-M</code>, <code>&#8211;mountpoint</code> <i>path</i></p>
<dl>
<dd>Explicitly define the mountpoint file or directory. See also <code>&#8211;target</code>.</dl>
<p> <code>-m</code>, <code>&#8211;mtab</code></p>
<dl>
<dd>Search in <i>/etc/mtab</i>. The output is in the list format by default (see <code>&#8211;tree</code>). The output may include user space mount options.</dl>
<p> <code>-N</code>, <code>&#8211;task</code> <i>tid</i></p>
<dl>
<dd>Use alternative namespace <i>/proc/&lt;tid&gt;/mountinfo</i> rather than the default <i>/proc/self/mountinfo</i>. If the option is specified more than once, then tree-like output is disabled (see the <code>&#8211;list</code> option). See also the <code><a href="/docs/linux/man/1-unshare/">unshare</a></code>(1) command.</dl>
<p> <code>-n</code>, <code>&#8211;noheadings</code></p>
<dl>
<dd>Do not print a header line.</dl>
<p> <code>-O</code>, <code>&#8211;options</code> <i>list</i></p>
<dl>
<dd>Limit the set of printed filesystems. More than one option may be specified in a comma-separated list. The <code>-t</code> and <code>-O</code> options are cumulative in effect. It is different from <code>-t</code> in that each option is matched exactly; a leading <i>no</i> at the beginning does not have global meaning. The &quot;no&quot; can used for individual items in the list. The &quot;no&quot; prefix interpretation can be disabled by &quot;+&quot; prefix.</dl>
<p> <code>-o</code>, <code>&#8211;output</code> <i>list</i></p>
<dl>
<dd>Define output columns. See the <code>&#8211;help</code> output to get a list of the currently supported columns. The <code>TARGET</code> column contains tree formatting if the <code>&#8211;list</code> or <code>&#8211;raw</code> options are not specified. </p>
<p> The default list of columns may be extended if <i>list</i> is specified in the format <i>+list</i> (e.g., <code>findmnt -o +PROPAGATION</code>).</dl>
<p> <code>&#8211;output-all</code></p>
<dl>
<dd>Output almost all available columns. The columns that require <code>&#8211;poll</code> are not included.</dl>
<p> <code>-P</code>, <code>&#8211;pairs</code></p>
<dl>
<dd>Produce output in the form of key=&quot;value&quot; pairs. All potentially unsafe value characters are hex-escaped (
