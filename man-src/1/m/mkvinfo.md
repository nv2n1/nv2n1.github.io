---
title: "mkvinfo(1)"
name: "mkvinfo"
section: "1"
letter: "m"
url: "/docs/linux/man/1-mkvinfo/"
description: "mkvinfo – Print information about elements in Matroska(TM) files"
---

<h2 class="name">NAME</h2>
<p> mkvinfo &#8211; Print information about elements in Matroska(TM) files </p>
<h2>SYNOPSIS</h2>
<dl>
<dt> <code>mkvinfo</code> [options] {source-filename}</dl>
<h2>DESCRIPTION</h2>
<dd>This program lists all elements contained in a Matroska(TM). The output can be limited to a list of tracks in the file including information about the codecs used. </p>
<p> <code>-g</code>, <code>&#8211;gui</code></p>
<dl>
<dt>
<dd> Start the GUI. This option is only available if mkvinfo was compiled with GUI support.</dl>
<p> <code>-c</code>, <code>&#8211;checksums</code></p>
<dl>
<dt>
<dd> Calculates and display the <code>Adler32</code> checksum for each frame. Useful for debugging only.</dl>
<p> <code>-s</code>, <code>&#8211;summary</code></p>
<dl>
<dt>
<dd> Only show a terse summary of what <code><a href="/docs/linux/man/1-mkvinfo/">mkvinfo</a></code>(1) finds and not each element.</dl>
<p> <code>-t</code>, <code>&#8211;track-info</code></p>
<dl>
<dt>
<dd> Show statistics for each track in verbose mode. Also sets verbosity to 1 if it was at level 0 before.</dl>
<p> <code>-x</code>, <code>&#8211;hexdump</code></p>
<dl>
<dt>
<dd> Show the first 16 bytes of each frame as a hex dump.</dl>
<p> <code>-X</code>, <code>&#8211;full-hexdump</code></p>
<dl>
<dt>
<dd> Show all bytes of each frame as a hex dump.</dl>
<p> <code>-z</code>, <code>&#8211;size</code></p>
<dl>
<dt>
<dd> Show the size of each element including its header.</dl>
<p> <code>&#8211;command-line-charset</code> <i>character-set</i></p>
<dl>
<dt>
<dd> Sets the character set to convert strings given on the command line from. It defaults to the character set given by system&#8217;s current locale.</dl>
<p> <code>&#8211;output-charset</code> <i>character-set</i></p>
<dl>
<dt>
<dd> Sets the character set to which strings are converted that are to be output. It defaults to the character set given by system&#8217;s current locale.</dl>
<p> <code>-r</code>, <code>&#8211;redirect-output</code> <i>file-name</i></p>
<dl>
<dt>
<dd> Writes all messages to the file <i>file-name</i> instead of to the console. While this can be done easily with output redirection there are cases in which this option is needed: when the terminal reinterprets the output before writing it to a file. The character set set with <code>&#8211;output-charset</code> is honored.</dl>
<p> <code>&#8211;ui-language</code> <i>code</i></p>
<dl>
<dt>
<dd> Forces the translations for the language <i>code</i> to be used (e.g. &#8216;de_DE&#8217; for the German translations). It is preferable to use the environment variables <i>LANG</i>, <i>LC_MESSAGES</i> and <i>LC_ALL</i> though. Entering &#8216;list&#8217; as the <i>code</i> will cause <code><a href="/docs/linux/man/1-mkvinfo/">mkvinfo</a></code>(1) to output a list of available translations.</dl>
<p> <code>&#8211;debug</code> <i>topic</i></p>
<dl>
<dt>
<dd> Turn on debugging for a specific feature. This option is only useful for developers.</dl>
<p> <code>&#8211;engage</code> <i>feature</i></p>
<dl>
<dt>
<dd> Turn on experimental features. A list of available features can be requested with <code>mkvinfo &#8211;engage list</code>. These features are not meant to be used in normal situations.</dl>
<p> <code>&#8211;gui-mode</code></p>
<dl>
<dt>
<dd> Turns on GUI mode. In this mode specially-formatted lines may be output that can tell a controlling GUI what&#8217;s happening. These messages follow the format &#8216;#GUI#message&#8217;. The message may be followed by key/value pairs as in &#8216;#GUI#message#key1=value1#key2=value2&#8230;&#8217;. Neither the messages nor the keys are ever translated and always output in English. </p>
<p> This switch has nothing to do with the <code>&#8211;gui</code> parameter which causes mkvinfo to display its own GUI.</dl>
<p> <code>-v</code>, <code>&#8211;verbose</code></p>
<dl>
<dt>
<dd> Be more verbose. See the section about verbosity levels for a description which information will be output at which level.</dl>
<p> <code>-h</code>, <code>&#8211;help</code></p>
<dl>
<dt>
<dd> Show usage information and exit.</dl>
<p> <code>-V</code>, <code>&#8211;version</code></p>
<dl>
<dt>
<dd> Show version information and exit.</dl>
<p> <code>&#8211;check-for-updates</code></p>
<dl>
<dt>
<dd> Checks online for new releases by downloading the URL m[blue]<code><a rel="nofollow" href="http://mkvtoolnix-releases.bunkus.org/latest-release.xml">http://mkvtoolnix-releases.bunkus.org/latest-release.xml</a></code>m[]. Four lines will be output in key=value style: the URL from where the information was retrieved (key version_check_url), the currently running version (key running_version), the latest release&#8217;s version (key available_version) and the download URL (key download_url). </p>
<p> Afterwards the program exists with an exit code of 0 if no newer release is available, with 1 if a newer release is available and with 2 if an error occured (e.g. if the update information could not be retrieved). </p>
<p> This option is only available if the program was built with support for libcurl.</dl>
<p> <code>@</code><i>options-file</i></p>
<dl>
<dt>
<dd> Reads additional command line arguments from the file <i>options-file</i>. Lines whose first non-whitespace character is a hash mark (&#8216;#&#8217;) are treated as comments and ignored. White spaces at the start and end of a line will be stripped. Each line must contain exactly one option. </p>
<p> Several chars can be escaped, e.g. if you need to start a non-comment line with &#8216;#&#8217;. The rules are described in the section about escaping text. </p>
<p> The command line &#8216;<code>mkvinfo -v -v input.mkv &#8211;redirect-output info.txt</code>&#8216; could be converted into the following option file: </p>
<dl>
<dt>
<dd>
<pre>
# Be more verbose
-v
-v
# Parse input.mkv
input.mkv
# and write the output to info.txt
--redirect-output
info.txt
</pre>
</dl>
</dl>
<h2>VERBOSITY LEVELS</h2>
<p> The <code>-v</code> option can be used to increase <code><a href="/docs/linux/man/1-mkvinfo/">mkvinfo</a></code>(1)&#8217;s verbosity level and print more information about the current file. </p>
<p> At level 0 <code><a href="/docs/linux/man/1-mkvinfo/">mkvinfo</a></code>(1) will print only the track headers it finds and their types. <code><a href="/docs/linux/man/1-mkvinfo/">mkvinfo</a></code>(1) will exit as soon as the headers are parsed completely (more technical: as soon as the first cluster is encountered). In this level the seek head entries and the cues will not be displayed &#8212; even if they&#8217;re located in front of the track information. </p>
<p> At level 1 <code><a href="/docs/linux/man/1-mkvinfo/">mkvinfo</a></code>(1) will also print all Matroska(TM) elements encountered for the complete file but the seek head entries and the cue entries. If the summary mode is enabled then <code><a href="/docs/linux/man/1-mkvinfo/">mkvinfo</a></code>(1) will output the frame position as well. </p>
<p> At level 2 <code><a href="/docs/linux/man/1-mkvinfo/">mkvinfo</a></code>(1) will also print the seek head entries, the cue entries and the file position at which each Matroska(TM) element can be found at. </p>
<p> At level 3 and above <code><a href="/docs/linux/man/1-mkvinfo/">mkvinfo</a></code>(1) will print some information that is not directly connected to a Matroska(TM) element. All other elements only print stuff about the elements that were just found. Level 3 adds meta information to ease debugging (read: it&#8217;s intended for developers only). All lines written by level 3 are enclosed in square brackets to make filtering them out easy.</p>
<h2>TEXT FILES AND CHARACTER SET CONVERSIONS</h2>
<p> For an in-depth discussion about how all tools in the MKVToolNix suite handle character set conversions, input/output encoding, command line encoding and console encoding please see the identically-named section in the <code><a href="/docs/linux/man/1-mkvmerge/">mkvmerge</a></code>(1) man page.</p>
<h2>EXIT CODES</h2>
<p> <code><a href="/docs/linux/man/1-mkvinfo/">mkvinfo</a></code>(1) exits with one of three exit codes: </p>
<dl>
<dt>
<dd> &bull; <code>0</code> &#8212; This exit codes means that the run has completed successfully.</dl>
<dl>
<dt>
<dd> &bull; <code>1</code> &#8212; In this case <code><a href="/docs/linux/man/1-mkvinfo/">mkvinfo</a></code>(1) has output at least one warning, but the run did continue. A warning is prefixed with the text &#8216;Warning:&#8217;.</dl>
<dl>
<dt>
<dd> &bull; <code>2</code> &#8212; This exit code is used after an error occurred. <code><a href="/docs/linux/man/1-mkvinfo/">mkvinfo</a></code>(1) aborts right after outputting the error message. Error messages range from wrong command line arguments over read/write errors to broken files.</dl>
<h2>ESCAPING SPECIAL CHARS IN TEXT</h2>
<p> There are a few places in which special characters in text must or should be escaped. The rules for escaping are simple: each character that needs escaping is replaced with a backslash followed by another character. </p>
<p> The rules are: &#8216; &#8216; (a space) becomes &#8216;\s&#8217;, &#8216;&quot;&#8217; (double quotes) becomes &#8216;\2&#8217;, &#8216;:&#8217; becomes &#8216;
