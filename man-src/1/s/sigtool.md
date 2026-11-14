---
title: "sigtool(1)"
name: "sigtool"
section: "1"
letter: "s"
url: "/docs/linux/man/1-sigtool/"
description: "sigtool – signature and database management tool"
---

<h2>NAME</h2>
<p> sigtool &#8211; signature and database management tool</p>
<h2>SYNOPSIS</h2>
<p> sigtool [options]</p>
<h2>DESCRIPTION</h2>
<p> sigtool can be used to generate MD5 checksums, convert data into hexadecimal format, list virus signatures and build/unpack/test/verify CVD databases and update scripts.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-h, &#8211;help</code></p>
<dd> Output help information and exit.</p>
<dt><code>-V, &#8211;version</code></p>
<dd> Print version number and exit.</p>
<dt><code>&#8211;quiet</code></p>
<dd> Be quiet &#8211; output only error messages.</p>
<dt><code>&#8211;stdout</code></p>
<dd> Write all messages to stdout.</p>
<dt><code>&#8211;hex-dump</code></p>
<dd> Read data from stdin and write hex string to stdout.</p>
<dt><code>&#8211;md5 [FILES]</code></p>
<dd> Generate MD5 checksum from stdin or MD5 sigs for FILES.</p>
<dt><code>&#8211;sha1 [FILES]</code></p>
<dd> Generate SHA1 checksum from stdin or SHA1 sigs for FILES.</p>
<dt><code>&#8211;sha256 [FILES]</code></p>
<dd> Generate SHA256 checksum from stdin or SHA256 sigs for FILES.</p>
<dt><code>&#8211;mdb [FILES]</code></p>
<dd> Generate .mdb signatures for FILES.</p>
<dt><code>&#8211;html-normalise=FILE</code></p>
<dd> Create normalised HTML files comment.html, nocomment.html, and script.html in current working directory.</p>
<dt><code>&#8211;utf16-decode=FILE</code></p>
<dd> Decode UTF16 encoded data.</p>
<dt><code>&#8211;vba=FILE</code></p>
<dd> Extract VBA/Word6 macros from given MS Office document.</p>
<dt><code>&#8211;vba-hex=FILE</code></p>
<dd> Extract Word6 macros from given MS Office document and display the corresponding hex values.</p>
<dt><code>-i, &#8211;info</code></p>
<dd> Print a CVD information and verify MD5 and a digital signature.</p>
<dt><code>-b, &#8211;build</code></p>
<dd> Build a CVD file. -s, &#8211;server is required.</p>
<dt><code>&#8211;max-bad-sigs=NUMBER</code></p>
<dd> Maximum number of mismatched signatures when building a CVD. Default: 3000</p>
<dt><code>&#8211;flevel</code></p>
<dd> Specify a custom flevel. Default: 77</p>
<dt><code>&#8211;cvd-version</code></p>
<dd> Specify the version number to use for the build. Default is to use the value+1 from the current CVD in &#8211;datadir. If no datafile is found the default behaviour is to prompt for a version number, this switch will prevent the prompt. NOTE: If a CVD is found in the &#8211;datadir its version+1 is used and this value is ignored.</p>
<dt><code>&#8211;no-cdiff</code></p>
<dd> Don&#8217;t create a .cdiff file when building a new database file.</p>
<dt><code>&#8211;unsigned</code></p>
<dd> Create a database file without digital signatures (.cua).</p>
<dt><code>&#8211;server</code></p>
<dd> ClamAV Signing Service address (for virus database maintainers only).</p>
<dt><code>&#8211;datadir=DIR</code></p>
<dd> Use DIR as the default database directory for all operations.</p>
<dt><code>&#8211;unpack=FILE, -u FILE</code></p>
<dd> Unpack FILE (CVD) to a current directory.</p>
<dt><code>&#8211;unpack-current</code></p>
<dd> Unpack a local CVD file (main or daily) to current directory.</p>
<dt><code>&#8211;diff=OLD NEW, -d OLD NEW</code></p>
<dd> Create a diff file for OLD and NEW CVDs/INCDIRs.</p>
<dt><code>&#8211;compare=OLD NEW, -c OLD NEW</code></p>
<dd> This command will compare two text files and print differences in a cdiff format.</p>
<dt><code>&#8211;run-cdiff=FILE, -r FILE</code></p>
<dd> Execute update script FILE in current directory.</p>
<dt><code>&#8211;verify-cdiff=FILE, -r FILE</code></p>
<dd> Verify DIFF against CVD/INCDIR.</p>
<dt><code>-l[FILE], &#8211;list-sigs[=FILE]</code></p>
<dd> List all signature names from the local database directory (default) or from FILE.</p>
<dt><code>-fREGEX, &#8211;find-sigs=REGEX</code></p>
<dd> Find and display signatures from the local database directory which match the given REGEX. The whole signature body (name, hex string, etc.) is checked.</p>
<dt><code>&#8211;decode-sigs=REGEX</code></p>
<dd> Decode signatures read from the standard input (eg. piped from &#8211;find-sigs)</p>
<dt><code>&#8211;test-sigs=DATABASE TARGET_FILE</code></p>
<dd> Test all signatures from DATABASE against TARGET_FILE. This option will only give valid results if the target file is the final one (after unpacking, normalization, etc.) for which the signatures were created.</p>
<dt><code>&#8211;print-certs=FILE</code></p>
<dd> Print Authenticode details from a PE file.</dl>
<h2>EXAMPLES</h2>
<dl>
<dt>Generate hex string from testfile and save it to testfile.hex:</p>
<dd>
<p> <code>cat testfile | sigtool &#8211;hex-dump &gt; testfile.hex</code></dl>
<h2>CREDITS</h2>
<p> Please check the full documentation for credits.</p>
<h2>AUTHOR</h2>
<p> Tomasz Kojm &lt;tkojm [at] clamav.net&gt;</p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-freshclam/">freshclam</a>(1), <a href="/docs/linux/man/5-freshclam-conf/">freshclam.conf</a>(5) </p>
<h2>Index</h2>
