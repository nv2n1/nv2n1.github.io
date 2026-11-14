---
title: "dump2dcm(1)"
name: "dump2dcm"
section: "1"
letter: "d"
url: "/docs/linux/man/1-dump2dcm/"
description: "dump2dcm – Convert ASCII dump to DICOM file"
---

<h2 class="name">NAME</h2>
<p> dump2dcm &#8211; Convert ASCII dump to DICOM file </p>
<h2>SYNOPSIS</h2>
<pre>
dump2dcm [options] dumpfile-in dcmfile-out
</pre>
<h2>DESCRIPTION</h2>
<p> The <code>dump2dcm</code> utility converts an ASCII dump file to a DICOM file. The dump file has the same format as the output of <code>dcmdump</code>. Thus it is possible to capture the output of <code>dcmdump</code> into a file, modify some attributes and create a new DICOM file.</p>
<h2>PARAMETERS</h2>
<pre>
dumpfile-in  dump input filename
dcmfile-out  DICOM output filename
</pre>
<h2>OPTIONS</h2>
<h3>general options</h3>
<pre><code>
- h-- help
        print this help text and exit-- version
            print version information and exit-- arguments
                print expanded command line arguments -
    q-- quiet
        quiet mode,
    print no warnings and errors - v-- verbose
                                       verbose mode,
    print processing details - d-- debug
                                   debug mode,
    print debug information - ll-- log - level[l] evel:string
                                                       constant(fatal, error, warn, info, debug, trace)
         use level l for the logger
  -lc  --log-config  [f]ilename: string
         use config file f for the logger
</code></pre>
<h3>input options</h3>
<p>input file format : +f&#8211; read &#8211; meta &#8211; info read meta information if present (default) &#8211; f&#8211; ignore &#8211; meta &#8211; info ignore file meta information other input options : +l&#8211; line[m] ax &#8211; length : integer maximum line length m(default : 4096)</p>
<h3>processing options</h3>
<pre>
unique identifiers:
  +Ug  --generate-new-uids
         generate new Study/Series/SOP Instance UID
  -Uo  --dont-overwrite-uids
         do not overwrite existing UIDs (default)
  +Uo  --overwrite-uids
         overwrite existing UIDs
</pre>
<h3>output options</h3>
<p>output file format:<br />
  +F   &#8211;write-file<br />
         write file format (default)<br />
  -F   &#8211;write-dataset<br />
         write data set without file meta information<br />
  +Fu  &#8211;update-meta-info<br />
         update particular file meta information<br />
output transfer syntax:<br />
  +t=  &#8211;write-xfer-same<br />
         write with same TS as input (default)<br />
  +te  &#8211;write-xfer-little<br />
         write with explicit VR little endian<br />
  +tb  &#8211;write-xfer-big<br />
         write with explicit VR big endian TS<br />
  +ti  &#8211;write-xfer-implicit<br />
         write with implicit VR little endian TS<br />
  +td  &#8211;write-xfer-deflated<br />
         write with deflated explicit VR little endian TS<br />
error handling:<br />
  -E   &#8211;stop-on-error<br />
         do not write if dump is damaged (default)<br />
  +E   &#8211;ignore-errors<br />
         attempt to write even if dump is damaged<br />
post-1993 value representations:<br />
  +u   &#8211;enable-new-vr<br />
         enable support for new VRs (UN/UT) (default)<br />
  -u   &#8211;disable-new-vr<br />
         disable support for new VRs, convert to OB<br />
group length encoding:<br />
  +g=  &#8211;group-length-recalc<br />
         recalculate group lengths if present (default)<br />
  +g   &#8211;group-length-create<br />
         always write with group length elements<br />
  -g   &#8211;group-length-remove<br />
         always write without group length elements<br />
length encoding in sequences and items:<br />
  +e   &#8211;length-explicit<br />
         write with explicit lengths (default)<br />
  -e   &#8211;length-undefined<br />
         write with undefined lengths<br />
data set trailing padding (not with &#8211;write-dataset):<br />
  -p=  &#8211;padding-retain<br />
         do not change padding (default if not &#8211;write-dataset)<br />
  -p   &#8211;padding-off<br />
         no padding (implicit if &#8211;write-dataset)<br />
  +p   &#8211;padding-create  [f]ile-pad [i]tem-pad: integer<br />
         align file on multiple of f bytes<br />
         and items on multiple of i bytes<br />
deflate compression level (only with &#8211;write-xfer-deflated):<br />
  +cl  &#8211;compression-level  [l]evel: integer (default: 6)<br />
         0=uncompressed, 1=fastest, 9=best compression</p>
<h2>NOTES</h2>
<h3>Dump File Description</h3>
<p> The input file can be an output of <code>dcmdump</code> (default indented format only). One element (tag, VR, value) must be written into one line separated by arbitrary spaces or tab characters. A &#8216;#&#8217; begins a comment that ends at the line end. Empty lines are allowed. </p>
<p> The individual parts of a line have the following syntax: </p>
<p>Tag:   (gggg,eeee)<br />
       with gggg and eeee are 4 character hexadecimal values<br />
       representing group and element tag.  Spaces and tabs can be<br />
       anywhere in a tag specification.<br />
VR:    Value Representation must be written as 2 characters as in<br />
       Part 6 of the DICOM standard.  No spaces or tabs are allowed<br />
       between the two characters.  If the VR can be determined from<br />
       the tag, this part of a line is optional.<br />
Value: There are several rules for writing values:<br />
       1. US, SS, SL, UL, FD, FL are written as decimal strings that<br />
          can be read by scanf().<br />
       2. AT is written as &#8216;(gggg,eeee)&#8217; with additional spaces<br />
          stripped off automatically and gggg and eeee being decimal<br />
          strings that can be read by scanf().<br />
       3. OB and OW values are written as byte or word hexadecimal<br />
          values separated by &#8216;\&#8217; character.  Alternatively, OB or OW<br />
          values can be read from a separate file by writing the<br />
          filename prefixed by a &#8216;=&#8217; character (e.g. &#8216;=largepix.dat&#8217;).<br />
          The contents of the file will be read as is.  OW data is<br />
          expected to be little endian ordered and will be swapped if<br />
          necessary.  No checks will be made to ensure that the amount<br />
          of data is reasonable in terms of other attributes such as<br />
          Rows or Columns.<br />
          In case of compressed pixel data, the line should start with<br />
          &#8216;(7fe0,0010) OB (PixelSequence&#8217; in order to distinguish from<br />
          uncompressed pixel data.<br />
       4. UI is written as &#8216;=Name&#8217; in data dictionary or as unique<br />
          identifier string (see 6.), e.g. &#8216;[1.2.840&#8230;..]&#8217;.<br />
       5. Strings without () &lt;&gt; [] spaces, tabs and # can be written<br />
          directly.<br />
       6. Other strings must be surrounded by &#8216;[&#8216; and &#8216;]&#8217;.  No bracket<br />
          structure is passed.  The value ends at the last &#8216;]&#8217; in the<br />
          line.  Anything after the &#8216;]&#8217; is interpreted as comment.<br />
       7. &#8216;(&#8216; and &#8216;&lt;&#8216; are interpreted special and may not be used when<br />
          writing an input file by hand as beginning characters of a<br />
          string.  Multiple Value are separated by &#8216;\&#8217;.  The lines<br />
          need not be sorted into ascending tag order.  References in<br />
          DICOM Directories are not supported.  Semantic errors are<br />
          not detected.</p>
<h3>Example</h3>
<pre><code>
(0008, 0020) DA[19921012] #8, 1 StudyDate(0008, 0016) UI = MRImageStorage #26, 1 SOPClassUID(0002, 0012) UI[1.2.276.0.7230010.100.1.1](0020, 0032) DS[0.0
