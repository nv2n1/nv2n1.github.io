---
title: "foomatic-ppd-to-xml(1)"
name: "foomatic-ppd-to-xml"
section: "1"
letter: "f"
url: "/docs/linux/man/1-foomatic-ppd-to-xml/"
description: "foomatic-ppd-to-xml – Generate Foomatic printer XML from a PPD"
---

<h2>NAME</h2>
<p> foomatic-ppd-to-xml &#8211; Generate Foomatic printer XML from a PPD</p>
<h2>SYNOPSIS</h2>
<dl>
<dt> <code>foomatic-ppd-to-xml</code> <i>OPTIONSFR [DRIVER</i>:]<i>PPD</i> [[<i>DRIVER</i>:]<i>PPD</i> &#8230;]</p>
<dt> <code>foomatic-ppd-to-xml</code> -h </p>
</dl>
<h2>DESCRIPTION</h2>
<dd>The first form of the <code>foomatic-ppd-to-xml</code> command creates Foomatic printer XML corresponding to a given PPD file. </p>
<p> If <i>DRIVER</i> is specified, it is the driver to which the PPD file should get assigned. If not supplied, the first driver in the driver list supplied via the <code>-d</code> option is used. Note that the PPD files have to be supplied to different drivers, so drivers need to be specified if using more than one PPD. </p>
<p> The second form prints a help message and exits. </p>
<h3>Options</h3>
<dl>
<dt><code>-d</code> <i>DRIVERS</i></p>
<dd> Comma-separated list of drivers with which the printer works. First driver is the one for which the PPD file is. If not otherwise stated by the <code>-r</code> option, this is also the recommended driver. Drivers already specified together with PPDs do not need to be specified with this option again. The option is not needed if drivers are specified for all PPDs. </p>
<dt><code>-r</code> <i>DRIVER</i></p>
<dd> Recommended driver. </p>
<dt><code>-p</code> <i>PDLS</i></p>
<dd> Comma-separated list of known Page Description Languages (PDLs) which the printer supports. This will add all suitable drivers to the XML entry. Currently supported are: Postscript, PCLXL, PCL6, PCL5e, PCL5c, PCL5, and PCL4. </p>
<dt><code>-l</code></p>
<dd> Add a link to the PPD file to the driver entry in the XML file. </p>
<dt><code>-b</code> <i>DIRECTORY</i></p>
<dd> Base directory for a relative link to the PPD. If the base directory is given, the link set via the <code>-l</code> option is relative to this directory (and not relative to the current directory). With a base directory given the <i>PPD</i> can also be given relative to this directory. </p>
<dt><code>-D</code></p>
<dd> Add only the driver requested by <code>-d</code> and <code>-r</code> to the driver list in the XML file, do not add drivers based on PDLs, not even on the PDLs supplied by the <code>-p</code> option. </p>
<dt><code>-c</code> <i>COMMENT</i></p>
<dd> Add the given comment to the comment field of the XML file. Comments are in HTML. </p>
<dt><code>-C</code></p>
<dd> Suppress any default comments (max paper width, pages per minute, automatically generated XML, &#8230;). Does not suppress the comment supplied with <code>-c</code>. </p>
<dt><code>-f</code> <i>DIRECTORY</i></p>
<dd> Directory in which to write the resulting XML file. The name of the file will be the printer ID with the &quot;.xml&quot; extension. </p>
<dt><code>-n</code></p>
<dd> Do not write modified versions of existing XML files, only create XML files for printers for which there is no XML file yet. </p>
<dt><code>-x</code></p>
<dd> Create XML files independent of whether or not there are already XML files for the printers covered by the PPD. This makes the process vastly faster if you have PPD files for printers which are definitely not yet in the Foomatic database. </p>
</dl>
<h2>EXIT STATUS</h2>
<p> <code>foomatic-ppd-to-xml</code> returns 0 on success, 1 otherwise. </p>
<h2>BUGS</h2>
<p> None so far. </p>
<p> Please post bug reports on </p>
<p> <a rel="nofollow" href="http://lists.freestandards.org/mailman/listinfo/printing-foomatic">http://lists.freestandards.org/mailman/listinfo/printing-foomatic</a> </p>
<h2>Index</h2>
