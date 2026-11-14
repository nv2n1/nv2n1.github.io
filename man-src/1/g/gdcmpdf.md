---
title: "gdcmpdf(1)"
name: "gdcmpdf"
section: "1"
letter: "g"
url: "/docs/linux/man/1-gdcmpdf/"
description: "gdcmpdf – .TH \"gdcmpdf\" 1 \"Fri Oct 29 2010\" \"Version 2.0.16\" \"GDCM\""
---

<h2 class="name">NAME</h2>
<p> gdcmpdf &#8211; .TH &quot;gdcmpdf&quot; 1 &quot;Fri Oct 29 2010&quot; &quot;Version 2.0.16&quot; &quot;GDCM&quot; </p>
<h2 class="name">NAME</h2>
<p> gdcmpdf &#8211; .SH &quot;SYNOPSIS&quot; </p>
<pre>
gdcmpdf [options] file-in file-out
</pre>
<h2>DESCRIPTION</h2>
<p> The <code>gdcmpdf</code> tool convert a PDF file (any PDF version) into an encapsulated PDF/DICOM file. By default it will try to read the PDF meta information stored in the PDF and convert this information to some specific DICOM fields (see below). However it may fails (eg. wrong password on encrypted PDF file) in which case empty value are used.</p>
<h2>PARAMETERS</h2>
<pre>
file-in   PDF input filename
file-out  DICOM output filename
</pre>
<h2>OPTIONS</h2>
<h3>general options</h3>
<pre><code>
- h-- help
        print this help text and exit -
    v-- version
        print version information and exit -
    V-- verbose
        verbose
        mode(warning + error)
            .-
    W-- warning
    warning mode,
    print warning information
        - E-- error
        error mode,
    print error information
        - D-- debug
        debug mode,
    print debug information
</code></pre>
<h2>Usage Example</h2>
<pre>
 $ wget <a rel="nofollow" href="http://gdcm.sourceforge.net/gdcm.pdf">http://gdcm.sourceforge.net/gdcm.pdf</a>
 $ gdcmpdf gdcm.pdf gdcm.dcm
</pre>
<p> To re-extract the encapsulated pdf file: </p>
<pre>
 $ gdcmraw -i gdcm.dcm -t 42,11 -o gdcm.dcm.pdf
 $ diff gdcm.pdf gdcm.dcm.pdf
</pre>
<h2>PDF Info Mapping</h2>
<p> Here is how the PDF info is mapped to DICOM information (typical pdfinfo output): </p>
<pre>
Title:          GDCM Reference Manual
Subject:        Grassroots DICOM API reference
Keywords:       GDCM,DICOM,JPEG,Lossless JPEG,JPEG-LS,J2K,JPEG 2000,RLE
Author:         Mathieu Malaterre and co.
Creator:        LaTeX with hyperref package
Producer:       pdfeTeX-1.21a
CreationDate:   Tue Apr 28 15:34:26 2009
Tagged:         no
Pages:          1188
Encrypted:      no
Page size:      612 x 792 pts (letter)
File size:      13756841 bytes
Optimized:      yes
PDF version:    1.4
</pre>
<p> Converted to DICOM this leads to: </p>
<pre><code>
#Dicom - Data - Set
#Used TransferSyntax : Little Endian Explicit
(0008,0005) CS [ISO_IR 100]                             #  10, 1 SpecificCharacterSet
(0008,0012) DA [20090428]                               #   8, 1 InstanceCreationDate
(0008,0013) TM [182550.302631]                          #  14, 1 InstanceCreationTime
(0008,0016) UI =EncapsulatedPDFStorage                  #  30, 1 SOPClassUID
(0008,0018) UI [1.2.826.0.1.3680043.2.1143.776842935192792959289022034349197114] #  64, 1 SOPInstanceUID
(0008,0020) DA [20090428]                               #   8, 1 StudyDate
(0008,0023) DA [20090428]                               #   8, 1 ContentDate
(0008,002a) DT [20090428153437.000000]                  #  22, 1 AcquisitionDateTime
(0008,0030) TM [182550.302160]                          #  14, 1 StudyTime
(0008,0033) TM [153426.000000]                          #  14, 1 ContentTime
(0008,0050) SH (no value available)                     #   0, 0 AccessionNumber
(0008,0060) CS [OT]                                     #   2, 1 Modality
(0008,0064) CS [WSD]                                    #   4, 1 ConversionType
(0008,0070) LO [LaTeX with hyperref package]            #  28, 1 Manufacturer
(0008,0090) PN (no value available)                     #   0, 0 ReferringPhysiciansName
(0010,0010) PN [Mathieu Malaterre and co.]              #  26, 1 PatientsName
(0010,0020) LO (no value available)                     #   0, 0 PatientID
(0010,0030) DA (no value available)                     #   0, 0 PatientsBirthDate
(0010,0040) CS (no value available)                     #   0, 0 PatientsSex
(0018,1020) LO [pdfeTeX-1.21a]                          #  14, 1 SoftwareVersions
(0020,000d) UI [1.2.826.0.1.3680043.2.1143.1868121832223417351654232480755123133] #  64, 1 StudyInstanceUID
(0020,000e) UI [1.2.826.0.1.3680043.2.1143.1330099150825746617507846107663964311] #  64, 1 SeriesInstanceUID
(0020,0010) SH (no value available)                     #   0, 0 StudyID
(0020,0011) IS [1]                                      #   2, 1 SeriesNumber
(0020,0013) IS [1]                                      #   2, 1 InstanceNumber
(0028,0301) CS [YES]                                    #   4, 1 BurnedInAnnotation
(0040,a043) SQ (Sequence with explicit length #=0)      #   0, 1 ConceptNameCodeSequence
(fffe,e0dd) na (SequenceDelimitationItem for re-encod.) #   0, 0 SequenceDelimitationItem
(0042,0010) ST [GDCM Reference Manual]                  #  22, 1 DocumentTitle
(0042,0011) OB 25\50\44\46\2d\31\2e\34
