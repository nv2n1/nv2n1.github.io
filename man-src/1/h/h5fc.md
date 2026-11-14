---
title: "h5fc(1)"
name: "h5fc"
section: "1"
letter: "h"
url: "/docs/linux/man/1-h5fc/"
description: "Fortran – Reports statistics regarding an HDF5 file and the objects in the file."
---

<h2>NAME</h2>
<p> Fortran &#8211; Reports statistics regarding an HDF5 file and the objects in the file.</p>
<h2>DESCRIPTION</h2>
<p> usage: h5fc [OPTIONS] &lt;compile line&gt;</p>
<dl>
<dt>
<dd> OPTIONS:</p>
<dt><code>-help</code></p>
<dd> This help message.</p>
<dt><code>-echo</code></p>
<dd> Show all the shell commands executed</p>
<dt><code>-prefix</code>=<i>DIR</i></p>
<dd> Prefix directory to find HDF5 lib/ and include/</p>
<dt>
<dd> subdirectories [default: /usr]</p>
<dt><code>-show</code></p>
<dd> Show the commands without executing them</p>
<dt><code>-showconfig</code></p>
<dd> Show the HDF5 library configuration summary</p>
<dt><code>-shlib</code></p>
<dd> Compile with shared HDF5 libraries</p>
<dt><code>-noshlib</code></p>
<dd> Compile with static HDF5 libraries [default]</p>
<dt>&lt;compile line&gt;</p>
<dd> &#8211; the normal compile line options for your compiler.</p>
<dt>
<dd> h5fc uses the same compiler you used to compile HDF5. Check with your compiler&#8217;s man pages for more information on which options are needed.</p>
<dt>
<dd> You can override the compiler and linker to compile your program by setting the following environment variables accordingly:</p>
<dt>HDF5_FC</p>
<dd> &#8211; use a different Fortran 90 or 95 compiler</p>
<dt>HDF5_FLINKER</p>
<dd> &#8211; use a different linker</p>
<dt>HDF5_USE_SHLIB=[yes|no]</p>
<dd> &#8211; use shared or static version of the HDF5 library</p>
<dt>
<dd> [default: no]</p>
<dt>
<dd> You can also add or change paths and flags to the compile line using the following environment varibles or by assigning them to their counterparts in the &#8216;Things You Can Modify to Override&#8230;&#8217; section of h5fc</p>
<dt>Variable</p>
<dd> Current value to be replaced</p>
<dt>HDF5_FFLAGS</p>
<dd> &quot;&quot;</p>
<dt>HDF5_LDFLAGS</p>
<dd> &quot;&quot;</p>
<dt>HDF5_LIBS</p>
<dd> &quot;&quot;</p>
<dt>
<dd> Note that adding library paths to HDF5_LDFLAGS where another hdf5 version is located may link your program with that other hdf5 library version.</dl>
<h2>COPYRIGHT</h2>
<p> Copyright &#169; 2011 Free Software Foundation, Inc. </p>
<p> GNU Fortran comes with NO WARRANTY, to the extent permitted by law. You may redistribute copies of GNU Fortran under the terms of the GNU General Public License. For more information about these matters, see the file named COPYING</p>
<h2>SEE ALSO</h2>
<p> The full documentation for <code>Fortran</code> is maintained as a Texinfo manual. If the <code>info</code> and <code>Fortran</code> programs are properly installed at your site, the command</p>
<dl>
<dt>
<dd> <code>info Fortran</code></dl>
<p> should give you access to the complete manual. </p>
<h2>Index</h2>
