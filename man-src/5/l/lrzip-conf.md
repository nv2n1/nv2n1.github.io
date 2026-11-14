---
title: "lrzip-conf(5)"
name: "lrzip-conf"
section: "5"
letter: "l"
url: "/docs/linux/man/5-lrzip-conf/"
description: "lrzip.conf – Configuration File for lrzip"
---

<p>lrzip.conf &#8211; Configuration File for lrzip</p>
<h2>Description</h2>
<p>This file if used, will be read by the lrzip program, parsed, and options passed to the program. Some options may be overridden on the command line. Others are fixed. </p>
<p> The configuration file must be called <code>lrzip.conf</code>. The lrzip program will search for the file automatically in one of three places: </p>
<pre>$PWD - Current Directory
/etc/lrzip
$HOME/./lrzip
Parameters are set in <code>PARAMETER=VALUE</code> fashion where any line
beginning with a <code>#</code> or that is blank will be ignored.
Parameter values are not case sensitive.</pre>
<h2>Config File Example</h2>
<pre># This is a comment.
# Compression Window size in 100MB. Normally selected by program.
# WINDOW = 5
# Compression Level 1-9 (7 Default).
# COMPRESSIONLEVEL = 7
# Unlimited Ram Compression
# UNLIMITED = YES
# Compression Method, rzip, gzip, bzip2, lzo, or lzma (default), zpaq.
# COMPRESSIONMETHOD = LZMA
# Perform LZO Test. Default = YES (-T option, NO)
# LZOTEST = NO
# Hash Check on decompression, YES
# HASHCHECK = YES
# Show HASH value on Compression even if Verbose is off, YES
# SHOWHASH = YES
# Default output directory
# OUTPUTDIRECTORY = location
# Verbosity, Yes or Max
# VERBOSITY = MAX
# Show Progress as file is parsed, YES, NO (yes is default)
# SHOWPROGRESS = NO
# Set Niceness. 19 is default. -20 to 19 is the allowable range
# NICE = 19
# Keep broken or damaged output files, YES
# KEEPBROKEN = YES
# Delete source file after compression
# this parameter and value are case sensitive
# value must be YES to activate
# DELETEFILES = NO
# Replace existing lrzip file when compressing
# this parameter and value are case sensitive
# value must be YES to activate
# REPLACEFILE = NO
# Select Temporary Directory when stdin/stdout or Test file is used
# TMPDIR = /tmp</pre>
<h2>Notes</h2>
<p>Be careful when using <code>DELETEFILES</code> or <code>REPLACEFILE</code> as no warning will be given and lrzip will simply delete the source or replace the output file! </p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/1-lrzip/">lrzip</a>(1) </p>
