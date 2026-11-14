---
title: "digitaglinktree(1)"
name: "digitaglinktree"
section: "1"
letter: "d"
url: "/docs/linux/man/1-digitaglinktree/"
description: "digitaglinktree – Export tag structure of photos in digikam to the filesystem."
---

<h2>NAME</h2>
<p> digitaglinktree &#8211; Export tag structure of photos in digikam to the filesystem.</p>
<h2>SYNOPSIS</h2>
<p> <code>digitaglinktree </code> </p>
<p> <code>-l</code><i> taglinkdir</i> | <code>-A</code><i> archivedir</i> </p>
<p> <code>-d</code><i> database</i> </p>
<p> <code>[-r</code><i> rootdir]</i> </p>
<p> <code>[-H|-f|-a|-v|-C]</code> </p>
<h2>DESCRIPTION</h2>
<p> <code>digitaglinktree </code> will create a linktree for all photos in a digikam database that have tags set on them. Tags (like eg. &quot;family&quot;, &quot;events&quot;, &#8230;) are used in digikam to create virtual folders containing images that all have one or more tags assigned. Please note: Photos that have no tags at all assigned are silently ignored by this script. The program will not modify or even touch your original photos managed by digikam.<br />
&nbsp;<wbr> </p>
<p> The script can be used in two ways: If you call it using Option -l <i>taglinkdir</i> the script will create the user specified directory <i>taglinkdir</i> and inside this directory it will create sub directories for digikam tags set on the photos. Inside these subdirectories it will finally place symbolic or hard links (see -H) to photos having the tags in question. As a result you will see the tags of your photos as folders and in these folders you will find links to your original photos. </p>
<p> In this way you can access the collection of all images that share a certain tag by changing directory to the folder with the tags name created by this script. This allows you e.g. to run JAlbum a photo album software that needs to find the pictures to be put into a web album in the filesystem because JAlbum cannot access digikams virtual folders directly. </p>
<p> The second way of calling this script is the so called archive-mode by setting option -A <i>archiveDir</i>. </p>
<p> Archive mode is thought for people who want to archive tagged photos independently of digikams root directories and the photos therein. This way you can put your photos and their tag structure in eg. a tar archive and send it to a friend, who can look at the photos via their tag structure. In this mode the script creates the directory given as parameter to -A and in this directory two more subdirectories. One named Photos and a second named Tags. The Photos directory contains hard links to your original photos, and the Tags directory contains a subdirectory for each Tag used by any of your photos. Inside this subdirectory there are links (either symbolic or hard links) to the files in the Photos directory. This way the archive directory needs nearly no additional space on your harddisk and you have an archive that allows you or a friend to easily look at the photos tag structure. </p>
<p> Another benefit from using this script is that you have kind of a backup of your tag settings for all of your photos. The backup is simply the directory structure containing links to the original images that wear the tags. This could become important if for whatever reason the digikam.db file gets corrupted or even lost. </p>
<h2>COMMAND-LINE OPTIONS</h2>
<dl>
<dt><code> -l</code><i> taglinkdir</i></p>
<dd> Parameter <i> taglinkdir</i> denotes a directory in which the tag structure of all your photos stored in rootdir will be exported to by creating subdirectories for each tag and placing symbolic links in these subdirectories that point to the original photo wearing the tags. If calling the script with option -l<i> taglinkDir</i> you also have to specify options -r <i>rootdir</i> as well as -d <i>database</i>. </p>
<dt><code> -A </code><i>archivedirectory</i></p>
<dd> <i>archivedirectory</i> denotes a directory into which the script will export the photos and their tag structure. -A has to be used together with option -r <i>rootdir</i> if using digikam version &lt; 0.10, as well as -d<i> database</i> else the script will terminate. Inside the archive directory the script will create a Photos and a Tags directory. It will put hard links in the Photos directory that point to your original photos. By using hard links you are independent of changes in your digikam root directory but on the other hand you are limited to one filesystem. So the directory given by -r <i>rootdir</i> and the directory specified for -A <i>archivedir</i> have to be one the same filesystem. If using digikam in version &gt;= 0.10 you cannot specify <i>-r rootdir</i> . Instead the root paths of all albums are taken from digikams database directly. However still the requirement holds, that <i>archivedir</i> has to be on the same filesystem like all the root directories containing photos you defined in digikam. If one of digikams root directories is on another filesystem this one will not be processed, since hardlinking the photos inside the Photos directory would not work in this case! The Tags subdirectory will contain links to the files in the Photos directory. This way you have one archive directory that is completely self contained. You can tar it, send it to a friend or just put it somewhere for archivel or backup purposes. Usually only those photos will be archived that have a digikam tag set on them. By using option -C however you can perform a complete archive. See -C for more infos. </p>
<dt><code> -d </code><i>database</i></p>
<dd> <i>database</i> is the complete path including the filename to digikams photo database which usually can be found in digikams root directory. The files name is usually digikam.db . </p>
<dt><code> -r </code><i>rootdir</i></p>
<dd> <i>rootdir</i> denotes the digikam base directory containing all your photos if you are using digikam in a version before 0.10. If you are using digikam 0.10 or newer you must not use this option. If you do it anyway you will see a hint that the option given will be ignored because digikams version 0.10 database contains the root directories of all albums defined in digikam. </p>
<dt><code> -C</code></p>
<dd> When the script is called with option -A <i>archivedir</i> only those photos will be archived (by placing links) in the Photos subdirectory of <i>archivedir</i> that have at least one digikam tag set. By setting option -C all photos will be archived to <i>archivedir</i> no matter if they have a tag set or not. Note: This only changes the contents of the Photos subdirectory not of the Tags subdirectory in the <i>archivedir</i> directory. </p>
<dt><code> -a </code></p>
<dd> By default the script will try to create relative symbolic links from the directory <i>taglinkdir</i> set by option -l to the photo files under <i>rootdir</i> given by option -r. Using this option will result in absolute symbolic links beeing created instead of relative ones. </p>
<dt><code> -H </code></p>
<dd> By default the script will create soft (symbolic) links from the Tag-Tree to the photos. By setting option -H the script will use hard links instead. Please note that hard links can only be created inside one filesystem. So your photos and the Tag tree have to be one the same filesystem. If not you will see a warning about this problem and the script will not run. </p>
<dt><code> -f </code></p>
<dd> In digikam photos can have hierachical tags (tags that have subtags). In this case digitaglinktree would by default add a directory for the tag and a subdirectory for each of the subtags of this tag. By setting <code> -f </code> a subtag is treated like a regular tag just as its parent tag so digitaglinktree will create all subdirectories for tags and subtags at the same level independent of the tag &#8211; subtag hierarchy. </p>
<dt><code> -Y </code></p>
<dd> Create year directory under each tag directory. Year information is taken from &quot;Date taken&quot; in database. </p>
<dt><code> -i </code><i>tag1,..,tagn</i></p>
<dd> <i>tag1,..,tagn</i> Include only images with tags in the list. Use comma as tag separator. Default is &quot;none&quot;. Use &quot;all&quot; to include all tags at once if you really want this. Better try a list with only some tags first to see how long it takes to complete. </p>
<dt><code> -e </code><i>tag1,..,tagn</i></p>
<dd> <i>tag1,..,tagn</i> Exclude images with tags in the list. Use comma as tag separator. Default is &quot;none&quot;. </p>
<dt><code> -M </code><i>level_number</i></p>
<dd> <i>level_number</i> specify the number of directory level. <i>-M</i> specifies that instead of following normal tag hierarchy, it creates a hierarchy combining different tags together and not only within one tag hierarchy (for example combining Places and People tags). You have to add tags to be included by using the option -i (see above). Depending on the level given and the number of tags you have included and how many photos you manage using digikam, this option may take a considerable amount of time (possibly more than one hour) to complete! <i>level_number</i> of &quot;5&quot; seems to be the maximum reasonable level to start with in this mode. Options -A -C -a -H -f not tested with this option! </p>
<dt><code> -V </code></p>
<dd> Verbose mode. </p>
<dt><code> -v </code></p>
<dd> Prints the scripts version number and exits. </p>
</dl>
<h2>CONFIGURATION</h2>
<p> By default this script will run with all photo databases created by digikam version 0.10 as well as older version like 0.9 and 0.8. If you still have digikam version 0.7 then you have to reconfigure the script itself. </p>
<p> You have to reconfigure the script by setting the path to the sqlite binary that is used by the script to query the digikam database digikam.db. Since very old digikam version use sqlite in version 2, but later digikam versions need sqlite version 3 you have to take care to install the correct version of sqlite for the installed digikam version and to set the path to the correct sqlite executable in the scripts head: </p>
<p> Choose </p>
<p> $SQLITE=&quot;/usr/bin/sqlite3&quot;; </p>
<p> for digikam version 0.8x and 0.9x and 0.10x </p>
<p> $SQLITE=&quot;/usr/bin/sqlite&quot;; </p>
<p> for digikam version 0.7x. </p>
<h2>EXAMPLE</h2>
<p> A call to digitaglinktree is shown below: </p>
<p> digiTagLinktree -l /home/user/tags<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>-d&nbsp;<wbr>/home/user/photos/digikam.db </p>
<p> In this example we assume that you are running digikam version 0.10 or higher so that no option -r was used to specify the photo root dir. Instead this information will automatically be fetched from digikams database. </p>
<p> In case you want to run the script on a digikam database that was created by digikam version 0.9 or earlier you have to use -r to specify the root directory where you keep all your photos that are managed by digikam: </p>
<p> digiTagLinktree -l /home/user/tags<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>-d&nbsp;<wbr>/home/user/photos/digikam.db </p>
<p> In this example digikams photo root denoted by -r is /home/user/photos. </p>
<p> Option -l /home/user/tags tells the script that all the subdirectories and symbolic links will be placed in the directory /home/user/tags. The folder was chosen so that the tags-directory is not under digikams photo root. You may put the tags folder inside digikams photoroot but this is not the preferred method. Because the link directory contains only links this tag structure does hardly need any additional space on your harddisk. </p>
<p> digiTagLinktree -r /home/user/photos -l /home/user/tags <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt> -d /home/user/photos/digikam.db</p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>-i People,Place<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>-M 2<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>-Y </p>
<p> In this example if you have an image with the tags People/me, Place/home from 1970 it will create the following directory (link to the image under _all directory) </p>
<p> /home/user/tags/Date/1970/_all/ </p>
<p> /home/user/tags/Date/1970/People/me/_all/ </p>
<p> /home/user/tags/Date/1970/People/me/Place/home/_all/ </p>
<p> /home/user/tags/Date/1970/Place/home/_all/ </p>
<p> /home/user/tags/Date/1970/Place/home/People/me/_all/ </p>
<p> same starting with /Place &#8230; same starting with /People &#8230; </p>
<h2>AUTHORS</h2>
<p> <code>digitaglinktree</code> was written by Rainer Krienke &lt;krienke at uni-koblenz.de&gt; </p>
<h2>Index</h2>
