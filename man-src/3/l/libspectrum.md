---

title: "libspectrum(3)"
name: "libspectrum"
section: "3"
letter: "l"
url: "/docs/linux/man/3-libspectrum/"
---

libspectrum - Sinclair ZX Spectrum support library 

<h2>DESCRIPTION</h2>

 <i>libspectrum</i> is a library for reading and writing some of the file formats used by emulators of the Sinclair ZX Spectrum. It also contains routines providing information about the various Spectrum clones which were available. 

 The file formats currently supported by <i>libspectrum</i> are:
<dl>
<dt>*
</dt><dd> Snapshots: .z80, .szx, .sna (all read/write), .zxs, .sp., .snp and +D snapshots (read only).
</dd><dt>*
</dt><dd> Tape images: .tzx, .tap, .spc, .sta, .ltp (read/write) and Warajevo .tap, Z80Em and CSW version 1 (read only).
</dd><dt>*
</dt><dd> Input recordings: .rzx (read/write).
</dd><dt>*
</dt><dd> Disk images: .dsk (both plain and extended), .fdi, .sad, .scl, .td0, .trd and .udi (identification only).
</dd><dt>*
</dt><dd> Timex cartridges: .dck (read only).
</dd><dt>*
</dt><dd> IDE hard disk images: .hdf (read/write).
</dd><dt>*
</dt><dd> Microdrive cartridge images: .mdr (read/write).</dd></dl>
 

 Additionally, any files compressed with <i><a HREF="/docs/linux/man/3-bzip2/">bzip2</a></i>(3) or <i><a HREF="/docs/linux/man/3-gzip/">gzip</a></i>(3) can be read and will be transparently decompressed. 

 Full documentation for <i>libspectrum</i> is provided in `<i>libspectrum.txt</i>'.

<h2>SEE ALSO</h2>

 <i><a HREF="/docs/linux/man/3-bzip2/">bzip2</a></i>(3), <i><a HREF="/docs/linux/man/1-fuse/">fuse</a></i>(1), <i><a HREF="/docs/linux/man/1-fuse-utils/">fuse-utils</a></i>(1), <i><a HREF="/docs/linux/man/3-gzip/">gzip</a></i>(3) 

 The comp.sys.sinclair Spectrum FAQ, at 
 <i><a rel="nofollow" HREF="http://www.worldofspectrum.org/faq/index.html">http://www.worldofspectrum.org/faq/index.html</a></i>.

<h2>AUTHOR</h2>

 Philip Kendall (philip-fuse [at] shadowmagic.org.uk)
