---
title: "dcmodify(1)"
name: "dcmodify"
section: "1"
letter: "d"
url: "/docs/linux/man/1-dcmodify/"
description: "dcmodify – Modify DICOM files"
---

<h2 class="name">NAME</h2>
<p> dcmodify &#8211; Modify DICOM files </p>
<h2>SYNOPSIS</h2>
<pre>
dcmodify [options] dcmfile-in...
</pre>
<h2>DESCRIPTION</h2>
<p> <code>dcmodify</code> is a tool that allows to modify, insert and delete tags and items in DICOM files. Sequences and tags with a value multiplicity &gt; 1 are also supported. Metaheader information and the tag&#8217;s VR can not be modified directly by <code>dcmodify</code> at this time. In addition to tag modifications, <code>dcmodify</code> makes available some input options &#8211; forcing <code>dcmodify</code> to handle its input files as the user specifies &#8211; and output options to control the output format of the resulting files. </p>
<p> In case multiple modifications have to be performed, <code>dcmodify</code> does the modifications in the same order as they appear on the command line. Please note that <code>dcmodify</code> does not check whether a given value matches its value representation (VR). Usually, an error message is printed but generally the user should take care of the right VR usage. </p>
<p> If <code>dcmodify</code> doesn&#8217;t know the tag it should insert, then the tag&#8217;s VR is set to UN and the value provided on commandline is interpreted as being a series of hexadecimal numbers (like they are provided for VR=OB). Please insert these tags into the dictionary to avoid this behaviour. Also, specifying the <i>-iun</i> option, it is possible to force <code>dcmodify</code> to leave UN values untouched. Using option <i>-u</i> lets <code>dcmodify</code> saving all VR=UN attributes as OB. </p>
<p> <code>dcmodify</code> is able to work with so-called tag paths to access tags in sequences. The (pseudo-formalized) syntax is </p>
<pre><code>
{sequence[item - no].} * element
</code></pre>
<p> where &#8216;sequence&#8217; is a sequence tag like (0008,1111) or a dictionary name for a tag. &#8216;item-no&#8217; describes the item number to be accessed (counting from zero). &#8216;element&#8217; defines the target tag to work on. A tag can either be specified directly as (0010,0010) or through the corresponding dictionary name &#8216;PatientName&#8217;. The &#8216;*&#8217; denotes that you can repeat sequence statements to access deeper levels in DICOM files (see EXAMPLES section). For &#8216;item-no&#8217;, also a wildcard character &#8216;*&#8217; can be used selecting all items in surrounding sequence (see section WILDCARDS below). </p>
<p> When inserting tag paths consisting of multiple nodes (i.e. not a single element) using the <i>-i</i> option, any missing path elements (items, sequences, leaf elements) are inserted automatically when missing. That does not work for item wildcards: When no single item exists in the surrounding sequence <code>dcmodify</code> of course can&#8217;t decide, how many items should be generated. However, if specifying an item number like &#8216;5&#8217;, all 6 items (counted from zero) can be (and are) automatically generated in insert mode. If already 2 items would exist, the rest (4) would be inserted. </p>
<p> Please note that there are some issues concerning the modification of private tags (see PRIVATE TAGS section) and for changing UIDs (CHANGING UIDs section).</p>
<h2>PARAMETERS</h2>
<pre>
dcmfile-in  DICOM input filename(s) to be modified
</pre>
<h2>OPTIONS</h2>
<h3>general options</h3>
<p>&#8211; h&#8211; help<br />
        print this help text and exit&#8211; version<br />
            print version information and exit&#8211; arguments<br />
                print expanded command line arguments &#8211;<br />
    q&#8211; quiet<br />
        quiet mode,<br />
    print no warnings and errors &#8211; v&#8211; verbose<br />
                                       verbose mode,<br />
    print processing details &#8211; d&#8211; debug<br />
                                   debug mode,<br />
    print debug information &#8211; ll&#8211; log &#8211; level[l] evel:string<br />
                                                       constant(fatal, error, warn, info, debug, trace)<br />
          use level l for the logger<br />
  -lc   &#8211;log-config  [f]ilename: string<br />
          use config file f for the logger<br />
  -ie   &#8211;ignore-errors<br />
          continue with file, if modify error occurs<br />
  -nb   &#8211;no-backup<br />
          don&#8217;t backup files (DANGEROUS)</p>
<h3>input options</h3>
<p>input file format : +f&#8211; read &#8211; file<br />
                                    read file format or<br />
    data set(default) + fo&#8211; read &#8211; file &#8211; only read file format only<br />
        &#8211; f&#8211; read &#8211; dataset read data set without file meta information input transfer syntax : -t = &#8211;read &#8211; xfer &#8211; auto use TS recognition(default) &#8211; td&#8211; read &#8211; xfer &#8211; detect ignore TS specified in the file meta header<br />
                                                                                                      &#8211; te&#8211; read &#8211; xfer &#8211; little read with explicit VR little endian TS<br />
                                                                                                      &#8211; tb&#8211; read &#8211; xfer &#8211; big read with explicit VR big endian TS<br />
                                                                                                      &#8211; ti&#8211; read &#8211; xfer &#8211; implicit read with implicit VR little endian TS parsing of odd &#8211; length attributes : +ao&#8211; accept &#8211; odd &#8211; length accept odd length attributes(default) + ae&#8211; assume &#8211; even &#8211; length assume real length is one byte larger automatic data correction : +dc&#8211; enable &#8211; correction enable automatic data correction(default) &#8211; dc&#8211; disable &#8211; correction disable automatic data correction bitstream format of deflated input : +bd&#8211; bitstream &#8211; deflated expect deflated bitstream(default) + bz&#8211; bitstream &#8211; zlib expect deflated zlib bitstream</p>
<h3>processing options</h3>
<p>insert mode : -i&#8211; insert &#8220;[t]ag-path=[v]alue&#8221; insert(or overwrite) path at position t with value v<br />
              &#8211;<br />
              if &#8211;insert &#8211; from &#8211; file &#8220;[t]ag-path=[f]ilename&#8221; insert(or overwrite) path at position t with value from file f<br />
              &#8211;<br />
              nrc&#8211; no &#8211; reserv &#8211; check do not check private reservations modify mode : -m&#8211; modify &#8220;[t]ag-path=[v]alue&#8221; modify tag at position t to value v<br />
                                                                                        &#8211;<br />
                                                                                        mf&#8211; modify &#8211; from &#8211; file &#8220;[t]ag-path=[f]ilename&#8221; modify tag at position t to value from file f<br />
                                                                                        &#8211;<br />
                                                                                        ma&#8211; modify &#8211; all &#8220;[t]ag=[v]alue&#8221; modify ALL matching tags t in file to value v erase mode : -e&#8211; erase &#8220;[t]ag-path&#8221; erase tag / item at position t<br />
                                                                                        &#8211;<br />
                                                                                        ea&#8211; erase &#8211; all &#8220;[t]ag&#8221; erase ALL matching tags t in file<br />
                                                                                        &#8211;<br />
                                                                                        ep&#8211; erase &#8211; private erase ALL private data from file unique identifier : -gst&#8211; gen &#8211; stud &#8211; uid generate new Study Instance UID<br />
                                                                                                                                                                  &#8211;<br />
                                                                                                                                                                  gse&#8211; gen &#8211; ser &#8211; uid generate new Series Instance UID<br />
                                                                                                                                                                  &#8211;<br />
                                                                                                                                                                  gin&#8211; gen &#8211; inst &#8211; uid generate new SOP Instance UID<br />
                                                                                                                                                                  &#8211;<br />
                                                                                                                                                                  nmu&#8211; no &#8211; meta &#8211; uid do not update metaheader UIDs if related UIDs in the dataset are modified other processing options : -imt&#8211; ignore &#8211; missing &#8211; tags treat &#8216;tag not found&#8217; as success when modifying<br />
    or erasing in files<br />
           &#8211; iun&#8211; ignore &#8211; un &#8211; values do not try writing any values to elements having VR of UN</p>
<h3>output options</h3>
<p>output file format:<br />
  +F    &#8211;write-file<br />
          write file format (default)<br />
  -F    &#8211;write-dataset<br />
          write data set without file meta information<br />
output transfer syntax:<br />
  +t=   &#8211;write-xfer-same<br />
          write with same TS as input (default)<br />
  +te   &#8211;write-xfer-little<br />
          write with explicit VR little endian TS<br />
  +tb   &#8211;write-xfer-big<br />
          write with explicit VR big endian TS<br />
  +ti   &#8211;write-xfer-implicit<br />
          write with implicit VR little endian TS<br />
post-1993 value representations:<br />
  +u    &#8211;enable-new-vr<br />
          enable support for new VRs (UN/UT) (default)<br />
  -u    &#8211;disable-new-vr<br />
          disable support for new VRs, convert to OB<br />
group length encoding:<br />
  +g=   &#8211;group-length-recalc<br />
          recalculate group lengths if present (default)<br />
  +g    &#8211;group-length-create<br />
          always write with group length elements<br />
  -g    &#8211;group-length-remove<br />
          always write without group length elements<br />
length encoding in sequences and items:<br />
  +le   &#8211;length-explicit<br />
          write with explicit lengths (default)<br />
  -le   &#8211;length-undefined<br />
          write with undefined lengths<br />
data set trailing padding (not with &#8211;write-dataset):<br />
  -p=   &#8211;padding-retain<br />
          do not change padding (default if not &#8211;write-dataset)<br />
  -p    &#8211;padding-off<br />
          no padding (implicit if &#8211;write-dataset)<br />
  +p    &#8211;padding-create  [f]ile-pad [i]tem-pad: integer<br />
          align file on multiple of f bytes and items on<br />
          multiple of i bytes</p>
<h2>PRIVATE TAGS</h2>
<p> There are some issues you have to consider when working with private tags. However, the insertion or modification of a reservation tag (gggg,00xx) should always work.</p>
<h3>Insertions</h3>
<p> If you wish to insert a private tag (not a reservation with gggg,00xx), be sure, that you&#8217;ve listed it in your dictionary (see <i>&lt;docdir&gt;/datadict.txt</i> for details). If it&#8217;s not listed, <code>dcmodify</code> will insert it with VR=UN. Also, for some cases insertion may even fail for some values. </p>
<p> If you&#8217;ve got your private tag in the dictionary, <code>dcmodify</code> acts as follows: When it finds a reservation in the tag&#8217;s enclosing dataset, whose private creator matches, insertion is done with the VR found in the dictionary and the value given on command line. But if the private creator doesn&#8217;t match or none is set, <code>dcmodify</code> will return with an error. If a private tag should be inserted regardless whether a reservation does not exist, the option <i>-nrc</i> can be used, forcing an insertion. However, the VR is set to UN then, because the tag then cannot be found in the dictionary. </p>
<p> See description above how inserting values into elements with unknown VR are handled.</p>
<h3>Modifications</h3>
<p> If you modify a private tags value, <code>dcmodify</code> won&#8217;t check its VR against the dictionary. So please be careful to enter only values that match the tag&#8217;s VR. </p>
<p> If you wish to change a private tags value <i>and</i> VR, because you just added this tag to your dictionary, you can delete it with <code>dcmodify</code> and re-insert it. Then <code>dcmodify</code> uses your dicitionary entry to determine the right VR (also see subsection insertions). </p>
<p> Also, see description above how inserting values into elements with unknown VR are handled.</p>
<h3>Deletions</h3>
<p> When you use <code>dcmodify</code> to delete a private reservation tag, please note that <code>dcmodify</code> won&#8217;t touch the private tags that are under this reservation. The user is forced to handle the consistency between reservations and their pending private tags. </p>
<p> For the deletion of private non-reservation tags there are no special issues.</p>
<h2>CHANGING UIDS</h2>
<p> <code>dcmodify</code> will automatically correct &#8216;Media Storage SOP Class UID&#8217; and &#8216;Media Storage SOP Instance UID&#8217; in the metaheader, if you make changes to the related tags in the dataset (&#8216;SOP Class UID&#8217; and &#8216;SOP Instance UID&#8217;) via insert or modify mode options. You can disable this behaviour by using the <i>-nmu</i> option. </p>
<p> If you generate new UID&#8217;s with <i>-gst</i>, <i>-gse</i> or <i>-gin</i>, this will only affect the UID you choosed to generate. So if you use <i>-gst</i> to generate a new &#8216;Study Instance UID&#8217;, then &#8216;Series Instance UID&#8217; and &#8216;SOP Instance UID&#8217; will not be affected! This gives you the possibility to generate each value separately. Normally, you would also modify the &#8216;underlying&#8217; UIDs. As a disadvantage of this flexibility, the user has to assure, that when creating &#8216;new&#8217; DICOM files with new UIDs with <code>dcmodify</code>, other UIDs have to be updated by the user as necessary. </p>
<p> When choosing the <i>-gin</i> option, the related metaheader tag (&#8216;Media Storage SOP Instance UID&#8217;) is updated automatically. This behaviour cannot be disabled.</p>
<h2>ELEMENT VALUES FROM FILE</h2>
<p> In order to read the element value from a file instead of specifying it on the command line, option <i>-mf</i> and <i>-if</i> can be used. Please note that for OW elements, the data is expected to be little endian ordered and will be swapped if necessary. The file size should always be an even number of bytes, i.e. no automatic padding is performed.</p>
<h2>WILDCARDS</h2>
<p> <code>dcmodify</code> also permits the usage of a wildcard character &#8216;*&#8217; for item numbers in path expressions, e.g. &#8216;ContentSequence[*].CodeValue&#8217; selects all &#8216;Code Value&#8217; attributes in all items of the ContentSequence. Using a wildcard is possible for all basic operations, i.e. modifying <i>-m</i>, inserting <i>-i</i> and <i>-e</i> options which makes it, together with the automatic creation of intermediate path nodes a powerful tool for construction and processing complex datasets. </p>
<p> The options <i>-ma</i> and <i>-ea</i> for modifying or deleting all occurences of a DICOM element based on its tag do not accept any wildcards but only work on single elements (i.e. a single dictionary name or tag key).</p>
<h2>EXAMPLES</h2>
<pre><code>
-i   --insert:
       dcmodify -i "(0010,0010)=A Name" file.dcm
       Inserts the PatientName tag into 'file.dcm' at 1st level.
       If tag already exists, -i will overwrite it!  If you want to
       insert an element with value multiplicity &gt; 1 (e.g. 4) you
       can do this with: dcmodify -i "(0018,1310)=1\2\3\4"
       dcmodify -i "(0008,1111)[0].PatientName=Another Name" *.dcm
       Inserts PatientName tag into the first item of sequence
       (0008,1111).  Note that the use of wildcards for files is
       possible.  You can specify longer tag paths, too (e.g.
       "(0008,1111)[0].(0008,1111)[1].(0010,0010)=A Third One").
       If any part of the path, e.g. the sequence or the item "0"
       does not exist, it is automatically inserted by dcmodify.
       dcmodify -i "(0008,1111)[*].PatientName=Another Name" *.dcm
       Inserts PatientName tag into _every_ item of sequence
       (0008,1111).  Note that the use of wildcards for files is
       possible.  You can specify longer tag paths, too (e.g.
       "(0008,1111)[*].(0008,1111)[*].(0010,0010)=A Third One").
-if  --insert-from-file:
       dcmodify -if "PixelData=pixel.raw" file.dcm
       Inserts the content of file 'pixel.raw' into the PixelData element
       of 'file.dcm'.  The contents of the file will be read as is.
       OW data is expected to be little endian ordered and will be
       swapped if necessary.  No checks will be made to ensure that the
       amount of data is reasonable in terms of other attributes such as
       Rows or Columns.
-m   --modify:
       dcmodify -m "(0010,0010)=A Name" file.dcm
       Changes tag (0010,0010) on 1st level to "A Name".
       This option also permits longer tag paths as demonstrated
       above for -i. If the leaf element or any intermediate
       part of the path does not exist, it is not inserted as it
       would be if using the '-i' option.
       dcmodify -m "(0010,0010)=A Name" -imt file.dcm
       Changes tag (0010,0010) on 1st level to "A Name". Due to the
       given option '-imt', success is returned instead of "tag not found",
       if the element/item (or any intermediate node in a longer path) does
       not exist.
       Note that for the '-m' option the last node in the path must be
       a leaf element, i.e. not a sequence or an item.
-mf  --modify-from-file:
       dcmodify -mf "PixelData=pixel.raw" file.dcm
       Does the same as -if in case there was already a PixelData element
       in 'file.dcm'.  Otherwise nothing is changed.
-ma  --modify-all:
       dcmodify -ma "(0010,0010)=New Name" file.dcm
       Does the same as -m but works on all matching tags found in
       'file.dcm'.  Therefore, it searches the whole dataset including
       sequences for tag (0010,0010) and changes them to "New Name"
-e   --erase:
       dcmodify -e "(0010,0010)" *.dcm
       Erases tag (0010,0010) in all *.dcm files at 1st level.
       This option also allows longer tag paths as demonstrated
       above for -i.
       dcmodify -e "(0010,0010)" -imt *.dcm
       Erases tag (0010,0010) in all *.dcm files at 1st level. Due to the
       given option '-imt', success is returned instead of "tag not found",
       if the element/item (or any intermediate node in a longer path) does
       not exist.
-ea  --erase-all:
       dcmodify -ea "(0010,0010)" *.dcm
       Same as -e, but also searches in sequences and items.
-ep  --erase-private:
       dcmodify -ep *.dcm
       Deletes all private tags (i.e. tags having an odd group number) from
       all files matching *.dcm in the current directory.
-gst --gen-stud-uid:
       dcmodify -gst file.dcm
       This generates a new value for the StudyInstanceUID
       (0020,000d).  Other UIDs are not modified!
-gse --gen-ser-uid:
       dcmodify -gse file.dcm
       This generates a new value for the SeriesInstanceUID
       (0020,000e).  Other UIDs are not modified!
-gin --gen-inst-uid:
       dcmodify -gin file.dcm
       This command generates a new value for the SOPInstanceUID
       (0008,0018).  The corresponding MediaStorageSOPInstanceUID
       (0002,0003) is adjusted to the new value automatically.
       Please note that it's not possible to avoid this metaheader
       update via the -nmu option.
-nmu --no-meta-uid:
       dcmodify -m "SOPInstanceUID=[UID]" -nmu *.dcm
       This will modify the SOPInstanceUID to the given [UID],
       but -nmu avoids, that dcmodify adjusts the
       MediaStorageSOPInstanceUID in the metaheader, too.
</code></pre>
<h2>ERROR HANDLING</h2>
<p> <code>dcmodify</code> tries executing each modify operation given on command line: If one returns an error, the others are being performed anyway. However in case of any error, the modified file is not saved, unless the <i>&#8211;ignore-errors</i> option is specified. If that option is selected, <code>dcmodify</code> also continues modifying further files specified on commandline; otherwise <code>dcmodify</code> exits after the first file that had modification errors. </p>
<p> If the <i>&#8211;ignore-missing-tags</i> option is enabled, any modify or erase operations (i.e. not <i>&#8211;insert</i>) that fails because of a non-existing tag is treated as being successful. That does make sense if someone wants to be sure that specific tags are not present in the file or that &#8211; if they exist &#8211; that they are set to a specific value.</p>
<h2>LOGGING</h2>
<p> The level of logging output of the various command line tools and underlying libraries can be specified by the user. By default, only errors and warnings are written to the standard error stream. Using option <i>&#8211;verbose</i> also informational messages like processing details are reported. Option <i>&#8211;debug</i> can be used to get more details on the internal activity, e.g. for debugging purposes. Other logging levels can be selected using option <i>&#8211;log-level</i>. In <i>&#8211;quiet</i> mode only fatal errors are reported. In such very severe error events, the application will usually terminate. For more details on the different logging levels, see documentation of module &#8216;oflog&#8217;. </p>
<p> In case the logging output should be written to file (optionally with logfile rotation), to syslog (Unix) or the event log (Windows) option <i>&#8211;log-config</i> can be used. This configuration file also allows for directing only certain messages to a particular output stream and for filtering certain messages based on the module or application where they are generated. An example configuration file is provided in <i>&lt;etcdir&gt;/logger.cfg</i>).</p>
<h2>COMMAND LINE</h2>
<p> All command line tools use the following notation for parameters: square brackets enclose optional values (0-1), three trailing dots indicate that multiple values are allowed (1-n), a combination of both means 0 to n values. </p>
<p> Command line options are distinguished from parameters by a leading &#8216;+&#8217; or &#8216;-&#8216; sign, respectively. Usually, order and position of command line options are arbitrary (i.e. they can appear anywhere). However, if options are mutually exclusive the rightmost appearance is used. This behaviour conforms to the standard evaluation rules of common Unix shells. </p>
<p> In addition, one or more command files can be specified using an &#8216;@&#8217; sign as a prefix to the filename (e.g. <i>@command.txt</i>). Such a command argument is replaced by the content of the corresponding text file (multiple whitespaces are treated as a single separator unless they appear between two quotation marks) prior to any further evaluation. Please note that a command file cannot contain another command file. This simple but effective approach allows to summarize common combinations of options/parameters and avoids longish and confusing command lines (an example is provided in file <i>&lt;datadir&gt;/dumppat.txt</i>).</p>
<h2>ENVIRONMENT</h2>
<p> The <code>dcmodify</code> utility will attempt to load DICOM data dictionaries specified in the <i>DCMDICTPATH</i> environment variable. By default, i.e. if the <i>DCMDICTPATH</i> environment variable is not set, the file <i>&lt;datadir&gt;/dicom.dic</i> will be loaded unless the dictionary is built into the application (default for Windows). </p>
<p> The default behaviour should be preferred and the <i>DCMDICTPATH</i> environment variable only used when alternative data dictionaries are required. The <i>DCMDICTPATH</i> environment variable has the same format as the Unix shell <i>PATH</i> variable in that a colon (&#8216;:&#8217;) separates entries. On Windows systems, a semicolon (&#8216;;&#8217;) is used as a separator. The data dictionary code will attempt to load each file specified in the <i>DCMDICTPATH</i> environment variable. It is an error if no data dictionary can be loaded.</p>
<h2>COPYRIGHT</h2>
<p> Copyright (C) 2003-2010 by OFFIS e.V., Escherweg 2, 26121 Oldenburg, Germany. </p>
<h2>Index</h2>
