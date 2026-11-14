---
title: "update-alternatives(1)"
name: "update-alternatives"
section: "1"
letter: "u"
url: "/docs/linux/man/1-update-alternatives/"
description: "update-alternatives – maintain symbolic links determining default commands"
---

<h2 class="name">NAME</h2>
<p> update-alternatives &#8211; maintain symbolic links determining default commands </p>
<h2>SYNOPSIS</h2>
<p> <code>update-alternatives</code> [<i>option</i>&#8230;] <i>command</i></p>
<h2>DESCRIPTION</h2>
<p> <code>update-alternatives</code> creates, removes, maintains and displays information about the symbolic links comprising the Debian alternatives system. </p>
<p> It is possible for several programs fulfilling the same or similar functions to be installed on a single system at the same time. For example, many systems have several text editors installed at once. This gives choice to the users of a system, allowing each to use a different editor, if desired, but makes it difficult for a program to make a good choice for an editor to invoke if the user has not specified a particular preference. </p>
<p> Debian&#8217;s alternatives system aims to solve this problem. A generic name in the filesystem is shared by all files providing interchangeable functionality. The alternatives system and the system administrator together determine which actual file is referenced by this generic name. For example, if the text editors <code><a href="/docs/linux/man/1-ed/">ed</a></code>(1) and <code><a href="/docs/linux/man/1-nvi/">nvi</a></code>(1) are both installed on the system, the alternatives system will cause the generic name <i>/usr/bin/editor</i> to refer to <i>/usr/bin/nvi</i> by default. The system administrator can override this and cause it to refer to <i>/usr/bin/ed</i> instead, and the alternatives system will not alter this setting until explicitly requested to do so. </p>
<p> The generic name is not a direct symbolic link to the selected alternative. Instead, it is a symbolic link to a name in the <i>alternatives</i> <i>directory</i>, which in turn is a symbolic link to the actual file referenced. This is done so that the system administrator&#8217;s changes can be confined within the <i>/etc</i> directory: the <font SIZE="-1">FHS</font> (q.v.) gives reasons why this is a Good Thing. </p>
<p> When each package providing a file with a particular functionality is installed, changed or removed, <code>update-alternatives</code> is called to update information about that file in the alternatives system. <code>update-alternatives</code> is usually called from the following Debian package maintainer scripts, <code>postinst</code> (configure) to install the alternative and from <code>prerm</code> and <code>postrm</code> (remove) to remove the alternative. <code>Note:</code> in most (if not all) cases no other maintainer script actions should call <code>update-alternatives</code>, in particular neither of <code>upgrade</code> nor <code>disappear</code>, as any other such action can lose the manual state of an alternative, or make the alternative temporarily flip-flop, or completely switch when several of them have the same priority. </p>
<p> It is often useful for a number of alternatives to be synchronized, so that they are changed as a group; for example, when several versions of the <code><a href="/docs/linux/man/1-vi/">vi</a></code>(1) editor are installed, the man page referenced by <i>/usr/share/man/man1/vi.1</i> should correspond to the executable referenced by <i>/usr/bin/vi</i>. <code>update-alternatives</code> handles this by means of <i>master</i> and <i>slave</i> links; when the master is changed, any associated slaves are changed too. A master link and its associated slaves make up a <i>link</i> <i>group</i>. </p>
<p> Each link group is, at any given time, in one of two modes: automatic or manual. When a group is in automatic mode, the alternatives system will automatically decide, as packages are installed and removed, whether and how to update the links. In manual mode, the alternatives system will retain the choice of the administrator and avoid changing the links (except when something is broken). </p>
<p> Link groups are in automatic mode when they are first introduced to the system. If the system administrator makes changes to the system&#8217;s automatic settings, this will be noticed the next time <code>update-alternatives</code> is run on the changed link&#8217;s group, and the group will automatically be switched to manual mode. </p>
<p> Each alternative has a <i>priority</i> associated with it. When a link group is in automatic mode, the alternatives pointed to by members of the group will be those which have the highest priority. </p>
<p> When using the <code>&#8211;config</code> option, <code>update-alternatives</code> will list all of the choices for the link group of which given <i>name</i> is the master alternative name. The current choice is marked with a &#8216;*&#8217;. You will then be prompted for your choice regarding this link group. Depending on the choice made, the link group might no longer be in <i>auto</i> mode. You will need to use the <code>&#8211;auto</code> option in order to return to the automatic mode (or you can rerun <code>&#8211;config</code> and select the entry marked as automatic). </p>
<p> If you want to configure non-interactively you can use the <code>&#8211;set</code> option instead (see below). </p>
<p> Different packages providing the same file need to do so <code>cooperatively</code>. In other words, the usage of <code>update-alternatives</code> is <code>mandatory</code> for all involved packages in such case. It is not possible to override some file in a package that does not employ the <code>update-alternatives</code> mechanism.</p>
<h2>TERMINOLOGY</h2>
<p> Since the activities of <code>update-alternatives</code> are quite involved, some specific terms will help to explain its operation.</p>
<dl>
<dt>generic name (or alternative link)</p>
<dd> A name, like <i>/usr/bin/editor</i>, which refers, via the alternatives system, to one of a number of files of similar function.</p>
<dt>alternative name</p>
<dd> The name of a symbolic link in the alternatives directory.</p>
<dt>alternative (or alternative path)</p>
<dd> The name of a specific file in the filesystem, which may be made accessible via a generic name using the alternatives system.</p>
<dt>alternatives directory</p>
<dd> A directory, by default <i>/etc/alternatives</i>, containing the symlinks.</p>
<dt>administrative directory</p>
<dd> A directory, by default <i>/var/lib/dpkg/alternatives</i>, containing <code>update-alternatives</code>&#8216; state information.</p>
<dt>link group</p>
<dd> A set of related symlinks, intended to be updated as a group.</p>
<dt>master link</p>
<dd> The alternative link in a link group which determines how the other links in the group are configured.</p>
<dt>slave link</p>
<dd> An alternative link in a link group which is controlled by the setting of the master link.</p>
<dt>automatic mode</p>
<dd> When a link group is in automatic mode, the alternatives system ensures that the links in the group point to the highest priority alternative appropriate for the group.</p>
<dt>manual mode</p>
<dd> When a link group is in manual mode, the alternatives system will not make any changes to the system administrator&#8217;s settings.</dl>
<h2>COMMANDS</h2>
<dl>
<dt><code>&#8211;install</code> <i>link name path priority</i> [<code>&#8211;slave</code> <i>link name path</i>]&#8230;</p>
<dd> Add a group of alternatives to the system. <i>link</i> is the generic name for the master link, <i>name</i> is the name of its symlink in the alternatives directory, and <i>path</i> is the alternative being introduced for the master link. The arguments after <code>&#8211;slave</code> are the generic name, symlink name in the alternatives directory and the alternative path for a slave link. Zero or more <code>&#8211;slave</code> options, each followed by three arguments, may be specified. Note that the master alternative must exist or the call will fail. However if a slave alternative doesn&#8217;t exist, the corresponding slave alternative link will simply not be installed (a warning will still be displayed). If some real file is installed where an alternative link has to be installed, it is kept unless <code>&#8211;force</code> is used. </p>
<p> If the alternative name specified exists already in the alternatives system&#8217;s records, the information supplied will be added as a new set of alternatives for the group. Otherwise, a new group, set to automatic mode, will be added with this information. If the group is in automatic mode, and the newly added alternatives&#8217; priority is higher than any other installed alternatives for this group, the symlinks will be updated to point to the newly added alternatives.</p>
<dt><code>&#8211;set</code> <i>name path</i></p>
<dd> Set the program <i>path</i> as alternative for <i>name</i>. This is equivalent to <code>&#8211;config</code> but is non-interactive and thus scriptable.</p>
<dt><code>&#8211;remove</code> <i>name path</i></p>
<dd> Remove an alternative and all of its associated slave links. <i>name</i> is a name in the alternatives directory, and <i>path</i> is an absolute filename to which <i>name</i> could be linked. If <i>name</i> is indeed linked to <i>path</i>, <i>name</i> will be updated to point to another appropriate alternative (and the group is put back in automatic mode), or removed if there is no such alternative left. Associated slave links will be updated or removed, correspondingly. If the link is not currently pointing to <i>path</i>, no links are changed; only the information about the alternative is removed.</p>
<dt><code>&#8211;remove-all</code> <i>name</i></p>
<dd> Remove all alternatives and all of their associated slave links. <i>name</i> is a name in the alternatives directory.</p>
<dt><code>&#8211;all</code></p>
<dd> Call <code>&#8211;config</code> on all alternatives. It can be usefully combined with <code>&#8211;skip-auto</code> to review and configure all alternatives which are not configured in automatic mode. Broken alternatives are also displayed. Thus a simple way to fix all broken alternatives is to call <code>yes &#8221; | update-alternatives &#8211;force &#8211;all</code>.</p>
<dt><code>&#8211;auto</code> <i>name</i></p>
<dd> Switch the link group behind the alternative for <i>name</i> to automatic mode. In the process, the master symlink and its slaves are updated to point to the highest priority installed alternatives.</p>
<dt><code>&#8211;display</code> <i>name</i></p>
<dd> Display information about the link group. Information displayed includes the group&#8217;s mode (auto or manual), the master and slave links, which alternative the master link currently points to, what other alternatives are available (and their corresponding slave alternatives), and the highest priority alternative currently installed.</p>
<dt><code>&#8211;get-selections</code></p>
<dd> List all master alternative names (those controlling a link group) and their status (since version 1.15.0). Each line contains up to 3 fields (separated by one or more spaces). The first field is the alternative name, the second one is the status (either <code>auto</code> or <code>manual</code>), and the last one contains the current choice in the alternative (beware: it&#8217;s a filename and thus might contain spaces).</p>
<dt><code>&#8211;set-selections</code></p>
<dd> Read configuration of alternatives on standard input in the format generated by <code>&#8211;get-selections</code> and reconfigure them accordingly (since version 1.15.0).</p>
<dt><code>&#8211;query</code> <i>name</i></p>
<dd> Display information about the link group like <code>&#8211;display</code> does, but in a machine parseable way (since version 1.15.0, see section <font SIZE="-1"><code>QUERY FORMAT</code></font> below).</p>
<dt><code>&#8211;list</code> <i>name</i></p>
<dd> Display all targets of the link group.</p>
<dt><code>&#8211;config</code> <i>name</i></p>
<dd> Show available alternatives for a link group and allow the user to interactively select which one to use. The link group is updated.</p>
<dt><code>&#8211;help</code></p>
<dd> Show the usage message and exit.</p>
<dt><code>&#8211;version</code></p>
<dd> Show the version and exit.</dl>
<h2>OPTIONS</h2>
<dl>
<dt><code>&#8211;altdir</code> <i>directory</i></p>
<dd> Specifies the alternatives directory, when this is to be different from the default. Defaults to &laquo;<i>/etc/alternatives</i>&raquo;.</p>
<dt><code>&#8211;admindir</code> <i>directory</i></p>
<dd> Specifies the administrative directory, when this is to be different from the default. Defaults to &laquo;<i>/var/lib/dpkg/alternatives</i>&raquo;</p>
<dt><code>&#8211;instdir</code> <i>directory</i></p>
<dd> Specifies the installation directory where alternatives links will be created (since version 1.20.1). Defaults to &laquo;&raquo;.</p>
<dt><code>&#8211;root</code> <i>directory</i></p>
<dd> Specifies the root directory (since version 1.20.1). This also sets the alternatives, installation and administrative directories to match. Defaults to &laquo;&raquo;.</p>
<dt><code>&#8211;log</code> <i>file</i></p>
<dd> Specifies the log file (since version 1.15.0), when this is to be different from the default (/var/log/alternatives.log).</p>
<dt><code>&#8211;force</code></p>
<dd> Allow replacing or dropping any real file that is installed where an alternative link has to be installed or removed.</p>
<dt><code>&#8211;skip-auto</code></p>
<dd> Skip configuration prompt for alternatives which are properly configured in automatic mode. This option is only relevant with <code>&#8211;config</code> or <code>&#8211;all</code>.</p>
<dt><code>&#8211;quiet</code></p>
<dd> Do not generate any comments unless errors occur.</p>
<dt><code>&#8211;verbose</code></p>
<dd> Generate more comments about what is being done.</p>
<dt><code>&#8211;debug</code></p>
<dd> Generate even more comments, helpful for debugging, about what is being done (since version 1.19.3).</dl>
<h2>EXIT STATUS</h2>
<dl>
<dt><code>0</code></p>
<dd> The requested action was successfully performed.</p>
<dt><code>2</code></p>
<dd> Problems were encountered whilst parsing the command line or performing the action.</dl>
<h2>ENVIRONMENT</h2>
<dl>
<dt><font SIZE="-1"><code>DPKG_ADMINDIR</code></font></p>
<dd> If set and the <code>&#8211;admindir</code> option has not been specified, it will be used as the base administrative directory.</dl>
<h2>FILES</h2>
<dl>
<dt><i>/etc/alternatives/</i></p>
<dd> The default alternatives directory. Can be overridden by the <code>&#8211;altdir</code> option.</p>
<dt><i>/var/lib/dpkg/alternatives/</i></p>
<dd> The default administration directory. Can be overridden by the <code>&#8211;admindir</code> option.</dl>
<h2>QUERY FORMAT</h2>
<p> The <code>&#8211;query</code> format is using an RFC822-like flat format. It&#8217;s made of <i>n</i> + 1 blocks where <i>n</i> is the number of alternatives available in the queried link group. The first block contains the following fields:</p>
<dl>
<dt><code>Name:</code> <i>name</i></p>
<dd> The alternative name in the alternative directory.</p>
<dt><code>Link:</code> <i>link</i></p>
<dd> The generic name of the alternative.</p>
<dt><code>Slaves:</code> <i>list-of-slaves</i></p>
<dd> When this field is present, the <code>next</code> lines hold all slave links associated to the master link of the alternative. There is one slave per line. Each line contains one space, the generic name of the slave alternative, another space, and the path to the slave link.</p>
<dt><code>Status:</code> <i>status</i></p>
<dd> The status of the alternative (<code>auto</code> or <code>manual</code>).</p>
<dt><code>Best:</code> <i>best-choice</i></p>
<dd> The path of the best alternative for this link group. Not present if there is no alternatives available.</p>
<dt><code>Value:</code> <i>currently-selected-alternative</i></p>
<dd> The path of the currently selected alternative. It can also take the magic value <code>none</code>. It is used if the link doesn&#8217;t exist.</dl>
<p> The other blocks describe the available alternatives in the queried link group:</p>
<dl>
<dt><code>Alternative:</code> <i>path-of-this-alternative</i></p>
<dd> Path to this block&#8217;s alternative.</p>
<dt><code>Priority:</code> <i>priority-value</i></p>
<dd> Value of the priority of this alternative.</p>
<dt><code>Slaves:</code> <i>list-of-slaves</i></p>
<dd> When this field is present, the <code>next</code> lines hold all slave alternatives associated to the master link of the alternative. There is one slave per line. Each line contains one space, the generic name of the slave alternative, another space, and the path to the slave alternative.</dl>
<h3>Example</h3>
<pre>
 $ update-alternatives --query editor
 Name: editor
 Link: /usr/bin/editor
 Slaves:
  editor.1.gz /usr/share/man/man1/editor.1.gz
  editor.fr.1.gz /usr/share/man/fr/man1/editor.1.gz
  editor.it.1.gz /usr/share/man/it/man1/editor.1.gz
  editor.pl.1.gz /usr/share/man/pl/man1/editor.1.gz
  editor.ru.1.gz /usr/share/man/ru/man1/editor.1.gz
 Status: auto
 Best: /usr/bin/vim.basic
 Value: /usr/bin/vim.basic
 Alternative: /bin/ed
 Priority: -100
 Slaves:
  editor.1.gz /usr/share/man/man1/ed.1.gz
 Alternative: /usr/bin/vim.basic
 Priority: 50
 Slaves:
  editor.1.gz /usr/share/man/man1/vim.1.gz
  editor.fr.1.gz /usr/share/man/fr/man1/vim.1.gz
  editor.it.1.gz /usr/share/man/it/man1/vim.1.gz
  editor.pl.1.gz /usr/share/man/pl/man1/vim.1.gz
  editor.ru.1.gz /usr/share/man/ru/man1/vim.1.gz
</pre>
<h2>DIAGNOSTICS</h2>
<p> With <code>&#8211;verbose</code> <code>update-alternatives</code> chatters incessantly about its activities on its standard output channel. If problems occur, <code>update-alternatives</code> outputs error messages on its standard error channel and returns an exit status of 2. These diagnostics should be self-explanatory; if you do not find them so, please report this as a bug.</p>
<h2>EXAMPLES</h2>
<p> There are several packages which provide a text editor compatible with <code>vi</code>, for example <code>nvi</code> and <code>vim</code>. Which one is used is controlled by the link group <code>vi</code>, which includes links for the program itself and the associated manpage. </p>
<p> To display the available packages which provide <code>vi</code> and the current setting for it, use the <code>&#8211;display</code> action: </p>
<pre>
 update-alternatives --display vi
</pre>
<p> To choose a particular <code>vi</code> implementation, use this command as root and then select a number from the list: </p>
<pre>
 update-alternatives --config vi
</pre>
<p> To go back to having the <code>vi</code> implementation chosen automatically, do this as root: </p>
<pre>
 update-alternatives --auto vi
</pre>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-ln/">ln</a></code>(1), <font SIZE="-1">FHS</font> (the Filesystem Hierarchy Standard). </p>
<h2>Index</h2>
