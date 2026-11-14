---
title: "tkcvs(1)"
name: "tkcvs"
section: "1"
letter: "t"
url: "/docs/linux/man/1-tkcvs/"
description: "TkCVS – a Tk/Tcl Graphical Interface to CVS and Subversion"
---

<h2>NAME</h2>
<p> TkCVS &#8211; a Tk/Tcl Graphical Interface to CVS and Subversion</p>
<h2>SYNOPSIS</h2>
<p> <code>tkcvs</code> [-dir directory] [-root cvsroot] [-win workdir|module|merge] [-log file]</p>
<h2>DESCRIPTION</h2>
<p> TkCVS is a Tcl/Tk-based graphical interface to the CVS and Subversion configuration management systems. It displays the status of the files in the current working directory, and provides buttons and menus to execute configuration-management commands on the selected files. Limited RCS functionality is also present. TkDiff is bundled in for browsing and merging your changes. </p>
<p> TkCVS also aids in browsing the repository. For Subversion, the repository tree is browsed like an ordinary file tree. For CVS, the CVSROOT/modules file is read. TkCVS extends CVS with a method to produce a browsable, &quot;user friendly&quot; listing of modules. This requires special comments in the CVSROOT/modules file. See &quot;CVS Modules File&quot; for more guidance.</p>
<h2>OPTIONS</h2>
<p> TkCVS accepts the following options.</p>
<dl>
<dt><code>-dir</code><i> directory</i></p>
<dd> Start TkCVS in the specified directory.</p>
<dt><code>-help</code></p>
<dd> Print a usage message.</p>
<dt><code>-log</code><i> file</i></p>
<dd> Invoke a log browser for the specified file. -log and -win are mutually exclusive.</p>
<dt><code>-root</code><i> cvsroot</i></p>
<dd> Set $CVSROOT to the specified repository.</p>
<dt><code>-win</code><i> workdir|module|merge</i></p>
<dd> Start by displaying the directory browser (the default), the module browser, or the directory-merge tool. -win and -log are mutually exclusive.</dl>
<h2>Examples</h2>
<dl>
<dt>
<dd> % tkcvs -win module -root /jaz/repository</dl>
<p> Browse the modules located in CVSROOT /jaz/repository</p>
<dl>
<dt>
<dd> % tkcvs -log tstheap.c</dl>
<p> View the log of the file tstheap.c</p>
<h2>Working Directory Browser</h2>
<p> The working directory browser shows the files in your local working copy, or &quot;sandbox.&quot; It shows the status of the files at a glance and provides tools to help with most of the common CVS, SVN, and RCS operations you might do. </p>
<p> At the top of the browser you will find: </p>
<p> * The name of the current directory. You can change directories by typing in this field. Recently visited directories are saved in the picklist. </p>
<p> * The relative path of the current directory in the repository. If it is not contained in the repository you may import it using the menu or toolbar button. </p>
<p> * A Directory Tag name, if the directory is contained in the repository and it has been checked out against a particular branch or tag. In Subversion, the branch or tag is inferred from the URL based on the conventional trunk-branches-tags repository organization. </p>
<p> * The CVSROOT of the current directory if it&#8217;s under CVS control, or the URL of the Subversion repository if it&#8217;s under Subversion control. If neither is true, it may default to the value of the $CVSROOT environment variable. </p>
<p> The main part of the working directory browser is a list of the files in the current directory with an icon next to each showing its status. You select a file by clicking on its name or icon once with the left mouse button. Holding the Control key while clicking will add the file to the group of those already selected. You can select a contiguous group of files by holding the Shift key while clicking. You can also select a group of files by dragging the mouse with the middle or right button pressed to select an area. Selecting an item that&#8217;s already selected de-selects that item. To unselect all files, click the left mouse button in an empty area of the file list. </p>
<p> * The Date column (can be hidden) shows the modification time of the file is shown. The format of the date column may be specified with cvscfg(dateformat). The default format was chosen because it sorts the same way alphabetically as chronologically. </p>
<p> If the directory belongs to a revision system, other columns are present. </p>
<p> * The revision column shows which revision of the file is checked out, and whether it&#8217;s on the trunk or on a branch. </p>
<p> * The status column (can be hidden) shows the revision of the file spelled out in text. This information is mostly redundant to the icon in the file column. </p>
<p> * The Editor/Author/Locker column (can be hidden) varies according to revision system. In Subversion, the author of the most recent checkin is shown. In CVS, it shows a list of people editing the files if your site uses &quot;cvs watch&quot; and/or &quot;cvs edit&quot;. Otherwise, it will be empty. In RCS, it shows who, if anyone, has the file locked. </p>
<p> The optional columns can be displayed or hidden using the Options menu. </p>
<p> You can move into a directory by double-clicking on it. </p>
<p> Double clicking on a file will load the file into a suitable editor so you can change it. A different editor can be used for different file types (see Configuration Files).</p>
<h3>File Status</h3>
<p> When you are in a directory that is under CVS or Subversion control, the file status will be shown by an icon next to each file. Checking the &quot;Status Column&quot; option causes the status to be displayed in text in its own column. Some possible statuses are:</p>
<dl>
<dt><code>Up-to-date</code></p>
<dd> The file is up to date with respect to the repository.</p>
<dt><code>Locally Modified</code></p>
<dd> The file has been modified in the current directory since being checked out of the repository.</p>
<dt><code>Locally Added</code></p>
<dd> The file has been added to the repository. This file will become permanent in the repository once a commit is made.</p>
<dt><code>Locally Removed</code></p>
<dd> You have removed the file with remove, and not yet committed your changes.</p>
<dt><code>Needs Checkout</code></p>
<dd> Someone else has committed a newer revision to the repository. The name is slightly misleading; you will ordinarily use update rather than checkout to get that newer revision.</p>
<dt><code>Needs Patch</code></p>
<dd> Like Needs Checkout, but the CVS server will send a patch rather than the entire file. Sending a patch or sending an entire file accomplishes the same thing.</p>
<dt><code>Needs Merge</code></p>
<dd> Someone else has committed a newer revision to the repository, and you have also made modifications to the file.</p>
<dt><code>Unresolved Conflict</code></p>
<dd> This is like Locally Modified, except that a previous update command gave a conflict. You need to resolve the conflict before checking in.</p>
<dt><code>?</code></p>
<dd> The file is not contained in the repository. You may need to add the file to the repository by pressing the &quot;Add&quot; button.</p>
<dt><code>[directory:CVS]</code></p>
<dd> A directory which has been checked out from a CVS repository.</p>
<dt><code>[directory:SVN]</code></p>
<dd> The file is a directory which has been checked out from a Subversion repository. In Subversion, directories are themselves versioned objects.</p>
<dt><code>[directory:RCS]</code></p>
<dd> A directory which contains an RCS sub-directory or some files with the ,v suffix, presumably containing some files that are under RCS revision control.</p>
<dt><code>[directory]</code></p>
<dd> The file is a directory.</dl>
<h3>File Filters</h3>
<p> You can specify file matching patterns to instruct TkCVS which files you wish to see. You can also specify patterns telling it which files to remove when you press the &quot;Clean&quot; button or select the <code>File-&gt;Cleanup</code> menu item. </p>
<p> &quot;Hide&quot; works exactly the way a .cvsignore file works. That is, it causes non-CVS files with the pattern to be ignored. It&#8217;s meant for hiding .o files and such. Any file under CVS control will be listed anyway. </p>
<p> &quot;Show&quot; is the inverse. It hides non-CVS files except for those with the pattern.</p>
<h3>Buttons</h3>
<dl>
<dt><i>Module Browser:</i></p>
<dd> The big button at the upper right opens the module browser. Opens a module browser window which will enable you to explore items in the repository even if they&#8217;re not checked out. In CVS, this requires that there be entries in the CVSROOT/modules file. Browsing can be improved by using TkCVS-specific comments in CVSROOT/modules.</p>
<dt><i>Go Up:</i></p>
<dd> The button to the left of the entry that shows the current directory. Press it and you go up one level.</dl>
<p> There are a number of buttons at the bottom of the window. Pressing on one of these causes the following actions:</p>
<dl>
<dt><i>Delete:</i></p>
<dd> Press this button to delete the selected files. The files will not be removed from the repository. To remove the files from the repository as well as delete them, press the &quot;Remove&quot; button instead.</p>
<dt><i>Edit:</i></p>
<dd> Press this button to load the selected files in to an appropriate editor.</p>
<dt><i>View:</i></p>
<dd> Press this button to view the selected files in a Tk text window. This can be a lot faster then Edit, in case your preferred editor is xemacs or something of that magnitude.</p>
<dt><i>Refresh:</i></p>
<dd> Press this button to re-read the current directory, in case the status of some files may have changed.</p>
<dt><i>Status Check:</i></p>
<dd> Shows, in a searchable text window, the status of all the files. By default, it is recursive and lists unknown (?) files. These can be changed in the Options menu.</p>
<dt><i>Directory Branch Browse:</i></p>
<dd> For merging the entire directory. In Subversion, it opens the Branch Browser for &quot;.&quot; In CVS, it chooses a &quot;representative&quot; file in the current directory and opens a graphical tool for directory merges.</p>
<dt><i>Log (Branch) Browse:</i></p>
<dd> This button will bring up the log browser window for each of the selected files in the window. See the Log Browser section.</p>
<dt><i>Annotate:</i></p>
<dd> This displays a window in which the selected file is shown with the lines highlighted according to when and by whom they were last revised. In Subversion, it&#8217;s also called &quot;blame.&quot;</p>
<dt><i>Diff:</i></p>
<dd> This compares the selected files with the equivalent files in the repository. A separate program called &quot;TkDiff&quot; (also supplied with TkCVS) is used to do this. For more information on TkDiff, see TkDiff&#8217;s help menu.</p>
<dt><i>Merge Conflict:</i></p>
<dd> If a file&#8217;s status says &quot;Needs Merge&quot;, &quot;Conflict&quot;, or is marked with a &quot;C&quot; in CVS Check, there was a difference which CVS needs help to reconcile. This button invokes TkDiff with the -conflict option, opening a merge window to help you merge the differences.</p>
<dt><i>Check In:</i></p>
<dd> This button commits your changes to the repository. This includes adding new files and removing deleted files. When you press this button, a dialog will appear asking you for the version number of the files you want to commit, and a comment. You need only enter a version number if you want to bring the files in the repository up to the next major version number. For example, if a file is version 1.10, and you do not enter a version number, it will be checked in as version 1.11. If you enter the version number 3, then it will be checked in as version 3.0 instead. It is usually better to use symbolic tags for that purpose. If you use rcsinfo to supply a template for the comment, you must use an external editor. Set cvscfg(use_cvseditor) to do this. For checking in to RCS, an externel editor is always used.</p>
<dt><i>Update:</i></p>
<dd> This updates your sandbox directory with any changes committed to the repository by other developers.</p>
<dt><i>Update with Options:</i></p>
<dd> Allows you to update from a different branch, with a tag, with empty directories, and so on.</p>
<dt><i>Add Files:</i></p>
<dd> Press this button when you want to add new files to the repository. You must create the file before adding it to the repository. To add some files, select them and press the Add Files button. The files that you have added to the repository will be committed next time you press the Check In button. It is not recursive. Use the menu CVS -&gt; Add Recursively for that.</p>
<dt><i>Remove Files:</i></p>
<dd> This button will remove files. To remove files, select them and press the Remove button. The files will disappear from the directory, and will be removed from the repository next time you press the Check In button. It is not recursive. Use the menu CVS -&gt; Remove Recursively for that.</p>
<dt><i>Tag:</i></p>
<dd> This button will tag the selected files. In CVS, the -F (force) option will move the tag if it already exists on the file.</p>
<dt><i>Branch Tag:</i></p>
<dd> This button will tag the selected files, creating a branch. In CVS, the -F (force) option will move the tag if it already exists on the file.</p>
<dt><i>Lock (CVS and RCS):</i></p>
<dd> Lock an RCS file for editing. If cvscfg(cvslock) is set, lock a CVS file. Use of locking is philosophically discouraged in CVS since it&#8217;s against the &quot;concurrent&quot; part of Concurrent Versioning System, but locking policy is nevertheless used at some sites. One size doesn&#8217;t fit all.</p>
<dt><i>Unlock (CVS and RCS):</i></p>
<dd> Unlock an RCS file. If cvscfg(cvslock) is set, unlock a CVS file.</p>
<dt><i>Set Edit Flag (CVS):</i></p>
<dd> This button sets the edit flag on the selected files, enabling other developers to see that you are currently editing those files (See &quot;cvs edit&quot; in the CVS documentation).</p>
<dt><i>Reset Edit Flag (CVS):</i></p>
<dd> This button resets the edit flag on the selected files, enabling other developers to see that you are no longer editing those files (See &quot;cvs edit&quot; in the CVS documentation). As the current version of cvs waits on a prompt for &quot;cvs unedit&quot; if changes have been made to the file in question (to ask if you want to revert the changes to the current revision), the current action of tkcvs is to abort the unedit (by piping in nothing to stdin). Therefore, to lose the changes and revert to the current revision, it is necessary to delete the file and do an update (this will also clear the edit flag). To keep the changes, make a copy of the file, delete the original, update, and then move the saved copy back to the original filename.</p>
<dt><i>Close:</i></p>
<dd> Press this button to close the Working Directory Browser. If no other windows are open, TkCVS exits.</dl>
<h2>Log (Branch) Browser</h2>
<p> The TkCVS Log Browser window enables you to view a graphical display of the revision log of a file, including all previous versions and any branched versions. </p>
<p> You can get to the log browser window in three ways, either by invoking it directly with &quot;tkcvs [-log] &lt;filename&gt;&quot;, by selecting a file within the main window of TkCVS and pressing the Log Browse button, or by selecting a file in a list invoked from the module browser and pressing the Log Browse button. </p>
<p> If the Log Browser is examining a checked-out file, the buttons for performing merge operations are enabled.</p>
<h3>Log Browser Window</h3>
<p> The log browser window has three components. These are the file name and version information section at the top, the log display in the middle, and a row of buttons along the bottom.</p>
<h3>Log Display</h3>
<p> The main log display is fairly self explanatory. It shows a group of boxes connected by lines indicating the main trunk of the file development (on the left hand side) and any branches that the file has (which spread out to the right of the main trunk). </p>
<p> Each box contains the version number, author of the version, and other information determined by the menu View -&gt; Revision Layout. </p>
<p> Constructing the branch diagram from Subversion is inefficient, so the Log Browser counts the tags when doing a Subversion diagram and pops up a dialog giving you a chance to skip the tag step if there are too many tags (where &quot;many&quot; arbitrarily equals 10.)</p>
<h3>Version Numbers</h3>
<p> Once a file is loaded into the log browser, one or two version numbers may be selected. The primary version (Selection A) is selected by clicking the left mouse button on a version box in the main log display. </p>
<p> The secondary version (Selection B) is selected by clicking the right mouse button on a version box in the main log display. </p>
<p> Operations such as &quot;View&quot; and &quot;Annotate&quot; operate only on the primary version selected. </p>
<p> Operations such as &quot;Diff&quot; and &quot;Merge Changes to Current&quot; require two versions to be selected.</p>
<h3>Searching the Diagram</h3>
<p> You can search the canvas for tags, revisions, authors, and dates. </p>
<p> The following special characters are used in the search pattern: </p>
<p>&nbsp;<wbr>&nbsp;<wbr>*&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Matches any sequence of characters in string, including a null string. </p>
<p>&nbsp;<wbr>&nbsp;<wbr>?&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Matches any single character in string. </p>
<p>&nbsp;<wbr>&nbsp;<wbr>[chars]&nbsp;<wbr>Matches any character in the set given by chars. If a sequence of the form x-y appears in chars, then any character between x and y, inclusive, will match. </p>
<p>Matches the single character x. This provides a way of avoiding the special interpretation of the characters&nbsp;<wbr>*?[]&nbsp;<wbr>in pattern. </p>
<p> If you only enter &quot;FOO&quot; (without the</p>
<h3>Log Browser Buttons</h3>
<p> The log browser contains the following buttons:</p>
<dl>
<dt><i>Refresh:</i></p>
<dd> Re-reads the revision history of the file.</p>
<dt><i>View:</i></p>
<dd> Pressing this button displays a Tk text window containing the version of the file at Selection A.</p>
<dt><i>Annotate:</i></p>
<dd> This displays a window in which the file is shown with its lines highlighted according to when and by whom they were last revised. In Subversion, it&#8217;s also called &quot;blame.&quot;</p>
<dt><i>Diff:</i></p>
<dd> Pressing this button runs the &quot;tkdiff&quot; program to display the differences between version A and version B.</p>
<dt><i>Merge:</i></p>
<dd> To use this button, select a branch version of the file, other than the branch you are currently on, as the primary version (Selection A). The changes made along the branch up to that version will be merged into the current version, and stored in the current directory. Optionally, select another version (Selection B) and the changes will be from that point rather than from the base of the branch. The version of the file in the current directory will be merged, but no commit will occur. Then you inspect the merged files, correct any conflicts which may occur, and commit when you are satisfied. Optionally, TkCVS will tag the version that the merge is from. It suggests a tag of the form &quot;mergefrom_&lt;rev&gt;_date.&quot; If you use this auto-tagging function, another dialog containing a suggested tag for the merged-to version will appear. It&#8217;s suggested to leave the dialog up until you are finished, then copy-and-paste the suggested tag into the &quot;Tag&quot; dialog. It is always a good practice to tag when doing merges, and if you use tags of the suggested form, the Branch Browser can diagram them. (Auto-tagging is not implemented in Subversion because, despite the fact that tags are &quot;cheap,&quot; it&#8217;s somewhat impractical to auto-tag single files. You can do the tagging manually, however.)</p>
<dt><i>View Tags:</i></p>
<dd> This button lists all the tags applied to the file in a searchable text window.</p>
<dt><i>Close:</i></p>
<dd> This button closes the Log Browser. If no other windows are open, TkCVS exits.</dl>
<h3>The View Options Menu</h3>
<p> The View Menu allows you to control what you see in the branch diagram. You can choose how much information to show in the boxes, whether to show empty revisions, and whether to show tags. You can even control the size of the boxes. If you are using Subversion, you may wish to turn the display of tags off. If they aren&#8217;t asked for they won&#8217;t be read from the repository, which can save a lot of time.</p>
<h2>Merge Tool for CVS</h2>
<p> The Merge Tool chooses a &quot;representative&quot; file in the current directory and diagrams the branch tags. It tries to pick the &quot;bushiest&quot; file, or failing that, the most-revised file. If you disagree with its choice, you can type the name of another file in the top entry and press Return to diagram that file instead. </p>
<p> The main purpose of this tool is to do merges (cvs update -j rev [-j rev]) on the whole directory. For merging one file at a time, you should use the Log Browser. You can only merge to the line (trunk or branch) that you are currently on. Select a branch to merge from by clicking on it. Then press either the &quot;Merge&quot; or &quot;Merge Changes&quot; button. The version of the file in the current directory will be over-written, but it will not be committed to the repository. You do that after you&#8217;ve reconciled conflicts and decided if it&#8217;s what you really want.</p>
<dl>
<dt><i>Merge Branch to Current:</i></p>
<dd> The changes made on the branch since its beginning will be merged into the current version.</p>
<dt><i>Merge Changes to Current:</i></p>
<dd> Instead of merging from the base of the branch, this button merges the changes that were made since a particular version on the branch. It pops up a dialog in which you fill in the version. It should usually be the version that was last merged.</dl>
<h2>Module Browser</h2>
<p> Operations that are performed on the repository instead of in a checked-out working directory are done with the Module Browser. The most common of these operations is checking out or exporting from the repository. The Module Browser can be started from the command line (tkcvs -win module) or started from the main window by pressing the big button. </p>
<p> Subversion repositories can be browsed like a file tree, and that is what you will see in the Module Browser. CVS repositories aren&#8217;t directly browsable, but if the CVSROOT/modules file is maintained appropriately, TkCVS can display the modules and infer tree structures if they are present. See the &quot;CVS Modules File&quot; section. </p>
<p> Using the module browser window, you can select a module to check out. When you check out a module, a new directory is created in the current working directory with the same name as the module.</p>
<h3>Tagging and Branching (cvs rtag)</h3>
<p> You can tag particular versions of a module or file in the repository, with plain or branch tags, without having the module checked out.</p>
<h3>Exporting</h3>
<p> Once a software release has been tagged, you can use a special type of checkout called an export. This allows you to cleanly check out files from the repository, without all of the administrivia that CVS needs to have while working on the files. It is useful for delivery of a software release to a customer.</p>
<h3>Importing</h3>
<p> TkCVS contains a special dialog to allow users to import new files into the repository. In CVS, new modules can be assigned places within the repository, as well as descriptive names (so that other people know what they are for). </p>
<p> When the Module Browser displays a CVS repository, the first column is a tree showing the module codes and directory names of all of the items in the repository. The icon shows whether the item is a directory (which may contain other directories or modules), or whether it is a module (which may be checked out from TkCVS). It is possible for an item to be both a module and a directory. If it has a red ball on it, you can check it out. If it shows a plain folder icon, you have to open the folder to get to the items that you can check out. </p>
<p> To select a module, click on it with the left mouse button. The right mouse button will perform a secondary selection, which is used only for Subversion diff and patch. To clear the selection, click on the item again or click in an empty area of the module column. There can only be one primary and one secondary selection.</p>
<h3>Repository Browser Buttons</h3>
<p> The module browser contains the following buttons:</p>
<dl>
<dt><i>Who:</i></p>
<dd> Shows which modules are checked out by whom.</p>
<dt><i>Import:</i></p>
<dd> This item will import the contents of the current directory (the one shown in the Working Directory Display) into the repository as a module. See the section titled Importing for more information.</p>
<dt><i>File Browse:</i></p>
<dd> Displays a list of the selected module&#8217;s files. From the file list, you can view the file, browse its revision history, or see a list of its tags.</p>
<dt><i>Check Out:</i></p>
<dd> Checks out the current version of a module. A dialog allows you to specify a tag, change the destination, and so on.</p>
<dt><i>Export:</i></p>
<dd> Exports the current version of a module. A dialog allows you to specify a tag, change the destination, and so on. Export is similar to check-out, except exported directories do not contain the CVS or administrative directories, and are therefore cleaner (but cannot be used for checking files back in to the repository). You must supply a tag name when you are exporting a module to make sure you can reproduce the exported files at a later date.</p>
<dt><i>Tag:</i></p>
<dd> This button tags an entire module.</p>
<dt><i>Branch Tag:</i></p>
<dd> This creates a branch of a module by giving it a branch tag.</p>
<dt><i>Patch Summary:</i></p>
<dd> This item displays a short summary of the differences between two versions of a module.</p>
<dt><i>Create Patch File:</i></p>
<dd> This item creates a Larry Wall format <a href="/docs/linux/man/1-patch/">patch</a>(1) file of the module selected.</p>
<dt><i>Close:</i></p>
<dd> This button closes the Repository Browser. If no other windows are open, TkCVS exits.</dl>
<h2>Importing New Modules</h2>
<p> Before importing a new module, first check to make sure that you have write permission to the repository. Also you&#8217;ll have to make sure the module name is not already in use. </p>
<p> To import a module you first need a directory where the module is located. Make sure that there is nothing in this directory except the files that you want to import. </p>
<p> Press the big &quot;Repository Browser&quot; button in the top part of the tkcvs UI, or use CVS -&gt; Import WD into Repository from the menu bar. </p>
<p> In the module browser, press the Import button on the bottom, the one that shows a folder and an up arrow. </p>
<p> In the dialog that pops up, fill in a descriptive title for the module. This will be what you see in the right side of the module browser. </p>
<p> OK the dialog. Several things happen now. The directory is imported, the CVSROOT/module file is updated, your original directory is saved as directory.orig, and the newly created module is checked out. </p>
<p> When it finishes, you should find the original Working Directory Browser showing the files in the newly created, checked out module. </p>
<p> Here is a more detailed description of the fields in the Import Dialog.</p>
<dl>
<dt><i>Module Name:</i></p>
<dd> A name for the module. This name must not already exist in the repository. Your organization could settle on a single unambiguous code for modules. One possibility is something like:</dl>
<dl>
<dt>
<dd>
&nbsp;<wbr>[project code]-[subsystem code]-[module code]</dl>
<dl>
<dt><i>Module Path:</i></p>
<dd> The location in the repository tree where your new module will go.</p>
<dt><i>Descriptive Title:</i></p>
<dd> A one-line descriptive title for your module. This will be displayed in the right-hand column of the browser.</p>
<dt><i>Version Number:</i></p>
<dd> The current version number of the module. This should be a number of the form X.Y.Z where .Y and .Z are optional. You can leave this blank, in which case 1 will be used as the first version number.</dl>
<p> Importing a directory into Subversion is similar but not so complicated. You use the SVN -&gt; Import CWD into Repository menu. You need supply only the path in the repository where you want the directory to go. The repository must be prepared and the path must exist, however.</p>
<h2>Importing to an Existing Module (CVS)</h2>
<p> Before importing to an existing module, first check to make sure that you have write permission to the repository. </p>
<p> To import to an existing module you first need a directory where the code is located. Make sure that there is nothing in this directory (including no CVS directory) except the files that you want to import. </p>
<p> Open up the Repository Browser by selecting File/Browse Modules from the menu bar. </p>
<p> In the Repository Browser, select File/Import To An Existing Module from the menu bar. </p>
<p> In the dialog that pops up, press the Browse button and select the name of an existing module. Press the OK to close this dialog box. Enter the version number of the code to be imported. </p>
<p> OK the dialog. Several things happen now. The directory is imported, your original directory is saved as directory.orig, and the newly created module is checked out. </p>
<p> When it finishes, you will find the original Working Directory Browser showing the original code. If you press the &quot;Re-read the current directory&quot; button you will see the results of the checked out code. </p>
<p> Here is a more detailed description of the fields in the Import Dialog.</p>
<dl>
<dt><i>Module Name:</i></p>
<dd> A name for the existing module. Filled in by the use of the the Browse button</p>
<dt><i>Module Path:</i></p>
<dd> The location in the repository tree where the existing module is. Filled in by the use of the Browse button.</p>
<dt><i>Version Number:</i></p>
<dd> The current version number of the module to be imported. This should be a number of the form X.Y.Z where .Y and .Z are optional. You can leave this blank, in which case 1 will be used as the first version number.</dl>
<h2>Vendor Merge (CVS)</h2>
<p> Software development is sometimes based on source distribution from a vendor or third-party distributor. After building a local version of this distribution, merging or tracking the vendor&#8217;s future release into the local version of the distribution can be done with the vendor merge command. </p>
<p> The vendor merge command assumes that a separate module has already been defined for the vendor or third-party distribution with the use of the &quot;Import To A New Module&quot; and &quot;Import To An Existing Module&quot; commands. It also assumes that a separate module has already been defined for the local code for which the vendor merge operation is to be applied to. </p>
<p> Start from an empty directory and invoke tkcvs. Open up the Repository Browser by selecting File/Browse Modules from the menu bar. </p>
<p> Checkout the module of the local code to be merged with changes from the vendor module. (Use the red icon with the down arrow) </p>
<p> In the Repository Browser, after verifying that the Module entry box still has the name the module of the local code to which the vendor code is to be merged into, select File/Vendor Merge from the menu bar. </p>
<p> In the Module Level Merge With Vendor Code window, press the Browse button to select the module to be used as the vendor module. </p>
<p> OK the dialog. All revisions from the vendor module will be shown in the two scroll lists. Fill in the From and To entry boxes by clicking in the appropriate scroll lists. Ok the dialog. Several things happens now. Several screens will appear showing the output from cvs commands for (1)checking out temp files, (2)cvs merge, and (3)cvs rdiff. Information in these screens will tell you what routines will have merge conflicts and what files are new or deleted. After perusing the files, close each screen. .TP <i>(In the preceeding dialog box, there was an option to save outputs from the merge and rdiff operations to files CVSmerge.out and CVSrdiff.out.)</i> </p>
<p> The checked out local code will now contain changes from a merge between two revisions of the vendor modules. This code will not be checked into the repository. You can do that after you&#8217;ve reconciled conflicts and decide if that is what you really want. </p>
<p> A detailed example on how to use the vendor merge operation is provided in the PDF file vendor5readme.pdf.</p>
<h2>Configuration Files</h2>
<p> There are two configuration files for TkCVS. The first is stored in the directory in which the *.tcl files for TkCVS are installed. This is called tkcvs_def.tcl. You can put a file called site_def in that directory, too. That&#8217;s a good place for site-specific things like tagcolours. Unlike tkcvs_def.tcl, it will not be overwritten when you install a newer version of TkCVS. </p>
<p> Values in the site configuration files can be over-ridden at the user level by placing a .tkcvs file in your home directory. Commands in either of these files should use Tcl syntax. In other words, to set a variable name, you should have the following command in your .tkcvs file: </p>
<dl>
<dt>
<dd>
&nbsp;<wbr>set variablename value</dl>
<p> for example: </p>
<dl>
<dt>
<dd>
&nbsp;<wbr>set cvscfg(editor)&nbsp;<wbr>&quot;gvim&quot;</dl>
<p> The following variables are supported by TkCVS:</p>
<h3>Startup</h3>
<dl>
<dt><code>cvscfg(startwindow)</code></p>
<dd> Which window you want to see on startup. (workdir or module)</dl>
<h3>CVS</h3>
<dl>
<dt><code>cvscfg(cvsroot)</code></p>
<dd> If set, it overrides the CVSROOT environment variable.</dl>
<h3>Subversion</h3>
<p> If your SVN repository has a structure similar to trunk, branches, and tags but with different names, you can tell TkCVS about it by setting variables in tkcvs_def.tcl:<br />
&nbsp;<wbr>set cvscfg(svn_trunkdir)&nbsp;<wbr>&quot;elephants&quot;<br />
&nbsp;<wbr>set cvscfg(svn_branchdir)&nbsp;<wbr>&quot;dogs&quot;<br />
&nbsp;<wbr>set cvscfg(svn_tagdir)&nbsp;<wbr>&quot;ducklings&quot; The branch browser depends on the convention of having a trunk, branches, and tags structure to draw the diagram. These variables may give you a little more flexibility.</p>
<h3>GUI</h3>
<p> Most colors and fonts can be customized by using the options database. For example, you can add lines like these to your .tkcvs file: </p>
<dl>
<dt>
<dd>
option add&nbsp;<wbr>*Canvas.background&nbsp;<wbr>#c3c3c3&nbsp;<wbr></dl>
<dl>
<dt>
<dd>
option add&nbsp;<wbr>*Menu.background&nbsp;<wbr>#c3c3c3&nbsp;<wbr></dl>
<dl>
<dt>
<dd>
option add&nbsp;<wbr>*selectColor&nbsp;<wbr>#ffec8b&nbsp;<wbr></dl>
<dl>
<dt>
<dd>
option add&nbsp;<wbr>*Text.background gray92&nbsp;<wbr></dl>
<dl>
<dt>
<dd>
option add&nbsp;<wbr>*Entry.background gray92&nbsp;<wbr></dl>
<dl>
<dt>
<dd>
option add&nbsp;<wbr>*Listbox.background gray92&nbsp;<wbr></dl>
<dl>
<dt>
<dd>
option add&nbsp;<wbr>*ToolTip.background LightGoldenrod1&nbsp;<wbr></dl>
<dl>
<dt>
<dd>
option add&nbsp;<wbr>*ToolTip.foreground black&nbsp;<wbr></dl>
<dl>
<dt><code>cvscfg(picklist_items)</code></p>
<dd> Maximum number of visited directories and repositories to save in the picklist history</dl>
<h3>Log browser</h3>
<dl>
<dt><code>cvscfg(colourA) cvscfg(colourB)</code></p>
<dd> Hilight colours for revision-log boxes</p>
<dt><code>cvscfg(tagdepth)</code></p>
<dd> Number of tags you want to see for each revision on the branching diagram before it says &quot;more&#8230;&quot; and offers a pop-up to show the rest</p>
<dt><code>cvscfg(toomany_tags)</code></p>
<dd> Number of tags in a Subversion repository that&#8217;s &quot;too many&quot;, ie. will take longer to proecess for the branch diagram than you&#8217;re willing to wait. (Building a branch diagram for Subversion is very inefficient.) If there are more than that number and cvscfg(confirm_prompt) is true, a dialog will appear asking whether to process the tags or to draw the diagram without them.</p>
<dt><code>cvscfg(tagcolour,tagstring)</code></p>
<dd> Colors for marking tags. For example:</p>
<dl>
<dt>
<dd>
&nbsp;<wbr>set cvscfg(tagcolour,tkcvs_r6)&nbsp;<wbr>Purple</dl>
</dl>
<h3>Module browser</h3>
<dl>
<dt><code>cvscfg(aliasfolder)</code></p>
<dd> In the CVS module browser, if true this will cause the alias modules to be grouped in one folder. Cleans up clutter if there are a lot of aliases.</dl>
<h3>User preferences</h3>
<dl>
<dt><code>cvscfg(allfiles)</code></p>
<dd> Set this to false to see normal files only in the directory browser. Set it to true to see all files including hidden files.</p>
<dt><code>cvscfg(auto_status)</code></p>
<dd> Set the default for automatic status-refresh of a CVS controlled directory. Automatic updates are done when a directory is entered and after some operations.</p>
<dt><code>cvscfg(auto_tag)</code></p>
<dd> Whether to tag the merged-from revision when using TkCVS to merge different revisions of files by default. A dialog still lets you change your mind, regardless of the default.</p>
<dt><code>cvscfg(confirm_prompt)</code></p>
<dd> Ask for confirmation before performing an operation(true or false)</p>
<dt><code>cvscfg(dateformat)</code></p>
<dd> Format for the date string shown in the &quot;Date&quot; column, for example &quot;%Y/%m/%d %H:%M&quot;</p>
<dt><code>cvscfg(cvslock)</code></p>
<dd> Set to true to turn on the ability to use cvs-admin locking from the GUI.</p>
<dt><code>cvscfg(econtrol)</code></p>
<dd> Set this to true to turn on the ability to use CVS Edit and Unedit, if your site is configured to allow the feature.</p>
<dt><code>cvscfg(editor)</code></p>
<dd> Preferred default editor</p>
<dt><code>cvscfg(editors)</code></p>
<dd> String pairs giving the editor-command and string-match-pattern, for deciding which editor to use</p>
<dt><code>cvscfg(editorargs)</code></p>
<dd> Command-line arguments to send to the default editing program.</p>
<dt><code>cvscfg(ldetail)</code></p>
<dd> Detail level for status reports (latest, summary, verbose)</p>
<dt><code>cvscfg(mergetoformat)</code></p>
<dd>
<dt><code>cvscfg(mergefromformat)</code></p>
<dd> Format for mergeto- and mergefrom- tags. The _BRANCH_ part must be left as-is, but you can change the prefix and the date format, for example &quot;mergeto_BRANCH_%d%b%y&quot;. The date format must be the same for both. CVS rule: a tag must not contain the characters `$,.:;@&#8217;</p>
<dt><code>cvscfg(rdetail)</code></p>
<dd> Detail for repository and workdir reports (terse, summary, verbose)</p>
<dt><code>cvscfg(recurse)</code></p>
<dd> Whether reports are recursive (true or false)</p>
<dt><code>cvscfg(savelines)</code></p>
<dd> How many lines to keep in the trace window</p>
<dt><code>cvscfg(status_filter)</code></p>
<dd> Filter out unknown files (status &quot;?&quot;) from CVS Check and CVS Update reports.</p>
<dt><code>cvscfg(use_cvseditor)</code></p>
<dd> Let CVS invoke an editor for commit log messages rather than having tkcvs use its own input box. By doing this, your site&#8217;s commit template (rcsinfo) can be used.</dl>
<h3>File filters</h3>
<dl>
<dt><code>cvscfg(file_filter)</code></p>
<dd> Pattern for which files to list. Empty string is equivalent to the entire directory (minus hidden files)</p>
<dt><code>cvscfg(ignore_file_filter)</code></p>
<dd> Pattern used in the workdir filter for files to be ignored</p>
<dt><code>cvscfg(clean_these)</code></p>
<dd> Pattern to be used for cleaning a directory (removing unwanted files)</dl>
<h3>System</h3>
<dl>
<dt><code>cvscfg(print_cmd)</code></p>
<dd> System command used for printing. lpr, enscript -Ghr, etc)</p>
<dt><code>cvscfg(shell)</code></p>
<dd> What you want to happen when you ask for a shell</p>
<dt><code>cvscfg(terminal)</code></p>
<dd> Command prefix to use to run something in a terminal window</dl>
<h3>Portability</h3>
<dl>
<dt><code>cvscfg(aster)</code></p>
<dd> File mask for all files (* for Unix, *.* for windows)</p>
<dt><code>cvscfg(null)</code></p>
<dd> The null device. /dev/null for Unix, nul for windows</p>
<dt><code>cvscfg(tkdiff)</code></p>
<dd> How to start tkdiff. Example sh /usr/local/bin/tkdiff</p>
<dt><code>cvscfg(tmpdir)</code></p>
<dd> Directory in which to do behind-the-scenes checkouts. Usually /tmp or /var/tmp)</dl>
<h3>Debugging</h3>
<dl>
<dt><code>cvscfg(log_classes)</code></p>
<dd> For debugging: C=CVS commands, E=CVS stderr output, F=File creation/deletion, T=Function entry/exit tracing, D=Debugging</p>
<dt><code>cvscfg(logging)</code></p>
<dd> Logging (debugging) on or off</dl>
<h2>Environment Variables</h2>
<p> You should have the CVSROOT environment variable pointing to the location of your CVS repository before you run TkCVS. It will still allow you to work with different repositories within the same session. </p>
<p> If you wish TkCVS to point to a Subversion repository by default, you can set the environment variable SVNROOT. This has no meaning to Subversion itself, but it will clue TkCVS if it&#8217;s started in an un-versioned directory.</p>
<h2>User Configurable Menu Extensions</h2>
<p> It is possible to extend the TkCVS menu by inserting additional commands into the .tkcvs or tkcvs_def.tcl files. These extensions appear on an extra menu to the right of the TkCVS Options menu. </p>
<p> To create new menu entries on the user-defined menu, set the following variables:</p>
<h3>cvsmenu(command)</h3>
<p> Setting a variable with this name to a value like &quot;commandname&quot; causes the CVS command &quot;cvs commandname&quot; to be run when this menu option is selected. For example, the following line: </p>
<dl>
<dt>
<dd>
&nbsp;<wbr>set cvsmenu(update_A)&nbsp;<wbr>&quot;update -A&quot;</dl>
<p> Causes a new menu option titled &quot;update_A&quot; to be added to the user defined menu that will run the command &quot;cvs update -A&quot; on the selected files when it is activated. </p>
<p> (This example command, for versions of CVS later than 1.3, will force an update to the head version of a file, ignoring any sticky tags or versions attached to the file).</p>
<h3>usermenu(command)</h3>
<p> Setting a variable with this name to a value like &quot;commandname&quot; causes the command &quot;commandname&quot; to be run when this menu option is selected. For example, the following line: </p>
<dl>
<dt>
<dd>
&nbsp;<wbr>set usermenu(view)&nbsp;<wbr>&quot;cat&quot;</dl>
<p> Causes a new menu option titled &quot;view&quot; to be added to the User defined menu that will run the command &quot;cat&quot; on the selected files when it is activated. </p>
<p> Any user-defined commands will be passed a list of file names corresponding to the files selected on the directory listing on the main menu as arguments. </p>
<p> The output of the user defined commands will be displayed in a window when the command is finished.</p>
<h2>CVS Modules File</h2>
<p> If you haven&#8217;t put anything in your CVSROOT/modules file, please do so. See the &quot;Administrative Files&quot; section of the CVS manual. Then, you can add comments which TkCVS can use to title the modules and to display them in a tree structure. </p>
<p> The simplest use of TkCVS&#8217;s &quot;#D&quot; directive is to display a meaningful title for the module: </p>
<dl>
<dt>
<dd> #D softproj Software Development Projects</dl>
<dl>
<dt>
<dd> softproj softproj</dl>
<p> A fancier use is to organize the modules into a tree which will mimic their directory nesting in the repository when they appear in the module browser. For example, suppose we have a directory called &quot;chocolate&quot; which is organized like this: </p>
<dl>
<dt>
<dd> chocolate/</dl>
<dl>
<dt>
<dd>
&nbsp;<wbr>truffle/</dl>
<dl>
<dt>
<dd>
&nbsp;<wbr>&nbsp;<wbr>cocoa3/</dl>
<dl>
<dt>
<dd>
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>biter/</dl>
<dl>
<dt>
<dd>
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>sniffer/</dl>
<dl>
<dt>
<dd>
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>snuffler/</dl>
<p> To display its hierarchy, as well as make the deepest directories more accessible by giving them module names, we could put this in the modules file: </p>
<dl>
<dt>
<dd> #D<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>chocolate<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>Top Chocolate
</dl>
<dl>
<dt>
<dd> #D<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>chocolate/truffle<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>Cocoa Level 2
</dl>
<dl>
<dt>
<dd> #D<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>chocolate/truffle/cocoa3<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>Cocoa Level 3
</dl>
<dl>
<dt>
<dd> #D<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>sniffer<tt>&nbsp;<wbr></tt>Chocolate Sniffer
</dl>
<dl>
<dt>
<dd> sniffer<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>chocolate/truffle/cocoa3/sniffer
</dl>
<dl>
<dt>
<dd> #D<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>snuff<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>Chocolate Snuffler
</dl>
<dl>
<dt>
<dd> snuff<tt>&nbsp;<wbr>&nbsp;<wbr></tt>chocolate/truffle/cocoa3/snuffler
</dl>
<dl>
<dt>
<dd> #D<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>biter<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>Chocolate Biter
</dl>
<dl>
<dt>
<dd> biter<tt>&nbsp;<wbr>&nbsp;<wbr></tt>chocolate/truffle/cocoa3/biter
</dl>
<p> When you are installing TkCVS, you may like to add these additional lines to the modules file (remember to check out the modules module from the repository, and then commit it again when you have finished the edits). </p>
<p> These extension lines commence with a &quot;#&quot; character, so CVS interprets them as comments. They can be safely left in the file whether you are using TkCVS or not. </p>
<p> &quot;#M&quot; is equivalent to &quot;#D&quot;. The two had different functions in previous versions of TkCVS, but now both are parsed the same way.</p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-cvs/">cvs</a>(1), <a href="/docs/linux/man/1-svn/">svn</a>(1)</p>
<h2>AUTHOR</h2>
<p> Del (del [at] babel.babel.com.au): Maintenance and Subversion support: Dorothy Robinson </p>
<h2>Index</h2>
