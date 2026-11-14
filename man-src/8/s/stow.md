---
title: "stow(8)"
name: "stow"
section: "8"
letter: "s"
url: "/docs/linux/man/8-stow/"
description: "stow – software package installation manager"
---

<p>stow &#8211; software package installation manager</p>
<h2>Synopsis</h2>
<p>stow [ options ] package &#8230;</p>
<h2>Description</h2>
<p>This manual page describes <font SIZE="-1">GNU</font> Stow <tt>@VERSION</tt>@, a program for managing the installation of software packages. This is not the definitive documentation for stow; for that, see the info manual. </p>
<p> Stow is a tool for managing the installation of multiple software packages in the same run-time directory tree. One historical difficulty of this task has been the need to administer, upgrade, install, and remove files in independent packages without confusing them with other files sharing the same filesystem space. For instance, it is common to install Perl and Emacs in <i>/usr/local</i>. When one does so, one winds up (as of Perl 4.036 and Emacs 19.22) with the following files in <i>/usr/local/man/man1</i>: <i>a2p.1</i>; <i>ctags.1</i>; <i>emacs.1</i>; <i>etags.1</i>; <i>h2ph.1</i>; <i>perl.1</i>; and <i>s2p.1</i>. Now suppose it&#8217;s time to uninstall Perl. Which man pages get removed? Obviously <i>perl.1</i> is one of them, but it should not be the administrator&#8217;s responsibility to memorize the ownership of individual files by separate packages. </p>
<p> The approach used by Stow is to install each package into its own tree, then use symbolic links to make it appear as though the files are installed in the common tree. Administration can be performed in the package&#8217;s private tree in isolation from clutter from other packages. Stow can then be used to update the symbolic links. The structure of each private tree should reflect the desired structure in the common tree; i.e. (in the typical case) there should be a <i>bin</i> directory containing executables, a <i>man/man1</i> directory containing section 1 man pages, and so on. </p>
<p> Stow was inspired by Carnegie Mellon&#8217;s Depot program, but is substantially simpler and safer. Whereas Depot required database files to keep things in sync, Stow stores no extra state between runs, so there&#8217;s no danger (as there was in Depot) of mangling directories when file hierarchies don&#8217;t match the database. Also unlike Depot, Stow will never delete any files, directories, or links that appear in a Stow directory (e.g., <i>/usr/local/stow/emacs</i>), so it&#8217;s always possible to rebuild the target tree (e.g., <i>/usr/local</i>).</p>
<h2>Terminology</h2>
<p>A &#8220;package&#8221; is a related collection of files and directories that you wish to administer as a unit &#8212; e.g., Perl or Emacs &#8212; and that needs to be installed in a particular directory structure &#8212; e.g., with <i>bin</i>, <i>lib</i>, and <i>man</i> subdirectories. </p>
<p> A &#8220;target directory&#8221; is the root of a tree in which one or more packages wish to <code>appear</code> to be installed. A common, but by no means the only such location is <i>/usr/local</i>. The examples in this manual page will use <i>/usr/local</i> as the target directory. </p>
<p> A &#8220;stow directory&#8221; is the root of a tree containing separate packages in private subtrees. When Stow runs, it uses the current directory as the default stow directory. The examples in this manual page will use <i>/usr/local/stow</i> as the stow directory, so that individual packages will be, for example, <i>/usr/local/stow/perl</i> and <i>/usr/local/stow/emacs</i>. </p>
<p> An &#8220;installation image&#8221; is the layout of files and directories required by a package, relative to the target directory. Thus, the installation image for Perl includes: a <i>bin</i> directory containing <i>perl</i> and <i>a2p</i> (among others); an <i>info</i> directory containing Texinfo documentation; a <i>lib/perl</i> directory containing Perl libraries; and a <i>man/man1</i> directory containing man pages. </p>
<p> A &#8220;package directory&#8221; is the root of a tree containing the installation image for a particular package. Each package directory must reside in a stow directory &#8212; e.g., the package directory <i>/usr/local/stow/perl</i> must reside in the stow directory <i>/usr/local/stow</i>. The &#8220;name&#8221; of a package is the name of its directory within the stow directory &#8212; e.g., <i>perl</i>. </p>
<p> Thus, the Perl executable might reside in <i>/usr/local/stow/perl/bin/perl</i>, where <i>/usr/local</i> is the target directory, <i>/usr/local/stow</i> is the stow directory, <i>/usr/local/stow/perl</i> is the package directory, and <i>bin/perl</i> within is part of the installation image. </p>
<p> A &#8220;symlink&#8221; is a symbolic link. A symlink can be &#8220;relative&#8221; or &#8220;absolute&#8221;. An absolute symlink names a full path; that is, one starting from <i>/</i>. A relative symlink names a relative path; that is, one not starting from <i>/</i>. The target of a relative symlink is computed starting from the symlink&#8217;s own directory. Stow only creates relative symlinks.</p>
<h2>Options</h2>
<p>The stow directory is assumed to be the value of the <tt>&quot;STOW_DIR&quot;</tt> environment variable or if unset the current directory, and the target directory is assumed to be the parent of the current directory (so it is typical to execute <i>stow</i> from the directory <i>/usr/local/stow</i>). Each <i>package</i> given on the command line is the name of a package in the stow directory (e.g., <i>perl</i>). By default, they are installed into the target directory (but they can be deleted instead using <tt>&quot;-D&quot;</tt>).</p>
<dl>
<dt>-n</p>
<dd>
<dt>&#8211;no</p>
<dd>Do not perform any operations that modify the filesystem; merely show what would happen.</p>
<dt>-d <font SIZE="-1">DIR</font></p>
<dd>
<dt>&#8211;dir=DIR</p>
<dd>Set the stow directory to <tt>&quot;DIR&quot;</tt> instead of the current directory. This also has the effect of making the default target directory be the parent of <tt>&quot;DIR&quot;</tt>.</p>
<dt>-t <font SIZE="-1">DIR</font></p>
<dd>
<dt>&#8211;target=DIR</p>
<dd>Set the target directory to <tt>&quot;DIR&quot;</tt> instead of the parent of the stow directory.</p>
<dt>-v</p>
<dd>
<dt>&#8211;verbose[=N]</p>
<dd>Send verbose output to standard error describing what Stow is doing. Verbosity levels are 0, 1, 2, 3, and 4; 0 is the default. Using <tt>&quot;-v&quot;</tt> or <tt>&quot;--verbose&quot;</tt> increases the verbosity by one; using `&#8211;verbose=N&#8217; sets it to N.</p>
<dt>-S</p>
<dd>
<dt>&#8211;stow</p>
<dd>Stow the packages that follow this option into the target directory. This is the default action and so can be omitted if you are only stowing packages rather than performing a mixture of stow/delete/restow actions.</p>
<dt>-D</p>
<dd>
<dt>&#8211;delete</p>
<dd>Unstow the packages that follow this option from the target directory rather than installing them.</p>
<dt>-R</p>
<dd>
<dt>&#8211;restow</p>
<dd>Restow packages (first unstow, then stow again). This is useful for pruning obsolete symlinks from the target tree after updating the software in a package.</p>
<dt>&#8211;adopt</p>
<dd><code>Warning!</code> This behaviour is specifically intended to alter the contents of your stow directory. If you do not want that, this option is not for you. </p>
<p> When stowing, if a target is encountered which already exists but is a plain file (and hence not owned by any existing stow package), then normally Stow will register this as a conflict and refuse to proceed. This option changes that behaviour so that the file is moved to the same relative place within the package&#8217;s installation image within the stow directory, and then stowing proceeds as before. So effectively, the file becomes adopted by the stow package, without its contents changing.</p>
<dt>&#8211;no-folding</p>
<dd>Disable folding of newly stowed directories when stowing, and refolding of newly foldable directories when unstowing.</p>
<dt>&#8211;ignore=REGEX</p>
<dd>Ignore files ending in this Perl regex.</p>
<dt>&#8211;defer=REGEX</p>
<dd>Don&#8217;t stow files beginning with this Perl regex if the file is already stowed to another package.</p>
<dt>&#8211;override=REGEX</p>
<dd>Force stowing files beginning with this Perl regex if the file is already stowed to another package.</p>
<dt>-V</p>
<dd>
<dt>&#8211;version</p>
<dd>Show Stow version number, and exit.</p>
<dt>-h</p>
<dd>
<dt>&#8211;help</p>
<dd>Show Stow command syntax, and exit.</dl>
<h2>Installing Packages</h2>
<p>The default action of Stow is to install a package. This means creating symlinks in the target tree that point into the package tree. Stow attempts to do this with as few symlinks as possible; in other words, if Stow can create a single symlink that points to an entire subtree within the package tree, it will choose to do that rather than create a directory in the target tree and populate it with symlinks. </p>
<p> For example, suppose that no packages have yet been installed in <i>/usr/local</i>; it&#8217;s completely empty (except for the <i>stow</i> subdirectory, of course). Now suppose the Perl package is installed. Recall that it includes the following directories in its installation image: <i>bin</i>; <i>info</i>; <i>lib/perl</i>; <i>man/man1</i>. Rather than creating the directory <i>/usr/local/bin</i> and populating it with symlinks to <i>../stow/perl/bin/perl</i> and <i>../stow/perl/bin/a2p</i> (and so on), Stow will create a single symlink, <i>/usr/local/bin</i>, which points to <i>stow/perl/bin</i>. In this way, it still works to refer to <i>/usr/local/bin/perl</i> and <i>/usr/local/bin/a2p</i>, and fewer symlinks have been created. This is called &#8220;tree folding&#8221;, since an entire subtree is &#8220;folded&#8221; into a single symlink. </p>
<p> To complete this example, Stow will also create the symlink <i>/usr/local/info</i> pointing to <i>stow/perl/info</i>; the symlink <i>/usr/local/lib</i> pointing to <i>stow/perl/lib</i>; and the symlink <i>/usr/local/man</i> pointing to <i>stow/perl/man</i>. </p>
<p> Now suppose that instead of installing the Perl package into an empty target tree, the target tree is not empty to begin with. Instead, it contains several files and directories installed under a different system-administration philosophy. In particular, <i>/usr/local/bin</i> already exists and is a directory, as are <i>/usr/local/lib</i> and <i>/usr/local/man/man1</i>. In this case, Stow will descend into <i>/usr/local/bin</i> and create symlinks to <i>../stow/perl/bin/perl</i> and <i>../stow/perl/bin/a2p</i> (etc.), and it will descend into <i>/usr/local/lib</i> and create the tree-folding symlink <i>perl</i> pointing to <i>../stow/perl/lib/perl</i>, and so on. As a rule, Stow only descends as far as necessary into the target tree when it can create a tree-folding symlink. </p>
<p> The time often comes when a tree-folding symlink has to be undone because another package uses one or more of the folded subdirectories in its installation image. This operation is called &#8220;splitting open&#8221; a folded tree. It involves removing the original symlink from the target tree, creating a true directory in its place, and then populating the new directory with symlinks to the newly-installed package <code>and</code> to the old package that used the old symlink. For example, suppose that after installing Perl into an empty <i>/usr/local</i>, we wish to install Emacs. Emacs&#8217;s installation image includes a <i>bin</i> directory containing the <i>emacs</i> and <i>etags</i> executables, among others. Stow must make these files appear to be installed in <i>/usr/local/bin</i>, but presently <i>/usr/local/bin</i> is a symlink to <i>stow/perl/bin</i>. Stow therefore takes the following steps: the symlink <i>/usr/local/bin</i> is deleted; the directory <i>/usr/local/bin</i> is created; links are made from <i>/usr/local/bin</i> to <i>../stow/emacs/bin/emacs</i> and <i>../stow/emacs/bin/etags</i>; and links are made from <i>/usr/local/bin</i> to <i>../stow/perl/bin/perl</i> and <i>../stow/perl/bin/a2p</i>. </p>
<p> When splitting open a folded tree, Stow makes sure that the symlink it is about to remove points inside a valid package in the current stow directory.</p>
<h3>Stow will never delete anything that it doesn&#8217;t own.</h3>
<p>Stow &#8220;owns&#8221; everything living in the target tree that points into a package in the stow directory. Anything Stow owns, it can recompute if lost. Note that by this definition, Stow doesn&#8217;t &#8220;own&#8221; anything <code>in</code> the stow directory or in any of the packages. </p>
<p> If Stow needs to create a directory or a symlink in the target tree and it cannot because that name is already in use and is not owned by Stow, then a conflict has arisen. See the &#8220;Conflicts&#8221; section in the info manual.</p>
<h2>Deleting Packages</h2>
<p>When the <tt>&quot;-D&quot;</tt> option is given, the action of Stow is to delete a package from the target tree. Note that Stow will not delete anything it doesn&#8217;t &#8220;own&#8221;. Deleting a package does <code>not</code> mean removing it from the stow directory or discarding the package tree. </p>
<p> To delete a package, Stow recursively scans the target tree, skipping over the stow directory (since that is usually a subdirectory of the target tree) and any other stow directories it encounters (see &#8220;Multiple stow directories&#8221; in the info manual). Any symlink it finds that points into the package being deleted is removed. Any directory that contained only symlinks to the package being deleted is removed. Any directory that, after removing symlinks and empty subdirectories, contains only symlinks to a single other package, is considered to be a previously &#8220;folded&#8221; tree that was &#8220;split open.&#8221; Stow will re-fold the tree by removing the symlinks to the surviving package, removing the directory, then linking the directory back to the surviving package.</p>
<h2>See Also</h2>
<p>The full documentation for <i>stow</i> is maintained as a Texinfo manual. If the <i>info</i> and <i>stow</i> programs are properly installed at your site, the command </p>
<pre> info stow</pre>
<p>should give you access to the complete manual.</p>
<h2>Bugs</h2>
<p>Please report bugs in Stow using the Debian bug tracking system. </p>
<p> Currently known bugs include:</p>
<dl>
<dt>&bull;</p>
<dd>The empty-directory problem. </p>
<p> If package <i>foo</i> includes an empty directory &#8212; say, <i>foo/bar</i> &#8212; then if no other package has a <i>bar</i> subdirectory, everything&#8217;s fine. If another stowed package <i>quux</i>, has a <i>bar</i> subdirectory, then when stowing, <i>targetdir/bar</i> will be &#8220;split open&#8221; and the contents of <i>quux/bar</i> will be individually stowed. So far, so good. But when unstowing <i>quux</i>, <i>targetdir/bar</i> will be removed, even though <i>foo/bar</i> needs it to remain. A workaround for this problem is to create a file in <i>foo/bar</i> as a placeholder. If you name that file <i>.placeholder</i>, it will be easy to find and remove such files when this bug is fixed.</p>
<dt>&bull;</p>
<dd>When using multiple stow directories (see &#8220;Multiple stow directories&#8221; in the info manual), Stow fails to &#8220;split open&#8221; tree-folding symlinks (see &#8220;Installing packages&#8221; in the info manual) that point into a stow directory which is not the one in use by the current Stow command. Before failing, it should search the target of the link to see whether any element of the path contains a <i>.stow</i> file. If it finds one, it can &#8220;learn&#8221; about the cooperating stow directory to short-circuit the <i>.stow</i> search the next time it encounters a tree-folding symlink.</dl>
<h2>Author</h2>
<p>This man page was originally constructed by Charles Briscoe-Smith from parts of Stow&#8217;s info manual, and then converted to <font SIZE="-1">POD</font> format by Adam Spiers. The info manual contains the following notice, which, as it says, applies to this manual page, too. The text of the section entitled &#8220;<font SIZE="-1">GNU</font> General Public License&#8221; can be found in the file <i>/usr/share/common-licenses/GPL</i> on any Debian GNU/Linux system. If you don&#8217;t have access to a Debian system, or the <font SIZE="-1">GPL</font> is not there, write to the Free Software Foundation, Inc., 59 Temple Place, Suite 330, Boston, <font SIZE="-1">MA</font>, 02111-1307, <font SIZE="-1">USA</font>.</p>
<h2>Copyright</h2>
<p>Copyright (C) 1993, 1994, 1995, 1996 by Bob Glickstein &lt;bobg+stow [at] zanshin.com&gt;; 2000, 2001 by Guillaume Morin; 2007 by Kahlil Hodgson; 2011 by Adam Spiers; and others. </p>
<p> Permission is granted to make and distribute verbatim copies of this manual provided the copyright notice and this permission notice are preserved on all copies. </p>
<p> Permission is granted to copy and distribute modified versions of this manual under the conditions for verbatim copying, provided also that the section entitled &#8220;<font SIZE="-1">GNU</font> General Public License&#8221; is included with the modified manual, and provided that the entire resulting derived work is distributed under the terms of a permission notice identical to this one. </p>
<p> Permission is granted to copy and distribute translations of this manual into another language, under the above conditions for modified versions, except that this permission notice may be stated in a translation approved by the Free Software Foundation.</p>
