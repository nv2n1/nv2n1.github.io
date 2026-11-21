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
<p> sigtool [options]</p>
<p> sigtool can be used to generate MD5 checksums, convert data into hexadecimal format, list virus signatures and build/unpack/test/verify CVD databases and update scripts.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-h, &#8211;help</code></dt>
<dd> Output help information and exit.</dd>
<dt><code>-V, &#8211;version</code></dt>
<dd> Print version number and exit.</dd>
<dt><code>&#8211;quiet</code></dt>
<dd> Be quiet &#8211; output only error messages.</dd>
<dt><code>&#8211;stdout</code></dt>
<dd> Write all messages to stdout.</dd>
<dt><code>&#8211;hex-dump</code></dt>
<dd> Read data from stdin and write hex string to stdout.</dd>
<dt><code>&#8211;md5 [FILES]</code></dt>
<dd> Generate MD5 checksum from stdin or MD5 sigs for FILES.</dd>
<dt><code>&#8211;sha1 [FILES]</code></dt>
<dd> Generate SHA1 checksum from stdin or SHA1 sigs for FILES.</dd>
<dt><code>&#8211;sha256 [FILES]</code></dt>
<dd> Generate SHA256 checksum from stdin or SHA256 sigs for FILES.</dd>
<dt><code>&#8211;mdb [FILES]</code></dt>
<dd> Generate .mdb signatures for FILES.</dd>
<dt><code>&#8211;html-normalise=FILE</code></dt>
<dd> Create normalised HTML files comment.html, nocomment.html, and script.html in current working directory.</dd>
<dt><code>&#8211;utf16-decode=FILE</code></dt>
<dd> Decode UTF16 encoded data.</dd>
<dt><code>&#8211;vba=FILE</code></dt>
<dd> Extract VBA/Word6 macros from given MS Office document.</dd>
<dt><code>&#8211;vba-hex=FILE</code></dt>
<dd> Extract Word6 macros from given MS Office document and display the corresponding hex values.</dd>
<dt><code>-i, &#8211;info</code></dt>
<dd> Print a CVD information and verify MD5 and a digital signature.</dd>
<dt><code>-b, &#8211;build</code></dt>
<dd> Build a CVD file. -s, &#8211;server is required.</dd>
<dt><code>&#8211;max-bad-sigs=NUMBER</code></dt>
<dd> Maximum number of mismatched signatures when building a CVD. Default: 3000</dd>
<dt><code>&#8211;flevel</code></dt>
<dd> Specify a custom flevel. Default: 77</dd>
<dt><code>&#8211;cvd-version</code></dt>
<dd> Specify the version number to use for the build. Default is to use the value+1 from the current CVD in &#8211;datadir. If no datafile is found the default behaviour is to prompt for a version number, this switch will prevent the prompt. NOTE: If a CVD is found in the &#8211;datadir its version+1 is used and this value is ignored.</dd>
<dt><code>&#8211;no-cdiff</code></dt>
<dd> Don&#8217;t create a .cdiff file when building a new database file.</dd>
<dt><code>&#8211;unsigned</code></dt>
<dd> Create a database file without digital signatures (.cua).</dd>
<dt><code>&#8211;server</code></dt>
<dd> ClamAV Signing Service address (for virus database maintainers only).</dd>
<dt><code>&#8211;datadir=DIR</code></dt>
<dd> Use DIR as the default database directory for all operations.</dd>
<dt><code>&#8211;unpack=FILE, -u FILE</code></dt>
<dd> Unpack FILE (CVD) to a current directory.</dd>
<dt><code>&#8211;unpack-current</code></dt>
<dd> Unpack a local CVD file (main or daily) to current directory.</dd>
<dt><code>&#8211;diff=OLD NEW, -d OLD NEW</code></dt>
<dd> Create a diff file for OLD and NEW CVDs/INCDIRs.</dd>
<dt><code>&#8211;compare=OLD NEW, -c OLD NEW</code></dt>
<dd> This command will compare two text files and print differences in a cdiff format.</dd>
<dt><code>&#8211;run-cdiff=FILE, -r FILE</code></dt>
<dd> Execute update script FILE in current directory.</dd>
<dt><code>&#8211;verify-cdiff=FILE, -r FILE</code></dt>
<dd> Verify DIFF against CVD/INCDIR.</dd>
<dt><code>-l[FILE], &#8211;list-sigs[=FILE]</code></dt>
<dd> List all signature names from the local database directory (default) or from FILE.</dd>
<dt><code>-fREGEX, &#8211;find-sigs=REGEX</code></dt>
<dd> Find and display signatures from the local database directory which match the given REGEX. The whole signature body (name, hex string, etc.) is checked.</dd>
<dt><code>&#8211;decode-sigs=REGEX</code></dt>
<dd> Decode signatures read from the standard input (eg. piped from &#8211;find-sigs)</dd>
<dt><code>&#8211;test-sigs=DATABASE TARGET_FILE</code></dt>
<dd> Test all signatures from DATABASE against TARGET_FILE. This option will only give valid results if the target file is the final one (after unpacking, normalization, etc.) for which the signatures were created.</dd>
<dt><code>&#8211;print-certs=FILE</code></dt>
<dd> Print Authenticode details from a PE file.</dd></dl>
<h2>EXAMPLES</h2>
<dl>
<dt>Generate hex string from testfile and save it to testfile.hex:</dt>
<dd>
<p> <code>cat testfile | sigtool &#8211;hex-dump &gt; testfile.hex</code></dd></dl>
<h2>CREDITS</h2>
<p> Please check the full documentation for credits.</p>
<h2>AUTHOR</h2>
<p> Tomasz Kojm &lt;tkojm [at] clamav.net&gt;</p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-freshclam/">freshclam</a>(1), <a href="/docs/linux/man/5-freshclam-conf/">freshclam.conf</a>(5) </p>
