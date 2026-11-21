---

title: "mimetype(1)"
name: "mimetype"
section: "1"
letter: "m"
url: "/docs/linux/man/1-mimetype/"
description: "mimetype – Determine file type"
---

<p> mimetype [options] [-] files</p>
<p> This script tries to determine the mime type of a file using the Shared MIME-info database. It is intended as a kind of <i><a href="/docs/linux/man/1-file/">file</a>(1)</i> work-alike, but uses mimetypes instead of descriptions. </p>
<p> If one symlinks the <i>file</i> command to <i>mimetype</i> it will behave a little more compatible, see &#8220;&#8211;file-compat&#8221;. Commandline options to specify alternative magic files are not implemented the same because of the conflicting data formats. Also the wording of the descriptions will differ. </p>
<p> For naming switches I followed the manpage of <i><a href="/docs/linux/man/1-file/">file</a></i>(1) version 4.02 when possible. They seem to differ completely from the spec in the &#8216;utilities&#8217; chapter of <font SIZE="-1">IEEE</font> Std 1003.1-2001 (<font SIZE="-1">POSIX</font>).</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-a</code>, <code>&#8211;all</code></dt>
<dd> Show output of all rules that match the file. </dd>
<p> <font SIZE="-1">TODO:</font> this method now just returns one match for each method (globs, magic, etc.).</p>
<dt><code>-b</code>, <code>&#8211;brief</code></dt>
<dd> Do not prepend filenames to output lines (brief mode).</dd>
<dt><code>&#8211;database</code>=<i>mimedir</i>:<i>mimedir</i>:&#8230;</dt>
<dd> Force the program to look in these directories for the shared mime-info database. The directories specified by the basedir specification are ignored.</dd>
<dt><code>-d</code>, <code>&#8211;describe</code></dt>
<dd> Print file descriptions instead of mime types, this is the default when using &#8220;&#8211;file-compat&#8221;.</dd>
<dt><code>-D</code>, <code>&#8211;debug</code></dt>
<dd> Print debug information about how the mimetype was determined.</dd>
<dt><code>-f</code> <i>namefile</i>, <code>&#8211;namefile</code>=<i>namefile</i></dt>
<dd> Read the names of the files to be examined from the file &#8216;namefile&#8217; (one per line) before the argument list.</dd>
<dt><code>&#8211;file-compat</code></dt>
<dd> Make mimetype behave a little more <i><a href="/docs/linux/man/1-file/">file</a></i>(1) compatible. This is turned on automatically when you call mimetype by a link called &#8216;file&#8217;. </dd>
<p> A single &#8216;-&#8216; won&#8217;t be considered a separator between options and filenames anymore, but becomes identical to &#8220;&#8211;stdin&#8221;. ( You can still use &#8216;&#8211;&#8216; as separator, but that is not backward compatible with the original file command. ) Also the default becomes to print descriptions instead of mimetypes.</p>
<dt><code>-F</code> <i>string</i>, <code>&#8211;separator</code>=<i>string</i></dt>
<dd> Use string as custom separator between the file name and its mimetype or description, defaults to &#8216;:&#8217; .</dd>
<dt><code>-h</code>, <code>&#8211;help</code></dt>
<dd>
</dd><dt><code>-u</code>, <code>&#8211;usage</code></dt>
<dd> Print a help message and exits.</dd>
<dt><code>-i</code>, <code>&#8211;mimetype</code></dt>
<dd> Use mime types, opposite to &#8220;&#8211;describe&#8221;, this is the default when _not_ using &#8220;&#8211;file-compat&#8221;.</dd>
<dt><code>-L</code>, <code>&#8211;dereference</code></dt>
<dd> Follow symbolic links.</dd>
<dt><code>-l</code> <i>code</i>, <code>&#8211;language</code>=<i>code</i></dt>
<dd> The language attribute specifies a two letter language code, this makes descriptions being outputted in the specified language.</dd>
<dt><code>-M</code>, <code>&#8211;magic-only</code></dt>
<dd> Do not check for extensions, globs or inode type, only look at the content of the file. This is particularly useful if for some reason you don&#8217;t trust the name or the extension a file has.</dd>
<dt><code>-N</code>, <code>&#8211;noalign</code></dt>
<dd> Do not align output fields.</dd>
<dt><code>&#8211;output-format</code></dt>
<dd> If you want an alternative output format, you can specify a format string containing the following escapes: </dd>
<pre>
        %f for the filename
        %d description
        %m mime type
</pre>
<p> Alignment is not available when using this, you need to post-process the output to do that.</p>
<dt><code>&#8211;stdin</code></dt>
<dd> Determine type of content from <font SIZE="-1">STDIN,</font> less powerful then normal file checking because it only uses magic typing. This will happen also if the <font SIZE="-1">STDIN</font> filehandle is a pipe. </dd>
<p> To use this option IO::Scalar needs to be installed.</p>
<dt><code>-v</code>, <code>&#8211;version</code></dt>
<dd> Print the version of the program and exit.</dd></dl>
<h2>ENVIRONMENT</h2>
<dl>
<dt><font SIZE="-1">XDG_DATA_HOME</font></dt>
<dd>
</dd><dt><font SIZE="-1">XDG_DATA_DIRS</font></dt>
<dd> These variables can list base directories to search for data files. The shared mime-info will be expected in the &#8220;mime&#8221; sub directory of one of these directories. If these are not set, there will be searched for the following directories: </dd>
<pre>
        $HOME/.local/share/mime
        /usr/local/share/mime
        /usr/share/mime
</pre>
<p> See also the &#8220;<font SIZE="-1">XDG</font> Base Directory Specification&#8221; &lt;<a rel="nofollow" href="http://freedesktop.org/Standards/basedir-spec">http://freedesktop.org/Standards/basedir-spec</a>&gt;</dl>
<h2>FILES</h2>
<p> The base dir for all data files is determined by two environment variables, see &#8220;<font SIZE="-1">ENVIRONMENT&#8221;</font>.</p>
<dl>
<dt><i>BASE/mime/packages/SOURCE.xml</i></dt>
<dd> All other files are compiled from these source files. To re-compile them use <a href="/docs/linux/man/1-update-mime-database/">update-mime-database</a><code>(1)</code>.</dd>
<dt><i>BASE/mime/globs</i></dt>
<dd> Compiled information about globs.</dd>
<dt><i>BASE/mime/magic</i></dt>
<dd> Compiled information about magic numbers.</dd>
<dt><i>BASE/mime/MEDIA/SUBTYPE.xml</i></dt>
<dd> Descriptions of a mimetype in multiple languages, used for the &#8220;&#8211;describe&#8221; switch.</dd></dl>
<h2>DIAGNOSTICS</h2>
<p> If a file has an empty mimetype or an empty description, most probably the file doesn&#8217;t exist and the given name doesn&#8217;t match any globs. An empty description can also mean that there is no description available in the language you specified. </p>
<p> The program exits with a non-zero exit value if either the commandline arguments failed, a module it depends on wasn&#8217;t found or the shared mime-info database wasn&#8217;t accessible. See File::MimeInfo for more details.</p>
<h2>TODO</h2>
<p> The &#8216;&#8211;all&#8217; switch doesn&#8217;t really show all matches, but only one per mime-typing method. This needs to be implemented in the modules first.</p>
<h2>BUGS</h2>
<p> No known bugs, please mail the author if you find one. </p>
<p> <code>mimetype</code> doesn&#8217;t provide a switch for looking inside compressed files because it seems to me that this can only be done by un-compressing the file, something that defeats the purpose. On the other hand the option should exist for strict compatibility with <i><a href="/docs/linux/man/1-file/">file</a></i>(1). Possibly a subclass should be made for this one day.</p>
<h2>AUTHOR</h2>
<p> Jaap Karrssenberg &lt;pardus [at] cpan.org&gt;</p>
<h2>COPYRIGHT</h2>
<p> Copyright (c) 2003, 2012 Jaap G Karssenberg. All rights reserved. This program is free software; you can redistribute it and/or modify it under the same terms as Perl. </p>
<p> This program is distributed in the hope that it will be useful, but <font SIZE="-1">WITHOUT ANY WARRANTY</font>; without even the implied warranty of <font SIZE="-1">MERCHANTABILITY</font> or <font SIZE="-1">FITNESS FOR A PARTICULAR PURPOSE.</font></p>
<h2>SEE ALSO</h2>
<p> <i><a href="/docs/linux/man/1-file/">file</a></i>(1), <i><a href="/docs/linux/man/1-update-mime-database/">update-mime-database</a></i>(1), <i>File::MimeInfo</i>(3), &lt;<a rel="nofollow" href="http://freedesktop.org/Software/shared-mime-info">http://freedesktop.org/Software/shared-mime-info</a>&gt; </p>
