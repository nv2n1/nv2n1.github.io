---
title: "dpkgpath(3)"
name: "dpkgpath"
section: "3"
letter: "d"
url: "/docs/linux/man/3-dpkgpath/"
---

Dpkg::Path - some common path handling functions 

<h2>Description</h2>It provides some functions to handle various path.
<h2>Methods</h2><dl COMPACT><dt>get_pkg_root_dir($file)
<dd>This function will scan upwards the hierarchy of directory to find out the directory which contains the ``<font SIZE="-1">DEBIAN''</font> sub-directory and it will return its path. This directory is the root directory of a package being built. 

 If no <font SIZE="-1">DEBIAN</font> subdirectory is found, it will return undef.
<dt>relative_to_pkg_root($file)
<dd>Returns the filename relative to get_pkg_root_dir($file).
<dt>guess_pkg_root_dir($file)
<dd>This function tries to guess the root directory of the package build tree. It will first use <i>get_pkg_root_dir()</i>, but it will fallback to a more imprecise check: namely it will use the parent directory that is a sub-directory of the debian directory. 

 It can still return undef if a file outside of the debian sub-directory is provided.
<dt>check_files_are_the_same($file1, $file2, $resolve_symlink)
<dd>This function verifies that both files are the same by checking that the device numbers and the inode numbers returned by <i>stat()</i>/<i>lstat()</i> are the same. If <tt>$resolve_symlink</tt> is true then <i>stat()</i> is used, otherwise <i>lstat()</i> is used.
<dt>canonpath($file)
<dd>This function returns a cleaned path. It simplifies double //, and remove /./ and /../ intelligently. For /../ it simplifies the path only if the previous element is not a symlink. Thus it should only be used on real filenames.
<dt>$newpath = resolve_symlink($symlink)
<dd>Return the filename of the file pointed by the symlink. The new name is canonicalized by <i>canonpath()</i>.
<dt>my $cmdpath = find_command($command)
<dd>Return the path of the command if defined and available on an absolute or relative path or on the <tt>$PATH</tt>, undef otherwise.
<dt>my $control_file = get_control_path($pkg, $filetype)
<dd>Return the path of the control file of type <tt>$filetype</tt> for the given package.
<dt>my @control_files = get_control_path($pkg)
<dd>Return the path of all available control files for the given package.
<dt>my $file = find_build_file($basename)
<dd>Selects the right variant of the given file: the arch-specific variant (``$basename.$arch'') has priority over the OS-specific variant (``$basename.$os'') which has priority over the default variant (``$basename''). If none of the files exists, then it returns undef.
<dt>my @files = find_build_file($basename)
<dd>Return the available variants of the given file. Returns an empty list if none of the files exists.</dl><h2>Changes</h2><h3>Version 1.04</h3>Update semantics: <i>find_command()</i> now handles an empty or undef argument.
<h3>Version 1.03</h3>New function: <i>find_build_file()</i>
<h3>Version 1.02</h3>New function: <i>get_control_path()</i>
<h3>Version 1.01</h3>New function: <i>find_command()</i>
<h3>Version 1.00</h3>Mark the module as public.
<h2>Author</h2>Raphaël Hertzog &lt;hertzog [at] debian.org&gt;.
