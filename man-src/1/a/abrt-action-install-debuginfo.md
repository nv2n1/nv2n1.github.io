---
title: "abrt-action-install-debuginfo(1)"
name: "abrt-action-install-debuginfo"
section: "1"
letter: "a"
url: "/docs/linux/man/1-abrt-action-install-debuginfo/"
---

<h2 class="name">NAME</h2>
 

 abrt-action-install-debuginfo - Install debuginfos for build-ids 

<h2>SYNOPSIS</h2>

 

 <i>abrt-action-install-debuginfo</i> [-vy] [--ids=BUILD_IDS_FILE] [--tmpdir=TMPDIR] [--cache=CACHEDIR[:DEBUGINFODIR1:DEBUGINFODIR2...]] [--size_mb=SIZE] [-e PATH]

<h2>DESCRIPTION</h2>

 

 Installs debuginfos for all build-ids listed in BUILD_IDS_FILE to CACHEDIR, using TMPDIR as temporary staging area. Old files in CACHEDIR are deleted until it is smaller than SIZE.

<h2>OPTIONS</h2>

 

 -v
<dl>
<dt>
</dt><dd> Be more verbose. Can be given multiple times.</dd></dl>
 

 -y
<dl>
<dt>
</dt><dd> Noninteractive, assume <i>Yes</i> to all questions</dd></dl>
 

 --ids
<dl>
<dt>
</dt><dd> Path to file with list of build ids. Default: build_ids</dd></dl>
 

 --tmpdir
<dl>
<dt>
</dt><dd> Path to tmp directory. Default: /tmp/abrt-tmp-debuginfo-RANDOM_SUFFIX</dd></dl>
 

 --cache
<dl>
<dt>
</dt><dd> Path to cache directory. Default: /var/cache/abrt-di</dd></dl>
 

 --size_mb
<dl>
<dt>
</dt><dd> Default: 4096</dd></dl>
 

 -e,--exact
<dl>
<dt>
</dt><dd> Download only specified files</dd></dl>

<h2>AUTHORS</h2>

 

<dl>
<dt>
</dt><dd> &bull; ABRT team</dd></dl>
