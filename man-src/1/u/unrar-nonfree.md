---
title: "unrar-nonfree(1)"
name: "unrar-nonfree"
section: "1"
letter: "u"
url: "/docs/linux/man/1-unrar-nonfree/"
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
<dt><code>archive</code></p>
<dd> Archive file name in RAR or other supported format. If archive file uses RAR multiple volume format, specify only first volume file name as <code>archive</code> file name.</p>
<dt><code>file &#8230;</code></p>
<dd> File path name to extract. You can specify more path names at one time.</p>
<dt><code>@listfiles &#8230;</code></p>
<dd> If argument starts with &quot;@&quot;, unrar uses <code>listfile</code> as file path list file. This list file includes file path list to extract from archive file. You can use 2 or more list files at one time.<br />
 File list uses one line for one file path. And blank line is ignored.<br />
 This file is used to extract many file path names in one time that your shell can&#8217;t accept.</p>
<dt><code>path_to_extract</code></p>
<dd> If last argument is ended with &quot;/&quot;, unrar uses <code>path_to_extract</code> as file extraction target path.</dl>
<h2>COMMANDS</h2>
<p> After the program name comes a command and then optional switches with dashes before them. A summary of commands is included below. For a complete description, run <code>unrar</code> without options.</p>
<dl>
<dt><code>e</code></p>
<dd> Extract files to current directory.</p>
<dt><code>l[t[a],b]</code></p>
<dd> List archive content [technical[all], bare].</p>
<dt><code>p</code></p>
<dd> Print file to stdout.</p>
<dt><code>t</code></p>
<dd> Test archive files.</p>
<dt><code>v[t[a],b]</code></p>
<dd> Verbosely list archive [technical[all], bare].</p>
<dt><code>x</code></p>
<dd> Extract files with full path.</dl>
<h2>OPTIONS</h2>
<p> <code>NOTE:</code> Every switch must be separated by a whitespace. You cannot put them together.</p>
<dl>
<dt><code>&#8211;</code></p>
<dd> Stop switches scanning.</p>
<dt><code>@[+]</code></p>
<dd> Disable [enable] file lists.</p>
<dt><code>-ad[1,2]</code></p>
<dd> Alternate destination path</p>
<dt><code>-ag[format]</code></p>
<dd> Generate archive name using the current date.</p>
<dt><code>-ai</code></p>
<dd> Ignore file attributes.</p>
<dt><code>-ap&lt;path&gt;</code></p>
<dd> Set path inside archive.</p>
<dt><code>-c-</code></p>
<dd> Disable comments show.</p>
<dt><code>-cfg-</code></p>
<dd> Disable read configuration.</p>
<dt><code>-cl</code></p>
<dd> Convert names to lower case.</p>
<dt><code>-cu</code></p>
<dd> Convert names to upper case.</p>
<dt><code>-dh</code></p>
<dd> Open shared files.</p>
<dt><code>-ep</code></p>
<dd> Exclude paths from names.</p>
<dt><code>-ep3</code></p>
<dd> Expand paths to full name.</p>
<dt><code>-f</code></p>
<dd> Freshen files.</p>
<dt><code>-id[c,d,n,p,q]</code></p>
<dd> Display or disable messages.</p>
<dt><code>-kb</code></p>
<dd> Keep broken extracted files.</p>
<dt><code>-ierr</code></p>
<dd> Send all messages to stderr.</p>
<dt><code>-inul</code></p>
<dd> Disable all messages.</p>
<dt><code>-n&lt;file&gt;</code></p>
<dd> Additionally filter included files.</p>
<dt><code>-n@</code></p>
<dd> Read additional filter masks from stdin.</p>
<dt><code>-n@&lt;list&gt;</code></p>
<dd> Read additional filter masks from list file.</p>
<dt><code>-o+</code></p>
<dd> Overwrite existing files.</p>
<dt><code>-o-</code></p>
<dd> Do not overwrite existing files.</p>
<dt><code>-ol[a]</code></p>
<dd> Process symbolic links as the link [absolute paths].</p>
<dt><code>-or</code></p>
<dd> Rename files automatically.</p>
<dt><code>-ow</code></p>
<dd> Save or restore file owner and group.</p>
<dt><code>-p</code><i>password</i></p>
<dd> Set password.</p>
<dt><code>-p-</code></p>
<dd> Do not query password.</p>
<dt><code>-r</code></p>
<dd> Recurse subdirectories.</p>
<dt><code>-sc&lt;chr&gt;[obj]</code></p>
<dd> Specify the character set.</p>
<dt><code>-sl&lt;size&gt;</code></p>
<dd> Process files with size less than specified.</p>
<dt><code>-sm&lt;size&gt;</code></p>
<dd> Process files with size more than specified.</p>
<dt><code>-ta[mcao]&lt;d&gt;</code></p>
<dd> Process files modified after &lt;d&gt; YYYYMMDDHHMMSS date.</p>
<dt><code>-tb[mcao]&lt;d&gt;</code></p>
<dd> Process files modified before &lt;d&gt; YYYYMMDDHHMMSS date.</p>
<dt><code>-tn[mcao]&lt;t&gt;</code></p>
<dd> Process files newer than &lt;t&gt; time.</p>
<dt><code>-to[mcao]&lt;t&gt;</code></p>
<dd> Process files older than &lt;t&gt; time.</p>
<dt><code>-ts[m,c,a,p]</code></p>
<dd> Save or restore time (modification, creation, access, preserve).</p>
<dt><code>-u</code></p>
<dd> Update files.</p>
<dt><code>-v</code></p>
<dd> List all volumes.</p>
<dt><code>-ver[n]</code></p>
<dd> File version control.</p>
<dt><code>-vp</code></p>
<dd> Pause before each volume.</p>
<dt><code>-x&lt;file&gt;</code></p>
<dd> Exclude specified file.</p>
<dt><code>-x@&lt;list&gt;</code></p>
<dd> Exclude files in specified list file.</p>
<dt><code>-x@</code></p>
<dd> Read file names to exclude from stdin.</p>
<dt><code>-y</code></p>
<dd> Assume Yes on all queries.</dl>
<h2>FILES</h2>
<dl>
<dt>$HOME/.rarrc</p>
<dd>
<dt>/etc/.rarrc</p>
<dd>
<dt>/etc/rar/.rarrc</p>
<dd>
<dt>/usr/lib/.rarrc</p>
<dd>
<dt>/usr/local/lib/.rarrc</p>
<dd>
<dt>/usr/local/etc/.rarrc</p>
<dd> UnRAR (and RAR) configuration file.</p>
<dt>Syntax: (switches for all commands)</p>
<dd> switches=&lt;any RAR switches separated by spaces&gt;</p>
<dt>Syntax: (switches for specific command)</p>
<dd> switches_&lt;command&gt;=&lt;any RAR switches separated by spaces&gt;</p>
<dt>Example:</p>
<dd> switches=-m5 -s<br />
 switches_a=-m5 -s<br />
 switches_x=-o+</dl>
<h2>AUTHORS</h2>
<p> This manual page was written by Petr Cech &lt;cech [at] debian.org&gt; according to &quot;unrar&quot; for the Debian GNU/Linux system (but may be used by others). </p>
<h2>Index</h2>
