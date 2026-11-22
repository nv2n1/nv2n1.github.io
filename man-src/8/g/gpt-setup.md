---
title: "gpt-setup(8)"
name: "gpt-setup"
section: "8"
letter: "g"
url: "/docs/linux/man/8-gpt-setup/"
description: "gpt-setup – Create automake and autoconf files to convert software into a package"
---

<p><code>gpt-setup</code> &#8211; Create automake and autoconf files to convert software into a package</p>
<h2>Synopsis</h2>
<p>gpt-setup name version [directory_containing_source_code] [build_directory]</p>
<h2>Description</h2>
<p><code>gpt-setup</code> creates Makefile.am files and a configure.in file as well as other stuff that is used to convert a software distribution into a globus package. <i>name</i> is the name of the package. <i>version</i> is the version of the package. <i>directory_containing_source_code</i> is the top source directory for the distribution (the default is the current directory). <i>build_directory</i> is the top level directory containing the resulting binaries (default is the source directory). The resulting build depends on other files from the globus packaging tools (GPT) as well as the globus_core package. <code>NOTE</code> that the files that gpt-setup creates need to be edited by hand in order for the packaging to be complete. The idea behind gpt-setup is simple; &#8220;It is easier to edit than to create.&#8221;.</p>
<h2>Description of the Files that <code>gpt-setup</code> Creates</h2>
<dl>
<dt><code>Makefile.am</code>. <code>gpt-setup</code> creates a Makefile.am in the top level directory and every subdirectory except for those called CVS or RCS. The Makefile.am files contain a list of sources, subdirectories, libraries, programs, and scripts. All libraries will be built as libtool libraries. <code>NOTE</code> that all of the sources found will be included in all of the targets found. All libraries and executables have flags from the autoconf variables GPT_INCLUDES, GPT_CFLAGS, GPT_LDFLAGS, and GPT_LIBS added to them. All of the Makefiles contain directives to include files from globus_core that contain standard make targets and rules.</dt>
<dd>
</dd><dt><code>configure.in</code> <code>gpt-setup</code> creates a top level configure.in containing the standard GLOBUS_* macros from globus_core. The script detects the occurance of *.in files and headers and adds them to AM_CONFIG_HEADER and AC_OUTPUT.</dt>
<dd>
</dd><dt><code>bootstrap</code> <code>gpt-setup</code> creates a top level bootstrap script which is used to invoke aclocal, automake, autoheader, and autoconf in the correct order.</dt>
<dd>
</dd><dt><code>pkgdata</code> <code>gpt-setup</code> creates a pkgdata directory that contains the following:</dt>
<dd>
</dd><dl>
<dd>
</dd><dl>
<dt><code>pkg_data_src.gpt.in</code> is a file that contains the packaging metadata for the newly created package. <code>gpt-setup</code> inserts the name and version of the package as well as a list of all of the libraries that the package provides.</dt>
<dd>
</dd><dt><code>MyFilelists.pm</code> is a perl module that is used by <code>gpt_sort_file_list</code> to sort the installed files from the source package into binary packages. The module can be modified to take care of special files.</dt>
<dd>
</dd><dt><code>Makefile.am</code> is a makefile that assembles the filelists and packaging data into the various files.</dt>
<dd></dd></dl>
</dl>
<dl>
<dd></dd></dl>
</dl>
<h2>Post gpt-setup Tasks (What is Left to the Developer)</h2>
<p><code>gpt-setup</code> does not do everything that is needed to compile a package. Some tasks need a developer&#8217;s touch. Here is a checklist of tasks that may need to be done by hand:</p>
<dl>
<dt>Dependencies need to be added to pkgdata/pkg_data_src.gpt.in</dt>
<dd>You can use the GUI tool <code>gpt-edit</code> or edit the file by hand. The format is explained in <code>Package</code>, <code>SourceDependency</code>, and <code>Version</code>.</dd>
<dt>Build Environment flags need to be added to configure.in</dt>
<dd>Use the autoconf macros GPT_SET_CFLAGS, GPT_SET_INCLUDES, GPT_SET_LIBS pass build environment flags to both the Makefiles and the packaging metadata. With the exception of GPT_SET_CFLAGS, these flags will be included in the packaging metadata and used when packages using this package are built. See <code>Package</code> for details on the build environment metadata.</dd>
<dt>Source needs to be assigned to programs and libraries in the Makefile.am&#8217;s.</dt>
<dd><code>gpt-edit</code> automatically assigns all source found in a directory to all of the targets found in a directory. For example: </dd>
<pre> Sources = \
 foo.c \
 foo.h \
 fee.c \
 fee.h
 bin_programs = foo fee
 foo_SOURCES = $(Sources)
 fee_SOURCES = $(Sources)</pre>
<p>As you can see both programs fee and foo wind up being built with the same set of sources. This is of course wrong and needs to be corrected for every directory where more than one program or library is built.</p>
<dt>Autoconf defines need to be tested for</dt>
<dd>Use <code>gpt-undefines</code> to identify all of the preprocesser macros that are used in the source code which are not defined internally. This list will highlight the autoconf tests that need to be added to the configure.in script.</dd></dl>
<h2>See Also</h2>
<p><i>gpt-edit</i>(8) <i><a href="/docs/linux/man/8-gpt-undefines/">gpt-undefines</a></i>(8) <i><a href="/docs/linux/man/1-automake/">automake</a></i>(1) <i><a href="/docs/linux/man/1-autoconf/">autoconf</a></i>(1) <i>Package</i>(3) <i><a href="/docs/linux/man/3-version/">Version</a></i>(3) <i>SourceDependency</i>(3)</p>
<h2>Author</h2>
<p>Michael Bletzinger &lt;mbletzin.ncsa.uiuc.edu&gt; and Eric Blau &lt;eblau.ncsa.uiuc.edu&gt;</p>
