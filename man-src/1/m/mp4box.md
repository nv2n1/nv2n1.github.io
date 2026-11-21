---
title: "mp4box(1)"
name: "mp4box"
section: "1"
letter: "m"
url: "/docs/linux/man/1-mp4box/"
description: "MP4Box – MPEG-4 Systems Toolbox"
---

<h2>NAME</h2>
<p> MP4Box &#8211; MPEG-4 Systems Toolbox</p>
<h2>SYNOPSIS</h2>
<p> <code>MP4Box</code> [options]<i>&nbsp;<wbr>file</i>&nbsp;<wbr>[options] </p>
<h2>DESCRIPTION</h2>
<p> MP4Box is a multi-purpose command line tool to create and edit MPEG-4 Systems presentations and manipulate ISO-media files (MP4, 3GP, MOV). </p>
<p> MP4Box supports file conversion from various raw formats and IsoMedia/AVI/MPEG-PS/OGG containers, file hinting for RTP streaming for QuickTime compatible streaming servers, file interleaving, file fragmentation and track extraction. </p>
<p> MP4Box also provides dump tools used to inspect file layout, RTP hint tracks, SDP information, scene composition. It may also be used to convert to and from BT/XMT-A/VRML/X3D. </p>
<p> MP4Box also features MPEG-4 Systems encoders and decoders for BIFS and OD tools. </p>
<p> MP4Box doesn&#8217;t expect any particular order in options at prompt.</p>
<h2>GETTING HELP WITH MP4Box</h2>
<dl>
<dt><code>-h [type]</code></dt>
<dd> prints help screen. &quot;type&quot; can be one of &quot;general&quot;, &quot;hint&quot;, &quot;import&quot;, &quot;encode&quot;, &quot;extract&quot;, &quot;dump&quot;, &quot;swf&quot;, &quot;meta&quot;, &quot;crypt&quot;, &quot;format&quot;, &quot;rtp&quot;, &quot;live&quot; for specific help.</dd>
<dt><code>-version</code></dt>
<dd> prints version of MP4Box.</dd>
<dt><code>-noprog</code></dt>
<dd> disable progress reports.</dd>
<dt><code>-quiet</code></dt>
<dd> quiet mode (no log info).</dd>
<dt><code>-v</code></dt>
<dd> verbose mode (more log info).</dd>
<dt><code>-strict-error</code></dt>
<dd> exits after the first error is reported.</dd>
<dt><code>-nodes</code></dt>
<dd> lists supported MPEG-4 Systems nodes in MP4Box current build.</dd>
<dt><code>-node NodeName</code></dt>
<dd> prints the node syntax. Each field is listed as<br />
 <i>eventType fieldType fieldName defaultValue</i><br />
 and field quantization information and quantization bounds if any.</dd>
<dt><code>-xnodes</code></dt>
<dd> lists supported X3D nodes in MP4Box current build.</dd>
<dt><code>-xnode NodeName</code></dt>
<dd> prints the X3D node syntax. Each field is listed as</dd>
<dt><code>-snodes</code></dt>
<dd> lists supported SVG/LASeR nodes in MP4Box current build.</dd></dl>
<h2>GENERAL OPTIONS</h2>
<dl>
<dt><code>-inter duration</code></dt>
<dd> interleaves media data in chunks of the maximum specified duration (expressed in milliseconds) and prepare file for HTTP/FTP streaming. By default MP4Box always stores with 0.5 second interleaving. An interleaving value of &#8216;0&#8217; stores without interleaving (meta-data then track after track).<br />
 <code>-old-inter duration</code> same as -inter but without drift adjustment<br />
 <code>NOTE: Track Edit Lists are ignored when performing interleaving.</code></dd>
<dt><code>-flat</code></dt>
<dd> stores file with all media data first, non interleaved. If used when creating a new file, no temporary file is created (faster storage).</dd>
<dt><code>-frag duration</code></dt>
<dd> fragments file using ISO-Media movie fragments. Tracks will be fragmented so that no track run exceeds the specified duration (expressed in milliseconds). Disables interleaving.</dd>
<dt><code>-out&nbsp;<wbr>&lt;filename&gt;</code></dt>
<dd> specifies output file name.</dd>
<dt><code>-tmp&nbsp;<wbr>&lt;dirname&gt;</code></dt>
<dd> specifies driectory for temporary storage. If not set, temporary storage is OS-dependent.</dd>
<dt><code>-ffspace size</code></dt>
<dd> inserts free space before moof in fragmented files.</dd>
<dt><code>-nosys</code></dt>
<dd> removes all MPEG-4 Systems information from the file but keeps an empty IOD for MPEG-4 Profile [at] Level indications. alias: -no-sys</dd>
<dt><code>-no-iod</code></dt>
<dd> removes InitialObjectDescriptor from file.</dd>
<dt><code>-isma</code></dt>
<dd> rewrites the file as an ISMA 1.0 Audio/Video file (all systems info rewritten) with proper clock references.</dd>
<dt><code>-ismax</code></dt>
<dd> rewrites the file as an ISMA 1.0 Audio/Video file (all systems info rewritten) with ISMA clock references (streams not explicetly synchronized).<br />
 <code>NOTE: Seeking may be broken with some players (in ISMA, audio and video streams do not depend on main scene clock).</code></dd>
<dt><code>-3gp</code></dt>
<dd> rewrites the file as a 3GP file (no more MPEG-4 Systems specific info). This option is turned on by default when input file extension is .3gp or .3g2.</dd>
<dt><code>-ipod</code></dt>
<dd> rewrites the file for iPod.</dd>
<dt><code>-brand ABCD[:v]</code></dt>
<dd> sets major brand of file, with optional version.</dd>
<dt><code>-ab ABCD</code></dt>
<dd> adds given brand to file&#8217;s alternate brand list.</dd>
<dt><code>-rb ABCD</code></dt>
<dd> removes given brand to file&#8217;s alternate brand list.</dd>
<dt><code>-cprt string</code></dt>
<dd> adds string copyright notice to file.</dd>
<dt><code>-chap chap_file</code></dt>
<dd> adds chapter information contained in chap_file to movie. For more details on chapter file syntax, cf <a rel="nofollow" href="http://gpac.sourceforge.net/auth_mp4box.php.">http://gpac.sourceforge.net/auth_mp4box.php.</a></dd>
<dt><code>-rem trackID</code></dt>
<dd> removes given track from file &#8211; can be specified multiple times.</dd>
<dt><code>-enable trackID</code></dt>
<dd> enables given track.</dd>
<dt><code>-disable trackID</code></dt>
<dd> disables given track.</dd>
<dt><code>-new</code></dt>
<dd> forces creation of a new destination file.</dd>
<dt><code>-lang [tkID=]LAN</code></dt>
<dd> sets the language of all tracks or the given track. LAN is the ISO 639-2 3 character code.</dd>
<dt><code>-delay [tkID=]delay_ms</code></dt>
<dd> sets the delay in milliseconds of all tracks or the given track. LAN is the ISO 639-2 3 character code.</dd>
<dt><code>-par tkID=PAR</code></dt>
<dd> sets visual track pixel aspect ratio (PAR=Num:Den or &quot;none&quot;).</dd>
<dt><code>-name tkID=name</code></dt>
<dd> sets track handler name.</dd>
<dt><code>-itags tag1[:tag2]</code></dt>
<dd> sets iTunes tags to file &#8211; more info: MP4Box -tag-list.</dd>
<dt><code>-split time_in_seconds</code></dt>
<dd> splits in files of desired maximum duration. This will remove all MPEG-4 Systems media.</dd>
<dt><code>-split-size size_in_kilobytes</code></dt>
<dd> splits in files of desired maximum size. This will remove all MPEG-4 Systems media. Alias: -splits</dd>
<dt><code>-split-chunk start:end</code></dt>
<dd> extracts a new file from specified start to end times (in seconds). This will remove all MPEG-4 Systems media. Alias: -splitx</dd>
<dt><code>-splitz start:end</code></dt>
<dd> same as -split-chunk option, but adjust end time to be juste before the last rap found in the chunk.</dd>
<dt><code>-split-rap start:end</code></dt>
<dd> splits in files begining at each RAP. This will remove all MPEG-4 Systems media. Alias: -splitr</dd>
<dt><code>-group-add fmt</code></dt>
<dd> creates a new grouping information in the file. Format is a colon-separated list of following options:<br />
 refTrack=ID: ID of the track used as a group reference. If not set, the track will belong to the same group as the previous trackID specified. If 0 or no previous track specified, a new alternate group will be created.<br />
 switchID=ID: ID of the switch group to create. If 0, a new ID will be computed for you. If &lt;0, disables SwitchGroup.<br />
 criteria=string: list of space-separated 4CCs.<br />
 trackID=ID: ID of the track to add to this group.<br />
 *WARNING* Options modify state as they are parsed: trackID=1:criteria=lang:trackID=2 is different from: criteria=lang:trackID=1:trackID=2. <code>-group-rem-track ID</code> removes track from its group.</dd>
<dt><code>-group-rem ID</code></dt>
<dd> removes the track&#8217;s group.</dd>
<dt><code>-group-clean</code></dt>
<dd> removes all group information from all tracks.</dd>
<dt><code>-ref id:XXXX:refID</code></dt>
<dd> adds a reference of type 4CC from track ID to track refID.</dd>
<dt><code>-dash DUR</code></dt>
<dd> enables DASH-ing of the file with a segment duration of DUR.</dd>
<dt><code>-rap</code></dt>
<dd> segments begin with random access points.</dd>
<dt><code>-frags-per-sidx N</code></dt>
<dd> sets the number of segments to be written in each SIDX box.</dd>
<dt><code>-segment-name name</code></dt>
<dd> sets the segment name for generated segments.</dd>
<dt><code>-segment-ext name</code></dt>
<dd> sets the segment extension name. Default is m4s.</dd>
<dt><code>-url-template</code></dt>
<dd> uses UrlTemplate instead of explicit sources in segments.</dd>
<dt><code>-daisy-chain</code></dt>
<dd> Uses daisy-chain SIDX instead of hierarchical. Ignored if frags/sidx is 0.</dd>
<dt><code>-dash-ctx FILE</code></dt>
<dd> Stores/restore DASH timing from FILE.</dd>
<dt><code>-dash-ts-prog N</code></dt>
<dd> Program_number to be considered in case of an MPTS input file. </dd>
<p> <code>When input file is an ISO-Media file (QT, MP4, 3GP), if no output is specified THE INPUT FILE IS OVERWRITTEN.</code></dl>
<h2>HINTING OPTIONS</h2>
<dl>
<dt><code>-hint</code></dt>
<dd> hint the file for RTP/RTSP sessions. Payload type is automatically detected and configured unless forced through one of MPEG-4 Generic RTP payload.</dd>
<dt><code>-mtu size</code></dt>
<dd> specifies Maximum Transmission Unit size in bytes (eg maximum RTP packet size). Default size is 1500 bytes (Ethernet MTU). This must be choosen carefully: specifying too large packets will result in undesired packet fragmentation at UDP layer while specifying too small packets will result in RTP header overhead.</dd>
<dt><code>-copy</code></dt>
<dd> forces hinted data to be copied to the hint track instead of simply referenced. This speeds up RTP packet construction at the server side but results in much bigger files.</dd>
<dt><code>-tight</code></dt>
<dd> performs sample-based interleaving of media tracks and hint tracks. This should reduce disk seeks at server side (depending on server implementation) but results in a bigger file.</dd>
<dt><code>-multi [maxptime]</code></dt>
<dd> enables Access Units concatenation in RTP packets if possible. maxptime is optional and specifies the maximum packet duration in milliseconds (default 100).</dd>
<dt><code>-rate ck_rate</code></dt>
<dd> specifies the rtp rate in Hz when no default rate for payload. Default value is 90000 (MPEG rtp rates).</dd>
<dt><code>-mpeg4</code></dt>
<dd> forces usage of the MPEG-4 generic payload whenever possible. Media tracks without a mapping to MPEG-4 Systems cannot use this.</dd>
<dt><code>-latm</code></dt>
<dd> forces usage of the LATM payload for AAC audio.</dd>
<dt><code>-static</code></dt>
<dd> enables usage of static RTP payload IDs for streams with official payload IDs. By default MP4Box always uses dynamic payload IDs for maximum interoperability, some players having troubles with static ones.</dd></dl>
<p> <code>MPEG-4 Generic Payload Options (Experts only)</code></p>
<dl>
<dt>
</dt><dd> <code>-ocr</code> forces all media tracks in the file to be served synchronized. This is needed because most streaming servers don&#8217;t support desynchronized tracks in a single file. Be extremelly carefull when designing MPEG-4 interactive presentations for streaming since you will have to take care of the streaming server capabilities&#8230; MP4Box generates warnings when the file timeline can be ambiguously interpreted by the server.</dd>
<dt>
</dt><dd> <code>-rap</code> signals Access Units random access flag in RTP packets. This is usually only needed for streaming of MPEG-4 Systems streams.</dd>
<dt>
</dt><dd> <code>-ts</code> signals Access Units Time Stamps (CTS and DTS) in RTP packets.</dd>
<dt>
</dt><dd> <code>-size</code> signals Access Units size in RTP packets.</dd>
<dt>
</dt><dd> <code>-idx</code> signals Access Units indexes (sequence numbers) in RTP packets.</dd>
<dt>
</dt><dd> <code>-multi</code> enables Access Units concatenation in RTP packets (-ts, -size and -idx are selected if needed).</dd>
<dt>
</dt><dd> <code>-iod</code> prevents system tracks embedding in IOD (ISMA-like IOD) when generating in SDP. MP4Box automatically detects ambiguous (ISMA/non-ISMA) files but nobody&#8217;s perfect. This shouldn&#8217;t be used with -isma option.</dd>
<dt><code>-add-sdp string</code></dt>
<dd> adds string to movie SDP or track SDP (tkID:string, where tkID is the OD of the hint track or its media track). This takes care of SDP line reordering, but not of SDP content validity.</dd>
<dt><code>-unhint</code></dt>
<dd> removes all hint tracks and other hinting info from the file.</dd></dl>
<h2>IMPORT OPTIONS</h2>
<dl>
<dt><code>-add &lt;src_file&gt;</code></dt>
<dd> adds all src_file tracks to input file, creating it if not exisiting. Up to 20 cumulated -add operations can be used. Supported syntaxes are:<br />
 file#video: imports first video track from src_file.<br />
 file#audio: imports first audio track from src_file.<br />
 file#trackID=ID or file#ID: imports given trackfrom src_file. To get a listing of tracks in input file, use -info [ID]<br />
 [;lang=LAN]: specifies language of imported media.<br />
 [;delay=delay_ms]: specifies initial delay in milliseconds of imported media.</dd>
<dt><code>-cat &lt;src_file&gt;</code></dt>
<dd> concatenates all src_file tracks to input file, creating it if not exisiting. Media samples are added at the end of existing compatible tracks. If no compatible track is found for a media it is created. Up to 20 cumulated -cat operations can be used. Syntax is the same as -add.</dd>
<dt><code>-force-cat</code></dt>
<dd> skips media configuration check when concatenating file.</dd>
<dt><code>-keepsys</code></dt>
<dd> by default all MPEG-4 systems media are removed with -add and -cat. This option will avoid removing them from final file.</dd>
<dt><code>-keep-all</code></dt>
<dd> keeps all existing tracks when add file.</dd>
<dt><code>-dref</code></dt>
<dd> keeps media data in original file an only imports meta-data (frame timing, size and random access). </dd>
<dt><code>NOTE</code></dt>
<dd> Data referencing may fail with some AVI because it requires the framed data (eg an MP4 sample) to be continuous in the original file, which is not always the case depending on the original interleaving.</dd>
<dt><code>-no-drop</code></dt>
<dd> forces constant FPS when importing AVI video. By default non coded frames (n-vop) are removed at import time, resulting in a variable frame-rate media.</dd>
<dt><code>-packed</code></dt>
<dd> for CMP/M4V (raw MPEG-4 Visual), forces packed-bitstream mode (removes all n-vops and import at constant frame rate).</dd>
<dt><code>-sbr</code></dt>
<dd> imports AAC as AAC-SBR, with backward compatible signaling (non AAC-SBR decoders should be able to play it).</dd>
<dt><code>-sbrx</code></dt>
<dd> imports AAC as AAC-SBR, with non-backward compatible signaling (non AAC-SBR decoders will not be able to play it).</dd>
<dt><code>-ovsbr</code></dt>
<dd> imports AAC as AAC-SBR with oversample SBR.</dd>
<dt><code>-ps</code></dt>
<dd> imports AAC as AAC-PS, with backward compatible signaling of AAC-PS.</dd>
<dt><code>-psx</code></dt>
<dd> imports AAC as AAC-PS, with non-backward compatible signaling (non AAC-PS decoders will not be able to play it).</dd>
<dt><code>-fps FrameRate</code></dt>
<dd> overrides the input video frame rate or specifies it for SUB subtitles.</dd>
<dt><code>-mpeg4</code></dt>
<dd> forces using MPEG-4 sample descriptions rather than 3GP ones (3GP2 QCELP/EVRC/SMV audio only).</dd>
<dt><code>-agg N</code></dt>
<dd> aggregates N audio frames in 1 sample (3GP media only). Maximum possible value is 15, and default value is 1 (no aggregation).</dd></dl>
<h2>ENCODING OPTIONS</h2>
<dl>
<dt><code>-mp4</code></dt>
<dd> specifies input file is for encoding. Supported inputs are BT/XMT-A/WRL/SWF files. Output file name is by default the input file name without extensions plus &quot;.mp4&quot; extension.</dd>
<dt><code>-def</code></dt>
<dd> encodes DEF&#8217;ed nodes and routes with their textual names.</dd>
<dt><code>-log</code></dt>
<dd> generates BIFS encoder log file.</dd>
<dt><code>-ms file</code></dt>
<dd> specifies file for track importing &#8211; by default FILE.mp4 is used when encoding FILE.bt (in-place rewrite). This option is only needed if you don&#8217;t provide a proper muxInfo per stream in the BT/XMT file.</dd>
<dt><code>-sync time</code></dt>
<dd> forces BIFS random access point generation every time milliseconds. Cannot be used with -shadow. WARNING: this may result in weird behavior of your presentation since a BIFS random access point restarts all media currently running in the scene (EXPERTS ONLY &#8211; DANGEROUS). Cannot be used with -shadow.</dd>
<dt><code>-shadow time</code></dt>
<dd> forces BIFS shadow random access points generation every time milliseconds. Shadow samples are random access points that can be used instead of non random access points when seeking. WARNING: this may be not supported by some players (EXPERTS ONLY &#8211; DANGEROUS). Cannot be used with -sync.</dd>
<dt><code>-ctx-in file</code></dt>
<dd> specifies initial context (MP4/BT/XMTA) for chunk processing. Input file must then be a command-only file: no IOD, and no implicit commands (commands without &#8216;AT&#8217;).</dd>
<dt><code>-ctx-out file</code></dt>
<dd> specifies output file of updated context (MP4/BT/XMTA) in chunk processing mode. This is optional, chunk processing doesn&#8217;t need to store the final context.</dd>
<dt><code>-resolution res</code></dt>
<dd> LASeR resolution factor (-8 to 7, default 0). All coords are multiplied by 2^res before truncation.</dd>
<dt><code>-coord-bits bits</code></dt>
<dd> bits used for encoding truncated coordinates in LASeR. (0 to 31, default 12)</dd>
<dt><code>-scale-bits bits</code></dt>
<dd> bits used for encoding truncated scales in LASeR. (0 to 4, default 0)</dd>
<dt><code>-auto-quant res</code></dt>
<dd> Use automatic LASeR quantification. resolution is given as if using -resolution but coord-bits and scale-bits are infered.</dd></dl>
<h2>ISMACRYPT OPTIONS</h2>
<dl>
<dt><code>-crypt drm_file</code></dt>
<dd> crypts a specific track using ISMA AES CTR 128.</dd>
<dt><code>-decrypt [drm_file]</code></dt>
<dd> decrypts a specific track using ISMA AES CTR 128. drm_file can be omitted if keys are in file.</dd>
<dt><code>-set-kms [tkID=]kms_uri</code></dt>
<dd> changes KMS location for all tracks or a given one if tkID is specified.</dd>
<dt><code>DRM file syntax for GPAC ISMACryp</code></dt>
<dd> File is XML and shall start with xml header. File root is an &quot;ISMACryp&quot; element. File is a list of &quot;ISMACrypTrack&quot; elements.<br />
 ISMACrypTrack attributes:<br />
 TrackID: ID of track to en/decrypt.<br />
 key: AES-128 key formatted (hex string 0x +32 chars.<br />
 salt: CTR IV salt key (64 bits) (hex string 0x +16 chars.<br />
 Encryption only attributes<br />
 Scheme_URI: URI of scheme used.<br />
 KMS_URI: URI of key management system &#8211; &#8216;self&#8217; writes key and salt in the file.<br />
 selectiveType selective encryption type &#8211; understood values are &quot;None&quot;: all samples encrypted (default), &quot;RAP&quot;: only encrypts random access units, &quot;Non-RAP&quot;: only encrypts non-random access units, &quot;Rand&quot;: random selection is performed&quot;, &quot;X&quot;: Encrypts every first sample out of X, &quot;RandX&quot;: Encrypts one random sample out of X.<br />
 ipmpType: IPMP Signaling Type: None, IPMP, IPMPX.<br />
 ipmpDescriptorID: IPMP_Descriptor ID to use if IPMP(X) is used. If not set MP4Box will generate one for you. </dd>
</dl>
<h2>EXTRACTING OPTIONS</h2>
<dl>
<dt><code>-raw TrackID</code></dt>
<dd> extracts given track in native format when supported.</dd>
<dt><code>-raws TrackID</code></dt>
<dd> extract each track sample to a file. Note: &#8216;TrackID:N&#8217; extracts Nth sample of the track.</dd>
<dt><code>-nhnt TrackID</code></dt>
<dd> extracts given track in NHNT format. All track types except ObjectDescriptors tracks can be exported.</dd>
<dt><code>-nhml TrackID</code></dt>
<dd> extracts track in nhml format (XML nhnt). All track types except ObjectDescriptors tracks can be exported.</dd>
<dt><code>-single TrackID</code></dt>
<dd> extracts given track to a new mp4 file with a single track.</dd>
<dt><code>-avi TrackID</code></dt>
<dd> extracts visual track to an avi file.</dd>
<dt><code>-qcp TrackID</code></dt>
<dd> same as &#8216;-raw&#8217; but defaults to QCP file format for AVRC and SMV audio codecs.</dd>
<dt><code>-aviraw TK</code></dt>
<dd> extracts AVI track to its raw format. TK can be one of &quot;video&quot;, &quot;audio&quot; or &quot;audioN&quot; for multi-track avi files (cf &#8216;-info&#8217;).</dd>
<dt><code>-saf</code></dt>
<dd> remux file to SAF multiplex.</dd>
<dt><code>-dvbhdemux</code></dt>
<dd> demux DVB-H file into IP Datagrams.</dd>
<dt><code>-diod</code></dt>
<dd> extracts file IOD in raw format when supported.</dd></dl>
<h2>DUMP OPTIONS</h2>
<dl>
<dt><code>-info [TrackID]</code></dt>
<dd> prints movie and tracks information. If TrackID specified, dumps only extended track info. If input file is not an IsoMedia file, lists known tracks for import.</dd>
<dt><code>-bt</code></dt>
<dd> dumps complete scene in a BT file. This will remove unknown MPEG4 nodes.</dd>
<dt><code>-xmt</code></dt>
<dd> dumps complete scene in an XMT-A file. This will remove unknown MPEG4 nodes.</dd>
<dt><code>-wrl</code></dt>
<dd> dumps complete scene in an VRML97 WRL file. This will remove unknown VRML97 nodes.</dd>
<dt><code>-x3d</code></dt>
<dd> dumps complete scene in an X3D XML file. This will remove unknown X3D nodes.</dd>
<dt><code>-x3dv</code></dt>
<dd> dumps complete scene in an X3D Text (VRML) file. This will remove unknown X3D nodes.</dd>
<dt><code>-lsr</code></dt>
<dd> dumps complete scene in a LASeR+XML file.</dd>
<dt><code>-diso</code></dt>
<dd> creates XML image of the file atoms.</dd>
<dt><code>-drtp</code></dt>
<dd> creates XML image of all hint tracks samples of a hinted mp4 file.</dd>
<dt><code>-dts</code></dt>
<dd> prints sample timing to text output.</dd>
<dt><code>-dcr</code></dt>
<dd> creates XML image of all ISMACryp tracks samples of an mp4 file.</dd>
<dt><code>-sdp</code></dt>
<dd> creates SDP file associated with a hinted mp4 file.</dd>
<dt><code>-dump-cover</code></dt>
<dd> Extracts cover art if any.</dd>
<dt><code>-dump-chap</code></dt>
<dd> Extracts chapter list to file if any.</dd>
<dt><code>-ttxt</code></dt>
<dd> converts input subtitle to GPAC TTXT format.</dd>
<dt><code>-ttxt trackID</code></dt>
<dd> exports given text track to GPAC TTXT format.</dd>
<dt><code>-srt</code></dt>
<dd> converts input subtitle to SRT format.</dd>
<dt><code>-srt trackID</code></dt>
<dd> exports given text track to SRT subtitle format.</dd>
<dt><code>-std</code></dt>
<dd> dumps to stdout rather than file.</dd>
<dt><code>-stat</code></dt>
<dd> generates statitistic report on node/field usage for the whole presentation.</dd>
<dt><code>-stats</code></dt>
<dd> generates statistic report on node/field usage per BIFS Access Unit.</dd>
<dt><code>-statx</code></dt>
<dd> generates statistic report on node/field usage in the scene graph after each BIFS Access Unit.</dd>
<dt><code>-hash</code></dt>
<dd> generates SHA-1 Hash of the input file.</dd></dl>
<h2>Meta OPTIONS</h2>
<p> MP4Box supports the Meta addition to IsoMedia file format, used to make the file a generic data container (timed or untimed).</p>
<dl>
<dt><code>-set-meta args</code></dt>
<dd> sets meta object type. Syntax is &quot;ABCD[;tk=N] where:<br />
 ABCD is the four character code of the type, or O/NULL to remove the meta object<br />
 tk indicates whether the meta is at the root level (no &quot;tk&quot;), at the moov level (tk=0) or at the track level (tk=trackID).</dd>
<dt><code>-add-item args</code></dt>
<dd> adds resource to the given meta. args is the item file path followed by &#8216;;&#8217; separated options:<br />
 tk=N: same as above<br />
 name=item_name: specifies the item name, otherwise file name is used<br />
 mime=mimeType: specifies the item mime type, otherwise application/octet-stream is used<br />
 encoding=enctype: specifies the content encoding type Note that file path set to &quot;this&quot; or &quot;self&quot; will identify the item added as the whole IsoMedia file</dd>
<dt><code>-rem-item args</code></dt>
<dd> removes item from given meta. Syntax is itemID[;tk=ID].</dd>
<dt><code>-set-primary args</code></dt>
<dd> sets given item as the primary one of the given meta. Syntax is itemID[;tk=ID].</dd>
<dt><code>-set-xml args</code></dt>
<dd> sets XML to the given meta. Syntax is xml_file_path[;tk=ID][;binary].</dd>
<dt><code>-rem-xml [tk=ID]</code></dt>
<dd> removes XML data from the given meta.</dd>
<dt><code>-dump-xml xml_out_file_name[;tk=ID]</code></dt>
<dd> dumps the XML data of the given meta to a file.</dd>
<dt><code>-dump-item itemID[;tk=ID][;path=fileName]</code></dt>
<dd> dumps the given item of the the given meta to a file. By default the item name is used as the output file name.</dd>
<dt><code>-package</code></dt>
<dd> packages input XML file into an ISO container. all media referenced except hyperlinks are added to file.</dd>
<dt><code>-mgt</code></dt>
<dd> packages input XML file into an MPEG-U widget in ISO container. All files contained in the current folder are added to the widget package.</dd></dl>
<h2>RTP STREAMER OPTIONS</h2>
<p> MP4Box can stream ISO files to RTP. The streamer currently doesn&#8217;t support data carrouselling and will therefore not handle BIFS and OD streams properly.</p>
<dl>
<dt><code>-rtp</code></dt>
<dd> enables rtp file streamer.</dd>
<dt><code>-noloop</code></dt>
<dd> disables looping when streaming.</dd>
<dt><code>-mpeg4</code></dt>
<dd> forces MPEG-4 ES Generic for all RTP streams.</dd>
<dt><code>-dst=IP</code></dt>
<dd> IP destination (uni/multi-cast). Default: 127.0.0.1.</dd>
<dt><code>-port=PORT</code></dt>
<dd> output port of the first stream. Default: 7000.</dd>
<dt><code>-mtu=MTU</code></dt>
<dd> path MTU for RTP packets. Default is 1450 bytes.</dd>
<dt><code>-ifce=IP</code></dt>
<dd> IP address of the physical interface to use. Default: NULL (ANY).</dd>
<dt><code>-ttl=N</code></dt>
<dd> time to live for multicast packets. Default: 1.</dd>
<dt><code>-sdp=FILE</code></dt>
<dd> file name of the generated SDP. Default is session.sdp.</dd></dl>
<h2>LIVE SCENE STREAMER OPTIONS</h2>
<p> MP4Box can stream BIFS or DIMS content to RTP with carousel generation and updates. The streamer currently doesn&#8217;t support audio/video/image streaming at the same time. All options supported by the file streamer are supported.</p>
<dl>
<dt><code>-live</code></dt>
<dd> enables rtp live streamer.</dd>
<dt><code>-dims</code></dt>
<dd> turns on DIMS mode for SVG input &#8211; default: off.</dd>
<dt><code>-src=FILE</code></dt>
<dd> source of updates &#8211; default: null.</dd>
<dt><code>-rap=TIME</code></dt>
<dd> duration in ms of base carousel &#8211; default: 0 (off). you can specify the RAP period of a single ESID (not in DIMS) with -rap=ESID=X:time.</dd>
<dt><code>Runtime Options</code></dt>
<dd> The following options can be used at prompt:<br />
 q: quits<br />
 u: inputs some commands to be sent<br />
 U: same as u but signals the updates as critical<br />
 e: inputs some commands to be sent without being aggregated<br />
 E: same as e but signals the updates as critical<br />
 f: forces RAP sending<br />
 F: forces RAP regeneration and sending<br />
 p: dumps current scene</dd></dl>
<h2>SWF OPTIONS</h2>
<p> MP4Box can import very simple Macromedia Flash files (&quot;.SWF&quot;). You can specify a SWF input file with -bt, xmt and -mp4 switches.</p>
<dl>
<dt><code>-global</code></dt>
<dd> all SWF defines are placed in first scene replace. By default SWF defines are sent when needed.</dd>
<dt><code>-no-ctrl</code></dt>
<dd> uses a dedicated stream for movie control. This will disable ActionScript.</dd>
<dt><code>-no-text</code></dt>
<dd> removes all SWF text.</dd>
<dt><code>-no-font</code></dt>
<dd> removes all embedded SWF Fonts, forcing usage of MPEG-4 Text and terminal fonts.</dd>
<dt><code>-no-line</code></dt>
<dd> removes all lines from SWF shapes.</dd>
<dt><code>-no-grad</code></dt>
<dd> removes all gradients from swf shapes.</dd>
<dt><code>-quad</code></dt>
<dd> uses quadratic bezier curves instead of cubic ones.</dd>
<dt><code>-xlp</code></dt>
<dd> support for lines transparency and scalability.</dd>
<dt><code>-flatten Value</code></dt>
<dd> replaces 2 consecutive lines by a single one when angle between lines is less than Value (expressed in radians). Value 0 disables flattening.</dd></dl>
<h2>SUPPORTED INPUT FORMATS</h2>
<dl>
<dt><code>RAW Formats and extensions</code></dt>
<dd>
</dd><dt>
</dt><dd> NHNT (.media .nhnt .info)<br />
 MPEG Audio (.mp3)<br />
 ADTS-AAC (.aac)<br />
 MPEG-4 Visual (.cmp .m4v)<br />
 H263 Video (.263 .h263)<br />
 AVC/H264 Video (.h264 .h26L .264 .26L)<br />
 JPEG Images (.jpg .jpeg)<br />
 PNG Images (.png)<br />
 AMR(WB) Audio (.amr .awb)<br />
 EVRC Audio (.evc)<br />
 SMV Audio (.smv)</dd>
<dt><code>Container Formats and extensions</code></dt>
<dd>
</dd><dt>
</dt><dd> AVI (.avi)<br />
 MPEG-PS (.mpg .mpeg .vob .vcd .svcd)<br />
 QCP (.qcp)<br />
 OGG (.ogg)<br />
 ISO-Media files (no extension checking)</dd>
<dt><code>Text Formats and extensions</code></dt>
<dd>
</dd><dt>
</dt><dd>
 SRT Subtitles (.srt)<br />
 SUB Subtitles (.sub)<br />
 GPAC Timed Text (.ttxt)<br />
 QuickTime TeXML Text (.xml) (cf QT documentation)</dd>
<dt><code>Scene Formats and extensions</code></dt>
<dd>
</dd><dt>
</dt><dd> MPEG-4 XMT-A (.xmt .xmta .xmt.gz .xmta.gz) </dd>
<p> MPEG-4 BT (.bt .bt.gz)<br />
 VRML (.wrl .wrl.gz)<br />
 X3D-XML (.x3d .x3d.gz)<br />
 X3D-VRML (.x3dv .x3dv.gz)<br />
 MacroMedia Flash (.swf) &#8211; very limitted import support only</dl>
<h2>COMMON USAGE</h2>
<dl>
<dt><code>Importing a file</code></dt>
<dd>
</dd><dt>
</dt><dd> Import an AVI: MP4Box -add myfile.avi mymp4.mp4<br />
 Import audio from an AVI: MP4Box -add myfile.avi#audio mymp4.mp4<br />
 Import video from an AVI: MP4Box -add myfile.avi#video mymp4.mp4<br />
 Import an MP3 and leave data outside: MP4Box -dref -add myfile.mp3 mymp4.mp4<br />
 Import a JPEG or PNG: MP4Box -add myfile.jpg mymp4.mp4<br />
 Create a movie with subtitle: MP4Box -add video.avi -add audio.mp3 -add Subtitle.srt mymp4.mp4 </dd>
<dt><code>Base File operations</code></dt>
<dd>
</dd><dt>
</dt><dd> Convert file for HTTP/FTP streaming: MP4Box -inter 1000 myfile.mp4<br />
 Convert unknown file to ISMA for HTTP/FTP streaming: MP4Box -isma -inter 1000 myfile.mp4<br />
 Convert unknown file to ISMA and respect ISMA broken sync: MP4Box -ismax myfile.mp4<br />
 Convert unknown file to 3GP : MP4Box -3gp myfile.mp4 </dd>
<dt><code>Hinting a File</code></dt>
<dd>
</dd><dt>
</dt><dd> Prepare any mp4 for ISMA streaming: MP4Box -isma -hint myfile.mp4<br />
 Prepare any 3GP for streaming: MP4Box -hint myfile.3gp<br />
 Prepare any 3GP for streaming with RTP aggregation : MP4Box -hint -multi myfile.3gp<br />
 Prepare a simple audio/video mp4 optimized for server: MP4Box -hint -copy -tight myfile.mp4<br />
 Prepare a complex mp4 with BIFS for streaming: MP4Box -ocr -iod -hint myfile.mp4 </dd>
<dt><code>Encoding/Decoding a file</code></dt>
<dd>
</dd><dt>
</dt><dd> Encode a BT file and keep node names for later inspection: MP4Box -mp4 -def pres.bt<br />
 Encode a XMT-A file: MP4Box -mp4 pres.xmt<br />
 Translate BT to XMT-A file: MP4Box -xmt pres.bt<br />
 Translate XMT-A to BT file: MP4Box -bt pres.xmt<br />
 Decode MP4 to BT: MP4Box -bt pres.mp4
</dd></dl>
<h2>BUGS and OTHER HELP</h2>
<dl>
<dt>For bug reports, more information on BT or XMT-A formats or GPAC TTXT files or ISMACryp, MPEG-4 Systems usage and more help on MP4Box please visit the GPAC web site <a rel="nofollow" href="http://gpac.sourceforge.net">http://gpac.sourceforge.net</a></dt>
<dd></dd></dl>
<h2>AUTHORS</h2>
<p> Jean Le Feuvre &lt;jeanlf [at] users.sourceforge.net&gt; &#8211; GPAC (c) 2000-2005 &#8211; (c) Telecom ParisTech 2005-2011</p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-gpac/">GPAC</a>(1), <a href="/docs/linux/man/1-mp4client/">MP4Client</a>(1) </p>
