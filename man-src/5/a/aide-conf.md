---
title: "aide-conf(5)"
name: "aide-conf"
section: "5"
letter: "a"
url: "/docs/linux/man/5-aide-conf/"
description: "aide.conf – The configuration file for Advanced Intrusion Detection Environment"
---

<p>aide.conf &#8211; The configuration file for Advanced Intrusion Detection Environment </p>
<h2>Synopsis</h2>
<p><code>aide.conf</code> is the configuration file for Advanced Intrusion Detection Environment. <code>aide.conf</code> contains the runtime configuration aide uses to initiailize or check the aide database. </p>
<h2>File Format</h2>
<p><code>aide.conf</code> is similar in to Tripwire(tm)&#8217;s configuration file. With little effort tw.conf can be converted to aide.conf. </p>
<p> aide.conf is case-sensitive. Leading and trailing whitespaces are ignored. </p>
<p> There are three types of lines in <code>aide.conf</code>. First there are the configuration lines which are used to set configuration parameters and define/undefine variables. Second, there are selection lines that are used to indicate which files are added to the database. Third, macro lines define or undefine variables within the config file. Lines beginning with # are ignored as comments.</p>
<h2>Config Lines</h2>
<p>These lines have the format parameter=value. See URLS for a list of valid urls. </p>
<dl>
<dt>database</dt>
<dd>The url from which database is read. There can only be one of these lines. If there are multiple database lines then the first is used. The default value is &quot;/usr/etc/aide.db&quot;.</dd>
<dt>database_out</dt>
<dd>The url to which the new database is written to. There can only be one of these lines. If there are multiple database_out lines then the first is used. The default value is &quot;/usr/etc/aide.db.new&quot;.</dd>
<dt>database_new</dt>
<dd>The url from which the other database for &#8211;compare is read. There is no default for this one.</dd>
<dt>verbose</dt>
<dd>The level of messages that is output. This value can be 0-255 inclusive. This parameter can only be given once. Value from the first occurence is used. If &#8211;verbose or -V is used then the value from that is used. The default is 5. If verbosity is 20 then additional report output is written when doing &#8211;check, &#8211;update or &#8211;compare.</dd>
<dt>report_url</dt>
<dd>The url that the output is written to. There can be multiple instances of this parameter. Output is written to all of them. The default is stdout.</dd>
<dt>gzip_dbout</dt>
<dd>Whether the output to the database is gzipped or not. Valid values are yes,true,no and false. The default is no. This option is available only if zlib support is compiled in.</dd>
<dt>acl_no_symlink_follow</dt>
<dd>Whether to check ACLs for symlinks or not. Valid values are yes,true,no and false. The default is to follow symlinks. This option is available only if acl support is compiled in.</dd>
<dt>warn_dead_symlinks</dt>
<dd>Whether to warn about dead symlinks or not. Valid values are yes,true,no and false. The default is not to warn about dead symlinks.</dd>
<dt>grouped</dt>
<dd>Whether to group the files in the report by added, removed and changed files or not. Valid values are yes, true, no and false. The default is to group the files in the report.</dd>
<dt>summarize_changes</dt>
<dd>Whether to summarize changes in the added, removed and changed files sections of the report or not. Valid values are yes,true,no and false. The default is not to summarize the changes. </dd>
<p> The general format is like the string YlZbpugamcinCAXSE, where Y is replaced by the file-type (<code>f</code> for a regular file, <code>d</code> for a directory, <code>L</code> for a symbolic link, <code>D</code> for a character device, <code>B</code> for a block device, <code>F</code> for a FIFO, <code>s</code> for a unix socket, <code>|</code> for a Solaris door, <code>!</code> if file type has changed and <code>?</code> otherwise). </p>
<p> The Z is replaced as follows: A <code>=</code> means that the size has not changed, a <code>&lt;</code> reports a shrinked size and a <code>&gt;</code> reports a grown size. </p>
<p> The other letters in the string are the actual letters that will be output if the associated attribute for the item has been changed or a &quot;.&quot; for no change, a &quot;+&quot; if the attribute has been added, a &quot;-&quot; if it has been removed, a &quot;:&quot; if the attribute is listed in ignore_list or a &quot; &quot; if the attribute has not been checked. The exceptions to this are: (1) a newly created file replaces each letter with a &quot;+&quot;, and (2) a removed file replaces each letter with a &quot;-&quot;. </p>
<p> The attribute that is associated with each letter is as follows: </p>
<dl>
<dd>
</dd><dl>
<dt>o</dt>
<dd>A <code>l</code> means that the link name has changed.</dd>
<dt>o</dt>
<dd>A <code>b</code> means that the block count has changed.</dd>
<dt>o</dt>
<dd>A <code>p</code> means that the permissions have changed.</dd>
<dt>o</dt>
<dd>An <code>u</code> means that the uid has changed.</dd>
<dt>o</dt>
<dd>A <code>g</code> means that the gid has changed.</dd>
<dt>o</dt>
<dd>An <code>a</code> means that the access time has changed.</dd>
<dt>o</dt>
<dd>A <code>m</code> means that the modification time has changed.</dd>
<dt>o</dt>
<dd>A <code>c</code> means that the change time has changed.</dd>
<dt>o</dt>
<dd>An <code>i</code> means that the inode has changed.</dd>
<dt>o</dt>
<dd>A <code>n</code> means that the link count has changed.</dd>
<dt>o</dt>
<dd>A <code>C</code> means that one or more checksums have changed.</dd></dl>
</dl>
<dl>
<dd>The following letters are only available when explicitly enabled using configure:</dd></dl>
<dl>
<dd>
</dd><dl>
<dt>o</dt>
<dd>A <code>A</code> means that the access control list has changed.</dd>
<dt>o</dt>
<dd>A <code>X</code> means that the extended attributes have changed.</dd>
<dt>o</dt>
<dd>A <code>S</code> means that the SELinux attributes have changed.</dd>
<dt>o</dt>
<dd>A <code>E</code> means that the file attributes on a second extended file system have changed.</dd></dl>
</dl>
<dt>report_attributes</dt>
<dd>Special group definition that lists parameters which are always printed in the final report for changed files.</dd>
<dt>ignore_list</dt>
<dd>Special group definition that lists parameters which are to be ignored from the final report.</dd>
<dt>config_version</dt>
<dd>The value of config_version is printed in the report and also printed to the database. This is for informational purposes only. It has no other functionality.</dd>
<dt>Group definitions</dt>
<dd>If the parameter is not one of the previous parameters then it is regarded as a group definition. Value is then regarded as an expression. Expression is of the following form.</dd>
<dd>
<pre> &lt;predefined group&gt;| &lt;expr&gt; + &lt;predefined group&gt;
 | &lt;expr&gt; - &lt;predifined group&gt;</pre>
</dd><dd>See DEFAULT GROUPS for an explanation of default predefined groups. Note that this is different from the way Tripwire(tm) does it.</dd>
<dd>There is also a special group named &quot;ignore_list&quot;. The predefined -groups listed in it are NOT displayed in the final report.</dd></dl>
<h2>Selection Lines</h2>
<p>aide supports three types of selection lines (regular, negative, equals) Lines beginning with &quot;/&quot; are regular selection lines. Lines beginning with &quot;=&quot; are equals selection lines. And lines beginning with &quot;!&quot; are negative selection lines. The string following the first character is taken as a regular expression matching to a complete filename, including the path. In a regular selection rule the &quot;/&quot; is included in the regular expression. Special characters in your filenames can be escaped using two-digit URL encoding (for example, %20 to represent a space). Following the regular expression is a group definition as explained above. See EXAMPLES and doc/aide.conf for examples. </p>
<p> More in-depth discussion of the selection algorithm can be found in the aide manual.</p>
<dl>
<dd></dd></dl>
<h2>Macro Lines</h2>
<dl>
<dt>@@define <code>VAR</code> <code>val</code></dt>
<dd>Define variable <code>VAR</code> to value <code>val</code>.</dd>
<dt>@@undef <code>VAR</code></dt>
<dd>Undefine variable <code>VAR</code>.</dd>
<dt>@@ifdef <code>VAR</code>, @@ifndef <code>VAR</code></dt>
<dd>@@ifdef begins an if statement. It must be terminated with an @@endif statement. The lines between @@ifdef and @@endif are used if variable <code>VAR</code> is defined. If there is an @@else statement then the part between @@ifdef and @@else is used is <code>VAR</code> is defined otherwise the part between @@else and @@endif is used. @@ifndef reverses the logic of @@ifdef statement but otherwise works similarly.</dd>
<dt>@@ifhost <code>hostname</code>, @@ifnhost <code>hostname</code></dt>
<dd>@@ifhost works like @@ifdef only difference is that it checks whether <code>hostname</code> equals the name of the host that aide is running on. <code>hostname</code> is the name of the host without the domainname (hostname, not hostname.aide.org).</dd>
<dt>@@{<code>VAR</code>}</dt>
<dd>@@{<code>VAR</code>} is replaced with the value of the variable <code>VAR</code>. If variable <code>VAR</code> is not defined an empty string is used. Unlike Tripwire(tm) @@VAR is NOT supported. One special <code>VAR</code> is @@{HOSTNAME} which is substituted for the hostname of the current system.</dd>
<dt>@@else</dt>
<dd>Begins the else part of an if statement.</dd>
<dt>@@endif</dt>
<dd>Ends an if statement.</dd>
<dt>@@include <code>VAR</code></dt>
<dd>Includes the file <code>VAR</code>. The content of the file is used as if it were inserted in this part of the config file.</dd></dl>
<h2>Urls</h2>
<p>Urls can be one of the following. Input urls cannot be used as outputs and vice versa.</p>
<dl>
<dt>stdout</dt>
<dd>
</dd><dt>stderr</dt>
<dd>Output is sent to stdout,stderr respectively.</dd>
<dt>stdin</dt>
<dd>Input is read from stdin.</dd>
<dt>file://<code>filename</code></dt>
<dd>Input is read from <code>filename</code> or output is written to <code>filename</code>.</dd>
<dt>fd:<code>number</code></dt>
<dd>Input is read from filedescriptor <code>number</code> or output is written to <code>number</code>.</dd></dl>
<h2>Default Groups</h2>
<dl>
<dt>p:<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>permissions</dt>
<dd>
</dd><dt>ftype: file type</dt>
<dd>
</dd><dt>i:<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>inode</dt>
<dd>
</dd><dt>l:<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>link name</dt>
<dd>
</dd><dt>n:<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>number of links</dt>
<dd>
</dd><dt>u:<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>user</dt>
<dd>
</dd><dt>g:<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>group</dt>
<dd>
</dd><dt>s:<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>size</dt>
<dd>
</dd><dt>b:<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>block count</dt>
<dd>
</dd><dt>m:<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>mtime</dt>
<dd>
</dd><dt>a:<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>atime</dt>
<dd>
</dd><dt>c:<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>ctime</dt>
<dd>
</dd><dt>S:<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>check for growing size</dt>
<dd>
</dd><dt>I:<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>ignore changed filename</dt>
<dd>
</dd><dt>ANF:<tt>&nbsp;<wbr>&nbsp;<wbr></tt>allow new files</dt>
<dd>
</dd><dt>ARF:<tt>&nbsp;<wbr>&nbsp;<wbr></tt>allow removed files</dt>
<dd>
</dd><dt>md5:<tt>&nbsp;<wbr>&nbsp;<wbr></tt>md5 checksum</dt>
<dd>
</dd><dt>sha1: sha1 checksum</dt>
<dd>
</dd><dt>sha256: sha256 checksum</dt>
<dd>
</dd><dt>sha512: sha512 checksum</dt>
<dd>
</dd><dt>rmd160: rmd160 checksum</dt>
<dd>
</dd><dt>tiger: tiger checksum</dt>
<dd>
</dd><dt>haval: haval checksum</dt>
<dd>
</dd><dt>crc32:<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>crc32 checksum</dt>
<dd>
</dd><dt>R:<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>p+ftype+i+l+n+u+g+s+m+c+md5</dt>
<dd>
</dd><dt>L:<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>p+ftype+i+l+n+u+g</dt>
<dd>
</dd><dt>E:<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>Empty group</dt>
<dd>
</dd><dt>&gt;:<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>Growing logfile p+ftype+l+u+g+i+n+S</dt>
<dd>
</dd><dt>And also the following if you have mhash support enabled</dt>
<dd>
</dd><dt>gost: gost checksum</dt>
<dd>
</dd><dt>whirlpool: whirlpool checksum</dt>
<dd>
</dd><dt>The following are available and added to the default groups R, L and &gt;</dt>
<dd>
</dd><dt>only when explicitly enabled using configure</dt>
<dd>
</dd><dt>acl: access control list</dt>
<dd>
</dd><dt>selinux: selinux attributes</dt>
<dd>
</dd><dt>xattrs: extended attributes</dt>
<dd>
</dd><dt>e2fsattrs: file attributes on a second extended file system</dt>
<dd></dd></dl>
<p> Please note that &#8216;I&#8217; and &#8216;c&#8217; are incompatible. When the name of a file<br />
 is changed, it&#8217;s ctime is updated as well. When you put &#8216;c&#8217; and &#8216;I&#8217; in the same rule the, a changed ctime is silently ignored. </p>
<p> When &#8216;ANF&#8217; is used, new files are added to the new database, but are ignored in the report. </p>
<p> When &#8216;ARF&#8217; is used, files missing on disk are omitted from the new database, but are ignored in the report.</p>
<h2>Examples</h2>
<dl>
<dd><code>/<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>R</code></dd></dl>
<p> This adds all files on your machine to the database. This is one line<br />
 is a fully qualified configuration file.</p>
<dl>
<dd><code>!/dev</code></dd></dl>
<p> This ignores the /dev directory structure.</p>
<dl>
<dd><code>=/tmp</code></dd></dl>
<p> Only /tmp is taken into the database. None of its children are added.</p>
<dl>
<dd><code>All</code>=p+i+n+u+g+s+m+c+a+md5+sha1+tiger+rmd160</dd></dl>
<p> This line defines group <code>All</code>. It has all attributes and all md checksum functions. If you absolutely want all digest functions then you should enable mhash support and add +crc32+haval+gost to the end of the definition for <code>All</code>. Mhash support can only be enabled at compile-time. </p>
<h2>Hints</h2>
<dl>
<dd><code>=/foo p+i+l+n+u+g+s+m+c+md5</code></dd>
<dd><code>/foo/bar p+i+l+n+u+g+s+m+c+md5</code></dd></dl>
<p> This config adds all files under /foo because they match to regex /foo, which is equivalent to /foo.* . What you probably want is:</p>
<dl>
<dd><code>=/foo$ p+i+l+n+u+g+s+m+c+md5</code></dd>
<dd><code>/foo/bar p+i+l+n+u+g+s+m+c+md5</code></dd></dl>
<p> Note that the following still works as expected because =/foo$ stop recuring of directory /foo.</p>
<dl>
<dd><code>=/foo p+i+l+n+u+g+s+m+c+md5</code></dd></dl>
<p> In the following, the first is not allowed in AIDE. Use the latter instead.</p>
<dl>
<dd><code>/foo epug</code></dd>
<dd><code>/foo e+p+u+g</code></dd></dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-aide/">aide</a></code>(1) <code><a rel="nofollow" href="http://www.cs.tut.fi/~rammer/aide/manual.html">http://www.cs.tut.fi/~rammer/aide/manual.html</a></code></p>
<h2>Disclaimer</h2>
<p>All trademarks are the property of their respective owners. No animals were harmed while making this webpage or this piece of software.</p>
