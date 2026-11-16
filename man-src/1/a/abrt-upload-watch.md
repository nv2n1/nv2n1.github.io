---
title: "abrt-upload-watch(1)"
name: "abrt-upload-watch"
section: "1"
letter: "a"
url: "/docs/linux/man/1-abrt-upload-watch/"
---

<h2 class="name">NAME</h2>
 

 abrt-upload-watch - Watch upload directory and unpacks incoming archives into DumpLocation 

<h2>SYNOPSIS</h2>

 

 <i>abrt-upload-watch</i> [-vs] [-w NUM_WORKERS] [-c CACHE_SIZE_MIB] [UPLOAD_DIRECTORY]

<h2>OPTIONS</h2>

 

 -v, --verbose
<dl>
<dt>
</dt><dd> Be more verbose. Can be given multiple times.</dd></dl>
 

 -s
<dl>
<dt>
</dt><dd> Log to syslog</dd></dl>
 

 -d
<dl>
<dt>
</dt><dd> Daemonize</dd></dl>
 

 -w NUM_WORKERS
<dl>
<dt>
</dt><dd> Number of concurrent workers. Default is 10</dd></dl>
 

 -c CACHE_SIZE_MIB
<dl>
<dt>
</dt><dd> Maximal cache size in MiB. Default is 4</dd></dl>
 

 UPLOAD_DIRECTORY
<dl>
<dt>
</dt><dd> Watched directory. Default is a value of WatchCrashdumpArchiveDir option from abrt.conf</dd></dl>

<h2>FILES</h2>

 

 Uses these three configuration options from file <i>/etc/abrt/abrt.conf</i>: 

 WatchCrashdumpArchiveDir
<dl>
<dt>
</dt><dd> Default upload directory</dd></dl>
 

 DumpLocation
<dl>
<dt>
</dt><dd> Place where uploaded archives are unpacked</dd></dl>
 

 DeleteUploaded
<dl>
<dt>
</dt><dd> Specifies if uploaded archives are deleted after unpacking</dd></dl>

<h2>SEE ALSO</h2>

 

 <a HREF="/docs/linux/man/5-abrt-conf/">abrt.conf</a>(5)

<h2>AUTHORS</h2>

 

<dl>
<dt>
</dt><dd> &bull; ABRT team</dd></dl>
 

<h2>Index</h2>


