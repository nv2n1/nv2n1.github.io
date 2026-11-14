---
title: "vstp(1)"
name: "vstp"
section: "1"
letter: "v"
url: "/docs/linux/man/1-vstp/"
description: "vstpg, vstpp – VisioBraille file transferring"
---

<h2 class="name">NAME</h2>
<p> vstpg, vstpp &#8211; VisioBraille file transferring </p>
<h2>SYNOPSIS</h2>
<p> vstpg [-ifbnd] [-s <i>socketport</i>] [-k <i>keyname</i>] [-o <i>configname</i>] file &#8230;</p>
<h2>DESCRIPTION</h2>
<p> <i>vstpg</i> (resp. <i>vstpp</i>) gets (resp. puts) files from (resp. onto) a VisioBraille terminal. </p>
<p> For communicating with the terminal, you must launch brltty with the BrlNet driver, and telling BrlNet to use the VisioBraille driver. </p>
<p> Before putting on the terminal, file names are truncated to 8 characters without any extension. </p>
<p> Before getting from terminal, leading path and trailing extensions are removed, but put back for local filename. </p>
<h2>COMMAND-LINE OPTIONS</h2>
<dl>
<dt><code>-i</code></p>
<dd> ask for confirmation of transfer, for each file (on the terminal)</p>
<dt><code>-f</code></p>
<dd> don&#8217;t ask for such a confirmation (default)</p>
<dt><code>-b</code></p>
<dd> if they exists, recursively rename the old files with an added .x suffix, just like logrotate does</p>
<dt><code>-n</code></p>
<dd> do not keep such backup file (default)</p>
<dt><code>-s</code> <i>socketport</i></p>
<dd> use socketport as the port number instead of default for connecting to BrlNet</p>
<dt><code>-k</code> <i>filename</i></p>
<dd> use filename as key path instead of default for reading BrlNet&#8217;s authentication key</p>
<dt><code>-d</code></p>
<dd> use current directory rather than the download directory (see <i>vbs_dir</i> below)</p>
<dt><code>-o</code> <i>filename</i></p>
<dd> also read filename as config file </p>
</dl>
<h2>CONFIG FILE</h2>
<p> <i>vstpg</i> and <i>vstpp</i> read a configuration file <code>$HOME/.vstprc</code> which contains keywords or equalities, one per line (what follows a # is ignored). </p>
<p> You can ask them to also read any other file thanks to the <code>-o</code> option. </p>
<p> Here are keywords: </p>
<dl>
<dt><code>backup</code></p>
<dd> make <code>-b</code> option the default </p>
<dt><code>nobackup</code></p>
<dd> make <code>-f</code> option the default </p>
<dt>and equalities:</p>
<dd>
<dt><code>keyname</code> = <i>filename</i></p>
<dd> use this file instead of default, to find BrlNet&#8217;s authentication key </p>
<dt><code>socketport</code> = <i>port</i></p>
<dd> use this port number, instead of default, to connect to BrlNet </p>
<dt><code>vbs_ext</code> = <i>.ext</i></p>
<dd> use .ext as an extension for downloaded files (.vis by default) this is overridden on command line if an extension is provided in the file name </p>
<dt><code>vbs_dir</code> = <i>path</i></p>
<dd> use path instead of current directory for putting files, except when using the <code>-d</code> option, or if the filename begins with &#8216;.&#8217; </p>
</dl>
<h2>RETURNED VALUE</h2>
<table>
<tr VALIGN=top>
<td><code>1</code></td>
<td>syntax error on command line
</td>
</tr>
<tr VALIGN=top>
<td><code>2</code></td>
<td>connection with BrlNet error
</td>
</tr>
<tr VALIGN=top>
<td><code>3</code></td>
<td>Unix file error
</td>
</tr>
<tr VALIGN=top>
<td><code>4</code></td>
<td>Protocol error
</td>
</tr>
<tr VALIGN=top>
<td><code>16</code></td>
<td>interrupted by user
</td>
</tr>
</table>
<h2>SHELL EXPANSIONS</h2>
<p> Beware of special chars: * and . are often expanded by your shell, hence <i>vstpp *</i> will probably do what you want, putting every file existing in the current directory onto the terminal, but <i>vstpg *</i> may not do what you want: it will only get every file which already exist in the current directory, skipping those you just created on your terminal ! If you want to get every file which exist in the terminal, you should use <i>vstpg &#8216;*&#8217;</i> or something similar (please read your shell manual). </p>
<p> The same warning applies to other special chars, such as $, ~, &amp;,&#8230; which should be protected by surrounding arguments by quotes (&#8216;) or by using single backslashes (\) just before them (please read your shell manual). </p>
<h2>BUGS</h2>
<p> The one we could find has been corrected :) </p>
<h2>AUTHOR</h2>
<p> Samuel Thibault &lt;samuel.thibault [at] ens-lyon.org&gt; and Sebastien Hinderer &lt;sebastien.hinderer [at] ens-lyon.fr&gt; </p>
<h2>Index</h2>
