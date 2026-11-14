---
title: "dar_manager(1)"
name: "dar_manager"
section: "1"
letter: "d"
url: "/docs/linux/man/1-dar_manager/"
description: "dar_manager – compiles several archives contents in a database to ease file restoration"
---

<h2 class="name">NAME</h2>
<p> dar_manager &#8211; compiles several archives contents in a database to ease file restoration </p>
<h2>SYNOPSIS</h2>
<p> dar_manager [-v] -C [&lt;path&gt;/]&lt;database&gt; </p>
<p> dar_manager [-v] -B [&lt;path&gt;/]&lt;database&gt; -A [&lt;path&gt;/]&lt;basename&gt; [-9 &lt;min-digits&gt;] [[&lt;path&gt;/]&lt;archive_basename&gt;] </p>
<p> dar_manager [-v] -B [&lt;path&gt;/]&lt;database&gt; -l </p>
<p> dar_manager [-v] -B [&lt;path&gt;/]&lt;database&gt; -D &lt;number&gt;[-&lt;number&gt;] </p>
<p> dar_manager [-v] -B [&lt;path&gt;/]&lt;database&gt; -b &lt;number&gt; &lt;new_archive_basename&gt; </p>
<p> dar_manager [-v] -B [&lt;path&gt;/]&lt;database&gt; -p &lt;number&gt; &lt;path&gt; </p>
<p> dar_manager [-v] -B [&lt;path&gt;/]&lt;database&gt; -o [list of options to pass to dar] </p>
<p> dar_manager [-v] -B [&lt;path&gt;/]&lt;database&gt; -d [&lt;path to dar command&gt;] </p>
<p> dar_manager [-v] -B [&lt;path&gt;/]&lt;database&gt; [-N] [-k] [-w &lt;date&gt;] [-e &quot;&lt;extra options to dar&gt;&quot;] -r [list of files to restore] </p>
<p> dar_manager [-v] -B [&lt;path&gt;/]&lt;database&gt; -u &lt;number&gt; </p>
<p> dar_manager [-v] -B [&lt;path&gt;/]&lt;database&gt; -f file </p>
<p> dar_manager [-v] -B [&lt;path&gt;/]&lt;database&gt; -s </p>
<p> dar_manager [-v] -B [&lt;path&gt;/]&lt;database&gt; -m &lt;number&gt; &lt;number&gt; </p>
<p> dar_manager [-v] -B [&lt;path&gt;/]&lt;database&gt; -c </p>
<p> dar_manager [-v] -B [&lt;path&gt;/]&lt;database&gt; -i </p>
<p> dar_manager [-v] -B [&lt;path&gt;/]&lt;database&gt; -@ { &lt;filename&gt; | &quot;-&quot; } </p>
<p> dar_manager -h </p>
<p> dar_manager -V </p>
<h2>DESCRIPTION</h2>
<p> <code>dar_manager</code> is part of the Disk Archive suite. Its purpose is to simplify the restoration of a set of few files present in many backup, full or differential. This is achieved by gathering the catalogue of each archive (this has to be done once). At any time you just have to give the relative path to the files you want to restore, dar_manager will call dar with the proper options and restore the last version of each file (or the last version before given date). Note that dar_manager is to be used when you have remove some files by accident some time ago and wish to recover them. It thus not adapted to restore the state a directory tree had at a given time, in particular when some files have to be removed. For that you must use dar directly with the corresponding archive to the date for which you wish to restore the state. </p>
<p> you can restore any file by hand without <code>dar_manager</code> , but if you make a lot of differential backup, you may spend many time to find the archive that contains the last version of your file, as dar will not save it if it has not changed since previous backup. <code>dar_manager</code> simplify the process by looking in its internal database, built from archive &quot;catalogues&quot;.</p>
<h2>OPTIONS</h2>
<dl>
<dt>-C, &#8211;create [&lt;path&gt;/]&lt;database&gt;</p>
<dd> creates an empty database that will collect information about several archives. The &lt;database&gt; is a filename that is required for -B option. To destroy a &lt;database&gt; just remove the file.</p>
<dt>-B, &#8211;base [&lt;path&gt;/]&lt;database&gt;</p>
<dd> specify the database to read or modify. The &lt;database&gt; file must exist, and have a database structure (see -C option).</p>
<dt>-i, &#8211;interactive</p>
<dd> use a keyboard interactive text menu to do operations on the given database. So you may avoid reading the other options described in this manual page, if you wish, and just use the interactive option. You will however always have to create an empty database (-C option) and restore files manually (-r option).</p>
<dt>-A, &#8211;add [&lt;path&gt;/]&lt;basename&gt; [ [&lt;path&gt;/]&lt;archive_basename&gt;]</p>
<dd> add an archive to the database. An isolated catalogue can also be used only if it has been produced by dar version 1.2.0 or above. Why ? Because, an isolated catalogue produced by older version will always tell that no files are saved in the archive of reference, in that case the solution is to provide the archive itself as argument. An optional second argument is the basename of the archive if it is different from the first argument (need for extraction of files). For example you could have an isolated catalogue in first argument and the basename of the original archive (where is stored the data) as second argument. By default,</p>
<dt>-9, &#8211;min-digits &lt;num&gt;</p>
<dd> the slice number zeroed padding to use to get the slices filename (for more details see dar man page at this same option) <code>dar_manager</code> will look for an archive of reference in the command line used to create each archive, but in some cases, it may be necessary to specify the archive name (for example if you&#8217;ve changed its name).</p>
<dt>-l, &#8211;list</p>
<dd> displays the information about the archives compiled in the database. In particular, a number is given to each archive, which is required to some other option to design a particular archive within the database. Nothing avoids you to feed the database with several archive of the same basename ! You will just have to guess which one is asked under this name. :-)</p>
<dt>-D, &#8211;delete &lt;number&gt;[-&lt;number&gt;]</p>
<dd> removes an archive (or a range of archive) from the database. The number of the archive (or the min and max number or the archive range) is correspond to those given by the -l option. Note that all archive number greater than the one(s) to be delete will be decremented to keep continuous numbering of the archive inside the database. If a single number is given (not a range), it may be also a negative number, by which it means counting from the end. For example, -1 means the last archive of the base, -2 the penultimate, etc.</p>
<dt>-b, &#8211;base &lt;number&gt; &lt;new_archive_basename&gt;</p>
<dd> this option allows you to rename the archive basename (used when restoring files from it). Here too, the number may be also a negative number.</p>
<dt>-p, &#8211;path &lt;number&gt; &lt;path&gt;</p>
<dd> this option allows you to change the location of a given archive (used when restoring files from it). Here too, a negative number is allowed.</p>
<dt>-o, &#8211;options [list of option to pass to dar]</p>
<dd> Specify the option to use when calling dar. Each call erases the previous setting. Possible <code>dar</code> options are all the available ones except &quot;-x&quot; and simple arguments (the [list of path]) which will be added by <code>dar_manager</code> itself.</p>
<dt>-d, &#8211;dar [&lt;path&gt;]</p>
<dd> Set the path to dar. If no argument is given, dar is expected to be located in the PATH</p>
<dt>-r, &#8211;restore [list of files or directories to restore]</p>
<dd> <code>dar_manager</code> will restore all (an only) the given files or directories, in their latest recorded status, or before the date give thanks to the -e option. If a directory is given all subfiles and subdirectories are restored recursively in it. You can filter out some files from this recursion thanks to dar usual filtering option (see dar man page) you can provide beside -r using the -e option (see below). Dar_manager lead dar to remove any file, if a file is stored as having been removed at date requested for restoration, it is simply not restored. Thus if you restore in an empty directory you will get all the files and directories you provided to dar_manager in the state they have at the date you asked. File that did not existed at that time will not be restored. However you can restore over an existing installation, dar will then warn you before overwriting files (see -w and -n options for dar) but will still not remove files that were recorded removed from a previous archive of reference. Note that files listed after -r option, must never have an absolute path. They will be restored under the directory specified with -R option of dar (passed to dar using -o or -e options), or by default, under the current directory.</p>
<dt>-w, &#8211;when &lt;date&gt;</p>
<dd> alters the -r option behavior: still restores the files in the most recent version available but only before the given date (versions of more recent dates are ignored). The &lt;date&gt; must respect the following format [ [ [year/]month/]day-]hour:minute[:second]. For example &quot;22:10&quot; for 10 PM past 10 or the current day, &quot;7-22:10&quot; for 10 PM past 10 the 7th of the current month, &quot;3/07-22:10&quot; for the 7th of march at 22:10 of the current year, &quot;2002/03/31-14:00:00&quot; the date of the first dar&#8217;s release ;-). The given date must be in the past, of course, and is compared to the &quot;last modification&quot; date of the saved files and not to the date at which archives have been done. Thus if a file has been changed long ago but saved in a recent (full) archive, it will be elected for restoration even for dates older than the creation of the archive. In the other way, a file saved long time ago with a mtime that was set to a date in the future will not be elected for restoration when giving the date at which was done the archive.</p>
<dt>-e, &#8211;extra &lt;options&gt;</p>
<dd> pass some more options to dar. While the -o options takes all that follows on the command line as argument to pass to dar and write these in the database, the -e option does not alter the database and has only one argument. In other words, if you need to pass several options to dar through the use of the -e option, you need to use quotes (simple quotes &#8216; or double quotes &quot;) to enclose these options. Example:</dl>
<dl>
<dt>
<dd>
<dl>
<dt>
<dd> dar_manager -B database.dmd -e &quot;-w -v -p -b -r -H 1&quot; -r some/files</dl>
<p> while using -o option you must not use quotes: </p>
<dl>
<dt>
<dd> dar_manager -B database.dmd -o -w -v -p -b -r -H 1</dl>
</dl>
<dl>
<dt>-u, &#8211;used &lt;number&gt;</p>
<dd> list the files that the given archive owns as last version available. Thus when no file is listed, the given archive is no more useful in database, and can be removed safely (-D option). If &lt;number&gt; is zero, all available file are listed, the status provided for each file present in the database is the most recent status. A negative number is allowed for this option (see -D option for details).</p>
<dt>-f, &#8211;file &lt;file&gt;</p>
<dd> displays in which archive the given file is saved, and what are the modification date (mtime) and change date (ctime).</p>
<dt>-s, &#8211;stats</p>
<dd> show the number of most recent files by archive. This helps to determine which archive can be safely removed from the database.</p>
<dt>-m, &#8211;move &lt;number&gt; &lt;number&gt;</p>
<dd> changes the order of archives in the database. The first number is the number of the archive to move, while the second is the place where it must be shifted to. </p>
<p> Archive order is important: An old archive must have a smaller index than a recent archive. If you add archive to a database in the order they have been created all should be fine. Else if a file has a more recent version in an archive which index is smaller, a warning will be issued (unless -ai option is used). This can occur if by mistake you added an archive to the database in the wrong order (old archive added after a recent one), in that case simply using the -m option will let you fix this mistake. If instead the problem is relative to a single file (or a small set of file), you should wonder why this file has its modification date altered in a way that it pretends to be older than its really is. Checking for the signs of a rootkit may be a good idea.</p>
<dt>-c, &#8211;check</p>
<dd> check the database consistency, in particular the date ordering is verified and warning are issued for each file having more recent version located in an archive with a smaller index inside the database. -ai option makes -c option useless.</p>
<dt>-N, &#8211;ignore-options-in-base</p>
<dd> Do not use the options stored in database when calling dar for restoration. This option is only useful while restoring files from dar_manager, either directly (-r option) or using a batch file (-@ option, see below).</p>
<dt>-k, &#8211;ignore-when-removed</p>
<dd> By default, dar_manager does not ask dar to restore file that have been removed at the requested date (or in the latest state available). This is useful for example to restore a directory in the state it has at a given date (only files that existed at that time are restored). However when you want to restore a file that has been destroyed by accident, you need to use -k option so you don&#8217;t have to determine at which date that file existed to be be able to ask dar_manager to restore that file in the state it had before that date. In other words, -k option gives a behavior of dar_manager backward compatible with dar_manager released beside version 2.3.x of dar.</p>
<dt>-ai, &#8211;alter=ignore-order</p>
<dd> avoid dar_manager to issue a warning for each file not following a chronological order of modification date when the archive number in the database is growing.</p>
<dt>-@, &#8211;batch &lt;filename&gt;</p>
<dd> allows you to do several operations on a given database. All operations are defined in the provided &lt;filename&gt; and refer to the same database as defined by the -B switch on command line. This batch file, must thus not contain neither -B, -C, -i or -ai option (-ai are global to the batch operation). The batch file expected layout is one command per line, thus several arguments (like -l -v for example) may take place on a given line of the file (-v can be found both on command line for verbose output about the batch operation steps, as well as inside the batch file for verbose output of a particular batched command). Arguments are separated by spaces or tabs, other characters are passed as-is. In consequence, you should only need to use quotes (using &quot; or &#8216;) if you intend to use an argument containing space. Last, comments may be placed on any line beginning by a hash character (#).</p>
<dt>-Q</p>
<dd> Do not display any message on stderr when not launched from a terminal (for example when launched from an at job or crontab). Remains that any question to the user will be assumed a &#8216;no&#8217; answer, which most of the time will abort the program.</p>
<dt>-v, &#8211;verbose</p>
<dd> displays additional information about what it is doing.</p>
<dt>-h, &#8211;help</p>
<dd> display help usage</p>
<dt>-V, &#8211;version</p>
<dd> display software version </p>
</dl>
<h2>EXIT CODES</h2>
<p> <code>dar_manager</code> exits with the following code:</p>
<dl>
<dt>0</p>
<dd> Operation successful.</p>
<dt>1</p>
<dd> see dar manual page for signification</p>
<dt>2</p>
<dd> see dar manual page for signification</p>
<dt>3</p>
<dd> see dar manual page for signification</p>
<dt>5</p>
<dd> see dar manual page for signification</p>
<dt>7</p>
<dd> see dar manual page for signification</p>
<dt>8</p>
<dd> see dar manual page for signification</p>
<dt>11 and above</p>
<dd> <code>dar</code><br />
&nbsp;<wbr>called from dar_manager has exited with non zero status. Subtract 10 to this exit code to get dar&#8217;s exit code. </p>
</dl>
<h2>SIGNALS</h2>
<p> dar_manager acts like dar (see dar man page for list of signals), upon certain signal reception dar aborts cleanly </p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-dar/">dar</a>(1), <a href="/docs/linux/man/1-dar_xform/">dar_xform</a>(1), <a href="/docs/linux/man/1-dar_slave/">dar_slave</a>(1), <a href="/docs/linux/man/1-dar_cp/">dar_cp</a>(1), <a href="/docs/linux/man/1-dar_split/">dar_split</a>(1) </p>
<h2>LIMITATIONS</h2>
<p> at most 65534 archives can be compiled in a given database, which should be enough for most users. Dar_manager does not support encrypted archives for now and archive cannot neither be encrypted. See the FAQ for a workaround. </p>
<h2>KNOWN BUGS</h2>
<p> <a rel="nofollow" href="http://sourceforge.net/p/dar/bugs/">http://sourceforge.net/p/dar/bugs/</a> </p>
<h2>AUTHOR</h2>
<pre>
<a rel="nofollow" href="http://dar.linux.free.fr/">http://dar.linux.free.fr/</a>
Denis Corbin
France
Europe
</pre>
<h2>Index</h2>
