---
title: "storescu(1)"
name: "storescu"
section: "1"
letter: "s"
url: "/docs/linux/man/1-storescu/"
description: "storescu – DICOM storage (C-STORE) SCU"
---

<h2 class="name">NAME</h2>
<p> storescu &#8211; DICOM storage (C-STORE) SCU </p>
<h2>SYNOPSIS</h2>
<pre>
storescu [options] peer port dcmfile-in...
</pre>
<h2>DESCRIPTION</h2>
<p> The <code>storescu</code> application implements a Service Class User (SCU) for the Storage Service Class. For each DICOM file on the command line it sends a C-STORE message to a Storage Service Class Provider (SCP) and waits for a response. The application can be used to transmit DICOM images and other DICOM composite objects.</p>
<h2>PARAMETERS</h2>
<pre>
peer        hostname of DICOM peer
port        tcp/ip port number of peer
dcmfile-in  DICOM file or directory to be transmitted
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
  -lc   --log-config  [f]ilename: string
          use config file f for the logger
  +v    --verbose-pc
          show presentation contexts in verbose mode
</code></pre>
<h3>input options</h3>
<p>input file format:<br />
  +f    &#8211;read-file<br />
          read file format or data set (default)<br />
  +fo   &#8211;read-file-only<br />
          read file format only<br />
  -f    &#8211;read-dataset<br />
          read data set without file meta information<br />
input files:<br />
  +sd   &#8211;scan-directories<br />
          scan directories for input files (dcmfile-in)<br />
  +sp   &#8211;scan-pattern  [p]attern: string (only with &#8211;scan-directories)<br />
          pattern for filename matching (wildcards)<br />
#possibly not available on all systems<br />
  -r    &#8211;no-recurse<br />
          do not recurse within directories (default)<br />
  +r    &#8211;recurse<br />
          recurse within specified directories</p>
<h3>network options</h3>
<p>application entity titles:<br />
  -aet  &#8211;aetitle  [a]etitle: string<br />
          set my calling AE title (default: STORESCU)<br />
  -aec  &#8211;call  [a]etitle: string<br />
          set called AE title of peer (default: ANY-SCP)<br />
association negotiation profile from configuration file:<br />
  -xf   &#8211;config-file  [f]ilename, [p]rofile: string<br />
          use profile p from config file f<br />
proposed transmission transfer syntaxes (not with &#8211;config-file):<br />
  -x=   &#8211;propose-uncompr<br />
          propose all uncompressed TS, explicit VR<br />
          with local byte ordering first (default)<br />
  -xe   &#8211;propose-little<br />
          propose all uncompressed TS, explicit VR little endian first<br />
  -xb   &#8211;propose-big<br />
          propose all uncompressed TS, explicit VR big endian first<br />
  -xi   &#8211;propose-implicit<br />
          propose implicit VR little endian TS only<br />
  -xs   &#8211;propose-lossless<br />
          propose default JPEG lossless TS<br />
          and all uncompressed transfer syntaxes<br />
  -xy   &#8211;propose-jpeg8<br />
          propose default JPEG lossy TS for 8 bit data<br />
          and all uncompressed transfer syntaxes<br />
  -xx   &#8211;propose-jpeg12<br />
          propose default JPEG lossy TS for 12 bit data<br />
          and all uncompressed transfer syntaxes<br />
  -xv   &#8211;propose-j2k-lossless<br />
          propose JPEG 2000 lossless TS<br />
          and all uncompressed transfer syntaxes<br />
  -xw   &#8211;propose-j2k-lossy<br />
          propose JPEG 2000 lossy TS<br />
          and all uncompressed transfer syntaxes<br />
  -xt   &#8211;propose-jls-lossless<br />
          propose JPEG-LS lossless TS<br />
          and all uncompressed transfer syntaxes<br />
  -xu   &#8211;propose-jls-lossy<br />
          propose JPEG-LS lossy TS<br />
          and all uncompressed transfer syntaxes<br />
  -xm   &#8211;propose-mpeg2<br />
          propose MPEG2 Main Profile @ Main Level TS only<br />
  -xh   &#8211;propose-mpeg2-high<br />
          propose MPEG2 Main Profile @ High Level TS only<br />
  -xr   &#8211;propose-rle<br />
          propose RLE lossless TS<br />
          and all uncompressed transfer syntaxes<br />
  -R    &#8211;required<br />
          propose only required presentation contexts<br />
          (default: propose all supported)<br />
  +C    &#8211;combine<br />
          combine proposed transfer syntaxes<br />
          (default: separate presentation context for each TS)<br />
post-1993 value representations:<br />
  +u    &#8211;enable-new-vr<br />
          enable support for new VRs (UN/UT) (default)<br />
  -u    &#8211;disable-new-vr<br />
          disable support for new VRs, convert to OB<br />
deflate compression level (only with &#8211;propose-deflated or &#8211;config-file):<br />
  +cl   &#8211;compression-level  [l]evel: integer (default: 6)<br />
          0=uncompressed, 1=fastest, 9=best compression<br />
user identity negotiation:<br />
  -usr  &#8211;user  [u]ser name: string<br />
          authenticate using user name u<br />
  -pwd  &#8211;password  [p]assword: string (only with &#8211;user)<br />
          authenticate using password p<br />
  -epw  &#8211;empty-password<br />
          send empty password (only with &#8211;user)<br />
  -kt   &#8211;kerberos  [f]ilename: string<br />
          read kerberos ticket from file f<br />
        &#8211;saml  [f]ilename: string<br />
          read SAML request from file f<br />
  -rsp  &#8211;pos-response<br />
          expect positive response<br />
other network options:<br />
  -to   &#8211;timeout  [s]econds: integer (default: unlimited)<br />
          timeout for connection requests<br />
  -ta   &#8211;acse-timeout  [s]econds: integer (default: 30)<br />
          timeout for ACSE messages<br />
  -td   &#8211;dimse-timeout  [s]econds: integer (default: unlimited)<br />
          timeout for DIMSE messages<br />
  -pdu  &#8211;max-pdu  [n]umber of bytes: integer (4096..131072)<br />
          set max receive pdu to n bytes (default: 16384)<br />
        &#8211;max-send-pdu  [n]umber of bytes: integer (4096..131072)<br />
          restrict max send pdu to n bytes<br />
        &#8211;repeat  [n]umber: integer<br />
          repeat n times<br />
        &#8211;abort<br />
          abort association instead of releasing it<br />
  -nh   &#8211;no-halt<br />
          do not halt if unsuccessful store encountered<br />
          (default: do halt)<br />
  -up   &#8211;uid-padding<br />
          silently correct space-padded UIDs<br />
  +II   &#8211;invent-instance<br />
          invent a new SOP instance UID for every image sent<br />
  +IR   &#8211;invent-series  [n]umber: integer (implies &#8211;invent-instance)<br />
          invent a new series UID after n images have been sent<br />
          (default: 100)<br />
  +IS   &#8211;invent-study  [n]umber: integer (implies &#8211;invent-instance)<br />
          invent a new study UID after n series have been sent<br />
          (default: 50)<br />
  +IP   &#8211;invent-patient  [n]umber: integer (implies &#8211;invent-instance)<br />
          invent a new patient ID and name after n studies have been sent<br />
          (default: 25)</p>
<h3>transport layer security (TLS) options</h3>
<pre><code>
transport protocol stack:
  -tls  --disable-tls
          use normal TCP/IP connection (default)
  +tls  --enable-tls  [p]rivate key file, [c]ertificate file: string
          use authenticated secure TLS connection
  +tla  --anonymous-tls
          use secure TLS connection without certificate
private key password (only with --enable-tls):
  +ps   --std-passwd
          prompt user to type password on stdin (default)
  +pw   --use-passwd  [p]assword: string
          use specified password
  -pw   --null-passwd
          use empty string as password
key and certificate file format:
  -pem  --pem-keys
          read keys and certificates as PEM file (default)
  -der  --der-keys
          read keys and certificates as DER file
certification authority:
  +cf   --add-cert-file  [c]ertificate filename: string
          add certificate file to list of certificates
  +cd   --add-cert-dir  [c]ertificate directory: string
          add certificates in d to list of certificates
ciphersuite:
  +cs   --cipher  [c]iphersuite name: string
          add ciphersuite to list of negotiated suites
  +dp   --dhparam  [f]ilename: string
          read DH parameters for DH/DSS ciphersuites
pseudo random generator:
  +rs   --seed  [f]ilename: string
          seed random generator with contents of f
  +ws   --write-seed
          write back modified seed (only with --seed)
  +wf   --write-seed-file  [f]ilename: string (only with --seed)
          write modified seed to file f
peer authentication:
  -rc   --require-peer-cert
          verify peer certificate, fail if absent (default)
  -vc   --verify-peer-cert
          verify peer certificate if present
  -ic   --ignore-peer-cert
          don't verify peer certificate
</code></pre>
<h2>NOTES</h2>
<h3>DICOM Conformance</h3>
<p> The <code>storescu</code> application supports the following Storage SOP Classes as an SCU: </p>
<pre>
ComputedRadiographyImageStorage                      1.2.840.10008.5.1.4.1.1.1
DigitalXRayImageStorageForPresentation               1.2.840.10008.5.1.4.1.1.1.1
DigitalXRayImageStorageForProcessing                 1.2.840.10008.5.1.4.1.1.1.1.1
DigitalMammographyXRayImageStorageForPresentation    1.2.840.10008.5.1.4.1.1.1.2
DigitalMammographyXRayImageStorageForProcessing      1.2.840.10008.5.1.4.1.1.1.2.1
DigitalIntraOralXRayImageStorageForPresentation      1.2.840.10008.5.1.4.1.1.1.3
DigitalIntraOralXRayImageStorageForProcessing        1.2.840.10008.5.1.4.1.1.1.3.1
CTImageStorage                                       1.2.840.10008.5.1.4.1.1.2
EnhancedCTImageStorage                               1.2.840.10008.5.1.4.1.1.2.1
UltrasoundMultiframeImageStorage                     1.2.840.10008.5.1.4.1.1.3.1
MRImageStorage                                       1.2.840.10008.5.1.4.1.1.4
EnhancedMRImageStorage                               1.2.840.10008.5.1.4.1.1.4.1
MRSpectroscopyStorage                                1.2.840.10008.5.1.4.1.1.4.2
UltrasoundImageStorage                               1.2.840.10008.5.1.4.1.1.6.1
SecondaryCaptureImageStorage                         1.2.840.10008.5.1.4.1.1.7
MultiframeSingleBitSecondaryCaptureImageStorage      1.2.840.10008.5.1.4.1.1.7.1
MultiframeGrayscaleByteSecondaryCaptureImageStorage  1.2.840.10008.5.1.4.1.1.7.2
MultiframeGrayscaleWordSecondaryCaptureImageStorage  1.2.840.10008.5.1.4.1.1.7.3
MultiframeTrueColorSecondaryCaptureImageStorage      1.2.840.10008.5.1.4.1.1.7.4
TwelveLeadECGWaveformStorage                         1.2.840.10008.5.1.4.1.1.9.1.1
GeneralECGWaveformStorage                            1.2.840.10008.5.1.4.1.1.9.1.2
AmbulatoryECGWaveformStorage                         1.2.840.10008.5.1.4.1.1.9.1.3
HemodynamicWaveformStorage                           1.2.840.10008.5.1.4.1.1.9.2.1
CardiacElectrophysiologyWaveformStorage              1.2.840.10008.5.1.4.1.1.9.3.1
BasicVoiceAudioWaveformStorage                       1.2.840.10008.5.1.4.1.1.9.4.1
GrayscaleSoftcopyPresentationStateStorage            1.2.840.10008.5.1.4.1.1.11.1
ColorSoftcopyPresentationStateStorage                1.2.840.10008.5.1.4.1.1.11.2
PseudoColorSoftcopyPresentationStateStorage          1.2.840.10008.5.1.4.1.1.11.3
BlendingSoftcopyPresentationStateStorage             1.2.840.10008.5.1.4.1.1.11.4
XRayAngiographicImageStorage                         1.2.840.10008.5.1.4.1.1.12.1
EnhancedXAImageStorage                               1.2.840.10008.5.1.4.1.1.12.1.1
XRayRadiofluoroscopicImageStorage                    1.2.840.10008.5.1.4.1.1.12.2
EnhancedXRFImageStorage                              1.2.840.10008.5.1.4.1.1.12.2.1
NuclearMedicineImageStorage                          1.2.840.10008.5.1.4.1.1.20
RawDataStorage                                       1.2.840.10008.5.1.4.1.1.66
SpatialRegistrationStorage                           1.2.840.10008.5.1.4.1.1.66.1
SpatialFiducialsStorage                              1.2.840.10008.5.1.4.1.1.66.2
RealWorldValueMappingStorage                         1.2.840.10008.5.1.4.1.1.67
VLEndoscopicImageStorage                             1.2.840.10008.5.1.4.1.1.77.1.1
VLMicroscopicImageStorage                            1.2.840.10008.5.1.4.1.1.77.1.2
VLSlideCoordinatesMicroscopicImageStorage            1.2.840.10008.5.1.4.1.1.77.1.3
VLPhotographicImageStorage                           1.2.840.10008.5.1.4.1.1.77.1.4
OphthalmicPhotography8BitImageStorage                1.2.840.10008.5.1.4.1.1.77.1.5.1
OphthalmicPhotography16BitImageStorage               1.2.840.10008.5.1.4.1.1.77.1.5.2
StereometricRelationshipStorage                      1.2.840.10008.5.1.4.1.1.77.1.5.3
OphthalmicTomographyImageStorage                     1.2.840.10008.5.1.4.1.1.77.1.5.4
BasicTextSRStorage                                   1.2.840.10008.5.1.4.1.1.88.11
EnhancedSRStorage                                    1.2.840.10008.5.1.4.1.1.88.22
ComprehensiveSRStorage                               1.2.840.10008.5.1.4.1.1.88.33
ProcedureLogStorage                                  1.2.840.10008.5.1.4.1.1.88.40
MammographyCADSRStorage                              1.2.840.10008.5.1.4.1.1.88.50
KeyObjectSelectionDocumentStorage                    1.2.840.10008.5.1.4.1.1.88.59
ChestCADSRStorage                                    1.2.840.10008.5.1.4.1.1.88.65
XRayRadiationDoseSRStorage                           1.2.840.10008.5.1.4.1.1.88.67
ColonCADSRStorage                                    1.2.840.10008.5.1.4.1.1.88.69
EncapsulatedPDFStorage                               1.2.840.10008.5.1.4.1.1.104.1
PositronEmissionTomographyImageStorage               1.2.840.10008.5.1.4.1.1.128
RTImageStorage                                       1.2.840.10008.5.1.4.1.1.481.1
RTDoseStorage                                        1.2.840.10008.5.1.4.1.1.481.2
RTStructureSetStorage                                1.2.840.10008.5.1.4.1.1.481.3
RTBeamsTreatmentRecordStorage                        1.2.840.10008.5.1.4.1.1.481.4
RTPlanStorage                                        1.2.840.10008.5.1.4.1.1.481.5
RTBrachyTreatmentRecordStorage                       1.2.840.10008.5.1.4.1.1.481.6
RTTreatmentSummaryRecordStorage                      1.2.840.10008.5.1.4.1.1.481.7
</pre>
<p> The default behaviour of <code>storescu</code> is to propose two presentation contexts for each supported SOP class (abstract syntax) &#8211; one with the preferred transfer syntax and one with all other uncompressed transfer syntaxes. The default preferred transfer syntax is explicit VR with byte ordering corresponding to the local byte ordering of the machine on which <code>storescu</code> is running. This behaviour can be changed with the <i>&#8211;propose</i>, <i>&#8211;combine</i> and <i>&#8211;required</i> options, see above. Depending on these options, the following transfer syntaxes are supported: </p>
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
<p> The <code>storescu</code> application does not support extended negotiation by default. However, using an appropriate association negotiation profile (see below) the optional support for extended negotiation can be added to particular SOP classes.</p>
<h3>Association Negotiation Profiles and Configuration Files</h3>
<p> <code>storescu</code> supports a flexible mechanism for specifying the DICOM network association negotiation behaviour, based on so-called &#8216;association negotiation profiles&#8217; which may be read from a configuration file. The format and semantics of this configuration file are documented in <i>asconfig.txt</i>.</p>
<h2>LOGGING</h2>
<p> The level of logging output of the various command line tools and underlying libraries can be specified by the user. By default, only errors and warnings are written to the standard error stream. Using option <i>&#8211;verbose</i> also informational messages like processing details are reported. Option <i>&#8211;debug</i> can be used to get more details on the internal activity, e.g. for debugging purposes. Other logging levels can be selected using option <i>&#8211;log-level</i>. In <i>&#8211;quiet</i> mode only fatal errors are reported. In such very severe error events, the application will usually terminate. For more details on the different logging levels, see documentation of module &#8216;oflog&#8217;. </p>
<p> In case the logging output should be written to file (optionally with logfile rotation), to syslog (Unix) or the event log (Windows) option <i>&#8211;log-config</i> can be used. This configuration file also allows for directing only certain messages to a particular output stream and for filtering certain messages based on the module or application where they are generated. An example configuration file is provided in <i>&lt;etcdir&gt;/logger.cfg</i>).</p>
<h2>COMMAND LINE</h2>
<p> All command line tools use the following notation for parameters: square brackets enclose optional values (0-1), three trailing dots indicate that multiple values are allowed (1-n), a combination of both means 0 to n values. </p>
<p> Command line options are distinguished from parameters by a leading &#8216;+&#8217; or &#8216;-&#8216; sign, respectively. Usually, order and position of command line options are arbitrary (i.e. they can appear anywhere). However, if options are mutually exclusive the rightmost appearance is used. This behaviour conforms to the standard evaluation rules of common Unix shells. </p>
<p> In addition, one or more command files can be specified using an &#8216;@&#8217; sign as a prefix to the filename (e.g. <i>@command.txt</i>). Such a command argument is replaced by the content of the corresponding text file (multiple whitespaces are treated as a single separator unless they appear between two quotation marks) prior to any further evaluation. Please note that a command file cannot contain another command file. This simple but effective approach allows to summarize common combinations of options/parameters and avoids longish and confusing command lines (an example is provided in file <i>&lt;datadir&gt;/dumppat.txt</i>).</p>
<h2>ENVIRONMENT</h2>
<p> The <code>storescu</code> utility will attempt to load DICOM data dictionaries specified in the <i>DCMDICTPATH</i> environment variable. By default, i.e. if the <i>DCMDICTPATH</i> environment variable is not set, the file <i>&lt;datadir&gt;/dicom.dic</i> will be loaded unless the dictionary is built into the application (default for Windows). </p>
<p> The default behaviour should be preferred and the <i>DCMDICTPATH</i> environment variable only used when alternative data dictionaries are required. The <i>DCMDICTPATH</i> environment variable has the same format as the Unix shell <i>PATH</i> variable in that a colon (&#8216;:&#8217;) separates entries. On Windows systems, a semicolon (&#8216;;&#8217;) is used as a separator. The data dictionary code will attempt to load each file specified in the <i>DCMDICTPATH</i> environment variable. It is an error if no data dictionary can be loaded.</p>
<h2>FILES</h2>
<p> <i>&lt;docdir&gt;/asconfig.txt</i> &#8211; configuration file documentation<br />
 <i>&lt;etcdir&gt;/storescu.cfg</i> &#8211; example association negotiation profile</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-storescp/">storescp</a></code>(1)</p>
<h2>COPYRIGHT</h2>
<p> Copyright (C) 1996-2010 by OFFIS e.V., Escherweg 2, 26121 Oldenburg, Germany. </p>
<h2>Index</h2>
