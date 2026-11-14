---
title: "atool(1)"
name: "atool"
section: "1"
letter: "a"
url: "/docs/linux/man/1-atool/"
description: "atool – A script for managing file archives of various types"
---

<h2 class="name">NAME</h2>
<p> atool &#8211; A script for managing file archives of various types </p>
<h2>SYNOPSIS</h2>
<p> <code>atool</code> [<i>OPTION</i>]&#8230;<i> ARCHIVE </i>[<i>FILE</i>]&#8230;<br />
 <code>aunpack</code> [<i>OPTION</i>]&#8230;<i> ARCHIVE </i>[<i>FILE</i>]&#8230;<br />
 <code>apack</code> [<i>OPTION</i>]&#8230;<i> ARCHIVE </i>[<i>FILE</i>]&#8230;<br />
 <code>als</code> [<i>OPTION</i>]&#8230;<i> ARCHIVE </i>[<i>FILE</i>]&#8230;<br />
 <code>acat</code> [<i>OPTION</i>]&#8230;<i> ARCHIVE </i>[<i>FILE</i>]&#8230;<br />
 <code>adiff</code> [<i>OPTION</i>]&#8230;<i> ARCHIVE </i><i>ARCHIVE</i><br />
 <code>arepack</code> [<i>OPTION</i>]&#8230;<i> OLD-ARCHIVE </i><i>NEW-ARCHIVE</i></p>
<h2>DESCRIPTION</h2>
<p> This manual page document describes the <code>atool</code> commands. These commands are used for managing file archives of various types, such as tar and Zip archives. Each command can be executed individually or by giving the appropriate options to <code>atool</code> (see <code>OPTIONS</code> below). </p>
<p> <code>aunpack</code> extracts files from an archive. Often one wants to extract all files in an archive to a single subdirectory. However, some archives contain multiple files in their root directories. The aunpack program overcomes this problem by first extracting files to a unique (temporary) directory, and then moving its contents back if possible. This also prevents local files from being overwritten by mistake. </p>
<p> <code>apack</code> creates archives (or compresses files). If no file arguments are specified, filenames to add are read from standard in. </p>
<p> <code>als</code> lists files in an archive. </p>
<p> <code>acat</code> extracts files in an archive to standard out. </p>
<p> <code>adiff</code> generates a diff between two archives using <a href="/docs/linux/man/1-diff/">diff</a>(1). </p>
<p> <code>arepack</code> repacks archives to a different format. It does this by first extracting all files of the old archive into a temporary directory, then packing all files extracted to that directory to the new archive. Use the &#8211;each (-e) option in combination with &#8211;format (-F) to repack multiple archives using a single invocation of atool. Note that arepack will not remove the old archive. </p>
<p> Unless the <code>&#8211;format</code> (<code>-F</code>) option is provided, the archive format is determined by the archive file extension. I.e. an extension &quot;.tar.gz&quot; or &quot;.tgz&quot; means tar+gzip format. Note that the extensions are checked in the order listed in the section <code>ARCHIVE TYPES</code> below, which is why a file with extension &quot;.tar.gz&quot; is considered to a be tar+gzip archive, not a gzip compressed file.</p>
<h2>OPTIONS</h2>
<p> These programs follow the usual GNU command line syntax, with long options starting with two dashes (`-&#8216;). A summary of options is included below.</p>
<dl>
<dt><code>-l, &#8211;list</code></p>
<dd> List files in archive. This option is automatically assumed when <code>als</code> is executed.</p>
<dt><code>-x, &#8211;extract</code></p>
<dd> Extract files from archive. This option is automatically assumed when <code>aunpack</code> is executed.</p>
<dt><code>-X, &#8211;extract-to</code>=<i>PATH</i></p>
<dd> Extract files from archive to the specified directory. When unpacking compressed files, PATH may refer to either a filename or an existing directory.</p>
<dt><code>-a, &#8211;add</code></p>
<dd> Create archive. This option is automatically assumed when <code>apack</code> is executed.</p>
<dt><code>-c, &#8211;cat</code></p>
<dd> Extract a file from archive to standard out (displaying it on screen). This option is automatically assumed when <code>acat</code> is executed.</p>
<dt><code>-d, &#8211;diff</code></p>
<dd> Extract two archives and use <a href="/docs/linux/man/1-diff/">diff</a>(1) to generate differencies between them. This option is automatically assumed when <code>adiff</code> is executed.</p>
<dt><code>-e, &#8211;each</code></p>
<dd> For each argument, execute the specified command. This can be used to quickly extract, list or create multiple archives (see <code>EXAMPLES</code> below). This option can not be used with the cat command.</p>
<dt><code>-F, &#8211;format</code>=<i>EXTENSION</i></p>
<dd> Specify archive format manually (see <code>ARCHIVE TYPES</code> below).</p>
<dt><code>-S, &#8211;simulate</code></p>
<dd> Run atool in simulation mode. No changes to the filesystem (i.e. writes) will be made, and all commands that would be executed are displayed instead. This option can&#8217;t be combined with <code>&#8211;explain</code> (since it implies that already). </p>
<p> Note that it is not guaranteed that the commands printed in simulation mode will be the same as those executed in non- simulation mode. This is because some operations depend on what files archives contain, and atool can at this time only determine that by extracting archives.</p>
<dt><code>-E, &#8211;explain</code></p>
<dd> Display commands executed by atool. This option can&#8217;t be combined with <code>&#8211;simulate</code>.</p>
<dt><code>-p, &#8211;page</code></p>
<dd> Run output through a pager, usually <code>pager</code> unless the environment variable <code>PAGER</code> is set.</p>
<dt><code>-f, &#8211;force</code></p>
<dd> When extracting from files, allow overwriting of local files. When creating an archive, allow the archive file to be overwritten if it already exists. Note that it is possible to add files to existing RAR and Zip archives (this is not possible for many other formats).</p>
<dt><code>-D, &#8211;subdir</code></p>
<dd> When extracting archives, always create a new directory for the archive even if the archive only contains one file in its root directory.</p>
<dt><code>-0, &#8211;null</code></p>
<dd> If no file arguments are specified when creating or adding files to archives, the list of files will be read from standard in. Normally these filenames are separated by newline, but with this option they are separated by null-bytes. This is useful with the GNU find -print0 option.</p>
<dt><code>-q, &#8211;quiet</code></p>
<dd> Decrease verbosity level by one. This is subtracted from the default verbosity level, or the level specified with <code>&#8211;verbosity</code>. This option may be specified more than once to make atool even less verbose.</p>
<dt><code>-v, &#8211;verbose</code></p>
<dd> Increase verbosity level by one. This is added to the default verbosity level, or the level specified with <code>&#8211;verbosity</code>. This option may be specified more than once to make atool even more verbose.</p>
<dt><code>-V, &#8211;verbosity</code>=<i>LEVEL</i></p>
<dd> Specify verbosity level. The default level is 1, which means &quot;normal verbosity&quot; &#8211; e.g. when creating and extracting from archives, files will be listed.</p>
<dt><code>&#8211;config</code>=<i>FILE</i></p>
<dd> Load configuration from the specified file. When using this option, the system-wide and user-wide configuration files will not be loaded. If the specified file does not exist or can not be read, atool will terminate with an error message.</p>
<dt><code>-o, &#8211;option</code>=<i>KEY=VALUE</i></p>
<dd> Override a configuration option. These are applied after reading the configuration files. </p>
<p> You can specify this multiple times to override different options.</p>
<dt>
<dd> <code>-O, &#8211;format-option</code>=<i>OPTION</i> Send additional options to the archiver command. This can be useful when specifying compression options for some archives, e.g. </p>
<p>&nbsp;<wbr>&nbsp;<wbr><code>apack -F7z -O-mx=9 archive.7z dir</code><br />
 You can specify this multiple times add different options.</p>
<dt><code>&#8211;save-outdir</code>=<i>FILE</i></p>
<dd> When extracting files, save the name of the directory which the archive was extracted to to the specified file. If the command was not `extract&#8217;, or the archive was not extracted to a new directory, then nothing will be written to the specified file. If multiple archives were specified (with -e), then only the last directory that files were extracted to will be written to FILE. </p>
<p> This option is used internally (see <code>EXAMPLES</code> below).</p>
<dt><code>&#8211;help</code></p>
<dd> Show summary of options.</p>
<dt><code>&#8211;version</code></p>
<dd> Output version information and exit.</dl>
<h2>ARCHIVE TYPES</h2>
<p> Unless the -f (&#8211;format) option is provided, the archive format is determined by the archive file extension. I.e. an extension &quot;.tar.gz&quot; or &quot;.tgz&quot; means tar+gzip format. Note that the extensions are checked in the other listed above, which is why a file with extension &quot;.tar.gz&quot; is considered to a tar+gzip archive, not a gzip archive. </p>
<p> The diff command is supported whenever the extract command is supported. </p>
<p> The supported archive types are:</p>
<dl>
<dt><code>tar+gzip</code><i> </i>(<i>.tar.gz</i>, <i>.tgz</i>)</p>
<dd> All commands are supported.</p>
<dt><code>tar+bzip</code><i> </i>(<i>.tar.bz</i>, <i>.tbz</i>)</p>
<dd> All commands are supported.</p>
<dt><code>tar+bzip2</code><i> </i>(<i>.tar.bz2</i>, <i>.tbz2</i>)</p>
<dd> All commands are supported.</p>
<dt><code>tar+compress</code><i> </i>(<i>.tar.Z</i>, <i>.tZ</i>)</p>
<dd> All commands are supported.</p>
<dt><code>tar+lzop</code><i> </i>(<i>.tar.lzo</i>, <i>.tzo</i>)</p>
<dd> All commands are supported.</p>
<dt><code>tar+lzip</code><i> </i>(<i>.tar.lz</i>, <i>.tlz</i>)</p>
<dd> All commands are supported.</p>
<dt><code>tar+xz</code><i> </i>(<i>.tar.xz</i>, <i>.txz</i>)</p>
<dd> All commands are supported.</p>
<dt><code>tar+7z</code><i> </i>(<i>.tar.7z</i>, <i>.t7z</i>)</p>
<dd> All commands are supported.</p>
<dt><code>tar</code><i> </i>(<i>.tar</i>)</p>
<dd> All commands are supported.</p>
<dt><code>zip</code><i> </i>(<i>.zip</i>)</p>
<dd> All commands are supported.</p>
<dt><code>jar</code><i> </i>(<i>.jar</i>, <i>.war</i>)</p>
<dd> List, extract, and add commands are supported. Cat is supported if use_jar_program is disabled.</p>
<dt><code>rar</code><i> </i>(<i>.rar</i>)</p>
<dd> All commands are supported.</p>
<dt><code>lha</code><i> </i>(<i>.lha</i>, <i>.lzh</i>)</p>
<dd> All commands are supported.</p>
<dt><code>7z</code><i> </i>(<i>.7z</i>)</p>
<dd> Extract, list and add commands are supported.</p>
<dt><code>alzip</code><i> </i>(<i>.alz</i>)</p>
<dd> Extract command is supported.</p>
<dt><code>ace</code><i> </i>(<i>.ace</i>)</p>
<dd> Extract and list commands are supported.</p>
<dt><code>ar</code><i> </i>(<i>.a</i>)</p>
<dd> All commands are supported.</p>
<dt><code>arj</code><i> </i>(<i>.arj</i>)</p>
<dd> List, extract and add commands are supported.</p>
<dt><code>arc</code><i> </i>(<i>.arc</i>)</p>
<dd> All command are supported. (Note that arc outputs an extra newline when the cat command is used.)</p>
<dt><code>rpm</code><i> </i>(<i>.rpm</i>)</p>
<dd> Extract and list commands are supported.</p>
<dt><code>deb</code><i> </i>(<i>.deb</i>)</p>
<dd> Extract and list commands are supported.</p>
<dt><code>cab</code><i> </i>(<i>.cab</i>)</p>
<dd> Cat, extract, and list commands are supported.</p>
<dt><code>gzip</code><i> </i>(<i>.gz</i>)</p>
<dd> Cat, extract, and add commands are supported.</p>
<dt><code>bzip</code><i> </i>(<i>.bz</i>)</p>
<dd> Cat, extract, and add commands are supported.</p>
<dt><code>bzip2</code><i> </i>(<i>.bz2</i>)</p>
<dd> Cat, extract, and add commands are supported.</p>
<dt><code>compress</code><i> </i>(<i>.Z</i>)</p>
<dd> Cat, extract, and add commands are supported.</p>
<dt><code>lzma</code><i> </i>(<i>.lzma</i>)</p>
<dd> Cat, extract, and add commands are supported.</p>
<dt><code>lzop</code><i> </i>(<i>.lzo</i>)</p>
<dd> Extract and add commands are supported. The cat command is not supported because lzop does not want to extract files to standard out unless the -f flag is given.</p>
<dt><code>lzip</code><i> </i>(<i>.lz</i>)</p>
<dd> Cat, extract, and add commands are supported.</p>
<dt><code>xz</code><i> </i>(<i>.xz</i>)</p>
<dd> Cat, extract, and add commands are supported.</p>
<dt><code>rzip</code><i> </i>(<i>.rz</i>)</p>
<dd> Extract and add commands are supported.</p>
<dt><code>lrzip</code><i> </i>(<i>.lrz</i>)</p>
<dd> Extract and add commands are supported.</p>
<dt><code>7zip</code><i> </i>(<i>.7z</i>)</p>
<dd> All commands are supported. (Note that 7z refuses to write extracted files to standard out if standard out is a terminal. Use -p or pipe the output of atool/acat to a pager when reading in a terminal.)</p>
<dt><code>cpio</code><i> </i>(<i>.cpio</i>)</p>
<dd> List, extract and add commands are supported. </p>
</dl>
<h2>CONFIGURATION</h2>
<p> Since version 0.8.0, atool can read custom configuration files. First, hardcoded defaults in the atool program file are evaluated. Then system-wide configuration values are loaded from <i>/etc/atool.conf</i> if that file exists. Finally, per-user configuration values are loaded from <i>.atoolrc</i> in the current user&#8217;s home directory. </p>
<p> The format of the configuration files is simple:</p>
<dl>
<dt>
<dd> variable value</dl>
<p> Here <code>variable</code> is a variable listed below, and <code>value</code> is the value to associate the variable with. <code>variable</code> and <code>value</code> should be separated with at least one whitespace (space, tab etc). Empty lines and lines beginning with # are discarded. </p>
<p> A value of `1&#8242; means that the option is enabled, and `0&#8242; that it is disabled. Strings should not be quoted, as they start at the first non-whitespace character and end at the end of the line. </p>
<p> The options are:</p>
<dl>
<dt><code>use_tar_bzip2_option </code>(default: 1)</p>
<dd> Enable this if you use GNU tar and it supports the <code>&#8211;bzip2</code> option for filtering bzip2&#8217;ed files through bzip2. Versions 1.13.6 or later of GNU tar support <code>&#8211;bzip2</code>. Therefore, if you use GNU tar earlier than 1.13.6, you will need to disable this option. </p>
<p> This used to be <code>use_tar_j_option</code> but using &#8211;bzip2 is more portable.</p>
<dt><code>use_tar_lzip_option </code>(default: 0)</p>
<dd> Enable this if you use GNU tar and it supports the <code>&#8211;lzip</code> option for filtering lzip&#8217;ed files through lzip. Versions 1.23 or later of GNU tar support <code>&#8211;lzip</code>. Therefore, if you use GNU tar earlier than 1.23, you will need to disable this option.</p>
<dt><code>use_tar_z_option </code>(default: 1)</p>
<dd> Enable this if you use GNU tar and it supports the <code>-z</code> option for filtering gzipped files through gzip. You will need to disable this and <i>use_tar_j_option</i> if you don&#8217;t use GNU tar. </p>
<p> Disabling these two options doesn&#8217;t mean that atool can&#8217;t extract bzip2/gzip files. If disabled, atool use a pipe to send output from bzip2/gzip to tar instead. </p>
<p> If possible, these options should be enabled since error management is better when filtering is done by tar.</p>
<dt><code>use_tar_lzma_option </code>(default: 1)</p>
<dd> Enable this if you use GNU tar and it supports the <code>&#8211;lzma</code> option for filtering lzma compressed files through lzma. Versions 1.20 or later of GNU tar support <code>&#8211;lzma</code>.</p>
<dt><code>use_tar_lzop_option </code>(default: 0)</p>
<dd> Enable this if you use GNU tar and it supports the <code>&#8211;lzop</code> option for filtering lzop compressed files through lzop. Versions 1.21 or later of GNU tar support <code>&#8211;lzop</code>.</p>
<dt><code>use_tar_xz_option </code>(default: 0)</p>
<dd> Enable this if you use GNU tar and it supports the <code>&#8211;xz</code> option for filtering xz compressed files through xz. Versions 1.22 or later of GNU tar support <code>&#8211;xz</code>.</p>
<dt><code>use_gzip_for_z </code>(default: 1)</p>
<dd> Enable this if you want to use gzip instead of uncompress when decompressing compress&#8217;ed files (`.Z&#8217; files).</p>
<dt><code>use_rar_for_unpack </code>(default: 0)</p>
<dd> Enable this if you want to always use rar instead of unrar when possible. This makes atool use the rar command (path_rar) even when listing and extracting RAR files.</p>
<dt><code>use_arc_for_unpack </code>(default: 0)</p>
<dd> Enable this if you want to always use arc instead of nomarch when possible. This makes atool use the arc command (path_arc) even when listing and extracting ARC files.</p>
<dt><code>use_arj_for_unpack </code>(default: 0)</p>
<dd> Enable this if you want to always use arj instead of unarj when possible. This makes atool use the arj command (path_arj) even when listing and extracting ARJ files.</p>
<dt><code>use_find_cpio_print0 </code>(default: 1)</p>
<dd> Enable this if find supports the -print0 option and cpio supports the -0 option. Without it, it is impossible/harder to make cpio archives of files with newline characters in their names.</p>
<dt><code>extract_deb_control </code>(default: 1)</p>
<dd> Debian .deb package files contain control information in a DEBIAN directory, especially the package&#8217;s &quot;control&quot; file. Enable this if you want the control information to be exctracted during extraction in addition to the normal files.</p>
<dt><code>strip_unknown_ext </code>(default: 1)</p>
<dd> Certain types of files are actually archives, but their extensions doesn&#8217;t tell so. Examples are Open Office documents (Zip files) and Gnumeric documents (gzip&#8217;ed files). Since the extensions of those filenames are unknown to atool, they would not be stripped with this option set to 0. The output file in that case would be something like Unpack-XYZW. Setting this option to 1 will cause the extension to be stripped instead.</p>
<dt><code>use_pbzip2 </code>(default: 0)</p>
<dd> Enable this if you want to use pbzip2 rather than bzip2. Please not that if use_tar_bzip2_option is enabled, then bzip2 will be used by tar regardless of the use_pbzip2 option. So if you want tar to use pbzip2 rather than bzip2, set use_pbzip2 to 1 and use_tar_bzip2_option to 0.</p>
<dt><code>use_lbzip2 </code>(default: 0)</p>
<dd> Enable this if you want to use lbzip2 rather than bzip2. Please not that if use_tar_bzip2_option is enabled, then bzip2 will be used by tar regardless of the use_lbzip2 option. So if you want tar to use lbzip2 rather than bzip2, set use_lbzip2 to 1 and use_tar_bzip2_option to 0.</p>
<dt><code>use_pigz </code>(default: 0)</p>
<dd> Enable this if you want to use pigz rather than gzip. Please not that if use_tar_z_option is enabled, then gzip will be used by tar regardless of the use_pigz option. So if you want tar to use pigz rather than gzip, set use_pigz to 1 and use_tar_z_option to 0.</p>
<dt><code>use_plzip </code>(default: 0)</p>
<dd> Enable this if you want to use plzip rather than lzip. Please not that if use_tar_lzip_option is enabled, then lzip will be used by tar regardless of the use_plzip option. So if you want tar to use plzip rather than lzip, set use_plzip to 1 and use_tar_lzip_option to 0.</p>
<dt><code>use_jar </code>(default: 0)</p>
<dd> Enable this if you want to use jar for managing jar archives. If you disable this option, zip will be used (which should work just as well, and probably be faster too). </p>
<p> This option is disabled by default since extracting files to standard out (`cat&#8217;) is not supported by jar.</p>
<dt><code>use_file </code>(default: 1)</p>
<dd> Enable this if you want atool to identify file types using <a href="/docs/linux/man/1-file/">file</a>(1) for those files with an unrecognized extension (or none at all).</p>
<dt><code>use_file_always </code>(default: 0)</p>
<dd> Enable this if you want atool to always identify archives using <a href="/docs/linux/man/1-file/">file</a>(1), regardless of the file extension. Please note that this currently has some drawbacks, such as not being able to identify all archive types (especially tar archives compressed with 7zip, lzop, szip etc).</p>
<dt><code>tmpdir_name </code>(default: Unpack-%04d)</p>
<dd> atool extracts to a temporary directory created in the current directory so that no files are overwritten. This variable controlls what name that temporary directory should have. </p>
<p> The `%d&#8217; string in this variable will be replaced with a random number between 0 and 9999. It is possible change the format of this number by using something else than `%d&#8217; &#8211; see <a href="/docs/linux/man/3-printf/">printf</a>(3).</p>
<dt><code>tmpfile_name </code>(default: Pack-%04d)</p>
<dd> When using pbzip2, and creating archives, a temporary file need to be created. This option controls the name of that file. See tmpdir_name for further details on the format.</p>
<dt><code>path_pager </code>(default: pager)</p>
<dd>
<dt><code>path_jar </code>(default: jar)</p>
<dd>
<dt><code>path_tar </code>(default: tar)</p>
<dd>
<dt><code>path_zip </code>(default: zip)</p>
<dd>
<dt><code>path_unzip </code>(default: unzip)</p>
<dd>
<dt><code>path_gzip </code>(default: gzip)</p>
<dd>
<dt><code>path_bzip </code>(default: bzip)</p>
<dd>
<dt><code>path_bzip2 </code>(default: bzip2)</p>
<dd>
<dt><code>path_pbzip2 </code>(default: pbzip2)</p>
<dd>
<dt><code>path_compress </code>(default: compress)</p>
<dd>
<dt><code>path_lzma </code>(default: lzma)</p>
<dd>
<dt><code>path_lzop </code>(default: lzop)</p>
<dd>
<dt><code>path_lzip </code>(default: lzip)</p>
<dd>
<dt><code>path_rar </code>(default: rar)</p>
<dd>
<dt><code>path_unrar </code>(default: unrar)</p>
<dd>
<dt><code>path_lbzip2 </code>(default: lbzip2)</p>
<dd>
<dt><code>path_pigz </code>(default: pigz)</p>
<dd>
<dt><code>path_cabextract </code>(default: cabextract)</p>
<dd>
<dt><code>path_7z </code>(default: 7z)</p>
<dd>
<dt><code>path_unalz </code>(default: unalz)</p>
<dd>
<dt><code>path_lha </code>(default: lha)</p>
<dd>
<dt><code>path_unace </code>(default: unace)</p>
<dd>
<dt><code>path_ar </code>(default: ar)</p>
<dd>
<dt><code>path_arj </code>(default: arj)</p>
<dd>
<dt><code>path_unarj </code>(default: unarj)</p>
<dd>
<dt><code>path_arc </code>(default: arc)</p>
<dd>
<dt><code>path_nomarch </code>(default: nomarch)</p>
<dd>
<dt><code>path_rpm </code>(default: rpm)</p>
<dd>
<dt><code>path_rpm2cpio </code>(default: rpm2cpio)</p>
<dd>
<dt><code>path_dpkg_deb </code>(default: dpkg-deb)</p>
<dd>
<dt><code>path_cpio </code>(default: cpio)</p>
<dd>
<dt><code>path_file </code>(default: file)</p>
<dd>
<dt><code>path_find </code>(default: find)</p>
<dd>
<dt><code>path_xargs </code>(default: xargs)</p>
<dd>
<dt><code>path_cat </code>(default: cat)</p>
<dd>
<dt><code>path_diff </code>(default: diff)</p>
<dd> These are all paths to the corresponding programs. It is usually best to leave them as is, because that way their locations can be looked up from the PATH variable.</p>
<dt><code>args_diff </code>(default: -ru)</p>
<dd> This variable specifies command line arguments to pass to the diff command (as specified by path_diff) when using adiff. Space characters separate arguments in this string.</p>
<dt><code>path_syscfg </code>(default: /etc/atool.conf)</p>
<dd> (This variable can only be set in the atool program file.) This variable specifies the directory where the system-wide configuration file is located.</p>
<dt><code>path_usercfg </code>(default: .atoolrc)</p>
<dd> (This variable can only be set in the atool program file and system-wide configuration file.) This variable specifies where the user configuration file is located. Note that if this filename is relative (i.e. doesn&#8217;t being with `/&#8217;), it will be relative to the current user&#8217;s home directory (as determined by the HOME environment variable).</p>
<dt><code>default_verbosity </code>(default: 1)</p>
<dd> This is the default verbosity of atool. By using -q and -v options, the verbosity level can be raised and lowered. Level 1 means &quot;normal verbosity&quot; &#8211; e.g. when creating and extracting from archives, files will be listed.</p>
<dt><code>show_extracted </code>(default: 1)</p>
<dd> If this is set to 1, the aunpack command will always show what file or directory that was extracted. Otherwise that will only be printed if the archive was extracted to an unexpected location (as a result of local files already existing or the archive having multiple files in its root directory). </p>
<p> This can be quite useful in combinatiaon with `default_verbosity 0&#8242;. Note that this option will have no effect when the -X option is used with aunpack, and it has no effect on compressed files.</p>
<dt><code>keep_compressed </code>(default: 1)</p>
<dd> When compressing a file with gzip or bzip2, the original (uncompressed) file is usually deleted once it has been compressed. I.e. if you compress a file &quot;test&quot; you will end up with only one file, &quot;test.gz&quot;. With this option set to 1, you will make atool keep the original file as well. The original behaviour is achieved by setting this option to 0. </p>
<p> This option also has an equivalent effect on uncompressing compressed files. When set to 1, the original (compressed) file will be kept. Otherwise it will be deleted. </p>
<p> Note however that this option has no effect when packing up a compressed file with the -X option (for specifying an output directory or file). In that case the original file is always kept.</p>
<dt><code>decompress_to_cwd </code>(default: 1)</p>
<dd> When decompressing a file with commands such as gzip or bzip2, the decompressed file is usually placed in the same directory as the compressed file. With this option set to 1, the decompressed file is instead placed in the current working directory. </p>
<p> Note that this option has no effect when -X is used. </p>
</dl>
<h2>ENVIRONMENT VARIABLES</h2>
<p> <code>PAGER</code> The default pager to use when the -p/&#8211;page option is specified.</p>
<h2>EXAMPLES</h2>
<p> To extract all files from archive `foobar.tar.gz&#8217; to a subdirectory (or the current directory if it only contains one file):<br />
 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt><code>aunpack foobar.tar.gz</code></p>
<p> To extract all files from all `.tar.gz&#8217; archives in the current directory:<br />
 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt><code>aunpack -e *.tar.gz</code></p>
<p> To create a zip archive of two files `foo&#8217; and `bar&#8217;:<br />
 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt><code>apack myarchive.zip foo bar</code></p>
<p> To display the file `baz&#8217; in the archive `myarchive.zip&#8217; through a pager:<br />
 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt><code>acat -p myarchive.zip baz</code></p>
<p> To list contents of the rar archive `stuff.rar&#8217;:<br />
 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt><code>als stuff.rar</code></p>
<p> To create three archives, `dir1.tar.gz&#8217;, `dir2.tar.gz&#8217; and `dir3.tar.gz&#8217;, so that the first one contains all files in dir1, the second all in dir2 and the third all dir3:<br />
 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt><code>apack -e -F .tar.gz dir1 dir2 dir3</code></p>
<p> To show all differences between version 2.4.17 and 2.4.18 of the kernel:<br />
 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt><code>adiff linux-2.4.17.tar.gz linux-2.4.18.tar.gz</code></p>
<p> To repack all .tar.gz archives in the current directory to .tar.7z (the old archive will be kept untouched):<br />
 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt><code>arepack -F.tar.7z -e *.tar.gz</code></p>
<p> Here&#8217;s a shell function that will make the aunpack command change into the directory where files were extracted:<br />
 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt><code>aunpack () {</code></p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt><code> TMP=`mktemp /tmp/aunpack.XXXXXXXXXX`</code></p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt><code> atool -x &#8211;save-outdir=$TMP &quot;$@&quot;</code></p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt><code> DIR=&quot;`cat $TMP`&quot;</code></p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt><code> [ &quot;$DIR&quot; != &quot;&quot; -a -d &quot;$DIR&quot; ] &amp;&amp; cd &quot;$DIR&quot;</code></p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt><code> rm $TMP</code></p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt><code>}</code></p>
<p> If you don&#8217;t have the mktemp program, you can replace the second line with (note however that this is not entirely safe)<br />
 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt><code> TMP=&quot;/tmp/atool_outdir.$$&quot;</code></p>
<h2>KNOWN BUGS</h2>
<p> Trying to extract gzip and other compressed files without the .gz (or .bz2 etc) extension won&#8217;t work: </p>
<p>&nbsp;<wbr>&nbsp;<wbr>aunpack: foo: format not known, identifying using file<br />
&nbsp;<wbr>&nbsp;<wbr>aunpack: foo: format is&nbsp;<wbr>`gzip&#8217;<br />
&nbsp;<wbr>&nbsp;<wbr>gzip: foo: unknown suffix &#8212; ignored </p>
<p> This last error above is generated by <code>gzip -d foo</code>. </p>
<p> If you find a bug not listed here, please report it to &lt;oskar [at] osk.mine.nu&gt;.</p>
<h2>REPORTING BUGS</h2>
<p> Report bugs to &lt;<i>oskar [at] osk.mine.nu</i>&gt;.</p>
<h2>AUTHOR</h2>
<p> The author of <code>atool</code> and this manual page is Oskar Liljeblad &lt;<i>oskar [at] osk.mine.nu</i>&gt;.</p>
<h2>COPYRIGHT</h2>
<p> Copyright &#169; 2001, 2002, 2003, 2004, 2005, 2007, 2008, 2009, 2011, 2012 Oskar Liljeblad </p>
<p> This is free software; see the source for copying conditions. There is NO warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. </p>
<h2>Index</h2>
