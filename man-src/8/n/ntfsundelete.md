---
title: "ntfsundelete(8)"
name: "ntfsundelete"
section: "8"
letter: "n"
url: "/docs/linux/man/8-ntfsundelete/"
description: "ntfsundelete – recover a deleted file from an NTFS volume."
---

<p>ntfsundelete &#8211; recover a deleted file from an NTFS volume.</p>
<h2>Synopsis</h2>
<p><code>ntfsundelete</code> [<i>options</i>] <i>device</i></p>
<h2>Description</h2>
<p><code>ntfsundelete</code> has three modes of operation: <i>scan</i>, <i>undelete</i> and <i>copy</i>.</p>
<h3>Scan</h3>
<p>The default mode, <i>scan</i> simply reads an NTFS Volume and looks for files that have been deleted. Then it will print a list giving the inode number, name and size.</p>
<h3>Undelete</h3>
<p>The <i>undelete</i> mode takes the files either matching the regular expression (option -m) or specified by the inode-expressions and recovers as much of the data as possible. It saves the result to another location. Partly for safety, but mostly because NTFS write support isn&#8217;t finished.</p>
<h3>Copy</h3>
<p>This is a wizard&#8217;s option. It will save a portion of the MFT to a file. This probably only be useful when debugging <i>ntfsundelete</i></p>
<h3>Notes</h3>
<p><code>ntfsundelete</code> only ever <code>reads</code> from the NTFS Volume. <code>ntfsundelete</code> will never change the volume.</p>
<h2>Caveats</h2>
<h3>Miracles</h3>
<p><code>ntfsundelete</code> cannot perform the impossible. </p>
<p> When a file is deleted the MFT Record is marked as not in use and the bitmap representing the disk usage is updated. If the power isn&#8217;t turned off immediately, the free space, where the file used to live, may become overwritten. Worse, the MFT Record may be reused for another file. If this happens it is impossible to tell where the file was on disk. </p>
<p> Even if all the clusters of a file are not in use, there is no guarantee that they haven&#8217;t been overwritten by some short-lived file.</p>
<h3>Locale</h3>
<p>In NTFS all the filenames are stored as Unicode. They will be converted into the current locale for display by <code>ntfsundelete</code>. The utility has successfully displayed some Chinese pictogram filenames and then correctly recovered them.</p>
<h3>Extended MFT Records</h3>
<p>In rare circumstances, a single MFT Record will not be large enough to hold the metadata describing a file (a file would have to be in hundreds of fragments for this to happen). In these cases one MFT record may hold the filename, but another will hold the information about the data. <code>ntfsundelete</code> will not try and piece together such records. It will simply show unnamed files with data.</p>
<h3>Compressed and Encrypted Files</h3>
<p><code>ntfsundelete</code> cannot recover compressed or encrypted files. When scanning for them, it will display as being 0% recoverable.</p>
<h3>The Recovered File&#8217;s Size and Date</h3>
<p>To recover a file <code>ntfsundelete</code> has to read the file&#8217;s metadata. Unfortunately, this isn&#8217;t always intact. When a file is deleted, the metadata can be left in an inconsistent state. e.g. the file size may be zero; the dates of the file may be set to the time it was deleted, or random.<br />
 To be safe <code>ntfsundelete</code> will pick the largest file size it finds and write that to disk. It will also try and set the file&#8217;s date to the last modified date. This date may be the correct last modified date, or something unexpected.</p>
<h2>Options</h2>
<p>Below is a summary of all the options that <code>ntfsundelete</code> accepts. Nearly all options have two equivalent names. The short name is preceded by <code>&#8211;</code> and the long name is preceded by <code>&#8212;</code>. Any single letter options, that don&#8217;t take an argument, can be combined into a single command, e.g. <code>-fv</code> is equivalent to <code>-f -v</code>. Long named options can be abbreviated to any unique prefix of their name.</p>
<dl>
<dt><code>-b</code>, <code>&#8211;byte</code> NUM</p>
<dd>If any clusters of the file cannot be recovered, the missing parts will be filled with this byte. The default is zeros.</p>
<dt><code>-C</code>, <code>&#8211;case</code></p>
<dd>When scanning an NTFS volume, any filename matching (using the <code>&#8211;match</code> option) is case-insensitive. This option makes the matching case-sensitive.</p>
<dt><code>-c</code>, <code>&#8211;copy</code> RANGE</p>
<dd>This wizard&#8217;s option will write a block of MFT FILE records to a file. The default file is <i>mft</i> which will be created in the current directory. This option can be combined with the <code>&#8211;output</code> and <code>&#8211;destination</code> options.</p>
<dt><code>-d</code>, <code>&#8211;destination</code> DIR</p>
<dd>This option controls where to put the output file of the <code>&#8211;undelete</code> and <code>&#8211;copy</code> options.</p>
<dt><code>-f</code>, <code>&#8211;force</code></p>
<dd>This will override some sensible defaults, such as not overwriting an existing file. Use this option with caution.</p>
<dt><code>-h</code>, <code>&#8211;help</code></p>
<dd>Show a list of options with a brief description of each one.</p>
<dt><code>-i</code>, <code>&#8211;inodes</code> RANGE</p>
<dd>Recover the files with these inode numbers. <i>RANGE</i> can be a single inode number, several numbers separated by commas &quot;,&quot; or a range separated by a dash &quot;-&quot;.</p>
<dt><code>-m</code>, <code>&#8211;match</code> PATTERN</p>
<dd>Filter the output by only looking for matching filenames. The pattern can include the wildcards &#8216;?&#8217;, match exactly one character or &#8216;*&#8217;, match zero or more characters. By default the matching is case-insensitive. To make the search case sensitive, use the <code>&#8211;case</code> option.</p>
<dt><code>-O</code>, <code>&#8211;optimistic</code></p>
<dd>Recover parts of the file even if they are currently marked as in use.</p>
<dt><code>-o</code>, <code>&#8211;output</code> FILE</p>
<dd>Use this option to set name of output file that <code>&#8211;undelete</code> or <code>&#8211;copy</code> will create.</p>
<dt><code>-P</code>, <code>&#8211;parent</code></p>
<dd>Display the parent directory of a deleted file.</p>
<dt><code>-p</code>, <code>&#8211;percentage</code> NUM</p>
<dd>Filter the output of the <code>&#8211;scan</code> option, by only matching files with a certain amount of recoverable content. <code>Please read the caveats section for more details.</code></p>
<dt><code>-q</code>, <code>&#8211;quiet</code></p>
<dd>Reduce the amount of output to a minimum. Naturally, it doesn&#8217;t make sense to combine this option with <code>&#8211;scan</code>.</p>
<dt><code>-s</code>, <code>&#8211;scan</code></p>
<dd>Search through an NTFS volume and print a list of files that could be recovered. This is the default action of <code>ntfsundelete</code>. This list can be filtered by filename, size, percentage recoverable or last modification time, using the <code>&#8211;match</code>, <code>&#8211;size</code>, <code>&#8211;percent</code> and <code>&#8211;time</code> options, respectively. </p>
<p> The output of scan will be: </p>
<pre>Inode Flags %age Date Time Size Filename
 6038 FN.. 93% 2002-07-17 13:42 26629 thesis.doc</pre>
<table BORDER>
<tr>
<td>
<table>
<tr VALIGN=top>
<td><code>Flag</code></td>
<td><code>Description</code>
</td>
</tr>
<tr VALIGN=top>
<td>F/D</td>
<td>File/Directory
</td>
</tr>
<tr VALIGN=top>
<td>N/R</td>
<td>(Non-)Resident data stream
</td>
</tr>
<tr VALIGN=top>
<td>C/E</td>
<td>Compressed/Encrypted data stream
</td>
</tr>
<tr VALIGN=top>
<td>!</td>
<td>Missing attributes
</td>
</tr>
</table>
</table>
<p> The percentage field shows how much of the file can potentially be recovered.</p>
<dt><code>-S</code>, <code>&#8211;size</code> RANGE</p>
<dd>Filter the output of the <code>&#8211;scan</code> option, by looking for a particular range of file sizes. The range may be specified as two numbers separated by a &#8216;-&#8216;. The sizes may be abbreviated using the suffixes k, m, g, t, for kilobytes, megabytes, gigabytes and terabytes respectively.</p>
<dt><code>-t</code>, <code>&#8211;time</code> SINCE</p>
<dd>Filter the output of the <code>&#8211;scan</code> option. Only match files that have been altered since this time. The time must be given as number using a suffix of d, w, m, y for days, weeks, months or years ago.</p>
<dt><code>-T</code>, <code>&#8211;truncate</code></p>
<dd>If <code>ntfsundelete</code> is confident about the size of a deleted file, then it will restore the file to exactly that size. The default behaviour is to round up the size to the nearest cluster (which will be a multiple of 512 bytes).</p>
<dt><code>-u</code>, <code>&#8211;undelete</code></p>
<dd>Select <code>undelete</code> mode. You can specify the files to be recovered using by using <code>&#8211;match</code> or <code>&#8211;inodes</code> options. This option can be combined with <code>&#8211;output</code>, <code>&#8211;destination</code>, and <code>&#8211;byte</code>. </p>
<p> When the file is recovered it will be given its original name, unless the <code>&#8211;output</code> option is used.</p>
<dt><code>-v</code>, <code>&#8211;verbose</code></p>
<dd>Increase the amount of output that <code>ntfsundelete</code> prints.</p>
<dt><code>-V</code>, <code>&#8211;version</code></p>
<dd>Show the version number, copyright and license for <code>ntfsundelete</code>.</dl>
<h2>Examples</h2>
<p>Look for deleted files on /dev/hda1.</p>
<dl>
<dd><code>ntfsundelete /dev/hda1</code></dl>
<p> Look for deleted documents on /dev/hda1.</p>
<dl>
<dd><code>ntfsundelete /dev/hda1 -s -m &#8216;*.doc&#8217;</code></dl>
<p> Look for deleted files between 5000 and 6000000 bytes, with at least 90% of the data recoverable, on /dev/hda1.</p>
<dl>
<dd><code>ntfsundelete /dev/hda1 -S 5k-6m -p 90</code></dl>
<p> Look for deleted files altered in the last two days</p>
<dl>
<dd><code>ntfsundelete /dev/hda1 -t 2d</code></dl>
<p> Undelete inodes 2, 5 and 100 to 131 of device /dev/sda1</p>
<dl>
<dd><code>ntfsundelete /dev/sda1 -u -i 2,5,100-131</code></dl>
<p> Undelete inode number 3689, call the file &#8216;work.doc&#8217;, set it to recovered size and put it in the user&#8217;s home directory.</p>
<dl>
<dd><code>ntfsundelete /dev/hda1 -u -T -i 3689 -o work.doc -d ~</code></dl>
<p> Save MFT Records 3689 to 3690 to a file &#8216;debug&#8217;</p>
<dl>
<dd><code>ntfsundelete /dev/hda1 -c 3689-3690 -o debug</code> </p>
<h2>Bugs</h2>
<p>There are some small limitations to <code>ntfsundelete</code>, but currently no known bugs. If you find a bug please send an email describing the problem to the development team:<br />
 ntfs-3g-devel [at] lists.sf.net</p>
<h2>Authors</h2>
<p><code>ntfsundelete</code> was written by Richard Russon and Holger Ohmacht, with contributions from Anton Altaparmakov. It was ported to ntfs-3g by Erik Larsson and Jean-Pierre Andre.</p>
<h2>Availability</h2>
<p><code>ntfsundelete</code> is part of the <code>ntfs-3g</code> package and is available from:<br />
 <a rel="nofollow" href="https://github.com/tuxera/ntfs-3g/wiki/">https://github.com/tuxera/ntfs-3g/wiki/</a></p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-ntfsinfo/">ntfsinfo</a></code>(8), <code><a href="/docs/linux/man/8-ntfsprogs/">ntfsprogs</a></code>(8) </p>
