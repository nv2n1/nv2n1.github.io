---
title: "arj(1)"
name: "arj"
section: "1"
letter: "a"
url: "/docs/linux/man/1-arj/"
description: "arj – Archiver for .arj files"
---

<h2 class="name">NAME</h2>
<p> arj &#8211; Archiver for .arj files </p>
<h2>SYNOPSIS</h2>
<p> <code>arj</code> <i>command</i> [<i>-switch</i>[<i>&#8211;</i>|<i>+</i>|<i>option</i>]] <i>archive</i>[<i>.arj</i>] [<i>base directory</i>] [<i>!list name</i>|<i>path name</i>|<i>wildcard name</i>]</p>
<h2>DESCRIPTION</h2>
<p> <i>arj</i> is a compression and file archiving utility. It was invented by Robert K. Jung. <i>ARJ</i> stands for <i>A</i>rchived by <i>R</i>obert <i>J</i>ung.</p>
<h2>COMMANDS</h2>
<dl>
<dt><code>ac</code></dt>
<dd> Add Chapter to chapter archive.</dd>
<dt><code>cc</code></dt>
<dd> Convert archive to Chapter archive.</dd>
<dt><code>dc</code></dt>
<dd> Delete last Chapter from archive.</dd>
<dt><code>a</code></dt>
<dd> Add files to archive.</dd>
<dt><code>b</code></dt>
<dd> execute Batch or dos command.</dd>
<dt><code>c</code></dt>
<dd> Comment archive files.</dd>
<dt><code>d</code></dt>
<dd> Delete files from archive.</dd>
<dt><code>e</code></dt>
<dd> Extract files from archive.</dd>
<dt><code>f</code></dt>
<dd> Freshen files in archive.</dd>
<dt><code>g</code></dt>
<dd> Garble files in archive.</dd>
<dt><code>i</code></dt>
<dd> check Integrity of the <code>arj</code> program.</dd>
<dt><code>j</code></dt>
<dd> Join archives to archive</dd>
<dt><code>k</code></dt>
<dd> remove obsolete bacKup files.</dd>
<dt><code>l</code></dt>
<dd> List contents of archive.</dd>
<dt><code>m</code></dt>
<dd> Move files to archive.</dd>
<dt><code>n</code></dt>
<dd> reName files in archive.</dd>
<dt><code>o</code></dt>
<dd> Order files in archive.</dd>
<dt><code>p</code></dt>
<dd> Print files to standard output.</dd>
<dt><code>q</code></dt>
<dd> recover damaged <code>arj</code> file.</dd>
<dt><code>r</code></dt>
<dd> Remove paths from filenames.</dd>
<dt><code>s</code></dt>
<dd> Sample files to screen with pause.</dd>
<dt><code>t</code></dt>
<dd> Test integrity of archive.</dd>
<dt><code>u</code></dt>
<dd> Update files to archive.</dd>
<dt><code>v</code></dt>
<dd> Verbosely list contents of archive.</dd>
<dt><code>w</code></dt>
<dd> Where are text strings in archive.</dd>
<dt><code>x</code></dt>
<dd> eXtract files with full pathname.</dd>
<dt><code>y</code></dt>
<dd> copY archive with new options.</dd></dl>
<h2>SWITCHES</h2>
<dl>
<dt><code>c</code></dt>
<dd> skip time-stamp Check</dd>
<dt><code>e</code></dt>
<dd> Exclude paths from names</dd>
<dt><code>f</code></dt>
<dd> Freshen existing files</dd>
<dt><code>g</code></dt>
<dd> Garble with password</dd>
<dt><code>i</code></dt>
<dd> with no progress Indicator</dd>
<dt><code>m</code></dt>
<dd> with Method 0, 1, 2, 3, 4</dd>
<dt><code>n</code></dt>
<dd> only New files (not exist)</dd>
<dt><code>r</code></dt>
<dd> Recurse subdirectories</dd>
<dt><code>u</code></dt>
<dd> Update files (new and newer)</dd>
<dt><code>v</code></dt>
<dd> enable multiple Volumes</dd>
<dt><code>w</code></dt>
<dd> assign Work directory</dd>
<dt><code>x</code></dt>
<dd> eXclude selected files</dd>
<dt><code>y</code></dt>
<dd> assume Yes on all queries</dd>
<dt><code>hk</code></dt>
<dd> enable ARJ-PROTECT damage protection</dd></dl>
<h2>DETAILED SWITCHES</h2>
<dl>
<dt><code>&#8211;</code></dt>
<dd> Disables switch char</dd>
<dt><code>+</code></dt>
<dd> Inhibits ARJ_SW usage</dd>
<dl>
<dt>
</dt><dd> +var: set environment variable</dd></dl>
<dt><code>@</code></dt>
<dd> Set 1 token per response file line</dd>
<dt><code>!</code></dt>
<dd> Set list char (!)</dd>
<dt><code>&amp;</code></dt>
<dd> Set batch critical error handler</dd>
<dt><code>#</code></dt>
<dd> Select files by number</dd>
<dt><code>$</code></dt>
<dd> Add/extract volume label</dd>
<dl>
<dt>
</dt><dd> $A: add/extract label to drive A</dd></dl>
<dt><code>a</code></dt>
<dd> Allow any file Attribute</dd>
<dl>
<dt>
</dt><dd> a1: any files, directories and UNIX special files</dd></dl>
<dt><code>b</code></dt>
<dd> Backup changed files </dd>
<pre>
<dl><dt></dt><dd>b1: Backup changed, reset archive bits
b2: only reset archive bits
b3: reset archive bit during restore
b4: do not restore bits, reset arc
b5: do not restore any file attributes
</dd></dl>
</pre>
<dt><code>c</code></dt>
<dd> Skip time-stamp Check</dd>
<dt><code>d</code></dt>
<dd> Delete added files asks permission before deleting </dd>
<pre>
<dl><dt></dt><dd>d1: Delete without permission (same as <code>arj m</code>)
d2: Truncate instead of deleting
</dd></dl>
</pre>
<dt><code>e</code></dt>
<dd> Exclude paths from names</dd>
<dl>
<dt>
</dt><dd> e1: Exclude base dir from names</dd></dl>
<dt><code>f</code></dt>
<dd> Freshen existing files </dd>
<pre>
<dl><dt></dt><dd>f1: Freshen with OLDER files
f2: Freshen with DIFFERENT files
f3: Freshen with CRC mismatched files
</dd></dl>
</pre>
<dt><code>g</code></dt>
<dd> Garble with password </dd>
<pre>
<dl><dt></dt><dd>g<i>stew</i>: garble with password stew
g?: prompt for password
</dd></dl>
</pre>
<dt><code>i</code></dt>
<dd> Show no progress Indicator </dd>
<pre>
<dl><dt></dt><dd>i1: show bar graph Indicator
i2: show percentage and bar graph
i3: total progress percentage
i4: total progress bar graph
i5: total percentage and bar graph
i6: total percentage and file graph
</dd></dl>
</pre>
<dt><code>k</code></dt>
<dd> Keep a .bak of <code>arj</code> archive</dd>
<dt><code>l</code></dt>
<dd> Create List_name file</dd>
<dl>
<dt>
</dt><dd> l<i>names.list</i>: create <i>names.list</i></dd></dl>
<dt><code>m</code></dt>
<dd> With Method 0, 1, 2, 3, 4 </dd>
<pre>
<dl><dt></dt><dd>m0: store (no compression)
m1: good compression (default)
m2: less memory and compression
m3: FAST! less compression
m4: FASTEST! least compression
</dd></dl>
</pre>
<dt><code>n</code></dt>
<dd> Only New files (not exist)</dd>
<dt><code>o</code></dt>
<dd> On or after YYYYMMDDHHMMSS </dd>
<pre>
<dl><dt></dt><dd>o:       on today
o19901225: on/after 12/25/1990
ob: Before YYYYMMDDHHMMSS
ob:       before today
ob19901225: before 12/25/1990
od: no older than N Days
od5: five or less days old
oa: After YYYYMMDDHHMMSS (last access)
oa:       on today
oa19901225: after 12/25/1990
oab: Before YYYYMMDDHHMMSS (last access)
oab:      before today
oab19901225: before 12/25/1990
oc: After YYYYMMDDHHMMSS (created)
oc:       on today
oc19901225: after 12/25/1990
ocb: Before YYYYMMDDHHMMSS
ocb:      before today
ocb19901225: before 12/25/1990
</dd></dl>
</pre>
<dt><code>p</code></dt>
<dd> Match using full Pathnames</dd>
<dl>
<dt>
</dt><dd> p1: match Pathname with subdirs</dd></dl>
<dt><code>q</code></dt>
<dd> Query on each file</dd>
<dt><code>r</code></dt>
<dd> Recurse subdirectories</dd>
<dt><code>s</code></dt>
<dd> Set archive time-Stamp to newest </dd>
<pre>
<dl><dt></dt><dd>s1: save original time-Stamp
s2: set archive time-Stamp
s3: save both original time-Stamps
</dd></dl>
</pre>
<dt><code>t</code></dt>
<dd> Set file Type (default 0) </dd>
<pre>
<dl><dt></dt><dd>t0: set binary file type
t1: set C text file type
t1f: force C text file type
t1g: set C text with graphics
</dd></dl>
</pre>
<dt><code>u</code></dt>
<dd> Update files (new + newer) </dd>
<pre>
<dl><dt></dt><dd>u1: Update files (new + OLDER)
u2: Update files (new + different)
u3: Update files (new + CRC mismatch)
</dd></dl>
</pre>
<dt><code>v</code></dt>
<dd> Enable multiple Volumes </dd>
<pre>
<dl><dt></dt><dd>v360: build 362000 byte volumes
v50K: build 50000 byte volumes
va: auto-detect space available
vd<i>/tmp/*</i>: delete <i>/tmp/*</i>
ve: use alternate volume naming
vi: inhibit diskette change test
vr50K: reserve 50000 bytes of space on first volume
vs: provide command prompt
vs<code>cmd</code>: execute <code>cmd</code> before each vol
vv: beep between volumes
vw: keep Whole files in volumes
vz: provide command with no echo
v360,v720,v1200,v1440: abbrevs Volume options may be in any order
       except s and z which must be last
</dd></dl>
</pre>
<dt><code>w</code></dt>
<dd> Assign Work directory</dd>
<dl>
<dt>
</dt><dd> w<i>/tmp</i>: use <i>/tmp</i> as work directory</dd></dl>
<dt><code>x</code></dt>
<dd> eXclude selected files </dd>
<pre>
<dl><dt></dt><dd>x<i>*.sh</i>: exclude <i>*.sh</i> files
x!<i>names</i>: exclude files in <i>names</i> multiple exclusions are allowed
</dd></dl>
</pre>
<dt><code>y</code></dt>
<dd> Assume Yes on all queries except diskette volume prompts<br />
&nbsp;<wbr>Use this switch for batch mode</dd>
<dt><code>z</code></dt>
<dd> Supply archive comment file <code>_</code> Convert filenames to lower case </dd>
<pre>
<dl><dt></dt><dd>z<i>arc.cmt</i>: use <i>arc.cmt</i> for comments
z<i>/dev/null</i>: use to strip comments
</dd></dl>
</pre>
</dl>
<h2>SHIFTED SWITCHES</h2>
<dl>
<dt><code>h#</code></dt>
<dd> Append date string to name </dd>
<pre>
<dl><dt></dt><dd>h#1: append time string to name
h#2: append DHHMMSS to name (custom: h#{Y,M,D,N,h,m,s})
h#YYYY-MMDD: append YYYY-MMDD
</dd></dl>
</pre>
<dt><code>h$</code></dt>
<dd> Try to use longnames (Win2000)</dd>
<dt><code>h2</code></dt>
<dd> Obsolete synonym for -2 group of options</dd>
<dt><code>ha</code></dt>
<dd> Ignore readonly Attribute</dd>
<dt><code>hb</code></dt>
<dd> Select by file attribute/type </dd>
<pre>
<dl><dt></dt><dd>a - archive bit set
b - archive bit clear
r - readonly
s - system
h - hidden
d - directory
n - normal file, not d,h,r,s,c,l
c - chapter label
l - volume label
f - abbrev for n,d,r,s,h
u - UNIX special files
w - win95 long filenames
hb: select all types
hbsh: select hidden, system only
hbd: select dirs only
</dd></dl>
</pre>
<dt><code>hc</code></dt>
<dd> Execute Command at <code>arj</code> start</dd>
<dl>
<dt>
</dt><dd> hc<code>clear</code>: execute <code>clear</code></dd></dl>
<dt><code>he</code></dt>
<dd> Skip test of security Envelope</dd>
<dl>
<dt>
</dt><dd> he1: set error on security Envelope</dd></dl>
<dt><code>hf</code></dt>
<dd> Set short filenames only </dd>
<pre>
<dl><dt></dt><dd>hf1: set longnames in file comment or extract with <i>w95lname.nnn</i>
hf2: use long filenames in DOS
hf3: set longnames in file comment using shortname wildcards
hf4: set all files archived in Windows as Windows long filenames
</dd></dl>
</pre>
<dt><code>hg</code></dt>
<dd> Specify garble module filename </dd>
<pre>
<dl><dt></dt><dd>hg<i>arjcrypt.so</i>: set <i>arjcrypt.so</i> as name of garble module
hg!: specify use of 40 bit encryption
</dd></dl>
</pre>
<dt><code>hi</code></dt>
<dd> Detailed display in Index files</dd>
<dt><code>hk</code></dt>
<dd> Build data protection record</dd>
<dt><code>hk</code></dt>
<dd> Default amount of recovery data </dd>
<pre>
<dl><dt></dt><dd>hk1: more recovery data
hk9: maximum amount of recovery data
     Disable ARJ-PROTECT when used with the <code>&quot;y&quot;</code> command
</dd></dl>
</pre>
<dt><code>hl</code></dt>
<dd> Return error for Listfile error</dd>
<dt><code>hm</code></dt>
<dd> Increase file list capacity </dd>
<pre>
<dl><dt></dt><dd>hm!: redirect -hm temp file
hm! : move temp file to XMS mem
hm!<i>/tmp</i> : move temp file to <i>/tmp</i>
</dd></dl>
</pre>
<dt><code>hn</code></dt>
<dd> Specify non-existent filespec</dd>
<dl>
<dt>
</dt><dd> hn<code>####</code>: set <code>####</code> as filespec</dd></dl>
<dt><code>ho</code></dt>
<dd> Only extract files with matches</dd>
<dl>
<dt>
</dt><dd> ho1: Only extract files without matches</dd></dl>
<dt><code>hq</code></dt>
<dd> Ignore open access error on adds </dd>
<pre>
<dl><dt></dt><dd>hq1: ignore open not found error on adds
hq2: ignore access and not found on adds
</dd></dl>
</pre>
<dt><code>hr</code></dt>
<dd> Try to ignore archive errors</dd>
<dt><code>hs</code></dt>
<dd> Disable file Sharing</dd>
<dt><code>ht</code></dt>
<dd> Set Target directory</dd>
<dl>
<dt>
</dt><dd> ht<i>/destdir</i></dd></dl>
<dt><code>hu</code></dt>
<dd> Allow Update of volume archives</dd>
<dt><code>hv</code></dt>
<dd> Check for <code>arj</code> version</dd>
<dt><code>hw</code></dt>
<dd> Scroll save search filename display</dd>
<dl>
<dt>
</dt><dd> hw1: display only filenames with matches</dd></dl>
<dt><code>hx</code></dt>
<dd> Set default archive extensions</dd>
<dl>
<dt>
</dt><dd> hx<i>.arj.sdn</i></dd></dl>
<dt><code>hy</code></dt>
<dd> set <code>arj32</code> to use ANSI codepage set <code>arj</code> to extract ANSI codepage archive </dd>
<pre>
<dl><dt></dt><dd>hy1: force <code>arj32</code> to use OEM codepage
hy2: force <code>arj32</code> to use ANSI codepage
</dd></dl>
</pre>
<dt><code>hz</code></dt>
<dd> Create an ARJ-SECURITY envelope</dd>
<dt><code>j#</code></dt>
<dd> Store only CRC and not the file </dd>
<pre>
<dl><dt></dt><dd>j#1: store only date, size, attributes
j#2: restore file attributes
j#3: restore file dates
j#4: restore file attributes and dates
</dd></dl>
</pre>
<dt><code>j$</code></dt>
<dd> Do not process file DTA and DTC</dd>
<dt><code>ja</code></dt>
<dd> Set P command to display ANSI</dd>
<dl>
<dt>
</dt><dd> ja1: inhibit the display of comments</dd></dl>
<dt><code>jb</code></dt>
<dd> Set chapter backup processing </dd>
<pre>
<dl><dt></dt><dd>jb0: clear chapter archive status
jb*: select all chapter backup files
</dd></dl>
</pre>
<dt><code>jc</code></dt>
<dd> Exit after Count of files </dd>
<pre>
<dl><dt></dt><dd>jc5: exit after 5 files
jc <i>nam1 nam2</i>: exit after 2 files
</dd></dl>
</pre>
<dt><code>jd</code></dt>
<dd> Ensure free Disk space </dd>
<pre>
<dl><dt></dt><dd>e -jd<i>50K</i>: skip file if&lt;<i>50000</i> free
l -jd<i>1000</i>: set error if&lt;<i>1000</i> free
</dd></dl>
</pre>
<dt><code>je</code></dt>
<dd> Create self-extracting archive</dd>
<dl>
<dt>
</dt><dd> je1: create SFXJR archive</dd></dl>
<dt><code>jf</code></dt>
<dd> Store/use Full specified path</dd>
<dl>
<dt>
</dt><dd> jf1: store/use path minus drive</dd></dl>
<dt><code>jg</code></dt>
<dd> [OBSOLETE]</dd>
<dl>
<dt>
</dt><dd> jg1: [OBSOLETE]</dd></dl>
<dt><code>jh</code></dt>
<dd> Set Huffman buffer size </dd>
<pre>
<dl><dt></dt><dd>jh<i>65535</i>: set to <i>65535</i> bytes (max)
jh<i>2048</i>: set to <i>2048</i> bytes (min)
</dd></dl>
</pre>
<dt><code>ji</code></dt>
<dd> Create Index file</dd>
<dl>
<dt>
</dt><dd> ji<i>index.file</i>: create <i>index.file</i></dd></dl>
<dt><code>jk</code></dt>
<dd> Keep temp archive on error</dd>
<dt><code>jl</code></dt>
<dd> Display only filespecs</dd>
<dt><code>jm</code></dt>
<dd> Set Maximum compression mode</dd>
<dl>
<dt>
</dt><dd> jm1: set faster Maximum compression</dd></dl>
<dt><code>jn</code></dt>
<dd> Restart volumes at fileName </dd>
<pre>
<dl><dt></dt><dd>jn<i>/bin/test</i>: restart at <i>/bin/test</i>
jn: get restart information from previously written index file
</dd></dl>
</pre>
<dt><code>jo</code></dt>
<dd> Query when updating archive file </dd>
<pre>
<dl><dt></dt><dd>jo: extract to unique Output names
jo1: extract to unique Output names keeping file extension
</dd></dl>
</pre>
<dt><code>jp</code></dt>
<dd> Pause after each screenful</dd>
<dl>
<dt>
</dt><dd> jp<i>50</i>: pause, set page size to <i>50</i></dd></dl>
<dt><code>jq</code></dt>
<dd> Set string parameter</dd>
<dl>
<dt>
</dt><dd> jq<i>string</i>: set parameter to <i>string</i></dd></dl>
<dt><code>jr</code></dt>
<dd> Recover broken archive files</dd>
<dl>
<dt>
</dt><dd> jr1: Recover badly broken archive files</dd></dl>
<dt><code>js</code></dt>
<dd> Store archives by suffix (default is arj, arc, lzh, pak, rar, zip, zoo, j, and uc2).</dd>
<dl>
<dt>
</dt><dd> js<i>.zoo</i>: store only <i>.zoo</i> files</dd></dl>
<dt><code>jt</code></dt>
<dd> Test temporary archive by CRC </dd>
<pre>
<dl><dt></dt><dd>jt1: Test CRC and file contents
jt2: Test only added file contents
jt3: Test only file date-time and size
</dd></dl>
</pre>
<dt><code>ju</code></dt>
<dd> Translate UNIX style paths</dd>
<dt><code>jv</code></dt>
<dd> Set Verbose display</dd>
<dl>
<dt>
</dt><dd> jv1: set special verbose list mode</dd></dl>
<dt><code>jw</code></dt>
<dd> Set extract output filename</dd>
<dl>
<dt>
</dt><dd> jw<i>new.file</i>: output to <i>new.file</i></dd></dl>
<dt><code>jx</code></dt>
<dd> Start at eXtended position</dd>
<dl>
<dt>
</dt><dd> jx<i>10000</i>: start at position 10000</dd></dl>
<dt><code>jy</code></dt>
<dd> Suppress queries assuming Yes </dd>
<pre>
<dl><dt></dt><dd>a - skip append query
c - skip create directory query
d - skip delete files query
k - skip disk space available query
n - skip new filename prompt
o - skip overwrite file query
r - erase all type-ahead before query
s - skip scanned enough text query
v - skip proceed to next volume query
y - accept single character Y/N/A/Q
jycny: skip create, new name queries in single character
        input mode
</dd></dl>
</pre>
<dt><code>jz</code></dt>
<dd> Supply file for file comment </dd>
<pre>
<dl><dt></dt><dd>jz<i>file.cmt</i>: use <i>file.cmt</i> for comments
jz<i>/dev/null</i>: use to strip file comments
</dd></dl>
</pre>
<dt><code>2a</code></dt>
<dd> Serialize names on extraction</dd>
<dt><code>2b</code></dt>
<dd> [UNIX] restrict to Block devices </dd>
<pre>
<dl><dt></dt><dd>2b or 2b<i>.</i>: current device only
2b-<i>/usr</i>: all except where <i>/usr</i> is located
</dd></dl>
</pre>
<dt><code>2c</code></dt>
<dd> [OS/2, NT] handle Crit. EAs only</dd>
<dt><code>2d</code></dt>
<dd> <code>arj</code>/DOS compatibility mode</dd>
<dl>
<dt>
</dt><dd> 2d1: (OBSOLETE) comment compatibility</dd></dl>
<dt><code>2e</code></dt>
<dd> [OS/2, NT] filter Extended attrs </dd>
<pre>
<dl><dt></dt><dd>2e.*: pack/unpack system EAs only
2e.ICON?: pack/unpack icons only
2e: disable EAs handling
</dd></dl>
</pre>
<dt><code>2f</code></dt>
<dd> Disable comment serialization across multiple volumes</dd>
<dt><code>2h</code></dt>
<dd> [UNIX] Disable hardlink handling</dd>
<dl>
<dt>
</dt><dd> 2h1: Extract hardlinks as symlinks</dd></dl>
<dt><code>2k</code></dt>
<dd> Skip century display in dates</dd>
<dl>
<dt>
</dt><dd> 2k1: use a non-ambiguous date display format</dd></dl>
<dt><code>2l</code></dt>
<dd> [OS/2, NT] treat .LONGNAME EAs as filenames when possible</dd>
<dt><code>2o</code></dt>
<dd> [UNIX] store/restore file ownership</dd>
<dl>
<dt>
</dt><dd> 2o1: Store numeric UID/GID values 2o2: Same as -2o but saves group as well</dd></dl>
<dt><code>2p</code></dt>
<dd> Specify process Priority class </dd>
<pre>
<dl><dt></dt><dd>OS/2, NT: 2p1...2p4
Linux, FreeBSD: 2p1...2p41
</dd></dl>
</pre>
<dt><code>2r</code></dt>
<dd> Revert directory Recursion order</dd>
<dt><code>2s</code></dt>
<dd> [UNIX] preserve Symlink properties</dd>
<dt><code>2x</code></dt>
<dd> [OS/2, NT]: eXclude extended attrs</dd>
<dl>
<dt>
</dt><dd> 2x.ICON?: ignore icons</dd></dl>
</dl>
<h2>DEFAULTS</h2>
<pre><code>
Save path information in archive
Save long filenames
Save/restore extended attributes
Save/restore file date-time created and accessed in Win95 and OS/2
Save timestamps in the UNIX format under UNIX-like operating systems
Don't save drive and root in path information
Display comment ANSI sequences with built-in display handler
Prompt before overwriting output files
Use method 1 compression
Use binary mode
Use ! as list file symbol
The "ac" command is an abbreviation for "u -u2 -jb"
The "cc" command is an abbreviation for "y -jb"
The "dc" command is an abbreviation for "d -jb"
</code></pre>
<p> Under Win32, <code>arj</code> uses OEM codepage by default. The <code>&quot;-hy&quot;</code> option sets <code>arj</code> to use the ANSI codepage which is the Windows graphical environment default. <code>arj</code>/Win32 self-extracting archives should be built using the <code>&quot;-hy&quot;</code> option. </p>
<p> To ensure compatibility with previous versions of <code>arj</code>, the <code>&quot;-2d&quot;</code> parameter has to be specified when archiving under UNIX.</p>
<h2>USER PROMPT RESPONSES</h2>
<dl>
<dt><code>Yes</code></dt>
<dd> yes</dd>
<dt><code>No</code></dt>
<dd> no</dd>
<dt><code>Quit</code></dt>
<dd> abort out of <code>arj</code></dd>
<dt><code>Always</code></dt>
<dd> always assume yes for current type of query</dd>
<dt><code>Skip</code></dt>
<dd> always assume no for current type of query</dd>
<dt><code>Global</code></dt>
<dd> always assume yes for all queries except diskette volume prompts</dd>
<dt><code>Command</code></dt>
<dd> prompt for and execute one system command</dd></dl>
<h2>ENVIRONMENT</h2>
<p> <code>ARJ_SW</code> = <code>-jyry -jv -i1</code><br />
 <code>ARJ_SW</code> = <i>/etc/arj.cfg</i></p>
<h2>EXIT STATUS</h2>
<dl>
<dt><code>0</code></dt>
<dd> Success</dd>
<dt><code>1</code></dt>
<dd> Warning (specified file to add to archive not found, specified file to list, extract, etc., not found, or answering negatively to &quot;OK to proceed to next volume&#8230;&quot; prompt)</dd>
<dt><code>2</code></dt>
<dd> Fatal error</dd>
<dt><code>3</code></dt>
<dd> CRC error (header or file CRC error or bad password)</dd>
<dt><code>4</code></dt>
<dd> ARJ-SECURITY error or attempt to update an ARJ-SECURED archive</dd>
<dt><code>5</code></dt>
<dd> Disk full or write error</dd>
<dt><code>6</code></dt>
<dd> Cannot open archive or file</dd>
<dt><code>7</code></dt>
<dd> Simple user error (bad parameters)</dd>
<dt><code>8</code></dt>
<dd> Not enough memory</dd>
<dt><code>9</code></dt>
<dd> Not an <code>arj</code> archive</dd>
<dt><code>10</code></dt>
<dd> [DOS] XMS memory error (read or write)</dd>
<dt><code>11</code></dt>
<dd> User control break</dd>
<dt><code>12</code></dt>
<dd> Too many chapters (over 250)</dd></dl>
<h2>EXAMPLES</h2>
<dl>
<dt>Add files minus directory structure:</dt>
<dd> <code>arj</code> a -e archive *</dd>
<dt>Add two files to archive:</dt>
<dd> <code>arj</code> a archive <i>name1 name2</i></dd>
<dt>Add files to archive with verification:</dt>
<dd> <code>arj</code> a -jt archive *</dd>
<dt>Add files with maximum compression:</dt>
<dd> <code>arj</code> a -jm archive *</dd>
<dt>Add several directories of files:</dt>
<dd> <code>arj</code> a archive &#8230; <i>dir1 dir2 dir3</i></dd>
<dt>Add thousands of files to an archive:</dt>
<dd> <code>arj</code> a -hm1 -r archive *</dd>
<dt>Add a chapter to an archive:</dt>
<dd> <code>arj</code> ac archive <i>/foo/dir/*</i> -r</dd>
<dt>Comment archive header only:</dt>
<dd> <code>arj</code> c archive -z<i>cmt.fil</i></dd>
<dt>Convert standard archive to chapter:</dt>
<dd> <code>arj</code> cc archive</dd>
<dt>Convert chapter archive to standard:</dt>
<dd> <code>arj</code> y archive -jb0</dd>
<dt>Delete the last chapter from an archive:</dt>
<dd> <code>arj</code> dc archive *</dd>
<dt>Strip archive comment only:</dt>
<dd> <code>arj</code> c archive -z<i>/dev/null</i></dd>
<dt>Extract files from archive:</dt>
<dd> <code>arj</code> e archive</dd>
<dt>Extract maintaining directory structure:</dt>
<dd> <code>arj</code> x archive</dd>
<dt>Extract new and newer files without query:</dt>
<dd> <code>arj</code> e archive -u -y</dd>
<dt>Extract subdirectory from archive:</dt>
<dd> <code>arj</code> e archive <i>subdir/*</i> -p1</dd>
<dt>Extract files to directory:</dt>
<dd> <code>arj</code> x archive <i>destdir/</i> *</dd>
<dt>Extract files to directory:</dt>
<dd> <code>arj</code> x archive * -htdestdir</dd>
<dt>Extract files to directory with space:</dt>
<dd> <code>arj</code> x archive &quot;<i>Some Dir/ </i>&quot;</dd>
<dt>Extract files to directory with space:</dt>
<dd> <code>arj</code> x archive &quot;-ht<i>Some Dir</i>&quot;</dd>
<dt>Extract a Win95 archive to plain DOS:</dt>
<dd> <code>arj</code> x archive -hf2</dd>
<dt>List files in archive:</dt>
<dd> <code>arj</code> l archive</dd>
<dt>Move files to archive:</dt>
<dd> <code>arj</code> m archive <i>*.tex</i></dd>
<dt>Move files from archive:</dt>
<dd> <code>arj</code> e -d archive <i>*.tex</i></dd>
<dt>Recover files from a damaged archive:</dt>
<dd> <code>arj</code> x archive -jr</dd>
<dt>Test integrity of files in archive:</dt>
<dd> <code>arj</code> t archive</dd>
<dt>Test multiple <code>arj</code> archives:</dt>
<dd> <code>arj</code> t <i>*.arj</i> -hr</dd>
<dt>Add files to a multiple volume archive:</dt>
<dd> <code>arj</code> a -va <i>/floppy/archive</i> *</dd>
<dt>Create up to 999 archive volumes:</dt>
<dd> <code>arj</code> a -va <i>/floppy/archive.001</i></dd>
<dt>Extract from a multiple volume archive:</dt>
<dd> <code>arj</code> x -v <i>/floppy/archive</i></dd>
<dt>Create a multiple volume self-extractor:</dt>
<dd> <code>arj</code> a -va -je <i>/floppy/archive</i> *</dd>
<dt>Convert archive to self-extractor:</dt>
<dd> <code>arj</code> y -je1 archive</dd>
<dt>Backup dir <i>/foo</i> to dir <i>/floppy</i>:</dt>
<dd> <code>arj</code> a <i>/floppy/backup</i> <i>/foo</i> -a1 -b2 -r -vvas -w<i>/foo</i> -js -jt -hk</dd>
<dt>Restore backup on dir <i>/floppy</i> to dir <i>/foo</i>:</dt>
<dd> <code>arj</code> x <i>/floppy/backup</i> <i>/foo</i> -vv -y</dd></dl>
<h2>SELF-EXTRACTOR ARCHIVES</h2>
<p> If the first two characters of an <code>arj</code> comment are &quot;<code>))</code>&quot; in a self-extractor, then the self-extractor will accept the appended line as its command line. </p>
<p> &quot;<code>)) -o</code>&quot; will force the self-extractor to overwrite existing files.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-rearj/">rearj</a></code>(1), <code><a href="/docs/linux/man/1-unarj/">unarj</a></code>(1), <code>arj-register</code>(1).</p>
<h2>AUTHOR</h2>
<p> This manual page was written by Ola Lundqvist &lt;opal [at] debian.org&gt; in pod format, then converted by Guillem Jover &lt;guillem [at] debian.org&gt; to nroff format. </p>
<h2>Index</h2>
