---
title: "lessfile(1)"
name: "lessfile"
section: "1"
letter: "l"
url: "/docs/linux/man/1-lessfile/"
description: "lessfile, lesspipe – \"input preprocessor\" for less."
---

<h2 class="name">NAME</h2>
<p> lessfile, lesspipe &#8211; &quot;input preprocessor&quot; for less. </p>
<h2>SYNOPSIS</h2>
<p> <code>lessfile, lesspipe</code></p>
<h2>DESCRIPTION</h2>
<p> This manual page documents briefly the <i>lessfile</i>, and <i>lesspipe</i> commands. This manual page was written for the Debian GNU/Linux distribution because the input preprocessor scripts are provided by Debian GNU/Linux and are not part of the original program. </p>
<p> <i>lessfile</i> and <i>lesspipe</i> are programs that can be used to modify the way the contents of a file are displayed in <i>less.</i> What this means is that <i>less</i> can automatically open up tar files, uncompress gzipped files, and even display something reasonable for graphics files. </p>
<p> <i>lesspipe</i> will toss the contents/info on STDOUT and <i>less</i> will read them as they come across. This means that you do not have to wait for the decoding to finish before less shows you the file. This also means that you will get a &#8216;byte N&#8217; instead of an N% as your file position. You can seek to the end and back to get the N% but that means you have to wait for the pipe to finish. </p>
<p> <i>lessfile</i> will toss the contents/info on a file which <i>less</i> will then read. After you are done, <i>lessfile</i> will then delete the file. This means that the process has to finish before you see it, but you get nice percentages (N%) up front.</p>
<h2>USAGE</h2>
<p> Just put one of the following two commands in your login script (e.g. ~/.bash_profile): </p>
<p>&nbsp;<wbr>&nbsp;eval&nbsp;&quot;$(lessfile)&quot; </p>
<p> or </p>
<p>&nbsp;<wbr>&nbsp;eval&nbsp;&quot;$(lesspipe)&quot;</p>
<h2>FILE TYPE RECOGNITION</h2>
<p> File types are recognized by their extensions. This is a list of currently supported extensions (grouped by the programs that handle them): </p>
<p>&nbsp;<wbr>&nbsp;*.a<br />
&nbsp;<wbr>&nbsp;*.arj<br />
&nbsp;<wbr>&nbsp;*.tar.bz2<br />
&nbsp;<wbr>&nbsp;*.bz<br />
&nbsp;<wbr>&nbsp;*.bz2<br />
&nbsp;<wbr>&nbsp;*.deb,&nbsp;*.udeb,&nbsp;*.ddeb<br />
&nbsp;<wbr>&nbsp;*.doc<br />
&nbsp;<wbr>&nbsp;*.egg<br />
&nbsp;<wbr>&nbsp;*.gif,&nbsp;*.jpeg,&nbsp;*.jpg,&nbsp;*.pcd,&nbsp;*.png,&nbsp;*.tga,&nbsp;*.tiff,&nbsp;*.tif<br />
&nbsp;<wbr>&nbsp;*.iso,&nbsp;*.raw,&nbsp;*.bin<br />
&nbsp;<wbr>&nbsp;*.lha,&nbsp;*.lzh<br />
&nbsp;<wbr>&nbsp;*.tar.lz,&nbsp;*.tlz<br />
&nbsp;<wbr>&nbsp;*.lz<br />
&nbsp;<wbr>&nbsp;*.7z<br />
&nbsp;<wbr>&nbsp;*.pdf<br />
&nbsp;<wbr>&nbsp;*.rar,&nbsp;*.r[0-9][0-9]<br />
&nbsp;<wbr>&nbsp;*.rpm<br />
&nbsp;<wbr>&nbsp;*.tar.gz,&nbsp;*.tgz,&nbsp;*.tar.z,&nbsp;*.tar.dz<br />
&nbsp;<wbr>&nbsp;*.gz,&nbsp;*.z,&nbsp;*.dz<br />
&nbsp;<wbr>&nbsp;*.tar<br />
&nbsp;<wbr>&nbsp;*.tar.xz,&nbsp;*.xz<br />
&nbsp;<wbr>&nbsp;*.whl<br />
&nbsp;<wbr>&nbsp;*.jar,&nbsp;*.war,&nbsp;*.xpi,&nbsp;*.zip<br />
&nbsp;<wbr>&nbsp;*.zoo<br />
&nbsp;<wbr>&nbsp;*.tar.zst,&nbsp;*.tzst<br />
&nbsp;<wbr>&nbsp;*.zst</p>
<h2>USER DEFINED FILTERS</h2>
<p> It is possible to extend and overwrite the default <i>lesspipe</i> and <i>lessfile</i> input processor if you have specialized requirements. Create an executable program with the name <i>.lessfilter</i> and put it into your home directory. This can be a shell script or a binary program. </p>
<p> It is important that this program returns the correct exit code: return 0 if your filter handles the input, return 1 if the standard <i>lesspipe/lessfile</i> filter should handle the input. </p>
<p> Here is an example script: </p>
<p>&nbsp;<wbr>&nbsp;#!/bin/sh </p>
<p>&nbsp;<wbr>&nbsp;case&nbsp;&quot;$1&quot;&nbsp;in<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;*.extension)<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;extension-handler&nbsp;&quot;$1&quot;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;;;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;*)<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;#&nbsp;We don&#8217;t handle this format.<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;exit 1<br />
&nbsp;<wbr>&nbsp;esac </p>
<p>&nbsp;<wbr>&nbsp;#&nbsp;No further processing by lesspipe necessary<br />
&nbsp;<wbr>&nbsp;exit 0 </p>
<h2>FILES</h2>
<dl>
<dt><i>~/.lessfilter</i></p>
<dd> Executable file that can do user defined processing. See section USER DEFINED FILTERS for more information.</dl>
<h2>BUGS</h2>
<p> Sometimes, less does not display the contents file you want to view but output that is produced by your login scripts (~/.bashrc or ~/.bash_profile). This happens because less uses your current shell to run the lesspipe filter. Bash first looks for the variable $BASH_ENV in the environment expands its value and uses the expanded value as the name of a file to read and execute. If this file produces any output less will display this. A way to solve this problem is to put the following lines on the top of your login script that produces output: </p>
<p>&nbsp;<wbr>&nbsp;if&nbsp;[&nbsp;-z&nbsp;&quot;$PS1&quot;&nbsp;];&nbsp;then<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;exit<br />
&nbsp;<wbr>&nbsp;fi </p>
<p> This tests whether the prompt variable $PS1 is set and if it isn&#8217;t (which is the case for non-interactive shells) it will exit the script.</p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-less/">less</a>(1)</p>
<h2>AUTHOR</h2>
<p> This manual page was written by Thomas Schoepf &lt;schoepf [at] debian.org&gt;, for the Debian GNU/Linux system (but may be used by others). Most of the text was copied from a description written by Darren Stalder &lt;torin [at] daft.com&gt;. </p>
<h2>Index</h2>
