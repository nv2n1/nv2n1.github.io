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
<dt><code>ac</code></p>
<dd> Add Chapter to chapter archive.</p>
<dt><code>cc</code></p>
<dd> Convert archive to Chapter archive.</p>
<dt><code>dc</code></p>
<dd> Delete last Chapter from archive.</p>
<dt><code>a</code></p>
<dd> Add files to archive.</p>
<dt><code>b</code></p>
<dd> execute Batch or dos command.</p>
<dt><code>c</code></p>
<dd> Comment archive files.</p>
<dt><code>d</code></p>
<dd> Delete files from archive.</p>
<dt><code>e</code></p>
<dd> Extract files from archive.</p>
<dt><code>f</code></p>
<dd> Freshen files in archive.</p>
<dt><code>g</code></p>
<dd> Garble files in archive.</p>
<dt><code>i</code></p>
<dd> check Integrity of the <code>arj</code> program.</p>
<dt><code>j</code></p>
<dd> Join archives to archive</p>
<dt><code>k</code></p>
<dd> remove obsolete bacKup files.</p>
<dt><code>l</code></p>
<dd> List contents of archive.</p>
<dt><code>m</code></p>
<dd> Move files to archive.</p>
<dt><code>n</code></p>
<dd> reName files in archive.</p>
<dt><code>o</code></p>
<dd> Order files in archive.</p>
<dt><code>p</code></p>
<dd> Print files to standard output.</p>
<dt><code>q</code></p>
<dd> recover damaged <code>arj</code> file.</p>
<dt><code>r</code></p>
<dd> Remove paths from filenames.</p>
<dt><code>s</code></p>
<dd> Sample files to screen with pause.</p>
<dt><code>t</code></p>
<dd> Test integrity of archive.</p>
<dt><code>u</code></p>
<dd> Update files to archive.</p>
<dt><code>v</code></p>
<dd> Verbosely list contents of archive.</p>
<dt><code>w</code></p>
<dd> Where are text strings in archive.</p>
<dt><code>x</code></p>
<dd> eXtract files with full pathname.</p>
<dt><code>y</code></p>
<dd> copY archive with new options.</dl>
<h2>SWITCHES</h2>
<dl>
<dt><code>c</code></p>
<dd> skip time-stamp Check</p>
<dt><code>e</code></p>
<dd> Exclude paths from names</p>
<dt><code>f</code></p>
<dd> Freshen existing files</p>
<dt><code>g</code></p>
<dd> Garble with password</p>
<dt><code>i</code></p>
<dd> with no progress Indicator</p>
<dt><code>m</code></p>
<dd> with Method 0, 1, 2, 3, 4</p>
<dt><code>n</code></p>
<dd> only New files (not exist)</p>
<dt><code>r</code></p>
<dd> Recurse subdirectories</p>
<dt><code>u</code></p>
<dd> Update files (new and newer)</p>
<dt><code>v</code></p>
<dd> enable multiple Volumes</p>
<dt><code>w</code></p>
<dd> assign Work directory</p>
<dt><code>x</code></p>
<dd> eXclude selected files</p>
<dt><code>y</code></p>
<dd> assume Yes on all queries</p>
<dt><code>hk</code></p>
<dd> enable ARJ-PROTECT damage protection</dl>
<h2>DETAILED SWITCHES</h2>
<dl>
<dt><code>&#8211;</code></p>
<dd> Disables switch char</p>
<dt><code>+</code></p>
<dd> Inhibits ARJ_SW usage</p>
<dl>
<dt>
<dd> +var: set environment variable</dl>
<dt><code>@</code></p>
<dd> Set 1 token per response file line</p>
<dt><code>!</code></p>
<dd> Set list char (!)</p>
<dt><code>&amp;</code></p>
<dd> Set batch critical error handler</p>
<dt><code>#</code></p>
<dd> Select files by number</p>
<dt><code>$</code></p>
<dd> Add/extract volume label</p>
<dl>
<dt>
<dd> $A: add/extract label to drive A</dl>
<dt><code>a</code></p>
<dd> Allow any file Attribute</p>
<dl>
<dt>
<dd> a1: any files, directories and UNIX special files</dl>
<dt><code>b</code></p>
<dd> Backup changed files </p>
<pre>
<dl><dt><dd>b1: Backup changed, reset archive bits
b2: only reset archive bits
b3: reset archive bit during restore
b4: do not restore bits, reset arc
b5: do not restore any file attributes
</dl>
</pre>
<dt><code>c</code></p>
<dd> Skip time-stamp Check</p>
<dt><code>d</code></p>
<dd> Delete added files asks permission before deleting </p>
<pre>
<dl><dt><dd>d1: Delete without permission (same as <code>arj m</code>)
d2: Truncate instead of deleting
</dl>
</pre>
<dt><code>e</code></p>
<dd> Exclude paths from names</p>
<dl>
<dt>
<dd> e1: Exclude base dir from names</dl>
<dt><code>f</code></p>
<dd> Freshen existing files </p>
<pre>
<dl><dt><dd>f1: Freshen with OLDER files
f2: Freshen with DIFFERENT files
f3: Freshen with CRC mismatched files
</dl>
</pre>
<dt><code>g</code></p>
<dd> Garble with password </p>
<pre>
<dl><dt><dd>g<i>stew</i>: garble with password stew
g?: prompt for password
</dl>
</pre>
<dt><code>i</code></p>
<dd> Show no progress Indicator </p>
<pre>
<dl><dt><dd>i1: show bar graph Indicator
i2: show percentage and bar graph
i3: total progress percentage
i4: total progress bar graph
i5: total percentage and bar graph
i6: total percentage and file graph
</dl>
</pre>
<dt><code>k</code></p>
<dd> Keep a .bak of <code>arj</code> archive</p>
<dt><code>l</code></p>
<dd> Create List_name file</p>
<dl>
<dt>
<dd> l<i>names.list</i>: create <i>names.list</i></dl>
<dt><code>m</code></p>
<dd> With Method 0, 1, 2, 3, 4 </p>
<pre>
<dl><dt><dd>m0: store (no compression)
m1: good compression (default)
m2: less memory and compression
m3: FAST! less compression
m4: FASTEST! least compression
</dl>
</pre>
<dt><code>n</code></p>
<dd> Only New files (not exist)</p>
<dt><code>o</code></p>
<dd> On or after YYYYMMDDHHMMSS </p>
<pre>
<dl><dt><dd>o:       on today
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
</dl>
</pre>
<dt><code>p</code></p>
<dd> Match using full Pathnames</p>
<dl>
<dt>
<dd> p1: match Pathname with subdirs</dl>
<dt><code>q</code></p>
<dd> Query on each file</p>
<dt><code>r</code></p>
<dd> Recurse subdirectories</p>
<dt><code>s</code></p>
<dd> Set archive time-Stamp to newest </p>
<pre>
<dl><dt><dd>s1: save original time-Stamp
s2: set archive time-Stamp
s3: save both original time-Stamps
</dl>
</pre>
<dt><code>t</code></p>
<dd> Set file Type (default 0) </p>
<pre>
<dl><dt><dd>t0: set binary file type
t1: set C text file type
t1f: force C text file type
t1g: set C text with graphics
</dl>
</pre>
<dt><code>u</code></p>
<dd> Update files (new + newer) </p>
<pre>
<dl><dt><dd>u1: Update files (new + OLDER)
u2: Update files (new + different)
u3: Update files (new + CRC mismatch)
</dl>
</pre>
<dt><code>v</code></p>
<dd> Enable multiple Volumes </p>
<pre>
<dl><dt><dd>v360: build 362000 byte volumes
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
</dl>
</pre>
<dt><code>w</code></p>
<dd> Assign Work directory</p>
<dl>
<dt>
<dd> w<i>/tmp</i>: use <i>/tmp</i> as work directory</dl>
<dt><code>x</code></p>
<dd> eXclude selected files </p>
<pre>
<dl><dt><dd>x<i>*.sh</i>: exclude <i>*.sh</i> files
x!<i>names</i>: exclude files in <i>names</i> multiple exclusions are allowed
</dl>
</pre>
<dt><code>y</code></p>
<dd> Assume Yes on all queries except diskette volume prompts<br />
&nbsp;<wbr>Use this switch for batch mode</p>
<dt><code>z</code></p>
<dd> Supply archive comment file <code>_</code> Convert filenames to lower case </p>
<pre>
<dl><dt><dd>z<i>arc.cmt</i>: use <i>arc.cmt</i> for comments
z<i>/dev/null</i>: use to strip comments
</dl>
</pre>
</dl>
<h2>SHIFTED SWITCHES</h2>
<dl>
<dt><code>h#</code></p>
<dd> Append date string to name </p>
<pre>
<dl><dt><dd>h#1: append time string to name
h#2: append DHHMMSS to name (custom: h#{Y,M,D,N,h,m,s})
h#YYYY-MMDD: append YYYY-MMDD
</dl>
</pre>
<dt><code>h$</code></p>
<dd> Try to use longnames (Win2000)</p>
<dt><code>h2</code></p>
<dd> Obsolete synonym for -2 group of options</p>
<dt><code>ha</code></p>
<dd> Ignore readonly Attribute</p>
<dt><code>hb</code></p>
<dd> Select by file attribute/type </p>
<pre>
<dl><dt><dd>a - archive bit set
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
</dl>
</pre>
<dt><code>hc</code></p>
<dd> Execute Command at <code>arj</code> start</p>
<dl>
<dt>
<dd> hc<code>clear</code>: execute <code>clear</code></dl>
<dt><code>he</code></p>
<dd> Skip test of security Envelope</p>
<dl>
<dt>
<dd> he1: set error on security Envelope</dl>
<dt><code>hf</code></p>
<dd> Set short filenames only </p>
<pre>
<dl><dt><dd>hf1: set longnames in file comment or extract with <i>w95lname.nnn</i>
hf2: use long filenames in DOS
hf3: set longnames in file comment using shortname wildcards
hf4: set all files archived in Windows as Windows long filenames
</dl>
</pre>
<dt><code>hg</code></p>
<dd> Specify garble module filename </p>
<pre>
<dl><dt><dd>hg<i>arjcrypt.so</i>: set <i>arjcrypt.so</i> as name of garble module
hg!: specify use of 40 bit encryption
</dl>
</pre>
<dt><code>hi</code></p>
<dd> Detailed display in Index files</p>
<dt><code>hk</code></p>
<dd> Build data protection record</p>
<dt><code>hk</code></p>
<dd> Default amount of recovery data </p>
<pre>
<dl><dt><dd>hk1: more recovery data
hk9: maximum amount of recovery data
     Disable ARJ-PROTECT when used with the <code>&quot;y&quot;</code> command
</dl>
</pre>
<dt><code>hl</code></p>
<dd> Return error for Listfile error</p>
<dt><code>hm</code></p>
<dd> Increase file list capacity </p>
<pre>
<dl><dt><dd>hm!: redirect -hm temp file
hm! : move temp file to XMS mem
hm!<i>/tmp</i> : move temp file to <i>/tmp</i>
</dl>
</pre>
<dt><code>hn</code></p>
<dd> Specify non-existent filespec</p>
<dl>
<dt>
<dd> hn<code>####</code>: set <code>####</code> as filespec</dl>
<dt><code>ho</code></p>
<dd> Only extract files with matches</p>
<dl>
<dt>
<dd> ho1: Only extract files without matches</dl>
<dt><code>hq</code></p>
<dd> Ignore open access error on adds </p>
<pre>
<dl><dt><dd>hq1: ignore open not found error on adds
hq2: ignore access and not found on adds
</dl>
</pre>
<dt><code>hr</code></p>
<dd> Try to ignore archive errors</p>
<dt><code>hs</code></p>
<dd> Disable file Sharing</p>
<dt><code>ht</code></p>
<dd> Set Target directory</p>
<dl>
<dt>
<dd> ht<i>/destdir</i></dl>
<dt><code>hu</code></p>
<dd> Allow Update of volume archives</p>
<dt><code>hv</code></p>
<dd> Check for <code>arj</code> version</p>
<dt><code>hw</code></p>
<dd> Scroll save search filename display</p>
<dl>
<dt>
<dd> hw1: display only filenames with matches</dl>
<dt><code>hx</code></p>
<dd> Set default archive extensions</p>
<dl>
<dt>
<dd> hx<i>.arj.sdn</i></dl>
<dt><code>hy</code></p>
<dd> set <code>arj32</code> to use ANSI codepage set <code>arj</code> to extract ANSI codepage archive </p>
<pre>
<dl><dt><dd>hy1: force <code>arj32</code> to use OEM codepage
hy2: force <code>arj32</code> to use ANSI codepage
</dl>
</pre>
<dt><code>hz</code></p>
<dd> Create an ARJ-SECURITY envelope</p>
<dt><code>j#</code></p>
<dd> Store only CRC and not the file </p>
<pre>
<dl><dt><dd>j#1: store only date, size, attributes
j#2: restore file attributes
j#3: restore file dates
j#4: restore file attributes and dates
</dl>
</pre>
<dt><code>j$</code></p>
<dd> Do not process file DTA and DTC</p>
<dt><code>ja</code></p>
<dd> Set P command to display ANSI</p>
<dl>
<dt>
<dd> ja1: inhibit the display of comments</dl>
<dt><code>jb</code></p>
<dd> Set chapter backup processing </p>
<pre>
<dl><dt><dd>jb0: clear chapter archive status
jb*: select all chapter backup files
</dl>
</pre>
<dt><code>jc</code></p>
<dd> Exit after Count of files </p>
<pre>
<dl><dt><dd>jc5: exit after 5 files
jc <i>nam1 nam2</i>: exit after 2 files
</dl>
</pre>
<dt><code>jd</code></p>
<dd> Ensure free Disk space </p>
<pre>
<dl><dt><dd>e -jd<i>50K</i>: skip file if&lt;<i>50000</i> free
l -jd<i>1000</i>: set error if&lt;<i>1000</i> free
</dl>
</pre>
<dt><code>je</code></p>
<dd> Create self-extracting archive</p>
<dl>
<dt>
<dd> je1: create SFXJR archive</dl>
<dt><code>jf</code></p>
<dd> Store/use Full specified path</p>
<dl>
<dt>
<dd> jf1: store/use path minus drive</dl>
<dt><code>jg</code></p>
<dd> [OBSOLETE]</p>
<dl>
<dt>
<dd> jg1: [OBSOLETE]</dl>
<dt><code>jh</code></p>
<dd> Set Huffman buffer size </p>
<pre>
<dl><dt><dd>jh<i>65535</i>: set to <i>65535</i> bytes (max)
jh<i>2048</i>: set to <i>2048</i> bytes (min)
</dl>
</pre>
<dt><code>ji</code></p>
<dd> Create Index file</p>
<dl>
<dt>
<dd> ji<i>index.file</i>: create <i>index.file</i></dl>
<dt><code>jk</code></p>
<dd> Keep temp archive on error</p>
<dt><code>jl</code></p>
<dd> Display only filespecs</p>
<dt><code>jm</code></p>
<dd> Set Maximum compression mode</p>
<dl>
<dt>
<dd> jm1: set faster Maximum compression</dl>
<dt><code>jn</code></p>
<dd> Restart volumes at fileName </p>
<pre>
<dl><dt><dd>jn<i>/bin/test</i>: restart at <i>/bin/test</i>
jn: get restart information from previously written index file
</dl>
</pre>
<dt><code>jo</code></p>
<dd> Query when updating archive file </p>
<pre>
<dl><dt><dd>jo: extract to unique Output names
jo1: extract to unique Output names keeping file extension
</dl>
</pre>
<dt><code>jp</code></p>
<dd> Pause after each screenful</p>
<dl>
<dt>
<dd> jp<i>50</i>: pause, set page size to <i>50</i></dl>
<dt><code>jq</code></p>
<dd> Set string parameter</p>
<dl>
<dt>
<dd> jq<i>string</i>: set parameter to <i>string</i></dl>
<dt><code>jr</code></p>
<dd> Recover broken archive files</p>
<dl>
<dt>
<dd> jr1: Recover badly broken archive files</dl>
<dt><code>js</code></p>
<dd> Store archives by suffix (default is arj, arc, lzh, pak, rar, zip, zoo, j, and uc2).</p>
<dl>
<dt>
<dd> js<i>.zoo</i>: store only <i>.zoo</i> files</dl>
<dt><code>jt</code></p>
<dd> Test temporary archive by CRC </p>
<pre>
<dl><dt><dd>jt1: Test CRC and file contents
jt2: Test only added file contents
jt3: Test only file date-time and size
</dl>
</pre>
<dt><code>ju</code></p>
<dd> Translate UNIX style paths</p>
<dt><code>jv</code></p>
<dd> Set Verbose display</p>
<dl>
<dt>
<dd> jv1: set special verbose list mode</dl>
<dt><code>jw</code></p>
<dd> Set extract output filename</p>
<dl>
<dt>
<dd> jw<i>new.file</i>: output to <i>new.file</i></dl>
<dt><code>jx</code></p>
<dd> Start at eXtended position</p>
<dl>
<dt>
<dd> jx<i>10000</i>: start at position 10000</dl>
<dt><code>jy</code></p>
<dd> Suppress queries assuming Yes </p>
<pre>
<dl><dt><dd>a - skip append query
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
</dl>
</pre>
<dt><code>jz</code></p>
<dd> Supply file for file comment </p>
<pre>
<dl><dt><dd>jz<i>file.cmt</i>: use <i>file.cmt</i> for comments
jz<i>/dev/null</i>: use to strip file comments
</dl>
</pre>
<dt><code>2a</code></p>
<dd> Serialize names on extraction</p>
<dt><code>2b</code></p>
<dd> [UNIX] restrict to Block devices </p>
<pre>
<dl><dt><dd>2b or 2b<i>.</i>: current device only
2b-<i>/usr</i>: all except where <i>/usr</i> is located
</dl>
</pre>
<dt><code>2c</code></p>
<dd> [OS/2, NT] handle Crit. EAs only</p>
<dt><code>2d</code></p>
<dd> <code>arj</code>/DOS compatibility mode</p>
<dl>
<dt>
<dd> 2d1: (OBSOLETE) comment compatibility</dl>
<dt><code>2e</code></p>
<dd> [OS/2, NT] filter Extended attrs </p>
<pre>
<dl><dt><dd>2e.*: pack/unpack system EAs only
2e.ICON?: pack/unpack icons only
2e: disable EAs handling
</dl>
</pre>
<dt><code>2f</code></p>
<dd> Disable comment serialization across multiple volumes</p>
<dt><code>2h</code></p>
<dd> [UNIX] Disable hardlink handling</p>
<dl>
<dt>
<dd> 2h1: Extract hardlinks as symlinks</dl>
<dt><code>2k</code></p>
<dd> Skip century display in dates</p>
<dl>
<dt>
<dd> 2k1: use a non-ambiguous date display format</dl>
<dt><code>2l</code></p>
<dd> [OS/2, NT] treat .LONGNAME EAs as filenames when possible</p>
<dt><code>2o</code></p>
<dd> [UNIX] store/restore file ownership</p>
<dl>
<dt>
<dd> 2o1: Store numeric UID/GID values 2o2: Same as -2o but saves group as well</dl>
<dt><code>2p</code></p>
<dd> Specify process Priority class </p>
<pre>
<dl><dt><dd>OS/2, NT: 2p1...2p4
Linux, FreeBSD: 2p1...2p41
</dl>
</pre>
<dt><code>2r</code></p>
<dd> Revert directory Recursion order</p>
<dt><code>2s</code></p>
<dd> [UNIX] preserve Symlink properties</p>
<dt><code>2x</code></p>
<dd> [OS/2, NT]: eXclude extended attrs</p>
<dl>
<dt>
<dd> 2x.ICON?: ignore icons</dl>
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
<dt><code>Yes</code></p>
<dd> yes</p>
<dt><code>No</code></p>
<dd> no</p>
<dt><code>Quit</code></p>
<dd> abort out of <code>arj</code></p>
<dt><code>Always</code></p>
<dd> always assume yes for current type of query</p>
<dt><code>Skip</code></p>
<dd> always assume no for current type of query</p>
<dt><code>Global</code></p>
<dd> always assume yes for all queries except diskette volume prompts</p>
<dt><code>Command</code></p>
<dd> prompt for and execute one system command</dl>
<h2>ENVIRONMENT</h2>
<p> <code>ARJ_SW</code> = <code>-jyry -jv -i1</code><br />
 <code>ARJ_SW</code> = <i>/etc/arj.cfg</i></p>
<h2>EXIT STATUS</h2>
<dl>
<dt><code>0</code></p>
<dd> Success</p>
<dt><code>1</code></p>
<dd> Warning (specified file to add to archive not found, specified file to list, extract, etc., not found, or answering negatively to &quot;OK to proceed to next volume&#8230;&quot; prompt)</p>
<dt><code>2</code></p>
<dd> Fatal error</p>
<dt><code>3</code></p>
<dd> CRC error (header or file CRC error or bad password)</p>
<dt><code>4</code></p>
<dd> ARJ-SECURITY error or attempt to update an ARJ-SECURED archive</p>
<dt><code>5</code></p>
<dd> Disk full or write error</p>
<dt><code>6</code></p>
<dd> Cannot open archive or file</p>
<dt><code>7</code></p>
<dd> Simple user error (bad parameters)</p>
<dt><code>8</code></p>
<dd> Not enough memory</p>
<dt><code>9</code></p>
<dd> Not an <code>arj</code> archive</p>
<dt><code>10</code></p>
<dd> [DOS] XMS memory error (read or write)</p>
<dt><code>11</code></p>
<dd> User control break</p>
<dt><code>12</code></p>
<dd> Too many chapters (over 250)</dl>
<h2>EXAMPLES</h2>
<dl>
<dt>Add files minus directory structure:</p>
<dd> <code>arj</code> a -e archive *</p>
<dt>Add two files to archive:</p>
<dd> <code>arj</code> a archive <i>name1 name2</i></p>
<dt>Add files to archive with verification:</p>
<dd> <code>arj</code> a -jt archive *</p>
<dt>Add files with maximum compression:</p>
<dd> <code>arj</code> a -jm archive *</p>
<dt>Add several directories of files:</p>
<dd> <code>arj</code> a archive &#8230; <i>dir1 dir2 dir3</i></p>
<dt>Add thousands of files to an archive:</p>
<dd> <code>arj</code> a -hm1 -r archive *</p>
<dt>Add a chapter to an archive:</p>
<dd> <code>arj</code> ac archive <i>/foo/dir/*</i> -r</p>
<dt>Comment archive header only:</p>
<dd> <code>arj</code> c archive -z<i>cmt.fil</i></p>
<dt>Convert standard archive to chapter:</p>
<dd> <code>arj</code> cc archive</p>
<dt>Convert chapter archive to standard:</p>
<dd> <code>arj</code> y archive -jb0</p>
<dt>Delete the last chapter from an archive:</p>
<dd> <code>arj</code> dc archive *</p>
<dt>Strip archive comment only:</p>
<dd> <code>arj</code> c archive -z<i>/dev/null</i></p>
<dt>Extract files from archive:</p>
<dd> <code>arj</code> e archive</p>
<dt>Extract maintaining directory structure:</p>
<dd> <code>arj</code> x archive</p>
<dt>Extract new and newer files without query:</p>
<dd> <code>arj</code> e archive -u -y</p>
<dt>Extract subdirectory from archive:</p>
<dd> <code>arj</code> e archive <i>subdir/*</i> -p1</p>
<dt>Extract files to directory:</p>
<dd> <code>arj</code> x archive <i>destdir/</i> *</p>
<dt>Extract files to directory:</p>
<dd> <code>arj</code> x archive * -htdestdir</p>
<dt>Extract files to directory with space:</p>
<dd> <code>arj</code> x archive &quot;<i>Some Dir/ </i>&quot;</p>
<dt>Extract files to directory with space:</p>
<dd> <code>arj</code> x archive &quot;-ht<i>Some Dir</i>&quot;</p>
<dt>Extract a Win95 archive to plain DOS:</p>
<dd> <code>arj</code> x archive -hf2</p>
<dt>List files in archive:</p>
<dd> <code>arj</code> l archive</p>
<dt>Move files to archive:</p>
<dd> <code>arj</code> m archive <i>*.tex</i></p>
<dt>Move files from archive:</p>
<dd> <code>arj</code> e -d archive <i>*.tex</i></p>
<dt>Recover files from a damaged archive:</p>
<dd> <code>arj</code> x archive -jr</p>
<dt>Test integrity of files in archive:</p>
<dd> <code>arj</code> t archive</p>
<dt>Test multiple <code>arj</code> archives:</p>
<dd> <code>arj</code> t <i>*.arj</i> -hr</p>
<dt>Add files to a multiple volume archive:</p>
<dd> <code>arj</code> a -va <i>/floppy/archive</i> *</p>
<dt>Create up to 999 archive volumes:</p>
<dd> <code>arj</code> a -va <i>/floppy/archive.001</i></p>
<dt>Extract from a multiple volume archive:</p>
<dd> <code>arj</code> x -v <i>/floppy/archive</i></p>
<dt>Create a multiple volume self-extractor:</p>
<dd> <code>arj</code> a -va -je <i>/floppy/archive</i> *</p>
<dt>Convert archive to self-extractor:</p>
<dd> <code>arj</code> y -je1 archive</p>
<dt>Backup dir <i>/foo</i> to dir <i>/floppy</i>:</p>
<dd> <code>arj</code> a <i>/floppy/backup</i> <i>/foo</i> -a1 -b2 -r -vvas -w<i>/foo</i> -js -jt -hk</p>
<dt>Restore backup on dir <i>/floppy</i> to dir <i>/foo</i>:</p>
<dd> <code>arj</code> x <i>/floppy/backup</i> <i>/foo</i> -vv -y</dl>
<h2>SELF-EXTRACTOR ARCHIVES</h2>
<p> If the first two characters of an <code>arj</code> comment are &quot;<code>))</code>&quot; in a self-extractor, then the self-extractor will accept the appended line as its command line. </p>
<p> &quot;<code>)) -o</code>&quot; will force the self-extractor to overwrite existing files.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-rearj/">rearj</a></code>(1), <code><a href="/docs/linux/man/1-unarj/">unarj</a></code>(1), <code><a href="/docs/linux/man/1-arj-register/">arj-register</a></code>(1).</p>
<h2>AUTHOR</h2>
<p> This manual page was written by Ola Lundqvist &lt;opal [at] debian.org&gt; in pod format, then converted by Guillem Jover &lt;guillem [at] debian.org&gt; to nroff format. </p>
<h2>Index</h2>
