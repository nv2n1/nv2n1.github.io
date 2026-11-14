---
title: "pcp-archive(5)"
name: "pcp-archive"
section: "5"
letter: "p"
url: "/docs/linux/man/5-pcp-archive/"
description: "pcp-archive – Archive Files for Performance Co-Pilot"
---

<p><code>pcp-archive</code> &#8211; Archive Files for Performance Co-Pilot</p>
<h2>Synopsis</h2>
<p><i>$PCP_LOG_DIR/pmlogger/*/*.{meta,index,0}</i> <i>$PCP_LOG_DIR/pmmgr/*/*.{meta,index,0}</i> </p>
<h2>Description</h2>
<p>PCP log archives store volumes of historical values of arbitrary Performance Co-Pilot metrics recorded from a single host. Archives are self-contained in the sense that they contain all the important metadata that would be required for off-line or off-site analysis. The format is intended to be stable in order to allow long-term historical storage and processing by current tools. (Compatibility in the other direction &#8211; new files, old tools &#8211; is not as fully assured.) Archives may be read by most PCP client tools, using the <i>-a ARCHIVE</i> option, or dumped raw by <code><a href="/docs/linux/man/1-pmdumplog/">pmdumplog</a></code>(1). Archives may be created by <code><a href="/docs/linux/man/1-pmlogger/">pmlogger</a></code>(1) and bulk-import tools. Archives may be merged, analyzed, and subsampled using specialized tools such as <code><a href="/docs/linux/man/1-pmlogsummary/">pmlogsummary</a></code>(1), <code><a href="/docs/linux/man/1-pmlogreduce/">pmlogreduce</a></code>(1), <code><a href="/docs/linux/man/1-pmlogrewrite/">pmlogrewrite</a></code>(1), and <code><a href="/docs/linux/man/1-pmlogextract/">pmlogextract</a></code>(1). In addition, PCP archives may examined in sets or grouped together into PCP &quot;archive folios&quot;, which are managed by the <code><a href="/docs/linux/man/1-pmafm/">pmafm</a></code>(1) tool. PCP archives consist of several physical files that share a common arbitrary prefix, e.g., <i>myarchive</i>.</p>
<dl>
<dt>myarchive.0, myarchive.1, &#8230;</p>
<dd>Metric values. May grow rapidly.</p>
<dt>myarchive.meta</p>
<dd>Information for PMAPI functions such as <i><a href="/docs/linux/man/3-pmlookupdesc/">pmLookupDesc</a></i>(3) and <i><a href="/docs/linux/man/3-pmgetindom/">pmGetInDom</a></i>(3). May grow in fits and spurts, as logged instances and instance domains vary.</p>
<dt>myarchive.index</p>
<dd>A temporal index, mapping timestamps to offsets in the other files. Grows slowly. </p>
<h2>Common Features</h2>
<p>All three types of files have a similar record-based structure, a convention of network-byte-order (big-endian) encoding, and 32-bit fields for tagging/padding for those records. Strings are stored as 8-bit characters without assuming a specific encoding, so normally ASCII. See also the <code>__pmLog*</code> types in <i>include/pcp/impl.h</i>.</p>
<h3>Record Framing</h3>
<p>The volume and meta files are divided into self-identifying records. <center></p>
<table BORDER>
<tr>
<td>
<table>
<tr VALIGN=top>
<td ALIGN=center>Offset</td>
<td ALIGN=center>Length</td>
<td ALIGN=center>Name
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=3>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=center>0</td>
<td ALIGN=center>4</td>
<td>N, length of record, in bytes, including this field
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=center>4</td>
<td ALIGN=center>N-8</td>
<td>record payload, usually starting with a 32-bit tag
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=center>N-4</td>
<td ALIGN=center>4</td>
<td>N, length of record (again)
</td>
</tr>
</table>
</table>
<p></center></p>
<h3>Archive Log Label</h3>
<p>All three types of files begin with a &quot;log label&quot; header, which identifies the host name, the time interval covered, and a time zone. <center></p>
<table BORDER>
<tr>
<td>
<table>
<tr VALIGN=top>
<td ALIGN=center>Offset</td>
<td ALIGN=center>Length</td>
<td ALIGN=center>Name
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=3>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=center>0</td>
<td ALIGN=center>4</td>
<td>tag, PM_LOG_MAGIC | PM_LOG_VERS02=0x50052602
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=center>4</td>
<td ALIGN=center>4</td>
<td>pid of pmlogger process that wrote file
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=center>8</td>
<td ALIGN=center>4</td>
<td>log start time, seconds part (past UNIX epoch)
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=center>12</td>
<td ALIGN=center>4</td>
<td>log start time, microseconds part
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=center>16</td>
<td ALIGN=center>4</td>
<td>current log volume number (or -1=.meta, -2=.index)
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=center>20</td>
<td ALIGN=center>64</td>
<td>name of collection host
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=center>80</td>
<td ALIGN=center>40</td>
<td>time zone string ($TZ environment variable)
</td>
</tr>
</table>
</table>
<p></center> </p>
<p> All fields, except for the current log volume number field, match for all archive-related files produced by a single run of the tool.</p>
<h2>Archive Volume (.0, .1, &#8230;) Records</h2>
<h3>pmResult</h3>
<p>After the archive log label record, an archive volume file contains metric values corresponding to the <i>pmResult</i> set of one <i>pmFetch</i> operation, which is almost identical to the form on disk. The record size may vary according to number of PMIDs being fetched, the number of instances for their domains. File size is limited to 2GB, due to storage of 32-bit offsets within the .index file. <center></p>
<table BORDER>
<tr>
<td>
<table>
<tr VALIGN=top>
<td ALIGN=center>Offset</td>
<td ALIGN=center>Length</td>
<td ALIGN=center>Name
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=3>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=center>0</td>
<td ALIGN=center>4</td>
<td>timestamp, seconds part (past UNIX epoch)
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=center>4</td>
<td ALIGN=center>4</td>
<td>timestamp, microseconds part
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=center>8</td>
<td ALIGN=center>4</td>
<td>number of PMIDs with data following
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=center>12</td>
<td ALIGN=center>M</td>
<td>pmValueSet #0
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=center>12+M</td>
<td ALIGN=center>N</td>
<td>pmValueSet #1
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=center>12+M+N</td>
<td ALIGN=center>&#8230;</td>
<td>&#8230;
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=center>NOP</td>
<td ALIGN=center>X</td>
<td>pmValueBlock #0
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=center>NOP+X</td>
<td ALIGN=center>Y</td>
<td>pmValueBlock #1
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=center>NOP+X+Y</td>
<td ALIGN=center>&#8230;</td>
<td>&#8230;
</td>
</tr>
</table>
</table>
<p></center> </p>
<p> Records with a number-of-PMIDs equal to zero are &quot;markers&quot;, and may represent interruptions, missing data, or time discontinuities in logging.</p>
<h3>pmValueSet</h3>
<p>This subrecord represents the measurements for one metric. </p>
<p> <center></p>
<table BORDER>
<tr>
<td>
<table>
<tr VALIGN=top>
<td ALIGN=center>Offset</td>
<td ALIGN=center>Length</td>
<td ALIGN=center>Name
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=3>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=center>0</td>
<td ALIGN=center>4</td>
<td>PMID
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=center>4</td>
<td ALIGN=center>4</td>
<td>number of values
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=center>8</td>
<td ALIGN=center>4</td>
<td>storage mode, PM_VAL_INSITU=0 or PM_VAL_DPTR=1
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=center>12</td>
<td ALIGN=center>M</td>
<td>pmValue #0
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=center>12+M</td>
<td ALIGN=center>N</td>
<td>pmValue #1
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=center>12+M+N</td>
<td ALIGN=center>&#8230;</td>
<td>&#8230;
</td>
</tr>
</table>
</table>
<p></center> </p>
<p> The metric-description metadata for PMIDs is found in the .meta files. These entries are not timestamped, so the metadata is assumed to be unchanging throughout the archiving session.</p>
<h3>pmValue</h3>
<p>This subrecord represents one measurement for one instance of the metric. It is a variant type, depending on the parent pmValueSet&#8217;s value-format field. This allows small numbers to be encoded compactly, but retain flexibility for larger or variable-length data to be stored later in the pmResult record. </p>
<p> <center></p>
<table BORDER>
<tr>
<td>
<table>
<tr VALIGN=top>
<td ALIGN=center>Offset</td>
<td ALIGN=center>Length</td>
<td ALIGN=center>Name
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=3>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=center>0</td>
<td ALIGN=center>4</td>
<td>number in instance-domain (or PM_IN_NULL=-1)
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=center>4</td>
<td ALIGN=center>4</td>
<td>value (INSITU) <i>or</i>
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=center></td>
<td ALIGN=center></td>
<td>offset in pmResult to our pmValueBlock (DPTR)
</td>
</tr>
</table>
</table>
<p></center> </p>
<p> The instance-domain metadata for PMIDs is found in the .meta files. Since the numeric mappings may change during the lifetime of the logging session, it is important to match up the timestamp of the measurement record with the corresponding instance-domain record. That is, the instance-domain corresponding to a measurement at time T are the records with largest timestamps T&#8217; &lt;= T.</p>
<h3>pmValueBlock</h3>
<p>Instances of this subrecord are placed at the end of the <i>pmValueSet</i>, after all the <i>pmValue</i> subrecords. Iff needed, they are padded at the end to the next-higher 32-bit boundary. </p>
<p> <center></p>
<table BORDER>
<tr>
<td>
<table>
<tr VALIGN=top>
<td ALIGN=center>Offset</td>
<td ALIGN=center>Length</td>
<td ALIGN=center>Name
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=3>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=center>0</td>
<td ALIGN=center>1</td>
<td>value type (same as <i>pmDesc.type</i>)
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=center>1</td>
<td ALIGN=center>3</td>
<td>4 + N, the length of the subrecord
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=center>4</td>
<td ALIGN=center>N</td>
<td>bytes that make up the raw value
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=center>4+N</td>
<td ALIGN=center>0-3</td>
<td>padding (not included in the 4+N length field)
</td>
</tr>
</table>
</table>
<p></center> </p>
<p> Note that for <i>PM_TYPE_STRING</i>, the length includes an explicit NUL terminator byte. For <i>PM_TYPE_EVENT</i>, the value bytestring is further structured.</p>
<h3>pmEventArray</h3>
<p><i>(TBD)</i></p>
<h2>METADATA FILE (.meta) RECORDS</h2>
<p>After the archive log label record, the metadata file contains interleaved metric-description and timestamped instance-domain descriptors. File size is limited to 2GB, due to storage of 32-bit offsets within the .index file. Unlike the archive volumes, these records are not forced to 32-bit alignment! See also <i>src/libpcp/src/logmeta.c</i>.</p>
<h3>pmDesc</h3>
<p>Instances of this record represent the metric description, giving a name, type, instance-domain identifier, and a set of names to each PMID used in the archive volume. </p>
<p> <center></p>
<table BORDER>
<tr>
<td>
<table>
<tr VALIGN=top>
<td ALIGN=center>Offset</td>
<td ALIGN=center>Length</td>
<td ALIGN=center>Name
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=3>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=center>0</td>
<td ALIGN=center>4</td>
<td>tag, TYPE_DESC=1
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=center>4</td>
<td ALIGN=center>4</td>
<td>pmid
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=center>8</td>
<td ALIGN=center>4</td>
<td>type (PM_TYPE_*)
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=center>12</td>
<td ALIGN=center>4</td>
<td>instance domain number
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=center>16</td>
<td ALIGN=center>4</td>
<td>semantics of value (PM_SEM_*)
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=center>20</td>
<td ALIGN=center>4</td>
<td>units: bit-packed pmUnits
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=center>4</td>
<td ALIGN=center>4</td>
<td>number of alternative names for this PMID
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=center>28</td>
<td ALIGN=center>4</td>
<td>N: number of bytes in this name
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=center>32</td>
<td ALIGN=center>N</td>
<td>bytes of the name, no NUL terminator nor padding
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=center>32+N</td>
<td ALIGN=center>4</td>
<td>N2: number of bytes in next name
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=center>36+N</td>
<td ALIGN=center>N2</td>
<td>bytes of the name, no NUL terminator nor padding
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=center>&#8230;</td>
<td ALIGN=center>&#8230;</td>
<td>&#8230;
</td>
</tr>
</table>
</table>
<p></center></p>
<h3>pmLogIndom</h3>
<p>Instances of this record represent the number-string mapping table of an instance domain. The instance domain number will have already been mentioned in a prior <i>pmDesc</i> record. Since new instances may appear over a long archiving run, these records are timestamped, and must be searched when decoding <i>pmResult</i> records from the main archive volumes. Instance names may be reused between instance numbers, so an offset-based string table is used that could permit sharing.<br />
&nbsp;<wbr> <center></p>
<table BORDER>
<tr>
<td>
<table>
<tr VALIGN=top>
<td ALIGN=center>Offset</td>
<td ALIGN=center>Length</td>
<td ALIGN=center>Name
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=3>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=center>0</td>
<td ALIGN=center>4</td>
<td>tag, TYPE_INDOM=2
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=center>4</td>
<td ALIGN=center>4</td>
<td>timestamp, seconds part (past UNIX epoch)
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=center>8</td>
<td ALIGN=center>4</td>
<td>timestamp, microseconds part
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=center>12</td>
<td ALIGN=center>4</td>
<td>instance domain number
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=center>16</td>
<td ALIGN=center>4</td>
<td>N: number of instances in domain, normally &gt;0
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=center>20</td>
<td ALIGN=center>4</td>
<td>first instance number
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=center>24</td>
<td ALIGN=center>4</td>
<td>second instance number (if appropriate)
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=center>&#8230;</td>
<td ALIGN=center>&#8230;</td>
<td>&#8230;
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=center>20+4*N</td>
<td ALIGN=center>4</td>
<td>first offset into string table (see below)
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=center>20+4*N+4</td>
<td ALIGN=center>4</td>
<td>second offset into string table (etc.)
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=center>&#8230;</td>
<td ALIGN=center>&#8230;</td>
<td>&#8230;
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=center>20+8*N</td>
<td ALIGN=center>M</td>
<td>base of string table, containing
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=center></td>
<td ALIGN=center></td>
<td>packed, NUL-terminated instance names
</td>
</tr>
</table>
</table>
<p></center> </p>
<p> Records of this form <i>replace</i> the existing instance-domain: prior records are not searched for resolving instance numbers in measurements after this timestamp.<br />
&nbsp;<wbr></p>
<h2>INDEX FILE (.index) RECORDS</h2>
<p>After the archive log label record, the temporal index file contains a plainly concatenated, unframed group of tuples, which relate timestamps to 32-bit seek offsets in the volume and meta files. (This limits those files to 2GB in size.) These records are fixed-size, fixed-format, and are <i>not</i> enclosed in the standard length/payload/length wrapper: they just take up the entire remainder of the .index file. See also <i>src/libpcp/src/logutil.c</i>. </p>
<p> <center></p>
<table BORDER>
<tr>
<td>
<table>
<tr VALIGN=top>
<td ALIGN=center>Offset</td>
<td ALIGN=center>Length</td>
<td ALIGN=center>Name
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=3>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=center>0</td>
<td ALIGN=center>4</td>
<td>event time, seconds part (past UNIX epoch)
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=center>4</td>
<td ALIGN=center>4</td>
<td>event time, microseconds part
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=center>8</td>
<td ALIGN=center>4</td>
<td>archive volume number (0&#8230;N)
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=center>12</td>
<td ALIGN=center>4</td>
<td>byte offset in .meta file of pmDesc or pmLogIndom
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=center>16</td>
<td ALIGN=center>4</td>
<td>byte offset in archive volume file of pmResult
</td>
</tr>
</table>
</table>
<p></center> </p>
<p> Since temporal indexes are optional, and exist only to speed up time-wise random access of metrics and their metadata, index records are emitted only intermittently. An archive reader program should not presume any particular rate of data flow into the index. However, common events that may trigger a new temporal-index record include changes in instance-domains, switching over to a new archive volume, just starting or stopping logging. One reliable invariant however is that, for each index entry, there are to be no meta or archive-volume records with a timestamp after that in the index, but physically before the byte-offset in the index.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-pcpintro/">PCPIntro</a></code>(1), <code><a href="/docs/linux/man/3-pmapi/">PMAPI</a></code>(3), <code><a href="/docs/linux/man/1-pmlogger/">pmlogger</a></code>(1), <code><a href="/docs/linux/man/1-pmdumplog/">pmdumplog</a></code>(1), <code><a href="/docs/linux/man/1-pmafm/">pmafm</a></code>(1), <code><a href="/docs/linux/man/5-pcp-conf/">pcp.conf</a></code>(5), and <code><a href="/docs/linux/man/5-pcp-env/">pcp.env</a></code>(5). </p>
