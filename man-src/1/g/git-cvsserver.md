---
title: "git-cvsserver(1)"
name: "git-cvsserver"
section: "1"
letter: "g"
url: "/docs/linux/man/1-git-cvsserver/"
description: "git-cvsserver – A CVS server emulator for Git"
---

<h2 class="name">NAME</h2>
<p> git-cvsserver &#8211; A CVS server emulator for Git </p>
<h2>SYNOPSIS</h2>
<p> SSH: </p>
<pre>
export CVS_SERVER=&quot;git cvsserver&quot;
<i>cvs</i> -d :ext:user [at] server/path/repo.git co &lt;HEAD_name&gt;
</pre>
<p> pserver (/etc/inetd.conf): </p>
<pre>
cvspserver stream tcp nowait nobody /usr/bin/git-cvsserver git-cvsserver pserver
</pre>
<p> Usage: </p>
<pre><code>
git - cvsserver[options][pserver | server][&lt;directory&gt;...]
</code></pre>
<h2>OPTIONS</h2>
<p> All these options obviously only make sense if enforced by the server side. They have been implemented to resemble the <code><a href="/docs/linux/man/1-git-daemon/">git-daemon</a></code>(1) options as closely as possible. </p>
<p> &#8211;base-path &lt;path&gt;</p>
<dl>
<dt>
<dd> Prepend <i>path</i> to requested CVSROOT</dl>
<p> &#8211;strict-paths</p>
<dl>
<dt>
<dd> Don&#8217;t allow recursing into subdirectories</dl>
<p> &#8211;export-all</p>
<dl>
<dt>
<dd> Don&#8217;t check for gitcvs.enabled in config. You also have to specify a list of allowed directories (see below) if you want to use this option.</dl>
<p> -V, &#8211;version</p>
<dl>
<dt>
<dd> Print version information and exit</dl>
<p> -h, -H, &#8211;help</p>
<dl>
<dt>
<dd> Print usage information and exit</dl>
<p> &lt;directory&gt;</p>
<dl>
<dt>
<dd> You can specify a list of allowed directories. If no directories are given, all are allowed. This is an additional restriction, gitcvs access still needs to be enabled by the gitcvs.enabled config option unless <i>&#8211;export-all</i> was given, too.</dl>
<h2>DESCRIPTION</h2>
<p> This application is a CVS emulation layer for Git. </p>
<p> It is highly functional. However, not all methods are implemented, and for those methods that are implemented, not all switches are implemented. </p>
<p> Testing has been done using both the CLI CVS client, and the Eclipse CVS plugin. Most functionality works fine with both of these clients.</p>
<h2>LIMITATIONS</h2>
<p> CVS clients cannot tag, branch or perform Git merges. </p>
<p> <i>git-cvsserver</i> maps Git branches to CVS modules. This is very different from what most CVS users would expect since in CVS modules usually represent one or more directories.</p>
<h2>INSTALLATION</h2>
<dl>
<dt>
<dd> 1. If you are going to offer CVS access via pserver, add a line in /etc/inetd.conf like </p>
<dl>
<dt>
<dd>
<pre>
   cvspserver stream tcp nowait nobody git-cvsserver pserver
</pre>
</dl>
<p> Note: Some inetd servers let you specify the name of the executable independently of the value of argv[0] (i.e. the name the program assumes it was executed with). In this case the correct line in /etc/inetd.conf looks like </p>
<dl>
<dt>
<dd>
<pre>
   cvspserver stream tcp nowait nobody /usr/bin/git-cvsserver git-cvsserver pserver
</pre>
</dl>
<p> Only anonymous access is provided by pserve by default. To commit you will have to create pserver accounts, simply add a gitcvs.authdb setting in the config file of the repositories you want the cvsserver to allow writes to, for example: </p>
<dl>
<dt>
<dd>
<pre>
   [gitcvs]
        authdb = /etc/cvsserver/passwd
</pre>
</dl>
<p> The format of these files is username followed by the crypted password, for example: </p>
<dl>
<dt>
<dd>
<pre>
   myuser:$1Oyx5r9mdGZ2
   myuser:$1$BA)@$vbnMJMDym7tA32AamXrm./
</pre>
</dl>
<p> You can use the <i>htpasswd</i> facility that comes with Apache to make these files, but Apache&#8217;s MD5 crypt method differs from the one used by most C library&#8217;s crypt() function, so don&#8217;t use the -m option. </p>
<p> Alternatively you can produce the password with perl&#8217;s crypt() operator: </p>
<dl>
<dt>
<dd>
<pre>
   perl -e 'my ($user, $pass) = @ARGV; printf &quot;%s:%s
&quot;, $user, crypt($user, $pass)' $USER password
</pre>
</dl>
<p> Then provide your password via the pserver method, for example: </p>
<dl>
<dt>
<dd>
<pre>
   cvs -d:pserver:someuser:somepassword &lt;at&gt; server/path/repo.git co &lt;HEAD_name&gt;
</pre>
</dl>
<p> No special setup is needed for SSH access, other than having Git tools in the PATH. If you have clients that do not accept the CVS_SERVER environment variable, you can rename <i>git-cvsserver</i> to cvs. </p>
<p> Note: Newer CVS versions (&gt;= 1.12.11) also support specifying CVS_SERVER directly in CVSROOT like </p>
<dl>
<dt>
<dd>
<pre>
cvs -d &quot;:ext;CVS_SERVER=git cvsserver:user [at] server/path/repo.git&quot; co &lt;HEAD_name&gt;
</pre>
</dl>
<p> This has the advantage that it will be saved in your <i>CVS/Root</i> files and you don&#8217;t need to worry about always setting the correct environment variable. SSH users restricted to <i>git-shell</i> don&#8217;t need to override the default with CVS_SERVER (and shouldn&#8217;t) as <i>git-shell</i> understands cvs to mean <i>git-cvsserver</i> and pretends that the other end runs the real <i>cvs</i> better.</dl>
<dl>
<dt>
<dd> 2. For each repo that you want accessible from CVS you need to edit config in the repo and add the following section. </p>
<dl>
<dt>
<dd>
<pre>
   [gitcvs]
        enabled=1
        # optional for debugging
        logfile=/path/to/logfile
</pre>
</dl>
<p> Note: you need to ensure each user that is going to invoke <i>git-cvsserver</i> has write access to the log file and to the database (see Database Backend. If you want to offer write access over SSH, the users of course also need write access to the Git repository itself. </p>
<p> You also need to ensure that each repository is &quot;bare&quot; (without a Git index file) for cvs commit to work. See <code><a href="/docs/linux/man/7-gitcvs-migration/">gitcvs-migration</a></code>(7). </p>
<p> All configuration variables can also be overridden for a specific method of access. Valid method names are &quot;ext&quot; (for SSH access) and &quot;pserver&quot;. The following example configuration would disable pserver access while still allowing access over SSH. </p>
<dl>
<dt>
<dd>
<pre><code>
[gitcvs] enabled = 0
    [gitcvs "ext"] enabled = 1
</code></pre>
</dl>
</dl>
<dl>
<dt>
<dd> 3. If you didn&#8217;t specify the CVSROOT/CVS_SERVER directly in the checkout command, automatically saving it in your <i>CVS/Root</i> files, then you need to set them explicitly in your environment. CVSROOT should be set as per normal, but the directory should point at the appropriate Git repo. As above, for SSH clients <i>not</i> restricted to <i>git-shell</i>, CVS_SERVER should be set to <i>git-cvsserver</i>. </p>
<dl>
<dt>
<dd>
<pre>
     export CVSROOT=:ext:user [at] server:/var/git/project.git
     export CVS_SERVER=&quot;git cvsserver&quot;
</pre>
</dl>
</dl>
<dl>
<dt>
<dd> 4. For SSH clients that will make commits, make sure their server-side .ssh/environment files (or .bashrc, etc., according to their specific shell) export appropriate values for GIT_AUTHOR_NAME, GIT_AUTHOR_EMAIL, GIT_COMMITTER_NAME, and GIT_COMMITTER_EMAIL. For SSH clients whose login shell is bash, .bashrc may be a reasonable alternative.</dl>
<dl>
<dt>
<dd> 5. Clients should now be able to check out the project. Use the CVS <i>module</i> name to indicate what Git <i>head</i> you want to check out. This also sets the name of your newly checked-out directory, unless you tell it otherwise with -d &lt;dir_name&gt;. For example, this checks out <i>master</i> branch to the project-master directory: </p>
<dl>
<dt>
<dd>
<pre>
     cvs co -d project-master master
</pre>
</dl>
</dl>
<h2>DATABASE BACKEND</h2>
<p> <i>git-cvsserver</i> uses one database per Git head (i.e. CVS module) to store information about the repository to maintain consistent CVS revision numbers. The database needs to be updated (i.e. written to) after every commit. </p>
<p> If the commit is done directly by using git (as opposed to using <i>git-cvsserver</i>) the update will need to happen on the next repository access by <i>git-cvsserver</i>, independent of access method and requested operation. </p>
<p> That means that even if you offer only read access (e.g. by using the pserver method), <i>git-cvsserver</i> should have write access to the database to work reliably (otherwise you need to make sure that the database is up-to-date any time <i>git-cvsserver</i> is executed). </p>
<p> By default it uses SQLite databases in the Git directory, named gitcvs.&lt;module_name&gt;.sqlite. Note that the SQLite backend creates temporary files in the same directory as the database file on write so it might not be enough to grant the users using <i>git-cvsserver</i> write access to the database file without granting them write access to the directory, too. </p>
<p> The database can not be reliably regenerated in a consistent form after the branch it is tracking has changed. Example: For merged branches, <i>git-cvsserver</i> only tracks one branch of development, and after a <i>git merge</i> an incrementally updated database may track a different branch than a database regenerated from scratch, causing inconsistent CVS revision numbers. git-cvsserver has no way of knowing which branch it would have picked if it had been run incrementally pre-merge. So if you have to fully or partially (from old backup) regenerate the database, you should be suspicious of pre-existing CVS sandboxes. </p>
<p> You can configure the database backend with the following configuration variables:</p>
<h3>Configuring database backend</h3>
<p> <i>git-cvsserver</i> uses the Perl DBI module. Please also read its documentation if changing these variables, especially about DBI-&gt;connect(). </p>
<p> gitcvs.dbname</p>
<dl>
<dt>
<dd> Database name. The exact meaning depends on the selected database driver, for SQLite this is a filename. Supports variable substitution (see below). May not contain semicolons (;). Default: <i>%Ggitcvs.%m.sqlite</i></dl>
<p> gitcvs.dbdriver</p>
<dl>
<dt>
<dd> Used DBI driver. You can specify any available driver for this here, but it might not work. cvsserver is tested with <i>DBD::SQLite</i>, reported to work with <i>DBD::Pg</i>, and reported <code>not</code> to work with <i>DBD::mysql</i>. Please regard this as an experimental feature. May not contain colons (:). Default: <i>SQLite</i></dl>
<p> gitcvs.dbuser</p>
<dl>
<dt>
<dd> Database user. Only useful if setting dbdriver, since SQLite has no concept of database users. Supports variable substitution (see below).</dl>
<p> gitcvs.dbpass</p>
<dl>
<dt>
<dd> Database password. Only useful if setting dbdriver, since SQLite has no concept of database passwords.</dl>
<p> gitcvs.dbTableNamePrefix</p>
<dl>
<dt>
<dd> Database table name prefix. Supports variable substitution (see below). Any non-alphabetic characters will be replaced with underscores.</dl>
<p> All variables can also be set per access method, see above. </p>
<p> <font SIZE="+1"> <code>Variable substitution</code></p>
<dl>
<dt>
<dd>
<p> In dbdriver and dbuser you can use the following variables: </p>
<p> %G</p>
<dl>
<dt>
<dd> Git directory name</dl>
<p> %g</p>
<dl>
<dt>
<dd> Git directory name, where all characters except for alpha-numeric ones, ., and &#8211; are replaced with _ (this should make it easier to use the directory name in a filename if wanted)</dl>
<p> %m</p>
<dl>
<dt>
<dd> CVS module/Git head name</dl>
<p> %a</p>
<dl>
<dt>
<dd> access method (one of &quot;ext&quot; or &quot;pserver&quot;)</dl>
<p> %u</p>
<dl>
<dt>
<dd> Name of the user running <i>git-cvsserver</i>. If no name can be determined, the numeric uid is used.</dl>
</dl>
<p> </font></p>
<h2>ENVIRONMENT</h2>
<p> These variables obviate the need for command-line options in some circumstances, allowing easier restricted usage through git-shell. </p>
<p> GIT_CVSSERVER_BASE_PATH takes the place of the argument to &#8211;base-path. </p>
<p> GIT_CVSSERVER_ROOT specifies a single-directory whitelist. The repository must still be configured to allow access through git-cvsserver, as described above. </p>
<p> When these environment variables are set, the corresponding command-line arguments may not be used.</p>
<h2>ECLIPSE CVS CLIENT NOTES</h2>
<p> To get a checkout with the Eclipse CVS client: </p>
<dl>
<dt>
<dd> 1. Select &quot;Create a new project &rarr; From CVS checkout&quot;</dl>
<dl>
<dt>
<dd> 2. Create a new location. See the notes below for details on how to choose the right protocol.</dl>
<dl>
<dt>
<dd> 3. Browse the <i>modules</i> available. It will give you a list of the heads in the repository. You will not be able to browse the tree from there. Only the heads.</dl>
<dl>
<dt>
<dd> 4. Pick <i>HEAD</i> when it asks what branch/tag to check out. Untick the &quot;launch commit wizard&quot; to avoid committing the .project file.</dl>
<p> Protocol notes: If you are using anonymous access via pserver, just select that. Those using SSH access should choose the <i>ext</i> protocol, and configure <i>ext</i> access on the Preferences&rarr;Team&rarr;CVS&rarr;ExtConnection pane. Set CVS_SERVER to &quot;git cvsserver&quot;. Note that password support is not good when using <i>ext</i>, you will definitely want to have SSH keys setup. </p>
<p> Alternatively, you can just use the non-standard extssh protocol that Eclipse offer. In that case CVS_SERVER is ignored, and you will have to replace the cvs utility on the server with <i>git-cvsserver</i> or manipulate your .bashrc so that calling <i>cvs</i> effectively calls <i>git-cvsserver</i>.</p>
<h2>CLIENTS KNOWN TO WORK</h2>
<dl>
<dt>
<dd> &bull; CVS 1.12.9 on Debian</dl>
<dl>
<dt>
<dd> &bull; CVS 1.11.17 on MacOSX (from Fink package)</dl>
<dl>
<dt>
<dd> &bull; Eclipse 3.0, 3.1.2 on MacOSX (see Eclipse CVS Client Notes)</dl>
<dl>
<dt>
<dd> &bull; TortoiseCVS</dl>
<h2>OPERATIONS SUPPORTED</h2>
<p> All the operations required for normal use are supported, including checkout, diff, status, update, log, add, remove, commit. </p>
<p> Most CVS command arguments that read CVS tags or revision numbers (typically -r) work, and also support any git refspec (tag, branch, commit ID, etc). However, CVS revision numbers for non-default branches are not well emulated, and cvs log does not show tags or branches at all. (Non-main-branch CVS revision numbers superficially resemble CVS revision numbers, but they actually encode a git commit ID directly, rather than represent the number of revisions since the branch point.) </p>
<p> Note that there are two ways to checkout a particular branch. As described elsewhere on this page, the &quot;module&quot; parameter of cvs checkout is interpreted as a branch name, and it becomes the main branch. It remains the main branch for a given sandbox even if you temporarily make another branch sticky with cvs update -r. Alternatively, the -r argument can indicate some other branch to actually checkout, even though the module is still the &quot;main&quot; branch. Tradeoffs (as currently implemented): Each new &quot;module&quot; creates a new database on disk with a history for the given module, and after the database is created, operations against that main branch are fast. Or alternatively, -r doesn&#8217;t take any extra disk space, but may be significantly slower for many operations, like cvs update. </p>
<p> If you want to refer to a git refspec that has characters that are not allowed by CVS, you have two options. First, it may just work to supply the git refspec directly to the appropriate CVS -r argument; some CVS clients don&#8217;t seem to do much sanity checking of the argument. Second, if that fails, you can use a special character escape mechanism that only uses characters that are valid in CVS tags. A sequence of 4 or 5 characters of the form (underscore (&quot;_&quot;), dash (&quot;-&quot;), one or two characters, and dash (&quot;-&quot;)) can encode various characters based on the one or two letters: &quot;s&quot; for slash (&quot;/&quot;), &quot;p&quot; for period (&quot;.&quot;), &quot;u&quot; for underscore (&quot;_&quot;), or two hexadecimal digits for any byte value at all (typically an ASCII number, or perhaps a part of a UTF-8 encoded character). </p>
<p> Legacy monitoring operations are not supported (edit, watch and related). Exports and tagging (tags and branches) are not supported at this stage.</p>
<h3>CRLF Line Ending Conversions</h3>
<p> By default the server leaves the <i>-k</i> mode blank for all files, which causes the CVS client to treat them as a text files, subject to end-of-line conversion on some platforms. </p>
<p> You can make the server use the end-of-line conversion attributes to set the <i>-k</i> modes for files by setting the gitcvs.usecrlfattr config variable. See <code><a href="/docs/linux/man/5-gitattributes/">gitattributes</a></code>(5) for more information about end-of-line conversion. </p>
<p> Alternatively, if gitcvs.usecrlfattr config is not enabled or the attributes do not allow automatic detection for a filename, then the server uses the gitcvs.allbinary config for the default setting. If gitcvs.allbinary is set, then file not otherwise specified will default to <i>-kb</i> mode. Otherwise the <i>-k</i> mode is left blank. But if gitcvs.allbinary is set to &quot;guess&quot;, then the correct <i>-k</i> mode will be guessed based on the contents of the file. </p>
<p> For best consistency with <i>cvs</i>, it is probably best to override the defaults by setting gitcvs.usecrlfattr to true, and gitcvs.allbinary to &quot;guess&quot;.</p>
<h2>DEPENDENCIES</h2>
<p> <i>git-cvsserver</i> depends on DBD::SQLite.</p>
<h2>GIT</h2>
<p> Part of the <code><a href="/docs/linux/man/1-git/">git</a></code>(1) suite </p>
<h2>Index</h2>
