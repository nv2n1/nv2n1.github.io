---
title: "alternatives(8)"
name: "alternatives"
section: "8"
letter: "a"
url: "/docs/linux/man/8-alternatives/"
description: "alternatives – maintain symbolic links determining default commands"
---

<p>alternatives &#8211; maintain symbolic links determining default commands</p>
<h2>Synopsis</h2>
<p><code>alternatives</code> [<i>options</i>] <code>&#8211;install</code> <i>link name path priority</i> [<code>&#8211;slave</code> <i>link name</i> <i>path</i>]&#8230; [<code>&#8211;initscript</code> <i>service</i>] [<code>&#8211;family</code> <i>name</i>] </p>
<p> <code>alternatives</code> [<i>options</i>] <code>&#8211;remove</code> <i>name path</i> </p>
<p> <code>alternatives</code> [<i>options</i>] <code>&#8211;set</code> <i>name path</i> </p>
<p> <code>alternatives</code> [<i>options</i>] <code>&#8211;auto</code> <i>name</i> </p>
<p> <code>alternatives</code> [<i>options</i>] <code>&#8211;display</code> <i>name</i> </p>
<p> <code>alternatives</code> [<i>options</i>] <code>&#8211;config</code> <i>name</i> </p>
<p> <code>alternatives</code> [<i>options</i>] <code>&#8211;list</code> <i>name</i></p>
<h2>Description</h2>
<p><code>alternatives</code> creates, removes, maintains and displays information about the symbolic links comprising the alternatives system. The alternatives system is a reimplementation of the Debian alternatives system. It was rewritten primarily to remove the dependence on perl; it is intended to be a drop in replacement for Debian&#8217;s <code>update-dependencies</code> script. This man page is a slightly modified version of the man page from the Debian project. </p>
<p> It is possible for several programs fulfilling the same or similar functions to be installed on a single system at the same time. For example, many systems have several text editors installed at once. This gives choice to the users of a system, allowing each to use a different editor, if desired, but makes it difficult for a program to make a good choice of editor to invoke if the user has not specified a particular preference. </p>
<p> The alternatives system aims to solve this problem. A generic name in the filesystem is shared by all files providing interchangeable functionality. The alternatives system and the system administrator together determine which actual file is referenced by this generic name. For example, if the text editors <code><a href="/docs/linux/man/1-ed/">ed</a></code>(1) and <code><a href="/docs/linux/man/1-nvi/">nvi</a></code>(1) are both installed on the system, the alternatives system will cause the generic name <i>/usr/bin/editor</i> to refer to <i>/usr/bin/nvi</i> by default. The system administrator can override this and cause it to refer to <i>/usr/bin/ed</i> instead, and the alternatives system will not alter this setting until explicitly requested to do so. </p>
<p> The generic name is not a direct symbolic link to the selected alternative. Instead, it is a symbolic link to a name in the <i>alternatives</i> <i>directory</i>, which in turn is a symbolic link to the actual file referenced. This is done so that the system administrator&#8217;s changes can be confined within the <i>/etc</i> directory: the FHS (q.v.) gives reasons why this is a Good Thing. </p>
<p> When each package providing a file with a particular functionality is installed, changed or removed, <code>alternatives</code> is called to update information about that file in the alternatives system. <code>alternatives</code> is usually called from the <code>%post</code> or <code>%pre</code> scripts in RPM packages. </p>
<p> It is often useful for a number of alternatives to be synchronised, so that they are changed as a group; for example, when several versions of the <code><a href="/docs/linux/man/1-vi/">vi</a></code>(1) editor are installed, the man page referenced by <i>/usr/share/man/man1/vi.1</i> should correspond to the executable referenced by <i>/usr/bin/vi</i>. <code>alternatives</code> handles this by means of <i>master</i> and <i>slave</i> links; when the master is changed, any associated slaves are changed too. A master link and its associated slaves make up a <i>link</i> <i>group</i>. </p>
<p> Each link group is, at any given time, in one of two modes: automatic or manual. When a group is in automatic mode, the alternatives system will automatically decide, as packages are installed and removed, whether and how to update the links. In manual mode, the alternatives system will not change the links; it will leave all the decisions to the system administrator. </p>
<p> Link groups are in automatic mode when they are first introduced to the system. If the system administrator makes changes to the system&#8217;s automatic settings, this will be noticed the next time <code>alternatives</code> is run on the changed link&#8217;s group, and the group will automatically be switched to manual mode. </p>
<p> Each alternative has a <i>priority</i> associated with it. When a link group is in automatic mode, the alternatives pointed to by members of the group will be those which have the highest priority. </p>
<p> When using the <i>&#8211;config</i> option, <code>alternatives</code> will list all of the choices for the link group of which given <i>name</i> is the master link. You will then be prompted for which of the choices to use for the link group. Once you make a change, the link group will no longer be in <i>auto</i> mode. You will need to use the <i>&#8211;auto</i> option in order to return to the automatic state.</p>
<h2>Terminology</h2>
<p>Since the activities of <code>alternatives</code> are quite involved, some specific terms will help to explain its operation.</p>
<dl>
<dt>generic name</p>
<dd>A name, like <i>/usr/bin/editor</i>, which refers, via the alternatives system, to one of a number of files of similar function.</p>
<dt>symlink</p>
<dd>Without any further qualification, this means a symbolic link in the alternatives directory: one which the system administrator is expected to adjust.</p>
<dt>alternative</p>
<dd>The name of a specific file in the filesystem, which may be made accessible via a generic name using the alternatives system.</p>
<dt>alternatives directory</p>
<dd>A directory, by default <i>/etc/alternatives</i>, containing the symlinks.</p>
<dt>administrative directory</p>
<dd>A directory, by default <i>/var/lib/alternatives</i>, containing <code>alternatives</code>&#8216; state information.</p>
<dt>link group</p>
<dd>A set of related symlinks, intended to be updated as a group.</p>
<dt>master link</p>
<dd>The link in a link group which determines how the other links in the group are configured.</p>
<dt>slave link</p>
<dd>A link in a link group which is controlled by the setting of the master link.</p>
<dt>automatic mode</p>
<dd>When a link group is in automatic mode, the alternatives system ensures that the links in the group point to the highest priority alternatives appropriate for the group.</p>
<dt>manual mode</p>
<dd>When a link group is in manual mode, the alternatives system will not make any changes to the system administrator&#8217;s settings.</dl>
<h2>Options</h2>
<p>Exactly one action must be specified if <code>alternatives</code> is to perform any meaningful task. Any number of the common options may be specified together with any action.</p>
<h3>Common Options</h3>
<dl>
<dt><code>&#8211;verbose</code></p>
<dd>Generate more comments about what <code>alternatives</code> is doing.</p>
<dt><code>&#8211;quiet</code></p>
<dd>Don&#8217;t generate any comments unless errors occur. This option is not yet implemented.</p>
<dt><code>&#8211;test</code></p>
<dd>Don&#8217;t actually do anything, just say what would be done. This option is not yet implemented.</p>
<dt><code>&#8211;help</code></p>
<dd>Give some usage information (and say which version of <code>alternatives</code> this is).</p>
<dt><code>&#8211;version</code></p>
<dd>Tell which version of <code>alternatives</code> this is (and give some usage information).</p>
<dt><code>&#8211;altdir</code> <i>directory</i></p>
<dd>Specifies the alternatives directory, when this is to be different from the default.</p>
<dt><code>&#8211;admindir</code> <i>directory</i></p>
<dd>Specifies the administrative directory, when this is to be different from the default.</dl>
<h3>Actions</h3>
<dl>
<dt><code>&#8211;install</code> <i>link name path priority</i> [<code>&#8211;slave</code> <i>slink sname spath</i>] [<code>&#8211;initscript</code> <i>service</i>]&#8230;</p>
<dd>Add a group of alternatives to the system. <i>name</i> is the generic name for the master link, <i>link</i> is the name of its symlink, <i>path</i> is the alternative being introduced for the master link, and <i>priority</i> is the priority of the alternatives group. Higher priorities take precendence if no alternative is manually selected. <i>sname</i>, <i>slink</i> and <i>spath</i> are the generic name, symlink name and alternative for a slave link, and <i>service</i> is the name of any associated initscript for the alternative. <code>NOTE:</code> <code>&#8211;initscript and &#8211;family</code> are a Red Hat Linux specific options. Zero or more <code>&#8211;slave</code> options, each followed by three arguments, may be specified.</p>
<dd>If the master symlink specified exists already in the alternatives system&#8217;s records, the information supplied will be added as a new set of alternatives for the group. Otherwise, a new group, set to automatic mode, will be added with this information. If the group is in automatic mode, and the newly added alternatives&#8217; priority is higher than any other installed alternatives for this group, the symlinks will be updated to point to the newly added alternatives. </p>
<p> If <code>&#8211;initscript</code> is used, the alternatives system will manage the initscript associated with the alternative via <code>chkconfig,</code> registering and unregistering the init script depending on which alternative is active. </p>
<p> <code>NOTE:</code> <code>&#8211;initscript</code> is a Red Hat Linux specific option. </p>
<p> <code>&#8211;family</code> can be used to group similar alternatives. If the group is in manual mode and the alternative currently used is removed, alternatives will try to change links to different one with same family and highest priority. </p>
<p> <code>NOTE:</code> <code>&#8211;family</code> is a Red Hat Linux specific option.</p>
<dt><code>&#8211;remove</code> <i>name path</i></p>
<dd>Remove an alternative and all of its associated slave links. <i>name</i> is a name in the alternatives directory, and <i>path</i> is an absolute filename to which <i>name</i> could be linked. If <i>name</i> is indeed linked to <i>path</i>, <i>name</i> will be updated to point to another appropriate alternative, or removed if there is no such alternative left. Associated slave links will be updated or removed, correspondingly. If the link is not currently pointing to <i>path</i>, no links are changed; only the information about the alternative is removed.</p>
<dt><code>&#8211;set</code> <i>name path</i></p>
<dd>The symbolic link and slaves for link group <i>name</i> set to those configured for <i>path</i>, and the link group is set to manual mode. This option is not in the original Debian implementation.</p>
<dt><code>&#8211;config</code> <i>name</i></p>
<dd>Present the user with a configuration menu for choosing the master link and slaves for link group <i>name</i>. Once chosen, the link group is set to manual mode.</p>
<dt><code>&#8211;auto</code> <i>name</i></p>
<dd>Switch the master symlink <i>name</i> to automatic mode. In the process, this symlink and its slaves are updated to point to the highest priority installed alternatives.</p>
<dt><code>&#8211;display</code> <i>name</i></p>
<dd>Display information about the link group of which <i>name</i> is the master link. Information displayed includes the group&#8217;s mode (auto or manual), which alternative the symlink currently points to, what other alternatives are available (and their corresponding slave alternatives), and the highest priority alternative currently installed.</p>
<dt><code>&#8211;list </code></p>
<dd>Display information about all link groups.</dl>
<h2>Files</h2>
<dl>
<dt><i>/etc/alternatives/</i></p>
<dd>The default alternatives directory. Can be overridden by the <code>&#8211;altdir</code> option.</p>
<dt><i>/var/lib/alternatives/</i></p>
<dd>The default administration directory. Can be overridden by the <code>&#8211;admindir</code> option.</dl>
<h2>Exit Status</h2>
<dl>
<dt>0</p>
<dd>The requested action was successfully performed.</p>
<dt>2</p>
<dd>Problems were encountered whilst parsing the command line or performing the action.</dl>
<h2>Diagnostics</h2>
<p><code>alternatives</code> chatters incessantly about its activities on its standard output channel. If problems occur, <code>alternatives</code> outputs error messages on its standard error channel and returns an exit status of 2. These diagnostics should be self-explanatory; if you do not find them so, please report this as a bug.</p>
<h2>Bugs</h2>
<p>If you find a bug, please report it using the Red Hat bug tracking system at <code><a rel="nofollow" href="http://bugzilla.redhat.com">http://bugzilla.redhat.com</a></code>. </p>
<p> If you find any discrepancy between the operation of <code>alternatives</code> and this manual page, it is a bug, either in the implementation or the documentation; please report it. Any significant differences between this implementation and Debian&#8217;s is also a bug and should be reported, unless otherwise noted in this man page.</p>
<h2>Author</h2>
<p>alternatives is copyright 2002 Red Hat, Inc.. It is free software; see the GNU General Public Licence version 2 or later for copying conditions. There is NO warranty. </p>
<p> This manual page is copyright 1997/98 Charles Briscoe-Smith and 2002 Red Hat, Inc. This is free documentation; see the GNU General Public Licence version 2 or later for copying conditions. There is NO WARRANTY.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-ln/">ln</a></code>(1), FHS, the Filesystem Hierarchy Standard. alternatives.c chkconfig.c COPYING leveldb.c leveldb.h Makefile ntsysv.c ook </p>
