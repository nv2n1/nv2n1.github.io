---

title: "vorbiscomment(1)"
name: "vorbiscomment"
section: "1"
letter: "v"
url: "/docs/linux/man/1-vorbiscomment/"
description: "vorbiscomment – List or edit comments in Ogg Vorbis files"
---

<p> vorbiscomment - List or edit comments in Ogg Vorbis files  </p>
<h2>SYNOPSIS</h2>
<p> <code>vorbiscomment</code> <code>[-l]</code> [<code>-R</code>] [<code>-e</code>] <i>file.ogg</i> <br />
 <code>vorbiscomment</code> <code>-a</code> <code>[ -c commentfile | -t ``name=value&#8217;&#8216; ]</code> [<code>-q</code>] [<code>-R</code>] [<code>-e</code>] <i>in.ogg</i> <i>[out.ogg]</i> <br />
 <code>vorbiscomment</code> <code>-w</code> <code>[ -c commentfile | -t ``name=value&#8217;&#8216; ]</code> [<code>-q</code>] [<code>-R</code>] [<code>-e</code>] <i>in.ogg</i> <i>[out.ogg]</i> </p>
<h2>DESCRIPTION</h2>
<p> <code>vorbiscomment</code> Reads, modifies, and appends Ogg Vorbis audio file metadata tags. </p>
<h2>OPTIONS</h2>
<dl>
<dt>-a, --append</dt>
<dd> <p> Append comments. </p>
 </dd>
<dt>-c file, --commentfile file</dt>
<dd> <p> Take comments from a file. The file is the same format as is output by the -l option or given to the -t option: one element per line in &#8216;tag=value&#8217; format. If the file is /dev/null and -w was passed, the existing comments will be removed. </p>
 </dd>
<dt>-h, --help</dt>
<dd> <p> Show command help. </p>
 </dd>
<dt>-l, --list</dt>
<dd> <p> List the comments in the Ogg Vorbis file. </p>
 </dd>
<dt>-t &#8216;name=value&#8217;, --tag &#8216;name=value&#8217;</dt>
<dd> <p> Specify a new tag on the command line. Each tag is given as a single string. The part before the &#8216;=&#8216; is treated as the tag name and the part after as the value. </p>
 </dd>
<dt>-w, --write</dt>
<dd> <p> Replace comments with the new set given either on the command line with -t or from a file with -c. If neither -c nor -t is given, the new set will be read from the standard input. </p>
 </dd>
<dt>-R, --raw</dt>
<dd> <p> Read and write comments in UTF-8, rather than converting to the user&#8217;s character set. </p>
 </dd>
<dt>-e, --escapes</dt>
<dd> <p> Quote/unquote newlines and backslashes in the comments. This ensures every comment is exactly one line in the output (or input), allowing to filter and round-trip them. Without it, you can only write multi-line comments by using -t and you can&#8217;t reliably distinguish them from multiple one-line comments. </p>
<p> Supported escapes are c-style &quot;\n&quot;, &quot;\r&quot;, &quot;\\&quot; and &quot;\0&quot;. A backslash followed by anything else is an error. </p>
<p> Note: currently, anything after the first &quot;\0&quot; is thrown away while writing. This is a bug -- the Vorbis format can safely store null characters, but most other tools wouldn&#8217;t handle them anyway. </p>
 </dd>
<dt>-V, --version</dt>
<dd> <p> Display the version of vorbiscomment. </p>
 </dd></dl>
<h2>EXAMPLES</h2>
<p> To just see what comment tags are in a file: </p>
<p> <br />
&nbsp;<wbr>vorbiscomment -l file.ogg </p>
<p> To edit those comments: </p>
<p> <br />
&nbsp;<wbr>vorbiscomment -l file.ogg&nbsp;<wbr>&gt;&nbsp;<wbr>file.txt <br />
&nbsp;<wbr>[edit the comments in file.txt to your satisfaction] <br />
&nbsp;<wbr>vorbiscomment -w -c file.txt file.ogg newfile.ogg </p>
<p> To simply add a comment: </p>
<p> <br />
&nbsp;<wbr>vorbiscomment -a -t&nbsp;<wbr>&#8216;ARTIST=No One You Know&#8217;&nbsp;<wbr>file.ogg newfile.ogg </p>
<p> To add a set of comments from the standard input: </p>
<p> <br />
&nbsp;<wbr>vorbiscomment -a file.ogg <br />
&nbsp;<wbr>ARTIST=No One You Know <br />
&nbsp;<wbr>ALBUM=The Famous Album <br />
&nbsp;<wbr>&lt;ctrl-d&gt; </p>
<h2>TAG FORMAT</h2>
<p> See <a rel="nofollow" href="http://xiph.org/vorbis/doc/v-comment.html">http://xiph.org/vorbis/doc/v-comment.html</a> for documentation on the Ogg Vorbis tag format, including a suggested list of canonical tag names. </p>
<h2>AUTHORS</h2>
<dl>
<dt>Program Authors:</dt>
<dd> <p> <br />
 Michael Smith &lt;msmith [at] xiph.org&gt; <br />
 Ralph Giles &lt;giles [at] xiph.org&gt; <br />
 </p>
 </dd>
<dt>Manpage Author:</dt>
<dd> <p> <br />
 Christopher L Cheney &lt;ccheney [at] debian.org&gt; </p>
 </dd></dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-oggenc/">oggenc</a></code>(1), <code><a href="/docs/linux/man/1-oggdec/">oggdec</a></code>(1), <code><a href="/docs/linux/man/1-ogg123/">ogg123</a></code>(1), <code><a href="/docs/linux/man/1-ogginfo/">ogginfo</a></code>(1) </p>
