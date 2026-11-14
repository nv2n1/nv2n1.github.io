---
title: "dave(1)"
name: "dave"
section: "1"
letter: "d"
url: "/docs/linux/man/1-dave/"
description: "dave – DAV Explorer"
---

<h2 class="name">NAME</h2>
<p> dave &#8211; DAV Explorer </p>
<h2>SYNOPSIS</h2>
<pre>
    dave [OPTIONS] URL
</pre>
<p> E.g. </p>
<pre>
   $ dave -u pcollins -p mypass <a rel="nofollow" href="http://www.host.org">www.host.org</a>/dav_dir/
   ...
   dave&gt; get file.txt
</pre>
<p> Use <tt>&quot;dave -h&quot;</tt> to get help on options. </p>
<p> Use <tt>&quot;perldoc dave&quot;</tt> for the whole manpage.</p>
<h2>DESCRIPTION</h2>
<p> dave is a powerful command-line program for interacting with WebDAV-enabled webservers. With dave you can:</p>
<dl>
<dt>&bull;</p>
<dd> get and put files</p>
<dt>&bull;</p>
<dd> make directories on a remote webserver</p>
<dt>&bull;</p>
<dd> remove files and directories from a remote webserver</p>
<dt>&bull;</p>
<dd> edit a file on the webserver with a single command</p>
<dt>&bull;</p>
<dd> recursively get a remote directory</p>
<dt>&bull;</p>
<dd> recursively put a local directory</p>
<dt>&bull;</p>
<dd> lock and unlock remote files and directories</p>
<dt>&bull;</p>
<dd> securely transfer over https</p>
<dt>&bull;</p>
<dd> authenticate using the safer Digest authentication</dl>
<p> Dave is a part of the PerlDAV project (<a rel="nofollow" href="http://www.webdav.org/perldav/)">http://www.webdav.org/perldav/)</a> and is built on top of the <font SIZE="-1">HTTP::DAV</font> perl <font SIZE="-1">API.</font> </p>
<p> If you would like to script webdav interactions in Perl checkout the <font SIZE="-1">HTTP::DAV API</font> as it&#8217;s commands are the basis for dave&#8217;s.</p>
<h2>OPTIONS</h2>
<dl>
<dt>&quot;-debug N&quot;</p>
<dd> Sets the debug level to N. 0=none. 3=noisy.</p>
<dt>&quot;-h&quot;</p>
<dd> Prints basic help and options.</p>
<dt>&quot;-man&quot;</p>
<dd> Prints the full manual (equivalent to perldoc dave). </p>
<p> You will need to use a pager like <tt>&quot;more&quot;</tt> or <tt>&quot;less&quot;</tt>. e.g. </p>
<pre>
    dave -man |less
</pre>
<dt>&quot;-p &lt;password&gt;&quot;</p>
<dd> Sets the password to be used for the <font SIZE="-1">URL.</font> You must also supply a user. See <tt>&quot;-u&quot;</tt>.</p>
<dt>&quot;-u &lt;username&gt;&quot;</p>
<dd> Sets the username to be used for the <font SIZE="-1">URL.</font> You must also supply a pass. See <tt>&quot;-p&quot;</tt>.</p>
<dt>&quot;-tmpdir /some/path&quot;</p>
<dd> Create temporary files in <tt>&quot;/some/path&quot;</tt> instead of the default <tt>&quot;/tmp&quot;</tt>.</dl>
<h2>COMMANDS</h2>
<dl>
<dt><code>cd </code><font SIZE="-1"><code>URL</code></font></p>
<dd> changes directories </p>
<pre>
   dave&gt; open host.org/dav_dir/
   dave&gt; cd dir1
   dave&gt; cd ../dir2
</pre>
<dt><code>cat </code><font SIZE="-1"><code>URL</code></font></p>
<dd> shows the contents of a remote file </p>
<pre>
   dave&gt; open host.org/dav_dir/
   dave&gt; cat index.html
</pre>
<p> Note: you cannot cat a directory (collection).</p>
<dt><code>cp</code></p>
<dd>
<dt><code>copy </code><font SIZE="-1"><code>SOURCE_URL DEST_URL</code></font></p>
<dd> copies one remote resource to another </p>
<pre>
  dave&gt; open host.org/dav_dir/
</pre>
<p> Create a copy of dir1/ as dav2/ </p>
<pre>
  dave&gt; cp dir1 dav2
</pre>
<p> Create a copy of dir1/file.txt as dav2/file.txt </p>
<pre>
  dave&gt; cd dir1
  dave&gt; copy file.txt ../dav2
</pre>
<p> Create a copy of file.txt as ../dav2/new_file.txt </p>
<pre>
  dave&gt; copy file.txt dav2/new_file.txt
</pre>
<p> Aliases: cp</p>
<dt><code>rmdir </code><font SIZE="-1"><code>URL</code></font></p>
<dd>
<dt><code>rm </code><font SIZE="-1"><code>URL</code></font></p>
<dd>
<dt><code>delete </code><font SIZE="-1"><code>URL</code></font></p>
<dd> deletes a remote resource </p>
<pre>
   dave&gt; open host.org/dav_dir/
   dave&gt; delete index.html
   dave&gt; rmdir ./dir1
   dave&gt; delete /dav_dir/dir2/
   dave&gt; delete /dav_dir/*.html
</pre>
<p> This command recursively deletes directories. <font SIZE="-1">BE CAREFUL :</font>) </p>
<p> This command supported wildcards (globbing). See get. </p>
<p> Aliases: rm, rmdir</p>
<dt><code>edit </code><font SIZE="-1"><code>URL</code></font></p>
<dd> edits the contents of a remote file </p>
<pre>
   dave&gt; open host.org/dav_dir/
   dave&gt; edit index.html
</pre>
<p> Edit is equivalent to the following sequence of commands: </p>
<pre>
   LOCK index.html (if allowed)
   GET index.html /tmp/dave.perldav.421341234124
   sh $EDITOR /tmp/dave.perldav.421341234124
   PUT index.html (if modified)
   UNLOCK index.html (if locked)
</pre>
<p> Where <tt>$EDITOR</tt> is determined from the environment variables <font SIZE="-1">DAV_EDITOR</font> or <font SIZE="-1">EDITOR. </font> </p>
<p> If <font SIZE="-1">DAV_EDITOR</font> is set, it will use that, otherwise it will use <font SIZE="-1">EDITOR.</font> If neither variables are set, then &#8220;vi&#8221; will be used. </p>
<p> Notes: </p>
<p> The lock only lasts for 10 hours. </p>
<p> You cannot edit a directory (collection). </p>
<p> The temporary save directory is editable by editing dave and changing <font SIZE="-1">TMP_DIR</font></p>
<dt><code>get </code><font SIZE="-1"><code>URL</code></font><code> [</code><font SIZE="-1"><code>FILE</code></font><code>]</code></p>
<dd> downloads the file or directory at <font SIZE="-1">URL</font> </p>
<p> If <font SIZE="-1">FILE</font> is not specified it will be saved to your current working directory using the same name as the remote name. </p>
<pre>
  dave&gt; open host.org/dav_dir/
</pre>
<p> Recursively get remote my_dir/ to . </p>
<pre>
  dave&gt; get my_dir/
</pre>
<p> Recursively get remote my_dir/ to /tmp/my_dir/ </p>
<pre>
  dave&gt; get my_dir /tmp
</pre>
<p> Get remote my_dir/index.html to /tmp/index.html </p>
<pre>
  dave&gt; get /dav_dir/my_dir/index.html /tmp
</pre>
<p> Get remote index.html to /tmp/index1.html </p>
<pre>
  dave&gt; get index.html /tmp/index1.html
</pre>
<p> Use globs and save to /tmp </p>
<pre>
  dave&gt; get index* /tmp                   # Gets index*.html, index*.txt, etc.
  dave&gt; get index*.html /tmp/index1.html  # Gets index*.html
  dave&gt; get index[12].htm?                # Gets file1 and file2, .htm and .html
</pre>
<dt><code>? [</code><font SIZE="-1"><code>CMD</code></font><code>]</code></p>
<dd>
<dt><code>h [</code><font SIZE="-1"><code>CMD</code></font><code>]</code></p>
<dd>
<dt><code>help [</code><font SIZE="-1"><code>CMD</code></font><code>]</code></p>
<dd> prints list of commands or help for <font SIZE="-1">CMD</font> </p>
<pre>
  dave&gt; ?
  dave&gt; help get
</pre>
<p> Aliases: ?, h</p>
<dt><code>lcd [</code><font SIZE="-1"><code>DIR</code></font><code>]</code></p>
<dd> changes local directory </p>
<pre>
  dave&gt; lcd /tmp
</pre>
<dt><code>lls [</code><font SIZE="-1"><code>DIR</code></font><code>]</code></p>
<dd> lists local directory contents </p>
<pre>
  dave&gt; lcd /tmp
  dave&gt; lls
  dave&gt; lls /home
</pre>
<p> This command simply execs the local ls command and is equivalent to &#8220;!ls&#8221;</p>
<dt><code>dir [</code><font SIZE="-1"><code>URL</code></font><code>]</code></p>
<dd>
<dt><code>ls [</code><font SIZE="-1"><code>URL</code></font><code>]</code></p>
<dd> lists remote directory contents or file props </p>
<pre>
  dave&gt; ls
  Listing of <a rel="nofollow" href="http://host.org/dav_dir/">http://host.org/dav_dir/</a>
                  ./          Aug 29 02:26  &lt;dir&gt;
     mtx_0.04.tar.gz   52640  Aug 11 11:45
          index.html    4580  Aug 11 11:45
      index0.04.html    4936  Nov 11  2000
              mydir/          Aug 19 21:14  &lt;dir&gt;,&lt;locked&gt;
  dave&gt; ls index.html
  URL: <a rel="nofollow" href="http://www.webdav.org/perldav/index.html">http://www.webdav.org/perldav/index.html</a>
  Content-type: text/html
  Creation date: Sun Aug 12 21:58:02 2001
  Last modified:
  Size: 4580 bytes
  Locks supported: write/exclusive write/shared
  Locks:
</pre>
<p> Use propfind to get a similar printout of a collection (directory). </p>
<p> Aliases: dir</p>
<dt><code>lock [</code><font SIZE="-1"><code>URL</code></font><code> [</code><font SIZE="-1"><code>TIMEOUT</code></font><code>] [</code><font SIZE="-1"><code>DEPTH</code></font><code>]]</code></p>
<dd> locks a resource </p>
<p> Without a <font SIZE="-1">URL</font> you will lock the current remote collection. </p>
<p> <font SIZE="-1">TIMEOUT</font> can be any of the following formats:<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>30s&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>30 seconds from now<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>10m&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>ten minutes from now<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>1h&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>one hour from now<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>1d&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>tomorrow<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>3M&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>in three months<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>10y&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>in ten years time<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>2000-02-31 00:40:33<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>2000-02-31 </p>
<p> Default is an infinite timeout </p>
<p> See perldoc <tt>&quot;HTTP::DAV::Resource&quot;</tt> for more information about timeouts. </p>
<p> <font SIZE="-1">DEPTH</font> can be either &#8220;0&#8221; or &#8220;infinity&#8221; (default) </p>
<p> Seeting the lock Scope and Type is not currently implemented. Let me know if you need it as it shouldn&#8217;t be too much effort.</p>
<dt><code>mkdir </code><font SIZE="-1"><code>URL</code></font></p>
<dd>
<dt><code>mkcol </code><font SIZE="-1"><code>URL</code></font></p>
<dd> make a remote collection (directory) </p>
<pre>
  dave&gt; open host.org/dav_dir/
  dave&gt; mkcol new_dir
  dave&gt; mkdir /dav_dir/new_dir
</pre>
<p> Aliases: mkdir</p>
<dt><code>mv</code></p>
<dd>
<dt><code>move </code><font SIZE="-1"><code>SOURCE_URL DEST_URL</code></font></p>
<dd> moves a remote resource to another </p>
<pre>
  dave&gt; open host.org/dav_dir/
</pre>
<p> Move dir1/ to dav2/ </p>
<pre>
  dave&gt; move dir1 dav2
</pre>
<p> Move file dir2/file.txt to ../file.txt </p>
<pre>
  dave&gt; cd dir2
  dave&gt; move file.txt ..
</pre>
<p> Move file.txt to dav2/new_file.txt </p>
<pre>
  dave&gt; move file.txt dav2/new_file.txt
</pre>
<p> Aliases: mv</p>
<dt><code>open </code><font SIZE="-1"><code>URL</code></font></p>
<dd> connects to the WebDAV-enabled server at <font SIZE="-1">URL</font> </p>
<pre>
   dave&gt; open host.org/dav_dir/
</pre>
<p> Note that if authorization details are required you will be prompted for them. </p>
<p> https and Digest authorization are not currently supported. Please let me know if you need it.</p>
<dt><code>options [</code><font SIZE="-1"><code>URL</code></font><code>]</code></p>
<dd> show the <font SIZE="-1">HTTP</font> methods allowed for a <font SIZE="-1">URL</font> </p>
<pre>
   dave&gt; options index.html
   OPTIONS, GET, HEAD, POST, DELETE, TRACE, PROPFIND, 
   PROPPATCH, COPY, MOVE, LOCK, UNLOCK
</pre>
<p> Note that Microsoft&#8217;s <font SIZE="-1">IIS</font> does not support <font SIZE="-1">LOCK</font> on collections (directories). Nor does it support <font SIZE="-1">PROPPATCH.</font></p>
<dt><code>propfind [</code><font SIZE="-1"><code>URL</code></font><code>]</code></p>
<dd> show the properties of a resource </p>
<pre>
  dave&gt; propfind test
  URL: <a rel="nofollow" href="http://host.org/dav_dir/test/">http://host.org/dav_dir/test/</a>
  Content-type: httpd/unix-directory
  Creation date: Wed Aug 29 00:36:42 2001
  Last modified:
  Size:  bytes
  Locks supported: write/exclusive write/shared
  Locks:
</pre>
<p> Using ls will get you the same printout if you ls a file. But ls&#8217;ing a collection will show you the collections contents.</p>
<dt><code>put </code><font SIZE="-1"><code>FILE</code></font><code> [</code><font SIZE="-1"><code>URL</code></font><code>]</code></p>
<dd> uploads a local file or directory to <font SIZE="-1">URL</font> or the currently opened location. </p>
<p> If <font SIZE="-1">URL</font> is an existing collection then the dir/file will be copied <font SIZE="-1">INTO</font> that collection. </p>
<pre>
  dave&gt; open host.org/dav_dir/
</pre>
<p> Recursively put local my_dir/ to host.org/dav_dir/my_dir/: </p>
<pre>
  dave&gt; put my_dir/
</pre>
<p> Put local index.html to host.org/dav_dir/index1.html: </p>
<pre>
  dave&gt; put /tmp/index.html index1.html
</pre>
<p> Put * to remote directory </p>
<pre>
  dave&gt; put *
</pre>
<p> Put index[12].htm? to remote directory /dav_dir (/dav_dir must exist) </p>
<pre>
  dave&gt; put index[12].htm? /dav_dir
</pre>
<p> Put index[1234].htm? to remote directory /dav_dir (/dav_dir must exist) </p>
<pre>
  dave&gt; put index[1-4].htm? /dav_dir
</pre>
<p> Glob types supported are, * (matches any characters), ? (matches any one character), [&#8230;] (matches any characters in the set &#8230;).</p>
<dt><code>pwd</code></p>
<dd> prints the currently opened <font SIZE="-1">URL </font>(working directory) </p>
<pre>
 dave&gt; open host.org/dav_dir/
 dave&gt; cd new_dir/
 dave&gt; pwd
 <a rel="nofollow" href="http://host.org/dav_dir/new_dir/">http://host.org/dav_dir/new_dir/</a>
</pre>
<dt><code>q</code></p>
<dd>
<dt><code>bye</code></p>
<dd>
<dt><code>quit</code></p>
<dd> exits dave </p>
<p> Note that dave does not unlock any locks created during your session. </p>
<p> Aliases: q, quit</p>
<dt><code>set </code><font SIZE="-1"><code>URL PROPERTY VALUE</code></font><code> [</code><font SIZE="-1"><code>NAMESPACE</code></font><code>]</code></p>
<dd> sets a custom property on a resource </p>
<pre>
   dave&gt; set file.txt author &quot;Patrick Collins&quot;
   dave&gt; set file.txt author &quot;Patrick Collins&quot; &quot;mynamespace&quot;
</pre>
<p> The <font SIZE="-1">NAMESPACE</font> by default is &#8220;<font SIZE="-1">DAV:&#8221;.</font></p>
<dt><code>!</code></p>
<dd>
<dt><code>sh</code></p>
<dd> executes a local command (alias !) </p>
<pre>
   dave&gt; sh cat localfile
   dave&gt; !gzip localfile.gz
   dave&gt; ! &quot;cat localfile | less&quot;
</pre>
<p> Aliases: !</p>
<dt><code>showlocks</code></p>
<dd> show my locks on a resource </p>
<p> Shows any locked resources that you&#8217;ve locked in this session. </p>
<p> See <tt>&quot;propfind&quot;</tt> if you&#8217;d like to see anyone&#8217;s locks held against a particular resource.</p>
<dt><code>steal [</code><font SIZE="-1"><code>URL</code></font><code>]</code></p>
<dd> remove <font SIZE="-1">ANY</font> locks on a resource </p>
<p> Useful if you accidentally forgot to unlock a resource from a previous session or if you think that somebody has forgotten to unlock a resource.</p>
<dt><code>unlock [</code><font SIZE="-1"><code>URL</code></font><code>]</code></p>
<dd> unlocks a resource </p>
<p> Note that unlock will only unlock locks that you have created. Use steal if you want to forcefully unlock somebody else&#8217;s lock.</p>
<dt><code>unset </code><font SIZE="-1"><code>URL PROPERTY</code></font><code> [</code><font SIZE="-1"><code>NAMESPACE</code></font><code>]</code></p>
<dd> unsets a property from a resource </p>
<pre>
   dave&gt; unset file.txt author
   dave&gt; unset file.txt author &quot;mynamespace&quot;
</pre>
<p> The <font SIZE="-1">NAMESPACE</font> by default is &#8220;<font SIZE="-1">DAV:&#8221;.</font></dl>
<h2>GETTING HELP</h2>
<p> The perldav mailing list There is a mailing list for PerlDAV and dave for use by Developers and Users. Please see <a rel="nofollow" href="http://mailman.webdav.org/mailman/listinfo/perldav">http://mailman.webdav.org/mailman/listinfo/perldav</a></p>
<h2>INSTALLATION</h2>
<p> dave is installed to /usr/local/bin by default when you install the PerlDAV library. See <a rel="nofollow" href="http://www.webdav.org/perldav/">http://www.webdav.org/perldav/</a> for installation details of PerlDAV.</p>
<h2>WHAT PLATFORMS WILL IT WORK ON?</h2>
<p> dave is pure perl so only needs Perl5.003 (or later) and the <tt>&quot;PerlDAV&quot;</tt> library to be installed. </p>
<p> I have not ported dave to Windows but would like somebody to have a shot at it.</p>
<h2>SEE ALSO</h2>
<p> The <tt>&quot;PerlDAV&quot;</tt> perl <font SIZE="-1">API</font> at <a rel="nofollow" href="http://www.webdav.org/perldav/">http://www.webdav.org/perldav/</a> or by typing &#8220;perldoc <font SIZE="-1">HTTP::DAV&#8221;</font> on your command line.</p>
<h2>AUTHOR AND COPYRIGHT</h2>
<p> This module is Copyright (C) 2001 by </p>
<pre>
    Patrick Collins
    G03 Gloucester Place, Kensington
    Sydney, Australia
    Email: pcollins [at] cpan.org
    Phone: +61 2 9663 4916
</pre>
<p> All rights reserved. </p>
<p> You may distribute this module under the terms of either the <font SIZE="-1">GNU</font> General Public License or the Artistic License, as specified in the Perl <font SIZE="-1">README</font> file.</p>
<h2>MAINTAINER</h2>
<p> Cosimo Streppone, &lt;cosimo [at] cpan.org&gt; </p>
<h2>Index</h2>
