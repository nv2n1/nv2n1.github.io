---
title: "storescp(1)"
name: "storescp"
section: "1"
letter: "s"
url: "/docs/linux/man/1-storescp/"
description: "storescp – DICOM storage (C-STORE) SCP"
---

<h2 class="name">NAME</h2>
<p> storescp &#8211; DICOM storage (C-STORE) SCP </p>
<h2>SYNOPSIS</h2>
<pre><code>
storescp[options][port]
</code></pre>
<h2>DESCRIPTION</h2>
<p> The <code>storescp</code> application implements a Service Class Provider (SCP) for the Storage Service Class. It listens on a specific TCP/IP port for incoming association requests from a Storage Service Class User (SCU) and can receive both DICOM images and other DICOM composite objects. The <code>storescp</code> application also supports the Verification Service Class as an SCP.</p>
<h2>PARAMETERS</h2>
<pre>
port  tcp/ip port number to listen on
      (this parameter is required unless the --inetd option is specified)
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
  +v    &#8211;verbose-pc<br />
          show presentation contexts in verbose mode</p>
<h3>multi-process options</h3>
<pre>
        --single-process
          single process mode (default)
        --fork
          fork child process for each association
</pre>
<h3>network options</h3>
<p>association negotiation profile from configuration file:<br />
  -xf   &#8211;config-file  [f]ilename [p]rofile: string<br />
          use profile p from config file f<br />
preferred network transfer syntaxes (not with &#8211;config-file):<br />
  +x=   &#8211;prefer-uncompr<br />
          prefer explicit VR local byte order (default)<br />
  +xe   &#8211;prefer-little<br />
          prefer explicit VR little endian TS<br />
  +xb   &#8211;prefer-big<br />
          prefer explicit VR big endian TS<br />
  +xs   &#8211;prefer-lossless<br />
          prefer default JPEG lossless TS<br />
  +xy   &#8211;prefer-jpeg8<br />
          prefer default JPEG lossy TS for 8 bit data<br />
  +xx   &#8211;prefer-jpeg12<br />
          prefer default JPEG lossy TS for 12 bit data<br />
  +xv   &#8211;prefer-j2k-lossless<br />
          prefer JPEG 2000 lossless TS<br />
  +xw   &#8211;prefer-j2k-lossy<br />
          prefer JPEG 2000 lossy TS<br />
  +xt   &#8211;prefer-jls-lossless<br />
          prefer JPEG-LS lossless TS<br />
  +xu   &#8211;prefer-jls-lossy<br />
          prefer JPEG-LS lossy TS<br />
  +xm   &#8211;prefer-mpeg2<br />
          prefer MPEG2 Main Profile @ Main Level TS<br />
  +xh   &#8211;prefer-mpeg2-high<br />
          prefer MPEG2 Main Profile @ High Level TS<br />
  +xr   &#8211;prefer-rle<br />
          prefer RLE lossless TS<br />
  +xd   &#8211;prefer-deflated<br />
          prefer deflated explicit VR little endian TS<br />
  +xi   &#8211;implicit<br />
          accept implicit VR little endian TS only<br />
  +xa   &#8211;accept-all<br />
          accept all supported transfer syntaxes<br />
network host access control (tcp wrapper):<br />
  -ac   &#8211;access-full<br />
          accept connections from any host (default)<br />
  +ac   &#8211;access-control<br />
          enforce host access control rules<br />
other network options:<br />
  -id   &#8211;inetd<br />
          run from inetd super server (not with &#8211;fork)<br />
          (this option is available only on Posix platforms)<br />
  -ta   &#8211;acse-timeout  [s]econds: integer (default: 30)<br />
          timeout for ACSE messages<br />
  -td   &#8211;dimse-timeout  [s]econds: integer (default: unlimited)<br />
          timeout for DIMSE messages<br />
  -aet  &#8211;aetitle  [a]etitle: string<br />
          set my AE title (default: STORESCP)<br />
  -pdu  &#8211;max-pdu  [n]umber of bytes: integer (4096..131072)<br />
          set max receive pdu to n bytes (default: 16384)<br />
  -dhl  &#8211;disable-host-lookup<br />
          disable hostname lookup<br />
        &#8211;refuse<br />
          refuse association<br />
        &#8211;reject<br />
          reject association if no implementation class UID<br />
        &#8211;ignore<br />
          ignore store data, receive but do not store<br />
        &#8211;sleep-after  [s]econds: integer<br />
          sleep s seconds after store (default: 0)<br />
        &#8211;sleep-during  [s]econds: integer<br />
          sleep s seconds during store (default: 0)<br />
        &#8211;abort-after<br />
          abort association after receipt of C-STORE-RQ<br />
          (but before sending response)<br />
        &#8211;abort-during<br />
          abort association during receipt of C-STORE-RQ<br />
  -pm   &#8211;promiscuous<br />
          promiscuous mode, accept unknown SOP classes<br />
          (not with &#8211;config-file)<br />
  -up   &#8211;uid-padding<br />
          silently correct space-padded UIDs</p>
<h2>output options</h2>
<p>general:<br />
  -od   &#8211;output-directory  [d]irectory: string (default: &#8220;.&#8221;)<br />
          write received objects to existing directory d<br />
bit preserving mode:<br />
  -B    &#8211;normal<br />
          allow implicit format conversions (default)<br />
  +B    &#8211;bit-preserving<br />
          write data exactly as read<br />
output file format:<br />
  +F    &#8211;write-file<br />
          write file format (default)<br />
  -F    &#8211;write-dataset<br />
          write data set without file meta information<br />
output transfer syntax<br />
(not with &#8211;bit-preserving or compressed transmission):<br />
  +t=   &#8211;write-xfer-same<br />
          write with same TS as input (default)<br />
  +te   &#8211;write-xfer-little<br />
          write with explicit VR little endian TS<br />
  +tb   &#8211;write-xfer-big<br />
          write with explicit VR big endian TS<br />
  +ti   &#8211;write-xfer-implicit<br />
          write with implicit VR little endian TS<br />
  +td   &#8211;write-xfer-deflated<br />
          write with deflated explicit VR little endian TS<br />
post-1993 value representations (not with &#8211;bit-preserving):<br />
  +u    &#8211;enable-new-vr<br />
          enable support for new VRs (UN/UT) (default)<br />
  -u    &#8211;disable-new-vr<br />
          disable support for new VRs, convert to OB<br />
group length encoding (not with &#8211;bit-preserving):<br />
  +g=   &#8211;group-length-recalc<br />
          recalculate group lengths if present (default)<br />
  +g    &#8211;group-length-create<br />
          always write with group length elements<br />
  -g    &#8211;group-length-remove<br />
          always write without group length elements<br />
length encoding in sequences and items (not with &#8211;bit-preserving):<br />
  +e    &#8211;length-explicit<br />
          write with explicit lengths (default)<br />
  -e    &#8211;length-undefined<br />
          write with undefined lengths<br />
data set trailing padding<br />
(not with &#8211;write-dataset or &#8211;bit-preserving):<br />
  -p    &#8211;padding-off<br />
          no padding (default)<br />
  +p    &#8211;padding-create  [f]ile-pad [i]tem-pad: integer<br />
          align file on multiple of f bytes and items on<br />
          multiple of i bytes<br />
deflate compression level (only with &#8211;write-xfer-deflated/same):<br />
  +cl   &#8211;compression-level  [l]evel: integer (default: 6)<br />
          0=uncompressed, 1=fastest, 9=best compression<br />
sorting into subdirectories (not with &#8211;bit-preserving):<br />
  -ss   &#8211;sort-conc-studies  [p]refix: string<br />
          sort studies using prefix p and a timestamp<br />
  -su   &#8211;sort-on-study-uid  [p]refix: string<br />
          sort studies using prefix p and the Study Instance UID<br />
  -sp   &#8211;sort-on-patientname<br />
          sort studies using the Patient&#8217;s Name and a timestamp<br />
filename generation:<br />
  -uf   &#8211;default-filenames<br />
          generate filename from instance UID (default)<br />
  +uf   &#8211;unique-filenames<br />
          generate unique filenames<br />
  -tn   &#8211;timenames<br />
          generate filename from creation time<br />
  -fe   &#8211;filename-extension  [e]xtension: string<br />
          append e to all filenames</p>
<h3>event options</h3>
<p>  -xcr  &#8211;exec-on-reception  [c]ommand: string<br />
          execute command c after having received and processed<br />
          one C-STORE-RQ message<br />
  -xcs  &#8211;exec-on-eostudy  [c]ommand: string<br />
          execute command c after having received and processed<br />
          all C-STORE-RQ messages that belong to one study<br />
  -rns  &#8211;rename-on-eostudy<br />
          having received and processed all C-STORE-RQ messages<br />
          that belong to one study, rename output files according<br />
          to a certain pattern<br />
  -tos  &#8211;eostudy-timeout  [t]imeout: integer<br />
          specifies a timeout of t seconds for end-of-study<br />
          determination<br />
  -xs   &#8211;exec-sync<br />
          execute command synchronously in foreground</p>
<h3>transport layer security (TLS) options</h3>
<p>transport protocol stack:<br />
  -tls  &#8211;disable-tls<br />
          use normal TCP/IP connection (default)<br />
  +tls  &#8211;enable-tls  [p]rivate key file, [c]ertificate file: string<br />
          use authenticated secure TLS connection<br />
private key password (only with &#8211;enable-tls):<br />
  +ps   &#8211;std-passwd<br />
          prompt user to type password on stdin (default)<br />
  +pw   &#8211;use-passwd  [p]assword: string<br />
          use specified password<br />
  -pw   &#8211;null-passwd<br />
          use empty string as password<br />
key and certificate file format:<br />
  -pem  &#8211;pem-keys<br />
          read keys and certificates as PEM file (default)<br />
  -der  &#8211;der-keys<br />
          read keys and certificates as DER file<br />
certification authority:<br />
  +cf   &#8211;add-cert-file  [c]ertificate filename: string<br />
          add certificate file to list of certificates<br />
  +cd   &#8211;add-cert-dir  [c]ertificate directory: string<br />
          add certificates in d to list of certificates<br />
ciphersuite:<br />
  +cs   &#8211;cipher  [c]iphersuite name: string<br />
          add ciphersuite to list of negotiated suites<br />
  +dp   &#8211;dhparam  [f]ilename: string<br />
          read DH parameters for DH/DSS ciphersuites<br />
pseudo random generator:<br />
  +rs   &#8211;seed  [f]ilename: string<br />
          seed random generator with contents of f<br />
  +ws   &#8211;write-seed<br />
          write back modified seed (only with &#8211;seed)<br />
  +wf   &#8211;write-seed-file  [f]ilename: string (only with &#8211;seed)<br />
          write modified seed to file f<br />
peer authentication:<br />
  -rc   &#8211;require-peer-cert<br />
          verify peer certificate, fail if absent (default)<br />
  -vc   &#8211;verify-peer-cert<br />
          verify peer certificate if present<br />
  -ic   &#8211;ignore-peer-cert<br />
          don&#8217;t verify peer certificate</p>
<h2>NOTES</h2>
<p> The semantic impacts of the above mentioned options is clear for the majority of options. Some particular options, however, are so specific that they need detailed descriptions which will be given in this passage. </p>
<p> Option <i>&#8211;sort-conc-studies</i> enables a user to sort all received DICOM objects into different subdirectories. The sorting will be done with regard to the studies the individual objects belong to, i.e. objects that belong to the same study will be stored in the same subdirectory. In general, a DICOM object d_n+1 is considered to belong to the same study as a DICOM object d_n if and only if d_n and d_n+1 show the exact same values in attribute Study Instance UID. The names of the resulting subdirectories always start with a prefix p which was passed to this option as a parameter. In addition to this prefix, the subdirectory names contain time stamp information with regard to the date and time of reception of this particular study&#8217;s first DICOM object. In detail, the determination of the subdirectory names pertains to the pattern </p>
<p>[prefix] _[YYYYMMDD] _[HHMMSSPPP]</p>
<p> where YYYY refers to year (4 digits), MM to month (01-12), DD to day (01-31), HH to hour (00-23), MM to minute (00-59), SS to second (00-59) and PPP to milliseconds (000-999). If the prefix is an empty string, the first &#8216;_&#8217; is omitted. </p>
<p> The other <i>&#8211;sort-xxx</i> options work in a similar manner, only the subdirectory names are created differently. For option <i>&#8211;sort-on-study-uid</i> the pattern is </p>
<p>[prefix] _[StudyInstanceUID]</p>
<p> and for option <i>&#8211;sort-on-patientname</i> </p>
<p>[PatientName] _[YYYYMMDD] _[HHMMSSPPP]</p>
<p> where &#8216;PatientName&#8217; is replaced by &#8216;ANONYMOUS&#8217; if the data element is empty or absent in the data set. Please note, however, that for option <i>&#8211;sort-on-study-uid</i> the same subdirectory will be used for all DICOM objects that belong to the same study, i.e. in contrast to the other <i>&#8211;sort-xxx</i> options there is no guarantee that a study directory is ever completed. </p>
<p> Option <i>&#8211;timenames</i> creates filenames from timestamps corresponding to the time, <code>storescp</code> writes a file to disk. The format is </p>
<p>[YYYYMMDDHHMMSSPPP] _[SERIALNO].[MD]</p>
<p> where YYYY, MM, DD, HH, MM, SS, PPP are interpreted as described above. If more files are created at the same time, SERIALNO is inserted. It consists of a 4-digit, consecutive number (0000 to 9999). For the first file, that exists for a specific time, no number (and no &#8216;_&#8217;) is inserted at all. MD represents an identification code (2 letters) for the kind of object stored in the file (see notes on <i>&#8211;rename-on-eostudy</i>). </p>
<p> Option <i>&#8211;filename-extension</i> appends a specified suffix to each filename (a dot &#8216;.&#8217; is not added automatically). This suffix is not appended to the filenames created by <i>&#8211;rename-on-eostudy</i> to maintain the length of 8 characters. </p>
<p> Option <i>&#8211;exec-on-reception</i> allows to execute a certain command line after having received and processed one DICOM object (through a C-STORE-RQ message). The command line to be executed is passed to this option as a parameter. The specified command line may contain a number of placeholders which will be replaced at run time: </p>
<dl>
<dt>&bull;</p>
<dd> <code>#p:</code> complete path to the output directory into which the last DICOM object was stored (not available with option <i>&#8211;ignore</i> though)</p>
<dt>&bull;</p>
<dd> <code>#f:</code> filename of the current output file (not available with option <i>&#8211;ignore</i> though)</p>
<dt>&bull;</p>
<dd> <code>#a:</code> calling application entity title of the peer Storage SCU</p>
<dt>&bull;</p>
<dd> <code>#c:</code> called application entity title used by the peer Storage SCU to address <code>storescp</code></p>
<dt>&bull;</p>
<dd> <code>#r:</code> calling presentation address, i.e. hostname or IP address of the peer Storage SCU</dl>
<p> The specified command line is executed as a separate process, so that the execution of <code>storescp</code> will not be held back. </p>
<p> Option <i>&#8211;exec-on-eostudy</i> allows to execute a certain command line when all DICOM objects that belong to one study have been received by <code>storescp</code>. The same placeholders as with <i>&#8211;exec-on-reception</i> may be used, except for &#8216;#f&#8217;, which is not supported. A study is considered complete by <code>storescp</code> when an object belonging to a different study is received or the timeout specified with <i>&#8211;eostudy-timeout</i> takes place. If option <i>&#8211;rename-on-eostudy</i> is in force, the renaming takes place before the external command is executed. </p>
<p> Option <i>&#8211;rename-on-eostudy</i> refers to the above mentioned <i>&#8211;sort-xxx</i> options and can only be used in combination with one of these options. If a user specifies option <i>&#8211;rename-on-eostudy</i> and <code>storescp</code> determines that all DICOM objects that belong to a certain study have been received, all DICOM files that belong to the last study will be renamed in the corresponding output directory. The filenames into which the files are being renamed will be calculated using the pattern </p>
<pre><code>
[prefix][consecutive numbering]
</code></pre>
<p> where [prefix] is a 2 character prefix that reveals the kind of DICOM object stored in the file and [consecutive numbering] is a consecutively numbered, 6-digit number, starting at &#8216;000001&#8217;. In general, the question if all DICOM objects that belong to one study have been received by <code>storescp</code> will be answered positively if and only if two consecutively received DICOM objects d_n and d_n+1 do not show the same values in attribute Study Instance UID; in such a case, d_n+1 is considered to belong to a new study. </p>
<p> Using option <i>&#8211;eostudy-timeout</i> a user can modify the determination process to figure out if all DICOM objects that belong to one study have already been received by <code>storescp</code>. With regard to this fact, it is clear that this option can only be used in combination with at least one of the following options: <i>&#8211;sort-xxx</i>, <i>&#8211;exec-on-eostudy</i> and <i>&#8211;rename-on-eostudy</i>. If option <i>&#8211;eostudy-timeout</i> is specified, the end of a study is considered to have occurred not only if two consecutively received DICOM objects d_n and d_n+1 do not show the same values in attribute Study Instance UID, but also if whithin a time span of x seconds after the reception of a DICOM object d_n, no other DICOM object was received over the network. Note that the amount x of seconds (which determines the length of this time span) has to be passed to this option as a parameter.</p>
<h3>DICOM Conformance</h3>
<p> The <code>storescp</code> application supports the following SOP Classes as an SCP: </p>
<pre>
VerificationSOPClass                                 1.2.840.10008.1.1
RETIRED_StoredPrintStorage                           1.2.840.10008.5.1.1.27
RETIRED_HardcopyGrayscaleImageStorage                1.2.840.10008.5.1.1.29
RETIRED_HardcopyColorImageStorage                    1.2.840.10008.5.1.1.30
ComputedRadiographyImageStorage                      1.2.840.10008.5.1.4.1.1.1
DigitalXRayImageStorageForPresentation               1.2.840.10008.5.1.4.1.1.1.1
DigitalXRayImageStorageForProcessing                 1.2.840.10008.5.1.4.1.1.1.1.1
DigitalMammographyXRayImageStorageForPresentation    1.2.840.10008.5.1.4.1.1.1.2
DigitalMammographyXRayImageStorageForProcessing      1.2.840.10008.5.1.4.1.1.1.2.1
DigitalIntraOralXRayImageStorageForPresentation      1.2.840.10008.5.1.4.1.1.1.3
DigitalIntraOralXRayImageStorageForProcessing        1.2.840.10008.5.1.4.1.1.1.3.1
CTImageStorage                                       1.2.840.10008.5.1.4.1.1.2
EnhancedCTImageStorage                               1.2.840.10008.5.1.4.1.1.2.1
RETIRED_UltrasoundMultiframeImageStorage             1.2.840.10008.5.1.4.1.1.3
UltrasoundMultiframeImageStorage                     1.2.840.10008.5.1.4.1.1.3.1
MRImageStorage                                       1.2.840.10008.5.1.4.1.1.4
EnhancedMRImageStorage                               1.2.840.10008.5.1.4.1.1.4.1
MRSpectroscopyStorage                                1.2.840.10008.5.1.4.1.1.4.2
EnhancedMRColorImageStorage                          1.2.840.10008.5.1.4.1.1.4.3
RETIRED_NuclearMedicineImageStorage                  1.2.840.10008.5.1.4.1.1.5
RETIRED_UltrasoundImageStorage                       1.2.840.10008.5.1.4.1.1.6
UltrasoundImageStorage                               1.2.840.10008.5.1.4.1.1.6.1
EnhancedUSVolumeStorage                              1.2.840.10008.5.1.4.1.1.6.2
SecondaryCaptureImageStorage                         1.2.840.10008.5.1.4.1.1.7
MultiframeSingleBitSecondaryCaptureImageStorage      1.2.840.10008.5.1.4.1.1.7.1
MultiframeGrayscaleByteSecondaryCaptureImageStorage  1.2.840.10008.5.1.4.1.1.7.2
MultiframeGrayscaleWordSecondaryCaptureImageStorage  1.2.840.10008.5.1.4.1.1.7.3
MultiframeTrueColorSecondaryCaptureImageStorage      1.2.840.10008.5.1.4.1.1.7.4
RETIRED_StandaloneOverlayStorage                     1.2.840.10008.5.1.4.1.1.8
RETIRED_StandaloneCurveStorage                       1.2.840.10008.5.1.4.1.1.9
DRAFT_WaveformStorage                                1.2.840.10008.5.1.4.1.1.9.1
TwelveLeadECGWaveformStorage                         1.2.840.10008.5.1.4.1.1.9.1.1
GeneralECGWaveformStorage                            1.2.840.10008.5.1.4.1.1.9.1.2
AmbulatoryECGWaveformStorage                         1.2.840.10008.5.1.4.1.1.9.1.3
HemodynamicWaveformStorage                           1.2.840.10008.5.1.4.1.1.9.2.1
CardiacElectrophysiologyWaveformStorage              1.2.840.10008.5.1.4.1.1.9.3.1
BasicVoiceAudioWaveformStorage                       1.2.840.10008.5.1.4.1.1.9.4.1
GeneralAudioWaveformStorage                          1.2.840.10008.5.1.4.1.1.9.4.2
ArterialPulseWaveformStorage                         1.2.840.10008.5.1.4.1.1.9.5.1
RespiratoryWaveformStorage                           1.2.840.10008.5.1.4.1.1.9.6.1
RETIRED_StandaloneModalityLUTStorage                 1.2.840.10008.5.1.4.1.1.10
RETIRED_StandaloneVOILUTStorage                      1.2.840.10008.5.1.4.1.1.11
GrayscaleSoftcopyPresentationStateStorage            1.2.840.10008.5.1.4.1.1.11.1
ColorSoftcopyPresentationStateStorage                1.2.840.10008.5.1.4.1.1.11.2
PseudoColorSoftcopyPresentationStateStorage          1.2.840.10008.5.1.4.1.1.11.3
BlendingSoftcopyPresentationStateStorage             1.2.840.10008.5.1.4.1.1.11.4
XAXRFGrayscaleSoftcopyPresentationStateStorage       1.2.840.10008.5.1.4.1.1.11.5
XRayAngiographicImageStorage                         1.2.840.10008.5.1.4.1.1.12.1
EnhancedXAImageStorage                               1.2.840.10008.5.1.4.1.1.12.1.1
XRayRadiofluoroscopicImageStorage                    1.2.840.10008.5.1.4.1.1.12.2
EnhancedXRFImageStorage                              1.2.840.10008.5.1.4.1.1.12.2.1
XRay3DAngiographicImageStorage                       1.2.840.10008.5.1.4.1.1.13.1.1
XRay3DCraniofacialImageStorage                       1.2.840.10008.5.1.4.1.1.13.1.2
BreastTomosynthesisImageStorage                      1.2.840.10008.5.1.4.1.1.13.1.3
RETIRED_XRayAngiographicBiPlaneImageStorage          1.2.840.10008.5.1.4.1.1.12.3
NuclearMedicineImageStorage                          1.2.840.10008.5.1.4.1.1.20
RawDataStorage                                       1.2.840.10008.5.1.4.1.1.66
SpatialRegistrationStorage                           1.2.840.10008.5.1.4.1.1.66.1
SpatialFiducialsStorage                              1.2.840.10008.5.1.4.1.1.66.2
DeformableSpatialRegistrationStorage                 1.2.840.10008.5.1.4.1.1.66.3
SegmentationStorage                                  1.2.840.10008.5.1.4.1.1.66.4
SurfaceSegmentationStorage                           1.2.840.10008.5.1.4.1.1.66.5
RealWorldValueMappingStorage                         1.2.840.10008.5.1.4.1.1.67
RETIRED_VLImageStorage                               1.2.840.10008.5.1.4.1.1.77.1
VLEndoscopicImageStorage                             1.2.840.10008.5.1.4.1.1.77.1.1
VideoEndoscopicImageStorage                          1.2.840.10008.5.1.4.1.1.77.1.1.1
VLMicroscopicImageStorage                            1.2.840.10008.5.1.4.1.1.77.1.2
VideoMicroscopicImageStorage                         1.2.840.10008.5.1.4.1.1.77.1.2.1
VLSlideCoordinatesMicroscopicImageStorage            1.2.840.10008.5.1.4.1.1.77.1.3
VLPhotographicImageStorage                           1.2.840.10008.5.1.4.1.1.77.1.4
VideoPhotographicImageStorage                        1.2.840.10008.5.1.4.1.1.77.1.4.1
OphthalmicPhotography8BitImageStorage                1.2.840.10008.5.1.4.1.1.77.1.5.1
OphthalmicPhotography16BitImageStorage               1.2.840.10008.5.1.4.1.1.77.1.5.2
StereometricRelationshipStorage                      1.2.840.10008.5.1.4.1.1.77.1.5.3
OphthalmicTomographyImageStorage                     1.2.840.10008.5.1.4.1.1.77.1.5.4
VLWholeSlideMicroscopyImageStorage                   1.2.840.10008.5.1.4.1.1.77.1.6
RETIRED_VLMultiFrameImageStorage                     1.2.840.10008.5.1.4.1.1.77.2
LensometryMeasurementsStorage                        1.2.840.10008.5.1.4.1.1.78.1
AutorefractionMeasurementsStorage                    1.2.840.10008.5.1.4.1.1.78.2
KeratometryMeasurementsStorage                       1.2.840.10008.5.1.4.1.1.78.3
SubjectiveRefractionMeasurementsStorage              1.2.840.10008.5.1.4.1.1.78.4
VisualAcuityMeasurementsStorage                      1.2.840.10008.5.1.4.1.1.78.5
SpectaclePrescriptionReportStorage                   1.2.840.10008.5.1.4.1.1.78.6
OphthalmicAxialMeasurementsStorage                   1.2.840.10008.5.1.4.1.1.78.7
IntraocularLensCalculationsStorage                   1.2.840.10008.5.1.4.1.1.78.8
MacularGridThicknessAndVolumeReportStorage           1.2.840.10008.5.1.4.1.1.79.1
OphthalmicVisualFieldStaticPerimetryMeasurementsSt.  1.2.840.10008.5.1.4.1.1.80.1
DRAFT_SRTextStorage                                  1.2.840.10008.5.1.4.1.1.88.1
DRAFT_SRAudioStorage                                 1.2.840.10008.5.1.4.1.1.88.2
DRAFT_SRDetailStorage                                1.2.840.10008.5.1.4.1.1.88.3
DRAFT_SRComprehensiveStorage                         1.2.840.10008.5.1.4.1.1.88.4
BasicTextSRStorage                                   1.2.840.10008.5.1.4.1.1.88.11
EnhancedSRStorage                                    1.2.840.10008.5.1.4.1.1.88.22
ComprehensiveSRStorage                               1.2.840.10008.5.1.4.1.1.88.33
ProcedureLogStorage                                  1.2.840.10008.5.1.4.1.1.88.40
MammographyCADSRStorage                              1.2.840.10008.5.1.4.1.1.88.50
KeyObjectSelectionDocumentStorage                    1.2.840.10008.5.1.4.1.1.88.59
ChestCADSRStorage                                    1.2.840.10008.5.1.4.1.1.88.65
XRayRadiationDoseSRStorage                           1.2.840.10008.5.1.4.1.1.88.67
ColonCADSRStorage                                    1.2.840.10008.5.1.4.1.1.88.69
ImplantationPlanSRDocumentStorage                    1.2.840.10008.5.1.4.1.1.88.70
EncapsulatedPDFStorage                               1.2.840.10008.5.1.4.1.1.104.1
EncapsulatedCDAStorage                               1.2.840.10008.5.1.4.1.1.104.2
PositronEmissionTomographyImageStorage               1.2.840.10008.5.1.4.1.1.128
RETIRED_StandalonePETCurveStorage                    1.2.840.10008.5.1.4.1.1.129
EnhancedPETImageStorage                              1.2.840.10008.5.1.4.1.1.130
BasicStructuredDisplayStorage                        1.2.840.10008.5.1.4.1.1.131
RTImageStorage                                       1.2.840.10008.5.1.4.1.1.481.1
RTDoseStorage                                        1.2.840.10008.5.1.4.1.1.481.2
RTStructureSetStorage                                1.2.840.10008.5.1.4.1.1.481.3
RTBeamsTreatmentRecordStorage                        1.2.840.10008.5.1.4.1.1.481.4
RTPlanStorage                                        1.2.840.10008.5.1.4.1.1.481.5
RTBrachyTreatmentRecordStorage                       1.2.840.10008.5.1.4.1.1.481.6
RTTreatmentSummaryRecordStorage                      1.2.840.10008.5.1.4.1.1.481.7
RTIonPlanStorage                                     1.2.840.10008.5.1.4.1.1.481.8
RTIonBeamsTreatmentRecordStorage                     1.2.840.10008.5.1.4.1.1.481.9
DRAFT_RTBeamsDeliveryInstructionStorage              1.2.840.10008.5.1.4.34.1
GenericImplantTemplateStorage                        1.2.840.10008.5.1.4.43.1
ImplantAssemblyTemplateStorage                       1.2.840.10008.5.1.4.44.1
ImplantTemplateGroupStorage                          1.2.840.10008.5.1.4.45.1
</pre>
<p> The <code>storescp</code> application will accept presentation contexts for all of the abovementioned supported SOP Classes using any of the following transfer syntaxes: </p>
<pre>
LittleEndianImplicitTransferSyntax                   1.2.840.10008.1.2
LittleEndianExplicitTransferSyntax                   1.2.840.10008.1.2.1
BigEndianExplicitTransferSyntax                      1.2.840.10008.1.2.2
</pre>
<p> The default behaviour of the <code>storescp</code> application is to prefer transfer syntaxes having an explicit encoding over the default implicit transfer syntax. If <code>storescp</code> is running on big-endian hardware it will prefer BigEndianExplicit to LittleEndianExplicit transfer syntax (and vice versa). This behaviour can be changed with the <i>&#8211;prefer</i> options (see above). Using option <i>&#8211;accept-all</i> any of the following transfer syntaxes is supported: </p>
<pre>
LittleEndianImplicitTransferSyntax                   1.2.840.10008.1.2
LittleEndianExplicitTransferSyntax                   1.2.840.10008.1.2.1
DeflatedExplicitVRLittleEndianTransferSyntax         1.2.840.10008.1.2.1.99
BigEndianExplicitTransferSyntax                      1.2.840.10008.1.2.2
JPEGProcess1TransferSyntax                           1.2.840.10008.1.2.4.50
JPEGProcess2_4TransferSyntax                         1.2.840.10008.1.2.4.51
JPEGProcess14SV1TransferSyntax                       1.2.840.10008.1.2.4.70
JPEGLSLosslessTransferSyntax                         1.2.840.10008.1.2.4.80
JPEGLSLossyTransferSyntax                            1.2.840.10008.1.2.4.81
JPEG2000LosslessOnlyTransferSyntax                   1.2.840.10008.1.2.4.90
JPEG2000TransferSyntax                               1.2.840.10008.1.2.4.91
MPEG2MainProfileAtMainLevelTransferSyntax            1.2.840.10008.1.2.4.100
MPEG2MainProfileAtHighLevelTransferSyntax            1.2.840.10008.1.2.4.101
RLELosslessTransferSyntax                            1.2.840.10008.1.2.5
</pre>
<p> Additional Storage SOP Classes and Transfer Syntaxes can be used with the so-called &#8216;association negotiation profiles&#8217; (see below). </p>
<p> The <code>storescp</code> application does not support extended negotiation by default. However, using an appropriate association negotiation profile (see below) the optional support for extended negotiation can be added to particular SOP classes.</p>
<h3>Access Control</h3>
<p> When compiled on Unix platforms with TCP wrapper support, host-based access control can be enabled with the <i>&#8211;access-control</i> command line option. In this case the access control rules defined in the system&#8217;s host access control tables for <code>storescp</code> are enforced. The default locations of the host access control tables are <i>/etc/hosts.allow</i> and <i>/etc/hosts.deny</i>. Further details are described in <code><a href="/docs/linux/man/5-hosts_access/">hosts_access</a></code>(5).</p>
<h3>Running storescp from inetd</h3>
<p> On Posix platforms, <code>storescp</code> can be initiated through the <a href="/docs/linux/man/8-inetd/">inetd</a>(8) super server. This requires that <code>storescp</code> be configured in the <i>/etc/inetd.conf</i> configuration file. A typical configuration line could look like this: </p>
<pre>
acr-nema stream tcp nowait root /usr/sbin/storescp -id +ac -od /tmp/storescp
</pre>
<p> where <i>-id</i> (<i>&#8211;inetd</i>) activates the inetd mode in which the DICOM association is actually accepted by inetd and passed to <code>storescp</code>, <i>+ac</i> (<i>&#8211;access-control</i>) activates the TCP wrapper based access control described above and <i>-od</i> (<i>&#8211;output-directory</i>) defines the directory in which <code>storescp</code> stores incoming DICOM objects. Note that the service name (&#8216;acr-nema&#8217; in this example) determines the port number on which DICOM associations are accepted and must be defined in <i>/etc/services</i>. When runnning from inetd, the stdout and stderr streams are redirected to files in the <i>/tmp</i> filesystem which can be identified by the filename starting with the prefix &#8216;storescp_&#8217;. </p>
<p> Please note that when run through inetd, <code>storescp</code> is executed with root privileges, which may be a security risk.</p>
<h3>Association Negotiation Profiles and Configuration Files</h3>
<p> <code>storescp</code> supports a flexible mechanism for specifying the DICOM network association negotiation behaviour, based on so-called &#8216;association negotiation profiles&#8217; which may be read from a configuration file. The format and semantics of this configuration file are documented in <i>asconfig.txt</i>.</p>
<h2>LOGGING</h2>
<p> The level of logging output of the various command line tools and underlying libraries can be specified by the user. By default, only errors and warnings are written to the standard error stream. Using option <i>&#8211;verbose</i> also informational messages like processing details are reported. Option <i>&#8211;debug</i> can be used to get more details on the internal activity, e.g. for debugging purposes. Other logging levels can be selected using option <i>&#8211;log-level</i>. In <i>&#8211;quiet</i> mode only fatal errors are reported. In such very severe error events, the application will usually terminate. For more details on the different logging levels, see documentation of module &#8216;oflog&#8217;. </p>
<p> In case the logging output should be written to file (optionally with logfile rotation), to syslog (Unix) or the event log (Windows) option <i>&#8211;log-config</i> can be used. This configuration file also allows for directing only certain messages to a particular output stream and for filtering certain messages based on the module or application where they are generated. An example configuration file is provided in <i>&lt;etcdir&gt;/logger.cfg</i>).</p>
<h2>COMMAND LINE</h2>
<p> All command line tools use the following notation for parameters: square brackets enclose optional values (0-1), three trailing dots indicate that multiple values are allowed (1-n), a combination of both means 0 to n values. </p>
<p> Command line options are distinguished from parameters by a leading &#8216;+&#8217; or &#8216;-&#8216; sign, respectively. Usually, order and position of command line options are arbitrary (i.e. they can appear anywhere). However, if options are mutually exclusive the rightmost appearance is used. This behaviour conforms to the standard evaluation rules of common Unix shells. </p>
<p> In addition, one or more command files can be specified using an &#8216;@&#8217; sign as a prefix to the filename (e.g. <i>@command.txt</i>). Such a command argument is replaced by the content of the corresponding text file (multiple whitespaces are treated as a single separator unless they appear between two quotation marks) prior to any further evaluation. Please note that a command file cannot contain another command file. This simple but effective approach allows to summarize common combinations of options/parameters and avoids longish and confusing command lines (an example is provided in file <i>&lt;datadir&gt;/dumppat.txt</i>).</p>
<h2>ENVIRONMENT</h2>
<p> The <code>storescp</code> utility will attempt to load DICOM data dictionaries specified in the <i>DCMDICTPATH</i> environment variable. By default, i.e. if the <i>DCMDICTPATH</i> environment variable is not set, the file <i>&lt;datadir&gt;/dicom.dic</i> will be loaded unless the dictionary is built into the application (default for Windows). </p>
<p> The default behaviour should be preferred and the <i>DCMDICTPATH</i> environment variable only used when alternative data dictionaries are required. The <i>DCMDICTPATH</i> environment variable has the same format as the Unix shell <i>PATH</i> variable in that a colon (&#8216;:&#8217;) separates entries. On Windows systems, a semicolon (&#8216;;&#8217;) is used as a separator. The data dictionary code will attempt to load each file specified in the <i>DCMDICTPATH</i> environment variable. It is an error if no data dictionary can be loaded.</p>
<h2>FILES</h2>
<p> <i>&lt;docdir&gt;/asconfig.txt</i> &#8211; configuration file documentation<br />
 <i>&lt;etcdir&gt;/storescp.cfg</i> &#8211; example association negotiation profile</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-storescu/">storescu</a></code>(1)</p>
<h2>COPYRIGHT</h2>
<p> Copyright (C) 1996-2010 by OFFIS e.V., Escherweg 2, 26121 Oldenburg, Germany. </p>
<h2>Index</h2>
