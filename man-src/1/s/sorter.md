---
title: "sorter(1)"
name: "sorter"
section: "1"
letter: "s"
url: "/docs/linux/man/1-sorter/"
description: "sorter – Sort files in an image into categories based on file type"
---

<h2 class="name">NAME</h2>
<p> sorter &#8211; Sort files in an image into categories based on file type </p>
<h2>SYNOPSIS</h2>
<p> <code>[-b</code> <i>size</i> <code>] [-e] [-E] [-h] [-l] [-md5] [-s] [-sha1] [-U] [-v] [-V] [-a</code> <i>hash_alert</i> <code>] [-c </code> <i>config</i> <code>] [-C </code> <i>config</i> <code>] [-d</code> <i>dir</i> <code>] [-m</code> <i>mnt</i> <code>] [-n</code> <i>nsrl_db</i> <code>] [-x</code> <i>hash_exclude</i> <code>] [-i imgtype] [-o imgoffset] [-f fstype] image [image] [meta_addr]</code></p>
<h2>DESCRIPTION</h2>
<p> <code>sorter</code> is a Perl script that analyzes a file system to organize the allocated and unallocated files by file type. It runs the &#8216;file&#8217; command on each file and organizes the files according to the rules in configuration files. Extension mismatching is also done to identify &#8216;hidden&#8217; files. One can also provide hash databases for files that are known to be good and can be ignored and files that are known to be bad and should be alerted. </p>
<p> By default, the program uses the configuration files in the directory where The Sleuth Kit was installed. Those can be overruled with run-time options. There is a standard configuration file for all file system types and then a specific one for a given operating system. </p>
<h2>ARGUMENTS</h2>
<p> The required arguments are as follows. This will analyze one or more images and either save the results in the &#8216;-d&#8217; directory or list the results to STDOUT (if &#8216;-l&#8217; is given). </p>
<dl>
<dt>-d dir</p>
<dd> Specify the location of where all files should be written. This includes the index files and subdirectories if the &#8216;-s&#8217; flag is given. This MUST be given, unless the &#8216;-l&#8217; list flag is given.</p>
<dt>-l</p>
<dd> List information to STDOUT (no files are ever written). This is useful for Incident Response, with the use of &#8216;netcat&#8217;. This cannot be used if &#8216;-d&#8217; is used.</p>
<dt>image [images]</p>
<dd> The disk or partition image to read, whose format is given with &#8216;-i&#8217;. Multiple image file names can be given if the image is split into multiple segments. If only one image file is given, and its name is the first in a sequence (e.g., as indicated by ending in &#8216;.001&#8217;), subsequent image segments will be included automatically. </p>
</dl>
<p> The options are as follows:</p>
<dl>
<dt>-f fstype</p>
<dd> Specify the file system type of the image(s). This is the same type that The Sleuth Kit uses. </p>
<dt>-i imgtype</p>
<dd> Specify the image type in which the file system is located. This is the same type that The Sleuth Kit uses. </p>
<dt>-o imgoffset</p>
<dd> Specify the sector offset from the beginning of the image to the start of the file system. </p>
<dt>-b size</p>
<dd> Specify the minimum size of file to process. All files less than this size will be ignored. </p>
<dt>-c config</p>
<dd> Specify the location of an additional configuration file. This file will be loaded in addition to the standard ones in the install directory. These settings will have priority over the standard files.</p>
<dt>-C config</p>
<dd> Specify the location of the ONLY configuration file. The standard config files will not be loaded if this option is given. For example, in the &#8216;share/sort&#8217; directory there is a file called &#8216;images.sort&#8217;. This file contains only rules about graphic images. If it is specified with -C, then only images will be saved about the image.</p>
<dt>-m mnt</p>
<dd> Specify the mounting point of the image being analyzed. This is only for cosmetic reasons. When the entries in the output files are written, the files will have a the full path instead of just the relative path. If this is given, then only one image can be given.</p>
<dt>-a hash_alert</p>
<dd> Specify the location a hash database with entries of known &#8216;bad&#8217; files. If any file is found with an MD5 hash value in this database, it will be placed in a special alert file. This database must have been indexed for MD5 using &#8216;hfind&#8217; in The Sleuth Kit before it is used by sorter.</p>
<dt>-n nsrl_db</p>
<dd> Specify the location of the NIST National Software Reference Library (NSRL) database (<a rel="nofollow" href="http://www.nsrl.nist.org">www.nsrl.nist.org</a>). Any file found in the NSRL will be ignored and not placed into a category. The database must be indexed for MD5 with &#8216;hfind&#8217; in The Sleuth Kit before it is used by sorter. The database file is currently called &#8216;NSRLFile.txt&#8217;.</p>
<dt>-x hash_exclude</p>
<dd> Specify the location a hash database with entries of known &#8216;good&#8217; files. If any file is found with an MD5 hash value in this database, it will be ignored and not processed or saved to the category files. This database must have been indexed for MD5 using &#8216;hfind&#8217; in The Sleuth Kit before it is used by sorter.</p>
<dt>-e</p>
<dd> Perform extension mismatch checks on (no category index files are generated)</p>
<dt>-U</p>
<dd> Do no save data about unknown file types. By default, an &#8216;unknown&#8217; file is created for files where the &#8216;file&#8217; output is not known. This allows one to refine their configuration. If this is not desired, use this flag.</p>
<dt>-h</p>
<dd> Create category files in HTML</p>
<dt>-md5</p>
<dd> Calculate the MD5 value for each file and save it in the category file. This will be done automatically when any of the databases are given.</p>
<dt>-sha1</p>
<dd> Calculate the SHA-1 value for each file and save it in the category file.</p>
<dt>-s</p>
<dd> Save the actual file content to sub-directories in the directory specified by &#8216;-d&#8217;. For example, all JPG and GIF files would actually be saved in the &#8216;images&#8217; directory. If &#8216;-h&#8217; is also given, thumbnails of graphic images are also created.</p>
<dt>-v</p>
<dd> Display verbose information</p>
<dt>-V</p>
<dd> Display version.</p>
<dt>[meta_addr]</p>
<dd> The meta data address of the directory to start with. By default, the root directory is used. If this is given, then only one image can be given. </p>
</dl>
<h2>HIGH-LEVEL OVERVIEW OF PROCESS</h2>
<p> <code>sorter</code> is a Perl script that interacts with other The Sleuth Kit tools. It starts by reading the configuration files from the installation directory. There is a general configuration file and a specific one for each operating system. The specific one is determined from the &#8216;-f&#8217; flag. Each configuration file contains rules for processing the output of the &#8216;file&#8217; command. One type of line identifies which category (i.e. &#8216;images&#8217;) a given &#8216;file&#8217; output belongs to (i.e. &#8216;image data&#8217;) (using regular expressions). Another rule shows the file extensions (i.e. .txt) that belong to a &#8216;file&#8217; output (i.e. ASCII(.*?)text). See the Rules section below. </p>
<p> The program then runs the &#8216;fls&#8217; tool in The Sleuth Kit to identify the files in the file system image. Each identified file is viewed using the &#8216;icat&#8217; tool. If a hash database is given, the hash of the file is calculated and looked up. If it is found in an &#8216;alert&#8217; database, then it is added to a special &#8216;alert.txt&#8217; file. If it is found in the NSRL or &#8216;exclude&#8217; database, then it is ignored as a known good file. Excluded files are recorded in an &#8216;exclude&#8217; file for future reference but it is not saved in the category files. </p>
<p> The &#8216;file&#8217; command is then run to identify the file type (based on header information). The configuration file rules are used to identify which category it belongs to. An entry is added to the corresponding category file (in the &#8216;-d dir&#8217; directory). If the &#8216;-s&#8217; flag is given, then a copy of the file is saved in a subdirectory of the same name as the category. If the HTML format is used, then hyper-links will allow one to easily view saved files and view what is in each category. </p>
<p> Files that do not have a category are recorded in the &#8216;unknown&#8217; category and the &#8216;data&#8217; category. &#8216;data&#8217; is for files with a structure that &#8216;file&#8217; does not know and &#8216;unknown&#8217; is for files with a structure that &#8216;file&#8217; knows about. These are saved for future reference, but the unknown category can be ignored by using the &#8216;-U&#8217; flag. </p>
<p> A copy of the files can be saved by using the &#8216;-s&#8217; flag. If so, then the files are saved in a subdirectory that is named with the category name. Each file is named using the file system image name followed by the meta data address and the original file extension. The category index file can be used to translate the actual name to the saved name. The HTML format makes viewing easier as there are links to each file from the category index file. </p>
<p> The program will also consult the rules about the file extension. If the file has an extension at the end of it (anything after a &#8216;.&#8217;), it will be compared to the rules. If the extension is not found in the rules as a valid extension for the file type, it will be added to the file of &#8216;mismatch&#8217;. If the file does not have an extension it will not be entered even if the file type has valid extensions. This check is done even if the file is found in one of the known good hash databases. If it is found in one of those, it will be added to a special file. Files of type &#8216;data&#8217; have no extension checks done by default (as they have an unknown structure). </p>
<p> The program repeats the above procedures using the output of the &#8216;ils&#8217; command as well. This allows &#8216;sorter&#8217; to examine the contents of unallocated files that still have pointers to the data units (not all file systems will produce data from this step). </p>
<h2>CONFIGURATION FILES</h2>
<p> Configuration files are used to define what file types belong in which categories and what extensions belong to what file types. Configuration files are distributed with the &#8216;sorter&#8217; tool and are located in the installation directory in the &#8216;share/sorter&#8217; directory. </p>
<p> The &#8216;default.sort&#8217; file is used by any file system type. It contains entries for common file types. A specific operating system file also exists, which is useful for extensions that are specific to a given OS. By default, the default file and the OS specific one will be used. Using the &#8216;-c&#8217; flag, an additional file can be used. If the &#8216;-C&#8217; flag is used, then only the supplied configuration file is used. </p>
<p> There are two rule types in the configuration files. Each rule starts with a header that specifies which rule type it is (category or ext). Both rule types have two additional columns that can be separated by any white space. </p>
<p> The category rule has the category name as the second column and a Perl regular expression in the third column. The category name can not have any spaces in it and can only be letters and numbers. The regular expression is used to examine the output of &#8216;file&#8217;. The regular expression will be used case insensitive. More than one rule can exist for a category, but only one category can exist for a given file output. For example: </p>
<p> This saves all file output with &#8216;image data&#8217; anywhere in it to the &#8216;images&#8217; category:<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;category&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;images&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;image data </p>
<p> This saves all file output that has &#8216;ASCII&#8217; followed by anything and then &#8216;text&#8217; to be saved to the &#8216;text&#8217; category:<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;category&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;text&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;ASCII(.*?)text </p>
<p> This saves all file output that is just &#8216;data&#8217; to the &#8216;data&#8217; category (the ^ and $ define the boundaries in Perl). The &#8216;data&#8217; value is common in the output of file for unknown binary data.<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;category&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;data&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;^data? </p>
<p> There is a special category of &#8216;ignore&#8217; that is used to skip over files of this type. This is mainly a time and space saver. </p>
<p> The extension rule is similar except that the second column has the value extensions for the file output. Multiple rules can exist for the same file type. The comparison will be done case insensitive. If no extension is valid for the file type, a rule does not need to be made. That is already assumed. </p>
<p> For example, the ASCII is used for several file extensions so the following rules could exist: </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;ext&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;txt,log&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;ASCII(.*?)text<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;ext&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;c,cpp,h,js&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;ASCII(.*?)text </p>
<p> Please email me any rules that you find useful for standard investigations and I will incorporate them into future releases (carrier at sleuthkit dot org). </p>
<h2>EXAMPLES</h2>
<p> To run sorter with no hash databases, the following can be used: </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;#&nbsp;sorter -f ntfs -d data/sorter images/hda1.dd <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt></p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;#&nbsp;sorter -d data/sorter images/hda1.dd </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;#&nbsp;sorter -i raw -f ntfs -o 63 -d data/sorter images/hda.dd </p>
<p> To include the NSRL, an exclude, and an alert hash database: </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;#&nbsp;sorter -f ntfs -d data/sorter -a&nbsp;/usr/hash/rootkit.db&nbsp;<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>&nbsp;<wbr>&nbsp;-x&nbsp;/usr/hash/win2k.db -n&nbsp;/usr/hash/nsrl/NSRLFile.txt&nbsp;<wbr>&nbsp;<wbr>&nbsp;images/hda1.dd</p>
<p> To just identify images using the supplied &#8216;images.sort&#8217; file: </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;#&nbsp;sorter -f ntfs -C&nbsp;/usr/local/sleuthkit/share/sort/images.sort&nbsp;<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>&nbsp;<wbr>&nbsp;-d data/sorter -h -s images/hda1.dd</p>
<h2>REQUIREMENTS</h2>
<p> The NIST National Software Reference Library (NSRL) can be found at <a rel="nofollow" href="http://www.nsrl.nist.gov">www.nsrl.nist.gov</a>. </p>
<h2>LICENSE</h2>
<p> Distributed under the Common Public License, found in the <i>cpl1.0.txt</i> file in the The Sleuth Kit licenses directory. </p>
<h2>AUTHOR</h2>
<p> Brian Carrier &lt;carrier at sleuthkit dogt org&gt; </p>
<p> Send documentation updates to &lt;doc-updates at sleuthkit dot org&gt; </p>
<h2>Index</h2>
