---
title: "unrar(1)"
name: "unrar"
section: "1"
letter: "u"
url: "/docs/linux/man/1-unrar/"
description: "unrar – extract files from rar archives"
---

<h2 class="name">NAME</h2>
<p> unrar &#8211; extract files from rar archives </p>
<h2>SYNOPSIS</h2>
<p> <code>unrar</code> <i>command</i> [<i>-switch</i> &#8230;] <i>archive</i> [<i>file</i> &#8230;] [@<i>listfiles</i> &#8230;] [<i>path</i> &#8230;] [<i>path_to_extract</i>/]</p>
<h2>DESCRIPTION</h2>
<p> This manual page documents briefly the <code>unrar</code> command.<br />
 This manual page was written for the Debian GNU/Linux distribution because the original program does not have a manual page.<br />
 Commands and options described here are as of unrar 6.0.</p>
<h2>USAGE</h2>
<dl>
<dt><code>archive</code></dt>
<dd> Archive file name in RAR or other supported format. If archive file uses RAR multiple volume format, specify only first volume file name as <code>archive</code> file name.</dd>
<dt><code>file &#8230;</code></dt>
<dd> File path name to extract. You can specify more path names at one time.</dd>
<dt><code>@listfiles &#8230;</code></dt>
<dd> If argument starts with &quot;@&quot;, unrar uses <code>listfile</code> as file path list file. This list file includes file path list to extract from archive file. You can use 2 or more list files at one time.<br />
 File list uses one line for one file path. And blank line is ignored.<br />
 This file is used to extract many file path names in one time that your shell can&#8217;t accept.</dd>
<dt><code>path_to_extract</code></dt>
<dd> If last argument is ended with &quot;/&quot;, unrar uses <code>path_to_extract</code> as file extraction target path.</dd></dl>
<h2>COMMANDS</h2>
<p> After the program name comes a command and then optional switches with dashes before them. A summary of commands is included below. For a complete description, run <code>unrar</code> without options.</p>
<dl>
<dt><code>e</code></dt>
<dd> Extract files to current directory.</dd>
<dt><code>l[t[a],b]</code></dt>
<dd> List archive content [technical[all], bare].</dd>
<dt><code>p</code></dt>
<dd> Print file to stdout.</dd>
<dt><code>t</code></dt>
<dd> Test archive files.</dd>
<dt><code>v[t[a],b]</code></dt>
<dd> Verbosely list archive [technical[all], bare].</dd>
<dt><code>x</code></dt>
<dd> Extract files with full path.</dd></dl>
<h2>OPTIONS</h2>
<p> <code>NOTE:</code> Every switch must be separated by a whitespace. You cannot put them together.</p>
<dl>
<dt><code>&#8211;</code></dt>
<dd> Stop switches scanning.</dd>
<dt><code>@[+]</code></dt>
<dd> Disable [enable] file lists.</dd>
<dt><code>-ad[1,2]</code></dt>
<dd> Alternate destination path</dd>
<dt><code>-ag[format]</code></dt>
<dd> Generate archive name using the current date.</dd>
<dt><code>-ai</code></dt>
<dd> Ignore file attributes.</dd>
<dt><code>-ap&lt;path&gt;</code></dt>
<dd> Set path inside archive.</dd>
<dt><code>-c-</code></dt>
<dd> Disable comments show.</dd>
<dt><code>-cfg-</code></dt>
<dd> Disable read configuration.</dd>
<dt><code>-cl</code></dt>
<dd> Convert names to lower case.</dd>
<dt><code>-cu</code></dt>
<dd> Convert names to upper case.</dd>
<dt><code>-dh</code></dt>
<dd> Open shared files.</dd>
<dt><code>-ep</code></dt>
<dd> Exclude paths from names.</dd>
<dt><code>-ep3</code></dt>
<dd> Expand paths to full name.</dd>
<dt><code>-f</code></dt>
<dd> Freshen files.</dd>
<dt><code>-id[c,d,n,p,q]</code></dt>
<dd> Display or disable messages.</dd>
<dt><code>-kb</code></dt>
<dd> Keep broken extracted files.</dd>
<dt><code>-ierr</code></dt>
<dd> Send all messages to stderr.</dd>
<dt><code>-inul</code></dt>
<dd> Disable all messages.</dd>
<dt><code>-n&lt;file&gt;</code></dt>
<dd> Additionally filter included files.</dd>
<dt><code>-n@</code></dt>
<dd> Read additional filter masks from stdin.</dd>
<dt><code>-n@&lt;list&gt;</code></dt>
<dd> Read additional filter masks from list file.</dd>
<dt><code>-o+</code></dt>
<dd> Overwrite existing files.</dd>
<dt><code>-o-</code></dt>
<dd> Do not overwrite existing files.</dd>
<dt><code>-ol[a]</code></dt>
<dd> Process symbolic links as the link [absolute paths].</dd>
<dt><code>-or</code></dt>
<dd> Rename files automatically.</dd>
<dt><code>-ow</code></dt>
<dd> Save or restore file owner and group.</dd>
<dt><code>-p</code><i>password</i></dt>
<dd> Set password.</dd>
<dt><code>-p-</code></dt>
<dd> Do not query password.</dd>
<dt><code>-r</code></dt>
<dd> Recurse subdirectories.</dd>
<dt><code>-sc&lt;chr&gt;[obj]</code></dt>
<dd> Specify the character set.</dd>
<dt><code>-sl&lt;size&gt;</code></dt>
<dd> Process files with size less than specified.</dd>
<dt><code>-sm&lt;size&gt;</code></dt>
<dd> Process files with size more than specified.</dd>
<dt><code>-ta[mcao]&lt;d&gt;</code></dt>
<dd> Process files modified after &lt;d&gt; YYYYMMDDHHMMSS date.</dd>
<dt><code>-tb[mcao]&lt;d&gt;</code></dt>
<dd> Process files modified before &lt;d&gt; YYYYMMDDHHMMSS date.</dd>
<dt><code>-tn[mcao]&lt;t&gt;</code></dt>
<dd> Process files newer than &lt;t&gt; time.</dd>
<dt><code>-to[mcao]&lt;t&gt;</code></dt>
<dd> Process files older than &lt;t&gt; time.</dd>
<dt><code>-ts[m,c,a,p]</code></dt>
<dd> Save or restore time (modification, creation, access, preserve).</dd>
<dt><code>-u</code></dt>
<dd> Update files.</dd>
<dt><code>-v</code></dt>
<dd> List all volumes.</dd>
<dt><code>-ver[n]</code></dt>
<dd> File version control.</dd>
<dt><code>-vp</code></dt>
<dd> Pause before each volume.</dd>
<dt><code>-x&lt;file&gt;</code></dt>
<dd> Exclude specified file.</dd>
<dt><code>-x@&lt;list&gt;</code></dt>
<dd> Exclude files in specified list file.</dd>
<dt><code>-x@</code></dt>
<dd> Read file names to exclude from stdin.</dd>
<dt><code>-y</code></dt>
<dd> Assume Yes on all queries.</dd></dl>
<h2>FILES</h2>
<dl>
<dt>$HOME/.rarrc</dt>
<dd>
</dd><dt>/etc/.rarrc</dt>
<dd>
</dd><dt>/etc/rar/.rarrc</dt>
<dd>
</dd><dt>/usr/lib/.rarrc</dt>
<dd>
</dd><dt>/usr/local/lib/.rarrc</dt>
<dd>
</dd><dt>/usr/local/etc/.rarrc</dt>
<dd> UnRAR (and RAR) configuration file.</dd>
<dt>Syntax: (switches for all commands)</dt>
<dd> switches=&lt;any RAR switches separated by spaces&gt;</dd>
<dt>Syntax: (switches for specific command)</dt>
<dd> switches_&lt;command&gt;=&lt;any RAR switches separated by spaces&gt;</dd>
<dt>Example:</dt>
<dd> switches=-m5 -s<br />
 switches_a=-m5 -s<br />
 switches_x=-o+</dd></dl>
<h2>AUTHORS</h2>
<p> This manual page was written by Petr Cech &lt;cech [at] debian.org&gt; according to &quot;unrar&quot; for the Debian GNU/Linux system (but may be used by others). </p>
