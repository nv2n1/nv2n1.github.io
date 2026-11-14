---
title: "git-gui(1)"
name: "git-gui"
section: "1"
letter: "g"
url: "/docs/linux/man/1-git-gui/"
description: "git-gui – A portable graphical interface to Git"
---

<h2 class="name">NAME</h2>
<p> git-gui &#8211; A portable graphical interface to Git </p>
<h2>SYNOPSIS</h2>
<pre><code>
git gui[&lt;command&gt;][arguments]
</code></pre>
<h2>DESCRIPTION</h2>
<p> A Tcl/Tk based graphical user interface to Git. <i>git gui</i> focuses on allowing users to make changes to their repository by making new commits, amending existing ones, creating branches, performing local merges, and fetching/pushing to remote repositories. </p>
<p> Unlike <i>gitk</i>, <i>git gui</i> focuses on commit generation and single file annotation and does not show project history. It does however supply menu actions to start a <i>gitk</i> session from within <i>git gui</i>. </p>
<p> <i>git gui</i> is known to work on all popular UNIX systems, Mac OS X, and Windows (under both Cygwin and MSYS). To the extent possible OS specific user interface guidelines are followed, making <i>git gui</i> a fairly native interface for users.</p>
<h2>COMMANDS</h2>
<p> blame</p>
<dl>
<dt>
<dd> Start a blame viewer on the specified file on the given version (or working directory if not specified).</dl>
<p> browser</p>
<dl>
<dt>
<dd> Start a tree browser showing all files in the specified commit (or <i>HEAD</i> by default). Files selected through the browser are opened in the blame viewer.</dl>
<p> citool</p>
<dl>
<dt>
<dd> Start <i>git gui</i> and arrange to make exactly one commit before exiting and returning to the shell. The interface is limited to only commit actions, slightly reducing the application&#8217;s startup time and simplifying the menubar.</dl>
<p> version</p>
<dl>
<dt>
<dd> Display the currently running version of <i>git gui</i>.</dl>
<h2>EXAMPLES</h2>
<p> git gui blame Makefile</p>
<dl>
<dt>
<dd> Show the contents of the file <i>Makefile</i> in the current working directory, and provide annotations for both the original author of each line, and who moved the line to its current location. The uncommitted file is annotated, and uncommitted changes (if any) are explicitly attributed to <i>Not Yet Committed</i>.</dl>
<p> git gui blame v0.99.8 Makefile</p>
<dl>
<dt>
<dd> Show the contents of <i>Makefile</i> in revision <i>v0.99.8</i> and provide annotations for each line. Unlike the above example the file is read from the object database and not the working directory.</dl>
<p> git gui blame &#8211;line=100 Makefile</p>
<dl>
<dt>
<dd> Loads annotations as described above and automatically scrolls the view to center on line <i>100</i>.</dl>
<p> git gui citool</p>
<dl>
<dt>
<dd> Make one commit and return to the shell when it is complete. This command returns a non-zero exit code if the window was closed in any way other than by making a commit.</dl>
<p> git gui citool &#8211;amend</p>
<dl>
<dt>
<dd> Automatically enter the <i>Amend Last Commit</i> mode of the interface.</dl>
<p> git gui citool &#8211;nocommit</p>
<dl>
<dt>
<dd> Behave as normal citool, but instead of making a commit simply terminate with a zero exit code. It still checks that the index does not contain any unmerged entries, so you can use it as a GUI version of <code><a href="/docs/linux/man/1-git-mergetool/">git-mergetool</a></code>(1)</dl>
<p> git citool</p>
<dl>
<dt>
<dd> Same as git gui citool (above).</dl>
<p> git gui browser maint</p>
<dl>
<dt>
<dd> Show a browser for the tree of the <i>maint</i> branch. Files selected in the browser can be viewed with the internal blame viewer.</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-gitk/">gitk</a></code>(1)</p>
<dl>
<dt>
<dd> The Git repository browser. Shows branches, commit history and file differences. gitk is the utility started by <i>git gui</i>&#8216;s Repository Visualize actions.</dl>
<h2>OTHER</h2>
<p> <i>git gui</i> is actually maintained as an independent project, but stable versions are distributed as part of the Git suite for the convenience of end users. </p>
<p> A <i>git gui</i> development repository can be obtained from: </p>
<dl>
<dt>
<dd>
<pre>
git clone <a href="git://repo.or.cz/git-gui.git">git://repo.or.cz/git-gui.git</a>
</pre>
</dl>
<p> or </p>
<dl>
<dt>
<dd>
<pre>
git clone <a rel="nofollow" href="http://repo.or.cz/r/git-gui.git">http://repo.or.cz/r/git-gui.git</a>
</pre>
</dl>
<p> or browsed online at m[blue]<code><a rel="nofollow" href="http://repo.or.cz/w/git-gui.git/">http://repo.or.cz/w/git-gui.git/</a></code>m[].</p>
<h2>GIT</h2>
<p> Part of the <code><a href="/docs/linux/man/1-git/">git</a></code>(1) suite </p>
<h2>Index</h2>
